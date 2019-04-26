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
    return 1


if __name__ == "__main__":

   list_tests = [
    ["TEST_CASE", ["DESCRIPTION"], "SCENE NAME.blend", any_value],
   ]
   launch_tests()
