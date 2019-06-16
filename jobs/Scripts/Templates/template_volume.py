

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
	volume_material = [e for e in bpy.data.materials if e.name == "Material"][0]
	node_volume = [n for n in volume_material.node_tree.nodes if n.name=="RPR Volume"][0]
	return volume_material, node_volume

def create_imagemap(attr, image_name):
	volume_material, node_volume = get_material_and_node()
	tree = volume_material.node_tree

	# create image map
	node_imagemap = tree.nodes.new(type='rpr_texture_node_image_map')
	image_path = os.path.join(r"{res_path}", "Maps", image_name)
	image = bpy.data.images.load(image_path)
	node_imagemap.image = image

	if attr == "scatter_color_in":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_volume.inputs[node_volume.scatter_color_in])
	elif attr == "transmission_color_in":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_volume.inputs[node_volume.transmission_color_in])
	elif attr == "emission_color_in":
		tree.links.new(node_imagemap.outputs[node_imagemap.value_out], node_volume.inputs[node_volume.transmission_color_in])


def delete_imagemap():
	volume_material, node_volume = get_material_and_node()
	node_imagemap = [n for n in volume_material.node_tree.nodes if n.name=="RPR Image Map"][0]
	volume_material.node_tree.nodes.remove(node_imagemap)
	default_settings()


def default_settings():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.scatter_color_in].default_value = (1, 1, 1, 1.0)
	node_volume.inputs[node_volume.scattering_direction_in].default_value = 0
	node_volume.inputs[node_volume.emission_color_in].default_value = (1, 1, 1, 1.0)
	node_volume.inputs[node_volume.density_in].default_value = 1
	node_volume.inputs[5].default_value = False # multiscattering checkbox
	node_volume.inputs[node_volume.transmission_color_in].default_value = (1, 1, 1, 1.0)
	

def volume_001():
	default_settings()
	create_imagemap("scatter_color_in", "scatterColor.png")

def volume_002():
	create_imagemap("scatter_color_in", "scatterColor.tga")

def volume_003():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.scatter_color_in].default_value = (0, 0.4, 0, 1.0)

def volume_004():
	create_imagemap("transmission_color_in", "transmissionColor.png")

def volume_005():
	create_imagemap("transmission_color_in", "transmissionColor.tga")

def volume_006():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.transmission_color_in].default_value = (0, 0.4, 0, 1.0)

def volume_007():
	create_imagemap("emission_color_in", "emissionColor.tga")

def volume_008():
	create_imagemap("emission_color_in", "emissionColor.tga")

def volume_009():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.emission_color_in].default_value = (0, 0.4, 0, 1.0)

def volume_010():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.emission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.transmission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.scatter_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.density_in].default_value = 0

def volume_011():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.emission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.transmission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.scatter_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.density_in].default_value = 10

def volume_012():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.emission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.transmission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.scatter_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.density_in].default_value = 100

def volume_013():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.emission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.transmission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.scatter_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.scattering_direction_in].default_value = 1

def volume_014():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.emission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.transmission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.scatter_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.scattering_direction_in].default_value = -1

def volume_015():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.emission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.transmission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.scatter_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[5].default_value = True # multiscattering checkbox

def volume_016():
	volume_material, node_volume = get_material_and_node()
	node_volume.inputs[node_volume.emission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.transmission_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.scatter_color_in].default_value = (0, 0.4, 0, 1.0)
	node_volume.inputs[node_volume.density_in].default_value = 10
	node_volume.inputs[5].default_value = True # multiscattering checkbox


if __name__ == '__main__':

	list_tests = [
	["BL_MAT_VM_001", ["scatter color.png"], volume_001, delete_imagemap, "Volume.blend"],
	["BL_MAT_VM_002", ["scatter color.tga"], volume_002, delete_imagemap, "Volume.blend"],
	["BL_MAT_VM_003", ["scatter color green"], volume_003, default_settings, "Volume.blend"],
	["BL_MAT_VM_004", ["transmission color png"], volume_004, delete_imagemap, "Volume.blend"],
	["BL_MAT_VM_005", ["transmission color tga"], volume_005, delete_imagemap, "Volume.blend"],
	["BL_MAT_VM_006", ["transmission color green"], volume_006, default_settings, "Volume.blend"],
	["BL_MAT_VM_007", ["emission color png"], volume_007, delete_imagemap, "Volume.blend"],
	["BL_MAT_VM_008", ["emission color tga"], volume_008, delete_imagemap, "Volume.blend"],
	["BL_MAT_VM_009", ["emission color green"], volume_009, default_settings, "Volume.blend"],
	["BL_MAT_VM_010", ["scatter emission transmission color green", "density 0"], volume_010, default_settings, "Volume.blend"],
	["BL_MAT_VM_011", ["scatter emission transmission color green", "density 10"], volume_011, default_settings, "Volume.blend"],
	["BL_MAT_VM_012", ["scatter emission transmission color green", "density 100"], volume_012, default_settings, "Volume.blend"],
	["BL_MAT_VM_013", ["scatter emission transmission color green", "scattering direction 1"], volume_013, default_settings, "Volume.blend"],
	["BL_MAT_VM_014", ["scatter emission transmission color green", "scattering direction -1"], volume_014, default_settings, "Volume.blend"],
	["BL_MAT_VM_015", ["scatter emission transmission color green", "multiscattering true"], volume_015, default_settings, "Volume.blend"],
	["BL_MAT_VM_016", ["scatter emission transmission color green", "density 10", "multiscattering true"], volume_016, default_settings, "Volume.blend"],
	]

	launch_tests()

