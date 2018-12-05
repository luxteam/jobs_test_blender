

def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[4]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[4]))

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
	
	# make changes
	test_list[2]()
	# render
	render(test_list[0], test_list[1])
	# undo changes
	test_list[3]()			

	return 1

def get_material_and_node():
	uber_material = [e for e in bpy.data.materials if e.name == "Uber"][0]
	node_uber = [n for n in uber_material.node_tree.nodes if n.name=="RPR Uber"][0]
	return uber_material, node_uber

def create_imagemap(attr, image_name):
	uber_material, node_uber = get_material_and_node()
	tree = uber_material.node_tree

	# create image map
	node_imagemap = tree.nodes.new(type='rpr_texture_node_image_map')
	image_path = os.path.join(r"{res_path}", "Maps", image_name)
	image = bpy.data.images.load(image_path)
	node_imagemap.image = image

	if attr == "diffuse_color":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.diffuse_color])
	elif attr == "diffuse_weight":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.diffuse_weight])
	elif attr == "coating_color":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.coating_color])
	elif attr == "reflection_color":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.reflection_color])
	elif attr == "reflection_weight":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.reflection_weight])
	elif attr == "refraction_color":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.refraction_color])
	elif attr == "reflraction_weight":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.refraction_weight])
	elif attr == "emissive_color":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.emissive_color])
	elif attr == "emissive_weight":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.emissive_weight])
	elif attr == "subsurface_weight":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.subsurface_weight])
	elif attr == "subsurface_scatter_color":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.subsurface_scatter_color])
	elif attr == "normal_in":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.normal_in])
	elif attr == "transparency_value":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.transparency_value])
	elif attr == "displacement_map":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_uber.inputs[node_uber.displacement_map])


def delete_imagemap():
	uber_material, node_uber = get_material_and_node()
	node_imagemap = [n for n in uber_material.node_tree.nodes if n.name=="RPR Image Map"][0]
	uber_material.node_tree.nodes.remove(node_imagemap)
	default_settings()


def default_settings():
	uber_material, node_uber = get_material_and_node()

	node_uber.diffuse = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0.5, 0.5, 0.5, 1.0)
	node_uber.inputs[node_uber.diffuse_weight].default_value = 1
	node_uber.inputs[node_uber.diffuse_roughness].default_value = 0.5
	node_uber.inputs[node_uber.backscatter_weight].default_value = 0

	node_uber.coating = False
	node_uber.inputs[node_uber.coating_color].default_value = (1, 1, 1, 1.0)
	node_uber.inputs[node_uber.coating_weight].default_value = 1
	node_uber.inputs[node_uber.coating_roughness].default_value = 0.01
	node_uber.inputs[node_uber.coating_ior].default_value = 1.5
	node_uber.inputs[node_uber.coating_thickness].default_value = 0
	node_uber.inputs[node_uber.coating_transmission_color].default_value = (1, 1, 1, 1.0)

	node_uber.reflection = False
	node_uber.reflection_mode = 'IOR'
	node_uber.inputs[node_uber.reflection_color].default_value = (1, 1, 1, 1.0)
	node_uber.inputs[node_uber.reflection_weight].default_value = 1
	node_uber.inputs[node_uber.reflection_roughness].default_value = 0.1
	node_uber.inputs[node_uber.reflection_ior].default_value = 1.5
	node_uber.inputs[node_uber.reflection_metalness].default_value = 0
	node_uber.inputs[node_uber.reflection_anisotropy].default_value = 0
	node_uber.inputs[node_uber.reflection_anisotropy_rotation].default_value = 0

	node_uber.refraction = False
	node_uber.inputs[node_uber.refraction_color].default_value = (1, 1, 1, 1.0)
	node_uber.inputs[node_uber.refraction_weight].default_value = 1
	node_uber.inputs[node_uber.refraction_roughness].default_value = 0
	node_uber.inputs[node_uber.refraction_ior].default_value = 1.5
	node_uber.inputs[node_uber.refraction_absorption_distance].default_value = 1
	node_uber.refraction_thin_surface = False
	node_uber.refraction_caustics = False

	node_uber.sheen = False
	node_uber.inputs[node_uber.sheen_color].default_value = (0.5, 0.5, 0.5, 1.0)
	node_uber.inputs[node_uber.sheen_tint].default_value = 0.5
	node_uber.inputs[node_uber.sheen_weight].default_value = 1

	node_uber.emissive = False
	node_uber.inputs[node_uber.emissive_color].default_value =  (1, 1, 1, 1.0)
	node_uber.inputs[node_uber.emissive_weight].default_value = 1
	node_uber.inputs[node_uber.emissive_intensity].default_value = 1
	node_uber.emissive_double_sided = False

	node_uber.subsurface = False
	node_uber.inputs[node_uber.subsurface_scatter_color].default_value =  (0.436, 0.227, 0.131, 1.0)
	node_uber.inputs[node_uber.subsurface_weight].default_value = 1
	node_uber.inputs[node_uber.subsurface_scatter_direction].default_value = 0
	node_uber.inputs[node_uber.subsurface_radius].default_value[0] = 3.67
	node_uber.inputs[node_uber.subsurface_radius].default_value[1] = 1.37
	node_uber.inputs[node_uber.subsurface_radius].default_value[2] = 0.68
	node_uber.subsurface_multiple_scattering = False
	node_uber.subsurface_use_diffuse_color = False

	node_uber.normal = False
	# node_uber.normal_in for connection

	node_uber.transparency = False
	node_uber.inputs[node_uber.transparency_value].default_value = 1

	node_uber.displacement = False
	# node_uber.displacement_map for connection


