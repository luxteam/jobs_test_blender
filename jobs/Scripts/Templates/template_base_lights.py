
def main(type_light, intensity, use_map):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'


	bpy.context.scene.objects.active = bpy.data.objects['Lamp']
	bpy.context.object.data.type = type_light
	bpy.data.lamps["Lamp"].rpr_lamp.intensity = intensity
	if use_map:
		ies = os.path.join("{res_path}", "Candle.fbm\\PD6R12ED010- PDM6835-694SNB.ies")
		bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = ies
	else:
		bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = r""

	render(type_light, intensity, use_map)

if __name__ == "__main__":

	main('POINT', 1000, False)
	main('POINT', 1000, True)
	main('HEMI', 50, False)
	main('SUN', 50, False)
	main('SPOT', 2000, False)
	main('AREA', 100, False)
	main('AREA', 100, True)


