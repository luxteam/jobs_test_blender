from math import radians


def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", "Render_Settings", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	rpr_env = bpy.context.scene.world.rpr
	rpr_env.mode = 'SUN_SKY'
	# setup type default sun_sky params
	rpr_env.sun_sky.ground_color = (0.4, 0.00703741, 0.00508468)
	rpr_env.sun_sky.resolution = test_list[4]
		

	if (test_list[3] == 'ANALYTICAL'):
		rpr_env.sun_sky.type = test_list[3]
		rpr_env.sun_sky.azimuth = radians(test_list[5])
		rpr_env.sun_sky.altitude = radians(test_list[6])
	elif (test_list[3] == 'turbidity'):
		rpr_env.sun_sky.azimuth = radians(18)
		rpr_env.sun_sky.altitude = radians(5)
		rpr_env.sun_sky.turbidity = test_list[5]
	elif (test_list[3] == 'intencity'):
		rpr_env.sun_sky.azimuth = radians(18)
		rpr_env.sun_sky.altitude = radians(5)
		rpr_env.sun_sky.turbidity = 0.2
		rpr_env.intensity = test_list[5]
	elif (test_list[3] == "sun_glow"):
		rpr_env.sun_sky.azimuth = radians(18)
		rpr_env.sun_sky.altitude = radians(5)
		rpr_env.sun_sky.turbidity = 0.2
		rpr_env.sun_sky.sun_glow = test_list[5]
	elif (test_list[3] == "sun_disc"):
		rpr_env.sun_sky.azimuth = radians(18)
		rpr_env.sun_sky.altitude = radians(5)
		rpr_env.sun_sky.turbidity = 0.2
		rpr_env.sun_sky.sun_glow = 1
		rpr_env.sun_sky.sun_disc = test_list[5]
	elif (test_list[3] == "saturation"):
		rpr_env.sun_sky.azimuth = radians(18)
		rpr_env.sun_sky.altitude = radians(5)
		rpr_env.sun_sky.turbidity = 0.2
		rpr_env.sun_sky.sun_glow = 1
		rpr_env.sun_sky.sun_disc = 0.5
		rpr_env.sun_sky.saturation = test_list[5]
	elif (test_list[3] == "horizon_heigh"):
		rpr_env.sun_sky.azimuth = radians(18)
		rpr_env.sun_sky.altitude = radians(5)
		rpr_env.sun_sky.turbidity = 0.2
		rpr_env.sun_sky.sun_glow = 1
		rpr_env.sun_sky.sun_disc = 0.5
		rpr_env.sun_sky.saturation = 0.5
		rpr_env.sun_sky.horizon_height = test_list[5]
	elif (test_list[3] == "horizon_blue"):
		rpr_env.sun_sky.azimuth = radians(18)
		rpr_env.sun_sky.altitude = radians(5)
		rpr_env.sun_sky.turbidity = 0.2
		rpr_env.sun_sky.sun_glow = 1
		rpr_env.sun_sky.sun_disc = 0.5
		rpr_env.sun_sky.saturation = 0.5
		rpr_env.sun_sky.horizon_height = 0
		rpr_env.sun_sky.horizon_blue = test_list[5]
	elif (test_list[3] == "filter_color"):
		rpr_env.sun_sky.azimuth = radians(18)
		rpr_env.sun_sky.altitude = radians(5)
		rpr_env.sun_sky.turbidity = 0.2
		rpr_env.sun_sky.sun_glow = 1
		rpr_env.sun_sky.sun_disc = 0.5
		rpr_env.sun_sky.saturation = 0.5
		rpr_env.sun_sky.horizon_height = 0
		rpr_env.sun_sky.horizon_blue = 0.5
		rpr_env.sun_sky.filter_color = test_list[5]
	elif (test_list[3] == "ground_color"):
		rpr_env.sun_sky.azimuth = radians(18)
		rpr_env.sun_sky.altitude = radians(5)
		rpr_env.sun_sky.turbidity = 0.2
		rpr_env.sun_sky.sun_glow = 1
		rpr_env.sun_sky.sun_disc = 0.5
		rpr_env.sun_sky.saturation = 0.5
		rpr_env.sun_sky.horizon_height = 0
		rpr_env.sun_sky.horizon_blue = 0.5
		rpr_env.sun_sky.filter_color = (1,0,1)
		rpr_env.sun_sky.ground_color = test_list[5]

	elif (test_list[3] == 'date_time_location'):

		rpr_env.sun_sky.latitude = 56
		rpr_env.sun_sky.longitude = 38
		rpr_env.sun_sky.time_zone = 3.0

		if (test_list[6] == "Moscow"):
			rpr_env.sun_sky.time_zone = 3
			rpr_env.sun_sky.latitude = 0.973583
			rpr_env.sun_sky.longitude = 0.656516
		elif (test_list[6] == "Canberra"):
			rpr_env.sun_sky.time_zone = 11
			rpr_env.sun_sky.latitude = -0.615752
			rpr_env.sun_sky.longitude = 2.60277
		elif (test_list[6] == "Miami_Beach"):
			rpr_env.sun_sky.time_zone = -5
			rpr_env.sun_sky.latitude = 0.450131
			rpr_env.sun_sky.longitude = -1.39853

		rpr_env.sun_sky.time_hours = test_list[5][0]
		rpr_env.sun_sky.time_minutes = test_list[5][1]
		rpr_env.sun_sky.time_seconds = test_list[5][2]


	render(test_list[0], test_list[1])
	return 1


