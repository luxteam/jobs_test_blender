
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)
	
	# make changes
	test_list[3]()
	# render
	render(test_list[0], test_list[1])
	# undo changes
	test_list[4]()			

	return 1


def get_material_and_node():
	uber_material = [e for e in bpy.data.materials if e.name == "Uber"][0]
	node_uber = [n for n in uber_material.node_tree.nodes if n.name=="RPR Uber.001"][0]
	return uber_material, node_uber


def create_normal_map(attr, image_name):
	uber_material, node_uber = get_material_and_node()
	tree = uber_material.node_tree

	# create image map
	node_imagemap = tree.nodes.new(type='ShaderNodeTexImage')
	image = bpy.data.images.load(os.path.join(r"{resource_path}", "Maps", image_name))
	node_imagemap.image = image

	# crete normal map
	node_normalmap = tree.nodes.new(type='ShaderNodeNormalMap')
	tree.links.new(node_imagemap.outputs['Color'], node_normalmap.inputs['Color'])

	# connect normal with material
	tree.links.new(node_normalmap.outputs['Normal'], node_uber.inputs[attr])


def create_imagemap(attr, image_name):
	uber_material, node_uber = get_material_and_node()
	tree = uber_material.node_tree

	# create image map
	node_imagemap = tree.nodes.new(type='ShaderNodeTexImage')
	image = bpy.data.images.load(os.path.join(r"{resource_path}", "Maps", image_name))
	node_imagemap.image = image
	
	if type(node_uber.inputs[attr]['default_value']) == tuple:
		tree.links.new(node_imagemap.outputs['Color'], node_uber.inputs[attr])
	elif type(node_uber.inputs[attr]['default_value']) == float:
		tree.links.new(node_imagemap.outputs['Alpha'], node_uber.inputs[attr])


def delete_normalmap():
	uber_material, node_uber = get_material_and_node()
	node_normalmap = [n for n in uber_material.node_tree.nodes if n.name=="Normal Map"][0]
	uber_material.node_tree.nodes.remove(node_normalmap)
	delete_imagemap()


def delete_imagemap():
	uber_material, node_uber = get_material_and_node()
	node_imagemap = [n for n in uber_material.node_tree.nodes if n.name=="Image Texture"][0]
	uber_material.node_tree.nodes.remove(node_imagemap)
	default_settings()


