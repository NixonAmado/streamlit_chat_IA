import streamlit as st
from IAConfiguration.configuration import client

st.title("Chat Qwen 2.5")
st.subheader("")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner('Wait for it...'):
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model="Qwen/Qwen2.5-Coder-32B-Instruct",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                temperature=0.5,
                max_tokens=2048,
                top_p=0.5,
                stream=True
            )
            response = ""
            for chunk in stream:
                response += chunk.choices[0].delta.content
            content = st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})