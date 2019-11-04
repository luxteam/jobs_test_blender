
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	# make changes
	test_list[3]()
	# render
	render(test_list[0], test_list[1])
	# undo changes
	test_list[4]()	

	render(test_list[0], test_list[1])
	return 1


def resetSceneAttributes():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 8)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 3)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 5)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 5)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 5)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 5)
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 0.02)
	set_value(bpy.context.scene.rpr, 'use_clamp_radiance', True)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 1)


def ql_001():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 0)


def ql_002():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 1)


def ql_003():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 2)


def ql_004():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 5)


def ql_005():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 10)


def ql_006():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 15)


def ql_007():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 20)


def ql_008():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 30)


def ql_009():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 40)


def ql_010():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)


def ql_011():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 0)


def ql_012():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 1)


def ql_013():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 2)


def ql_014():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 5)


def ql_015():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 10)


def ql_016():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 15)


def ql_017():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 20)


def ql_018():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 30)


def ql_019():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 40)


def ql_020():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 50)


def ql_021():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 0)


def ql_022():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 1)


def ql_023():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 2)


def ql_024():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 5)


def ql_025():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 10)


def ql_026():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 15)


def ql_027():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 20)


def ql_028():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 30)


def ql_029():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 40)


def ql_030():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)


def ql_031():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 0)


def ql_032():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 1)


def ql_033():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 2)


def ql_034():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 5)


def ql_035():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 10)


def ql_036():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 15)


def ql_037():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 20)


def ql_038():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 30)


def ql_039():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 40)


def ql_040():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)


def ql_041():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 0)


def ql_042():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 1)


def ql_043():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 2)


def ql_044():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 5)


def ql_045():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 10)


def ql_046():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 15)


def ql_047():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 20)


def ql_048():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 30)


def ql_049():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 40)


def ql_050():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 50)


def ql_051():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 0)


def ql_052():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 1)


def ql_053():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 2)


def ql_054():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 5)


def ql_055():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 10)


def ql_056():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 15)


def ql_057():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 20)


def ql_058():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 30)


def ql_059():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 40)


def ql_060():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 50)


def ql_061():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 0)


def ql_062():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 0.001)


def ql_063():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 0.01)


def ql_064():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 0.1)


def ql_065():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 1)


def ql_066():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 2)


def ql_067():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 5)


def ql_068():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 10)


def ql_069():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 15)


def ql_070():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 20)


def ql_071():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 30)


def ql_072():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 40)


def ql_073():
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 50)


def ql_074():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 0)


def ql_075():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 1)


def ql_076():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 2)


def ql_077():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 5)


def ql_078():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 10)


def ql_079():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 15)


def ql_080():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 20)


def ql_081():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 30)


def ql_082():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 40)


def ql_083():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 50)


def ql_084():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 100)


def ql_085():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'use_clamp_radiance', False)


def ql_086():
	pass


def ql_087():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 2)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 2)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 2)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 1)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 1)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 1)
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 0)


