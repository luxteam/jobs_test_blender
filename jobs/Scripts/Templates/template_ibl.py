
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	Scenename = bpy.context.scene.name

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = test_list[3]
	bpy.context.scene.world.rpr_data.environment.ibl.intensity = test_list[4]

	if (test_list[3] == 'IBL'):
		bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
		ibl_map = os.path.join("{res_path}", test_list[5])
		bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_IBL_001", ["Type: Color", "Intensity: 0"], "ComplexTestUber.blend", 'COLOR', 0, 'None'], 
	["BL_RS_IBL_002", ["Type: Color", "Intensity: 1"], "ComplexTestUber.blend", 'COLOR', 1, 'None'],
	["BL_RS_IBL_003", ["Type: Color", "Intensity: 2"], "ComplexTestUber.blend", 'COLOR', 2, 'None'],
	["BL_RS_IBL_004", ["Type: Color", "Intensity: 3"], "ComplexTestUber.blend", 'COLOR', 3, 'None'],
	["BL_RS_IBL_005", ["Type: Color", "Intensity: 5"], "ComplexTestUber.blend", 'COLOR', 5, 'None'],
	["BL_RS_IBL_006", ["Type: Color", "Intensity: 7"], "ComplexTestUber.blend", 'COLOR', 7, 'None'],
	["BL_RS_IBL_007", ["Type: Color", "Intensity: 10"], "ComplexTestUber.blend", 'COLOR', 10, 'None'],
	["BL_RS_IBL_008", ["Type: IBL with hdr map", "Intensity: 0"], "ComplexTestUber.blend", 'IBL', 0, 'Tropical_Beach_3k.hdr'],
	["BL_RS_IBL_009", ["Type: IBL with hdr map", "Intensity: 1"], "ComplexTestUber.blend", 'IBL', 1, 'Tropical_Beach_3k.hdr'],
	["BL_RS_IBL_010", ["Type: IBL with hdr map", "Intensity: 2"], "ComplexTestUber.blend", 'IBL', 2, 'Tropical_Beach_3k.hdr'],
	["BL_RS_IBL_011", ["Type: IBL with hdr map", "Intensity: 3"], "ComplexTestUber.blend", 'IBL', 3, 'Tropical_Beach_3k.hdr'],
	["BL_RS_IBL_012", ["Type: IBL with hdr map", "Intensity: 5"], "ComplexTestUber.blend", 'IBL', 5, 'Tropical_Beach_3k.hdr'],
	["BL_RS_IBL_013", ["Type: IBL with hdr map", "Intensity: 7"], "ComplexTestUber.blend", 'IBL', 7, 'Tropical_Beach_3k.hdr'],
	["BL_RS_IBL_014", ["Type: IBL with hdr map", "Intensity: 10"], "ComplexTestUber.blend", 'IBL', 10, 'Tropical_Beach_3k.hdr'],
	["BL_RS_IBL_015", ["Type: IBL with exr map", "Intensity: 0"], "ComplexTestUber.blend", 'IBL', 0, 'ibl_test.exr'],
	["BL_RS_IBL_016", ["Type: IBL with exr map", "Intensity: 1"], "ComplexTestUber.blend", 'IBL', 1, 'ibl_test.exr'],
	["BL_RS_IBL_017", ["Type: IBL with exr map", "Intensity: 2"], "ComplexTestUber.blend", 'IBL', 2, 'ibl_test.exr'],
	["BL_RS_IBL_018", ["Type: IBL with exr map", "Intensity: 3"], "ComplexTestUber.blend", 'IBL', 3, 'ibl_test.exr'],
	["BL_RS_IBL_019", ["Type: IBL with exr map", "Intensity: 5"], "ComplexTestUber.blend", 'IBL', 5, 'ibl_test.exr'],
	["BL_RS_IBL_020", ["Type: IBL with exr map", "Intensity: 7"], "ComplexTestUber.blend", 'IBL', 7, 'ibl_test.exr'],
	["BL_RS_IBL_021", ["Type: IBL with exr map", "Intensity: 10"], "ComplexTestUber.blend", 'IBL', 10, 'ibl_test.exr']
	]

	launch_tests()