if __name__ == "__main__":

	list_tests = [
	["BL_RS_SS_001", ["Sun&Sky System: Analytical sky", "Azimuth: 0", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'ANALYTICAL', '1024', 0, 0],
	["BL_RS_SS_002", ["Sun&Sky System: Analytical sky", "Azimuth: 0", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 0, 45],
	["BL_RS_SS_003", ["Sun&Sky System: Analytical sky", "Azimuth: 0", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 0, 90],
	["BL_RS_SS_004", ["Sun&Sky System: Analytical sky", "Azimuth: 90", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'ANALYTICAL', '1024', 90, 0],
	["BL_RS_SS_005", ["Sun&Sky System: Analytical sky", "Azimuth: 90", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 90, 45],
	["BL_RS_SS_006", ["Sun&Sky System: Analytical sky", "Azimuth: 90", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 90, 90],
	["BL_RS_SS_007", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'ANALYTICAL', '1024', 180, 0],
	["BL_RS_SS_008", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 180, 45],
	["BL_RS_SS_009", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 180, 90],
	["BL_RS_SS_010", ["Sun&Sky System: Analytical sky", "Azimuth: 270", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'ANALYTICAL', '1024', 270, 0],
	["BL_RS_SS_011", ["Sun&Sky System: Analytical sky", "Azimuth: 270", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 270, 45],
	["BL_RS_SS_012", ["Sun&Sky System: Analytical sky", "Azimuth: 270", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 270, 90],
	["BL_RS_SS_013", ["Sun&Sky System: Analytical sky", "Azimuth: 360", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'ANALYTICAL', '1024', 360, 0],
	["BL_RS_SS_014", ["Sun&Sky System: Analytical sky", "Azimuth: 360", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 360, 45],
	["BL_RS_SS_015", ["Sun&Sky System: Analytical sky", "Azimuth: 360", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'ANALYTICAL', '1024', 360, 90],
	
	["BL_RS_SS_016", ["Sun&Sky System: Date, Time and Location", "Texture Resolution: small"], "TestSunSky.blend", 'textire_resolution', '256'],
	["BL_RS_SS_017", ["Sun&Sky System: Date, Time and Location",  "Texture Resolution: normal"], "TestSunSky.blend", 'textire_resolution', '1024'],
	["BL_RS_SS_018", ["Sun&Sky System: Date, Time and Location",  "Texture Resolution: high"], "TestSunSky.blend", 'textire_resolution', '4096'],

	["BL_RS_SS_019", ["Sun&Sky System: Date, Time and Location", "Turbidity - 0.2"], "TestSunSky.blend", 'turbidity', '1024', 0.2],
	["BL_RS_SS_020", ["Sun&Sky System: Date, Time and Location", "Turbidity - 1"], "TestSunSky.blend", 'turbidity', '1024', 1],
	["BL_RS_SS_021", ["Sun&Sky System: Date, Time and Location", "Turbidity - 2"], "TestSunSky.blend", 'turbidity', '1024', 2],
	["BL_RS_SS_022", ["Sun&Sky System: Date, Time and Location", "Turbidity - 5"], "TestSunSky.blend", 'turbidity', '1024', 5],
	
	["BL_RS_SS_023", ["Sun&Sky System: Date, Time and Location", "Intencity - 1"], "TestSunSky.blend", 'intencity', '1024', 1],
	["BL_RS_SS_024", ["Sun&Sky System: Date, Time and Location", "Intencity - 2"], "TestSunSky.blend", 'intencity', '1024', 2],
	["BL_RS_SS_025", ["Sun&Sky System: Date, Time and Location", "Intencity - 5"], "TestSunSky.blend", 'intencity', '1024', 5],
	
	["BL_RS_SS_026", ["Sun&Sky System: Date, Time and Location", "Sun Glow - 1"], "TestSunSky.blend", 'sun_glow', '1024', 1],
	["BL_RS_SS_027", ["Sun&Sky System: Date, Time and Location", "Sun Glow - 2"], "TestSunSky.blend", 'sun_glow', '1024', 2],
	["BL_RS_SS_028", ["Sun&Sky System: Date, Time and Location", "Sun Glow - 5"], "TestSunSky.blend", 'sun_glow', '1024', 5],

	["BL_RS_SS_029", ["Sun&Sky System: Date, Time and Location", "Sun Disc - 0.5"], "TestSunSky.blend", 'sun_disc','1024', 0.5],
	["BL_RS_SS_030", ["Sun&Sky System: Date, Time and Location", "Sun Disc - 1"], "TestSunSky.blend", 'sun_disc', '1024', 1],
	["BL_RS_SS_031", ["Sun&Sky System: Date, Time and Location", "Sun Disc - 2"], "TestSunSky.blend", 'sun_disc', '1024', 2],

	["BL_RS_SS_032", ["Sun&Sky System: Date, Time and Location", "Saturation - 0"], "TestSunSky.blend", 'saturation', '1024', 0],
	["BL_RS_SS_033", ["Sun&Sky System: Date, Time and Location", "Saturation - 0.5"], "TestSunSky.blend", 'saturation', '1024', 0.5],
	["BL_RS_SS_034", ["Sun&Sky System: Date, Time and Location", "Saturation - 1"], "TestSunSky.blend", 'saturation', '1024', 1],

	["BL_RS_SS_035", ["Sun&Sky System: Date, Time and Location", "Horizon Heigh - -0.5"], "TestSunSky.blend", 'horizon_heigh', '1024', -0.5],
	["BL_RS_SS_036", ["Sun&Sky System: Date, Time and Location", "Horizon Heigh - 0"], "TestSunSky.blend", 'horizon_heigh', '1024', 0],
	["BL_RS_SS_037", ["Sun&Sky System: Date, Time and Location", "Horizon Heigh - 0.5"], "TestSunSky.blend", 'horizon_heigh', '1024', 0.5],

	["BL_RS_SS_038", ["Sun&Sky System: Date, Time and Location", "Horizon Blue - 0.10"], "TestSunSky.blend", 'horizon_blue', '1024', 0.10],
	["BL_RS_SS_039", ["Sun&Sky System: Date, Time and Location", "Horizon Blue - 0.50"], "TestSunSky.blend", 'horizon_blue', '1024', 0.50],
	["BL_RS_SS_040", ["Sun&Sky System: Date, Time and Location", "Horizon Blue - 1.0"], "TestSunSky.blend", 'horizon_blue', '1024', 1.0],

	["BL_RS_SS_041", ["Sun&Sky System: Date, Time and Location", "Filter Color - 0.50"], "TestSunSky.blend", 'filter_color', '1024', (1,0,1)],
	["BL_RS_SS_042", ["Sun&Sky System: Date, Time and Location", "Ground Color - 1.0"], "TestSunSky.blend", 'ground_color', '1024', (0,1,0)],
	

	# ["BL_RS_SS_043", [""], "TestSunSky.blend", 'date_time_location', '1024', (0,0,0), "Moscow"],
	# ["BL_RS_SS_044", [""], "TestSunSky.blend", 'date_time_location', '1024', (6,0,0), "Moscow"],
	# ["BL_RS_SS_045", [""], "TestSunSky.blend", 'date_time_location', '1024', (12,0,0), "Moscow"],
	# ["BL_RS_SS_046", [""], "TestSunSky.blend", 'date_time_location', '1024', (18,0,0), "Moscow"],
	# ["BL_RS_SS_047", [""], "TestSunSky.blend", 'date_time_location', '1024', (24,0,0), "Moscow"],
	# ["BL_RS_SS_048", [""], "TestSunSky.blend", 'date_time_location', '256', (12,0,0), "Moscow"],
	# ["BL_RS_SS_049", [""], "TestSunSky.blend", 'date_time_location', '1024', (12,0,0), "Moscow"],
	# ["BL_RS_SS_050", [""], "TestSunSky.blend", 'date_time_location', '4096', (12,0,0), "Moscow"],
	
	# ["BL_RS_SS_050", [""], "TestSunSky.blend", 'date_time_location', '1024', (12,0,0), "Moscow"],
	
	# ["BL_RS_SS_051", [""], "TestSunSky.blend", '1', '256'],
	# ["BL_RS_SS_052", [""], "TestSunSky.blend", '1', '1024'],
	# ["BL_RS_SS_053", [""], "TestSunSky.blend", '1', '4096'],
	# ["BL_RS_SS_054", [""], "TestSunSky.blend", '2', '1024', (0,0,0), "Miami_Beach"],
	# ["BL_RS_SS_055", [""], "TestSunSky.blend", '2', '1024', (12,0,0), "Miami_Beach"],
	# ["BL_RS_SS_056", [""], "TestSunSky.blend", '2', '1024', (24,0,0), "Miami_Beach"],
	# ["BL_RS_SS_057", [""], "TestSunSky.blend", '3', '1024', (0,0,0), "Canberra"],
	# ["BL_RS_SS_058", [""], "TestSunSky.blend", '3', '1024', (12,0,0), "Canberra"],
	# ["BL_RS_SS_059", [""], "TestSunSky.blend", '3', '1024', (24,0,0), "Canberra"],
	]

	launch_tests()

