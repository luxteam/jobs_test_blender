
def main(size, size_r_x, size_r_y, size_a_x, size_a_y):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	# resolution
	bpy.data.scenes[Scenename].render.resolution_x = size_r_x
	bpy.data.scenes[Scenename].render.resolution_y = size_r_y
	bpy.data.scenes[Scenename].render.pixel_aspect_x = size_a_x
	bpy.data.scenes[Scenename].render.pixel_aspect_y = size_a_y
	bpy.data.scenes[Scenename].render.resolution_percentage = 100

	render(size)

if __name__ == "__main__":
	
	main("DVCPRO_HD_1080p", 1280, 1080, 3, 2)
	main("DVCPRO_HD_720p", 960, 720, 4, 3)
	main("HDTV_1080p", 1920, 1080, 1, 1)
	main("HDTV_720p", 1280, 720, 1, 1)
	main("HDV_1080p", 1440, 1080, 4, 3)
	main("HDV_NTSC_1080p", 1440, 1080, 4, 3)
	main("HDV_PAL_1080p", 1440, 1080, 4, 3)
	main("TV_NTSC_16_9", 720, 480, 40.1, 33)
	main("TV_NTSC_4_3", 720, 486, 10, 11)
	main("TV_PAL_16_9", 720, 576, 16, 11)
	main("TV_PAL_4_3", 720, 576, 12, 11)
	main("2K", 2048, 1152, 3, 2)
	main("4K", 4096, 3204, 3, 2)
	main("1500x1125", 1500, 1125, 3, 2)
	main("2000x2000", 2000, 2000, 3, 2)
	main("3000x3000", 3000, 3000, 3, 2)
	main("4000x4000", 4000, 4000, 3, 2)
	#main("5000x5000", 5000, 5000, 3, 2)
	#main("6000x6000", 6000, 6000, 3, 2)
	#main("7000x7000", 7000, 7000, 3, 2)
	#main("8000x8000", 8000, 8000, 3, 2)

