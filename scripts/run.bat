set PATH=c:\python35\;c:\python35\scripts\;%PATH%
set RENDER_DEVICE=gpu
set FILE_FILTER=Test
set TESTS_FILTER="%3"

python ..\jobs_launcher\executeTests.py --test_filter %TESTS_FILTER% --file_filter %FILE_FILTER% --tests_root ..\jobs --work_root ..\Work\Results --work_dir Blender --cmd_variables Tool "C:\Program Files\Blender2.8\blender.exe" RenderDevice %RENDER_DEVICE% ResPath "C:\TestResources\Blender2.8Assets" PassLimit 10 rx 0 ry 0     

pause