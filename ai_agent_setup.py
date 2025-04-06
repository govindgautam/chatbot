# Step 1: Setup API Keys
import os
from dotenv import load_dotenv
Groq_api_key = os.environ.get("GROQ_API_KEY")
Tavily_api_key = os.environ.get("TAVILY_API_KEY")
Open_api_key = os.environ.get("OPENAI_API_KEY")  # ✅ Corrected name

# Step 2: Setup LLM Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

Open_llm = ChatOpenAI(model="gpt-4o-mini" , api_key="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"
)  # ✅ Passing key
groq_llm = ChatGroq(model="llama3-70b-8192")  # Optional if needed
search_tool = TavilySearchResults(max_results=2)

load_dotenv()
# Step 3: Setup AI Agent
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
 

system_prompt = "Act as an AI chatbot who is smart and friendly"
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    agent=create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]
