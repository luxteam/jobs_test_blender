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

	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)

	if test_list[3] == "bilateral":
		return test_bilateral(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7], test_list[8])
	elif test_list[3] == "lwr":    
		return test_lwr(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6])
	elif test_list[3] == "eaw":
		return test_eaw(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7])
	else: # ML
		set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
		render(test_list[0], test_list[1])
		return 1
		

def test_bilateral(test_case, script_info, radius, color_sigma, normal_sigma, p_sigma, trans_sigma):
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	set_value(view_layer.rpr.denoiser, 'radius', radius)
	set_value(view_layer.rpr.denoiser, 'color_sigma', color_sigma)
	set_value(view_layer.rpr.denoiser, 'normal_sigma', normal_sigma)
	set_value(view_layer.rpr.denoiser, 'p_sigma', p_sigma)
	set_value(view_layer.rpr.denoiser, 'trans_sigma', trans_sigma)

	render(test_case, script_info)
	return 1

def test_eaw(test_case, script_info, color_sigma, normal_sigma, depth_sigma, trans_sigma):
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'color_sigma', color_sigma)
	set_value(view_layer.rpr.denoiser, 'normal_sigma', normal_sigma)
	set_value(view_layer.rpr.denoiser, 'depth_sigma', depth_sigma)
	set_value(view_layer.rpr.denoiser, 'trans_sigma', trans_sigma)

	render(test_case, script_info)
	return 1

def test_lwr(test_case, script_info, samples, half_window, bandwidth):
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'samples', samples)
	set_value(view_layer.rpr.denoiser, 'half_window', half_window)
	set_value(view_layer.rpr.denoiser, 'bandwidth', bandwidth)

	render(test_case, script_info)
	return 1

if __name__ == "__main__":

	list_tests = [
	# Bilateral
	["BL28_RS_DEN_001", ["Bilateral default"], "Candle.blend", "bilateral", 1, 0.75, 0.01, 0.10, 0.01],
	["BL28_RS_DEN_002", ["Bilateral", "Radius 5"], "Candle.blend", "bilateral", 5, 0.75, 0.01, 0.10, 0.01],
	["BL28_RS_DEN_003", ["Bilateral", "Radius 10"], "Candle.blend", "bilateral", 10, 0.75, 0.01, 0.10, 0.01],
	["BL28_RS_DEN_004", ["Bilateral", "Radius 5", "Color sigma 0.2"], "Candle.blend", "bilateral", 5, 0.2, 0.01, 0.10, 0.01],
	["BL28_RS_DEN_005", ["Bilateral", "Radius 5", "Normal sigma 0.5"], "Candle.blend", "bilateral", 5, 0.75, 0.5, 0.10, 0.01],
	["BL28_RS_DEN_006", ["Bilateral", "Radius 5", "Color sigma 0.5"], "Candle.blend", "bilateral", 5, 0.5, 0.01, 0.10, 0.01],
	["BL28_RS_DEN_007", ["Bilateral", "Radius 5", "ID sigma 0.5"], "Candle.blend", "bilateral", 5, 0.75, 0.01, 0.10, 0.5],
	["BL28_RS_DEN_008", ["Bilateral", "Radius 5", "All sigma's 0.5"], "Candle.blend", "bilateral", 5, 0.5, 0.5, 0.5, 0.5],
	["BL28_RS_DEN_009", ["Bilateral", "Radius 5", "All sigma's 1"], "Candle.blend", "bilateral", 5, 1, 1, 1, 1],
	# LWR
	["BL28_RS_DEN_010", ["LWR default"], "Candle.blend", "lwr", 4, 4, 0.1],
	["BL28_RS_DEN_011", ["LWR", "Samples 1"], "Candle.blend", "lwr", 1, 4, 0.1],
	["BL28_RS_DEN_012", ["LWR", "Samples 5"], "Candle.blend", "lwr", 5, 4, 0.1],
	["BL28_RS_DEN_013", ["LWR", "Samples 10"], "Candle.blend", "lwr", 10, 4, 0.1],
	["BL28_RS_DEN_014", ["LWR", "Samples 5", "Filter radius 1"], "Candle.blend", "lwr", 5, 1, 0.1],
	["BL28_RS_DEN_015", ["LWR", "Samples 5", "Filter radius 5"], "Candle.blend", "lwr", 5, 5, 0.1],
	["BL28_RS_DEN_016", ["LWR", "Samples 5", "Filter radius 10"], "Candle.blend", "lwr", 5, 10, 0.1],
	["BL28_RS_DEN_017", ["LWR", "Samples 5", "Bandwidth 0.5"], "Candle.blend", "lwr", 5, 4, 0.5],
	["BL28_RS_DEN_018", ["LWR", "Samples 5", "Bandwidth 1"], "Candle.blend", "lwr", 5, 4, 1],
	["BL28_RS_DEN_019", ["LWR", "Samples 1", "Filter radius 1", "Bandwidth 0"], "Candle.blend", "lwr", 1, 1, 0],
	["BL28_RS_DEN_020", ["LWR", "Samples 5", "Filter radius 5", "Bandwidth 0.5"], "Candle.blend", "lwr", 5, 5, 0.5],
	["BL28_RS_DEN_021", ["LWR", "Samples 10", "Filter radius 10", "Bandwidth 1"], "Candle.blend", "lwr", 10, 10, 1],
	# EAW
	["BL28_RS_DEN_022", ["EAW default"], "Candle.blend", "eaw", 0.75, 0.01, 0.01, 0.01],
	["BL28_RS_DEN_023", ["EAW", "Color sigma 0.2"], "Candle.blend", "eaw", 0.2, 0.01, 0.01, 0.01],
	["BL28_RS_DEN_024", ["EAW", "Normal sigma 0.2"], "Candle.blend", "eaw", 0.75, 0.2, 0.01, 0.01],
	["BL28_RS_DEN_025", ["EAW", "Color sigma 0.5"], "Candle.blend", "eaw", 0.5, 0.01, 0.01, 0.01],
	["BL28_RS_DEN_026", ["EAW", "ID sigma 0.5"], "Candle.blend", "eaw", 0.75, 0.01, 0.01, 0.5],
	["BL28_RS_DEN_027", ["EAW", "Color sigma 0.5", "Normal sigma 0.5", "Depth sigma 0.5", "ID sigma 0.5"], "Candle.blend", "eaw", 0.5, 0.5, 0.5, 0.5],
	["BL28_RS_DEN_028", ["EAW", "Color sigma 1", "Normal sigma 1", "Depth sigma 1", "ID sigma 1"], "Candle.blend", "eaw", 1, 1, 1, 1],
	# ML
	["BL28_RS_DEN_029", ["Machine learning"], "Candle.blend", "ml"],
	]

	launch_tests()
