---
title: Creating and running pipelines
---

# Docop pipelines explained

Pipelines are defined as YAML formatted files. They specify an ordered sequence of tasks to run.

## How to review available pipelines

Use the `pipes` command to list them:

```bash
docop pipes
```

Presuming the earlier 'mypipe' pipeline existed, the command would output:

```
mypipe: My first full pipe (retrieve → process1 → process2 → export)
```

## How to create a task pipeline

Create a YAML file with a descriptive name, add a comment line to describe it and list the tasks in an ordered sequence:

```yaml  title="mypipe.yaml"
--8<-- "./documentation/docs/example-pipe.yaml"
```

## How to run a pipeline

Just use the `run` command. Docproc will automatically find the given pipeline and run it. No need to give a path to the pipeline definition file or include the `.yaml` suffix.

Using the `--help` option gives more details:

```
--8<-- "./documentation/docs/runhelp.txt"
```

Docproc will provide ample status information when it runs the pipeline.


## How Docop runs task pipelines

The following diagram describes how docop loops over sources, content and targets and runs a pipe of tasks to fetch, process and export content.

``` mermaid
graph LR
  S((Start)) --> QS{Sources\nfetched?};
  QS -- No --> RT(⚡ Run 1st task\nto fetch);
  RT --> QS;
  QS -- Yes --> QL{Next\ntask\nlast?};
  QL -- No --> RP(⚡ Run next task\nto process);
  RP --> QL;
  QL --  Yes --> RE(⚡ Run last task\nto export);
  RE --> QE{Docs\nexported?};
  QE -- Yes --> E((End));
  QE -- No --> RE;
```

To recap:

1. When a task runs, it is provided a set of [execution context variables](tasks.md#data-available-for-tasks)

1. The first task in a pipe should check the sources and fetch them

1. The next tasks should process the fetched content

1. The last task should export content to targets

1. Each task can process one or more source, collection, document or target per run
