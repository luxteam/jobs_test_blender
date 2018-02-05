import bpy
import addon_utils
import datetime
import sys
import json
import os

def main(size, size_r_x, size_r_y, size_a_x, size_a_y):

	#get scene name
	Scenename = bpy.context.scene.name

	# RPR Settings
	if((addon_utils.check("rprblender"))[0] == False) : 
	    addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}

	# resolution
	bpy.data.scenes[Scenename].render.resolution_x = size_r_x
	bpy.data.scenes[Scenename].render.resolution_y = size_r_y
	bpy.data.scenes[Scenename].render.pixel_aspect_x = size_a_x
	bpy.data.scenes[Scenename].render.pixel_aspect_y = size_a_y
	bpy.data.scenes[Scenename].render.resolution_percentage = 100

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
	name_scene = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + size
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
	name_scene_for_json = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + size + "BL"
	log_name = os.path.join(r'{work_dir}', name_scene_for_json + ".json")
	report = {{}}
	report['render_version'] = version
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['tool'] = "Blender " + bpy.app.version_string
	report['file_name'] = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + size + "_01.jpg"
	report['scene_name'] = bpy.context.scene.name
	report['render_time'] = Render_time.total_seconds()
	report['render_color_path'] = r"{work_dir}" + "/Color/" + name_scene + "_01.jpg"
	report['date_time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['difference_color'] = "not compared yet"


	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')

if __name__ == "__main__":
	
	main("DVCPRO_HD_1080p", 1280, 1080, 3, 2)
	main("DVCPRO_HD_720p", 960, 720, 4, 3)
	main("HDTV_1080p", 1920, 1080, 1, 1)
	main("HDTV_720p", 1280, 720, 1, 1)
	main("HDV_1080p", 1440, 1080, 4, 3)
	main("HDV_NTSC_1080p", 1440, 1080, 4, 3)
	main("HDV_PAL_1080p", 1440, 1080, 4, 3)
	main("TV_NTSC_16_9", 720, 480, 40.1, 33)
	main("TV_NTSC_4_3", 720, 486, 10, 11)
	main("TV_PAL_16_9", 720, 576, 16, 11)
	main("TV_PAL_4_3", 720, 576, 12, 11)
	main("2K", 2048, 1152, 3, 2)
	main("4K", 4096, 3204, 3, 2)
	main("2000x2000", 2000, 2000, 3, 2)
	main("3000x3000", 3000, 3000, 3, 2)
	main("4000x4000", 4000, 4000, 3, 2)
	main("5000x5000", 5000, 5000, 3, 2)
	main("6000x6000", 6000, 6000, 3, 2)
	main("7000x7000", 7000, 7000, 3, 2)
	main("8000x8000", 8000, 8000, 3, 2)

