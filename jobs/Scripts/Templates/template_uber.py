def main(test_case):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	render(test_case)

if __name__ == "__main__":
		
	if bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsCoat.blend":
		main('BL_MAT_UBR_001')

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsEmissive.blend":
		main('BL_MAT_UBR_002')

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsReflect.blend":
		main('BL_MAT_UBR_003')

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsRefract.blend":
		main('BL_MAT_UBR_004')

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestSceneMetalls.blend":
		main('BL_MAT_UBR_005')

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "ComplexTestUber.blend":
		main('BL_MAT_UBR_006')

