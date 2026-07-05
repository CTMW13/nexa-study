import csv
from io import StringIO


def extract_flashcards(text):
    """
    Extracts flashcards written as:

    Q: question
    A: answer

    This parser supports multiline questions and answers.
    """

    flashcards = []

    current_question_lines = []
    current_answer_lines = []
    current_mode = None

    def save_current_card():
        question = " ".join(line.strip() for line in current_question_lines).strip()
        answer = "\n".join(line.rstrip() for line in current_answer_lines).strip()

        if question and answer:
            flashcards.append(
                {
                    "front": question,
                    "back": answer,
                }
            )

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            if current_mode == "answer" and current_answer_lines:
                current_answer_lines.append("")
            continue

        if stripped.lower().startswith("q:"):
            if current_question_lines or current_answer_lines:
                save_current_card()

            current_question_lines = [stripped[2:].strip()]
            current_answer_lines = []
            current_mode = "question"

        elif stripped.lower().startswith("a:"):
            current_answer_lines = [stripped[2:].strip()]
            current_mode = "answer"

        else:
            if current_mode == "question":
                current_question_lines.append(stripped)
            elif current_mode == "answer":
                current_answer_lines.append(line)

    if current_question_lines or current_answer_lines:
        save_current_card()

    return flashcards


def flashcards_to_csv(flashcards):
    """
    Converts flashcards into CSV format with Front and Back columns.
    """
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Front", "Back"])

    for card in flashcards:
        writer.writerow([card["front"], card["back"]])

    return output.getvalue()