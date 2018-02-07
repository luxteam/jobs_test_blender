
def main(format):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = format

	render(format)


if __name__ == "__main__":

	formats = ['JPEG', 'BMP', 'PNG', 'IRIS', 'JPEG2000', 'TARGA', 'TARGA_RAW', 'DPX', 'OPEN_EXR_MULTILAYER', 'OPEN_EXR', 'CINEON', 'HDR', 'TIFF']
	for format in formats:
		main(format)