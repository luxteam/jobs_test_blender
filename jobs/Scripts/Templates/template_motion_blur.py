
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

	set_value(scene.rpr, 'motion_blur', True)

	bpy.context.scene.rpr.motion_blur_exposure = 1
	bpy.context.scene.rpr.motion_blur_exposure_apply = 'SELECTED'
	bpy.context.scene.rpr.motion_blur_exposure_apply = 'ALL'
	bpy.context.scene.rpr.motion_blur_exposure_apply = 'ACTIVE'

	scene.rpr.motion_blur = True
	scene.rpr.motion_blur_exposure_apply = test_list[3]
	scene.rpr.motion_blur_exposure = test_list[4]
	scene.rpr.motion_blur_scale_apply = test_list[5]
	scene.rpr.motion_blur_scale = test_list[6]

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_MB_001", ["Default"], "MotionBlur.blend", 'ACTIVE', 1, 'SELECTED', 1], 
	["BL_RS_MB_002", ["Exposure: 0"], "MotionBlur.blend", 'ACTIVE', 0, 'SELECTED', 1], 
	["BL_RS_MB_003", ["Exposure: 50"], "MotionBlur.blend", 'ACTIVE', 50, 'SELECTED', 1], 
	["BL_RS_MB_004", ["Exposure: 100"], "MotionBlur.blend", 'ACTIVE', 100, 'SELECTED', 1], 
	["BL_RS_MB_005", ["Scale: 0"], "MotionBlur.blend", 'ACTIVE', 1, 'SELECTED', 0], 
	["BL_RS_MB_006", ["Scale: 50"], "MotionBlur.blend", 'ACTIVE', 1, 'SELECTED', 50], 
	["BL_RS_MB_007", ["Scale: 100"], "MotionBlur.blend", 'ACTIVE', 1, 'SELECTED', 100], 
	["BL_RS_MB_008", ["Exposure: 0", "Scale: 0"], "MotionBlur.blend", 'ACTIVE', 0, 'SELECTED', 0], 
	["BL_RS_MB_009", ["Exposure: 50", "Scale: 50"], "MotionBlur.blend", 'ACTIVE', 50, 'SELECTED', 50], 
	["BL_RS_MB_010", ["Exposure: 100", "Scale: 100"], "MotionBlur.blend", 'ACTIVE', 100, 'SELECTED', 100], 
	["BL_RS_MB_011", ["Exposure: 0",  "Apply Scale: Entire Scene",  "Apply Exposure: Entire Scene"], "MotionBlur.blend", 'ALL', 0, 'ALL', 1], 
	["BL_RS_MB_012", ["Exposure: 50",  "Apply Scale: Entire Scene",  "Apply Exposure: Entire Scene"], "MotionBlur.blend", 'ALL', 50, 'ALL', 1], 
	["BL_RS_MB_013", ["Exposure: 100",  "Apply Scale: Entire Scene",  "Apply Exposure: Entire Scene"], "MotionBlur.blend", 'ALL', 100, 'ALL', 1], 
	["BL_RS_MB_014", ["Scale: 0",  "Apply Scale: Entire Scene",  "Apply Exposure: Entire Scene"], "MotionBlur.blend", 'ALL', 1, 'ALL', 0], 
	["BL_RS_MB_015", ["Scale: 50",  "Apply Scale: Entire Scene",  "Apply Exposure: Entire Scene"], "MotionBlur.blend", 'ALL', 1, 'ALL', 50], 
	["BL_RS_MB_016", ["Scale: 100",  "Apply Scale: Entire Scene",  "Apply Exposure: Entire Scene"], "MotionBlur.blend", 'ALL', 1, 'ALL', 100], 
	["BL_RS_MB_017", ["Exposure: 0", "Scale: 0", "Apply Scale: Entire Scene", "Apply Exposure: Entire Scene"], "MotionBlur.blend", 'ALL', 0, 'ALL', 0], 
	["BL_RS_MB_018", ["Exposure: 50", "Scale: 50", "Apply Scale: Entire Scene", "Apply Exposure: Entire Scene"], "MotionBlur.blend", 'ALL', 50, 'ALL', 50], 
	["BL_RS_MB_019", ["Exposure: 100", "Scale: 100", "Apply Scale: Entire Scene", "Apply Exposure: Entire Scene"], "MotionBlur.blend", 'ALL', 100, 'ALL', 100]
	]

	launch_tests()



