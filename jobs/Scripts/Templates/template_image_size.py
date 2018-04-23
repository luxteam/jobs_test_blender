
def main(size_r_x, size_r_y, size_a_x, size_a_y, test_case, script_info):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	# resolution
	bpy.data.scenes[Scenename].render.resolution_x = size_r_x
	bpy.data.scenes[Scenename].render.resolution_y = size_r_y
	bpy.data.scenes[Scenename].render.pixel_aspect_x = size_a_x
	bpy.data.scenes[Scenename].render.pixel_aspect_y = size_a_y
	bpy.data.scenes[Scenename].render.resolution_percentage = 100

	render(test_case, script_info)

if __name__ == "__main__":
	
	main(1280, 1080, 3, 2, "BL_RS_IS_001", ["Preset: DVCPRO_HD_1080p"])
	main(960, 720, 4, 3, "BL_RS_IS_002", ["Preset: DVCPRO_HD_720p"])
	main(1920, 1080, 1, 1, "BL_RS_IS_003", ["Preset: HDTV_1080p"])
	main(1280, 720, 1, 1, "BL_RS_IS_004", ["Preset: HDTV_720p"])
	main(1440, 1080, 4, 3, "BL_RS_IS_005", ["Preset: HDV_1080p"])
	main(1440, 1080, 4, 3, "BL_RS_IS_006", ["Preset: HDV_NTSC_1080p"])
	main(1440, 1080, 4, 3, "BL_RS_IS_007", ["Preset: HDV_PAL_1080p"])
	main(720, 480, 40.1, 33, "BL_RS_IS_008", ["Preset: TV_NTSC_16_9"])
	main(720, 486, 10, 11, "BL_RS_IS_009", ["Preset: TV_NTSC_4_3"])
	main(720, 576, 16, 11, "BL_RS_IS_010", ["Preset: TV_PAL_16_9"])
	main(720, 576, 12, 11, "BL_RS_IS_011", ["Preset: TV_PAL_4_3"])
	main(2000, 2000, 3, 2, "BL_RS_IS_012", ["Resolution: 2000x2000"])
	main(3000, 3000, 3, 2, "BL_RS_IS_013", ["Resolution: 3000x3000"])
	main(4000, 4000, 3, 2, "BL_RS_IS_014", ["Resolution: 4000x4000"])
	main(5000, 5000, 3, 2, "BL_RS_IS_015", ["Resolution: 5000x5000"])
	main(1, 1, 1, 1, "BL_RS_IS_016", ["Resolution: 6000x6000"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/failed.jpg", "{work_dir}/Color/BL_RS_IS_016.jpg")
	main(1, 1, 1, 1, "BL_RS_IS_017", ["Resolution: 7000x7000"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/failed.jpg", "{work_dir}/Color/BL_RS_IS_017.jpg")
	main(1, 1, 1, 1, "BL_RS_IS_018", ["Resolution: 8000x8000"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/failed.jpg", "{work_dir}/Color/BL_RS_IS_018.jpg")
	#main(6000, 6000, 3, 2, "BL_RS_IS_016", ["Resolution: 6000x6000"])
	#main(7000, 7000, 3, 2, "BL_RS_IS_017", ["Resolution: 7000x7000"])
	#main(8000, 8000, 3, 2, "BL_RS_IS_018", ["Resolution: 8000x8000"])
	main(2048, 1152, 3, 2, "BL_RS_IS_019", ["Resolution: 2K"])
	main(4096, 3204, 3, 2, "BL_RS_IS_020", ["Resolution: 4K"])
	main(1500, 1125, 3, 2, "BL_RS_IS_021", ["Resolution: 1500x1125"])