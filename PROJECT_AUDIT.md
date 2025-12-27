# NCERT Doubt Solver - Project Audit & Setup Guide

## ✅ ENVIRONMENT CHECK

### Installed Software:
- **Python**: 3.10.11 ✅
- **Node.js**: v22.14.0 ✅  
- **MongoDB**: v8.0.8 ✅
- **OS**: Windows 10/11 ✅

**Status**: Your environment is CORRECT and ready!

---

## 📁 PROJECT STRUCTURE ANALYSIS

### Backend Structure:
```
backend/
├── server.js (Main Express server - Port 8080) ✅
├── db.js (MongoDB connection) ✅
├── package.json (Dependencies configured) ✅
├── uploads/ (File storage directory) ✅
├── gateway-node/
│   ├── src/
│   │   ├── routes/ (upload.js, chat.js, history.js) ✅
│   │   ├── models/ (Chat.js, Users.js, Feedback.js) ✅
│   │   └── middleware/ (cors.js) ✅
│   └── uploads/ (Alternative upload location) ⚠️
└── ai_model_training/
    ├── main.py (FastAPI server - Port 8001) ✅
    ├── ocr.py (PDF/Image text extraction) ✅
    ├── rag.py (Vector DB & retrieval) ✅
    ├── llm.py (Mistral-7B for reasoning) ✅
    ├── ingest.py (File processing pipeline) ✅
    └── requirements.txt ✅
```

### Frontend Structure:
```
frontend/ncert/
├── src/
│   ├── components/ (Chat, FileUpload, Message, SideBar) ✅
│   ├── services/ (api.js) ✅
│   └── App.jsx ✅
├── package.json ✅
└── vite.config.js (Port 5173) ✅
```

---

## ⚠️ IDENTIFIED ISSUES

### 1. **Duplicate Upload Directories**
- `backend/uploads/` 
- `backend/gateway-node/uploads/`
**Fix**: Consolidated to use `backend/uploads/`

### 2. **Mistral-7B Model Too Large**
- **Size**: ~14GB download
- **RAM Required**: 14-16GB minimum
- **Issue**: Will cause laptop to freeze/crash

### 3. **AI Model Not Working**
- Mistral-7B is too resource-intensive for most laptops
- Need lighter alternative

---

## 🔧 RECOMMENDED FIXES

### Fix 1: Use Lighter AI Model
Replace Mistral-7B with **TinyLlama-1.1B** (much lighter):
- **Size**: ~2.2GB
- **RAM**: 4-6GB
- **Speed**: 5-10x faster

### Fix 2: Simplify Requirements
Remove heavy dependencies that cause conflicts

---

## 📋 CORRECTED SETUP STEPS

### Step 1: Install Backend Dependencies
```bash
cd backend
npm install
```

### Step 2: Install Lightweight Python Dependencies
```bash
cd backend/ai_model_training
pip install fastapi uvicorn pydantic PyPDF2 paddleocr transformers torch --index-url https://download.pytorch.org/whl/cpu
```

### Step 3: Install Frontend Dependencies  
```bash
cd frontend/ncert
npm install
```

### Step 4: Start Services

**Terminal 1 - MongoDB:**
```bash
cd d:\ncert_initial
mongod --dbpath ./data
```

**Terminal 2 - Backend:**
```bash
cd d:\ncert_initial\backend
npm start
```

**Terminal 3 - AI Service:**
```bash
cd d:\ncert_initial\backend\ai_model_training
python main.py
```

**Terminal 4 - Frontend:**
```bash
cd d:\ncert_initial\frontend\ncert
npm run dev
```

---

## 🎯 WORKING CONFIGURATION

### Ports:
- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:8080
- **AI Service**: http://localhost:8001
- **MongoDB**: mongodb://127.0.0.1:27017

### Data Flow:
1. User uploads PDF → Backend saves to `uploads/`
2. Backend sends path → AI Service (Port 8001)
3. AI extracts text → Stores in Vector DB
4. User asks question → AI retrieves relevant chunks
5. LLM generates answer → Returns to user
6. Chat saved to MongoDB

---

## ⚡ NEXT STEPS TO FIX AI MODEL

I will now update the LLM to use TinyLlama instead of Mistral-7B so your laptop can handle it properly.