def uber_001():
	create_imagemap("diffuse_color", "diffuseColor.png")

def uber_002():
	create_imagemap("diffuse_color", "diffuseColor.tga")

def uber_003():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.diffuse_roughness].default_value = 0
	node_uber.inputs[node_uber.diffuse].default_value = 0

def uber_004():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.diffuse_roughness].default_value = 0.5
	node_uber.inputs[node_uber.diffuse].default_value = 0.5

def uber_005():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.diffuse_roughness].default_value = 1
	node_uber.inputs[node_uber.diffuse].default_value = 1

def uber_006():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	create_imagemap("diffuse_weight", "diffuseWeight.png")

def uber_007():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	create_imagemap("diffuse_weight", "diffuseWeight.tga")

def uber_008():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.backscatter_weight].default_value = 0.5

def uber_009():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.backscatter_weight].default_value = 1

def uber_010():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	create_imagemap("coating_color", "coatColor.png")

def uber_011():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	create_imagemap("coating_color", "coatColor.tga")

def uber_012():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)

def uber_013():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.coating_weight].default_value = 0

def uber_014():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.coating_weight].default_value = 0.5

def uber_015():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.coating_roughness].default_value = 0.5

def uber_016():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.coating_roughness].default_value = 1

def uber_017():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.coating_ior].default_value = 1

def uber_018():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.coating_ior].default_value = 3

def uber_019():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.coating_thickness].default_value = 1

def uber_020():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.coating_thickness].default_value = 3

def uber_021():
	uber_material, node_uber = get_material_and_node()
	node_uber.coating = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.coating_transmission_color].default_value = (0, 0.8, 0, 1.0)

def uber_022():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	create_imagemap("reflection_color", "reflectionColor.png")

def uber_023():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	create_imagemap("reflection_color", "reflectionColor.tga")

def uber_024():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	create_imagemap("reflection_weight", "reflectionWeight.png")

def uber_025():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	create_imagemap("reflection_weight", "reflectionWeight.tga")

def uber_026():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.reflection_weight].default_value = 0

def uber_027():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.reflection_anisotropy].default_value = 1

def uber_028():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.reflection_anisotropy].default_value = 1

def uber_029():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.reflection_anisotropy].default_value = 1
	node_uber.inputs[node_uber.reflection_anisotropy_rotation].default_value = 1.5707963705062866 # 90deg

def uber_030():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.reflection_roughness].default_value = 0

def uber_031():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.reflection_roughness].default_value = 1

def uber_032():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.reflection_ior].default_value = 1

def uber_033():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.inputs[node_uber.reflection_ior].default_value = 3

def uber_034():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.reflection_mode = 'METALNESS'
	create_imagemap("reflection_color", "reflectionColor.png")

def uber_035():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.reflection_mode = 'METALNESS'
	create_imagemap("reflection_color", "reflectionColor.tga")

def uber_036():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.reflection_mode = 'METALNESS'
	create_imagemap("reflection_weight", "reflectionWeight.png")

