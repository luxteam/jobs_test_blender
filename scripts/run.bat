set PATH=c:\python35\;c:\python35\scripts\;%PATH%
set RENDER_DEVICE=%1
set FILE_FILTER=%2
set TESTS_FILTER="%3"
set RX=%4
set RY=%5
set SPU=%6
set ITER=%7
set THRESHOLD=%8

if not defined RX set RX=0
if not defined RY set RY=0
if not defined SPU set SPU=25
if not defined ITER set ITER=50
if not defined THRESHOLD set THRESHOLD=0.05

python -m pip install -r ../jobs_launcher/install/requirements.txt

python ..\jobs_launcher\executeTests.py --test_filter %TESTS_FILTER% --file_filter %FILE_FILTER% --tests_root ..\jobs --work_root ..\Work\Results --work_dir Blender28 --cmd_variables Tool "C:\Program Files\Blender Foundation\Blender 2.82\blender.exe" RenderDevice %RENDER_DEVICE% ResPath "C:\TestResources\Blender2.8Assets" PassLimit %ITER% rx %RX% ry %RY% SPU %SPU% threshold %THRESHOLD%