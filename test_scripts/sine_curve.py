import bpy
import math
# Select objects by type
for o in bpy.context.scene.objects:
    print(o.type)
    if o.type == 'CURVE':
        o.select_set(True)
    else:
        o.select_set(False)

# Call the operator only once
bpy.ops.object.delete()

def create_sine(numCycles = 1, stepsPerCycle = 16, curvelen=2, yscale=1):

    curve = bpy.data.curves.new('sinepath', type='CURVE')
    curve.dimensions = '2D'
    curve.resolution_u = 1
    spline = curve.splines.new('NURBS')

    #cursor = bpy.context.scene.cursor_location
    xscale = float(curvelen)/stepsPerCycle/numCycles

    for x in range(0, stepsPerCycle * numCycles+1):
        y = math.sin(float(x) / stepsPerCycle * math.pi*2)

        #Add first point for start of Nurbs (needs extra point)
        if x == 0:
            spline.points[0].co = (x*xscale,y*yscale, 0.0,1)

        # Add point
        spline.points.add(1)
        spline.points[-1].co = (x*xscale, y*yscale,0.0,1)

    # Add end point
    spline.points.add(1)
    spline.points[-1].co = (x*xscale, y*yscale,0.0,1)

    curveObject = bpy.data.objects.new('sinepath', curve)
    
    bpy.context.collection.objects.link(curveObject)
create_sine(numCycles = 1, stepsPerCycle = 5, yscale=1,curvelen=2)
