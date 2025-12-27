import express from "express";
import Chat from "../models/Chat.js";

const router = express.Router();

router.get("/:userId", async (req, res) => {
  try {
    const { userId } = req.params;
    const chat = await Chat.findOne({ userId });
    
    if (!chat) {
      return res.json({ messages: [] });
    }
    
    res.json({ messages: chat.messages });
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch chat history" });
  }
});

export default router;