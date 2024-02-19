import sys
import os
from pathlib import Path
from importlib.metadata import entry_points
from importlib.util import find_spec
from importlib.resources import files
from copy import deepcopy
from collections import ChainMap
from click import argument, group, option, pass_context, echo, UNPROCESSED
from yamlstore import Document, Collection
from .util import task_from_module, get_docs, get_ep_docstring, get_module_docstring
from rich.console import Console
from rich import print
from rich.panel import Panel

console = Console()

@group()
@option('--config', default="config.yaml", help="Configuration file to use.", type=Path)
@pass_context
def docop(ctx, config):
    "Document pipeline processor."

    if config.exists():
        cfg = Document(config, title="default")

        # Merge any extra configs and make sure we have all the sections
        extra_conf_paths = tuple(Path(cfg["dirs"]["configs"]).glob("*.yaml"))
        extra_configs = [Document(cfg_path) for cfg_path in extra_conf_paths]
        for section in ("sources", "targets", "content", "accounts"):
            extras = [extra[section] for extra in extra_configs if section in extra]
            cfg[section] = ChainMap(cfg.get(section, {}), *extras)
    else:
        if ctx.invoked_subcommand not in ("init", "tasks") and sys.argv[-1] != "--help":
            print(f"No configuration file found so don't know where to find {ctx.invoked_subcommand}.")
            sys.exit()
        cfg = None

    ctx.obj = cfg



@docop.command()
@argument("directory", required=True, type=Path)
@pass_context
def init(ctx, directory):
    "Initialize a docop project."
    try:
        os.makedirs(directory, exist_ok=False)
    except FileExistsError:
        print(f"Project directory '{directory}' already exists. Not doing anything.")
        return
    else:
        os.mkdir(directory / "content")
        os.mkdir(directory / "configs")
        os.mkdir(directory / "pipes")
        os.mkdir(directory / "tasks")
        config_example = files(__package__).joinpath('config.yaml.in').read_text()
        (directory / "config.yaml").write_text(config_example)
    print(f"Created project directory structure at '{directory}' and added an example configuration file.", end=' ')
    print(f"You can now do 'cd {directory}' and start using docop.")

@docop.command()
@pass_context
def pipes(ctx):
    "List available task pipelines."

    pipes = Collection(directory=Path(ctx.obj["dirs"]["pipes"]), readonly=True)
    for pipe in pipes.values():
        echo(f"{pipe['title']}: {pipe['description']} ({' → '.join(pipe['tasks'])})")


@docop.command()
@pass_context
def tasks(ctx):
    "List available tasks."

    eps = entry_points()
    packaged_tasks = eps.select(group="docop.tasks")
    restricted_tasks = eps.select(group="docop.tasks.restricted")
    if ctx.obj:
        module_tasks = tuple(Path(ctx.obj["dirs"]["tasks"]).glob("*.py"))
    else:
        module_tasks = None

    if packaged_tasks:
        print("\n[bold]Packaged tasks:[/]")
        for task_ref in packaged_tasks:
            doc_str, _ = get_ep_docstring(task_ref)
            print(f"{task_ref.name}: {doc_str}")

    if restricted_tasks:
        print("\n[bold]Packaged restricted-license tasks:[/]")
        for task_ref in restricted_tasks:
            doc_str, _ = get_ep_docstring(task_ref)
            print(f"{task_ref.name}: {doc_str}")

    if module_tasks:
        print("\n[bold]Your local custom tasks:[/]")
        for task_path in module_tasks:
            name = task_path.name[:-3]
            doc_str, _ = get_module_docstring(task_path)
            print(f"{name}: {doc_str}")
    if not packaged_tasks and not restricted_tasks and not module_tasks:
        echo("No tasks found.")


