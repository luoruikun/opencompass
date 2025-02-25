from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.demo.demo_cmmlu_chat_gen import \
        cmmlu_datasets
    from opencompass.configs.datasets.demo.demo_gpqa_chat_gen import \
        gpqa_datasets
    from opencompass.configs.datasets.demo.demo_mmlupro_chat_gen import \
        mmlu_pro_datasets
    from opencompass.configs.datasets.humaneval.humaneval_gen import \
        humaneval_datasets
    from opencompass.configs.datasets.IFEval.IFEval_gen import \
        ifeval_datasets
    
    # from opencompass.configs.models.openai.gpt_4o_2024_05_13 import \
    #     models as model

    # qwen2.5-7b
    # from opencompass.configs.models.hkgai.qwen2_5_7b import \
    #     models as model

    # dev
    from opencompass.configs.models.hkgai.dev import \
        models as model

datasets = cmmlu_datasets + gpqa_datasets + mmlu_pro_datasets + humaneval_datasets + ifeval_datasets
# datasets = humaneval_datasets
# datasets = ifeval_datasets
models = model
