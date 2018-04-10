
def main(type_sun_sky, quality, param1, param2, location, test_case):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'


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

	render(test_case)


if __name__ == "__main__":

	main('analytical_sky', 'normal', 0, 0, "none", "BL_RS_SS_001") # 0 0
	main('analytical_sky', 'normal', 0, 0.785398, "none", "BL_RS_SS_002") # 0 45
	main('analytical_sky', 'normal', 0, 1.5708, "none", "BL_RS_SS_003") # 0 90
	main('analytical_sky', 'normal', 1.5708, 0, "none", "BL_RS_SS_004") # 90 0
	main('analytical_sky', 'normal', 1.5708, 0.785398, "none", "BL_RS_SS_005") # 90 45
	main('analytical_sky', 'normal', 1.5708, 1.5708, "none", "BL_RS_SS_006") # 90 90
	main('analytical_sky', 'normal', 3.14159, 0, "none", "BL_RS_SS_007") # 180 0
	main('analytical_sky', 'normal', 3.14159, 0.785398, "none", "BL_RS_SS_008") # 180 45
	main('analytical_sky', 'normal', 3.14159, 1.5708, "none", "BL_RS_SS_009") # 180 90
	main('analytical_sky', 'normal', 4.71239, 0, "none", "BL_RS_SS_010") # 270 0
	main('analytical_sky', 'normal', 4.71239, 0.785398, "none", "BL_RS_SS_011") # 270 45
	main('analytical_sky', 'normal', 4.71239, 1.5708, "none", "BL_RS_SS_012") # 270 90
	main('analytical_sky', 'normal', 6.28319, 0, "none", "BL_RS_SS_013") # 360 0
	main('analytical_sky', 'normal', 6.28319, 0.785398, "none", "BL_RS_SS_014") # 360 45
	main('analytical_sky', 'normal', 6.28319, 1.5708, "none", "BL_RS_SS_015") # 360 90

	main('date_time_location', 'normal', 0, 1, "Moscow", "BL_RS_SS_016")
	main('date_time_location', 'normal', 6, 1, "Moscow", "BL_RS_SS_017")
	main('date_time_location', 'normal', 12, 1, "Moscow", "BL_RS_SS_018")
	main('date_time_location', 'normal', 18, 1, "Moscow", "BL_RS_SS_019")
	main('date_time_location', 'normal', 24, 1, "Moscow", "BL_RS_SS_020")

	main('date_time_location', 'small', 12, 0, "Moscow", "BL_RS_SS_021")
	main('date_time_location', 'normal', 12, 0, "Moscow", "BL_RS_SS_022")
	main('date_time_location', 'high', 12, 0, "Moscow", "BL_RS_SS_023")

	main('analytical_sky', 'small', 3.14159, 0.785398, "none", "BL_RS_SS_024") 
	main('analytical_sky', 'normal', 3.14159, 0.785398, "none", "BL_RS_SS_025") 
	main('analytical_sky', 'high', 3.14159, 0.785398, "none", "BL_RS_SS_026") 

	main('date_time_location', 'normal', 0, 1, "Miami_Beach", "BL_RS_SS_027")
	main('date_time_location', 'normal', 12, 1, "Miami_Beach", "BL_RS_SS_028")
	main('date_time_location', 'normal', 24, 1, "Miami_Beach", "BL_RS_SS_029")

	main('date_time_location', 'normal', 0, 1, "Canberra", "BL_RS_SS_030")
	main('date_time_location', 'normal', 12, 1, "Canberra", "BL_RS_SS_031")
	main('date_time_location', 'normal', 24, 1, "Canberra", "BL_RS_SS_032")
