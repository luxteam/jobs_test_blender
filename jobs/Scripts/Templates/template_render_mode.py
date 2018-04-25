
def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.rpr.render.render_mode = test_list[2]

	render(test_list[0], test_list[1])

if __name__ == "__main__":

	list_tests = [
	["BL_RS_RM_001", ["Render mode: Wireframe"], 'WIREFRAME'], 
	["BL_RS_RM_002", ["Render mode: Texcoord"], 'TEXCOORD'],
	["BL_RS_RM_003", ["Render mode: Position"], 'POSITION'], 
	["BL_RS_RM_004", ["Render mode: Normal"], 'NORMAL'], 
	["BL_RS_RM_005", ["Render mode: Material index"], 'MATERIAL_INDEX'], 
	["BL_RS_RM_006", ["Render mode: Global illumination"], 'GLOBAL_ILLUMINATION'],
	["BL_RS_RM_007", ["Render mode: Direct illumination no shadow"], 'DIRECT_ILLUMINATION_NO_SHADOW'],
	["BL_RS_RM_008", ["Render mode: Direct illumination"], 'DIRECT_ILLUMINATION'], 
	["BL_RS_RM_009", ["Render mode: Diffuse"], 'DIFFUSE'],
	["BL_RS_RM_010", ["Render mode: Ambient occlusion"], 'AMBIENT_OCCLUSION']
	]
	
	launch_tests()

