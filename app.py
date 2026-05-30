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
            color: #7a007a !important;
            font-size: 16px;
            padding: 10px;
        }
        .stTextInput>div>input::placeholder {
            color: #c485f5 !important;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff85b3, #c785f5);
            color: white !important;
            border: none;
            border-radius: 20px;
            padding: 12px 24px;
            font-size: 16px;
            width: 100%;
            margin: 5px 0;
        }
        .stCheckbox label p {
            color: #7a007a !important;
            font-size: 16px !important;
        }
        .stCheckbox label {
            color: #7a007a !important;
            font-size: 16px !important;
        }
        .stCheckbox span {
            color: #7a007a !important;
        }
        div[data-testid="stCheckbox"] label {
            color: #7a007a !important;
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

if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "input_key" not in st.session_state:
    st.session_state.input_key = 0
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- HOME PAGE ---
if st.session_state.page == "home":
    st.markdown(" ")
    st.markdown(" ")
    st.markdown("<h1 style='text-align:center;'>🌸 Tanvi's To-Do List 🌸</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#9b59b6; font-style:italic; font-size:14px;'>Made by Wasif🌟</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:20px;'>🌷 🌸 🌼 🌷</p>", unsafe_allow_html=True)
    st.markdown(" ")

    total = len(st.session_state.tasks)
    done_count = sum(1 for t in st.session_state.tasks if t["done"])
    st.markdown(f"<p style='text-align:center; color:#9b59b6; font-size:16px;'>📋 {total} tasks &nbsp;|&nbsp; ✅ {done_count} completed</p>", unsafe_allow_html=True)

    st.markdown(" ")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📋  View My Tasks"):
            st.session_state.page = "view"
            st.rerun()
        st.markdown(" ")
        if st.button("➕  Add a Task"):
            st.session_state.page = "add"
            st.rerun()
        st.markdown(" ")
        if st.button("🗑️  Delete a Task"):
            st.session_state.page = "delete"
            st.rerun()

    st.markdown(" ")
    st.markdown(" ")
    st.markdown("<p style='text-align:center; color:#c0007a; font-size:14px;'>💪 You're doing great, keep going! 🌸</p>", unsafe_allow_html=True)

# --- VIEW TASKS PAGE ---
elif st.session_state.page == "view":
    st.markdown("<h2 style='text-align:center;'>📋 Your Tasks</h2>", unsafe_allow_html=True)
    st.markdown(" ")

    if len(st.session_state.tasks) == 0:
        st.markdown("<p style='color:#9b59b6; text-align:center; font-size:16px;'>No tasks yet! Add something 🌸</p>", unsafe_allow_html=True)
    else:
        total = len(st.session_state.tasks)
        done_count = sum(1 for t in st.session_state.tasks if t["done"])
        st.progress(done_count / total)
        st.markdown(f"<p style='color:#9b59b6;'>✅ {done_count} of {total} tasks completed</p>", unsafe_allow_html=True)
        st.markdown(" ")

        if done_count == total and total > 0:
            st.balloons()
            st.markdown("<h3 style='text-align:center; color:#c0007a;'>🌟 All done! Amazing work! 🌟</h3>", unsafe_allow_html=True)

        for i, task in enumerate(st.session_state.tasks):
            checked = st.checkbox(
                task["task"],
                value=task["done"],
                key=f"task_{i}"
            )
            st.session_state.tasks[i]["done"] = checked

    st.markdown(" ")
    if st.button("⬅️  Back to Home"):
        st.session_state.page = "home"
        st.rerun()

# --- ADD TASK PAGE ---
elif st.session_state.page == "add":
    st.markdown("<h2 style='text-align:center;'>➕ Add a New Task</h2>", unsafe_allow_html=True)
    st.markdown(" ")

    new_task = st.text_input("", placeholder="What do you need to do? 🌸", label_visibility="collapsed", key=f"input_{st.session_state.input_key}")

    st.markdown(" ")
    if st.button("Add Task 🌸"):
        if new_task.strip() != "":
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.session_state.input_key += 1
            st.success("Task added! ✅")
            st.rerun()
        else:
            st.warning("Please type something first! 🌸")

    st.markdown(" ")
    if st.button("⬅️  Back to Home"):
        st.session_state.page = "home"
        st.rerun()

# --- DELETE TASK PAGE ---
elif st.session_state.page == "delete":
    st.markdown("<h2 style='text-align:center;'>🗑️ Delete a Task</h2>", unsafe_allow_html=True)
    st.markdown(" ")

    if len(st.session_state.tasks) == 0:
        st.markdown("<p style='color:#9b59b6; text-align:center;'>No tasks to delete! 🌸</p>", unsafe_allow_html=True)
    else:
        to_delete = None
        for i, task in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([5, 1])
            with col1:
                checkbox = "✅" if task["done"] else "⬜"
                st.markdown(f"<p style='color:#7a007a; font-size:16px; padding-top:8px;'>{checkbox} {task['task']}</p>", unsafe_allow_html=True)
            with col2:
                if st.button("🗑️", key=f"del_{i}"):
                    to_delete = i

        if to_delete is not None:
            st.session_state.tasks.pop(to_delete)
            st.rerun()

    st.markdown(" ")
    if st.button("⬅️  Back to Home"):
        st.session_state.page = "home"
        st.rerun()

st.markdown(" ")
st.markdown("<p style='text-align:center; color:#9b59b6; font-size:12px;'>Made By Wasif🌟</p>", unsafe_allow_html=True)
