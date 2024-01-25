# -*- encoding: utf-8 -*-
"""
@File       :  text_demo.py
@Contact    :  harvey.wxia@gmail.com
@License    :  (C)Copyright 2020-2021
-------------------------------------
@Modify Time:  2022/2/15 5:07 PM
@Author     :  xiawei
@Version    :  1.0
@Description :
启动方法 streamlit run app.py
"""
import configparser

import spacy_streamlit
from pathlib import Path
import srsly
import importlib
import streamlit as st

TITLE = "自然语言处理"
MODELS = srsly.read_json(Path(__file__).parent / "models.json")
DEFAULT_MODEL = "zh_core_web_sm"
DEFAULT_TEXT = "北京时间2月15日，2022年北京奥运会单板滑雪男子大跳台决赛继续进行，结果苏翊鸣凭借前两轮的完美发挥，" \
               "以182.50的总分夺得中国军团本届冬奥会上的第六金，也创造了中国在这个项目上的最好成绩！"
# DESCRIPTION = """**Explore trained [spaCy v3.0](https://nightly.spacy.io) pipelines**"""
DESCRIPTION = "工业级的自然语言处理"


def get_default_text(nlp):
    """
    获取默认语句
    Check if spaCy has built-in example texts for the language
    :param nlp:
    :return: 默认的语句
    """
    try:
        examples = importlib.import_module(f".lang.{nlp.lang}.examples", "spacy")
        print(examples.sentences[0])
        print(type(examples.sentences[0]))
        # return examples.sentences[0]
        return DEFAULT_TEXT
    except (ModuleNotFoundError, ImportError):
        return ""


spacy_streamlit.visualize(
    MODELS,
    default_model=DEFAULT_MODEL,
    visualizers=["ner", "parser", "tokens"],
    # visualizers=["parser", "ner"],
    # ner_labels=["PERSON"],
    show_visualizer_select=True,
    sidebar_description=DESCRIPTION,
    show_pipeline_info=True,
    get_default_text=get_default_text,
    sidebar_title=f"{TITLE}",
    show_logo=False,
    show_json_doc=True,
    show_meta=False,
    show_config=False
)

# ---------------------utils------------------------------------
# def check_login(username: str, password: str):
#     config = configparser.ConfigParser()
#     config.read('user_info.ini')
#     if username == config['USER_INFO']['username'] and password == config['USER_INFO']['password']:
#         return True
#     return False
#
# def login_user(username,password):
#     if check_login(username,password):
#         return True
#     else:
#         st.warning("用户名不存在，请先选择注册按钮完成注册。")
#         return False
# # ---------------------utils------------------------------------
#
# if 'count' not in st.session_state:
#     st.session_state.count = 0


# --------------登录---------------------------
# login_title = st.sidebar.subheader("登录区域")
# username = st.sidebar.text_input("用户名")
# password = st.sidebar.text_input("密码", type= "password")
# logged_user = login_user(username,password)
# if logged_user:
#     st.session_state.count += 1
#     if st.session_state.count >= 1:
#
#         spacy_streamlit.visualize(
#             MODELS,
#             default_model=DEFAULT_MODEL,
#             visualizers=["parser", "ner", "similarity", "tokens"],
#             show_visualizer_select=True,
#             sidebar_description=DESCRIPTION,
#             get_default_text=get_default_text
#         )

FOOTER = """
<span style="font-size: 1em">&hearts; Built by [`bchren.fun`](https://bchren.fun/en/spacy/)
</span>"""

st.sidebar.markdown(
        FOOTER,
        unsafe_allow_html=True,
    )
