
def prerender(test_list):

	bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)
	
	test_list[3]()
	render(test_list[0], test_list[1])

	return 1


def get_material_and_node():
	volume_material = [e for e in bpy.data.materials if e.name == "Material"][0]
	volume_node = [n for n in volume_material.node_tree.nodes if n.type=="PRINCIPLED_VOLUME"][0]
	return volume_material, volume_node


def create_checker_texture(attr):
	volume_material, volume_node = get_material_and_node()
	tree = volume_material.node_tree
	checker_texture_node = tree.nodes.new(type='ShaderNodeTexChecker')

	if type(volume_node.inputs[attr].default_value) == float:
		tree.links.new(checker_texture_node.outputs['Fac'], volume_node.inputs[attr])
	else:
		tree.links.new(checker_texture_node.outputs['Color'], volume_node.inputs[attr])


def create_imagemap(attr, image_name):
	volume_material, volume_node = get_material_and_node()
	tree = volume_material.node_tree

	imagemap_node = tree.nodes.new(type='ShaderNodeTexImage')
	image = bpy.data.images.load(os.path.join(r"{resource_path}", "Maps", image_name))
	imagemap_node.image = image
	
	if type(volume_node.inputs[attr].default_value) == float:
		tree.links.new(imagemap_node.outputs['Alpha'], volume_node.inputs[attr])
	else:
		tree.links.new(imagemap_node.outputs['Color'], volume_node.inputs[attr])

	
def vm_001():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0, 0, 0, 1)


def vm_002():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)


def vm_003():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (1, 1, 1, 1)


def vm_004():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0, 1, 0, 1)


def vm_005():
	create_checker_texture('Color')


def vm_006():
	create_imagemap('Color', 'diffuseColor.tga')


def vm_007():
	create_imagemap('Color', 'diffuseColor.png')


def vm_008():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 0


def vm_009():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 0.5


def vm_010():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1


def vm_011():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 5


def vm_012():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 10


def vm_013():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	create_checker_texture('Density')


def vm_014():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	create_imagemap('Density', 'reflectionColor.tga')


def vm_015():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	create_imagemap('Density', 'reflectionColor.png')


def vm_016():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = -1
	volume_node.inputs['Absorption Color'].default_value = (0.5, 0, 0, 1.0)


def vm_017():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 0
	volume_node.inputs['Absorption Color'].default_value = (0.5, 0, 0, 1.0)


def vm_018():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 1
	volume_node.inputs['Absorption Color'].default_value = (0.5, 0, 0, 1.0)


def vm_019():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 1
	volume_node.inputs['Absorption Color'].default_value = (0, 0.5, 0, 1.0)


def vm_020():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 1
	volume_node.inputs['Absorption Color'].default_value = (0, 0, 0, 0.5)


def vm_021():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 1
	create_checker_texture('Anisotropy')


def vm_022():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 1
	create_checker_texture('Absorption Color')


def vm_023():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 1
	create_imagemap('Absorption Color', 'transmissionColor.tga')


def vm_024():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 1
	create_imagemap('Absorption Color', 'transmissionColor.png')


def vm_025():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 0
	volume_node.inputs['Absorption Color'].default_value = (0, 0, 0, 1)
	volume_node.inputs['Emission Color'].default_value = (0, 0, 0.5, 1)
	volume_node.inputs['Emission Strength'].default_value = 0.5


def vm_026():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 0
	volume_node.inputs['Absorption Color'].default_value = (0, 0, 0, 1)
	volume_node.inputs['Emission Color'].default_value = (0, 0, 0.5, 1)
	volume_node.inputs['Emission Strength'].default_value = 1


def vm_027():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 0
	volume_node.inputs['Absorption Color'].default_value = (0, 0, 0, 1)
	volume_node.inputs['Emission Color'].default_value = (0, 0, 0.5, 1)
	volume_node.inputs['Emission Strength'].default_value = 5


def vm_028():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 0
	volume_node.inputs['Absorption Color'].default_value = (0, 0, 0, 1)
	volume_node.inputs['Emission Color'].default_value = (0, 0, 0.5, 1)
	volume_node.inputs['Emission Strength'].default_value = 10


def vm_029():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 0
	volume_node.inputs['Absorption Color'].default_value = (0, 0, 0, 1)
	create_checker_texture('Emission Strength')


def vm_030():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 0
	volume_node.inputs['Absorption Color'].default_value = (0, 0, 0, 1)
	volume_node.inputs['Emission Strength'].default_value = 1
	create_checker_texture('Emission Color')


def vm_031():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 0
	volume_node.inputs['Absorption Color'].default_value = (0, 0, 0, 1)
	create_imagemap('Emission Color', 'emissiveColor.tga')


