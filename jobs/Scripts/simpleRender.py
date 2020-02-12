import argparse
import os
import subprocess
import psutil
import json
import ctypes
import pyscreenshot
import platform
from datetime import datetime
from shutil import copyfile, which
import sys
import re
import time

sys.path.append(os.path.abspath(os.path.join(
	os.path.dirname(__file__), os.path.pardir, os.path.pardir)))

import jobs_launcher.core.config as core_config
from jobs_launcher.core.system_info import get_gpu
from jobs_launcher.core.kill_process import kill_process

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
PROCESS = ['blender', 'blender.exe', 'Blender']


def createArgsParser():
	parser = argparse.ArgumentParser()

	parser.add_argument('--tool', required=True, metavar="<path>")
	parser.add_argument('--render_device', required=True)
	parser.add_argument('--output', required=True, metavar="<dir>")
	parser.add_argument('--testType', required=True)
	parser.add_argument('--res_path', required=True)
	parser.add_argument('--resolution_x', required=True)
	parser.add_argument('--resolution_y', required=True)
	parser.add_argument('--max_samples', required=True)
	parser.add_argument('--testCases', required=True)
	parser.add_argument('--SPU', required=False, default=25)
	parser.add_argument('--fail_count', required=False, default=0, type=int)

	return parser


