#! /bin/sh

SCRIPT_RELATIVE_DIR=$(dirname "${BASH_SOURCE[0]}")
cd $SCRIPT_RELATIVE_DIR
pwd

echo "RUNNING REALTIME PYTHON CODE"
python3 realtime.py