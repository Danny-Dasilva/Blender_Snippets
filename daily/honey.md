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



check frame s and liquidity settings