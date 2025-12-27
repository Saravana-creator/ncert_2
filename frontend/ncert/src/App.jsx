
import './App.css'
import SideBar from './components/SideBar'
import FileUpload from './components/FileUpload'
import Chat from './components/Chat'

function App() {
 
  return (
    <div className="flex h-screen">
      <SideBar />
        <div className="flex-1 flex flex-col">
        <FileUpload />
        <Chat />
      </div>
    </div>
  )
}

export default App
