
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
	resetSceneAttributes()	

	return 1


def resetSceneAttributes():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data, 'color', (1, 1, 1))
	set_value(light_data.rpr, 'use_temperature', False)
	set_value(light_data.rpr, 'temperature', 10000)
	set_value(light_data.rpr, 'ies_file', None)
	set_value(light_data.rpr, 'intensity_units_point', "DEFAULT")
	set_value(light_data.rpr, 'luminous_efficacy', 100)

	set_value(light_data.rpr, 'shadow_softness', 0)
	set_value(light_data.rpr, 'intensity_units_dir', 'DEFAULT')

	set_value(light_data, 'spot_size', 1.309)
	set_value(light_data, 'spot_blend', 0.511811)

	set_value(light_data, 'shape', 'SQUARE')
	set_value(light_data, 'visible', True)
	set_value(light_data, 'cast_shadows', True)
	set_value(light_data, 'intensity_normalization', True)


def pl_001():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 0)


def pl_002():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)


def pl_003():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 1000)


def pl_004():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 5000)


def pl_005():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 6500)


def pl_006():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 1000)


def pl_007():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 3200)


def pl_008():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 9600)


def pl_009():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	bpy.ops.image.open(filepath="//ies//2.ies", directory="{resource_path}//ies//", files=[{{"name":"2.ies"}}], relative_path=True, show_multiview=False)
	set_value(light_data.rpr, 'ies_file', bpy.data.images["2.ies"])


def pl_010():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 1000)
	bpy.ops.image.open(filepath="//ies//2.ies", directory="{resource_path}//ies//", files=[{{"name":"2.ies"}}], relative_path=True, show_multiview=False)
	set_value(light_data.rpr, 'ies_file', bpy.data.images["2.ies"])


def pl_011():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	bpy.ops.image.open(filepath="//ies//UVgrid2.png", directory="{resource_path}//ies//", files=[{{"name":"UVgrid2.png"}}], relative_path=True, show_multiview=False)
	set_value(light_data.rpr, 'ies_file', bpy.data.images["UVgrid2.png"])


def pl_012():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	bpy.ops.image.open(filepath="//ies//UVgrid2.tif", directory="{resource_path}//ies//", files=[{{"name":"UVgrid2.tif"}}], relative_path=True, show_multiview=False)
	set_value(light_data.rpr, 'ies_file', bpy.data.images["UVgrid2.tif"])


def pl_013():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	bpy.ops.image.open(filepath="//ies//UVgrid2.jpg", directory="{resource_path}//ies//", files=[{{"name":"UVgrid2.jpg"}}], relative_path=True, show_multiview=False)
	set_value(light_data.rpr, 'ies_file', bpy.data.images["UVgrid2.jpg"])


def pl_014():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	bpy.ops.image.open(filepath="//ies//UVgrid2GS.png", directory="{resource_path}//ies//", files=[{{"name":"UVgrid2GS.png"}}], relative_path=True, show_multiview=False)
	set_value(light_data.rpr, 'ies_file', bpy.data.images["UVgrid2GS.png"])


def pl_015():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 1000)
	bpy.ops.image.open(filepath="//ies//2.ies", directory="{resource_path}//ies//", files=[{{"name":"2.ies"}}], relative_path=True, show_multiview=False)
	set_value(light_data.rpr, 'ies_file', bpy.data.images["2.ies"])


def pl_016():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 3200)
	bpy.ops.image.open(filepath="//ies//2.ies", directory="{resource_path}//ies//", files=[{{"name":"2.ies"}}], relative_path=True, show_multiview=False)
	set_value(light_data.rpr, 'ies_file', bpy.data.images["2.ies"])


def pl_017():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 9600)
	bpy.ops.image.open(filepath="//ies//2.ies", directory="{resource_path}//ies//", files=[{{"name":"2.ies"}}], relative_path=True, show_multiview=False)
	set_value(light_data.rpr, 'ies_file', bpy.data.images["2.ies"])


