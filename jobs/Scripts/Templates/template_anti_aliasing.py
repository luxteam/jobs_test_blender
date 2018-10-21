
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	Scenename = bpy.context.scene.name

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.data.scenes[Scenename].rpr.render.aa.filter = test_list[3]
	bpy.data.scenes[Scenename].rpr.render.aa.radius = test_list[4]

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_AA_001", ["AA filter: Mitchell", "Radius: 0"], "ComplexTestUber.blend", 'MITCHELL', 0], 
	["BL_RS_AA_002", ["AA filter: Mitchell", "Radius: 1"], "ComplexTestUber.blend", 'MITCHELL', 1],
	["BL_RS_AA_003", ["AA filter: Mitchell", "Radius: 5"], "ComplexTestUber.blend", 'MITCHELL', 5], 
	["BL_RS_AA_004", ["AA filter: Mitchell", "Radius: 10"], "ComplexTestUber.blend", 'MITCHELL', 10],
	["BL_RS_AA_005", ["AA filter: Lanczos", "Radius: 0"], "ComplexTestUber.blend", 'LANCZOS', 0], 
	["BL_RS_AA_006", ["AA filter: Lanczos", "Radius: 1"], "ComplexTestUber.blend", 'LANCZOS', 1],
	["BL_RS_AA_007", ["AA filter: Lanczos", "Radius: 5"], "ComplexTestUber.blend", 'LANCZOS', 5], 
	["BL_RS_AA_008", ["AA filter: Lanczos", "Radius: 10"], "ComplexTestUber.blend", 'LANCZOS', 10],
	["BL_RS_AA_009", ["AA filter: Triangle", "Radius: 0"], "ComplexTestUber.blend", 'TRIANGLE', 0], 
	["BL_RS_AA_010", ["AA filter: Triangle", "Radius: 1"], "ComplexTestUber.blend", 'TRIANGLE', 1],
	["BL_RS_AA_011", ["AA filter: Triangle", "Radius: 5"], "ComplexTestUber.blend", 'TRIANGLE', 5], 
	["BL_RS_AA_012", ["AA filter: Triangle", "Radius: 10"], "ComplexTestUber.blend", 'TRIANGLE', 10],
	["BL_RS_AA_013", ["AA filter: Box", "Radius: 0"], "ComplexTestUber.blend", 'BOX', 0], 
	["BL_RS_AA_014", ["AA filter: Box", "Radius: 1"], "ComplexTestUber.blend", 'BOX', 1], 
	["BL_RS_AA_015", ["AA filter: Box", "Radius: 5"], "ComplexTestUber.blend", 'BOX', 5], 
	["BL_RS_AA_016", ["AA filter: Box", "Radius: 10"], "ComplexTestUber.blend", 'BOX', 10],
	["BL_RS_AA_017", ["AA filter: Gaussian", "Radius: 0"], "ComplexTestUber.blend", 'GAUSSIAN', 0], 
	["BL_RS_AA_018", ["AA filter: Gaussian", "Radius: 1"], "ComplexTestUber.blend", 'GAUSSIAN', 1],
	["BL_RS_AA_019", ["AA filter: Gaussian", "Radius: 5"], "ComplexTestUber.blend", 'GAUSSIAN', 5], 
	["BL_RS_AA_020", ["AA filter: Gaussian", "Radius: 10"], "ComplexTestUber.blend", 'GAUSSIAN', 10],
	["BL_RS_AA_021", ["AA filter: Blackmanharris", "Radius: 0"], "ComplexTestUber.blend", 'BLACKMANHARRIS', 0], 
	["BL_RS_AA_022", ["AA filter: Blackmanharris", "Radius: 1"], "ComplexTestUber.blend", 'BLACKMANHARRIS', 1],
	["BL_RS_AA_023", ["AA filter: Blackmanharris", "Radius: 5"], "ComplexTestUber.blend", 'BLACKMANHARRIS', 5], 
	["BL_RS_AA_024", ["AA filter: Blackmanharris", "Radius: 10"], "ComplexTestUber.blend", 'BLACKMANHARRIS', 10]
	]

	launch_tests()



