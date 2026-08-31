/* =====================================================
   EMMU CHATBOT — Portfolio AI Assistant for Eman Fatima
   ===================================================== */

(function () {
  'use strict';

  /* ── Knowledge Base ── */
  var KB = {
    identity: {
      name: 'Eman Fatima',
      title: 'Artificial Intelligence Engineer & Cybersecurity Analyst',
      university: 'The Islamia University of Bahawalpur',
      degree: 'BS Cybersecurity and Digital Forensics',
      cgpa: '3.50',
      location: 'Lahore, Pakistan (originally from Rahim Yar Khan)',
      currentJob: 'Center of Information Technology (CIT)',
      currentDirector: 'Sir Amar Jaffri',
      currentSupervisor: 'Sir Aman Ijaz',
      available: 'Mon - Fri, 9 AM - 6 PM',
      openTo: 'Artificial Intelligence Engineering, Cybersecurity, AI Automation, and Digital Forensics roles'
    },
    contact: {
      email: 'emanfatima60860@gmail.com',
      email2: 'emanarif056@gmail.com',
      phone: '0303 8775831',
      linkedin: 'https://www.linkedin.com/in/eman-fatima-512a01246/',
      github: 'https://github.com/EmanFatima045'
    },
    stats: {
      projects: '12+',
      cgpa: '3.50',
      publications: '2',
      certifications: '6'
    },
    skills: {
      programming: ['Python', 'C++', 'Java', 'JavaScript', 'HTML/CSS'],
      cybersecurity: ['Threat Detection', 'Threat Modeling', 'Risk Assessment', 'Incident Response', 'Network Security', 'OSINT', 'Ethical Hacking'],
      forensics: ['Audio Forensics', 'Diarization', 'Temporal Inconsistencies', 'Metadata Analysis', 'Autopsy', 'FTK Imager', 'RAM Capturer', 'X-Ways', 'WinHex', 'Belkasoft'],
      securityTools: ['Wireshark', 'Nmap', 'OWASP ZAP', 'Threat Modeling Tool', 'Linux'],
      aiml: ['TensorFlow', 'Keras', 'Scikit-learn', 'PyTorch', 'OpenCV', 'HuggingFace', 'OpenAI Whisper', 'Wav2Vec2', 'Deep Learning & ML Model Selection', 'Markov Chains'],
      webCloud: ['WordPress', 'Custom Plugins', 'Database & Backend (MySQL/PHP)', 'Geo-Location Mapping', 'n8n Workflow Automation', 'Flask', 'Django', 'FastAPI', 'React.js', 'Ethereum', 'IPFS', 'Microsoft Azure', 'Streamlit']
    },
    certifications: [
      { name: 'Foundations of Cybersecurity', issuer: 'Google - Coursera', date: 'Aug 2024' },
      { name: 'Play it Safe: Manage Security Risks', issuer: 'Google - Coursera', date: '' },
      { name: 'Connect and Protect: Network Security Fundamentals', issuer: 'Google - Coursera', date: '' },
      { name: 'Generative AI & Deep Learning', issuer: 'Boot Camp', date: 'May 2025' },
      { name: 'Microsoft Azure Cloud Services', issuer: 'Microsoft', date: 'In Progress' },
      { name: 'AI for Beginners', issuer: 'Microsoft - Online', date: '' }
    ],
    projects: [
      {
        name: 'Center of Information Technology (CIT) Official Platform',
        category: 'Enterprise Web, Custom Plugins & AI - Live',
        desc: 'Official website of Center of Information Technology (www.cit.com.pk) built under Director Sir Amar Jaffri and Supervisor Sir Aman Ijaz. Making the complete website, developing custom WordPress plugins, interactive geo-location / geological mapping features, database design & backend systems, custom AI chatbot integration, and n8n workflow automation.',
        tech: ['WordPress', 'Custom Plugins', 'Database & Backend', 'Geo-Location', 'n8n Automation', 'AI Chatbot', 'Cybersecurity'],
        link: 'https://www.cit.com.pk'
      },
      {
        name: 'Healthcare Security with Blockchain & AI',
        category: 'Final Year Project - Live',
        desc: 'Secure hospital management system using Ethereum smart contracts for role-based access control and IPFS for decentralized storage, with a Random Forest model flagging suspicious login patterns. Live at healerplus.live',
        tech: ['Python', 'Ethereum', 'IPFS', 'React.js', 'Random Forest', 'Flask'],
        link: 'https://github.com/EmanFatima045'
      },
      {
        name: 'Audio Forensics & Tampering Detection',
        category: 'Digital Forensics - AI',
        desc: 'Web-based audio forensics platform that analyzes uploaded audio to detect synthetic or tampered deepfakes using speaker diarization, temporal inconsistencies, timestamps, and deep metadata analysis to generate full forensic audit reports.',
        tech: ['Python', 'Whisper', 'DistilBERT', 'Diarization', 'Acoustic Metadata', 'JavaScript'],
        link: 'https://github.com/EmanFatima045'
      },
      {
        name: 'AI Based Phishing Detection & Threat Analysis',
        category: 'Cybersecurity - Machine Learning',
        desc: 'Full-stack platform detecting phishing across URLs, emails and web content in real time using NLP, WHOIS and DNS lookups, outputting confidence-scored risk classifications.',
        tech: ['Flask', 'Scikit-learn', 'TF-IDF', 'WHOIS', 'Random Forest', 'Pandas'],
        link: 'https://github.com/EmanFatima045/AI-Based-Phisphing-Detection-Threat-Analysis-Platform'
      },
      {
        name: 'AI Based Traffic Sign Recognition',
        category: 'Computer Vision - Deep Learning',
        desc: 'Deep learning model trained on the German Traffic Sign dataset to detect and classify road signs using computer vision techniques with 98%+ accuracy.',
        tech: ['OpenCV', 'TensorFlow', 'Scikit-learn'],
        link: 'https://github.com/EmanFatima045'
      },
      {
        name: 'Quran Pronunciation Checker (AI Recitation Evaluator)',
        category: 'AI - NLP - Completed at CMIT',
        desc: 'AI-powered Quran recitation evaluation system that takes user audio, compares phoneme-level pronunciation against renowned Quranic reciters, and pinpoints exact mispronounced words with accuracy scores.',
        tech: ['Python', 'OpenAI Whisper', 'Wav2Vec2', 'HuggingFace', 'PyTorch', 'FastAPI', 'Streamlit'],
        link: 'https://github.com/EmanFatima045'
      },
      {
        name: 'Exploratory Data Analysis & ML Benchmarking',
        category: 'Data Science - EDA',
        desc: 'End-to-end data science project covering missing value handling, outlier detection and correlation analysis, then benchmarking six ML algorithms including DBSCAN for spatial anomaly detection.',
        tech: ['Pandas', 'NumPy', 'DBSCAN', 'Seaborn', 'Matplotlib', 'Scikit-learn'],
        link: 'https://github.com/EmanFatima045'
      },
      {
        name: 'Image Classifier - Cat vs Dog with Confidence Threshold',
        category: 'Deep Learning - CNN',
        desc: 'CNN-based classifier for Cat vs Dog categorization with a confidence threshold to flag unknown animals and per-class confidence scores in a Streamlit interface.',
        tech: ['TensorFlow', 'Keras', 'CNN', 'OpenCV', 'Streamlit', 'NumPy'],
        link: 'https://github.com/EmanFatima045'
      },
      {
        name: 'PassAudit',
        category: 'Security Auditing',
        desc: 'Audits password strength, enforces policy requirements and checks credentials against known breached password databases in real time.',
        tech: ['Python', 'Cryptography'],
        link: 'https://github.com/EmanFatima045'
      }
    ],
    experience: [
      {
        role: 'WordPress Developer, AI Automation & Cybersecurity Specialist',
        company: 'Center of Information Technology (CIT)',
        location: 'Pakistan (Director: Sir Amar Jaffri & Supervisor: Sir Aman Ijaz)',
        period: 'Jul 2026 - Present (Selected: 20 Jul 2026)',
        bullets: [
          'Architecting, developing, and managing the complete official website for Center of Information Technology (www.cit.com.pk), including About Us, Events, Directory Links, Contact, and Geo-location / geological mapping features',
          'Engineered bespoke custom WordPress plugins, designed and optimized the database architecture & backend systems, and built scalable API workflows',
          'Developed custom AI chatbot integrations and designed n8n automated workflow pipelines (NIT / workflow automation)',
          'Overseeing website cybersecurity, system hardening, and access controls under Director Sir Amar Jaffri and Supervisor Sir Aman Ijaz'
        ]
      },
      {
        role: 'Artificial Intelligence Intern (CMIT Internship Program 2025–26)',
        company: 'BuiltinSoft',
        location: 'Rahim Yar Khan, Onsite',
        period: '8 Jan 2026 - 8 Jun 2026',
        bullets: [
          'Developed the Quran Pronunciation Checker website (AI Recitation Evaluator) that captures user audio and pinpoints exact mispronounced words with phoneme-level accuracy feedback',
          'Trained, benchmarked, and analyzed multiple Machine Learning and Deep Learning models (KNN, K-Means, Random Forest, SVM, Decision Trees, CNNs), evaluating data characteristics to determine optimal model architectures and training pipelines',
          'Built automated workflow pipelines and data processing routines using n8n and automation tools (NIT and workflow automation)',
          'Implemented conversational chatbot logic with Markov Chain algorithms and developed Django REST APIs for e-commerce platforms'
        ]
      },
      {
        role: 'Cybersecurity & Audio Forensics Intern',
        company: 'National Cyber Crime and Forensics Lab (NCCFL / Air University)',
        location: 'Islamabad, Hybrid',
        period: 'Jul 2025 - Sep 2025',
        bullets: [
          'Developed an end-to-end Audio Forensics & Tampering Detection website that analyzes audio authenticity to identify fake/tampered recordings and delivers comprehensive forensic reports to users',
          'Applied advanced forensic techniques including speaker diarization, temporal inconsistencies detection, timestamp verification, and acoustic metadata analysis',
          'Performed sentiment analysis, acoustic feature modeling, and gender classification in an active national cybersecurity research environment',
          'Prepared detailed technical reports and presented analytical findings with clarity and precision to research teams'
        ]
      }
    ],
    publications: [
      {
        title: 'Enhancing Healthcare Security with Blockchain and AI Based Anomaly Detection',
        status: 'Accepted - ICACNC 2025',
        authors: 'Eman Fatima, Rao Sharif Mansoob, Muhammad Shoaib, Iftikhar Rasheed, Umar Fayyaz',
        summary: 'Proposed a secure hospital data system using Ethereum blockchain, IPFS and AI anomaly detection. Smart contracts enabled secure logins; Random Forest achieved high accuracy detecting suspicious patterns.'
      },
      {
        title: 'Blockchain and AI in Healthcare Security: A Comprehensive Review of Anomaly Detection Approaches',
        status: 'Under Review - JAIR',
        authors: 'Eman Fatima et al.',
        summary: 'Literature review examining blockchain and AI-driven anomaly detection in healthcare, covering security, privacy and real-world deployments such as Estonia\'s eHealth infrastructure.'
      }
    ],
    leadership: [
      { title: 'Team Leader, University Lab Group', desc: 'Led a five-member team on image and video processing projects, coordinating task delegation, progress tracking and technical delivery.' },
      { title: 'Event Host, Departmental Farewell Functions', desc: 'Managed logistics and hosted formal university events, building strong communication and coordination skills.' },
      { title: 'Technical Host, IEEE Cybersecurity Events', desc: 'Moderated expert panels, facilitated Q&A discussions and presented technical cybersecurity content to diverse audiences.' }
    ],
    about: 'Eman Fatima is an <b>Artificial Intelligence Engineer and Cybersecurity Analyst</b>, with a BS in Cybersecurity and Digital Forensics from The Islamia University of Bahawalpur (CGPA 3.50). She is currently working at the <b>Center of Information Technology (CIT)</b> under Director <b>Sir Amar Jaffri</b> and Supervisor <b>Sir Aman Ijaz</b>, handling WordPress development (www.cit.com.pk), custom plugins, geological/geo-location mapping, database & backend systems, AI chatbot integrations, n8n/NIT workflow automations, and cybersecurity. She has previous experience as an AI Intern at <b>CMIT (BuiltinSoft)</b> developing the Quran Pronunciation Checker and training ML/DL models, and as a Cybersecurity & Audio Forensics Intern at <b>National Cyber Crime & Forensics Lab (Air University)</b> building deepfake audio detection systems. She is also a published researcher at ICACNC 2025.'
  };

  /* ── Intent Matching ── */
  function matchIntent(msg) {
    var m = msg.toLowerCase().trim();
    if (/^(hi|hello|hey|hii+|yo|sup|howdy|greet|good\s*(morning|evening|afternoon|day)|salam|assalam)/i.test(m)) return 'greeting';
    if (/\b(cit|center of information technology|amar|jaffri|jafri|aman|ijaz|cit\.com\.pk|custom plugin|plugins|geological|geolocation|geo-location|database|backend)\b/i.test(m)) return 'cit';
    if (/\b(who (is|are) (eman|she|you)|about eman|introduce|about yourself|tell me about|who is iman|about iman)\b/i.test(m)) return 'about';
    if (/\b(name|full name|called|iman fatima|eman fatima)\b/i.test(m)) return 'name';
    if (/\b(cgpa|grade|gpa|marks|score|university|degree|education|study|graduated|bahawalpur)\b/i.test(m)) return 'education';
    if (/\b(cmit|builtinsoft|quran|pronunciation|recitation|tajweed|mispronounced|deep learning model)\b/i.test(m)) return 'cmit';
    if (/\b(ncc|nccfl|air university|national cyber|audio forensic|diarization|temporal inconsistenc|timestamp|tamper|metadata analysis|fake audio)\b/i.test(m)) return 'ncc';
    if (/\b(automation|n8n|workflow|nit|workflows)\b/i.test(m)) return 'automation';
    if (/\b(email|mail|contact|reach|phone|number|linkedin|github|location|where|available|hire|hiring|opportunity|open to)\b/i.test(m)) return 'contact';
    if (/\b(skill|skills|language|tool|framework|know|expertise|technolog|profici|capable|ability|python|java|javascript|tensorflow|keras|pytorch|scikit|opencv|whisper|flask|django|react|ethereum|azure|wireshark|nmap|autopsy|forensic tool)\b/i.test(m)) return 'skills';
    if (/\b(project|projects|work|built|build|develop|healthcare|blockchain|phishing|traffic|audio|forensic|classifier|cat|dog|passaudit|recitation|eda|data analysis|anomaly|healerplus)\b/i.test(m)) return 'projects';
    if (/\b(experience|intern|job|company|role|career|work history|where has she worked|current job)\b/i.test(m)) return 'experience';
    if (/\b(research|paper|publication|published|icacnc|jair|journal|review)\b/i.test(m)) return 'publications';
    if (/\b(cert|certification|course|coursera|google|microsoft|azure|training)\b/i.test(m)) return 'certifications';
    if (/\b(lead|leader|ieee|event|host|extracurr|club|team)\b/i.test(m)) return 'leadership';
    if (/\b(cv|resume|download|pdf)\b/i.test(m)) return 'cv';
    if (/\b(help|what can you|what do you|options|menu|topics)\b/i.test(m)) return 'help';
    if (/\b(thank|thanks|thx|ty|appreciate|great|awesome|cool|nice|perfect|got it|okay|ok)\b/i.test(m)) return 'thanks';
    if (/\b(bye|goodbye|see you|later|ciao|exit|close)\b/i.test(m)) return 'bye';

    // Fuzzy keyword matches
    if (/project/i.test(m)) return 'projects';
    if (/experience|intern|work/i.test(m)) return 'experience';
    if (/skill|tech/i.test(m)) return 'skills';
    if (/contact|email|phone/i.test(m)) return 'contact';

    return 'unknown';
  }

  /* ── Response Generator ── */
  function getResponse(intent, msg) {
    switch (intent) {
      case 'greeting':
        return 'Hey there! <b>I\'m Emmu</b>, Eman Fatima\'s personal AI assistant! Eman Fatima is an <b>Artificial Intelligence Engineer and Cybersecurity Analyst</b>. I know all about her work at CIT (under Director Sir Amar Jaffri & Supervisor Sir Aman Ijaz), her AI internships, deepfake audio forensics, Quran pronunciation checker, publications, and skills. What would you like to know?<br><br><em>Try asking: "Tell me about her CIT project", "What are her projects?", or "Tell me about her experience"</em>';

      case 'about':
        return '<b>About Eman Fatima</b><br><br>' + KB.about + '<br><br>She is actively open to <b>' + KB.identity.openTo + '</b>.';

      case 'name':
        return 'Her name is <b>Eman Fatima</b> (also referred to as Iman Fatima) — an <b>Artificial Intelligence Engineer & Cybersecurity Analyst</b> from Pakistan.';

      case 'cit':
        return '💼 <b>Center of Information Technology (CIT) · Pakistan</b><br>' +
          '📅 <b>Period:</b> Jul 2026 – Present (Selected: 20 July 2026)<br>' +
          '👤 <b>Director:</b> Sir Amar Jaffri<br>' +
          '👤 <b>Supervisor:</b> Sir Aman Ijaz<br>' +
          '🌐 <b>Website:</b> <a href="https://www.cit.com.pk" target="_blank">www.cit.com.pk</a><br><br>' +
          '<b>What Eman is building at CIT:</b><br>' +
          '• <b>Official Website:</b> Making the complete WordPress portal (<a href="https://www.cit.com.pk" target="_blank">www.cit.com.pk</a>) including About Us, Events, Directory Links, and Contact.<br>' +
          '• <b>Custom Plugins:</b> Engineered bespoke WordPress plugins tailored specifically for CIT portal needs.<br>' +
          '• <b>Geo-Location Mapping:</b> Developed interactive geological/geo-location features for mapped center directory listings.<br>' +
          '• <b>Database & Backend:</b> Architected backend logic and database structures for scalable performance.<br>' +
          '• <b>AI Chatbots & Automation:</b> Built custom AI chatbots and implemented <b>n8n / NIT automated workflows</b>.<br>' +
          '• <b>Cybersecurity:</b> Manages website security posture, vulnerability prevention, and system hardening under Director <b>Sir Amar Jaffri</b> and Supervisor <b>Sir Aman Ijaz</b>.';

      case 'cmit':
        return '🤖 <b>CMIT Internship Program (BuiltinSoft)</b><br>' +
          '📅 <b>Period:</b> 8 Jan 2026 – 8 Jun 2026 · Rahim Yar Khan, Onsite<br><br>' +
          '<b>Key Highlights:</b><br>' +
          '• Built the <b>Quran Pronunciation Checker</b> website (AI Recitation Evaluator) that captures user audio and detects exact mispronounced words with phoneme-level accuracy feedback.<br>' +
          '• Trained and evaluated numerous <b>Machine Learning & Deep Learning models</b> (KNN, K-Means, Random Forest, SVM, Decision Trees, CNNs), analyzing dataset behaviors to choose optimal architectures and data training pipelines.<br>' +
          '• Built automated workflow pipelines using <b>n8n / NIT automation</b>.<br>' +
          '• Implemented conversational AI algorithms, Markov Chains, and production Django REST APIs.';
      case 'ncc':
        return '🛡️ <b>Cybersecurity & Audio Forensics Intern — NCCFL / Air University</b><br>' +
          '📅 <b>Period:</b> Jul 2025 – Sep 2025 · Islamabad (Hybrid)<br><br>' +
          '<b>Key Highlights:</b><br>' +
          '• Built an end-to-end <b>Audio Forensics & Tampering Detection</b> website that analyzes audio to verify if it is authentic or fake/tampered and generates full forensic audit reports.<br>' +
          '• Implemented forensic techniques: <b>speaker diarization, temporal inconsistencies detection, timestamp verification, and deep metadata analysis</b>.<br>' +
          '• Conducted sentiment analysis, acoustic feature modeling, and gender classification in an active national cybersecurity research lab.<br>' +
          '• Prepared detailed technical reports and presented findings to cybersecurity researchers.';
      case 'automation':
        return '⚡ <b>Workflow & AI Automation (n8n / NIT)</b><br><br>' +
          'Eman has extensive experience building automated pipelines and workflows:<br>' +
          '• <b>At CIT:</b> Automating WordPress data flows, notifications, and custom plugin integrations via n8n.<br>' +
          '• <b>At CMIT:</b> Built automated data pipelines and model preprocessing routines.<br>' +
          '• Expertise in connecting APIs, webhooks, databases, and AI models into seamless automated workflows.';
      case 'education':
        return '🎓 <b>Education</b><br><br><b>Degree:</b> BS Cybersecurity & Digital Forensics<br><b>University:</b> The Islamia University of Bahawalpur<br><b>CGPA:</b> 3.50 / 4.0<br><br>Her coursework spans Artificial Intelligence, network security, digital forensics, machine learning, cryptography, and blockchain security.';
      case 'contact':
        return '<b>Contact Eman</b><br><br>Email: <a href="mailto:emanfatima60860@gmail.com">emanfatima60860@gmail.com</a><br>Phone: 0303 8775831<br>LinkedIn: <a href="' + KB.contact.linkedin + '" target="_blank">eman-fatima-512a01246</a><br>GitHub: <a href="' + KB.contact.github + '" target="_blank">EmanFatima045</a><br>Location: Lahore, Pakistan<br>Available: Mon - Fri, 9 AM - 6 PM<br><br>She is <b>open to opportunities</b> in AI Engineering, Cybersecurity, AI Automation & Digital Forensics!';
      case 'skills': {
        var s = KB.skills;
        return '<b>Eman\'s Technical Skills</b><br><br>' +
          '<b>AI & Deep Learning:</b> ' + s.aiml.join(', ') + '<br>' +
          '<b>Cybersecurity & Risk:</b> ' + s.cybersecurity.join(', ') + '<br>' +
          '<b>Digital Forensics:</b> ' + s.forensics.join(', ') + '<br>' +
          '<b>Web, CMS & Automation:</b> ' + s.webCloud.join(', ') + '<br>' +
          '<b>Security Tools:</b> ' + s.securityTools.join(', ') + '<br>' +
          '<b>Programming:</b> ' + s.programming.join(', ');
      }
      case 'projects': {
        var q = msg.toLowerCase();
        var found = null;
        for (var i = 0; i < KB.projects.length; i++) {
          var p = KB.projects[i];
          var words = p.name.toLowerCase().split(' ');
          for (var j = 0; j < words.length; j++) {
            if (words[j].length > 4 && q.includes(words[j])) { found = p; break; }
          }
          if (found) break;
        }
        if (found) {
          return '<b>' + found.name + '</b><br><em>' + found.category + '</em><br><br>' + found.desc + '<br><br><b>Tech:</b> ' + found.tech.join(', ') + '<br><a href="' + found.link + '" target="_blank">View on GitHub</a>';
        }
        var html = '<b>Eman\'s Projects (' + KB.projects.length + ' total)</b><br><br>';
        KB.projects.forEach(function(proj, idx) {
          html += '<b>' + (idx + 1) + '. ' + proj.name + '</b><br><em>' + proj.category + '</em><br>' + proj.desc.substring(0, 100) + '...<br><br>';
        });
        html += 'Ask me about any specific project for details!';
        return html;
      }
      case 'experience': {
        var html = '<b>Professional Experience</b><br><br>';
        KB.experience.forEach(function(exp) {
          html += '<b>' + exp.role + '</b><br>' + exp.company + ' - ' + exp.location + '<br>' + exp.period + '<br>';
          exp.bullets.forEach(function(b) { html += '• ' + b + '<br>'; });
          html += '<br>';
        });
        return html;
      }
      case 'publications': {
        var html = '<b>Research Publications</b><br><br>';
        KB.publications.forEach(function(pub) {
          html += '<b>' + pub.title + '</b><br><em>' + pub.status + '</em><br>' + pub.authors + '<br>' + pub.summary + '<br><br>';
        });
        return html;
      }
      case 'certifications': {
        var html = '<b>Certifications & Training</b><br><br>';
        KB.certifications.forEach(function(c) {
          html += '<b>' + c.name + '</b> — ' + c.issuer + (c.date ? ' (' + c.date + ')' : '') + '<br>';
        });
        return html;
      }
      case 'leadership': {
        var html = '<b>Leadership & Extracurricular</b><br><br>';
        KB.leadership.forEach(function(l) {
          html += '<b>' + l.title + '</b><br>' + l.desc + '<br><br>';
        });
        return html;
      }
      case 'cv':
        return 'You can view and download Eman\'s updated ATS-compliant CV directly from the portfolio!<br><br>Click the <b>"Download Resume"</b> button at the top, or <a href="resume.html" target="_blank">click here to open & save CV as PDF</a>.';
      case 'help':
        return '<b>Here is what I can tell you!</b><br><br>About Eman — background & bio<br>Education — university, CGPA, degree<br>Skills — all technical skills & tools<br>Projects — all 8 projects with details<br>Experience — internships & work history<br>Publications — research papers<br>Certifications — all 6 certifications<br>Leadership — IEEE, team lead roles<br>Contact — email, phone, LinkedIn<br><br>Just type naturally — I\'ll figure it out!';
      case 'thanks':
        return 'You\'re welcome! Is there anything else you\'d like to know about Eman? I\'m always here to help!';
      case 'bye':
        return 'Goodbye! It was lovely chatting with you. Feel free to come back anytime. Have a wonderful day!';
      default:
        return 'Hmm, I\'m not sure about that! I specialize in everything about <b>Eman Fatima\'s portfolio</b>. Try asking about her skills, projects, experience, or how to contact her. Type <em>"help"</em> to see all topics!';
    }
  }

  var QUICK_REPLIES = [
    { label: 'About Eman', msg: 'Tell me about Eman' },
    { label: 'CIT Project & Role', msg: 'Tell me about her CIT project and role' },
    { label: 'Skills', msg: 'What are her skills?' },
    { label: 'All Projects', msg: 'Show me her projects' },
    { label: 'Experience', msg: 'Tell me about her experience' },
    { label: 'Research', msg: 'What research has she published?' },
    { label: 'Contact', msg: 'How to contact Eman?' }
  ];

  function buildChatbot() {
    var style = document.createElement('style');
    style.textContent = [
      '#emmu-fab{position:fixed;bottom:32px;left:32px;z-index:10000;width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#8b1e2d 0%,#c0392b 100%);border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 28px rgba(139,30,45,0.55);animation:emmuPulse 2.8s ease-in-out infinite;transition:transform 0.3s,box-shadow 0.3s;outline:none;padding:0;}',
      '#emmu-fab:hover{transform:scale(1.13) translateY(-3px);box-shadow:0 16px 40px rgba(139,30,45,0.65);}',
      '@keyframes emmuPulse{0%,100%{box-shadow:0 8px 28px rgba(139,30,45,0.55),0 0 0 0 rgba(139,30,45,0.35);}50%{box-shadow:0 8px 28px rgba(139,30,45,0.55),0 0 0 14px rgba(139,30,45,0);}}',
      '#emmu-fab-inner{display:flex;flex-direction:column;align-items:center;gap:1px;}',
      '#emmu-fab-label{font-size:7.5px;font-weight:800;color:#fff;letter-spacing:0.06em;text-transform:uppercase;line-height:1;margin-top:1px;}',
      '#emmu-notif{position:absolute;top:1px;right:1px;width:15px;height:15px;background:#ff4757;border-radius:50%;border:2px solid #fff;animation:emmubounce 1s ease-in-out infinite;}',
      '@keyframes emmubounce{0%,100%{transform:scale(1);}50%{transform:scale(1.3);}}',
      '#emmu-tooltip{position:fixed;bottom:108px;left:32px;background:linear-gradient(135deg,#8b1e2d,#c0392b);color:#fff;padding:10px 16px;border-radius:14px 14px 14px 4px;font-size:13px;font-weight:600;white-space:nowrap;box-shadow:0 8px 24px rgba(139,30,45,0.35);z-index:9999;pointer-events:none;animation:emmuSlideIn 0.4s cubic-bezier(0.16,1,0.3,1) forwards;}',
      '@keyframes emmuSlideIn{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:translateY(0);}}',
      '#emmu-window{position:fixed;bottom:112px;left:32px;width:374px;max-height:590px;background:#fff;border:1px solid #f0dde0;border-radius:22px;box-shadow:0 24px 70px rgba(139,30,45,0.2),0 4px 16px rgba(0,0,0,0.08);display:flex;flex-direction:column;z-index:9999;overflow:hidden;transform-origin:bottom left;animation:emmuWinIn 0.45s cubic-bezier(0.16,1,0.3,1) forwards;}',
      '@keyframes emmuWinIn{from{opacity:0;transform:scale(0.7) translateY(30px);}to{opacity:1;transform:scale(1) translateY(0);}}',
      '#emmu-window.closing{animation:emmuWinOut 0.28s cubic-bezier(0.4,0,1,1) forwards;}',
      '@keyframes emmuWinOut{from{opacity:1;transform:scale(1) translateY(0);}to{opacity:0;transform:scale(0.75) translateY(20px);}}',
      '#emmu-header{background:linear-gradient(135deg,#8b1e2d 0%,#c0392b 100%);padding:14px 16px 12px;display:flex;align-items:center;gap:11px;flex-shrink:0;}',
      '#emmu-avatar-wrap{width:46px;height:46px;border-radius:50%;background:rgba(255,255,255,0.15);border:2px solid rgba(255,255,255,0.4);display:flex;align-items:center;justify-content:center;flex-shrink:0;animation:emmuBob 3s ease-in-out infinite;}',
      '@keyframes emmuBob{0%,100%{transform:translateY(0);}50%{transform:translateY(-4px);}}',
      '.emmu-hinfo{flex:1;min-width:0;}.emmu-hname{font-size:14.5px;font-weight:700;color:#fff;line-height:1.2;}',
      '.emmu-hstatus{display:flex;align-items:center;gap:5px;font-size:10.5px;color:rgba(255,255,255,0.82);margin-top:2px;}',
      '.emmu-hdot{width:7px;height:7px;background:#5dde8f;border-radius:50%;animation:emmustat 2s ease-in-out infinite;flex-shrink:0;}',
      '@keyframes emmustat{0%,100%{opacity:1;}50%{opacity:0.4;}}',
      '#emmu-close{width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);color:#fff;font-size:14px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:background 0.2s;flex-shrink:0;line-height:1;}',
      '#emmu-close:hover{background:rgba(255,255,255,0.28);}',
      '#emmu-msgs{flex:1;overflow-y:auto;padding:14px 13px;display:flex;flex-direction:column;gap:11px;scroll-behavior:smooth;}',
      '#emmu-msgs::-webkit-scrollbar{width:4px;}#emmu-msgs::-webkit-scrollbar-thumb{background:#f0dde0;border-radius:4px;}',
      '.emmu-msg{display:flex;gap:8px;align-items:flex-end;animation:emmumsgIn 0.35s cubic-bezier(0.16,1,0.3,1) forwards;}',
      '@keyframes emmumsgIn{from{opacity:0;transform:translateY(12px);}to{opacity:1;transform:translateY(0);}}',
      '.emmu-msg.user{flex-direction:row-reverse;}',
      '.emmu-msg-icon{width:30px;height:30px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#8b1e2d,#c0392b);font-size:16px;}',
      '.emmu-msg.user .emmu-msg-icon{background:#fbf1f2;border:1px solid #f0dde0;font-size:13px;}',
      '.emmu-bubble{max-width:80%;padding:10px 13px;border-radius:18px 18px 18px 4px;font-size:13px;line-height:1.65;color:#25080f;background:#fdf5f6;border:1px solid #f0dde0;word-break:break-word;}',
      '.emmu-bubble a{color:#c0392b;text-decoration:none;font-weight:600;border-bottom:1px solid rgba(192,57,43,0.4);}',
      '.emmu-bubble a:hover{border-color:#c0392b;}',
      '.emmu-msg.user .emmu-bubble{background:linear-gradient(135deg,#8b1e2d,#c0392b);color:#fff;border-color:transparent;border-radius:18px 18px 4px 18px;}',
      '.emmu-typing .emmu-bubble{display:flex;gap:5px;align-items:center;padding:12px 16px;}',
      '.emmu-dot{width:7px;height:7px;border-radius:50%;background:#c0392b;opacity:0.5;animation:emmuTyping 1.2s ease-in-out infinite;}',
      '.emmu-dot:nth-child(2){animation-delay:0.2s;}.emmu-dot:nth-child(3){animation-delay:0.4s;}',
      '@keyframes emmuTyping{0%,100%{opacity:0.25;transform:translateY(0);}50%{opacity:1;transform:translateY(-5px);}}',
      '#emmu-quick{padding:8px 12px 10px;display:flex;flex-wrap:wrap;gap:6px;border-top:1px solid #f0dde0;background:#fff;flex-shrink:0;}',
      '.emmu-qbtn{padding:5px 11px;border-radius:100px;background:#fdf5f6;border:1px solid #e3c3ca;color:#c0392b;font-size:11px;font-weight:700;cursor:pointer;transition:all 0.22s cubic-bezier(0.34,1.56,0.64,1);white-space:nowrap;}',
      '.emmu-qbtn:hover{background:linear-gradient(135deg,#8b1e2d,#c0392b);color:#fff;border-color:transparent;transform:scale(1.06) translateY(-2px);}',
      '#emmu-input-area{padding:9px 13px 13px;display:flex;gap:8px;align-items:center;border-top:1px solid #f0dde0;background:#fff;flex-shrink:0;}',
      '#emmu-input{flex:1;padding:10px 14px;border:1.5px solid #f0dde0;border-radius:100px;background:#fbf4f5;color:#25080f;font-size:13px;outline:none;transition:border-color 0.2s,box-shadow 0.2s;}',
      '#emmu-input:focus{border-color:#c0392b;box-shadow:0 0 0 3px rgba(139,30,45,0.1);}',
      '#emmu-input::placeholder{color:#a2818a;}',
      '#emmu-send{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#8b1e2d,#c0392b);border:none;color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:transform 0.25s cubic-bezier(0.34,1.56,0.64,1),box-shadow 0.25s;box-shadow:0 4px 14px rgba(139,30,45,0.35);flex-shrink:0;}',
      '#emmu-send:hover{transform:scale(1.12) rotate(8deg);box-shadow:0 8px 22px rgba(139,30,45,0.5);}',
      '@media(max-width:480px){#emmu-window{width:calc(100vw - 32px);left:16px;bottom:100px;}#emmu-fab{bottom:20px;left:20px;}#emmu-tooltip{left:20px;bottom:96px;}}'
    ].join('');
    document.head.appendChild(style);

    var robotSVG = '<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" width="28" height="28">' +
      '<rect x="10" y="14" width="28" height="22" rx="7" fill="white" fill-opacity="0.95"/>' +
      '<rect x="21.5" y="5" width="5" height="9" rx="2.5" fill="white" fill-opacity="0.9"/>' +
      '<circle cx="24" cy="4.5" r="3.5" fill="white" fill-opacity="0.9"/>' +
      '<circle cx="24" cy="4.5" r="1.8" fill="#ff6b8a"/>' +
      '<circle cx="17.5" cy="24" r="4" fill="#c0392b"/>' +
      '<circle cx="30.5" cy="24" r="4" fill="#c0392b"/>' +
      '<circle cx="18.2" cy="23.2" r="1.3" fill="white"/>' +
      '<circle cx="31.2" cy="23.2" r="1.3" fill="white"/>' +
      '<rect x="16" y="31" width="16" height="3.5" rx="1.75" fill="#8b1e2d" fill-opacity="0.7"/>' +
      '<rect x="17.5" y="31" width="3" height="3.5" rx="0.75" fill="white" fill-opacity="0.45"/>' +
      '<rect x="22.5" y="31" width="3" height="3.5" rx="0.75" fill="white" fill-opacity="0.45"/>' +
      '<rect x="27.5" y="31" width="3" height="3.5" rx="0.75" fill="white" fill-opacity="0.45"/>' +
      '<rect x="6" y="20" width="5" height="9" rx="2.5" fill="white" fill-opacity="0.8"/>' +
      '<rect x="37" y="20" width="5" height="9" rx="2.5" fill="white" fill-opacity="0.8"/>' +
      '</svg>';

    var fab = document.createElement('button');
    fab.id = 'emmu-fab';
    fab.title = 'Chat with Emmu';
    fab.setAttribute('aria-label', 'Open Emmu Chatbot');
    fab.innerHTML = '<div id="emmu-fab-inner">' + robotSVG + '<div id="emmu-fab-label">Emmu</div></div><span id="emmu-notif"></span>';
    document.body.appendChild(fab);

    var tooltip = document.createElement('div');
    tooltip.id = 'emmu-tooltip';
    tooltip.textContent = 'Hi! I\'m Emmu — Ask me anything about Eman!';
    document.body.appendChild(tooltip);
    setTimeout(function() { if (tooltip.parentNode) tooltip.remove(); }, 5000);

    var win = document.createElement('div');
    win.id = 'emmu-window';
    win.style.display = 'none';
    win.innerHTML =
      '<div id="emmu-header">' +
        '<div id="emmu-avatar-wrap">' + robotSVG + '</div>' +
        '<div class="emmu-hinfo">' +
          '<div class="emmu-hname">Emmu \u2014 Eman\'s AI Assistant</div>' +
          '<div class="emmu-hstatus"><span class="emmu-hdot"></span>Online \u00b7 Ask me anything!</div>' +
        '</div>' +
        '<button id="emmu-close" title="Close">&#10005;</button>' +
      '</div>' +
      '<div id="emmu-msgs"></div>' +
      '<div id="emmu-quick"></div>' +
      '<div id="emmu-input-area">' +
        '<input id="emmu-input" type="text" placeholder="Ask about skills, projects, contact\u2026" autocomplete="off" maxlength="250"/>' +
        '<button id="emmu-send" title="Send">' +
          '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>' +
        '</button>' +
      '</div>';
    document.body.appendChild(win);

    var msgs = win.querySelector('#emmu-msgs');
    var input = win.querySelector('#emmu-input');
    var quick = win.querySelector('#emmu-quick');
    var notif = fab.querySelector('#emmu-notif');
    var isOpen = false;

    function renderQuickReplies() {
      quick.innerHTML = '';
      QUICK_REPLIES.forEach(function(qr) {
        var btn = document.createElement('button');
        btn.className = 'emmu-qbtn';
        btn.textContent = qr.label;
        btn.addEventListener('click', function() { sendMessage(qr.msg); });
        quick.appendChild(btn);
      });
    }
    renderQuickReplies();

    function appendMsg(text, isUser) {
      var row = document.createElement('div');
      row.className = 'emmu-msg' + (isUser ? ' user' : '');
      var iconEl = document.createElement('div');
      iconEl.className = 'emmu-msg-icon';
      if (isUser) {
        iconEl.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="#c0392b"><path d="M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z"/></svg>';
      } else {
        iconEl.textContent = '\uD83E\uDD16';
      }
      var bubble = document.createElement('div');
      bubble.className = 'emmu-bubble';
      bubble.innerHTML = text;
      row.appendChild(iconEl);
      row.appendChild(bubble);
      msgs.appendChild(row);
      msgs.scrollTop = msgs.scrollHeight;
    }

    function showTyping() {
      var row = document.createElement('div');
      row.className = 'emmu-msg emmu-typing';
      row.innerHTML = '<div class="emmu-msg-icon">\uD83E\uDD16</div><div class="emmu-bubble"><div class="emmu-dot"></div><div class="emmu-dot"></div><div class="emmu-dot"></div></div>';
      msgs.appendChild(row);
      msgs.scrollTop = msgs.scrollHeight;
      return row;
    }

    function sendMessage(text) {
      var trimmed = (text || '').trim();
      if (!trimmed) return;
      appendMsg(trimmed, true);
      if (input.value.trim() === trimmed) input.value = '';
      var typingRow = showTyping();
      var delay = 650 + Math.random() * 550;
      setTimeout(function() {
        typingRow.remove();
        var intent = matchIntent(trimmed);
        var resp = getResponse(intent, trimmed);
        appendMsg(resp, false);
      }, delay);
    }

    function openChat() {
      isOpen = true;
      win.style.display = 'flex';
      win.classList.remove('closing');
      if (notif && notif.parentNode) notif.remove();
      if (tooltip.parentNode) tooltip.remove();
      if (msgs.children.length === 0) {
        setTimeout(function() {
          appendMsg('Hey there! I\'m <b>Emmu</b> \u2014 Eman\'s AI portfolio assistant! \uD83E\uDD16\u2728<br><br>I know <em>everything</em> about Eman Fatima \u2014 her skills, projects, research, experience and more. What would you like to know?', false);
        }, 300);
      }
      setTimeout(function() { input.focus(); }, 120);
    }

    function closeChat() {
      win.classList.add('closing');
      setTimeout(function() {
        win.style.display = 'none';
        win.classList.remove('closing');
      }, 280);
      isOpen = false;
    }

    fab.addEventListener('click', function() { isOpen ? closeChat() : openChat(); });
    win.querySelector('#emmu-close').addEventListener('click', closeChat);
    win.querySelector('#emmu-send').addEventListener('click', function() { sendMessage(input.value); });
    input.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(input.value); }
    });
    document.addEventListener('click', function(e) {
      if (isOpen && !win.contains(e.target) && e.target !== fab && !fab.contains(e.target)) {
        closeChat();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildChatbot);
  } else {
    buildChatbot();
  }

})();
