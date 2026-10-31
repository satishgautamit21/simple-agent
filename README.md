# LangChain Simple Agent

A small LangChain project that demonstrates how an LLM can use external tools
to answer a user request. The agent can search the web with Tavily and retrieve
current weather from Weatherstack, with Gemini providing the language model.

## Concepts this project demonstrates

- **LLM integration:** configure a chat model and send it messages.
- **Direct model calls vs. agents:** compare a fixed model invocation with an
  agent created using `create_agent`.
- **Tool calling:** expose web search and a Python weather function as tools,
  then let the agent choose when to call them.
- **Tool interfaces:** describe a tool's purpose and arguments so the model can
  select and invoke it.
- **External API integration:** call third-party services and use their results
  in an AI response.
- **Basic user interface:** collect a request and display the result in
  Streamlit.
- **Configuration:** load API credentials from environment variables rather
  than embedding them in application code.

## What this is intended to prove

The central learning goal is that an LLM can be connected to bounded application
capabilities: instead of relying only on what the model already knows, the
agent can request live search or weather data and use the returned information
to answer a user.

This pattern is useful in enterprise applications that connect assistants to
approved business services, such as a product catalogue or an internal
knowledge-search API. The example is a learning prototype, not a production
architecture. Enterprise tools should enforce authorization, validate inputs,
limit access to data, and handle API errors and timeouts reliably.

## Setup

1. Create and activate a virtual environment:

   ```bash
   conda create -n langagent python=3.14 -y
   conda activate langagent
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:

   ```dotenv
   GEMINI_API_KEY=your_gemini_api_key
   TAVILY_API_KEY=your_tavily_api_key
   WEATHERSTACK_API_KEY=your_weatherstack_api_key
   ```

Use Python 3.14 for this setup.

## Run

Start the Streamlit interface from the project root:

```bash
streamlit run app.py
```

The command-line example can also be run with:

```bash
python main.py
```

The command-line script runs its example request; it does not currently accept
a custom request as a command-line argument.
