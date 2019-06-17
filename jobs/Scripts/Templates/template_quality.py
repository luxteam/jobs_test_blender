
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.rpr, 'max_ray_depth', test_list[3])
	set_value(scene.rpr, 'diffuse_depth', test_list[4])
	set_value(scene.rpr, 'glossy_depth', test_list[5])
	set_value(scene.rpr, 'refraction_depth', test_list[6])
	set_value(scene.rpr, 'glossy_refraction_depth', test_list[7])
	set_value(scene.rpr, 'shadow_depth', test_list[8])
	set_value(scene.rpr, 'ray_cast_epsilon', test_list[9])
	set_value(scene.rpr, 'use_clamp_radiance', test_list[10])
	set_value(scene.rpr, 'clamp_radiance', test_list[11])

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
		["BL28_RS_QL_001", ["Max Ray Depth - 2"], "Quality.blend", 2, 3, 5, 5, 5, 5, 0.02, True, 1], 
		["BL28_RS_QL_002", ["Max Ray Depth - 50"], "Quality.blend", 50, 3, 5, 5, 5, 5, 0.02, True, 1], 
		["BL28_RS_QL_003", ["Max Diffuse - 2"], "Quality.blend", 8, 2, 5, 5, 5, 5, 0.02, True, 1], 
		["BL28_RS_QL_004", ["Max Diffuse - 50"], "Quality.blend", 8, 50, 5, 5, 5, 5, 0.02, True, 1], 
		["BL28_RS_QL_005", ["Max Glossy - 2"], "Quality.blend", 8, 3, 2, 5, 5, 5, 0.02, True, 1], 
		["BL28_RS_QL_006", ["Max Glossy - 50"], "Quality.blend", 8, 3, 50, 5, 5, 5, 0.02, True, 1], 
		["BL28_RS_QL_007", ["Max Refraction - 1"], "Quality.blend", 8, 3, 5, 1, 5, 5, 0.02, True, 1], 
		["BL28_RS_QL_008", ["Max Refraction - 50"], "Quality.blend", 8, 3, 5, 50, 5, 5, 0.02, True, 1], 
		["BL28_RS_QL_009", ["Max Glossy Refraction - 1"], "Quality.blend", 8, 3, 5, 5, 1, 5, 0.02, True, 1], 
		["BL28_RS_QL_010", ["Max Glossy Refraction - 50"], "Quality.blend", 8, 3, 5, 5, 50, 5, 0.02, True, 1], 
		["BL28_RS_QL_011", ["Max Shadow - 1"], "Quality.blend", 8, 3, 5, 5, 5, 1, 0.02, True, 1], 
		["BL28_RS_QL_012", ["Max Shadow - 50"], "Quality.blend", 8, 3, 5, 5, 5, 50, 0.02, True, 1], 
		["BL28_RS_QL_013", ["Ray Cast Epsilon - 0"], "Quality.blend", 8, 3, 5, 5, 5, 5, 0, True, 1], 
		["BL28_RS_QL_014", ["Ray Cast Epsilon - 50"], "Quality.blend", 8, 3, 5, 5, 5, 5, 50, True, 1], 
		["BL28_RS_QL_015", ["Clamp Irradience - 100"], "Quality.blend", 8, 3, 5, 5, 5, 5, 0.02, True, 100], 
		["BL28_RS_QL_016", ["Turn off \"Use Clamp\""], "Quality.blend", 8, 3, 5, 5, 5, 5, 0.02, False, 1], 
		# ["BL28_RS_QL_017", ["Activate \"Downscale Textures in Production\" "], "Quality.blend", 8, 3, 5, 5, 5, 5, 0.02, True, 1], 
		["BL28_RS_QL_018", ["Complex parameters"], "Quality.blend", 2, 2, 2, 1, 1, 1, 0, True, 1], 
		["BL28_RS_QL_019", ["Complex parameters"], "Quality.blend", 50, 50, 50, 50, 50, 50, 50, True, 100]
	]

	launch_tests()



