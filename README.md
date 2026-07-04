# Nexa Study

Nexa Study is an AI-powered study tool for STEM learners. It turns messy notes into structured revision materials, downloadable study packs, and interactive flashcard decks.

The app was built with Python, Streamlit, the OpenAI API, and ReportLab as a portfolio project and MVP for exploring AI-assisted study tools.

![Nexa Study home screen](assets/nexa-study-home.png)


## Why I built this

I built Nexa Study because I wanted a practical tool that could help Engineering students turn rough, imperfect notes into clearer revision materials.

As a robotics and AI engineering student, I often find that learning is not just about having information. It is about transforming that information into something usable: summaries, worked examples, flashcards, quizzes, and practice questions.

Nexa Study is my way of exploring how AI can support that process while keeping the experience simple, structured, and student-friendly.


## Current features

- Generate summaries from pasted notes
- Create full revision packs
- Generate flashcards from study material
- Generate quiz questions and practice questions
- Export revision material as PDF
- Export revision material as Markdown
- Download an interactive flashcard deck as an offline HTML file
- Use flashcard decks with:
  - animated card flipping
  - typed answer box
  - correct / wrong tracking
  - unseen card counter
  - session size selection
  - shuffle and reset controls
- Choose subject area, difficulty level, output style, and target flashcard count
- Demo mode for testing without using API credits
- Feedback and privacy sections
- Custom UI styling with a soft study-focused theme


## Interactive flashcard deck

Nexa Study can generate a downloadable interactive flashcard deck.

The deck opens in a browser and works offline. It allows learners to type their answer, reveal the official answer, and mark themselves correct or wrong.

![Interactive flashcard deck](assets/nexa-study-flashcards.png)


## Tech stack

- Python
- Streamlit
- OpenAI API
- ReportLab
- HTML, CSS, and JavaScript
- Git and GitHub


## Project structure

```text
app.py                Main Streamlit app
config.py             App settings, labels, and dropdown options
styles.py             Custom CSS styling
ai_utils.py           OpenAI prompt and API logic
pdf_utils.py          PDF generation helpers
flashcard_utils.py    Flashcard extraction and CSV export
html_utils.py         Interactive HTML flashcard deck generation
requirements.txt      Python dependencies
```

## Status

Nexa Study is currently an MVP and portfolio project.


## Copyright

Copyright © 2026 Courtney Walsh. Nexa Study. All rights reserved.

This repository is public for portfolio and review purposes. No licence is currently granted for copying, distribution, modification, or commercial use.