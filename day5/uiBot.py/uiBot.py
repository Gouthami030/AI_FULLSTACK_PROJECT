import ollama
import streamlit as st
st.title(":rainbow[ Welcome to chatBot ai 🤖]")
with st.sidebar:
    personalities={
        "kid👶": " give the answers like you are explaining to a 5 year old kid. give the answer in 2 lines only.",
        "professor🧑‍🏫": " you are an IIT professor. explain the topic in 2 lines only.",
        "doctor🧑‍⚕️":"you are doctor.give advises in 2 lines only."
    }
    personality = st.selectbox("select a personality", personalities.keys())
    st.badge(personality)
    st.title(":orange[***_ chat setting📜_***]")
    if st.button("clear chat"):
        st.session_state.messages.clear()
        st.success("chat cleared succesfully!!!")
    uploaded_file = st.file_uploader("upload a file...📄")
    if uploaded_file:
        st.success("file uploaded successfully...")
        with st.expander("preview"):
            context = uploaded_file.read().decode("utf-8")
            st.text(context)
if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question =st.chat_input("you:")
if question:
    with st.chat_message("user"):
        st.write("user: ",question)

st.session_state.messages.append(
    {"role":"user",
    "content":question}
)
with st.spinner("thinking...."):
    response =ollama.chat(
            model="llama3.2:3b",
            messages=[{
                "role": "sysytem"," content": personalities[personality]
            }]+st.session_state.messages)
st.session_state.messages.append(
        {"role":"assistant",
         "content":response["message"]["content"]
        }
    )
with st.chat_message("assistant"):
    st.write("AI:",response["message"]["content"])

