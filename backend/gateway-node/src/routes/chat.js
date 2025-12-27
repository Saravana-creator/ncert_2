import express from "express";
import axios from "axios";
import mongoose from "mongoose";
import Chat from "../models/Chat.js";

const router = express.Router();

router.post("/", async (req, res) => {
  try {
    const { userId, message, grade } = req.body;

    let aiResponse;
    try {
      const ai = await axios.post("http://localhost:8001/ask", {
        question: message,
        grade
      });
      aiResponse = ai.data.answer;
    } catch (error) {
      console.log("AI service not available:", error.message);
      aiResponse = "Sorry, the AI service is currently unavailable. Please try again later.";
    }

    // Check if mongoose is connected
    if (mongoose.connection.readyState !== 1) {
      console.log('MongoDB not connected, skipping database save');
      return res.json({ answer: aiResponse });
    }

    const chat = await Chat.findOneAndUpdate(
      { userId },
      { $push: { messages: [{ role: "user", content: message }, { role: "assistant", content: aiResponse }] } },
      { upsert: true, new: true, maxTimeMS: 5000 }
    );

    res.json({ answer: aiResponse });
  } catch (error) {
    console.error("Chat error:", error);
    res.status(500).json({ error: "Failed to process chat message" });
  }
});

export default router;