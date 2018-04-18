
def main(type_camera, rpr_camera_type, stereo_camera, test_case):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.objects.active = bpy.data.objects['Camera']
	bpy.context.object.select = False
	bpy.context.scene.objects['Camera'].select = True

	bpy.context.object.data.type = type_camera
	if (rpr_camera_type != 'no_rpr_camera'):
		bpy.context.scene.rpr.render.camera.override_camera_settings = True
		bpy.context.scene.rpr.render.camera.panorama_type = rpr_camera_type
		if (stereo_camera == True):
			bpy.context.scene.rpr.render.camera.stereo = True
	else:
		bpy.context.scene.rpr.render.camera.override_camera_settings = False

	render(test_case)

if __name__ == "__main__":

	main('PERSP', 'no_rpr_camera', False, "BL_RS_CAM_001")
	main('PANO', 'no_rpr_camera', False, "BL_RS_CAM_002")
	main('ORTHO', 'no_rpr_camera', False, "BL_RS_CAM_003")

	main('PERSP', 'CUBEMAP', False, "BL_RS_CAM_004")
	main('PERSP', 'SPHERICAL_PANORAMA', False, "BL_RS_CAM_005")
	main('PERSP', 'CUBEMAP', True, "BL_RS_CAM_006")
	main('PERSP', 'SPHERICAL_PANORAMA', True, "BL_RS_CAM_007")




