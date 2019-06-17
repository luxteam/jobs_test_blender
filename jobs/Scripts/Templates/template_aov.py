
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.view_layers["RenderLayer"], 'use', True)
	set_value(scene.render, 'use_single_layer', False)
	set_value(scene, 'use_nodes', True)
	nodes = bpy.data.scenes[0].node_tree.nodes

	file_output = nodes["File Output"]
	file_output.base_path = r"{work_dir}" + "/Color"

	render_layer = nodes["Render Layers"]

	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr, 'enable_aovs[{{}}]'.format(test_list[4]), True)

	link = scene.node_tree.links.new(render_layer.outputs[test_list[3]], file_output.inputs[test_list[4]])

	render(test_list[0], test_list[1])

	scene.node_tree.links.remove(link)
	set_value(view_layer.rpr, 'enable_aovs[{{}}]'.format(test_list[4]), False)

	os.remove(r"{work_dir}" + "/Color/" + test_list[0] + '.jpg')
	os.rename(r"{work_dir}" + "/Color/" + test_list[0] + '0001.jpg', \
		r"{work_dir}" + "/Color/" + test_list[0] + '.jpg')

	return 1
	
if __name__ == "__main__":

	list_tests = [
		["BL28_RS_AOV_001", ["AOV: Combined"], "AOV_test.blend", 'Image', 0], 
		["BL28_RS_AOV_002", ["AOV: Depth"], "AOV_test.blend", 'Depth', 1], 
		["BL28_RS_AOV_003", ["AOV: UV"], "AOV_test.blend", 'UV', 2], 
		["BL28_RS_AOV_004", ["AOV: Object Index"], "AOV_test.blend", 'Object Index', 3], 
		["BL28_RS_AOV_005", ["AOV: Material Index"], "AOV_test.blend", 'Material Index', 4], 
		["BL28_RS_AOV_006", ["AOV: World Coordinate"], "AOV_test.blend", 'World Coordinate', 5],
		["BL28_RS_AOV_007", ["AOV: Geometric Normal"], "AOV_test.blend", 'Geometric Normal', 6], 
		["BL28_RS_AOV_008", ["AOV: Shading Normal"], "AOV_test.blend", 'Shading Normal', 7], 
		["BL28_RS_AOV_009", ["AOV: Group Index"], "AOV_test.blend", 'Group Index', 8],
		["BL28_RS_AOV_010", ["AOV: Shadow Catcher"], "AOV_test.blend", 'Shadow Catcher', 9], 
		["BL28_RS_AOV_011", ["AOV: Background"], "AOV_test.blend", 'Background', 10], 
		["BL28_RS_AOV_012", ["AOV: Emission"], "AOV_test.blend", 'Emission', 11],
		["BL28_RS_AOV_013", ["AOV: Velocity"], "AOV_test.blend", 'Velocity', 12], 
		["BL28_RS_AOV_014", ["AOV: Direct Illumination"], "AOV_test.blend", 'Direct Illumination', 13], 
		["BL28_RS_AOV_015", ["AOV: Indirect Illumination"], "AOV_test.blend", 'Indirect Illumination', 14],
		["BL28_RS_AOV_016", ["AOV: Ambient Occlusion"], "AOV_test.blend", 'Ambient Occlusion', 15], 
		["BL28_RS_AOV_017", ["AOV: Direct Diffuse"], "AOV_test.blend", 'Direct Diffuse', 16], 
		["BL28_RS_AOV_018", ["AOV: Direct Reflection"], "AOV_test.blend", 'Direct Reflect', 17], 
		["BL28_RS_AOV_019", ["AOV: Indirect Diffuse"], "AOV_test.blend", 'Indirect Diffuse', 18], 
		["BL28_RS_AOV_020", ["AOV: Indirect Reflection"], "AOV_test.blend", 'Indirect Reflect', 19], 
		["BL28_RS_AOV_021", ["AOV: Refraction"], "AOV_test.blend", 'Refraction', 20],
		["BL28_RS_AOV_022", ["AOV: Volume"], "AOV_test.blend", 'Volume', 21], 
		["BL28_RS_AOV_023", ["AOV: Opacity"], "AOV_test.blend", 'Opacity', 22],
		["BL28_RS_AOV_024", ["AOV: Environment Lighting"], "AOV_test.blend", 'Environment Lighting', 23],
		["BL28_RS_AOV_025", ["AOV: Key Lighting"], "AOV_test.blend", 'Key Lighting', 24],
		["BL28_RS_AOV_026", ["AOV: Fill Lighting"], "AOV_test.blend", 'Fill Lighting', 25],
		["BL28_RS_AOV_027", ["AOV: Emissive Lighting"], "AOV_test.blend", 'Emissive Lighting', 26],
		["BL28_RS_AOV_028", ["AOV: Color Variance"], "AOV_test.blend", 'Color Variance', 27]
	]

	launch_tests()
