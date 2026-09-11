import base64
import os

def b64(path):
    with open(path, 'rb') as f:
        ext = path.split('.')[-1]
        mime = 'image/png' if ext == 'png' else 'image/jpeg'
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode('utf-8')}"

logo_b64 = b64('images/kutubxona_logo.png')
gov1_b64 = b64('images/gov1.jpg')

html_content = f"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<title>Kutubxona AI — Yagona Strategik Taqdimot Slaydi</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

@page {{
    size: 1920px 1080px;
    margin: 0;
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

html, body {{
    width: 1920px;
    height: 1080px;
    max-width: 1920px;
    max-height: 1080px;
    overflow: hidden;
    background-color: #070c18;
    color: #f8fafc;
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

.slide {{
    width: 1920px;
    height: 1080px;
    padding: 14px 26px 10px 26px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: radial-gradient(circle at 90% 10%, rgba(16, 185, 129, 0.12) 0%, transparent 45%),
                radial-gradient(circle at 10% 90%, rgba(6, 182, 212, 0.1) 0%, transparent 40%),
                linear-gradient(135deg, #070c18 0%, #030710 100%);
    position: relative;
    box-sizing: border-box;
}}

/* Top Header */
.header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 8px;
}}

.brand-wrap {{
    display: flex;
    align-items: center;
    gap: 16px;
}}

.logo-img {{
    width: 66px;
    height: 66px;
    object-fit: contain;
    border-radius: 14px;
    background: rgba(16, 185, 129, 0.1);
    border: 1.5px solid rgba(16, 185, 129, 0.35);
    padding: 4px;
}}

.brand-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 40px;
    font-weight: 800;
    line-height: 1.05;
    color: #ffffff;
    letter-spacing: -0.5px;
}}

.brand-title span {{
    color: #10b981;
    font-weight: 900;
}}

.brand-sub {{
    font-size: 14.5px;
    font-weight: 700;
    color: #94a3b8;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 2px;
}}

.header-center {{
    display: flex;
    align-items: center;
    gap: 14px;
}}

.exec-badge {{
    background: rgba(16, 185, 129, 0.14);
    border: 1.5px solid rgba(16, 185, 129, 0.45);
    color: #34d399;
    padding: 9px 24px;
    border-radius: 9999px;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 10px;
}}

.exec-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #10b981;
}}

.target-badge {{
    background: rgba(6, 182, 212, 0.12);
    border: 1.5px solid rgba(6, 182, 212, 0.4);
    color: #38bdf8;
    padding: 9px 24px;
    border-radius: 9999px;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.3px;
}}

.header-right {{
    display: flex;
    align-items: center;
    gap: 16px;
}}

.status-pill {{
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(255, 255, 255, 0.05);
    border: 1.5px solid rgba(255, 255, 255, 0.15);
    padding: 9px 20px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: 600;
    color: #cbd5e1;
}}

.pulse-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #10b981;
}}

.web-link {{
    color: #10b981;
    font-weight: 700;
    text-decoration: none;
}}

/* Metrics Strip */
.metrics-strip {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin: 8px 0 10px 0;
}}

.metric-box {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 12px;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 14px;
}}

.metric-icon {{
    width: 50px;
    height: 50px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    flex-shrink: 0;
}}

.icon-red {{ background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.35); }}
.icon-green {{ background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); }}
.icon-cyan {{ background: rgba(6, 182, 212, 0.15); border: 1px solid rgba(6, 182, 212, 0.35); }}
.icon-amber {{ background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.35); }}

.metric-content {{
    flex: 1;
}}

.metric-label {{
    font-size: 14px;
    font-weight: 700;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

.metric-value {{
    font-size: 17.5px;
    font-weight: 700;
    color: #f1f5f9;
    margin-top: 2px;
    line-height: 1.25;
}}

.metric-value strong {{
    color: #34d399;
}}

/* Main Grid */
.main-grid {{
    display: grid;
    grid-template-columns: 1.1fr 1fr 1.05fr;
    gap: 16px;
    flex: 1;
    min-height: 0;
}}

.col {{
    display: flex;
    flex-direction: column;
    height: 100%;
}}

.card {{
    background: rgba(15, 23, 42, 0.72);
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 14px;
    padding: 14px 18px;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-between;
}}

.card-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
    padding-bottom: 6px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}}

