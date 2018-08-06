def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "Candle.fbm" , "PD6R12ED010- PDM6835-694SNB.ies")
	bpy.context.scene.rpr.render.denoiser.enable = True

	if (test_list[2] == "bilateral" and test_list[3] == -1):
		return test_bilateral(test_list[0], test_list[1], test_list[4], test_list[5])

	elif (test_list[2] == "lwr" and test_list[3] == -1):    
		return test_lwr(test_list[0], test_list[1], test_list[4], test_list[5])

	elif (test_list[2] == "eaw" and test_list[3] == -1):
		return test_eaw(test_list[0], test_list[1], test_list[4])

	elif (test_list[3] != -1):
		return test_aov_denoiser(test_list[0], test_list[1], test_list[2], test_list[3])

def test_aov_denoiser(test_case, script_info, denoiser, aov):
	
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[1] = False
	
	bpy.context.scene.rpr.render.denoiser.filter_type = denoiser

	if (denoiser == "bilateral"):
		bpy.context.scene.rpr.render.denoiser.color_sigma = 0.1
		bpy.context.scene.rpr.render.denoiser.normal_sigma = 0.1
		bpy.context.scene.rpr.render.denoiser.p_sigma = 0.1
		bpy.context.scene.rpr.render.denoiser.trans_sigma = 0.1
		bpy.context.scene.rpr.render.denoiser.radius = 5
	elif (denoiser == "lwr"):
		bpy.context.scene.rpr.render.denoiser.samples = 4
		bpy.context.scene.rpr.render.denoiser.half_window = 4
		bpy.context.scene.rpr.render.denoiser.bandwidth = 0.1
	elif (denoiser == "eaw"):
		bpy.context.scene.rpr.render.denoiser.color_sigma = 0.1
		bpy.context.scene.rpr.render.denoiser.normal_sigma = 0.1
		bpy.context.scene.rpr.render.denoiser.depth_sigma = 0.1
		bpy.context.scene.rpr.render.denoiser.trans_sigma = 0.1
	
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[aov] = True
	render(test_case, script_info)
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[aov] = False
	return 1

def test_bilateral(test_case, script_info, radius, sigma):

	bpy.context.scene.rpr.render.denoiser.filter_type = "bilateral"

	bpy.context.scene.rpr.render.denoiser.color_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.normal_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.p_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.trans_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.radius = radius

	render(test_case, script_info)
	return 1

def test_eaw(test_case, script_info, sigma):

	bpy.context.scene.rpr.render.denoiser.filter_type = 'eaw'

	bpy.context.scene.rpr.render.denoiser.color_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.normal_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.depth_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.trans_sigma = sigma

	render(test_case, script_info)
	return 1

