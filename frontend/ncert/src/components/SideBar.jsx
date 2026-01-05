import { useRef } from 'react'
import api from '../services/api'
import { FaBook, FaUpload, FaTrash, FaFile, FaBookOpen } from 'react-icons/fa'
import { MdClass } from 'react-icons/md'
import { HiFolder } from 'react-icons/hi'

export default function Sidebar({ grade, setGrade, uploadedFiles, onFileUpload, onClearChat }) {
  const fileInputRef = useRef(null)

  const handleFileClick = () => {
    fileInputRef.current?.click()
  }

  const handleFileChange = async (e) => {
    const file = e.target.files[0]
    if (!file) return

    const formData = new FormData()
    formData.append('file', file)

    try {
      await api.post('/upload', formData)
      onFileUpload(file.name)
      alert('✅ File uploaded successfully!')
    } catch (error) {
      alert('❌ Failed to upload file')
    }

    e.target.value = ''
  }

  const formatTime = (isoString) => {
    const date = new Date(isoString)
    return date.toLocaleString('en-IN', { 
      day: 'numeric', 
      month: 'short',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h1><FaBook /> NCERT Helper</h1>
        <p>Your Smart Study Buddy</p>
      </div>

      <div className="grade-selector">
        <label><MdClass /> Select Your Class</label>
        <select value={grade} onChange={(e) => setGrade(e.target.value)}>
          <option value="5">Class 5</option>
          <option value="6">Class 6</option>
          <option value="7">Class 7</option>
          <option value="8">Class 8</option>
          <option value="9">Class 9</option>
          <option value="10">Class 10</option>
        </select>
      </div>

      <div className="file-upload-section">
        <button className="upload-btn" onClick={handleFileClick}>
          <FaUpload /> Upload NCERT Book
        </button>
        <input
          ref={fileInputRef}
          type="file"
          accept=".pdf,.jpg,.jpeg,.png"
          onChange={handleFileChange}
          style={{ display: 'none' }}
        />
      </div>

      <div className="uploaded-files">
        <h3><HiFolder /> Uploaded Files ({uploadedFiles.length})</h3>
        {uploadedFiles.length === 0 ? (
          <p style={{ opacity: 0.7, fontSize: '13px', marginTop: '10px' }}>
            No files uploaded yet
          </p>
        ) : (
          uploadedFiles.map(file => (
            <div key={file.id} className="file-item">
              <div className="file-item-name"><FaFile /> {file.name}</div>
              <div className="file-item-time">{formatTime(file.uploadedAt)}</div>
            </div>
          ))
        )}
      </div>

      <div className="sidebar-footer">
        <button className="clear-btn" onClick={onClearChat}>
          <FaTrash /> Clear Chat
        </button>
      </div>
    </div>
  )
}
