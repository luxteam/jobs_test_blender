def main(i):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[i] = True
	render(i)
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[i] = False

if __name__ == "__main__":

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[1] = False

	for i in range(23):
		main(i)


