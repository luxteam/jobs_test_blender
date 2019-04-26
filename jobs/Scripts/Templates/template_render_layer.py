
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.rpr.limits, 'max_samples', {pass_limit})
	set_value(scene.render.image_settings, 'file_format', 'JPEG')

	if {resolution_x} and {resolution_y}:
		set_value(scene.render, 'resolution_x', {resolution_x})
		set_value(scene.render, 'resolution_y', {resolution_y})

	# Default disable
	bpy.context.scene.render.layers["Floor"].layers[4] = True
	bpy.context.scene.render.layers["Floor"].layers[0] = False
	bpy.context.scene.render.layers["Floor"].layers[1] = False
	bpy.context.scene.render.layers["Floor"].layers[2] = False
	bpy.context.scene.render.layers["Floor"].layers[3] = False
	
	# enable layer
	bpy.context.scene.render.layers["Floor"].layers[test_list[3]] = True
	bpy.context.scene.render.layers["Floor"].layers[4] = False

	render(test_list[0], test_list[1])

	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_RL_001", ["Render Layer: Decor"], "RenderLayer.blend", 3], 
	["BL_RS_RL_002", ["Render Layer: Chairs"], "RenderLayer.blend", 2],
	["BL_RS_RL_003", ["Render Layer: Table"], "RenderLayer.blend", 1], 
	["BL_RS_RL_004", ["Render Layer: Floor"], "RenderLayer.blend", 0], 
	]
	
	launch_tests()

