import os
import json
import datetime

import streamlit as st
from llama_index.llms import Ollama
from llama_index.llms import ChatMessage
# https://docs.llamaindex.ai/en/stable/examples/llm/ollama.html

# from list_ollama_models import OLLAMA_MODELS
from get_ollama_models import OLLAMA_MODELS

# filter non-arabic models
# OLLAMA_MODELS = [model for model in OLLAMA_MODELS if "arabic_" in model]


def update_formatting(text):
    if is_arabic(text):
        return f"<div style='direction: rtl; text-align: right;'>{text}</div>"
    return f"{text}"


def st_ollama(model_name, user_question, chat_history_key):

    llm_ = Ollama(model=model_name)
    
    if chat_history_key not in st.session_state.keys():
        st.session_state[chat_history_key] = []

    print_chat_history_timeline(chat_history_key)
        
    # run the model
    if user_question:
        st.session_state[chat_history_key].append({"content": f"{user_question}", "role": "user"})
        with st.chat_message("question", avatar="🧑‍🚀"):
            user_question = update_formatting(user_question)
            # st.write(user_question)
            # change color of user question to blue
            # user_question = f"<span style='color: #004d4d;'>{user_question}</span>"
            st.markdown(user_question, unsafe_allow_html=True)

        messages = [ChatMessage(content=message["content"], role=message["role"]) for message in st.session_state[chat_history_key]]

        with st.spinner("افكر كيف ارد  🤔 ... كلمة كلمة "):
            response = llm_.stream_chat(messages)
        
        # streaming response
        with st.chat_message("response", avatar="🤖"):
            chat_box = st.empty()
            response_message = ""
            for chunk in response:
                response_message += chunk.delta
                # chat_box.write(response_message)
                # check if content contains arabic characters
                # response_message = update_formatting(response_message)
                chat_box.markdown(response_message, unsafe_allow_html=True)
            response_message = update_formatting(response_message)
            chat_box.empty()
            st.markdown(response_message, unsafe_allow_html=True)
        st.session_state[chat_history_key].append({"content": f"{response_message}", "role": "assistant"})
        
        return response_message


def print_chat_history_timeline(chat_history_key):
    for message in st.session_state[chat_history_key]:
        role = message["role"]
        if role == "user":
            with st.chat_message("user", avatar="🧑‍🚀"): 
                question = message["content"]
                # check if content contains arabic characters
                question = update_formatting(question)
                st.markdown(f"{question}", unsafe_allow_html=True)
        elif role == "assistant":
            with st.chat_message("assistant", avatar="🤖"):
                content = message["content"]
                # check if content contains arabic characters
                content = update_formatting(content)  
                st.markdown(content, unsafe_allow_html=True)


# -- helpers --
def page_config():
     # page formatting for arabic models
    st.set_page_config(layout="wide", page_title="نماذج اللغة للذكاء الأصطناعي بالعربي", page_icon="🦙")
    
    # set entire page to rtl (for arabic support)
    st.markdown("<style>body {direction: rtl;}</style>", unsafe_allow_html=True)
    
    st.sidebar.title("تحدث مع اللاما 🦙")
    st.sidebar.subheader("نماذج اللغة للذكاء الأصطناعي بالعربي")
    
    footer = """<div style="position: fixed; left: 0; bottom: 0; background-color: #004d4d; color: white; padding: 10px 20px; border-top-right-radius: 10px; box-shadow: 2px 2px 5px grey; font-size: 10px; opacity: 0.5;">
                Source code <a href="https://github.com/iamaziz/st_ollama" style="color: white; text-decoration: none; font-weight: bold;">here</a>
                <br>
                <span style="font-size: 10px;">2023 By Aziz Alto</span>
        </div>"""
    st.sidebar.markdown(footer, unsafe_allow_html=True)
    st.markdown("<style>body {direction: rtl;}</style>", unsafe_allow_html=True) 
    

def select_model():

    # model names
    llm_names = [model["name"] for model in OLLAMA_MODELS]
    llm_name = st.sidebar.selectbox(f"Choose Agent ({len(llm_names)} available)", [""] + llm_names)
    
    # write model details as dict
    if llm_name:
        llm_details = [model for model in OLLAMA_MODELS if model["name"] == llm_name][0]
        with st.expander("Model Details", expanded=False):
            st.write(llm_details)

        
        
        

    return llm_name


def assert_models_installed():
    if len(OLLAMA_MODELS) < 1:
        st.sidebar.warning("No models found. Please install at least one model e.g. `ollama run llama2`")
        st.stop()


def save_conversation(llm_name, conversation_key):

    OUTPUT_DIR = "llm_conversations"
    OUTPUT_DIR = os.path.join(os.getcwd(), OUTPUT_DIR)

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{OUTPUT_DIR}/{timestamp}_{llm_name.replace(':', '-')}"

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    if st.session_state[conversation_key]:

        if st.sidebar.button("احفظ المحادثة"):
            with open(f"{filename}.json", "w", encoding='utf-8') as f:
                json.dump(st.session_state[conversation_key], f, indent=4, ensure_ascii=False)
            st.success(f"Conversation saved to {filename}.json")


def is_arabic(text):
    """Check if text contains arabic characters"""
    for character in text:
        if '\u0600' <= character <= '\u06FF' or '\u0750' <= character <= '\u077F' or '\uFB50' <= character <= '\uFDFF' or '\uFE70' <= character <= '\uFEFF':
            return True
    return False


if __name__ == "__main__":

    page_config()
    llm_name = select_model()
    
    assert_models_installed()
    
    if not llm_name: st.stop()

    conversation_key = f"model_{llm_name}"

    ask_question_message = f"أسألني عن أي شيء"
    prompt = st.chat_input(ask_question_message)
    

    st_ollama(llm_name, prompt, conversation_key)
    
    if st.session_state[conversation_key]:
        clear_conversation = st.sidebar.button("امسح المحادثة")
        if clear_conversation:
            st.session_state[conversation_key] = []
            st.rerun()

    # save conversation to file
    save_conversation(llm_name, conversation_key)