.card-badge {{
    width: 34px;
    height: 34px;
    border-radius: 8px;
    background: rgba(16, 185, 129, 0.15);
    border: 1.5px solid rgba(16, 185, 129, 0.45);
    color: #10b981;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 800;
}}

.card-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 23px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.2px;
}}

.card-subtitle {{
    margin-left: auto;
    font-size: 14px;
    font-weight: 700;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

/* Column 1: Tech Modules */
.modules-container {{
    display: flex;
    flex-direction: column;
    gap: 8px;
    flex: 1;
    justify-content: space-between;
}}

.module-item {{
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 12px;
    padding: 10px 14px;
    display: flex;
    gap: 14px;
    align-items: flex-start;
}}

.module-icon {{
    width: 46px;
    height: 46px;
    border-radius: 10px;
    background: rgba(16, 185, 129, 0.14);
    border: 1.5px solid rgba(16, 185, 129, 0.35);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    flex-shrink: 0;
}}

.module-info {{
    flex: 1;
}}

.module-head {{
    font-size: 18.5px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 2px;
}}

.module-desc {{
    font-size: 15px;
    color: #e2e8f0;
    line-height: 1.35;
    margin-bottom: 4px;
}}

.module-tags {{
    display: flex;
    gap: 8px;
}}

.m-tag {{
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.32);
    color: #34d399;
    font-size: 13.5px;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 5px;
}}

/* Column 2: Pilot & Impact */
.pilot-card {{
    background: rgba(15, 23, 42, 0.72);
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 14px;
    padding: 14px 18px;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-between;
}}

.pilot-img-wrap {{
    position: relative;
    width: 100%;
    height: 175px;
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 8px;
    border: 1.5px solid rgba(16, 185, 129, 0.35);
}}

.pilot-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
}}

.pilot-tag {{
    position: absolute;
    bottom: 8px;
    left: 8px;
    background: rgba(7, 12, 24, 0.92);
    border: 1.5px solid rgba(16, 185, 129, 0.5);
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 700;
    color: #34d399;
}}

.pilot-text {{
    font-size: 15.5px;
    color: #f1f5f9;
    line-height: 1.45;
    margin-bottom: 4px;
}}

.pilot-text strong {{
    color: #ffffff;
}}

.pilot-stats-strip {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin: 6px 0;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 10px;
    padding: 8px;
}}

.p-stat-box {{
    text-align: center;
}}

.p-stat-num {{
    font-family: 'Outfit', sans-serif;
    font-size: 23px;
    font-weight: 800;
    color: #38bdf8;
}}

.p-stat-lbl {{
    font-size: 13.5px;
    font-weight: 600;
    color: #94a3b8;
    margin-top: 2px;
}}

.impact-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-top: 4px;
}}

.impact-mini {{
    background: rgba(16, 185, 129, 0.09);
    border: 1.5px solid rgba(16, 185, 129, 0.28);
    border-radius: 8px;
    padding: 8px 6px;
    text-align: center;
}}

.impact-stat {{
    font-family: 'Outfit', sans-serif;
    font-size: 21px;
    font-weight: 800;
    color: #10b981;
}}

.impact-sub {{
    font-size: 13px;
    color: #e2e8f0;
    margin-top: 2px;
    line-height: 1.25;
}}

/* Column 3: Roadmap & Team */
.steps-container {{
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 6px;
}}

.step-item {{
    display: flex;
    gap: 12px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 10px;
    padding: 8px 12px;
    align-items: flex-start;
}}

.step-num {{
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: rgba(6, 182, 212, 0.15);
    border: 1.5px solid rgba(6, 182, 212, 0.4);
    color: #38bdf8;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    font-weight: 800;
    flex-shrink: 0;
}}

.step-info {{
    flex: 1;
}}

.step-head-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2px;
}}

.step-head {{
    font-size: 16px;
    font-weight: 700;
    color: #f1f5f9;
}}

.step-timeline {{
    font-size: 12.5px;
    font-weight: 700;
    color: #38bdf8;
    background: rgba(6, 182, 212, 0.14);
    border: 1px solid rgba(6, 182, 212, 0.35);
    padding: 2px 8px;
    border-radius: 4px;
}}

.step-desc {{
    font-size: 14.5px;
    color: #cbd5e1;
    line-height: 1.35;
}}

/* Strategic Guarantees & Integration Grid */
.guarantee-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    margin-top: 6px;
}}