def uber_037():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.reflection_mode = 'METALNESS'
	create_imagemap("reflection_weight", "reflectionWeight.tga")

def uber_038():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.reflection_mode = 'METALNESS'
	node_uber.inputs[node_uber.reflection_metalness].default_value = 0.5

def uber_039():
	uber_material, node_uber = get_material_and_node()
	node_uber.reflection = True
	node_uber.reflection_mode = 'METALNESS'
	node_uber.inputs[node_uber.reflection_metalness].default_value = 1

def uber_040():
	uber_material, node_uber = get_material_and_node()
	node_uber.refraction = True
	create_imagemap("refraction_color", "refractionColor.png")

def uber_041():
	uber_material, node_uber = get_material_and_node()
	node_uber.refraction = True
	create_imagemap("refraction_color", "refractionColor.tga")

def uber_042():
	uber_material, node_uber = get_material_and_node()
	node_uber.refraction = True
	create_imagemap("refraction_weight", "refractionWeight.png")

def uber_043():
	uber_material, node_uber = get_material_and_node()
	node_uber.refraction = True
	create_imagemap("refraction_weight", "refractionWeight.tga")

def uber_044():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.refraction = True
	node_uber.refraction_thin_surface = True

def uber_045():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.refraction = True
	node_uber.inputs[node_uber.refraction_weight].default_value = 0

def uber_046():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.refraction = True
	node_uber.inputs[node_uber.refraction_weight].default_value = 0.5

def uber_047():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.refraction = True
	node_uber.inputs[node_uber.refraction_roughness].default_value = 0.5

def uber_048():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.refraction = True
	node_uber.inputs[node_uber.refraction_roughness].default_value = 1

def uber_049():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.refraction = True
	node_uber.refraction_caustics = True
	node_uber.inputs[node_uber.refraction_ior].default_value = 1

def uber_050():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.refraction = True
	node_uber.refraction_caustics = True
	node_uber.inputs[node_uber.refraction_ior].default_value = 3

def uber_051():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.sheen = True
	node_uber.inputs[node_uber.sheen_color].default_value = (1, 1, 1, 1.0)

def uber_052():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.sheen = True
	node_uber.inputs[node_uber.sheen_color].default_value = (1, 1, 1, 1.0)
	node_uber.inputs[node_uber.sheen_weight].default_value = 0

def uber_053):
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.sheen = True
	node_uber.inputs[node_uber.sheen_color].default_value = (1, 1, 1, 1.0)
	node_uber.inputs[node_uber.sheen_weight].default_value = 0.5

def uber_054():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.sheen = True
	node_uber.inputs[node_uber.sheen_tint].default_value = 0

def uber_055():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.sheen = True
	node_uber.inputs[node_uber.sheen_tint].default_value = 1

def uber_056():
	uber_material, node_uber = get_material_and_node()
	node_uber.emissive = True
	create_imagemap("emissive_color", "emissiveColor.png")

def uber_057():
	uber_material, node_uber = get_material_and_node()
	node_uber.emissive = True
	create_imagemap("emissive_color", "emissiveColor.tga")

def uber_058():
	uber_material, node_uber = get_material_and_node()
	node_uber.emissive = True
	create_imagemap("emissive_weight", "emissiveWeight.png")

def uber_059():
	uber_material, node_uber = get_material_and_node()
	node_uber.emissive = True
	create_imagemap("emissive_weight", "emissiveWeight.tga")

def uber_060():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.emissive = True
	node_uber.inputs[node_uber.emissive_color].default_value = (0, 1, 0.1, 1.0)

def uber_061():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.emissive = True
	node_uber.inputs[node_uber.emissive_color].default_value = (0, 1, 0.1, 1.0)
	node_uber.inputs[node_uber.emissive_weight].default_value = 0

def uber_062():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.emissive = True
	node_uber.inputs[node_uber.emissive_color].default_value = (0, 1, 0.1, 1.0)
	node_uber.inputs[node_uber.emissive_weight].default_value = 0.5

def uber_063):
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.emissive = True
	node_uber.inputs[node_uber.emissive_color].default_value = (0, 1, 0.1, 1.0)
	node_uber.inputs[node_uber.emissive_intensity].default_value = 0

