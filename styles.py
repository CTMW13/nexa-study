CUSTOM_CSS = """
<style>
    :root {
        --baby-blue: #CBEFFF;
        --sky-blue: #A9DCF7;
        --deep-blue: #1E3A5F;
        --mid-blue: #274B72;
        --smoky-orange: #D9825B;
        --burnt-orange: #C96A43;
        --cream: #FFF8F1;
        --soft-white: #FFFFFF;
        --slate: #334155;
        --muted-slate: #64748B;

        --lilac: #F3E8FF;
        --lilac-strong: #E9D5FF;
        --purple-border: #C084FC;
        --purple-text: #4C1D95;

        --border-blue: rgba(30, 58, 95, 0.14);
        --border-orange: rgba(217, 130, 91, 0.22);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(169, 220, 247, 0.95), transparent 35%),
            radial-gradient(circle at top right, rgba(217, 130, 91, 0.24), transparent 34%),
            radial-gradient(circle at bottom right, rgba(217, 130, 91, 0.38), transparent 38%),
            radial-gradient(circle at 86% 88%, rgba(233, 213, 255, 0.42), transparent 32%),
            linear-gradient(135deg, #CBEFFF 0%, #E7F6FF 42%, #FFF8F1 100%);
        color: var(--deep-blue);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1180px;
    }

    .stApp,
    .stApp p,
    .stApp span,
    .stApp label,
    .stApp div,
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp h5,
    .stApp h6 {
        color: var(--deep-blue);
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stWidgetLabel"] label,
    [data-testid="stWidgetLabel"] p {
        color: var(--deep-blue) !important;
    }

    /* --------------------------------------------------
       Hero section
       -------------------------------------------------- */

    .hero-card {
        padding: 2.4rem;
        border-radius: 28px;
        background:
            radial-gradient(circle at 88% 18%, rgba(217, 130, 91, 0.26), transparent 34%),
            linear-gradient(135deg, rgba(169, 220, 247, 0.98) 0%, rgba(203, 239, 255, 0.96) 42%, rgba(217, 130, 91, 0.78) 100%);
        color: var(--deep-blue);
        box-shadow:
            0 24px 60px rgba(30, 58, 95, 0.18),
            inset 0 1px 0 rgba(255, 255, 255, 0.62);
        border: 1px solid rgba(255, 255, 255, 0.72);
        margin-bottom: 1.5rem;
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }

    .hero-title {
        font-size: 3.15rem;
        font-weight: 850;
        margin-bottom: 0.55rem;
        letter-spacing: -0.045em;
        color: var(--deep-blue) !important;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        line-height: 1.7;
        max-width: 830px;
        color: var(--mid-blue) !important;
    }

    .hero-badges {
        margin-top: 1.25rem;
    }

    .badge {
        display: inline-block;
        padding: 0.48rem 0.78rem;
        border-radius: 999px;
        background: rgba(255, 248, 241, 0.82);
        border: 1px solid rgba(201, 106, 67, 0.28);
        color: var(--deep-blue) !important;
        margin-right: 0.45rem;
        margin-bottom: 0.45rem;
        font-size: 0.9rem;
        font-weight: 650;
    }

    /* --------------------------------------------------
       Daily spark card
       -------------------------------------------------- */

    .spark-card {
        background: rgba(255, 248, 241, 0.94);
        border: 1px solid rgba(217, 130, 91, 0.24);
        border-left: 7px solid var(--smoky-orange);
        border-radius: 22px;
        padding: 1.25rem 1.35rem;
        margin-bottom: 1.4rem;
        box-shadow: 0 12px 30px rgba(30, 58, 95, 0.10);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }

    .spark-label {
        display: inline-block;
        background: linear-gradient(135deg, #D9825B 0%, #C96A43 100%);
        color: white !important;
        padding: 0.34rem 0.65rem;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 800;
        margin-bottom: 0.7rem;
    }

    .spark-title {
        font-size: 1.25rem;
        font-weight: 850;
        color: var(--deep-blue) !important;
        margin-bottom: 0.55rem;
    }

    .spark-text {
        color: var(--slate) !important;
        line-height: 1.6;
        margin-bottom: 0.45rem;
    }

    .spark-source a {
        color: var(--burnt-orange) !important;
        font-weight: 800;
        text-decoration: none;
    }

    .spark-source a:hover {
        text-decoration: underline;
    }

    /* --------------------------------------------------
       Intro and metric cards
       -------------------------------------------------- */

    .info-card {
        position: relative;
        overflow: hidden;
        background: rgba(255, 248, 241, 0.95);
        padding: 1.2rem;
        border-radius: 20px;
        border: 1px solid var(--border-orange);
        box-shadow: 0 10px 28px rgba(30, 58, 95, 0.09);
        min-height: 150px;
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }

    .info-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, rgba(217, 130, 91, 0.75), rgba(169, 220, 247, 0.75));
    }

    .info-card h3 {
        margin-top: 0;
        margin-bottom: 0.5rem;
        font-size: 1.05rem;
        color: var(--deep-blue) !important;
    }

    .info-card p {
        color: var(--slate) !important;
        font-size: 0.95rem;
        line-height: 1.55;
    }

    .metric-card {
        background: rgba(255, 255, 255, 0.90);
        padding: 0.85rem 1rem;
        border-radius: 16px;
        border: 1px solid rgba(169, 220, 247, 0.95);
        color: var(--deep-blue) !important;
        box-shadow: 0 8px 22px rgba(30, 58, 95, 0.06);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }

    .metric-card strong {
        color: var(--burnt-orange) !important;
    }

    /* --------------------------------------------------
       Lilac glass premium cards
       -------------------------------------------------- */

    .premium-card {
        position: relative;
        overflow: hidden;
        display: block;
        background:
            radial-gradient(circle at 18% 12%, rgba(255, 255, 255, 0.84), transparent 34%),
            radial-gradient(circle at 96% 0%, rgba(217, 130, 91, 0.12), transparent 32%),
            linear-gradient(135deg, rgba(243, 232, 255, 0.72), rgba(255, 255, 255, 0.46));
        padding: 1rem 1.05rem;
        border-radius: 17px;
        border: 1px solid rgba(192, 132, 252, 0.58);
        margin-bottom: 1rem;
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.84),
            0 12px 28px rgba(76, 29, 149, 0.10);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
    }

    .premium-card::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            linear-gradient(135deg, rgba(255, 255, 255, 0.55), transparent 42%),
            radial-gradient(circle at 92% 12%, rgba(217, 130, 91, 0.13), transparent 30%);
        pointer-events: none;
    }

    .premium-card:hover {
        transform: translateY(-2px);
        border-color: rgba(192, 132, 252, 0.78);
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.86),
            0 14px 30px rgba(76, 29, 149, 0.13);
    }

    .premium-card-title {
        position: relative;
        font-weight: 800;
        color: var(--purple-text) !important;
        margin-bottom: 0.3rem;
    }

    .premium-card-text {
        position: relative;
        color: #5B5270 !important;
        font-size: 0.86rem;
        line-height: 1.4;
    }

    /* --------------------------------------------------
       Main text sections
       -------------------------------------------------- */

    .section-title {
        font-size: 1.55rem;
        font-weight: 800;
        color: var(--deep-blue) !important;
        margin-top: 1.35rem;
        margin-bottom: 0.45rem;
    }

    .section-caption {
        color: var(--muted-slate) !important;
        margin-bottom: 1rem;
    }

    .privacy-note {
        background: rgba(255, 248, 241, 0.88);
        border-left: 5px solid var(--smoky-orange);
        border-radius: 14px;
        padding: 0.9rem 1rem;
        color: var(--slate) !important;
        margin-top: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 10px 24px rgba(30, 58, 95, 0.07);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }

    .contact-card {
        background: rgba(255, 248, 241, 0.94);
        padding: 1rem;
        border-radius: 18px;
        border: 1px solid rgba(217, 130, 91, 0.24);
        box-shadow: 0 10px 24px rgba(30, 58, 95, 0.07);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }

    .contact-card a {
        color: var(--burnt-orange) !important;
        font-weight: 800;
        text-decoration: none;
    }

    .contact-card a:hover {
        text-decoration: underline;
    }

    .feedback-button {
        display: inline-block;
        margin-top: 0.8rem;
        padding: 0.72rem 1rem;
        border-radius: 14px;
        background: linear-gradient(135deg, #D9825B 0%, #C96A43 100%);
        color: white !important;
        font-weight: 850;
        text-decoration: none !important;
        box-shadow: 0 10px 22px rgba(201, 106, 67, 0.22);
        transition:
            transform 0.16s ease,
            box-shadow 0.16s ease,
            filter 0.16s ease;
    }

    .feedback-button,
    .feedback-button:visited,
    .feedback-button:link,
    .feedback-button:hover,
    .feedback-button:active {
        color: white !important;
        text-decoration: none !important;
    }

    .feedback-button:hover {
        transform: translateY(-1px);
        filter: brightness(1.03);
        box-shadow: 0 14px 28px rgba(201, 106, 67, 0.28);
    }

    /* --------------------------------------------------
       Sidebar
       -------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background:
            radial-gradient(circle at bottom right, rgba(217, 130, 91, 0.16), transparent 34%),
            linear-gradient(180deg, #CBEFFF 0%, #E7F6FF 48%, #FFF8F1 100%);
        border-right: 1px solid rgba(30, 58, 95, 0.10);
    }

    section[data-testid="stSidebar"] * {
        color: var(--deep-blue) !important;
    }

    section[data-testid="stSidebar"] .stCaptionContainer,
    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        color: var(--muted-slate) !important;
    }

    section[data-testid="stSidebar"] hr {
        border: none;
        height: 1px;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(30, 58, 95, 0.18),
            transparent
        );
        margin: 1.8rem 0;
    }

    /* --------------------------------------------------
       Buttons
       -------------------------------------------------- */

    div.stButton > button {
        background: linear-gradient(135deg, #D9825B 0%, #C96A43 100%);
        color: white !important;
        border: none;
        border-radius: 16px;
        padding: 0.78rem 1.15rem;
        font-weight: 800;
        box-shadow: 0 10px 22px rgba(201, 106, 67, 0.25);
        transition:
            transform 0.16s ease,
            box-shadow 0.16s ease,
            filter 0.16s ease;
    }

    div.stButton > button * {
        color: white !important;
    }

    div.stButton > button:hover {
        border: none;
        color: white !important;
        transform: translateY(-1px);
        filter: brightness(1.03);
        box-shadow: 0 14px 28px rgba(201, 106, 67, 0.30);
    }

    div.stDownloadButton > button {
        border-radius: 16px;
        padding: 0.72rem 1rem;
        font-weight: 750;
        border: 1px solid rgba(201, 106, 67, 0.28);
        background: rgba(255, 255, 255, 0.95) !important;
        color: var(--deep-blue) !important;
    }

    div.stDownloadButton > button * {
        color: var(--deep-blue) !important;
    }

    /* --------------------------------------------------
       Text area and inputs
       -------------------------------------------------- */

    textarea,
    .stTextArea textarea {
        background: #FFFFFF !important;
        color: var(--deep-blue) !important;
        caret-color: #000000 !important;
        border: 1.5px solid rgba(192, 132, 252, 0.62) !important;
        border-radius: 18px !important;
        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.85),
            0 12px 28px rgba(76, 29, 149, 0.08) !important;
    }

    textarea:focus,
    .stTextArea textarea:focus {
        background: #FFFFFF !important;
        color: var(--deep-blue) !important;
        caret-color: #000000 !important;
        border: 1.5px solid rgba(192, 132, 252, 0.82) !important;
        box-shadow:
            0 0 0 3px rgba(192, 132, 252, 0.16),
            0 14px 32px rgba(76, 29, 149, 0.10) !important;
    }

    textarea::placeholder,
    .stTextArea textarea::placeholder,
    input::placeholder {
        color: rgba(30, 58, 95, 0.45) !important;
    }

    input {
        background-color: #FFFFFF !important;
        color: var(--deep-blue) !important;
        caret-color: #000000 !important;
        border: 1px solid rgba(192, 132, 252, 0.50) !important;
        border-radius: 16px !important;
    }

    input:focus {
        color: var(--deep-blue) !important;
        caret-color: #000000 !important;
        border: 1px solid rgba(192, 132, 252, 0.82) !important;
    }

    /* --------------------------------------------------
       Select boxes
       -------------------------------------------------- */

    [data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: var(--deep-blue) !important;
        border: 1px solid rgba(30, 58, 95, 0.18) !important;
        border-radius: 14px !important;
        box-shadow: none !important;
    }

    [data-baseweb="select"] span,
    [data-baseweb="select"] div {
        color: var(--deep-blue) !important;
    }

    [data-baseweb="select"] svg {
        color: var(--deep-blue) !important;
        fill: var(--deep-blue) !important;
    }

    [data-baseweb="select"] input {
        color: transparent !important;
        caret-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
        width: 1px !important;
        min-width: 1px !important;
        max-width: 1px !important;
        padding: 0 !important;
        margin: 0 !important;
        opacity: 0 !important;
    }

    [data-baseweb="select"] input:focus {
        color: transparent !important;
        caret-color: transparent !important;
        outline: none !important;
        border: none !important;
        box-shadow: none !important;
        opacity: 0 !important;
    }

    [data-baseweb="select"] [data-testid="stIconMaterial"] {
        background: transparent !important;
    }

    [data-baseweb="select"] > div > div:last-child {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 1px solid rgba(30, 58, 95, 0.18) !important;
        border-radius: 14px !important;
        box-shadow: none !important;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] > div > div {
        background: transparent !important;
        box-shadow: none !important;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] input {
        opacity: 0 !important;
        color: transparent !important;
        caret-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
        width: 1px !important;
        min-width: 1px !important;
        max-width: 1px !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    [data-baseweb="popover"] {
        background-color: #FFFFFF !important;
    }

    [role="listbox"] {
        background-color: #FFFFFF !important;
    }

    [role="option"] {
        background-color: #FFFFFF !important;
        color: var(--deep-blue) !important;
    }

    [role="option"]:hover {
        background-color: #CBEFFF !important;
        color: var(--deep-blue) !important;
    }

    /* --------------------------------------------------
       Alerts, expanders, checkboxes, tabs
       -------------------------------------------------- */

    [data-testid="stAlert"] {
        border-radius: 16px;
        color: var(--deep-blue) !important;
    }

    [data-testid="stAlert"] * {
        color: var(--deep-blue) !important;
    }

    [data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.78);
        border-radius: 16px;
        border: 1px solid rgba(217, 130, 91, 0.24);
        overflow: hidden;
        box-shadow: 0 12px 30px rgba(30, 58, 95, 0.08);
    }

    [data-testid="stExpander"] * {
        color: var(--deep-blue) !important;
    }

    [data-testid="stExpander"] summary {
        background: linear-gradient(135deg, rgba(217, 130, 91, 0.92) 0%, rgba(201, 106, 67, 0.92) 100%) !important;
        border-radius: 14px;
        padding: 0.45rem 0.7rem !important;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.18);
    }

    [data-testid="stExpander"] summary * {
        color: white !important;
        font-weight: 800 !important;
    }

    [data-testid="stExpander"] summary:hover {
        background: linear-gradient(135deg, #D9825B 0%, #C96A43 100%) !important;
    }

    [data-testid="stCheckbox"] label,
    [data-testid="stCheckbox"] p,
    [data-testid="stCheckbox"] span {
        color: var(--deep-blue) !important;
    }

    [data-baseweb="tab-list"] {
        gap: 0.35rem;
    }

    [data-baseweb="tab"] {
        color: var(--deep-blue) !important;
        border-radius: 999px !important;
        padding: 0.35rem 0.9rem !important;
    }

    [aria-selected="true"][data-baseweb="tab"] {
        background: rgba(243, 232, 255, 0.88) !important;
        color: var(--purple-text) !important;
        font-weight: 800 !important;
    }

    /* --------------------------------------------------
       Tiny rubber duck loading animation
       -------------------------------------------------- */

    .duck-loading {
        display: inline-flex;
        align-items: center;
        gap: 0.65rem;
        padding: 0.62rem 0.9rem;
        border-radius: 999px;
        background: rgba(255, 248, 241, 0.86);
        border: 1px solid rgba(217, 130, 91, 0.22);
        box-shadow: 0 10px 24px rgba(30, 58, 95, 0.08);
        margin: 0.35rem 0 0.65rem 0;
        font-size: 0.92rem;
        font-weight: 700;
        color: var(--deep-blue) !important;
    }

    .duck-loading span {
        color: var(--deep-blue) !important;
    }

    .rubber-duck {
        position: relative;
        width: 38px;
        height: 28px;
        display: inline-block;
        animation: duck-bob 1.05s ease-in-out infinite;
        transform-origin: center bottom;
        flex: 0 0 auto;
    }

    .rubber-duck::before {
        content: "";
        position: absolute;
        left: 3px;
        bottom: 2px;
        width: 27px;
        height: 17px;
        background: linear-gradient(135deg, #FFE66B 0%, #FFD84D 45%, #F6B91A 100%);
        border-radius: 62% 58% 56% 54%;
        box-shadow:
            inset 0 2px 2px rgba(255, 255, 255, 0.50),
            inset -2px -2px 4px rgba(197, 131, 0, 0.18),
            0 5px 10px rgba(217, 130, 91, 0.24);
    }

    .rubber-duck::after {
        content: "";
        position: absolute;
        left: 18px;
        top: 1px;
        width: 14px;
        height: 14px;
        background: linear-gradient(135deg, #FFF176 0%, #FFD84D 55%, #F6B91A 100%);
        border-radius: 50%;
        box-shadow:
            inset 0 2px 2px rgba(255, 255, 255, 0.50),
            inset -1px -2px 3px rgba(197, 131, 0, 0.15);
    }

    .duck-beak {
        position: absolute;
        left: 30px;
        top: 8px;
        width: 9px;
        height: 6px;
        background: linear-gradient(135deg, #FF9F43, #F97316);
        border-radius: 70% 45% 45% 70%;
        z-index: 3;
    }

    .duck-eye {
        position: absolute;
        left: 27px;
        top: 5px;
        width: 3px;
        height: 3px;
        background: #1E3A5F;
        border-radius: 50%;
        z-index: 4;
    }

    .duck-shine {
        position: absolute;
        left: 10px;
        bottom: 13px;
        width: 8px;
        height: 4px;
        background: rgba(255, 255, 255, 0.48);
        border-radius: 999px;
        transform: rotate(-12deg);
        z-index: 4;
    }

    @keyframes duck-bob {
        0% {
            transform: translateY(0) rotate(0deg);
        }

        35% {
            transform: translateY(-3px) rotate(-3deg);
        }

        70% {
            transform: translateY(1px) rotate(2deg);
        }

        100% {
            transform: translateY(0) rotate(0deg);
        }
    }

    /* --------------------------------------------------
       Footer
       -------------------------------------------------- */

    .mini-footer {
        color: var(--muted-slate) !important;
        font-size: 0.85rem;
        margin-top: 2rem;
        text-align: center;
        padding: 1.2rem 0 0.4rem 0;
        opacity: 0.88;
    }

    .mini-footer a {
        color: var(--burnt-orange) !important;
        font-weight: 800;
        text-decoration: none;
    }

    .mini-footer a:hover {
        text-decoration: underline;
    }

    .feedback-button-gap {
        height: 0.35rem;
    }

    .feedback-link-gap {
        height: 0.75rem;
    }

    /* --------------------------------------------------
       Final UI fixes
       -------------------------------------------------- */

    /* Generate button text boldness */
    div.stButton > button,
    div.stButton > button p,
    div.stButton > button span {
        font-weight: 850 !important;
    }

    /* Download button text boldness */
    div.stDownloadButton > button,
    div.stDownloadButton > button p,
    div.stDownloadButton > button span {
        font-weight: 850 !important;
    }

    /* Make bordered Streamlit containers feel more like cards */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: rgba(217, 130, 91, 0.24) !important;
        border-radius: 18px !important;
        box-shadow: 0 10px 24px rgba(30, 58, 95, 0.07) !important;
        background: rgba(255, 248, 241, 0.58) !important;
    }

    /* Change focus border from lilac/pink to thematic orange */
    textarea:focus,
    .stTextArea textarea:focus,
    input:focus {
        border-color: rgba(217, 130, 91, 0.82) !important;
        box-shadow:
            0 0 0 3px rgba(217, 130, 91, 0.16),
            0 14px 32px rgba(30, 58, 95, 0.10) !important;
    }

    /* Select dropdown focus colour */
    [data-baseweb="select"] > div:focus-within {
        border-color: rgba(217, 130, 91, 0.82) !important;
        box-shadow:
            0 0 0 3px rgba(217, 130, 91, 0.14) !important;
    }

    /* Small feedback spacing fix */
    .feedback-button-gap {
        height: 0.35rem;
    }

    .feedback-link-gap {
        height: 0.75rem;
    }

    /* --------------------------------------------------
       Downloads section
       -------------------------------------------------- */

    .download-card-marker {
        display: none;
    }

    .st-key-downloads_card {
        background: rgba(255, 248, 241, 0.94) !important;
        border: 1.5px solid rgba(217, 130, 91, 0.34) !important;
        border-radius: 22px !important;
        box-shadow:
            0 16px 36px rgba(30, 58, 95, 0.10),
            inset 0 1px 0 rgba(255, 255, 255, 0.74) !important;

        /* Keep heading near the top-left */
        padding-top: 0.85rem !important;
        padding-left: 1.8rem !important;
        padding-right: 1.8rem !important;

        /* Smaller, neater card height */
        padding-bottom: 1.6rem !important;
        min-height: 190px !important;

        margin-top: 1.25rem !important;
        margin-bottom: 0.9rem !important;
    }

    .st-key-downloads_card [data-testid="stVerticalBlock"] {
        gap: 0.65rem !important;
    }

    .download-card-main-title {
        font-size: 2rem;
        font-weight: 850;
        color: var(--deep-blue) !important;
        margin: 0 0 0.55rem 0 !important;
        letter-spacing: -0.025em;
    }

    .download-section-subheading {
        font-size: 1.22rem;
        font-weight: 850;
        color: var(--deep-blue) !important;
        margin-top: 1rem;
        margin-bottom: 0.3rem;
    }

    .download-card-caption {
        color: var(--mid-blue) !important;
        font-size: 1rem;
        line-height: 1.5;
        margin-bottom: 0 !important;
    }

    .download-button-spacer {
        height: 0.45rem;
    }

    .download-helper-text {
        color: var(--mid-blue) !important;
        font-size: 0.95rem;
        line-height: 1.45;
        padding-top: 0.55rem;
    }

    .st-key-downloads_card div.stDownloadButton > button {
        width: 100%;
        min-height: 3rem;
        font-weight: 850 !important;
    }

    .st-key-downloads_card div.stDownloadButton > button p,
    .st-key-downloads_card div.stDownloadButton > button span {
        font-weight: 850 !important;
    }

    .st-key-downloads_card [data-testid="stExpander"] {
        width: 100%;
        margin-top: 0.65rem;
    }

    .st-key-downloads_card [data-testid="stExpander"] summary {
        border-radius: 14px !important;
    }

    /* --------------------------------------------------
       Generated result spacing
       -------------------------------------------------- */

    [data-testid="stExpander"] {
        margin-top: 0.85rem;
    }
</style>
"""