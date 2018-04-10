
def main(format, test_case):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = format

	render(test_case)


if __name__ == "__main__":

	formats = ['JPEG', 'BMP', 'PNG', 'IRIS', 'JPEG2000', 'TARGA', 'TARGA_RAW', 'DPX', 'OPEN_EXR_MULTILAYER', 'OPEN_EXR', 'CINEON', 'HDR', 'TIFF']
	for f in range(len(formats)):
		if f < 10:
			main(formats[f], "BL_RS_IF_00" + str(f+1))
		else:
			main(formats[f], "BL_RS_IF_0" + str(f+1))