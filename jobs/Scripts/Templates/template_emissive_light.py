def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.world.rpr, 'enabled', False)
	set_value(scene.rpr.limits, 'max_samples', 100)

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":
		
	list_tests = [
	   ["BL28_L_EMIS_001", ["Scene with Emissive material as light"], "EmissiveLight.blend"],
	]

	launch_tests()
