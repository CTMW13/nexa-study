import time

import streamlit as st

from ai_utils import (
    build_prompt,
    create_openai_client,
    fake_output,
    generate_live_output,
    get_api_key,
)
from config import (
    APP_NAME,
    APP_TAGLINE,
    DAILY_SPARK_SOURCE_LABEL,
    DAILY_SPARK_SOURCE_URL,
    DAILY_SPARK_SUMMARY,
    DAILY_SPARK_TITLE,
    DAILY_SPARK_WHY_IT_MATTERS,
    DIFFICULTY_LEVELS,
    FEEDBACK_FORM_URL,
    FLASHCARD_COUNTS,
    GITHUB_REPO_URL,
    HERO_BADGES,
    OUTPUT_STYLES,
    OUTPUT_TYPES,
    SUBJECT_AREAS,
)
from flashcard_utils import extract_flashcards, flashcards_to_csv
from html_utils import flashcards_to_interactive_html
from pdf_utils import (
    convert_markdown_to_pdf,
    get_document_title,
    make_safe_filename,
)
from styles import CUSTOM_CSS


# --------------------------------------------------
# Load API key
# --------------------------------------------------

api_key = get_api_key(st.secrets)
client = create_openai_client(api_key)


# --------------------------------------------------
# Page setup
# --------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="⚙️",
    layout="wide",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# --------------------------------------------------
# Hero section
# --------------------------------------------------

badge_html = "".join([f'<span class="badge">{badge}</span>' for badge in HERO_BADGES])

