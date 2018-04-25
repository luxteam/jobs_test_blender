
def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[1] = False

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[test_list[2]] = True
	render(test_list[0], test_list[1])
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[test_list[2]] = False

if __name__ == "__main__":

	list_tests = [
	["BL_RS_AOV_001", ["AOV: Combined"], 0], 
	["BL_RS_AOV_002", ["AOV: Depth"], 1], 
	["BL_RS_AOV_003", ["AOV: UV"], 2], 
	["BL_RS_AOV_004", ["AOV: Object Index"], 3], 
	["BL_RS_AOV_005", ["AOV: Material Index"], 4], 
	["BL_RS_AOV_006", ["AOV: World Coordinate"], 5],
	["BL_RS_AOV_007", ["AOV: Geometric Normal"], 6], 
	["BL_RS_AOV_008", ["AOV: Shading Normal"], 7], 
	["BL_RS_AOV_009", ["AOV: Group Index"], 8],
	["BL_RS_AOV_010", ["AOV: Shadow Catcher"], 9], 
	["BL_RS_AOV_011", ["AOV: Background"], 10], 
	["BL_RS_AOV_012", ["AOV: Emission"], 11],
	["BL_RS_AOV_013", ["AOV: Velocity"], 12], 
	["BL_RS_AOV_014", ["AOV: Direct Illumination"], 13], 
	["BL_RS_AOV_015", ["AOV: Indirect Illumination"], 14],
	["BL_RS_AOV_016", ["AOV: Ambient Occlusion"], 15], 
	["BL_RS_AOV_017", ["AOV: Direct Diffuse"], 16], 
	["BL_RS_AOV_018", ["AOV: Direct Reflection"], 17], 
	["BL_RS_AOV_019", ["AOV: Indirect Diffuse"], 18], 
	["BL_RS_AOV_020", ["AOV: Indirect Reflection"], 19], 
	["BL_RS_AOV_021", ["AOV: Refraction"], 20],
	["BL_RS_AOV_022", ["AOV: Volume"], 21], 
	["BL_RS_AOV_023", ["AOV: Opacity"], 22]
	]

	launch_tests()
