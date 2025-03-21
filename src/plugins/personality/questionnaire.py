# 人格测试问卷题目 王孟成, 戴晓阳, & 姚树桥. (2011). 中国大五人格问卷的初步编制Ⅲ:简式版的制定及信效度检验. 
# 中国临床心理学杂志, 19(04), Article 04.
# 王孟成, 戴晓阳, & 姚树桥. (2010). 中国大五人格问卷的初步编制Ⅰ:理论框架与信度分析. 
# 中国临床心理学杂志, 18(05), Article 05.

PERSONALITY_QUESTIONS = [
    # 神经质维度 (F1)
    {"id": 1, "content": "我常担心有什么不好的事情要发生", "factor": "神经质", "reverse_scoring": False},
    {"id": 2, "content": "我常感到害怕", "factor": "神经质", "reverse_scoring": False},
    {"id": 3, "content": "有时我觉得自己一无是处", "factor": "神经质", "reverse_scoring": False},
    {"id": 4, "content": "我很少感到忧郁或沮丧", "factor": "神经质", "reverse_scoring": True},
    {"id": 5, "content": "别人一句漫不经心的话，我常会联系在自己身上", 
     "factor": "神经质", "reverse_scoring": False},
    {"id": 6, "content": "在面对压力时，我有种快要崩溃的感觉", 
     "factor": "神经质", "reverse_scoring": False},
    {"id": 7, "content": "我常担忧一些无关紧要的事情", 
     "factor": "神经质", "reverse_scoring": False},
    {"id": 8, "content": "我常常感到内心不踏实", 
     "factor": "神经质", "reverse_scoring": False},
    
    # 严谨性维度 (F2)
    {"id": 9, "content": "在工作上，我常只求能应付过去便可", 
     "factor": "严谨性", "reverse_scoring": True},
    {"id": 10, "content": "一旦确定了目标，我会坚持努力地实现它", 
      "factor": "严谨性", "reverse_scoring": False},
    {"id": 11, "content": "我常常是仔细考虑之后才做出决定", 
      "factor": "严谨性", "reverse_scoring": False},
    {"id": 12, "content": "别人认为我是个慎重的人", 
      "factor": "严谨性", "reverse_scoring": False},
    {"id": 13, "content": "做事讲究逻辑和条理是我的一个特点", 
      "factor": "严谨性", "reverse_scoring": False},
    {"id": 14, "content": "我喜欢一开头就把事情计划好", 
      "factor": "严谨性", "reverse_scoring": False},
    {"id": 15, "content": "我工作或学习很勤奋", 
      "factor": "严谨性", "reverse_scoring": False},
    {"id": 16, "content": "我是个倾尽全力做事的人", 
      "factor": "严谨性", "reverse_scoring": False},
    
    # 宜人性维度 (F3)
    {"id": 17, "content": "尽管人类社会存在着一些阴暗的东西（如战争、罪恶、欺诈），"
      "我仍然相信人性总的来说是善良的", "factor": "宜人性", "reverse_scoring": False},
    {"id": 18, "content": "我觉得大部分人基本上是心怀善意的", 
      "factor": "宜人性", "reverse_scoring": False},
    {"id": 19, "content": "虽然社会上有骗子，但我觉得大部分人还是可信的", 
      "factor": "宜人性", "reverse_scoring": False},
    {"id": 20, "content": "我不太关心别人是否受到不公正的待遇", 
      "factor": "宜人性", "reverse_scoring": True},
    {"id": 21, "content": "我时常觉得别人的痛苦与我无关", 
      "factor": "宜人性", "reverse_scoring": True},
    {"id": 22, "content": "我常为那些遭遇不幸的人感到难过", 
      "factor": "宜人性", "reverse_scoring": False},
    {"id": 23, "content": "我是那种只照顾好自己，不替别人担忧的人", 
      "factor": "宜人性", "reverse_scoring": True},
    {"id": 24, "content": "当别人向我诉说不幸时，我常感到难过", 
      "factor": "宜人性", "reverse_scoring": False},
    
    # 开放性维度 (F4)
    {"id": 25, "content": "我的想象力相当丰富", 
      "factor": "开放性", "reverse_scoring": False},
    {"id": 26, "content": "我头脑中经常充满生动的画面", 
      "factor": "开放性", "reverse_scoring": False},
    {"id": 27, "content": "我对许多事情有着很强的好奇心", 
      "factor": "开放性", "reverse_scoring": False},
    {"id": 28, "content": "我喜欢冒险", 
      "factor": "开放性", "reverse_scoring": False},
    {"id": 29, "content": "我是个勇于冒险，突破常规的人", 
      "factor": "开放性", "reverse_scoring": False},
    {"id": 30, "content": "我身上具有别人没有的冒险精神", 
      "factor": "开放性", "reverse_scoring": False},
    {"id": 31, "content": "我渴望学习一些新东西，即使它们与我的日常生活无关", 
      "factor": "开放性", "reverse_scoring": False},
    {"id": 32, "content": "我很愿意也很容易接受那些新事物、新观点、新想法", 
      "factor": "开放性", "reverse_scoring": False},
    
    # 外向性维度 (F5)
    {"id": 33, "content": "我喜欢参加社交与娱乐聚会", 
      "factor": "外向性", "reverse_scoring": False},
    {"id": 34, "content": "我对人多的聚会感到乏味", 
      "factor": "外向性", "reverse_scoring": True},
    {"id": 35, "content": "我尽量避免参加人多的聚会和嘈杂的环境", 
      "factor": "外向性", "reverse_scoring": True},
    {"id": 36, "content": "在热闹的聚会上，我常常表现主动并尽情玩耍", 
      "factor": "外向性", "reverse_scoring": False},
    {"id": 37, "content": "有我在的场合一般不会冷场", 
      "factor": "外向性", "reverse_scoring": False},
    {"id": 38, "content": "我希望成为领导者而不是被领导者", 
      "factor": "外向性", "reverse_scoring": False},
    {"id": 39, "content": "在一个团体中，我希望处于领导地位", 
      "factor": "外向性", "reverse_scoring": False},
    {"id": 40, "content": "别人多认为我是一个热情和友好的人", 
      "factor": "外向性", "reverse_scoring": False}
]

