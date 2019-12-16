def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	test_list[3]()
	render(test_list[0], test_list[1])
	resetSceneAttributes()

	return 1


def resetSceneAttributes():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', False)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')

	set_value(view_layer.rpr.denoiser, 'color_sigma', 0.75)
	set_value(view_layer.rpr.denoiser, 'depth_sigma', 0.01)
	set_value(view_layer.rpr.denoiser, 'normal_sigma', 0.01)
	set_value(view_layer.rpr.denoiser, 'trans_sigma', 0.01)

	set_value(view_layer.rpr.denoiser, 'radius', 1)
	set_value(view_layer.rpr.denoiser, 'p_sigma', 0.1)

	set_value(view_layer.rpr.denoiser, 'samples', 4)
	set_value(view_layer.rpr.denoiser, 'half_window', 4)
	set_value(view_layer.rpr.denoiser, 'bandwidth', 0.2)

	set_value(view_layer.rpr.denoiser, 'ml_color_only', True)

	set_value(bpy.context.scene.rpr, 'use_tile_render', False)


def den_001():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	set_value(view_layer.rpr.denoiser, 'radius', 1)


def den_002():
	exit(111)
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	set_value(view_layer.rpr.denoiser, 'radius', 5)


def den_003():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	set_value(view_layer.rpr.denoiser, 'radius', 10)


def den_004():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')


def den_005():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'samples', 5)


def den_006():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'samples', 10)


def den_007():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'half_window', 5)


def den_008():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'half_window', 10)


def den_009():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'bandwidth', 0.1)


def den_010():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'bandwidth', 0.5)


def den_011():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'samples', 2)
	set_value(view_layer.rpr.denoiser, 'half_window', 1)
	set_value(view_layer.rpr.denoiser, 'bandwidth', 0.1)


def den_012():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'samples', 5)
	set_value(view_layer.rpr.denoiser, 'half_window', 5)
	set_value(view_layer.rpr.denoiser, 'bandwidth', 0.5)


def den_013():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'samples', 10)
	set_value(view_layer.rpr.denoiser, 'half_window', 10)
	set_value(view_layer.rpr.denoiser, 'bandwidth', 1)


def den_014():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')


def den_015():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'color_sigma', 0.1)


def den_016():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'color_sigma', 0.5)


def den_017():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'depth_sigma', 0.1)


def den_018():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'depth_sigma', 0.5)


def den_019():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'normal_sigma', 0.1)


def den_020():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'normal_sigma', 0.5)


def den_021():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'trans_sigma', 0.1)


def den_022():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'trans_sigma', 0.5)


def den_023():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'color_sigma', 0.1)
	set_value(view_layer.rpr.denoiser, 'depth_sigma', 0.1)
	set_value(view_layer.rpr.denoiser, 'normal_sigma', 0.1)
	set_value(view_layer.rpr.denoiser, 'trans_sigma', 0.1)


def den_024():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	set_value(view_layer.rpr.denoiser, 'color_sigma', 0.5)
	set_value(view_layer.rpr.denoiser, 'depth_sigma', 0.5)
	set_value(view_layer.rpr.denoiser, 'normal_sigma', 0.5)
	set_value(view_layer.rpr.denoiser, 'trans_sigma', 0.5)


def den_025():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')


def den_026():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', True)


def den_027():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', False)


def den_028():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', True)
	set_value(bpy.context.scene.rpr, 'use_tile_render', True)


def den_029():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', False)
	set_value(bpy.context.scene.rpr, 'use_tile_render', True)


def den_030():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	set_value(view_layer.rpr.denoiser, 'radius', 1)


def den_031():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	set_value(view_layer.rpr.denoiser, 'radius', 5)


def den_032():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	set_value(view_layer.rpr.denoiser, 'radius', 10)


def den_033():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	set_value(view_layer.rpr.denoiser, 'radius', 1)
	set_value(bpy.context.scene.rpr, 'use_tile_render', True)


def den_034():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'samples', 5)


def den_035():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'samples', 10)


def den_036():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'half_window', 5)


def den_037():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'half_window', 10)


def den_038():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'bandwidth', 0.1)


