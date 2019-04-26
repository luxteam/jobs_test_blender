
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	# check rpr addon
	if not addon_utils.check("rprblender")[0]:
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.context.scene.render.engine = "RPR"

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.context.scene.rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.context.scene.render.image_settings.file_format = 'JPEG'

	if {resolution_x} and {resolution_y}:
		bpy.context.scene.render.resolution_x = {resolution_x}
		bpy.context.scene.render.resolution_y = {resolution_y}

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