def default_settings():
	uber_material, node_uber = get_material_and_node()

	set_value(node_uber, "enable_diffuse", True)
	set_value(node_uber, "diffuse_use_shader_normal", True)
	set_value(node_uber, "separate_backscatter_color", False)
	node_uber.inputs['Diffuse Color']['default_value'] = (0.033, 0.26, 0.5, 1.0)
	node_uber.inputs['Diffuse Weight']['default_value'] = 1.0
	node_uber.inputs['Diffuse Roughness']['default_value'] = 0.5
	node_uber.inputs['Backscatter Color']['default_value'] = (0.5, 0.5, 0.5, 1.0)
	node_uber.inputs['Backscatter Weight']['default_value'] = 0

	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "reflection_use_shader_normal", True)
	node_uber.inputs['Reflection Color']['default_value'] = (1.0, 1.0, 1.0, 1.0)
	node_uber.inputs['Reflection IOR']['default_value'] = 2.4
	node_uber.inputs['Reflection Anisotropy']['default_value'] = 0.0
	node_uber.inputs['Reflection Anisotropy Rotation']['default_value'] = 0.0
	node_uber.inputs['Reflection Metalness']['default_value'] = 0.0
	node_uber.inputs['Reflection Roughness']['default_value'] = 0.4
	node_uber.inputs['Reflection Weight']['default_value'] = 1.0
	
	set_value(node_uber, "enable_coating", False)
	set_value(node_uber, "coating_use_shader_normal", True)
	node_uber.inputs['Coating Color']['default_value'] = (1.0, 1.0, 1.0, 1.0)
	node_uber.inputs['Coating Weight']['default_value'] = 1.0
	node_uber.inputs['Coating IOR']['default_value'] = 1.5
	node_uber.inputs['Coating Roughness']['default_value'] = 0.01
	node_uber.inputs['Coating Thickness']['default_value'] = 0
	node_uber.inputs['Coating Transmission Color']['default_value'] = (1.0, 1.0, 1.0, 1.0)
   
	set_value(node_uber, "enable_refraction", False)
	set_value(node_uber, "refraction_caustics", False)
	set_value(node_uber, "refraction_thin_surface", False)
	set_value(node_uber, "refraction_use_shader_normal", True)
	node_uber.inputs['Refraction Color']['default_value'] = (1.0, 1.0, 1.0, 1.0)
	node_uber.inputs['Refraction Weight']['default_value'] = 1.0
	node_uber.inputs['Refraction Roughness']['default_value'] = 0
	node_uber.inputs['Refraction IOR']['default_value'] = 1.5
	node_uber.inputs['Refraction Absorption Color']['default_value'] = (1.0, 1.0, 1.0, 1.0)
	node_uber.inputs['Refraction Absorption Distance']['default_value'] = 0
					  
	set_value(node_uber, "enable_sheen", False)
	node_uber.inputs['Sheen Color']['default_value'] = (0.5, 0.5, 0.5, 1.0)
	node_uber.inputs['Sheen Tint']['default_value'] = 0.5
	node_uber.inputs['Sheen Weight']['default_value'] = 1.0
	
	set_value(node_uber, "enable_emission", False)
	set_value(node_uber, "emission_doublesided", False)
	set_value(node_uber, "emission_intensity", 1.0)
	node_uber.inputs['Emission Color']['default_value'] = (1.0, 1.0, 1.0, 1.0)
	node_uber.inputs['Emission Weight']['default_value'] = 1.0
	
	set_value(node_uber, "enable_sss", False)
	set_value(node_uber, "sss_multiscatter", False)
	set_value(node_uber, "sss_use_diffuse_color", False)
	node_uber.inputs['Subsurface Color']['default_value'] = (0.436, 0.227, 0.131, 1.0)
	node_uber.inputs['Subsurface Direction']['default_value'] = 0
	node_uber.inputs['Subsurface Radius']['default_value'] = (3.67, 1.37, 0.68)
	node_uber.inputs['Subsurface Weight']['default_value'] = 1.0

	set_value(node_uber, "enable_normal", False)

	set_value(node_uber, "enable_transparency", False)
	node_uber.inputs['Transparency']['default_value'] = 0

	set_value(node_uber, "enable_displacement", False)


def uber_001():
	default_settings()
	create_imagemap("Diffuse Color", "diffuseColor.png")


def uber_002():
	create_imagemap("Diffuse Color", "diffuseColor.tga")


def uber_003():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	node_uber.inputs['Diffuse Weight']['default_value'] = 0
	node_uber.inputs['Diffuse Roughness']['default_value'] = 0


def uber_004():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	node_uber.inputs['Diffuse Weight']['default_value'] = 0.5
	node_uber.inputs['Diffuse Roughness']['default_value'] = 0.5


def uber_005():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	node_uber.inputs['Diffuse Weight']['default_value'] = 1.0
	node_uber.inputs['Diffuse Roughness']['default_value'] = 1.0


def uber_006():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	create_imagemap("Diffuse Weight", "diffuseWeight.png")


def uber_007():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	create_imagemap("Diffuse Weight", "diffuseWeight.tga")


def uber_008():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "diffuse_use_shader_normal", False)
	create_normal_map("Diffuse Normal", "normal.png")


def uber_009():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Backscatter Weight']['default_value'] = 0.5


def uber_010():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Backscatter Weight']['default_value'] = 1.0


def uber_011():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_coating", True)
	create_imagemap("Coating Color", "coatColor.png")


def uber_012():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_coating", True)
	create_imagemap("Coating Color", "coatColor.png")


def uber_013():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)


def uber_014():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating Weight']['default_value'] = 0


def uber_015():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating Weight']['default_value'] = 0.5


def uber_016():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating Roughness']['default_value'] = 0.5


def uber_017():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating Roughness']['default_value'] = 1.0


