
import os 
from pathlib import Path
import certifi 
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
import requests
from langchain.agents import create_agent



# ==========================================
# LOAD ENV VARIABLES
# ==========================================
os.environ["SSL_CERT_FILE"] = certifi.where()
load_dotenv(Path(__file__).resolve().with_name(".env"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")

# ==========================================
# STREAMLIT PAGE CONFIG
# ==========================================


st.set_page_config(
    page_title="Agentic AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Agentic AI Assistant")
st.markdown("Search + Weather AI Agent using LangChain")

if not TAVILY_API_KEY:
    st.error(
        "Tavily search is not configured. Add TAVILY_API_KEY to the .env file "
        "in the project folder, then restart the app."
    )
    st.stop()

search_tool = TavilySearchResults(
    max_results=2,
    tavily_api_key=TAVILY_API_KEY,
)


@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather information for a city.
    """

    url = (
        f"https://api.weatherstack.com/current?"
        f"access_key={WEATHERSTACK_API_KEY}&query={city}"
    )

    response = requests.get(url)

    data = response.json()

    if "current" not in data:
        return f"Could not fetch weather data for {city}"

    return (
        f"City: {city}\n"
        f"Temperature: {data['current']['temperature']}°C\n"
        f"Weather: {data['current']['weather_descriptions'][0]}\n"
        f"Humidity: {data['current']['humidity']}%"
    )


result = search_tool.invoke("Give me the latest news on AI")



# Initialize the model (it automatically picks up GEMINI_API_KEY from your environment)
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.7
)

# Invoke the model with a message
messages = [HumanMessage(content="What is capital of Delhi?")]
response = llm.invoke(messages)

print(response.content)


tools = [search_tool, get_weather_data]





agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "Answer in no more than 3 concise sentences."
    
    ),
    debug=False
)


# ==========================================
# UI INPUT
# ==========================================

user_query = st.text_input(
    "Enter your query:",
    placeholder="Example: Find the capital of India and current weather"
)

# ==========================================
# RUN AGENT
# ==========================================

if st.button("Run Agent"):

    if user_query:

        with st.spinner("Agent is thinking..."):

            try:
                response = agent.invoke({
                    "messages": [
                            {
                                "role": "user",
                                "content": (
                                    user_query
                                )
                            }
                        ]
                })

                st.success("Response Generated")

                st.markdown("## Final Response")
                st.write(response["messages"][-1].content[0]["text"])

            except Exception as e:
                st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a query")