

def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)
	
	set_value(scene.render, 'use_single_layer', True)

	# make changes
	test_list[3]()
	# render
	render(test_list[0], test_list[1])
	# undo changes
	test_list[4]()			

	return 1


def empty():
	pass


def get_material_and_node(material_name, node_name):
	material = [e for e in bpy.data.materials if e.name == material_name][0]
	node = [n for n in material.node_tree.nodes if n.name == node_name][0]
	return material, node


def node_001():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection1"])


# create connection from weight map to RPR Blend mat. For cases 1-3.
def cancel_002_004():
	material, node = get_material_and_node("Mix Shader", "Mix Shader")
	node_imagemap = [n for n in material.node_tree.nodes if n.name=="Image Texture"][0]
	material.node_tree.links.new(node_imagemap.outputs['Color'], node.inputs['Fac'])


def node_002():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection1"])
	material, node = get_material_and_node("Mix Shader", "Mix Shader")
	material.node_tree.links.remove(material.node_tree.links.items()[11][1])


def node_003():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection1"])
	material, node = get_material_and_node("Mix Shader", "Mix Shader")
	material.node_tree.links.remove(material.node_tree.links.items()[11][1])
	set_value(node.inputs['Fac'], "default_value", 0)


def node_004():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection1"])
	material, node = get_material_and_node("Mix Shader", "Mix Shader")
	material.node_tree.links.remove(material.node_tree.links.items()[11][1])
	set_value(node.inputs['Fac'], "default_value", 1)


def node_005():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])


def cancel_006_008():
	material, node = get_material_and_node("Checker Texture", "Checker Texture")
	set_value(node.inputs['Scale'], "default_value", 5)


def node_006():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Checker Texture", "Checker Texture")
	set_value(node.inputs['Scale'], "default_value", 1)


def node_007():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Checker Texture", "Checker Texture")
	set_value(node.inputs['Scale'], "default_value", 5)


def node_008():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Checker Texture", "Checker Texture")
	set_value(node.inputs['Scale'], "default_value", 10)


def cancel_009_011():
	material, node = get_material_and_node("Noise Texture", "Noise Texture")
	set_value(node.inputs['Scale'], "default_value", 10)


def node_009():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Noise Texture", "Noise Texture")
	set_value(node.inputs['Scale'], "default_value", 1)


def node_010():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Noise Texture", "Noise Texture")
	set_value(node.inputs['Scale'], "default_value", 5)


def node_011():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Noise Texture", "Noise Texture")
	set_value(node.inputs['Scale'], "default_value", 10)


def cancel_012_018():
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'RADIAL')


def node_012():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'QUADRATIC')


def node_013():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'LINEAR')


def node_014():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'EASING')


def node_015():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'DIAGONAL')


def node_016():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'SPHERICAL')


def node_017():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'QUADRATIC_SPHERE')


def node_018():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection2"])
	material, node = get_material_and_node("Gradient Texture", "Gradient Texture")
	set_value(node, "gradient_type", 'RADIAL')


def node_019():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])


def cancel_020_024():
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'CONSTANT')
	

def node_020():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'LINEAR')


def node_021():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'EASE')


def node_022():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'CARDINAL')


def node_023():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'B_SPLINE')


def node_024():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("Color Ramp", "ColorRamp")
	set_value(node.color_ramp, "interpolation", 'CONSTANT')


def cancel_025():
	material, node = get_material_and_node("Mix", "Mix")
	set_value(node.inputs['Color1'], "default_value", (1.0, 0, 1.0, 1.0))
	set_value(node.inputs['Color2'], "default_value", (0, 0.5, 1.0, 1.0))


def node_025():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("Mix", "Mix")
	set_value(node.inputs['Color1'], "default_value", (0, 0, 0, 1.0))
	set_value(node.inputs['Color2'], "default_value", (1.0, 1.0, 1.0, 1.0))


def cancel_026_059():
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MUL')


def node_026():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ABS')


def node_027():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ADD')


def node_028():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ACOS')


