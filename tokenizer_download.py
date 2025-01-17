from transformers import AutoTokenizer
import os

# 设置环境变量
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["TRANSFORMERS_MODEL_HUB_URL"] = f"{os.environ['HF_ENDPOINT']}models"
os.environ["DATASETS_HF_ENDPOINT"] = f"{os.environ['HF_ENDPOINT']}datasets"
# 指定你想要保存 tokenizer 的本地路径
local_model_path = "./t5-base-tokenizer"

# 下载并保存 tokenizer 到本地路径
tokenizer = AutoTokenizer.from_pretrained("t5-base", model_max_length=512)
tokenizer.save_pretrained(local_model_path)