
def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.data.scenes[Scenename].render.resolution_x = test_list[2]
	bpy.data.scenes[Scenename].render.resolution_y = test_list[3]
	bpy.data.scenes[Scenename].render.pixel_aspect_x = test_list[4]
	bpy.data.scenes[Scenename].render.pixel_aspect_y = test_list[5]
	bpy.data.scenes[Scenename].render.resolution_percentage = 100

	render(test_list[0], test_list[1])

	return 1

if __name__ == "__main__":
	
	list_tests = [
	["BL_RS_IS_001", ["Preset: DVCPRO_HD_1080p"], 1280, 1080, 3, 2], 
	["BL_RS_IS_002", ["Preset: DVCPRO_HD_720p"], 960, 720, 4, 3],
	["BL_RS_IS_003", ["Preset: HDTV_1080p"], 1920, 1080, 1, 1], 
	["BL_RS_IS_004", ["Preset: HDTV_720p"], 1280, 720, 1, 1], 
	["BL_RS_IS_005", ["Preset: HDV_1080p"], 1440, 1080, 4, 3], 
	["BL_RS_IS_006", ["Preset: HDV_NTSC_1080p"], 1440, 1080, 4, 3],
	["BL_RS_IS_007", ["Preset: HDV_PAL_1080p"], 1440, 1080, 4, 3], 
	["BL_RS_IS_008", ["Preset: TV_NTSC_16_9"], 720, 480, 40.1, 33],
	["BL_RS_IS_009", ["Preset: TV_NTSC_4_3"], 720, 486, 10, 11], 
	["BL_RS_IS_010", ["Preset: TV_PAL_16_9"], 720, 576, 16, 11],
	["BL_RS_IS_011", ["Preset: TV_PAL_4_3"], 720, 576, 12, 11], 
	["BL_RS_IS_012", ["Resolution: 2000x2000"], 2000, 2000, 3, 2], 
	["BL_RS_IS_013", ["Resolution: 3000x3000"], 3000, 3000, 3, 2], 
	["BL_RS_IS_014", ["Resolution: 4000x4000"], 4000, 4000, 3, 2], 
	["BL_RS_IS_015", ["Resolution: 5000x5000"], 5000, 5000, 3, 2], 
	["BL_RS_IS_016", ["Resolution: 6000x6000"], 6000, 6000, 3, 2],
	["BL_RS_IS_017", ["Resolution: 7000x7000"], 7000, 7000, 3, 2], 
	["BL_RS_IS_018", ["Resolution: 8000x8000"], 8000, 8000, 3, 2],
	["BL_RS_IS_019", ["Resolution: 2K"], 2048, 1152, 3, 2], 
	["BL_RS_IS_020", ["Resolution: 4K"], 4096, 3204, 3, 2],
	["BL_RS_IS_021", ["Resolution: 1500x1125"], 1500, 1125, 3, 2]
	]
	
	launch_tests()
