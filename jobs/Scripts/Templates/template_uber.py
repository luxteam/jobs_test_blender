def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	if (bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsCoat.blend"):
		render(test_list[0], test_list[1])
		return 2
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsEmissive.blend"):
		render(test_list[0], test_list[1])
		return 2
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsReflect.blend"):
		render(test_list[0], test_list[1])
		return 2
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsRefract.blend"):
		render(test_list[0], test_list[1])
		return 2
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "TestSceneMetalls.blend"):
		render(test_list[0], test_list[1])
		return 2
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "ComplexTestUber.blend"):
		render(test_list[0], test_list[1])
		return 2

if __name__ == "__main__":
	
	list_tests = [
	['BL_MAT_UBR_001', ["Testing coating in Uber material"], "TestBallsCoat.blend"],
	['BL_MAT_UBR_002', ["Testing emissive in Uber material"], "TestBallsEmissive.blend"],
	['BL_MAT_UBR_003', ["Testing reflection in Uber material"], "TestBallsReflect.blend"],
	['BL_MAT_UBR_004', ["Testing refraction in Uber material"], "TestBallsRefract.blend"],
	['BL_MAT_UBR_005', ["Testing metalls in Uber material"], "TestSceneMetalls.blend"],
	['BL_MAT_UBR_006', ["Complex test of Uber material"], "ComplexTestUber.blend"]
	]

	launch_tests()

