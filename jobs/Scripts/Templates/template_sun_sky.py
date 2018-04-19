
def main(type_sun_sky, quality, param1, param2, location, test_case, script_info):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}


	bpy.context.scene.world.rpr_data.environment.type = 'SUN_SKY'
	bpy.context.scene.world.rpr_data.environment.sun_sky.type = type_sun_sky
	bpy.context.scene.world.rpr_data.environment.sun_sky.ground_color = (0.4, 0.00703741, 0.00508468)
	bpy.context.scene.world.rpr_data.environment.sun_sky.texture_resolution = quality

	if type_sun_sky == 'analytical_sky':
		bpy.context.scene.world.rpr_data.environment.sun_sky.azimuth = param1
		bpy.context.scene.world.rpr_data.environment.sun_sky.altitude = param2
	else:
		bpy.ops.rpr.op_get_time_now()
		
		if (location == "Moscow"):
			bpy.context.scene.world.rpr_data.environment.sun_sky.time_zone = 3
			bpy.context.scene.world.rpr_data.environment.sun_sky.latitude = 0.973583
			bpy.context.scene.world.rpr_data.environment.sun_sky.longitude = 0.656516
		elif (location == "Canberra"):
			bpy.context.scene.world.rpr_data.environment.sun_sky.time_zone = 11
			bpy.context.scene.world.rpr_data.environment.sun_sky.latitude = -0.615752
			bpy.context.scene.world.rpr_data.environment.sun_sky.longitude = 2.60277
		elif (location == "Miami_Beach"):
			bpy.context.scene.world.rpr_data.environment.sun_sky.time_zone = -5
			bpy.context.scene.world.rpr_data.environment.sun_sky.latitude = 0.450131
			bpy.context.scene.world.rpr_data.environment.sun_sky.longitude = -1.39853

		bpy.context.scene.world.rpr_data.environment.sun_sky.time_hours = param1
		bpy.context.scene.world.rpr_data.environment.sun_sky.time_minutes = param2

	render(test_case, script_info)