def den_039():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'color_sigma', 0.1)
	set_value(view_layer.rpr.denoiser, 'depth_sigma', 0.1)
	set_value(view_layer.rpr.denoiser, 'normal_sigma', 0.1)
	set_value(view_layer.rpr.denoiser, 'trans_sigma', 0.1)


def den_040():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	set_value(view_layer.rpr.denoiser, 'color_sigma', 0.5)
	set_value(view_layer.rpr.denoiser, 'depth_sigma', 0.5)
	set_value(view_layer.rpr.denoiser, 'normal_sigma', 0.5)
	set_value(view_layer.rpr.denoiser, 'trans_sigma', 0.5)


def den_041():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', True)
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 0)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_042():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', False)
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 0)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_043():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', True)
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 3)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_044():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', False)
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 0)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_045():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 0)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_046():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 3)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_047():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 0)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_048():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 3)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_049():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 0)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_050():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')
	physical_light_data = bpy.data.lights['Area']
	set_value(physical_light_data.rpr, 'intensity', 3)
	ies_light_data = bpy.data.lights['Point.001']
	set_value(ies_light_data.rpr, 'intensity', 3)


def den_051():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', True)


def den_052():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'ML')
	set_value(view_layer.rpr.denoiser, 'ml_color_only', False)


def den_053():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'EAW')


def den_054():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'LWR')


def den_055():
	view_layer = bpy.context.view_layer
	set_value(view_layer.rpr.denoiser, 'enable', True)
	set_value(view_layer.rpr.denoiser, 'filter_type', 'BILATERAL')



