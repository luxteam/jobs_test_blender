
def main(test_combination):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.data.scenes[Scenename].rpr.render.aa.filter = test_combination[0]
	bpy.data.scenes[Scenename].rpr.render.aa.radius = test_combination[1]

	render(test_combination[0], test_combination[1])

if __name__ == "__main__":

	values = [0, 1.5, 5, 10]
	filters = ['MITCHELL', 'LANCZOS','TRIANGLE', 'BOX', 'GAUSSIAN', 'BLACKMANHARRIS']

	test_combinations = [ (aa_filter, value) for aa_filter in filters for value in values]
	for each in test_combinations:
		main(each)


