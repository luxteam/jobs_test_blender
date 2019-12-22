#!/bin/bash
RENDER_DEVICE=$1
FILE_FILTER=$2
TESTS_FILTER="$3"

python -m pip install -r ../jobs_launcher/install/requirements.txt

python ../jobs_launcher/executeTests.py --test_filter $TESTS_FILTER --file_filter $FILE_FILTER --tests_root ../jobs --work_root ../Work/Results --work_dir Blender28 --cmd_variables Tool "blender" RenderDevice $RENDER_DEVICE ResPath "$CIS_TOOLS/../TestResources/Blender2.8Assets" PassLimit 10 rx 0 ry 0
