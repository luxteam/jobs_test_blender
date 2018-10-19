
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = test_list[3]
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	render(test_list[0], test_list[1])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/" + test_list[0] + ".jpg")
	
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_IF_001", ["Image format: jpeg"], "ComplexTestUber.blend", "JPEG"], 
	["BL_RS_IF_002", ["Image format: bmp"], "ComplexTestUber.blend", "BMP"], 
	["BL_RS_IF_003", ["Image format: png"], "ComplexTestUber.blend", "PNG"], 
	["BL_RS_IF_004", ["Image format: iris"], "ComplexTestUber.blend", "IRIS"], 
	["BL_RS_IF_005", ["Image format: jpeg2000"], "ComplexTestUber.blend", "JPEG2000"], 
	["BL_RS_IF_006", ["Image format: targa"], "ComplexTestUber.blend", "TARGA"], 
	["BL_RS_IF_007", ["Image format: targa_raw"], "ComplexTestUber.blend", "TARGA_RAW"], 
	["BL_RS_IF_008", ["Image format: dpx"], "ComplexTestUber.blend", "DPX"],
	["BL_RS_IF_009", ["Image format: open_exr_multilayer"], "ComplexTestUber.blend", "OPEN_EXR_MULTILAYER"], 
	["BL_RS_IF_010", ["Image format: open_exr"], "ComplexTestUber.blend", "OPEN_EXR"],
	["BL_RS_IF_011", ["Image format: cineon"], "ComplexTestUber.blend", "CINEON"], 
	["BL_RS_IF_012", ["Image format: hdr"], "ComplexTestUber.blend", "HDR"], 
	["BL_RS_IF_013", ["Image format: tiff"], "ComplexTestUber.blend", "TIFF"]
	]
 
	launch_tests()
