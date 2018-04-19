
def main(ibl_type, intensity, ibl_file, test_case, script_info):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = ibl_type
	bpy.context.scene.world.rpr_data.environment.ibl.intensity = intensity

	if (ibl_type == 'IBL'):
		bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
		ibl_map = os.path.join("{res_path}", ibl_file)
		bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)

	render(test_case, script_info)

if __name__ == "__main__":

	main('COLOR', 0, 'None', 'BL_RS_IBL_001', ["Type: Color", "Intensity: 0"])
	main('COLOR', 1, 'None', 'BL_RS_IBL_002', ["Type: Color", "Intensity: 1"])
	main('COLOR', 2, 'None', 'BL_RS_IBL_003', ["Type: Color", "Intensity: 2"])
	main('COLOR', 3, 'None', 'BL_RS_IBL_004', ["Type: Color", "Intensity: 3"])
	main('COLOR', 5, 'None', 'BL_RS_IBL_005', ["Type: Color", "Intensity: 5"])
	main('COLOR', 7, 'None', 'BL_RS_IBL_006', ["Type: Color", "Intensity: 7"])
	main('COLOR', 10, 'None', 'BL_RS_IBL_007', ["Type: Color", "Intensity: 10"])

	main('IBL', 0, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_008', ["Type: IBL with hdr map", "Intensity: 0"])
	main('IBL', 1, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_009', ["Type: IBL with hdr map", "Intensity: 1"])
	main('IBL', 2, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_010', ["Type: IBL with hdr map", "Intensity: 2"])
	main('IBL', 3, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_011', ["Type: IBL with hdr map", "Intensity: 3"])
	main('IBL', 5, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_012', ["Type: IBL with hdr map", "Intensity: 5"])
	main('IBL', 7, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_013', ["Type: IBL with hdr map", "Intensity: 7"])
	main('IBL', 10, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_014', ["Type: IBL with hdr map", "Intensity: 10"])

	main('IBL', 0, 'ibl_test.exr', 'BL_RS_IBL_015', ["Type: IBL with exr map", "Intensity: 0"])
	main('IBL', 1, 'ibl_test.exr', 'BL_RS_IBL_016', ["Type: IBL with exr map", "Intensity: 1"])
	main('IBL', 2, 'ibl_test.exr', 'BL_RS_IBL_017', ["Type: IBL with exr map", "Intensity: 2"])
	main('IBL', 3, 'ibl_test.exr', 'BL_RS_IBL_018', ["Type: IBL with exr map", "Intensity: 3"])
	main('IBL', 5, 'ibl_test.exr', 'BL_RS_IBL_019', ["Type: IBL with exr map", "Intensity: 5"])
	main('IBL', 7, 'ibl_test.exr', 'BL_RS_IBL_020', ["Type: IBL with exr map", "Intensity: 7"])
	main('IBL', 10, 'ibl_test.exr', 'BL_RS_IBL_021', ["Type: IBL with exr map", "Intensity: 10"])


