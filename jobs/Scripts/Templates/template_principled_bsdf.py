
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
	resetSceneAttributes()

	return 1


def get_material_and_node():
	prbsdf_material = [e for e in bpy.data.materials if e.name == "Principled BSDF"][0]
	prbsdf_node = [n for n in prbsdf_material.node_tree.nodes if n.type=="BSDF_PRINCIPLED"][0]
	return prbsdf_material, prbsdf_node


def create_normal_map(attr, image_name):
	prbsdf_material, prbsdf_node = get_material_and_node()
	tree = prbsdf_material.node_tree

	# create image map
	imagemap_node = tree.nodes.new(type='ShaderNodeTexImage')
	image = bpy.data.images.load(os.path.join(r"{resource_path}", "Maps", image_name))
	imagemap_node.image = image

	# crete normal map
	normalmap_node = tree.nodes.new(type='ShaderNodeNormalMap')
	tree.links.new(imagemap_node.outputs['Color'], normalmap_node.inputs['Normal'])

	# connect normal with material
	tree.links.new(normalmap_node.outputs['Normal'], prbsdf_node.inputs[attr])


def create_imagemap(attr, image_name):
	prbsdf_material, prbsdf_node = get_material_and_node()
	tree = prbsdf_material.node_tree

	imagemap_node = tree.nodes.new(type='ShaderNodeTexImage')
	image = bpy.data.images.load(os.path.join(r"{resource_path}", "Maps", image_name))
	imagemap_node.image = image
	
	if type(prbsdf_node.inputs[attr].default_value) == float:
		tree.links.new(imagemap_node.outputs['Alpha'], prbsdf_node.inputs[attr])
	else:
		tree.links.new(imagemap_node.outputs['Color'], prbsdf_node.inputs[attr])


def delete_imagemaps(prbsdf_material):
	normal_nodes = [n for n in prbsdf_material.node_tree.nodes if n.type=="NORMAL"]
	for normal_node in normal_nodes:
		prbsdf_material.node_tree.nodes.remove(normal_node)

	imagemap_nodes = [n for n in prbsdf_material.node_tree.nodes if n.type=="TEX_IMAGE"]
	for imagemap_node in imagemap_nodes:
		prbsdf_material.node_tree.nodes.remove(imagemap_node)


def resetSceneAttributes():
	prbsdf_material, prbsdf_node = get_material_and_node()
	delete_imagemaps(prbsdf_material)

	prbsdf_node.inputs['Base Color'].default_value = (0.8, 0.8, 0.8, 1.0)
	prbsdf_node.inputs['Subsurface'].default_value = 0
	prbsdf_node.inputs['Subsurface Radius'].default_value = (1, 0.2, 0.1)
	prbsdf_node.inputs['Subsurface Color'].default_value = (0.8, 0.8, 0.8, 1.0)
	prbsdf_node.inputs['Metallic'].default_value = 0
	prbsdf_node.inputs['Specular'].default_value = 0
	prbsdf_node.inputs['Specular Tint'].default_value = 0
	prbsdf_node.inputs['Roughness'].default_value = 0
	prbsdf_node.inputs['Anisotropic'].default_value = 0
	prbsdf_node.inputs['Anisotropic Rotation'].default_value = 0
	prbsdf_node.inputs['Sheen'].default_value = 0
	prbsdf_node.inputs['Sheen Tint'].default_value = 0
	prbsdf_node.inputs['Clearcoat'].default_value = 0
	prbsdf_node.inputs['Clearcoat Roughness'].default_value = 0
	prbsdf_node.inputs['IOR'].default_value = 1.45
	prbsdf_node.inputs['Transmission'].default_value = 0
	prbsdf_node.inputs['Transmission Roughness'].default_value = 0
	prbsdf_node.inputs['Emission'].default_value = (0.0, 0.0, 0.0, 1)
	prbsdf_node.inputs['Alpha'].default_value = 1


def prbsdf_001():
	create_imagemap("Base Color", "baseColor.png")


def prbsdf_002():
	create_imagemap("Base Color", "baseColor.tga")


def prbsdf_003():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)


def prbsdf_004():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface'].default_value = 1
	create_imagemap("Subsurface Color", "sssColor.png")


def prbsdf_005():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface'].default_value = 1
	create_imagemap("Subsurface Color", "sssColor.tga")


