def main(test_case, script_info):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}


	render(test_case, script_info)

if __name__ == "__main__":
		
	if bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsCoat.blend":
		main('BL_MAT_UBR_001', ["Testing coating in Uber material"])

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsEmissive.blend":
		main('BL_MAT_UBR_002', ["Testing emissive in Uber material"])

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsReflect.blend":
		main('BL_MAT_UBR_003', ["Testing reflection in Uber material"])

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsRefract.blend":
		main('BL_MAT_UBR_004', ["Testing refraction in Uber material"])

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestSceneMetalls.blend":
		main('BL_MAT_UBR_005', ["Testing metalls in Uber material"])

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "ComplexTestUber.blend":
		main('BL_MAT_UBR_006', ["Complex test of Uber material"])