def uber_018():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating IOR']['default_value'] = 1.0


def uber_019():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating IOR']['default_value'] = 3.0


def uber_020():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating Thickness']['default_value'] = 1.0

def uber_021():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating Thickness']['default_value'] = 3.0

def uber_022():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating Transmission Color']['default_value'] = (0, 0.8, 0, 1.0)


def uber_022():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_coating", True)
	node_uber.inputs['Coating Transmission Color']['default_value'] = (0, 0.8, 0, 1.0)


def uber_023():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_coating", True)
	set_value(node_uber, "coating_use_shader_normal", False)
	create_normal_map("Coating Normal", "normal.png")


def uber_024():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	create_imagemap("Reflection Color", "reflectionColor.png")


def uber_025():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	create_imagemap("Reflection Color", "reflectionColor.tga")


def uber_026():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	create_imagemap("Reflection Weight", "reflectionWeight.png")


def uber_027():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	create_imagemap("Reflection Weight", "reflectionWeight.tga")


def uber_028():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	node_uber.inputs['Reflection Weight']['default_value'] = 0


def uber_029():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	node_uber.inputs['Reflection Anisotropy']['default_value'] = -1


def uber_030():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	node_uber.inputs['Reflection Anisotropy']['default_value'] = 1


def uber_031():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	node_uber.inputs['Reflection Anisotropy']['default_value'] = 1
	node_uber.inputs['Reflection Anisotropy Rotation']['default_value'] = 1.5708


def uber_032():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	node_uber.inputs['Reflection Roughness']['default_value'] = 0


def uber_033():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	node_uber.inputs['Reflection Roughness']['default_value'] = 1


def uber_034():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	node_uber.inputs['Reflection IOR']['default_value'] = 0


def uber_035():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	node_uber.inputs['Reflection IOR']['default_value'] = 3


def uber_036():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "reflection_use_shader_normal", False)
	create_normal_map("Reflection Normal", "normal.png")


def uber_037():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'METALNESS')
	create_imagemap("Reflection Color", "reflectionColor.png")


def uber_038():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'METALNESS')
	create_imagemap("Reflection Color", "reflectionColor.tga")


def uber_039():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'METALNESS')
	create_imagemap("Reflection Weight", "reflectionWeight.png")

def uber_040():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'METALNESS')
	create_imagemap("Reflection Weight", "reflectionWeight.tga")


def uber_041():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'METALNESS')
	node_uber.inputs['Reflection Metalness']['default_value'] = 0.5


def uber_042():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'METALNESS')
	node_uber.inputs['Reflection Metalness']['default_value'] = 1


def uber_043():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	create_imagemap("Refraction Color", "refractionColor.png")


def uber_044():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	create_imagemap("Refraction Color", "refractionColor.tga")


def uber_045():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	create_imagemap("Refraction Weight", "refractionWeight.png")


def uber_046():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	create_imagemap("Refraction Weight", "refractionWeight.tga")


def uber_047():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	set_value(node_uber, "refraction_thin_surface", True)


def uber_048():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	node_uber.inputs['Refraction Weight']['default_value'] = 0


def uber_049():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	node_uber.inputs['Refraction Weight']['default_value'] = 0.5


def uber_050():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	node_uber.inputs['Refraction Roughness']['default_value'] = 0.5


def uber_051():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	node_uber.inputs['Refraction Roughness']['default_value'] = 1


def uber_052():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	set_value(node_uber, "refraction_caustics", True)
	node_uber.inputs['Refraction IOR']['default_value'] = 1


def uber_053():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	set_value(node_uber, "refraction_caustics", True)
	node_uber.inputs['Refraction IOR']['default_value'] = 3


def uber_054():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_reflection", True)
	set_value(node_uber, "reflection_mode", 'PBR')
	set_value(node_uber, "enable_refraction", True)
	set_value(node_uber, "refraction_use_shader_normal", False)
	create_normal_map("Refraction Normal", "normal.png")


def uber_055():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_sheen", True)
	node_uber.inputs['Sheen Color']['default_value'] = (1.0, 1.0, 1.0, 1.0)


