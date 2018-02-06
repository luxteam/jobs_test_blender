import bpy
from rprblender import node_editor
import addon_utils
import datetime
import sys
import json
import os

def make_presets(test_name, passes):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = passes

	# Render device in RPR
	bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type_plus_cpu = False
	bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type = '{render_mode}'
	#bpy.context.user_preferences.addons["rprblender"].preferences.settings.gpu_count = 2
	#bpy.context.user_preferences.addons["rprblender"].preferences.settings.samples = 1
	bpy.context.user_preferences.addons["rprblender"].preferences.settings.include_uncertified_devices = True

	# frame range
	bpy.data.scenes[Scenename].frame_start = 1
	bpy.data.scenes[Scenename].frame_end = 1

	# image format
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	bpy.data.scenes[Scenename].render.image_settings.quality = 80
	bpy.data.scenes[Scenename].render.image_settings.color_mode = 'RGB'

	# output
	name_scene = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + test_name
	output = r"{work_dir}" + "/Color/" + name_scene + "_##"
	bpy.data.scenes[Scenename].render.filepath = output 
	bpy.data.scenes[Scenename].render.use_placeholder = True
	bpy.data.scenes[Scenename].render.use_file_extension = True
	bpy.data.scenes[Scenename].render.use_overwrite = True

	# start render animation
	TIMER = datetime.datetime.now()
	bpy.ops.render.render(animation=True,scene=Scenename)
	Render_time = datetime.datetime.now() - TIMER

	# get version of rpr addon
	for mod_name in bpy.context.user_preferences.addons.keys():
		if (mod_name == 'rprblender') : 
			mod = sys.modules[mod_name]
			ver = mod.bl_info.get('version')
			version = str(ver[0]) + "." + str(ver[1]) + "." + str(ver[2])
		 
	# LOG
	name_scene_for_json = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + test_name + "BL"
	log_name = os.path.join(r'{work_dir}', name_scene_for_json + ".json")
	report = {{}}
	report['render_version'] = version
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['tool'] = "Blender " + bpy.app.version_string
	report['file_name'] = bpy.path.basename(bpy.context.blend_data.filepath) + "_" + test_name + "_01.jpg"
	report['scene_name'] = bpy.context.scene.name
	report['render_time'] = Render_time.total_seconds()
	report['render_color_path'] = r"{work_dir}" + "/Color/" + name_scene + "_01.jpg"
	report['date_time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
	report['render_device'] = bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type
	report['difference_color'] = "not compared yet"


	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')

def test_IES():

	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = r"C:\\TestResources\\BlenderAssets\\scenes\\Candle.fbm\\PD6R12ED010- PDM6835-694SNB.ies"

def base_light():

	bpy.context.scene.world.rpr_data.environment.enable = False

def test_IBL_on():

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = False

def test_IBL_off():

	bpy.context.scene.world.rpr_data.environment.enable = False

def test_Sun():

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'SUN_SKY'
	bpy.context.scene.world.rpr_data.environment.sun_sky.altitude = 90

def import_test():

	bpy.context.scene.render.engine = 'RPR'
	bpy.context.scene.world.rpr_data.environment.enable = True

	bpy.context.scene.objects['Cube'].hide_render = True
	bpy.context.scene.objects['Cube'].hide = True

	file_loc = r"C:\\TestResources\\BlenderAssets\\scenes\\example.obj"
	imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
	obj_object = bpy.context.selected_objects[0] 
	bpy.data.objects["shader_ball"].dimensions = (3, 3, 3)
	bpy.data.objects["shader_ball"].location = (0, 0, 0)


def create_Uber2():

	if((addon_utils.check("rprblender"))[0] == False) : 
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)

	bpy.context.object.select = False
	bpy.context.scene.objects['shader_ball'].select = True

	material = bpy.data.materials.new('Shader_mat')
	mesh = bpy.context.object.data
	

	# create material nodetree and retrieve it
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
	make_presets("Import", 30)
	create_Uber2()
	make_presets("Uber2", 30)
	base_light()
	make_presets("Base_Light", 30)
	test_IES()
	make_presets("IES Light", 30)
	test_IBL_on()
	make_presets("IBL_on", 30)
	test_Sun()
	make_presets("Sun", 30)

	make_presets("Full_100", 100)
	make_presets("Full_500", 500)