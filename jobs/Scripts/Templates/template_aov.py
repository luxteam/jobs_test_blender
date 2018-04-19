def main(i, test_case):

	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} != 0 and {resolution_y} != 0):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[i] = True
	render(test_case)
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[i] = False

if __name__ == "__main__":

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[1] = False

	for i in range(23):
		if i<10:
			main(i, "BL_RS_AOV_00" + str(i+1))
		else:
			main(i, "BL_RS_AOV_0" + str(i+1))

	main(0, "BL_RS_AOV_001", ["AOV: "])
	main(1, "BL_RS_AOV_002", ["AOV: "])
	main(2, "BL_RS_AOV_003", ["AOV: "])
	main(3, "BL_RS_AOV_004", ["AOV: "])
	main(4, "BL_RS_AOV_005", ["AOV: "])
	main(5, "BL_RS_AOV_006", ["AOV: "])
	main(6, "BL_RS_AOV_007", ["AOV: "])
	main(7, "BL_RS_AOV_008", ["AOV: "])
	main(8, "BL_RS_AOV_009", ["AOV: "])
	main(9, "BL_RS_AOV_010", ["AOV: "])
	main(10, "BL_RS_AOV_011", ["AOV: "])
	main(11, "BL_RS_AOV_012", ["AOV: "])
	main(12, "BL_RS_AOV_013", ["AOV: "])
	main(13, "BL_RS_AOV_014", ["AOV: "])
	main(14, "BL_RS_AOV_015", ["AOV: "])
	main(15, "BL_RS_AOV_016", ["AOV: "])
	main(16, "BL_RS_AOV_017", ["AOV: "])
	main(17, "BL_RS_AOV_018", ["AOV: "])
	main(18, "BL_RS_AOV_019", ["AOV: "])
	main(19, "BL_RS_AOV_020", ["AOV: "])
	main(20, "BL_RS_AOV_021", ["AOV: "])
	main(21, "BL_RS_AOV_022", ["AOV: "])
	main(22, "BL_RS_AOV_023", ["AOV: "])
