

def prerender(test):
    material_name = test[2]
    test_case = test[0]
    script_info = test[1]
    # get scene name
    Scenename = bpy.context.scene.name

    bpy.context.scene.rpr.use_render_stamp = False
    bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
    bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
    if ({resolution_x} and {resolution_y}):
        bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
        bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

    matlib = material_browser.RPRMaterialLibrary()
    matlib_path = matlib.get_library_path() + material_name + "/" + material_name + ".xml"
    material = bpy.data.materials['Material']
    material_browser.import_xml_material(matlib_path, material)

    render(test_case, script_info)
    return 1


if __name__ == "__main__":

    with open("{work_dir}" + "/../../../../jobs/Tests/Material_Library/materials.txt") as mat:
        materials = mat.read()
    materials = materials.split(",\n")

    list_tests = []
    for i in range(0, len(materials)):
        list_tests.append(["BL_MAT_LIB_00" + str(i + 1), ["Material: " + materials[i]], materials[i]])

    launch_tests()
