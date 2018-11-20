
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	scene = bpy.context.scene

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	scene.render.engine = "RPR"

	scene.rpr.use_render_stamp = False
	scene.rpr.render.rendering_limits.iterations = {pass_limit}
	scene.render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		scene.render.resolution_x = {resolution_x}
		scene.render.resolution_y = {resolution_y}

	scene.frame_set(test_list[3])


	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_AN_001", ["Frame: 41"], "Keyed_Animation.blend", 41], 
	["BL_RS_AN_002", ["Frame: 42"], "Keyed_Animation.blend", 42],
	["BL_RS_AN_003", ["Frame: 43"], "Keyed_Animation.blend", 43],
	["BL_RS_AN_004", ["Frame: 44"], "Keyed_Animation.blend", 44],
	["BL_RS_AN_005", ["Frame: 45"], "Keyed_Animation.blend", 45],
	["BL_RS_AN_006", ["Frame: 46"], "Keyed_Animation.blend", 46],
	["BL_RS_AN_007", ["Frame: 47"], "Keyed_Animation.blend", 47],
	["BL_RS_AN_008", ["Frame: 48"], "Keyed_Animation.blend", 48],
	["BL_RS_AN_009", ["Frame: 49"], "Keyed_Animation.blend", 49],
	["BL_RS_AN_010", ["Frame: 50"], "Keyed_Animation.blend", 50],
	["BL_RS_AN_011", ["Frame: 81"], "Keyed_Animation.blend", 81], 
	["BL_RS_AN_012", ["Frame: 82"], "Keyed_Animation.blend", 82],
	["BL_RS_AN_013", ["Frame: 83"], "Keyed_Animation.blend", 83],
	["BL_RS_AN_014", ["Frame: 84"], "Keyed_Animation.blend", 84],
	["BL_RS_AN_015", ["Frame: 85"], "Keyed_Animation.blend", 85],
	["BL_RS_AN_016", ["Frame: 86"], "Keyed_Animation.blend", 86],
	["BL_RS_AN_017", ["Frame: 87"], "Keyed_Animation.blend", 87],
	["BL_RS_AN_018", ["Frame: 88"], "Keyed_Animation.blend", 88],
	["BL_RS_AN_019", ["Frame: 89"], "Keyed_Animation.blend", 89],
	["BL_RS_AN_020", ["Frame: 90"], "Keyed_Animation.blend", 90],
	["BL_RS_AN_021", ["Frame: 141"], "Keyed_Animation.blend", 141], 
	["BL_RS_AN_022", ["Frame: 142"], "Keyed_Animation.blend", 142],
	["BL_RS_AN_023", ["Frame: 143"], "Keyed_Animation.blend", 143],
	["BL_RS_AN_024", ["Frame: 144"], "Keyed_Animation.blend", 144],
	["BL_RS_AN_025", ["Frame: 145"], "Keyed_Animation.blend", 145],
	["BL_RS_AN_026", ["Frame: 146"], "Keyed_Animation.blend", 146],
	["BL_RS_AN_027", ["Frame: 147"], "Keyed_Animation.blend", 147],
	["BL_RS_AN_028", ["Frame: 148"], "Keyed_Animation.blend", 148],
	["BL_RS_AN_029", ["Frame: 149"], "Keyed_Animation.blend", 149],
	["BL_RS_AN_030", ["Frame: 150"], "Keyed_Animation.blend", 150],
	["BL_RS_AN_031", ["Frame: 1"], "NonKeyed_Animation.blend", 1], 
	["BL_RS_AN_032", ["Frame: 2"], "NonKeyed_Animation.blend", 2],
	["BL_RS_AN_033", ["Frame: 3"], "NonKeyed_Animation.blend", 3],
	["BL_RS_AN_034", ["Frame: 4"], "NonKeyed_Animation.blend", 4],
	["BL_RS_AN_035", ["Frame: 5"], "NonKeyed_Animation.blend", 5],
	["BL_RS_AN_036", ["Frame: 6"], "NonKeyed_Animation.blend", 6],
	["BL_RS_AN_037", ["Frame: 7"], "NonKeyed_Animation.blend", 7],
	["BL_RS_AN_038", ["Frame: 8"], "NonKeyed_Animation.blend", 8],
	["BL_RS_AN_039", ["Frame: 9"], "NonKeyed_Animation.blend", 9],
	["BL_RS_AN_040", ["Frame: 10"], "NonKeyed_Animation.blend", 10],
	["BL_RS_AN_041", ["Frame: 11"], "NonKeyed_Animation.blend", 11], 
	["BL_RS_AN_042", ["Frame: 12"], "NonKeyed_Animation.blend", 12],
	["BL_RS_AN_043", ["Frame: 13"], "NonKeyed_Animation.blend", 13],
	["BL_RS_AN_044", ["Frame: 14"], "NonKeyed_Animation.blend", 14],
	["BL_RS_AN_045", ["Frame: 15"], "NonKeyed_Animation.blend", 15],
	["BL_RS_AN_046", ["Frame: 16"], "NonKeyed_Animation.blend", 16],
	["BL_RS_AN_047", ["Frame: 17"], "NonKeyed_Animation.blend", 17],
	["BL_RS_AN_048", ["Frame: 18"], "NonKeyed_Animation.blend", 18],
	["BL_RS_AN_049", ["Frame: 19"], "NonKeyed_Animation.blend", 19],
	["BL_RS_AN_050", ["Frame: 20"], "NonKeyed_Animation.blend", 20],
	["BL_RS_AN_051", ["Frame: 21"], "NonKeyed_Animation.blend", 21], 
	["BL_RS_AN_052", ["Frame: 22"], "NonKeyed_Animation.blend", 22],
	["BL_RS_AN_053", ["Frame: 23"], "NonKeyed_Animation.blend", 23],
	["BL_RS_AN_054", ["Frame: 24"], "NonKeyed_Animation.blend", 24],
	["BL_RS_AN_055", ["Frame: 25"], "NonKeyed_Animation.blend", 25],
	["BL_RS_AN_056", ["Frame: 26"], "NonKeyed_Animation.blend", 26],
	["BL_RS_AN_057", ["Frame: 27"], "NonKeyed_Animation.blend", 27],
	["BL_RS_AN_058", ["Frame: 28"], "NonKeyed_Animation.blend", 28],
	["BL_RS_AN_059", ["Frame: 29"], "NonKeyed_Animation.blend", 29],
	["BL_RS_AN_060", ["Frame: 30"], "NonKeyed_Animation.blend", 30]
	
	]

	launch_tests()



