

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
	
	# make changes
	test_list[2]()
	# render
	render(test_list[0], test_list[1])
	# undo changes
	test_list[3]()			

	return 1


def already_default():
	pass


def set_layer(number):

	bpy.context.scene.render.layers["RenderLayer"].layers[19] = True
	bpy.context.scene.layers[19] = True
	for i in range(19):
		bpy.context.scene.render.layers["RenderLayer"].layers[i] = False
		bpy.context.scene.layers[i] = False
	
	bpy.context.scene.render.layers["RenderLayer"].layers[number] = True
	bpy.context.scene.layers[number] = True

	bpy.context.scene.render.layers["RenderLayer"].layers[19] = False
	bpy.context.scene.layers[19] = False


def get_material_and_node(material_name, node_name):
	material = [e for e in bpy.data.materials if e.name == material_name][0]
	node = [n for n in material.node_tree.nodes if n.name==node_name][0]
	return material, node


def node_001():
	set_layer(0)

# create connection from weight map to RPR Blend mat. For cases 1-3.
def cancel_002_004():
	material, node = get_material_and_node("RPRBlend", "RPR Shader Blend")
	tree = material.node_tree
	node_imagemap = [n for n in material.node_tree.nodes if n.name=="RPR Image Map"][0]
	tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node.inputs[node.weight_in])

def node_002():
	set_layer(0)
	material, node = get_material_and_node("RPRBlend", "RPR Shader Blend")
	node_imagemap = [n for n in material.node_tree.nodes if n.name=="RPR Image Map"][0]
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])

def node_003():
	set_layer(0)
	material, node = get_material_and_node("RPRBlend", "RPR Shader Blend")
	node_imagemap = [n for n in material.node_tree.nodes if n.name=="RPR Image Map"][0]
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	node.inputs[node.weight_in].default_value = 0

def node_004():
	set_layer(0)
	material, node = get_material_and_node("RPRBlend", "RPR Shader Blend")
	node_imagemap = [n for n in material.node_tree.nodes if n.name=="RPR Image Map"][0]
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	node.inputs[node.weight_in].default_value = 1

def node_005():
	set_layer(1)

def cancel_006():
	set_layer(1)
	material, node = get_material_and_node("RPRDot", "RPR Texture Mapping")
	node.inputs[node.scale_in].default_value = (3, 3)

def node_006():
	set_layer(1)
	material, node = get_material_and_node("RPRDot", "RPR Texture Mapping")
	node.inputs[node.scale_in].default_value = (1, 1)

def node_007():
	set_layer(2)

def cancel_008_009():
	set_layer(2)
	material, node = get_material_and_node("RPRGradient", "RPR Gradient")
	node.inputs[node.color1_in].default_value = (0.03, 0.162, 1, 1)
	node.inputs[node.color2_in].default_value = (1, 0, 0.497, 1)

def node_008():
	set_layer(2)
	material, node = get_material_and_node("RPRGradient", "RPR Gradient")
	node.inputs[node.color1_in].default_value = (0, 0, 0, 1)
	node.inputs[node.color2_in].default_value = (1, 1, 1, 1)

def node_009():
	set_layer(2)
	material, node = get_material_and_node("RPRGradient", "RPR Gradient")
	node.inputs[node.color1_in].default_value = (0, 0, 1, 1)
	node.inputs[node.color2_in].default_value = (1, 0, 0, 1)

def cancel_010_012():
	set_layer(2)
	material, node = get_material_and_node("RPRValueBlend", "RPR Value Blend")
	node.type = 'color'
	node.inputs[node.value1_in].default_value = (1, 0.007, 0.807, 1)
	node.inputs[node.value2_in].default_value = (0.016, 0.268, 1, 1)

def node_010():
	set_layer(2)
	material, node = get_material_and_node("RPRValueBlend", "RPR Value Blend")
	node.type = 'color'
	node.inputs[node.value1_in].default_value = (0, 0, 0, 1)
	node.inputs[node.value2_in].default_value = (1, 1, 1, 1)

def node_011():
	set_layer(2)
	material, node = get_material_and_node("RPRValueBlend", "RPR Value Blend")
	node.type = 'float'
	node.inputs[node.value1_in].value_float = 1
	node.inputs[node.value2_in].value_float = 1

def node_012():
	set_layer(2)
	material, node = get_material_and_node("RPRValueBlend", "RPR Value Blend")
	node.type = 'vector'
	node.inputs[node.value1_in].default_value = (1, 1, 1, 1)
	node.inputs[node.value2_in].default_value = (1, 1, 1, 1)

def cancel_013_042():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'MUL'
	node.type = 'color'

def node_013():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'FLOOR'

def node_014():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'DOT4'

def node_015():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'DOT3'

def node_016():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'DIV'

def node_017():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'CROSS3'

def node_018():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'COS'

def node_019():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'COMBINE'

def node_020():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'AVERAGE_XYZ'

def node_021():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'AVERAGE'

def node_022():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'ATAN'

def node_023():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'ASIN'

def node_024():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'ACOS'

def node_025():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'ADD'

