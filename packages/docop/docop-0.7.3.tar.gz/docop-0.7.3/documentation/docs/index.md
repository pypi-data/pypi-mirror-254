---
title: Home
---
# Welcome to Docop

Docproc provides some opinionated means to very easily build simple document processing pipelines for importing, processing and exporting textual content items, or in general anything possibly having a textual representation.

It has been used to for example fetching HTML pages, converting them to plaintext and exporting the results to an AI knowledge base.

## Introduction

Some basic concepts:

- sources specify the content you will retrieve
- content speficies already retrieved content documents to process
- targets specify destinations to export the results to

Practicalities:

- [configuration](config.md) is given in a YAML file
- [tasks](tasks.md) are Python modules
- [pipelines](pipes.md) are defined as YAML files
- file names are used as names for tasks, docs and pipelines
- first comment lines are used as the description for tasks and pipelines
- retrieved content is stored as YAML [documents](documents.md), with arbitrary metadata addable by tasks

## Getting started

- do a pip install
- set up a few directories for tasks, docs and  and pipes
- copy config.yaml.in to config.yaml and specify the directories there
- read the docs on how to [configure docop](config.md), use the [command-line tool](cmdline.md), create [tasks](tasks.md) and [pipes](pipes.md) etc.

