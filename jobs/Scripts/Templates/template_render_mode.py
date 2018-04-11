
def main(render_mode, test_case):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.scene.rpr.render.render_mode = render_mode

	render(test_case)

if __name__ == "__main__":

	render_modes = ['WIREFRAME', 'TEXCOORD', 'POSITION', 'NORMAL', 'MATERIAL_INDEX', 'GLOBAL_ILLUMINATION', 'DIRECT_ILLUMINATION_NO_SHADOW', \
	'DIRECT_ILLUMINATION', 'DIFFUSE', 'AMBIENT_OCCLUSION']

	for mode in range(len(render_modes)):
		if mode < 10:
			main(render_modes[mode], "BL_RS_RM_00" + str(mode+1))
		else:
			main(render_modes[mode], "BL_RS_RM_0" + str(mode+1))

