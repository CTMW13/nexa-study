CUSTOM_CSS = """
<style>
    :root {
        --baby-blue: #CBEFFF;
        --sky-blue: #A9DCF7;
        --deep-navy: #1E3A5F;
        --smoky-orange: #D9825B;
        --burnt-orange: #C96A43;
        --cream: #FFF8F1;
        --soft-lilac: #F3E8FF;
        --glass-lilac: rgba(243, 232, 255, 0.58);
        --glass-white: rgba(255, 255, 255, 0.42);
        --soft-border: rgba(255, 255, 255, 0.66);
    }

    html, body, [class*="css"] {
        font-family: "Segoe UI", Arial, Helvetica, sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 4% 88%, rgba(217, 130, 91, 0.48), transparent 34%),
            radial-gradient(circle at 0% 100%, rgba(201, 106, 67, 0.36), transparent 30%),
            radial-gradient(circle at 18% 96%, rgba(255, 248, 241, 0.42), transparent 30%),
            radial-gradient(circle at 88% 10%, rgba(255, 255, 255, 0.46), transparent 26%),
            radial-gradient(circle at 86% 78%, rgba(243, 232, 255, 0.36), transparent 34%),
            radial-gradient(circle at top left, rgba(217, 130, 91, 0.18), transparent 34%),
            linear-gradient(135deg, #CBEFFF 0%, #A9DCF7 43%, #F7FBFF 100%);
        color: var(--deep-navy);
    }

    section[data-testid="stSidebar"] {
        background:
            radial-gradient(circle at 10% 92%, rgba(217, 130, 91, 0.18), transparent 36%),
            linear-gradient(180deg, rgba(203, 239, 255, 0.82), rgba(255, 248, 241, 0.58));
        border-right: 1px solid rgba(30, 58, 95, 0.08);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 1180px;
    }

    h1, h2, h3, h4 {
        color: var(--deep-navy);
    }

    .hero-card {
        padding: 2.2rem 2.4rem;
        border-radius: 30px;
        background:
            radial-gradient(circle at 16% 18%, rgba(255, 255, 255, 0.42), transparent 28%),
            radial-gradient(circle at 90% 18%, rgba(217, 130, 91, 0.34), transparent 36%),
            linear-gradient(135deg, rgba(203, 239, 255, 0.92), rgba(169, 220, 247, 0.72));
        border: 1px solid rgba(255, 255, 255, 0.68);
        box-shadow: 0 24px 60px rgba(30, 58, 95, 0.18);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        margin-bottom: 1.4rem;
    }

    .hero-card h1 {
        font-family: Arial, Helvetica, sans-serif;
        font-size: clamp(2.6rem, 6vw, 4.6rem);
        line-height: 0.95;
        font-weight: 900;
        letter-spacing: -0.065em;
        color: var(--deep-navy);
        margin: 0 0 0.65rem 0;
    }

    .hero-card p {
        font-size: 1.12rem;
        line-height: 1.55;
        max-width: 820px;
        margin: 0;
        color: rgba(30, 58, 95, 0.86);
    }

    .beta-note {
        padding: 1rem 1.15rem;
        border-radius: 18px;
        background: rgba(255, 248, 241, 0.84);
        border: 1px solid rgba(217, 130, 91, 0.28);
        box-shadow: 0 12px 28px rgba(30, 58, 95, 0.08);
        margin: 1rem 0 1.3rem 0;
        color: var(--deep-navy);
    }

    .beta-note strong {
        color: var(--burnt-orange);
    }

    .section-card,
    .spark-card {
        padding: 1.3rem 1.35rem;
        border-radius: 24px;
        background:
            linear-gradient(135deg, rgba(255, 248, 241, 0.88), rgba(255, 255, 255, 0.58));
        border: 1px solid rgba(255, 255, 255, 0.72);
        box-shadow: 0 18px 42px rgba(30, 58, 95, 0.12);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        margin-bottom: 1rem;
    }

    .spark-card {
        border-left: 8px solid rgba(217, 130, 91, 0.94);
    }

    .spark-label {
        display: inline-block;
        padding: 0.32rem 0.68rem;
        border-radius: 999px;
        background: linear-gradient(135deg, var(--smoky-orange), var(--burnt-orange));
        color: white;
        font-size: 0.78rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
        letter-spacing: 0.01em;
    }

    .spark-card h4 {
        margin: 0 0 0.55rem 0;
        color: var(--deep-navy);
        font-weight: 850;
    }

    .spark-card p {
        color: rgba(30, 58, 95, 0.84);
        line-height: 1.5;
    }

    .info-card {
        padding: 1.25rem 1.35rem;
        border-radius: 22px;
        background: rgba(255, 248, 241, 0.82);
        border: 1px solid rgba(255, 255, 255, 0.72);
        box-shadow: 0 16px 36px rgba(30, 58, 95, 0.10);
        min-height: 150px;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
    }

    .info-card h4 {
        margin-top: 0;
        margin-bottom: 0.6rem;
        color: var(--deep-navy);
        font-weight: 850;
    }

    .info-card p {
        color: rgba(30, 58, 95, 0.84);
        line-height: 1.5;
        margin-bottom: 0;
    }

    .glass-card {
        background:
            radial-gradient(circle at 20% 14%, rgba(255, 255, 255, 0.78), transparent 34%),
            linear-gradient(135deg, rgba(255, 255, 255, 0.46), rgba(203, 239, 255, 0.28));
        border: 1px solid rgba(255, 255, 255, 0.66);
        border-radius: 24px;
        padding: 1.3rem;
        box-shadow: 0 18px 42px rgba(30, 58, 95, 0.15);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        color: var(--deep-navy);
        min-height: 172px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .glass-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 24px 52px rgba(30, 58, 95, 0.20);
    }

    .glass-card h4 {
        margin-top: 0;
        margin-bottom: 0.45rem;
        color: var(--deep-navy);
        font-weight: 850;
    }

    .glass-card p {
        color: rgba(30, 58, 95, 0.82);
        line-height: 1.45;
        margin-bottom: 0;
    }

    .glass-icon {
        width: 46px;
        height: 46px;
        border-radius: 17px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 0.9rem;
        background:
            radial-gradient(circle at 30% 20%, rgba(255, 255, 255, 0.98), transparent 38%),
            linear-gradient(135deg, rgba(255, 255, 255, 0.84), rgba(203, 239, 255, 0.36));
        border: 1px solid rgba(255, 255, 255, 0.78);
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.95),
            0 10px 25px rgba(30, 58, 95, 0.14);
        font-size: 1.35rem;
    }

    .premium-card,
    .premium-preview-card,
    .premium-feature-card,
    .locked-feature-card {
        position: relative;
        overflow: hidden;
        padding: 1rem 1rem;
        border-radius: 20px;
        background:
            radial-gradient(circle at 22% 12%, rgba(255, 255, 255, 0.82), transparent 35%),
            linear-gradient(135deg, rgba(243, 232, 255, 0.74), rgba(255, 255, 255, 0.36));
        border: 1px solid rgba(203, 154, 255, 0.62);
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.78),
            0 14px 32px rgba(76, 29, 149, 0.11);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        color: var(--deep-navy);
        transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
    }

    .premium-card::before,
    .premium-preview-card::before,
    .premium-feature-card::before,
    .locked-feature-card::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            linear-gradient(135deg, rgba(255, 255, 255, 0.55), transparent 42%),
            radial-gradient(circle at 90% 10%, rgba(217, 130, 91, 0.15), transparent 30%);
        pointer-events: none;
    }

    .premium-card:hover,
    .premium-preview-card:hover,
    .premium-feature-card:hover,
    .locked-feature-card:hover {
        transform: translateY(-2px);
        border-color: rgba(192, 132, 252, 0.78);
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.86),
            0 18px 38px rgba(76, 29, 149, 0.15);
    }

    .premium-card h4,
    .premium-preview-card h4,
    .premium-feature-card h4,
    .locked-feature-card h4 {
        position: relative;
        margin: 0 0 0.5rem 0;
        color: var(--deep-navy);
        font-weight: 850;
    }

    .premium-card p,
    .premium-preview-card p,
    .premium-feature-card p,
    .locked-feature-card p {
        position: relative;
        color: rgba(30, 58, 95, 0.84);
        line-height: 1.45;
        margin-bottom: 0;
    }

    .flashcard-review-card {
        padding: 1.7rem;
        border-radius: 28px;
        background:
            radial-gradient(circle at 18% 12%, rgba(255, 255, 255, 0.72), transparent 32%),
            linear-gradient(135deg, rgba(255, 255, 255, 0.48), rgba(203, 239, 255, 0.36));
        border: 1px solid rgba(255, 255, 255, 0.68);
        box-shadow: 0 22px 52px rgba(30, 58, 95, 0.16);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        margin: 1rem 0 1rem 0;
        min-height: 210px;
    }

    .flashcard-topline {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        align-items: center;
        margin-bottom: 1rem;
    }

    .flashcard-pill {
        display: inline-block;
        padding: 0.32rem 0.68rem;
        border-radius: 999px;
        background: rgba(217, 130, 91, 0.15);
        color: var(--burnt-orange);
        font-size: 0.78rem;
        font-weight: 850;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    .flashcard-status {
        display: inline-block;
        padding: 0.32rem 0.68rem;
        border-radius: 999px;
        background: rgba(30, 58, 95, 0.08);
        color: var(--deep-navy);
        font-size: 0.78rem;
        font-weight: 850;
    }

    .flashcard-question {
        font-size: 1.25rem;
        line-height: 1.45;
        color: var(--deep-navy);
        font-weight: 800;
        margin: 0.8rem 0 1rem 0;
    }

    .flashcard-answer {
        margin-top: 1.1rem;
        padding: 1rem 1.1rem;
        border-radius: 18px;
        background: rgba(255, 248, 241, 0.74);
        border: 1px solid rgba(217, 130, 91, 0.20);
        color: rgba(30, 58, 95, 0.9);
        line-height: 1.5;
    }

    .flashcard-answer strong {
        color: var(--burnt-orange);
    }

    .flashcard-progress-card {
        padding: 1rem 1.1rem;
        border-radius: 20px;
        background: rgba(255, 248, 241, 0.80);
        border: 1px solid rgba(255, 255, 255, 0.70);
        box-shadow: 0 12px 28px rgba(30, 58, 95, 0.09);
        margin: 0.8rem 0 1rem 0;
    }

    .flashcard-progress-card p {
        margin: 0.25rem 0;
        color: rgba(30, 58, 95, 0.86);
    }

    .contact-card {
        padding: 1.2rem 1.3rem;
        border-radius: 22px;
        background: rgba(255, 248, 241, 0.84);
        border: 1px solid rgba(255, 255, 255, 0.72);
        box-shadow: 0 16px 34px rgba(30, 58, 95, 0.10);
    }

    .feedback-button,
    .feedback-button:visited,
    .feedback-button:link,
    .feedback-button:hover,
    .feedback-button:active,
    .contact-card .feedback-button,
    .contact-card .feedback-button:visited,
    .contact-card .feedback-button:link,
    .contact-card .feedback-button:hover,
    .contact-card .feedback-button:active {
        display: inline-block;
        padding: 0.72rem 1rem;
        border-radius: 14px;
        background: linear-gradient(135deg, var(--smoky-orange), var(--burnt-orange));
        color: white !important;
        text-decoration: none !important;
        font-weight: 800;
        box-shadow: 0 10px 24px rgba(201, 106, 67, 0.26);
        margin-top: 0.5rem;
    }

    .footer {
        text-align: center;
        color: rgba(30, 58, 95, 0.72);
        font-size: 0.9rem;
        padding: 2rem 0 0.8rem 0;
    }

    .footer a {
        color: var(--burnt-orange) !important;
        font-weight: 700;
        text-decoration: none;
    }

    div.stButton > button,
    div.stDownloadButton > button {
        background: linear-gradient(135deg, var(--smoky-orange), var(--burnt-orange));
        color: white;
        border: 0;
        border-radius: 14px;
        padding: 0.7rem 1rem;
        font-weight: 800;
        box-shadow: 0 10px 24px rgba(201, 106, 67, 0.24);
        transition: transform 0.16s ease, box-shadow 0.16s ease;
    }

    div.stButton > button:hover,
    div.stDownloadButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 30px rgba(201, 106, 67, 0.30);
        color: white;
    }

    textarea,
    input,
    .stTextInput input,
    .stTextArea textarea {
        border-radius: 16px !important;
        border: 1px solid rgba(30, 58, 95, 0.16) !important;
        background: rgba(255, 255, 255, 0.78) !important;
        color: var(--deep-navy) !important;
    }

    div[data-baseweb="select"] > div {
        background: rgba(255, 255, 255, 0.84) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(30, 58, 95, 0.14) !important;
        color: var(--deep-navy) !important;
    }

    div[data-baseweb="select"] svg {
        opacity: 0.58 !important;
    }

    div[data-baseweb="popover"] {
        border-radius: 14px !important;
    }

    [data-testid="stExpander"] {
        background: rgba(255, 248, 241, 0.78);
        border: 1px solid rgba(255, 255, 255, 0.72);
        border-radius: 18px;
        box-shadow: 0 12px 26px rgba(30, 58, 95, 0.08);
        overflow: hidden;
    }

    [data-testid="stExpander"] summary {
        color: var(--deep-navy);
        font-weight: 800;
    }

    .stMarkdown h2,
    .stMarkdown h3 {
        color: var(--deep-navy);
    }

    .small-muted {
        color: rgba(30, 58, 95, 0.68);
        font-size: 0.92rem;
    }
</style>
"""
