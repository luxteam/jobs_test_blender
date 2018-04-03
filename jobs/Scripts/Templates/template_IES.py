
def main(IES_file):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.object.data.type = 'POINT'
	bpy.data.lamps["Lamp"].rpr_lamp.intensity = 50
	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , IES_file)

	render(IES_file.split(".")[0])

if __name__ == "__main__":
	
	for each_ies in range(1,11):
		main(str(each_ies) + ".ies")



