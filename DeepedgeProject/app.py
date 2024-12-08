import os
import streamlit as st
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

# Set environment variable explicitly (Temporary fix)
os.environ["TAVILY_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] ="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"
# Streamlit UI setup
st.title("Smart Query Response App")
st.write("Enter a query and let the AI fetch and generate a response for you!")

# User input
query = st.text_input("Enter your query:")
submit_button = st.button("Submit")

if submit_button and query.strip():
    with st.spinner("Processing your query..."):
        # Step 1: Create the Tavily + LangChain agent
        from langgraph.checkpoint.memory import MemorySaver
        memory = MemorySaver()
        model = ChatOpenAI(model="gpt-4o-mini")
        search = TavilySearchResults(max_results=3)
        tools = [search]
        agent_executor = create_react_agent(model, tools,checkpointer=memory)
        config = {"configurable": {"thread_id": "abc123"}}

        # Step 2: Pass user query to the agent
        agent_response = ""
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=query)]},config
        ):
            agent_response = chunk
        
        # Step 3: Display the response
        st.subheader("Response:")
        agent_response = agent_response["agent"]["messages"][0].content
        st.write(agent_response)
else:
    st.warning("Please enter a query!")
