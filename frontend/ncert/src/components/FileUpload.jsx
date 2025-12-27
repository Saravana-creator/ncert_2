import api from "../services/api"

export default function FileUpload(){
    const upload = async(e)=>{
        const file=e.target.files[0];
        if(!file) return;

        const form =new FormData();
        form.append("file",file);
        await api.post("/upload",form)
        alert("File uploaded successfully")
    };

    return(
        <div className="border-b bg-white px-6 py-4 flex items-center justify-between">
            <h1 className="text-lg font-semibold">NCERT doubt solver</h1>
            <label className="cursor-pointer text-sm text-primary font-medium">Upload NCERT
                <input type="file" className="hidden" onChange={upload}/>
            </label>
        </div>
    )
}