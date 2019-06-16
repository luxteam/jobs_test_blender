

def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)
	
	# make changes
	test_list[2]()
	# render
	render(test_list[0], test_list[1])
	# undo changes
	test_list[3]()			

	return 1

def get_material_and_node():
	pbr_material = [e for e in bpy.data.materials if e.name == "PBR"][0]
	node_pbr = [n for n in pbr_material.node_tree.nodes if n.name=="RPR PBR"][0]
	return pbr_material, node_pbr

def create_imagemap(attr, image_name):
	pbr_material, node_pbr = get_material_and_node()
	tree = pbr_material.node_tree

	# create image map
	node_imagemap = tree.nodes.new(type='rpr_texture_node_image_map')
	image_path = os.path.join(r"{res_path}", "Maps", image_name)
	image = bpy.data.images.load(image_path)
	node_imagemap.image = image

	if attr == "base_color":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.base_color])
	elif attr == "roughness":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.roughness])
	elif attr == "metalness":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.metalness])
	elif attr == "specular":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.specular])
	elif attr == "normal":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.normal])
	elif attr == "glass_weight":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.glass_weight])
	elif attr == "glass_ior":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.glass_ior])
	elif attr == "emissive_weight":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.emissive_weight])
	elif attr == "emissive_color":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.emissive_color])
	elif attr == "subsurface_weight":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.subsurface_weight])
	elif attr == "subsurface_color":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.subsurface_color])
	elif attr == "subsurface_radius":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_pbr.inputs[node_pbr.subsurface_radius])


def delete_imagemap():
	pbr_material, node_pbr = get_material_and_node()
	node_imagemap = [n for n in pbr_material.node_tree.nodes if n.name=="RPR Image Map"][0]
	pbr_material.node_tree.nodes.remove(node_imagemap)
	default_settings()


def default_settings():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (0.5, 0.5, 0.5, 1.0)
	node_pbr.inputs[node_pbr.roughness].default_value = 0.25
	node_pbr.inputs[node_pbr.metalness].default_value = 0
	node_pbr.inputs[node_pbr.specular].default_value = 1
	node_pbr.inputs[node_pbr.glass_weight].default_value = 0
	node_pbr.inputs[node_pbr.glass_ior].default_value = 1.5
	node_pbr.inputs[node_pbr.emissive_weight].default_value = 0
	node_pbr.inputs[node_pbr.emissive_color].default_value = (1, 1, 1, 1.0)
	node_pbr.inputs[node_pbr.subsurface_weight].default_value = 0
	node_pbr.inputs[node_pbr.subsurface_color].default_value = (0.436, 0.227, 0.131, 1.0)
	node_pbr.inputs[node_pbr.subsurface_radius].default_value = (3.67, 1.37, 0.68)
	

def pbr_001():
	create_imagemap("base_color", "baseColor.png")

def pbr_002():
	create_imagemap("base_color", "baseColor.tga")

def pbr_003():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (0, 0.4, 0, 1.0)

def pbr_004():
	create_imagemap("roughness", "roughness.png")

def pbr_005():
	create_imagemap("roughness", "roughness.tga")

def pbr_006():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (0, 0.4, 0, 1.0)
	node_pbr.inputs[node_pbr.roughness].default_value = 0

def pbr_007():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (0, 0.4, 0, 1.0)
	node_pbr.inputs[node_pbr.roughness].default_value = 0.5

def pbr_008():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (0, 0.4, 0, 1.0)
	node_pbr.inputs[node_pbr.roughness].default_value = 1

def pbr_009():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.roughness].default_value = 0
	create_imagemap("metalness", "metalness.png")

def pbr_010():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.roughness].default_value = 0
	create_imagemap("metalness", "metalness.tga")

def pbr_011():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.roughness].default_value = 0
	node_pbr.inputs[node_pbr.metalness].default_value = 0.5

def pbr_012():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.roughness].default_value = 0
	node_pbr.inputs[node_pbr.metalness].default_value = 1

