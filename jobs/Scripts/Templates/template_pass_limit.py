
def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = test_list[3]
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	if (test_list[2] == "ComplexTestUber.blend"):
		render(test_list[0], test_list[1])
	elif (test_list[2] == "default.blend"):
		render(test_list[0], test_list[1])
	elif (test_list[2] == "rpr_default.blend"):
		render(test_list[0], test_list[1])

if __name__ == "__main__":

	list_tests = [
	["BL_RS_PS_001", ["Pass Limit: 1"], "ComplexTestUber.blend", 1],
	["BL_RS_PS_002", ["Pass Limit: 100"], "ComplexTestUber.blend", 100],
	["BL_RS_PS_003", ["Pass Limit: 500"], "ComplexTestUber.blend", 500],
	["BL_RS_PS_004", ["Pass Limit: 1000"], "ComplexTestUber.blend", 1000],
	["BL_RS_PS_005", ["Pass Limit: 5000"], "ComplexTestUber.blend", 5000],
	["BL_RS_PS_006", ["Pass Limit: 10000"], "ComplexTestUber.blend", 10000],
	["BL_RS_PS_007", ["Pass Limit: 1", "NEED SCENE"], "default.blend", 1],
	["BL_RS_PS_008", ["Pass Limit: 100", "NEED SCENE"], "default.blend", 100],
	["BL_RS_PS_009", ["Pass Limit: 500", "NEED SCENE"], "default.blend", 500],
	["BL_RS_PS_010", ["Pass Limit: 1000", "NEED SCENE"], "default.blend", 1000],
	["BL_RS_PS_011", ["Pass Limit: 5000", "NEED SCENE"], "default.blend", 5000],
	["BL_RS_PS_012", ["Pass Limit: 10000", "NEED SCENE"], "default.blend", 10000],
	["BL_RS_PS_013", ["Pass Limit: 1", "NEED SCENE"], "rpr_default.blend", 1],
	["BL_RS_PS_014", ["Pass Limit: 100", "NEED SCENE"], "rpr_default.blend", 100],
	["BL_RS_PS_015", ["Pass Limit: 500", "NEED SCENE"], "rpr_default.blend", 500],
	["BL_RS_PS_016", ["Pass Limit: 1000", "NEED SCENE"], "rpr_default.blend", 1000],
	["BL_RS_PS_017", ["Pass Limit: 5000", "NEED SCENE"], "rpr_default.blend", 5000],
	["BL_RS_PS_018", ["Pass Limit: 10000", "NEED SCENE"], "rpr_default.blend", 10000],
	]

	launch_tests()