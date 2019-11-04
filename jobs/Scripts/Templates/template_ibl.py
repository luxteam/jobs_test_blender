
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	# make changes
	test_list[3]()
	# render
	render(test_list[0], test_list[1])
	# undo changes
	resetSceneAttributes()	

	return 1


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
	set_value(bpy.context.scene.world.rpr, 'transparency_color', (0.5, 0.5, 0.5))
	set_value(bpy.context.scene.world.rpr, 'transparency_image', None)


def ibl_001():
	set_value(bpy.context.scene.world.rpr, 'intensity', 0)


def ibl_002():
	set_value(bpy.context.scene.world.rpr, 'intensity', 1)


def ibl_003():
	set_value(bpy.context.scene.world.rpr, 'intensity', 2)


def ibl_004():
	set_value(bpy.context.scene.world.rpr, 'intensity', 3)


def ibl_005():
	set_value(bpy.context.scene.world.rpr, 'intensity', 5)


def ibl_006():
	set_value(bpy.context.scene.world.rpr, 'intensity', 7)


def ibl_007():
	set_value(bpy.context.scene.world.rpr, 'intensity', 10)


def ibl_008():
	set_value(bpy.context.scene.world.rpr, 'intensity', 0)
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.hdr'])


def ibl_009():
	set_value(bpy.context.scene.world.rpr, 'intensity', 1)
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.hdr'])


def ibl_010():
	set_value(bpy.context.scene.world.rpr, 'intensity', 2)
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.hdr'])


def ibl_011():
	set_value(bpy.context.scene.world.rpr, 'intensity', 3)
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.hdr'])


def ibl_012():
	set_value(bpy.context.scene.world.rpr, 'intensity', 5)
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.hdr'])


def ibl_013():
	set_value(bpy.context.scene.world.rpr, 'intensity', 7)
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.hdr'])


def ibl_014():
	set_value(bpy.context.scene.world.rpr, 'intensity', 10)
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.hdr'])


def ibl_015():
	set_value(bpy.context.scene.world.rpr, 'intensity', 0)
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.exr'])


def ibl_016():
	set_value(bpy.context.scene.world.rpr, 'intensity', 1)
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.exr'])


def ibl_017():
	set_value(bpy.context.scene.world.rpr, 'intensity', 2)
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.exr'])


def ibl_018():
	set_value(bpy.context.scene.world.rpr, 'intensity', 3)
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.exr'])


def ibl_019():
	set_value(bpy.context.scene.world.rpr, 'intensity', 5)
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.exr'])


def ibl_020():
	set_value(bpy.context.scene.world.rpr, 'intensity', 7)
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.exr'])


def ibl_021():
	set_value(bpy.context.scene.world.rpr, 'intensity', 10)
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr.ibl, 'image', bpy.data.images['1.exr'])


def ibl_022():
	set_value(bpy.context.scene.world.rpr, 'background_override', True)
	set_value(bpy.context.scene.world.rpr, 'background_image_type', 'SPHERE')
	set_value(bpy.context.scene.world.rpr, 'background_color', (0, 0.4, 0))


def ibl_023():
	set_value(bpy.context.scene.world.rpr, 'background_override', True)
	set_value(bpy.context.scene.world.rpr, 'background_image_type', 'SPHERE')
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr, 'background_image', bpy.data.images['1.hdr'])


def ibl_024():
	set_value(bpy.context.scene.world.rpr, 'background_override', True)
	set_value(bpy.context.scene.world.rpr, 'background_image_type', 'SPHERE')
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr, 'background_image', bpy.data.images['1.exr'])


def ibl_034():
	set_value(bpy.context.scene.world.rpr, 'background_override', True)
	set_value(bpy.context.scene.world.rpr, 'background_image_type', 'BACKPLATE')
	bpy.ops.image.open(filepath="//Maps//UVgrid2.jpg", directory="{resource_path}//Maps//", files=[{{"name":"UVgrid2.jpg"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr, 'background_image', bpy.data.images['UVgrid2.jpg'])


def ibl_025():
	set_value(bpy.context.scene.world.rpr, 'reflection_override', True)
	set_value(bpy.context.scene.world.rpr, 'reflection_image_type', 'SPHERE')
	set_value(bpy.context.scene.world.rpr, 'reflection_color', (0, 0.4, 0))


def ibl_026():
	set_value(bpy.context.scene.world.rpr, 'reflection_override', True)
	set_value(bpy.context.scene.world.rpr, 'reflection_image_type', 'SPHERE')
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr, 'reflection_image', bpy.data.images['1.hdr'])


def ibl_027():
	set_value(bpy.context.scene.world.rpr, 'reflection_override', True)
	set_value(bpy.context.scene.world.rpr, 'reflection_image_type', 'SPHERE')
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr, 'reflection_image', bpy.data.images['1.exr'])


def ibl_028():
	set_value(bpy.context.scene.world.rpr, 'refraction_override', True)
	set_value(bpy.context.scene.world.rpr, 'refraction_image_type', 'SPHERE')
	set_value(bpy.context.scene.world.rpr, 'refraction_color', (0, 0.4, 0))


def ibl_029():
	set_value(bpy.context.scene.world.rpr, 'refraction_override', True)
	set_value(bpy.context.scene.world.rpr, 'refraction_image_type', 'SPHERE')
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr, 'refraction_image', bpy.data.images['1.hdr'])


def ibl_030():
	set_value(bpy.context.scene.world.rpr, 'refraction_override', True)
	set_value(bpy.context.scene.world.rpr, 'refraction_image_type', 'SPHERE')
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr, 'refraction_image', bpy.data.images['1.exr'])


