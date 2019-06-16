
def prerender(test_list):

    current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
    if current_scene != test_list[2]:
        bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

    scene = bpy.context.scene
    enable_rpr_render(scene)

	bpy.context.scene.rpr.render.aa.filter = test_list[3]
	bpy.context.scene.rpr.render.aa.radius = test_list[4]

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_AA_001", ["AA filter: Mitchell", "Radius: 0"], "easy_scene.blend", 'MITCHELL', 0], 
	["BL_RS_AA_002", ["AA filter: Mitchell", "Radius: 1"], "easy_scene.blend", 'MITCHELL', 1],
	["BL_RS_AA_003", ["AA filter: Mitchell", "Radius: 10"], "easy_scene.blend", 'MITCHELL', 10], 
	["BL_RS_AA_004", ["AA filter: Lanczos", "Radius: 0"], "easy_scene.blend", 'LANCZOS', 0], 
	["BL_RS_AA_005", ["AA filter: Lanczos", "Radius: 1"], "easy_scene.blend", 'LANCZOS', 1],
	["BL_RS_AA_006", ["AA filter: Lanczos", "Radius: 10"], "easy_scene.blend", 'LANCZOS', 10],
	["BL_RS_AA_007", ["AA filter: Triangle", "Radius: 0"], "easy_scene.blend", 'TRIANGLE', 0], 
	["BL_RS_AA_008", ["AA filter: Triangle", "Radius: 1"], "easy_scene.blend", 'TRIANGLE', 1],
	["BL_RS_AA_009", ["AA filter: Triangle", "Radius: 10"], "easy_scene.blend", 'TRIANGLE', 10],
	["BL_RS_AA_010", ["AA filter: Box", "Radius: 0"], "easy_scene.blend", 'BOX', 0], 
	["BL_RS_AA_011", ["AA filter: Box", "Radius: 1"], "easy_scene.blend", 'BOX', 1], 
	["BL_RS_AA_012", ["AA filter: Box", "Radius: 10"], "easy_scene.blend", 'BOX', 10],
	["BL_RS_AA_013", ["AA filter: Gaussian", "Radius: 0"], "easy_scene.blend", 'GAUSSIAN', 0], 
	["BL_RS_AA_014", ["AA filter: Gaussian", "Radius: 1"], "easy_scene.blend", 'GAUSSIAN', 1],
	["BL_RS_AA_015", ["AA filter: Gaussian", "Radius: 10"], "easy_scene.blend", 'GAUSSIAN', 10],
	["BL_RS_AA_016", ["AA filter: Blackmanharris", "Radius: 0"], "easy_scene.blend", 'BLACKMANHARRIS', 0], 
	["BL_RS_AA_017", ["AA filter: Blackmanharris", "Radius: 1"], "easy_scene.blend", 'BLACKMANHARRIS', 1],
	["BL_RS_AA_018", ["AA filter: Blackmanharris", "Radius: 10"], "easy_scene.blend", 'BLACKMANHARRIS', 10],
	["BL_RS_AA_019", ["AA filter: Mitchell", "Radius: 0"], "normal_scene.blend", 'MITCHELL', 0], 
	["BL_RS_AA_020", ["AA filter: Mitchell", "Radius: 1"], "normal_scene.blend", 'MITCHELL', 1],
	["BL_RS_AA_021", ["AA filter: Mitchell", "Radius: 10"], "normal_scene.blend", 'MITCHELL', 10],
	["BL_RS_AA_022", ["AA filter: Lanczos", "Radius: 0"], "normal_scene.blend", 'LANCZOS', 0], 
	["BL_RS_AA_023", ["AA filter: Lanczos", "Radius: 1"], "normal_scene.blend", 'LANCZOS', 1],
	["BL_RS_AA_024", ["AA filter: Lanczos", "Radius: 10"], "normal_scene.blend", 'LANCZOS', 10],
	["BL_RS_AA_025", ["AA filter: Triangle", "Radius: 0"], "normal_scene.blend", 'TRIANGLE', 0], 
	["BL_RS_AA_026", ["AA filter: Triangle", "Radius: 1"], "normal_scene.blend", 'TRIANGLE', 1],
	["BL_RS_AA_027", ["AA filter: Triangle", "Radius: 10"], "normal_scene.blend", 'TRIANGLE', 10],
	["BL_RS_AA_028", ["AA filter: Box", "Radius: 0"], "normal_scene.blend", 'BOX', 0], 
	["BL_RS_AA_029", ["AA filter: Box", "Radius: 1"], "normal_scene.blend", 'BOX', 1], 
	["BL_RS_AA_030", ["AA filter: Box", "Radius: 10"], "normal_scene.blend", 'BOX', 10],
	["BL_RS_AA_031", ["AA filter: Gaussian", "Radius: 0"], "normal_scene.blend", 'GAUSSIAN', 0], 
	["BL_RS_AA_032", ["AA filter: Gaussian", "Radius: 1"], "normal_scene.blend", 'GAUSSIAN', 1],
	["BL_RS_AA_033", ["AA filter: Gaussian", "Radius: 10"], "normal_scene.blend", 'GAUSSIAN', 10],
	["BL_RS_AA_034", ["AA filter: Blackmanharris", "Radius: 0"], "normal_scene.blend", 'BLACKMANHARRIS', 0], 
	["BL_RS_AA_035", ["AA filter: Blackmanharris", "Radius: 1"], "normal_scene.blend", 'BLACKMANHARRIS', 1],
	["BL_RS_AA_036", ["AA filter: Blackmanharris", "Radius: 10"], "normal_scene.blend", 'BLACKMANHARRIS', 10]
	]

	launch_tests()



