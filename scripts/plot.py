import json
import os
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
# === Colors mapping
COLORS = [[196, 196, 196],
       [190, 153, 153],
       [180, 165, 180],
       [ 90, 120, 150],
       [102, 102, 156],
       [128,  64, 255],
       [170, 170, 170],
       [250, 170, 160],
       [ 96,  96,  96],
       [230, 150, 140],
       [128,  64, 128],
       [110, 110, 110],
       [244,  35, 232],
       [150, 100, 100],
       [ 70,  70,  70],
       [150, 120,  90],
       [255, 255, 255],
       [ 64, 170,  64],
       [230, 160,  50],
       [ 70, 130, 180],
       [190, 255, 255],
       [152, 251, 152],
       [107, 142,  35],
       [  0, 170,  30],
       [ 70, 100, 150],
       [  0,  80, 100],
       [ 32,  32,  32],
       [120,  10,  10],
       [165,  42,  42],
       [  0, 192,   0],
       [140, 140, 200],
       [220,  20,  60],
       [255,   0,   0],
       [255,   0, 100],
       [255,   0, 200],
       [200, 128, 128],
       [255, 255, 128],
       [250,   0,  30],
       [100, 140, 180],
       [220, 220, 220],
       [220, 128, 128],
       [222,  40,  40],
       [100, 170,  30],
       [ 40,  40,  40],
       [ 33,  33,  33],
       [100, 128, 160],
       [142,   0,   0],
       [210, 170, 100],
       [153, 153, 153],
       [128, 128, 128],
       [  0,   0,  80],
       [250, 170,  30],
       [192, 192, 192],
       [220, 220,   0],
       [140, 140,  20],
       [119,  11,  32],
       [150,   0, 255],
       [  0,  60, 100],
       [  0,   0, 142],
       [  0,   0,  90],
       [  0,   0, 230],
       [128,  64,  64],
       [  0,   0, 110],
       [  0,   0,  70],
       [  0,   0, 192]]

select_COLORS = {
    'person': [220,  20,  60],
    'rider': [255,   0,   0],
    'pole': [153, 153, 153],
    'traffic-light': [250, 170,  30],
    'vehicle': [  0,   0, 142],
    'bike': [119,  11,  32]
}

# === dict of instance categories
INSTANCE = {
    "animal--bird": [],
    "animal--ground-animal": [],
    "construction--flat--crosswalk-plain": [],
    "human--person": [],
    "human--rider--bicyclist": [],
    "human--rider--motorcyclist": [],
    "human--rider--other-rider": [],
    "marking--crosswalk-zebra": [],
    "object--banner": [],
    "object--bench": [],
    "object--bike-rack": [],
    "object--billboard": [],
    "object--catch-basin": [],
    "object--cctv-camera": [],
    "object--fire-hydrant": [],
    "object--junction-box": [],
    "object--mailbox": [],
    "object--manhole": [],
    "object--phone-booth": [],
    "object--street-light": [],
    "object--support--pole": [],
    "object--support--traffic-sign-frame": [],
    "object--support--utility-pole": [],
    "object--traffic-light": [],
    "object--traffic-sign--back": [],
    "object--traffic-sign--front": [],
    "object--trash-can": [],
    "object--vehicle--bicycle": [],
    "object--vehicle--boat": [],
    "object--vehicle--bus": [],
    "object--vehicle--car": [],
    "object--vehicle--caravan": [],
    "object--vehicle--motorcycle": [],
    "object--vehicle--other-vehicle": [],
    "object--vehicle--trailer": [],
    "object--vehicle--truck": [],
    "object--vehicle--wheeled-slow": []
}
HUMAN = ["human--person", "human--rider--bicyclist", "human--rider--motorcyclist"]
OBJECT = ["object--support--pole", "object--traffic-light",
        "object--vehicle--bicycle", "object--vehicle--bus",
        "object--vehicle--car", "object--vehicle--motorcycle",
        "object--vehicle--truck"]
THING = HUMAN + OBJECT

SCENCE_FRAME ={
    'intersection_1': ['0725', '0785'],
    # 'sidewalk_1': ['0786', '1600'],           # CS building
    'sidewalk_1': ['1200', '1400'],           # CS building
    'bridge': ['1710', '1940'],
    # 'bridge_1': ['1710', '1770'],
    # 'bridge_2': ['1860', '1940'],
    'sidewalk_2': ['2100', '2300'],           # Audimax
    # 'sidewalk_3': ['2800', '3400'],           # Mensa
    'sidewalk_3': ['3000', '3200'],           # Mensa
    'sidewalk_4': ['3401', '3600'],           # Library
    'intersection_2': ['3601', '3680'],          # Library
    # 'sidewalk_5': ['3681', '4200'],
    'sidewalk_5': ['3681', '4200'],
    'intersection_3': ['4201', '4300'],          # Durlach Tor
    'platform': ['4301', '4565'],
    # 'sidewalk_6': ['4920', '5670'],           # Rotesonne
    'sidewalk_6': ['5180', '5380'],           # Rotesonne
    'intersection_4': ['5720', '5870'],          # Karl Wilhelm
    'intersection_5': ['5950', '6050'],
    # 'sidewalk_7': ['6100', '6890'],
    'sidewalk_7': ['6100', '6300'],
    'intersection_6': ['6891', '6920'],
    'sidewalk_8': ['6921', '6990']
}

