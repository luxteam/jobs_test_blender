
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


def cam_084():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 1)
	set_value(bpy.context.object.data, 'clip_end', 10)


def cam_085():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 1)
	set_value(bpy.context.object.data, 'clip_end', 15)


def cam_086():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 1)
	set_value(bpy.context.object.data, 'clip_end', 30)


def cam_087():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 10)
	set_value(bpy.context.object.data, 'clip_end', 50)


def cam_088():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 15)
	set_value(bpy.context.object.data, 'clip_end', 50)


def cam_089():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data, 'clip_start', 21)
	set_value(bpy.context.object.data, 'clip_end', 50)


def cam_118():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 15)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 0.4)
	set_value(bpy.context.object.data.dof, 'aperture_blades', 0)


def cam_119():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 15)
	set_value(bpy.context.object.data.dof, 'aperture_fstop', 0.4)
	set_value(bpy.context.object.data.dof, 'aperture_blades', 3)


def cam_120():
	set_value(bpy.context.object.data, 'type', 'PERSP')
	set_value(bpy.context.object.data.dof, 'use_dof', True)
	set_value(bpy.context.object.data.dof, 'focus_distance', 15)
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
		["BL_RS_CAM_038", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 128"], "Camera.blend", cam_038],
		["BL_RS_CAM_039", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 128"], "Camera.blend", cam_039], 

		["BL_RS_CAM_040", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 50"], "Camera.blend", cam_040],
		["BL_RS_CAM_041", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 50"], "Camera.blend", cam_041],
		["BL_RS_CAM_042", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 50"], "Camera.blend", cam_042],
		["BL_RS_CAM_043", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 50"], "Camera.blend", cam_043], 

		["BL_RS_CAM_044", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 10"], "Camera.blend", cam_044],
		["BL_RS_CAM_045", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 10"], "Camera.blend", cam_045],
		["BL_RS_CAM_046", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 10"], "Camera.blend", cam_046],
		["BL_RS_CAM_047", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 10"], "Camera.blend", cam_047], 

		["BL_RS_CAM_048", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 0.4"], "Camera.blend", cam_048],
		["BL_RS_CAM_049", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 0.4"], "Camera.blend", cam_049],
		["BL_RS_CAM_050", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 0.4"], "Camera.blend", cam_050],
		["BL_RS_CAM_051", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 0.4"], "Camera.blend", cam_051],

		["BL_RS_CAM_052", ["Perspective camera", "Depth of Field: Activated", "Distance: 6", "Aperture F-stop: 0.4", "Aperture Blades: 0"], "Camera.blend", cam_052],
		["BL_RS_CAM_053", ["Perspective camera", "Depth of Field: Activated", "Distance: 6", "Aperture F-stop: 0.4", "Aperture Blades: 3"], "Camera.blend", cam_053],
		["BL_RS_CAM_054", ["Perspective camera", "Depth of Field: Activated", "Distance: 6", "Aperture F-stop: 0.4", "Aperture Blades: 5"], "Camera.blend", cam_054],

		# Not implemented in plugin
		#["BL_RS_CAM_055", ["Perspective - Spherical"], "Camera.blend", cam_055], 
		#["BL_RS_CAM_056", ["Perspective - Spherical - Use stereo camera"], "Camera.blend", cam_056], 
		#["BL_RS_CAM_057", ["Perspective - Cube map"], "Camera.blend", cam_057], 
		#["BL_RS_CAM_058", ["Perspective - Cube map - Use stereo camera"], "Camera.blend", cam_058], 
		#["BL_RS_CAM_059", ["Orthographic - Spherical"], "Camera.blend", cam_059], 
		#["BL_RS_CAM_060", ["Orthographic - Spherical - Use stereo camera"], "Camera.blend", cam_060], 
		#["BL_RS_CAM_061", ["Orthographic - Cube map"], "Camera.blend", cam_061], 
		#["BL_RS_CAM_062", ["Orthographic - Cube map - Use stereo camera"], "Camera.blend", cam_062], 
		#["BL_RS_CAM_063", ["Panoramic - Spherical"], "Camera.blend", cam_063], 
		#["BL_RS_CAM_064", ["Panoramic - Spherical - Use stereo camera"], "Camera.blend", cam_064], 
		#["BL_RS_CAM_065", ["Panoramic - Cube map"], "Camera.blend", cam_065], 
		#["BL_RS_CAM_066", ["Panoramic - Cube map - Use stereo camera"], "Camera.blend", cam_066], 

		["BL_RS_CAM_067", ["Perspective camera"], "medium.blend", cam_001], 
		["BL_RS_CAM_068", ["Orthographic camera"], "medium.blend", cam_002], 
		["BL_RS_CAM_069", ["Panoramic camera"], "medium.blend", cam_003], 

		["BL_RS_CAM_070", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 10"], "medium.blend", cam_004], 
		["BL_RS_CAM_071", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 25"], "medium.blend", cam_005], 
		["BL_RS_CAM_072", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 50"], "medium.blend", cam_006], 
		["BL_RS_CAM_073", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 80"], "medium.blend", cam_007], 
		["BL_RS_CAM_074", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 120"], "medium.blend", cam_008], 

		["BL_RS_CAM_075", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 10°"], "medium.blend", cam_009], 
		["BL_RS_CAM_076", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 25°"], "medium.blend", cam_010], 
		["BL_RS_CAM_077", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 50°"], "medium.blend", cam_011], 
		["BL_RS_CAM_078", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 80°"], "medium.blend", cam_012], 
		["BL_RS_CAM_079", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 120°"], "medium.blend", cam_013], 

		["BL_RS_CAM_080", ["Perspective camera", "Shift X: 0.1"], "medium.blend", cam_014], 
		["BL_RS_CAM_081", ["Perspective camera", "Shift X: -0.1"], "medium.blend", cam_015], 
		["BL_RS_CAM_082", ["Perspective camera", "Shift Y: 0.1"], "medium.blend", cam_016], 
		["BL_RS_CAM_083", ["Perspective camera", "Shift Y: -0.1"], "medium.blend", cam_017], 

		["BL_RS_CAM_084", ["Perspective camera", "Clip start: 1", "Clip end: 10"], "medium.blend", cam_084], 
		["BL_RS_CAM_085", ["Perspective camera", "Clip start: 1", "Clip end: 15"], "medium.blend", cam_085], 
		["BL_RS_CAM_086", ["Perspective camera", "Clip start: 1", "Clip end: 30"], "medium.blend", cam_086], 
		["BL_RS_CAM_087", ["Perspective camera", "Clip start: 10", "Clip end: 50"], "medium.blend", cam_087], 
		["BL_RS_CAM_088", ["Perspective camera", "Clip start: 15", "Clip end: 50"], "medium.blend", cam_088], 
		["BL_RS_CAM_089", ["Perspective camera", "Clip start: 21", "Clip end: 50"], "medium.blend", cam_089], 

		["BL_RS_CAM_090", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 1"], "medium.blend", cam_024], 
		["BL_RS_CAM_091", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 10"], "medium.blend", cam_025], 
		["BL_RS_CAM_092", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 50"], "medium.blend", cam_026], 
		["BL_RS_CAM_093", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 100"], "medium.blend", cam_027], 

		["BL_RS_CAM_094", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 1"], "medium.blend", cam_028], 
		["BL_RS_CAM_095", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 10"], "medium.blend", cam_029], 
		["BL_RS_CAM_096", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 50"], "medium.blend", cam_030], 
		["BL_RS_CAM_097", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 100"], "medium.blend", cam_031], 

		["BL_RS_CAM_098", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 1"], "medium.blend", cam_032], 
		["BL_RS_CAM_099", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 10"], "medium.blend", cam_033], 
		["BL_RS_CAM_100", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 50"], "medium.blend", cam_034], 
		["BL_RS_CAM_101", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 100"], "medium.blend", cam_035], 

		["BL_RS_CAM_102", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 128"], "medium.blend", cam_036],
		["BL_RS_CAM_103", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 128"], "medium.blend", cam_037],
		["BL_RS_CAM_104", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 128"], "medium.blend", cam_038],
		["BL_RS_CAM_105", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 128"], "medium.blend", cam_039], 

		["BL_RS_CAM_106", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 50"], "medium.blend", cam_040],
		["BL_RS_CAM_107", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 50"], "medium.blend", cam_041],
		["BL_RS_CAM_108", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 50"], "medium.blend", cam_042],
		["BL_RS_CAM_109", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 50"], "medium.blend", cam_043], 

		["BL_RS_CAM_110", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 10"], "medium.blend", cam_044],
		["BL_RS_CAM_111", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 10"], "medium.blend", cam_045],
		["BL_RS_CAM_112", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 10"], "medium.blend", cam_046],
		["BL_RS_CAM_113", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 10"], "medium.blend", cam_047], 

		["BL_RS_CAM_114", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 0.4"], "medium.blend", cam_048],
		["BL_RS_CAM_115", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 0.4"], "medium.blend", cam_049],
		["BL_RS_CAM_116", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 0.4"], "medium.blend", cam_050],
		["BL_RS_CAM_117", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 0.4"], "medium.blend", cam_051],

		["BL_RS_CAM_118", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 0.4", "Aperture Blades: 0"], "medium.blend", cam_118],
		["BL_RS_CAM_119", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 0.4", "Aperture Blades: 3"], "medium.blend", cam_119],
		["BL_RS_CAM_120", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 0.4", "Aperture Blades: 5"], "medium.blend", cam_120],

		# Not implemented in plugin
		#["BL_RS_CAM_121", ["Perspective - Spherical"], "medium.blend", cam_055], 
		#["BL_RS_CAM_122", ["Perspective - Spherical - Use stereo camera"], "medium.blend", cam_056], 
		#["BL_RS_CAM_123", ["Perspective - Cube map"], "medium.blend", cam_057], 
		#["BL_RS_CAM_124", ["Perspective - Cube map - Use stereo camera"], "medium.blend", cam_058], 
		#["BL_RS_CAM_125", ["Orthographic - Spherical"], "medium.blend", cam_059], 
		#["BL_RS_CAM_126", ["Orthographic - Spherical - Use stereo camera"], "medium.blend", cam_060], 
		#["BL_RS_CAM_127", ["Orthographic - Cube map"], "medium.blend", cam_061], 
		#["BL_RS_CAM_128", ["Orthographic - Cube map - Use stereo camera"], "medium.blend", cam_062], 
		#["BL_RS_CAM_129", ["Panoramic - Spherical"], "medium.blend", cam_063], 
		#["BL_RS_CAM_130", ["Panoramic - Spherical - Use stereo camera"], "medium.blend", cam_064], 
		#["BL_RS_CAM_131", ["Panoramic - Cube map"], "medium.blend", cam_065], 
		#["BL_RS_CAM_132", ["Panoramic - Cube map - Use stereo camera"], "medium.blend", cam_066], 

		["BL_RS_CAM_133", ["Perspective camera"], "hard.blend", cam_001], 
		["BL_RS_CAM_134", ["Orthographic camera"], "hard.blend", cam_002], 
		["BL_RS_CAM_135", ["Panoramic camera"], "hard.blend", cam_003], 

		["BL_RS_CAM_0136", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 10"], "hard.blend", cam_004], 
		["BL_RS_CAM_0137", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 25"], "hard.blend", cam_005], 
		["BL_RS_CAM_0138", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 50"], "hard.blend", cam_006], 
		["BL_RS_CAM_0139", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 80"], "hard.blend", cam_007], 
		["BL_RS_CAM_0140", ["Perspective camera", "Lens Unit: Millimeters", "Focal Length: 120"], "hard.blend", cam_008], 

		["BL_RS_CAM_141", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 10°"], "hard.blend", cam_009], 
		["BL_RS_CAM_142", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 25°"], "hard.blend", cam_010], 
		["BL_RS_CAM_143", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 50°"], "hard.blend", cam_011], 
		["BL_RS_CAM_144", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 80°"], "hard.blend", cam_012], 
		["BL_RS_CAM_145", ["Perspective camera", "Lens Unit: Field of View", "Field of View: 120°"], "hard.blend", cam_013], 

		["BL_RS_CAM_146", ["Perspective camera", "Shift X: 0.1"], "medium.blend", cam_014], 
		["BL_RS_CAM_147", ["Perspective camera", "Shift X: -0.1"], "medium.blend", cam_015], 
		["BL_RS_CAM_148", ["Perspective camera", "Shift Y: 0.1"], "medium.blend", cam_016], 
		["BL_RS_CAM_149", ["Perspective camera", "Shift Y: -0.1"], "medium.blend", cam_017], 

		["BL_RS_CAM_150", ["Perspective camera", "Clip start: 1", "Clip end: 0.7"], "Camera.blend", cam_018], 
		["BL_RS_CAM_151", ["Perspective camera", "Clip start: 1", "Clip end: 1.2"], "Camera.blend", cam_019], 
		["BL_RS_CAM_152", ["Perspective camera", "Clip start: 1", "Clip end: 5"], "Camera.blend", cam_020], 
		["BL_RS_CAM_153", ["Perspective camera", "Clip start: 7.4", "Clip end: 50"], "Camera.blend", cam_021], 
		["BL_RS_CAM_154", ["Perspective camera", "Clip start: 8", "Clip end: 50"], "Camera.blend", cam_022], 
		["BL_RS_CAM_155", ["Perspective camera", "Clip start: 9.5", "Clip end: 50"], "Camera.blend", cam_023], 

		["BL_RS_CAM_156", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 1"], "medium.blend", cam_024], 
		["BL_RS_CAM_157", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 10"], "medium.blend", cam_025], 
		["BL_RS_CAM_158", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 50"], "medium.blend", cam_026], 
		["BL_RS_CAM_159", ["Perspective camera", "Sensor fit: Auto", "Sensor size: 100"], "medium.blend", cam_027], 

		["BL_RS_CAM_160", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 1"], "medium.blend", cam_028], 
		["BL_RS_CAM_161", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 10"], "medium.blend", cam_029], 
		["BL_RS_CAM_162", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 50"], "medium.blend", cam_030], 
		["BL_RS_CAM_163", ["Perspective camera", "Sensor fit: Horizontal", "Sensor width: 100"], "medium.blend", cam_031], 

		["BL_RS_CAM_164", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 1"], "medium.blend", cam_032], 
		["BL_RS_CAM_165", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 10"], "medium.blend", cam_033], 
		["BL_RS_CAM_166", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 50"], "medium.blend", cam_034], 
		["BL_RS_CAM_167", ["Perspective camera", "Sensor fit: Vertical", "Sensor height: 100"], "medium.blend", cam_035], 

		["BL_RS_CAM_168", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 128"], "Camera.blend", cam_036],
		["BL_RS_CAM_169", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 128"], "Camera.blend", cam_037],
		["BL_RS_CAM_170", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 128"], "Camera.blend", cam_038],
		["BL_RS_CAM_171", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 128"], "Camera.blend", cam_039], 

		["BL_RS_CAM_172", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 50"], "Camera.blend", cam_040],
		["BL_RS_CAM_173", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 50"], "Camera.blend", cam_041],
		["BL_RS_CAM_174", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 50"], "Camera.blend", cam_042],
		["BL_RS_CAM_175", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 50"], "Camera.blend", cam_043], 

		["BL_RS_CAM_176", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 10"], "Camera.blend", cam_044],
		["BL_RS_CAM_177", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 10"], "Camera.blend", cam_045],
		["BL_RS_CAM_178", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 10"], "Camera.blend", cam_046],
		["BL_RS_CAM_179", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 10"], "Camera.blend", cam_047], 

		["BL_RS_CAM_180", ["Perspective camera", "Depth of Field: Activated", "Distance: 0.01", "Aperture F-stop: 0.4"], "Camera.blend", cam_048],
		["BL_RS_CAM_181", ["Perspective camera", "Depth of Field: Activated", "Distance: 1", "Aperture F-stop: 0.4"], "Camera.blend", cam_049],
		["BL_RS_CAM_182", ["Perspective camera", "Depth of Field: Activated", "Distance: 8", "Aperture F-stop: 0.4"], "Camera.blend", cam_050],
		["BL_RS_CAM_183", ["Perspective camera", "Depth of Field: Activated", "Distance: 15", "Aperture F-stop: 0.4"], "Camera.blend", cam_051],

		["BL_RS_CAM_184", ["Perspective camera", "Depth of Field: Activated", "Distance: 6", "Aperture F-stop: 0.4", "Aperture Blades: 0"], "Camera.blend", cam_052],
		["BL_RS_CAM_185", ["Perspective camera", "Depth of Field: Activated", "Distance: 6", "Aperture F-stop: 0.4", "Aperture Blades: 3"], "Camera.blend", cam_053],
		["BL_RS_CAM_186", ["Perspective camera", "Depth of Field: Activated", "Distance: 6", "Aperture F-stop: 0.4", "Aperture Blades: 5"], "Camera.blend", cam_054],

		# Not implemented in plugin
		#["BL_RS_CAM_187", ["Perspective - Spherical"], "Camera.blend", cam_055], 
		#["BL_RS_CAM_188", ["Perspective - Spherical - Use stereo camera"], "Camera.blend", cam_056], 
		#["BL_RS_CAM_189", ["Perspective - Cube map"], "Camera.blend", cam_057], 
		#["BL_RS_CAM_190", ["Perspective - Cube map - Use stereo camera"], "Camera.blend", cam_058], 
		#["BL_RS_CAM_191", ["Orthographic - Spherical"], "Camera.blend", cam_059], 
		#["BL_RS_CAM_192", ["Orthographic - Spherical - Use stereo camera"], "Camera.blend", cam_060], 
		#["BL_RS_CAM_193", ["Orthographic - Cube map"], "Camera.blend", cam_061], 
		#["BL_RS_CAM_194", ["Orthographic - Cube map - Use stereo camera"], "Camera.blend", cam_062], 
		#["BL_RS_CAM_195", ["Panoramic - Spherical"], "Camera.blend", cam_063], 
		#["BL_RS_CAM_196", ["Panoramic - Spherical - Use stereo camera"], "Camera.blend", cam_064], 
		#["BL_RS_CAM_197", ["Panoramic - Cube map"], "Camera.blend", cam_065], 
		#["BL_RS_CAM_198", ["Panoramic - Cube map - Use stereo camera"], "Camera.blend", cam_066], 

	]
	
	launch_tests()





