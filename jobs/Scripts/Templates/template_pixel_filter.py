
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	# make changes
	test_list[3]()
	# render
	render(test_list[0], test_list[1])
	
	return 1


def pf_001():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'MITCHELL')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 0)


def pf_002():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'MITCHELL')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1)


def pf_003():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'MITCHELL')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1.5)


def pf_004():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'MITCHELL')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 5)


def pf_005():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'MITCHELL')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 10)


def pf_006():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'TRIANGLE')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 0)


def pf_007():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'TRIANGLE')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1)


def pf_008():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'TRIANGLE')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1.5)


def pf_009():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'TRIANGLE')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 5)


def pf_010():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'TRIANGLE')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 10)


def pf_011():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'LANCZOS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 0)


def pf_012():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'LANCZOS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1)


def pf_013():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'LANCZOS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1.5)


def pf_014():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'LANCZOS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 5)


def pf_015():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'LANCZOS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 10)


def pf_016():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'GAUSSIAN')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 0)


def pf_017():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'GAUSSIAN')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1)


def pf_018():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'GAUSSIAN')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1.5)


def pf_019():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'GAUSSIAN')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 5)


def pf_020():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'GAUSSIAN')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 10)


def pf_021():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BOX')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 0)


def pf_022():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BOX')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1)


def pf_023():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BOX')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1.5)


def pf_024():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BOX')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 5)


def pf_025():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BOX')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 10)


def pf_026():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BLACKMANHARRIS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 0)


def pf_027():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BLACKMANHARRIS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1)


def pf_028():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BLACKMANHARRIS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 1.5)


def pf_029():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BLACKMANHARRIS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 5)


def pf_030():
	set_value(bpy.context.scene.rpr, 'pixel_filter', 'BLACKMANHARRIS')
	set_value(bpy.context.scene.rpr, 'pixel_filter_width', 10)


