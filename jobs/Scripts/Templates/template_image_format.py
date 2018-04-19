
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
	main("BMP", "BL_RS_IF_002", ["Image format: bmp"])
	main("PNG", "BL_RS_IF_003", ["Image format: png"])
	main("IRIS", "BL_RS_IF_004", ["Image format: iris"])
	main("JPEG2000", "BL_RS_IF_005", ["Image format: jpeg2000"])
	main("TARGA", "BL_RS_IF_006", ["Image format: targa"])
	main("TARGA_RAW", "BL_RS_IF_007", ["Image format: targa_raw"])
	main("DPX", "BL_RS_IF_008", ["Image format: dpx"])
	main("OPEN_EXR_MULTILAYER", "BL_RS_IF_009", ["Image format: open_exr_multilayer"])
	main("OPEN_EXR", "BL_RS_IF_010", ["Image format: open_exr"])
	main("CINEON", "BL_RS_IF_011", ["Image format: cineon"])
	main("HDR", "BL_RS_IF_012", ["Image format: hdr"])
	main("TIFF", "BL_RS_IF_013", ["Image format: tiff"])