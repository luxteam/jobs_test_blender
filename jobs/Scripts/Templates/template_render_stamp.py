import bpy
import addon_utils
import datetime
import sys
import json
import os

def main(stamp, stamp_value, device_type):

	#get scene name
	Scenename = bpy.context.scene.name

	# RPR Settings
	if((addon_utils.check("rprblender"))[0] == False) : 
	    addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}

	#stamp

	bpy.data.scenes[Scenename].rpr.use_render_stamp = True
	bpy.data.scenes[Scenename].rpr.render_stamp = stamp_value

	# Render device in RPR
	if (device_type == 'dual'):
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type_plus_cpu = True
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type = 'gpu'
	else:
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type_plus_cpu = False
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type = device_type

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
	name_scene = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + stamp
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
	name_scene_for_json = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + stamp + "BL"
	log_name = os.path.join(r'{work_dir}', name_scene_for_json + ".json")
	report = {{}}
	report['render_version'] = version
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['tool'] = "Blender " + bpy.app.version_string
	report['file_name'] = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + stamp + "_01.jpg"
	report['scene_name'] = bpy.context.scene.name
	report['render_time'] = Render_time.total_seconds()
	report['render_color_path'] = r"{work_dir}" + "/Color/" + name_scene + "_01.jpg"
	report['date_time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['difference_color'] = "not compared yet"


	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')

if __name__ == "__main__":
	
	main("default_stamp", "Radeon ProRender for Blender %b | %h | Time: %pt | Passes: %pp | Objects: %so | Lights: %sl", "gpu")
	main("gpu_stamp", "Radeon ProRender for Blender %b | CPU %c | GPU %g | Render mode %r | Render device %h", "gpu")
	main("cpu_stamp", "Radeon ProRender for Blender %b | CPU %c | GPU %g | Render mode  %r | Render device %h", "cpu")
	main("dual_stamp", "Radeon ProRender for Blender %b | CPU %c | GPU %g | Render mode  %r | Render device %h", "dual")
	main("additional_info", "Radeon ProRender for Blender %b | Computer name %i | Current date %d", "gpu")