@docop.command()
@argument("task_or_pipe", metavar="TASKNAME or PIPENAME", nargs=1, required=True, type=str)
@option('--source', '-s', multiple=True, help='Sources that will be fetched and stored as documents.')
@option('--content', '-c', type=Path, multiple=True, help='Stored documents to process.')
@option('--target', '-t', multiple=True, help='Targets to export document content to')
@option('--account', '-a', multiple=False, help='Account to use (source or target)')
@argument('extras', nargs=-1, type=UNPROCESSED)
@pass_context
def run(ctx, task_or_pipe, source, content, target, account, extras):
    "Run a task or pipeline."


    extras = {} if not extras else dict((e.split('=')) for e in extras)

    #
    # MAKE SURE WE HAVE ONE AND ONLY ONE UNAMBIGUOUSLY REFERENCED TASK OR PIPE
    #
    if not task_or_pipe:
        echo("No task or pipe given. Not doing anything.")
        return

    module_tasks = [Path(tf).stem for tf in Path(ctx.obj["dirs"]["tasks"]).glob("*.py")]
    eps = entry_points()
    task_eps = {ep.name:ep for ep in eps.select(group="docop.tasks") + eps.select(group="docop.tasks.restricted")}
    packaged_tasks = [ep.name for ep in eps.select(group="docop.tasks")]
    restricted_tasks = [ep.name for ep in eps.select(group="docop.tasks.restricted")]
    tasknames = module_tasks + packaged_tasks + restricted_tasks 
    pipenames = [Path(pf).stem for pf in Path(ctx.obj["dirs"]["pipes"]).glob("*.yaml")]

    if task_or_pipe in tasknames and task_or_pipe in pipenames:
        echo(f"There is both a task and and a pipe named '{task_or_pipe}'. Please rename either.")
        return

    if task_or_pipe not in tasknames + pipenames:
        echo(f"No task or pipe named '{task_or_pipe}' found.")
        return

    #
    # CONSTRUCT THE PIPELINE
    #
    if task_or_pipe in tasknames:
        pipe = Document(title=task_or_pipe, description=f"run a [bold]{task_or_pipe}[/] task", readonly=True)
        pipe.data["tasks"] = (task_or_pipe,)
    else:
        pipe_path = Path(ctx.obj["dirs"]["pipes"]) / f"{task_or_pipe}.yaml"
        pipe = Document(pipe_path, readonly=True)

    pipesize = len(pipe["tasks"])

    print("\n")
    console.rule(f"Building a pipe to {pipe['description']}")

    #
    # SET UP SOURCE RESOURCES TO RETRIEVE
    #
    if source:
        try:
            source_queue = [(srcname, ctx.obj["sources"][srcname]) for srcname in source]
        except KeyError as exc:
            print(f"⚠️  [bold red] source {exc} not found")
            return
    else:
        source_queue = list(pipe.get("sources", {}).items())

    if source_queue:
        print(" • will fetch resources from %i sources: %s" % (len(source_queue), ", ".join((n[0] for n in source_queue))))

    #
    # SET UP LOCALLY STORED CONTENT TO PROCESS
    #
    content_queue = []
    if content:
        content_root = Path(ctx.obj["dirs"]["content"])
        partial_collections = {}
        for content_path in content:
            if Path(content_path).exists():
                path = Path(content_path)
            else:
                path = content_root / content_path
            if path.is_dir():
                content_queue.append((path.name, Collection(path)))
            elif path.is_file():
                if path.parent not in partial_collections:
                    partial_collections[path.parent] = Collection(path.parent, autoload=False)
                partial_collections[path.parent] += Document(path)
            else:
                echo(f"Content path '{path}' not found.")
                return
        content_queue.extend(tuple(partial_collections.items()))

    if content_queue:
        summary = ", ".join((name + f" ({len(c)} documents)" for name, c in content_queue))
        print(" • will process %i collections: %s" % (len(content_queue), summary))

    #
    # SET UP TARGETS TO EXPORT TO
    #
    if target:
        target_queue =[(tgtname, ctx.obj["targets"][tgtname]) for tgtname in target]
    else:
        target_queue = list(pipe.get("targets", {}).items())

    if target_queue:
        print(" • will export content to %i targets: %s" % (len(target_queue), ", ".join((n[0] for n in target_queue))), end='')

    #
    # SET UP ACCOUNT TO USE IF GIVEN
    #
    if account:
        try:
            account = ctx.obj["accounts"][account]
        except KeyError as exc:
            print(f"⚠️  [bold red]account {exc} not found")
            return

    # SET UP GLOBAL CONFIGURATION CONTEXT FOR TASK EXECUTION
    #

    config_ctx = {
        "config": ctx.obj,
        "extras": extras,
        "sources": deepcopy(source_queue),
        "targets": deepcopy(target_queue),
        "content": deepcopy(content_queue),
        "pipeconfig": pipe
    }

    #
    # RUN PIPELINE. FIRST TASK FETCHES SOURCES, NEXT ONES PROCESS AND LAST ONE EXPORTS
    #

    tasklist = ' → '.join((task for task in pipe["tasks"]))
    print(f"\n • will run {len(pipe['tasks'])} tasks: {tasklist}")

    pipe_ctx = {}

    for counter, task in enumerate(pipe["tasks"], start=1):
        #
        # CONSTRUCT TASK EXECUTABLE
        #
        if task in module_tasks:
            task_path = Path(ctx.obj["dirs"]["tasks"]) / f"{task}.py"
            try:
                code = task_from_module(task_path)
            except SyntaxError as exc:
                print(f" ⚠️  [bold red]task has error[/]:", exc.msg)
                return
            docstr, _ = get_module_docstring(task_path)
        else: # task in (packaged_tasks + restricted_tasks)
            spec = find_spec(task_eps[task].module)
            code = spec.loader.get_code(task_eps[task].module)
            docstr, _ = get_ep_docstring(task_eps[task])

        print("\n", Panel(f"⚙️  {counter}. {task} → {docstr}"))

        #
        # SET UP BASE EXECUTION CONTEXT FOR TASK
        #
        exec_ctx = {
            "account": account,
            "pipedata": pipe_ctx,
        }

        #
        # HANDLE CASE WHEN NO SOURCES OR CONTENT OR TARGETS ARE PROVIDED
        #
        if not (source_queue or content_queue or target_queue):
            try:
                exec(code, config_ctx | exec_ctx)
            except Exception as e:
                print("⚠️  [bold red]Task run failed: %s[/]" % e)
            else:
                pipe_ctx = exec_ctx["pipedata"]

        #
        #  PIPELINE SUBLOOP 1: PROCESS EACH SOURCE
        #
        if source_queue:
            while source_queue:
                sourcename, source = source_queue.pop(0)

                print(f"Retrieving content for '{sourcename}'...")
                collection = Collection(name=sourcename, directory=Path(ctx.obj["dirs"]["content"]) / sourcename, autosync=True)
                retrieval_ctx = {
                    "source": source,
                    "collection": collection
                }
                if not account:
                    try:
                        retrieval_ctx["account"] = ctx.obj["accounts"][source["account"]]
                    except KeyError as exc:
                        pass

                for ref in source["resources"]:
                    retrieval_ctx["reference"] = ref
                    doc = Document()
                    doc["reference"] = ref
                    collection._modified = False
                    doc._modified = False
                    retrieval_ctx["document"] = doc
                    retrieval_ctx.update({
                        "reference": ref,
                        "document": doc,
                        "pipedata": pipe_ctx
                    })
                    try:
                        exec(code, config_ctx | exec_ctx | retrieval_ctx)
                    except Exception as e:
                        print("⚠️  [bold red]Task run failed: %s[/]" % e)
                        return
                    else:
                        pipe_ctx = retrieval_ctx["pipedata"]
                        # If the task added documents, we're done with this source.
                        if retrieval_ctx['collection'].modified:
                            break
                        # Otherwise, we'll store the doc that the task modified.
                        if retrieval_ctx["document"].modified:
                            print(f"↳ fetched \'{doc['title']}\' ✅")
                            collection += retrieval_ctx["document"]
                            print(f"↳ result at {doc._path} ✅")

                content_queue.append((sourcename, collection))
            # move to the next task
            continue

        #
        # PIPELINE SUBLOOP 2: PROCESS CONTENT COLLECTIONS OR DOCUMENTS
        #
        # If there is a target queue waiting, let the last task of the pipe do exporting
        if not source_queue and not (target_queue and counter == pipesize):
            for name, collection in content_queue:
                print(f"Processing '{name}' content collection ...")
                proc_ctx = {
                    "collection": collection,
                    "pipedata": pipe_ctx
                }

                for count, (doc_name, doc) in enumerate(collection.items(), start=1):
                    doc._modified = False
                    proc_ctx["document"] = doc
                    try:
                        exec(code, config_ctx | exec_ctx | proc_ctx)
                    except Exception as e:
                        print(f"⚠️  [bold red]failed to process content[/] '{doc}': %s" % e)
                    else:
                        pipe_ctx = proc_ctx["pipedata"]
                        if proc_ctx["document"].modified:
                            proc_ctx["document"].sync()
                            print(f"↳ '{doc['title']}' ✅")
            # move to the next task
            continue

        #
        # PIPELINE SUBLOOP 3: PROCESS EACH TARGET
        #
        if target_queue:
            for targetname, target in target_queue:
                print(f"Exporting to '{targetname}' ...")
                for name, collection in content_queue:
                    print(f" ↳ Processing '{name}' content collection")
                    export_ctx = {
                        "collection": collection,
                        "target": target,
                        "pipedata": pipe_ctx
                    }
                    if not account:
                        try:
                            export_ctx["account"] = ctx.obj["accounts"][target["account"]]
                        except KeyError as exc:
                            pass
                    try:
                        exec(code, config_ctx | exec_ctx | export_ctx)
                    except Exception as exc:
                        print("⚠️  [bold red]task failed[/] %s" % exc)
                        return
                    else:
                        pipe_ctx = export_ctx["pipedata"]


@docop.command()
@pass_context
def content(ctx):
    "List the stored collections of YAML documents."

    docs, batches = get_docs((Path(ctx.obj["dirs"]["content"]),))
    if not (docs or batches):
        echo("No documents found.")
        return

    if batches:
        for batch in batches:
            echo(f"{batch.name} ({len(batch)} docs)")

    if docs:
        for doc in docs:
            echo(f"{doc['title']} ({doc['description']})")


@docop.command()
@pass_context
def configs(ctx):
    "List available configurations."

    configs = Collection(Path(ctx.obj["dirs"]["configs"]), readonly=True)
    for config in configs.values():
        echo(f"{config['title']} ({config['description']})")
