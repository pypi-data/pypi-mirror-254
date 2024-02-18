import sys
import typing
from . import uvcalc_transform
from . import add_mesh_torus
from . import object
from . import image
from . import node
from . import anim
from . import constraint
from . import file
from . import rigidbody
from . import userpref
from . import clip
from . import bmesh
from . import presets
from . import spreadsheet
from . import geometry_nodes
from . import screen_play_rendered_anim
from . import uvcalc_lightmap
from . import object_quick_effects
from . import assets
from . import object_randomize_transform
from . import sequencer
from . import view3d
from . import wm
from . import console
from . import freestyle
from . import uvcalc_follow_active
from . import object_align
from . import mesh
from . import vertexpaint_dirt

GenericType = typing.TypeVar("GenericType")

def register(): ...
def unregister(): ...
