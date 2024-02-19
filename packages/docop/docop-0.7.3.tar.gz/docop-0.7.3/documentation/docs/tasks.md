---
title: Creating and running tasks
---

# Docop tasks explained

Tasks are Python modules that docop can run for you to fetch some content, process or export it. You may store them as you like in your file system, or use prepackaged [docop-tasks](https://pypi.org/project/docop-tasks) or [docop-tasks-restricted](https://pypi.org/project/docop-tasks-restricted) task packages from PyPI or elsewhere.

## How to review available tasks

Use the `tasks` command. Docproc will search your Python installation for any packaged docop tasks or local task modules pointed to in your config file `tasks` setting.

```bash
docop tasks
```

## How to run a task

Use the `run` command. Docproc will automatically find the given task and run it. No need to give a path to the file or include the `.py` suffix.

Using the `--help` option gives more details:

```
--8<-- "./documentation/docs/runhelp.txt"
```

## How to create new tasks

Create a Python module suffixed `.py` and put it into your `tasks` directory.

 No function definitions, classes or such are required. When a task is called, the main config and relevant data for the task are put into the task namespace. A task can choose to process one source, document or export target at a time, or more, or all at once.

## Data available for tasks

For each task invocation, execution context variables are injected into the Python task module namespace.

#### Configuration context

The following static configuration variables are always available for every task invocation.

`config`

:   your docop configuration as a dictionary keyed by config section names

`extras`

:   any extra commmand-line parameters, as a parameter name-value dictionary

`account`

:   if given by the `--account` cmdline param, a dictionary of account data

`sources`

:   a sequence of resource sources discovered in configuration files

`content`

:   all the local content discovered in local file system

`targets`

:   all the export targets discovered in configuration files

#### Retrieval context

As Docproc loops over sources, it injects each source and resource reference and an associated collection and document to the invoked task namespace.

`source`

:   the source to be processed by the task

`collection`

:   a Collection for storing retrieved source resources; useful if the application needs to implement custom looping

`reference`

:   the reference such as URL of the resource to be retrieved

`document`

:   a Document for storing the retrieved resource


#### Content processing context

As Docproc loops over the given content (directories), it reads and parses all YAML files in the directories into collections and documents and injects them to the task namespace.

`collection`

:   a Collection of Documents to be processed by tasks

`document`

:   a Document to be processed by tasks

#### Export task context

`target`

:   current target being processed


## Task processing rules

There are some rules of thumb to keep in mind when writing tasks.

- after the task `document` is modified, Docproc automatically adds it to the task `collection` and persists the changes on disk

- if the `document` is not modified, it is not added nor persisted

- if the task, instead of modifying its `document`, instantiates one or more Document and adds them to the `collection`, Docproc moves to the next (source and) collection after the task has finished running
