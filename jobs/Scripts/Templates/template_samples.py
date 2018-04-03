
def main(iteration):

	
	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = iteration
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	render(iteration)

if __name__ == "__main__":

	iterations = [1, 100, 500, 1000, 5000, 10000] 
	for each in iterations:
		main(each)


