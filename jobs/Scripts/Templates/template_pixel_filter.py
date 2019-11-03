
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	bpy.context.scene.rpr.pixel_filter = test_list[3]
	bpy.context.scene.rpr.pixel_filter_width = test_list[4]
	
	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
		["BL_RS_PF_001", ["Pixel filter: Mitchell", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", 'MITCHELL', 0], 
		["BL_RS_PF_002", ["Pixel filter: Mitchell", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", 'MITCHELL', 1],
		["BL_RS_PF_003", ["Pixel filter: Mitchell", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", 'MITCHELL', 1.5], 
		["BL_RS_PF_004", ["Pixel filter: Mitchell", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", 'MITCHELL', 5], 
		["BL_RS_PF_005", ["Pixel filter: Mitchell", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", 'MITCHELL', 10], 

		["BL_RS_PF_006", ["Pixel filter: Triangle", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", 'TRIANGLE', 0], 
		["BL_RS_PF_007", ["Pixel filter: Triangle", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", 'TRIANGLE', 1],
		["BL_RS_PF_008", ["Pixel filter: Triangle", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", 'TRIANGLE', 1.5], 
		["BL_RS_PF_009", ["Pixel filter: Triangle", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", 'TRIANGLE', 5], 
		["BL_RS_PF_010", ["Pixel filter: Triangle", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", 'TRIANGLE', 10], 

		["BL_RS_PF_011", ["Pixel filter: Lanczos", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", 'LANCZOS', 0], 
		["BL_RS_PF_012", ["Pixel filter: Lanczos", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", 'LANCZOS', 1],
		["BL_RS_PF_013", ["Pixel filter: Lanczos", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", 'LANCZOS', 1.5], 
		["BL_RS_PF_014", ["Pixel filter: Lanczos", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", 'LANCZOS', 5], 
		["BL_RS_PF_015", ["Pixel filter: Lanczos", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", 'LANCZOS', 10], 

		["BL_RS_PF_016", ["Pixel filter: Gaussian", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", 'GAUSSIAN', 0], 
		["BL_RS_PF_017", ["Pixel filter: Gaussian", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", 'GAUSSIAN', 1],
		["BL_RS_PF_018", ["Pixel filter: Gaussian", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", 'GAUSSIAN', 1.5], 
		["BL_RS_PF_019", ["Pixel filter: Gaussian", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", 'GAUSSIAN', 5], 
		["BL_RS_PF_020", ["Pixel filter: Gaussian", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", 'GAUSSIAN', 10],

		["BL_RS_PF_021", ["Pixel filter: Box", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", 'BOX', 0], 
		["BL_RS_PF_022", ["Pixel filter: Box", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", 'BOX', 1],
		["BL_RS_PF_023", ["Pixel filter: Box", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", 'BOX', 1.5], 
		["BL_RS_PF_024", ["Pixel filter: Box", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", 'BOX', 5], 
		["BL_RS_PF_025", ["Pixel filter: Box", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", 'BOX', 10], 

		["BL_RS_PF_026", ["Pixel filter: Blackmanharris", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 0], 
		["BL_RS_PF_027", ["Pixel filter: Blackmanharris", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 1],
		["BL_RS_PF_028", ["Pixel filter: Blackmanharris", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 1.5], 
		["BL_RS_PF_029", ["Pixel filter: Blackmanharris", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 5], 
		["BL_RS_PF_030", ["Pixel filter: Blackmanharris", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 10],  

		["BL_RS_PF_031", ["Pixel filter: Mitchell", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", 'MITCHELL', 0], 
		["BL_RS_PF_032", ["Pixel filter: Mitchell", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", 'MITCHELL', 1],
		["BL_RS_PF_033", ["Pixel filter: Mitchell", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", 'MITCHELL', 1.5], 
		["BL_RS_PF_034", ["Pixel filter: Mitchell", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", 'MITCHELL', 5], 
		["BL_RS_PF_035", ["Pixel filter: Mitchell", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", 'MITCHELL', 10], 

		["BL_RS_PF_036", ["Pixel filter: Triangle", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", 'TRIANGLE', 0], 
		["BL_RS_PF_037", ["Pixel filter: Triangle", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", 'TRIANGLE', 1],
		["BL_RS_PF_038", ["Pixel filter: Triangle", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", 'TRIANGLE', 1.5], 
		["BL_RS_PF_039", ["Pixel filter: Triangle", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", 'TRIANGLE', 5], 
		["BL_RS_PF_040", ["Pixel filter: Triangle", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", 'TRIANGLE', 10], 

		["BL_RS_PF_041", ["Pixel filter: Lanczos", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", 'LANCZOS', 0], 
		["BL_RS_PF_042", ["Pixel filter: Lanczos", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", 'LANCZOS', 1],
		["BL_RS_PF_043", ["Pixel filter: Lanczos", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", 'LANCZOS', 1.5], 
		["BL_RS_PF_044", ["Pixel filter: Lanczos", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", 'LANCZOS', 5], 
		["BL_RS_PF_045", ["Pixel filter: Lanczos", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", 'LANCZOS', 10], 

		["BL_RS_PF_046", ["Pixel filter: Gaussian", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", 'GAUSSIAN', 0], 
		["BL_RS_PF_047", ["Pixel filter: Gaussian", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", 'GAUSSIAN', 1],
		["BL_RS_PF_048", ["Pixel filter: Gaussian", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", 'GAUSSIAN', 1.5], 
		["BL_RS_PF_049", ["Pixel filter: Gaussian", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", 'GAUSSIAN', 5], 
		["BL_RS_PF_050", ["Pixel filter: Gaussian", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", 'GAUSSIAN', 10],

		["BL_RS_PF_051", ["Pixel filter: Box", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", 'BOX', 0], 
		["BL_RS_PF_052", ["Pixel filter: Box", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", 'BOX', 1],
		["BL_RS_PF_053", ["Pixel filter: Box", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", 'BOX', 1.5], 
		["BL_RS_PF_054", ["Pixel filter: Box", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", 'BOX', 5], 
		["BL_RS_PF_055", ["Pixel filter: Box", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", 'BOX', 10], 

		["BL_RS_PF_056", ["Pixel filter: Blackmanharris", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 0], 
		["BL_RS_PF_057", ["Pixel filter: Blackmanharris", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 1],
		["BL_RS_PF_058", ["Pixel filter: Blackmanharris", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 1.5], 
		["BL_RS_PF_059", ["Pixel filter: Blackmanharris", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 5], 
		["BL_RS_PF_060", ["Pixel filter: Blackmanharris", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", 'BLACKMANHARRIS', 10]
	
	]

	launch_tests()



