
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.render, 'use_single_layer', True)
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["{{}}".format(test_list[3])])
	
	render(test_list[0], test_list[1])

	return 1

if __name__ == "__main__":

	list_tests = [
		["BL28_RS_RL_001", ["Render Layer: Decor"], "RenderLayer.blend", "Decor"], 
		["BL28_RS_RL_002", ["Render Layer: Chairs"], "RenderLayer.blend", "Chairs"],
		["BL28_RS_RL_003", ["Render Layer: Table"], "RenderLayer.blend", "Table"], 
		["BL28_RS_RL_004", ["Render Layer: Floor"], "RenderLayer.blend", "Floor"]
	]
	
	launch_tests()

