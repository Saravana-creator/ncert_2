# NCERT Doubt Solver - Complete Startup Guide

## 🎯 ONE-TIME SETUP

### 1. Setup Python Virtual Environment
```bash
cd d:\ncert_initial\backend\ai_model_training
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Install Node Dependencies
```bash
cd d:\ncert_initial\backend
npm install

cd d:\ncert_initial\frontend\ncert
npm install
```

---

## 🚀 DAILY STARTUP (4 Terminals)

### Terminal 1: MongoDB
```bash
cd d:\ncert_initial
mongod --dbpath ./data
```
**Keep this running**

### Terminal 2: Backend Server
```bash
cd d:\ncert_initial\backend
npm start
```
**Server runs on: http://localhost:8080**

### Terminal 3: AI Service (with venv)
```bash
cd d:\ncert_initial\backend\ai_model_training
venv\Scripts\activate
python main.py
```
**AI Service runs on: http://localhost:8001**

### Terminal 4: Frontend
```bash
cd d:\ncert_initial\frontend\ncert
npm run dev
```
**Frontend runs on: http://localhost:5173**

---

## ⚡ QUICK START (Using Batch File)

Just double-click: `d:\ncert_initial\backend\ai_model_training\start_ai.bat`

This will:
1. Create venv (if not exists)
2. Activate venv
3. Install dependencies
4. Start AI service

---

## 🔍 VERIFY EVERYTHING IS WORKING

1. **MongoDB**: Check terminal shows "Waiting for connections"
2. **Backend**: Visit http://localhost:8080 (should show "Welcome to NCERT Doubt Solver API")
3. **AI Service**: Check terminal shows "Uvicorn running on http://0.0.0.0:8001"
4. **Frontend**: Visit http://localhost:5173 (should show the chat interface)

---

## 📊 SYSTEM REQUIREMENTS MET ✅

- **RAM**: 8GB+ recommended
- **Storage**: 10GB+ free space
- **Python**: 3.10+
- **Node.js**: 18+
- **MongoDB**: 6.0+

---

## 🎓 MODEL INFO

**Current Model**: Qwen2.5-1.5B-Instruct
- **Size**: ~3.1GB
- **RAM Usage**: 6-8GB
- **Quality**: State-of-the-art for reasoning and instruction following.
- **Speed**: 2-4 seconds per answer (optimized for CPU).
- **Strategy**: Uses "Chain-of-Thought" reasoning to prevent hallucinations.

---

## ❓ TROUBLESHOOTING

**If AI service fails to start (Import Errors):**
- Ensure you have activated the venv: `venv\Scripts\activate`
- Try force-reinstalling requirements: `pip install -r requirements.txt --force-reinstall`

**If out of memory:**
- Close other high-memory applications (Chrome, Games)
- Restart your laptop
- Ensure you are on a 64-bit Python version.