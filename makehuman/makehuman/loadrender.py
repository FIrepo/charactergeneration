from core import G
import scene


# G.app.modules['']
settings = {'dimensions':[800,600],
            'AA':True,
            'lightmapSSS':False,
            'scene':G.app.scene}


def mh_width(request):
    """Set rendering resolution."""
    try:
        settings['dimensions'][0]= int(request)
    except KeyError:
        return str(settings['dimensions'])

def mh_height(request):
    """Set rendering resolution."""
    try:
        settings['dimensions'][1]= int(request)
    except KeyError:
        return str(settings['dimensions'])


def mh_anti_aliasing(request):
    '''Set anti aliasing True or False.
    '''
    try:
        aa = bool(int(request))
        settings['AA'] = aa
        return 'OK'
    except KeyError:
        return json.dumps(settings['AA'])


def mh_lightmap_sss(request):
    try:
        ss = bool(int(request))
        settings['lightmapSSS'] = ss
        return 'OK'
    except KeyError:
        return json.dumps(settings['lightmapSSS'])

def mh_x_rotation(request):
    try:
        human = G.app.selectedHuman
        rot = human.getRotation()
        rot[0] = float(request)
        human.setRotation(rot)
        G.app.redraw()
        return 'OK'
    except KeyError:
        return human.getRotation()

# def mh_z_rotation(request):
#     try:
#         human = G.app.selectedHuman
#         rot = human.getRotation()
#         rot[1] = float(request)
#         human.setRotation(rot)
#         return 'OK'
#     except KeyError:
#         return human.getRotation()

def mh_y_rotation(request):
    try:
        human = G.app.selectedHuman
        rot = human.getRotation()
        rot[1] = float(request)
        human.setRotation(rot)
        G.app.redraw()
        return 'OK'
    except KeyError:
        return human.getRotation()

def mh_x_position(request):
    try:
        human = G.app.selectedHuman
        pos = human.getPosition()
        pos[0] = float(request)
        human.setPosition(pos)
        return 'OK'
    except KeyError:
        return human.getPosition()

def mh_z_position(request):
    try:
        human = G.app.selectedHuman
        pos = human.getPosition()
        pos[2] = float(request)
        human.setPosition(pos)
        return 'OK'
    except KeyError:
        return human.getPosition()

def mh_y_position(request):
    try:
        human = G.app.selectedHuman
        pos = human.getPosition()
        pos[1] = float(request)
        human.setPosition(pos)
        return 'OK'
    except KeyError:
        return human.getPosition()

def mh_zoom(request):
    try:
        G.app.modelCamera.zoomFactor = float(request)
        return 'OK'
    except KeyError:
        return G.app.modelCamera.zoomFactor



def mh_scene(request):
    G.app.setScene(scene.Scene('data/scenes/'+request+'.mhscene'))


def mh_render():
    G.app.modules['4_rendering_opengl'].mh2opengl.Render(settings)
    return 'OK'
