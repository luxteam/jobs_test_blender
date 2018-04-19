
def main(render_mode, test_case, script_info):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.rpr.render.render_mode = render_mode

	render(test_case, script_info)

if __name__ == "__main__":

	main('WIREFRAME', "BL_RS_RM_001", ["Render mode: Wireframe"])
	main('TEXCOORD', "BL_RS_RM_002", ["Render mode: Texcoord"])
	main('POSITION', "BL_RS_RM_003", ["Render mode: Position"])
	main('NORMAL', "BL_RS_RM_004", ["Render mode: Normal"])
	main('MATERIAL_INDEX', "BL_RS_RM_005", ["Render mode: Material_index"])
	main('GLOBAL_ILLUMINATION', "BL_RS_RM_006", ["Render mode: Global illumination"])
	main('DIRECT_ILLUMINATION_NO_SHADOW', "BL_RS_RM_007", ["Render mode: Direct illumination no shadow"])
	main('DIRECT_ILLUMINATION', "BL_RS_RM_008", ["Render mode: Direct illumination"])
	main('DIFFUSE', "BL_RS_RM_009", ["Render mode: Diffuse"])
	main('AMBIENT_OCCLUSION', "BL_RS_RM_010", ["Render mode: Ambient occlusion"])

