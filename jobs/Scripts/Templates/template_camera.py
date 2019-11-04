
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
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens', 53.93)
	set_value(bpy.context.object.data, 'lens_unit', 'MILLIMETERS')

	set_value(bpy.context.object.data, 'shift_x', 0)
	set_value(bpy.context.object.data, 'shift_y', 0)
	set_value(bpy.context.object.data, 'clip_start', 0.1)
	set_value(bpy.context.object.data, 'clip_end', 100)

	set_value(bpy.context.object.data, 'sensor_fit', 'AUTO')
	set_value(bpy.context.object.data, 'sensor_width', 32)

	set_value(bpy.context.object.data.dof, 'use_dof', False)
	set_value(bpy.context.object.data.dof, 'focus_distance', 0)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 128)
	set_value(bpy.context.object.data.dof, 'aperture_blades', 0)


def cam_001():
	set_value(bpy.context.object.data, 'type', 'PERSP')


def cam_002():
	set_value(bpy.context.object.data, 'type', 'ORTHO')


def cam_003():
	set_value(bpy.context.object.data, 'type', 'PANO')


def cam_004():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'MILLIMETERS')
	set_value(bpy.context.object.data, 'lens', 10)


def cam_005():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'MILLIMETERS')
	set_value(bpy.context.object.data, 'lens', 25)
	

def cam_006():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'MILLIMETERS')
	set_value(bpy.context.object.data, 'lens', 50)
	

def cam_007():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'MILLIMETERS')
	set_value(bpy.context.object.data, 'lens', 80)
	

def cam_008():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'MILLIMETERS')
	set_value(bpy.context.object.data, 'lens', 120)
	

def cam_009():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'FOV')
	set_value(bpy.context.object.data, 'angle', 0.174533)


def cam_010():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'FOV')
	set_value(bpy.context.object.data, 'angle', 0.436332)


def cam_011():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'FOV')
	set_value(bpy.context.object.data, 'angle', 0.872665)


def cam_012():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'FOV')
	set_value(bpy.context.object.data, 'angle', 1.39626)


def cam_013():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'lens_unit', 'FOV')
	set_value(bpy.context.object.data, 'angle', 2.0944)
	

def cam_014():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'shift_x', 0.1)
	set_value(bpy.context.object.data, 'shift_y', 0)


def cam_015():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'shift_x', -0.1)
	set_value(bpy.context.object.data, 'shift_y', 0)


def cam_016():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'shift_x', 0)
	set_value(bpy.context.object.data, 'shift_y', 0.1)


def cam_017():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'shift_x', 0)
	set_value(bpy.context.object.data, 'shift_y', -0.1)


def cam_018():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 1)
	set_value(bpy.context.object.data, 'clip_end', 0.7)


def cam_019():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 1)
	set_value(bpy.context.object.data, 'clip_end', 1.2)


def cam_020():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 1)
	set_value(bpy.context.object.data, 'clip_end', 5)


def cam_021():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 7.4)
	set_value(bpy.context.object.data, 'clip_end', 50)


def cam_022():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 8)
	set_value(bpy.context.object.data, 'clip_end', 50)


def cam_023():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 9.5)
	set_value(bpy.context.object.data, 'clip_end', 50)


def cam_023():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 9.5)
	set_value(bpy.context.object.data, 'clip_end', 50)


def cam_024():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'AUTO')
	set_value(bpy.context.object.data, 'sensor_width', 1)


def cam_025():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'AUTO')
	set_value(bpy.context.object.data, 'sensor_width', 10)


def cam_026():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'AUTO')
	set_value(bpy.context.object.data, 'sensor_width', 50)


def cam_027():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'AUTO')
	set_value(bpy.context.object.data, 'sensor_width', 100)


def cam_024():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'AUTO')
	set_value(bpy.context.object.data, 'sensor_width', 1)


def cam_025():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'AUTO')
	set_value(bpy.context.object.data, 'sensor_width', 10)


def cam_026():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'AUTO')
	set_value(bpy.context.object.data, 'sensor_width', 50)