def uber_064():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.emissive = True
	node_uber.inputs[node_uber.emissive_color].default_value = (0, 1, 0.1, 1.0)
	node_uber.inputs[node_uber.emissive_intensity].default_value = 100

def uber_065():
	uber_material, node_uber = get_material_and_node()
	node_uber.inputs[node_uber.diffuse_color].default_value = (0, 0.4, 0, 1.0)
	node_uber.emissive = True
	node_uber.emissive_double_sided = True
	node_uber.inputs[node_uber.emissive_color].default_value = (0, 1, 0.1, 1.0)
	node_uber.inputs[node_uber.emissive_intensity].default_value = 10

def uber_066():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	create_imagemap("subsurface_scatter_color", "sssColor.png")

def uber_067():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	create_imagemap("subsurface_scatter_color", "sssColor.tga")

def uber_068():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	create_imagemap("subsurface_weight", "sssWeight.png")

def uber_069():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	create_imagemap("subsurface_weight", "sssWeight.tga")

def uber_070():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	node_uber.subsurface_use_diffuse_color = True

def uber_071):
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	node_uber.subsurface_multiple_scattering = True

def uber_072():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	node_uber.inputs[node_uber.subsurface_scatter_color].default_value = (0, 0.4, 0, 1.0)

def uber_073():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	node_uber.inputs[node_uber.subsurface_weight].default_value = 0

def uber_074():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	node_uber.inputs[node_uber.subsurface_weight].default_value = 0.5

def uber_075):
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	node_uber.inputs[node_uber.subsurface_scatter_direction].default_value = -1

def uber_076():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	node_uber.inputs[node_uber.subsurface_scatter_direction].default_value = 1

def uber_077():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	node_uber.inputs[node_uber.subsurface_radius].default_value[0] = 0
	node_uber.inputs[node_uber.subsurface_radius].default_value[1] = 0
	node_uber.inputs[node_uber.subsurface_radius].default_value[2] = 0

def uber_078():
	uber_material, node_uber = get_material_and_node()
	node_uber.subsurface = True
	node_uber.inputs[node_uber.subsurface_radius].default_value[0] = 5
	node_uber.inputs[node_uber.subsurface_radius].default_value[1] = 5
	node_uber.inputs[node_uber.subsurface_radius].default_value[2] = 5

def uber_079():
	uber_material, node_uber = get_material_and_node()
	node_uber.normal = True
	create_imagemap("normal_in", "normal.png")

def uber_080():
	uber_material, node_uber = get_material_and_node()
	node_uber.normal = True
	create_imagemap("normal_in", "normal.tga")

def uber_081():
	uber_material, node_uber = get_material_and_node()
	node_uber.transparency = True
	create_imagemap("transparency_value", "transparency.png")

def uber_082():
	uber_material, node_uber = get_material_and_node()
	node_uber.transparency = True
	create_imagemap("transparency_value", "transparency.tga")

def uber_083():
	uber_material, node_uber = get_material_and_node()
	node_uber.transparency = True
	node_uber.inputs[node_uber.transparency_value].default_value = 0
	
def uber_084():
	uber_material, node_uber = get_material_and_node()
	node_uber.transparency = True
	node_uber.inputs[node_uber.transparency_value].default_value = 0.5

def uber_085():
	uber_material, node_uber = get_material_and_node()
	node_uber.displacement = True
	create_imagemap("displacement_map", "Displacement.png")

def uber_086():
	uber_material, node_uber = get_material_and_node()
	node_uber.displacement = True
	create_imagemap("displacement_map", "Displacement.tga")

