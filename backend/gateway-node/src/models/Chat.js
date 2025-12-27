import mongoose from "mongoose"

export default mongoose.model("Chat",new mongoose.Schema({
    userId:String,
    messages:[{
        role:String,
        content:String,
        time:{type:Date,default:Date.now}
    }]
}));