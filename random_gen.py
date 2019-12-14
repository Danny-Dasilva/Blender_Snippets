import bpy
from random import randint


bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

number = 100

for i in range(0, number):
    x = randint(-5, 5)
    y = randint(-5, 5)
    z = randint(-5,5)

    bpy.ops.mesh.primitive_monkey_add(location=(x,y,z))
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].render_levels = 2
    bpy.context.object.modifiers["Subdivision"].levels = 1
    bpy.ops.object.shade_smooth()

