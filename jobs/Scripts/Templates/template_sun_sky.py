import bpy
import addon_utils
import datetime
import sys
import json
import os

def main(type_sun_sky, quality, param1, param2):

	#get scene name
	Scenename = bpy.context.scene.name

	# RPR Settings
	if((addon_utils.check("rprblender"))[0] == False) : 
	    addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}


	bpy.context.scene.world.rpr_data.environment.type = 'SUN_SKY'
	bpy.context.scene.world.rpr_data.environment.sun_sky.type = type_sun_sky
	bpy.context.scene.world.rpr_data.environment.sun_sky.ground_color = (0.4, 0.00703741, 0.00508468)
	bpy.context.scene.world.rpr_data.environment.sun_sky.texture_resolution = quality

	if type_sun_sky == 'analytical_sky':
		bpy.context.scene.world.rpr_data.environment.sun_sky.azimuth = param1
		bpy.context.scene.world.rpr_data.environment.sun_sky.altitude = param2
	else:
		bpy.ops.rpr.op_get_time_now()
		bpy.context.scene.world.rpr_data.environment.sun_sky.time_zone = 3
		bpy.context.scene.world.rpr_data.environment.sun_sky.latitude = 0.973583
		bpy.context.scene.world.rpr_data.environment.sun_sky.longitude = 0.656516
		bpy.context.scene.world.rpr_data.environment.sun_sky.time_hours = param1
		bpy.context.scene.world.rpr_data.environment.sun_sky.time_minutes = param2

	# Render device in RPR
	if '{render_mode}' == 'dual':
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type_plus_cpu = True
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type = 'gpu'
	else:
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type = '{render_mode}'
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type_plus_cpu = False
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
	name_scene = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + type_sun_sky + "_" + quality + "_" + str(param1) + "_" + str(param2)
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
	name_scene_for_json = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + type_sun_sky + "_" + quality + "_" + str(param1) + "_" + str(param2) + "BL"
	log_name = os.path.join(r'{work_dir}', name_scene_for_json + ".json")
	report = {{}}
	report['render_version'] = version
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['tool'] = "Blender " + bpy.app.version_string
	report['file_name'] = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + type_sun_sky + "_" + quality + "_" + str(param1) + "_" + str(param2) + "_01.jpg"
	report['scene_name'] = bpy.context.scene.name
	report['render_time'] = Render_time.total_seconds()
	report['render_color_path'] = r"{work_dir}" + "/Color/" + name_scene + "_01.jpg"
	report['date_time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['difference_color'] = "not compared yet"


	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')

if __name__ == "__main__":
	main('analytical_sky', 'small', 0, 0.523599)
	main('analytical_sky', 'normal', 0, 0.523599)
	main('analytical_sky', 'high', 0, 0.523599)
	main('date_time_location', 'small', 12, 0)	
	main('date_time_location', 'normal', 12, 0)	
	main('date_time_location', 'high', 12, 0)
	main('date_time_location', 'normal', 0, 0)	
	main('date_time_location', 'normal', 6, 0)	
	main('date_time_location', 'normal', 18, 0)	
	main('date_time_location', 'normal', 23, 59)	
	main('analytical_sky', 'normal', 0, 0)
	main('analytical_sky', 'normal', 0, 0.785398)
	main('analytical_sky', 'normal', 0, 1.5708)
	main('analytical_sky', 'normal', 1.5708, 0)
	main('analytical_sky', 'normal', 1.5708, 0.785398)
	main('analytical_sky', 'normal', 1.5708, 1.5708)
	main('analytical_sky', 'normal', 3.14159, 0)
	main('analytical_sky', 'normal', 3.14159, 0.785398)
	main('analytical_sky', 'normal', 3.14159, 1.5708)
	main('analytical_sky', 'normal', 4.71239, 0)
	main('analytical_sky', 'normal', 4.71239, 0.785398)
	main('analytical_sky', 'normal', 4.71239, 1.5708)
	main('analytical_sky', 'normal', 6.28319, 0)
	main('analytical_sky', 'normal', 6.28319, 0.785398)
	main('analytical_sky', 'normal', 6.28319, 1.5708)



