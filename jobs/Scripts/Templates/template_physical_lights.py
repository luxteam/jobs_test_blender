
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	if test_list[3] == "POINT":
		return point_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7], test_list[8], test_list[9], test_list[10])
	elif test_list[3] == "SUN":    
		return sun_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7], test_list[8], test_list[9], test_list[10])
	elif test_list[3] == "SPOT":
		return spot_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7], test_list[8], test_list[9], test_list[10], test_list[11])
	elif test_list[3] == "AREA":
		return area_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7], test_list[8], test_list[9], test_list[10], test_list[11], test_list[12], test_list[13], test_list[14], test_list[15])


def point_light(test_case, script_info, intensity, use_temperature, temperature, ies, color, intensity_units_point, luminous_efficacy):

	lamp_data = bpy.data.lights['Point']
	set_value(lamp_data, 'type', 'POINT')
	set_value(lamp_data.rpr, 'intensity', intensity)
	set_value(lamp_data.rpr, 'use_temperature', use_temperature)
	set_value(lamp_data.rpr, 'temperature', temperature)
	set_value(lamp_data, 'color', color)
	set_value(lamp_data.rpr, 'intensity_units_point', intensity_units_point)
	if intensity_units_point == "WATTS":
		set_value(lamp_data.rpr, 'luminous_efficacy', luminous_efficacy)

	if ies:
		bpy.ops.image.open(filepath="//ies//{{}}".format(ies), directory="{resource_path}//ies//", files=[{{"name":"{{}}".format(ies)}}], \
																														relative_path=True, show_multiview=False)
		set_value(lamp_data.rpr, 'ies_file', bpy.data.images[ies])

	render(test_case, script_info)
	return 1


def sun_light(test_case, script_info, intensity, use_temperature, temperature, color, intensity_units_dir, luminous_efficacy, shadow_softness):

	lamp_data = bpy.data.lights['Point']
	set_value(lamp_data, 'type', 'SUN')

	set_value(lamp_data.rpr, 'intensity', intensity)
	set_value(lamp_data.rpr, 'use_temperature', use_temperature)
	set_value(lamp_data.rpr, 'temperature', temperature)
	set_value(lamp_data, 'color', color)
	set_value(lamp_data.rpr, 'intensity_units_dir', intensity_units_dir)
	if intensity_units_dir == "RADIANCE":
		set_value(lamp_data.rpr, 'luminous_efficacy', luminous_efficacy)
	set_value(lamp_data.rpr, 'shadow_softness', shadow_softness)

	render(test_case, script_info)
	return 1


def spot_light(test_case, script_info, intensity, use_temperature, temperature, spot_size, spot_blend, color, intensity_units_point, luminous_efficacy):

	lamp_data = bpy.data.lights['Point']
	set_value(lamp_data, 'type', 'SPOT')

	set_value(lamp_data.rpr, 'intensity', intensity)
	set_value(lamp_data.rpr, 'use_temperature', use_temperature)
	set_value(lamp_data.rpr, 'temperature', temperature)
	set_value(lamp_data, 'spot_size', spot_size)
	set_value(lamp_data, 'spot_blend', spot_blend)
	set_value(lamp_data, 'color', color)
	set_value(lamp_data.rpr, 'intensity_units_point', intensity_units_point)
	if intensity_units_point == "WATTS":
		set_value(lamp_data.rpr, 'luminous_efficacy', luminous_efficacy)

	render(test_case, script_info)
	return 1


