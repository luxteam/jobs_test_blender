import bpy
import addon_utils
import datetime
import sys
import json
import os

def main(filter_a, value):

	#get scene name
	Scenename = bpy.context.scene.name

	# RPR Settings
	if((addon_utils.check("rprblender"))[0] == False) : 
	    addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}

	bpy.data.scenes[Scenename].rpr.render.aa.filter = filter_a
	bpy.data.scenes[Scenename].rpr.render.aa.radius = value

	# Render device in RPR
	bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type_plus_cpu = False
	bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type = '{render_mode}'
	#bpy.context.user_preferences.addons["rprblender"].preferences.settings.gpu_count = 2
	#bpy.context.user_preferences.addons["rprblender"].preferences.settings.samples = 1
	bpy.context.user_preferences.addons["rprblender"].preferences.settings.include_uncertified_devices = True

	# frame range
	bpy.data.scenes[Scenename].frame_start = 1
	bpy.data.scenes[Scenename].frame_end = 1

	# image format
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	bpy.data.scenes[Scenename].render.image_settings.quality = 80
	bpy.data.scenes[Scenename].render.image_settings.color_mode = 'RGB'

	# output
	name_scene = bpy.path.basename(bpy.context.blend_data.filepath) +  "_" + filter_a + "_" + str(value)
	output = r"{work_dir}" + "/Color/" + name_scene + "_##"
	bpy.data.scenes[Scenename].render.filepath = output 
	bpy.data.scenes[Scenename].render.use_placeholder = True
	bpy.data.scenes[Scenename].render.use_file_extension = True
	bpy.data.scenes[Scenename].render.use_overwrite = True

	# start render animation
	TIMER = datetime.datetime.now()
	bpy.ops.render.render(animation=True,scene=Scenename)
	Render_time = datetime.datetime.now() - TIMER

	# get version of rpr addon
	for mod_name in bpy.context.user_preferences.addons.keys():
	    if (mod_name == 'rprblender') : 
	        mod = sys.modules[mod_name]
	        ver = mod.bl_info.get('version')
	        version = str(ver[0]) + "." + str(ver[1]) + "." + str(ver[2])
	     
	# LOG
	name_scene_for_json = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + filter_a + "_" + str(value) + "BL"
	log_name = os.path.join(r'{work_dir}', name_scene_for_json + ".json")
	report = {{}}
	report['render_version'] = version
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['tool'] = "Blender " + bpy.app.version_string
	report['file_name'] = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + filter_a + "_" + str(value) + "_01.jpg"
	report['scene_name'] = bpy.context.scene.name
	report['render_time'] = Render_time.total_seconds()
	report['render_color_path'] = r"{work_dir}" + "/Color/" + name_scene + "_01.jpg"
	report['date_time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['difference_color'] = "not compared yet"


	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')

if __name__ == "__main__":
	main('MITCHELL', 0)
	main('MITCHELL', 1.5)
	main('MITCHELL', 5)
	main('MITCHELL', 8)
	main('MITCHELL', 10)
	main('TRIANGLE', 0)
	main('TRIANGLE', 1.5)
	main('TRIANGLE', 5)
	main('TRIANGLE', 8)
	main('TRIANGLE', 10)
	main('LANCZOS', 0)
	main('LANCZOS', 1.5)
	main('LANCZOS', 5)
	main('LANCZOS', 8)
	main('LANCZOS', 10)
	main('GAUSSIAN', 0)
	main('GAUSSIAN', 1.5)
	main('GAUSSIAN', 5)
	main('GAUSSIAN', 8)
	main('GAUSSIAN', 10)
	main('BOX', 0)
	main('BOX', 1.5)
	main('BOX', 5)
	main('BOX', 8)
	main('BOX', 10)
	main('BLACKMANHARRIS', 0)
	main('BLACKMANHARRIS', 1.5)
	main('BLACKMANHARRIS', 5)
	main('BLACKMANHARRIS', 8)
	main('BLACKMANHARRIS', 10)


