
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.world.rpr, 'enabled', True)
	set_value(scene.world.rpr, 'mode', 'IBL')
	set_value(scene.world.rpr, 'intensity', test_list[3])

	if type(test_list[4]) == tuple:
		set_value(scene.world.rpr.ibl, 'color', test_list[4])
	else:
		bpy.ops.image.open(filepath="//Maps//{{}}".format(test_list[4]), directory="{resource_path}//Maps//", files=[{{"name":"{{}}".format(test_list[4])}}], \
																															relative_path=True, show_multiview=False)
		set_value(scene.world.rpr.ibl, 'image', bpy.data.images['{{}}'.format(test_list[4])])

	if test_list[5]:
		set_value(scene.world.rpr, '{{}}_override'.format(test_list[5]), True)
		if type(test_list[6]) == tuple:
			set_value(scene.world.rpr, '{{}}_color'.format(test_list[5]), test_list[6])
		else:
			bpy.ops.image.open(filepath="//Maps//{{}}".format(test_list[6]), directory="{resource_path}//Maps//", files=[{{"name":"{{}}".format(test_list[6])}}], \
																															relative_path=True, show_multiview=False)
			set_value(scene.world.rpr, '{{}}_image'.format(test_list[5]), bpy.data.images['{{}}'.format(test_list[6])])


	render(test_list[0], test_list[1])

	if test_list[5]:
		set_value(scene.world.rpr, '{{}}_override'.format(test_list[5]), False)

	return 1

if __name__ == "__main__":

	list_tests = [
		["BL28_RS_IBL_001", ["Intensity: 0"], "ComplexTestUber.blend", 0, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_002", ["Intensity: 1"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_003", ["Intensity: 2"], "ComplexTestUber.blend", 2, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_004", ["Intensity: 3"], "ComplexTestUber.blend", 3, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_005", ["Intensity: 5"], "ComplexTestUber.blend", 5, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_006", ["Intensity: 7"], "ComplexTestUber.blend", 7, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_007", ["Intensity: 10"], "ComplexTestUber.blend", 10, (0.5, 0.5, 0.5), None, None],
		["BL28_RS_IBL_008", ["Intensity: 0", "HDR Map"], "ComplexTestUber.blend", 0, "1.hdr", None, None], 
		["BL28_RS_IBL_009", ["Intensity: 1", "HDR Map"], "ComplexTestUber.blend", 1, "1.hdr", None, None], 
		["BL28_RS_IBL_010", ["Intensity: 2", "HDR Map"], "ComplexTestUber.blend", 2, "1.hdr", None, None], 
		["BL28_RS_IBL_011", ["Intensity: 3", "HDR Map"], "ComplexTestUber.blend", 3, "1.hdr", None, None], 
		["BL28_RS_IBL_012", ["Intensity: 5", "HDR Map"], "ComplexTestUber.blend", 5, "1.hdr", None, None], 
		["BL28_RS_IBL_013", ["Intensity: 7", "HDR Map"], "ComplexTestUber.blend", 7, "1.hdr", None, None], 
		["BL28_RS_IBL_014", ["Intensity: 10", "HDR Map"], "ComplexTestUber.blend", 10, "1.hdr", None, None],
		["BL28_RS_IBL_015", ["Intensity: 0", "EXR Map"], "ComplexTestUber.blend", 0, "1.exr", None, None], 
		["BL28_RS_IBL_016", ["Intensity: 1", "EXR Map"], "ComplexTestUber.blend", 1, "1.exr", None, None], 
		["BL28_RS_IBL_017", ["Intensity: 2", "EXR Map"], "ComplexTestUber.blend", 2, "1.exr", None, None], 
		["BL28_RS_IBL_018", ["Intensity: 3", "EXR Map"], "ComplexTestUber.blend", 3, "1.exr", None, None], 
		["BL28_RS_IBL_019", ["Intensity: 5", "EXR Map"], "ComplexTestUber.blend", 5, "1.exr", None, None], 
		["BL28_RS_IBL_020", ["Intensity: 7", "EXR Map"], "ComplexTestUber.blend", 7, "1.exr", None, None], 
		["BL28_RS_IBL_021", ["Intensity: 10", "EXR Map"], "ComplexTestUber.blend", 10, "1.exr", None, None],
		["BL28_RS_IBL_022", ["Override Background Color"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "background", (0.5, 0.5, 0.5)],
		["BL28_RS_IBL_023", ["Override Background Map HDR"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "background", "1.hdr"],
		["BL28_RS_IBL_024", ["Override Background Map EXR"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "background", "1.exr"],
		["BL28_RS_IBL_025", ["Override Reflection Color"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "reflection", (0.5, 0.5, 0.5)],
		["BL28_RS_IBL_026", ["Override Reflection Map HDR"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "reflection", "1.hdr"],
		["BL28_RS_IBL_027", ["Override Reflection Map EXR"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "reflection", "1.exr"],
		["BL28_RS_IBL_028", ["Override Refraction Color"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "refraction", (0.5, 0.5, 0.5)],
		["BL28_RS_IBL_029", ["Override Refraction Map HDR"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "refraction", "1.hdr"],
		["BL28_RS_IBL_030", ["Override Refraction Map EXR"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "refraction", "1.exr"],
		["BL28_RS_IBL_031", ["Override Transparency Color"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "transparency", (0.5, 0.5, 0.5)],
		["BL28_RS_IBL_032", ["Override Transparency Map HDR"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "transparency", "1.hdr"],
		["BL28_RS_IBL_033", ["Override Transparency Map EXR"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), "transparency", "1.exr"],
	]

	launch_tests()


