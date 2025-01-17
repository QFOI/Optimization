python run_glue.py \
    --model_name_or_path roberta-base \
    --task_name mrpc \
    --enable_galore \
    --lora_all_modules \
    --max_length 512 \
    --seed=1234 \
    --lora_r 4 \
    --galore_scale 4 \
    --per_device_train_batch_size 16 \
    --update_proj_gap 500 \
    --learning_rate 3e-5 \
    --num_train_epochs 30 \
    --output_dir results/ft/roberta_base/mrpc