import streamlit as st
import time
# 設定網頁標題，以及使用寬屏模式
st.set_page_config(
    page_title="運維管理後臺",
    layout="wide"

)
# 隱藏右邊的選單以及頁尾
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# 左邊導航欄
sidebar = st.sidebar.radio(
    "導航欄",
    ("首頁", "專案管理", "使用者管理", "許可權管理")
)
if sidebar == "專案管理":
    st.title("專案管理")
    # 專案選擇框
    project_name = st.selectbox(
        "請選擇專案",
        ["專案A", "專案B"]
    )
    if project_name:
        # 表單
        with st.form(project_name):
            project_info_1 = st.text_input("專案資訊1", project_name)
            project_info_2 = st.text_input("專案資訊2", project_name)
            project_info_3 = st.text_input("專案資訊3", project_name)
            submitted = st.form_submit_button("提交")
            if submitted:
                # 在這裡新增真實的業務邏輯
                # 這是一個進度條
                bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    bar.progress(i)
                st.write("專案資訊1:%s, 專案資訊2:%s, 專案資訊3:%s" % (project_info_1, project_info_2, project_info_3))
                st.success("提交成功")


elif sidebar == "使用者管理":
    st.title("使用者管理")
    # 將頁面分為左半邊和右半邊
    left, right = st.beta_columns(2)
    # 左半邊頁面展示部分
    with left:
        st.header("檢視、更新使用者資訊")
        user_name = st.selectbox(
            "請選擇使用者",
            ["鄭立賽", "賈伯斯", "王大拿"]
        )
        if user_name:
            with st.form(user_name):
                phone_num = st.text_input("手機號", user_name)
                role = st.multiselect(
                    "使用者角色",
                    ["大神", "大拿"],
                    ["大神"]
                )
                user_group = st.multiselect(
                    "請選擇使用者組",
                    ["大神組", "大拿組"],
                    ["大神組"]
                )
                submitted = st.form_submit_button("提交")
                if submitted:
                    # 這裡新增真實的業務邏輯
                    st.write("使用者名稱:%s, 手機號:%s, 使用者角色:%s, 使用者組:%s" % (user_name, phone_num, role, user_group))
                    st.success("提交成功")
    # 右半邊頁面展示部分
    with right:
        st.header("新增、刪除使用者")
        user_action = st.selectbox(
            "請選擇操作",
            ["新增使用者", "刪除使用者"]
        )
        if user_action:
            with st.form(user_action):
                if user_action == "新增使用者":
                    phone_num = st.text_input("手機號", user_name)
                    role = st.multiselect(
                        "使用者角色",
                        ["大神", "大拿"]
                    )
                    user_group = st.multiselect(
                        "請選擇使用者組",
                        ["大神組", "大拿組"]
                    )
                    submitted = st.form_submit_button("提交")
                    if submitted:
                        # 請在這裡新增真實業務邏輯，或者單獨寫一個業務邏輯函式
                        st.write("user_name:%s, phone_num:%s, role:%s, user_group:%s" % (user_name, phone_num, role, user_group))
                        st.success("提交成功")
                else:
                    user_group = st.multiselect(
                        "請選擇要刪除的使用者",
                        ["鄭立賽", "賈伯斯", "王大拿"]
                    )
                    submitted = st.form_submit_button("提交")
                    if submitted:
                        # 請在這裡新增真實業務邏輯，或者單獨寫一個業務邏輯函式
                        st.write("user_name:%s, phone_num:%s, role:%s, user_group:%s" % (user_name, phone_num, role, user_group))
                        st.success("提交成功")
elif sidebar == "許可權管理":
    st.title("許可權管理")
    with st.form("auth"):
        user = st.multiselect(
            "選擇使用者",
            ["鄭立賽", "賈伯斯", "王大拿"]
        )
        role = st.multiselect(
            "選擇使用者角色",
            ["大神", "大拿"]
        )
        user_group = st.multiselect(
            "請選擇使用者組",
            ["大神組", "大拿組"]
        )
        submitted = st.form_submit_button("提交")
        if submitted:
            # 請在這裡新增真實業務邏輯，或者單獨寫一個業務邏輯函式
            st.write(
                "使用者:%s, 角色:%s, 使用者組:%s" % (user, role, user_group))
            st.success("提交成功")
else:
    st.title("運維管理後臺")
    st.write("歡迎使用運維管理後臺")
