
def main(ibl_type, intensity, ibl_file, test_case):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = ibl_type
	bpy.context.scene.world.rpr_data.environment.ibl.intensity = intensity

	if (ibl_type == 'IBL'):
		bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
		ibl_map = os.path.join("{res_path}", ibl_file)
		bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)

	render(test_case)

if __name__ == "__main__":

	main('COLOR', 0, 'None', 'BL_RS_IBL_001')
	main('COLOR', 1, 'None', 'BL_RS_IBL_002')
	main('COLOR', 2, 'None', 'BL_RS_IBL_003')
	main('COLOR', 3, 'None', 'BL_RS_IBL_004')
	main('COLOR', 5, 'None', 'BL_RS_IBL_005')
	main('COLOR', 7, 'None', 'BL_RS_IBL_006')
	main('COLOR', 10, 'None', 'BL_RS_IBL_007')

	main('IBL', 0, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_008')
	main('IBL', 1, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_009')
	main('IBL', 2, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_010')
	main('IBL', 3, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_011')
	main('IBL', 5, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_012')
	main('IBL', 7, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_013')
	main('IBL', 10, 'Tropical_Beach_3k.hdr', 'BL_RS_IBL_014')

	main('IBL', 0, 'ibl_test.exr', 'BL_RS_IBL_015')
	main('IBL', 1, 'ibl_test.exr', 'BL_RS_IBL_016')
	main('IBL', 2, 'ibl_test.exr', 'BL_RS_IBL_017')
	main('IBL', 3, 'ibl_test.exr', 'BL_RS_IBL_018')
	main('IBL', 5, 'ibl_test.exr', 'BL_RS_IBL_019')
	main('IBL', 7, 'ibl_test.exr', 'BL_RS_IBL_020')
	main('IBL', 10, 'ibl_test.exr', 'BL_RS_IBL_021')


