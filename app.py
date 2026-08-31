import json
import os
import re
import smtplib
import ssl
import urllib.parse
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from typing import Any, Dict, List, Tuple

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

load_dotenv()

ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT

app = FastAPI(title="Eman Portfolio Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount assets folder for images/files
assets_path = STATIC_DIR / "assets"
if assets_path.exists():
    app.mount("/assets", StaticFiles(directory=str(assets_path)), name="assets")


class ChatRequest(BaseModel):
    message: str


class ContactRequest(BaseModel):
    name: str
    email: str
    subject: str
    message: str


# ─────────────────────────────────────────────
#  KNOWLEDGE BASE — trained on Eman's CV & portfolio
# ─────────────────────────────────────────────

KNOWLEDGE_BASE: List[Dict] = [
    # ── GREETINGS ──
    {
        "patterns": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening", "sup", "what's up", "salam", "assalam"],
        "response": "👋 Hello! I'm <b>Emuu</b>, Eman Fatima's personal AI assistant. Eman Fatima is an <b>Artificial Intelligence Engineer and Cybersecurity Analyst</b>. I can tell you all about her current role at CIT (Center of Information Technology), internships, Quran pronunciation checker, audio forensics, skills, projects, and research. What would you like to know? 😊"
    },
    {
        "patterns": ["how are you", "how r u", "how are u", "you doing", "hows it going"],
        "response": "I'm doing great, thanks for asking! I'm here to help you learn all about Eman Fatima, Artificial Intelligence Engineer & Cybersecurity Analyst. Feel free to ask me anything! 😄"
    },
    {
        "patterns": ["who are you", "what are you", "who is this", "introduce yourself", "your name"],
        "response": "I'm <b>Emuu</b> — Eman Fatima's personal AI assistant built right into her portfolio! Eman Fatima is an <b>Artificial Intelligence Engineer & Cybersecurity Analyst</b>. I know everything about her work at CIT, AI internships, projects, skills, research, and experience. Go ahead, ask me anything! 🤖"
    },
    {
        "patterns": ["bye", "goodbye", "see you", "take care", "later"],
        "response": "Goodbye! Feel free to come back anytime you have questions about Eman. Don't forget to check out her amazing projects! 👋"
    },
    {
        "patterns": ["thank you", "thanks", "thank u", "thx", "appreciate"],
        "response": "You're welcome! 😊 If you have more questions about Eman's skills, projects, or experience, I'm always here. Feel free to contact her at <b>emanfatima60860@gmail.com</b>!"
    },

    # ── ABOUT EMAN ──
    {
        "patterns": ["who is eman", "who is she", "tell me about eman", "about eman", "what does eman do", "what is eman", "eman fatima", "introduce eman", "who is iman", "about iman", "iman fatima"],
        "response": "<b>Eman Fatima</b> is an <b>Artificial Intelligence Engineer and Cybersecurity Analyst</b> with a BS in Cybersecurity & Digital Forensics from The Islamia University of Bahawalpur (CGPA <b>3.50</b>).<br><br>💼 <b>Current Position:</b> Working at <b>Center of Information Technology (CIT)</b> under Director <b>Sir Amar Jafri</b>, building the official WordPress website (www.cit.com.pk), custom plugins, AI chatbot integrations, n8n/NIT workflow automation, and managing website cybersecurity.<br><br>⭐ <b>Core Expertise:</b><br>🤖 AI/ML & Deep Learning Model Selection & Training<br>⚡ Workflow Automation (n8n / NIT automation)<br>🎙️ Audio Forensics, Diarization & Tamper Detection<br>🔐 Threat Detection & Network Security<br>⛓️ Blockchain Security (Ethereum, IPFS)"
    },
    {
        "patterns": ["specialization", "what she specializes", "area of expertise", "expertise", "specialty"],
        "response": "Eman specializes in: 🤖 <b>Artificial Intelligence & Deep Learning</b>, ⚡ <b>AI & Workflow Automation (n8n)</b>, 🔐 <b>Cybersecurity & Threat Detection</b>, 🎙️ <b>Digital & Audio Forensics</b>, 🌐 <b>WordPress & Custom Plugin Development</b>, and ⛓️ <b>Blockchain Security</b>."
    },

    # ── CIT (CURRENT JOB & PROJECT) ──
    {
        "patterns": ["cit", "center of information technology", "amar", "jaffri", "jafri", "aman", "ijaz", "cit.com.pk", "wordpress", "custom plugin", "custom plugins", "plugins", "geological", "geolocation", "geo-location", "database", "backend", "current job", "current role", "where does she work currently"],
        "response": "💼 <b>Center of Information Technology (CIT) · Pakistan</b><br>📅 <b>Period:</b> Jul 2026 – Present (Selected: 20 July 2026)<br>👤 <b>Director:</b> Sir Amar Jaffri<br>👤 <b>Supervisor:</b> Sir Aman Ijaz<br>🌐 <b>Website:</b> <a href=\"https://www.cit.com.pk\" target=\"_blank\">www.cit.com.pk</a><br><br><b>Responsibilities & Projects at CIT:</b><br>• <b>Official Website:</b> Making the complete WordPress portal (<a href=\"https://www.cit.com.pk\" target=\"_blank\">www.cit.com.pk</a>) including About Us, Events, Directory Links, Contact, and Geo-location / geological mapping features.<br>• <b>Custom Plugins:</b> Engineered bespoke WordPress plugins tailored specifically for CIT portal needs.<br>• <b>Database & Backend:</b> Designed database structures, optimized MySQL queries, and built scalable backend API workflows.<br>• <b>AI Chatbots & Automation:</b> Built custom AI chatbots and implemented <b>n8n & NIT automated workflow pipelines</b>.<br>• <b>Cybersecurity:</b> Managing website security posture, vulnerability prevention, and system hardening under Director <b>Sir Amar Jaffri</b> and Supervisor <b>Sir Aman Ijaz</b>."
    },

    # ── CMIT INTERNSHIP (BUILTINSOFT) ──
    {
        "patterns": ["cmit", "builtinsoft", "built in soft", "quran", "pronunciation", "recitation", "tajweed", "mispronounced", "deep learning model", "ml models"],
        "response": "🤖 <b>CMIT Internship Program — BuiltinSoft</b><br>📅 <b>Period:</b> 8 Jan 2026 – 8 Jun 2026 · Rahim Yar Khan, Onsite<br><br><b>Key Highlights:</b><br>• Developed the <b>Quran Pronunciation Checker</b> website (AI Recitation Evaluator) that captures audio and pinpoints exact mispronounced words with phoneme-level accuracy feedback.<br>• Trained, evaluated, and benchmarked multiple Machine Learning and Deep Learning models (KNN, K-Means, Random Forest, SVM, Decision Trees, CNNs), matching data distributions to optimal model architectures and training pipelines.<br>• Built automated workflow pipelines and data processing routines using n8n and automation tools (NIT and workflow automation).<br>• Implemented conversational chatbot logic with Markov Chain algorithms and developed Django REST APIs."
    },

    # ── NCCFL / AIR UNIVERSITY INTERNSHIP ──
    {
        "patterns": ["ncc", "nccfl", "air university", "national cyber", "cyber crime", "audio forensic", "diarization", "temporal", "tamper", "fake audio", "forensics lab", "islamabad"],
        "response": "🛡️ <b>Cybersecurity & Audio Forensics Intern — NCCFL / Air University</b><br>📅 <b>Period:</b> Jul 2025 – Sep 2025 · Islamabad (Hybrid)<br><br><b>Key Highlights:</b><br>• Built an end-to-end <b>Audio Forensics & Tampering Detection</b> website that analyzes audio authenticity to identify fake/tampered recordings and delivers comprehensive forensic audit reports to users.<br>• Applied advanced forensic techniques: <b>speaker diarization, temporal inconsistencies detection, timestamp verification, and acoustic metadata analysis</b>.<br>• Performed sentiment analysis, acoustic feature modeling, and gender classification in an active national cybersecurity research environment.<br>• Prepared detailed technical reports and presented findings to cybersecurity researchers."
    },

    # ── AUTOMATION & WORKFLOWS ──
    {
        "patterns": ["automation", "n8n", "workflow", "nit", "workflows", "automate"],
        "response": "⚡ <b>Workflow & AI Automation (n8n / NIT):</b><br><br>Eman has extensive experience building automated pipelines and workflows:<br>• <b>At CIT:</b> Automating WordPress data flows, notifications, and custom plugin integrations via n8n.<br>• <b>At CMIT:</b> Built automated data pipelines and model preprocessing routines.<br>• Expertise in connecting APIs, webhooks, databases, and AI models into seamless automated workflows."
    },

    # ── ALL WORK EXPERIENCES ──
    {
        "patterns": ["experience", "internship", "work", "job", "where has she worked", "employment", "worked", "intern", "career"],
        "response": "💼 <b>Professional Experience (3 Roles):</b><br><br>1️⃣ <b>WordPress Developer, AI Automation & Cybersecurity Specialist — Center of Information Technology (CIT)</b> (Jul 2026 – Present)<br>📍 Pakistan (Director: <b>Sir Amar Jaffri</b> & Supervisor: <b>Sir Aman Ijaz</b>)<br>• Official website development (<a href=\"https://www.cit.com.pk\" target=\"_blank\">www.cit.com.pk</a>), custom plugins, database & backend, geological mapping, AI chatbot, n8n/NIT workflow automation, cybersecurity<br><br>2️⃣ <b>AI Intern (CMIT Internship Program 2025–26) — BuiltinSoft</b> (8 Jan 2026 – 8 Jun 2026)<br>📍 Rahim Yar Khan, Onsite<br>• Quran Pronunciation Checker website, ML/DL model selection & training, n8n workflow automation, Django REST APIs<br><br>3️⃣ <b>Cybersecurity & Audio Forensics Intern — National Cyber Crime & Forensics Lab (Air University)</b> (Jul – Sep 2025)<br>📍 Islamabad, Hybrid<br>• Audio Forensics deepfake tampering website, diarization, temporal inconsistencies, metadata analysis, sentiment analysis"
    },

    # ── ALL PROJECTS ──
    {
        "patterns": ["projects", "what projects", "show projects", "all projects", "portfolio projects", "what has she built", "her work", "list projects", "project list"],
        "response": "🚀 <b>Eman's Key Projects:</b><br><br>1. 🌐 <b>CIT Official Platform & Ecosystem</b> — WordPress, Custom Plugins, Database/Backend, Geo-location, n8n, AI Chatbot (Live at www.cit.com.pk)<br>2. 🏥 <b>Healthcare Security via Blockchain & AI</b> — FYP, live at healerplus.live<br>3. 🎵 <b>Audio Forensics & Tampering Detection</b> — Whisper + DistilBERT + Diarization<br>4. 🎣 <b>AI Phishing Detection Platform</b> — NLP + WHOIS/DNS<br>5. 🚦 <b>AI Traffic Sign Recognition</b> — CNN, 98.2% accuracy<br>6. 📖 <b>Quran Pronunciation Checker (AI Recitation)</b> — Wav2Vec2 + Whisper<br>7. 📊 <b>Exploratory Data Analysis & ML Benchmarking</b> — DBSCAN, Pandas<br>8. 🐱 <b>Image Classifier (Cat vs Dog)</b> — CNN + Streamlit<br>9. 🔑 <b>PassAudit</b> — Password & breach auditor<br><br>Ask me about any specific project for details!"
    },

    # ── SPECIFIC PROJECTS ──
    {
        "patterns": ["healthcare", "blockchain", "healerplus", "fyp", "final year", "ethereum", "ipfs", "hospital", "healer"],
        "response": "🏥 <b>Healthcare Security via Blockchain & AI</b> (Final Year Project)<br>🌐 Live at: <b>healerplus.live</b><br><br>Built a secure hospital management system using:<br>• <b>Ethereum smart contracts</b> for role-based access control<br>• <b>IPFS</b> for decentralized data storage<br>• <b>Random Forest AI</b> for anomaly detection & breach prevention<br>• React.js frontend + Flask backend + Web3.js<br><br>📄 Also accepted as a research paper at <b>ICACNC 2025</b>! ⛓️"
    },
    {
        "patterns": ["audio forensics", "tampering", "distilbert", "audio detection", "audio tamper", "audio forensic"],
        "response": "🎵 <b>Audio Forensics & Tampering Detection</b><br><br>A web platform that detects digital tampering in audio files using:<br>• <b>OpenAI Whisper</b> for audio transcription<br>• <b>DistilBERT</b> for NLP-based authenticity analysis<br>• Waveform visualization for tamper region detection<br>• Python + JavaScript stack"
    },
    {
        "patterns": ["phishing", "phishing detection", "threat analysis", "url detection", "phishing platform"],
        "response": "🎣 <b>AI-Based Phishing Detection Platform</b><br><br>Full-stack platform detecting phishing URLs, emails & web content in real-time:<br>• <b>TF-IDF + NLP</b> for text analysis<br>• <b>WHOIS & DNS lookups</b> for domain verification<br>• Risk scoring dashboard with confidence scores<br>• Python + Flask<br>📂 GitHub: EmanFatima045/AI-Based-Phisphing-Detection-Threat-Analysis-Platform"
    },
    {
        "patterns": ["traffic sign", "traffic recognition", "gtsrb", "road sign", "traffic sign recognition"],
        "response": "🚦 <b>AI Traffic Sign Recognition</b><br><br>Deep learning model trained on the <b>German Traffic Sign (GTSRB) dataset</b>:<br>• Achieves <b>98.2% confidence</b> accuracy<br>• Uses CNN + computer vision<br>• Stack: Python, TensorFlow, OpenCV, Scikit-learn"
    },
    {
        "patterns": ["recitation", "quran", "wav2vec", "pronunciation", "recitation evaluator", "islamic", "tajweed"],
        "response": "📖 <b>AI Recitation Evaluator</b> (In Progress)<br><br>Records audio to evaluate Quranic recitation accuracy:<br>• <b>Phoneme-level analysis</b><br>• <b>OpenAI Whisper</b> for speech recognition<br>• <b>Wav2Vec2</b> for phoneme alignment<br>• FastAPI backend + PyTorch"
    },
    {
        "patterns": ["cat dog", "cat vs dog", "image classifier", "streamlit", "cnn classifier"],
        "response": "🐱🐶 <b>Image Classifier with Confidence Logic</b><br><br>CNN-based classifier for Cat vs Dog categorization:<br>• <b>85%+ confidence threshold</b> logic<br>• Per-class confidence scores<br>• <b>Streamlit UI</b> for easy interaction<br>• Stack: TensorFlow, CNN, OpenCV, Streamlit"
    },
    {
        "patterns": ["passaudit", "password audit", "password strength", "password checker", "breach"],
        "response": "🔑 <b>PassAudit</b><br><br>Comprehensive password security auditor:<br>• Checks password <b>strength & policy requirements</b><br>• Verifies against <b>known breached password databases</b><br>• Enforces complexity rules (length, special chars, case)<br>• Stack: Python, Cryptography"
    },
    {
        "patterns": ["portx", "port scanner", "port scan", "network scanner", "open ports", "network recon"],
        "response": "🔌 <b>PortX — Network Port Scanner</b><br><br>Lightweight multi-threaded port scanner:<br>• Scans all <b>65535 ports</b> rapidly<br>• <b>100 concurrent threads</b> for speed<br>• Discovers open ports, live hosts, active services<br>• Stack: Python, Socket, Threading"
    },
    {
        "patterns": ["metasniff", "metadata", "exif", "gps coordinates", "osint tool", "file metadata"],
        "response": "🔍 <b>MetaSniff — Metadata Forensics</b><br><br>Extracts hidden metadata from documents & images:<br>• <b>EXIF data</b> (camera model, settings, ISO)<br>• <b>GPS coordinates</b> (location tracking)<br>• Author & organization info<br>• File creation/modification timelines<br>• Stack: Python, ExifRead — great for OSINT investigations"
    },
    {
        "patterns": ["stegohawk", "steganography", "lsb", "hidden message", "stego", "steganographic"],
        "response": "🦅 <b>StegoHawk — LSB Steganography Tool</b><br><br>Conceals encrypted data inside images invisibly:<br>• <b>AES-256 encryption</b> before embedding<br>• <b>LSB (Least Significant Bit)</b> steganography<br>• Supports text & file payloads<br>• Stack: Python, Steganography, OpenCV"
    },
    {
        "patterns": ["hashguard", "hashing", "sha256", "md5", "checksum", "hash", "sha512", "sha-256"],
        "response": "🔒 <b>HashGuard — Cryptographic Hash Utility</b><br><br>Multi-algorithm hashing for data integrity:<br>• Supports <b>SHA-256, MD5, SHA-512</b><br>• Checksum generation & verification<br>• Ensures data integrity across file transfers<br>• Stack: Python, Cryptography"
    },
    {
        "patterns": ["memstrings", "memory forensics", "memory dump", "malware analysis", "ram forensics"],
        "response": "🧠 <b>MemStrings — Memory Forensics Scanner</b><br><br>Scans memory dumps for suspicious patterns:<br>• Extracts readable <b>ASCII and Unicode strings</b><br>• Flags <b>credentials, C2 URLs, suspicious executables</b><br>• Identifies malware indicators (cmd.exe, .bat scripts, registry keys)<br>• Stack: Python, Memory Analysis, Malware Analysis"
    },

    # ── SKILLS ──
    {
        "patterns": ["skills", "technical skills", "what can she do", "technologies", "tools", "what does she know", "her skills", "all skills", "tech stack"],
        "response": "🛠️ <b>Eman's Technical Skills:</b><br><br>💻 <b>Languages:</b> Python, C++, Java, JavaScript, HTML/CSS<br><br>🔐 <b>Security Tools:</b> Wireshark, Nmap, OWASP ZAP, Autopsy, FTK Imager, WinHex, Belkasoft<br><br>🤖 <b>AI/ML:</b> TensorFlow, Scikit-learn, PyTorch, OpenCV, HuggingFace, Whisper, NLTK<br><br>🌐 <b>Web/Backend:</b> Flask, Django, FastAPI, React.js, Web3.js, REST APIs<br><br>⛓️ <b>Blockchain:</b> Ethereum, IPFS, Smart Contracts, Solidity<br><br>☁️ <b>Cloud:</b> Microsoft Azure"
    },
    {
        "patterns": ["python", "programming language", "coding language", "c++", "java", "javascript"],
        "response": "💻 <b>Programming Languages:</b><br>Eman is proficient in <b>Python, C++, Java, JavaScript, and HTML/CSS</b>. Python is her primary language — she uses it for cybersecurity tools, ML models, web backends (Flask, Django, FastAPI), and forensics scripts."
    },
    {
        "patterns": ["machine learning", "ml", "artificial intelligence", "deep learning", "tensorflow", "pytorch", "scikit", "neural network", "cnn", "model"],
        "response": "🤖 <b>AI/ML Skills:</b><br>Eman works with <b>TensorFlow, PyTorch, Scikit-learn, OpenCV, HuggingFace, Whisper, NLTK</b>.<br><br>Models she has built: CNN, Random Forest, KNN, K-Means, SVM, Decision Trees, DistilBERT, Wav2Vec2."
    },
    {
        "patterns": ["wireshark", "nmap", "autopsy", "ftk", "forensic tools", "security tools", "owasp", "winhex", "belkasoft"],
        "response": "🔐 <b>Security & Forensics Tools:</b><br>• <b>Network:</b> Wireshark, Nmap, OWASP ZAP<br>• <b>Forensics:</b> Autopsy, FTK Imager, WinHex, Belkasoft<br>She's proficient in the full forensic investigation toolkit used by professionals in digital forensics labs."
    },
    {
        "patterns": ["web development", "flask", "django", "fastapi", "react", "backend", "frontend", "web dev", "api"],
        "response": "🌐 <b>Web & Backend Skills:</b><br>Flask, Django, FastAPI, React.js, Web3.js, REST APIs.<br><br>She integrates these into security projects — e.g., her phishing detection platform uses Flask, her blockchain healthcare system uses React.js + Web3.js."
    },
    {
        "patterns": ["blockchain", "ethereum", "solidity", "smart contract", "ipfs", "web3", "decentralized"],
        "response": "⛓️ <b>Blockchain Skills:</b><br>• <b>Ethereum</b> smart contracts for access control<br>• <b>Solidity</b> for contract development<br>• <b>IPFS</b> for decentralized storage<br>• <b>Web3.js</b> for frontend integration<br>Applied in her FYP: healerplus.live"
    },
    {
        "patterns": ["azure", "cloud", "microsoft", "cloud computing"],
        "response": "☁️ Eman is currently completing her <b>Microsoft Azure Cloud Services</b> certification. She applies cloud knowledge to deploy and host her security applications and web projects."
    },

    # ── RESEARCH & PUBLICATIONS ──
    {
        "patterns": ["research", "publication", "paper", "journal", "icacnc", "jair", "published", "academic paper", "research paper", "ieee paper"],
        "response": "📚 <b>Research & Publications:</b><br><br>1️⃣ ✅ <b>Accepted — ICACNC 2025</b><br>\"Enhancing Healthcare Security with Blockchain and AI-Based Anomaly Detection\"<br>Authors: Eman Fatima, Rao Sharif Mansoob, Muhammad Shoaib, Iftikhar Rasheed, Umar Fayyaz<br>Proposed secure hospital data system using Ethereum blockchain, IPFS, and AI anomaly detection.<br><br>2️⃣ 🔄 <b>Under Review — JAIR</b><br>\"Blockchain and AI in Healthcare Security: A Comprehensive Review of Anomaly Detection Approaches\"<br>Comprehensive literature review examining blockchain-AI security, including Estonia's eHealth infrastructure. 🔬"
    },

    # ── CERTIFICATIONS ──
    {
        "patterns": ["certification", "certifications", "certificate", "google", "coursera", "azure certified", "certified", "credentials"],
        "response": "🏆 <b>Certifications (6+):</b><br><br>1. 🛡️ Foundations of Cybersecurity — Google/Coursera (Aug 2024)<br>2. 🔐 Manage Security Risks — Google/Coursera<br>3. 🌐 Connect & Protect: Network Security — Google/Coursera<br>4. 🤖 Generative AI & Deep Learning Boot Camp (May 2025)<br>5. ☁️ Microsoft Azure Cloud Services — In Progress<br>6. 🧠 AI for Beginners — Microsoft"
    },

    # ── LEADERSHIP ──
    {
        "patterns": ["leadership", "ieee", "team leader", "host", "event", "extracurricular", "activities", "volunteer", "organizing"],
        "response": "🌟 <b>Leadership & Activities:</b><br>• <b>Team Leader</b> — University Lab (Image & Video Processing)<br>• <b>IEEE Cybersecurity Event Host</b> — organized and hosted cybersecurity awareness events<br>• <b>Departmental Function Host / MC</b> — hosted university events<br>• Active in research collaboration and academic competitions"
    },

    # ── CONTACT ──
    {
        "patterns": ["contact", "email", "reach", "connect", "how to contact", "get in touch", "linkedin", "github", "reach out"],
        "response": "📬 <b>Contact Eman Fatima:</b><br><br>📧 <b>Email:</b> emanfatima60860@gmail.com<br>💼 <b>LinkedIn:</b> linkedin.com/in/eman-fatima-512a01246/<br>💻 <b>GitHub:</b> github.com/EmanFatima045<br>📍 <b>Location:</b> Rahim Yar Khan, Pakistan<br><br>✅ She is <b>actively looking</b> for cybersecurity roles, research collaborations, and internships!"
    },
    {
        "patterns": ["hire", "available", "looking for job", "open to work", "opportunities", "recruit", "hiring", "vacancy"],
        "response": "✅ <b>Yes! Eman is actively open to opportunities!</b><br><br>She's looking for:<br>• 🔐 Cybersecurity analyst/engineer roles<br>• 🤖 AI/ML security positions<br>• 🔬 Research collaborations<br>• 💼 Internships in security or AI<br><br>Contact her: <b>emanfatima60860@gmail.com</b> 📧"
    },

    # ── LOCATION ──
    {
        "patterns": ["location", "where is she", "where does she live", "city", "pakistan", "rahim yar khan", "where from"],
        "response": "📍 Eman is based in <b>Rahim Yar Khan, Punjab, Pakistan</b>. She is open to remote work opportunities and relocation."
    },

    # ── CV / RESUME ──
    {
        "patterns": ["cv", "resume", "download", "download cv", "curriculum vitae", "resume download"],
        "response": "📄 You can download Eman's CV directly from her portfolio! Click the <b>'Download CV'</b> button in the hero section or the contact section to get the PDF. 📥"
    },

    # ── CGPA ──
    {
        "patterns": ["cgpa", "gpa", "grade", "marks", "3.50", "score", "result", "percentage"],
        "response": "📊 Eman maintains a <b>CGPA of 3.50</b> in her BS Cybersecurity & Digital Forensics program at The Islamia University of Bahawalpur — strong academic performance alongside 12+ practical projects and 2 research publications."
    },

    # ── WHISPER ──
    {
        "patterns": ["whisper", "openai whisper", "speech recognition", "transcription"],
        "response": "🎙️ Eman uses <b>OpenAI Whisper</b> in two projects:<br>1. <b>Audio Forensics</b> — transcribes audio for tampering analysis<br>2. <b>AI Recitation Evaluator</b> — speech recognition for Quranic recitation assessment<br>She combines Whisper with DistilBERT and Wav2Vec2 for advanced NLP analysis."
    },

    # ── IEEE ──
    {
        "patterns": ["ieee", "event host", "cybersecurity event", "community"],
        "response": "🌐 Eman has served as an <b>IEEE Cybersecurity Event Host</b>, organizing and hosting cybersecurity awareness events at her university. She is also a <b>Team Leader</b> in the university's Image & Video Processing lab."
    },
]


def build_chat_reply(message: str) -> str:
    text = message.lower().strip()

    filler_words = [
        "please", "can you", "could you", "would you", "tell me", "what is",
        "what are", "how is", "how are", "i want to know", "do you know",
        "i'd like to know", "give me", "show me", "explain", "describe"
    ]
    cleaned = text
    for f in filler_words:
        cleaned = cleaned.replace(f, " ")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    best_match = None
    best_score = 0

    for entry in KNOWLEDGE_BASE:
        score = 0
        for pattern in entry["patterns"]:
            if pattern in text:
                score = max(score, len(pattern) * 3)
            elif pattern in cleaned:
                score = max(score, len(pattern) * 2)
            else:
                pattern_words = set(pattern.split())
                text_words = set(re.findall(r'\b\w+\b', text))
                overlap = len(pattern_words & text_words)
                if overlap > 0 and overlap >= len(pattern_words) * 0.6:
                    score = max(score, overlap * len(pattern))

        if score > best_score:
            best_score = score
            best_match = entry

    if best_match and best_score > 0:
        return best_match["response"]

    return (
        "🤔 I'm not sure about that specific question, but I can help with:<br><br>"
        "🎓 <b>Education</b> — degree, CGPA, university<br>"
        "💼 <b>Experience</b> — BuiltinSoft & National Cyber Crime Lab internships<br>"
        "🚀 <b>Projects</b> — 12+ security & AI projects<br>"
        "📚 <b>Research</b> — accepted paper at ICACNC 2025, under review at JAIR<br>"
        "🛠️ <b>Skills</b> — Python, cybersecurity tools, AI/ML, blockchain<br>"
        "🏆 <b>Certifications</b> — Google, Microsoft, and more<br>"
        "📬 <b>Contact</b> — emanfatima60860@gmail.com<br><br>"
        "Try: <i>'What projects has she built?'</i> or <i>'Tell me about her experience'</i>"
    )


# ─────────────────────────────────────────────
#  EMAIL
# ─────────────────────────────────────────────

def build_contact_mailto(data: Dict[str, Any]) -> str:
    recipient = os.getenv("CONTACT_TO", "emanfatima60860@gmail.com").strip()
    subject = urllib.parse.quote(f"Portfolio Contact: {data.get('subject', 'Hello') or 'Hello'}")
    body = urllib.parse.quote(
        f"Name: {data.get('name', '') or ''}\n"
        f"Email: {data.get('email', '') or ''}\n\n"
        f"Message:\n{data.get('message', '') or ''}"
    )
    return f"mailto:{recipient}?subject={subject}&body={body}"


def send_contact_email(data: Dict[str, Any], log_path: Path | None = None) -> Tuple[bool, str]:
    """
    Sends contact form email via Gmail SMTP.

    Required .env variables:
        SMTP_USER = your Gmail address  (e.g. emanfatima60860@gmail.com)
        SMTP_PASS = Gmail App Password  (16-char, spaces optional — they get stripped)
                    Generate: Google Account → Security → 2-Step Verification → App Passwords
        CONTACT_TO = emanfatima60860@gmail.com  (already default)
    """
    if log_path is None:
        log_path = ROOT / "contact_messages.jsonl"

    payload = {
        "name":      data.get("name", "").strip(),
        "email":     data.get("email", "").strip(),
        "subject":   data.get("subject", "").strip(),
        "message":   data.get("message", "").strip(),
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

    # Always log locally as backup
    try:
        with log_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except Exception:
        pass

    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com").strip()
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "").strip()

    # ── FIX 1: Strip ALL spaces from App Password ──
    # Gmail App Passwords are sometimes copied with spaces ("yqkv lrda bxqb plqn")
    # but the .env value may also have trailing whitespace — strip everything.
    smtp_pass = "".join(os.getenv("SMTP_PASS", "").split())

    recipient = os.getenv("CONTACT_TO", "emanfatima60860@gmail.com").strip()

    if not smtp_user or not smtp_pass:
        return False, (
            "⚠️ Email server not configured yet. Your message has been saved locally. "
            "Please contact Eman directly at <b>emanfatima60860@gmail.com</b>."
        )

    try:
        msg = EmailMessage()
        msg["Subject"] = f"Portfolio Contact: {payload['subject'] or 'New Message'}"
        msg["From"]    = smtp_user
        msg["To"]      = recipient
        msg["Reply-To"] = payload["email"] or smtp_user

        msg.set_content(
            f"═══════════════════════════════\n"
            f"  NEW MESSAGE FROM PORTFOLIO\n"
            f"═══════════════════════════════\n\n"
            f"Name    : {payload['name']}\n"
            f"Email   : {payload['email']}\n"
            f"Subject : {payload['subject']}\n"
            f"Time    : {payload['timestamp']}\n\n"
            f"Message:\n{'─'*40}\n{payload['message']}\n{'─'*40}\n\n"
            f"Reply directly to this email to respond."
        )

        # ── FIX 2: Don't use 'with smtplib.SMTP' context manager ──
        # smtplib.SMTP.__exit__ calls quit(), which can raise if the connection
        # is already in a broken state and masks the real auth error.
        # Managing the connection manually gives cleaner error reporting.
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
        try:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()                        # re-identify after STARTTLS
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        finally:
            try:
                server.quit()
            except Exception:
                pass  # Already disconnected — safe to ignore

        return True, "✅ Message sent successfully! Eman will get back to you soon."

    except smtplib.SMTPAuthenticationError:
        return False, (
            "❌ Gmail authentication failed. Make sure you are using a Gmail "
            "<b>App Password</b> (not your regular Gmail password). "
            "Generate one at: Google Account → Security → 2-Step Verification → App Passwords. "
            "Your message was saved locally."
        )
    except smtplib.SMTPException as e:
        return False, (
            f"❌ Email error: {str(e)}. Your message was saved. "
            f"Contact Eman at <b>emanfatima60860@gmail.com</b>."
        )
    except Exception as e:
        return False, (
            f"❌ Unexpected error: {str(e)}. Your message was saved. "
            f"Contact Eman at <b>emanfatima60860@gmail.com</b>."
        )


# ─────────────────────────────────────────────
#  ROUTES
# ─────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
def read_root():
    index_path = ROOT / "index.html"
    if not index_path.exists():
        raise HTTPException(status_code=404, detail="index.html not found")
    return index_path.read_text(encoding="utf-8")


@app.post("/chat")
async def chat_endpoint(payload: ChatRequest):
    if not payload.message or not payload.message.strip():
        return JSONResponse({"reply": "Please ask me something about Eman! 😊"})
    reply = build_chat_reply(payload.message.strip())
    return JSONResponse({"reply": reply})


@app.post("/contact")
async def contact_endpoint(payload: ContactRequest):
    if not payload.name.strip() or not payload.email.strip() or not payload.message.strip():
        raise HTTPException(status_code=400, detail="Name, email, and message are required.")

    success, message = send_contact_email(payload.model_dump())
    return JSONResponse({
        "success": success,
        "message": message
    })


@app.get("/health")
def health():
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = "".join(os.getenv("SMTP_PASS", "").split())  # strip spaces for length check
    return JSONResponse({
        "status": "ok",
        "smtp_configured": bool(smtp_user and smtp_pass),
        "smtp_user": smtp_user[:6] + "****" if smtp_user else "NOT SET",
        "smtp_pass_length": len(smtp_pass),           # should be 16 for Gmail App Password
        "contact_to": os.getenv("CONTACT_TO", "emanfatima60860@gmail.com")
    })