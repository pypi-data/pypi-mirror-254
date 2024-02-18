from urllib import request
from pathlib import Path
from setuptools import setup
from setuptools.command.install import install


class CustomInstall(install):

    def run(self):
        install.run(self)

        # vars
        jars = {
            "utilities-0.1.0-beta1-bundled.jar": "https://d1bjpw1aruo86w.cloudfront.net/05eb631ce7f32184ac864b6f1cc81db8/utilities-0.1.0-beta1-bundled.jar",
            "iceberg-spark-runtime-3.4_2.12-1.4.2.jar": "https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.4_2.12/1.4.2/iceberg-spark-runtime-3.4_2.12-1.4.2.jar",
            "iceberg-aws-bundle-1.4.2.jar": "https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/1.4.2/iceberg-aws-bundle-1.4.2.jar",
        }

        # paths
        path = Path(__file__).resolve().parent / "jars"
        path.mkdir(exist_ok=True)

        # download jars
        for jar, url in jars.items():
            if not (path / jar).exists():
                request.urlretrieve(
                    url,
                    path / jar,
                )


setup(cmdclass={"install": CustomInstall})
