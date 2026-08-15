import pymupdf
import re


def extract_text_from_pdf(file_path):

    document = pymupdf.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_email(text):

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text):

    pattern = r'(?:\+91[\s-]?)?[6-9]\d{4}[\s-]?\d{5}'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None

def extract_name(text):

    lines = text.strip().split("\n")

    for line in lines:

        line = line.strip()

        if line and "@" not in line and not re.search(r'\d', line):

            return line

    return None
SKILLS = [
    "Python",
    "Java",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "Scikit-learn",
    "H2O",
    "TPOT",
    "CNN",
    "LSTM",
    "Transfer Learning",
    "LangChain",
    "LangGraph",
    "RAG",
    "FAISS",
    "LoRA",
    "Hugging Face",
    "Mistral AI",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "OpenCV",
    "Pillow",
    "Git",
    "Docker",
    "Jenkins",
    "Oracle SQL",
    "Jupyter",
    "VS Code",
    "Google Colab",
    "Power BI",
    "Tableau",
    "Qlik Sense",
    "Flask",
    "Streamlit"
]


def extract_skills(text):

    found_skills = []

    text_lower = text.lower()

    for skill in SKILLS:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills