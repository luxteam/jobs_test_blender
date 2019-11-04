
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[4]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[4]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.rpr.limits, 'max_samples', test_list[5])

	if test_list[2] != "pass":
		test_list[2]()
		render(test_list[0], test_list[1])
		test_list[3]()			
	else:
		create_report(test_list[0], test_list[1], "pass")

	return 1


def empty():
	pass


def import_fbx():
	shader_ball = bpy.data.objects['Cube']
	shader_ball.hide_render = True

	fbx_path = os.path.join(r"{resource_path}", "1.fbx")
	bpy.ops.import_scene.fbx(filepath=fbx_path, global_scale=10)

	
def import_obj():
	shader_ball = bpy.data.objects['shader_ball']
	shader_ball.hide_render = True

	obj_path = os.path.join(r"{resource_path}", "1.obj")
	bpy.ops.import_scene.obj(filepath=obj_path)


def delete_obj():
	shader_ball = bpy.data.objects['shader_ball.001']
	shader_ball.hide_render = True

	shader_ball = bpy.data.objects['shader_ball']
	shader_ball.hide_render = False


def create_IBL():
	scene = bpy.context.scene
	set_value(scene.world.rpr, 'enabled', True)
	set_value(scene.world.rpr, 'mode', 'IBL')


def update_IBL_hdr():
	scene = bpy.context.scene
	set_value(scene.world.rpr, 'enabled', True)
	set_value(scene.world.rpr, 'mode', 'IBL')
	bpy.ops.image.open(filepath="//Maps//Tropical_Beach_3k.hdr", directory="{resource_path}//Maps//", files=[{{"name":"Tropical_Beach_3k.hdr"}}], relative_path=True, show_multiview=False)
	set_value(scene.world.rpr.ibl, 'image', bpy.data.images['Tropical_Beach_3k.hdr'])


def update_IBL_exr():
	scene = bpy.context.scene
	set_value(scene.world.rpr, 'enabled', True)
	set_value(scene.world.rpr, 'mode', 'IBL')
	bpy.ops.image.open(filepath="//Maps//ibl_test.exr", directory="{resource_path}//Maps//", files=[{{"name":"ibl_test.exr"}}], relative_path=True, show_multiview=False)
	set_value(scene.world.rpr.ibl, 'image', bpy.data.images['ibl_test.exr'])


def delete_map_IBL():
	scene = bpy.context.scene
	set_value(scene.world.rpr, 'enabled', True)
	set_value(scene.world.rpr, 'mode', 'IBL')
	set_value(scene.world.rpr.ibl, 'image', None)


def create_sun_sky():
	scene = bpy.context.scene
	set_value(scene.world.rpr, 'enabled', True)
	set_value(scene.world.rpr, 'mode', 'SUN_SKY')
	

def delete_sun_sky():
	scene = bpy.context.scene
	set_value(scene.world.rpr, 'enabled', False)


def create_ies_light():
	scene = bpy.context.scene
	set_value(scene.world.rpr, 'enabled', False)
	light = bpy.data.lights['Lamp']
	set_value(light, 'type', 'POINT')
	set_value(light.rpr, 'intensity', 100)
	bpy.ops.image.open(filepath="//Maps//1.ies", directory="{resource_path}//Maps//", files=[{{"name":"1.ies"}}], \
																														relative_path=True, show_multiview=False)
	set_value(light.rpr, 'ies_file', bpy.data.images["1.ies"])
	

def delete_ies_light():
	light = bpy.data.lights['Lamp']
	set_value(light.rpr, 'ies_file_name', '')


def activate_tile_rendering():
	scene = bpy.context.scene
	set_value(scene.rpr, 'use_tile_render', True)


def deactivate_tile_rendering():
	scene = bpy.context.scene
	set_value(scene.rpr, 'use_tile_render', False)


def activate_color_srgb():
	scene = bpy.context.scene
	set_value(scene.display_settings, 'display_device', 'sRGB')
	set_value(scene.view_settings, 'view_transform', 'Filmic')
	set_value(scene.view_settings, 'look', 'None')


def deactivate_color_srgb():
	scene = bpy.context.scene
	set_value(scene.display_settings, 'display_device', 'sRGB')
	set_value(scene.view_settings, 'view_transform', 'Filmic')
	set_value(scene.view_settings, 'look', 'None')


def activate_color_look():
	scene = bpy.context.scene
	set_value(scene.display_settings, 'display_device', 'sRGB')
	set_value(scene.view_settings, 'view_transform', 'Filmic')
	set_value(scene.view_settings, 'look', 'Filmic - Very High Contrast')


def deactivate_color_look():
	scene = bpy.context.scene
	set_value(scene.display_settings, 'display_device', 'sRGB')
	set_value(scene.view_settings, 'view_transform', 'Filmic')
	set_value(scene.view_settings, 'look', 'None')


def activate_render_stamp():
	scene = bpy.context.scene
	set_value(scene.rpr, 'use_render_stamp', True)


def deactivate_render_stamp():
	scene = bpy.context.scene
	set_value(scene.rpr, 'use_render_stamp', False)


def change_image_size_hd720():
	scene = bpy.context.scene
	set_value(scene.render, 'resolution_x', 1280)
	set_value(scene.render, 'resolution_y', 720)


def change_image_size_custom():
	scene = bpy.context.scene
	set_value(scene.render, 'resolution_x', 1500)
	set_value(scene.render, 'resolution_y', 1125)


def change_image_size_default():
	scene = bpy.context.scene
	set_value(scene.render, 'resolution_x', 1920)
	set_value(scene.render, 'resolution_y', 1080)


def activate_jpg_format():
	scene = bpy.context.scene
	set_value(scene.render.image_settings, 'file_format', 'JPEG')


def activate_png_format():
	scene = bpy.context.scene
	set_value(scene.render.image_settings, 'file_format', 'PNG')


def activate_denoiser_bilateral():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')


def activate_denoiser_lwr():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')


def activate_denoiser_eaw():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')


def activate_denoiser_ml():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')


def deactivate_denoiser():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', False)


def activate_aov():
	view_layer = bpy.context.view_layer

	view_layer.rpr.enable_aovs[1] = False
	view_layer.rpr.enable_aovs[6] = True

	'''
	os.remove(r"{work_dir}" + "/Color/" + test_list[0] + '.jpg')
	os.rename(r"{work_dir}" + "/Color/" + test_list[0] + '0040.jpg', \
		r"{work_dir}" + "/Color/" + test_list[0] + '.jpg')
	'''


def deactivate_aov():
	view_layer = bpy.context.view_layer
	view_layer.rpr.enable_aovs[1] = True
	view_layer.rpr.enable_aovs[6] = False


def create_area_light():
	scene = bpy.context.scene
	set_value(scene.world.rpr, 'enabled', False)
	light = bpy.data.lights['Light']
	set_value(light, 'type', 'AREA')


def delete_area_light():
	scene = bpy.context.scene
	set_value(scene.world.rpr, 'enabled', True)
	light = bpy.data.lights['Light']
	set_value(light, 'type', 'POINT')


def activate_medium_quality():
	scene = bpy.context.scene
	set_value(scene.rpr, 'max_ray_depth', 15)
	set_value(scene.rpr, 'refraction_depth', 10)


def deactivate_medium_quality():
	scene = bpy.context.scene
	set_value(scene.rpr, 'max_ray_depth', 8)
	set_value(scene.rpr, 'refraction_depth', 5)


def activate_hair():
	shader_ball = bpy.data.objects["shader_ball"]
	shader_ball.select_set(True)    
	bpy.context.view_layer.objects.active = shader_ball
	bpy.ops.object.particle_system_add()
	bpy.data.particles["ParticleSettings"].type = 'HAIR'


def copy_objects():
	obj = bpy.data.objects["Suzanne"]
	bpy.context.view_layer.objects.active = obj
	obj.select_set(state=True)
	bpy.ops.object.duplicate(linked=True)
	obj.location.z += 1.3


