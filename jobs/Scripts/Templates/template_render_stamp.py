
def main(stamp, stamp_value):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	#stamp
	bpy.data.scenes[Scenename].rpr.use_render_stamp = True
	bpy.data.scenes[Scenename].rpr.render_stamp = stamp_value

	render(stamp)

if __name__ == "__main__":
	
	main("default_stamp", "Radeon ProRender for Blender %b | %h | Time: %pt | Passes: %pp | Objects: %so | Lights: %sl")
	main("gpu_stamp", "Radeon ProRender for Blender %b | CPU %c | GPU %g | Render mode %r | Render device %h")
	main("additional_info", "Radeon ProRender for Blender %b | Computer name %i | Current date %d")