def node_026():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'ABS'

def node_027():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'TAN'

def node_028():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'SUB'

def node_029():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'SIN'

def node_030():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'SELECT_Z'

def node_031():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'SELECT_Y'

def node_032():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'SELECT_X'

def node_033():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'SELECT_W'

def node_034():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'POW'

def node_035():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'NORMALIZE3'

def node_036():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'MUL'

def node_037():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'MOD'

def node_038():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'MIN'

def node_039():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'MAX'

def node_040():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'LENGTH3'

def node_041():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'ADD'
	node.type = 'float'

def node_042():
	set_layer(2)
	material, node = get_material_and_node("RPRMath", "RPR Math")
	node.op = 'ADD'
	node.type = 'vector'

def node_043():
	set_layer(3)

def node_044():
	set_layer(4)

def cancel_045_048():
	set_layer(4)
	material, node = get_material_and_node("RPRLookup", "RPR Lookup")
	node.type = "UV"

def node_045():
	set_layer(4)
	material, node = get_material_and_node("RPRLookup", "RPR Lookup")
	node.type = "OUTVEC"

def node_046():
	set_layer(4)
	material, node = get_material_and_node("RPRLookup", "RPR Lookup")
	node.type = "INVEC"

def node_047():
	set_layer(4)
	material, node = get_material_and_node("RPRLookup", "RPR Lookup")
	node.type = "P"

def node_048():
	set_layer(4)
	material, node = get_material_and_node("RPRLookup", "RPR Lookup")
	node.type = "N"

def node_049():
	set_layer(10)

def node_050():
	set_layer(11)

def cancel_051_052():
	set_layer(11)
	material, node = get_material_and_node("RPRFresnelShlick", "RPR Fresnel Schlick")
	node.inputs[node.reflectance_in].default_value = 0

def node_051():
	set_layer(11)
	material, node = get_material_and_node("RPRFresnelShlick", "RPR Fresnel Schlick")
	node.inputs[node.reflectance_in].default_value = 0.5

def node_052():
	set_layer(11)
	material, node = get_material_and_node("RPRFresnelShlick", "RPR Fresnel Schlick")
	node.inputs[node.reflectance_in].default_value = 1

def cancel_053_055():
	set_layer(11)
	material, node = get_material_and_node("RPRFresnel", "RPR Fresnel")
	node.inputs[node.ior_in].default_value = 1.2

def node_053():
	set_layer(11)
	material, node = get_material_and_node("RPRFresnel", "RPR Fresnel")
	node.inputs[node.ior_in].default_value = 0

def node_054():
	set_layer(11)
	material, node = get_material_and_node("RPRFresnel", "RPR Fresnel")
	node.inputs[node.ior_in].default_value = 1

def node_055():
	set_layer(11)
	material, node = get_material_and_node("RPRFresnel", "RPR Fresnel")
	node.inputs[node.ior_in].default_value = 3

def node_056():
	set_layer(12)

def cancel_057_060():
	set_layer(12)
	material, node = get_material_and_node("RPRDisplasement", "RPR Uber")
	node.displacement = False
	node.displacement_max = 0.07
	bpy.context.object.rpr_object.subdivision_type = 'level'
	bpy.context.object.rpr_object.subdivision = 2

def node_057():
	set_layer(12)
	material, node = get_material_and_node("RPRDisplasement", "RPR Uber")
	node.displacement = True
	node.displacement_max = 0.04

def node_058():
	set_layer(12)
	material, node = get_material_and_node("RPRDisplasement", "RPR Uber")
	node.displacement = True
	node.displacement_max = 0.04

def node_059():
	set_layer(12)
	material, node = get_material_and_node("RPRDisplasement", "RPR Uber")
	node.displacement = True
	node.displacement_max = 0.04
	bpy.context.object.rpr_object.subdivision = 5

def node_060():
	set_layer(12)
	material, node = get_material_and_node("RPRDisplasement", "RPR Uber")
	node.displacement = True
	node.displacement_max = 0.04
	bpy.context.object.rpr_object.subdivision_type = 'adaptive'
	bpy.context.object.rpr_object.adaptive_subdivision = 5

def node_061():
	set_layer(13)

def cancel_062():
	set_layer(12)
	material, node = get_material_and_node("RPRTransparent", "RPR Transparent")
	node.inputs[node.color_in].default_value = (0.024, 0.036, 1, 1)

def node_062():
	set_layer(13)
	material, node = get_material_and_node("RPRTransparent", "RPR Transparent")
	node.inputs[node.color_in].default_value = (1, 0.5, 1, 1)

	