def node_029():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ASIN')


def node_030():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'ATAN')


def node_031():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'AVERAGE')


def node_032():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'AVERAGE_XYZ')


def node_033():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'COMBINE')


def node_034():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'COS')


def node_035():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'CROSS3')


def node_036():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'DIV')


def node_037():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'DOT3')


def node_038():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'DOT4')


def node_039():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'FLOOR')


def node_040():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'LENGTH3')


def node_041():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'LOG')


def node_042():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MAX')


def node_043():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MIN')


def node_044():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MOD')


def node_045():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'MUL')


def node_046():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'NORMALIZE3')


def node_047():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'POW')


def node_048():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SELECT_W')


def node_049():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SELECT_X')


def node_050():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SELECT_Y')


def node_051():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SELECT_Z')


def node_052():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SIN')


def node_053():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SUB')


def node_054():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'TAN')


def node_055():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SHUFFLE_WXYZ')


def node_056():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SHUFFLE_YZWX')


def node_057():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "operation", 'SHUFFLE_ZWXY')


def node_058():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "display_type", 'FLOAT')


def node_059():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "display_type", 'VECTOR')


def node_059():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection3"])
	material, node = get_material_and_node("RPRMath", "RPR Math.001")
	set_value(node, "display_type", 'VECTOR')


def node_060():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection4"])


def node_061():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])


def cancel_062_067():
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Generated'], node.inputs['Fac'])


def node_062():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Generated'], node.inputs['Fac'])


def node_063():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Normal'], node.inputs['Fac'])


def node_064():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['UV'], node.inputs['Fac'])


def node_065():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Object'], node.inputs['Fac'])


def node_066():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Camera'], node.inputs['Fac'])


def node_067():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("Texture Coordinate", "Mix")
	tree = material.node_tree
	material.node_tree.links.remove(material.node_tree.links.items()[3][1])
	texture_coordinate = [n for n in material.node_tree.nodes if n.name=="Texture Coordinate"][0]
	tree.links.new(texture_coordinate.outputs['Window'], node.inputs['Fac'])


def cancel_068_070():
	material, node = get_material_and_node("Fresnel", "Fresnel")
	set_value(node.inputs['IOR'], "default_value", 1.65)


def node_068():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("Fresnel", "Fresnel")
	set_value(node.inputs['IOR'], "default_value", 1)


def node_069():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("Fresnel", "Fresnel")
	set_value(node.inputs['IOR'], "default_value", 1.5)


def node_070():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("Fresnel", "Fresnel")
	set_value(node.inputs['IOR'], "default_value", 3)


def cancel_071_077():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("LookUp", "RPR Lookup")
	set_value(node, "lookup_type", 'UV')


def node_071():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("LookUp", "RPR Lookup")
	set_value(node, "lookup_type", 'UV')


def node_072():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("LookUp", "RPR Lookup")
	set_value(node, "lookup_type", 'NORMAL')


def node_073():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("LookUp", "RPR Lookup")
	set_value(node, "lookup_type", 'POS')


def node_074():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("LookUp", "RPR Lookup")
	set_value(node, "lookup_type", 'INVEC')


def node_075():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("LookUp", "RPR Lookup")
	set_value(node, "lookup_type", 'UV1')


def node_076():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("LookUp", "RPR Lookup")
	set_value(node, "lookup_type", 'P_LOCAL')


def node_077():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection5"])
	material, node = get_material_and_node("LookUp", "RPR Lookup")
	set_value(node, "lookup_type", 'VERTEX_COLOR')


def node_078():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection6"])


def node_085():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection7"])


