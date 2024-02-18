# package python package
cd "$ROOT_PATH"
flit build

# upload python package
cd "$ROOT_PATH"
flit publish --repository pypi
