def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	if test_list[2] == "non_linear":
		bpy.context.scene.rpr.render.tone_mapping.nonlinear.burn = test_list[3]
		bpy.context.scene.rpr.render.tone_mapping.nonlinear.prescale = test_list[4]
		bpy.context.scene.rpr.render.tone_mapping.nonlinear.postscale = test_list[5]
	elif test_list[2] == "linear":
		bpy.context.scene.rpr.render.tone_mapping.linear.iso = test_list[3]
		bpy.context.scene.rpr.render.tone_mapping.linear.f_stop = test_list[4]
		bpy.context.scene.rpr.render.tone_mapping.linear.shutter_speed = test_list[5]
	elif test_list[2] == "simplified":
		bpy.context.scene.rpr.render.tone_mapping.simplified.exposure = test_list[3]
		bpy.context.scene.rpr.render.tone_mapping.simplified.contrast = test_list[4]


	if (bpy.path.basename(bpy.context.blend_data.filepath) == "ComplexTestUber.blend"):
		render(test_list[0], test_list[1])
		if (test_list[0] == "BL_RS_TM_012"):
			return 2
		else: 
			return 1
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsCoat.blend"):
		render(test_list[0], test_list[1])
		if (test_list[0] == "BL_RS_TM_024"):
			return 2
		else: 
			return 1
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsEmissive.blend"):
		render(test_list[0], test_list[1])
		if (test_list[0] == "BL_RS_TM_036"):
			return 2
		else: 
			return 1
	elif (bpy.path.basename(bpy.context.blend_data.filepath) == "TestBallsReflect.blend"):
		render(test_list[0], test_list[1])
		if (test_list[0] == "BL_RS_TM_048"):
			return 2
		else: 
			return 1

