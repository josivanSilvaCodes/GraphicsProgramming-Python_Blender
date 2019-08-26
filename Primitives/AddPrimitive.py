
# AddPrimitive.py
# Code write by Prof. Josivan Pereira da Silva, 2019
# Used in Graphics Programming classes at University
# To facilitate the learning by the students all the comments are in Portuguese
# Everyone can use it, but maintain the credits, please
# e-mail: josivan.engenharia@gmail.com

import bpy

# Primitivas padrao do Blender
# Add >> Mesh >> Cylinder


bom_prefix = bpy.ops.mesh

bom_prefix.primitive_monkey_add(location=(0,3,0))

bom_prefix.primitive_cone_add(location=(0,-3,0))

bom_prefix.primitive_cylinder_add(location=(0,3,3))


path = ""
path = "C:\\Users\\user\\Desktop\\imgs\\primitivas.png"
bpy.context.scene.render.filepath = path
bpy.ops.render.render(use_viewport = True, write_still = True)



