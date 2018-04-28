def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	if (bpy.path.basename(bpy.context.blend_data.filepath) == "EmissiveLight.blend"):
		render(test_list[0], test_list[1])
		return 2

if __name__ == "__main__":
		
	list_tests = [
	['BL_L_EMIS_001', ["Scene with Emissive material as light"], "EmissiveLight.blend"],
	]

	launch_tests()