def prbsdf_006():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	create_imagemap("Subsurface", "sssWeight.png")


def prbsdf_007():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	create_imagemap("Subsurface", "sssWeight.tga")


def prbsdf_008():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Subsurface'].default_value = 0


def prbsdf_009():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Subsurface'].default_value = 0.5


def prbsdf_010():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Subsurface'].default_value = 1


def prbsdf_011():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface'].default_value = 1
	create_imagemap("Subsurface Radius", "sssRadius.png")


def prbsdf_012():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface'].default_value = 1
	create_imagemap("Subsurface Radius", "sssRadius.tga")


def prbsdf_013():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface'].default_value = 1
	prbsdf_node.inputs['Subsurface Radius'].default_value = (0, 0, 0)


def prbsdf_014():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Subsurface'].default_value = 1
	prbsdf_node.inputs['Subsurface Radius'].default_value = (5, 5, 5)


def prbsdf_015():
	create_imagemap("Metallic", "metalness.png")


def prbsdf_016():
	create_imagemap("Metallic", "metalness.tga")


def prbsdf_017():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Metallic'].default_value = 0


def prbsdf_018():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Metallic'].default_value = 0.5


def prbsdf_019():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Metallic'].default_value = 1


def prbsdf_020():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	create_imagemap("Specular", "specular.png")


def prbsdf_021():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	create_imagemap("Specular", "specular.tga")


def prbsdf_022():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	prbsdf_node.inputs['Specular'].default_value = 0


def prbsdf_023():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	prbsdf_node.inputs['Specular'].default_value = 0.5


def prbsdf_024():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	prbsdf_node.inputs['Specular'].default_value = 1


def prbsdf_025():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	prbsdf_node.inputs['Specular'].default_value = 1
	create_imagemap("Specular Tint", "specular.png")


def prbsdf_026():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	prbsdf_node.inputs['Specular'].default_value = 1
	create_imagemap("Specular Tint", "specular.tga")


def prbsdf_027():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Specular Tint'].default_value = 0


def prbsdf_028():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Specular Tint'].default_value = 0.5


def prbsdf_029():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Roughness'].default_value = 0
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Specular Tint'].default_value = 1


def prbsdf_030():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	create_imagemap("Roughness", "roughness.png")


def prbsdf_031():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	create_imagemap("Roughness", "roughness.tga")


def prbsdf_032():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Roughness'].default_value = 0


def prbsdf_033():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Roughness'].default_value = 0.5


def prbsdf_034():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Roughness'].default_value = 1


def prbsdf_035():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	create_imagemap("Anisotropic", "roughness.png")


def prbsdf_036():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	create_imagemap("Anisotropic", "roughness.tga")


def prbsdf_037():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	prbsdf_node.inputs['Anisotropic'].default_value = 0


def prbsdf_038():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	prbsdf_node.inputs['Anisotropic'].default_value = 0.5


def prbsdf_039():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	prbsdf_node.inputs['Anisotropic'].default_value = 1


def prbsdf_040():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	prbsdf_node.inputs['Anisotropic'].default_value = 1
	create_imagemap("Anisotropic Rotation", "roughness.png")


def prbsdf_041():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	prbsdf_node.inputs['Anisotropic'].default_value = 1
	create_imagemap("Anisotropic Rotation", "roughness.tga")


def prbsdf_042():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	prbsdf_node.inputs['Anisotropic'].default_value = 1
	prbsdf_node.inputs['Anisotropic Rotation'].default_value = 0


def prbsdf_043():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	prbsdf_node.inputs['Anisotropic'].default_value = 1
	prbsdf_node.inputs['Anisotropic Rotation'].default_value = 0.5


def prbsdf_044():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Metallic'].default_value = 1
	prbsdf_node.inputs['Anisotropic'].default_value = 1
	prbsdf_node.inputs['Anisotropic Rotation'].default_value = 1


def prbsdf_045():
	create_imagemap("Sheen", "roughness.png")


def prbsdf_046():
	create_imagemap("Sheen", "roughness.tga")


def prbsdf_047():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Sheen'].default_value = 0


def prbsdf_048():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Sheen'].default_value = 0.5


def prbsdf_049():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Sheen'].default_value = 1


def prbsdf_050():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Sheen'].default_value = 1
	create_imagemap("Sheen Tint", "roughness.png")


