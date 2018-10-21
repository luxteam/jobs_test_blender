
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	Scenename = bpy.context.scene.name

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.data.scenes[Scenename].rpr.use_render_stamp = True
	bpy.data.scenes[Scenename].rpr.render_stamp = test_list[3]

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":
	
	list_tests = [
	["BL_RS_RS_001", ["Base stamp"], "ComplexTestUber.blend", "Radeon ProRender for Blender %b | %h | Time: %pt | Passes: %pp | Objects: %so | Lights: %sl"],
	["BL_RS_RS_002", ["CPU&GPU stamp"], "ComplexTestUber.blend", "Radeon ProRender for Blender %b | CPU %c | GPU %g | Render mode %r | Render device %h"],
	["BL_RS_RS_003", ["Computer name stamp"], "ComplexTestUber.blend", "Radeon ProRender for Blender %b | Computer name %i | Current date %d"]
	]
	
	launch_tests()
