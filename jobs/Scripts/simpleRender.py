import argparse
import sys
import os
import subprocess
import psutil
import json
import ctypes
import pyscreenshot


def get_windows_titles():
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

    titles = []

    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)

    return titles


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
            .format(tool=tool,scene = args.res_path  + "\\" + each, template = BlenderScriptPath)

    cmdScriptPath = os.path.join(work_dir, 'script.bat')
    with open(cmdScriptPath, 'w') as f:
        f.write(cmdRun)

    os.chdir(work_dir)

    p = subprocess.Popen(os.path.join(args.output, 'script.bat'), stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()

    #with open(os.path.join(args.output, "blender.txt"), 'w') as file:
     #   file.write(stdout)

    #p = psutil.Popen(os.path.join(args.output, 'script.bat'), stdout=subprocess.PIPE)
    rc = -1

    while True:
        try:
            rc = p.wait(timeout=20)
        except psutil.TimeoutExpired as err:
            fatal_errors_titles = ['Radeon ProRender']
            if set(fatal_errors_titles).intersection(get_windows_titles()):
                rc = -1
                error_screen = pyscreenshot.grab()
                error_screen.save(os.path.join(args.output, 'error_screenshot.jpg'))
                for child in reversed(p.children(recursive=True)):
                    child.terminate()
                p.terminate()
                break
        else:
            break

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
