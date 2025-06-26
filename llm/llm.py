# llm/llm.py
# Using only CrewAI's built-in LLM compatibility (no manual LLMs)

# You don't need to define a separate LLM loader file when using CrewAI defaults.
# Agents will automatically use the default LLM configuration provided by CrewAI.

# If you want to later extend with a specific model, you can define it inside your agent files like:
# from langchain.chat_models import ChatOpenAI
# llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

# For now, this file is intentionally left empty or unused.
# All agents should be initialized with `llm=None` or use the CrewAI default.