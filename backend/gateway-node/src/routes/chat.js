import express from "express";
import axios from "axios";
import mongoose from "mongoose";
import Chat from "../models/Chat.js";

const router = express.Router();

router.post("/", async (req, res) => {
  try {
    const { userId, message, grade } = req.body;

    let aiResponseText = "";
    
    try {
      const ai = await axios.post("http://localhost:8001/ask", {
        question: message,
        grade
      });
      
      const { answer, citations } = ai.data;
      
      aiResponseText = answer;
      
      if (citations && citations.length > 0) {
          aiResponseText += "\n\n**Sources:**\n" + citations.map(c => `- ${c}`).join("\n");
      }
      
    } catch (error) {
      console.log("AI service error:", error.message);
      if (error.code === 'ECONNREFUSED') {
          aiResponseText = "⚠️ **System Unavailable**: The AI service is currently offline. Please try again later.";
      } else {
          aiResponseText = "⚠️ **Error**: " + (error.response?.data?.message || "Something went wrong processing your request.");
      }
    }

    // Check if mongoose is connected
    if (mongoose.connection.readyState !== 1) {
      console.log('MongoDB not connected, skipping database save');
      return res.json({ answer: aiResponseText });
    }

    // Save to History
    try {
        const chat = await Chat.findOneAndUpdate(
          { userId },
          { $push: { messages: [{ role: "user", content: message }, { role: "assistant", content: aiResponseText }] } },
          { upsert: true, new: true, maxTimeMS: 5000 }
        );
    } catch(dbErr) {
        console.error("Failed to save chat history:", dbErr.message);
        // Don't fail the request just because DB save failed
    }

    res.json({ answer: aiResponseText });
  } catch (error) {
    console.error("Chat error:", error);
    res.status(500).json({ error: "Failed to process chat message" });
  }
});

export default router;