def vm_032():
	volume_material, volume_node = get_material_and_node()
	volume_node.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
	volume_node.inputs['Density'].default_value = 1
	volume_node.inputs['Anisotropy'].default_value = 0
	volume_node.inputs['Absorption Color'].default_value = (0, 0, 0, 1)
	create_imagemap('Emission Color', 'emissiveColor.png')


if __name__ == '__main__':

	list_tests = [

		["BL28_MAT_VM_001", ["Volume Color RGB - 0 0 0"], "Volume.blend", vm_001],
		["BL28_MAT_VM_002", ["Volume Color RGB - 0.5 0.5 0.5"], "Volume.blend", vm_002],
		["BL28_MAT_VM_003", ["Volume Color RGB - 1 1 1"], "Volume.blend", vm_003],
		["BL28_MAT_VM_004", ["Volume Color RGB - 0 1 0"], "Volume.blend", vm_004],
		["BL28_MAT_VM_005", ["Volume Color Checker texture"], "Volume.blend", vm_005],
		["BL28_MAT_VM_006", ["Volume Color .tga"], "Volume.blend", vm_006],
		["BL28_MAT_VM_007", ["Volume Color .png"], "Volume.blend", vm_007],

		["BL28_MAT_VM_008", ["Volume Density - 0"], "Volume.blend", vm_001],
		["BL28_MAT_VM_009", ["Volume Density - 0.5"], "Volume.blend", vm_001],
		["BL28_MAT_VM_010", ["Volume Density - 1"], "Volume.blend", vm_010],
		["BL28_MAT_VM_011", ["Volume Density - 5"], "Volume.blend", vm_011],
		["BL28_MAT_VM_012", ["Volume Density - 10"], "Volume.blend", vm_012],
		["BL28_MAT_VM_013", ["Volume Density Checker texture"], "Volume.blend", vm_013],
		["BL28_MAT_VM_014", ["Volume Density .tga"], "Volume.blend", vm_014],
		["BL28_MAT_VM_015", ["Volume Density .png"], "Volume.blend", vm_015],

		["BL28_MAT_VM_016", ["Volume Anisotropy -1"], "Volume.blend", vm_016],
		["BL28_MAT_VM_017", ["Volume Anisotropy 0"], "Volume.blend", vm_017],
		["BL28_MAT_VM_018", ["Volume Anisotropy 1"], "Volume.blend", vm_018],
		["BL28_MAT_VM_019", ["Volume Anisotropy color RGB - 0;0.5;0"], "Volume.blend", vm_019],
		["BL28_MAT_VM_020", ["Volume Anisotropy color RGB - 0;0;0.5"], "Volume.blend", vm_020],
		["BL28_MAT_VM_021", ["Volume Anisotropy Checker texture"], "Volume.blend", vm_021],
		["BL28_MAT_VM_022", ["Volume Anisotropy Color Checker texture"], "Volume.blend", vm_022],
		["BL28_MAT_VM_023", ["Volume Anisotropy Color .tga"], "Volume.blend", vm_023],
		["BL28_MAT_VM_024", ["Volume Anisotropy Color .png"], "Volume.blend", vm_024],

		["BL28_MAT_VM_025", ["Volume Emission - 0.5"], "Volume.blend", vm_025],
		["BL28_MAT_VM_026", ["Volume Emission - 1"], "Volume.blend", vm_026],
		["BL28_MAT_VM_027", ["Volume Emission - 5"], "Volume.blend", vm_027],
		["BL28_MAT_VM_028", ["Volume Emission - 10"], "Volume.blend", vm_028],
		["BL28_MAT_VM_029", ["Volume Emission Checker texture"], "Volume.blend", vm_029],
		["BL28_MAT_VM_030", ["Volume Emission Color Checker texture"], "Volume.blend", vm_030],
		["BL28_MAT_VM_031", ["Volume Emission Color .tga"], "Volume.blend", vm_031],
		["BL28_MAT_VM_032", ["Volume Emission Color .png"], "Volume.blend", vm_032],

		#["BL28_MAT_VM_033", ["Volume Blackbody Intencity - 0.5"], "Volume.blend", vm_033],
		#["BL28_MAT_VM_034", ["Volume Blackbody Intencity- 0.6"], "Volume.blend", vm_034],
		#["BL28_MAT_VM_035", ["Volume Blackbody Intencity Checker texture"], "Volume.blend", vm_035],
		#["BL28_MAT_VM_036", ["Volume Blackbody Tint Checker texture"], "Volume.blend", vm_036],
		#["BL28_MAT_VM_037", ["Volume Blackbody Tint .tga"], "Volume.blend", vm_037],
		#["BL28_MAT_VM_038", ["Volume Blackbody Tint .png"], "Volume.blend", vm_038],

	]

	launch_tests()

