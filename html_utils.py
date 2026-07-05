import html
import json

def escape_json_for_script(data):
    """
    Safely escapes JSON before embedding it inside a <script> tag.
    """
    json_data = json.dumps(data, ensure_ascii=False)

    return (
        json_data
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )

def flashcards_to_interactive_html(flashcards, title="Nexa Study Flashcards"):
    """
    Creates a self-contained interactive HTML flashcard deck.

    The downloaded file works offline in a browser.
    """

    safe_title = html.escape(title)

    safe_flashcards = [
        {
            "id": index,
            "front": str(card.get("front", "")).strip(),
            "back": str(card.get("back", "")).strip(),
        }
        for index, card in enumerate(flashcards)
        if str(card.get("front", "")).strip() and str(card.get("back", "")).strip()
    ]

    flashcards_json = escape_json_for_script(safe_flashcards)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{safe_title}</title>

    <style>
        :root {{
            --baby-blue: #CBEFFF;
            --deep-blue: #1E3A5F;
            --mid-blue: #274B72;
            --smoky-orange: #D9825B;
            --burnt-orange: #C96A43;
            --cream: #FFF8F1;
            --lilac: #F3E8FF;
            --purple-border: #C084FC;
            --purple-text: #4C1D95;
            --white: #FFFFFF;
            --slate: #334155;
            --muted-slate: #64748B;
        }}

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            min-height: 100vh;
            font-family: Arial, Helvetica, sans-serif;
            background:
                radial-gradient(circle at top left, rgba(169, 220, 247, 0.95), transparent 35%),
                radial-gradient(circle at bottom right, rgba(217, 130, 91, 0.38), transparent 38%),
                radial-gradient(circle at 86% 88%, rgba(233, 213, 255, 0.42), transparent 32%),
                linear-gradient(135deg, #CBEFFF 0%, #E7F6FF 42%, #FFF8F1 100%);
            color: var(--deep-blue);
            padding: 2rem;
        }}

        .app-shell {{
            max-width: 960px;
            margin: 0 auto;
        }}

        .hero {{
            padding: 2rem;
            border-radius: 28px;
            background:
                radial-gradient(circle at 88% 18%, rgba(217, 130, 91, 0.24), transparent 34%),
                linear-gradient(135deg, rgba(169, 220, 247, 0.95), rgba(255, 248, 241, 0.88));
            border: 1px solid rgba(255, 255, 255, 0.72);
            box-shadow: 0 24px 60px rgba(30, 58, 95, 0.16);
            margin-bottom: 1.5rem;
        }}

        .hero h1 {{
            margin: 0 0 0.5rem 0;
            font-size: 2.4rem;
            letter-spacing: -0.04em;
        }}

        .hero p {{
            margin: 0;
            color: var(--mid-blue);
            line-height: 1.6;
        }}

        .deck-panel {{
            background: rgba(255, 248, 241, 0.9);
            border: 1px solid rgba(217, 130, 91, 0.22);
            border-radius: 26px;
            padding: 1.4rem;
            box-shadow: 0 18px 42px rgba(30, 58, 95, 0.12);
        }}

        .deck-topbar {{
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            align-items: center;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }}

        .progress-text {{
            font-weight: 900;
            color: var(--deep-blue);
        }}

        .progress-subtext {{
            color: var(--muted-slate);
            font-size: 0.92rem;
            margin-top: 0.2rem;
        }}

        .session-tools {{
            display: flex;
            gap: 0.65rem;
            align-items: center;
            flex-wrap: wrap;
        }}

        select {{
            border-radius: 14px;
            border: 1px solid rgba(192, 132, 252, 0.58);
            padding: 0.72rem 0.8rem;
            color: var(--deep-blue);
            background: white;
            font-weight: 700;
        }}

        .progress-track {{
            width: 100%;
            height: 10px;
            background: rgba(30, 58, 95, 0.12);
            border-radius: 999px;
            overflow: hidden;
            margin-bottom: 1.3rem;
        }}

        .progress-fill {{
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, var(--smoky-orange), var(--purple-border));
            border-radius: 999px;
            transition: width 0.25s ease;
        }}

        .flashcard-scene {{
            perspective: 1200px;
        }}

        .flashcard {{
            min-height: 300px;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.65s ease;
            cursor: pointer;
        }}

        .flashcard.is-flipped {{
            transform: rotateY(180deg);
        }}

        .flashcard-face {{
            position: absolute;
            inset: 0;
            border-radius: 26px;
            background:
                radial-gradient(circle at 18% 12%, rgba(255, 255, 255, 0.84), transparent 34%),
                linear-gradient(135deg, rgba(243, 232, 255, 0.72), rgba(255, 255, 255, 0.58));
            border: 1px solid rgba(192, 132, 252, 0.58);
            box-shadow:
                inset 0 1px 0 rgba(255, 255, 255, 0.84),
                0 16px 34px rgba(76, 29, 149, 0.10);
            backface-visibility: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
            text-align: center;
        }}

        .flashcard-back {{
            transform: rotateY(180deg);
            background:
                radial-gradient(circle at 18% 12%, rgba(255, 255, 255, 0.86), transparent 34%),
                linear-gradient(135deg, rgba(255, 248, 241, 0.85), rgba(243, 232, 255, 0.66));
        }}

        .card-label {{
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.78rem;
            font-weight: 900;
            color: var(--burnt-orange);
            margin-bottom: 0.9rem;
        }}

        .flashcard-back .card-label {{
            color: var(--purple-text);
        }}

        .card-text {{
            font-size: 1.35rem;
            line-height: 1.55;
            font-weight: 800;
            color: var(--deep-blue);
            white-space: pre-wrap;
        }}

        .answer-box {{
            margin-top: 1rem;
            background: rgba(255, 255, 255, 0.82);
            border: 1px solid rgba(192, 132, 252, 0.45);
            border-radius: 20px;
            padding: 1rem;
        }}

        .answer-box label {{
            display: block;
            font-weight: 900;
            margin-bottom: 0.5rem;
            color: var(--deep-blue);
        }}

        textarea {{
            width: 100%;
            min-height: 86px;
            resize: vertical;
            border-radius: 16px;
            border: 1.5px solid rgba(192, 132, 252, 0.62);
            padding: 0.8rem;
            color: var(--deep-blue);
            caret-color: black;
            font-size: 1rem;
            outline: none;
            background: white;
        }}

        textarea:focus {{
            border-color: rgba(192, 132, 252, 0.92);
            box-shadow: 0 0 0 3px rgba(192, 132, 252, 0.16);
        }}

        .your-answer-preview {{
            margin-top: 0.8rem;
            color: var(--muted-slate);
            font-size: 0.92rem;
        }}

        .controls {{
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 0.75rem;
            margin-top: 1rem;
        }}

        button {{
            border: none;
            border-radius: 16px;
            padding: 0.82rem 1rem;
            font-weight: 850;
            color: white;
            background: linear-gradient(135deg, #D9825B 0%, #C96A43 100%);
            box-shadow: 0 10px 22px rgba(201, 106, 67, 0.22);
            cursor: pointer;
            transition: transform 0.16s ease, box-shadow 0.16s ease, filter 0.16s ease;
        }}

        button:hover {{
            transform: translateY(-1px);
            filter: brightness(1.03);
            box-shadow: 0 14px 28px rgba(201, 106, 67, 0.28);
        }}

        button.secondary {{
            background: rgba(255, 255, 255, 0.92);
            color: var(--deep-blue);
            border: 1px solid rgba(192, 132, 252, 0.52);
        }}

        button.success {{
            background: linear-gradient(135deg, #7C3AED, #C084FC);
        }}

        button.danger {{
            background: linear-gradient(135deg, #64748B, #334155);
        }}

        .deck-footer {{
            margin-top: 1rem;
            color: var(--muted-slate);
            font-size: 0.9rem;
            text-align: center;
        }}

        .empty-state {{
            background: rgba(255, 255, 255, 0.86);
            border-radius: 18px;
            padding: 1rem;
            border: 1px solid rgba(192, 132, 252, 0.45);
            color: var(--deep-blue);
        }}

        @media (max-width: 760px) {{
            body {{
                padding: 1rem;
            }}

            .hero h1 {{
                font-size: 1.85rem;
            }}

            .flashcard {{
                min-height: 280px;
            }}

            .card-text {{
                font-size: 1.08rem;
            }}

            .controls {{
                grid-template-columns: 1fr 1fr;
            }}
        }}
    </style>
</head>

<body>
    <main class="app-shell">
        <section class="hero">
            <h1>⚙️ {safe_title}</h1>
            <p>Interactive flashcard deck generated by Nexa Study. Type your answer, reveal the card, then mark yourself correct or wrong.</p>
        </section>

        <section class="deck-panel">
            <div id="deck-content">
                <div class="deck-topbar">
                    <div>
                        <div class="progress-text" id="progress-text">Card 1 of 1</div>
                        <div class="progress-subtext" id="progress-subtext">0 correct • 0 wrong • 0 unseen</div>
                    </div>

                    <div class="session-tools">
                        <select id="session-size" onchange="changeSessionSize()"></select>
                        <button class="secondary" onclick="shuffleDeck()">Shuffle</button>
                        <button class="secondary" onclick="resetDeck()">Reset</button>
                    </div>
                </div>

                <div class="progress-track">
                    <div class="progress-fill" id="progress-fill"></div>
                </div>

                <div class="flashcard-scene">
                    <div class="flashcard" id="flashcard" onclick="toggleAnswer()">
                        <div class="flashcard-face flashcard-front">
                            <div>
                                <div class="card-label">Question</div>
                                <div class="card-text" id="front-text"></div>
                            </div>
                        </div>

                        <div class="flashcard-face flashcard-back">
                            <div>
                                <div class="card-label">Answer</div>
                                <div class="card-text" id="back-text"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="answer-box">
                    <label for="guess-input">Your guessed answer</label>
                    <textarea id="guess-input" placeholder="Type your answer here before revealing the official answer..."></textarea>
                    <div class="your-answer-preview" id="answer-preview">
                        Your typed answer stays here while you compare it with the official answer.
                    </div>
                </div>

                <div class="controls">
                    <button class="secondary" onclick="previousCard()">Previous</button>
                    <button onclick="toggleAnswer()" id="flip-button">Show answer</button>
                    <button class="danger" onclick="markWrong()">Mark wrong</button>
                    <button class="success" onclick="markCorrect()">Mark correct</button>
                    <button class="secondary" onclick="nextCard()">Next</button>
                </div>

                <div class="deck-footer">
                    Tip: type your answer first, then reveal the card and mark yourself honestly. Annoying, but effective.
                </div>
            </div>
        </section>
    </main>

    <script>
        const originalFlashcards = {flashcards_json};

        let fullDeck = [...originalFlashcards];
        let flashcards = [...originalFlashcards];
        let currentIndex = 0;
        let showingAnswer = false;
        let correct = new Set();
        let wrong = new Set();
        let guesses = {{}};

        const deckContent = document.getElementById("deck-content");
        const card = document.getElementById("flashcard");
        const frontText = document.getElementById("front-text");
        const backText = document.getElementById("back-text");
        const progressText = document.getElementById("progress-text");
        const progressSubtext = document.getElementById("progress-subtext");
        const progressFill = document.getElementById("progress-fill");
        const guessInput = document.getElementById("guess-input");
        const answerPreview = document.getElementById("answer-preview");
        const flipButton = document.getElementById("flip-button");
        const sessionSize = document.getElementById("session-size");

        function renderEmptyState() {{
            deckContent.innerHTML = `
                <div class="empty-state">
                    No flashcards were found in this deck.
                </div>
            `;
        }}

        function setupSessionSizeOptions() {{
            const total = fullDeck.length;
            const possibleSizes = [4, 8, 12, 16, 20].filter(size => size < total);

            sessionSize.innerHTML = "";

            possibleSizes.forEach(size => {{
                const option = document.createElement("option");
                option.value = size;
                option.textContent = `${{size}} cards`;
                sessionSize.appendChild(option);
            }});

            const allOption = document.createElement("option");
            allOption.value = "all";
            allOption.textContent = `All cards (${{total}})`;
            allOption.selected = true;
            sessionSize.appendChild(allOption);
        }}

        function getCurrentCard() {{
            return flashcards[currentIndex];
        }}

        function renderCard() {{
            if (!flashcards.length) {{
                renderEmptyState();
                return;
            }}

            const currentCard = getCurrentCard();

            frontText.textContent = currentCard.front;
            backText.textContent = currentCard.back;

            card.classList.toggle("is-flipped", showingAnswer);
            flipButton.textContent = showingAnswer ? "Show question" : "Show answer";

            guessInput.value = guesses[currentCard.id] || "";

            progressText.textContent = `Card ${{currentIndex + 1}} of ${{flashcards.length}}`;

            const unseen = flashcards.filter(card => !correct.has(card.id) && !wrong.has(card.id)).length;

            progressSubtext.textContent = `${{correct.size}} correct • ${{wrong.size}} wrong • ${{unseen}} unseen`;

            const progressPercent = flashcards.length
                ? Math.round(((correct.size + wrong.size) / flashcards.length) * 100)
                : 0;

            progressFill.style.width = `${{progressPercent}}%`;

            updateAnswerPreview();
        }}

        function updateAnswerPreview() {{
            const typed = guessInput.value.trim();

            if (!typed) {{
                answerPreview.textContent = "Your typed answer stays here while you compare it with the official answer.";
                return;
            }}

            answerPreview.textContent = `Your answer: ${{typed}}`;
        }}

        guessInput.addEventListener("input", () => {{
            const currentCard = getCurrentCard();
            guesses[currentCard.id] = guessInput.value;
            updateAnswerPreview();
        }});

        function toggleAnswer() {{
            showingAnswer = !showingAnswer;
            renderCard();
        }}

        function nextCard() {{
            showingAnswer = false;
            currentIndex = (currentIndex + 1) % flashcards.length;
            renderCard();
        }}

        function previousCard() {{
            showingAnswer = false;
            currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length;
            renderCard();
        }}

        function markCorrect() {{
            const currentCard = getCurrentCard();
            correct.add(currentCard.id);
            wrong.delete(currentCard.id);
            nextCard();
        }}

        function markWrong() {{
            const currentCard = getCurrentCard();
            wrong.add(currentCard.id);
            correct.delete(currentCard.id);
            nextCard();
        }}

        function shuffleArray(array) {{
            for (let i = array.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }}
            return array;
        }}

        function shuffleDeck() {{
            flashcards = shuffleArray([...flashcards]);
            currentIndex = 0;
            showingAnswer = false;
            renderCard();
        }}

        function changeSessionSize() {{
            const value = sessionSize.value;

            let selectedDeck = [...fullDeck];

            if (value !== "all") {{
                selectedDeck = selectedDeck.slice(0, Number(value));
            }}

            flashcards = selectedDeck;
            currentIndex = 0;
            showingAnswer = false;
            correct = new Set();
            wrong = new Set();
            guesses = {{}};

            renderCard();
        }}

        function resetDeck() {{
            currentIndex = 0;
            showingAnswer = false;
            correct = new Set();
            wrong = new Set();
            guesses = {{}};
            renderCard();
        }}

        setupSessionSizeOptions();
        renderCard();
    </script>
</body>
</html>
"""