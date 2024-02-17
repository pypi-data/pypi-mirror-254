#! /bin/sh

# fail on first error
set -e

# protect cwd
pushd . &> /dev/null

ScriptDir="$( cd "$( dirname "$0" )" && pwd )"

# script is at proj_root/
cd "$ScriptDir"
servName=$(basename "$ScriptDir")
poetry run python src/"$servName"_cli.py "$@"

popd &> /dev/null
