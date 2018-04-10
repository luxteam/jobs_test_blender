
def main(filter_aa, value, test_case):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.data.scenes[Scenename].rpr.render.aa.filter = filter_aa
	bpy.data.scenes[Scenename].rpr.render.aa.radius = value

	render(test_case)

if __name__ == "__main__":

	main('MITCHELL', 0, "BL_RS_AA_001")
	main('MITCHELL', 1, "BL_RS_AA_002")
	main('MITCHELL', 5, "BL_RS_AA_003")
	main('MITCHELL', 10, "BL_RS_AA_004")

	main('LANCZOS', 0, "BL_RS_AA_005")
	main('LANCZOS', 1, "BL_RS_AA_006")
	main('LANCZOS', 5, "BL_RS_AA_007")
	main('LANCZOS', 10, "BL_RS_AA_008")

	main('TRIANGLE', 0, "BL_RS_AA_009")
	main('TRIANGLE', 1, "BL_RS_AA_010")
	main('TRIANGLE', 5, "BL_RS_AA_011")
	main('TRIANGLE', 10, "BL_RS_AA_012")

	main('BOX', 0, "BL_RS_AA_013")
	main('BOX', 1, "BL_RS_AA_014")
	main('BOX', 5, "BL_RS_AA_015")
	main('BOX', 10, "BL_RS_AA_016")

	main('GAUSSIAN', 0, "BL_RS_AA_017")
	main('GAUSSIAN', 1, "BL_RS_AA_018")
	main('GAUSSIAN', 5, "BL_RS_AA_019")
	main('GAUSSIAN', 10, "BL_RS_AA_020")

	main('BLACKMANHARRIS', 0, "BL_RS_AA_021")
	main('BLACKMANHARRIS', 1, "BL_RS_AA_022")
	main('BLACKMANHARRIS', 5, "BL_RS_AA_023")
	main('BLACKMANHARRIS', 10, "BL_RS_AA_024")


