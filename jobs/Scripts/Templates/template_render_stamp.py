
def main(stamp_value, test_case):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	#stamp
	bpy.data.scenes[Scenename].rpr.use_render_stamp = True
	bpy.data.scenes[Scenename].rpr.render_stamp = stamp_value

	render(test_case)

if __name__ == "__main__":
	
	main("Radeon ProRender for Blender %b | %h | Time: %pt | Passes: %pp | Objects: %so | Lights: %sl", "BL_RS_RS_001")
	main("Radeon ProRender for Blender %b | CPU %c | GPU %g | Render mode %r | Render device %h", "BL_RS_RS_002")
	main("Radeon ProRender for Blender %b | Computer name %i | Current date %d", "BL_RS_RS_003")


