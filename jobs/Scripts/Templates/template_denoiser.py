def aov_denoiser(denoiser, aov):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.scene.rpr.render.denoiser.filter_type = denoiser
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[aov] = True
	render(aov)
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[aov] = False

def test_bilateral(radius, sigma):

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

	render("bilateral", radius, sigma)

def test_eaw(sigma):

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

	render("eaw", sigma)

def test_lwr(param1, param2):

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

	render("lwr", param1, param1, param2)

if __name__ == "__main__":

	test_bilateral(1, 0.1)
	test_bilateral(25, 0.1)
	test_bilateral(50, 0.1)
	test_bilateral(25, 0.5)
	test_bilateral(25, 1.0)

	test_eaw(0.1)
	test_eaw(0.5)
	test_eaw(1.0)

	test_lwr(4, 0.1)
	test_lwr(10, 10)
	test_lwr(1, 0)

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[1] = False

	for aov in range(23):
		aov_denoiser("eaw", aov)
		aov_denoiser("lwr", aov)
		aov_denoiser("bilateral", aov)







