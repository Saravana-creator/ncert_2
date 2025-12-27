export default function Message({role,content}){
    let isUser=role==="user";

    return(
        <div className={`flex mb-4 ${isUser ? "justify-end":"justify-start"}`}>
            <div className={`max-w-[70%] px-4 py-3 rounded-2xl text-sm leading-relaxed
                ${isUser ? "bg-primary text-white rounded-br-none" : "bg-white text-gray-800 shadow rounded-bl-none"}`}>{content}</div>
        </div>
    )
}