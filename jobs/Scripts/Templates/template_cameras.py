
def main(type_camera, rpr_camera_type, stereo_camera):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

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

	render(type_camera, rpr_camera_type, stereo_camera)


if __name__ == "__main__":

	camera_type = ['PERSP', 'PANO','ORTHO']
	rpr_camera_type = ['CUBEMAP', 'SPHERICAL_PANORAMA']

	for each in camera_type:
		main(each, 'no_rpr_camera', False)
		
	for each in rpr_camera_type:
		main('PERSP', each, False)
		main('PERSP', each, True)