def uber_056():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_sheen", True)
	node_uber.inputs['Sheen Color']['default_value'] = (1.0, 1.0, 1.0, 1.0)
	node_uber.inputs['Sheen Weight']['default_value'] = 0


def uber_057():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_sheen", True)
	node_uber.inputs['Sheen Color']['default_value'] = (1.0, 1.0, 1.0, 1.0)
	node_uber.inputs['Sheen Weight']['default_value'] = 0.5


def uber_058():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_sheen", True)
	node_uber.inputs['Sheen Tint']['default_value'] = 0


def uber_059():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_sheen", True)
	node_uber.inputs['Sheen Tint']['default_value'] = 1


def uber_060():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	create_imagemap("Emission Color", "emissiveColor.png")


def uber_061():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	create_imagemap("Emission Color", "emissiveColor.tga")


def uber_062():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	create_imagemap("Emission Weight", "emissiveWeight.png")

def uber_063():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	create_imagemap("Emission Weight", "emissiveWeight.tga")


def uber_064():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	node_uber.inputs['Emission Color']['default_value'] = (0, 0.1, 0, 1.0)


def uber_065():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	node_uber.inputs['Emission Weight']['default_value'] = 0


def uber_066():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	node_uber.inputs['Emission Weight']['default_value'] = 0.5


def uber_067():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	set_value(node_uber, "emission_intensity", 0)


def uber_068():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	set_value(node_uber, "emission_intensity", 100)


def uber_069():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs['Diffuse Color']['default_value'] = (0, 0.4, 0, 1.0)
	set_value(node_uber, "enable_emission", True)
	set_value(node_uber, "emission_doublesided", True)
	set_value(node_uber, "emission_intensity", 3)


def uber_070():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	create_imagemap("Subsurface Color", "sssColor.png")


def uber_071():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	create_imagemap("Subsurface Color", "sssColor.tga")


def uber_072():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	create_imagemap("Subsurface Weight", "sssWeight.png")


def uber_073():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	create_imagemap("Subsurface Weight", "sssWeight.tga")


def uber_074():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	set_value(node_uber, "sss_use_diffuse_color", True)


def uber_075():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	set_value(node_uber, "sss_multiscatter", True)


def uber_076():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	node_uber.inputs['Subsurface Color']['default_value'] = (0, 0.4, 0, 1.0)


def uber_077():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	node_uber.inputs['Subsurface Weight']['default_value'] = 0


def uber_078():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	node_uber.inputs['Subsurface Weight']['default_value'] = 0.5


def uber_079():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	node_uber.inputs['Subsurface Direction']['default_value'] = -1


def uber_080():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	node_uber.inputs['Subsurface Direction']['default_value'] = 1


def uber_081():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	node_uber.inputs['Subsurface Radius']['default_value'] = (0, 0, 0)


def uber_082():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_sss", True)
	node_uber.inputs['Subsurface Radius']['default_value'] = (5, 5, 5)


def uber_083():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_normal", True)
	create_normal_map("Normal", "normal.png")

	
def uber_084():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_normal", True)
	create_normal_map("Normal", "normal.tga")


def uber_085():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_transparency", True)
	create_imagemap("Transparency", "transparency.png")

def uber_086():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_transparency", True)
	create_imagemap("Transparency", "transparency.tga")


def uber_087():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_transparency", True)
	node_uber.inputs['Transparency']['default_value'] = 0


def uber_088():
	uber_material, node_uber = get_material_and_node()
	set_value(node_uber, "enable_transparency", True)
	node_uber.inputs['Transparency']['default_value'] = 0.5