def pl_018():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data, 'color', (0.5, 0, 0))


def pl_019():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data, 'color', (0, 0.5, 0))


def pl_020():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data, 'color', (0, 0, 0.5))


def pl_021():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_point', "WATTS")
	set_value(light_data.rpr, 'luminous_efficacy', 17)


def pl_022():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_point', "WATTS")
	set_value(light_data.rpr, 'luminous_efficacy', 100)


def pl_023():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_point', "LUMEN")


def pl_024():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'intensity_units_point', "LUMEN")


def pl_025():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'POINT')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'intensity_units_point', "LUMEN")


def pl_026():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 50)


def pl_027():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 0)


def pl_028():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)


def pl_029():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 1000)


def pl_030():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 5000)


def pl_031():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 6500)


def pl_032():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 1000)


def pl_033():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 3200)


def pl_034():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 9600)


def pl_035():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data, 'color', (0.5, 0, 0))


def pl_036():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data, 'color', (0, 0.5, 0))


def pl_037():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data, 'color', (0, 0, 0.5))


def pl_038():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_dir', 'RADIANCE')
	set_value(light_data.rpr, 'luminous_efficacy', 17)


def pl_039():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_dir', 'RADIANCE')
	set_value(light_data.rpr, 'luminous_efficacy', 100)


def pl_040():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_dir', 'LUMINANCE')


def pl_041():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'intensity_units_dir', 'LUMINANCE')


def pl_042():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'intensity_units_dir', 'LUMINANCE')


def pl_043():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shadow_softness', 0)


def pl_044():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shadow_softness', 0.1)


def pl_045():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shadow_softness', 0.5)


def pl_046():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shadow_softness', 1)


def pl_047():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 0)


def pl_048():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 100)


def pl_049():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 1000)


def pl_050():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 5000)


def pl_051():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 6500)


def pl_052():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 1000)


def pl_053():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 3200)


def pl_054():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 9600)


def pl_055():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data, 'color', (0.5, 0, 0))


def pl_056():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data, 'color', (0, 0.5, 0))


def pl_057():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SPOT')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data, 'color', (0, 0, 0.5))


def pl_058():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_point', 'WATTS')
	set_value(light_data.rpr, 'luminous_efficacy', 17)


def pl_059():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_point', 'WATTS')
	set_value(light_data.rpr, 'luminous_efficacy', 100)


def pl_060():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_point', 'LUMEN')


def pl_061():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'intensity_units_point', 'LUMEN')


def pl_062():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'intensity_units_point', 'LUMEN')


def pl_063():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'spot_size', 0.0174533)


def pl_064():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'spot_size', 0.785398)


def pl_065():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'spot_size', 1.5708)


def pl_066():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'spot_size', 3.14159)


def pl_067():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'spot_blend', 0)


def pl_068():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'spot_blend', 0.15)


def pl_069():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'spot_blend', 0.5)


def pl_070():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'SUN')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'spot_blend', 1)


def pl_071():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 0)


def pl_072():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)


def pl_073():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)


def pl_074():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)


def pl_075():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 0)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_076():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_077():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_078():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_079():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 6500)


def pl_080():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 1000)


def pl_081():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 3200)


def pl_082():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'use_temperature', True)
	set_value(light_data.rpr, 'temperature', 9600)


def pl_083():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'color', (0.5, 0, 0))


def pl_084():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'color', (0, 0.5, 0))


def pl_085():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'color', (0, 0, 0.5))


def pl_086():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_area', 'WATTS')
	set_value(light_data.rpr, 'luminous_efficacy', 17)


def pl_087():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_area', 'WATTS')
	set_value(light_data.rpr, 'luminous_efficacy', 100)


def pl_088():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_area', 'LUMEN')


def pl_089():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'intensity_units_area', 'LUMEN')


def pl_090():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'intensity_units_area', 'LUMEN')


def pl_091():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_area', 'RADIANCE')
	set_value(light_data.rpr, 'luminous_efficacy', 17)


