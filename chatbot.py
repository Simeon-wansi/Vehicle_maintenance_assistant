import os
from dotenv import load_dotenv
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from memory import memory
from fuel_cost_tool import fuel_cost_calculator
from weather_tool import get_current_weather


# Load API key
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Initialize the language model
llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=openai_key)

# Define the tools
tools = [fuel_cost_calculator, get_current_weather]

# Define the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Create the agent
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

# Create the chatbot with memory
chatbot = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)
