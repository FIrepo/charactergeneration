from core import G



human = G.app.selectedHuman
#for m in human.modifiers:
#    print(m.fullName, m.getMin(), m.getDefaultValue(), m.getMax(), m.description)
custom = {
    "skin": "Name of a file in data/skin/*/ without the extension",
    "eyes": "Name of a file in data/skin/*/ without the extension",
    "teeth": "Name of a file in data/skin/*/ without the extension",
    "hair": "Name of a file in data/skin/*/ without the extension",
    "eyebrows": "Name of a file in data/skin/*/ without the extension",
    "eyelashes": "Name of a file in data/skin/*/ without the extension",
    "tongue": "Name of a file in data/skin/*/ without the extension",
    "clothes": "Array of names of a files in data/clothes/*/ without the extensions. ie. [\"\"male_elegantsuit01\"\",\"\"fedora\"\"]"
}

oldvars = {"african": ["setAfrican"],
"age": ["head/head-age-decr|incr", "setAge"],
"angle": ["head/head-angle-in|out"],
"ankle_circum": ["measure/measure-ankle-circ-decr|incr"],
"asian": ["setAsian"],
"breast_firmness": ["breast/BreastFirmness"],
"breast_size": ["breast/BreastSize"],
"breast_volume": ["breast/breast-volume-vert-down|up"],
"bust_circum": ["measure/measure-bust-circ-decr|incr"],
"buttocks_volume": ["buttocks/buttocks-volume-decr|incr"],
"calf_circum": ["measure/measure-calf-circ-decr|incr"],
"caucasian": ["setCaucasian"],
"cheek_inner_volume": ["cheek/l-cheek-inner-decr|incr", "cheek/r-cheek-inner-decr|incr"],
"cheek_outer_volume": ["cheek/l-cheek-volume-decr|incr", "cheek/r-cheek-volume-decr|incr"],
"cleft_chin": ["chin/chin-cleft-decr|incr"],
"compression": ["nose/nose-compression-compress|uncompress"],
"cranic_shape": ["forehead/forehead-nubian-decr|incr"],
"cupids_bow_shape": ["mouth/mouth-cupidsbow-decr|incr"],
"cupids_bow_width": ["mouth/mouth-cupidsbow-width-decr|incr"],
"curve": ["nose/nose-curve-concave|convex"],
"diamond": ["head/head-diamond"],
"dimples": ["mouth/mouth-dimples-in|out"],
"dorsi_muscle": ["torso/torso-muscle-dorsi-decr|incr"],
"double_neck": ["neck/neck-double-decr|incr"],
"ear_flapped": ["ears/r-ear-flap-decr|incr"],
"ear_rotation": ["ears/l-ear-rot-backward|forward", "ears/r-ear-rot-backward|forward"],
"ear_shape_pointed_triangle": ["ears/l-ear-shape-pointed|triangle", "ears/r-ear-shape-pointed|triangle"],
"ear_shape_squared_round": ["ears/r-ear-shape-square|round", "ears/l-ear-shape-square|round"],
"ear_wing_shaped": ["ears/r-ear-wing-decr|incr", "ears/l-ear-wing-decr|incr"],
"eye_bag_distorsion": ["eyes/l-eye-bag-in|out", "eyes/r-eye-bag-in|out"],
"eye_bag_height": ["eyes/r-eye-bag-height-decr|incr", "eyes/l-eye-bag-height-decr|incr"],
"eye_bag_volume": ["eyes/l-eye-bag-decr|incr", "eyes/r-eye-bag-decr|incr"],
"eye_epicanthus": ["eyes/r-eye-epicanthus-in|out", "eyes/l-eye-epicanthus-in|out"],
"eyebrows_angle": ["eyebrows/eyebrows-angle-down|up"],
"eyebrows_bulge": ["eyebrows/eyebrows-trans-backward|forward"],
"eyefold_angle": ["eyes/l-eye-eyefold-angle-down|up", "eyes/r-eye-eyefold-angle-down|up"],
"eyefold_position": ["eyes/r-eye-eyefold-down|up", "eyes/l-eye-eyefold-down|up"],
"eyefold_volume": ["eyes/r-eye-eyefold-concave|convex", "eyes/l-eye-eyefold-concave|convex"],
"fingers_diameter": ["armslegs/r-hand-fingers-diameter-decr|incr", "armslegs/l-hand-fingers-diameter-decr|incr"],
"fingers_distance": ["armslegs/r-hand-fingers-distance-decr|incr", "armslegs/l-hand-fingers-distance-decr|incr"],
"fingers_length": ["armslegs/r-hand-fingers-length-decr|incr", "armslegs/l-hand-fingers-length-decr|incr"],
"forehead_bulge": ["forehead/forehead-trans-backward|forward"],
"front_chest_dist": ["measure/measure-frontchest-dist-decr|incr"],
"gender": ["setGender"],
"genital_volume": ["pelvis/bulge-decr|incr"],
"greek": ["nose/nose-greek-decr|incr"],
"hand_position": ["armslegs/l-hand-trans-in|out", "armslegs/r-hand-trans-in|out"],
"head_fat": ["head/head-fat-decr|incr"],
"height": ["setHeight"],
"hips_circum": ["measure/measure-hips-circ-decr|incr"],
"horizontal_distance": ["breast/breast-dist-decr|incr"],
"hump": ["nose/nose-hump-decr|incr"],
"invertedtriangular": ["head/head-invertedtriangular"],
"knee_circ": ["measure/measure-knee-circ-decr|incr"],
"laugh_lines": ["mouth/mouth-laugh-lines-in|out"],
"lowerarm_length": ["armslegs/l-lowerarm-scale-horiz-decr|incr", "measure/measure-lowerarm-length-decr|incr", "armslegs/r-lowerarm-scale-horiz-decr|incr"],
"lowerarm_muscles": ["armslegs/r-lowerarm-muscle-decr|incr", "armslegs/l-lowerarm-muscle-decr|incr"],
"lowerarm_skinny_fat": ["armslegs/r-lowerarm-fat-decr|incr"],
"lowerarm_thickness_1": ["armslegs/l-lowerarm-scale-depth-decr|incr", "armslegs/r-lowerarm-scale-depth-decr|incr"],
"lowerarm_thickness_2": ["armslegs/l-lowerarm-scale-vert-decr|incr", "armslegs/r-lowerarm-scale-vert-decr|incr"],
"lowerleg_height": ["measure/measure-lowerleg-height-decr|incr"],
"lowerleg_muscle": ["armslegs/r-lowerleg-muscle-decr|incr", "armslegs/l-lowerleg-muscle-decr|incr"],
"lowerleg_scale_depth": ["armslegs/r-lowerleg-scale-depth-decr|incr", "armslegs/l-lowerleg-scale-depth-decr|incr"],
"lowerleg_scale_horizontally": ["armslegs/r-lowerleg-scale-horiz-decr|incr", "armslegs/l-lowerleg-scale-horiz-decr|incr"],
"lowerleg_skinny_fat": ["armslegs/r-lowerleg-fat-decr|incr", "armslegs/l-lowerleg-fat-decr|incr"],
"lowerlegs_height": ["armslegs/lowerlegs-height-decr|incr"],
"lowerlip_curved_shape": ["mouth/mouth-lowerlip-ext-down|up"],
"move_base_vert": ["nose/nose-base-down|up"],
"move_corners_vert": ["mouth/mouth-angles-down|up"],
"move_depth": ["head/head-trans-backward|forward", "nose/nose-trans-backward|forward", "neck/neck-trans-backward|forward", "hip/hip-trans-backward|forward", "ears/r-ear-trans-backward|forward", "ears/l-ear-trans-backward|forward", "armslegs/l-foot-trans-backward|forward", "armslegs/r-foot-trans-backward|forward", "mouth/mouth-trans-backward|forward", "torso/torso-trans-backward|forward"],
"move_eye_horizontally": ["eyes/l-eye-trans-in|out", "eyes/r-eye-trans-in|out"],
"move_eye_vertically": ["eyes/l-eye-trans-down|up", "eyes/r-eye-trans-down|up"],
"move_horizontally": ["armslegs/r-foot-trans-in|out", "neck/neck-trans-in|out", "hip/hip-trans-in|out", "head/head-trans-in|out", "nose/nose-trans-in|out", "torso/torso-trans-in|out", "armslegs/l-foot-trans-in|out", "mouth/mouth-trans-in|out"],
"move_inner_corner_horiz": ["eyes/l-eye-push2-in|out", "eyes/r-eye-push2-in|out"],
"move_inner_corner_vert": ["eyes/r-eye-corner2-down|up", "eyes/l-eye-corner2-down|up"],
"move_knee_horizontally": ["armslegs/l-leg-valgus-decr|incr", "armslegs/r-leg-valgus-decr|incr"],
"move_knee_vertically": ["armslegs/r-upperleg-scale-vert-decr|incr", "armslegs/l-upperleg-scale-vert-decr|incr"],
"move_outer_corner_horiz": ["eyes/l-eye-push1-in|out", "eyes/r-eye-push1-in|out"],
"move_outer_corner_vert": ["eyes/r-eye-corner1-down|up", "eyes/l-eye-corner1-down|up"],
"move_tip_vertically": ["nose/nose-point-down|up"],
"move_vert": ["eyebrows/eyebrows-trans-down|up"],
"move_vertically": ["ears/l-ear-trans-down|up", "neck/neck-trans-down|up", "mouth/mouth-trans-down|up", "head/head-trans-down|up", "hip/hip-trans-down|up", "ears/r-ear-trans-down|up", "cheek/l-cheek-trans-down|up", "cheek/r-cheek-trans-down|up", "nose/nose-trans-down|up", "torso/torso-trans-down|up"],
"muscle": ["setMuscle"],
"muscular_tone": ["stomach/stomach-tone-decr|incr"],
"nape_to_waist": ["measure/measure-napetowaist-dist-decr|incr"],
"navel_bump": ["stomach/stomach-navel-in|out"],
"navel_position": ["stomach/stomach-navel-down|up"],
"neck_circum": ["measure/measure-neck-circ-decr|incr"],
"neck_height": ["measure/measure-neck-height-decr|incr"],
"nipple_point": ["breast/nipple-point-decr|incr"],
"nipple_size": ["breast/nipple-size-decr|incr"],
"nostrils_angle": ["nose/nose-nostrils-angle-down|up"],
"oval": ["head/head-oval"],
"pelvis_muscular_tone": ["pelvis/pelvis-tone-decr|incr"],
"penis_circumference": ["genitals/penis-circ-decr|incr"],
"penis_length": ["genitals/penis-length-decr|incr"],
"pointiness": ["breast/breast-point-decr|incr"],
"pregnancy_shape": ["stomach/stomach-pregnant-decr|incr"],
"proportions": ["macrodetails-proportions/BodyProportions"],
"setProportions": ["macrodetails-proportions/BodyProportions"],
"rectangular": ["head/head-rectangular"],
"round": ["head/head-round"],
"scale_cheek_prominence": ["cheek/l-cheek-bones-decr|incr", "cheek/r-cheek-bones-decr|incr"],
"scale_chin_angular": ["chin/chin-bones-decr|incr"],
"scale_chin_height": ["chin/chin-height-decr|incr"],
"scale_chin_prognathism": ["chin/chin-prognathism-decr|incr"],
"scale_chin_prominence": ["chin/chin-prominent-decr|incr"],
"scale_chin_width": ["chin/chin-width-decr|incr"],
"scale_cone_shape": ["torso/torso-vshape-decr|incr"],
"scale_depth": ["neck/neck-scale-depth-decr|incr", "head/head-scale-depth-decr|incr", "hip/hip-scale-depth-decr|incr", "mouth/mouth-scale-depth-decr|incr", "nose/nose-scale-depth-decr|incr", "torso/torso-scale-depth-decr|incr"],
"scale_depth_of_nape": ["neck/neck-back-scale-depth-decr|incr"],
"scale_depth_of_parietal_side": ["head/head-back-scale-depth-decr|incr"],
"scale_ear": ["ears/r-ear-scale-decr|incr", "ears/l-ear-scale-decr|incr"],
"scale_eye": ["eyes/r-eye-scale-decr|incr", "eyes/l-eye-scale-decr|incr"],
"scale_foot": ["armslegs/l-foot-scale-decr|incr", "armslegs/r-foot-scale-decr|incr"],
"scale_hand": ["armslegs/l-hand-scale-decr|incr", "armslegs/r-hand-scale-decr|incr"],
"scale_height": ["ears/r-ear-scale-vert-decr|incr", "ears/l-ear-scale-vert-decr|incr"],
"scale_height_1": ["eyes/r-eye-height1-decr|incr", "eyes/l-eye-height1-decr|incr"],
"scale_height_2": ["eyes/l-eye-height2-decr|incr", "eyes/r-eye-height2-decr|incr"],
"scale_height_3": ["eyes/l-eye-height3-decr|incr", "eyes/r-eye-height3-decr|incr"],
"scale_horizontally_neck": ["neck/neck-scale-horiz-decr|incr"],
"scale_horizontally_nose": ["nose/nose-scale-horiz-decr|incr"],
"scale_horizontally_torso": ["torso/torso-scale-horiz-decr|incr"],
"scale_horizontally_mouth": ["mouth/mouth-scale-horiz-decr|incr"],
"scale_horizontally_hip": ["hip/hip-scale-horiz-decr|incr"],
"scale_horizontally_head": ["head/head-scale-horiz-decr|incr"],
"scale_lobe": ["ears/r-ear-lobe-decr|incr", "ears/l-ear-lobe-decr|incr"],
"scale_lowerlip_height": ["mouth/mouth-lowerlip-height-decr|incr"],
"scale_lowerlip_volume": ["mouth/mouth-lowerlip-volume-decr|incr"],
"scale_lowerlip_width": ["mouth/mouth-lowerlip-width-decr|incr"],
"scale_middle_lowerlip": ["mouth/mouth-lowerlip-middle-down|up"],
"scale_middle_upperlip": ["mouth/mouth-upperlip-middle-down|up"],
"scale_nostrils_flaring": ["nose/nose-flaring-decr|incr"],
"scale_nostrils_width": ["nose/nose-nostrils-width-decr|incr"],
"scale_philtrum_volume": ["mouth/mouth-philtrum-volume-decr|incr"],
"scale_tip_width": ["nose/nose-point-width-decr|incr"],
"scale_upperlip_height": ["mouth/mouth-upperlip-height-decr|incr"],
"scale_upperlip_volume": ["mouth/mouth-upperlip-volume-decr|incr"],
"scale_upperlip_width": ["mouth/mouth-upperlip-width-decr|incr"],
"scale_vertically": ["head/head-scale-vert-decr|incr", "nose/nose-scale-vert-decr|incr", "forehead/forehead-scale-vert-decr|incr", "neck/neck-scale-vert-decr|incr", "torso/torso-scale-vert-decr|incr", "hip/hip-scale-vert-decr|incr", "mouth/mouth-scale-vert-decr|incr"],
"scale_width": ["ears/l-ear-scale-depth-decr|incr", "ears/r-ear-scale-depth-decr|incr"],
"scale_width_1": ["nose/nose-width1-decr|incr"],
"scale_width_2": ["nose/nose-width2-decr|incr"],
"scale_width_3": ["nose/nose-width3-decr|incr"],
"septum_angle": ["nose/nose-septumangle-decr|incr"],
"shoulder_dist": ["measure/measure-shoulder-dist-decr|incr"],
"shoulder_muscle_mass": ["armslegs/r-upperarm-shoulder-muscle-decr|incr", "armslegs/l-upperarm-shoulder-muscle-decr|incr"],
"square": ["head/head-square"],
"temple_bulge": ["forehead/forehead-temple-decr|incr"],
"testicles_size": ["genitals/penis-testicles-decr|incr"],
"thigh_circ": ["measure/measure-thigh-circ-decr|incr"],
"tone_of_side_chin": ["chin/chin-jaw-drop-decr|incr"],
"triangular": ["head/head-triangular"],
"underbust_circum": ["measure/measure-underbust-circ-decr|incr"],
"upper_arm_circum": ["measure/measure-upperarm-circ-decr|incr"],
"upperarm_length": ["armslegs/l-upperarm-scale-horiz-decr|incr", "armslegs/r-upperarm-scale-horiz-decr|incr", "measure/measure-upperarm-length-decr|incr"],
"upperarm_muscles": ["armslegs/l-upperarm-muscle-decr|incr", "armslegs/r-upperarm-muscle-decr|incr"],
"upperarm_skinny_fat": ["armslegs/r-upperarm-fat-decr|incr", "armslegs/l-upperarm-fat-decr|incr"],
"upperarm_thickness_1": ["armslegs/l-upperarm-scale-depth-decr|incr", "armslegs/r-upperarm-scale-depth-decr|incr"],
"upperarm_thickness_2": ["armslegs/r-upperarm-scale-vert-decr|incr", "armslegs/l-upperarm-scale-vert-decr|incr"],
"upperleg_height": ["measure/measure-upperleg-height-decr|incr"],
"upperleg_muscle": ["armslegs/r-upperleg-muscle-decr|incr", "armslegs/l-upperleg-muscle-decr|incr"],
"upperleg_scale_depth": ["armslegs/r-upperleg-scale-depth-decr|incr", "armslegs/l-upperleg-scale-depth-decr|incr"],
"upperleg_scale_horizontally": ["armslegs/r-upperleg-scale-horiz-decr|incr", "armslegs/l-upperleg-scale-horiz-decr|incr"],
"upperleg_skinny_fat": ["armslegs/r-upperleg-fat-decr|incr", "armslegs/l-upperleg-fat-decr|incr"],
"upperlegs_height": ["armslegs/upperlegs-height-decr|incr"],
"upperlip_curved_shape": ["mouth/mouth-upperlip-ext-down|up"],
"vertical_position": ["breast/breast-trans-down|up"],
"volume": ["nose/nose-volume-decr|incr"],
"waist_circum": ["measure/measure-waist-circ-decr|incr"],
"waist_to_hip": ["measure/measure-waisttohip-dist-decr|incr"],
"waist_vertical_position": ["hip/hip-waist-down|up"],
"weight": ["setWeight"],
"wrist_circum": ["measure/measure-wrist-circ-decr|incr"]}


