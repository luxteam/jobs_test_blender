
def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.data.scenes[Scenename].rpr.render.aa.filter = test_list[2]
	bpy.data.scenes[Scenename].rpr.render.aa.radius = test_list[3]

	render(test_list[0], test_list[1])

if __name__ == "__main__":

	list_tests = [
	["BL_RS_AA_001", ["AA filter: Mitchell", "Radius: 0"], 'MITCHELL', 0], 
	["BL_RS_AA_002", ["AA filter: Mitchell", "Radius: 1"], 'MITCHELL', 1],
	["BL_RS_AA_003", ["AA filter: Mitchell", "Radius: 5"], 'MITCHELL', 5], 
	["BL_RS_AA_004", ["AA filter: Mitchell", "Radius: 10"], 'MITCHELL', 10],
	["BL_RS_AA_005", ["AA filter: Lanczos", "Radius: 0"], 'LANCZOS', 0], 
	["BL_RS_AA_006", ["AA filter: Lanczos", "Radius: 1"], 'LANCZOS', 1],
	["BL_RS_AA_007", ["AA filter: Lanczos", "Radius: 5"], 'LANCZOS', 5], 
	["BL_RS_AA_008", ["AA filter: Lanczos", "Radius: 10"], 'LANCZOS', 10],
	["BL_RS_AA_009", ["AA filter: Triangle", "Radius: 0"], 'TRIANGLE', 0], 
	["BL_RS_AA_010", ["AA filter: Triangle", "Radius: 1"], 'TRIANGLE', 1],
	["BL_RS_AA_011", ["AA filter: Triangle", "Radius: 5"], 'TRIANGLE', 5], 
	["BL_RS_AA_012", ["AA filter: Triangle", "Radius: 10"], 'TRIANGLE', 10],
	["BL_RS_AA_013", ["AA filter: Box", "Radius: 0"], 'BOX', 0], 
	["BL_RS_AA_014", ["AA filter: Box", "Radius: 1"], 'BOX', 1], 
	["BL_RS_AA_015", ["AA filter: Box", "Radius: 5"], 'BOX', 5], 
	["BL_RS_AA_016", ["AA filter: Box", "Radius: 10"], 'BOX', 10],
	["BL_RS_AA_017", ["AA filter: Gaussian", "Radius: 0"], 'GAUSSIAN', 0], 
	["BL_RS_AA_018", ["AA filter: Gaussian", "Radius: 1"], 'GAUSSIAN', 1],
	["BL_RS_AA_019", ["AA filter: Gaussian", "Radius: 5"], 'GAUSSIAN', 5], 
	["BL_RS_AA_020", ["AA filter: Gaussian", "Radius: 10"], 'GAUSSIAN', 10],
	["BL_RS_AA_021", ["AA filter: Blackmanharris", "Radius: 0"], 'BLACKMANHARRIS', 0], 
	["BL_RS_AA_022", ["AA filter: Blackmanharris", "Radius: 1"], 'BLACKMANHARRIS', 1],
	["BL_RS_AA_023", ["AA filter: Blackmanharris", "Radius: 5"], 'BLACKMANHARRIS', 5], 
	["BL_RS_AA_024", ["AA filter: Blackmanharris", "Radius: 10"], 'BLACKMANHARRIS', 10]
	]

	launch_tests()



