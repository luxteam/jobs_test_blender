def main(i, test_case, script_info):

	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[i] = True
	render(test_case, script_info)
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[i] = False

if __name__ == "__main__":

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[1] = False

	main(0, "BL_RS_AOV_001", ["AOV: Combined"])
	main(1, "BL_RS_AOV_002", ["AOV: Depth"])
	main(2, "BL_RS_AOV_003", ["AOV: UV"])
	main(3, "BL_RS_AOV_004", ["AOV: Object Index"])
	main(4, "BL_RS_AOV_005", ["AOV: Material Index"])
	main(5, "BL_RS_AOV_006", ["AOV: World Coordinate"])
	main(6, "BL_RS_AOV_007", ["AOV: Geometric Normal"])
	main(7, "BL_RS_AOV_008", ["AOV: Shading Normal"])
	main(8, "BL_RS_AOV_009", ["AOV: Group Index"])
	main(9, "BL_RS_AOV_010", ["AOV: Shadow Catcher"])
	main(10, "BL_RS_AOV_011", ["AOV: Background"])
	main(11, "BL_RS_AOV_012", ["AOV: Emission"])
	main(12, "BL_RS_AOV_013", ["AOV: Velocity"])
	main(13, "BL_RS_AOV_014", ["AOV: Direct Illumination"])
	main(14, "BL_RS_AOV_015", ["AOV: Indirect Illumination"])
	main(15, "BL_RS_AOV_016", ["AOV: Ambient Occlusion"])
	main(16, "BL_RS_AOV_017", ["AOV: Direct Diffuse"])
	main(17, "BL_RS_AOV_018", ["AOV: Direct Reflection"])
	main(18, "BL_RS_AOV_019", ["AOV: Indirect Diffuse"])
	main(19, "BL_RS_AOV_020", ["AOV: Indirect Reflection"])
	main(20, "BL_RS_AOV_021", ["AOV: Refraction"])
	main(21, "BL_RS_AOV_022", ["AOV: Volume"])
	main(22, "BL_RS_AOV_023", ["AOV: Opacity"])
