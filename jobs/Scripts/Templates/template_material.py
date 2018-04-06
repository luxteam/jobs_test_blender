def main(material_name):

	#get scene name
	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	matlib = material_browser.RPRMaterialLibrary()
	matlib_path = matlib.get_library_path() + material_name + "\\" + material_name + ".xml"
	material = bpy.data.materials['Material']
	material_browser.import_xml_material(matlib_path, material)
	render(material_name)

if __name__ == "__main__":

	with open("{work_dir}" + "/../../../../jobs/Tests/Material_Library_Test/materials.txt") as mat:
		print ("{work_dir}" + "/../../../../jobs/Tests/Material_Library_Test/materials.txt")
		materials = mat.read()
	materials = materials.split(",\n")

	for m in materials:
		main(m)