def import_rpr_matlib():
	material_name= 'Gold.xml'
	xml_path = os.path.join(material_library.path.get_library_path(), material_name.split('.')[0], material_name)
	gold_material = bpy.data.materials.new('Gold')
	gold_material.use_nodes = True
	bpy.data.objects['shader_ball'].active_material = gold_material
	material_library.import_xml_material(gold_material, material_name, xml_path, False)


def create_and_assign_uber():
	uber_material = bpy.data.materials.new('Uber')
	uber_material.use_nodes = True
	bpy.data.objects['shader_ball'].active_material = uber_material
	tree = uber_material.node_tree
	uber_node = tree.nodes.new(type='RPRShaderNodeUber')
	output_node = tree.nodes['Material Output']
	tree.links.new(uber_node.outputs[0], output_node.inputs[0])
	uber_node.inputs['Diffuse Color'].default_value = (0.8, 0.0154239, 0.00939292, 1)


def create_and_assign_principled_bsdf():
	principled_bsdf_material = bpy.data.materials.new('Principled BSDF')
	principled_bsdf_material.use_nodes = True
	bpy.data.objects['shader_ball'].active_material = principled_bsdf_material
	tree = principled_bsdf_material.node_tree
	principled_bsdf_node = tree.nodes['Principled BSDF']
	principled_bsdf_node.inputs['Base Color'].default_value = (0.00643981, 0.8, 0.0358057, 1)


def assign_standart_material():
	bpy.data.objects['shader_ball'].active_material = bpy.data.materials['Default']


def activateIPR():
	for area in bpy.context.workspace.screens[0].areas:
		for space in area.spaces:
			if space.type == 'VIEW_3D':
				space.shading.type = 'RENDERED'


def deactivateIPR():
	for area in bpy.context.workspace.screens[0].areas:
		for space in area.spaces:
			if space.type == 'VIEW_3D':
				space.shading.type = 'SOLID'


def activate_transparent_background():
	scene = bpy.context.scene
	set_value(scene.render, 'film_transparent', True)


def deactivate_transparent_background():
	scene = bpy.context.scene
	set_value(scene.render, 'film_transparent', False)



