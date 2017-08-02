from core import G

exp = None

# G.app.modules['']
def mh_setup(exformat):
    global exp
    print(exp)
    if exformat == "fbx":
        exp = G.app.getCategory('Files').getTaskByName('Export').getExporter('Filmbox (fbx)')
    elif exformat == "dae":
        exp = G.app.getCategory('Files').getTaskByName('Export').getExporter('Collada (dae)')
    elif exformat == "obj":
        exp = G.app.getCategory('Files').getTaskByName('Export').getExporter('Wavefront obj')
    elif exformat == "ogre":
        exp = G.app.getCategory('Files').getTaskByName('Export').getExporter('Ogre3D')
    elif exformat == "stl":
        exp = G.app.getCategory('Files').getTaskByName('Export').getExporter('Stereolithography (stl)')
    elif exformat == "bvh":
        exp = G.app.getCategory('Files').getTaskByName('Export').getExporter('Biovision Hierarchy BVH')
    elif exformat == "lm":
        exp = G.app.getCategory('Files').getTaskByName('Export').getExporter('Lightmap')
    elif exformat == "uvm":
        exp = G.app.getCategory('Files').getTaskByName('Export').getExporter('UV map')
    # return exp   
    # exp.export(G.app.selectedHuman, lambda x: "test.fbx")


def mh_unit(request):
    """Set set scale units."""
    if str(request) in ("inch", "decimeter", "meter", "centimeter"):
        for (button, name) in exp.taskview.scaleButtons:
            if name == request:
                button.setChecked(True)
    else:
        return "Invalid Unit " + str(request)


def mh_feet_on_ground(request):
    try:
        ft = bool(int(request))
        exp.feetOnGround.setChecked(ft)
        return 'OK'
    except KeyError:
        return exp.feetOnGround.selected

def mh_binary(request):
    ft = bool(int(request))
    try:
        if hasattr(exp, 'binary'):
            exp.binary.setChecked(ft)
        elif hasattr(exp, 'stlBinary'):
            exp.stlBinary.setChecked(ft)
        return 'OK'
    except AttributeError:
        return exp.binary.selected

def mh_hidden_geom(request):
    try:
        ft = bool(int(request))
        exp.hiddenGeom.setChecked(ft)
        return 'OK'
    except KeyError:
        return exp.hiddenGeom.selected

def mh_facial_pose_units(request):
    try:
        ft = bool(int(request))
        exp.facePoseUnits.setChecked(ft)
        return 'OK'
    except KeyError:
        return exp.facePoseUnits.selected

def mh_orientation(request):
    try:
        getattr(exp,str(request)).setChecked(True)
    except KeyError:
        return False

def mh_bone_orientation(request):
    try:
        getattr(exp,str(request)).setChecked(True)
    except KeyError:
        return False


def mh_use_normals(request):
    try:
        ss = bool(int(request))
        exp.useNormals.setChecked(ss)
        return 'OK'
    except KeyError:
        return exp.useNormals.selected

def mh_use_rel_paths(request):
    try:
        ss = bool(int(request))
        exp.useRelPaths.setChecked(ss)
        return 'OK'
    except KeyError:
        return exp.useRelPaths.selected


def mh_tex_folder(request):
    try:
        exp.texFolder = str(request)
        return 'OK'
    except KeyError:
        return exp.texFolder

def mh_custom_prefix(request):
    try:
        exp.customPrefix = str(request)
        return 'OK'
    except KeyError:
        return exp.texFolder



def mh_export(file):
    exp.export(G.app.selectedHuman, lambda x: file)