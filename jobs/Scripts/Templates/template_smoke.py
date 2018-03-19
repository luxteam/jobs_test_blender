
def main(test_name, passes, size_r_x, size_r_y, size_a_x, size_a_y):

	Scenename = bpy.context.scene.name
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = passes
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	# resolution
	bpy.data.scenes[Scenename].render.resolution_x = size_r_x
	bpy.data.scenes[Scenename].render.resolution_y = size_r_y
	bpy.data.scenes[Scenename].render.pixel_aspect_x = size_a_x
	bpy.data.scenes[Scenename].render.pixel_aspect_y = size_a_y
	bpy.data.scenes[Scenename].render.resolution_percentage = 100

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
	main("Import_Test", 50, 1920, 1080, 1, 1)

	create_Uber2()
	main("Uber2_Test", 50, 1920, 1080, 1, 1)

	test_base_light()
	main("Base_Light_Test", 50, 1920, 1080, 1, 1)

	test_IES()
	main("IES_Light_Test", 50, 1920, 1080, 1, 1)

	test_IBL_on()
	main("IBL_Test", 50, 1920, 1080, 1, 1)

	test_IBL_hdr()
	main("IBL_hdr", 50, 1920, 1080, 1, 1)

	test_IBL_exr()
	main("IBL_exr", 50, 1920, 1080, 1, 1)

	test_Sun()
	main("Sun_Sky_Test", 50, 1920, 1080, 1, 1)

	main("Full_Test", 1, 1920, 1080, 1, 1)
	main("Full_Test", 100, 1920, 1080, 1, 1)
	main("Full_Test", 500, 1920, 1080, 1, 1)
	main("Full_Test", 1000, 1920, 1080, 1, 1)

	#image size
	main("DVCPRO_HD_1080p", 30, 1280, 1080, 3, 2)
	main("DVCPRO_HD_720p", 30, 960, 720, 4, 3)
	main("HDTV_1080p", 30, 1920, 1080, 1, 1)
	main("HDTV_720p", 30, 1280, 720, 1, 1)
	main("HDV_1080p", 30, 1440, 1080, 4, 3)
	main("HDV_NTSC_1080p", 30, 1440, 1080, 4, 3)
	main("HDV_PAL_1080p", 30, 1440, 1080, 4, 3)
	main("TV_NTSC_16_9", 30, 720, 480, 40.1, 33)
	main("TV_NTSC_4_3", 30, 720, 486, 10, 11)
	main("TV_PAL_16_9", 30, 720, 576, 16, 11)
	main("TV_PAL_4_3", 30, 720, 576, 12, 11)
	main("2K", 30, 2048, 1152, 3, 2)
	main("4K", 30, 4096, 3204, 3, 2)
	main("2000x2000", 30, 2000, 2000, 3, 2)
	main("3000x3000", 30, 3000, 3000, 3, 2) 
	main("4000x4000", 30, 4000, 4000, 3, 2) 
	#main("5000x5000", 30, 5000, 5000, 3, 2) 
	#main("6000x6000", 30, 6000, 6000, 3, 2)
	#main("7000x7000", 30, 7000, 7000, 3, 2)
	#main("8000x8000", 30, 8000, 8000, 3, 2)