if __name__ == '__main__':

	list_tests = [
		["BL28_SM_001", ["Install RPR"], "pass", "pass", "rpr_default.blend", 1],
		["BL28_SM_002", ["Select RPR"], "pass", "pass", "rpr_default.blend", 1],
		["BL28_SM_003", ["Open RPR scene"], "pass", "pass", "rpr_default.blend", 1],
		["BL28_SM_004", ["Render empty scene", "Pass Limit: 50"], empty, empty, "rpr_default.blend", 50],
		["BL28_SM_005", ["IES", "Pass Limit: 50"], create_ies_light, delete_ies_light, "IES.blend", 50],
		["BL28_SM_006", ["Import FBX", "Pass Limit: 50"], import_fbx, empty, "rpr_default.blend", 50],
		["BL28_SM_007", ["Import OBJ", "Pass Limit: 50"], import_obj, delete_obj, "default.blend", 50],
		["BL28_SM_008", ["RPR Uber material", "Pass Limit: 50"], create_and_assign_uber, assign_standart_material, "default.blend", 50],
		["BL28_SM_009", ["Sun_Sky", "Pass Limit: 50"], create_sun_sky, delete_sun_sky, "default.blend", 50],
		["BL28_SM_010", ["IBL", "Pass Limit: 50"], create_IBL, empty, "default.blend", 50],
		["BL28_SM_011", ["IBL with HDR", "Pass Limit: 50"], update_IBL_hdr, delete_map_IBL, "default.blend", 50],
		["BL28_SM_012", ["IBL with EXR", "Pass Limit: 50"], update_IBL_exr, empty, "default.blend", 50],
		["BL28_SM_013", ["Render 1 pass"], empty, empty, "default.blend", 1],
		["BL28_SM_014", ["Render 100 pass"], empty, empty, "default.blend", 100],
		["BL28_SM_015", ["Render 500 pass"], empty, empty, "default.blend", 500],
		["BL28_SM_016", ["Tile Rendering"], activate_tile_rendering, deactivate_tile_rendering, "default.blend", 50],
		["BL28_SM_017", ["Color Management (sRGB)"], activate_color_srgb, deactivate_color_srgb, "default.blend", 50],
		["BL28_SM_018", ["Color Management (Look)"], activate_color_look, deactivate_color_look, "default.blend", 50],
		["BL28_SM_019", ["Render Stamp", "Pass Limit: 50"], activate_render_stamp, deactivate_render_stamp, "default.blend", 50],

		## Not implemented in plugin
		##["BL28_SM_020", ["Render mode wireframe", "Pass Limit: 50"], activate_wireframe_mode, deactivate_wireframe_mode, "default.blend", 50],

		["BL28_SM_021", ["Image size 720HD", "Pass Limit: 50"], change_image_size_hd720, empty, "default.blend", 50],
		["BL28_SM_022", ["Image size 1500 1125", "Pass Limit: 50"], change_image_size_custom, change_image_size_default, "default.blend", 50],
		["BL28_SM_023", ["PNG format", "Pass Limit: 50"], activate_png_format, empty, "default.blend", 50],	
		["BL28_SM_024", ["JPG format", "Pass Limit: 50"], activate_jpg_format, empty, "default.blend", 50],
		["BL28_SM_025", ["Denoiser EAW", "Pass Limit: 50"], activate_denoiser_eaw, deactivate_denoiser, "default.blend", 50],
		["BL28_SM_026", ["Denoiser LWR", "Pass Limit: 50"], activate_denoiser_lwr, deactivate_denoiser, "default.blend", 50],
		["BL28_SM_027", ["Denoiser Bilateral", "Pass Limit: 50"], activate_denoiser_bilateral, deactivate_denoiser, "default.blend", 50],
		["BL28_SM_028", ["Denoiser ML", "Pass Limit: 50"], activate_denoiser_ml, deactivate_denoiser, "default.blend", 50],
		["BL28_SM_029", ["Principled BSDF", "Pass Limit: 50"], create_and_assign_principled_bsdf, assign_standart_material, "default.blend", 50],
		["BL28_SM_030", ["Mat lib", "Pass Limit: 50"], import_rpr_matlib, assign_standart_material, "default.blend", 50],

		# Wait for ticket 847
		#["BL28_SM_031", ["AOV Geometric Normal", "Pass Limit: 50"], activate_aov, deactivate_aov, "default.blend", 50],

		["BL28_SM_032", ["Area light", "Pass Limit: 50"], create_area_light, delete_area_light, "default.blend", 50],
		["BL28_SM_033", ["Instances", "Pass Limit: 50"], copy_objects, empty, "instances.blend", 50],
		["BL28_SM_034", ["5 lights", "Pass Limit: 50"], empty, empty, "5_lights.blend", 50],
		["BL28_SM_035", ["AOV SC", "Pass Limit: 50"], empty, empty, "AOV_SC.blend", 50],
		["BL28_SM_036", ["SSS", "Pass Limit: 50"], empty, empty, "SSS_Test.blend", 50],
		["BL28_SM_037", ["Displacement", "Pass Limit: 50"], empty, empty, "Displacement.blend", 50],
		["BL28_SM_038", ["Quality", "Pass Limit: 50"], activate_medium_quality, deactivate_medium_quality, "WaterInsideGlass.blend", 50],
		["BL28_SM_039", ["IPR"], activateIPR, deactivateIPR, "default.blend", 50],
		["BL28_SM_040", ["Hair", "Pass Limit: 50"], activate_hair, empty, "default.blend", 50],
		["BL28_SM_041", ["Transparent Background", "Pass Limit: 50"], activate_transparent_background, deactivate_transparent_background, "AOV_SC.blend", 50],
		["BL28_SM_042", ["Volumetric Light", "Pass Limit: 50"], empty, empty, "Volume.blend", 50]
	]

	launch_tests()
