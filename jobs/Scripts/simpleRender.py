import argparse
import sys
import os
import subprocess
import psutil
import json
import ctypes
import pyscreenshot
import platform

def main():
    stage_report = [{'status': 'INIT'}, {'log': ['simpleRender.py start']}]
    parser = argparse.ArgumentParser()

    parser.add_argument('--stage_report', required=True)
    parser.add_argument('--tool', required=True, metavar="<path>")
    parser.add_argument('--res_path', required=True)
    parser.add_argument('--render_mode', required=True)
    parser.add_argument('--template', required=True)
    parser.add_argument('--pass_limit', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--test_list', required=True)

    args = parser.parse_args()

    tool = args.tool
    scenes = args.test_list

    template = args.template
    with open(os.path.join(os.path.dirname(sys.argv[0]), template)) as f:
        blender_script_template = f.read()

    with open(os.path.join(os.path.dirname(sys.argv[0]), scenes)) as f:
        blender_scenes = f.read()


    if (args.render_mode == '0') :
        render_mode = 'cpu'
    else :
        render_mode = 'gpu'

    scene_list = blender_scenes.split(",\n")
    work_dir = args.output 

    BlenderScript = blender_script_template.format(work_dir = work_dir, render_mode = render_mode, pass_limit = args.pass_limit)

    try:
        os.makedirs(work_dir)
    except BaseException:
        print("")

    BlenderScriptPath = os.path.join(work_dir, 'script.py')
    with open(BlenderScriptPath, 'w') as f:
        f.write(BlenderScript)

    cmdRun = ""
    for each in scene_list :
        cmdRun += '"{tool}" -b "{scene}" -P "{template}"\n' \
            .format(tool=tool,scene = os.path.join(args.res_path, each), template = BlenderScriptPath)


    system_pl = platform.system()
    if (system_pl == 'Linux'):
        cmdScriptPath = os.path.join(work_dir, 'script.sh')
        with open(cmdScriptPath, 'w') as f:
            f.write(cmdRun)

        os.system('chmod +x {}'.format(cmdScriptPath))
    elif (system_pl == "Windows" ):
        cmdScriptPath = os.path.join(work_dir, 'script.bat')
        with open(cmdScriptPath, 'w') as f:
            f.write(cmdRun)

    os.chdir(work_dir)

    p = subprocess.Popen(cmdScriptPath, shell = True   , stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()

    with open(os.path.join(args.output, "log"), 'w') as file:
        stdout = stdout.decode("utf-8")
        file.write(stdout)

    with open(os.path.join(args.output, "error"), 'w') as file:
        stderr = stderr.decode("utf-8")
        file.write(stderr)

    #p = psutil.Popen(os.path.join(args.output, 'script.bat'), stdout=subprocess.PIPE)
    rc = -1

    
    try:
        rc = p.wait(timeout=100)
    except psutil.TimeoutExpired as err:
        rc = -1
        error_screen = pyscreenshot.grab()
        error_screen.save(os.path.join(args.output, 'error_screenshot.jpg'))
        for child in reversed(p.children(recursive=True)):
            child.terminate()
        p.terminate()

    if rc == 0:
        print('passed')
        stage_report[0]['status'] = 'OK'
        stage_report[1]['log'].append('subprocess PASSED')
    else:
        print('failed')
        stage_report[0]['status'] = 'TERMINATED'
        stage_report[1]['log'].append('subprocess FAILED and was TERMINATED')

    with open(os.path.join(args.output, args.stage_report), 'w') as file:
        json.dump(stage_report, file, indent=' ')

    return rc


if __name__ == "__main__":
    rc = main()
    exit(rc)