def commit():
    human.applyAllTargets()


def set_modifier(mod, value):
    if mod in human.modifierNames:
        modifier = human.getModifier(mod)
        modifier.setValue(float(value))
    elif mod in custom.keys():
        globals()['mh_'+mod](value)
    elif mod in oldvars.keys():
        for var in oldvars[mod]:
            if "/" in var:
                modifier = human.getModifier(var)
                modifier.setValue(float(value))
            elif "set" in var:
                getattr(human, var)(value)
    elif "set" in mod:
        getattr(human, mod)(value)



def saveopts(filename):
    with open(filename, 'w') as fh:
        fh.write('"Modifier","Min value","Max Value","Default Value","Description"\r\n')
        for key in custom.keys():
            fh.write('"{}","","","","{}"\r\n'.format(key,custom[key]))
        for m in sorted(human.modifiers, key=lambda x: x.fullName):
            fh.write('"{}","{}","{}","{}","{}"\r\n'.format(m.fullName,m.getMin(),m.getMax(),m.getDefaultValue(),m.description))

def savevalues(filename):
    with open(filename, 'w') as fh:
        import json
        values = dict()
        for m in human.modifiers:
            values[m.fullName] = m.getValue()
        json.dump(values,fh)

def mh_skin(request):
    human = G.app.selectedHuman
    import material
    import os
    skin = 'data/skins/default.mhmat'
    for root, dirs, files in os.walk("data/skins"):
        for file_ in files:
            if (file_ == request+'.mhmat'):
                skin = os.path.join(root, file_)
                print skin
    try:
        human.setMaterial(material.fromFile(skin))
    except KeyError:
        return str(human.getMaterial())

