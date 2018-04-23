
def main(iteration, test_case, script_info):

	
	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = iteration
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	render(test_case, script_info)

if __name__ == "__main__":

	if bpy.path.basename(bpy.context.blend_data.filepath) == "ComplexTestUber.blend":
		main(1, "BL_RS_PS_001", ["Pass Limit: 1"])
		main(100, "BL_RS_PS_002", ["Pass Limit: 100"])
		main(500, "BL_RS_PS_003", ["Pass Limit: 500"])
		main(1000, "BL_RS_PS_004", ["Pass Limit: 1000"])
		main(5000, "BL_RS_PS_005", ["Pass Limit: 5000"])
		main(10000, "BL_RS_PS_006", ["Pass Limit: 10000"])
	elif bpy.path.basename(bpy.context.blend_data.filepath) == "default.blend":
		main(1, "BL_RS_PS_007", ["Pass Limit: 1", "NEED SCENE"])
		main(100, "BL_RS_PS_008", ["Pass Limit: 100", "NEED SCENE"])
		main(500, "BL_RS_PS_009", ["Pass Limit: 500", "NEED SCENE"])
		main(1000, "BL_RS_PS_010", ["Pass Limit: 1000", "NEED SCENE"])
		main(5000, "BL_RS_PS_011", ["Pass Limit: 5000", "NEED SCENE"])
		main(10000, "BL_RS_PS_012", ["Pass Limit: 10000", "NEED SCENE"])
	elif bpy.path.basename(bpy.context.blend_data.filepath) == "rpr_default.blend":
		main(1, "BL_RS_PS_013", ["Pass Limit: 1", "NEED SCENE"])
		main(100, "BL_RS_PS_014", ["Pass Limit: 100", "NEED SCENE"])
		main(500, "BL_RS_PS_015", ["Pass Limit: 500", "NEED SCENE"])
		main(1000, "BL_RS_PS_016", ["Pass Limit: 1000", "NEED SCENE"])
		main(5000, "BL_RS_PS_017", ["Pass Limit: 5000", "NEED SCENE"])
		main(10000, "BL_RS_PS_018", ["Pass Limit: 10000", "NEED SCENE"])
