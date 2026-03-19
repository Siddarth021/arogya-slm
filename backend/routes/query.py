# backend/routes/query.py

from fastapi import APIRouter
from backend.fusion.fusion import build_context
from backend.core.llm import llm
from backend.core.prompt import build_prompt

router = APIRouter()

@router.post("/")
def query(user_input: str):

    context, dosha = build_context(user_input)

    prompt = build_prompt(user_input, context, dosha)

    response = llm.generate(prompt)

    return {
        "dosha": dosha,
        "response": response
    }