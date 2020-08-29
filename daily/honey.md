in blender 2.9
s3 > gz3
toggle xray


add icosphere
s .25 > gz 5

shade icosphere smooth
add subdivision surface modifier to ico sphere
set to 2

in physics
add fluid > flow to flow 
add fluid > domain to domain
for hitting do effector 

you can keyframe flow

in domain
set resolution division to 100-200
timesteps 15-12 

uncheck border collisions

check diffusion

exponent to 1
surface tension 1.8
base to 2

mesh to 3 - 




Traceback (most recent call last):
  File "C:\Users\yahch\AppData\Roaming\Blender Foundation\Blender\2.90\scripts\addons\tissue-master\dual_mesh.py", line 247, in execute
    apply_as='DATA', modifier='dual_mesh_subsurf'
  File "D:\Users\yahch\Downloads\blender-2.90.0-21cb6f09ffa8-windows64\blender2.9\2.90\scripts\modules\bpy\ops.py", line 201, in __call__
    ret = op_call(self.idname_py(), None, kw)
TypeError: Converting py args to operator properties: : keyword "apply_as" unrecognized

location: <unknown location>:-1