def test_lwr(test_case, script_info, param1, param2):

	bpy.context.scene.rpr.render.denoiser.filter_type = 'lwr'

	bpy.context.scene.rpr.render.denoiser.samples = param1
	bpy.context.scene.rpr.render.denoiser.half_window = param1
	bpy.context.scene.rpr.render.denoiser.bandwidth = param2

	render(test_case, script_info)
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_DEN_001", ["Filter type: Bilateral", "Radius: 1", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"], "bilateral", -1, 1, 0.1],
	["BL_RS_DEN_002", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"], "bilateral", -1, 25, 0.1],
	["BL_RS_DEN_003", ["Filter type: Bilateral", "Radius: 50", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"], "bilateral", -1, 50, 0.1],
	["BL_RS_DEN_004", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 0.5", "Normal sigma: 0.5", "ID sigma: 0.5"], "bilateral", -1, 25, 0.5],
	["BL_RS_DEN_005", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 1", "Normal sigma: 1", "ID sigma: 1"], "bilateral", -1, 25, 1.0],
	["BL_RS_DEN_006", ["Filter type: Local Weighted Regression", "Samples: 4", "Filter radius: 4", "Bandwidth: 0.1"], "lwr", -1, 4, 0.1],
	["BL_RS_DEN_007", ["Filter type: Local Weighted Regression", "Samples: 10", "Filter radius: 10", "Bandwidth: 10"], "lwr", -1, 10, 10 ],
	["BL_RS_DEN_008", ["Filter type: Local Weighted Regression", "Samples: 1.0", "Filter radius: 1.0", "Bandwidth: 0"], "lwr", -1, 1, 0],
	["BL_RS_DEN_009", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 0.1", "Normal sigma: 0.1", "Depth sigma: 0.1", "ID sigma: 0.1"], "eaw", -1, 0.1],
	["BL_RS_DEN_010", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 0.5", "Normal sigma: 0.5", "Depth sigma: 0.5", "ID sigma: 0.5"], "eaw", -1, 0.5],
	["BL_RS_DEN_011", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 1.0", "Normal sigma: 1.0", "Depth sigma: 1.0", "ID sigma: 1.0"], "eaw", -1, 1.0],
	["BL_RS_DEN_012", ["Filter type: Bilateral", "AOV: Combined"], "bilateral", 0],
	["BL_RS_DEN_013", ["Filter type: Bilateral", "AOV: Depth"], "bilateral", 1],
	["BL_RS_DEN_014", ["Filter type: Bilateral", "AOV: UV"], "bilateral", 2],
	["BL_RS_DEN_015", ["Filter type: Bilateral", "AOV: Object Index"], "bilateral", 3 ],
	["BL_RS_DEN_016", ["Filter type: Bilateral", "AOV: Material Index"], "bilateral", 4],
	["BL_RS_DEN_017", ["Filter type: Bilateral", "AOV: World Coordinate"], "bilateral", 5],
	["BL_RS_DEN_018", ["Filter type: Bilateral", "AOV: Geometric Normal"], "bilateral", 6],
	["BL_RS_DEN_019", ["Filter type: Bilateral", "AOV: Shading Normal"], "bilateral", 7],
	["BL_RS_DEN_020", ["Filter type: Bilateral", "AOV: Group Index"], "bilateral", 8],
	["BL_RS_DEN_021", ["Filter type: Bilateral", "AOV: Shadow Catcher"], "bilateral", 9],
	["BL_RS_DEN_022", ["Filter type: Bilateral", "AOV: Background"], "bilateral", 10],
	["BL_RS_DEN_023", ["Filter type: Bilateral", "AOV: Emission"], "bilateral", 11],
	["BL_RS_DEN_024", ["Filter type: Bilateral", "AOV: Velocity"], "bilateral", 12],
	["BL_RS_DEN_025", ["Filter type: Bilateral", "AOV: Direct Illumination"], "bilateral", 13],
	["BL_RS_DEN_026", ["Filter type: Bilateral", "AOV: Indirect Illumination"], "bilateral", 14],
	["BL_RS_DEN_027", ["Filter type: Bilateral", "AOV: Ambient Occlusion"], "bilateral", 15],
	["BL_RS_DEN_028", ["Filter type: Bilateral", "AOV: Direct Diffuse"], "bilateral", 16],
	["BL_RS_DEN_029", ["Filter type: Bilateral", "AOV: Direct Reflection"], "bilateral", 17],
	["BL_RS_DEN_030", ["Filter type: Bilateral", "AOV: Indirect Diffuse"], "bilateral", 18],
	["BL_RS_DEN_031", ["Filter type: Bilateral", "AOV: Indirect Reflection"], "bilateral", 19],
	["BL_RS_DEN_032", ["Filter type: Bilateral", "AOV: Refraction"], "bilateral", 20],
	["BL_RS_DEN_033", ["Filter type: Bilateral", "AOV: Volume"], "bilateral", 21],
	["BL_RS_DEN_034", ["Filter type: Bilateral", "AOV: Opacity"], "bilateral", 22],
	["BL_RS_DEN_035", ["Filter type: Local Weighted Regression", "AOV: Combined"], "lwr", 0],
	["BL_RS_DEN_036", ["Filter type: Local Weighted Regression", "AOV: Depth"], "lwr", 1],
	["BL_RS_DEN_037", ["Filter type: Local Weighted Regression", "AOV: UV"], "lwr", 2],
	["BL_RS_DEN_038", ["Filter type: Local Weighted Regression", "AOV: Object Index"], "lwr", 3],
	["BL_RS_DEN_039", ["Filter type: Local Weighted Regression", "AOV: Material Index"], "lwr", 4],
	["BL_RS_DEN_040", ["Filter type: Local Weighted Regression", "AOV: World Coordinate"], "lwr", 5],
	["BL_RS_DEN_041", ["Filter type: Local Weighted Regression", "AOV: Geometric Normal"], "lwr", 6],
	["BL_RS_DEN_042", ["Filter type: Local Weighted Regression", "AOV: Shading Normal"], "lwr", 7],
	["BL_RS_DEN_043", ["Filter type: Local Weighted Regression", "AOV: Group Index"], "lwr", 8],
	["BL_RS_DEN_044", ["Filter type: Local Weighted Regression", "AOV: Shadow Catcher"], "lwr", 9],
	["BL_RS_DEN_045", ["Filter type: Local Weighted Regression", "AOV: Background"], "lwr", 10],
	["BL_RS_DEN_046", ["Filter type: Local Weighted Regression", "AOV: Emission"], "lwr", 11],
	["BL_RS_DEN_047", ["Filter type: Local Weighted Regression", "AOV: Velocity"], "lwr", 12],
	["BL_RS_DEN_048", ["Filter type: Local Weighted Regression", "AOV: Direct Illumination"], "lwr", 13],
	["BL_RS_DEN_049", ["Filter type: Local Weighted Regression", "AOV: Indirect Illumination"], "lwr", 14],
	["BL_RS_DEN_050", ["Filter type: Local Weighted Regression", "AOV: Ambient Occlusion"], "lwr", 15],
	["BL_RS_DEN_051", ["Filter type: Local Weighted Regression", "AOV: Direct Diffuse"], "lwr", 16],
	["BL_RS_DEN_052", ["Filter type: Local Weighted Regression", "AOV: Direct Reflection"], "lwr", 17],
	["BL_RS_DEN_053", ["Filter type: Local Weighted Regression", "AOV: Indirect Diffuse"], "lwr", 18],
	["BL_RS_DEN_054", ["Filter type: Local Weighted Regression", "AOV: Indirect Reflection"], "lwr", 19],
	["BL_RS_DEN_055", ["Filter type: Local Weighted Regression", "AOV: Refraction"], "lwr", 20],
	["BL_RS_DEN_056", ["Filter type: Local Weighted Regression", "AOV: Volume"], "lwr", 21],
	["BL_RS_DEN_057", ["Filter type: Local Weighted Regression", "AOV: Opacity"], "lwr", 22],
	["BL_RS_DEN_058", ["Filter type: Edge Avoiding Wavelets", "AOV: Combined"], "eaw", 0],
	["BL_RS_DEN_059", ["Filter type: Edge Avoiding Wavelets", "AOV: Depth"], "eaw", 1],
	["BL_RS_DEN_060", ["Filter type: Edge Avoiding Wavelets", "AOV: UV"], "eaw", 2],
	["BL_RS_DEN_061", ["Filter type: Edge Avoiding Wavelets", "AOV: Object Index"], "eaw", 3],
	["BL_RS_DEN_062", ["Filter type: Edge Avoiding Wavelets", "AOV: Material Index"], "eaw", 4],
	["BL_RS_DEN_063", ["Filter type: Edge Avoiding Wavelets", "AOV: World Coordinate"], "eaw", 5],
	["BL_RS_DEN_064", ["Filter type: Edge Avoiding Wavelets", "AOV: Geometric Normal"], "eaw", 6],
	["BL_RS_DEN_065", ["Filter type: Edge Avoiding Wavelets", "AOV: Shading Normal"], "eaw", 7],
	["BL_RS_DEN_066", ["Filter type: Edge Avoiding Wavelets", "AOV: Group Index"], "eaw", 8],
	["BL_RS_DEN_067", ["Filter type: Edge Avoiding Wavelets", "AOV: Shadow Catcher"], "eaw", 9],
	["BL_RS_DEN_068", ["Filter type: Edge Avoiding Wavelets", "AOV: Background"], "eaw", 10],
	["BL_RS_DEN_069", ["Filter type: Edge Avoiding Wavelets", "AOV: Emission"], "eaw", 11],
	["BL_RS_DEN_070", ["Filter type: Edge Avoiding Wavelets", "AOV: Velocity"], "eaw", 12],
	["BL_RS_DEN_071", ["Filter type: Edge Avoiding Wavelets", "AOV: Direct Illumination"], "eaw", 13],
	["BL_RS_DEN_072", ["Filter type: Edge Avoiding Wavelets", "AOV: Indirect Illumination"], "eaw", 14],
	["BL_RS_DEN_073", ["Filter type: Edge Avoiding Wavelets", "AOV: Ambient Occlusion"], "eaw", 15],
	["BL_RS_DEN_074", ["Filter type: Edge Avoiding Wavelets", "AOV: Direct Diffuse"], "eaw", 16],
	["BL_RS_DEN_075", ["Filter type: Edge Avoiding Wavelets", "AOV: Direct Reflection"], "eaw", 17],
	["BL_RS_DEN_076", ["Filter type: Edge Avoiding Wavelets", "AOV: Indirect Diffuse"], "eaw", 18],
	["BL_RS_DEN_077", ["Filter type: Edge Avoiding Wavelets", "AOV: Indirect Reflection"], "eaw", 19],
	["BL_RS_DEN_078", ["Filter type: Edge Avoiding Wavelets", "AOV: Refraction"], "eaw", 20],
	["BL_RS_DEN_079", ["Filter type: Edge Avoiding Wavelets", "AOV: Volume"], "eaw", 21],
	["BL_RS_DEN_080", ["Filter type: Edge Avoiding Wavelets", "AOV: Opacity"], "eaw", 22]
	]

	launch_tests()
