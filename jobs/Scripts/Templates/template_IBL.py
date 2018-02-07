
def main(test_combination):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = test_combination[0]
	bpy.context.scene.world.rpr_data.environment.ibl.intensity = test_combination[1]
	if (test_combination[0] == 'IBL'):
		bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
		bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(r"C:\TestResources\BlenderAssets\scenes\ibl_test.exr", True)

	render(test_combination[0], test_combination[1])

if __name__ == "__main__":

	values = [0, 1, 2, 3, 5, 7, 10]
	IBL_types = ['COLOR', 'IBL']

	test_combinations = [(ibl_type, value) for ibl_type in IBL_types for value in values]
	for each in test_combinations:
		main(each)

