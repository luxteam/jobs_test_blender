
def prerender(test_list):

	Scenename = bpy.context.scene.name

	if Scenename != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.use_nodes = True
	nodes = bpy.data.scenes[0].node_tree.nodes

	file_output = nodes["File Output"]
	file_output.base_path = r"{work_dir}" + "/Color"
	#file_output.file_slots[0].path = test_list[0]

	render_layer = nodes["Render Layers"]
	bpy.context.scene.node_tree.links.new(render_layer.outputs[test_list[3]], file_output.inputs[test_list[4]])

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[test_list[4]] = True
	render(test_list[0], test_list[1])
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[test_list[4]] = False
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[0] = True

	os.remove(r"{work_dir}" + "/Color/" + test_list[0] + '.jpg')
	os.rename(r"{work_dir}" + "/Color/" + test_list[0] + '0001.jpg', \
		r"{work_dir}" + "/Color/" + test_list[0] + '.jpg')

	return 1
	
if __name__ == "__main__":

	list_tests = [
	["BL_RS_AOV_001", ["AOV: Combined"], "AOV_test.blend", 'Image', 0], 
	["BL_RS_AOV_002", ["AOV: Depth"], "AOV_test.blend", 'Depth', 1], 
	["BL_RS_AOV_003", ["AOV: UV"], "AOV_test.blend", 'UV', 2], 
	["BL_RS_AOV_004", ["AOV: Object Index"], "AOV_test.blend", 'Object Index', 3], 
	["BL_RS_AOV_005", ["AOV: Material Index"], "AOV_test.blend", 'Material Index', 4], 
	["BL_RS_AOV_006", ["AOV: World Coordinate"], "AOV_test.blend", 'World Coordinate', 5],
	["BL_RS_AOV_007", ["AOV: Geometric Normal"], "AOV_test.blend", 'Geometric Normal', 6], 
	["BL_RS_AOV_008", ["AOV: Shading Normal"], "AOV_test.blend", 'Shading Normal', 7], 
	["BL_RS_AOV_009", ["AOV: Group Index"], "AOV_test.blend", 'Group Index', 8],
	["BL_RS_AOV_010", ["AOV: Shadow Catcher"], "AOV_test.blend", 'Shadow Catcher', 9], 
	["BL_RS_AOV_011", ["AOV: Background"], "AOV_test.blend", 'Background', 10], 
	["BL_RS_AOV_012", ["AOV: Emission"], "AOV_test.blend", 'Emission', 11],
	# ["BL_RS_AOV_013", ["AOV: Velocity"], "AOV_test.blend", 'Velocity', 12], 
	["BL_RS_AOV_014", ["AOV: Direct Illumination"], "AOV_test.blend", 'Direct Illumination', 13], 
	["BL_RS_AOV_015", ["AOV: Indirect Illumination"], "AOV_test.blend", 'Indirect Illumination', 14],
	["BL_RS_AOV_016", ["AOV: Ambient Occlusion"], "AOV_test.blend", 'Ambient Occlusion', 15], 
	["BL_RS_AOV_017", ["AOV: Direct Diffuse"], "AOV_test.blend", 'Direct Diffuse', 16], 
	["BL_RS_AOV_018", ["AOV: Direct Reflection"], "AOV_test.blend", 'Direct Reflection', 17], 
	["BL_RS_AOV_019", ["AOV: Indirect Diffuse"], "AOV_test.blend", 'Indirect Diffuse', 18], 
	["BL_RS_AOV_020", ["AOV: Indirect Reflection"], "AOV_test.blend", 'Indirect Reflection', 19], 
	["BL_RS_AOV_021", ["AOV: Refraction"], "AOV_test.blend", 'Refraction', 20],
	["BL_RS_AOV_022", ["AOV: Volume"], "AOV_test.blend", 'Volume', 21], 
	["BL_RS_AOV_023", ["AOV: Opacity"], "AOV_test.blend", 'Opacity', 22]
	]

	launch_tests()