def main(args):
	if which(args.tool) is None:
		core_config.main_logger.error('Can\'t find tool ' + args.tool)
		exit(-1)

	core_config.main_logger.info('Make "base_functions.py"')

	try:
		with open(os.path.join(os.path.dirname(__file__), "base_functions.py")) as f:
			script = f.read()
		with open(os.path.realpath(os.path.join(os.path.dirname(__file__),  '..', 'Tests', args.testType, 'test_cases.json'))) as f:
			test_cases = f.read()
	except OSError as e:
		core_config.main_logger.error(str(e))
		return 1

	if os.path.exists(os.path.join(os.path.dirname(__file__), 'extensions', args.testType + '.py')):
		with open(os.path.join(os.path.dirname(__file__), 'extensions', args.testType + '.py')) as f:
			extension_script = f.read()
		script = script.split('# place for extension functions')
		script = script[0] + extension_script + script[1]

	work_dir = os.path.abspath(args.output)
	script = script.format(work_dir=work_dir, testType=args.testType, render_device=args.render_device, res_path=args.res_path,
							  resolution_x=args.resolution_x, resolution_y=args.resolution_y, SPU=args.SPU)

	with open(os.path.join(args.output, 'base_functions.py'), 'w') as file:
		file.write(script)

	try:
		cases = json.load(open(os.path.realpath(
			os.path.join(work_dir, 'test_cases.json'))))
	except:
		try:
			cases = json.load(open(os.path.realpath(os.path.join(os.path.dirname(__file__),  '..', 'Tests', args.testType, 'test_cases.json'))))
		except:
			core_config.logging.error("Can't load test_cases.json")

	if (os.path.exists(os.path.join(os.path.dirname(__file__), args.testCases))):
		with open(os.path.join(os.path.dirname(__file__), args.testCases)) as f:
			tc = f.read()
			test_cases = json.loads(tc)[args.testType]
		necessary_cases = [item for item in cases if item['case'] in test_cases]
		cases = necessary_cases

	core_config.main_logger.info('Create empty report files')	

	if not os.path.exists(os.path.join(work_dir, 'Color')):
		os.makedirs(os.path.join(work_dir, 'Color'))
	copyfile(os.path.abspath(os.path.join(work_dir, '..', '..', '..', '..', 'jobs_launcher',
                                       'common', 'img', 'error.jpg')), os.path.join(work_dir, 'Color', 'failed.jpg'))

	gpu = get_gpu()
	if gpu == False:
		core_config.main_logger.error("Can't get gpu name")
	render_platform = set([platform.system(), gpu])

	for case in cases:
		if sum([current_conf & set(skip_conf) == set(skip_conf) for skip_conf in case.get('skip_on', '')]):
			for i in case['skip_on']:
				skip_on = set(i)
				if render_platform.intersection(skip_on) == skip_on:
					case['status'] = 'skipped'

		if case['status'] != 'done':
			if case["status"] == 'inprogress':
				case['status'] = 'fail'

			template = core_config.RENDER_REPORT_BASE
			template['test_case'] = case['case']
			template['render_device'] = get_gpu()
			template['test_status'] = 'error'
			template['script_info'] = case['script_info']
			template['scene_name'] = case.get('scene', '')
			template['file_name'] = 'failed.jpg'
			template['render_color_path'] = os.path.join('Color', 'failed.jpg')
			template['test_group'] = args.testType
			template['date_time'] = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
				
			with open(os.path.join(work_dir, case['case'] + core_config.CASE_REPORT_SUFFIX), 'w') as f:
				f.write(json.dumps([template], indent=4))

	with open(os.path.join(work_dir, 'test_cases.json'), "w+") as f:
		json.dump(cases, f, indent=4)

	cmdRun = '"{tool}" -b -P "{template}"\n'.format(tool=args.tool, template=os.path.join(args.output, 'base_functions.py'))

	system_pl = platform.system()
	if system_pl == "Windows":
		cmdScriptPath = os.path.join(work_dir, 'script.bat')
		with open(cmdScriptPath, 'w') as f:
			f.write(cmdRun)
	else:
		cmdScriptPath = os.path.join(work_dir, 'script.sh')
		with open(cmdScriptPath, 'w') as f:
			f.write(cmdRun)
		os.system('chmod +x {}'.format(cmdScriptPath))

	p = subprocess.Popen(cmdScriptPath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = p.communicate()

	with open(os.path.join(args.output, "renderTool.log"), 'a', encoding='utf-8') as file:
		stdout = stdout.decode("utf-8")
		file.write(stdout)

	with open(os.path.join(args.output, "renderTool.log"), 'a', encoding='utf-8') as file:
		file.write("\n ----STEDERR---- \n")
		stderr = stderr.decode("utf-8")
		file.write(stderr)

	try:
		rc = p.wait(timeout=100)
	except psutil.TimeoutExpired as err:
		rc = -1
		for child in reversed(p.children(recursive=True)):
			child.terminate()
		p.terminate()

	'''
	TODO: check athena work in blender 
	if args.testType in ['Athena']:
		subprocess.call([sys.executable, os.path.realpath(os.path.join(os.path.dirname(__file__), 'extensions', args.testType + '.py')), args.output])
	core_config.main_logger.info("Main func return : {}".format(rc))
	'''

	return rc


def group_failed(args):
	try:
		cases = json.load(open(os.path.realpath(os.path.join(os.path.abspath(args.output).replace('\\', '/'), 'test_cases.json'))))
	except:
		cases = json.load(open(os.path.realpath(os.path.join(os.path.dirname(__file__),  '..', 'Tests', args.testType, 'test_cases.json'))))

	for case in cases:
		if case['status'] == 'active':
			case['status'] = 'skipped'

	with open(os.path.join(os.path.abspath(args.output).replace('\\', '/'), 'test_cases.json'), "w+") as f:
		json.dump(cases, f, indent=4)

	rc = main(args)
	kill_process(PROCESS)
	core_config.main_logger.info("Finish simpleRender with code: {}".format(rc))
	exit(rc)


if __name__ == "__main__":

	core_config.main_logger.info("simpleRender start working...")
	args = createArgsParser().parse_args()

	iteration = 0

	try:
		os.makedirs(args.output)
	except OSError as e:
		pass

	while True:
		iteration += 1
		core_config.main_logger.info('Try to run script in blender (#' + str(iteration) + ')')
		if iteration > 1:
			copyfile(os.path.join(os.path.abspath(args.output), 'renderTool.log'), os.path.join(os.path.abspath(args.output), 'renderTool' + str(iteration-1) + '.log'))

		rc = main(args)

		try:
			cases = json.load(open(os.path.realpath(os.path.join(os.path.abspath(args.output), 'test_cases.json'))))
		except:
			cases = json.load(open(os.path.realpath(os.path.join(os.path.dirname(__file__),  '..', 'Tests', args.testType, 'test_cases.json'))))

		active_cases = 0
		failed_count = 0

		for case in cases:
			if case['status'] not in ['skipped']:
				if case['status'] in ['fail', 'error', 'inprogress']:
					failed_count += 1
					if args.fail_count == failed_count:
						group_failed(args)
				else:
					failed_count = 0

				if case['status'] in ['active', 'fail', 'inprogress']:
					active_cases += 1

		if active_cases == 0:
			kill_process(PROCESS)
			core_config.main_logger.info("Finish simpleRender with code: {}".format(rc))
			exit(rc)

