import { useState } from "react"
import api from "../services/api"
import Message from "./Message"

export default function Chat(){
    const [messages,setMessages] = useState([]);
    const [input,setInput] = useState("");
    const [userId] = useState("user123"); // Default user ID
    const [grade] = useState("10"); // Default grade

const send = async()=>{
    if(!input.trim()) return;

    const userMsg={role:"user",content:input}
    setMessages(prev=>[...prev,userMsg])

    try {
        const res=await api.post("/chat",{
            userId,
            grade,
            message:input
        })
        setMessages(prev=>[...prev,{role:"assistant",content:res.data.answer}])
    } catch (error) {
        setMessages(prev=>[...prev,{role:"assistant",content:"Sorry, I encountered an error. Please try again."}])
    }
    setInput("")
}

    return(
        <div className="flex flex-col h-screen">
            <div className="flex-1 overflow-y-auto px-6 py-4">
                {messages.map((m,i)=>(
                    <Message key={i} role={m.role} content={m.content}/> 
                    ))}
            </div>

            <div className="border-t bg-white px-4 py-3">
                <input className="w-full rounded-xl border px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary" placeholder="Ask the NCERT doubt" value={input} onChange={(e)=>setInput(e.target.value)} onKeyDown={(e)=> e.key==="Enter" && send()}/>
            </div>
        </div>
    )
}