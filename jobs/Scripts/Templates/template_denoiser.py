def aov_denoiser(denoiser, aov, test_case, script_info):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

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

def test_bilateral(radius, sigma, test_case, script_info):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.scene.rpr.render.denoiser.enable = True
	bpy.context.scene.rpr.render.denoiser.filter_type = "bilateral"

	bpy.context.scene.rpr.render.denoiser.color_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.normal_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.p_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.trans_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.radius = radius

	render(test_case, script_info)

def test_eaw(sigma, test_case, script_info):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.scene.rpr.render.denoiser.enable = True
	bpy.context.scene.rpr.render.denoiser.filter_type = 'eaw'

	bpy.context.scene.rpr.render.denoiser.color_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.normal_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.depth_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.trans_sigma = sigma

	render(test_case, script_info)

def test_lwr(param1, param2, test_case, script_info):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.scene.rpr.render.denoiser.enable = True
	bpy.context.scene.rpr.render.denoiser.filter_type = 'lwr'

	bpy.context.scene.rpr.render.denoiser.samples = param1
	bpy.context.scene.rpr.render.denoiser.half_window = param1
	bpy.context.scene.rpr.render.denoiser.bandwidth = param2

	render(test_case, script_info)

if __name__ == "__main__":

	test_bilateral(1, 0.1, "BL_RS_DEN_001", ["Filter type: Bilateral", "Radius: 1", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"])
	test_bilateral(25, 0.1, "BL_RS_DEN_002", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"])
	test_bilateral(50, 0.1, "BL_RS_DEN_003", ["Filter type: Bilateral", "Radius: 50", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"])
	test_bilateral(25, 0.5, "BL_RS_DEN_004", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 0.5", "Normal sigma: 0.5", "ID sigma: 0.5"])
	test_bilateral(25, 1.0, "BL_RS_DEN_005", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 1", "Normal sigma: 1", "ID sigma: 1"])

	test_lwr(4, 0.1, "BL_RS_DEN_006", ["Filter type: Local Weighted Regression", "Samples: 4", "Filter radius: 4", "Bandwidth: 0.1"])
	test_lwr(10, 10, "BL_RS_DEN_007", ["Filter type: Local Weighted Regression", "Samples: 10", "Filter radius: 10", "Bandwidth: 10"])
	test_lwr(1, 0, "BL_RS_DEN_008", ["Filter type: Local Weighted Regression", "Samples: 1.0", "Filter radius: 1.0", "Bandwidth: 0"])

	test_eaw(0.1, "BL_RS_DEN_009", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 0.1", "Normal sigma: 0.1", "Depth sigma: 0.1", "ID sigma: 0.1"])
	test_eaw(0.5, "BL_RS_DEN_010", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 0.5", "Normal sigma: 0.5", "Depth sigma: 0.5", "ID sigma: 0.5"])
	test_eaw(1.0, "BL_RS_DEN_011", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 1.0", "Normal sigma: 1.0", "Depth sigma: 1.0", "ID sigma: 1.0"])

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[1] = False

	main("bilateral", 0, "BL_RS_DEN_012", ["Filter type: Bilateral", "AOV: Combined"])
	main("bilateral", 1, "BL_RS_DEN_013", ["Filter type: Bilateral", "AOV: Depth"])
	main("bilateral", 2, "BL_RS_DEN_014", ["Filter type: Bilateral", "AOV: UV"])
	main("bilateral", 3, "BL_RS_DEN_015", ["Filter type: Bilateral", "AOV: Object Index"])
	main("bilateral", 4, "BL_RS_DEN_016", ["Filter type: Bilateral", "AOV: Material Index"])
	main("bilateral", 5, "BL_RS_DEN_017", ["Filter type: Bilateral", "AOV: World Coordinate"])
	main("bilateral", 6, "BL_RS_DEN_018", ["Filter type: Bilateral", "AOV: Geometric Normal"])
	main("bilateral", 7, "BL_RS_DEN_019", ["Filter type: Bilateral", "AOV: Shading Normal"])
	main("bilateral", 8, "BL_RS_DEN_020", ["Filter type: Bilateral", "AOV: Group Index"])
	main("bilateral", 9, "BL_RS_DEN_021", ["Filter type: Bilateral", "AOV: Shadow Catcher"])
	main("bilateral", 10, "BL_RS_DEN_022", ["Filter type: Bilateral", "AOV: Background"])
	main("bilateral", 11, "BL_RS_DEN_023", ["Filter type: Bilateral", "AOV: Emission"])
	main("bilateral", 12, "BL_RS_DEN_024", ["Filter type: Bilateral", "AOV: Velocity"])
	main("bilateral", 13, "BL_RS_DEN_025", ["Filter type: Bilateral", "AOV: Direct Illumination"])
	main("bilateral", 14, "BL_RS_DEN_026", ["Filter type: Bilateral", "AOV: Indirect Illumination"])
	main("bilateral", 15, "BL_RS_DEN_027", ["Filter type: Bilateral", "AOV: Ambient Occlusion"])
	main("bilateral", 16, "BL_RS_DEN_028", ["Filter type: Bilateral", "AOV: Direct Diffuse"])
	main("bilateral", 17, "BL_RS_DEN_029", ["Filter type: Bilateral", "AOV: Direct Reflection"])
	main("bilateral", 18, "BL_RS_DEN_030", ["Filter type: Bilateral", "AOV: Indirect Diffuse"])
	main("bilateral", 19, "BL_RS_DEN_031", ["Filter type: Bilateral", "AOV: Indirect Reflection"])
	main("bilateral", 20, "BL_RS_DEN_032", ["Filter type: Bilateral", "AOV: Refraction"])
	main("bilateral", 21, "BL_RS_DEN_033", ["Filter type: Bilateral", "AOV: Volume"])
	main("bilateral", 22, "BL_RS_DEN_034", ["Filter type: Bilateral", "AOV: Opacity"])

	main("lwr", 0, "BL_RS_DEN_035", ["Filter type: Local Weighted Regression", "AOV: Combined"])
	main("lwr", 1, "BL_RS_DEN_036", ["Filter type: Local Weighted Regression", "AOV: Depth"])
	main("lwr", 2, "BL_RS_DEN_037", ["Filter type: Local Weighted Regression", "AOV: UV"])
	main("lwr", 3, "BL_RS_DEN_038", ["Filter type: Local Weighted Regression", "AOV: Object Index"])
	main("lwr", 4, "BL_RS_DEN_039", ["Filter type: Local Weighted Regression", "AOV: Material Index"])
	main("lwr", 5, "BL_RS_DEN_040", ["Filter type: Local Weighted Regression", "AOV: World Coordinate"])
	main("lwr", 6, "BL_RS_DEN_041", ["Filter type: Local Weighted Regression", "AOV: Geometric Normal"])
	main("lwr", 7, "BL_RS_DEN_042", ["Filter type: Local Weighted Regression", "AOV: Shading Normal"])
	main("lwr", 8, "BL_RS_DEN_043", ["Filter type: Local Weighted Regression", "AOV: Group Index"])
	main("lwr", 9, "BL_RS_DEN_044", ["Filter type: Local Weighted Regression", "AOV: Shadow Catcher"])
	main("lwr", 10, "BL_RS_DEN_045", ["Filter type: Local Weighted Regression", "AOV: Background"])
	main("lwr", 11, "BL_RS_DEN_046", ["Filter type: Local Weighted Regression", "AOV: Emission"])
	main("lwr", 12, "BL_RS_DEN_047", ["Filter type: Local Weighted Regression", "AOV: Velocity"])
	main("lwr", 13, "BL_RS_DEN_048", ["Filter type: Local Weighted Regression", "AOV: Direct Illumination"])
	main("lwr", 14, "BL_RS_DEN_049", ["Filter type: Local Weighted Regression", "AOV: Indirect Illumination"])
	main("lwr", 15, "BL_RS_DEN_050", ["Filter type: Local Weighted Regression", "AOV: Ambient Occlusion"])
	main("lwr", 16, "BL_RS_DEN_051", ["Filter type: Local Weighted Regression", "AOV: Direct Diffuse"])
	main("lwr", 17, "BL_RS_DEN_052", ["Filter type: Local Weighted Regression", "AOV: Direct Reflection"])
	main("lwr", 18, "BL_RS_DEN_053", ["Filter type: Local Weighted Regression", "AOV: Indirect Diffuse"])
	main("lwr", 19, "BL_RS_DEN_054", ["Filter type: Local Weighted Regression", "AOV: Indirect Reflection"])
	main("lwr", 20, "BL_RS_DEN_055", ["Filter type: Local Weighted Regression", "AOV: Refraction"])
	main("lwr", 21, "BL_RS_DEN_056", ["Filter type: Local Weighted Regression", "AOV: Volume"])
	main("lwr", 22, "BL_RS_DEN_057", ["Filter type: Local Weighted Regression", "AOV: Opacity"])

	main("eaw", 0, "BL_RS_DEN_058", ["Filter type: Edge Avoiding Wavelets", "AOV: Combined"])
	main("eaw", 1, "BL_RS_DEN_059", ["Filter type: Edge Avoiding Wavelets", "AOV: Depth"])
	main("eaw", 2, "BL_RS_DEN_060", ["Filter type: Edge Avoiding Wavelets", "AOV: UV"])
	main("eaw", 3, "BL_RS_DEN_061", ["Filter type: Edge Avoiding Wavelets", "AOV: Object Index"])
	main("eaw", 4, "BL_RS_DEN_062", ["Filter type: Edge Avoiding Wavelets", "AOV: Material Index"])
	main("eaw", 5, "BL_RS_DEN_063", ["Filter type: Edge Avoiding Wavelets", "AOV: World Coordinate"])
	main("eaw", 6, "BL_RS_DEN_064", ["Filter type: Edge Avoiding Wavelets", "AOV: Geometric Normal"])
	main("eaw", 7, "BL_RS_DEN_065", ["Filter type: Edge Avoiding Wavelets", "AOV: Shading Normal"])
	main("eaw", 8, "BL_RS_DEN_066", ["Filter type: Edge Avoiding Wavelets", "AOV: Group Index"])
	main("eaw", 9, "BL_RS_DEN_067", ["Filter type: Edge Avoiding Wavelets", "AOV: Shadow Catcher"])
	main("eaw", 10, "BL_RS_DEN_068", ["Filter type: Edge Avoiding Wavelets", "AOV: Background"])
	main("eaw", 11, "BL_RS_DEN_069", ["Filter type: Edge Avoiding Wavelets", "AOV: Emission"])
	main("eaw", 12, "BL_RS_DEN_070", ["Filter type: Edge Avoiding Wavelets", "AOV: Velocity"])
	main("eaw", 13, "BL_RS_DEN_071", ["Filter type: Edge Avoiding Wavelets", "AOV: Direct Illumination"])
	main("eaw", 14, "BL_RS_DEN_072", ["Filter type: Edge Avoiding Wavelets", "AOV: Indirect Illumination"])
	main("eaw", 15, "BL_RS_DEN_073", ["Filter type: Edge Avoiding Wavelets", "AOV: Ambient Occlusion"])
	main("eaw", 16, "BL_RS_DEN_074", ["Filter type: Edge Avoiding Wavelets", "AOV: Direct Diffuse"])
	main("eaw", 17, "BL_RS_DEN_075", ["Filter type: Edge Avoiding Wavelets", "AOV: Direct Reflection"])
	main("eaw", 18, "BL_RS_DEN_076", ["Filter type: Edge Avoiding Wavelets", "AOV: Indirect Diffuse"])
	main("eaw", 19, "BL_RS_DEN_077", ["Filter type: Edge Avoiding Wavelets", "AOV: Indirect Reflection"])
	main("eaw", 20, "BL_RS_DEN_078", ["Filter type: Edge Avoiding Wavelets", "AOV: Refraction"])
	main("eaw", 21, "BL_RS_DEN_079", ["Filter type: Edge Avoiding Wavelets", "AOV: Volume"])
	main("eaw", 22, "BL_RS_DEN_080", ["Filter type: Edge Avoiding Wavelets", "AOV: Opacity"])

		
		
		







