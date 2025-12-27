import express from "express"
import cors from "cors"
import "./db.js"
import upload from "./gateway-node/src/routes/upload.js"
import chat from "./gateway-node/src/routes/chat.js"
import history from "./gateway-node/src/routes/history.js"

const app=express()

app.use(cors())
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.use("/upload",upload)
app.use("/chat",chat)
app.use("/history",history)

app.listen(8080,()=>{
    console.log("Server is running on port 8080")
})