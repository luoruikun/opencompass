from mmengine import read_base

with read_base():
    from ..mmlu_pro.mmlu_pro_few_shot_gen_bfaf90 import mmlu_pro_datasets

for d in mmlu_pro_datasets:
    d['abbr'] = 'demo_' + d['abbr']
    d['reader_cfg']['test_range'] = '[0:500]'
