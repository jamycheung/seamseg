## Experiment result

**Inference time** on different resolutions and GPUs, with same setup: CUDA 10.1, PyTorch v1.1.0, Batch size as 1.

|           | GeForce 940MX (s) | GTX 1070 (s) | GTX 1080Ti (s) |
| --------- | ----------------- | ------------ | -------------- |
| 240, 320  | 0.829             | 0.114        | 0.158          |
| 480, 640  | 1.312             | 0.162        | 0.244          |
| 960, 1280 | 2.261             | 0.259        | 0.209          |

