# `onetable_py`
This package wraps the java package [onetable](https://onetable.dev) into a python cli/library along with it's dependencies. This provides the onetable jar in an easy consumeable format for various CI/CD or workflow management platforms such as Apache Airflow.

**Usage**:

```console
$ onetable_py [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-v, --version`: Show the application's version and exit.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `init`
* `sync`

## `onetable_py init`
Downloads the required jars for onetable

**Usage**:

```console
$ onetable_py init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `onetable_py sync`
Runs "io.onetable.utilities.RunSync"

**Usage**:

```console
$ onetable_py sync [OPTIONS]
```

**Options**:

* `--config TEXT`: [required]
* `--catalog TEXT`
* `--help`: Show this message and exit.

## Requirements

* Java 11.0
* jenv 0.5.6
