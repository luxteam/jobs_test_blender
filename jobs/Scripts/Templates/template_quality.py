
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	Scenename = bpy.context.scene.name

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.rpr.render.global_illumination.max_ray_depth = test_list[3]
	bpy.context.scene.rpr.render.global_illumination.max_diffuse_depth = test_list[4]
	bpy.context.scene.rpr.render.global_illumination.max_glossy_depth = test_list[5]
	bpy.context.scene.rpr.render.global_illumination.max_refraction_depth = test_list[6]
	bpy.context.scene.rpr.render.global_illumination.max_glossy_refraction_depth = test_list[7]
	bpy.context.scene.rpr.render.global_illumination.max_shadow_depth = test_list[8]
	bpy.context.scene.rpr.render.global_illumination.ray_epsilon = test_list[9]
	bpy.context.scene.rpr.render.global_illumination.use_clamp_irradiance = test_list[10]
	bpy.context.scene.rpr.render.global_illumination.clamp_irradiance = test_list[11]
	bpy.context.scene.rpr.render.downscale_textures_production = test_list[12]

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_QL_001", ["Max Ray Depth - 2"], "Quality.blend", 2, 3, 5, 5, 5, 5, 0.02, True, 1, False], 
	["BL_RS_QL_002", ["Max Ray Depth - 50"], "Quality.blend", 50, 3, 5, 5, 5, 5, 0.02, True, 1, False], 
	["BL_RS_QL_003", ["Max Diffuse - 2"], "Quality.blend", 8, 2, 5, 5, 5, 5, 0.02, True, 1, False], 
	["BL_RS_QL_004", ["Max Diffuse - 50"], "Quality.blend", 8, 50, 5, 5, 5, 5, 0.02, True, 1, False], 
	["BL_RS_QL_005", ["Max Glossy - 2"], "Quality.blend", 8, 3, 2, 5, 5, 5, 0.02, True, 1, False], 
	["BL_RS_QL_006", ["Max Glossy - 50"], "Quality.blend", 8, 3, 50, 5, 5, 5, 0.02, True, 1, False], 
	["BL_RS_QL_007", ["Max Refraction - 1"], "Quality.blend", 8, 3, 5, 1, 5, 5, 0.02, True, 1, False], 
	["BL_RS_QL_008", ["Max Refraction - 50"], "Quality.blend", 8, 3, 5, 50, 5, 5, 0.02, True, 1, False], 
	["BL_RS_QL_009", ["Max Glossy Refraction - 1"], "Quality.blend", 8, 3, 5, 5, 1, 5, 0.02, True, 1, False], 
	["BL_RS_QL_010", ["Max Glossy Refraction - 50"], "Quality.blend", 8, 3, 5, 5, 50, 5, 0.02, True, 1, False], 
	["BL_RS_QL_011", ["Max Shadow - 1"], "Quality.blend", 8, 3, 5, 5, 5, 1, 0.02, True, 1, False], 
	["BL_RS_QL_012", ["Max Shadow - 50"], "Quality.blend", 8, 3, 5, 5, 5, 50, 0.02, True, 1, False], 
	["BL_RS_QL_013", ["Ray Cast Epsilon - 0"], "Quality.blend", 8, 3, 5, 5, 5, 5, 0, True, 1, False], 
	["BL_RS_QL_014", ["Ray Cast Epsilon - 50"], "Quality.blend", 8, 3, 5, 5, 5, 5, 50, True, 1, False], 
	["BL_RS_QL_015", ["Clamp Irradience - 100"], "Quality.blend", 8, 3, 5, 5, 5, 5, 0.02, True, 100, False], 
	["BL_RS_QL_016", ["Turn off \"Use Clamp\""], "Quality.blend", 8, 3, 5, 5, 5, 5, 0.02, False, 1, False], 
	["BL_RS_QL_017", ["Activate \"Downscale Textures in Production\" "], "Quality.blend", 8, 3, 5, 5, 5, 5, 0.02, True, 1, True], 
	["BL_RS_QL_018", ["Complex parameters"], "Quality.blend", 2, 2, 2, 1, 1, 1, 0, True, 1, False], 
	["BL_RS_QL_019", ["Complex parameters"], "Quality.blend", 50, 50, 50, 50, 50, 50, 50, True, 100, False], 

	]

	launch_tests()