def cam_027():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'AUTO')
	set_value(bpy.context.object.data, 'sensor_width', 100)


def cam_028():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'HORIZONTAL')
	set_value(bpy.context.object.data, 'sensor_width', 1)


def cam_029():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'HORIZONTAL')
	set_value(bpy.context.object.data, 'sensor_width', 10)


def cam_030():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'HORIZONTAL')
	set_value(bpy.context.object.data, 'sensor_width', 50)


def cam_031():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'HORIZONTAL')
	set_value(bpy.context.object.data, 'sensor_width', 100)


def cam_032():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'VERTICAL')
	set_value(bpy.context.object.data, 'sensor_height', 1)


def cam_033():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'VERTICAL')
	set_value(bpy.context.object.data, 'sensor_height', 10)


def cam_034():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'VERTICAL')
	set_value(bpy.context.object.data, 'sensor_height', 50)


def cam_035():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'sensor_fit', 'VERTICAL')
	set_value(bpy.context.object.data, 'sensor_height', 100)


def cam_036():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 0.01)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 128)


def cam_037():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 1)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 128)


def cam_038():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 8)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 128)


def cam_039():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 15)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 128)


def cam_040():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 0.01)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 50)


def cam_041():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 1)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 50)


def cam_042():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 8)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 50)


def cam_043():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 15)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 50)


def cam_044():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 0.01)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 10)


def cam_045():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 1)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 10)


def cam_046():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 8)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 10)


def cam_047():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 15)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 10)


def cam_048():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 0.01)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 0.4)


def cam_049():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 1)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 0.4)


def cam_050():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 8)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 0.4)


def cam_051():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 15)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 0.4)


def cam_052():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 6)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 0.4)
	set_value(bpy.context.object.data.dof, 'aperture_blades', 0)


def cam_053():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 6)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 0.4)
	set_value(bpy.context.object.data.dof, 'aperture_blades', 3)


def cam_054():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 6)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 0.4)
	set_value(bpy.context.object.data.dof, 'aperture_blades', 5)