st.markdown(
    f"""
    <div class="hero-card">
        <div class="hero-title">⚙️ {APP_NAME}</div>
        <div class="hero-subtitle">
            {APP_TAGLINE}
        </div>
        <div class="hero-badges">
            {badge_html}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Daily Engineering Spark
# --------------------------------------------------

st.markdown(
    f"""
    <div class="spark-card">
        <div class="spark-label">Daily Engineering Spark</div>
        <div class="spark-title">{DAILY_SPARK_TITLE}</div>
        <div class="spark-text">{DAILY_SPARK_SUMMARY}</div>
        <div class="spark-text">
            <strong>Why it matters:</strong> {DAILY_SPARK_WHY_IT_MATTERS}
        </div>
        <div class="spark-source">
            Source:
            <a href="{DAILY_SPARK_SOURCE_URL}" target="_blank">
                {DAILY_SPARK_SOURCE_LABEL}
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Intro cards
# --------------------------------------------------

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown(
        """
        <div class="info-card">
            <h3>1. Paste your notes</h3>
            <p>Add lecture notes, textbook extracts, rough explanations, or messy revision ideas.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_b:
    st.markdown(
        """
        <div class="info-card">
            <h3>2. Choose your format</h3>
            <p>Generate summaries, flashcards, quizzes, cheat sheets, or full revision packs.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_c:
    st.markdown(
        """
        <div class="info-card">
            <h3>3. Download your pack</h3>
            <p>Export your generated material as PDF, Markdown, or interactive flashcard decks.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# Sidebar settings
# --------------------------------------------------

st.sidebar.title("⚙️ Workspace")
st.sidebar.caption("Shape the revision pack before generating.")

subject = st.sidebar.selectbox("Subject area", SUBJECT_AREAS)
difficulty = st.sidebar.selectbox("Difficulty level", DIFFICULTY_LEVELS)
style = st.sidebar.selectbox("Output style", OUTPUT_STYLES)

st.sidebar.divider()

st.sidebar.subheader("🔒 Premium Preview")
st.sidebar.caption("Planned features for future memberships.")

st.sidebar.markdown(
    """
    <div class="premium-card">
        <div class="premium-card-title">🎨 PDF styling themes 🔒</div>
        <div class="premium-card-text">
            Choose clean STEM, exam mode, minimal, or engineering notebook layouts.
        </div>
    </div>

    <div class="premium-card">
        <div class="premium-card-title">📂 File uploads 🔒</div>
        <div class="premium-card-text">
            Upload notes, PDFs, slides, and revision sheets directly.
        </div>
    </div>

    <div class="premium-card">
        <div class="premium-card-title">🧾 Saved revision history 🔒</div>
        <div class="premium-card-text">
            Save generated packs and return to them later.
        </div>
    </div>

    <div class="premium-card">
        <div class="premium-card-title">⚙️ Custom study branding 🔒</div>
        <div class="premium-card-text">
            Personalise generated packs with preferred formatting and style.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Main input area
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Create a revision pack</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-caption">
        Paste your notes, choose an output type, then generate your study material.
    </div>
    """,
    unsafe_allow_html=True,
)

left_col, right_col = st.columns([2, 1])

with left_col:
    notes = st.text_area(
        "Paste your notes here:",
        height=330,
        placeholder=(
            "Example: Ohm’s law states that current equals voltage divided by resistance. "
            "I = V / R..."
        ),
    )

    note_length = len(notes)
    word_count = len(notes.split()) if notes.strip() else 0

    if note_length == 0:
        length_label = "No notes yet"
        length_message = "Paste your notes to begin."
    elif note_length < 500:
        length_label = "Short notes"
        length_message = "Good for quick summaries or flashcards."
    elif note_length < 2500:
        length_label = "Medium notes"
        length_message = "Good length for a full revision pack."
    else:
        length_label = "Long notes"
        length_message = "Consider using a detailed or exam revision style."

    if note_length == 0:
        note_metric_line = "0 words • 0 characters"
    else:
        note_metric_line = f"{word_count} words • {note_length} characters"

    st.markdown(
        f"""
        <div class="metric-card">
            <strong>{length_label}</strong><br>
            {note_metric_line}<br>
            {length_message}
        </div>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    output_type = st.selectbox("Output type", OUTPUT_TYPES)

    flashcard_count = st.selectbox(
        "Target flashcards",
        FLASHCARD_COUNTS,
        index=1,
        help=(
            "Choose how many flashcards Nexa Study should try to generate. "
            "Short topics may produce fewer strong cards."
        ),
    )

    st.info("Tip: Use Flashcards or Full Revision Pack if you want an interactive study deck.")

    demo_mode = st.checkbox("Demo mode: sample density pack")

    if demo_mode:
        st.success("Demo mode uses sample density content only.")

    with st.expander("How to get better results"):
        st.write(
            """
            - Paste enough context, not just one sentence.
            - Include formulas, examples, or mistakes you want explained.
            - Choose the correct subject and difficulty level.
            - Use **Full Revision Pack** for the most complete output.
            - Use **Flashcards** if you want an interactive study deck.
            - Avoid pasting sensitive personal data.
            """
        )

st.markdown(
    """
    <div class="privacy-note">
        <strong>Privacy reminder:</strong> Do not paste sensitive personal information,
        private addresses, student ID numbers, medical details, passwords, or anything
        you would not want processed by an AI service.
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Tiny rubber duck loading helper
# --------------------------------------------------

def show_duck_loading(slot, message):
    slot.markdown(
        f"""
        <div class="duck-loading">
            <span>{message}</span>
            <span class="rubber-duck">
                <span class="duck-eye"></span>
                <span class="duck-beak"></span>
                <span class="duck-shine"></span>
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def clear_loading_area(loading_area):
    loading_area.empty()


# --------------------------------------------------
# Export helpers
# --------------------------------------------------

def get_export_summary(selected_output_type):
    if selected_output_type == "Flashcards":
        return "Interactive deck + CSV"

    if selected_output_type == "Full Revision Pack":
        return "PDF + Markdown + Deck"

    return "PDF + Markdown"


def make_flashcard_deck_title(document_title):
    cleaned_title = document_title.strip()

    cleaned_title = cleaned_title.replace("— Full Revision Pack", "")
    cleaned_title = cleaned_title.replace("- Full Revision Pack", "")
    cleaned_title = cleaned_title.replace("Full Revision Pack", "")
    cleaned_title = cleaned_title.strip()

    if cleaned_title.lower().startswith("flashcards:"):
        return cleaned_title

    if cleaned_title.lower().endswith(" flashcards"):
        cleaned_title = cleaned_title[:-len(" flashcards")].strip()

    return f"Flashcards: {cleaned_title}"


# --------------------------------------------------
# Download buttons
# --------------------------------------------------

def show_download_buttons(result, output_type):
    document_title = get_document_title(result)
    base_filename = make_safe_filename(result)
    flashcards = extract_flashcards(result)

    is_flashcard_output = output_type == "Flashcards"
    is_full_revision_pack = output_type == "Full Revision Pack"

    with st.container(key="downloads_card"):
        st.markdown(
            '<div class="download-card-marker"></div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="download-card-main-title">Downloads</div>
            """,
            unsafe_allow_html=True,
        )

        if not is_flashcard_output:
            st.markdown(
                f"""
                <div class="download-card-caption">
                    Export your generated {output_type.lower()} as a clean study file.
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="download-button-spacer"></div>',
                unsafe_allow_html=True,
            )

            pdf_data = convert_markdown_to_pdf(result, document_title)

            download_col_1, download_col_2 = st.columns(2)

            with download_col_1:
                st.download_button(
                    label=f"Download {output_type} as PDF",
                    data=pdf_data,
                    file_name=f"{base_filename}.pdf",
                    mime="application/pdf",
                    key="download_pdf",
                )

            with download_col_2:
                st.download_button(
                    label=f"Download {output_type} as Markdown",
                    data=result,
                    file_name=f"{base_filename}.md",
                    mime="text/markdown",
                    key="download_markdown",
                )

            if flashcards and is_full_revision_pack:
                st.markdown(
                    """
                    <div class="download-section-subheading">Study tools</div>
                    <div class="download-card-caption">
                        Download an interactive flashcard deck that opens in your browser.
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.markdown(
                    '<div class="download-button-spacer"></div>',
                    unsafe_allow_html=True,
                )

                deck_title = make_flashcard_deck_title(document_title)

                interactive_deck = flashcards_to_interactive_html(
                    flashcards=flashcards,
                    title=deck_title,
                )

                deck_col_1, deck_col_2 = st.columns([1, 2])

                with deck_col_1:
                    st.download_button(
                        label="Download Interactive Study Deck",
                        data=interactive_deck,
                        file_name=f"{base_filename}_interactive_flashcards.html",
                        mime="text/html",
                        key="download_interactive_flashcards",
                    )

                with deck_col_2:
                    st.markdown(
                        """
                        <div class="download-helper-text">
                            Best for active recall, self-testing, and offline browser study.
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with st.expander("Advanced flashcard export"):
                    flashcard_csv = flashcards_to_csv(flashcards)

                    st.download_button(
                        label="Download Flashcards as CSV",
                        data=flashcard_csv,
                        file_name=f"{base_filename}_flashcards.csv",
                        mime="text/csv",
                        key="download_flashcards_csv",
                    )

                    st.caption(
                        "CSV is useful if you want to import flashcards into another study tool."
                    )

        elif flashcards:
            st.markdown(
                """
                <div class="download-card-caption">
                    Download an interactive flashcard deck that opens in your browser.
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                '<div class="download-button-spacer"></div>',
                unsafe_allow_html=True,
            )

            deck_title = make_flashcard_deck_title(document_title)

            interactive_deck = flashcards_to_interactive_html(
                flashcards=flashcards,
                title=deck_title,
            )

            deck_col_1, deck_col_2 = st.columns([1, 2])

            with deck_col_1:
                st.download_button(
                    label="Download Interactive Study Deck",
                    data=interactive_deck,
                    file_name=f"{base_filename}_interactive_flashcards.html",
                    mime="text/html",
                    key="download_interactive_flashcards",
                )

            with deck_col_2:
                st.markdown(
                    """
                    <div class="download-helper-text">
                        Best for active recall, self-testing, and offline browser study.
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with st.expander("Advanced flashcard export"):
                flashcard_csv = flashcards_to_csv(flashcards)

                st.download_button(
                    label="Download Flashcards as CSV",
                    data=flashcard_csv,
                    file_name=f"{base_filename}_flashcards.csv",
                    mime="text/csv",
                    key="download_flashcards_csv",
                )

                st.caption(
                    "CSV is useful if you want to import flashcards into another study tool."
                )

        else:
            st.warning(
                "No flashcards were found in the generated output. Try generating again or choose Full Revision Pack."
            )


# --------------------------------------------------
# Generated result preview
# --------------------------------------------------

def make_result_preview(result, max_characters=1400):
    if len(result) <= max_characters:
        return result

    preview = result[:max_characters].rstrip()

    if "\n" in preview:
        preview = preview.rsplit("\n", 1)[0]

    return preview + "\n\n..."


def show_result_area(result, output_type):
    preview_text = make_result_preview(result)

    with st.expander("Preview generated content", expanded=False):
        st.caption("Open this to quickly check the generated study material.")

        with st.container(border=True):
            st.markdown(preview_text)

        if preview_text != result:
            st.info(
                "This is a short preview. The full generated content is included in the downloads."
            )

    show_download_buttons(result, output_type)


# --------------------------------------------------
# Generate button logic
# --------------------------------------------------

generate_clicked = st.button("Generate Revision Pack")

if generate_clicked:
    if not notes.strip() and not demo_mode:
        st.warning("Paste some notes first.")

    else:
        st.markdown(
            '<div class="section-title">Generated result</div>',
            unsafe_allow_html=True,
        )

        summary_col_1, summary_col_2, summary_col_3, summary_col_4 = st.columns(4)

        with summary_col_1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <strong>Subject</strong><br>{subject}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with summary_col_2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <strong>Level</strong><br>{difficulty}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with summary_col_3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <strong>Output</strong><br>{output_type}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with summary_col_4:
            export_summary = get_export_summary(output_type)

            st.markdown(
                f"""
                <div class="metric-card">
                    <strong>Exports</strong><br>{export_summary}
                </div>
                """,
                unsafe_allow_html=True,
            )

        if demo_mode:
            st.success("Demo mode active: sample density pack used. No API credits used.")

            loading_area = st.empty()

            with loading_area.container():
                duck_slot = st.empty()

                show_duck_loading(duck_slot, "Cleaning up your notes...")
                time.sleep(1.2)

                show_duck_loading(duck_slot, f"Generating your {output_type.lower()}...")
                time.sleep(1.2)

                show_duck_loading(duck_slot, "Preparing your downloads...")
                time.sleep(0.8)

            clear_loading_area(loading_area)

            try:
                st.toast("Sample revision pack ready.")
            except Exception:
                pass

            result = fake_output()
            show_result_area(result, output_type)

        else:
            st.warning("Live API mode: this may use API credits.")

            if not api_key or not client:
                st.error("No API key found. Check your .env file or Streamlit secrets.")

            else:
                prompt = build_prompt(
                    notes=notes,
                    output_type=output_type,
                    subject=subject,
                    difficulty=difficulty,
                    style=style,
                    flashcard_count=flashcard_count,
                )

                try:
                    loading_area = st.empty()

                    with loading_area.container():
                        duck_slot = st.empty()

                        show_duck_loading(duck_slot, "Cleaning up your notes...")
                        time.sleep(1.2)

                        show_duck_loading(duck_slot, f"Generating your {output_type.lower()}...")
                        result = generate_live_output(client, prompt)

                        show_duck_loading(duck_slot, "Preparing your downloads...")
                        time.sleep(0.8)

                    clear_loading_area(loading_area)

                    try:
                        st.toast("Revision pack ready.")
                    except Exception:
                        pass

                    show_result_area(result, output_type)

                except Exception as error:
                    clear_loading_area(loading_area)
                    st.error("Something went wrong.")
                    st.code(str(error))


# --------------------------------------------------
# Feedback and privacy sections
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Feedback & privacy</div>',
    unsafe_allow_html=True,
)

feedback_col, privacy_col = st.columns(2)

with feedback_col:
    with st.expander("Send feedback or report a bug"):
        st.markdown(
            f"""
            <div class="contact-card">
                <strong>Help improve {APP_NAME}</strong><br><br>
                Feedback is collected through a short form. You do not need to provide
                your name or email unless you want a reply.
                <div class="feedback-button-gap"></div>
                <a class="feedback-button" href="{FEEDBACK_FORM_URL}" target="_blank">
                    Open feedback form
                </a>
                <div class="feedback-link-gap"></div>
                You can also view the project on GitHub:<br>
                <a href="{GITHUB_REPO_URL}" target="_blank">
                    GitHub repository
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div style="margin-top: 1.1rem;">
                <strong>Useful feedback includes:</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write(
            """
            - Broken PDF, Markdown, or flashcard downloads
            - Confusing explanations
            - Missing subjects or levels
            - UI suggestions
            - Feature ideas
            """
        )

with privacy_col:
    with st.expander("Privacy notice"):
        st.write(
            """
            Nexa Study processes notes pasted into the app to generate study materials.

            Current MVP behaviour:
            - Notes are used to generate revision content.
            - Notes may be sent to an AI provider for processing.
            - The app does not intentionally store pasted notes.
            - Feedback is collected through a form rather than direct email.
            - Users should avoid entering sensitive personal information.

            Do not paste:
            - Passwords
            - Addresses
            - Student ID numbers
            - Medical or legal information
            - Private personal documents
            - Anything you would not want processed by an AI service
            """
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    f"""
    <div class="mini-footer">
        {APP_NAME} MVP • Built with Python, Streamlit, OpenAI API, ReportLab,
        and a suspicious amount of debugging.<br>
        <a href="{FEEDBACK_FORM_URL}" target="_blank">Send anonymous feedback</a>
    </div>
    """,
    unsafe_allow_html=True,
)