This project contains a LangChain agent that searches the web and fetches
current weather information.

Setup

1. Create a virtual environment:
   conda create -n langagent python=3.14 -y
   conda activate langagent
2. Install dependencies:
   pip install -r requirements.txt
3. Configure your environment:
   Create a `.env` file in the project root with these keys:

   ```dotenv
   GEMINI_API_KEY=your_gemini_api_key
   TAVILY_API_KEY=your_tavily_api_key
   WEATHERSTACK_API_KEY=your_weatherstack_api_key
   ```

Use Python 3.14 for this setup.

Run the agent (the default request asks for France news and Paris weather):

python app.py

You can also provide a custom request:

python app.py "What is the capital of France?"

The agent uses Gemini, Tavily search, and Weatherstack. It exits with a clear
message if any required API key is missing.