if __name__ == "__main__":

	list_tests = [
		["BL_RS_PF_001", ["Pixel filter: Mitchell", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", pf_001], 
		["BL_RS_PF_002", ["Pixel filter: Mitchell", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", pf_002],
		["BL_RS_PF_003", ["Pixel filter: Mitchell", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", pf_003], 
		["BL_RS_PF_004", ["Pixel filter: Mitchell", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", pf_004], 
		["BL_RS_PF_005", ["Pixel filter: Mitchell", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", pf_005], 

		["BL_RS_PF_006", ["Pixel filter: Triangle", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", pf_006], 
		["BL_RS_PF_007", ["Pixel filter: Triangle", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", pf_007],
		["BL_RS_PF_008", ["Pixel filter: Triangle", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", pf_008], 
		["BL_RS_PF_009", ["Pixel filter: Triangle", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", pf_008], 
		["BL_RS_PF_010", ["Pixel filter: Triangle", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", pf_010], 

		["BL_RS_PF_011", ["Pixel filter: Lanczos", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", pf_011], 
		["BL_RS_PF_012", ["Pixel filter: Lanczos", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", pf_012],
		["BL_RS_PF_013", ["Pixel filter: Lanczos", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", pf_013], 
		["BL_RS_PF_014", ["Pixel filter: Lanczos", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", pf_014], 
		["BL_RS_PF_015", ["Pixel filter: Lanczos", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", pf_015], 

		["BL_RS_PF_016", ["Pixel filter: Gaussian", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", pf_016], 
		["BL_RS_PF_017", ["Pixel filter: Gaussian", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", pf_017],
		["BL_RS_PF_018", ["Pixel filter: Gaussian", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", pf_018], 
		["BL_RS_PF_019", ["Pixel filter: Gaussian", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", pf_019], 
		["BL_RS_PF_020", ["Pixel filter: Gaussian", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", pf_020],

		["BL_RS_PF_021", ["Pixel filter: Box", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", pf_021], 
		["BL_RS_PF_022", ["Pixel filter: Box", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", pf_022],
		["BL_RS_PF_023", ["Pixel filter: Box", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", pf_023], 
		["BL_RS_PF_024", ["Pixel filter: Box", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", pf_024], 
		["BL_RS_PF_025", ["Pixel filter: Box", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", pf_025], 

		["BL_RS_PF_026", ["Pixel filter: Blackmanharris", "Radius: 0"], "Ease_Pixel_Filters_Scene.blend", pf_026], 
		["BL_RS_PF_027", ["Pixel filter: Blackmanharris", "Radius: 1"], "Ease_Pixel_Filters_Scene.blend", pf_027],
		["BL_RS_PF_028", ["Pixel filter: Blackmanharris", "Radius: 1.5"], "Ease_Pixel_Filters_Scene.blend", pf_028], 
		["BL_RS_PF_029", ["Pixel filter: Blackmanharris", "Radius: 5"], "Ease_Pixel_Filters_Scene.blend", pf_029], 
		["BL_RS_PF_030", ["Pixel filter: Blackmanharris", "Radius: 10"], "Ease_Pixel_Filters_Scene.blend", pf_030],  

		["BL_RS_PF_031", ["Pixel filter: Mitchell", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", pf_001], 
		["BL_RS_PF_032", ["Pixel filter: Mitchell", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", pf_002],
		["BL_RS_PF_033", ["Pixel filter: Mitchell", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", pf_003], 
		["BL_RS_PF_034", ["Pixel filter: Mitchell", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", pf_004], 
		["BL_RS_PF_035", ["Pixel filter: Mitchell", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", pf_005], 

		["BL_RS_PF_036", ["Pixel filter: Triangle", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", pf_006], 
		["BL_RS_PF_037", ["Pixel filter: Triangle", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", pf_007],
		["BL_RS_PF_038", ["Pixel filter: Triangle", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", pf_008], 
		["BL_RS_PF_039", ["Pixel filter: Triangle", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", pf_009], 
		["BL_RS_PF_040", ["Pixel filter: Triangle", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", pf_010], 

		["BL_RS_PF_041", ["Pixel filter: Lanczos", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", pf_011], 
		["BL_RS_PF_042", ["Pixel filter: Lanczos", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", pf_012],
		["BL_RS_PF_043", ["Pixel filter: Lanczos", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", pf_013], 
		["BL_RS_PF_044", ["Pixel filter: Lanczos", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", pf_014], 
		["BL_RS_PF_045", ["Pixel filter: Lanczos", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", pf_015], 

		["BL_RS_PF_046", ["Pixel filter: Gaussian", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", pf_016], 
		["BL_RS_PF_047", ["Pixel filter: Gaussian", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", pf_017],
		["BL_RS_PF_048", ["Pixel filter: Gaussian", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", pf_018], 
		["BL_RS_PF_049", ["Pixel filter: Gaussian", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", pf_019], 
		["BL_RS_PF_050", ["Pixel filter: Gaussian", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", pf_020],

		["BL_RS_PF_051", ["Pixel filter: Box", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", pf_021], 
		["BL_RS_PF_052", ["Pixel filter: Box", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", pf_022],
		["BL_RS_PF_053", ["Pixel filter: Box", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", pf_023], 
		["BL_RS_PF_054", ["Pixel filter: Box", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", pf_024], 
		["BL_RS_PF_055", ["Pixel filter: Box", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", pf_025], 

		["BL_RS_PF_056", ["Pixel filter: Blackmanharris", "Radius: 0"], "Hard_Pixel_Filters_Scene.blend", pf_026], 
		["BL_RS_PF_057", ["Pixel filter: Blackmanharris", "Radius: 1"], "Hard_Pixel_Filters_Scene.blend", pf_027],
		["BL_RS_PF_058", ["Pixel filter: Blackmanharris", "Radius: 1.5"], "Hard_Pixel_Filters_Scene.blend", pf_028], 
		["BL_RS_PF_059", ["Pixel filter: Blackmanharris", "Radius: 5"], "Hard_Pixel_Filters_Scene.blend", pf_029], 
		["BL_RS_PF_060", ["Pixel filter: Blackmanharris", "Radius: 10"], "Hard_Pixel_Filters_Scene.blend", pf_030]
	
	]

	launch_tests()



