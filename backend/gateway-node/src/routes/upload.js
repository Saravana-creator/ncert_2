import express from "express"
import multer from "multer"
import axios from "axios"
import path from "path"
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

const router=express.Router()

// Configure multer to preserve file extensions
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, path.join(__dirname, "../../uploads"))
  },
  filename: function (req, file, cb) {
    // Keep original extension
    const ext = path.extname(file.originalname)
    cb(null, file.fieldname + '-' + Date.now() + ext)
  }
})

const upload = multer({ storage: storage })

router.post("/",upload.single("file"),async(req,res)=>{
    try {
        const absolutePath = path.resolve(req.file.path)
        console.log(`Uploading file: ${absolutePath}`)
        
        await axios.post("http://localhost:8001/ingest",{
            path: absolutePath
        });
        res.json({status:"ok", message:"File uploaded and processed successfully"})
    } catch (error) {
        console.log("AI service not available, file uploaded but not processed:", error.message);
        res.json({status:"ok", message:"File uploaded successfully (AI service offline)"})
    }
})

export default router;