def pbr_013():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.roughness].default_value = 0
	create_imagemap("specular", "metalness.png")

def pbr_014():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.roughness].default_value = 0
	create_imagemap("specular", "metalness.tga")

def pbr_015():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.roughness].default_value = 0
	node_pbr.inputs[node_pbr.specular].default_value = 0

def pbr_016():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.roughness].default_value = 0
	node_pbr.inputs[node_pbr.specular].default_value = 0.5

def pbr_017():
	create_imagemap("normal", "normal.png")

def pbr_018():
	create_imagemap("normal", "normal.tga")

def pbr_019():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (1, 1, 1, 1.0)
	create_imagemap("glass_weight", "glass.png")

def pbr_020():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (1, 1, 1, 1.0)
	create_imagemap("glass_weight", "glass.tga")

def pbr_021():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (1, 1, 1, 1.0)
	node_pbr.inputs[node_pbr.glass_weight].default_value = 0.5

def pbr_022():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (1, 1, 1, 1.0)
	node_pbr.inputs[node_pbr.glass_weight].default_value = 1
	node_pbr.inputs[node_pbr.glass_ior].default_value = 0

def pbr_023():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (1, 1, 1, 1.0)
	create_imagemap("glass_ior", "glassIOR.png")

def pbr_024():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (1, 1, 1, 1.0)
	create_imagemap("glass_ior", "glassIOR.tga")

def pbr_025():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (1, 1, 1, 1.0)
	node_pbr.inputs[node_pbr.glass_weight].default_value = 1
	node_pbr.inputs[node_pbr.glass_ior].default_value = 0

def pbr_026():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.base_color].default_value = (1, 1, 1, 1.0)
	node_pbr.inputs[node_pbr.glass_weight].default_value = 1
	node_pbr.inputs[node_pbr.glass_ior].default_value = 3

def pbr_027():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.emissive_weight].default_value = 1
	create_imagemap("emissive_color", "emissiveColor.png")

def pbr_028():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.emissive_weight].default_value = 1
	create_imagemap("emissive_color", "emissiveColor.tga")

def pbr_029():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.emissive_weight].default_value = 1
	node_pbr.inputs[node_pbr.emissive_color].default_value = (0, 0.4, 0, 1.0)

def pbr_030():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.emissive_weight].default_value = 1
	create_imagemap("emissive_weight", "emissiveWeight.png")

def pbr_031():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.emissive_weight].default_value = 1
	create_imagemap("emissive_weight", "emissiveWeight.tga")

def pbr_032():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.emissive_weight].default_value = 0.5
	node_pbr.inputs[node_pbr.emissive_color].default_value = (0, 0.4, 0, 1.0)

def pbr_033():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.emissive_weight].default_value = 1
	node_pbr.inputs[node_pbr.emissive_color].default_value = (0, 0.4, 0, 1.0)

def pbr_034():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.subsurface_weight].default_value = 1
	create_imagemap("subsurface_weight", "sssColor.png")

def pbr_035():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.subsurface_weight].default_value = 1
	create_imagemap("subsurface_weight", "sssColor.tga")

def pbr_036():
	create_imagemap("subsurface_color", "sssWeight.png")

def pbr_037():
	create_imagemap("subsurface_color", "sssWeight.tga")

def pbr_038():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.subsurface_weight].default_value = 0.5

def pbr_039():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.subsurface_weight].default_value = 1
	create_imagemap("subsurface_radius", "sssRadius.png")

def pbr_040():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.subsurface_weight].default_value = 1
	create_imagemap("subsurface_radius", "sssRadius.tga")

def pbr_041():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.subsurface_weight].default_value = 1
	node_pbr.inputs[node_pbr.subsurface_radius].default_value = (0, 0, 0)

def pbr_042():
	pbr_material, node_pbr = get_material_and_node()
	node_pbr.inputs[node_pbr.subsurface_weight].default_value = 1
	node_pbr.inputs[node_pbr.subsurface_radius].default_value = (5, 5, 5)


