
def main(test_case, passes, script_info):

	Scenename = bpy.context.scene.name
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = passes
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	render(test_case, script_info)

def delete_hierarchy(obj):

	names = set([obj.name])
	def get_child_names(obj):
		for child in obj.children:
			names.add(child.name)
			if child.children:
				get_child_names(child)

	get_child_names(obj)

	print(names)
	objects = bpy.data.objects
	[setattr(objects[n], 'select', True) for n in names]
	bpy.ops.object.delete()

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

def import_fbx_test():

	bpy.context.scene.render.engine = 'RPR'
	bpy.context.scene.world.rpr_data.environment.enable = True

	bpy.ops.object.select_all(action='DESELECT')
	bpy.data.objects['Cube'].select = True
	bpy.ops.object.delete() 

	file_loc = os.path.join("{res_path}", "park_bench1.fbx")
	imported_object = bpy.ops.import_scene.fbx(filepath=file_loc)
	obj_object = bpy.context.selected_objects[0] 
	bpy.data.objects["Default"].scale = (0.15, 0.15, 0.15)
	bpy.data.objects["Default"].location = (0, 0, 0)

def import_obj_test():

	bpy.context.scene.render.engine = 'RPR'
	bpy.context.scene.world.rpr_data.environment.enable = True

	bpy.ops.object.select_all(action='DESELECT')
	bpy.data.objects["Default"].select = True
	bpy.context.scene.objects.active = bpy.data.objects["Default"]
	delete_hierarchy(bpy.context.active_object)

	file_loc = os.path.join("{res_path}", "example.obj")
	imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
	obj_object = bpy.context.selected_objects[0] 
	bpy.data.objects["shader_ball"].dimensions = (3, 3, 3)
	bpy.data.objects["shader_ball"].location = (0, 0, 0)


def test_Uber2():

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

	if bpy.path.basename(bpy.context.blend_data.filepath) == "default.blend":
		main('BL_SM_003', 50, ["Render empty scene", "Pass Limit: 50"]) 

	elif bpy.path.basename(bpy.context.blend_data.filepath) == "rpr_default.blend":

		main('BL_SM_005', 50, ["Render empty scene with RPR parameters", "Pass Limit: 50"])

		import_fbx_test()
		main("BL_SM_006", 50, ["Import FBX", "Pass Limit: 50"])

		import_obj_test()
		main("BL_SM_007", 50, ["Import OBJ", "Pass Limit: 50"])

		test_Uber2()
		main("BL_SM_010", 50, ["Testing Uber material", "Pass Limit: 50"])

		test_base_light()
		main("BL_SM_011", 50, ["Testing base light", "Pass Limit: 50"])

		test_IES()
		main("BL_SM_012", 50, ["Testing IES light", "Pass Limit: 50"])

		test_Sun()
		main("BL_SM_013", 50, ["Testing Sun and Sky System", "Pass Limit: 50"])

		test_IBL_on()
		main("BL_SM_014", 50, ["Testing IBL", "Pass Limit: 50"])

		test_IBL_hdr()
		main("BL_SM_015", 50, ["Testing IBL with hdr", "Pass Limit: 50"])

		test_IBL_exr()
		main("BL_SM_016", 50, ["Testing IBL with exr", "Pass Limit: 50"])

		main("BL_SM_017", 1, ["Iteration test", "Pass Limit: 50"])
		main("BL_SM_018", 30, ["Iteration test", "Pass Limit: 50"])
		main("BL_SM_019", 100, ["Iteration test", "Pass Limit: 50"])
		main("BL_SM_020", 500, ["Iteration test", "Pass Limit: 50"])
		main("BL_SM_021", 1000, ["Iteration test", "Pass Limit: 50"])



