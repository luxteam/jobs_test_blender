
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	if test_list[3] == "POINT":
		return point_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7])
	elif test_list[3] == "SUN":    
		return sun_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6])
	elif test_list[3] == "SPOT":
		return spot_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7], test_list[8])
	elif test_list[3] == "AREA":
		return area_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7], test_list[8], test_list[9], test_list[10], test_list[11])


def point_light(test_case, script_info, intensity, use_temperature, temperature, ies):

	lamp_data = bpy.data.lights['Point']
	set_value(lamp_data, 'type', 'POINT')
	set_value(lamp_data.rpr, 'intensity', intensity)
	set_value(lamp_data.rpr, 'use_temperature', use_temperature)
	set_value(lamp_data.rpr, 'temperature', temperature)
	
	if ies:
		bpy.ops.image.open(filepath="//ies//{{}}".format(ies), directory="{resource_path}//ies//", files=[{{"name":"{{}}".format(ies)}}], \
																														relative_path=True, show_multiview=False)
		set_value(lamp_data.rpr, 'ies_file', bpy.data.images[ies])

	render(test_case, script_info)
	return 1


def sun_light(test_case, script_info, intensity, use_temperature, temperature):

	lamp_data = bpy.data.lights['Point']
	set_value(lamp_data, 'type', 'SUN')

	set_value(lamp_data.rpr, 'intensity', intensity)
	set_value(lamp_data.rpr, 'use_temperature', use_temperature)
	set_value(lamp_data.rpr, 'temperature', temperature)

	render(test_case, script_info)
	return 1


def spot_light(test_case, script_info, intensity, use_temperature, temperature, angle, fallof):

	lamp_data = bpy.data.lights['Point']
	set_value(lamp_data, 'type', 'SPOT')

	set_value(lamp_data.rpr, 'intensity', intensity)
	set_value(lamp_data.rpr, 'use_temperature', use_temperature)
	set_value(lamp_data.rpr, 'temperature', temperature)
	set_value(lamp_data.rpr, 'spot_size', angle)
	set_value(lamp_data.rpr, 'spot_blend', fallof)

	render(test_case, script_info)
	return 1


def area_light(test_case, script_info, shape, intensity, use_temperature, temperature, width, height, visible, mesh_obj):

	lamp_data = bpy.data.lights['Point']
	set_value(lamp_data, 'type', 'AREA')

	set_value(lamp_data.rpr, 'shape', shape)
	set_value(lamp_data.rpr, 'intensity', intensity)
	set_value(lamp_data.rpr, 'use_temperature', use_temperature)
	set_value(lamp_data.rpr, 'temperature', temperature)

	set_value(lamp_data.rpr, 'size', width)
	set_value(lamp_data.rpr, 'size_y', height)
	set_value(lamp_data.rpr, 'visible', visible)

	if shape == "MESH":
		set_value(lamp_data.rpr, 'mesh', bpy.data.meshes["{{}}".format(mesh_obj)])

	render(test_case, script_info)
	return 1


