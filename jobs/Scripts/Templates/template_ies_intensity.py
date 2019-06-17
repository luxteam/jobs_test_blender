def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
    if current_scene != test_list[2]:
        bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

    scene = bpy.context.scene
    enable_rpr_render(scene)

    set_value(scene.rpr.limits, 'max_samples', 100)

	lamp_data = bpy.data.lights['Point.001']
	set_value(lamp_data.rpr, 'intensity', 1000)

	render(test_list[0], test_list[1])
	return 1


if __name__ == "__main__":
	
	list_tests = [
		["BL28_L_INTLT_001", ["Render the scene with dirrerent IES lights intensity"], "IESintensity.blend"]
	]

	launch_tests()