def ql_088():
	set_value(bpy.context.scene.rpr, 'max_ray_depth', 50)
	set_value(bpy.context.scene.rpr, 'diffuse_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_depth', 50)
	set_value(bpy.context.scene.rpr, 'refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'glossy_refraction_depth', 50)
	set_value(bpy.context.scene.rpr, 'shadow_depth', 50)
	set_value(bpy.context.scene.rpr, 'ray_cast_epsilon', 50)
	set_value(bpy.context.scene.rpr, 'clamp_radiance', 100)


if __name__ == "__main__":

	list_tests = [
		["BL28_RS_QL_001", ["Ray Depth - 0"], "Quality.blend", ql_001, resetSceneAttributes], 
		["BL28_RS_QL_002", ["Ray Depth - 1"], "Quality.blend", ql_002, resetSceneAttributes], 
		["BL28_RS_QL_003", ["Ray Depth - 2"], "Quality.blend", ql_003, resetSceneAttributes], 
		["BL28_RS_QL_004", ["Ray Depth - 5"], "Quality.blend", ql_004, resetSceneAttributes], 
		["BL28_RS_QL_005", ["Ray Depth - 10"], "Quality.blend", ql_005, resetSceneAttributes], 
		["BL28_RS_QL_006", ["Ray Depth - 15"], "Quality.blend", ql_006, resetSceneAttributes], 
		["BL28_RS_QL_007", ["Ray Depth - 20"], "Quality.blend", ql_007, resetSceneAttributes], 
		["BL28_RS_QL_008", ["Ray Depth - 30"], "Quality.blend", ql_008, resetSceneAttributes], 
		["BL28_RS_QL_009", ["Ray Depth - 40"], "Quality.blend", ql_009, resetSceneAttributes], 
		["BL28_RS_QL_010", ["Ray Depth - 50"], "Quality.blend", ql_010, resetSceneAttributes], 

		["BL28_RS_QL_011", ["Ray Depth - 50", "Diffuse - 0"], "DiffuseDepth.blend", ql_011, resetSceneAttributes], 
		["BL28_RS_QL_012", ["Ray Depth - 50", "Diffuse - 1"], "DiffuseDepth.blend", ql_012, resetSceneAttributes], 
		["BL28_RS_QL_013", ["Ray Depth - 50", "Diffuse - 2"], "DiffuseDepth.blend", ql_013, resetSceneAttributes], 
		["BL28_RS_QL_014", ["Ray Depth - 50", "Diffuse - 5"], "DiffuseDepth.blend", ql_014, resetSceneAttributes], 
		["BL28_RS_QL_015", ["Ray Depth - 50", "Diffuse - 10"], "DiffuseDepth.blend", ql_015, resetSceneAttributes], 
		["BL28_RS_QL_016", ["Ray Depth - 50", "Diffuse - 15"], "DiffuseDepth.blend", ql_016, resetSceneAttributes], 
		["BL28_RS_QL_017", ["Ray Depth - 50", "Diffuse - 20"], "DiffuseDepth.blend", ql_017, resetSceneAttributes], 
		["BL28_RS_QL_018", ["Ray Depth - 50", "Diffuse - 30"], "DiffuseDepth.blend", ql_018, resetSceneAttributes], 
		["BL28_RS_QL_019", ["Ray Depth - 50", "Diffuse - 40"], "DiffuseDepth.blend", ql_019, resetSceneAttributes], 
		["BL28_RS_QL_020", ["Ray Depth - 50", "Diffuse - 50"], "DiffuseDepth.blend", ql_020, resetSceneAttributes], 

		["BL28_RS_QL_021", ["Ray Depth - 50", "Glossy - 0"], "GlossyDepth.blend", ql_021, resetSceneAttributes], 
		["BL28_RS_QL_022", ["Ray Depth - 50", "Glossy - 1"], "GlossyDepth.blend", ql_022, resetSceneAttributes], 
		["BL28_RS_QL_023", ["Ray Depth - 50", "Glossy - 2"], "GlossyDepth.blend", ql_023, resetSceneAttributes], 
		["BL28_RS_QL_024", ["Ray Depth - 50", "Glossy - 5"], "GlossyDepth.blend", ql_024, resetSceneAttributes], 
		["BL28_RS_QL_025", ["Ray Depth - 50", "Glossy - 10"], "GlossyDepth.blend", ql_025, resetSceneAttributes], 
		["BL28_RS_QL_026", ["Ray Depth - 50", "Glossy - 15"], "GlossyDepth.blend", ql_026, resetSceneAttributes], 
		["BL28_RS_QL_027", ["Ray Depth - 50", "Glossy - 20"], "GlossyDepth.blend", ql_027, resetSceneAttributes], 
		["BL28_RS_QL_028", ["Ray Depth - 50", "Glossy - 30"], "GlossyDepth.blend", ql_028, resetSceneAttributes], 
		["BL28_RS_QL_029", ["Ray Depth - 50", "Glossy - 40"], "GlossyDepth.blend", ql_029, resetSceneAttributes], 
		["BL28_RS_QL_030", ["Ray Depth - 50", "Glossy - 50"], "GlossyDepth.blend", ql_030, resetSceneAttributes], 

		["BL28_RS_QL_031", ["Ray Depth - 50", "Refraction - 0"], "RefractionDepth.blend", ql_031, resetSceneAttributes], 
		["BL28_RS_QL_032", ["Ray Depth - 50", "Refraction - 1"], "RefractionDepth.blend", ql_032, resetSceneAttributes], 
		["BL28_RS_QL_033", ["Ray Depth - 50", "Refraction - 2"], "RefractionDepth.blend", ql_033, resetSceneAttributes], 
		["BL28_RS_QL_034", ["Ray Depth - 50", "Refraction - 5"], "RefractionDepth.blend", ql_034, resetSceneAttributes], 
		["BL28_RS_QL_035", ["Ray Depth - 50", "Refraction - 10"], "RefractionDepth.blend", ql_035, resetSceneAttributes], 
		["BL28_RS_QL_036", ["Ray Depth - 50", "Refraction - 15"], "RefractionDepth.blend", ql_036, resetSceneAttributes], 
		["BL28_RS_QL_037", ["Ray Depth - 50", "Refraction - 20"], "RefractionDepth.blend", ql_037, resetSceneAttributes], 
		["BL28_RS_QL_038", ["Ray Depth - 50", "Refraction - 30"], "RefractionDepth.blend", ql_038, resetSceneAttributes], 
		["BL28_RS_QL_039", ["Ray Depth - 50", "Refraction - 40"], "RefractionDepth.blend", ql_039, resetSceneAttributes], 
		["BL28_RS_QL_040", ["Ray Depth - 50", "Refraction - 50"], "RefractionDepth.blend", ql_040, resetSceneAttributes], 

		["BL28_RS_QL_041", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 0"], "RefractionGlossyDepth.blend", ql_041, resetSceneAttributes], 
		["BL28_RS_QL_042", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 1"], "RefractionGlossyDepth.blend", ql_042, resetSceneAttributes], 
		["BL28_RS_QL_043", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 2"], "RefractionGlossyDepth.blend", ql_043, resetSceneAttributes], 
		["BL28_RS_QL_044", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 5"], "RefractionGlossyDepth.blend", ql_044, resetSceneAttributes], 
		["BL28_RS_QL_045", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 10"], "RefractionGlossyDepth.blend", ql_045, resetSceneAttributes], 
		["BL28_RS_QL_046", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 15"], "RefractionGlossyDepth.blend", ql_046, resetSceneAttributes], 
		["BL28_RS_QL_047", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 20"], "RefractionGlossyDepth.blend", ql_047, resetSceneAttributes], 
		["BL28_RS_QL_048", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 30"], "RefractionGlossyDepth.blend", ql_048, resetSceneAttributes], 
		["BL28_RS_QL_049", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 40"], "RefractionGlossyDepth.blend", ql_049, resetSceneAttributes], 
		["BL28_RS_QL_050", ["Ray Depth - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 50"], "RefractionGlossyDepth.blend", ql_050, resetSceneAttributes], 

		["BL28_RS_QL_051", ["Ray Depth - 50", "Shadow - 0"], "ShadowDepth.blend", ql_051, resetSceneAttributes], 
		["BL28_RS_QL_052", ["Ray Depth - 50", "Shadow - 1"], "ShadowDepth.blend", ql_052, resetSceneAttributes], 
		["BL28_RS_QL_053", ["Ray Depth - 50", "Shadow - 2"], "ShadowDepth.blend", ql_053, resetSceneAttributes], 
		["BL28_RS_QL_054", ["Ray Depth - 50", "Shadow - 5"], "ShadowDepth.blend", ql_054, resetSceneAttributes], 
		["BL28_RS_QL_055", ["Ray Depth - 50", "Shadow - 10"], "ShadowDepth.blend", ql_055, resetSceneAttributes], 
		["BL28_RS_QL_056", ["Ray Depth - 50", "Shadow - 15"], "ShadowDepth.blend", ql_056, resetSceneAttributes], 
		["BL28_RS_QL_057", ["Ray Depth - 50", "Shadow - 20"], "ShadowDepth.blend", ql_057, resetSceneAttributes], 
		["BL28_RS_QL_058", ["Ray Depth - 50", "Shadow - 30"], "ShadowDepth.blend", ql_058, resetSceneAttributes], 
		["BL28_RS_QL_059", ["Ray Depth - 50", "Shadow - 40"], "ShadowDepth.blend", ql_059, resetSceneAttributes], 
		["BL28_RS_QL_060", ["Ray Depth - 50", "Shadow - 50"], "ShadowDepth.blend", ql_060, resetSceneAttributes], 

		["BL28_RS_QL_061", ["Ray Cast Epsilon - 0"], "Quality.blend", ql_061, resetSceneAttributes], 
		["BL28_RS_QL_062", ["Ray Cast Epsilon - 0.001"], "Quality.blend", ql_062, resetSceneAttributes], 
		["BL28_RS_QL_063", ["Ray Cast Epsilon - 0.01"], "Quality.blend", ql_063, resetSceneAttributes], 
		["BL28_RS_QL_064", ["Ray Cast Epsilon - 0.1"], "Quality.blend", ql_064, resetSceneAttributes], 
		["BL28_RS_QL_065", ["Ray Cast Epsilon - 1"], "Quality.blend", ql_065, resetSceneAttributes], 
		["BL28_RS_QL_066", ["Ray Cast Epsilon - 2"], "Quality.blend", ql_066, resetSceneAttributes], 
		["BL28_RS_QL_067", ["Ray Cast Epsilon - 5"], "Quality.blend", ql_067, resetSceneAttributes], 
		["BL28_RS_QL_068", ["Ray Cast Epsilon - 10"], "Quality.blend", ql_068, resetSceneAttributes], 
		["BL28_RS_QL_069", ["Ray Cast Epsilon - 15"], "Quality.blend", ql_069, resetSceneAttributes], 
		["BL28_RS_QL_070", ["Ray Cast Epsilon - 20"], "Quality.blend", ql_070, resetSceneAttributes], 
		["BL28_RS_QL_071", ["Ray Cast Epsilon - 30"], "Quality.blend", ql_071, resetSceneAttributes], 
		["BL28_RS_QL_072", ["Ray Cast Epsilon - 40"], "Quality.blend", ql_072, resetSceneAttributes], 
		["BL28_RS_QL_073", ["Ray Cast Epsilon - 50"], "Quality.blend", ql_073, resetSceneAttributes],

		["BL28_RS_QL_074", ["Ray Depth - 50", "Clamp Radiance - 0"], "ClampRadiance.blend", ql_074, resetSceneAttributes], 
		["BL28_RS_QL_075", ["Ray Depth - 50", "Clamp Radiance - 1"], "ClampRadiance.blend", ql_075, resetSceneAttributes], 
		["BL28_RS_QL_076", ["Ray Depth - 50", "Clamp Radiance - 2"], "ClampRadiance.blend", ql_076, resetSceneAttributes], 
		["BL28_RS_QL_077", ["Ray Depth - 50", "Clamp Radiance - 5"], "ClampRadiance.blend", ql_077, resetSceneAttributes], 
		["BL28_RS_QL_078", ["Ray Depth - 50", "Clamp Radiance - 10"], "ClampRadiance.blend", ql_078, resetSceneAttributes], 
		["BL28_RS_QL_079", ["Ray Depth - 50", "Clamp Radiance - 15"], "ClampRadiance.blend", ql_079, resetSceneAttributes], 
		["BL28_RS_QL_080", ["Ray Depth - 50", "Clamp Radiance - 20"], "ClampRadiance.blend", ql_080, resetSceneAttributes], 
		["BL28_RS_QL_081", ["Ray Depth - 50", "Clamp Radiance - 30"], "ClampRadiance.blend", ql_081, resetSceneAttributes], 
		["BL28_RS_QL_082", ["Ray Depth - 50", "Clamp Radiance - 40"], "ClampRadiance.blend", ql_082, resetSceneAttributes], 
		["BL28_RS_QL_083", ["Ray Depth - 50", "Clamp Radiance - 50"], "ClampRadiance.blend", ql_083, resetSceneAttributes],
		["BL28_RS_QL_084", ["Ray Depth - 50", "Clamp Radiance - 100"], "ClampRadiance.blend", ql_084, resetSceneAttributes], 
		["BL28_RS_QL_085", ["Ray Depth - 50", "Turn off Use Clamp checkbox"], "ClampRadiance.blend", ql_085, resetSceneAttributes],

		#["BL28_RS_QL_086", ["Activate \"Downscale Textures in Production\" "], "Quality.blend", ql_086, resetSceneAttributes],

		["BL28_RS_QL_087", ["Ray Depth - 2", "Diffuse - 2", "Glossy - 2", "Refraction - 1", "Glossy Refraction - 1", "Shadow - 1", "Ray Cast Epsilon - 0"], "Quality.blend", ql_087, resetSceneAttributes],
		["BL28_RS_QL_088", ["Ray Depth - 50", "Diffuse - 50", "Glossy - 50", "Refraction - 50", "Glossy Refraction - 50", "Shadow - 50", "Ray Cast Epsilon - 50", "Clamp Irradience - 100"], "Quality.blend", ql_088, resetSceneAttributes]

	]

	launch_tests()



