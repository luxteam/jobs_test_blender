def get_material_and_node(material_name, node_name):
    material = [e for e in bpy.data.materials if e.name == material_name][0]
    node = [n for n in material.node_tree.nodes if n.name == node_name][0]
    return material, node
