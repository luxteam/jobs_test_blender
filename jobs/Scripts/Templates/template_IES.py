
def main(IES_file, test_case, script_info):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.object.data.type = 'POINT'
	bpy.data.lamps["Lamp"].rpr_lamp.intensity = 50
	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , IES_file)

	render(test_case, script_info)

if __name__ == "__main__":
	
	main("1.ies", "BL_L_IES_001", ["IES file: 1.ies", "Intensity: 50"])
	main("2.ies", "BL_L_IES_002", ["IES file: 2.ies", "Intensity: 50"])
	main("3.ies", "BL_L_IES_003", ["IES file: 3.ies", "Intensity: 50"])
	main("4.ies", "BL_L_IES_004", ["IES file: 4.ies", "Intensity: 50"])
	main("5.ies", "BL_L_IES_005", ["IES file: 5.ies", "Intensity: 50"])
	main("6.ies", "BL_L_IES_006", ["IES file: 6.ies", "Intensity: 50"])
	main("7.ies", "BL_L_IES_007", ["IES file: 7.ies", "Intensity: 50"])
	main("8.ies", "BL_L_IES_008", ["IES file: 8.ies", "Intensity: 50"])
	main("9.ies", "BL_L_IES_009", ["IES file: 9.ies", "Intensity: 50"])
	main("10.ies", "BL_L_IES_010", ["IES file: 10.ies", "Intensity: 50"])


