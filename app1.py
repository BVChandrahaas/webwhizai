import os
import streamlit as st
from streamlit_chat import message
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# Set environment variables
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# Streamlit page setup
st.set_page_config(page_title="Webscraper AI", layout="centered")
st.title("Web-Whiz AI Chatbot")

# Initializing conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input and submit
query = st.text_input("You: ", key="input")
submit_button = st.button("Send")

if submit_button and query.strip():
    # Adding user query to conversation history
    st.session_state.messages.append({"role": "user", "content": query})

    # Initializing LangChain model and tools
    model = ChatOpenAI(model="gpt-4o-mini")
    search = TavilySearchResults(max_results=3)
    tools = [search]
    
    # Creating agent executor
    agent_executor = create_react_agent(model, tools)
    config = {"configurable": {"thread_id": "abc123"}}
    
    with st.spinner("Processing your query..."):
        # giving full chat history to the agent
        conversation = [
            HumanMessage(content=msg["content"]) for msg in st.session_state.messages if msg["role"] == "user"
        ]
        agent_response = ""
        for chunk in agent_executor.stream({"messages": conversation}, config):
            agent_response = chunk
        
        # obtaining final response
        agent_response = agent_response["agent"]["messages"][0].content

    # Attaching bot response to conversation history
    st.session_state.messages.append({"role": "assistant", "content": agent_response})

# Displaying conversation
st.subheader("Conversation")
for i, message_data in enumerate(st.session_state.messages):
    if message_data["role"] == "user":
        message(message_data["content"], is_user=True, key=f"user_{i}")
    else:
        message(message_data["content"], key=f"bot_{i}")
