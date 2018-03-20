set PATH=c:\python35\;c:\python35\scripts\;%PATH%

python ..\jobs_launcher\executeTests.py --test_package Smoke_Test --tests_root ..\jobs --work_root ..\Work\Results --work_dir Blender --cmd_variables Tool "C:\Program Files\Blender Foundation\Blender\blender.exe" RenderDevice gpu TestsFilter full ResPath "C:\TestResources\BlenderAssets\scenes"
pause