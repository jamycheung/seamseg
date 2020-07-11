CUDA_VISIBLE_DEVICES=0,1 python -m torch.distributed.launch --nproc_per_node=2 eval_panoptic.py \
--log_dir logs \
--resume seamseg_r50_vistas.tar \
--eval \
config_eval.ini \
data/mvd