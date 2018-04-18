def main(i, test_case):

	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[i] = True
	render(test_case)
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[i] = False

if __name__ == "__main__":

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[1] = False

	for i in range(23):
		if i<10:
			main(i, "BL_RS_AOV_00" + str(i+1))
		else:
			main(i, "BL_RS_AOV_0" + str(i+1))

