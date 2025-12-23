import requests
import json
from groq import Groq
import os
def generate_mcq(text,difficulty):
    prompt = f"""
You are a JSON API.

Your task is to generate exactly 5 multiple-choice questions (MCQs).

STRICT RULES:
- Output ONLY valid JSON
- Do NOT add any explanation text
- Do NOT add markdown
- Do NOT add ``` or code fences
- Do NOT add comments
- Do NOT add trailing commas
- If you cannot comply, return an empty JSON array []

JSON FORMAT (must match exactly):
[
  {{
    "question": "string",
    "options": {{
      "A": "string",
      "B": "string",
      "C": "string",
      "D": "string"
    }},
    "answer": "A | B | C | D"
  }}
]

Difficulty: {difficulty}

Content:
{text}
"""



  

    client = Groq(api_key="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")
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
         {"role": "system", "content": "You are an expert exam question setter."},
          {"role": "user", "content": prompt}
      
        ],
        temperature=0,
        max_completion_tokens=2048,
        top_p=1,
        stream=False,
    
    )
    


    content = completion.choices[0].message.content

    # Try to parse as JSON
    try:
        mcqs = json.loads(content)
    except Exception:
        mcqs = content  # fallback if API doesn't return valid JSON

    return mcqs
