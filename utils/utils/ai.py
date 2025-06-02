import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_contract(text):
    prompt = f"""
You are a legal assistant. Analyze the following contract text.

1. Extract key clauses (e.g., Payment Terms, Termination, NDA).
2. Summarize each clause in simple language.
3. Identify potential risks for freelancers or startups.

Return the result in JSON format:
{{
  "clauses": {{
    "Clause Name": "Summary"
  }},
  "risks": [
    "List any potential risks"
  ]
}}

Contract text:
{text[:3000]}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
