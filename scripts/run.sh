#!/bin/bash
RENDER_DEVICE="$1"
TEST_PACKAGE="$2"
TESTS_FILTER="$3"

if [ "$RENDER_DEVICE" == "" ] || [ "$RENDER_DEVICE" == "null" ] ; then
    RENDER_DEVICE=gpu
fi

if [ "$TEST_PACKAGE" == "" ] || [ "$TEST_PACKAGE" == "null" ] ; then
    TEST_PACKAGE=smoke
fi

python ../jobs_launcher/executeTests.py --file_filter "$TEST_PACKAGE" --tests_filter "$TESTS_FILTER" --tests_root ../jobs --work_root ../Work/Results --work_dir Blender --cmd_variables Tool "blender" RenderDevice "$RENDER_DEVICE" ResPath "$CIS_TOOLS/../TestResources/BlenderAssets/scenes" PassLimit 15 rx 0 ry 0
