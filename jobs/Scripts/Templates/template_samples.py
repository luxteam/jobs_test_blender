
def main(iteration, test_case):

	
	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = iteration
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	render(test_case)

if __name__ == "__main__":

	iterations = [1, 100, 500, 1000, 5000, 10000] 
	for each in range(len(iterations)):
		main(iterations[each], "BL_RS_PS_00" + str(each+1))