# 因子维度说明
FACTOR_DESCRIPTIONS = {
    "外向性": {
        "description": (
            "反映个体神经系统的强弱和动力特征。外向性主要表现为个体在人际交往和社交活动中的倾向性，"
            "包括对社交活动的兴趣、对人群的态度、社交互动中的主动程度以及在群体中的影响力。"
            "高分者倾向于积极参与社交活动，乐于与人交往，善于表达自我，并往往在群体中发挥领导作用；"
            "低分者则倾向于独处，不喜欢热闹的社交场合，表现出内向、安静的特征。"
        ),
        "trait_words": ["热情", "活力", "社交", "主动"],
        "subfactors": {
            "合群性": "个体愿意与他人聚在一起，即接近人群的倾向；高分表现乐群、好交际，低分表现封闭、独处",
            "热情": "个体对待别人时所表现出的态度；高分表现热情好客，低分表现冷淡",
            "支配性": "个体喜欢指使、操纵他人，倾向于领导别人的特点；高分表现好强、发号施令，低分表现顺从、低调",
            "活跃": "个体精力充沛，活跃、主动性等特点；高分表现活跃，低分表现安静"
        }
    },
    "神经质": {
        "description": (
            "反映个体情绪的状态和体验内心苦恼的倾向性。这个维度主要关注个体在面对压力、挫折和"
            "日常生活挑战时的情绪稳定性和适应能力。它包含了对焦虑、抑郁、愤怒等负面情绪的敏感程度，"
            "以及个体对这些情绪的调节和控制能力。高分者容易体验负面情绪，对压力较为敏感，情绪波动较大；"
            "低分者则表现出较强的情绪稳定性，能够较好地应对压力和挫折。"
        ),
        "trait_words": ["稳定", "沉着", "从容", "坚韧"],
        "subfactors": {
            "焦虑": "个体体验焦虑感的个体差异；高分表现坐立不安，低分表现平静",
            "抑郁": "个体体验抑郁情感的个体差异；高分表现郁郁寡欢，低分表现平静",
            "敏感多疑": "个体常常关注自己的内心活动，行为和过于意识人对自己的看法、评价；"
                       "高分表现敏感多疑，低分表现淡定、自信",
            "脆弱性": "个体在危机或困难面前无力、脆弱的特点；高分表现无能、易受伤、逃避，低分表现坚强",
            "愤怒-敌意": "个体准备体验愤怒，及相关情绪的状态；高分表现暴躁易怒，低分表现平静"
        }
    },
    "严谨性": {
        "description": (
            "反映个体在目标导向行为上的组织、坚持和动机特征。这个维度体现了个体在工作、学习等"
            "目标性活动中的自我约束和行为管理能力。它涉及到个体的责任感、自律性、计划性、条理性以及"
            "完成任务的态度。高分者往往表现出强烈的责任心、良好的组织能力、谨慎的决策风格和持续的"
            "努力精神；低分者则可能表现出随意性强、缺乏规划、做事马虎或易放弃的特点。"
        ),
        "trait_words": ["负责", "自律", "条理", "勤奋"],
        "subfactors": {
            "责任心": "个体对待任务和他人认真负责，以及对自己承诺的信守；"
                     "高分表现有责任心、负责任，低分表现推卸责任、逃避处罚",
            "自我控制": "个体约束自己的能力，及自始至终的坚持性；高分表现自制、有毅力，低分表现冲动、无毅力",
            "审慎性": "个体在采取具体行动前的心理状态；高分表现谨慎、小心，低分表现鲁莽、草率",
            "条理性": "个体处理事务和工作的秩序，条理和逻辑性；高分表现整洁、有秩序，低分表现混乱、遗漏",
            "勤奋": "个体工作和学习的努力程度及为达到目标而表现出的进取精神；高分表现勤奋、刻苦，低分表现懒散"
        }
    },
    "开放性": {
        "description": (
            "反映个体对新异事物、新观念和新经验的接受程度，以及在思维和行为方面的创新倾向。"
            "这个维度体现了个体在认知和体验方面的广度、深度和灵活性。它包括对艺术的欣赏能力、"
            "对知识的求知欲、想象力的丰富程度，以及对冒险和创新的态度。高分者往往具有丰富的想象力、"
            "广泛的兴趣、开放的思维方式和创新的倾向；低分者则倾向于保守、传统，喜欢熟悉和常规的事物。"
        ),
        "trait_words": ["创新", "好奇", "艺术", "冒险"],
        "subfactors": {
            "幻想": "个体富于幻想和想象的水平；高分表现想象力丰富，低分表现想象力匮乏",
            "审美": "个体对于艺术和美的敏感与热爱程度；高分表现富有艺术气息，低分表现一般对艺术不敏感",
            "好奇心": "个体对未知事物的态度；高分表现兴趣广泛、好奇心浓，低分表现兴趣少、无好奇心",
            "冒险精神": "个体愿意尝试有风险活动的个体差异；高分表现好冒险，低分表现保守",
            "价值观念": "个体对新事物、新观念、怪异想法的态度；高分表现开放、坦然接受新事物，低分则相反"
        }
    },
    "宜人性": {
        "description": (
            "反映个体在人际关系中的亲和倾向，体现了对他人的关心、同情和合作意愿。这个维度主要"
            "关注个体与他人互动时的态度和行为特征，包括对他人的信任程度、同理心水平、助人意愿以及"
            "在人际冲突中的处理方式。高分者通常表现出友善、富有同情心、乐于助人的特质，善于与他人"
            "建立和谐关系；低分者则可能表现出较少的人际关注，在社交互动中更注重自身利益，较少考虑"
            "他人感受。"
        ),
        "trait_words": ["友善", "同理", "信任", "合作"],
        "subfactors": {
            "信任": "个体对他人和/或他人言论的相信程度；高分表现信任他人，低分表现怀疑",
            "体贴": "个体对别人的兴趣和需要的关注程度；高分表现体贴、温存，低分表现冷漠、不在乎",
            "同情": "个体对处于不利地位的人或物的态度；高分表现富有同情心，低分表现冷漠"
        }
    }
} 