
def prerender(test_list):

	bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	test_list[3]()
	render(test_list[0], test_list[1])

	return 1


def ss_001():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0)


def ss_002():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.785398)


def ss_003():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 1.5708)


def ss_004():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 1.5708)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0)


def ss_005():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 1.5708)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.785398)


def ss_006():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 1.5708)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 1.5708)


def ss_007():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 3.14159)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0)


def ss_008():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 3.14159)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.785398)


def ss_009():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 3.14159)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 1.5708)


def ss_010():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 4.71239)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0)


def ss_011():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 4.71239)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.785398)


def ss_012():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 4.71239)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 1.5708)


def ss_013():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 6.28319)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0)


def ss_014():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 6.28319)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.785398)


def ss_015():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 6.28319)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 1.5708)


def ss_016():
	set_value(bpy.context.scene.world.rpr.sun_sky, "resolution", '256')


def ss_017():
	set_value(bpy.context.scene.world.rpr.sun_sky, "resolution", '1024')


def ss_018():
	set_value(bpy.context.scene.world.rpr.sun_sky, "resolution", '4096')


def ss_019():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)


def ss_020():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 1)


def ss_021():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 2)


def ss_022():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 5)


def ss_023():
	set_value(bpy.context.scene.world.rpr, "intensity", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)


def ss_024():
	set_value(bpy.context.scene.world.rpr, "intensity", 2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)


def ss_025():
	set_value(bpy.context.scene.world.rpr, "intensity", 5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)


def ss_026():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)


def ss_027():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 2)


def ss_028():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 5)


def ss_029():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)


def ss_030():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 1)


def ss_031():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 2)


def ss_032():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0)


def ss_033():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0.5)


def ss_034():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 1)


def ss_035():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_height", -0.5)


def ss_036():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_height", 0)


def ss_037():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_height", 0.5)


def ss_038():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_height", 0)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_blur", 0.1)


def ss_039():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_height", 0)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_blur", 0.5)


def ss_040():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_height", 0)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_blur", 1)


def ss_041():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_height", 0)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_blur", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "filter_color", (1, 0, 1))


