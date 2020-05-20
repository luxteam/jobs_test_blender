#!/bin/bash
RENDER_DEVICE=$1
FILE_FILTER=$2
TESTS_FILTER="$3"
RX=${4:-0}
RY=${5:-0}
SPU=${6:-25}
ITER=${7:-50}
THRESHOLD=${8:-0.05}
ENGINE=${9:-FULL}

shift
shift
shift
shift
shift
shift
shift
shift

export RBS_BUILD_ID=$1
export RBS_JOB_ID=$2
export RBS_URL=$3
export RBS_ENV_LABEL=$4
export IMAGE_SERVICE_URL=$5
export RBS_USE=$6

python -m pip install -r ../jobs_launcher/install/requirements.txt

python ../jobs_launcher/executeTests.py --test_filter $TESTS_FILTER --file_filter $FILE_FILTER --tests_root ../jobs --work_root ../Work/Results --work_dir Blender28 --cmd_variables Tool "blender" RenderDevice $RENDER_DEVICE ResPath "$CIS_TOOLS/../TestResources/Blender2.8Assets" PassLimit $ITER rx $RX ry $RY SPU $SPU threshold $THRESHOLD engine $ENGINE
