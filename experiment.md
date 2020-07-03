## Experiment result

**Inference time** on different resolutions and GPUs:

Given shortest_size then upscale with same ratio, check `seamseg/data/transform.py ISSTestTransform._adjusted_scale()`

|           | GeForce 940MX (s) | GTX 1080Ti |
| --------- | ----------------- | ---------- |
| 240, 320  | 0.829             |            |
| 480, 640  | 1.312             |            |
| 960, 1280 | 2.261             |            |