.g-card {{
    background: rgba(255, 255, 255, 0.035);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 10px 8px 9px 8px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}}

.g-icon {{
    font-size: 22px;
    margin-bottom: 5px;
    line-height: 1;
}}

.g-name {{
    font-size: 13.5px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.25;
    margin-bottom: 3px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    width: 100%;
}}

.g-desc {{
    font-size: 11.5px;
    font-weight: 500;
    color: #94a3b8;
    line-height: 1.25;
}}

/* Slide Footer */
.footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 8px;
    font-size: 14.5px;
    color: #94a3b8;
}}

.footer-left strong {{
    color: #ffffff;
}}

.footer-right {{
    display: flex;
    align-items: center;
    gap: 16px;
    color: #cbd5e1;
}}

.footer-link {{
    color: #10b981;
    font-weight: 700;
    text-decoration: none;
}}
</style>
</head>
<body>

<div class="slide">
    <!-- Header -->
    <header class="header">
        <div class="brand-wrap">
            <img src="{logo_b64}" alt="Kutubxona AI" class="logo-img">
            <div>
                <div class="brand-title">Kutubxona<span>.AI</span></div>
                <div class="brand-sub">Milliy Sun'iy Intellekt Ta'lim Ekotizimi</div>
            </div>
        </div>

        <div class="header-center">
            <div class="exec-badge">
                <span class="exec-dot"></span>
                Milliy AI Ta'lim Ekotizimi
            </div>
            <div class="target-badge">
                O'zbekiston Yoshlari Va Talabalari Uchun
            </div>
        </div>

        <div class="header-right">
            <div class="status-pill">
                <span class="pulse-dot"></span>
                <span>Ishchi Tizim: <a href="https://www.kutubxona-ai.uz/" class="web-link" target="_blank">www.kutubxona-ai.uz</a></span>
            </div>
        </div>
    </header>

    <!-- Metrics Strip -->
    <div class="metrics-strip">
        <div class="metric-box">
            <div class="metric-icon icon-red">⚠️</div>
            <div class="metric-content">
                <div class="metric-label">Hozirgi Muammo</div>
                <div class="metric-value">Repetitorlik xarajatlari yuqori (<strong>$150M+/yil</strong>) va hududiy tengsizlik</div>
            </div>
        </div>
        <div class="metric-box">
            <div class="metric-icon icon-green">💡</div>
            <div class="metric-content">
                <div class="metric-label">Milliy AI Yechim</div>
                <div class="metric-value"><strong>100% Bepul, 24/7</strong> shaxsiy repetitor (O'zbek, Rus, Ingliz tillarida)</div>
            </div>
        </div>
        <div class="metric-box">
            <div class="metric-icon icon-cyan">🎯</div>
            <div class="metric-content">
                <div class="metric-label">Kutilayotgan Ta'sir</div>
                <div class="metric-value"><strong>100,000+ yoshlar</strong> qamrovi, <strong>$1.5M+</strong> oilaviy tejov, 3x sertifikatlar</div>
            </div>
        </div>
        <div class="metric-box">
            <div class="metric-icon icon-amber">🏛️</div>
            <div class="metric-content">
                <div class="metric-label">Amaliy Natija</div>
                <div class="metric-value">Samarqand viloyati axborot-kutubxona markazida <strong>to'liq sinovdan o'tgan</strong></div>
            </div>
        </div>
    </div>

    <!-- Main Grid -->
    <div class="main-grid">
        <!-- Column 1: Core AI Modules -->
        <div class="col">
            <div class="card">
                <div class="card-header">
                    <div class="card-badge">1</div>
                    <div class="card-title">4 Asosiy Texnologik Ustun</div>
                    <div class="card-subtitle">AI Modullari</div>
                </div>

                <div class="modules-container">
                    <div class="module-item">
                        <div class="module-icon">📚</div>
                        <div class="module-info">
                            <div class="module-head">Smart Library RAG (Ilmiy Kutubxona)</div>
                            <div class="module-desc">Darsliklar va tasdiqlangan ilmiy adabiyotlar bazasi. Har bir savolga manbaga tayangan 100% aniq javob.</div>
                            <div class="module-tags">
                                <span class="m-tag">✓ 5,000+ Darslik</span>
                                <span class="m-tag">✓ Manbaga Havola</span>
                                <span class="m-tag">✓ 0% Gallyutsinatsiya</span>
                            </div>
                        </div>
                    </div>

                    <div class="module-item">
                        <div class="module-icon">🎓</div>
                        <div class="module-info">
                            <div class="module-head">IELTS, SAT & CEFR AI Trener</div>
                            <div class="module-desc">Insholarni xalqaro rubrika bo'yicha 5 soniyada baholaydi, xatolarni tahlil qiladi va speakingni rivojlantiradi.</div>
                            <div class="module-tags">
                                <span class="m-tag">✓ Band 9.0 Rubrika</span>
                                <span class="m-tag">✓ Instant Tahlil</span>
                                <span class="m-tag">✓ Speaking Trenajyor</span>
                            </div>
                        </div>
                    </div>

                    <div class="module-item">
                        <div class="module-icon">🇺🇿</div>
                        <div class="module-info">
                            <div class="module-head">O'zbek Tili NLP Dvigateli</div>
                            <div class="module-desc">Lotin va Kirill imlosida akademik o'zbek tilida muloqot qiladi. Pedagogik atamalar va darsliklar standartiga mos.</div>
                            <div class="module-tags">
                                <span class="m-tag">✓ Lotin & Kirill</span>
                                <span class="m-tag">✓ Davlat Tili NLP</span>
                                <span class="m-tag">✓ Milliy Semantika</span>
                            </div>
                        </div>
                    </div>

                    <div class="module-item">
                        <div class="module-icon">📊</div>
                        <div class="module-info">
                            <div class="module-head">Intellektual O'quv Analitikasi</div>
                            <div class="module-desc">Talabalarning fanlar bo'yicha o'zlashtirish darajasi, kuchli va zaif tomonlari hamda bilim dinamikasi monitoringi.</div>
                            <div class="module-tags">
                                <span class="m-tag">✓ Shaxsiy Hisobot</span>
                                <span class="m-tag">✓ Real-vaqt Tahlili</span>
                                <span class="m-tag">✓ O'sish Dinamikasi</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Column 2: Regional Pilot & Impact -->
        <div class="col">
            <div class="pilot-card">
                <div>
                    <div class="card-header">
                        <div class="card-badge">2</div>
                        <div class="card-title">Samarqand Piloti & Amaliy Natija</div>
                        <div class="card-subtitle">Laboratoriya</div>
                    </div>

                    <div class="pilot-img-wrap">
                        <img src="{gov1_b64}" alt="Samarqand viloyati hokimi bilan uchrashuv" class="pilot-img">
                        <div class="pilot-tag">🏛️ Samarqand Axborot-Kutubxona Markazi</div>
                    </div>

                    <div class="pilot-text">
                        <strong>Samarqand viloyati hokimi Adiz Boboyev</strong> bilan uchrashuvda loyiha to'liq taqdim etildi va viloyat axborot-kutubxona markazida laboratoriya ishga tushirildi.
                    </div>
                    <div class="pilot-text" style="color: #cbd5e1; font-size: 14.5px;">
                        Laboratoriyada 1,200+ o'quvchi platformani sinovdan o'tkazdi va 94% ijobiy natija qayd etildi.
                    </div>
                </div>

                <div>
                    <div class="pilot-stats-strip">
                        <div class="p-stat-box">
                            <div class="p-stat-num">1.2 sek</div>
                            <div class="p-stat-lbl">Javob tezligi</div>
                        </div>
                        <div class="p-stat-box">
                            <div class="p-stat-num">5,000+</div>
                            <div class="p-stat-lbl">Ilmiy manbalar</div>
                        </div>
                        <div class="p-stat-box">
                            <div class="p-stat-num">96.8%</div>
                            <div class="p-stat-lbl">Baholash aniqligi</div>
                        </div>
                    </div>

                    <div class="impact-grid">
                        <div class="impact-mini">
                            <div class="impact-stat">800K so'm</div>
                            <div class="impact-sub">Oyiga oilaga tejov</div>
                        </div>
                        <div class="impact-mini">
                            <div class="impact-stat">100% Tenglik</div>
                            <div class="impact-sub">Chekka hududga imkon</div>
                        </div>
                        <div class="impact-mini">
                            <div class="impact-stat">Suverenitet</div>
                            <div class="impact-sub">Mahalliy xavfsiz tizim</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Column 3: Student Learning Benefits & Platform Statistics -->
        <div class="col">
            <div class="card">
                <div>
                    <div class="card-header">
                        <div class="card-badge">3</div>
                        <div class="card-title">Talabalar Uchun Natijalar & Imkoniyatlar</div>
                        <div class="card-subtitle">O'quv Foydasi</div>
                    </div>

                    <div class="steps-container">
                        <div class="step-item">
                            <div class="step-num">1</div>
                            <div class="step-info">
                                <div class="step-head-row">
                                    <div class="step-head">Exam Score Boost (+1.5 - 2.0 Band)</div>
                                    <div class="step-timeline">+180 SAT ball</div>
                                </div>
                                <div class="step-desc">IELTS, SAT va CEFR imtihonlariga tayyorlanishda o'rtacha 2-3 oyda sezilarli va kafolatlangan natija o'sishi.</div>
                            </div>
                        </div>

                        <div class="step-item">
                            <div class="step-num">2</div>
                            <div class="step-info">
                                <div class="step-head-row">
                                    <div class="step-head">Writing Task Correction & AI Feedback</div>
                                    <div class="step-timeline">5 sekund</div>
                                </div>
                                <div class="step-desc">IELTS Task 1 & 2 insholarini xalqaro rubrika bo'yicha chuqur grammatik, leksik va strukturaviy tahlil qilish.</div>
                            </div>
                        </div>

                        <div class="step-item">
                            <div class="step-num">3</div>
                            <div class="step-info">
                                <div class="step-head-row">
                                    <div class="step-head">Ko'p Tilli Akademik Lug'at & Grammatika</div>
                                    <div class="step-timeline">UZ • EN • RU</div>
                                </div>
                                <div class="step-desc">Ingliz, rus va o'zbek tillarida akademik terminologiya, professional lug'at boyligi va muloqot mashg'ulotlari.</div>
                            </div>
                        </div>

                        <div class="step-item">
                            <div class="step-num">4</div>
                            <div class="step-info">
                                <div class="step-head-row">
                                    <div class="step-head">Interaktiv O'quv Asboblari & 24/7 AI Mentor</div>
                                    <div class="step-timeline">24/7 Yordam</div>
                                </div>
                                <div class="step-desc">Istalgan vaqtda savollarga 100% aniq manbali javob beruvchi va murakkab mavzularni tushuntiruvchi AI yordamchisi.</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div>
                    <div style="font-size: 15px; font-weight: 700; color: #cbd5e1; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center;">
                        <span style="display: flex; align-items: center; gap: 8px; color: #f1f5f9;">📊 Platforma Samaradorligi & Asosiy Metrikalar</span>
                        <span style="color: #10b981; font-weight: 700; font-size: 12px; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.35); padding: 2px 8px; border-radius: 4px;">STATISTIKA</span>
                    </div>
                    <div class="guarantee-grid">
                        <div class="g-card">
                            <div class="g-icon">⚡</div>
                            <div class="g-name">1.2 sek</div>
                            <div class="g-desc">Instant tahlil va javob tezligi</div>
                        </div>
                        <div class="g-card">
                            <div class="g-icon">🎯</div>
                            <div class="g-name">96.8%</div>
                            <div class="g-desc">Baholash va tavsiya aniqligi</div>
                        </div>
                        <div class="g-card">
                            <div class="g-icon">📈</div>
                            <div class="g-name">3x Tezroq</div>
                            <div class="g-desc">Imtihonlarga intensiv tayyorgarlik</div>
                        </div>
                        <div class="g-card">
                            <div class="g-icon">💎</div>
                            <div class="g-name">100% Bepul</div>
                            <div class="g-desc">Barcha yoshlar uchun teng imkoniyat</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-left">
            <strong>Kutubxona AI</strong> — O'zbekiston yoshlari va talabalariga sun'iy intellekt orqali <strong>24/7 zamonaviy va bepul ta'lim</strong> beruvchi milliy platforma.
        </div>
        <div class="footer-right">
            <span>📍 Samarqand / Toshkent</span>
            <span>🌐 <a href="https://www.kutubxona-ai.uz/" class="footer-link" target="_blank">www.kutubxona-ai.uz</a></span>
            <span>© 2026 Smart Library AI Lab</span>
        </div>
    </footer>
</div>

</body>
</html>
"""

with open('kutubxona_ai_1page_presentation.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated massive typography presentation slide HTML successfully!")
