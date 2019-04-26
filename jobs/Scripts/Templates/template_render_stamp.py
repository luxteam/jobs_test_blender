
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	set_value(scene.rpr.limits, 'max_samples', {pass_limit})
	set_value(scene.render.image_settings, 'file_format', 'JPEG')

	if {resolution_x} and {resolution_y}:
		set_value(scene.render, 'resolution_x', {resolution_x})
		set_value(scene.render, 'resolution_y', {resolution_y})

	set_value(scene.rpr, 'use_render_stamp', True)
	set_value(scene.rpr, 'render_stamp', test_list[3])

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":
	
	list_tests = [
	["BL_RS_RS_001", ["Base stamp"], "ComplexTestUber.blend", "Radeon ProRender for Blender %b | %h | Time: %pt | Passes: %pp | Objects: %so | Lights: %sl"],
	["BL_RS_RS_002", ["CPU&GPU stamp"], "ComplexTestUber.blend", "Radeon ProRender for Blender %b | CPU %c | GPU %g | Render mode %r | Render device %h"],
	["BL_RS_RS_003", ["Computer name stamp"], "ComplexTestUber.blend", "Radeon ProRender for Blender %b | Computer name %i | Current date %d"]
	]
	
	launch_tests()