def pl_092():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_area', 'RADIANCE')
	set_value(light_data.rpr, 'luminous_efficacy', 100)


def pl_093():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'intensity_units_area', 'LUMINANCE')


def pl_094():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'intensity_units_area', 'LUMINANCE')


def pl_094():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'intensity_units_area', 'LUMINANCE')


def pl_095():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'intensity_units_area', 'LUMINANCE')


def pl_096():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 0)
	set_value(light_data, 'size_y', 0)


def pl_097():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)


def pl_098():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)
	set_value(light_data.rpr, 'visible', True)


def pl_099():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)
	set_value(light_data.rpr, 'visible', True)
	set_value(light_data.rpr, 'cast_shadows', True)


def pl_100():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_101():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_102():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)


def pl_103():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)


def pl_104():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'visible', True)


def pl_105():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'visible', True)
	set_value(light_data.rpr, 'cast_shadows', True)


def pl_106():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_107():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_108():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'shape', 'RECTANGLE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_109():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 0)


def pl_110():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 1)


def pl_111():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'visible', True)


def pl_112():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'visible', True)
	set_value(light_data.rpr, 'cast_shadows', True)


def pl_113():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_114():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_115():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_116():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 3)


def pl_117():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'visible', True)


def pl_118():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'visible', True)
	set_value(light_data.rpr, 'cast_shadows', True)


def pl_119():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_120():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_121():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'shape', 'SQUARE')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_122():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 0)


def pl_123():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 1)


def pl_124():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'visible', True)


def pl_125():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'visible', True)
	set_value(light_data.rpr, 'cast_shadows', True)


def pl_126():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_127():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_128():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_129():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 3)


def pl_130():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'visible', True)


def pl_131():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'visible', True)
	set_value(light_data.rpr, 'cast_shadows', True)


def pl_132():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_133():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_134():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'shape', 'DISK')
	set_value(light_data, 'size', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_135():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 0)
	set_value(light_data, 'size_y', 0)


def pl_136():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)


def pl_137():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)
	set_value(light_data.rpr, 'visible', True)


def pl_138():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)
	set_value(light_data.rpr, 'visible', True)
	set_value(light_data.rpr, 'cast_shadows', True)


def pl_139():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_140():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_141():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 1)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_142():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)


def pl_143():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'visible', True)


def pl_144():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'visible', True)
	set_value(light_data.rpr, 'cast_shadows', True)


def pl_145():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 100)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_146():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 1000)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


def pl_147():
	light_data = bpy.data.lights['Point']
	set_value(light_data, 'type', 'AREA')
	set_value(light_data.rpr, 'intensity', 5000)
	set_value(light_data.rpr, 'shape', 'ELLIPSE')
	set_value(light_data, 'size', 1)
	set_value(light_data, 'size_y', 3)
	set_value(light_data.rpr, 'intensity_normalization', False)


