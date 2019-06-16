
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.render, 'use_motion_blur', True)
	camera = bpy.data.cameras["Camera"]
	set_value(camera.rpr, 'motion_blur_exposure', test_list[3])

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL28_RS_MB_001", ["Default"], "MotionBlur.blend", 1], 
	["BL28_RS_MB_002", ["Exposure: 0"], "MotionBlur.blend", 0], 
	["BL28_RS_MB_003", ["Exposure: 0.5"], "MotionBlur.blend", 0,5], 
	["BL28_RS_MB_004", ["Exposure: 5"], "MotionBlur.blend", 5],
	["BL28_RS_MB_005", ["Exposure: 10"], "MotionBlur.blend", 10]
	]

	launch_tests()