def ss_042():
	set_value(bpy.context.scene.world.rpr.sun_sky, "azimuth", 0.318348)
	set_value(bpy.context.scene.world.rpr.sun_sky, "altitude", 0.0872665)
	set_value(bpy.context.scene.world.rpr.sun_sky, "turbidity", 0.2)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_glow", 1)
	set_value(bpy.context.scene.world.rpr.sun_sky, "sun_disc", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "saturation", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_height", 0)
	set_value(bpy.context.scene.world.rpr.sun_sky, "horizon_blur", 0.5)
	set_value(bpy.context.scene.world.rpr.sun_sky, "filter_color", (1, 0, 1))
	set_value(bpy.context.scene.world.rpr.sun_sky, "ground_color", (0, 1, 0))


if __name__ == "__main__":

	list_tests = [

		["BL28_RS_SS_001", ["Azimuth: 0", "Altitude: 0"], "TestSunSky.blend", ss_001],
		["BL28_RS_SS_002", ["Azimuth: 0", "Altitude: 45"], "TestSunSky.blend", ss_002],
		["BL28_RS_SS_003", ["Azimuth: 0", "Altitude: 90"], "TestSunSky.blend", ss_003],
		["BL28_RS_SS_004", ["Azimuth: 90", "Altitude: 0"], "TestSunSky.blend", ss_004],
		["BL28_RS_SS_005", ["Azimuth: 90", "Altitude: 45"], "TestSunSky.blend", ss_005],
		["BL28_RS_SS_006", ["Azimuth: 90", "Altitude: 90"], "TestSunSky.blend", ss_006],
		["BL28_RS_SS_007", ["Azimuth: 180", "Altitude: 0"], "TestSunSky.blend", ss_007],
		["BL28_RS_SS_008", ["Azimuth: 180", "Altitude: 45"], "TestSunSky.blend", ss_008],
		["BL28_RS_SS_009", ["Azimuth: 180", "Altitude: 90"], "TestSunSky.blend", ss_009],
		["BL28_RS_SS_010", ["Azimuth: 270", "Altitude: 0"], "TestSunSky.blend", ss_010],
		["BL28_RS_SS_011", ["Azimuth: 270", "Altitude: 45"], "TestSunSky.blend", ss_011],
		["BL28_RS_SS_012", ["Azimuth: 270", "Altitude: 90"], "TestSunSky.blend", ss_012],
		["BL28_RS_SS_013", ["Azimuth: 360", "Altitude: 0"], "TestSunSky.blend", ss_013],
		["BL28_RS_SS_014", ["Azimuth: 360", "Altitude: 45"], "TestSunSky.blend", ss_014],
		["BL28_RS_SS_015", ["Azimuth: 360", "Altitude: 90"], "TestSunSky.blend", ss_015],

		["BL28_RS_SS_016", ["Texture Resolution - Low"], "TestSunSky.blend", ss_016],
		["BL28_RS_SS_017", ["Texture Resolution - Normal"], "TestSunSky.blend", ss_017],
		["BL28_RS_SS_018", ["Texture Resolution - High"], "TestSunSky.blend", ss_018],

		["BL28_RS_SS_019", ["Turbidity - 0.2"], "TestSunSky.blend", ss_019],
		["BL28_RS_SS_020", ["Turbidity - 1"], "TestSunSky.blend", ss_020],
		["BL28_RS_SS_021", ["Turbidity - 2"], "TestSunSky.blend", ss_021],
		["BL28_RS_SS_022", ["Turbidity - 5"], "TestSunSky.blend", ss_022],

		["BL28_RS_SS_023", ["Intencity: 1"], "TestSunSky.blend", ss_023],
		["BL28_RS_SS_024", ["Intencity: 2"], "TestSunSky.blend", ss_024],
		["BL28_RS_SS_025", ["Intencity: 5"], "TestSunSky.blend", ss_025],

		["BL28_RS_SS_026", ["Sun Glow: 1"], "TestSunSky.blend", ss_026],
		["BL28_RS_SS_027", ["Sun Glow: 2"], "TestSunSky.blend", ss_027],
		["BL28_RS_SS_028", ["Sun Glow: 5"], "TestSunSky.blend", ss_028],

		["BL28_RS_SS_029", ["Sun Disc: 0.5"], "TestSunSky.blend", ss_029],
		["BL28_RS_SS_030", ["Sun Disc: 1"], "TestSunSky.blend", ss_030],
		["BL28_RS_SS_031", ["Sun Disc: 2"], "TestSunSky.blend", ss_031],

		["BL28_RS_SS_032", ["Saturation: 0"], "TestSunSky.blend", ss_032],
		["BL28_RS_SS_033", ["Saturation: 0.5"], "TestSunSky.blend", ss_033],
		["BL28_RS_SS_034", ["Saturation: 1"], "TestSunSky.blend", ss_034],

		["BL28_RS_SS_035", ["Horizon Heigh: -0.5"], "TestSunSky.blend", ss_035],
		["BL28_RS_SS_036", ["Horizon Heigh: 0"], "TestSunSky.blend", ss_036],
		["BL28_RS_SS_037", ["Horizon Heigh: 0.5"], "TestSunSky.blend", ss_037],

		["BL28_RS_SS_038", ["Horizon Blur: 0.1"], "TestSunSky.blend", ss_038],
		["BL28_RS_SS_039", ["Horizon Blur: 0.5"], "TestSunSky.blend", ss_039],
		["BL28_RS_SS_040", ["Horizon Blur: 1.0"], "TestSunSky.blend", ss_040],

		["BL28_RS_SS_041", ["Filter Color: RGB - 1 0 1"], "TestSunSky.blend", ss_041],
		["BL28_RS_SS_042", ["Ground Color: RGB - 0 1 0"], "TestSunSky.blend", ss_042],

		#["BL28_RS_SS_043", ["moscow loc + 0    56 38"], "TestSunSky.blend", ss_043],
		#["BL28_RS_SS_044", ["moscow loc + 6    56 38"], "TestSunSky.blend", ss_044],
		#["BL28_RS_SS_045", ["moscow loc + 12    56 38"], "TestSunSky.blend", ss_045],
		#["BL28_RS_SS_046", ["moscow loc + 18    56 38"], "TestSunSky.blend", ss_046],
		#["BL28_RS_SS_047", ["moscow loc + 24    56 38"], "TestSunSky.blend", ss_047],
		#["BL28_RS_SS_048", ["lownormalhigh & 0-30"], "TestSunSky.blend", ss_048],
		#["BL28_RS_SS_049", ["lownormalhigh & 0-30"], "TestSunSky.blend", ss_049],
		#["BL28_RS_SS_050", ["lownormalhigh & 0-30"], "TestSunSky.blend", ss_050],
		#["BL28_RS_SS_051", ["lownormalhigh & 0-30"], "TestSunSky.blend", ss_051],
		#["BL28_RS_SS_052", ["lownormalhigh & 0-30"], "TestSunSky.blend", ss_052],
		#["BL28_RS_SS_053", ["lownormalhigh & 0-30"], "TestSunSky.blend", ss_053],
		#["BL28_RS_SS_054", ["miami beach + 0     26   -80   -5"], "TestSunSky.blend", ss_054],
		#["BL28_RS_SS_055", ["miami beach + 12     26   -80   -5"], "TestSunSky.blend", ss_055],
		#["BL28_RS_SS_056", ["miami beach + 24     26   -80   -5"], "TestSunSky.blend", ss_056],
		#["BL28_RS_SS_057", ["canberra + 0     -35   149  11"], "TestSunSky.blend", ss_057],
		#["BL28_RS_SS_058", ["canberra + 12     -35   149  11"], "TestSunSky.blend", ss_058],
		#["BL28_RS_SS_059", ["canberra + 24     -35   149  11"], "TestSunSky.blend", ss_059]
		
	]

	launch_tests()

