
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.render, 'resolution_x', test_list[3])
	set_value(scene.render, 'resolution_y', test_list[4])
	set_value(scene.render, 'pixel_aspect_x', test_list[5])
	set_value(scene.render, 'pixel_aspect_y', test_list[6])
	set_value(scene.render, 'resolution_percentage', 100)

	render(test_list[0], test_list[1])

	return 1

if __name__ == "__main__":
	
	list_tests = [
	["BL28_RS_IS_001", ["Preset: 4K DCI 2160p"], "ComplexTestUber.blend", 4096, 2160, 1, 1], 
	["BL28_RS_IS_002", ["Preset: 4K UW 1600p"], "ComplexTestUber.blend", 3840, 1600, 1, 1],
	["BL28_RS_IS_003", ["Preset: 4k UHDTV 2160p"], "ComplexTestUber.blend", 3840, 2160, 1, 1], 
	["BL28_RS_IS_004", ["Preset: DVCPRO HD 1080p"], "ComplexTestUber.blend", 1280, 1080, 3, 2], 
	["BL28_RS_IS_005", ["Preset: DVCPRO HD 720p"], "ComplexTestUber.blend", 960, 720, 4, 3], 
	["BL28_RS_IS_006", ["Preset: HDTV 1080p"], "ComplexTestUber.blend", 1920, 1080, 1, 1],
	["BL28_RS_IS_007", ["Preset: HDTV 720p"], "ComplexTestUber.blend", 1280, 720, 1, 1], 
	["BL28_RS_IS_008", ["Preset: HDV 1080p"], "ComplexTestUber.blend", 1440, 1080, 4, 3],
	["BL28_RS_IS_009", ["Preset: HDV NTSC 1080p"], "ComplexTestUber.blend", 1440, 1080, 4, 3], 
	["BL28_RS_IS_010", ["Preset: HDV PAL 1080p"], "ComplexTestUber.blend", 1440, 1080, 4, 3],
	["BL28_RS_IS_011", ["Preset: TV NTSC 16:9"], "ComplexTestUber.blend", 720, 480, 40, 33], 
	["BL28_RS_IS_012", ["Preset: TV NTSC 4:3"], "ComplexTestUber.blend", 720, 486, 10, 11], 
	["BL28_RS_IS_013", ["Preset: TV PAL 16:9"], "ComplexTestUber.blend", 720, 576, 16, 11], 
	["BL28_RS_IS_014", ["Preset: TV PAL 4:3"], "ComplexTestUber.blend", 720, 576, 12, 11], 
	["BL28_RS_IS_015", ["Resolution: 2000x2000"], "ComplexTestUber.blend", 2000, 2000, 1, 1], 
	["BL28_RS_IS_016", ["Resolution: 3000x3000"], "ComplexTestUber.blend", 3000, 3000, 1, 1], 
	["BL28_RS_IS_017", ["Resolution: 4000x4000"], "ComplexTestUber.blend", 4000, 4000, 1, 1], 
	["BL28_RS_IS_018", ["Resolution: 5000x5000"], "ComplexTestUber.blend", 5000, 5000, 1, 1], 
	["BL28_RS_IS_019", ["Resolution: 6000x6000"], "ComplexTestUber.blend", 6000, 6000, 1, 1],
	["BL28_RS_IS_020", ["Resolution: 7000x7000"], "ComplexTestUber.blend", 7000, 7000, 1, 1], 
	["BL28_RS_IS_021", ["Resolution: 8000x8000"], "ComplexTestUber.blend", 8000, 8000, 1, 1],
	["BL28_RS_IS_022", ["Resolution: 2K"], "ComplexTestUber.blend", 2048, 1152, 1, 1], 
	["BL28_RS_IS_023", ["Resolution: 4K"], "ComplexTestUber.blend", 4096, 3204, 1, 1],
	["BL28_RS_IS_024", ["Resolution: 1500x1125"], "ComplexTestUber.blend", 1500, 1125, 1, 1]
	]
	
	launch_tests()
