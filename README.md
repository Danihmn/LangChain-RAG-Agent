# langchain-rag-agent

## Running

1. Make sure [Ollama](https://ollama.com) is running and the model is available:

   ```bash
   ollama pull llama3.2
   ```

2. Start the LangGraph server from the project root:

   ```bash
   uv run langgraph dev
   ```

3. Open [Agent Chat UI](https://agentchat.vercel.app) and fill in:

   - **Deployment URL:** `http://localhost:2024`
   - **Assistant / Graph ID:** `agent`
   - **LangSmith API Key:** leave blank (the server is local)

   Or open it already configured:
   <https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=agent>

## About the chat UI

[agentchat.vercel.app](https://agentchat.vercel.app) is the hosted version of LangChain's open-source
[Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui). Vercel only serves the page; the app runs in
your browser, which talks directly to the local LangGraph server at `localhost:2024`. No Node.js setup is
needed in this project.

- An internet connection is required to load the page, even though the model runs locally.
- Some browsers (e.g. Safari, Brave) may block an HTTPS page from calling `http://localhost`. Chrome and
  Firefox work.
- If the hosted version is ever unavailable, clone the repository above and run it locally with
  `npm install && npm run dev`.
