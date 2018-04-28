
def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = test_list[2]
	bpy.context.scene.world.rpr_data.environment.ibl.intensity = test_list[3]

	if (test_list[2] == 'IBL'):
		bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
		ibl_map = os.path.join("{res_path}", test_list[4])
		bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	['BL_RS_IBL_001', ["Type: Color", "Intensity: 0"], 'COLOR', 0, 'None'], 
	['BL_RS_IBL_002', ["Type: Color", "Intensity: 1"], 'COLOR', 1, 'None'],
	['BL_RS_IBL_003', ["Type: Color", "Intensity: 2"], 'COLOR', 2, 'None'],
	['BL_RS_IBL_004', ["Type: Color", "Intensity: 3"], 'COLOR', 3, 'None'],
	['BL_RS_IBL_005', ["Type: Color", "Intensity: 5"], 'COLOR', 5, 'None'],
	['BL_RS_IBL_006', ["Type: Color", "Intensity: 7"], 'COLOR', 7, 'None'],
	['BL_RS_IBL_007', ["Type: Color", "Intensity: 10"], 'COLOR', 10, 'None'],
	['BL_RS_IBL_008', ["Type: IBL with hdr map", "Intensity: 0"], 'IBL', 0, 'Tropical_Beach_3k.hdr'],
	['BL_RS_IBL_009', ["Type: IBL with hdr map", "Intensity: 1"], 'IBL', 1, 'Tropical_Beach_3k.hdr'],
	['BL_RS_IBL_010', ["Type: IBL with hdr map", "Intensity: 2"], 'IBL', 2, 'Tropical_Beach_3k.hdr'],
	['BL_RS_IBL_011', ["Type: IBL with hdr map", "Intensity: 3"], 'IBL', 3, 'Tropical_Beach_3k.hdr'],
	['BL_RS_IBL_012', ["Type: IBL with hdr map", "Intensity: 5"], 'IBL', 5, 'Tropical_Beach_3k.hdr'],
	['BL_RS_IBL_013', ["Type: IBL with hdr map", "Intensity: 7"], 'IBL', 7, 'Tropical_Beach_3k.hdr'],
	['BL_RS_IBL_014', ["Type: IBL with hdr map", "Intensity: 10"], 'IBL', 10, 'Tropical_Beach_3k.hdr'],
	['BL_RS_IBL_015', ["Type: IBL with exr map", "Intensity: 0"], 'IBL', 0, 'ibl_test.exr'],
	['BL_RS_IBL_016', ["Type: IBL with exr map", "Intensity: 1"], 'IBL', 1, 'ibl_test.exr'],
	['BL_RS_IBL_017', ["Type: IBL with exr map", "Intensity: 2"], 'IBL', 2, 'ibl_test.exr'],
	['BL_RS_IBL_018', ["Type: IBL with exr map", "Intensity: 3"], 'IBL', 3, 'ibl_test.exr'],
	['BL_RS_IBL_019', ["Type: IBL with exr map", "Intensity: 5"], 'IBL', 5, 'ibl_test.exr'],
	['BL_RS_IBL_020', ["Type: IBL with exr map", "Intensity: 7"], 'IBL', 7, 'ibl_test.exr'],
	['BL_RS_IBL_021', ["Type: IBL with exr map", "Intensity: 10"], 'IBL', 10, 'ibl_test.exr']
	]

	launch_tests()



