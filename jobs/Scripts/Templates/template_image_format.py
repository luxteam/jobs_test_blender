
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