if __name__ == '__main__':

	list_tests = [
		# Diffuse
		["BL28_MAT_UBR_001", ["diffuseColor.png"], "UBER.blend", uber_001, delete_imagemap],
		["BL28_MAT_UBR_002", ["diffuseColor.tga"], "UBER.blend", uber_002, delete_imagemap],
		["BL28_MAT_UBR_003", ["Diffuse Color green", "diffuse roughness 0", "diffuse weight 0"], "UBER.blend", uber_003, default_settings],
		["BL28_MAT_UBR_004", ["Diffuse Color green", "diffuse roughness 0.5", "diffuse weight 0.5"], "UBER.blend", uber_004, default_settings],
		["BL28_MAT_UBR_005", ["Diffuse Color green", "diffuse roughness 1", "diffuse weight 1"], "UBER.blend", uber_005, default_settings],
		["BL28_MAT_UBR_006", ["Diffuse Color green", "diffuse weight png"], "UBER.blend", uber_006, delete_imagemap],
		["BL28_MAT_UBR_007", ["Diffuse Color green", "diffuse weight tga"], "UBER.blend", uber_007, delete_imagemap],
		["BL28_MAT_UBR_008", ["Diffuse Normal Map"], "UBER.blend", uber_008, delete_normalmap],
		["BL28_MAT_UBR_009", ["Backscattering Weight - 0.5"], "UBER.blend", uber_009, default_settings],
		["BL28_MAT_UBR_010", ["Backscattering Weight - 1"], "UBER.blend", uber_010, default_settings],
		# Coating
		["BL28_MAT_UBR_011", ["coatColor.png"], "UBER.blend", uber_011, delete_imagemap],
		["BL28_MAT_UBR_012", ["coatColor.tga"], "UBER.blend", uber_012, delete_imagemap],
		["BL28_MAT_UBR_013", ["Diffuse Color green", "coating weight 1"], "UBER.blend", uber_013, default_settings],
		["BL28_MAT_UBR_014", ["Diffuse Color green", "coating weight 0"], "UBER.blend", uber_014, default_settings],
		["BL28_MAT_UBR_015", ["Diffuse Color green", "coating weight 0.5"], "UBER.blend", uber_015, default_settings],
		["BL28_MAT_UBR_016", ["Diffuse Color green", "coating roughness 0"], "UBER.blend", uber_016, default_settings],
		["BL28_MAT_UBR_017", ["Diffuse Color green", "coating roughness 0.5"], "UBER.blend", uber_017, default_settings],
		["BL28_MAT_UBR_018", ["Diffuse Color green", "coating ior 1"], "UBER.blend", uber_018, default_settings],
		["BL28_MAT_UBR_019", ["Diffuse Color green", "coating ior 3"], "UBER.blend", uber_019, default_settings],
		["BL28_MAT_UBR_020", ["Diffuse Color green", "coating thickness 1"], "UBER.blend", uber_020, default_settings],
		["BL28_MAT_UBR_021", ["Diffuse Color green", "coating thickness 3"], "UBER.blend", uber_021, default_settings],
		["BL28_MAT_UBR_022", ["Diffuse Color green", "Coating Transmission Color green"], "UBER.blend", uber_022, default_settings],
		["BL28_MAT_UBR_023", ["Coating Normal Map"], "UBER.blend", uber_023, delete_normalmap],
		# Reflection
		["BL28_MAT_UBR_024", ["reflectionColor.png"], "UBER.blend", uber_024, delete_imagemap],
		["BL28_MAT_UBR_025", ["reflectionColor.tga"], "UBER.blend", uber_025, delete_imagemap],
		["BL28_MAT_UBR_026", ["reflectionWeight.png"], "UBER.blend", uber_026, delete_imagemap],
		["BL28_MAT_UBR_027", ["reflectionWeight.tga"], "UBER.blend", uber_027, delete_imagemap],
		["BL28_MAT_UBR_028", ["Diffuse Color green", "Reflection Weight 0"], "UBER.blend", uber_028, default_settings],
		["BL28_MAT_UBR_029", ["Diffuse Color green", "Reflection Anisotropy -1"], "UBER.blend", uber_029, default_settings],
		["BL28_MAT_UBR_030", ["Diffuse Color green", "Reflection Anisotropy 1"], "UBER.blend", uber_030, default_settings],
		["BL28_MAT_UBR_031", ["Diffuse Color green", "Reflection Anisotropy 1", "Reflection Anisotropy Rotation 90"], "UBER.blend", uber_031, default_settings],
		["BL28_MAT_UBR_032", ["Diffuse Color green", "Reflection Roughness 0"], "UBER.blend", uber_032, default_settings],
		["BL28_MAT_UBR_033", ["Diffuse Color green", "Reflection Roughness 1"], "UBER.blend", uber_033, default_settings],
		["BL28_MAT_UBR_034", ["Diffuse Color green", "Reflection IOR 0"], "UBER.blend", uber_034, default_settings],
		["BL28_MAT_UBR_035", ["Diffuse Color green", "Reflection IOR 3"], "UBER.blend", uber_035, default_settings],
		["BL28_MAT_UBR_036", ["Reflection Normal Map"], "UBER.blend", uber_036, delete_normalmap],
		["BL28_MAT_UBR_037", ["reflectionColor.png", "Reflection Mode Metalness"], "UBER.blend", uber_037, delete_imagemap],
		["BL28_MAT_UBR_038", ["reflectionColor.tga", "Reflection Mode Metalness"], "UBER.blend", uber_038, delete_imagemap],
		["BL28_MAT_UBR_039", ["reflectionWeight.png", "Reflection Mode Metalness"], "UBER.blend", uber_039, delete_imagemap],
		["BL28_MAT_UBR_040", ["reflectionWeight.tga", "Reflection Mode Metalness"], "UBER.blend", uber_040, delete_imagemap],
		["BL28_MAT_UBR_041", ["Reflection Mode Metalness", "Metalness 0.5"], "UBER.blend", uber_041, default_settings],
		["BL28_MAT_UBR_042", ["Reflection Mode Metalness", "Metalness 1"], "UBER.blend", uber_042, default_settings],
		# Refraction
		["BL28_MAT_UBR_043", ["refractionColor.png"], "UBER.blend", uber_043, delete_imagemap],
		["BL28_MAT_UBR_044", ["refractionColor.tga"], "UBER.blend", uber_044, delete_imagemap],
		["BL28_MAT_UBR_045", ["refractionWeight.png"], "UBER.blend", uber_045, delete_imagemap],
		["BL28_MAT_UBR_046", ["refractionWeight.tga"], "UBER.blend", uber_046, delete_imagemap],
		["BL28_MAT_UBR_047", ["Diffuse Color green", "Refraction Thin Surface"], "UBER.blend", uber_047, default_settings],
		["BL28_MAT_UBR_048", ["Diffuse Color green", "Refraction Weight 0"], "UBER.blend", uber_048, default_settings],
		["BL28_MAT_UBR_049", ["Diffuse Color green", "Refraction Weight 0.5"], "UBER.blend", uber_049, default_settings],
		["BL28_MAT_UBR_050", ["Diffuse Color green", "Refraction Roughness 0.5"], "UBER.blend", uber_050, default_settings],
		["BL28_MAT_UBR_051", ["Diffuse Color green", "Refraction Roughness 1"], "UBER.blend", uber_051, default_settings],
		["BL28_MAT_UBR_052", ["Diffuse Color green", "Refraction IOR 1", "Allow caustics"], "UBER.blend", uber_052, default_settings],
		["BL28_MAT_UBR_053", ["Diffuse Color green", "Refraction IOR 3", "Allow caustics"], "UBER.blend", uber_053, default_settings],
		["BL28_MAT_UBR_054", ["Refraction Normal Map"], "UBER.blend", uber_054, delete_normalmap],
		# Sheen
		["BL28_MAT_UBR_055", ["Diffuse Color green", "Sheen Color white"], "UBER.blend", uber_055, default_settings],
		["BL28_MAT_UBR_056", ["Diffuse Color green", "Sheen Color white", "Sheen weight 0"], "UBER.blend", uber_056, default_settings],
		["BL28_MAT_UBR_057", ["Diffuse Color green", "Sheen Color white", "Sheen weight 0.5"], "UBER.blend", uber_057, default_settings],
		["BL28_MAT_UBR_058", ["Diffuse Color green", "Sheen Tint 0"], "UBER.blend", uber_058, default_settings],
		["BL28_MAT_UBR_059", ["Diffuse Color green", "Sheen Tint 1"], "UBER.blend", uber_059, default_settings],
		# Emission
		["BL28_MAT_UBR_060", ["Diffuse Color green", "emissiveColor.png"], "UBER.blend", uber_060, delete_imagemap],
		["BL28_MAT_UBR_061", ["Diffuse Color green", "emissiveColor.tga"], "UBER.blend", uber_061, delete_imagemap],
		["BL28_MAT_UBR_062", ["Diffuse Color green", "emissiveWeight.png"], "UBER.blend", uber_062, delete_imagemap],
		["BL28_MAT_UBR_063", ["Diffuse Color green", "emissiveWeight.tga"], "UBER.blend", uber_063, delete_imagemap],
		["BL28_MAT_UBR_064", ["Diffuse Color green", "Emission Color green"], "UBER.blend", uber_064, default_settings],
		["BL28_MAT_UBR_065", ["Diffuse Color green", "Emission Color green", "Emissive Weight 0"], "UBER.blend", uber_065, default_settings],
		["BL28_MAT_UBR_066", ["Diffuse Color green", "Emission Color green", "Emissive Weight 0.5"], "UBER.blend", uber_066, default_settings],
		["BL28_MAT_UBR_067", ["Diffuse Color green", "Emission Color green", "Emissive Intensity 0"], "UBER.blend", uber_067, default_settings],
		["BL28_MAT_UBR_068", ["Diffuse Color green", "Emission Color green", "Emissive Intensity 100"], "UBER.blend", uber_068, default_settings],
		["BL28_MAT_UBR_069", ["Diffuse Color green", "Emission Color green", "Emissive Intensity 3", "Double sided"], "UBER.blend", uber_069, default_settings],
		# SSS
		["BL28_MAT_UBR_070", ["sssColor.png"], "UBER.blend", uber_070, delete_imagemap],
		["BL28_MAT_UBR_071", ["sssColor.tga"], "UBER.blend", uber_071, delete_imagemap],
		["BL28_MAT_UBR_072", ["sssWeight.png"], "UBER.blend", uber_072, delete_imagemap],
		["BL28_MAT_UBR_073", ["sssWeight.tga"], "UBER.blend", uber_073, delete_imagemap],
		["BL28_MAT_UBR_074", ["Subsurface Use Diffuse Color"], "UBER.blend", uber_074, default_settings],
		["BL28_MAT_UBR_075", ["Subsurface Multiple Scattering"], "UBER.blend", uber_075, default_settings],
		["BL28_MAT_UBR_076", ["Subsurface Color green"], "UBER.blend", uber_076, default_settings],
		["BL28_MAT_UBR_077", ["Subsurface Weight 0"], "UBER.blend", uber_077, default_settings],
		["BL28_MAT_UBR_078", ["Subsurface Weight 0.5"], "UBER.blend", uber_078, default_settings],
		["BL28_MAT_UBR_079", ["Subsurface Direction -1"], "UBER.blend", uber_079, default_settings],
		["BL28_MAT_UBR_080", ["Subsurface Direction 1"], "UBER.blend", uber_080, default_settings],
		["BL28_MAT_UBR_081", ["Subsurface Radius 0 0 0"], "UBER.blend", uber_081, default_settings],
		["BL28_MAT_UBR_082", ["Subsurface Radius 5 5 5"], "UBER.blend", uber_082, default_settings],
		# Normal
		["BL28_MAT_UBR_083", ["Diffuse Color green", "Normal Map png"], "UBER.blend", uber_083, delete_normalmap],
		["BL28_MAT_UBR_084", ["Diffuse Color green", "Normal Map tga"], "UBER.blend", uber_084, delete_normalmap],
		# Transparency
		["BL28_MAT_UBR_085", ["transparency.png"], "UBER.blend", uber_085, delete_imagemap],
		["BL28_MAT_UBR_086", ["transparency.tga"], "UBER.blend", uber_086, delete_imagemap],
		["BL28_MAT_UBR_087", ["Transparency 0"], "UBER.blend", uber_087, default_settings],
		["BL28_MAT_UBR_088", ["Transparency 0.5"], "UBER.blend", uber_088, default_settings]
	]

	launch_tests()

