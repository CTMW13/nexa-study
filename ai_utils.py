import os

from dotenv import load_dotenv
from openai import OpenAI


def get_api_key(streamlit_secrets=None):
    """
    Loads the OpenAI API key from .env locally, or Streamlit secrets when deployed.
    """

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key and streamlit_secrets is not None:
        try:
            api_key = streamlit_secrets.get("OPENAI_API_KEY", None)
        except Exception:
            api_key = None

    return api_key


def create_openai_client(api_key):
    """
    Creates an OpenAI client only when an API key exists.
    """

    if not api_key:
        return None

    return OpenAI(api_key=api_key)


def build_prompt(notes, output_type, subject, difficulty, style):
    return f"""
You are Nexa Study, a study assistant for STEM students.

Create a {output_type} from the notes below.

Subject area: {subject}
Difficulty level: {difficulty}
Output style: {style}

Formatting rules:
- Use clean Markdown formatting.
- Do not use LaTeX.
- Do not use equation code.
- Do not write formulas using \\frac, \\text, \\rho, \\[...\\], or similar code.
- Write formulas in plain text.
- Use Markdown tables only when they are genuinely useful.
- Keep tables simple with short cell content.
- Use plain English variable names where possible.
- If using density symbols, write "rho" instead of the Greek symbol ρ.

Good formula examples:
Density = Mass / Volume
rho = m / V
Force = Mass × Acceleration
F = ma

Make the output:
- clear
- useful for revision
- beginner-friendly where needed
- structured with headings
- easy to copy into notes

If the notes contain a mistake, gently correct it and explain the correct version.

For a Full Revision Pack, include:
1. Key Definition
2. Main Formula
3. Symbol Meanings
4. Simple Explanation
5. Worked Example
6. Common Mistakes
7. Flashcards
8. Practice Questions
9. Quick Recap

For Flashcards, use exactly this format:
Q: question text
A: answer text

Create at least 8 flashcards if there is enough content.

For Quiz Questions, include answers underneath a separate "Answers" heading.

Notes:
{notes}
"""


def fake_output():
    return """
# Density — Full Revision Pack

## 1. Key Definition

Density tells us how much mass is packed into a certain volume.

In simple terms:

> Density = how compact or packed together a material is.

## 2. Main Formula

Density = Mass / Volume

rho = m / V

## 3. Symbol Meanings

| Symbol | Meaning | Unit |
|---|---|---|
| rho | Density | kg/m³ |
| m | Mass | kg |
| V | Volume | m³ |

## 4. Worked Example

If a block has:

- Mass = 10 kg
- Volume = 2 m³

Then:

Density = 10 / 2

Density = 5 kg/m³

## 5. Common Mistake

A common mistake is dividing density by mass.

Wrong:

Volume = Density / Mass

Correct:

Density = Mass / Volume

## 6. Flashcards

Q: What does density measure?
A: How much mass is packed into a certain volume.

Q: What is the formula for density?
A: Density = Mass / Volume.

Q: What is the SI unit of density?
A: kg/m³.

Q: What does rho represent?
A: Density.

## 7. Practice Questions

1. A block has mass 20 kg and volume 4 m³. Find the density.
2. A liquid has mass 12 kg and volume 3 m³. Find the density.

## Answers

1. Density = 20 / 4 = 5 kg/m³
2. Density = 12 / 3 = 4 kg/m³

## 8. Quick Recap

- Density tells us how compact a material is.
- Formula: Density = Mass / Volume.
- SI unit: kg/m³.
"""


def generate_live_output(client, prompt, model="gpt-5.5"):
    """
    Sends the prompt to the OpenAI Responses API and returns the generated text.
    """

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text
