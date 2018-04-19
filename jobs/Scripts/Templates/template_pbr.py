def main(test_case):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	render(test_case)

if __name__ == "__main__":
		
	if bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsCoatPBR.blend":
		main('BL_MAT_PBR_001')

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsEmissivePBR.blend":
		main('BL_MAT_PBR_002')

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "TestSceneMetallsPBR.blend":
		main('BL_MAT_PBR_003')

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "ComplexTestPBR.blend":
		main('BL_MAT_PBR_004')


