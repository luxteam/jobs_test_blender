
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.render, "use_single_layer", True)
	set_value(bpy.context.window, 'view_layer', bpy.data.scenes['Scene'].view_layers["{{}}".format(test_list[4])])

	if test_list[3] == "IBL":
		set_value(scene.world.rpr, 'enabled', True)
		set_value(scene.world.rpr, 'mode', 'IBL')
	elif test_list[3] == "HDR":    
		set_value(scene.world.rpr, 'enabled', True)
		set_value(scene.world.rpr, 'mode', 'IBL')
		bpy.ops.image.open(filepath="//Maps//Tropical_Beach_3k.hdr", directory="{resource_path}//Maps//", files=[{{"name":"Tropical_Beach_3k.hdr"}}], \
																															relative_path=True, show_multiview=False)
		set_value(scene.world.rpr.ibl, 'image', bpy.data.images['Tropical_Beach_3k.hdr'])
	elif test_list[3] == "Sun&Sky":
		set_value(scene.world.rpr, 'enabled', True)
		set_value(scene.world.rpr, 'mode', 'SUN_SKY')
	
	render(test_list[0], test_list[1])
	return 1


if __name__ == "__main__":

	list_tests = [
		# IBL
		["BL28_L_PTL_001", ["Portal Light, \"Interior_Cube\", IBL color"], "Portal_Light_Scene.blend", "IBL", "Interior_Cube"], 
		["BL28_L_PTL_002", ["Portal Light, \"Interior_Plane\", IBL color"], "Portal_Light_Scene.blend", "IBL", "Interior_Plane"], 
		["BL28_L_PTL_003", ["Portal Light, \"Interior_Sphere\", IBL color"], "Portal_Light_Scene.blend", "IBL", "Interior_Sphere"], 
		["BL28_L_PTL_004", ["Portal Light, \"Interior_Torus\", IBL color"], "Portal_Light_Scene.blend", "IBL", "Interior_Torus"], 
		["BL28_L_PTL_005", ["Portal Light, \"Open_Envy_Cube\", IBL color"], "Portal_Light_Scene.blend", "IBL", "Open_Envy_Cube"], 
		["BL28_L_PTL_006", ["Portal Light, \"Open_Envy_Plane\", IBL color"], "Portal_Light_Scene.blend", "IBL", "Open_Envy_Plane"], 
		["BL28_L_PTL_007", ["Portal Light, \"Open_Envy_Sphere\", IBL color"], "Portal_Light_Scene.blend", "IBL", "Open_Envy_Sphere"], 
		["BL28_L_PTL_008", ["Portal Light, \"Open_Envy_Torus\", IBL color"], "Portal_Light_Scene.blend", "IBL", "Open_Envy_Torus"], 
		# HDR MAP
		["BL28_L_PTL_009", ["Portal Light, \"Interior_Cube\", IBL Map"], "Portal_Light_Scene.blend", "HDR", "Interior_Cube"], 
		["BL28_L_PTL_010", ["Portal Light, \"Interior_Plane\", IBL Map"], "Portal_Light_Scene.blend", "HDR", "Interior_Plane"], 
		["BL28_L_PTL_011", ["Portal Light, \"Interior_Sphere\", IBL Map"], "Portal_Light_Scene.blend", "HDR", "Interior_Sphere"], 
		["BL28_L_PTL_012", ["Portal Light, \"Interior_Torus\", IBL Map"], "Portal_Light_Scene.blend", "HDR", "Interior_Torus"], 
		["BL28_L_PTL_013", ["Portal Light, \"Open_Envy_Cube\", IBL Map"], "Portal_Light_Scene.blend", "HDR", "Open_Envy_Cube"], 
		["BL28_L_PTL_014", ["Portal Light, \"Open_Envy_Plane\", IBL Map"], "Portal_Light_Scene.blend", "HDR", "Open_Envy_Plane"], 
		["BL28_L_PTL_015", ["Portal Light, \"Open_Envy_Sphere\", IBL Map"], "Portal_Light_Scene.blend", "HDR", "Open_Envy_Sphere"], 
		["BL28_L_PTL_016", ["Portal Light, \"Open_Envy_Torus\", IBL Map"], "Portal_Light_Scene.blend", "HDR", "Open_Envy_Torus"], 
		# SUN&SKY
		["BL28_L_PTL_017", ["Portal Light, \"Interior_Cube\", Sun&Sky"], "Portal_Light_Scene.blend", "Sun&Sky", "Interior_Cube"], 
		["BL28_L_PTL_018", ["Portal Light, \"Interior_Plane\", Sun&Sky"], "Portal_Light_Scene.blend", "Sun&Sky", "Interior_Plane"], 
		["BL28_L_PTL_019", ["Portal Light, \"Interior_Sphere\", Sun&Sky"], "Portal_Light_Scene.blend", "Sun&Sky", "Interior_Sphere"], 
		["BL28_L_PTL_020", ["Portal Light, \"Interior_Torus\", Sun&Sky"], "Portal_Light_Scene.blend", "Sun&Sky", "Interior_Torus"], 
		["BL28_L_PTL_021", ["Portal Light, \"Open_Envy_Cube\", Sun&Sky"], "Portal_Light_Scene.blend", "Sun&Sky", "Open_Envy_Cube"], 
		["BL28_L_PTL_022", ["Portal Light, \"Open_Envy_Plane\", Sun&Sky"], "Portal_Light_Scene.blend", "Sun&Sky", "Open_Envy_Plane"], 
		["BL28_L_PTL_023", ["Portal Light, \"Open_Envy_Sphere\", Sun&Sky"], "Portal_Light_Scene.blend", "Sun&Sky", "Open_Envy_Sphere"], 
		["BL28_L_PTL_024", ["Portal Light, \"Open_Envy_Torus\", Sun&Sky"], "Portal_Light_Scene.blend", "Sun&Sky", "Open_Envy_Torus"]
	]

	launch_tests()
