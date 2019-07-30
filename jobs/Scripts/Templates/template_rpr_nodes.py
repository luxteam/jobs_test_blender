

def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)
	
	set_value(scene.render, 'use_single_layer', True)
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["{{}}".format(test_list[3])])

	# make changes
	test_list[4]()
	# render
	render(test_list[0], test_list[1])
	# undo changes
	test_list[5]()			

	return 1


def empty():
	pass


def get_material_and_node(material_name, node_name):
	material = [e for e in bpy.data.materials if e.name == material_name][0]
	node = [n for n in material.node_tree.nodes if n.name == node_name][0]
	return material, node


# create connection from weight map to RPR Blend mat. For cases 1-3.
def cancel_002_004():
	material, node = get_material_and_node("Mix Shader", "Mix Shader")
	node_imagemap = [n for n in material.node_tree.nodes if n.name=="Image Texture"][0]
	material.node_tree.links.new(node_imagemap.outputs['Color'], node.inputs['Fac'])


def node_002():
	material, node = get_material_and_node("Mix Shader", "Mix Shader")
	material.node_tree.links.remove(material.node_tree.links.items()[11][1])


def node_003():
	material, node = get_material_and_node("Mix Shader", "Mix Shader")
	material.node_tree.links.remove(material.node_tree.links.items()[11][1])
	set_value(node.inputs['Fac'], "default_value", 0)


def node_004():
	material, node = get_material_and_node("Mix Shader", "Mix Shader")
	material.node_tree.links.remove(material.node_tree.links.items()[11][1])
	set_value(node.inputs['Fac'], "default_value", 1)


def cancel_006_008():
	material, node = get_material_and_node("Checker Texture", "Checker Texture")
	set_value(node.inputs['Scale'], "default_value", 5)


def node_006():
	material, node = get_material_and_node("Checker Texture", "Checker Texture")
	set_value(node.inputs['Scale'], "default_value", 1)


def node_007():
	material, node = get_material_and_node("Checker Texture", "Checker Texture")
	set_value(node.inputs['Scale'], "default_value", 5)


def node_008():
	material, node = get_material_and_node("Checker Texture", "Checker Texture")
	set_value(node.inputs['Scale'], "default_value", 10)


def cancel_009_011():
	material, node = get_material_and_node("Noise Texture", "Noise Texture")
	set_value(node.inputs['Scale'], "default_value", 10)


def node_009():
	material, node = get_material_and_node("Noise Texture", "Noise Texture")
	set_value(node.inputs['Scale'], "default_value", 1)


def node_010():
	material, node = get_material_and_node("Noise Texture", "Noise Texture")
	set_value(node.inputs['Scale'], "default_value", 5)


def node_011():
	material, node = get_material_and_node("Noise Texture", "Noise Texture")
	set_value(node.inputs['Scale'], "default_value", 10)


def cancel_012_018():
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'RADIAL')


def node_012():
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'QUADRATIC')


def node_013():
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'LINEAR')


def node_014():
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'EASING')


def node_015():
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'DIAGONAL')


def node_016():
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'SPHERICAL')


def node_017():
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'QUADRATIC_SPHERE')


def node_018():
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'RADIAL')


def cancel_020_024():
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'CONSTANT')
	

def node_020():
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'LINEAR')


def node_021():
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'EASE')


def node_022():
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'CARDINAL')


def node_023():
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'B_SPLINE')


def node_024():
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'CONSTANT')


def cancel_025():
	material, node = get_material_and_node("Mix", "Mix")
	set_value(node.inputs['Color1'], "default_value", (1.0, 0, 1.0, 1.0))
	set_value(node.inputs['Color2'], "default_value", (0, 0.5, 1.0, 1.0))


def node_025():
	material, node = get_material_and_node("Mix", "Mix")
	set_value(node.inputs['Color1'], "default_value", (0, 0, 0, 1.0))
	set_value(node.inputs['Color2'], "default_value", (1.0, 1.0, 1.0, 1.0))


def cancel_026_059():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MUL')


def node_026():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ABS')


def node_027():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ADD')


def node_028():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ACOS')


def node_029():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ASIN')


def node_030():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ATAN')


def node_031():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'AVERAGE')


def node_032():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'AVERAGE_XYZ')


def node_033():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'COMBINE')


def node_034():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'COS')


def node_035():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'CROSS3')


def node_036():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'DIV')


