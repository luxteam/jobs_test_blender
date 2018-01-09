import bpy
import addon_utils
import datetime
import sys
import json
import os

#get scene name
Scenename = bpy.context.scene.name

# RPR Settings
addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
bpy.data.scenes[Scenename].render.engine = "RPR"
bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}

# resolution
#bpy.data.scenes[Scenename].render.resolution_x = 1920
#bpy.data.scenes[Scenename].render.resolution_y = 1080
#bpy.data.scenes[Scenename].render.resolution_percentage = 30

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
name_scene = bpy.path.basename(bpy.context.blend_data.filepath)
output = "{work_dir}" + "\\" + name_scene + "_##"
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
# log_name = "{work_dir}" + "\\" + name_scene + ".json"

log_name = os.path.join('{work_dir}', "report.json")
report = {{}}
report['render_version'] = version
report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
report['tool'] = "Blender " + bpy.app.version_string
report['file_name'] = bpy.path.basename(bpy.context.blend_data.filepath)
report['scene_name'] = bpy.context.scene.name
# TODO: change on int (seconds)
report['render_time'] = str(Render_time)
report['render_color_path'] = bpy.path.basename(bpy.context.blend_data.filepath)

with open(log_name, 'w') as file:
	json.dump([report], file, indent=' ')

# file.write("Version of rprblender addon: " + version + "\r\n") 
# file.write("Render device type: " + bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type  + "\r\n")  
# file.write("Pass limit: " + str(bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations) + "\r\n")  
# file.write("Render size: " + str(bpy.data.scenes[Scenename].render.resolution_x) + " x " + str(bpy.data.scenes[Scenename].render.resolution_y) + "\r\n")  
# file.write("File name: " + bpy.path.basename(bpy.context.blend_data.filepath) + "\r\n")  
# file.write("Scene name: " + bpy.context.scene.name + "\r\n")  
# file.write("Frame: " + str(bpy.context.scene.frame_current) + "\r\n")  
# file.write("Date time: " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + "\r\n")  
# file.write("Render time: " + str(Render_time) + "\r\n")  

# file.close() 



