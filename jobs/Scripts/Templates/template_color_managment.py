
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.rpr.limits, 'max_samples', {pass_limit})
	set_value(scene.render.image_settings, 'file_format', 'JPEG')

	if {resolution_x} and {resolution_y}:
		set_value(scene.render, 'resolution_x', {resolution_x})
		set_value(scene.render, 'resolution_y', {resolution_y})

	set_value(scene.display_settings, 'display_device', test_list[3])
	set_value(scene.view_settings, 'view_transform', test_list[4])
	set_value(scene.view_settings, 'look', test_list[5])
	set_value(scene.view_settings, 'exposure', test_list[6])
	set_value(scene.view_settings, 'gamma', test_list[7])
	set_value(scene.sequencer_colorspace_settings, 'name', test_list[8])

	render(test_list[0], test_list[1])
	return 1


if __name__ == "__main__":
	
	list_tests = [
	["BL28_RS_CM_001", ["sRGB Display Device"], "ComplexTestUber.blend", "sRGB", "Standard", "None", 0, 1, "sRGB"],
	# ["BL28_RS_CM_002", ["DCI-P3 Display Device"], "ComplexTestUber.blend", "DCI-P3", "Standard", "None", 0, 1, "sRGB"],
	["BL28_RS_CM_003", ["None Display Device"], "ComplexTestUber.blend", "None", "Standard", "None", 0, 1, "sRGB"],
	# ["BL28_RS_CM_004", ["Rec709 Display Device"], "ComplexTestUber.blend", "Rec709", "Standard", "None", 0, 1, "sRGB"],
	["BL28_RS_CM_005", ["XYZ Display Device"], "ComplexTestUber.blend", "XYZ", "Standard", "None", 0, 1, "sRGB"],
	["BL28_RS_CM_006", ["Defaut Display Space"], "ComplexTestUber.blend", "sRGB", "Standard", "None", 0, 1, "sRGB"],
	["BL28_RS_CM_007", ["Filmic Display Space"], "ComplexTestUber.blend", "sRGB", "Filmic", "None", 0, 1, "sRGB"],
	# ["BL28_RS_CM_008", ["RRT Display Space"], "ComplexTestUber.blend", "sRGB", "RRT", "None", 0, 1, "sRGB"],
	# ["BL28_RS_CM_009", ["Film Display Space"], "ComplexTestUber.blend", "sRGB", "Film", "None", 0, 1, "sRGB"],
	["BL28_RS_CM_010", ["Raw Display Space"], "ComplexTestUber.blend", "sRGB", "Raw", "None", 0, 1, "sRGB"],
	["BL28_RS_CM_011", ["Filmic Log Display Space"], "ComplexTestUber.blend", "sRGB", "Filmic Log", "None", 0, 1, "sRGB"],
	["BL28_RS_CM_012", ["False Color Display Space"], "ComplexTestUber.blend", "sRGB", "False Color", "None", 0, 1, "sRGB"],
	["BL28_RS_CM_013", ["Base Contrast Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "sRGB"],
	# ["BL28_RS_CM_014", ["Agfa Agfacolor Optima II 200 Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Agfa Agfacolor Optima II 200 Contrast", 0, 1, "sRGB"],
	# ["BL28_RS_CM_015", ["Agfa Agfacolor Optima II 100 Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Agfa Agfacolor Optima II 100 Contrast", 0, 1, "sRGB"],
	# ["BL28_RS_CM_016", ["Agfa Agfacolor HDC 200 Plus Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Agfa Agfacolor HDC 200 Plus Contrast", 0, 1, "sRGB"],
	# ["BL28_RS_CM_017", ["Agfa Agfacolor Futura II 200 Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Agfa Agfacolor Futura II 200 Contrast", 0, 1, "sRGB"],
	# ["BL28_RS_CM_018", ["Agfa Agfacolor Futura 200 Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Agfa Agfacolor Futura 200 Contrast", 0, 1, "sRGB"],
	["BL28_RS_CM_019", ["Very Low Contrast Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Very Low Contrast", 0, 1, "sRGB"],
	["BL28_RS_CM_020", ["Low Contrast Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Low Contrast", 0, 1, "sRGB"],
	["BL28_RS_CM_021", ["Medium Low Contrast Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Medium Low Contrast", 0, 1, "sRGB"],
	["BL28_RS_CM_022", ["Medium High Contrast Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Medium High Contrast", 0, 1, "sRGB"],
	["BL28_RS_CM_023", ["High Contrast Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - High Contrast", 0, 1, "sRGB"],
	["BL28_RS_CM_024", ["Very High Contrast Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Very High Contrast", 0, 1, "sRGB"],
	# ["BL28_RS_CM_025", ["Kodak Portra 160 NC Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Kodak Portra 160 NC Contrast", 0, 1, "sRGB"],
	# ["BL28_RS_CM_026", ["Kodak Max Zoom 800 Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Kodak Max Zoom 800 Contrast", 0, 1, "sRGB"],
	# ["BL28_RS_CM_027", ["Kodak Gold 200 Look"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Kodak Gold 200 Contrast", 0, 1, "sRGB"],
	["BL28_RS_CM_028", ["Explosure -32"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", -32, 1, "sRGB"],
	["BL28_RS_CM_029", ["Explosure -10"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", -10, 1, "sRGB"],
	["BL28_RS_CM_030", ["Explosure -5"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", -5, 1, "sRGB"],
	["BL28_RS_CM_031", ["Explosure -1"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", -1, 1, "sRGB"],
	["BL28_RS_CM_032", ["Explosure 0"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "sRGB"],
	["BL28_RS_CM_033", ["Explosure 1"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 1	, 1, "sRGB"],
	["BL28_RS_CM_034", ["Explosure 5"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 5, 1, "sRGB"],
	["BL28_RS_CM_035", ["Explosure 10"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 10, 1, "sRGB"],
	["BL28_RS_CM_036", ["Explosure 32"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 32, 1, "sRGB"],
	["BL28_RS_CM_037", ["Gamma 0"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 0, "sRGB"],
	["BL28_RS_CM_038", ["Gamma 1"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "sRGB"],
	["BL28_RS_CM_039", ["Gamma 2.2"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 2.2, "sRGB"],
	["BL28_RS_CM_040", ["Gamma 5"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 5, "sRGB"],
	["BL28_RS_CM_041", ["Filmic Log Color Space"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "Filmic Log"],
	["BL28_RS_CM_042", ["Linear Color Space"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "Linear"],
	["BL28_RS_CM_043", ["Linear ACES Color Space"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "Linear ACES"],
	["BL28_RS_CM_044", ["Non-Color Color Space"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "Non-Color"],
	["BL28_RS_CM_045", ["Raw Color Space"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "Raw"],
	["BL28_RS_CM_046", ["sRGB Color Space"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "sRGB"],
	# ["BL28_RS_CM_047", ["VD16 Color Space"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "VD16"],
	["BL28_RS_CM_048", ["XYZ Color Space"], "ComplexTestUber.blend", "sRGB", "Standard", "Standard - Base Contrast", 0, 1, "XYZ"]
	]

	launch_tests()
