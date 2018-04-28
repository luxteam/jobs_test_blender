
def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = test_list[2]
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	render(test_list[0], test_list[1])

	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/" + test_list[0] + ".jpg")

	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_IF_001", ["Image format: jpeg"], "JPEG"], 
	["BL_RS_IF_002", ["Image format: bmp"], "BMP"], 
	["BL_RS_IF_003", ["Image format: png"], "PNG"], 
	["BL_RS_IF_004", ["Image format: iris"], "IRIS"], 
	["BL_RS_IF_005", ["Image format: jpeg2000"], "JPEG2000"], 
	["BL_RS_IF_006", ["Image format: targa"], "TARGA"], 
	["BL_RS_IF_007", ["Image format: targa_raw"], "TARGA_RAW"], 
	["BL_RS_IF_008", ["Image format: dpx"], "DPX"],
	["BL_RS_IF_009", ["Image format: open_exr_multilayer"], "OPEN_EXR_MULTILAYER"], 
	["BL_RS_IF_010", ["Image format: open_exr"], "OPEN_EXR"],
	["BL_RS_IF_011", ["Image format: cineon"], "CINEON"], 
	["BL_RS_IF_012", ["Image format: hdr"], "HDR"], 
	["BL_RS_IF_013", ["Image format: tiff"], "TIFF"]
	]
 
	launch_tests()
