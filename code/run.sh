#!/bin/bash

# Step 1: Set up environment
echo "Setting up environment..."

# Install torch first
#pip3 install torch==2.5.1
#pip3 install -r requirements.txt

# Step 2: Prepare data paths (optional, depending on where your datasets are stored)
DATA_PATH="../dataset"
TEXT_PATH="../information"

# Step 3: Train or Evaluate the model
echo "Starting model evaluation..."
python3 main.py \
  --config_file overall/LLM_deepspeed.yaml HLLM/HLLM.yaml \
  --train_batch_size 1 \
  --MAX_TEXT_LENGTH 8 \
  --dataset "amazon_books" \
  --MAX_ITEM_LIST_LENGTH 2 \
  --checkpoint_dir ../check_points \
  --optim_args.learning_rate 1e-4 \
  --item_pretrain_dir ../check_points/ \
  --user_pretrain_dir ../check_points/ \
  --text_path $TEXT_PATH \
  --val_only True

echo "Evaluation completed."