if __name__ == '__main__':

	list_tests = [
	["BL_MAT_PBR_001", ["base color.png"], pbr_001, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_002", ["base color.tga"], pbr_002, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_003", ["base color green"], pbr_003, default_settings, "PBR.blend"],
	["BL_MAT_PBR_004", ["roughness.png"], pbr_004, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_005", ["roughness.tga"], pbr_005, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_006", ["roughness 0"], pbr_006, default_settings, "PBR.blend"],
	["BL_MAT_PBR_007", ["roughness 0.5"], pbr_007, default_settings, "PBR.blend"],
	["BL_MAT_PBR_008", ["roughness 1"], pbr_008, default_settings, "PBR.blend"],
	["BL_MAT_PBR_009", ["metalness.png"], pbr_009, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_010", ["metalness.tga"], pbr_010, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_011", ["metalness 0.5"], pbr_011, default_settings, "PBR.blend"],
	["BL_MAT_PBR_012", ["metalness 1"], pbr_012, default_settings, "PBR.blend"],
	["BL_MAT_PBR_013", ["specular.png"], pbr_013, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_014", ["specular.tga"], pbr_014, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_015", ["specular 0"], pbr_015, default_settings, "PBR.blend"],
	["BL_MAT_PBR_016", ["specular 0.5"], pbr_016, default_settings, "PBR.blend"],
	["BL_MAT_PBR_017", ["normal.png"], pbr_017, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_018", ["normal.tga"], pbr_018, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_019", ["glass weight.png"], pbr_019, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_020", ["glass weight.tga"], pbr_020, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_021", ["glass weight 0.5"], pbr_021, default_settings, "PBR.blend"],
	["BL_MAT_PBR_022", ["glass weight 0.5", "glass_ior 0"], pbr_022, default_settings, "PBR.blend"],
	["BL_MAT_PBR_023", ["glass ior.png"], pbr_023, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_024", ["glass ior.tga"], pbr_024, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_025", ["glass weight 1", "glass_ior 0"], pbr_025, default_settings, "PBR.blend"],
	["BL_MAT_PBR_026", ["glass weight 1", "glass_ior 3"], pbr_026, default_settings, "PBR.blend"],
	["BL_MAT_PBR_027", ["emissive Color.png"], pbr_027, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_028", ["emissive Color.tga"], pbr_028, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_029", ["emissive Color green"], pbr_029, default_settings, "PBR.blend"],
	["BL_MAT_PBR_030", ["emissive Weight.png"], pbr_030, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_031", ["emissive Weight.tga"], pbr_031, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_032", ["emissive Weight 0.5", "emissive color green"], pbr_032, default_settings, "PBR.blend"],
	["BL_MAT_PBR_033", ["emissive Weight 1", "emissive color gree"], pbr_033, default_settings, "PBR.blend"],
	# ["BL_MAT_PBR_034", ["sss Color.png"], pbr_034, delete_imagemap, "PBR.blend"],
	# ["BL_MAT_PBR_035", ["sss Colort.tga"], pbr_035, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_036", ["sss Weight.png"], pbr_036, delete_imagemap, "PBR.blend"],
	["BL_MAT_PBR_037", ["sss Weight.tga"], pbr_037, delete_imagemap, "PBR.blend"],
	# ["BL_MAT_PBR_038", ["sss Weight 0.5"], pbr_038, default_settings, "PBR.blend"],
	# ["BL_MAT_PBR_039", ["sss Radius.png"], pbr_039, delete_imagemap, "PBR.blend"],
	# ["BL_MAT_PBR_040", ["sss Radius.tga"], pbr_040, delete_imagemap, "PBR.blend"],
	# ["BL_MAT_PBR_041", ["sss Radius 0 0 0"], pbr_041, default_settings, "PBR.blend"],
	# ["BL_MAT_PBR_042", ["sss Radius 5 5 5"], pbr_042, default_settings, "PBR.blend"],
	]

	launch_tests()

