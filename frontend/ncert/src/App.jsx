import { useState, useEffect } from 'react'
import './App.css'
import Sidebar from './components/Sidebar'
import ChatArea from './components/ChatArea'
import api from './services/api'

function App() {
  const [userId] = useState(() => localStorage.getItem('userId') || `user_${Date.now()}`)
  const [grade, setGrade] = useState(() => localStorage.getItem('grade') || '8')
  const [chatHistory, setChatHistory] = useState([])
  const [uploadedFiles, setUploadedFiles] = useState(() => {
    const saved = localStorage.getItem('uploadedFiles')
    return saved ? JSON.parse(saved) : []
  })
  const [currentMessages, setCurrentMessages] = useState([])

  useEffect(() => {
    localStorage.setItem('userId', userId)
    localStorage.setItem('grade', grade)
  }, [userId, grade])

  useEffect(() => {
    localStorage.setItem('uploadedFiles', JSON.stringify(uploadedFiles))
  }, [uploadedFiles])

  useEffect(() => {
    loadChatHistory()
  }, [])

  const loadChatHistory = async () => {
    try {
      const res = await api.get(`/history/${userId}`)
      if (res.data && res.data.messages) {
        setChatHistory(res.data.messages)
        setCurrentMessages(res.data.messages)
      }
    } catch (error) {
      console.log('No chat history found')
    }
  }

  const handleFileUpload = (fileName) => {
    const newFile = {
      id: Date.now(),
      name: fileName,
      uploadedAt: new Date().toISOString()
    }
    setUploadedFiles(prev => [newFile, ...prev])
  }

  const handleNewMessage = (message) => {
    setCurrentMessages(prev => [...prev, message])
    setChatHistory(prev => [...prev, message])
  }

  const clearChat = () => {
    setCurrentMessages([])
  }

  return (
    <div className="app-container">
      <Sidebar 
        grade={grade}
        setGrade={setGrade}
        uploadedFiles={uploadedFiles}
        onFileUpload={handleFileUpload}
        onClearChat={clearChat}
      />
      <ChatArea 
        userId={userId}
        grade={grade}
        messages={currentMessages}
        onNewMessage={handleNewMessage}
      />
    </div>
  )
}

export default App
