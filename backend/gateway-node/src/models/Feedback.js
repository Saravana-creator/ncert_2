import mongoose from "mongoose"

export default mongoose.model("Feedback",new mongoose.Schema({
    userId:String,
    rating:Number,
    comment:String,
    timestamp:{type:Date,default:Date.now}
}));