if __name__ == "__main__":

	main('analytical_sky', 'normal', 0, 0, "none", "BL_RS_SS_001", ["Sun&Sky System: Analytical sky", "Azimuth: 0", "Altitude: 0", "Texture Resolution: normal"]) # 0 0
	main('analytical_sky', 'normal', 0, 0.785398, "none", "BL_RS_SS_002", ["Sun&Sky System: Analytical sky", "Azimuth: 0", "Altitude: 45", "Texture Resolution: normal"]) # 0 45
	main('analytical_sky', 'normal', 0, 1.5708, "none", "BL_RS_SS_003", ["Sun&Sky System: Analytical sky", "Azimuth: 0", "Altitude: 90", "Texture Resolution: normal"]) # 0 90
	main('analytical_sky', 'normal', 1.5708, 0, "none", "BL_RS_SS_004", ["Sun&Sky System: Analytical sky", "Azimuth: 90", "Altitude: 0", "Texture Resolution: normal"]) # 90 0
	main('analytical_sky', 'normal', 1.5708, 0.785398, "none", "BL_RS_SS_005", ["Sun&Sky System: Analytical sky", "Azimuth: 90", "Altitude: 45", "Texture Resolution: normal"]) # 90 45
	main('analytical_sky', 'normal', 1.5708, 1.5708, "none", "BL_RS_SS_006", ["Sun&Sky System: Analytical sky", "Azimuth: 90", "Altitude: 90", "Texture Resolution: normal"]) # 90 90
	main('analytical_sky', 'normal', 3.14159, 0, "none", "BL_RS_SS_007", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 0", "Texture Resolution: normal"]) # 180 0
	main('analytical_sky', 'normal', 3.14159, 0.785398, "none", "BL_RS_SS_008", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 45", "Texture Resolution: normal"]) # 180 45
	main('analytical_sky', 'normal', 3.14159, 1.5708, "none", "BL_RS_SS_009", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 90", "Texture Resolution: normal"]) # 180 90
	main('analytical_sky', 'normal', 4.71239, 0, "none", "BL_RS_SS_010", ["Sun&Sky System: Analytical sky", "Azimuth: 270", "Altitude: 0", "Texture Resolution: normal"]) # 270 0
	main('analytical_sky', 'normal', 4.71239, 0.785398, "none", "BL_RS_SS_011", ["Sun&Sky System: Analytical sky", "Azimuth: 270", "Altitude: 45", "Texture Resolution: normal"]) # 270 45
	main('analytical_sky', 'normal', 4.71239, 1.5708, "none", "BL_RS_SS_012", ["Sun&Sky System: Analytical sky", "Azimuth: 270", "Altitude: 90", "Texture Resolution: normal"]) # 270 90
	main('analytical_sky', 'normal', 6.28319, 0, "none", "BL_RS_SS_013", ["Sun&Sky System: Analytical sky", "Azimuth: 360", "Altitude: 0", "Texture Resolution: normal"]) # 360 0
	main('analytical_sky', 'normal', 6.28319, 0.785398, "none", "BL_RS_SS_014", ["Sun&Sky System: Analytical sky", "Azimuth: 360", "Altitude: 45", "Texture Resolution: normal"]) # 360 45
	main('analytical_sky', 'normal', 6.28319, 1.5708, "none", "BL_RS_SS_015", ["Sun&Sky System: Analytical sky", "Azimuth: 360", "Altitude: 90", "Texture Resolution: normal"]) # 360 90

	main('date_time_location', 'normal', 0, 1, "Moscow", "BL_RS_SS_016", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 0", "Texture Resolution: normal"])
	main('date_time_location', 'normal', 6, 1, "Moscow", "BL_RS_SS_017", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 6", "Texture Resolution: normal"])
	main('date_time_location', 'normal', 12, 1, "Moscow", "BL_RS_SS_018", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 12", "Texture Resolution: normal"])
	main('date_time_location', 'normal', 18, 1, "Moscow", "BL_RS_SS_019", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 18", "Texture Resolution: normal"])
	main('date_time_location', 'normal', 24, 1, "Moscow", "BL_RS_SS_020", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 24", "Texture Resolution: normal"])

	main('date_time_location', 'small', 12, 0, "Moscow", "BL_RS_SS_021", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 12", "Texture Resolution: small"])
	main('date_time_location', 'normal', 12, 0, "Moscow", "BL_RS_SS_022", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 12", "Texture Resolution: normal"])
	main('date_time_location', 'high', 12, 0, "Moscow", "BL_RS_SS_023", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 12", "Texture Resolution: high"])

	main('analytical_sky', 'small', 3.14159, 0.785398, "none", "BL_RS_SS_024", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 45", "Texture Resolution: small"]) 
	main('analytical_sky', 'normal', 3.14159, 0.785398, "none", "BL_RS_SS_025", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 45", "Texture Resolution: normal"]) 
	main('analytical_sky', 'high', 3.14159, 0.785398, "none", "BL_RS_SS_026", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 45", "Texture Resolution: high"]) 

	main('date_time_location', 'normal', 0, 1, "Miami_Beach", "BL_RS_SS_027", ["Sun&Sky System: Date, Time and Location", "Location: Miami Beach", "Hour: 0", "Texture Resolution: normal"])
	main('date_time_location', 'normal', 12, 1, "Miami_Beach", "BL_RS_SS_028", ["Sun&Sky System: Date, Time and Location", "Location: Miami Beach", "Hour: 12", "Texture Resolution: normal"])
	main('date_time_location', 'normal', 24, 1, "Miami_Beach", "BL_RS_SS_029", ["Sun&Sky System: Date, Time and Location", "Location: Miami Beach", "Hour: 24", "Texture Resolution: normal"])

	main('date_time_location', 'normal', 0, 1, "Canberra", "BL_RS_SS_030", ["Sun&Sky System: Date, Time and Location", "Location: Canberra", "Hour: 0", "Texture Resolution: normal"])
	main('date_time_location', 'normal', 12, 1, "Canberra", "BL_RS_SS_031", ["Sun&Sky System: Date, Time and Location", "Location: Canberra", "Hour: 12", "Texture Resolution: normal"])
	main('date_time_location', 'normal', 24, 1, "Canberra", "BL_RS_SS_032", ["Sun&Sky System: Date, Time and Location", "Location: Canberra", "Hour: 24", "Texture Resolution: normal"])
