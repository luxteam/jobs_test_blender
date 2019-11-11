
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

	return 1


def impexp_001():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["barnfindorange solid"]

	bpy.data.objects['Shaders.002'].active_material = data_to.materials[0]


def impexp_002():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["car paint solid"]

	bpy.data.objects['Shaders.006'].active_material = data_to.materials[0]


def impexp_003():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["carbon fiber"]

	bpy.data.objects['Shaders.007'].active_material = data_to.materials[0]


def impexp_004():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["emissive fluorescent yellow"]

	bpy.data.objects['Shaders.008'].active_material = data_to.materials[0]


def impexp_005():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["gold paint"]

	bpy.data.objects['Shaders.009'].active_material = data_to.materials[0]


def impexp_006():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["lead rusted"]

	bpy.data.objects['Shaders'].active_material = data_to.materials[0]


def impexp_007():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["paint eggshell laserlemon"]

	bpy.data.objects['Shaders.005'].active_material = data_to.materials[0]


def impexp_008():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["rubber bumpy"]

	bpy.data.objects['Shaders.001'].active_material = data_to.materials[0]


def impexp_009():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["wood bark"]

	bpy.data.objects['Shaders.003'].active_material = data_to.materials[0]


def impexp_010():
	export_scene_path = os.path.join(r"{resource_path}", "Export.blend")
	with bpy.data.libraries.load(export_scene_path, link=False) as (data_from, data_to):
	    data_to.materials = ["wood planks oak glossy"]

	bpy.data.objects['Shaders.004'].active_material = data_to.materials[0]


if __name__ == "__main__":

	list_tests = [
		["BL28_MAT_IMPEXP_001", ["Material: barnfindorange solid"], "Import.blend", impexp_001],
		["BL28_MAT_IMPEXP_002", ["Material: car paint solid"], "Import.blend", impexp_002],
		["BL28_MAT_IMPEXP_003", ["Material: carbon fiber"], "Import.blend", impexp_003], 
		["BL28_MAT_IMPEXP_004", ["Material: emissive fluorescent yellow"], "Import.blend", impexp_004],
		["BL28_MAT_IMPEXP_005", ["Material: gold paint"], "Import.blend", impexp_005],
		["BL28_MAT_IMPEXP_006", ["Material: lead rusted"], "Import.blend", impexp_006],
		["BL28_MAT_IMPEXP_007", ["Material: paint eggshell laserlemon"], "Import.blend", impexp_007],
		["BL28_MAT_IMPEXP_008", ["Material: rubber bumpy"], "Import.blend", impexp_008],
		["BL28_MAT_IMPEXP_009", ["Material: wood bark"], "Import.blend", impexp_009],
		["BL28_MAT_IMPEXP_010", ["Material: wood planks oak glossy"], "Import.blend", impexp_010]
	]

	launch_tests()


