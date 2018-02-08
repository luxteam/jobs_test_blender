
def main(type_sun_sky, quality, param1, param2):

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
		bpy.context.scene.world.rpr_data.environment.sun_sky.time_zone = 3
		bpy.context.scene.world.rpr_data.environment.sun_sky.latitude = 0.973583
		bpy.context.scene.world.rpr_data.environment.sun_sky.longitude = 0.656516
		bpy.context.scene.world.rpr_data.environment.sun_sky.time_hours = param1
		bpy.context.scene.world.rpr_data.environment.sun_sky.time_minutes = param2

	render(type_sun_sky, quality, param1, param2)


if __name__ == "__main__":

	type_sun_sky = ['analytical_sky', 'date_time_location']
	qualities = ['small', 'normal', 'high']
	times = [0, 6, 12, 24]
	azimuths = [0, 1.5708, 3.14159, 4.71239, 6.28319]
	altitudes = [0, 0.785398, 1.5708] 

	for quality in qualities:
		main(type_sun_sky[0], quality, 0, 0.523599)
		main(type_sun_sky[1], quality, 12, 0)

	for time in times:
		main(type_sun_sky[1], qualities[1], time, 0)

	analytical_combinations = [ (azimuth, altitude) for azimuth in azimuths for altitude in altitudes]
	for each in test_combinations:
		main(type_sun_sky[0], quality[1], each[0], each[1])



