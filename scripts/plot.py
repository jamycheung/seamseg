import json
from pathlib import Path
import matplotlib.pyplot as plt
# === dict of instance categories
#     "animal--bird": 0,
#     "animal--ground-animal": 0,
#     "construction--flat--crosswalk-plain": 0,
#     "human--person": 14,
#     "human--rider--bicyclist": 0,
#     "human--rider--motorcyclist": 0,
#     "human--rider--other-rider": 0,
#     "marking--crosswalk-zebra": 1,
#     "object--banner": 0,
#     "object--bench": 0,
#     "object--bike-rack": 0,
#     "object--billboard": 0,
#     "object--catch-basin": 0,
#     "object--cctv-camera": 0,
#     "object--fire-hydrant": 0,
#     "object--junction-box": 0,
#     "object--mailbox": 0,
#     "object--manhole": 0,
#     "object--phone-booth": 0,
#     "object--street-light": 2,
#     "object--support--pole": 11,
#     "object--support--traffic-sign-frame": 0,
#     "object--support--utility-pole": 0,
#     "object--traffic-light": 3,
#     "object--traffic-sign--back": 1,
#     "object--traffic-sign--front": 2,
#     "object--trash-can": 0,
#     "object--vehicle--bicycle": 0,
#     "object--vehicle--boat": 0,
#     "object--vehicle--bus": 0,
#     "object--vehicle--car": 1,
#     "object--vehicle--caravan": 0,
#     "object--vehicle--motorcycle": 0,
#     "object--vehicle--other-vehicle": 0,
#     "object--vehicle--trailer": 0,
#     "object--vehicle--truck": 0,
#     "object--vehicle--wheeled-slow": 0


if __name__ == '__main__':
    out_dir = './data/outputs'
    jsons = sorted(Path(out_dir).glob('*.json'))
    plts = {
        "human--person": [],
        "object--support--pole": [],
        "object--vehicle--car": []
    }
    for js in jsons:
        with open(js) as js_file:
            data = json.load(js_file)
            for k, v in plts.items():
                v.append(data[k])
    json.dump(plts, open('ins_plot.json', 'w'), indent=4)
    # --- plot
    f = plt.figure()
    for k, v in plts.items():
        plt.plot(range(1, len(v) + 1), v,
                 linestyle='--', marker='o',
                 label=k.split('--')[-1])
    plt.xlabel('frame')
    plt.ylabel('#instance')
    plt.legend()
    # plt.show()
    f.savefig("ins_plot.pdf", bbox_inches='tight')
