# NCERT Doubt Solver

An AI-powered application to help students solve NCERT-related doubts using OCR, RAG (Retrieval Augmented Generation), and LLM technologies.

## Project Structure

```
ncert_initial/
├── backend/
│   ├── ai_model_training/     # AI/ML services (FastAPI)
│   ├── gateway-node/          # API gateway and routes
│   ├── server.js             # Main Express server
│   └── db.js                 # Database connection
├── frontend/
│   └── ncert/                # React frontend
└── package.json              # Root package configuration
```

## Features

- **File Upload**: Upload NCERT textbook images/PDFs
- **OCR Processing**: Extract text from uploaded files
- **AI Chat**: Ask questions and get AI-powered answers
- **Chat History**: Maintain conversation history
- **Responsive UI**: Modern React-based interface

## Setup Instructions

### Prerequisites
- Node.js (v16+)
- Python (v3.8+)
- MongoDB

### Installation

1. **Install all dependencies:**
   ```bash
   npm run install-all
   ```

2. **Install Python dependencies (with Virtual Environment):**
   ```bash
   cd backend/ai_model_training
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start MongoDB** (ensure it's running on localhost:27017)

2. **Start AI Service:**
   ```bash
   cd backend/ai_model_training
   venv\Scripts\activate
   python main.py
   ```

3. **Start Backend Server:**
   ```bash
   cd backend
   npm start
   ```

4. **Start Frontend:**
   ```bash
   cd frontend/ncert
   npm run dev
   ```

## Development Notes

- The application uses ES modules (`"type": "module"`)
- CORS is configured for cross-origin requests
- File uploads are handled with Multer
- AI responses are generated using **TinyLlama-1.1B-Chat** model
- Optimized for multilingual NCERT content with citations.