if __name__ == "__main__":
	
	list_tests = [
	['BL_RS_TM_001', ["Type: Non Linear, Burn: 10, Pre Scale: 0.1, Post Scale: 1.0"], "non_linear", 10, 0.1, 1.0],
	['BL_RS_TM_002', ["Type: Non Linear, Burn: 0, Pre Scale: 0, Post Scale: 0"], "non_linear", 0, 0, 0],
	['BL_RS_TM_003', ["Type: Non Linear, Burn: 5, Pre Scale: 5, Post Scale: 5"], "non_linear", 5, 5, 5],
	['BL_RS_TM_004', ["Type: Non Linear, Burn: 10, Pre Scale: 10, Post Scale: 10"], "non_linear", 10, 10, 10],
	['BL_RS_TM_005', ["Type: Linear, ISO: 100, F-Stop: 4.0, Shutter Speed: 1.0"], "linear", 100, 4, 1],
	['BL_RS_TM_006', ["Type: Linear, ISO: 0, F-Stop: 0, Shutter Speed: 0"], "linear", 0, 0, 0],
	['BL_RS_TM_007', ["Type: Linear, ISO: 5, F-Stop: 5, Shutter Speed: 5"], "linear", 5, 5, 5],
	['BL_RS_TM_008', ["Type: Linear, ISO: 10, F-Stop: 10, Shutter Speed: 10"], "linear", 10, 10, 10],
	['BL_RS_TM_009', ["Type: Simplified, Exposure: 0, Contrast: 1.0"], "simplified", 0, 1.0],
	['BL_RS_TM_010', ["Type: Simplified, Exposure: 0, Contrast: 0"], "simplified", 0, 0],
	['BL_RS_TM_011', ["Type: Simplified, Exposure: 5, Contrast: 5"], "simplified", 5, 5],
	['BL_RS_TM_012', ["Type: Simplified, Exposure: 10, Contrast: 10"], "simplified", 10, 10],

	['BL_RS_TM_013', ["Type: Non Linear, Burn: 10, Pre Scale: 0.1, Post Scale: 1.0"], "non_linear", 10, 0.1, 1.0],
	['BL_RS_TM_014', ["Type: Non Linear, Burn: 0, Pre Scale: 0, Post Scale: 0"], "non_linear", 0, 0, 0],
	['BL_RS_TM_015', ["Type: Non Linear, Burn: 5, Pre Scale: 5, Post Scale: 5"], "non_linear", 5, 5, 5],
	['BL_RS_TM_016', ["Type: Non Linear, Burn: 10, Pre Scale: 10, Post Scale: 10"], "non_linear", 10, 10, 10],
	['BL_RS_TM_017', ["Type: Linear, ISO: 100, F-Stop: 4.0, Shutter Speed: 1.0"], "linear", 100, 4, 1],
	['BL_RS_TM_018', ["Type: Linear, ISO: 0, F-Stop: 0, Shutter Speed: 0"], "linear", 0, 0, 0],
	['BL_RS_TM_019', ["Type: Linear, ISO: 5, F-Stop: 5, Shutter Speed: 5"], "linear", 5, 5, 5],
	['BL_RS_TM_020', ["Type: Linear, ISO: 10, F-Stop: 10, Shutter Speed: 10"], "linear", 10, 10, 10],
	['BL_RS_TM_021', ["Type: Simplified, Exposure: 0, Contrast: 1.0"], "simplified", 0, 1.0],
	['BL_RS_TM_022', ["Type: Simplified, Exposure: 0, Contrast: 0"], "simplified", 0, 0],
	['BL_RS_TM_023', ["Type: Simplified, Exposure: 5, Contrast: 5"], "simplified", 5, 5],
	['BL_RS_TM_024', ["Type: Simplified, Exposure: 10, Contrast: 10"], "simplified", 10, 10],

	['BL_RS_TM_025', ["Type: Non Linear, Burn: 10, Pre Scale: 0.1, Post Scale: 1.0"], "non_linear", 10, 0.1, 1.0],
	['BL_RS_TM_026', ["Type: Non Linear, Burn: 0, Pre Scale: 0, Post Scale: 0"], "non_linear", 0, 0, 0],
	['BL_RS_TM_027', ["Type: Non Linear, Burn: 5, Pre Scale: 5, Post Scale: 5"], "non_linear", 5, 5, 5],
	['BL_RS_TM_028', ["Type: Non Linear, Burn: 10, Pre Scale: 10, Post Scale: 10"], "non_linear", 10, 10, 10],
	['BL_RS_TM_029', ["Type: Linear, ISO: 100, F-Stop: 4.0, Shutter Speed: 1.0"], "linear", 100, 4, 1],
	['BL_RS_TM_030', ["Type: Linear, ISO: 0, F-Stop: 0, Shutter Speed: 0"], "linear", 0, 0, 0],
	['BL_RS_TM_031', ["Type: Linear, ISO: 5, F-Stop: 5, Shutter Speed: 5"], "linear", 5, 5, 5],
	['BL_RS_TM_032', ["Type: Linear, ISO: 10, F-Stop: 10, Shutter Speed: 10"], "linear", 10, 10, 10],
	['BL_RS_TM_033', ["Type: Simplified, Exposure: 0, Contrast: 1.0"], "simplified", 0, 1.0],
	['BL_RS_TM_034', ["Type: Simplified, Exposure: 0, Contrast: 0"], "simplified", 0, 0],
	['BL_RS_TM_035', ["Type: Simplified, Exposure: 5, Contrast: 5"], "simplified", 5, 5],
	['BL_RS_TM_036', ["Type: Simplified, Exposure: 10, Contrast: 10"], "simplified", 10, 10],

	['BL_RS_TM_037', ["Type: Non Linear, Burn: 10, Pre Scale: 0.1, Post Scale: 1.0"], "non_linear", 10, 0.1, 1.0],
	['BL_RS_TM_038', ["Type: Non Linear, Burn: 0, Pre Scale: 0, Post Scale: 0"], "non_linear", 0, 0, 0],
	['BL_RS_TM_039', ["Type: Non Linear, Burn: 5, Pre Scale: 5, Post Scale: 5"], "non_linear", 5, 5, 5],
	['BL_RS_TM_040', ["Type: Non Linear, Burn: 10, Pre Scale: 10, Post Scale: 10"], "non_linear", 10, 10, 10],
	['BL_RS_TM_041', ["Type: Linear, ISO: 100, F-Stop: 4.0, Shutter Speed: 1.0"], "linear", 100, 4, 1],
	['BL_RS_TM_042', ["Type: Linear, ISO: 0, F-Stop: 0, Shutter Speed: 0"], "linear", 0, 0, 0],
	['BL_RS_TM_043', ["Type: Linear, ISO: 5, F-Stop: 5, Shutter Speed: 5"], "linear", 5, 5, 5],
	['BL_RS_TM_044', ["Type: Linear, ISO: 10, F-Stop: 10, Shutter Speed: 10"], "linear", 10, 10, 10],
	['BL_RS_TM_045', ["Type: Simplified, Exposure: 0, Contrast: 1.0"], "simplified", 0, 1.0],
	['BL_RS_TM_046', ["Type: Simplified, Exposure: 0, Contrast: 0"], "simplified", 0, 0],
	['BL_RS_TM_047', ["Type: Simplified, Exposure: 5, Contrast: 5"], "simplified", 5, 5],
	['BL_RS_TM_048', ["Type: Simplified, Exposure: 10, Contrast: 10"], "simplified", 10, 10]
	]

	launch_tests()

