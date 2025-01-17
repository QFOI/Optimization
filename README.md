## 1.基于[Galore论文](https://github.com/jiaweizzhao/GaLore)中代码修改实现

### Galore配置：

```bash
pip install galore-torch
pip install -r exp_requirements.txt
```

注意请在python3.8环境下运行（实验使用版本为3.8.20）

#### 下载C4-en dataset与t5-base-tokenize

Tokenize下载

```bash
from transformers import AutoTokenizer, AutoModel

# 加载预训练的分词器和模型
tokenizer = AutoTokenizer.from_pretrained("google/t5-base")
model = AutoModel.from_pretrained("google/t5-base")

# 保存到本地
tokenizer.save_pretrained("./t5-base-tokenizer")
model.save_pretrained("./t5-base-model")
```

dataset下载

```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://hf-mirror.com/datasets/allenai/c4
cd c4
git lfs pull --include "en/*"
```

#### 运行

```bash
sh run.sh
```





## 2.ReLoRA相关实验代码地址为./GaLore/peft-training/relora.py直接运行即可