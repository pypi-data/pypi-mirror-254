"""This module provides the onetable_py CLI."""

import typer
import jpype
import jpype.imports
import jpype.types
from subprocess import Popen, PIPE, CalledProcessError
from urllib import request
from typing_extensions import Annotated
from rich import print
from pathlib import Path
from typing import Optional

from onetable_py import __app_name__, __version__

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


def _exec(cmd):
    with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            print(line, end="")  # process line here

    if p.returncode != 0:
        raise CalledProcessError(p.returncode, p.args)


@app.command()
def setup():
    # paths
    path = Path(__file__).resolve().parent / "jars"
    path.mkdir(exist_ok=True)

    # set to java 11
    _exec(["jenv", "local", "11.0"])

    # vars
    jars = {
        "iceberg-spark-runtime-3.4_2.12-1.4.2.jar": "https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.4_2.12/1.4.2/iceberg-spark-runtime-3.4_2.12-1.4.2.jar",
        "iceberg-aws-bundle-1.4.2.jar": "https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/1.4.2/iceberg-aws-bundle-1.4.2.jar",
        "utilities-0.1.0-SNAPSHOT-bundled.jar": "https://d1bjpw1aruo86w.cloudfront.net/05eb631ce7f32184ac864b6f1cc81db8/utilities-0.1.0-SNAPSHOT-bundled.jar",
    }

    # download jars
    for jar, url in jars.items():
        if not (path / jar).exists():
            print(f"Downloading {jar} ...")
            request.urlretrieve(
                url,
                path / jar,
            )


@app.command()
def sync(
    config: Annotated[str, typer.Option()],
    catalog: Annotated[str, typer.Option()] = None,
):
    # init
    setup()

    # Launch the JVM
    path = Path(__file__).resolve().parent
    jpype.startJVM(classpath=path / "jars/*")
    run_sync = jpype.JPackage("io").onetable.utilities.RunSync.main

    # call java class
    if catalog:
        run_sync(["--datasetConfig", config, "--icebergCatalogConfig", catalog])

    else:
        run_sync(["--datasetConfig", config])

    # shutdown
    jpype.shutdownJVM()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
