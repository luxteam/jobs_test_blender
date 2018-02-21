set PATH=c:\python35\;c:\python35\scripts\;%PATH%

python ..\jobs_launcher\executeTests.py --tests_root ..\jobs --work_root ..\Results --work_dir Blender --cmd_variables Tool ""C:\blender-2.79a-rc-windows64\blender-2.79a-rc-windows64\blender.exe"" RenderDevice gpu TestsFilter full ResPath "C:\TestResources\BlenderAssets\scenes"
