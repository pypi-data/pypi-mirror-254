#! /bin/sh

# fail on first error
set -e

# protect cwd
pushd . &> /dev/null

ScriptDir="$( cd "$( dirname "$0" )" && pwd )"
ServRootDir=$(dirname "$ScriptDir")
cd "$ServRootDir"
/usr/local/bin/poetry run python tool/tool.py "$@"

popd &> /dev/null
