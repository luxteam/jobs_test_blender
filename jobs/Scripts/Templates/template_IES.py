
def main(IES_file, test_case):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.object.data.type = 'POINT'
	bpy.data.lamps["Lamp"].rpr_lamp.intensity = 50
	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , IES_file)

	render(test_case)

if __name__ == "__main__":
	
	for each_ies in range(1,11):
		if each_ies < 10:
			main(str(each_ies) + ".ies", "BL_L_IES_00" + str(each_ies))
		else:
			main(str(each_ies) + ".ies", "BL_L_IES_0" + str(each_ies))



