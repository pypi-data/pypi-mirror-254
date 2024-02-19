---
title: Understanding documents
---

# What are Docop collections of documents

Docproc provides an automatic data persistence mechanism so that task user or creator does not need to deal with it.

- When retrieving resources from some source, a collection and a document are instantiated and put into the task namespace as variables
- When processing or exporting content, directories containing existing YAML documents are loaded into document collections and likewise put into the task namespace
- When a task has finished running, any modified documents are automatically persisted as YAML files

For more details on `collection`, `document` and other task variables, see the documentation on [available task data](tasks.md#what-data-is-passed-to-a-task).

## Reviewing stored documents and collections

Use the `docs` command to see them:

```bash
docop docs
```

## Technical details

Under the hood, Docop uses the `Document` and `Collection` classes from the [yamlstore](https://pypi.org/project/yamlstore/) package. They provide a thin wrapper to facilitate data persistence in directories of YAML-formatted document files.