from mmengine import read_base

with read_base():
    from ..gpqa.gpqa_openai_simple_evals_gen_5aeece import gpqa_datasets

for d in gpqa_datasets:
    d['abbr'] = 'demo_' + d['abbr']
    d['reader_cfg']['test_range'] = '[0:500]'
