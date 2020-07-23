bl_info = {
    "name": "Rig",
    "author": "////////",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > properties panel",
    "description": "display rig controls when selected (in pose mode)",
    "warning": "",
    "wiki_url": "",
    "category": "Animation"}

import bpy
from bpy.props import BoolProperty

rig_id = "Robot_rig"


class RigLayers(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Robot UI'
    bl_category = 'Rig UI'
    bl_idname = rig_id.upper() + '_PT_rig_layers'

    @classmethod
    def poll(self, context):
        if context.mode != 'POSE':
            return False

        try:
           ob = context.active_object
           return (context.active_object.data.get("rig_id") == rig_id)
        except AttributeError:
           return 0

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        id = context.active_object.data.get("rig_id")

        #Layers
        row = col.row()
        row.label(text="Main:")
        row.prop(context.active_object.data, "layers", index=16, toggle=True, text="Root")
        row.prop(context.active_object.data, "layers", index=1, toggle=True, text="Torso")

        row = col.row()
        row.label(text="Head:")
        row.prop(context.active_object.data, "layers", index=2, toggle=True, text="Head")
        row.label(text="")

        #Arms
        row = col.row()
        row.label(text="Arms:")
        row.prop(context.active_object.data, "layers", index=21, toggle=True, text="IK")
        row.prop(context.active_object.data, "layers", index=22, toggle=True, text="FK")
        #Legs
        row = col.row()
        row.label(text="Legs:")
        row.prop(context.active_object.data, "layers", index=5, toggle=True, text="IK")
        row.prop(context.active_object.data, "layers", index=6, toggle=True, text="FK")
        #Fingers
        row = col.row()
        row.label(text="Fingers:")
        row.prop(context.active_object.data, "layers", index=4, toggle=True, text="Fingers")
        row.prop(context.active_object.data, "layers", index=20, toggle=True, text="Fingers2")
        row = col.row()
        #Ribbon
        row = col.row()
        row.label(text="Bend:")
        row.prop(context.active_object.data, "layers", index=23, toggle=True, text="Arms")
        row.prop(context.active_object.data, "layers", index=7, toggle=True, text="Legs")

        row = col.row()
        row.separator()
        row = col.row()


        row = col.row()
        row.prop(context.active_object, 'show_in_front', toggle=True, text='X Ray')
 
        #simpflify
        row = col.row()
        row.separator()
        row = col.row()
        row.prop(context.scene.render, "use_simplify", toggle=True,text="Simplify")
        if context.scene.render.use_simplify:
            row.prop(context.scene.render, "simplify_subdivision", text="levels")
        else:    
            row.label(text="")
            
        #export property
        row = col.row()
        row.separator()
        row = col.row()
        row.prop(bpy.data.objects['Robot_rig_DEF'],'["export_mode"]', slider=True, text='Export mode')
            

class RigProperties(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Robot Properties"
    bl_category = "Rig UI"
    bl_idname = rig_id.upper() + '_PT_rig_properties'

    @classmethod
    def poll(self, context):
        if context.mode != 'POSE':
            return False

        try:
           ob = context.active_object
           return (context.active_object.data.get("rig_id") == rig_id)
        except AttributeError:
           return 0

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        pose_bones = context.active_object.pose.bones
        show_all = pose_bones["Root"]['show_all']

        #show all properties
        layout.prop(pose_bones["Root"], "show_all", toggle=False, text="Show all properties")

        #Head/Neck
        head = ["Head"]
        torso = ["Torso", "Hips", "Spine", "Chest"]

        #Arms
        fk_arm = ["Bicep.L", "Forearm.L", "Elbow_bend.L","Hand_FK.L"]
        ik_arm = ["Hand_IK.L", "Elbow.L", "Elbow_bend.L"]
        if is_selected(fk_arm+ik_arm) or show_all:
            layout.label(text="Left Arm:")
            layout.prop(pose_bones[ik_arm[0]], '["IK"]', text="IK", slider=True)
            layout.prop(pose_bones[ik_arm[0]], '["parent"]', text="World/Local", slider=True)
            layout.prop(pose_bones[fk_arm[0]], '["Isolate"]', text="Isolate FK", slider=True)

        fk_arm = ["Bicep.R", "Forearm.R", "Elbow_bend.R","Hand_FK.R"]
        ik_arm = ["Hand_IK.R", "Elbow.R", "Elbow_bend.R"]
        if is_selected(fk_arm+ik_arm) or show_all == True:
            layout.label(text="Right Arm:")
            layout.prop(pose_bones[ik_arm[0]], '["IK"]', text="IK", slider=True)
            layout.prop(pose_bones[ik_arm[0]], '["parent"]', text="World/Local", slider=True)
            layout.prop(pose_bones[fk_arm[0]], '["Isolate"]', text="Isolate FK", slider=True)


        #Legs
        fk_leg = ["Thigh.L", "Shin.L", "Knee_bend.L","Foot_FK.L", "Toe.L", "Toe_pivot.L", "Head"]
        ik_leg = ["Foot_IK.L", "Knee.L", "Foot_roll.L", "Foot_bank.L", "Knee_bend.L", "Head"]
        if is_selected(fk_leg+ik_leg) or show_all:
            layout.label(text="Left Leg:")
            layout.prop(pose_bones[ik_leg[0]], '["IK"]', text="IK", slider=True)
            layout.prop(pose_bones[ik_leg[0]], '["parent"]', text="World/Local", slider=True)
            layout.prop(pose_bones[ik_leg[0]], '["Isolate"]', text="Isolate FK", slider=True)

        fk_leg = ["Thigh.R", "Shin.R", "Knee_bend.R","Foot_FK.R", "Toe.R", "Toe_pivot.R", "Head"]
        ik_leg = ["Foot_IK.R", "Knee.R", "Foot_roll.R", "Foot_bank.R", "Knee_bend.R", "Head"]
        
        if is_selected(fk_leg+ik_leg) or show_all:
            layout.label(text="Right Leg:")
            layout.prop(pose_bones[ik_leg[0]], '["IK"]', text="IK", slider=True)
            layout.prop(pose_bones[ik_leg[0]], '["parent"]', text="World/Local", slider=True)
            layout.prop(pose_bones[ik_leg[0]], '["Isolate"]', text="Isolate FK", slider=True)


def is_selected(names):
    try:
        for name in names:
            if bpy.context.active_pose_bone.name == name:
                return True
        for bone in bpy.context.selected_pose_bones:
            for name in names:
                if bone.name == name:
                    return True
    except AttributeError:
        pass
    return False

bpy.types.PoseBone.show_all = BoolProperty(
	description = 'Display all properties',
	default = False)


# Registration
def register():
    bpy.utils.register_class(RigLayers)
    bpy.utils.register_class(RigProperties)


def unregister():
    bpy.utils.unregister_class(RigLayers)
    bpy.utils.unregister_class(RigProperties)

if __name__ == '__main__':
    register()
