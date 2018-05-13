import bpy
import os
import rna_keymap_ui

#---------------------------------------
# Preferences panel
#---------------------------------------

def get_hotkey_entry_item(km, kmi_name, properties): #kmi_value, properties):
	try:
		for i, km_item in enumerate(km.keymap_items):
			if km.keymap_items.keys()[i] == kmi_name:
				if km.keymap_items[i].properties.name == properties:
					return km_item
		return None
	except:
		pass


def get_addon_name():
	return os.path.basename(os.path.dirname(os.path.realpath(__file__)))

addon_files = [
			('Sculpt',"wm.call_menu","VIEW3D_MT_brush_options", "Brush Options"),
			('Sculpt',"wm.call_menu","VIEW3D_MT_brush_curve_menu", "Curve Menu"),
			#			   ("wm.call_menu","VIEW3D_MT_custom_menu", "Custom Menu"),
			('Mesh',"wm.call_menu","MESH_MT_context_delete_menu", "Delete"),
			('Sculpt',"wm.call_menu","VIEW3D_MT_dyntopo","Dynotopo Menu"),
			('Mesh',"view3d.extrude_menu_operator","Extrude", "Extrude"),
			('Object Mode', "view3d.layers_window","Layers", "Layers"),
			('Object Non-modal', "view3d.manipulator_operator","Manipulator", "Manipulator"),
			('Object Non-modal',"view3d.editor_mode_operator","Mode", "Interactive Mode"),
			('Object Non-modal',"wm.call_menu","VIEW3D_MT_pivot_point", "Pivot Menu"),
			('Mesh',"view3d.proportional_menu_operator","Falloff", "Falloff Menu"),
			('Mesh',"wm.call_menu","VIEW3D_MT_selection_menu", "Selection Menu"),
			('Object Non-modal',"view3d.shading_menu_operator","Shading_Menu", "Shading Menu"),
			('Object Non-modal',"view3d.snap_menu_operator","Snap", "Snapping Menu"),
			('Sculpt',"wm.call_menu","VIEW3D_MT_stroke_options", "Stroke Options"),
			('Sculpt',"wm.call_menu","VIEW3D_MT_master_symmetry_menu", "Symmetry Menu"),
			('Sculpt',"wm.call_menu","VIEW3D_MT_texture_menu", "Texture Menu"),
			('Object Non-modal',"wm.call_menu","VIEW3D_MT_view_menu", "View Menu")
			]
#

class AdvanceUIPreferences(bpy.types.AddonPreferences):
	bl_idname = get_addon_name()

	def draw(self, context):
		layout = self.layout
		scene = context.scene

		column = layout.column()
		column.separator()

		col = layout.column(align = True)
		row = col.row()
		box=layout.box()
		split = box.split()
		col = split.column()
		col.label('Hotkeys:')
		col.label('Do NOT remove hotkeys, disable them instead!')
		col.separator()

		wm = bpy.context.window_manager
		kc = wm.keyconfigs.user
		for addon in addon_files:
			km = kc.keymaps[addon[0]]
			kmi = get_hotkey_entry_item(km, addon[1], addon[2])
			if kmi:
				row = col.row()
				row = col.split(percentage=0.25)
				row.label(addon[3])
				row.context_pointer_set("keymap", km)
				rna_keymap_ui.draw_kmi([], kc, km, kmi, row, 0)
			else:
				row.label("restore hotkeys from interface tab")
