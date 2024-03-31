#!/bin/bash 

VOCAB_SIZE=8
MAX_LENGTH=8
N_LAYERS=3
N_HEADS_CAT=8
N_HEADS_NUM=8
N_CAT_MLPS=4
N_NUM_MLPS=4
SEED=0
DATASET="most_freq"

python src/run.py \
     --dataset "${DATASET}" \
     --vocab_size "${VOCAB_SIZE}" \
     --dataset_size 20000 \
     --min_length 1 \
     --max_length "${MAX_LENGTH}" \
     --n_epochs 250 \
     --batch_size 512 \
     --lr "5e-2" \
     --gumbel_samples 1 \
     --sample_fn "gumbel_soft" \
     --tau_init 3.0 \
     --tau_end 0.01 \
     --tau_schedule "geomspace" \
     --n_vars_cat 1 \
     --d_var "${MAX_LENGTH}" \
     --n_vars_num 1 \
     --n_layers "${N_LAYERS}" \
     --n_heads_cat "${N_HEADS_CAT}" \
     --n_heads_num "${N_HEADS_NUM}" \
     --n_cat_mlps "${N_CAT_MLPS}" \
     --n_num_mlps "${N_NUM_MLPS}" \
     --attention_type "cat" \
     --rel_pos_bias "fixed" \
     --one_hot_embed \
     --dropout 0.0 \
     --mlp_vars_in 2 \
     --d_mlp 64 \
     --count_only \
     --selector_width 0 \
     --seed "${SEED}" \
     --unique 1 \
     --save \
     --save_code \
     --output_dir "output/rasp/${DATASET}/vocab${VOCAB_SIZE}maxlen${MAX_LENGTH}/transformer_program/headsc${N_HEADS_CAT}headsn${N_HEADS_NUM}nlayers${N_LAYERS}cmlps${N_MLPS}nmlps${N_NUM_CAT_MLPS}/s${SEED}";
