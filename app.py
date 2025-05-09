import streamlit as st
from chatbot import chatbot

st.set_page_config(page_title="Vehicle Maintenance Assistant", page_icon="🚗")
st.title("🚗 AI-Powered Vehicle Maintenance Assistant")
st.write("Ask anything about car maintenance, dashboard warnings, or fuel usage.")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box
if user_input := st.chat_input("Ask your question here..."):
    # Append user input
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chatbot.invoke({"input": user_input})
            reply = response.get("output", "Sorry, I couldn't understand that.")
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
