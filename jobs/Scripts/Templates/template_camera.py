
def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.objects.active = bpy.data.objects['Camera']
	bpy.context.object.select = False
	bpy.context.scene.objects['Camera'].select = True
	bpy.context.object.data.type = test_list[2]

	if (test_list[3] != 'no_rpr_camera'):
		bpy.context.scene.rpr.render.camera.override_camera_settings = True
		bpy.context.scene.rpr.render.camera.panorama_type = test_list[3]
		if (test_list[4]):
			bpy.context.scene.rpr.render.camera.stereo = True
	else:
		bpy.context.scene.rpr.render.camera.override_camera_settings = False

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_CAM_001", ["Camera Type: Persp"], 'PERSP', 'no_rpr_camera'], 
	["BL_RS_CAM_002", ["Camera Type: Pano"], 'PANO', 'no_rpr_camera'],
	["BL_RS_CAM_003", ["Camera Type: Ortho"], 'ORTHO', 'no_rpr_camera'],
	["BL_RS_CAM_004", ["RPR Camera Type: Cubemap"], 'PERSP', 'CUBEMAP', False],
	["BL_RS_CAM_005", ["RPR Camera Type: Spherical panorama"], 'PERSP', 'SPHERICAL_PANORAMA', False],
	["BL_RS_CAM_006", ["RPR Camera Type: Stereo cubemap"], 'PERSP', 'CUBEMAP', True],
	["BL_RS_CAM_007", ["RPR Camera Type: Stereo spherical panorama"], 'PERSP', 'SPHERICAL_PANORAMA', True]
	]
	
	launch_tests()