if __name__ == "__main__":

	list_tests = [

		#["BL28_RS_DEN_001", ["Denoiser type: Bilateral", "Radius: 1"], "Test_Scene.blend", den_001],
		#["BL28_RS_DEN_002", ["Denoiser type: Bilateral", "Radius: 5"], "Test_Scene.blend", den_002],
		#["BL28_RS_DEN_003", ["Denoiser type: Bilateral", "Radius: 10"], "Test_Scene.blend", den_003],

		#["BL28_RS_DEN_004", ["Denoiser type: LWR"], "Test_Scene.blend", den_004],
		#["BL28_RS_DEN_005", ["Denoiser type: LWR", "Samples: 5"], "Test_Scene.blend", den_005],
		#["BL28_RS_DEN_006", ["Denoiser type: LWR", "Samples: 10"], "Test_Scene.blend", den_006],
		#["BL28_RS_DEN_007", ["Denoiser type: LWR", "Filter radius: 5"], "Test_Scene.blend", den_007],
		#["BL28_RS_DEN_008", ["Denoiser type: LWR", "Filter radius: 10"], "Test_Scene.blend", den_008],
		#["BL28_RS_DEN_009", ["Denoiser type: LWR", "Bandwidth: 0.1"], "Test_Scene.blend", den_009],
		#["BL28_RS_DEN_010", ["Denoiser type: LWR", "Bandwidth: 0.5"], "Test_Scene.blend", den_010],
		#["BL28_RS_DEN_011", ["Denoiser type: LWR", "Samples: 2", "Filter radius: 1", "Bandwidth: 0.1"], "Test_Scene.blend", den_011],
		#["BL28_RS_DEN_012", ["Denoiser type: LWR", "Samples: 5", "Filter radius: 5", "Bandwidth: 0.5"], "Test_Scene.blend", den_012],
		#["BL28_RS_DEN_013", ["Denoiser type: LWR", "Samples: 10", "Filter radius: 10", "Bandwidth: 1"], "Test_Scene.blend", den_013],

		#["BL28_RS_DEN_014", ["Denoiser type: EAW"], "Test_Scene.blend", den_014],
		#["BL28_RS_DEN_015", ["Denoiser type: EAW", "Color: 0.1"], "Test_Scene.blend", den_015],
		#["BL28_RS_DEN_016", ["Denoiser type: EAW", "Color: 0.5"], "Test_Scene.blend", den_016],
		#["BL28_RS_DEN_017", ["Denoiser type: EAW", "Depth: 0.1"], "Test_Scene.blend", den_017],
		#["BL28_RS_DEN_018", ["Denoiser type: EAW", "Depth: 0.5"], "Test_Scene.blend", den_018],
		#["BL28_RS_DEN_019", ["Denoiser type: EAW", "Normal: 0.1"], "Test_Scene.blend", den_019],
		#["BL28_RS_DEN_020", ["Denoiser type: EAW", "Normal: 0.5"], "Test_Scene.blend", den_019],
		#["BL28_RS_DEN_021", ["Denoiser type: EAW", "Trans: 0.1"], "Test_Scene.blend", den_021],
		#["BL28_RS_DEN_022", ["Denoiser type: EAW", "Trans: 0.5"], "Test_Scene.blend", den_022],
		#["BL28_RS_DEN_023", ["Denoiser type: EAW", "Color: 0.1", "Depth: 0.1", "Normal: 0.1", "Trans: 0.1"], "Test_Scene.blend", den_023],
		#["BL28_RS_DEN_024", ["Denoiser type: EAW", "Color: 0.5", "Depth: 0.5", "Normal: 0.5", "Trans: 0.5"], "Test_Scene.blend", den_024],

		#["BL28_RS_DEN_025", ["Denoiser type: ML"], "Test_Scene.blend", den_025],

		#["BL28_RS_DEN_026", ["Denoiser type: ML", "Use Color AOV: True"], "DenoiserMetal.blend", den_026],
		#["BL28_RS_DEN_027", ["Denoiser type: ML", "Use Color AOV: False"], "DenoiserMetal.blend", den_027],
		#["BL28_RS_DEN_028", ["Denoiser type: ML""Use Color AOV: True", "Tile Rendering: True"], "DenoiserMetal.blend", den_028],
		#["BL28_RS_DEN_029", ["Denoiser type: ML""Use Color AOV: False", "Tile Rendering: False"], "DenoiserMetal.blend", den_029],

		#["BL28_RS_DEN_030", ["Denoiser type: Bilateral", "Radius: 1"], "DenoiserMetal.blend", den_030],
		#["BL28_RS_DEN_031", ["Denoiser type: Bilateral", "Radius: 5"], "DenoiserMetal.blend", den_031],
		#["BL28_RS_DEN_032", ["Denoiser type: Bilateral", "Radius: 10"], "DenoiserMetal.blend", den_032],
		#["BL28_RS_DEN_033", ["Denoiser type: Bilateral", "Radius: 1", "Tile Rendering: True"], "DenoiserMetal.blend", den_033],
		#["BL28_RS_DEN_034", ["Denoiser type: LWR", "Samples: 5"], "DenoiserMetal.blend", den_034],
		#["BL28_RS_DEN_035", ["Denoiser type: LWR", "Samples: 10"], "DenoiserMetal.blend", den_035],
		#["BL28_RS_DEN_036", ["Denoiser type: LWR", "Filter radius: 5"], "DenoiserMetal.blend", den_036],
		#["BL28_RS_DEN_037", ["Denoiser type: LWR", "Filter radius: 5"], "DenoiserMetal.blend", den_037],
		#["BL28_RS_DEN_038", ["Denoiser type: LWR", "Bandwidth: 0.1"], "DenoiserMetal.blend", den_038],
		#["BL28_RS_DEN_039", ["Denoiser type: EAW", "Color: 0.1", "Depth: 0.1", "Normal: 0.1", "Trans: 0.1"], "DenoiserMetal.blend", den_039],
		#["BL28_RS_DEN_040", ["Denoiser type: EAW", "Color: 0.5", "Depth: 0.5", "Normal: 0.5", "Trans: 0.5"], "DenoiserMetal.blend", den_040],

		#["BL28_RS_DEN_041", ["Denoiser type: ML", "Use Color AOV: True", "PhysicalLight2 intensity: 0", "IES intensity: 3"], "DenoiserLight.blend", den_041],
		#["BL28_RS_DEN_042", ["Denoiser type: ML", "Use Color AOV: False", "PhysicalLight2 intensity: 0", "IES intensity: 3"], "DenoiserLight.blend", den_042],
		#["BL28_RS_DEN_043", ["Denoiser type: ML", "Use Color AOV: True", "PhysicalLight2 intensity: 3", "IES intensity: 3"], "DenoiserLight.blend", den_043],
		#["BL28_RS_DEN_044", ["Denoiser type: ML", "Use Color AOV: False", "PhysicalLight2 intensity: 3", "IES intensity: 3"], "DenoiserLight.blend", den_044],
		#["BL28_RS_DEN_045", ["Denoiser type: EAW", "PhysicalLight2 intensity: 0", "IES intensity: 3"], "DenoiserLight.blend", den_045],
		#["BL28_RS_DEN_046", ["Denoiser type: EAW", "PhysicalLight2 intensity: 3", "IES intensity: 3"], "DenoiserLight.blend", den_046],
		#["BL28_RS_DEN_047", ["Denoiser type: Bilateral", "PhysicalLight2 intensity: 3", "IES intensity: 3"], "DenoiserLight.blend", den_047],
		#["BL28_RS_DEN_048", ["Denoiser type: Bilateral", "PhysicalLight2 intensity: 3", "IES intensity: 3"], "DenoiserLight.blend", den_048],
		#["BL28_RS_DEN_049", ["Denoiser type: LWR", "PhysicalLight2 intensity: 3", "IES intensity: 3"], "DenoiserLight.blend", den_049],
		["BL28_RS_DEN_050", ["Denoiser type: LWR", "PhysicalLight2 intensity: 3", "IES intensity: 3"], "DenoiserLight.blend", den_050],

		["BL28_RS_DEN_051", ["Denoiser type: ML", "Use Color AOV: True"], "DenoiserDOF.blend", den_051],
		["BL28_RS_DEN_052", ["Denoiser type: ML", "Use Color AOV: False"], "DenoiserDOF.blend", den_052],
		["BL28_RS_DEN_053", ["Denoiser type: EAW"], "DenoiserDOF.blend", den_053],
		["BL28_RS_DEN_054", ["Denoiser type: LWR"], "DenoiserDOF.blend", den_054],
		["BL28_RS_DEN_055", ["Denoiser type: Bilateral"], "DenoiserDOF.blend", den_055],

		["BL28_RS_DEN_056", ["Denoiser type: ML", "Use Color AOV: True"], "DenoiserIBL.blend", den_051],
		["BL28_RS_DEN_057", ["Denoiser type: ML", "Use Color AOV: False"], "DenoiserIBL.blend", den_052],
		["BL28_RS_DEN_058", ["Denoiser type: EAW"], "DenoiserIBL.blend", den_053],
		["BL28_RS_DEN_059", ["Denoiser type: LWR"], "DenoiserIBL.blend", den_054],
		["BL28_RS_DEN_060", ["Denoiser type: Bilateral"], "DenoiserIBL.blend", den_055],

		["BL28_RS_DEN_061", ["Denoiser type: ML", "Use Color AOV: True"], "DenoiserComplexLighting.blend", den_051],
		["BL28_RS_DEN_062", ["Denoiser type: ML", "Use Color AOV: False"], "DenoiserComplexLighting.blend", den_052],
		["BL28_RS_DEN_063", ["Denoiser type: EAW"], "DenoiserComplexLighting.blend", den_053],
		["BL28_RS_DEN_064", ["Denoiser type: LWR"], "DenoiserComplexLighting.blend", den_054],
		["BL28_RS_DEN_065", ["Denoiser type: Bilateral"], "DenoiserComplexLighting.blend", den_055],

		["BL28_RS_DEN_066", ["Denoiser type: ML", "Use Color AOV: True"], "DenoiserMaterials.blend", den_051],
		["BL28_RS_DEN_067", ["Denoiser type: ML", "Use Color AOV: False"], "DenoiserMaterials.blend", den_052],
		["BL28_RS_DEN_068", ["Denoiser type: EAW"], "DenoiserMaterials.blend", den_053],
		["BL28_RS_DEN_069", ["Denoiser type: LWR"], "DenoiserMaterials.blend", den_054],
		["BL28_RS_DEN_070", ["Denoiser type: Bilateral"], "DenoiserMaterials.blend", den_055]
		
	]

	launch_tests()