def mh_clothes(request):
    human = G.app.selectedHuman
    clothing = ''
    import os
    import proxy
    for item in request:
        for root, dirs, files in os.walk("data/clothes"):
            for file_ in files:
                if (file_ == item+'.mhclo'):
                    clothing = os.path.join(root, file_)
        try:
            G.app.getTask('Geometries', 'Clothes').selectProxy(clothing)
        except KeyError:
            return str(human.getProxy())


def mh_eyes(request):
    human = G.app.selectedHuman
    try:
        G.app.getTask('Geometries', 'Eyes').selectProxy("data/eyes/"+request+"/"+request+".mhclo")
    except KeyError:
        return str(human.getProxy())


def mh_hair(request):
    human = G.app.selectedHuman
    try:
        G.app.getTask('Geometries', 'Hair').selectProxy("data/hair/"+request+"/"+request+".mhclo")
    except KeyError:
        return str(human.getProxy())

def mh_teeth(request):
    human = G.app.selectedHuman
    try:
        G.app.getTask('Geometries', 'Teeth').selectProxy("data/teeth/"+request+"/"+request+".mhclo")
    except KeyError:
        return str(human.getProxy())

def mh_eyebrows(request):
    human = G.app.selectedHuman
    try:
        G.app.getTask('Geometries', 'Eyebrows').selectProxy("data/eyebrows/"+request+"/"+request+".mhclo")
    except KeyError:
        return str(human.getProxy())

def mh_eyelashes(request):
    human = G.app.selectedHuman
    try:
        G.app.getTask('Geometries', 'Eyelashes').selectProxy("data/eyelashes/"+request+"/"+request+".mhclo")
    except KeyError:
        return str(human.getProxy())

def mh_tongue(request):
    human = G.app.selectedHuman
    try:
        G.app.getTask('Geometries', 'Tongue').selectProxy("data/tongue/"+request+"/"+request+".mhclo")
    except KeyError:
        return str(human.getProxy())
