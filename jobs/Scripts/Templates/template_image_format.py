
def main(format, test_case, script_info):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = format
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	render(test_case, script_info)


if __name__ == "__main__":

	main("JPEG", "BL_RS_IF_001", ["Image format: jpeg"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_001.jpg")
	main("BMP", "BL_RS_IF_002", ["Image format: bmp"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_002.jpg")
	main("PNG", "BL_RS_IF_003", ["Image format: png"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_003.jpg")
	main("IRIS", "BL_RS_IF_004", ["Image format: iris"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_004.jpg")
	main("JPEG2000", "BL_RS_IF_005", ["Image format: jpeg2000"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_005.jpg")
	main("TARGA", "BL_RS_IF_006", ["Image format: targa"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_006.jpg")
	main("TARGA_RAW", "BL_RS_IF_007", ["Image format: targa_raw"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_007.jpg")
	main("DPX", "BL_RS_IF_008", ["Image format: dpx"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_008.jpg")
	main("OPEN_EXR_MULTILAYER", "BL_RS_IF_009", ["Image format: open_exr_multilayer"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_009.jpg")
	main("OPEN_EXR", "BL_RS_IF_010", ["Image format: open_exr"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_010.jpg")
	main("CINEON", "BL_RS_IF_011", ["Image format: cineon"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_011.jpg")
	main("HDR", "BL_RS_IF_012", ["Image format: hdr"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_012.jpg")
	main("TIFF", "BL_RS_IF_013", ["Image format: tiff"])
	copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/BL_RS_IF_013.jpg")