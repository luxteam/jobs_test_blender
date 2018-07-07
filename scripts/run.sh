#!/bin/bash
RENDER_DEVICE=$1
FILE_FILTER=$2
TESTS_FILTER=$3

if [ "$RENDER_DEVICE" == "" ] || [ "$RENDER_DEVICE" == "null" ] ; then
    RENDER_DEVICE=gpu
fi

#if [ "$FILE_FILTER" == "" ] || [ "$FILE_FILTER" == "null" ] ; then
#    FILE_FILTER=smoke
#fi

python ../jobs_launcher/executeTests.py --test_filter $TESTS_FILTER --file_filter "$FILE_FILTER" --tests_root ../jobs --work_root ../Work/Results --work_dir Blender --cmd_variables Tool "blender" RenderDevice $RENDER_DEVICE ResPath "$CIS_TOOLS/../TestResources/BlenderAssets/scenes" PassLimit 5 rx 0 ry 0