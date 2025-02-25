import json

cmmlu_subject_mapping = {
    'agronomy': '农学',
    'anatomy': '解剖学',
    'ancient_chinese': '古汉语',
    'arts': '艺术学',
    'astronomy': '天文学',
    'business_ethics': '商业伦理',
    'chinese_civil_service_exam': '中国公务员考试',
    'chinese_driving_rule': '中国驾驶规则',
    'chinese_food_culture': '中国饮食文化',
    'chinese_foreign_policy': '中国外交政策',
    'chinese_history': '中国历史',
    'chinese_literature': '中国文学',
    'chinese_teacher_qualification': '中国教师资格',
    'clinical_knowledge': '临床知识',
    'college_actuarial_science': '大学精算学',
    'college_education': '大学教育学',
    'college_engineering_hydrology': '大学工程水文学',
    'college_law': '大学法律',
    'college_mathematics': '大学数学',
    'college_medical_statistics': '大学医学统计',
    'college_medicine': '大学医学',
    'computer_science': '计算机科学',
    'computer_security': '计算机安全',
    'conceptual_physics': '概念物理学',
    'construction_project_management': '建设工程管理',
    'economics': '经济学',
    'education': '教育学',
    'electrical_engineering': '电气工程',
    'elementary_chinese': '小学语文',
    'elementary_commonsense': '小学常识',
    'elementary_information_and_technology': '小学信息技术',
    'elementary_mathematics': '初等数学',
    'ethnology': '民族学',
    'food_science': '食品科学',
    'genetics': '遗传学',
    'global_facts': '全球事实',
    'high_school_biology': '高中生物',
    'high_school_chemistry': '高中化学',
    'high_school_geography': '高中地理',
    'high_school_mathematics': '高中数学',
    'high_school_physics': '高中物理学',
    'high_school_politics': '高中政治',
    'human_sexuality': '人类性行为',
    'international_law': '国际法学',
    'journalism': '新闻学',
    'jurisprudence': '法理学',
    'legal_and_moral_basis': '法律与道德基础',
    'logical': '逻辑学',
    'machine_learning': '机器学习',
    'management': '管理学',
    'marketing': '市场营销',
    'marxist_theory': '马克思主义理论',
    'modern_chinese': '现代汉语',
    'nutrition': '营养学',
    'philosophy': '哲学',
    'professional_accounting': '专业会计',
    'professional_law': '专业法学',
    'professional_medicine': '专业医学',
    'professional_psychology': '专业心理学',
    'public_relations': '公共关系',
    'security_study': '安全研究',
    'sociology': '社会学',
    'sports_science': '体育学',
    'traditional_chinese_medicine': '中医中药',
    'virology': '病毒学',
    'world_history': '世界历史',
    'world_religions': '世界宗教'
}

mmlu_pro_categories = [
    'math',
    'physics',
    'chemistry',
    'law',
    'engineering',
    'other',
    'economics',
    'health',
    'psychology',
    'business',
    'biology',
    'philosophy',
    'computer science',
    'history',
]

def gen_eval_mini_score(time_str, model_name):

    metrics = {}

    # CMMLU
    all_scores = []

    for subject in cmmlu_subject_mapping.keys():
        with open(f'outputs/default/{time_str}/results/{model_name}/demo_cmmlu-{subject}.json') as f:
            data = json.load(f)
            all_scores.append(data['accuracy'])
    
    metrics['cmmlu'] = sum(all_scores) / len(all_scores)

    # MMLU PRO
    all_scores = []

    for category in mmlu_pro_categories:
        category = category.replace(' ', '_')
        with open(f'outputs/default/{time_str}/results/{model_name}/demo_mmlu_pro_{category}.json') as f:
            data = json.load(f)
            all_scores.append(data['accuracy'])
    
    metrics['mmlu_pro'] = sum(all_scores) / len(all_scores)

    # GPQA
    with open(f'outputs/default/{time_str}/results/{model_name}/demo_GPQA_diamond.json') as f:
        data = json.load(f)
        metrics['gpqa'] = data['accuracy']
    
    # humaneval
    with open(f'outputs/default/{time_str}/results/{model_name}/openai_humaneval.json') as f:
        data = json.load(f)
        metrics['humaneval'] = data['humaneval_pass@1']
    
    # IFEval
    with open(f'outputs/default/{time_str}/results/{model_name}/IFEval.json') as f:
        data = json.load(f)
        metrics['ifeval'] = data['Prompt-level-strict-accuracy']
    
    # dump metrics
    with open(f'./tmp.json', 'w') as f:
        json.dump(metrics, f, indent=4)
    
    print(metrics)

if __name__ == '__main__':
    gen_eval_mini_score('20250224_134405', 'hkgai-dev')

