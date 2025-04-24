from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from echo_langchain_tool import EchoSentinelTool

tools = [EchoSentinelTool()]
llm = ChatOpenAI(temperature=0)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

chain = [
    "We are making amazing progress!",
    "This entire project might collapse.",
    "Actually, everything is stable now.",
    "But there's an urgent risk no one expected."
]

response = agent.run(f"Analyze this prompt chain for volatility: {chain}")
print(response)
