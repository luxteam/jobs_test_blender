def aov_denoiser(denoiser, aov, test_case):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

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
	render(test_case)
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[aov] = False

def test_bilateral(radius, sigma, test_case):

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

	render(test_case)

def test_eaw(sigma, test_case):

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

	render(test_case)

def test_lwr(param1, param2, test_case):

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

	render(test_case)

if __name__ == "__main__":

	test_bilateral(1, 0.1, "BL_RS_DEN_001")
	test_bilateral(25, 0.1, "BL_RS_DEN_002")
	test_bilateral(50, 0.1, "BL_RS_DEN_003")
	test_bilateral(25, 0.5, "BL_RS_DEN_004")
	test_bilateral(25, 1.0, "BL_RS_DEN_005")

	test_lwr(4, 0.1, "BL_RS_DEN_006")
	test_lwr(10, 10, "BL_RS_DEN_007")
	test_lwr(1, 0, "BL_RS_DEN_008")

	test_eaw(0.1, "BL_RS_DEN_009")
	test_eaw(0.5, "BL_RS_DEN_010")
	test_eaw(1.0, "BL_RS_DEN_011")

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[1] = False

	for aov in range(23):
		aov_denoiser("bilateral", aov, "BL_RS_DEN_0" + str(aov + 12))
	for aov in range(23):
		aov_denoiser("lwr", aov, "BL_RS_DEN_0" + str(aov + 35))
	for aov in range(23):
		aov_denoiser("eaw", aov, "BL_RS_DEN_0" + str(aov + 58))
		
		
		







