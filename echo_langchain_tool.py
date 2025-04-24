from langchain.tools import BaseTool
from typing import List, Type
from pydantic import BaseModel, Field
from echo_sentinel import analyze_prompt_chain


class EchoSentinelInput(BaseModel):
    prompt_chain: List[str] = Field(..., description="A list of prompts or agent messages to analyze.")

class EchoSentinelTool(BaseTool):
    name = "EchoSentinel"
    description = "Analyzes a list of prompts for emotional contradiction and volatility."
    args_schema: Type[BaseModel] = EchoSentinelInput

    def _run(self, prompt_chain: List[str]) -> str:
        result = analyze_prompt_chain(prompt_chain)
        return f"Volatility Score: {result['volatility_score']}, Action: {result['recommended_action']}"

    def _arun(self, prompt_chain: List[str]):
        raise NotImplementedError("Async not implemented.")