if __name__ == "__main__":

	list_tests = [
	
		["BL_RS_CAM_001", ["Perspective camera"], "Camera.blend", cam_001], 
		["BL_RS_CAM_002", ["Orthographic camera"], "Camera.blend", cam_002], 
		["BL_RS_CAM_003", ["Panoramic camera"], "Camera.blend", cam_003], 

		["BL_RS_CAM_004", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 10"], "Camera.blend", cam_004], 
		["BL_RS_CAM_005", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 25"], "Camera.blend", cam_005], 
		["BL_RS_CAM_006", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 50"], "Camera.blend", cam_006], 
		["BL_RS_CAM_007", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 80"], "Camera.blend", cam_007], 
		["BL_RS_CAM_008", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 120"], "Camera.blend", cam_008], 

		["BL_RS_CAM_009", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 10°"], "Camera.blend", cam_009], 
		["BL_RS_CAM_010", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 25°"], "Camera.blend", cam_010], 
		["BL_RS_CAM_011", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 50°"], "Camera.blend", cam_011], 
		["BL_RS_CAM_012", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 80°"], "Camera.blend", cam_012], 
		["BL_RS_CAM_013", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 120°"], "Camera.blend", cam_013], 

		["BL_RS_CAM_014", ["Perspective camera", "Shift X: 0.1"], "Camera.blend", cam_014], 
		["BL_RS_CAM_015", ["Perspective camera", "Shift X: -0.1"], "Camera.blend", cam_015], 
		["BL_RS_CAM_016", ["Perspective camera", "Shift Y: 0.1"], "Camera.blend", cam_016], 
		["BL_RS_CAM_017", ["Perspective camera", "Shift Y: -0.1"], "Camera.blend", cam_017], 

		["BL_RS_CAM_018", ["Perspective camera", "Clip start: 1", "Clip end: 0.7"], "Camera.blend", cam_018], 
		["BL_RS_CAM_019", ["Perspective camera", "Clip start: 1", "Clip end: 1.2"], "Camera.blend", cam_019], 
		["BL_RS_CAM_020", ["Perspective camera", "Clip start: 1", "Clip end: 5"], "Camera.blend", cam_020], 
		["BL_RS_CAM_021", ["Perspective camera", "Clip start: 7.4", "Clip end: 50"], "Camera.blend", cam_021], 
		["BL_RS_CAM_022", ["Perspective camera", "Clip start: 8", "Clip end: 50"], "Camera.blend", cam_022], 
		["BL_RS_CAM_023", ["Perspective camera", "Clip start: 9.5", "Clip end: 50"], "Camera.blend", cam_023], 

		["BL_RS_CAM_024", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 1"], "Camera.blend", cam_024], 
		["BL_RS_CAM_025", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 10"], "Camera.blend", cam_025], 
		["BL_RS_CAM_026", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 50"], "Camera.blend", cam_026], 
		["BL_RS_CAM_027", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 100"], "Camera.blend", cam_027], 

		["BL_RS_CAM_028", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 1"], "Camera.blend", cam_028], 
		["BL_RS_CAM_029", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 10"], "Camera.blend", cam_029], 
		["BL_RS_CAM_030", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 50"], "Camera.blend", cam_030], 
		["BL_RS_CAM_031", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 100"], "Camera.blend", cam_031], 

		["BL_RS_CAM_032", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 1"], "Camera.blend", cam_032], 
		["BL_RS_CAM_033", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 10"], "Camera.blend", cam_033], 
		["BL_RS_CAM_034", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 50"], "Camera.blend", cam_034], 
		["BL_RS_CAM_035", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 100"], "Camera.blend", cam_035], 

		["BL_RS_CAM_036", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 128"], "Camera.blend", cam_036],
		["BL_RS_CAM_037", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 128"], "Camera.blend", cam_037],
		["BL_RS_CAM_038", ["Perspective camera", "Depth of Field: Activated", "Distance: 5", "Aperture F-stop: 128"], "Camera.blend", cam_038],
		["BL_RS_CAM_039", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 128"], "Camera.blend", cam_039], 

		["BL_RS_CAM_040", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 50"], "Camera.blend", cam_040],
		["BL_RS_CAM_041", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 50"], "Camera.blend", cam_041],
		["BL_RS_CAM_042", ["Perspective camera", "Depth of Field: Activated", "Distance: 5", "Aperture F-stop: 50"], "Camera.blend", cam_042],
		["BL_RS_CAM_043", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 50"], "Camera.blend", cam_043], 

		["BL_RS_CAM_044", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 10"], "Camera.blend", cam_044],
		["BL_RS_CAM_045", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 10"], "Camera.blend", cam_045],
		["BL_RS_CAM_046", ["Perspective camera", "Depth of Field: Activated", "Distance: 5", "Aperture F-stop: 10"], "Camera.blend", cam_046],
		["BL_RS_CAM_047", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 10"], "Camera.blend", cam_047], 

		["BL_RS_CAM_048", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 0.4"], "Camera.blend", cam_048],
		["BL_RS_CAM_049", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 0.4"], "Camera.blend", cam_049],
		["BL_RS_CAM_050", ["Perspective camera", "Depth of Field: Activated", "Distance: 5", "Aperture F-stop: 0.4"], "Camera.blend", cam_050],
		["BL_RS_CAM_051", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 0.4"], "Camera.blend", cam_051],

		["BL_RS_CAM_052", ["Perspective camera", "Depth of Field: Activated", "Distance: 6", "Aperture F-stop: 0.4", "Aperture Blades: 0"], "Camera.blend", cam_052],
		["BL_RS_CAM_053", ["Perspective camera", "Depth of Field: Activated", "Distance: 6", "Aperture F-stop: 0.4", "Aperture Blades: 3"], "Camera.blend", cam_053],
		["BL_RS_CAM_054", ["Perspective camera", "Depth of Field: Activated", "Distance: 6", "Aperture F-stop: 0.4", "Aperture Blades: 5"], "Camera.blend", cam_054]

	]
	
	launch_tests()





