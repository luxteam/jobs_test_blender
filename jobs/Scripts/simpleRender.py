import argparse
import sys
import os
import subprocess
import psutil
import json
import ctypes
import pyscreenshot
import platform
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import jobs_launcher.core.config as core_config


def createArgsParser():
	parser = argparse.ArgumentParser()

	parser.add_argument('--tool', required=True, metavar="<path>")
	parser.add_argument('--resource_path', required=True)
	parser.add_argument('--render_mode', required=True)
	parser.add_argument('--template', required=True)
	parser.add_argument('--resolution_x', required=True)
	parser.add_argument('--resolution_y', required=True)
	parser.add_argument('--package_name', required=True)
	parser.add_argument('--output', required=True)

	return parser


def kill_process(deny=['maya.exe', 'blender.exe', '3dsmax.exe']):
	for p in psutil.process_iter():
		try:
			p_info = p.as_dict(attrs=['pid', 'name', 'cpu_percent', 'username'])
			core_config.main_logger.info(
				"{name} \t (PID: {pid}) \t| Username: {username} | CPU Percent: {cpu_percent}".format(
					name=p_info['name'],
					pid=p_info['pid'],
					username=p_info['username'],
					cpu_percent=p_info['cpu_percent']
				))

			if p_info['name'] in deny:
				try:
					core_config.main_logger.info("Trying to kill process {name}".format(name=p_info['name']))

					p.terminate()
					time.sleep(10)

					p.kill()
					time.sleep(10)

					status = p.status()
					core_config.main_logger.error("Process {name} is alive (status: {status}".format(
						name=p_info["name"],
						status=status
					))
				except psutil.NoSuchProcess:
					core_config.main_logger.info("ATENTION: {name} is killed.".format(
						name=p_info['name']
					))
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			core_config.main_logger.error("Can't killed process: {name}".format(name=p_info['name']))


def main(args):

	work_dir = args.output

	with open(os.path.join(os.path.dirname(sys.argv[0]), "Templates", "base_function.py")) as f:
		base = f.read()

	with open(os.path.join(os.path.dirname(sys.argv[0]), args.template)) as f:
		blender_script_template = f.read()

	blender_script_template = base + blender_script_template

	BlenderScript = blender_script_template.format(work_dir=work_dir, render_mode=args.render_mode, resource_path=args.resource_path, \
													resolution_x=args.resolution_x, resolution_y=args.resolution_y, package_name=args.package_name)

	BlenderScriptPath = os.path.join(work_dir, 'script.py')
	with open(BlenderScriptPath, 'w') as f:
		f.write(BlenderScript)

	cmdRun = '"{tool}" -b -P "{template}"\n'.format(tool=args.tool, template=BlenderScriptPath)

	system_pl = platform.system()
	if (system_pl == "Windows"):
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

	with open(os.path.join(args.output, "renderTool.log"), 'w', encoding='utf-8') as file:
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

	return rc


if __name__ == "__main__":
	args = createArgsParser().parse_args()

	try:
		os.makedirs(args.output)
	except OSError as e:
		pass

	def getJsonCount():
		return len(list(filter(lambda x: x.endswith('RPR.json'), os.listdir(args.output))))

	def totalCount():
		try:        
			with open(os.path.join(os.path.dirname(__file__),  args.template)) as f:
				script_template = f.read()
			return len(script_template.replace(" ", "").split(",\n[\"BL"))
		except OSError as e:
			return -1

	total_count = totalCount()
	current_test = 0

	while current_test < total_count:
		rc = main(args) 
		current_test = getJsonCount()

	kill_process()
	exit(1)