if __name__ == '__main__':

	list_tests = [
	["BL_MAT_UBR_001", ["diffuseColor.png"], uber_001, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_002", ["diffuseColor.tga"], uber_002, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_003", ["diffuse Color green", "diffuse roughness 0", "diffuse weight 0"], uber_003, default_settings, "UBER.blend"],
	["BL_MAT_UBR_004", ["diffuse Color green", "diffuse roughness 0.5", "diffuse weight 0.5"], uber_004, default_settings, "UBER.blend"],
	["BL_MAT_UBR_005", ["diffuse Color green", "diffuse roughness 1", "diffuse weight 1"], uber_005, default_settings, "UBER.blend"],
	["BL_MAT_UBR_006", ["diffuse Color green", "diffuse weight png"], uber_006, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_007", ["diffuse Color green", "diffuse weight tga"], uber_007, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_008", ["backscatter weight 0.5"], uber_008, default_settings, "UBER.blend"],
	["BL_MAT_UBR_009", ["backscatter weight 1"], uber_009, default_settings, "UBER.blend"],
	["BL_MAT_UBR_010", ["coating color png"], uber_010, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_011", ["coating color tga"], uber_011, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_012", ["diffuse color green"], uber_012, default_settings, "UBER.blend"],
	["BL_MAT_UBR_013", ["diffuse color green", "coating weight 0"], uber_013, default_settings, "UBER.blend"],
	["BL_MAT_UBR_014", ["diffuse color green", "coating weight 0.5"], uber_014, default_settings, "UBER.blend"],
	["BL_MAT_UBR_015", ["diffuse color green", "coating roughness 0.5"], uber_015, default_settings, "UBER.blend"],
	["BL_MAT_UBR_016", ["diffuse color green", "coating roughness 1"], uber_016, default_settings, "UBER.blend"],
	["BL_MAT_UBR_017", ["diffuse color green", "coating ior 1"], uber_017, default_settings, "UBER.blend"],
	["BL_MAT_UBR_018", ["diffuse color green", "coating ior 3"], uber_018, default_settings, "UBER.blend"],
	["BL_MAT_UBR_019", ["diffuse color green", "coating thickness 1"], uber_019, default_settings, "UBER.blend"],
	["BL_MAT_UBR_020", ["diffuse color green", "coating thickness 3"], uber_020, default_settings, "UBER.blend"],
	["BL_MAT_UBR_021", ["diffuse color green", "coating transmission сolor green"], uber_021, default_settings, "UBER.blend"],
	["BL_MAT_UBR_022", ["reflection color png"], uber_022, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_023", ["reflection color tga"], uber_023, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_024", ["reflection weight png"], uber_024, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_025", ["reflection weight tga"], uber_025, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_026", ["diffuse color green", "reflection weight 0"], uber_026, default_settings, "UBER.blend"],
	["BL_MAT_UBR_027", ["diffuse color green", "reflection anisotropy 1"], uber_027, default_settings, "UBER.blend"],
	["BL_MAT_UBR_028", ["diffuse color green", "reflection anisotropy 1"], uber_028, default_settings, "UBER.blend"],
	["BL_MAT_UBR_029", ["diffuse color green", "reflection anisotropy 1", "reflection anisotropy rotation 90"], uber_029, default_settings, "UBER.blend"],
	["BL_MAT_UBR_030", ["diffuse color green", "reflection roughness 0"], uber_030, default_settings, "UBER.blend"],
	["BL_MAT_UBR_031", ["diffuse color green", "reflection roughness 1"], uber_031, default_settings, "UBER.blend"],
	["BL_MAT_UBR_032", ["diffuse color green", "reflection ior 1"], uber_032, default_settings, "UBER.blend"],
	["BL_MAT_UBR_033", ["diffuse color green", "reflection ior 3"], uber_033, default_settings, "UBER.blend"],
	["BL_MAT_UBR_034", ["reflection color png", "reflection mode metalness"], uber_034, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_035", ["reflection color tga", "reflection mode metalness"], uber_035, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_036", ["reflection weight png", "reflection mode metalness"], uber_036, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_037", ["reflection weight tga", "reflection mode metalness"], uber_037, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_038", ["reflection mode metalness", "metalness 0.5"], uber_032, default_settings, "UBER.blend"],
	["BL_MAT_UBR_039", ["reflection mode metalness", "metalness 1"], uber_033, default_settings, "UBER.blend"],
	["BL_MAT_UBR_040", ["refraction color png"], uber_040, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_041", ["refraction color tga"], uber_041, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_042", ["refraction weight png"], uber_042, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_043", ["refraction weight tga"], uber_043, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_044", ["refraction thin surface true"], uber_044, default_settings, "UBER.blend"],
	["BL_MAT_UBR_045", ["refraction weight 0"], uber_045, default_settings, "UBER.blend"],
	["BL_MAT_UBR_046", ["refraction weight 0.5"], uber_046, default_settings, "UBER.blend"],
	["BL_MAT_UBR_047", ["refraction roughness 0.5"], uber_047, default_settings, "UBER.blend"],
	["BL_MAT_UBR_048", ["refraction roughness 1"], uber_048, default_settings, "UBER.blend"],
	["BL_MAT_UBR_049", ["refraction ior 1", "allow caustics true"], uber_049, default_settings, "UBER.blend"],
	["BL_MAT_UBR_050", ["refraction ior 3", "allow caustics true"], uber_050, default_settings, "UBER.blend"],
	["BL_MAT_UBR_051", ["diffuse color green", "sheen color white"], uber_051, default_settings, "UBER.blend"],
	["BL_MAT_UBR_052", ["diffuse color green", "sheen color white", "sheen weight 0"], uber_052, default_settings, "UBER.blend"],
	["BL_MAT_UBR_053", ["diffuse color green", "sheen color white", "sheen weight 0.5"], uber_053, default_settings, "UBER.blend"],
	["BL_MAT_UBR_054", ["diffuse color green", "sheen tint 0"], uber_054, default_settings, "UBER.blend"],
	["BL_MAT_UBR_055", ["diffuse color green", "sheen tint 1"], uber_055, default_settings, "UBER.blend"],
	["BL_MAT_UBR_056", ["diffuse color green", "emissive color png"], uber_056, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_057", ["diffuse color green", "emissive color tga"], uber_057, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_058", ["diffuse color green", "emissive weight png"], uber_058, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_059", ["diffuse color green", "emissive weight tga"], uber_059, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_060", ["diffuse color green", "emissive color green"], uber_060, default_settings, "UBER.blend"],
	["BL_MAT_UBR_061", ["diffuse color green", "emissive color green", "emissive weight 0"], uber_061, default_settings, "UBER.blend"],
	["BL_MAT_UBR_062", ["diffuse color green", "emissive color green", "emissive weight 0.5"], uber_062, default_settings, "UBER.blend"],
	["BL_MAT_UBR_063", ["diffuse color green", "emissive color green", "emissive intensity 0"], uber_063, default_settings, "UBER.blend"],
	["BL_MAT_UBR_064", ["diffuse color green", "emissive color green", "emissive intensity 100"], uber_064, default_settings, "UBER.blend"],
	["BL_MAT_UBR_065", ["diffuse color green", "emissive color green", "emissive intensity 10", "double sided true"], uber_065, default_settings, "UBER.blend"],
	["BL_MAT_UBR_066", ["sss color png"], uber_066, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_067", ["sss color tga"], uber_067, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_068", ["sss weight png"], uber_068, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_069", ["sss weight tga"], uber_069, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_070", ["subsurface use diffuse color true"], uber_070, default_settings, "UBER.blend"],
	["BL_MAT_UBR_071", ["subsurface multiple scattering true"], uber_071, default_settings, "UBER.blend"],
	["BL_MAT_UBR_072", ["subsurface scatter color green"], uber_072, default_settings, "UBER.blend"],
	["BL_MAT_UBR_073", ["subsurface weight 0"], uber_073, default_settings, "UBER.blend"],
	["BL_MAT_UBR_074", ["subsurface weight 0.5"], uber_074, default_settings, "UBER.blend"],
	["BL_MAT_UBR_075", ["subsurface scatter direction -1"], uber_075, default_settings, "UBER.blend"],
	["BL_MAT_UBR_076", ["subsurface scatter direction 1"], uber_076, default_settings, "UBER.blend"],
	["BL_MAT_UBR_077", ["subsurface radius 0 0 0"], uber_077, default_settings, "UBER.blend"],
	["BL_MAT_UBR_078", ["subsurface radius 5 5 5"], uber_078, default_settings, "UBER.blend"],
	["BL_MAT_UBR_079", ["normal png"], uber_079, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_080", ["normal tga"], uber_080, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_081", ["transparency png"], uber_081, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_082", ["transparency tga"], uber_082, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_083", ["transparency 0"], uber_083, default_settings, "UBER.blend"],
	["BL_MAT_UBR_084", ["transparency 0.5"], uber_084, default_settings, "UBER.blend"],
	["BL_MAT_UBR_085", ["displacement png"], uber_085, delete_imagemap, "UBER.blend"],
	["BL_MAT_UBR_086", ["displacement tga"], uber_086, delete_imagemap, "UBER.blend"]
	]

	launch_tests()

