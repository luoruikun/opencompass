from opencompass.models import OpenAI


api_meta_template = dict(
    round=[
            dict(role='HUMAN', api_role='HUMAN'),
            dict(role='BOT', api_role='BOT', generate=True),
    ],
)

models = [
    dict(abbr='hkgai-dev1111',
        type=OpenAI, path='HKGAI-Moe-dev1111',
        key='ENV',  # The key will be obtained from $OPENAI_API_KEY, but you can write down your key here as well
        meta_template=api_meta_template,
        query_per_second=10,
        max_out_len=8 * 1024, max_seq_len=32 * 1024, batch_size=8),
]
