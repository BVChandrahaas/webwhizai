# Web-Whiz AI Chatbot  https://webwhizai.streamlit.app/
## Overview
Web-Whiz AI Chatbot is a conversational AI application built using Streamlit, LangChain, and Tavily. The application allows users to interact with a chatbot that can answer questions and provide information on various topics. The chatbot uses Tavily for web scraping and ranking relevant content, which is then passed to a Large Language Model (LLM) to generate context-aware responses.
# Technical Components
### 1. Streamlit
Streamlit is a Python library used to build the user interface and handle user input. The application uses Streamlit to create a simple chat interface where users can input their queries.

### 2. LangChain
LangChain is a library that enables the creation of complex conversational AI systems. It provides a framework for integrating multiple AI models and tools, such as Tavily, to generate context-aware responses.

### 3. Tavily
Tavily is a web scraping and ranking tool that provides relevant content from the web. In this application, Tavily is used to scrape the web for relevant content based on the user's query. The scraped content is then ranked based on relevance, and the top-ranked content is passed to the LLM for generating a response.

# How Tavily Works
### Step 1: Web Scraping
When a user inputs a query, Tavily is triggered to scrape the web for relevant content. Tavily uses its proprietary algorithms to crawl the web and extract relevant information from various sources.

### Step 2: Ranking
The scraped content is then ranked based on relevance, using Tavily's ranking algorithms. The ranking is done based on various factors, such as the content's relevance to the query, its freshness, and its authority.

### Step 3: Top Content Selection
The top-ranked content is selected for further processing. In this application, the top 3 ranked content pieces are selected.

# How the LLM Works

### Step 1: Context Generation
The top-ranked content pieces from Tavily are passed to the LLM, along with the user's query and conversation history. The LLM uses this information to generate a context-aware response.

### Step 2: Response Generation
The LLM generates a response based on the context generated in the previous step. The response is designed to be informative, engaging, and relevant to the user's query.

# Application Flow

### Step 1: User Input
The user inputs a query into the chat interface.

### Step 2: Tavily Trigger
Tavily is triggered to scrape the web for relevant content.

### Step 3: Content Ranking
The scraped content is ranked based on relevance.

### Step 4: Top Content Selection
The top 3 ranked content pieces are selected.

### Step 5: LLM Trigger
The selected content pieces are passed to the LLM, along with the user's query and conversation history.

### Step 6: Response Generation
The LLM generates a context-aware response.

### Step 7: Response Display
The response is displayed to the user in the chat interface.

# Configuration
## Environment Variables
### TAVILY_API_KEY: The API key for Tavily.
Follow the link for more info of integrating Tavily: https://python.langchain.com/docs/integrations/tools/tavily_search/
### OPENAI_API_KEY: The API key for OpenAI.
I have used GPT-4o-mini model, you can go with the model of your choice.
### max_results: The maximum number of content pieces to retrieve from Tavily. (Default: 3)

# Deployment
The application is deployed using Streamlit. To deploy the application, simply run the app1.py script, and the application will be available at http://localhost:8501. 
