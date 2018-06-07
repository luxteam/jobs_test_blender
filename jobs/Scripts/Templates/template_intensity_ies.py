def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	if (bpy.path.basename(bpy.context.blend_data.filepath) == "IESintensity.blend"):
		
		bpy.data.lamps["Lamp.001"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "1.ies")
+		bpy.data.lamps["Lamp.002"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "2.ies")
+		bpy.data.lamps["Lamp.003"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "3.ies")
+		bpy.data.lamps["Lamp.004"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "4.ies")
+		bpy.data.lamps["Lamp.005"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "5.ies")
+		bpy.data.lamps["Lamp.006"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "6.ies")
+		bpy.data.lamps["Lamp.007"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "7.ies")
+		bpy.data.lamps["Lamp.008"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , "8.ies")
		
		render(test_list[0], test_list[1])
		return 2


if __name__ == "__main__":
	
	list_tests = [
	['BL_L_INTLT_001', ["Testing intensity with 8 IES"], "IESintensity.blend"]
	]

	launch_tests()