if __name__ == "__main__":

	list_tests = [
		# POINT
		["BL28_L_PL_001", ["Type: Point", "Intensity: 1000"], "Physical_Lights.blend", 'POINT', 1000, False, 6500, None], 
		["BL28_L_PL_002", ["Type: Point", "Intensity: 0, Expected Black Picture"], "Physical_Lights.blend", 'POINT', 0, False, 6500, None], 
		["BL28_L_PL_003", ["Type: Point", "Intensity: 5000"], "Physical_Lights.blend", 'POINT', 5000, False, 6500, None],
		["BL28_L_PL_004", ["Type: Point", "Intensity: 1000", "Temperature: 6500"], "Physical_Lights.blend", 'POINT', 1000, True, 6500, None],   
		["BL28_L_PL_005", ["Type: Point", "Intensity: 1000", "Temperature: 0"], "Physical_Lights.blend", 'POINT', 1000, True, 0, None], 
		["BL28_L_PL_006", ["Type: Point", "Intensity: 1000", "Temperature: 40 000"], "Physical_Lights.blend", 'POINT', 1000, True, 40000, None], 
		["BL28_L_PL_007", ["Type: Point", "Intensity: 1000", "IES file: 2.ies"], "Physical_Lights.blend", 'POINT', 1000, False, 6500, "2.ies"], 
		# SUN
		["BL28_L_PL_008", ["Type: Sun", "Intensity: 50"], "Physical_Lights.blend", 'SUN', 50, False, 6500], 
		["BL28_L_PL_009", ["Type: Sun", "Intensity: 1000"], "Physical_Lights.blend", 'SUN', 1000, False, 6500], 
		["BL28_L_PL_010", ["Type: Sun", "Intensity: 0, Expected Black Picture"], "Physical_Lights.blend", 'SUN', 0, False, 6500],
		["BL28_L_PL_011", ["Type: Sun", "Intensity: 5000"], "Physical_Lights.blend", 'SUN', 5000, False, 6500],  
		["BL28_L_PL_012", ["Type: Sun", "Intensity: 1000", "Temperature: 6500"], "Physical_Lights.blend", 'SUN', 1000, True, 6500], 
		["BL28_L_PL_013", ["Type: Sun", "Intensity: 1000", "Temperature: 0"], "Physical_Lights.blend", 'SUN', 1000, True, 0], 
		["BL28_L_PL_014", ["Type: Sun", "Intensity: 1000", "Temperature: 40 000"], "Physical_Lights.blend", 'SUN', 1000, True, 40000], 
		# SPOT
		["BL28_L_PL_015", ["Type: Spot", "Intensity: 2000"], "Physical_Lights.blend", 'SPOT', 2000, False, 6500, 1.309, 0.15], 
		["BL28_L_PL_016", ["Type: Spot", "Intensity: 1000"], "Physical_Lights.blend", 'SPOT', 1000, False, 6500, 1.309, 0.15],
		["BL28_L_PL_017", ["Type: Spot", "Intensity: 0, Expected Black Picture"], "Physical_Lights.blend", 'SPOT', 0, False, 6500, 1.309, 0.15],
		["BL28_L_PL_018", ["Type: Spot", "Intensity: 5000"], "Physical_Lights.blend", 'SPOT', 5000, False, 6500, 1.309, 0.15],
		["BL28_L_PL_019", ["Type: Spot", "Intensity: 1000", "Temperature: 6500"], "Physical_Lights.blend", 'SPOT', 1000, True, 6500, 1.309, 0.15],
		["BL28_L_PL_020", ["Type: Spot", "Intensity: 1000", "Temperature: 0"], "Physical_Lights.blend", 'SPOT', 1000, True, 0, 1.309, 0.15],
		["BL28_L_PL_021", ["Type: Spot", "Intensity: 1000", "Temperature: 40 000"], "Physical_Lights.blend", 'SPOT', 1000, True, 40000, 1.309, 0.15],
		["BL28_L_PL_022", ["Type: Spot", "Intensity: 1000", "Angle: 1"], "Physical_Lights.blend", 'SPOT', 1000, False, 6500, 0.0174533, 0.15],
		["BL28_L_PL_023", ["Type: Spot", "Intensity: 1000", "Angle: 180"], "Physical_Lights.blend", 'SPOT', 1000, False, 6500, 3.14159, 0.15],
		["BL28_L_PL_024", ["Type: Spot", "Intensity: 1000", "Falloff: 0"], "Physical_Lights.blend", 'SPOT', 1000, False, 6500, 1.309, 0],
		["BL28_L_PL_025", ["Type: Spot", "Intensity: 1000", "Falloff: 1"], "Physical_Lights.blend", 'SPOT', 1000, False, 6500, 1.309, 1],
		# AREA
		["BL28_L_PL_026", ["Type: Area", "Intensity: 300"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 300, False, 6500, 0.1, 0.1, False, None],
		["BL28_L_PL_027", ["Type: Area", "Intensity: 1000"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 1000, False, 6500, 0.1, 0.1, False, None],
		["BL28_L_PL_028", ["Type: Area", "Intensity: 0, Expected Black Picture"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 0, False, 6500, 0.1, 0.1, False, None],
		["BL28_L_PL_029", ["Type: Area", "Intensity: 5000"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 5000, False, 6500, 0.1, 0.1, False, None],
		["BL28_L_PL_030", ["Type: Area", "Intensity: 1000, Expected Black Picture", "Width, Height: 0"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 1000, False, 6500, 0, 0, False, None],
		["BL28_L_PL_031", ["Type: Area", "Intensity: 1000", "Width, Height: 100"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 1000, False, 6500, 100, 100, False, None],
		["BL28_L_PL_032", ["Type: Area", "Intensity: 1000", "Width, Height: 100", "Visible: active"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 1000, False, 6500, 100, 100, True, None],
		["BL28_L_PL_033", ["Type: Area", "Intensity: 1000", "Shape type: Rectangle"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 1000, False, 6500, 0.1, 0.1, False, None],
		["BL28_L_PL_034", ["Type: Area", "Intensity: 1000", "Shape type: Square"], "Physical_Lights.blend", 'AREA', 'SQUARE', 1000, False, 6500, 0.1, 0.1, False, None],
		["BL28_L_PL_035", ["Type: Area", "Intensity: 1000", "Shape type: Disk"], "Physical_Lights.blend", 'AREA', 'DISK', 1000, False, 6500, 0.1, 0.1, False, None],
		["BL28_L_PL_036", ["Type: Area", "Intensity: 1000", "Shape type: Ellipse"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 1000, False, 6500, 0.1, 0.1, False, None],
		["BL28_L_PL_037", ["Type: Area", "Intensity: 1000", "Shape type: Mesh"], "Physical_Lights.blend", 'AREA', 'MESH', 1000, False, 6500, 0.1, 0.1, False, 'Cube'],
		["BL28_L_PL_038", ["Type: Area", "Intensity: 1000", "Temperature: 0"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 1000, True, 0, 0.1, 0.1, False, None],
		["BL28_L_PL_039", ["Type: Area", "Intensity: 1000", "Temperature: 40 000"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 1000, True, 40000, 0.1, 0.1, False, None],
	]

	launch_tests()
