---
title: How to contribute
---

# Contributing to Docop

File an issue, submit a PR, the usual. In particular, share your tasks if you can!

## How to make your tasks available for other users

To create and publish reusable collections of tasks available to other users, create a Python package and associate the tasks with `docop.tasks` or `docop.tasks.restricted` entry point. If the task code can not be freely used for commercial purposes because of for example AGPL license being used by some library that the task uses, use the restricted entry point.

see the source code of the [docop-tasks](https://pypi.org/project/docop-tasks) and [docop-tasks-restricted](https://pypi.org/project/docop-tasks-restricted) packages for details.

If you think your task should be added to either of those packages, open an issue and an associated pull request for that.

Thank you!