def node_037():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'DOT3')


def node_038():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'DOT4')


def node_039():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'FLOOR')


def node_040():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'LENGTH3')


def node_041():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'LOG')


def node_042():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MAX')


def node_043():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MIN')


def node_044():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MOD')


def node_045():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MUL')


def node_046():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'NORMALIZE3')


def node_047():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'POW')


def node_048():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SELECT_W')


def node_049():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SELECT_X')


def node_050():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SELECT_Y')


def node_051():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SELECT_Z')


def node_052():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SIN')


def node_053():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SUB')


def node_054():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'TAN')


def node_055():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SHUFFLE_WXYZ')


def node_056():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SHUFFLE_YZWX')


def node_057():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SHUFFLE_ZWXY')


def node_058():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "display_type", 'FLOAT')


def node_059():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "display_type", 'VECTOR')


def node_059():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "display_type", 'VECTOR')


def cancel_062_067():
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Generated'], node.inputs['Fac'])


def node_062():
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Generated'], node.inputs['Fac'])


def node_063():
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Normal'], node.inputs['Fac'])


def node_064():
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['UV'], node.inputs['Fac'])


def node_065():
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Object'], node.inputs['Fac'])


def node_066():
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Window'], node.inputs['Fac'])


def node_067():
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Generated'], node.inputs['Fac'])


def cancel_068_070():
	material, node = get_material_and_node("Fresnel", "Fresnel")
	set_value(node.inputs['IOR'], "default_value", 1.65)


def node_068():
	material, node = get_material_and_node("Fresnel", "Fresnel")
	set_value(node.inputs['IOR'], "default_value", 1)


def node_069():
	material, node = get_material_and_node("Fresnel", "Fresnel")
	set_value(node.inputs['IOR'], "default_value", 1.5)


def node_070():
	material, node = get_material_and_node("Fresnel", "Fresnel")
	set_value(node.inputs['IOR'], "default_value", 3)


def cancel_083_087():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)


def node_083():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0)


def node_084():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 1)


def node_085():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 0)


def node_086():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)


def node_087():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 2)


def cancel_088():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)
	material.node_tree.links.remove(node.inputs['Normal'].links[0])
	node_imagemap = [n for n in material.node_tree.nodes if n.name== "Image Texture"][0]
	material.node_tree.links.new(node_imagemap.outputs['Color'], node.inputs['Height'])


def node_088():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)
	material.node_tree.links.remove(node.inputs['Height'].links[0])
	node_imagemap = [n for n in material.node_tree.nodes if n.name== "Image Texture.002"][0]
	material.node_tree.links.new(node_imagemap.outputs['Color'], node.inputs['Normal'])


def cancel_089():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)
	set_value(node, "space", "OBJECT")


def node_089():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)
	set_value(node, "space", "WORLD")



