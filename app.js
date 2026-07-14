const translations = {
    en: {
        landingTitle: "Kutubxona AI",
        landingSubtitle: "Enter password to access the digital learning assistant.",
        passwordPlaceholder: "Password",
        wrongPassword: "Incorrect password",
        enterBtn: "Enter",
        newConversation: "New Session",
        examPrep: "Exam Prep",
        ieltsSection: "IELTS Materials",
        satSection: "SAT Resources",
        apSection: "AP Courses",
        ceqSection: "Cambridge CEQ",
        langLearning: "Language Learning",
        englishBooks: "English Textbooks",
        russianBooks: "Russian Literature",
        settings: "Settings",
        libraryAssistant: "Educational Assistant",
        online: "Online",
        searchCatalog: "Search Books",
        libraryAccount: "Student Profile",
        welcomeMsg1: "Welcome! I am <strong>Kutubxona AI</strong>, your educational assistant.",
        welcomeMsg2: "I can help you in various areas of life.",
        askPlaceholder: "Ask about an exam, book, or topic...",
        footerNote: "Kutubxona AI is an educational assistant and its advice should be supplemented with official exam guidelines.",
        chip1: "Find IELTS Speaking books",
        chip2: "SAT Math practice tests",
        chip3: "AP History summary",
        chip4: "Cambridge CEQ past papers",
        companyCredit: "KutubxonaAI Scientific Project developed by Smart Library LLC"
    },
    uz: {
        landingTitle: "Kutubxona AI",
        landingSubtitle: "Ta'lim yordamchisiga kirish uchun parolni kiriting.",
        passwordPlaceholder: "Parol",
        wrongPassword: "Noto'g'ri parol",
        enterBtn: "Kirish",
        newConversation: "Yangi sessiya",
        examPrep: "Imtihonga tayyorgarlik",
        ieltsSection: "IELTS materiallari",
        satSection: "SAT manbalari",
        apSection: "AP kurslari",
        ceqSection: "Cambridge CEQ",
        langLearning: "Til o'rganish",
        englishBooks: "Ingliz tili darsliklari",
        russianBooks: "Rus adabiyoti",
        settings: "Sozlamalar",
        libraryAssistant: "Ta'lim yordamchisi",
        online: "Onlayn",
        searchCatalog: "Kitoblarni qidirish",
        libraryAccount: "Talaba profili",
        welcomeMsg1: "Xush kelibsiz! Men <strong>Kutubxona AI</strong>, sizning ta'lim yordamchingizman.",
        welcomeMsg2: "Men sizga hayotning har hil sohalarida yordam bera olaman.",
        askPlaceholder: "Imtihon, kitob yoki mavzu haqida so'rang...",
        footerNote: "Kutubxona AI ta'lim yordamchisi bo'lib, uning maslahatlari rasmiy imtihon qoidalari bilan to'ldirilishi kerak.",
        chip1: "IELTS Speaking kitoblarini topish",
        chip2: "SAT Math amaliy testlari",
        chip3: "AP Tarix xulosasi",
        chip4: "Cambridge CEQ o'tgan imtihon qog'ozlari",
        companyCredit: "\"Smart Library\" MCHJ tomonidan yaratilgan KutubxonaAI ilmiy loyihasi"
    },
    ru: {
        landingTitle: "Kutubxona AI",
        landingSubtitle: "Введите пароль для доступа к образовательному помощнику.",
        passwordPlaceholder: "Пароль",
        wrongPassword: "Неверный пароль",
        enterBtn: "Войти",
        newConversation: "Новая сессия",
        examPrep: "Подготовка к экзаменам",
        ieltsSection: "Материалы IELTS",
        satSection: "Ресурсы SAT",
        apSection: "Курсы AP",
        ceqSection: "Cambridge CEQ",
        langLearning: "Изучение языков",
        englishBooks: "Учебники английского",
        russianBooks: "Русская литература",
        settings: "Настройки",
        libraryAssistant: "Образовательный помощник",
        online: "В сети",
        searchCatalog: "Поиск книг",
        libraryAccount: "Профиль студента",
        welcomeMsg1: "Добро пожаловать! Я <strong>Kutubxona AI</strong>, ваш образовательный помощник.",
        welcomeMsg2: "Я могу помочь вам в различных сферах жизни.",
        askPlaceholder: "Спросите об экзамене, книге или теме...",
        footerNote: "Kutubxona AI - это образовательный помощник, его советы следует дополнять официальными руководствами по экзаменам.",
        chip1: "Найти книги IELTS Speaking",
        chip2: "Практические тесты SAT Math",
        chip3: "Резюме истории AP",
        chip4: "Прошлые работы Cambridge CEQ",
        companyCredit: "Научный проект KutubxonaAI, разработанный ООО «Smart Library»"
    }
};