def prbsdf_051():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Sheen'].default_value = 1
	create_imagemap("Sheen Tint", "roughness.tga")


def prbsdf_052():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Sheen'].default_value = 1
	prbsdf_node.inputs['Sheen Tint'].default_value = 0


def prbsdf_053():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Sheen'].default_value = 1
	prbsdf_node.inputs['Sheen Tint'].default_value = 0.5


def prbsdf_054():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Sheen'].default_value = 1
	prbsdf_node.inputs['Sheen Tint'].default_value = 1


def prbsdf_055():
	create_imagemap("Sheen Tint", "coatColor.png")


def prbsdf_056():
	create_imagemap("Sheen Tint", "coatColor.tga")


def prbsdf_057():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Clearcoat'].default_value = 0


def prbsdf_058():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Clearcoat'].default_value = 0.5


def prbsdf_059():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Clearcoat'].default_value = 1


def prbsdf_060():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Clearcoat'].default_value = 1
	create_imagemap("Clearcoat Roughness", "roughness.png")


def prbsdf_061():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Clearcoat'].default_value = 1
	create_imagemap("Clearcoat Roughness", "roughness.tga")


def prbsdf_062():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Clearcoat'].default_value = 1
	prbsdf_node.inputs['Clearcoat Roughness'].default_value = 0


def prbsdf_063():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Clearcoat'].default_value = 1
	prbsdf_node.inputs['Clearcoat Roughness'].default_value = 0.5


def prbsdf_064():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Clearcoat'].default_value = 1
	prbsdf_node.inputs['Clearcoat Roughness'].default_value = 1


def prbsdf_065():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	create_imagemap("IOR", "glassIOR.png")


def prbsdf_066():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	create_imagemap("IOR", "glassIOR.tga")


def prbsdf_067():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['IOR'].default_value = 1


def prbsdf_068():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['IOR'].default_value = 1.5


def prbsdf_069():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['IOR'].default_value = 2


def prbsdf_070():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	create_imagemap("Transmission", "transmissionColor.png")


def prbsdf_071():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Specular'].default_value = 1
	create_imagemap("Transmission", "transmissionColor.tga")


def prbsdf_072():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Transmission'].default_value = 0


def prbsdf_073():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Transmission'].default_value = 0.5


def prbsdf_074():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Specular'].default_value = 1
	prbsdf_node.inputs['Transmission'].default_value = 1


def prbsdf_075():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Transmission'].default_value = 1
	create_imagemap("Transmission Roughness", "roughness.png")


def prbsdf_076():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Transmission'].default_value = 1
	create_imagemap("Transmission Roughness", "roughness.tga")


def prbsdf_077():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Transmission'].default_value = 1
	prbsdf_node.inputs['Transmission Roughness'].default_value = 0


def prbsdf_078():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Transmission'].default_value = 1
	prbsdf_node.inputs['Transmission Roughness'].default_value = 0.5


def prbsdf_079():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Transmission'].default_value = 1
	prbsdf_node.inputs['Transmission Roughness'].default_value = 1


def prbsdf_080():
	create_imagemap("Emission", "emissionColor.png")


def prbsdf_081():
	create_imagemap("Emission", "emissionColor.tga")


def prbsdf_082():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Emission'].default_value = (0.4, 0.4, 0.4, 1.0)


def prbsdf_083():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Emission'].default_value = (0.0907472, 0.0903746, 0.399753, 1)


def prbsdf_084():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Emission'].default_value = (0.00010286, 0, 0.399753, 1)


def prbsdf_085():
	create_imagemap("Alpha", "transparency.png")


def prbsdf_086():
	create_imagemap("Alpha", "transparency.tga")


def prbsdf_087():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Alpha'].default_value = 0


def prbsdf_088():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Alpha'].default_value = 0.5


def prbsdf_089():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Base Color'].default_value = (0.0, 0.4, 0.0, 1.0)
	prbsdf_node.inputs['Alpha'].default_value = 1


def prbsdf_090():
	create_normal_map("Normal", "normal.png")


def prbsdf_091():
	create_normal_map("Normal", "normal.tga")


def prbsdf_092():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Clearcoat'].default_value = 1
	create_normal_map("Normal", "normal.png")


def prbsdf_093():
	prbsdf_material, prbsdf_node = get_material_and_node()
	prbsdf_node.inputs['Clearcoat'].default_value = 1
	create_normal_map("Normal", "normal.tga")


