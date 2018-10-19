
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.object.data.type = 'POINT'
	bpy.data.lamps["Lamp"].rpr_lamp.intensity = 50
	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , test_list[3])

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":
	
	list_tests = [
	["BL_L_IES_001", ["IES file: 1.ies", "Intensity: 50"], "IES.blend", "1.ies"], 
	["BL_L_IES_002", ["IES file: 2.ies", "Intensity: 50"], "IES.blend", "2.ies"],
	["BL_L_IES_003", ["IES file: 3.ies", "Intensity: 50"], "IES.blend", "3.ies"], 
	["BL_L_IES_004", ["IES file: 4.ies", "Intensity: 50"], "IES.blend", "4.ies"], 
	["BL_L_IES_005", ["IES file: 5.ies", "Intensity: 50"], "IES.blend", "5.ies"], 
	["BL_L_IES_006", ["IES file: 6.ies", "Intensity: 50"], "IES.blend", "6.ies"],
	["BL_L_IES_007", ["IES file: 7.ies", "Intensity: 50"], "IES.blend", "7.ies"], 
	["BL_L_IES_008", ["IES file: 8.ies", "Intensity: 50"], "IES.blend", "8.ies"], 
	["BL_L_IES_009", ["IES file: 9.ies", "Intensity: 50"], "IES.blend", "9.ies"], 
	["BL_L_IES_010", ["IES file: 10.ies", "Intensity: 50"], "IES.blend", "10.ies"]
	]
	
	launch_tests()


