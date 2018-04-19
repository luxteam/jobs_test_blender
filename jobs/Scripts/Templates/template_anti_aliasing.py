
def main(filter_aa, value, test_case, script_info):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.data.scenes[Scenename].rpr.render.aa.filter = filter_aa
	bpy.data.scenes[Scenename].rpr.render.aa.radius = value

	render(test_case)

if __name__ == "__main__":

	main('MITCHELL', 0, "BL_RS_AA_001", ["AA filter: Mitchell", "Radius: 0"])
	main('MITCHELL', 1, "BL_RS_AA_002", ["AA filter: Mitchell", "Radius: 1"])
	main('MITCHELL', 5, "BL_RS_AA_003", ["AA filter: Mitchell", "Radius: 5"])
	main('MITCHELL', 10, "BL_RS_AA_004", ["AA filter: Mitchell", "Radius: 10"])

	main('LANCZOS', 0, "BL_RS_AA_005", ["AA filter: Lanczos", "Radius: 0"])
	main('LANCZOS', 1, "BL_RS_AA_006", ["AA filter: Lanczos", "Radius: 1"])
	main('LANCZOS', 5, "BL_RS_AA_007", ["AA filter: Lanczos", "Radius: 5"])
	main('LANCZOS', 10, "BL_RS_AA_008", ["AA filter: Lanczos", "Radius: 10"])

	main('TRIANGLE', 0, "BL_RS_AA_009", ["AA filter: Triangle", "Radius: 0"])
	main('TRIANGLE', 1, "BL_RS_AA_010", ["AA filter: Triangle", "Radius: 1"])
	main('TRIANGLE', 5, "BL_RS_AA_011", ["AA filter: Triangle", "Radius: 5"])
	main('TRIANGLE', 10, "BL_RS_AA_012", ["AA filter: Triangle", "Radius: 10"])

	main('BOX', 0, "BL_RS_AA_013", ["AA filter: Box", "Radius: 0"])
	main('BOX', 1, "BL_RS_AA_014", ["AA filter: Box", "Radius: 1"])
	main('BOX', 5, "BL_RS_AA_015", ["AA filter: Box", "Radius: 5"])
	main('BOX', 10, "BL_RS_AA_016", ["AA filter: Box", "Radius: 10"])

	main('GAUSSIAN', 0, "BL_RS_AA_017", ["AA filter: Gaussian", "Radius: 0"])
	main('GAUSSIAN', 1, "BL_RS_AA_018", ["AA filter: Gaussian", "Radius: 1"])
	main('GAUSSIAN', 5, "BL_RS_AA_019", ["AA filter: Gaussian", "Radius: 5"])
	main('GAUSSIAN', 10, "BL_RS_AA_020", ["AA filter: Gaussian", "Radius: 10"])

	main('BLACKMANHARRIS', 0, "BL_RS_AA_021", ["AA filter: Blackmanharris", "Radius: 0"])
	main('BLACKMANHARRIS', 1, "BL_RS_AA_022", ["AA filter: Blackmanharris", "Radius: 1"])
	main('BLACKMANHARRIS', 5, "BL_RS_AA_023", ["AA filter: Blackmanharris", "Radius: 5"])
	main('BLACKMANHARRIS', 10, "BL_RS_AA_024", ["AA filter: Blackmanharris", "Radius: 10"])


