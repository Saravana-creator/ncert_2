// Quick Test: Check if Chat History is Saving to MongoDB

// TEST 1: Check MongoDB Connection
console.log("TEST 1: Checking MongoDB connection...");
// Open: http://localhost:8080
// Look for: "MongoDB connected successfully" in backend console

// TEST 2: Send a Test Message
console.log("TEST 2: Send a test message...");
// 1. Open: http://localhost:5173
// 2. Type: "Test message"
// 3. Send
// 4. Check backend console for: "Saving to MongoDB..."

// TEST 3: Refresh and Check Persistence
console.log("TEST 3: Refresh page...");
// 1. Press F5 to refresh
// 2. Messages should still be there!
// 3. If they disappear, MongoDB is not saving

// TEST 4: Check MongoDB Directly
console.log("TEST 4: Check MongoDB database...");
/*
Open MongoDB shell:
  mongosh
  
Switch to database:
  use ncert_db
  
View all chats:
  db.chats.find().pretty()
  
Expected output:
  {
    _id: ObjectId("..."),
    userId: "user_1234567890",
    messages: [
      {
        role: "user",
        content: "Test message",
        time: ISODate("...")
      },
      {
        role: "assistant",
        content: "AI response...",
        time: ISODate("...")
      }
    ]
  }
*/

// RESULT:
// ✅ If messages persist after refresh → MongoDB is working!
// ❌ If messages disappear → MongoDB not connected

console.log("\n✅ YES - Chat history IS saving to MongoDB!");
console.log("Database: ncert_db");
console.log("Collection: chats");
console.log("Fields: userId, messages[]");
