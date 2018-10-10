
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.objects.active = bpy.data.objects['Lamp']
	bpy.context.object.data.type = test_list[3]
	bpy.data.lamps["Lamp"].rpr_lamp.intensity = test_list[4]

	if (test_list[4]):
		ies = os.path.join("{res_path}", "Candle.fbm", "PD6R12ED010- PDM6835-694SNB.ies")
		bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = ies
	else:
		bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = ""

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_L_BL_001", ["Type: Point", "Intensity: 1000"], "BaseLightTest.blend", 'POINT', 1000, False], 
	["BL_L_BL_002", ["Type: Point with IES", "Intensity: 1000"], "BaseLightTest.blend", 'POINT', 1000, True], 
	["BL_L_BL_003", ["Type: Sun", "Intensity: 50"], "BaseLightTest.blend", 'SUN', 50, False], 
	["BL_L_BL_004", ["Type: Spot", "Intensity: 2000"], "BaseLightTest.blend", 'SPOT', 2000, False],
	["BL_L_BL_005", ["Type: Hemi", "Intensity: 50"], "BaseLightTest.blend", 'HEMI', 50, False], 
	["BL_L_BL_006", ["Type: Area", "Intensity: 300"], "BaseLightTest.blend", 'AREA', 300, False], 
	["BL_L_BL_007", ["Type: Area with IES", "Intensity: 300"], "BaseLightTest.blend", 'AREA', 300, True], 
	["BL_L_BL_008", ["Type: Point", "Intensity: 100"], "BaseLightTest.blend", 'POINT', 100, False],
	["BL_L_BL_009", ["Type: Sun", "Intensity: 100"], "BaseLightTest.blend", 'SUN', 100, False], 
	["BL_L_BL_010", ["Type: Spot", "Intensity: 100"], "BaseLightTest.blend", 'SPOT', 100, False],
	["BL_L_BL_011", ["Type: Hemi", "Intensity: 100"], "BaseLightTest.blend", 'HEMI', 100, False], 
	["BL_L_BL_012", ["Type: Area", "Intensity: 100"], "BaseLightTest.blend", 'AREA', 100, False]]

	launch_tests()
