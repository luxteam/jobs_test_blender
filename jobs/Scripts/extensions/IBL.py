def resetSceneAttributes():
    set_value(bpy.context.scene.world.rpr, 'enabled', True)
    set_value(bpy.context.scene.world.rpr, 'mode', 'IBL')
    set_value(bpy.context.scene.world.rpr, 'intensity', 1)
    set_value(bpy.context.scene.world.rpr.ibl, 'color', (0.5, 0.5, 0.5))
    set_value(bpy.context.scene.world.rpr.ibl, 'image', None)
    set_value(bpy.context.scene.world.rpr, 'background_override', False)
    set_value(bpy.context.scene.world.rpr, 'background_color', (0.5, 0.5, 0.5))
    set_value(bpy.context.scene.world.rpr, 'background_image', None)
    set_value(bpy.context.scene.world.rpr, 'reflection_override', False)
    set_value(bpy.context.scene.world.rpr, 'reflection_color', (0.5, 0.5, 0.5))
    set_value(bpy.context.scene.world.rpr, 'reflection_image', None)
    set_value(bpy.context.scene.world.rpr, 'refraction_override', False)
    set_value(bpy.context.scene.world.rpr, 'refraction_color', (0.5, 0.5, 0.5))
    set_value(bpy.context.scene.world.rpr, 'refraction_image', None)
    set_value(bpy.context.scene.world.rpr, 'transparency_override', False)
    set_value(bpy.context.scene.world.rpr,
              'transparency_color', (0.5, 0.5, 0.5))
    set_value(bpy.context.scene.world.rpr, 'transparency_image', None)