if __name__ == '__main__':

	list_tests = [
		["BL28_MAT_NODE_001", ["RPR Shader Blend weight map"], "RPR_Nodes.blend", "Collection1", empty, empty],
		["BL28_MAT_NODE_002", ["RPR Shader Blend without weight map"], "RPR_Nodes.blend", "Collection1", node_002, cancel_002_004],
		["BL28_MAT_NODE_003", ["RPR Shader Blend, weight - 0"], "RPR_Nodes.blend", "Collection1", node_003, cancel_002_004],
		["BL28_MAT_NODE_004", ["RPR Shader Blend, weight - 1"], "RPR_Nodes.blend", "Collection1", node_004, cancel_002_004],
		["BL28_MAT_NODE_005", ["Image Mapping default"], "RPR_Nodes.blend", "Collection2", empty, empty],
		["BL28_MAT_NODE_006", ["Checker Texture scale - 1"], "RPR_Nodes.blend", "Collection2", node_006, cancel_006_008],
		["BL28_MAT_NODE_007", ["Checker Texture scale - 5"], "RPR_Nodes.blend", "Collection2", node_007, cancel_006_008],
		["BL28_MAT_NODE_008", ["Checker Texture scale - 10"], "RPR_Nodes.blend", "Collection2", node_008, cancel_006_008],
		["BL28_MAT_NODE_009", ["Noise texture Scale - 1"], "RPR_Nodes.blend", "Collection2", node_009, cancel_009_011],
		["BL28_MAT_NODE_010", ["Noise texture Scale - 5"], "RPR_Nodes.blend", "Collection2", node_010, cancel_009_011],
		["BL28_MAT_NODE_011", ["Noise texture Scale - 10"], "RPR_Nodes.blend", "Collection2", node_011, cancel_009_011],
		["BL28_MAT_NODE_012", ["Gradient Texture Blendig - Quadrantic"], "RPR_Nodes.blend", "Collection2", node_012, cancel_012_018],
		["BL28_MAT_NODE_013", ["Gradient Texture Blendig - Linear "], "RPR_Nodes.blend", "Collection2", node_013, cancel_012_018],
		["BL28_MAT_NODE_014", ["Gradient Texture Blendig - Easing "], "RPR_Nodes.blend", "Collection2", node_014, cancel_012_018],
		["BL28_MAT_NODE_015", ["Gradient Texture Blendig - Diagonal "], "RPR_Nodes.blend", "Collection2", node_015, cancel_012_018],
		["BL28_MAT_NODE_016", ["Gradient Texture Blendig - Spherical "], "RPR_Nodes.blend", "Collection2", node_016, cancel_012_018],
		["BL28_MAT_NODE_017", ["Gradient Texture Blendig - Quadrantic sphere"], "RPR_Nodes.blend", "Collection2", node_017, cancel_012_018],
		["BL28_MAT_NODE_018", ["Gradient Texture Blendig - Radial"], "RPR_Nodes.blend", "Collection2", node_018, cancel_012_018],
		["BL28_MAT_NODE_019", ["Color Ramp Default"], "RPR_Nodes.blend", "Collection3", empty, empty],
		["BL28_MAT_NODE_020", ["Color Ramp \"Linear\" interpolation"], "RPR_Nodes.blend", "Collection3", node_020, cancel_020_024],
		["BL28_MAT_NODE_021", ["Color Ramp \"Ease\" interpolation"], "RPR_Nodes.blend", "Collection3", node_021, cancel_020_024],
		["BL28_MAT_NODE_022", ["Color Ramp \"Cardinal\" interpolation"], "RPR_Nodes.blend", "Collection3", node_022, cancel_020_024],
		["BL28_MAT_NODE_023", ["Color Ramp \"B-Spline\" interpolation"], "RPR_Nodes.blend", "Collection3", node_023, cancel_020_024],
		["BL28_MAT_NODE_024", ["Color Ramp \"Constant\" interpolation"], "RPR_Nodes.blend", "Collection3", node_024, cancel_020_024],
		["BL28_MAT_NODE_025", ["ColumnValueBlend, Value 1 - (0, 0, 0) (RGB), Value 2 - (1, 1, 1) (RGB)"], "RPR_Nodes.blend", "Collection3", node_025, cancel_025],
		["BL28_MAT_NODE_026", ["Operation - Abs"], "RPR_Nodes.blend", "Collection3", node_026, cancel_026_059],
		["BL28_MAT_NODE_027", ["Operation - Add"], "RPR_Nodes.blend", "Collection3", node_027, cancel_026_059],
		["BL28_MAT_NODE_028", ["Operation - Arccosine"], "RPR_Nodes.blend", "Collection3", node_028, cancel_026_059],
		["BL28_MAT_NODE_029", ["Operation - Arcsine"], "RPR_Nodes.blend", "Collection3", node_029, cancel_026_059],
		["BL28_MAT_NODE_030", ["Operation - Arctangent"], "RPR_Nodes.blend", "Collection3", node_030, cancel_026_059],
		["BL28_MAT_NODE_031", ["Operation - Average"], "RPR_Nodes.blend", "Collection3", node_031, cancel_026_059],
		["BL28_MAT_NODE_032", ["Operation - Average XYZ"], "RPR_Nodes.blend", "Collection3", node_032, cancel_026_059],
		["BL28_MAT_NODE_033", ["Operation - Combine"], "RPR_Nodes.blend", "Collection3", node_033, cancel_026_059],
		["BL28_MAT_NODE_034", ["Operation - Cosine"], "RPR_Nodes.blend", "Collection3", node_034, cancel_026_059],
		["BL28_MAT_NODE_035", ["Operation - Cross Product"], "RPR_Nodes.blend", "Collection3", node_035, cancel_026_059],
		["BL28_MAT_NODE_036", ["Operation - Divide"], "RPR_Nodes.blend", "Collection3", node_036, cancel_026_059],
		["BL28_MAT_NODE_037", ["Operation - Dot3 Product"], "RPR_Nodes.blend", "Collection3", node_037, cancel_026_059],
		["BL28_MAT_NODE_038", ["Operation - Dot4 Product"], "RPR_Nodes.blend", "Collection3", node_038, cancel_026_059],
		["BL28_MAT_NODE_039", ["Operation - Floor"], "RPR_Nodes.blend", "Collection3", node_039, cancel_026_059],
		["BL28_MAT_NODE_040", ["Operation - Length3"], "RPR_Nodes.blend", "Collection3", node_040, cancel_026_059],
		["BL28_MAT_NODE_041", ["Operation - Log"], "RPR_Nodes.blend", "Collection3", node_041, cancel_026_059],
		["BL28_MAT_NODE_042", ["Operation - Max"], "RPR_Nodes.blend", "Collection3", node_042, cancel_026_059],
		["BL28_MAT_NODE_043", ["Operation - Min"], "RPR_Nodes.blend", "Collection3", node_043, cancel_026_059],
		["BL28_MAT_NODE_044", ["Operation - Mod"], "RPR_Nodes.blend", "Collection3", node_044, cancel_026_059],
		["BL28_MAT_NODE_045", ["Operation - Multiply"], "RPR_Nodes.blend", "Collection3", node_045, cancel_026_059],
		["BL28_MAT_NODE_046", ["Operation - Normalize"], "RPR_Nodes.blend", "Collection3", node_046, cancel_026_059],
		["BL28_MAT_NODE_047", ["Operation - Pow"], "RPR_Nodes.blend", "Collection3", node_047, cancel_026_059],
		["BL28_MAT_NODE_048", ["Operation - Select W"], "RPR_Nodes.blend", "Collection3", node_048, cancel_026_059],
		["BL28_MAT_NODE_049", ["Operation - Select X"], "RPR_Nodes.blend", "Collection3", node_049, cancel_026_059],
		["BL28_MAT_NODE_050", ["Operation - Select Y"], "RPR_Nodes.blend", "Collection3", node_050, cancel_026_059],
		["BL28_MAT_NODE_051", ["Operation - Select Z"], "RPR_Nodes.blend", "Collection3", node_051, cancel_026_059],
		["BL28_MAT_NODE_052", ["Operation - Sine"], "RPR_Nodes.blend", "Collection3", node_052, cancel_026_059],
		["BL28_MAT_NODE_053", ["Operation - Subtract"], "RPR_Nodes.blend", "Collection3", node_053, cancel_026_059],
		["BL28_MAT_NODE_054", ["Operation - Tangent"], "RPR_Nodes.blend", "Collection3", node_054, cancel_026_059],
		["BL28_MAT_NODE_055", ["Operation - XYZW->WXYZ"], "RPR_Nodes.blend", "Collection3", node_055, cancel_026_059],
		["BL28_MAT_NODE_056", ["Operation - XYZW->YZWX"], "RPR_Nodes.blend", "Collection3", node_056, cancel_026_059],
		["BL28_MAT_NODE_057", ["Operation - XYZW->ZWXY"], "RPR_Nodes.blend", "Collection3", node_057, cancel_026_059],
		["BL28_MAT_NODE_058", ["Type - Float"], "RPR_Nodes.blend", "Collection3", node_058, cancel_026_059],
		["BL28_MAT_NODE_059", ["Type - Vector"], "RPR_Nodes.blend", "Collection3", node_059, cancel_026_059],
		["BL28_MAT_NODE_060", ["Normal and Bump"], "RPR_Nodes.blend", "Collection4", empty, empty],
		["BL28_MAT_NODE_061", ["Texture Coordinates"], "RPR_Nodes.blend", "Collection5", empty, empty],
		["BL28_MAT_NODE_062", ["Generetad Texture Coordinates"], "RPR_Nodes.blend", "Collection5", node_062, cancel_062_067],
		["BL28_MAT_NODE_063", ["Normal Texture Coordinates"], "RPR_Nodes.blend", "Collection5", node_063, cancel_062_067],
		["BL28_MAT_NODE_064", ["UV Texture Coordinates"], "RPR_Nodes.blend", "Collection5", node_064, cancel_062_067],
		["BL28_MAT_NODE_065", ["Object Texture Coordinates"], "RPR_Nodes.blend", "Collection5", node_065, cancel_062_067],
		["BL28_MAT_NODE_066", ["Camera Texture Coordinates"], "RPR_Nodes.blend", "Collection5", node_066, cancel_062_067],
		["BL28_MAT_NODE_067", ["Window Texture Coordinates"], "RPR_Nodes.blend", "Collection5", node_067, cancel_062_067],
		["BL28_MAT_NODE_068", ["Fresnel - 1"], "RPR_Nodes.blend", "Collection5", node_068, cancel_068_070],
		["BL28_MAT_NODE_069", ["Fresnel - 1.5"], "RPR_Nodes.blend", "Collection5", node_069, cancel_068_070],
		["BL28_MAT_NODE_070", ["Fresnel - 3"], "RPR_Nodes.blend", "Collection5", node_070, cancel_068_070],
		# ["BL28_MAT_NODE_071", ["RPR Lookup node, Type - OutVec"], "RPR_Nodes.blend", "Collection5", node_071, cancel_062],
		# ["BL28_MAT_NODE_072", ["RPR Lookup node, Type - InVec"], "RPR_Nodes.blend", "Collection5", node_072, cancel_062],
		# ["BL28_MAT_NODE_073", ["RPR Lookup node, Type - Position"], "RPR_Nodes.blend", "Collection5", node_073, cancel_062],
		# ["BL28_MAT_NODE_074", ["RPR Lookup node, Type - Normal"], "RPR_Nodes.blend", "Collection5", node_074, cancel_062],
		["BL28_MAT_NODE_075", ["Shadow Catcher"], "RPR_Nodes.blend", "Collection6", empty, empty],
		# ["BL28_MAT_NODE_076", ["RPR Fresnel Schlick, RPR Fresnel"], "RPR_Nodes.blend", "Collection7", node_076, cancel_062],
		# ["BL28_MAT_NODE_077", ["RPR Fresnel Schlick node, Reflectance - 0.5"], "RPR_Nodes.blend", "Collection7", node_077, cancel_062],
		# ["BL28_MAT_NODE_078", ["RPR Fresnel Schlick node, Reflectance - 1"], "RPR_Nodes.blend", "Collection7", node_078, cancel_062],
		# ["BL28_MAT_NODE_079", ["RPR Fresnel node, IOR - 0"], "RPR_Nodes.blend", "Collection7", node_079, cancel_062],
		# ["BL28_MAT_NODE_080", ["RPR Fresnel node, IOR - 1"], "RPR_Nodes.blend", "Collection7", node_080, cancel_062],
		# ["BL28_MAT_NODE_081", ["RPR Fresnel node, IOR - 3"], "RPR_Nodes.blend", "Collection7", node_081, cancel_062],
		["BL28_MAT_NODE_082", ["Displacement"], "RPR_Nodes.blend", "Collection8", empty, empty],
		["BL28_MAT_NODE_083", ["Displacement , Midlevel: - 0"], "RPR_Nodes.blend", "Collection8", node_083, cancel_083_087],
		["BL28_MAT_NODE_084", ["Displacement , Midlevel: - 1"], "RPR_Nodes.blend", "Collection8", node_084, cancel_083_087],
		["BL28_MAT_NODE_085", ["Displacement , Scale: - 0"], "RPR_Nodes.blend", "Collection8", node_085, cancel_083_087],
		["BL28_MAT_NODE_086", ["Displacement , Scale: - 1"], "RPR_Nodes.blend", "Collection8", node_086, cancel_083_087],
		["BL28_MAT_NODE_087", ["Displacement , Scale: - 2"], "RPR_Nodes.blend", "Collection8", node_087, cancel_083_087],
		["BL28_MAT_NODE_088", ["Displacement , Normal"], "RPR_Nodes.blend", "Collection8", node_088, cancel_088],
		["BL28_MAT_NODE_089", ["Displacement , World Space"], "RPR_Nodes.blend", "Collection8", node_089, cancel_089],
		# ["BL28_MAT_NODE_090", ["RPR Transparent default"], "RPR_Nodes.blend", "Collection9", node_087, cancel_062],
		# ["BL28_MAT_NODE_091", ["RPR Transparent node, Diffuse Color - (1, 0.5, 0)"], "RPR_Nodes.blend", "Collection9", node_088, cancel_062],
		["BL28_MAT_NODE_092", ["Blender Nodes"], "RPR_Nodes.blend", "Collection10", empty, empty]
	]

	launch_tests()