def cancel_086_090():
	material, node = get_material_and_node("RPRProceduralUV", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_PROJECT")


def node_086():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection7"])
	material, node = get_material_and_node("RPRProceduralUV", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_PLANAR")


def node_087():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection7"])
	material, node = get_material_and_node("RPRProceduralUV", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_CYLINDICAL")


def node_088():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection7"])
	material, node = get_material_and_node("RPRProceduralUV", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_SPHERICAL")


def node_089():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection7"])
	material, node = get_material_and_node("RPRProceduralUV", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_PROJECT")


def node_090():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection7"])
	material, node = get_material_and_node("RPRProceduralUV", "RPR Procedural UV")
	set_value(node, "procedural_type", "TRIPLANAR")


def node_091():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection8"])
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	material.cycles['displacement_method'] = 1


def cancel_092_096():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	material.cycles['displacement_method'] = 1
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)


def node_092():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection8"])
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	material.cycles['displacement_method'] = 1
	set_value(node.inputs['Midlevel'], "default_value", 0)


def node_093():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection8"])
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	material.cycles['displacement_method'] = 1
	set_value(node.inputs['Midlevel'], "default_value", 1)


def node_094():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection8"])
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	material.cycles['displacement_method'] = 1
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 0)


def node_095():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection8"])
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	material.cycles['displacement_method'] = 1
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)


def node_096():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection8"])
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	material.cycles['displacement_method'] = 1
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 2)


def cancel_097():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)
	material.node_tree.links.remove(node.inputs['Normal'].links[0])
	node_imagemap = [n for n in material.node_tree.nodes if n.name== "Image Texture"][0]
	material.node_tree.links.new(node_imagemap.outputs['Color'], node.inputs['Height'])


def node_097():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection8"])
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	material.cycles['displacement_method'] = 1
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)
	material.node_tree.links.remove(node.inputs['Height'].links[0])
	node_imagemap = [n for n in material.node_tree.nodes if n.name== "Image Texture.002"][0]
	material.node_tree.links.new(node_imagemap.outputs['Color'], node.inputs['Normal'])


def cancel_098():
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)
	set_value(node, "space", "OBJECT")


def node_098():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection8"])
	material, node = get_material_and_node("RPRDisplasement", "Displacement")
	material.cycles['displacement_method'] = 1
	set_value(node.inputs['Midlevel'], "default_value", 0.5)
	set_value(node.inputs['Scale'], "default_value", 1)
	set_value(node, "space", "WORLD")


def node_101():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection10"])


def node_102():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])


def cancel_103():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRVolume", "Principled Volume")
	set_value(node.inputs['Color'], "default_value", (1, 0.5, 0, 1))


def node_103():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRVolume", "Principled Volume")
	set_value(node.inputs['Color'], "default_value", (1, 0.5, 1, 1))


def cancel_104_108():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayeredShader", "RPR Procedural UV")
	set_value(node, "procedural_type", "TRIPLANAR")


def node_104():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayeredShader", "RPR Procedural UV")
	set_value(node, "procedural_type", "TRIPLANAR")


def node_105():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayeredShader", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_PLANAR")


def node_106():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayeredShader", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_CYLINDICAL")


def node_107():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayeredShader", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_SPHERICAL")


def node_108():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayeredShader", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_PROJECT")


def cancel_109_113():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayered Texture", "RPR Procedural UV")
	set_value(node, "procedural_type", "TRIPLANAR")


def node_109():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayered Texture", "RPR Procedural UV")
	set_value(node, "procedural_type", "TRIPLANAR")


def node_110():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayered Texture", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_PLANAR")


def node_111():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayered Texture", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_CYLINDICAL")


def node_112():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayered Texture", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_SPHERICAL")


def node_113():
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["Collection9"])
	material, node = get_material_and_node("RPRLayeredShader", "RPR Procedural UV")
	set_value(node, "procedural_type", "MATERIAL_NODE_UVTYPE_PROJECT")


