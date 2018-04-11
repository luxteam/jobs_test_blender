#!/bin/bash
RENDER_DEVICE="$1"
TESTS_FILTER="$2"
TEST_PACKAGE="$3"

if [ "$RENDER_DEVICE" == "" ] || [ "$RENDER_DEVICE" == "null" ] ; then
    RENDER_DEVICE=gpu
fi

if [ "$TESTS_FILTER" == "" ] || [ "$TESTS_FILTER" == "null" ] ; then
    TESTS_FILTER=full
fi

if [ "$TEST_PACKAGE" == "" ] || [ "$TEST_PACKAGE" == "null" ] ; then
    TEST_PACKAGE=""
fi

python ../jobs_launcher/executeTests.py --test_filter "$TEST_PACKAGE" --tests_root ../jobs --work_root ../Work/Results --work_dir Blender --cmd_variables Tool "/home/user/Desktop/blender-2.79-linux-glibc219-x86_64/blender" RenderDevice "$RENDER_DEVICE" TestsFilter "$TESTS_FILTER" ResPath "/home/user/Downloads/BlenderAssets/scenes"
