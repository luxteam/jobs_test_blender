def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.data.lamps["Point.001"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "1.ies")
	bpy.data.lamps["Point.002"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "2.ies")
	bpy.data.lamps["Point.003"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "3.ies")
	bpy.data.lamps["Point.004"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "4.ies")
	bpy.data.lamps["Point.005"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "5.ies")
	bpy.data.lamps["Point.006"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "6.ies")
	bpy.data.lamps["Point.007"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "7.ies")
	bpy.data.lamps["Point"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "8.ies")
	
	render(test_list[0], test_list[1])
	return 1


if __name__ == "__main__":
	
	list_tests = [
	['BL_L_INTLT_001', ["Testing intensity with 8 IES"], "IESintensity.blend"]
	]

	launch_tests()

