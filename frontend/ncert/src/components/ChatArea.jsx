import { useState, useRef, useEffect } from 'react'
import api from '../services/api'
import { FaUser, FaRobot, FaPaperPlane } from 'react-icons/fa'
import { BsChatDots, BsLightbulb } from 'react-icons/bs'
import { IoSchool } from 'react-icons/io5'
import { GiPlantSeed, GiWaterDrop } from 'react-icons/gi'
import { MdHowToVote } from 'react-icons/md'

export default function ChatArea({ userId, grade, messages, onNewMessage }) {
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSend = async () => {
    if (!input.trim() || isLoading) return

    const userMessage = { role: 'user', content: input }
    onNewMessage(userMessage)
    setInput('')
    setIsLoading(true)

    try {
      const res = await api.post('/chat', {
        userId,
        grade,
        message: input
      })
      
      const assistantMessage = { 
        role: 'assistant', 
        content: res.data.answer 
      }
      onNewMessage(assistantMessage)
    } catch (error) {
      const errorMessage = {
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please try again!'
      }
      onNewMessage(errorMessage)
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  const handleSuggestionClick = (question) => {
    setInput(question)
  }

  return (
    <div className="chat-area">
      <div className="chat-header">
        <h2><BsChatDots /> Ask Your Doubts</h2>
        <p>I'm here to help you understand NCERT concepts better!</p>
      </div>

      <div className="messages-container">
        {messages.length === 0 ? (
          <div className="empty-state">
            <div className="empty-state-icon"><IoSchool size={80} /></div>
            <h3>Welcome, Student!</h3>
            <p>Upload your NCERT book and start asking questions. I'll help you learn better!</p>
            <div className="suggestion-chips">
              <div className="chip" onClick={() => handleSuggestionClick('What is photosynthesis?')}>
                <GiPlantSeed /> What is photosynthesis?
              </div>
              <div className="chip" onClick={() => handleSuggestionClick('Explain the water cycle')}>
                <GiWaterDrop /> Explain the water cycle
              </div>
              <div className="chip" onClick={() => handleSuggestionClick('What is democracy?')}>
                <MdHowToVote /> What is democracy?
              </div>
            </div>
          </div>
        ) : (
          <>
            {messages.map((msg, idx) => (
              <div key={idx} className={`message ${msg.role}`}>
                <div className="message-avatar">
                  {msg.role === 'user' ? <FaUser size={20} /> : <FaRobot size={20} />}
                </div>
                <div className="message-content">
                  <p>{msg.content}</p>
                </div>
              </div>
            ))}
            {isLoading && (
              <div className="message assistant">
                <div className="message-avatar"><FaRobot size={20} /></div>
                <div className="message-content">
                  <div className="loading">
                    <div className="loading-dot"></div>
                    <div className="loading-dot"></div>
                    <div className="loading-dot"></div>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </>
        )}
      </div>

      <div className="input-area">
        <div className="input-container">
          <input
            type="text"
            placeholder="Type your question here..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            disabled={isLoading}
          />
          <button 
            className="send-btn" 
            onClick={handleSend}
            disabled={!input.trim() || isLoading}
          >
            <FaPaperPlane size={18} />
          </button>
        </div>
      </div>
    </div>
  )
}
