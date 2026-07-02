import csv
from io import StringIO


def extract_flashcards(text):
    """
    Extracts flashcards written as:

    Q: question
    A: answer
    """

    flashcards = []
    current_question = None

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if line.lower().startswith("q:"):
            current_question = line[2:].strip()

        elif line.lower().startswith("a:") and current_question:
            answer = line[2:].strip()

            if current_question and answer:
                flashcards.append(
                    {
                        "front": current_question,
                        "back": answer,
                    }
                )

            current_question = None

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
