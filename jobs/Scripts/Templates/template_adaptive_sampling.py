def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.rpr.limits, 'min_samples', test_list[3])
	set_value(scene.rpr.limits, 'max_samples', test_list[4])
	set_value(scene.rpr.limits, 'noise_threshold', test_list[5])
	set_value(scene.rpr.limits, 'update_samples', test_list[6])
	set_value(scene.rpr.limits, 'seconds', test_list[7])
	set_value(scene.rpr.limits, 'use_tile_render', test_list[8])
	set_value(scene.rpr.limits, 'tile_x', test_list[9])
	set_value(scene.rpr.limits, 'tile_y', test_list[10])
	set_value(scene.rpr.limits, 'tile_order', test_list[11])

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	   ["BL28_RS_AS_001", ["Easy, Default Adaptive Sampling"], "ComplexTestUber.blend", 64, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_002", ["Easy, Min Samples - 16"], "ComplexTestUber.blend", 16, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_003", ["Easy, Min Samples - 32"], "ComplexTestUber.blend", 32, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_004", ["Easy, Min Samples - 50"], "ComplexTestUber.blend", 50, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_005", ["Easy, Min Samples - 100"], "ComplexTestUber.blend", 100, 100, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_006", ["Easy, Max Samples - 16"], "ComplexTestUber.blend", 16, 16, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_007", ["Easy, Max Samples - 100"], "ComplexTestUber.blend", 16, 100, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_008", ["Easy, Max Samples - 500"], "ComplexTestUber.blend", 16, 500, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_009", ["Easy, Max Samples - 1000"], "ComplexTestUber.blend", 16, 1000, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_010", ["Easy, Max Samples - 5000"], "ComplexTestUber.blend", 16, 5000, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_011", ["Easy, Max Samples - 10000"], "ComplexTestUber.blend", 16, 10000, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_012", ["Easy, Noise Threshold - 0"], "ComplexTestUber.blend", 16, 64, 0, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_013", ["Easy, Noise Threshold - 0.05"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_014", ["Easy, Noise Threshold - 0.5"], "ComplexTestUber.blend", 16, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_015", ["Easy, Noise Threshold - 1"], "ComplexTestUber.blend", 16, 64, 1, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_016", ["Easy, Time Limit - 0"], "ComplexTestUber.blend", 16, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_017", ["Easy, Time Limit - 10"], "ComplexTestUber.blend", 16, 10000, 0.5, 1, 10, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_018", ["Easy, Time Limit - 50"], "ComplexTestUber.blend", 16, 10000, 0.5, 1, 50, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_019", ["Easy, Time Limit - 100"], "ComplexTestUber.blend", 16, 10000, 0.5, 1, 100, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_020", ["Easy, Time Limit - 500"], "ComplexTestUber.blend", 16, 10000, 0.5, 1, 500, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_021", ["Normal, Default Adaptive Sampling"], "PassLimit_1.blend", 64, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_022", ["Normal, Min Samples - 16 "], "PassLimit_1.blend", 16, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_023", ["Normal, Min Samples - 32"], "PassLimit_1.blend", 32, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_024", ["Normal, Min Samples - 50"], "PassLimit_1.blend", 50, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_025", ["Normal, Min Samples - 100"], "PassLimit_1.blend", 100, 100, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_026", ["Normal, Max Samples - 16"], "PassLimit_1.blend", 16, 16, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_027", ["Normal, Max Samples - 100"], "PassLimit_1.blend", 16, 100, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_028", ["Normal, Max Samples - 500"], "PassLimit_1.blend", 16, 500, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_029", ["Normal, Max Samples - 1000"], "PassLimit_1.blend", 16, 1000, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_030", ["Normal, Max Samples - 5000"], "PassLimit_1.blend", 16, 5000, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_031", ["Normal, Max Samples - 10000"], "PassLimit_1.blend", 16, 10000, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_032", ["Normal, Noise Threshold - 0"], "PassLimit_1.blend", 16, 64, 0, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_033", ["Normal, Noise Threshold - 0.05"], "PassLimit_1.blend", 16, 64, 0.05, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_034", ["Normal, Noise Threshold - 0.5"], "PassLimit_1.blend", 16, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_035", ["Normal, Noise Threshold - 1"], "PassLimit_1.blend", 16, 64, 1, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_036", ["Normal, Time Limit - 0"], "PassLimit_1.blend", 16, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_037", ["Normal, Time Limit - 10"], "PassLimit_1.blend", 16, 10000, 0.5, 1, 10, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_038", ["Normal, Time Limit - 50"], "PassLimit_1.blend", 16, 10000, 0.5, 1, 50, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_039", ["Normal, Time Limit - 100"], "PassLimit_1.blend", 16, 10000, 0.5, 1, 100, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_040", ["Normal, Time Limit - 500"], "PassLimit_1.blend", 16, 10000, 0.5, 1, 500, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_041", ["Complex, Default Adaptive Sampling"], "PassLimit_2.blend", 64, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_042", ["Complex, Min Samples - 16"], "PassLimit_2.blend", 16, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_043", ["Complex, Min Samples - 32"], "PassLimit_2.blend", 32, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_044", ["Complex, Min Samples - 50"], "PassLimit_2.blend", 50, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_045", ["Complex, Min Samples - 100"], "PassLimit_2.blend", 100, 100, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_046", ["Complex, Max Samples - 16"], "PassLimit_2.blend", 16, 16, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_047", ["Complex, Max Samples - 100"], "PassLimit_2.blend", 16, 100, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_048", ["Complex, Max Samples - 500"], "PassLimit_2.blend", 16, 500, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_049", ["Complex, Max Samples - 1000"], "PassLimit_2.blend", 16, 1000, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_050", ["Complex, Max Samples - 5000"], "PassLimit_2.blend", 16, 5000, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_051", ["Complex, Max Samples - 10000"], "PassLimit_2.blend", 16, 10000, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_052", ["Complex, Noise Threshold - 0"], "PassLimit_2.blend", 16, 64, 0, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_053", ["Complex, Noise Threshold - 0.05"], "PassLimit_2.blend", 16, 64, 0.05, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_054", ["Complex, Noise Threshold - 0.5"], "PassLimit_2.blend", 16, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_055", ["Complex, Noise Threshold - 1"], "PassLimit_2.blend", 16, 64, 1, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_056", ["Complex, Time Limit - 0"], "PassLimit_2.blend", 16, 64, 0.5, 1, 0, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_057", ["Complex, Time Limit - 10"], "PassLimit_2.blend", 16, 10000, 0.5, 1, 10, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_058", ["Complex, Time Limit - 50"], "PassLimit_2.blend", 16, 10000, 0.5, 1, 50, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_059", ["Complex, Time Limit - 100"], "PassLimit_2.blend", 16, 10000, 0.5, 1, 100, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_060", ["Complex, Time Limit - 500"], "PassLimit_2.blend", 16, 10000, 0.5, 1, 500, False, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_061", ["Tile rendering, 128x128, Center Spiral"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, True, 128, 128, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_062", ["Tile rendering, 256x256, Center Spiral"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, True, 256, 256, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_063", ["Tile rendering, 512x512, Center Spiral"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, True, 512, 512, 'CENTER_SPIRAL'],
	   ["BL28_RS_AS_064", ["Tile rendering, 128x128, Vertical"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, True, 128, 128, 'VERTICAL'],
	   ["BL28_RS_AS_065", ["Tile rendering, 256x256, Vertical"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, True, 256, 256, 'VERTICAL'],
	   ["BL28_RS_AS_066", ["Tile rendering, 512x512, Vertical"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, True, 512, 512, 'VERTICAL'],
	   ["BL28_RS_AS_067", ["Tile rendering, 128x128, Horizontal"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, True, 128, 128, 'HORIZONTAL'],
	   ["BL28_RS_AS_068", ["Tile rendering, 256x256, Horizontal"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, True, 256, 256, 'HORIZONTAL'],
	   ["BL28_RS_AS_069", ["Tile rendering, 512x512, Horizontal"], "ComplexTestUber.blend", 16, 64, 0.05, 1, 0, True, 512, 512, 'HORIZONTAL']
	]

	launch_tests()
