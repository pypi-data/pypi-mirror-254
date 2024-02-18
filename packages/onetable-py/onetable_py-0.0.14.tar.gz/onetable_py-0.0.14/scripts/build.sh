# clean up
export ROOT_PATH=$(git rev-parse --show-toplevel)
cd "$ROOT_PATH"
rm -rf onetable
rm -r dist
rm -r onetable_py/jars

# install requirements
pip install --upgrade pip

# clone sources
git clone --branch main --depth 1 https://github.com/onetable-io/onetable.git

# prepare paths
cd onetable
jenv local 11.0
export JAVA_HOME=$(jenv javahome)

# check java version
if type -p java; then
    echo found java executable in PATH
    _java=java
elif [[ -n "$JAVA_HOME" ]] && [[ -x "$JAVA_HOME/bin/java" ]];  then
    echo found java executable in JAVA_HOME     
    _java="$JAVA_HOME/bin/java"
else
    echo "no java"
fi

# if java11 build onetable jar
if [[ "$_java" ]]; then
    version=$(java -version 2>&1 | awk -F '"' '/version/ {print $2}' | awk -F '.' '{sub("^$", "0", $2); print $1$2}')
    echo version "$version"
    if [[ "$version" == "110" ]]; then
        mvn package -DskipTests=true
    else         
        echo java version is not 11.0. Need to use java 11.0 for building onetable.
    fi
fi

# copy jar to jars folder
mkdir -p "$ROOT_PATH/onetable_py/jars"
cp "$ROOT_PATH/onetable/utilities/target/utilities-0.1.0-SNAPSHOT-bundled.jar" "$ROOT_PATH/onetable_py/jars/"

# download additional jars
cd "$ROOT_PATH/onetable_py/jars"
wget https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.4_2.12/1.4.2/iceberg-spark-runtime-3.4_2.12-1.4.2.jar
wget https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/1.4.2/iceberg-aws-bundle-1.4.2.jar

# package python package
cd "$ROOT_PATH"
flit build --no-use-vcs
