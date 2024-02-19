---
title: Configuration settings
---
# Docop configuration

Configuration is given in the `config.yaml` file. Alternatively, another file may be given by using the `docop --config` option.

## Directories

The directories section specifies where docop will look up for pipelines (specified as `.yaml` files), Python task modules (`.py`) and documents that have been created by tasks.

Directories are relative to the current directory where docop is being run from.

``` yaml
--8<-- "./documentation/docs/example-config.yaml:dirs"
```

## Sources to fetch

``` yaml
--8<-- "./documentation/docs/example-config.yaml:sources"
```

## Export targets

Beyond mandating a `targets` section containing names of export targets, docop does not have any conventions for specifying target information. Any extra content can be given, including data used for authentication.

``` yaml
--8<-- "./documentation/docs/example-config.yaml:targets"
```

## Authentication

Often, when retrieving, processing or exporting content, some third party system needs to be authenticated with.

Authentication accounts with arbitrary information can be added in configuration files in the `accounts` section:

``` yaml
--8<-- "./documentation/docs/example-config.yaml:accounts"
```

The account to use can then be set for each source or target; see the export targets setting example above. For a general processing task, account can be given using the `--account` command-line option. The option can also be used to override the specified account.

