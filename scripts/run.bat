set PATH=c:\python35\;c:\python35\scripts\;%PATH%
set RENDER_DEVICE=%1
set FILE_FILTER=%2
set TESTS_FILTER="%3"
rem C:\Program Files\Blender Foundation\Blender2.8\blender.exe
python -m pip install -r ../jobs_launcher/install/requirements.txt

python ..\jobs_launcher\executeTests.py --test_filter %TESTS_FILTER% --file_filter %FILE_FILTER% --tests_root ..\jobs --work_root ..\Work\Results --work_dir Blender28 --cmd_variables Tool "C:\Program Files\Blender Foundation\Blender\blender.exe" RenderDevice %RENDER_DEVICE% ResPath "C:\TestResources\Blender2.8Assets" PassLimit 10 rx 0 ry 0