if __name__ == "__main__":

	list_tests = [
		
		["BL28_L_PL_001", ["Point light, int = 0", "Expected Black Picture"], "Physical_Lights.blend", pl_001], 
		["BL28_L_PL_002", ["Point light, int = 100"], "Physical_Lights.blend", pl_002], 
		["BL28_L_PL_003", ["Point light, int = 1000"], "Physical_Lights.blend", pl_003], 
		["BL28_L_PL_004", ["Point light, int = 5000"], "Physical_Lights.blend", pl_004], 
		["BL28_L_PL_005", ["Point light, int = 100, Temperature - 6500"], "Physical_Lights.blend", pl_005], 
		["BL28_L_PL_006", ["Point light, int = 100, Temperature - 1000"], "Physical_Lights.blend", pl_006], 
		["BL28_L_PL_007", ["Point light, int = 100, Temperature - 3200"], "Physical_Lights.blend", pl_007], 
		["BL28_L_PL_008", ["Point light, int = 100, Temperature - 9600"], "Physical_Lights.blend", pl_008], 
		["BL28_L_PL_009", ["Point light with IES, int = 100"], "Physical_Lights.blend", pl_009], 
		["BL28_L_PL_010", ["Point light with IES, int = 1000"], "Physical_Lights.blend", pl_010], 
		["BL28_L_PL_011", ["Point light with PNG, int = 100"], "Physical_Lights.blend", pl_011], 
		["BL28_L_PL_012", ["Point light with TIFF, int = 100"], "Physical_Lights.blend", pl_012], 
		["BL28_L_PL_013", ["Point light with JPG, int = 100"], "Physical_Lights.blend", pl_013], 
		["BL28_L_PL_014", ["Point light with GrayScale, int = 100"], "Physical_Lights.blend", pl_014], 
		["BL28_L_PL_015", ["Point light with IES, int = 100, Temperature - 1000"], "Physical_Lights.blend", pl_015], 
		["BL28_L_PL_016", ["Point light with IES, int = 100, Temperature - 3200"], "Physical_Lights.blend", pl_016], 
		["BL28_L_PL_017", ["Point light with IES, int = 100, Temperature - 9600"], "Physical_Lights.blend", pl_017], 
		["BL28_L_PL_018", ["Point light, int = 100, RGB: 0.5;0;0"], "Physical_Lights.blend", pl_018], 
		["BL28_L_PL_019", ["Point light, int = 100, RGB: 0;0.5;0"], "Physical_Lights.blend", pl_019], 
		["BL28_L_PL_020", ["Point light, int = 100, RGB: 0;0;0.5"], "Physical_Lights.blend", pl_020], 
		["BL28_L_PL_021", ["Point light, Units Watts, int = 100, Luminious Efficacy - 17"], "Physical_Lights.blend", pl_021], 
		["BL28_L_PL_022", ["Point light, Units Watts, int = 100, Luminious Efficacy - 100"], "Physical_Lights.blend", pl_022], 
		["BL28_L_PL_023", ["Point light, Units Lumen, int = 100"], "Physical_Lights.blend", pl_023], 
		["BL28_L_PL_024", ["Point light, Units Lumen, int = 1000"], "Physical_Lights.blend", pl_024], 
		["BL28_L_PL_025", ["Point light, Units Lumen, int = 5000"], "Physical_Lights.blend", pl_025], 

		["BL28_L_PL_025", ["Sun light, int = 50"], "Physical_Lights.blend", pl_026], 
		["BL28_L_PL_027", ["Sun light, int = 0", "Expected Black Picture"], "Physical_Lights.blend", pl_027], 
		["BL28_L_PL_028", ["Sun light, int = 100"], "Physical_Lights.blend", pl_028], 
		["BL28_L_PL_029", ["Sun light, int = 1000"], "Physical_Lights.blend", pl_029], 
		["BL28_L_PL_030", ["Sun light, int = 5000"], "Physical_Lights.blend", pl_030], 
		["BL28_L_PL_031", ["Sun light, int = 100, Temperature - 6500"], "Physical_Lights.blend", pl_031], 
		["BL28_L_PL_032", ["Sun light, int = 100, Temperature - 1000"], "Physical_Lights.blend", pl_032], 
		["BL28_L_PL_033", ["Sun light, int = 100, Temperature - 3200"], "Physical_Lights.blend", pl_033], 
		["BL28_L_PL_034", ["Sun light, int = 100, Temperature - 9600"], "Physical_Lights.blend", pl_034], 
		["BL28_L_PL_035", ["Sun light, int = 100,  RGB: 0.5;0;0"], "Physical_Lights.blend", pl_035], 
		["BL28_L_PL_036", ["Sun light, int = 100,  RGB: 0;0.5;0"], "Physical_Lights.blend", pl_036], 
		["BL28_L_PL_037", ["Sun light, int = 100,  RGB: 0;0;0.5"], "Physical_Lights.blend", pl_037], 
		["BL28_L_PL_038", ["Sun light, Units Radiance, int = 100, Luminious Efficacy - 17"], "Physical_Lights.blend", pl_038], 
		["BL28_L_PL_039", ["Sun light, Units Radiance, int = 100, Luminious Efficacy - 100"], "Physical_Lights.blend", pl_039], 
		["BL28_L_PL_040", ["Sun light, Units Luminance, int = 100"], "Physical_Lights.blend", pl_040], 
		["BL28_L_PL_041", ["Sun light, Units Luminance, int = 1000"], "Physical_Lights.blend", pl_041], 
		["BL28_L_PL_042", ["Sun light, Units Luminance, int = 5000"], "Physical_Lights.blend", pl_042], 
		["BL28_L_PL_043", ["Sun light, int = 100, Shadow Softness - 0.00"], "Physical_Lights.blend", pl_043], 
		["BL28_L_PL_044", ["Sun light, int = 100, Shadow Softness - 0.1"], "Physical_Lights.blend", pl_044], 
		["BL28_L_PL_045", ["Sun light, int = 100, Shadow Softness - 0.5"], "Physical_Lights.blend", pl_045], 
		["BL28_L_PL_046", ["Sun light, int = 100, Shadow Softness - 1"], "Physical_Lights.blend", pl_046], 

		["BL28_L_PL_047", ["Spot light, int = 0", "Expected Black Picture"], "Physical_Lights.blend", pl_047], 
		["BL28_L_PL_048", ["Spot light, int = 100"], "Physical_Lights.blend", pl_048], 
		["BL28_L_PL_049", ["Spot light, int = 1000"], "Physical_Lights.blend", pl_049], 
		["BL28_L_PL_050", ["Spot light, int = 5000"], "Physical_Lights.blend", pl_050], 
		["BL28_L_PL_051", ["Spot light, int = 100, Temperature - 6500"], "Physical_Lights.blend", pl_051], 
		["BL28_L_PL_052", ["Spot light, int = 100, Temperature - 1000"], "Physical_Lights.blend", pl_052], 
		["BL28_L_PL_053", ["Spot light, int = 100, Temperature - 3200"], "Physical_Lights.blend", pl_053], 
		["BL28_L_PL_054", ["Spot light, int = 100, Temperature - 9600"], "Physical_Lights.blend", pl_054], 
		["BL28_L_PL_055", ["Spot light, int = 100, RGB: 0.5;0;0"], "Physical_Lights.blend", pl_055], 
		["BL28_L_PL_056", ["Spot light, int = 100, RGB: 0;0.5;0"], "Physical_Lights.blend", pl_056], 
		["BL28_L_PL_057", ["Spot light, int = 100, RGB: 0;0;0.5"], "Physical_Lights.blend", pl_057], 
		["BL28_L_PL_058", ["Spot light, Units Watt, int = 100, Luminious Efficacy - 17"], "Physical_Lights.blend", pl_058], 
		["BL28_L_PL_059", ["Spot light, Units Watt, int = 100, Luminious Efficacy - 100"], "Physical_Lights.blend", pl_059], 
		["BL28_L_PL_060", ["Spot light, Units Lumen, int = 100"], "Physical_Lights.blend", pl_060], 
		["BL28_L_PL_061", ["Spot light, Units Lumen, int = 1000"], "Physical_Lights.blend", pl_061], 
		["BL28_L_PL_062", ["Spot light, Units Lumen, int = 5000"], "Physical_Lights.blend", pl_062], 
		["BL28_L_PL_063", ["Spot light, int = 100, Spot Size - 1"], "Physical_Lights.blend", pl_063], 
		["BL28_L_PL_064", ["Spot light, int = 100, Spot Size - 45"], "Physical_Lights.blend", pl_064], 
		["BL28_L_PL_065", ["Spot light, int = 100, Spot Size - 90"], "Physical_Lights.blend", pl_065], 
		["BL28_L_PL_066", ["Spot light, int = 100, Spot Size - 180"], "Physical_Lights.blend", pl_066], 
		["BL28_L_PL_067", ["Spot light, int = 100, Spot Blend - 0"], "Physical_Lights.blend", pl_067], 
		["BL28_L_PL_068", ["Spot light, int = 100, Spot Blend - 0.15"], "Physical_Lights.blend", pl_068], 
		["BL28_L_PL_069", ["Spot light, int = 100, Spot Blend - 0.5"], "Physical_Lights.blend", pl_069], 
		["BL28_L_PL_070", ["Spot light, int = 100, Spot Blend - 1"], "Physical_Lights.blend", pl_070], 

		["BL28_L_PL_071", ["Area light, int = 0", "Expected Black Picture"], "Physical_Lights.blend", pl_071], 
		["BL28_L_PL_072", ["Area light, int = 100"], "Physical_Lights.blend", pl_072], 
		["BL28_L_PL_073", ["Area light, int = 1000"], "Physical_Lights.blend", pl_073], 
		["BL28_L_PL_074", ["Area light, int = 5000"], "Physical_Lights.blend", pl_074], 
		["BL28_L_PL_075", ["Area light, int = 0, Deactivate Intencity Normalization"], "Physical_Lights.blend", pl_075], 
		["BL28_L_PL_076", ["Area light, int = 100, Deactivate Intencity Normalization"], "Physical_Lights.blend", pl_076], 
		["BL28_L_PL_077", ["Area light, int = 1000, Deactivate Intencity Normalization"], "Physical_Lights.blend", pl_077], 
		["BL28_L_PL_078", ["Area light, int = 5000, Deactivate Intencity Normalization"], "Physical_Lights.blend", pl_078], 
		["BL28_L_PL_079", ["Area light, int = 100, Temperature - 6500"], "Physical_Lights.blend", pl_079], 
		["BL28_L_PL_080", ["Area light, int = 100, Temperature - 1000"], "Physical_Lights.blend", pl_080], 
		["BL28_L_PL_081", ["Area light, int = 100, Temperature - 3200"], "Physical_Lights.blend", pl_081], 
		["BL28_L_PL_082", ["Area light, int = 100, Temperature - 9600"], "Physical_Lights.blend", pl_082], 
		["BL28_L_PL_083", ["Area light, int = 100, RGB: 0.5;0;0"], "Physical_Lights.blend", pl_083], 
		["BL28_L_PL_084", ["Area light, int = 100, RGB: 0;0.5;0"], "Physical_Lights.blend", pl_084], 
		["BL28_L_PL_085", ["Area light, int = 100, RGB: 0;0;0.5"], "Physical_Lights.blend", pl_085], 
		["BL28_L_PL_086", ["Area light, Units Watts, int = 100, Luminious Efficacy - 17"], "Physical_Lights.blend", pl_086], 
		["BL28_L_PL_087", ["Area light, Units Watts, int = 100, Luminious Efficacy - 100"], "Physical_Lights.blend", pl_087], 
		["BL28_L_PL_088", ["Area light, Units Lumen, int = 100"], "Physical_Lights.blend", pl_088], 
		["BL28_L_PL_089", ["Area light, Units Lumen, int = 1000"], "Physical_Lights.blend", pl_089], 
		["BL28_L_PL_090", ["Area light, Units Lumen, int = 5000"], "Physical_Lights.blend", pl_090], 
		["BL28_L_PL_091", ["Area light, Units Radiance, int = 100, Luminious Efficacy - 17 "], "Physical_Lights.blend", pl_091], 
		["BL28_L_PL_092", ["Area light, Units Radiance, int = 100, Luminious Efficacy - 100 "], "Physical_Lights.blend", pl_092], 
		["BL28_L_PL_093", ["Area light, Units Luminance, int = 100"], "Physical_Lights.blend", pl_093], 
		["BL28_L_PL_094", ["Area light, Units Luminance, int = 1000"], "Physical_Lights.blend", pl_094], 
		["BL28_L_PL_095", ["Area light, Units Luminance, int = 5000"], "Physical_Lights.blend", pl_095], 
		["BL28_L_PL_096", ["Area light, Rectangle, int = 100, Size X - 0, Size Y - 0"], "Physical_Lights.blend", pl_096], 
		["BL28_L_PL_097", ["Area light, Rectangle, int = 100, Size X - 1, Size Y - 1"], "Physical_Lights.blend", pl_097], 
		["BL28_L_PL_098", ["Area light, Rectangle, int = 100, Size X - 1, Size Y - 1, Visible"], "Physical_Lights.blend", pl_098], 
		["BL28_L_PL_099", ["Area light, Rectangle, int = 100, Size X - 1, Size Y - 1, Visible, Cast Shadows"], "Physical_Lights.blend", pl_099], 
		["BL28_L_PL_100", ["Area light, Rectangle, int = 100, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_100], 
		["BL28_L_PL_101", ["Area light, Rectangle, int = 1000, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_101], 
		["BL28_L_PL_102", ["Area light, Rectangle, int = 5000, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_102], 
		["BL28_L_PL_103", ["Area light, Rectangle, int = 100, Size X - 1, Size Y - 1"], "Physical_Lights.blend", pl_103], 
		["BL28_L_PL_104", ["Area light, Rectangle, int = 100, Size X - 1, Size Y - 1, Visible"], "Physical_Lights.blend", pl_104], 
		["BL28_L_PL_105", ["Area light, Rectangle, int = 100, Size X - 1, Size Y - 1, Visible, Cast Shadows"], "Physical_Lights.blend", pl_105], 
		["BL28_L_PL_106", ["Area light, Rectangle, int = 100, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_106], 
		["BL28_L_PL_107", ["Area light, Rectangle, int = 1000, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_107], 
		["BL28_L_PL_108", ["Area light, Rectangle, int = 5000, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_108], 
		["BL28_L_PL_109", ["Area light, Square, int = 100, Size - 0"], "Physical_Lights.blend", pl_109], 
		["BL28_L_PL_110", ["Area light, Square, int = 100, Size - 1"], "Physical_Lights.blend", pl_110], 
		["BL28_L_PL_111", ["Area light, Square, int = 100, Size - 1, Visible"], "Physical_Lights.blend", pl_111], 
		["BL28_L_PL_112", ["Area light, Square, int = 100, Size - 1, Visible, Cast Shadows"], "Physical_Lights.blend", pl_112], 
		["BL28_L_PL_113", ["Area light, Square, int = 100, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_113], 
		["BL28_L_PL_114", ["Area light, Square, int = 1000, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_114], 
		["BL28_L_PL_115", ["Area light, Square, int = 5000, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_115], 
		["BL28_L_PL_116", ["Area light, Square, int = 100, Size - 1"], "Physical_Lights.blend", pl_116], 
		["BL28_L_PL_117", ["Area light, Square, int = 100, Size - 1, Visible"], "Physical_Lights.blend", pl_117], 
		["BL28_L_PL_118", ["Area light, Square, int = 100, Size - 1, Visible, Cast Shadows"], "Physical_Lights.blend", pl_118], 
		["BL28_L_PL_119", ["Area light, Square, int = 100, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_119], 
		["BL28_L_PL_120", ["Area light, Square, int = 1000, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_120], 
		["BL28_L_PL_121", ["Area light, Square, int = 5000, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_121], 
		["BL28_L_PL_122", ["Area light, Disc, int = 100, Size - 0"], "Physical_Lights.blend", pl_122], 
		["BL28_L_PL_123", ["Area light, Disc, int = 100, Size - 1"], "Physical_Lights.blend", pl_123], 
		["BL28_L_PL_124", ["Area light, Disc, int = 100, Size - 1, Visible"], "Physical_Lights.blend", pl_124], 
		["BL28_L_PL_125", ["Area light, Disc, int = 100, Size - 1, Visible, Cast Shadows"], "Physical_Lights.blend", pl_125], 
		["BL28_L_PL_126", ["Area light, Disc, int = 100, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_126], 
		["BL28_L_PL_127", ["Area light, Disc, int = 1000, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_127], 
		["BL28_L_PL_128", ["Area light, Disc, int = 5000, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_128], 
		["BL28_L_PL_129", ["Area light, Disc, int = 100, Size - 1"], "Physical_Lights.blend", pl_129], 
		["BL28_L_PL_130", ["Area light, Disc, int = 100, Size - 1, Visible"], "Physical_Lights.blend", pl_130], 
		["BL28_L_PL_131", ["Area light, Disc, int = 100, Size - 1, Visible, Cast Shadows"], "Physical_Lights.blend", pl_131], 
		["BL28_L_PL_132", ["Area light, Disc, int = 100, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_132], 
		["BL28_L_PL_133", ["Area light, Disc, int = 1000, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_133], 
		["BL28_L_PL_134", ["Area light, Disc, int = 5000, Size - 1, Intencity Normalization"], "Physical_Lights.blend", pl_134], 
		["BL28_L_PL_135", ["Area light, Ellipse, int = 100, Size X - 0, Size Y - 0"], "Physical_Lights.blend", pl_135], 
		["BL28_L_PL_136", ["Area light, Ellipse, int = 100, Size X - 1, Size Y - 1"], "Physical_Lights.blend", pl_136], 
		["BL28_L_PL_137", ["Area light, Ellipse, int = 100, Size X - 1, Size Y - 1, Visible"], "Physical_Lights.blend", pl_137], 
		["BL28_L_PL_138", ["Area light, Ellipse, int = 100, Size X - 1, Size Y - 1, Visible, Cast Shadows"], "Physical_Lights.blend", pl_138], 
		["BL28_L_PL_139", ["Area light, Ellipse, int = 100, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_139], 
		["BL28_L_PL_140", ["Area light, Ellipse, int = 1000, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_140], 
		["BL28_L_PL_141", ["Area light, Ellipse, int = 5000, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_141], 
		["BL28_L_PL_142", ["Area light, Ellipse, int = 100, Size X - 1, Size Y - 1"], "Physical_Lights.blend", pl_142], 
		["BL28_L_PL_143", ["Area light, Ellipse, int = 100, Size X - 1, Size Y - 1, Visible"], "Physical_Lights.blend", pl_143], 
		["BL28_L_PL_144", ["Area light, Ellipse, int = 100, Size X - 1, Size Y - 1, Visible, Cast Shadows"], "Physical_Lights.blend", pl_144], 
		["BL28_L_PL_145", ["Area light, Ellipse, int = 100, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_145], 
		["BL28_L_PL_146", ["Area light, Ellipse, int = 1000, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_146], 
		["BL28_L_PL_147", ["Area light, Ellipse, int = 5000, Size X - 1, Size Y - 1, Intencity Normalization"], "Physical_Lights.blend", pl_147],

		#["BL28_L_PL_148", ["Area light, Mesh, int = 100"], "Physical_Lights.blend", pl_148], 
		#["BL28_L_PL_149", ["Area light, Mesh, int = 100, Visible"], "Physical_Lights.blend", pl_149], 
		#["BL28_L_PL_150", ["Area light, Mesh, int = 100, Visible, Cast Shadows"], "Physical_Lights.blend", pl_150], 
		#["BL28_L_PL_151", ["Area light, Mesh, int = 100, Intencity Normalization"], "Physical_Lights.blend", pl_151], 
		#["BL28_L_PL_152", ["Area light, Mesh, int = 1000, Intencity Normalization"], "Physical_Lights.blend", pl_152], 
		#["BL28_L_PL_153", ["Area light, Mesh, int = 5000, Intencity Normalization"], "Physical_Lights.blend", pl_153]

	]

	launch_tests()
