import bpy

#change scene name to yours
Scenename = 'Scene'

bpy.data.scenes[Scenename].render.engine = "RPR"

# quality
bpy.data.scenes[Scenename].render.resolution_x = 1920
bpy.data.scenes[Scenename].render.resolution_y = 1920
bpy.data.scenes[Scenename].render.resolution_percentage = 30

bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}

# frame range
bpy.data.scenes[Scenename].frame_start = 1
bpy.data.scenes[Scenename].frame_end = 1

# image format
bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
bpy.data.scenes[Scenename].render.image_settings.quality = 80
bpy.data.scenes[Scenename].render.image_settings.color_mode = 'RGB'

# Cycles sampling
#bpy.data.scenes[Scenename].cycles.samples = 200

# output
bpy.data.scenes[Scenename].render.filepath = "{work_dir}"
bpy.data.scenes[Scenename].render.use_placeholder = True
bpy.data.scenes[Scenename].render.use_file_extension = True
bpy.data.scenes[Scenename].render.use_overwrite = True

# start render animation
bpy.ops.render.render(animation=True,scene=Scenename)