if __name__ == '__main__':

	list_tests = [
	["BL_MAT_NODE_001", ["default"], node_001, already_default, "RPR_Nodes.blend"],
	["BL_MAT_NODE_002", ["RPRBlend"], node_002, cancel_002_004, "RPR_Nodes.blend"],
	["BL_MAT_NODE_003", ["RPRBlend"], node_003, cancel_002_004, "RPR_Nodes.blend"],
	["BL_MAT_NODE_004", ["RPRBlend"], node_004, cancel_002_004, "RPR_Nodes.blend"],
	["BL_MAT_NODE_005", ["RPRDot"], node_005, already_default, "RPR_Nodes.blend"],
	["BL_MAT_NODE_006", ["RPRDot"], node_006, cancel_006, "RPR_Nodes.blend"],
	["BL_MAT_NODE_007", ["RPRGradient"], node_007, already_default, "RPR_Nodes.blend"],
	["BL_MAT_NODE_008", ["RPRGradient"], node_008, cancel_008_009, "RPR_Nodes.blend"],
	["BL_MAT_NODE_009", ["RPRGradient"], node_009, cancel_008_009, "RPR_Nodes.blend"],
	["BL_MAT_NODE_010", ["RPRValueBlend"], node_010, cancel_010_012, "RPR_Nodes.blend"],
	["BL_MAT_NODE_011", ["RPRValueBlend"], node_011, cancel_010_012, "RPR_Nodes.blend"],
	["BL_MAT_NODE_012", ["RPRValueBlend"], node_012, cancel_010_012, "RPR_Nodes.blend"],
	["BL_MAT_NODE_013", ["RPRMath"], node_013, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_014", ["RPRMath"], node_014, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_015", ["RPRMath"], node_015, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_016", ["RPRMath"], node_016, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_017", ["RPRMath"], node_017, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_018", ["RPRMath"], node_018, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_019", ["RPRMath"], node_019, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_020", ["RPRMath"], node_020, cancel_013_042, "RPR_Nodes.blend"],
	#["BL_MAT_NODE_021", ["RPRMath"], node_021, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_022", ["RPRMath"], node_022, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_023", ["RPRMath"], node_023, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_024", ["RPRMath"], node_024, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_025", ["RPRMath"], node_025, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_026", ["RPRMath"], node_026, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_027", ["RPRMath"], node_027, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_028", ["RPRMath"], node_028, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_029", ["RPRMath"], node_029, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_030", ["RPRMath"], node_030, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_031", ["RPRMath"], node_031, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_032", ["RPRMath"], node_032, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_033", ["RPRMath"], node_033, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_034", ["RPRMath"], node_034, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_035", ["RPRMath"], node_035, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_036", ["RPRMath"], node_036, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_037", ["RPRMath"], node_037, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_038", ["RPRMath"], node_038, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_039", ["RPRMath"], node_039, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_040", ["RPRMath"], node_040, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_041", ["RPRMath"], node_041, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_042", ["RPRMath"], node_042, cancel_013_042, "RPR_Nodes.blend"],
	["BL_MAT_NODE_043", ["RPRMath"], node_043, already_default, "RPR_Nodes.blend"],
	["BL_MAT_NODE_044", ["RPRMath"], node_044, already_default, "RPR_Nodes.blend"],
	#["BL_MAT_NODE_045", ["RPRMath"], node_045, cancel_045_048, "RPR_Nodes.blend"],
	["BL_MAT_NODE_046", ["RPRMath"], node_046, cancel_045_048, "RPR_Nodes.blend"],
	["BL_MAT_NODE_047", ["RPRMath"], node_047, cancel_045_048, "RPR_Nodes.blend"],
	["BL_MAT_NODE_048", ["RPRMath"], node_048, cancel_045_048, "RPR_Nodes.blend"],
	["BL_MAT_NODE_049", ["RPRMath"], node_049, already_default, "RPR_Nodes.blend"],
	["BL_MAT_NODE_050", ["RPRMath"], node_050, already_default, "RPR_Nodes.blend"],
	["BL_MAT_NODE_051", ["RPRMath"], node_051, cancel_051_052, "RPR_Nodes.blend"],
	["BL_MAT_NODE_052", ["RPRMath"], node_052, cancel_051_052, "RPR_Nodes.blend"],
	["BL_MAT_NODE_053", ["RPRMath"], node_053, cancel_053_055, "RPR_Nodes.blend"],
	["BL_MAT_NODE_054", ["RPRMath"], node_054, cancel_053_055, "RPR_Nodes.blend"],
	["BL_MAT_NODE_055", ["RPRMath"], node_055, cancel_053_055, "RPR_Nodes.blend"],
	["BL_MAT_NODE_056", ["RPRMath"], node_056, already_default, "RPR_Nodes.blend"],
	["BL_MAT_NODE_057", ["RPRMath"], node_057, cancel_057_060, "RPR_Nodes.blend"],
	["BL_MAT_NODE_058", ["RPRMath"], node_058, cancel_057_060, "RPR_Nodes.blend"],
	["BL_MAT_NODE_059", ["RPRMath"], node_059, cancel_057_060, "RPR_Nodes.blend"],
	["BL_MAT_NODE_060", ["RPRMath"], node_060, cancel_057_060, "RPR_Nodes.blend"],
	["BL_MAT_NODE_061", ["RPRMath"], node_061, already_default, "RPR_Nodes.blend"],
	["BL_MAT_NODE_062", ["RPRMath"], node_062, cancel_062, "RPR_Nodes.blend"]

	]

	launch_tests()