def ibl_031():
	set_value(bpy.context.scene.world.rpr, 'transparency_override', True)
	set_value(bpy.context.scene.world.rpr, 'transparency_image_type', 'SPHERE')
	set_value(bpy.context.scene.world.rpr, 'transparency_color', (0, 0.4, 0))


def ibl_032():
	set_value(bpy.context.scene.world.rpr, 'transparency_override', True)
	set_value(bpy.context.scene.world.rpr, 'transparency_image_type', 'SPHERE')
	bpy.ops.image.open(filepath="//Maps//1.hdr", directory="{resource_path}//Maps//", files=[{{"name":"1.hdr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr, 'transparency_image', bpy.data.images['1.hdr'])


def ibl_033():
	set_value(bpy.context.scene.world.rpr, 'transparency_override', True)
	set_value(bpy.context.scene.world.rpr, 'transparency_image_type', 'SPHERE')
	bpy.ops.image.open(filepath="//Maps//1.exr", directory="{resource_path}//Maps//", files=[{{"name":"1.exr"}}], relative_path=True, show_multiview=False)
	set_value(bpy.context.scene.world.rpr, 'transparency_image', bpy.data.images['1.exr'])



if __name__ == "__main__":

	list_tests = [
		["BL28_RS_IBL_001", ["Intensity: 0"], "ComplexTestUber.blend", ibl_001], 
		["BL28_RS_IBL_002", ["Intensity: 1"], "ComplexTestUber.blend", ibl_002], 
		["BL28_RS_IBL_003", ["Intensity: 2"], "ComplexTestUber.blend", ibl_003], 
		["BL28_RS_IBL_004", ["Intensity: 3"], "ComplexTestUber.blend", ibl_004], 
		["BL28_RS_IBL_005", ["Intensity: 5"], "ComplexTestUber.blend", ibl_005], 
		["BL28_RS_IBL_006", ["Intensity: 7"], "ComplexTestUber.blend", ibl_006], 
		["BL28_RS_IBL_007", ["Intensity: 10"], "ComplexTestUber.blend", ibl_007],

		["BL28_RS_IBL_008", ["Intensity: 0", "HDR Map"], "ComplexTestUber.blend", ibl_008], 
		["BL28_RS_IBL_009", ["Intensity: 1", "HDR Map"], "ComplexTestUber.blend", ibl_009], 
		["BL28_RS_IBL_010", ["Intensity: 2", "HDR Map"], "ComplexTestUber.blend", ibl_010], 
		["BL28_RS_IBL_011", ["Intensity: 3", "HDR Map"], "ComplexTestUber.blend", ibl_011], 
		["BL28_RS_IBL_012", ["Intensity: 5", "HDR Map"], "ComplexTestUber.blend", ibl_012], 
		["BL28_RS_IBL_013", ["Intensity: 7", "HDR Map"], "ComplexTestUber.blend", ibl_013], 
		["BL28_RS_IBL_014", ["Intensity: 10", "HDR Map"], "ComplexTestUber.blend", ibl_014],

		["BL28_RS_IBL_015", ["Intensity: 0", "EXR Map"], "ComplexTestUber.blend", ibl_015], 
		["BL28_RS_IBL_016", ["Intensity: 1", "EXR Map"], "ComplexTestUber.blend", ibl_016], 
		["BL28_RS_IBL_017", ["Intensity: 2", "EXR Map"], "ComplexTestUber.blend", ibl_017], 
		["BL28_RS_IBL_018", ["Intensity: 3", "EXR Map"], "ComplexTestUber.blend", ibl_018], 
		["BL28_RS_IBL_019", ["Intensity: 5", "EXR Map"], "ComplexTestUber.blend", ibl_019], 
		["BL28_RS_IBL_020", ["Intensity: 7", "EXR Map"], "ComplexTestUber.blend", ibl_020], 
		["BL28_RS_IBL_021", ["Intensity: 10", "EXR Map"], "ComplexTestUber.blend", ibl_021],

		["BL28_RS_IBL_022", ["Override Background Color"], "ComplexTestUber.blend", ibl_022],
		["BL28_RS_IBL_023", ["Override Background Map HDR"], "ComplexTestUber.blend", ibl_023],
		["BL28_RS_IBL_024", ["Override Background Map EXR"], "ComplexTestUber.blend", ibl_024],

		["BL28_RS_IBL_025", ["Override Reflection Color"], "ComplexTestUber.blend", ibl_025],
		["BL28_RS_IBL_026", ["Override Reflection Map HDR"], "ComplexTestUber.blend", ibl_026],
		["BL28_RS_IBL_027", ["Override Reflection Map EXR"], "ComplexTestUber.blend", ibl_027],

		["BL28_RS_IBL_028", ["Override Refraction Color"], "ComplexTestUber.blend", ibl_028],
		["BL28_RS_IBL_029", ["Override Refraction Map HDR"], "ComplexTestUber.blend", ibl_029],
		["BL28_RS_IBL_030", ["Override Refraction Map EXR"], "ComplexTestUber.blend", ibl_030],

		["BL28_RS_IBL_031", ["Override Transparency Color"], "ComplexTestUber.blend", ibl_031],
		["BL28_RS_IBL_032", ["Override Transparency Map HDR"], "ComplexTestUber.blend", ibl_032],
		["BL28_RS_IBL_033", ["Override Transparency Map EXR"], "ComplexTestUber.blend", ibl_033],

		["BL28_RS_IBL_034", ["Override Background Backplate"], "ComplexTestUber.blend", ibl_034]
	]

	launch_tests()


