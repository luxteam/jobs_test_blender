def main(test_case):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	render(test_case)

if __name__ == "__main__":
		
	if bpy.path.basename(bpy.context.blend_data.filepath) == "EmissiveLight.blend":
		main('BL_L_EMIS_001')




