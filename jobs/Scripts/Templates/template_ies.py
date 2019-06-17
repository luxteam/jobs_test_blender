
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	lamp_data = bpy.data.lights['Lamp']
	set_value(lamp_data.rpr, 'intensity', 50)
	set_value(lamp_data.rpr, 'ies_file_name', os.path.join(r"{resource_path}", "ies", test_list[3]))

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":
	
	list_tests = [
		["BL28_L_IES_001", ["IES file: 1.ies", "Intensity: 50"], "IES.blend", "1.ies"], 
		["BL28_L_IES_002", ["IES file: 2.ies", "Intensity: 50"], "IES.blend", "2.ies"],
		["BL28_L_IES_003", ["IES file: 3.ies", "Intensity: 50"], "IES.blend", "3.ies"], 
		["BL28_L_IES_004", ["IES file: 4.ies", "Intensity: 50"], "IES.blend", "4.ies"], 
		["BL28_L_IES_005", ["IES file: 5.ies", "Intensity: 50"], "IES.blend", "5.ies"], 
		["BL28_L_IES_006", ["IES file: 6.ies", "Intensity: 50"], "IES.blend", "6.ies"],
		["BL28_L_IES_007", ["IES file: 7.ies", "Intensity: 50"], "IES.blend", "7.ies"], 
		["BL28_L_IES_008", ["IES file: 8.ies", "Intensity: 50"], "IES.blend", "8.ies"], 
		["BL28_L_IES_009", ["IES file: 9.ies", "Intensity: 50"], "IES.blend", "9.ies"], 
		["BL28_L_IES_010", ["IES file: 10.ies", "Intensity: 50"], "IES.blend", "10.ies"]
	]
	
	launch_tests()


