import bpy

#change scene name to yours
Scenename = 'Scene'

# image format
bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
bpy.data.scenes[Scenename].render.image_settings.quality = 80
bpy.data.scenes[Scenename].render.image_settings.color_mode = 'RGB'

# Cycles sampling
bpy.data.scenes[Scenename].cycles.samples = 30

# output
bpy.data.scenes[Scenename].render.filepath = "{work_dir}\\"
bpy.data.scenes[Scenename].render.use_placeholder = True
bpy.data.scenes[Scenename].render.use_file_extension = True
bpy.data.scenes[Scenename].render.use_overwrite = True

# start render animation
bpy.ops.render.render(animation=True,scene=Scenename)