def area_light(test_case, script_info, shape, intensity, intensity_normalization, use_temperature, temperature, color, intensity_units_area, luminous_efficacy, width, height, visible, cast_shadows):

	lamp_data = bpy.data.lights['Point']
	set_value(lamp_data, 'type', 'AREA')

	set_value(lamp_data.rpr, 'shape', shape)
	set_value(lamp_data.rpr, 'intensity', intensity)
	set_value(lamp_data.rpr, 'intensity_normalization', intensity_normalization)
	set_value(lamp_data.rpr, 'use_temperature', use_temperature)
	set_value(lamp_data.rpr, 'temperature', temperature)
	set_value(lamp_data, 'color', color)
	set_value(lamp_data.rpr, 'intensity_units_area', intensity_units_area)
	if intensity_units_area in ("WATTS", "RADIANCE"):
		set_value(lamp_data.rpr, 'luminous_efficacy', luminous_efficacy)

	set_value(lamp_data, 'size', width)
	set_value(lamp_data, 'size_y', height)
	set_value(lamp_data.rpr, 'visible', visible)
	set_value(lamp_data.rpr, 'cast_shadows', visible)

	if shape == "MESH":
		set_value(lamp_data.rpr, 'mesh', bpy.data.meshes["MeshLight"])

	render(test_case, script_info)
	return 1


