import streamlit as st

st.set_page_config(page_title="Tanvi's To-Do List", page_icon="🌸", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #ffe6f0, #f3e6ff);
        }
        h1, h2, h3 {
            color: #c0007a !important;
        }
        .stMarkdown p {
            color: #7a007a !important;
        }
        section[data-testid="stSidebar"] {
            display: none;
        }
        .stTextInput>div>input {
            border-radius: 20px;
            border: 2px solid #ffb6d9;
            background: white;
            color: #333;
            font-size: 16px;
            padding: 10px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff85b3, #c785f5);
            color: white;
            border: none;
            border-radius: 20px;
            padding: 10px 24px;
            font-size: 16px;
            width: 100%;
        }
        .stCheckbox label {
            color: #7a007a !important;
            font-size: 16px;
        }
        .stProgress > div > div {
            background: linear-gradient(90deg, #ff85b3, #c785f5);
        }
        @media (max-width: 768px) {
            .stTextInput>div>input {
                font-size: 14px;
            }
            h1 {
                font-size: 24px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🌸 Tanvi's To-Do List 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#9b59b6; font-style:italic; font-size:14px;'>Made with 🌟 by Wasif</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:20px;'>🌷 🌸 🌼 🌷</p>", unsafe_allow_html=True)

st.markdown("---")

if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

st.markdown("<h3 style='color:#c0007a;'>✨ Add a new task</h3>", unsafe_allow_html=True)
col1, col2 = st.columns([4, 1])
with col1:
    new_task = st.text_input("", placeholder="What do you need to do? 🌸", label_visibility="collapsed", key=f"input_{st.session_state.input_key}")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Add 🌸"):
        if new_task.strip() != "":
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.session_state.input_key += 1
            st.rerun()

st.markdown("---")
st.markdown("<h3 style='color:#c0007a;'>📋 Your Tasks</h3>", unsafe_allow_html=True)

if len(st.session_state.tasks) == 0:
    st.markdown("<p style='color:#9b59b6; text-align:center; font-size:16px;'>No tasks yet! Add something 🌸</p>", unsafe_allow_html=True)
else:
    total = len(st.session_state.tasks)
    done_count = sum(1 for t in st.session_state.tasks if t["done"])

    st.progress(done_count / total)
    st.markdown(f"<p style='color:#9b59b6;'>✅ {done_count} of {total} tasks completed</p>", unsafe_allow_html=True)

    if done_count == total and total > 0:
        st.balloons()
        st.markdown("<h3 style='text-align:center; color:#c0007a;'>🌟 All done! Amazing work! 🌟</h3>", unsafe_allow_html=True)

    to_delete = None
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([5, 1])
        with col1:
            checked = st.checkbox(
                task["task"],
                value=task["done"],
                key=f"task_{i}"
            )
            st.session_state.tasks[i]["done"] = checked
        with col2:
            if st.button("🗑️", key=f"del_{i}"):
                to_delete = i

    if to_delete is not None:
        st.session_state.tasks.pop(to_delete)
        st.rerun()

st.markdown("---")
st.markdown("<p style='text-align:center; color:#c0007a; font-size:15px;'>💪 You're doing great, keep going! 🌸</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#9b59b6; font-size:12px;'>Made with 🌟 by Wasif</p>", unsafe_allow_html=True)
