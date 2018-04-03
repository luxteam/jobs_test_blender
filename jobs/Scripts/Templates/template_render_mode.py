import bpy
import addon_utils
import datetime
import sys
import json
import os

def main(render_mode):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	bpy.context.scene.rpr.render.render_mode = render_mode

	render(render_mode)

if __name__ == "__main__":

	render_modes = ['WIREFRAME', 'TEXCOORD', 'POSITION', 'NORMAL', 'MATERIAL_INDEX', 'GLOBAL_ILLUMINATION', 'DIRECT_ILLUMINATION_NO_SHADOW', 'DIRECT_ILLUMINATION', 'DIFFUSE', 'AMBIENT_OCCLUSION']
	for mode in render_modes:
		main(mode)


