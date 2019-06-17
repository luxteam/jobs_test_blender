
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.world.rpr, 'enabled', True)
	set_value(scene.world.rpr, 'mode', 'IBL')
	set_value(scene.world.rpr, 'intensity', test_list[3])

	if type(test_list[4]) == tuple:
		set_value(scene.world.rpr.ibl, 'color', test_list[4])
	else:
		bpy.ops.image.open(filepath="//Maps//ibl_test.exr", directory="{resource_path}//Maps//", files=[{{"name":"ibl_test.exr"}}], relative_path=True, show_multiview=False)
		set_value(scene.world.rpr.ibl, 'image', bpy.data.images['ibl_test.exr'])

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
		["BL28_RS_IBL_001", ["Intensity: 0"], "ComplexTestUber.blend", 0, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_002", ["Intensity: 1"], "ComplexTestUber.blend", 1, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_003", ["Intensity: 2"], "ComplexTestUber.blend", 2, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_004", ["Intensity: 3"], "ComplexTestUber.blend", 3, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_005", ["Intensity: 5"], "ComplexTestUber.blend", 5, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_006", ["Intensity: 7"], "ComplexTestUber.blend", 7, (0.5, 0.5, 0.5), None, None], 
		["BL28_RS_IBL_007", ["Intensity: 10"], "ComplexTestUber.blend", 10, (0.5, 0.5, 0.5), None, None]
	]

	launch_tests()



