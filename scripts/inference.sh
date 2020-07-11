CUDA_VISIBLE_DEVICES=0,1 python -m torch.distributed.launch --nproc_per_node=2 test_panoptic.py \
--meta metadata.bin \
--log_dir logs \
config.ini \
seamseg_r50_vistas.tar \
data/inputs \
data/outputs
