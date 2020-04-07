#!/bin/bash

echo import os >> cache_build.py
echo import bpy >> cache_build.py
echo bpy.context.scene.render.image_settings.file_format = '"JPEG"' >> cache_build.py
echo bpy.context.scene.render.filepath = os.path.join'(os.getcwd(), "..", "Work", "Results", "Blender28", "cache_building")' >> cache_build.py
echo bpy.ops.render.render'(write_still=True, scene=r"$CIS_TOOLS/../TestResources/Blender2.8Assets/Smoke/default.blend")' >> cache_build.py

blender -b -E RPR -P "cache_build.py"