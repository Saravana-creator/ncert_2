# NCERT Doubt Solver - Complete Startup Guide

## 🎯 ONE-TIME SETUP

### 1. Setup Python Virtual Environment
```bash
cd d:\ncert_initial\backend\ai_model_training
python -m venv venv
venv\Scripts\activate
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
**OR simply double-click: `start_ai.bat`**

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
2. **Backend**: Visit http://localhost:8080 (should show "Cannot GET /")
3. **AI Service**: Check terminal shows "Uvicorn running on http://0.0.0.0:8001"
4. **Frontend**: Visit http://localhost:5173 (should show NCERT UI)

---

## 📊 SYSTEM REQUIREMENTS MET ✅

- **RAM**: 16GB ✅ (Perfect for Phi-2)
- **Storage**: 512GB SSD ✅ (Plenty of space)
- **Python**: 3.10.11 ✅
- **Node.js**: 22.14.0 ✅
- **MongoDB**: 8.0.8 ✅

---

## 🎓 MODEL INFO

**Current Model**: Microsoft Phi-2
- **Size**: 5.5GB
- **RAM Usage**: 8-10GB
- **Quality**: Excellent for NCERT
- **Speed**: 3-5 seconds per answer

---

## ❓ TROUBLESHOOTING

**If AI service fails to start:**
```bash
cd d:\ncert_initial\backend\ai_model_training
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

**If model download is slow:**
- First run will download 5.5GB (takes 10-30 minutes)
- Model is cached, subsequent runs are instant

**If out of memory:**
- Close other applications
- Restart your laptop
- Your 16GB RAM is sufficient!