if __name__ == '__main__':

	list_tests = [

		["BL28_MAT_NODE_001", ["RPR Shader Blend weight map"], "RPR_Nodes.blend", node_001, empty],
		["BL28_MAT_NODE_002", ["RPR Shader Blend without weight map"], "RPR_Nodes.blend", node_002, cancel_002_004],
		["BL28_MAT_NODE_003", ["RPR Shader Blend, weight - 0"], "RPR_Nodes.blend", node_003, cancel_002_004],
		["BL28_MAT_NODE_004", ["RPR Shader Blend, weight - 1"], "RPR_Nodes.blend", node_004, cancel_002_004],

		["BL28_MAT_NODE_005", ["Image Mapping default"], "RPR_Nodes.blend", node_005, empty],
		["BL28_MAT_NODE_006", ["Checker Texture scale - 1"], "RPR_Nodes.blend", node_006, cancel_006_008],
		["BL28_MAT_NODE_007", ["Checker Texture scale - 5"], "RPR_Nodes.blend", node_007, cancel_006_008],
		["BL28_MAT_NODE_008", ["Checker Texture scale - 10"], "RPR_Nodes.blend", node_008, cancel_006_008],
		["BL28_MAT_NODE_009", ["Noise texture Scale - 1"], "RPR_Nodes.blend", node_009, cancel_009_011],
		["BL28_MAT_NODE_010", ["Noise texture Scale - 5"], "RPR_Nodes.blend", node_010, cancel_009_011],
		["BL28_MAT_NODE_011", ["Noise texture Scale - 10"], "RPR_Nodes.blend", node_011, cancel_009_011],
		["BL28_MAT_NODE_012", ["Gradient Texture Blendig - Quadrantic"], "RPR_Nodes.blend", node_012, cancel_012_018],
		["BL28_MAT_NODE_013", ["Gradient Texture Blendig - Linear "], "RPR_Nodes.blend", node_013, cancel_012_018],
		["BL28_MAT_NODE_014", ["Gradient Texture Blendig - Easing "], "RPR_Nodes.blend", node_014, cancel_012_018],
		["BL28_MAT_NODE_015", ["Gradient Texture Blendig - Diagonal "], "RPR_Nodes.blend", node_015, cancel_012_018],
		["BL28_MAT_NODE_016", ["Gradient Texture Blendig - Spherical "], "RPR_Nodes.blend", node_016, cancel_012_018],
		["BL28_MAT_NODE_017", ["Gradient Texture Blendig - Quadrantic sphere"], "RPR_Nodes.blend", node_017, cancel_012_018],
		["BL28_MAT_NODE_018", ["Gradient Texture Blendig - Radial"], "RPR_Nodes.blend", node_018, cancel_012_018],

		["BL28_MAT_NODE_019", ["Color Ramp Default"], "RPR_Nodes.blend", node_019, empty],
		["BL28_MAT_NODE_020", ["Color Ramp \"Linear\" interpolation"], "RPR_Nodes.blend", node_020, cancel_020_024],
		["BL28_MAT_NODE_021", ["Color Ramp \"Ease\" interpolation"], "RPR_Nodes.blend", node_021, cancel_020_024],
		["BL28_MAT_NODE_022", ["Color Ramp \"Cardinal\" interpolation"], "RPR_Nodes.blend", node_022, cancel_020_024],
		["BL28_MAT_NODE_023", ["Color Ramp \"B-Spline\" interpolation"], "RPR_Nodes.blend", node_023, cancel_020_024],
		["BL28_MAT_NODE_024", ["Color Ramp \"Constant\" interpolation"], "RPR_Nodes.blend", node_024, cancel_020_024],
		["BL28_MAT_NODE_025", ["ColumnValueBlend, Value 1 - (0, 0, 0) (RGB), Value 2 - (1, 1, 1) (RGB)"], "RPR_Nodes.blend", node_025, cancel_025],
		["BL28_MAT_NODE_026", ["Operation - Abs"], "RPR_Nodes.blend", node_026, cancel_026_059],
		["BL28_MAT_NODE_027", ["Operation - Add"], "RPR_Nodes.blend", node_027, cancel_026_059],
		["BL28_MAT_NODE_028", ["Operation - Arccosine"], "RPR_Nodes.blend", node_028, cancel_026_059],
		["BL28_MAT_NODE_029", ["Operation - Arcsine"], "RPR_Nodes.blend", node_029, cancel_026_059],
		["BL28_MAT_NODE_030", ["Operation - Arctangent"], "RPR_Nodes.blend", node_030, cancel_026_059],
		["BL28_MAT_NODE_031", ["Operation - Average"], "RPR_Nodes.blend", node_031, cancel_026_059],
		["BL28_MAT_NODE_032", ["Operation - Average XYZ"], "RPR_Nodes.blend", node_032, cancel_026_059],
		["BL28_MAT_NODE_033", ["Operation - Combine"], "RPR_Nodes.blend", node_033, cancel_026_059],
		["BL28_MAT_NODE_034", ["Operation - Cosine"], "RPR_Nodes.blend", node_034, cancel_026_059],
		["BL28_MAT_NODE_035", ["Operation - Cross Product"], "RPR_Nodes.blend", node_035, cancel_026_059],
		["BL28_MAT_NODE_036", ["Operation - Divide"], "RPR_Nodes.blend", node_036, cancel_026_059],
		["BL28_MAT_NODE_037", ["Operation - Dot3 Product"], "RPR_Nodes.blend", node_037, cancel_026_059],
		["BL28_MAT_NODE_038", ["Operation - Dot4 Product"], "RPR_Nodes.blend", node_038, cancel_026_059],
		["BL28_MAT_NODE_039", ["Operation - Floor"], "RPR_Nodes.blend", node_039, cancel_026_059],
		["BL28_MAT_NODE_040", ["Operation - Length3"], "RPR_Nodes.blend", node_040, cancel_026_059],
		["BL28_MAT_NODE_041", ["Operation - Log"], "RPR_Nodes.blend", node_041, cancel_026_059],
		["BL28_MAT_NODE_042", ["Operation - Max"], "RPR_Nodes.blend", node_042, cancel_026_059],
		["BL28_MAT_NODE_043", ["Operation - Min"], "RPR_Nodes.blend", node_043, cancel_026_059],
		["BL28_MAT_NODE_044", ["Operation - Mod"], "RPR_Nodes.blend", node_044, cancel_026_059],
		["BL28_MAT_NODE_045", ["Operation - Multiply"], "RPR_Nodes.blend", node_045, cancel_026_059],
		["BL28_MAT_NODE_046", ["Operation - Normalize"], "RPR_Nodes.blend", node_046, cancel_026_059],
		["BL28_MAT_NODE_047", ["Operation - Pow"], "RPR_Nodes.blend", node_047, cancel_026_059],
		["BL28_MAT_NODE_048", ["Operation - Select W"], "RPR_Nodes.blend", node_048, cancel_026_059],
		["BL28_MAT_NODE_049", ["Operation - Select X"], "RPR_Nodes.blend", node_049, cancel_026_059],
		["BL28_MAT_NODE_050", ["Operation - Select Y"], "RPR_Nodes.blend", node_050, cancel_026_059],
		["BL28_MAT_NODE_051", ["Operation - Select Z"], "RPR_Nodes.blend", node_051, cancel_026_059],
		["BL28_MAT_NODE_052", ["Operation - Sine"], "RPR_Nodes.blend", node_052, cancel_026_059],
		["BL28_MAT_NODE_053", ["Operation - Subtract"], "RPR_Nodes.blend", node_053, cancel_026_059],
		["BL28_MAT_NODE_054", ["Operation - Tangent"], "RPR_Nodes.blend", node_054, cancel_026_059],
		["BL28_MAT_NODE_055", ["Operation - XYZW->WXYZ"], "RPR_Nodes.blend", node_055, cancel_026_059],
		["BL28_MAT_NODE_056", ["Operation - XYZW->YZWX"], "RPR_Nodes.blend", node_056, cancel_026_059],
		["BL28_MAT_NODE_057", ["Operation - XYZW->ZWXY"], "RPR_Nodes.blend", node_057, cancel_026_059],
		["BL28_MAT_NODE_058", ["Type - Float"], "RPR_Nodes.blend", node_058, cancel_026_059],
		["BL28_MAT_NODE_059", ["Type - Vector"], "RPR_Nodes.blend", node_059, cancel_026_059],

		["BL28_MAT_NODE_060", ["Normal and Bump"], "RPR_Nodes.blend", node_060, empty],

		["BL28_MAT_NODE_061", ["Texture Coordinates"], "RPR_Nodes.blend", node_061, empty],
		["BL28_MAT_NODE_062", ["Generetad Texture Coordinates"], "RPR_Nodes.blend", node_062, cancel_062_067],
		["BL28_MAT_NODE_063", ["Normal Texture Coordinates"], "RPR_Nodes.blend", node_063, cancel_062_067],
		["BL28_MAT_NODE_064", ["UV Texture Coordinates"], "RPR_Nodes.blend", node_064, cancel_062_067],
		["BL28_MAT_NODE_065", ["Object Texture Coordinates"], "RPR_Nodes.blend", node_065, cancel_062_067],
		["BL28_MAT_NODE_066", ["Camera Texture Coordinates"], "RPR_Nodes.blend", node_066, cancel_062_067],
		["BL28_MAT_NODE_067", ["Window Texture Coordinates"], "RPR_Nodes.blend", node_067, cancel_062_067],
		["BL28_MAT_NODE_068", ["Fresnel - 1"], "RPR_Nodes.blend", node_068, cancel_068_070],
		["BL28_MAT_NODE_069", ["Fresnel - 1.5"], "RPR_Nodes.blend", node_069, cancel_068_070],
		["BL28_MAT_NODE_070", ["Fresnel - 3"], "RPR_Nodes.blend", node_070, cancel_068_070],
		["BL28_MAT_NODE_071", ["RPR Lookup node, Type - UV"], "RPR_Nodes.blend", node_071, cancel_071_077],
		["BL28_MAT_NODE_072", ["RPR Lookup node, Type - Normal"], "RPR_Nodes.blend", node_072, cancel_071_077],
		["BL28_MAT_NODE_073", ["RPR Lookup node, Type - Position"], "RPR_Nodes.blend", node_073, cancel_071_077],
		["BL28_MAT_NODE_074", ["RPR Lookup node, Type - InVec"], "RPR_Nodes.blend", node_074, cancel_071_077],
		["BL28_MAT_NODE_075", ["RPR Lookup node, Type - UV1"], "RPR_Nodes.blend", node_075, cancel_071_077],
		["BL28_MAT_NODE_076", ["RPR Lookup node, Type - Object Position"], "RPR_Nodes.blend", node_076, cancel_071_077],
		["BL28_MAT_NODE_077", ["RPR Lookup node, Type - Vertex Color"], "RPR_Nodes.blend", node_077, cancel_071_077],

		["BL28_MAT_NODE_078", ["Shadow Catcher"], "RPR_Nodes.blend", node_078, empty],

		# ["BL28_MAT_NODE_079", ["RPR Fresnel Schlick, RPR Fresnel"], "RPR_Nodes.blend", node_079, empty],
		# ["BL28_MAT_NODE_080", ["RPR Fresnel Schlick node, Reflectance - 0.5"], "RPR_Nodes.blend",node_080, empty],
		# ["BL28_MAT_NODE_081", ["RPR Fresnel Schlick node, Reflectance - 1"], "RPR_Nodes.blend", node_081, empty],
		# ["BL28_MAT_NODE_082", ["RPR Fresnel node, IOR - 0"], "RPR_Nodes.blend", "Collection7", node_082, empty],
		# ["BL28_MAT_NODE_083", ["RPR Fresnel node, IOR - 1"], "RPR_Nodes.blend", "Collection7", node_083, empty],
		# ["BL28_MAT_NODE_084", ["RPR Fresnel node, IOR - 3"], "RPR_Nodes.blend", "Collection7", node_084, empty],

		["BL28_MAT_NODE_085", ["RPR Passthrough Node"], "RPR_Nodes.blend", node_085, empty],
		["BL28_MAT_NODE_086", ["RPR Procedural UV, Type - Plane"], "RPR_Nodes.blend", node_086, cancel_086_090],
		["BL28_MAT_NODE_087", ["RPR Procedural UV, Type - Cylinder"], "RPR_Nodes.blend", node_087, cancel_086_090],
		["BL28_MAT_NODE_088", ["RPR Procedural UV, Type - Sphere"], "RPR_Nodes.blend", node_088, cancel_086_090],
		["BL28_MAT_NODE_089", ["RPR Procedural UV, Type - Camera"], "RPR_Nodes.blend", node_089, cancel_086_090],
		["BL28_MAT_NODE_090", ["RPR Procedural UV, Type - Tryplanar"], "RPR_Nodes.blend", node_090, cancel_086_090],

		["BL28_MAT_NODE_091", ["Displacement"], "RPR_Nodes.blend", node_091, empty],
		["BL28_MAT_NODE_092", ["Displacement , Midlevel: - 0"], "RPR_Nodes.blend", node_092, cancel_092_096],
		["BL28_MAT_NODE_093", ["Displacement , Midlevel: - 1"], "RPR_Nodes.blend", node_093, cancel_092_096],
		["BL28_MAT_NODE_094", ["Displacement , Scale: - 0"], "RPR_Nodes.blend", node_094, cancel_092_096],
		["BL28_MAT_NODE_095", ["Displacement , Scale: - 1"], "RPR_Nodes.blend", node_095, cancel_092_096],
		["BL28_MAT_NODE_096", ["Displacement , Scale: - 2"], "RPR_Nodes.blend", node_096, cancel_092_096],
		["BL28_MAT_NODE_097", ["Displacement , Normal"], "RPR_Nodes.blend", node_097, cancel_097],
		["BL28_MAT_NODE_098", ["Displacement , World Space"], "RPR_Nodes.blend", node_089, cancel_098],

		#["BL28_MAT_NODE_099", ["RPR Transparent default"], "RPR_Nodes.blend", node_099, empty],
		#["BL28_MAT_NODE_100", ["RPR Transparent node, Diffuse Color - (1, 0.5, 0)"], "RPR_Nodes.blend", node_100, empty],

		["BL28_MAT_NODE_101", ["Blender Nodes"], "RPR_Nodes.blend", node_101, empty],

		["BL28_MAT_NODE_102", ["Volume + Layered materials"], "RPR_Nodes.blend", node_102, empty],
		["BL28_MAT_NODE_103", ["Volume Color"], "RPR_Nodes.blend", node_103, cancel_103],
		["BL28_MAT_NODE_104", ["Layer Shader Triplanar"], "RPR_Nodes.blend", node_104, cancel_104_108],
		["BL28_MAT_NODE_105", ["Layer Shader Plane"], "RPR_Nodes.blend", node_105, cancel_104_108],
		["BL28_MAT_NODE_106", ["Layer Shader Cilinder"], "RPR_Nodes.blend", node_106, cancel_104_108],
		["BL28_MAT_NODE_107", ["Layer Shader Sphere"], "RPR_Nodes.blend", node_107, cancel_104_108],
		["BL28_MAT_NODE_108", ["Layer Shader Camera"], "RPR_Nodes.blend", node_108, cancel_104_108],

		["BL28_MAT_NODE_109", ["Layer Shader Triplanar"], "RPR_Nodes.blend", node_109, cancel_109_113],
		["BL28_MAT_NODE_110", ["Layer Shader Plane"], "RPR_Nodes.blend", node_110, cancel_109_113],
		["BL28_MAT_NODE_111", ["Layer Shader Cilinder"], "RPR_Nodes.blend", node_111, cancel_109_113],
		["BL28_MAT_NODE_112", ["Layer Shader Sphere"], "RPR_Nodes.blend", node_112, cancel_109_113],
		["BL28_MAT_NODE_113", ["Layer Shader Camera"], "RPR_Nodes.blend", node_113, cancel_109_113]

	]

	launch_tests()

