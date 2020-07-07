import json
import os
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
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
    'insection_1': ['0725', '0785'],
    'sidewalk_1': ['0786', '1600'],           # CS building
    'bridge': ['1601', '1930'],
    'sidewalk_2': ['1931', '2500'],           # Audimax
    'sidewalk_3': ['2800', '3400'],           # Mensa
    'sidewalk_4': ['3401', '3600'],           # Library
    'insection_2': ['3601', '3680'],          # Library
    'sidewalk_5': ['3681', '4200'],
    'insection_3': ['4201', '4300'],          # Durlach Tor
    'platform': ['4301', '4565'],
    'sidewalk_6': ['4920', '5670'],           # Rotesonne
    'insection_4': ['5720', '5870'],          # Karl Wilhelm
    'insection_5': ['5950', '6050'],
    'sidewalk_7': ['6100', '6890'],
    'insection_6': ['6891', '6920'],
    'sidewalk_8': ['6921', '6990']
}

def plot_dict(d, save_path):
    # --- plot
    f = plt.figure(figsize=(20,10))
    for k, v in d.items():
        sub_seq = v[:]
        plt.plot(range(0, len(sub_seq)), sub_seq,
                 linestyle='-', #marker='o',
                 label=k.split('--')[-1], alpha=0.5)
    plt.xlabel('frame')
    plt.ylabel('#instance')
    plt.yticks(range(1, max([max(v) for v in d.values()]), 5))
    plt.legend()
    # plt.show()
    f.savefig(save_path, bbox_inches='tight')

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


if __name__ == '__main__':
    out_dir = '/media/jamy/My Passport/KITPS/outputs'
    ins_json_path = 'ins_plot.json'
    ins_dict = INSTANCE
    jsons = sorted(Path(out_dir).glob('*.json'))
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
    plot_dict(mg_thing, 'ins_merge.png')