document.addEventListener('DOMContentLoaded', () => {
    let currentLang = 'uz';

    // --- 3D Background Init ---
    if (typeof VANTA !== 'undefined') {
        VANTA.NET({
            el: "#vanta-bg",
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x10b981,
            backgroundColor: 0x09090b,
            points: 12.00,
            maxDistance: 22.00,
            spacing: 18.00
        });
    }

    // --- Localization Logic ---
    const updateLanguage = (lang) => {
        currentLang = lang;
        const dict = translations[lang];

        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) el.innerHTML = dict[key];
        });

        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (dict[key]) el.placeholder = dict[key];
        });
        
        document.querySelectorAll('[data-i18n-title]').forEach(el => {
            const key = el.getAttribute('data-i18n-title');
            if (dict[key]) el.title = dict[key];
        });
    };

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
            const selectedLang = e.target.getAttribute('data-lang');
            document.querySelectorAll(`.lang-btn[data-lang="${selectedLang}"]`).forEach(b => b.classList.add('active'));
            updateLanguage(selectedLang);
        });
    });

    // --- Authentication Logic ---
    const loginForm = document.getElementById('loginForm');
    const passwordInput = document.getElementById('passwordInput');
    const errorMsg = document.getElementById('errorMsg');
    const landingPage = document.getElementById('landingPage');
    const appContainer = document.getElementById('appContainer');

    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const pwd = passwordInput.value;
        if (pwd === 'kutubxona2026') {
            errorMsg.style.display = 'none';
            landingPage.classList.add('fade-out');
            setTimeout(() => {
                appContainer.classList.remove('hidden');
                document.getElementById('userInput').focus();
            }, 500);
        } else {
            errorMsg.style.display = 'block';
            passwordInput.value = '';
            document.querySelector('.glass-card').style.transform = 'translateX(-10px)';
            setTimeout(() => { document.querySelector('.glass-card').style.transform = 'translateX(10px)'; }, 100);
            setTimeout(() => { document.querySelector('.glass-card').style.transform = 'translateX(-10px)'; }, 200);
            setTimeout(() => { document.querySelector('.glass-card').style.transform = 'translateX(0)'; }, 300);
        }
    });

    // --- Chat Logic ---
    const chatForm = document.getElementById('chatForm');
    const userInput = document.getElementById('userInput');
    const chatMessages = document.getElementById('chatMessages');
    const sendBtn = document.getElementById('sendBtn');
    
    // Suggestion Chips Click Handler
    document.querySelectorAll('.chip').forEach(chip => {
        chip.addEventListener('click', (e) => {
            userInput.value = e.target.textContent;
            sendBtn.disabled = false;
            // trigger submit
            chatForm.dispatchEvent(new Event('submit'));
        });
    });

    const createMessageElement = (content, isUser = false) => {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'ai-message'}`;
        
        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'avatar';
        avatarDiv.innerHTML = isUser ? '<i class="fa-regular fa-user"></i>' : '<i class="fa-solid fa-graduation-cap"></i>';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        if (content === 'TYPING_INDICATOR') {
            contentDiv.innerHTML = `
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            `;
            contentDiv.id = 'typingIndicator';
        } else {
            contentDiv.innerHTML = `<p>${content}</p>`;
        }
        
        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);
        
        return messageDiv;
    };

    const scrollToBottom = () => {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    };

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const text = userInput.value.trim();
        if (!text) return;
        
        userInput.value = '';
        userInput.disabled = true;
        sendBtn.disabled = true;
        document.querySelectorAll('.chip').forEach(c => c.style.pointerEvents = 'none');
        
        const userMsg = createMessageElement(text, true);
        chatMessages.appendChild(userMsg);
        scrollToBottom();
        
        const typingMsg = createMessageElement('TYPING_INDICATOR', false);
        chatMessages.appendChild(typingMsg);
        scrollToBottom();
        
        try {
            // Determine backend URL based on environment
            const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
            const PRODUCTION_BACKEND_URL = 'https://kutubxona-backend-python.onrender.com';
            const BACKEND_URL = isLocalhost ? 'http://localhost:8000' : PRODUCTION_BACKEND_URL;

            const response = await fetch(`${BACKEND_URL}/api/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: text, language: currentLang })
            });
            
            if (!response.ok) throw new Error('Network response was not ok');
            
            const data = await response.json();
            
            chatMessages.removeChild(typingMsg);
            
            // Render markdown or text
            const aiResponseText = data.response.replace(/\n/g, '<br>'); // Simple line break handling
            
            const aiMsg = createMessageElement(aiResponseText, false);
            chatMessages.appendChild(aiMsg);
            
        } catch (error) {
            console.error('Error fetching AI response:', error);
            chatMessages.removeChild(typingMsg);
            const errorMsg = createMessageElement('Kechirasiz, tizimga ulanishda xatolik yuz berdi. Iltimos, keyinroq qayta urinib ko\'ring.', false);
            chatMessages.appendChild(errorMsg);
        }
        
        scrollToBottom();
        userInput.disabled = false;
        sendBtn.disabled = false;
        document.querySelectorAll('.chip').forEach(c => c.style.pointerEvents = 'auto');
        userInput.focus();
    });

    userInput.addEventListener('input', () => {
        sendBtn.disabled = userInput.value.trim().length === 0;
    });

    // Initialize default language
    updateLanguage('uz');
});