def plot_dict_line(d, frame_ids):
    # --- plot
    colors = dict((k, np.array(v)/255.0) for k,v in select_COLORS.items())
    def plot_one(sc, fr, id):
        f = plt.figure(figsize=(15, 10))
        for k, v in d.items():
            sub_seq = v[fr[0]:fr[1]]
            plt.plot(range(fr[0], fr[1]), sub_seq,
                     linestyle='-', #marker='o',
                     label=k.split('--')[-1], color=colors[k], alpha=0.5)
        plt.xlabel('frame')
        plt.ylabel('#instance')
        plt.yticks(range(0, max([max(v[fr[0]:fr[1]]) for v in d.values()]), 5))
        # plt.yticks(range(0, max([max(v) for v in d.values()]), 5))
        plt.legend()
        # plt.grid()
        # plt.show()
        f.savefig('./plots/'+id+'_ins_frams_'+sc+'.png', bbox_inches='tight')
        plt.cla()
        plt.close(f)
    i = 1
    for sc_name, fr_list in frame_ids.items():
        plot_one(sc_name, fr_list, str(i))
        i+=1
    plot_one('whole', [0, len(d['person'])], '0')


def plot_stacked_bar(data, series_labels, category_labels=None,
                     show_values=False, value_format="{}", x_label=None, y_label=None,
                     colors=None, grid=True, reverse=False, fr=None):

    ny = len(data[0])
    ind = list(range(fr[0], fr[1]))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    if reverse:
        data = np.flip(data, axis=1)
        category_labels = reversed(category_labels)

    for i, row_data in enumerate(data):
        color = colors[i] if colors is not None else None
        axes.append(plt.bar(ind, row_data, bottom=cum_size,
                            label=series_labels[i], color=color, alpha=0.5))
        cum_size += row_data

    if category_labels:
        plt.xticks(ind, category_labels)

    if x_label:
        plt.xlabel(x_label)

    if y_label:
        plt.ylabel(y_label)

    plt.legend()

    if grid:
        plt.grid()

    if show_values:
        for axis in axes:
            for bar in axis:
                w, h = bar.get_width(), bar.get_height()
                plt.text(bar.get_x() + w/2, bar.get_y() + h/2,
                         value_format.format(h), ha="center",
                         va="center")
def plot_dict_bar(d, frame_ids):
    # --- plot
    def plot_one(sc, fr, id):
        f = plt.figure(figsize=(15, 10))
        series_labels = list(d.keys())
        data = [l[fr[0]:fr[1]] for l in d.values()]
        category_labels = range(fr[0], fr[1])
        colors = [np.array(c)/255.0 for c in select_COLORS.values()]

        plot_stacked_bar(
            data,
            series_labels,
            # category_labels=category_labels,
            # show_values=True,
            # value_format="{:.0f}",
            colors=colors,
            x_label="frame",
            y_label="#instance",
            fr=fr
        )
        f.savefig('./plots/'+id+'_ins_frams_'+sc+'_bar.png', bbox_inches='tight')
        plt.cla()
        plt.close(f)
    i = 1
    for sc_name, fr_list in frame_ids.items():
        plot_one(sc_name, fr_list, str(i))
        i+=1
    # plot_one('whole', [0, len(d['person'])], '0')


def merge_thing(d):
    merge_d = {}
    merge_d['person'] = d['human--person']
    merge_d['rider'] = [a+b for a,b in zip(d['human--rider--bicyclist'], d['human--rider--motorcyclist'])]
    merge_d['pole'] = d['object--support--pole']
    merge_d['traffic-light'] = d['object--traffic-light']
    merge_d['vehicle'] = [a+b+c for a,b,c in zip(d['object--vehicle--bus'],
                        d['object--vehicle--car'], d['object--vehicle--truck'])]
    merge_d['bike'] = [a+b for a,b in zip(d['object--vehicle--bicycle'],d['object--vehicle--motorcycle'])]
    return merge_d


def name2id(js):
    names = [str(p.stem).split('--')[0] for p in js]
    ids = {}
    for k, v in SCENCE_FRAME.items():
        ids[k] = [names.index(i) for i in v]
    return ids

if __name__ == '__main__':
    out_dir = '/media/jamy/My Passport/KITPS/outputs'
    ins_json_path = 'ins_plot.json'
    ins_dict = INSTANCE
    jsons = sorted(Path(out_dir).glob('*.json'))
    frame_ids = name2id(jsons)
    if not os.path.isfile(ins_json_path):
        for js in jsons:
            with open(js) as js_file:
                data = json.load(js_file)
                for k, v in ins_dict.items():
                    v.append(data[k])
        json.dump(ins_dict, open(ins_json_path, 'w'), indent=4)
    else:
        ins_dict = json.load(open(ins_json_path))
    # human = dict((k, ins_dict[k]) for k in HUMAN)
    # obj = dict((k, ins_dict[k]) for k in OBJECT)
    thing = dict((k, ins_dict[k]) for k in THING)
    mg_thing = merge_thing(thing)
    # --- plot
    # plot_dict(human, "human_ins.png")
    # plot_dict(obj, "object_ins.png")
    plot_dict_bar(mg_thing, frame_ids)
    # plot_dict_line(mg_thing, frame_ids)