"""
Generate ATS-Friendly PDF Resume for Eman Fatima
Includes updated CIT (Director Sir Amar Jaffri, Supervisor Sir Aman Ijaz), CMIT, and NCCFL experience.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def build_pdf(filename="assets/Cv_Eman_Fatima.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    name_style = ParagraphStyle(
        'Name',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#111111')
    )
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#333333')
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#111111'),
        spaceBefore=8,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=12.2,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#222222')
    )
    
    role_style = ParagraphStyle(
        'Role',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=colors.HexColor('#111111')
    )
    
    org_style = ParagraphStyle(
        'Org',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#333333')
    )
    
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=12,
        alignment=TA_RIGHT,
        textColor=colors.HexColor('#444444')
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.8,
        leftIndent=12,
        firstLineIndent=-8,
        spaceBefore=1.5,
        spaceAfter=1.5,
        textColor=colors.HexColor('#222222')
    )
    
    story = []
    
    # ── HEADER ──
    story.append(Paragraph("EMAN FATIMA", name_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("03038775831 | emanfatima60860@gmail.com | <a href='https://www.linkedin.com/in/eman-fatima-512a01246/' color='#0044cc'><u>LinkedIn Profile</u></a> | <a href='https://github.com/EmanFatima045' color='#0044cc'><u>GitHub: EmanFatima045</u></a> | Lahore, Pakistan", contact_style))
    story.append(Spacer(1, 6))
    
    # ── PROFESSIONAL SUMMARY ──
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#222222'), spaceAfter=5))
    story.append(Paragraph("<b>Artificial Intelligence Engineer & Cybersecurity Analyst</b> with a BS in Cybersecurity & Digital Forensics (CGPA 3.50) from The Islamia University of Bahawalpur. Hands-on experience architecting full-stack web platforms, developing custom WordPress plugins, implementing n8n workflow automations, training/evaluating deep learning models, and conducting audio forensics deepfake tampering detection. Published researcher (ICACNC 2025) with proven leadership in technical event hosting and IEEE programs. Seeking to contribute technical engineering and security expertise to impactful enterprise initiatives.", body_style))
    story.append(Spacer(1, 6))
    
    # ── EDUCATION ──
    story.append(Paragraph("EDUCATION", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#222222'), spaceAfter=5))
    
    edu_table = Table([
        [Paragraph("<b>BS in Cybersecurity and Digital Forensics — CGPA: 3.50</b>", role_style), Paragraph("2021 – 2025", date_style)],
        [Paragraph("The Islamia University of Bahawalpur", org_style), Paragraph("Bahawalpur, Pakistan", date_style)]
    ], colWidths=[380, 160])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(edu_table)
    story.append(Paragraph("• <b>Relevant Coursework:</b> Artificial Intelligence, Machine Learning, Network Security, Cyber Forensic Analysis, Cryptography, Database Systems, Image & Video Processing.", bullet_style))
    story.append(Spacer(1, 6))
    
    # ── PROFESSIONAL EXPERIENCE ──
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#222222'), spaceAfter=5))
    
    # 1. CIT
    cit_table = Table([
        [Paragraph("<b>WordPress Developer, AI Automation & Cybersecurity Specialist</b>", role_style), Paragraph("Jul 2026 – Present", date_style)],
        [Paragraph("Center of Information Technology (CIT) — <i>(Director: Sir Amar Jaffri | Supervisor: Sir Aman Ijaz)</i>", org_style), Paragraph("Pakistan | Onsite", date_style)]
    ], colWidths=[390, 150])
    cit_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(cit_table)
    story.append(Paragraph("• <b>Full-Stack Web Development:</b> Architecting, developing, and maintaining the official enterprise portal for Center of Information Technology (<a href='https://www.cit.com.pk' color='#0044cc'><u>www.cit.com.pk</u></a>), including About Us, Events, Directory Links, Contact, and Geo-location / geological mapping modules.", bullet_style))
    story.append(Paragraph("• <b>Custom Plugin & Backend Engineering:</b> Engineered tailored custom WordPress plugins and structured scalable MySQL database schemas and backend API pipelines to support dynamic portal operations.", bullet_style))
    story.append(Paragraph("• <b>AI & Workflow Automation:</b> Integrated custom AI chatbot solutions and deployed n8n & NIT automated workflow pipelines to automate data synchronization, notifications, and operational reporting.", bullet_style))
    story.append(Paragraph("• <b>Cybersecurity Hardening:</b> Enforcing website security posture, role-based access controls (RBAC), and vulnerability mitigations under the leadership of Director Sir Amar Jaffri and Supervisor Sir Aman Ijaz.", bullet_style))
    story.append(Spacer(1, 4))
    
    # 2. CMIT
    cmit_table = Table([
        [Paragraph("<b>Artificial Intelligence Intern (CMIT Internship Program 2025–26)</b>", role_style), Paragraph("8 Jan 2026 – 8 Jun 2026", date_style)],
        [Paragraph("BuiltinSoft", org_style), Paragraph("Rahim Yar Khan | Onsite", date_style)]
    ], colWidths=[390, 150])
    cmit_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(cmit_table)
    story.append(Paragraph("• Developed the <b>Quran Pronunciation Checker</b> website (AI Recitation Evaluator) utilizing OpenAI Whisper and Wav2Vec2 for phoneme-level acoustic alignment to identify mispronounced words with precision feedback.", bullet_style))
    story.append(Paragraph("• Trained, analyzed, and benchmarked multiple ML/DL models (KNN, K-Means, Random Forest, SVM, Decision Trees, CNNs), matching data distributions to optimal model architectures and training pipelines.", bullet_style))
    story.append(Paragraph("• Built automated workflow pipelines using n8n and automation tools (NIT and workflow automation) to streamline dataset preprocessing and model inference workflows.", bullet_style))
    story.append(Paragraph("• Implemented conversational AI features with Markov Chain algorithms and developed production Django REST APIs for e-commerce systems.", bullet_style))
    story.append(Spacer(1, 4))
    
    # 3. NCCFL
    ncc_table = Table([
        [Paragraph("<b>Cybersecurity & Audio Forensics Intern</b>", role_style), Paragraph("Jul 2025 – Sep 2025", date_style)],
        [Paragraph("National Cyber Crime and Forensics Lab (NCCFL / Air University)", org_style), Paragraph("Islamabad | Hybrid", date_style)]
    ], colWidths=[390, 150])
    ncc_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(ncc_table)
    story.append(Paragraph("• Built an end-to-end <b>Audio Forensics & Tampering Detection</b> platform to analyze audio authenticity, detect synthetic/tampered deepfakes, and generate comprehensive forensic audit reports.", bullet_style))
    story.append(Paragraph("• Applied advanced forensic techniques: <b>speaker diarization, temporal inconsistencies detection, timestamp verification, and acoustic metadata analysis</b>.", bullet_style))
    story.append(Paragraph("• Performed sentiment analysis, acoustic feature modeling, and gender classification in an active national cybersecurity research lab; prepared and presented technical audit reports.", bullet_style))
    story.append(Spacer(1, 6))
    
    # ── PROJECTS ──
    story.append(Paragraph("KEY PROJECTS", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#222222'), spaceAfter=5))
    
    story.append(Paragraph("<b>Center of Information Technology Official Portal & Ecosystem</b> | <i>WordPress, Custom Plugins, MySQL, Geo-Location, n8n, AI Chatbot</i>", role_style))
    story.append(Paragraph("• Enterprise website with custom plugins, interactive geo-location directory mapping, automated n8n workflows, and integrated AI conversational chatbot. Live at: <a href='https://www.cit.com.pk' color='#0044cc'><u>www.cit.com.pk</u></a>", bullet_style))
    story.append(Spacer(1, 2))
    
    story.append(Paragraph("<b>Healthcare Security with Blockchain & AI Anomaly Detection (Final Year Project)</b> | <i>Python, Ethereum, IPFS, React.js, Random Forest, Flask</i>", role_style))
    story.append(Paragraph("• Built decentralized hospital management system using Ethereum smart contracts for role-based access control and IPFS storage, coupled with Random Forest AI anomaly detection to prevent unauthorized logins. Live at: <a href='https://healerplus.live' color='#0044cc'><u>healerplus.live</u></a>", bullet_style))
    story.append(Spacer(1, 2))
    
    story.append(Paragraph("<b>Audio Forensics & Digital Tampering Detection</b> | <i>Python, Whisper, DistilBERT, PyAudio, JavaScript</i>", role_style))
    story.append(Paragraph("• Deepfake audio detection platform combining Whisper transcription, DistilBERT NLP authenticity verification, and acoustic metadata/diarization forensics.", bullet_style))
    story.append(Spacer(1, 2))
    
    story.append(Paragraph("<b>AI-Based Phishing Detection & Threat Analysis Platform</b> | <i>Python, Flask, Scikit-learn, TF-IDF/NLP, WHOIS/DNS</i>", role_style))
    story.append(Paragraph("• Real-time phishing detection system analyzing URLs, email content, and domain metadata to classify threat confidence scores (Safe / Suspicious / Phishing).", bullet_style))
    story.append(Spacer(1, 2))
    
    story.append(Paragraph("<b>AI-Based Traffic Sign Recognition System</b> | <i>Python, OpenCV, TensorFlow, Scikit-learn</i>", role_style))
    story.append(Paragraph("• CNN-based computer vision model trained on GTSRB dataset achieving 98.2% classification accuracy across diverse road sign classes.", bullet_style))
    story.append(Spacer(1, 2))
    
    story.append(Paragraph("<b>PassAudit — Password Policy & Breach Auditor</b> | <i>Python, Cryptography, Hashing Algorithms</i>", role_style))
    story.append(Paragraph("• Real-time credential auditor checking password complexity policies and hashing against known compromised breach databases.", bullet_style))
    story.append(Spacer(1, 6))
    
    # ── TECHNICAL SKILLS ──
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#222222'), spaceAfter=5))
    
    skills_data = [
        [Paragraph("<b>Programming Languages:</b>", role_style), Paragraph("Python, C++, Java, JavaScript, PHP, HTML5/CSS3, SQL", body_style)],
        [Paragraph("<b>AI & Deep Learning:</b>", role_style), Paragraph("TensorFlow, Keras, PyTorch, Scikit-learn, OpenCV, HuggingFace, OpenAI Whisper, Wav2Vec2, CNNs, Random Forest", body_style)],
        [Paragraph("<b>Automation & Web CMS:</b>", role_style), Paragraph("n8n Workflow Automation, NIT Automation, WordPress, Custom Plugin Development, Django, Flask, FastAPI, React.js", body_style)],
        [Paragraph("<b>Cybersecurity & Forensics:</b>", role_style), Paragraph("Threat Detection, Audio Forensics, Speaker Diarization, Metadata Analysis, Wireshark, Nmap, OWASP ZAP, Autopsy, FTK Imager", body_style)],
        [Paragraph("<b>Database & Cloud:</b>", role_style), Paragraph("MySQL, PostgreSQL, Database Architecture, Ethereum Smart Contracts, IPFS, Microsoft Azure Cloud", body_style)],
    ]
    skills_table = Table(skills_data, colWidths=[160, 380])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 6))
    
    # ── PUBLICATIONS & CERTIFICATIONS ──
    story.append(Paragraph("PUBLICATIONS & CERTIFICATIONS", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#222222'), spaceAfter=5))
    story.append(Paragraph("• <b>Accepted Research Paper (ICACNC 2025):</b> <i>Enhancing Healthcare Security with Blockchain and AI Based Anomaly Detection</i> — Eman Fatima, Rao Sharif Mansoob, Muhammad Shoaib, Iftikhar Rasheed, Umar Fayyaz.", bullet_style))
    story.append(Paragraph("• <b>Certifications:</b> Foundations of Cybersecurity (Google), Manage Security Risks (Google), Generative AI & Deep Learning (Boot Camp, May 2025), Microsoft Azure Cloud Services (In Progress), AI for Beginners (Microsoft).", bullet_style))
    story.append(Spacer(1, 6))
    
    # ── LEADERSHIP ──
    story.append(Paragraph("LEADERSHIP & EXTRACURRICULAR", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#222222'), spaceAfter=5))
    story.append(Paragraph("• <b>Technical Host — IEEE Cybersecurity Events:</b> Moderated panels, led Q&A sessions, and presented cybersecurity insights to audience of 200+.", bullet_style))
    story.append(Paragraph("• <b>Team Leader — University Lab Group:</b> Led a 5-member team on computer vision and security projects, coordinating technical delivery.", bullet_style))
    
    doc.build(story)
    print(f"Generated ATS Resume PDF at: {filename}")

if __name__ == "__main__":
    build_pdf("assets/Cv_Eman_Fatima.pdf")
    if os.path.exists("portfolio-emanfatima"):
        build_pdf("portfolio-emanfatima/Cv_Eman_Fatima.pdf")
