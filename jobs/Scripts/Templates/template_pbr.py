def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	if (bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsCoatPBR.blend"):
		render(test_list[0], test_list[1])
		return 2
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsEmissivePBR.blend"):
		render(test_list[0], test_list[1])
		return 2
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "TestSceneMetallsPBR.blend"):
		render(test_list[0], test_list[1])
		return 2
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "ComplexTestPBR.blend"):
		render(test_list[0], test_list[1])
		return 2


if __name__ == "__main__":
	
	list_tests = [
	['BL_MAT_PBR_001', ["Testing coating in PBR material"], "TestBallsCoatPBR.blend"],
	['BL_MAT_PBR_002', ["Testing emissive in PBR material"], "TestBallsEmissivePBR.blend"],
	['BL_MAT_PBR_003', ["Testing metalls in PBR material"], "TestSceneMetallsPBR.blend"],
	['BL_MAT_PBR_004', ["Complex test of PBR material"], "ComplexTestPBR.blend"]
	]	
	
	launch_tests()

