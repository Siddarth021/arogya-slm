# backend/core/prompt.py

def build_prompt(user_input, context, dosha):

    return f"""
You are an Ayurvedic assistant.

User symptoms:
{user_input}

Relevant Ayurvedic knowledge:
{context}

Detected Dosha:
{dosha}

Tasks:
1. Explain dosha imbalance
2. Suggest remedies (diet + lifestyle)
3. Give precautions

Format:
Dosha:
Reason:
Remedies:
Precautions:
"""