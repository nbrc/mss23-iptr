#! /bin/sh

SCRIPT_RELATIVE_DIR=$(dirname "${BASH_SOURCE[0]}")
cd $SCRIPT_RELATIVE_DIR
pwd
cd ../python-scripts

echo "RUN REALTIME PYTHON CODE"
python3 realtime.py