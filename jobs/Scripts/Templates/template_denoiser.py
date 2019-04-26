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
		return test_bilateral(test_list[0], test_list[1], test_list[4], test_list[5])
	elif test_list[3] == "lwr":    
		return test_lwr(test_list[0], test_list[1], test_list[4], test_list[5])
	elif test_list[3] == "eaw":
		return test_eaw(test_list[0], test_list[1], test_list[4])
	else: # ML
		set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
		render(test_list[0], test_list[1])
		return 1
		

def test_bilateral(test_case, script_info, radius, sigma, view_layer):

	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')

	set_value(view_layer.rpr.denoiser, 'color_sigma', sigma)
	set_value(view_layer.rpr.denoiser, 'normal_sigma', sigma)
	set_value(view_layer.rpr.denoiser, 'p_sigma', sigma)
	set_value(view_layer.rpr.denoiser, 'trans_sigma', sigma)
	set_value(view_layer.rpr.denoiser, 'radius', radius)

	render(test_case, script_info)
	return 1

def test_eaw(test_case, script_info, sigma, view_layer):

	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')

	set_value(view_layer.rpr.denoiser, 'color_sigma', sigma)
	set_value(view_layer.rpr.denoiser, 'normal_sigma', sigma)
	set_value(view_layer.rpr.denoiser, 'depth_sigma', sigma)
	set_value(view_layer.rpr.denoiser, 'trans_sigma', sigma)

	render(test_case, script_info)
	return 1

def test_lwr(test_case, script_info, param1, param2, view_layer):

	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')

	set_value(view_layer.rpr.denoiser, 'samples', param1)
	set_value(view_layer.rpr.denoiser, 'half_window', param1)
	set_value(view_layer.rpr.denoiser, 'bandwidth', param2)

	render(test_case, script_info)
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_DEN_001", ["Filter type: Bilateral", "Radius: 1", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"], "Candle.blend", "bilateral", 1, 0.1],
	["BL_RS_DEN_002", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"], "Candle.blend", "bilateral", 25, 0.1],
	["BL_RS_DEN_003", ["Filter type: Bilateral", "Radius: 50", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"], "Candle.blend", "bilateral", 50, 0.1],
	["BL_RS_DEN_004", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 0.5", "Normal sigma: 0.5", "ID sigma: 0.5"], "Candle.blend", "bilateral", 25, 0.5],
	["BL_RS_DEN_005", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 1", "Normal sigma: 1", "ID sigma: 1"], "Candle.blend", "bilateral", 25, 1.0],
	["BL_RS_DEN_006", ["Filter type: Local Weighted Regression", "Samples: 4", "Filter radius: 4", "Bandwidth: 0.1"], "Candle.blend", "lwr", 4, 0.1],
	["BL_RS_DEN_007", ["Filter type: Local Weighted Regression", "Samples: 10", "Filter radius: 10", "Bandwidth: 10"], "Candle.blend", "lwr", 10, 10 ],
	["BL_RS_DEN_008", ["Filter type: Local Weighted Regression", "Samples: 1.0", "Filter radius: 1.0", "Bandwidth: 1"], "Candle.blend", "lwr", 2, 1],
	["BL_RS_DEN_009", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 0.1", "Normal sigma: 0.1", "Depth sigma: 0.1", "ID sigma: 0.1"], "Candle.blend", "eaw", 0.1],
	["BL_RS_DEN_010", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 0.5", "Normal sigma: 0.5", "Depth sigma: 0.5", "ID sigma: 0.5"], "Candle.blend", "eaw", 0.5],
	["BL_RS_DEN_011", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 1.0", "Normal sigma: 1.0", "Depth sigma: 1.0", "ID sigma: 1.0"], "Candle.blend", "eaw", 1.0]
	]

	launch_tests()
