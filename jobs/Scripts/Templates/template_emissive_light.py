def main(test_case, script_info):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	render(test_case, script_info)

if __name__ == "__main__":
		
	if bpy.path.basename(bpy.context.blend_data.filepath) == "EmissiveLight.blend":
		main('BL_L_EMIS_001', ["Scene with Emissive material as light"])