if __name__ == "__main__":

	list_tests = [
		# POINT LIGHT 
		# test list args: 
		# 4-intensity, 5-use temperature, 6-temperature, 7-ies file, 8-color, 9-units type, 10-luminous efficacy
		["BL28_L_PL_001", ["Type: Point", "Intensity: 0", "Expected Black Picture"], "Physical_Lights.blend", 'POINT', 0, False, 6500, None, (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_002", ["Type: Point", "Intensity: 100"], "Physical_Lights.blend", 'POINT', 100, False, 6500, None, (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_003", ["Type: Point", "Intensity: 1000"], "Physical_Lights.blend", 'POINT', 1000, False, 6500, None, (1.0, 1.0, 1.0), 'DEFAULT', 100],
		["BL28_L_PL_004", ["Type: Point", "Intensity: 5000"], "Physical_Lights.blend", 'POINT', 5000, False, 6500, None, (1.0, 1.0, 1.0), 'DEFAULT', 100],   
		["BL28_L_PL_005", ["Type: Point", "Intensity: 100", "Temperature: 6500"], "Physical_Lights.blend", 'POINT', 100, True, 6500, None, (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_006", ["Type: Point", "Intensity: 100", "Temperature: 1000"], "Physical_Lights.blend", 'POINT', 100, True, 1000, None, (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_007", ["Type: Point", "Intensity: 100", "Temperature: 3200"], "Physical_Lights.blend", 'POINT', 100, True, 3200, None, (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_008", ["Type: Point", "Intensity: 100", "Temperature: 9600"], "Physical_Lights.blend", 'POINT', 100, True, 9600, None, (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_009", ["Type: Point", "Intensity: 100", "IES file: 2.ies"], "Physical_Lights.blend", 'POINT', 100, False, 6500, "2.ies", (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_010", ["Type: Point", "Intensity: 1000", "IES file: 2.ies"], "Physical_Lights.blend", 'POINT', 1000, False, 6500, "2.ies", (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_011", ["Type: Point", "Intensity: 100", "IES file: UVgrid2.png"], "Physical_Lights.blend", 'POINT', 100, False, 6500, "UVgrid2.png", (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_012", ["Type: Point", "Intensity: 100", "IES file: UVgrid2.tif"], "Physical_Lights.blend", 'POINT', 100, False, 6500, "UVgrid2.tif", (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_013", ["Type: Point", "Intensity: 100", "IES file: UVgrid2.jpg"], "Physical_Lights.blend", 'POINT', 100, False, 6500, "UVgrid2.jpg", (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_014", ["Type: Point", "Intensity: 100", "IES file: UVgrid2GS.png"], "Physical_Lights.blend", 'POINT', 100, False, 6500, "UVgrid2GS.png", (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_015", ["Type: Point", "Intensity: 100", "IES file: 2.ies", "Temperature: 1000"], "Physical_Lights.blend", 'POINT', 100, True, 1000, "2.ies", (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_016", ["Type: Point", "Intensity: 100", "IES file: 2.ies", "Temperature: 3200"], "Physical_Lights.blend", 'POINT', 100, True, 3200, "2.ies", (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_017", ["Type: Point", "Intensity: 100", "IES file: 2.ies", "Temperature: 9600"], "Physical_Lights.blend", 'POINT', 100, True, 9600, "2.ies", (1.0, 1.0, 1.0), 'DEFAULT', 100], 
		["BL28_L_PL_018", ["Type: Point", "Intensity: 100", "Color: 0.5 0 0"], "Physical_Lights.blend", 'POINT', 100, False, 6500, None, (0.5, 0, 0), 'DEFAULT', 100],
		["BL28_L_PL_019", ["Type: Point", "Intensity: 100", "Color: 0 0.5 0"], "Physical_Lights.blend", 'POINT', 100, False, 6500, None, (0, 0.5, 0), 'DEFAULT', 100],
		["BL28_L_PL_020", ["Type: Point", "Intensity: 100", "Color: 0 0 0.5"], "Physical_Lights.blend", 'POINT', 100, False, 6500, None, (0, 0, 0.5), 'DEFAULT', 100],
		["BL28_L_PL_021", ["Type: Point", "Intensity: 100", "Units: Watts", "Luminious Efficacy 17"], "Physical_Lights.blend", 'POINT', 100, False, 6500, None, (1.0, 1.0, 1.0), 'WATTS', 17], 
		["BL28_L_PL_022", ["Type: Point", "Intensity: 100", "Units: Watts", "Luminious Efficacy 100"], "Physical_Lights.blend", 'POINT', 100, False, 6500, None, (1.0, 1.0, 1.0), 'WATTS', 100], 
		["BL28_L_PL_023", ["Type: Point", "Intensity: 100"], "Physical_Lights.blend", 'POINT', 100, False, 6500, None, (1.0, 1.0, 1.0), 'LUMEN', 100], 
		["BL28_L_PL_024", ["Type: Point", "Intensity: 1000"], "Physical_Lights.blend", 'POINT', 1000, False, 6500, None, (1.0, 1.0, 1.0), 'LUMEN', 100], 
		["BL28_L_PL_025", ["Type: Point", "Intensity: 5000"], "Physical_Lights.blend", 'POINT', 5000, False, 6500, None, (1.0, 1.0, 1.0), 'LUMEN', 100], 
		# SUN LIGHT 
		# test list args: 
		# 4-intensity, 5-use temperature, 6-temperature, 7-color, 8-units type, 9-luminous efficacy, 10-shadow softness
		["BL28_L_PL_026", ["Type: Sun", "Intensity: 50"], "Physical_Lights.blend", 'SUN', 50, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0], 
		["BL28_L_PL_027", ["Type: Sun", "Intensity: 0", "Expected Black Picture"], "Physical_Lights.blend", 'SUN', 0, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0], 
		["BL28_L_PL_028", ["Type: Sun", "Intensity: 100"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0],
		["BL28_L_PL_029", ["Type: Sun", "Intensity: 1000"], "Physical_Lights.blend", 'SUN', 1000, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0],  
		["BL28_L_PL_030", ["Type: Sun", "Intensity: 5000"], "Physical_Lights.blend", 'SUN', 5000, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0], 
		["BL28_L_PL_031", ["Type: Sun", "Intensity: 100", "Temperature: 6500"], "Physical_Lights.blend", 'SUN', 100, True, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0], 
		["BL28_L_PL_032", ["Type: Sun", "Intensity: 100", "Temperature: 1000"], "Physical_Lights.blend", 'SUN', 100, True, 1000, (1.0, 1.0, 1.0), "DEFAULT", 100, 0], 
		["BL28_L_PL_033", ["Type: Sun", "Intensity: 100", "Temperature: 3200"], "Physical_Lights.blend", 'SUN', 100, True, 3200, (1.0, 1.0, 1.0), "DEFAULT", 100, 0], 
		["BL28_L_PL_034", ["Type: Sun", "Intensity: 100", "Temperature: 9600"], "Physical_Lights.blend", 'SUN', 100, True, 9600, (1.0, 1.0, 1.0), "DEFAULT", 100, 0], 
		["BL28_L_PL_035", ["Type: Sun", "Intensity: 100", "RGB: 0.5 0 0"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (0.5, 0, 0), "DEFAULT", 100, 0], 
		["BL28_L_PL_036", ["Type: Sun", "Intensity: 100", "RGB: 0 0.5 0"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (0, 0.5, 0), "DEFAULT", 100, 0], 
		["BL28_L_PL_037", ["Type: Sun", "Intensity: 100", "RGB: 0 0 0.5"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (0, 0, 0.5), "DEFAULT", 100, 0], 
		["BL28_L_PL_038", ["Type: Sun", "Intensity: 100", "Units: Radiance", "Luminious Efficacy: 17"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (1.0, 1.0, 1.0), "RADIANCE", 17, 0], 
		["BL28_L_PL_039", ["Type: Sun", "Intensity: 100", "Units: Radiance", "Luminious Efficacy: 100"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (1.0, 1.0, 1.0), "RADIANCE", 100, 0], 
		["BL28_L_PL_040", ["Type: Sun", "Intensity: 100", "Units: Luminance"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (1.0, 1.0, 1.0), "LUMINANCE", 100, 0], 
		["BL28_L_PL_041", ["Type: Sun", "Intensity: 1000", "Units: Luminance"], "Physical_Lights.blend", 'SUN', 1000, False, 6500, (1.0, 1.0, 1.0), "LUMINANCE", 100, 0], 
		["BL28_L_PL_042", ["Type: Sun", "Intensity: 5000", "Units: Luminance"], "Physical_Lights.blend", 'SUN', 5000, False, 6500, (1.0, 1.0, 1.0), "LUMINANCE", 100, 0], 
		["BL28_L_PL_043", ["Type: Sun", "Intensity: 100", "Shadow Softness: 0"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0], 
		["BL28_L_PL_044", ["Type: Sun", "Intensity: 100", "Shadow Softness: 0.1"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0.1], 
		["BL28_L_PL_045", ["Type: Sun", "Intensity: 100", "Shadow Softness: 0.5"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0.5], 
		["BL28_L_PL_046", ["Type: Sun", "Intensity: 100", "Shadow Softness: 1.0"], "Physical_Lights.blend", 'SUN', 100, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0], 
		# SPOT LIGHT 
		# test list args: 
		# 4-intensity, 5-use temperature, 6-temperature, 7-spot size, 8-spot blend, 9-color, 10-units type, 11-luminous efficacy
		["BL28_L_PL_047", ["Type: Spot", "Intensity: 0", "Expected Black Picture"], "Physical_Lights.blend", 'SPOT', 0, False, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100], 
		["BL28_L_PL_048", ["Type: Spot", "Intensity: 100"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_049", ["Type: Spot", "Intensity: 1000"], "Physical_Lights.blend", 'SPOT', 1000, False, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_050", ["Type: Spot", "Intensity: 5000"], "Physical_Lights.blend", 'SPOT', 5000, False, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_051", ["Type: Spot", "Intensity: 100", "Temperature: 6500"], "Physical_Lights.blend", 'SPOT', 100, True, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_052", ["Type: Spot", "Intensity: 100", "Temperature: 1000"], "Physical_Lights.blend", 'SPOT', 100, True, 1000, 1.309, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_053", ["Type: Spot", "Intensity: 100", "Temperature: 3200"], "Physical_Lights.blend", 'SPOT', 100, True, 3200, 1.309, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_054", ["Type: Spot", "Intensity: 100", "Temperature: 9600"], "Physical_Lights.blend", 'SPOT', 100, True, 9600, 1.309, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_055", ["Type: Spot", "Intensity: 100", "RGB: 0.5 0 0"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0.511, (0.5, 0, 0), "DEFAULT", 100],
		["BL28_L_PL_056", ["Type: Spot", "Intensity: 100", "RGB: 0 0.5 0"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0.511, (0, 0.5, 0), "DEFAULT", 100],
		["BL28_L_PL_057", ["Type: Spot", "Intensity: 100", "RGB: 0 0 0.5"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0.511, (0, 0, 0.5), "DEFAULT", 100],
		["BL28_L_PL_058", ["Type: Spot", "Intensity: 100", "Units type: Watts", "Luminous efficacy: 17"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "WATTS", 17],
		["BL28_L_PL_059", ["Type: Spot", "Intensity: 100", "Units type: Watts", "Luminous efficacy: 100"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "WATTS", 100],
		["BL28_L_PL_060", ["Type: Spot", "Intensity: 100", "Units type: Lumen"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "LUMEN", 100],
		["BL28_L_PL_061", ["Type: Spot", "Intensity: 1000", "Units type: Lumen"], "Physical_Lights.blend", 'SPOT', 1000, False, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "LUMEN", 100],
		["BL28_L_PL_062", ["Type: Spot", "Intensity: 5000", "Units type: Lumen"], "Physical_Lights.blend", 'SPOT', 5000, False, 6500, 1.309, 0.511, (1.0, 1.0, 1.0), "LUMEN", 100],
		["BL28_L_PL_063", ["Type: Spot", "Intensity: 100", "Spot Size: 1", "Expected Black Picture"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 0.0174533, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_064", ["Type: Spot", "Intensity: 100", "Spot Size: 45"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 0.785398, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_065", ["Type: Spot", "Intensity: 100", "Spot Size: 90"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.5708, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_066", ["Type: Spot", "Intensity: 100", "Spot Size: 180"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 3.14159, 0.511, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_067", ["Type: Spot", "Intensity: 100", "Spot Size: 75", "Spot blend: 0"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_068", ["Type: Spot", "Intensity: 100", "Spot Size: 75", "Spot blend: 0.15"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0.15, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_069", ["Type: Spot", "Intensity: 100", "Spot Size: 75", "Spot blend: 0.5"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 0.5, (1.0, 1.0, 1.0), "DEFAULT", 100],
		["BL28_L_PL_070", ["Type: Spot", "Intensity: 100", "Spot Size: 75", "Spot blend: 1.0"], "Physical_Lights.blend", 'SPOT', 100, False, 6500, 1.309, 1.0, (1.0, 1.0, 1.0), "DEFAULT", 100],
		# SPOT LIGHT 
		# test list args: 
		# 4-type, 5-intensity, 6-intensity normalization, 7-use temperature, 8-temperature, 9-color, 10-units type, 11-luminous efficacy, 12-size x, 13-size y, 14-visible, 15-cast shadows
		["BL28_L_PL_071", ["Type: Area", "Intensity: 0", "Expected Black Picture"], "Physical_Lights.blend", 'AREA', 'SQUARE', 0, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_072", ["Type: Area", "Intensity: 100"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_073", ["Type: Area", "Intensity: 1000"], "Physical_Lights.blend", 'AREA', 'SQUARE', 1000, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_074", ["Type: Area", "Intensity: 5000"], "Physical_Lights.blend", 'AREA', 'SQUARE', 5000, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_075", ["Type: Area", "Intensity: 0", "Expected Black Picture", "Intensity Normalization"], "Physical_Lights.blend", 'AREA', 'SQUARE', 0, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_076", ["Type: Area", "Intensity: 100", "Intensity Normalization: true"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_077", ["Type: Area", "Intensity: 1000", "Intensity Normalization: true"], "Physical_Lights.blend", 'AREA', 'SQUARE', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_078", ["Type: Area", "Intensity: 5000", "Intensity Normalization: true"], "Physical_Lights.blend", 'AREA', 'SQUARE', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_079", ["Type: Area", "Intensity: 100", "Temperature: 6500"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, True, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_080", ["Type: Area", "Intensity: 100", "Temperature: 1000"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, True, 1000, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_081", ["Type: Area", "Intensity: 100", "Temperature: 3200"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, True, 3200, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_082", ["Type: Area", "Intensity: 100", "Temperature: 9600"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, True, 9600, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_083", ["Type: Area", "Intensity: 100", "Color 0.5 0 0"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (0.5, 0, 0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_084", ["Type: Area", "Intensity: 100", "Color 0 0.5 0"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (0, 0.5, 0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_085", ["Type: Area", "Intensity: 100", "Color 0 0 0.5"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (0, 0, 0.5), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_086", ["Type: Area", "Intensity: 100", "Units: Watts", "Luminous Efficacy: 17"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "WATTS", 17, 1.0, 1.0, False, False],
		["BL28_L_PL_087", ["Type: Area", "Intensity: 100", "Units: Watts", "Luminous Efficacy: 100"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "WATTS", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_088", ["Type: Area", "Intensity: 100", "Units: Lumen"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (01.0, 1.0, 1.0), "LUMEN", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_089", ["Type: Area", "Intensity: 1000", "Units: Lumen"], "Physical_Lights.blend", 'AREA', 'SQUARE', 1000, True, False, 6500, (1.0, 1.0, 1.0), "LUMEN", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_090", ["Type: Area", "Intensity: 5000", "Units: Lumen"], "Physical_Lights.blend", 'AREA', 'SQUARE', 5000, True, False, 6500, (1.0, 1.0, 1.0), "LUMEN", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_091", ["Type: Area", "Intensity: 100", "Units: Radiance", "Luminous Efficacy: 17"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "RADIANCE", 17, 1.0, 1.0, False, False],
		["BL28_L_PL_092", ["Type: Area", "Intensity: 100", "Units: Radiance", "Luminous Efficacy: 100"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "RADIANCE", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_093", ["Type: Area", "Intensity: 100", "Units: Luminance"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "LUMINANCE", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_094", ["Type: Area", "Intensity: 1000", "Units: Luminance"], "Physical_Lights.blend", 'AREA', 'SQUARE', 1000, True, False, 6500, (1.0, 1.0, 1.0), "LUMINANCE", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_095", ["Type: Area", "Intensity: 5000", "Units: Luminance"], "Physical_Lights.blend", 'AREA', 'SQUARE', 5000, True, False, 6500, (1.0, 1.0, 1.0), "LUMINANCE", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_096", ["Type: Area", "Intensity: 100", "Type: Rectangle", "Size X&Y: 0", "Expected Black Picture"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0, 0, False, False],
		["BL28_L_PL_097", ["Type: Area", "Intensity: 100", "Type: Rectangle", "Size X&Y: 1"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_098", ["Type: Area", "Intensity: 100", "Type: Rectangle", "Size X&Y: 1", "Visible: true"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, False],
		["BL28_L_PL_099", ["Type: Area", "Intensity: 100", "Type: Rectangle", "Size X&Y: 1", "Visible: true", "Cast shadows: true"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, True],
		["BL28_L_PL_100", ["Type: Area", "Intensity: 100", "Type: Rectangle", "Size X&Y: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_101", ["Type: Area", "Intensity: 1000", "Type: Rectangle", "Size X&Y: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_102", ["Type: Area", "Intensity: 5000", "Type: Rectangle", "Size X&Y: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_103", ["Type: Area", "Intensity: 100", "Type: Rectangle", "Size X: 1", "Size Y: 3"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, False, False],
		["BL28_L_PL_104", ["Type: Area", "Intensity: 100", "Type: Rectangle", "Size X: 1", "Size Y: 3", "Visible: true"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, True, False],
		["BL28_L_PL_105", ["Type: Area", "Intensity: 100", "Type: Rectangle", "Size X: 1", "Size Y: 3", "Visible: true", "Cast shadows: true"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, True, True],
		["BL28_L_PL_106", ["Type: Area", "Intensity: 100", "Type: Rectangle", "Size X: 1", "Size Y: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, False, False],
		["BL28_L_PL_107", ["Type: Area", "Intensity: 1000", "Type: Rectangle", "Size X: 1", "Size Y: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, False, False],
		["BL28_L_PL_108", ["Type: Area", "Intensity: 5000", "Type: Rectangle", "Size X: 1", "Size Y: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'RECTANGLE', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, False, False],
		["BL28_L_PL_109", ["Type: Area", "Intensity: 100", "Type: Square", "Size: 0", "Expected Black Picture"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0, 1.0, False, False],
		["BL28_L_PL_110", ["Type: Area", "Intensity: 100", "Type: Square", "Size: 1"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_111", ["Type: Area", "Intensity: 100", "Type: Square", "Size: 1", "Visible: true"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, False],
		["BL28_L_PL_112", ["Type: Area", "Intensity: 100", "Type: Square", "Size: 1", "Visible: true", "Cast shadows: true"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, True],
		["BL28_L_PL_113", ["Type: Area", "Intensity: 100", "Type: Square", "Size: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_114", ["Type: Area", "Intensity: 1000", "Type: Square", "Size: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'SQUARE', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_115", ["Type: Area", "Intensity: 5000", "Type: Square", "Size: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'SQUARE', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_116", ["Type: Area", "Intensity: 100", "Type: Square", "Size: 3"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, False, False],
		["BL28_L_PL_117", ["Type: Area", "Intensity: 100", "Type: Square", "Size: 3", "Visible: true"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, True, False],
		["BL28_L_PL_118", ["Type: Area", "Intensity: 100", "Type: Square", "Size: 3", "Visible: true", "Cast shadows: true"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, True, True],
		["BL28_L_PL_119", ["Type: Area", "Intensity: 100", "Type: Square", "Size: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'SQUARE', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, False, False],
		["BL28_L_PL_120", ["Type: Area", "Intensity: 1000", "Type: Square", "Size: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'SQUARE', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, False, False],
		["BL28_L_PL_121", ["Type: Area", "Intensity: 5000", "Type: Square", "Size: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'SQUARE', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, False, False],
		["BL28_L_PL_122", ["Type: Area", "Intensity: 100", "Type: Disk", "Size: 0", "Expected Black Picture"], "Physical_Lights.blend", 'AREA', 'DISK', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0, 1.0, False, False],
		["BL28_L_PL_123", ["Type: Area", "Intensity: 100", "Type: Disk", "Size: 1"], "Physical_Lights.blend", 'AREA', 'DISK', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_124", ["Type: Area", "Intensity: 100", "Type: Disk", "Size: 1", "Visible: true"], "Physical_Lights.blend", 'AREA', 'DISK', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, False],
		["BL28_L_PL_125", ["Type: Area", "Intensity: 100", "Type: Disk", "Size: 1", "Visible: true", "Cast shadows: true"], "Physical_Lights.blend", 'AREA', 'DISK', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, True],
		["BL28_L_PL_126", ["Type: Area", "Intensity: 100", "Type: Disk", "Size: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'DISK', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_127", ["Type: Area", "Intensity: 1000", "Type: Disk", "Size: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'DISK', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_128", ["Type: Area", "Intensity: 5000", "Type: Disk", "Size: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'DISK', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_129", ["Type: Area", "Intensity: 100", "Type: Disk", "Size: 3"], "Physical_Lights.blend", 'AREA', 'DISK', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, False, False],
		["BL28_L_PL_130", ["Type: Area", "Intensity: 100", "Type: Disk", "Size: 3", "Visible: true"], "Physical_Lights.blend", 'AREA', 'DISK', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, True, False],
		["BL28_L_PL_131", ["Type: Area", "Intensity: 100", "Type: Disk", "Size: 3", "Visible: true", "Cast shadows: true"], "Physical_Lights.blend", 'AREA', 'DISK', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, True, True],
		["BL28_L_PL_132", ["Type: Area", "Intensity: 100", "Type: Disk", "Size: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'DISK', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, False, False],
		["BL28_L_PL_133", ["Type: Area", "Intensity: 1000", "Type: Disk", "Size: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'DISK', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, False, False],
		["BL28_L_PL_134", ["Type: Area", "Intensity: 5000", "Type: Disk", "Size: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'DISK', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 3.0, 1.0, False, False],
		["BL28_L_PL_135", ["Type: Area", "Intensity: 100", "Type: Ellipse", "Size X&Y: 0", "Expected Black Picture"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 0, 0, False, False],
		["BL28_L_PL_136", ["Type: Area", "Intensity: 100", "Type: Ellipse", "Size X&Y: 1"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_137", ["Type: Area", "Intensity: 100", "Type: Ellipse", "Size X&Y: 1", "Visible: true"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, False],
		["BL28_L_PL_138", ["Type: Area", "Intensity: 100", "Type: Ellipse", "Size X&Y: 1", "Visible: true", "Cast shadows: true"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, True],
		["BL28_L_PL_139", ["Type: Area", "Intensity: 100", "Type: Ellipse", "Size X&Y: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_140", ["Type: Area", "Intensity: 1000", "Type: Ellipse", "Size X&Y: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_141", ["Type: Area", "Intensity: 5000", "Type: Ellipse", "Size X&Y: 1", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_142", ["Type: Area", "Intensity: 100", "Type: Ellipse", "Size X: 1", "Size Y: 3"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, False, False],
		["BL28_L_PL_143", ["Type: Area", "Intensity: 100", "Type: Ellipse", "Size X: 1", "Size Y: 3", "Visible: true"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, True, False],
		["BL28_L_PL_144", ["Type: Area", "Intensity: 100", "Type: Ellipse", "Size X: 1", "Size Y: 3", "Visible: true", "Cast shadows: true"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, True, True],
		["BL28_L_PL_145", ["Type: Area", "Intensity: 100", "Type: Ellipse", "Size X: 1", "Size Y: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, False, False],
		["BL28_L_PL_146", ["Type: Area", "Intensity: 1000", "Type: Ellipse", "Size X: 1", "Size Y: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, False, False],
		["BL28_L_PL_147", ["Type: Area", "Intensity: 5000", "Type: Ellipse", "Size X: 1", "Size Y: 3", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'ELLIPSE', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 3.0, False, False],
		["BL28_L_PL_148", ["Type: Area", "Intensity: 100", "Type: Mesh"], "Physical_Lights.blend", 'AREA', 'MESH', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_149", ["Type: Area", "Intensity: 100", "Type: Mesh", "Visible: true"], "Physical_Lights.blend", 'AREA', 'MESH', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, False],
		["BL28_L_PL_150", ["Type: Area", "Intensity: 100", "Type: Mesh", "Visible: true", "Cast shadows: true"], "Physical_Lights.blend", 'AREA', 'MESH', 100, True, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, True, True],
		["BL28_L_PL_151", ["Type: Area", "Intensity: 100", "Type: Mesh", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'MESH', 100, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_152", ["Type: Area", "Intensity: 1000", "Type: Mesh", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'MESH', 1000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],
		["BL28_L_PL_153", ["Type: Area", "Intensity: 5000", "Type: Mesh", "Intensity Normalization: false"], "Physical_Lights.blend", 'AREA', 'MESH', 5000, False, False, 6500, (1.0, 1.0, 1.0), "DEFAULT", 100, 1.0, 1.0, False, False],

	]

	launch_tests()