if __name__ == '__main__':

	list_tests = [

		["BL28_MAT_PRBSDF_001", ["Base Color map.png"], "Principled_BSDF.blend", prbsdf_001],
		["BL28_MAT_PRBSDF_002", ["Base Color map.tga"], "Principled_BSDF.blend", prbsdf_002],
		["BL28_MAT_PRBSDF_003", ["Base color, RGB color: 0:0.4:0"], "Principled_BSDF.blend", prbsdf_003],

		["BL28_MAT_PRBSDF_004", ["Subsurface Color map.png"], "Principled_BSDF.blend", prbsdf_004],
		["BL28_MAT_PRBSDF_005", ["Subsurface Color map.tga"], "Principled_BSDF.blend", prbsdf_005],
		["BL28_MAT_PRBSDF_006", ["Subsurface Weight map.png"], "Principled_BSDF.blend", prbsdf_006],
		["BL28_MAT_PRBSDF_007", ["Subsurface Weight.tga"], "Principled_BSDF.blend", prbsdf_007],
		["BL28_MAT_PRBSDF_008", ["Subsurface Weight - 0"], "Principled_BSDF.blend", prbsdf_008],
		["BL28_MAT_PRBSDF_009", ["Subsurface Weight - 0.5"], "Principled_BSDF.blend", prbsdf_009],
		["BL28_MAT_PRBSDF_010", ["Subsurface Weight - 1"], "Principled_BSDF.blend", prbsdf_010],
		["BL28_MAT_PRBSDF_011", ["Subsurface Radius map.png"], "Principled_BSDF.blend", prbsdf_011],
		["BL28_MAT_PRBSDF_012", ["Subsurface Radius map.tga"], "Principled_BSDF.blend", prbsdf_012],
		["BL28_MAT_PRBSDF_013", ["Subsurface Radius - 0, 0, 0"], "Principled_BSDF.blend", prbsdf_013],
		["BL28_MAT_PRBSDF_014", ["Subsurface Radius - 5, 5, 5"], "Principled_BSDF.blend", prbsdf_014],

		["BL28_MAT_PRBSDF_015", ["Metallic map.png"], "Principled_BSDF.blend", prbsdf_015],
		["BL28_MAT_PRBSDF_016", ["Metallic map.tga"], "Principled_BSDF.blend", prbsdf_016],
		["BL28_MAT_PRBSDF_017", ["Metallic -  0"], "Principled_BSDF.blend", prbsdf_017],
		["BL28_MAT_PRBSDF_018", ["Metallic -  0.5"], "Principled_BSDF.blend", prbsdf_018],
		["BL28_MAT_PRBSDF_019", ["Metallic -  1"], "Principled_BSDF.blend", prbsdf_019],

		["BL28_MAT_PRBSDF_020", ["Specular map.png"], "Principled_BSDF.blend", prbsdf_020],
		["BL28_MAT_PRBSDF_021", ["Specular map.tga"], "Principled_BSDF.blend", prbsdf_021],
		["BL28_MAT_PRBSDF_022", ["Specular - 0"], "Principled_BSDF.blend", prbsdf_022],
		["BL28_MAT_PRBSDF_023", ["Specular - 0.5"], "Principled_BSDF.blend", prbsdf_023],
		["BL28_MAT_PRBSDF_024", ["Specular - 1"], "Principled_BSDF.blend", prbsdf_024],

		["BL28_MAT_PRBSDF_025", ["Specular tint map.png"], "Principled_BSDF.blend", prbsdf_025],
		["BL28_MAT_PRBSDF_026", ["Specular tint map.tga"], "Principled_BSDF.blend", prbsdf_026],
		["BL28_MAT_PRBSDF_027", ["Specular tint - 0"], "Principled_BSDF.blend", prbsdf_027],
		["BL28_MAT_PRBSDF_028", ["Specular tint - 0.5"], "Principled_BSDF.blend", prbsdf_028],
		["BL28_MAT_PRBSDF_029", ["Specular tint - 1"], "Principled_BSDF.blend", prbsdf_029],

		["BL28_MAT_PRBSDF_030", ["Roughness map.png"], "Principled_BSDF.blend", prbsdf_030],
		["BL28_MAT_PRBSDF_031", ["Roughness map.tga"], "Principled_BSDF.blend", prbsdf_031],
		["BL28_MAT_PRBSDF_032", ["Roughness - 0"], "Principled_BSDF.blend", prbsdf_032],
		["BL28_MAT_PRBSDF_033", ["Roughness - 0.5"], "Principled_BSDF.blend", prbsdf_033],
		["BL28_MAT_PRBSDF_034", ["Roughness - 1"], "Principled_BSDF.blend", prbsdf_034],

		["BL28_MAT_PRBSDF_035", ["Anisotropic map.png"], "Principled_BSDF.blend", prbsdf_035],
		["BL28_MAT_PRBSDF_036", ["Anisotropic map.tga"], "Principled_BSDF.blend", prbsdf_036],
		["BL28_MAT_PRBSDF_037", ["Anisotropic - 0"], "Principled_BSDF.blend", prbsdf_037],
		["BL28_MAT_PRBSDF_038", ["Anisotropic - 0.5"], "Principled_BSDF.blend", prbsdf_038],
		["BL28_MAT_PRBSDF_039", ["Anisotropic - 1"], "Principled_BSDF.blend", prbsdf_039],

		["BL28_MAT_PRBSDF_040", ["Anisotropic Rotation map.png"], "Principled_BSDF.blend", prbsdf_040],
		["BL28_MAT_PRBSDF_041", ["Anisotropic Rotation map.tga"], "Principled_BSDF.blend", prbsdf_041],
		["BL28_MAT_PRBSDF_042", ["Anisotropic Rotation - 0"], "Principled_BSDF.blend", prbsdf_042],
		["BL28_MAT_PRBSDF_043", ["Anisotropic Rotation - 0.5"], "Principled_BSDF.blend", prbsdf_043],
		["BL28_MAT_PRBSDF_044", ["Anisotropic Rotation - 1"], "Principled_BSDF.blend", prbsdf_044],

		["BL28_MAT_PRBSDF_045", ["Sheen map.png"], "Principled_BSDF.blend", prbsdf_045],
		["BL28_MAT_PRBSDF_046", ["Sheen map.tga"], "Principled_BSDF.blend", prbsdf_046],
		["BL28_MAT_PRBSDF_047", ["Sheen - 0"], "Principled_BSDF.blend", prbsdf_047],
		["BL28_MAT_PRBSDF_048", ["Sheen - 0.5"], "Principled_BSDF.blend", prbsdf_048],
		["BL28_MAT_PRBSDF_049", ["Sheen - 1"], "Principled_BSDF.blend", prbsdf_049],

		["BL28_MAT_PRBSDF_050", ["Sheen Tint map.png"], "Principled_BSDF.blend", prbsdf_050],
		["BL28_MAT_PRBSDF_051", ["Sheen Tint map.tga"], "Principled_BSDF.blend", prbsdf_051],
		["BL28_MAT_PRBSDF_052", ["Sheen Tint - 0"], "Principled_BSDF.blend", prbsdf_052],
		["BL28_MAT_PRBSDF_053", ["Sheen Tint - 0.5"], "Principled_BSDF.blend", prbsdf_053],
		["BL28_MAT_PRBSDF_054", ["Sheen Tint - 1"], "Principled_BSDF.blend", prbsdf_054],

		["BL28_MAT_PRBSDF_055", ["Clearcoat map.png"], "Principled_BSDF.blend", prbsdf_055],
		["BL28_MAT_PRBSDF_056", ["Clearcoat map.tga"], "Principled_BSDF.blend", prbsdf_056],
		["BL28_MAT_PRBSDF_057", ["Clearcoat - 0"], "Principled_BSDF.blend", prbsdf_057],
		["BL28_MAT_PRBSDF_058", ["Clearcoat - 0.5"], "Principled_BSDF.blend", prbsdf_058],
		["BL28_MAT_PRBSDF_059", ["Clearcoat - 1"], "Principled_BSDF.blend", prbsdf_059],

		["BL28_MAT_PRBSDF_060", ["Clearcoat Roughness map.png"], "Principled_BSDF.blend", prbsdf_060],
		["BL28_MAT_PRBSDF_061", ["Clearcoat Roughness map.tga"], "Principled_BSDF.blend", prbsdf_061],
		["BL28_MAT_PRBSDF_062", ["Clearcoat Roughness - 0"], "Principled_BSDF.blend", prbsdf_062],
		["BL28_MAT_PRBSDF_063", ["Clearcoat Roughness - 0.5"], "Principled_BSDF.blend", prbsdf_063],
		["BL28_MAT_PRBSDF_064", ["Clearcoat Roughness - 1"], "Principled_BSDF.blend", prbsdf_064],

		["BL28_MAT_PRBSDF_065", ["IOR map.png"], "Principled_BSDF.blend", prbsdf_065],
		["BL28_MAT_PRBSDF_066", ["IOR map.tga"], "Principled_BSDF.blend", prbsdf_066],
		["BL28_MAT_PRBSDF_067", ["IOR - 1"], "Principled_BSDF.blend", prbsdf_067],
		["BL28_MAT_PRBSDF_068", ["IOR - 1.5"], "Principled_BSDF.blend", prbsdf_068],
		["BL28_MAT_PRBSDF_069", ["IOR - 2"], "Principled_BSDF.blend", prbsdf_069],

		["BL28_MAT_PRBSDF_070", ["Transmission map.png"], "Principled_BSDF.blend", prbsdf_070],
		["BL28_MAT_PRBSDF_071", ["Transmission map.tga"], "Principled_BSDF.blend", prbsdf_071],
		["BL28_MAT_PRBSDF_072", ["Transmission - 0"], "Principled_BSDF.blend", prbsdf_072],
		["BL28_MAT_PRBSDF_073", ["Transmission - 0.5"], "Principled_BSDF.blend", prbsdf_073],
		["BL28_MAT_PRBSDF_074", ["Transmission - 1"], "Principled_BSDF.blend", prbsdf_074],

		["BL28_MAT_PRBSDF_075", ["Transmission Roughness map.png"], "Principled_BSDF.blend", prbsdf_075],
		["BL28_MAT_PRBSDF_076", ["Transmission Roughness map.tga"], "Principled_BSDF.blend", prbsdf_076],
		["BL28_MAT_PRBSDF_077", ["Transmission Roughness - 0"], "Principled_BSDF.blend", prbsdf_077],
		["BL28_MAT_PRBSDF_078", ["Transmission Roughness - 0.5"], "Principled_BSDF.blend", prbsdf_078],
		["BL28_MAT_PRBSDF_079", ["Transmission Roughness - 1"], "Principled_BSDF.blend", prbsdf_079],

		["BL28_MAT_PRBSDF_080", ["Emission map.png"], "Principled_BSDF.blend", prbsdf_080],
		["BL28_MAT_PRBSDF_081", ["Emission map.tga"], "Principled_BSDF.blend", prbsdf_081],
		["BL28_MAT_PRBSDF_082", ["Emission - HSV: 0.667 0 0.665"], "Principled_BSDF.blend", prbsdf_082],
		["BL28_MAT_PRBSDF_083", ["Emission - HSV: 0.667 0.5 0.666"], "Principled_BSDF.blend", prbsdf_083],
		["BL28_MAT_PRBSDF_084", ["Emission - HSV: 0.667 1 0.667"], "Principled_BSDF.blend", prbsdf_084],

		["BL28_MAT_PRBSDF_085", ["Alpha map.png"], "Principled_BSDF.blend", prbsdf_085],
		["BL28_MAT_PRBSDF_086", ["Alpha map.tga"], "Principled_BSDF.blend", prbsdf_086],
		["BL28_MAT_PRBSDF_087", ["Alpha - 0"], "Principled_BSDF.blend", prbsdf_087],
		["BL28_MAT_PRBSDF_088", ["Alpha - 0"], "Principled_BSDF.blend", prbsdf_088],
		["BL28_MAT_PRBSDF_089", ["Alpha - 0"], "Principled_BSDF.blend", prbsdf_089],

		["BL28_MAT_PRBSDF_090", ["Normal map.png"], "Principled_BSDF.blend", prbsdf_090],
		["BL28_MAT_PRBSDF_091", ["Normal map.tga"], "Principled_BSDF.blend", prbsdf_091],
		["BL28_MAT_PRBSDF_092", ["Clearcoat Normal map.png"], "Principled_BSDF.blend", prbsdf_092],
		["BL28_MAT_PRBSDF_093", ["Clearcoat Normal map.tga"], "Principled_BSDF.blend", prbsdf_093]
		
	]

	launch_tests()

