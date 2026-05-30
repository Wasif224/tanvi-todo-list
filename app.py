import streamlit as st

st.set_page_config(page_title="Tanvi's To-Do List", page_icon="🌸")

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #ffe6f0, #f3e6ff);
        }
        .task-card {
            background: white;
            padding: 10px 20px;
            border-radius: 15px;
            margin: 8px 0;
            box-shadow: 2px 2px 10px rgba(255,182,193,0.4);
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff85b3, #c785f5);
            color: white;
            border: none;
            border-radius: 20px;
            padding: 8px 20px;
        }
        .stTextInput>div>input {
            border-radius: 20px;
            border: 2px solid #ffb6d9;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#d63384;'>🌸 Tanvi's To-Do List 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#9b59b6; font-style:italic;'>Made with 💕 by Wasif</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:22px;'>🌷🌺🌸🌼🌷</p>", unsafe_allow_html=True)

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.markdown("### ✨ Add a new task")
col1, col2 = st.columns([4, 1])
with col1:
    new_task = st.text_input("", placeholder="Enter something cute to do 🌸")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Add 🌸"):
        if new_task.strip() != "":
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.rerun()

st.markdown("### 📋 Your Tasks")

if len(st.session_state.tasks) == 0:
    st.markdown("<p style='color:#c485f5; text-align:center;'>No tasks yet! Add something cute 🌸</p>", unsafe_allow_html=True)
else:
    total = len(st.session_state.tasks)
    done_count = sum(1 for t in st.session_state.tasks if t["done"])
    st.progress(done_count / total)
    st.markdown(f"<p style='color:#9b59b6;'>✅ {done_count} of {total} tasks done!</p>", unsafe_allow_html=True)

    if done_count == total:
        st.balloons()
        st.markdown("<h3 style='text-align:center; color:#d63384;'>🌟 All done! You're a star! ⭐🌸</h3>", unsafe_allow_html=True)

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
st.markdown("<p style='text-align:center; color:#d63384;'>💪 You're doing amazing! Keep going! 🌸</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#9b59b6; font-size:12px;'>Made with 💕 by Wasif</p>", unsafe_allow_html=True)
