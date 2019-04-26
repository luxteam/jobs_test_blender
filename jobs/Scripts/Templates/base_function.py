import bpy
import addon_utils
import datetime
import sys
import json
import os
import logging
import traceback
from shutil import copyfile
import pyrpr
from rprblender import material_library


def set_value(path, name, value):
	if hasattr(path, name):
		setattr(path, name, value)
	else:
		logging.warning("No attribute found {{}}".format(name))


def get_value(path, name):
	if hasattr(path, name):
		return getattr(path, name)
	else:
		logging.warning("No attribute found {{}}".format(name))


def get_addon_version():
	tuple_ver = sys.modules['rprblender'].bl_info['version']
	version = str(tuple_ver[0]) + "." + str(tuple_ver[1]) + "." + str(tuple_ver[2])
	return version


def get_core_version():
	from pyrprwrap import API_VERSION
	mj = (API_VERSION & 0xFFFF00000) >> 28
	mn = (API_VERSION & 0xFFFFF) >> 8
	return "%x.%x" % (mj, mn)


def get_blender_version():
	return "Blender " + bpy.app.version_string.split(" (")[0]


def enable_rpr_render(scene):
	if not addon_utils.check('rprblender')[0]:
		addon_utils.enable('rprblender', default_set=True, persistent=False, handle_error=None)
	set_value(scene.render, 'engine', 'RPR')


def set_render_device(scene, render_mode):
	if render_mode == 'dual':
		set_value(scene.rpr.devices, "cpu_state", True)
		set_value(scene.rpr.devices, "gpu_states[0]", True)
		device_name = pyrpr.Context.cpu_state['name'] + " & " + pyrpr.Context.gpu_devices[0]['name']
	elif render_mode == 'cpu':
		set_value(scene.rpr.devices, "cpu_state", True)
		set_value(scene.rpr.devices, "gpu_states[0]", False)
		device_name = pyrpr.Context.cpu_state['name']
	elif render_mode == 'gpu':
		set_value(scene.rpr.devices, "cpu_state", False)
		set_value(scene.rpr.devices, "gpu_states[0]", True)
		device_name = pyrpr.Context.gpu_devices[0]['name']

	return device_name


def render(*argv):

	# get scene context
	scene = bpy.context.scene

	# enable rpr
	enable_rpr_render(scene)

	# set render device & get render device name
	render_mode = '{render_mode}'
	device_name = set_render_device(scene, render_mode)

	# test case name and description
	test_case = argv[0]
	script_info = argv[1]

	# image settings
	set_value(scene.render.image_settings, 'quality', 100)
	set_value(scene.render.image_settings, 'compression', 0)
	set_value(scene.render.image_settings, 'color_mode', 'RGB')

	# output settings
	set_value(scene.render, 'filepath', os.path.join("{work_dir}", "Color", test_case))
	set_value(scene.render, 'use_placeholder', True)
	set_value(scene.render, 'use_file_extension', True)
	set_value(scene.render, 'use_overwrite', True)

	# start render
	start_time = datetime.datetime.now()
	bpy.ops.render.render(write_still=True)
	render_time = (datetime.datetime.now() - start_time).total_seconds()

	image_format = get_value(scene.render.image_settings, 'file_format')
	if image_format == 'PNG':
		image_format = image_format.lower()
	else:
		image_format = 'jpg'

	# LOG
	file_name = test_case + "." + image_format
	log_name = os.path.join('{work_dir}', test_case + "_RPR.json")
	report = {{}}
	report['render_version'] = get_addon_version()
	report['render_mode'] = render_mode
	report['core_version'] = get_core_version()
	report['render_device'] = device_name
	report['test_group'] = '{package_name}'
	report['tool'] = get_blender_version()
	report['file_name'] = file_name
	report['scene_name'] = bpy.path.basename(bpy.context.blend_data.filepath)
	report['render_time'] = render_time
	report['render_color_path'] = os.path.join(r"Color", file_name)
	report['date_time'] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
	report['difference_color'] = "not compared yet"
	report['test_case'] = test_case
	report['script_info'] = script_info
	report['test_status'] = "undefined"

	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')


def create_report(*argv):
	
	# get scene context
	scene = bpy.context.scene

	# enable rpr
	enable_rpr_render(scene)

	# set render device & get render device name
	render_mode = '{render_mode}'
	device_name = set_render_device(scene, render_mode)
		
	# test case name and description
	test_case = argv[0]
	script_info = argv[1]
	picture = argv[2]

	# output
	copyfile(r"{work_dir}" + "/../../../../jobs/Tests/" + picture + ".jpg", r"{work_dir}/Color/" + test_case + ".jpg")

	# LOG
	file_name = test_case + ".jpg"
	log_name = os.path.join(r'{work_dir}', test_case + "_RPR.json")
	report = {{}}
	report['render_version'] = get_addon_version()
	report['render_mode'] = render_mode
	report['core_version'] = get_core_version()
	report['render_device'] = device_name
	report['test_group'] = '{package_name}'
	report['tool'] = get_blender_version()
	report['file_name'] = file_name
	report['scene_name'] = bpy.path.basename(bpy.context.blend_data.filepath)
	report['render_time'] = 0
	report['render_color_path'] = os.path.join(r"Color", file_name)
	report['date_time'] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
	report['difference_color'] = "not compared yet"
	report['test_case'] = test_case
	report['script_info'] = script_info
	report['test_status'] = "undefined"

	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')


def write_status(directory, status):
	with open(directory, 'r') as w:
		json_report = w.read()
	json_report = json_report.replace("undefined", status)
	json_report = json.loads(json_report)
	with open(directory, 'w') as file:
		json.dump(json_report, file, indent=' ')


def launch_tests():

	files = os.listdir(r"{work_dir}")
	json_files = list(filter(lambda x: x.endswith('RPR.json'), files))
	if not os.path.exists(os.path.join(r"{work_dir}", "Color")):
		os.makedirs(os.path.join(r"{work_dir}", "Color"))

	status = 0

	define_expected_result()

	for i in range(len(json_files), len(list_tests)):

		try:
			rc = prerender(list_tests[i])
			if rc:
				write_status(os.path.join(r"{work_dir}", list_tests[i][0] + "_RPR.json"), 'passed')
				status = 0
		except Exception as ex:
			traceback.print_exc()
			rc = -1

		if rc == -1:
			create_report(list_tests[i][0], list_tests[i][1], "failed")
			write_status(os.path.join(r"{work_dir}", list_tests[i][0] + "_RPR.json"), 'failed')
			status -= 1
			if status == -3:
				files = os.listdir(r"{work_dir}")
				json_files = list(filter(lambda x: x.endswith('RPR.json'), files))
				for i in range(len(json_files), len(list_tests)):
					create_report(list_tests[i][0], list_tests[i][1], "failed")
					write_status(os.path.join(r"{work_dir}", list_tests[i][0] + "_RPR.json"), 'failed')
				exit()
				
		with open(os.path.join(r"{work_dir}", 'log_status.txt'), 'a') as f:
			f.write("Current test: " + str(i) + " | fail count: " + \
				str(status) + " | last_status: " + str(rc) + " | total count: " + str(len(list_tests)) + "\n")


def define_expected_result():
	expected_tests = []

	for test in list_tests:
		expected_tests.append(test[0])

	with open(os.path.join(r"{work_dir}", "expected.json"), 'w') as file:
		json.dump(expected_tests, file, indent=4)
