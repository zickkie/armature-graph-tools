bl_info = {
    "name": "Armature Graph Tools",
    "author": "Arthur Shapriro",
    "version": (1, 0),
    "blender": (3, 2, 2),
    "location": "Graph Editor > N-panel",
    "description": "Tools for a better Armature-oriented Animation Workflow inside the Graph Editor",
    "warning": "",
    "doc_url": "https://github.com/zickkie/armature-graph-tools#readme",
    "category": "Animation",
}

import bpy

from . import functions
from . import operators
from . import panels



##################################   
########## REGISTRATION ##########
##################################  
def register():
    operators.register()
    panels.register()

def unregister():
    operators.unregister()
    panels.unregister()



if __name__ == "__main__":
    register()
