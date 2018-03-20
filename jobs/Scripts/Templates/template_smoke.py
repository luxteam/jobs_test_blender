
def main(test_name, passes):

	Scenename = bpy.context.scene.name
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = passes
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	render(test_name, passes)

def test_IES():

	ies = os.path.join("{res_path}", "Candle.fbm", "PD6R12ED010- PDM6835-694SNB.ies")
	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = ies

def test_base_light():

	bpy.context.scene.world.rpr_data.environment.enable = False

def test_IBL_on():

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'COLOR'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = False

def test_IBL_exr():

	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
	ibl_map = os.path.join("{res_path}", "ibl_test.exr")
	bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)

def test_IBL_hdr():

	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
	ibl_map = os.path.join("{res_path}", "Tropical_Beach_3k.hdr")
	bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)

def test_IBL_off():

	bpy.context.scene.world.rpr_data.environment.enable = False

def test_Sun():

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'SUN_SKY'
	bpy.context.scene.world.rpr_data.environment.sun_sky.altitude = 1.5708


def import_test():

	bpy.context.scene.render.engine = 'RPR'
	bpy.context.scene.world.rpr_data.environment.enable = True

	bpy.ops.object.select_all(action='DESELECT')
	bpy.data.objects['Cube'].select = True
	bpy.ops.object.delete() 

	file_loc = os.path.join("{res_path}", "example.obj")
	imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
	obj_object = bpy.context.selected_objects[0] 
	bpy.data.objects["shader_ball"].dimensions = (3, 3, 3)
	bpy.data.objects["shader_ball"].location = (0, 0, 0)


def create_Uber2():

	if((addon_utils.check("rprblender"))[0] == False) : 
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)

	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = bpy.data.objects['shader_ball']
	bpy.context.scene.objects['shader_ball'].select = True

	material = bpy.data.materials.new('Shader_mat')
	mesh = bpy.context.object.data
	
	override = bpy.context.copy()
	override['material'] = material
	bpy.ops.rpr.op_material_add_nodetree(override)
	tree = material.node_tree

	output = node_editor.find_node_in_nodetree(tree, node_editor.shader_node_output_name)
	uber2 = tree.nodes.new(type='rpr_shader_node_uber2')
	tree.links.new(uber2.outputs[uber2.shader_out], output.inputs[output.shader_in])

	uber2.diffuse = True
	uber2.inputs[uber2.diffuse_color].default_value = (0.65, 0.2, 0.2, 1.0)
	uber2.inputs[uber2.diffuse_weight].default_value = 1

	bpy.data.objects['shader_ball'].material_slots[0].material = bpy.data.materials['Shader_mat']


if __name__ == '__main__':

	import_test()
	main("Import_Test", 50)

	create_Uber2()
	main("Uber2_Test", 50)

	test_base_light()
	main("Base_Light_Test", 50)

	test_IES()
	main("IES_Light_Test", 50)

	test_IBL_on()
	main("IBL_Test", 50)

	test_IBL_hdr()
	main("IBL_hdr", 50)

	test_IBL_exr()
	main("IBL_exr", 50)

	test_Sun()
	main("Sun_Sky_Test", 50)

	main("Full_Test", 1)
	main("Full_Test", 100)
	main("Full_Test", 500)
	main("Full_Test", 1000)



