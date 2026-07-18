import { useState } from "react";

function UploadBox() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [fileName, setFileName] = useState("");

  const uploadFile = async () => {
    if (!file) {
      alert("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      setMessage(data.message || "Upload completed!");
      setFile(null);
    } catch (err) {
      setMessage("Upload failed.");
    }
  };

  return (
    <div className="upload-box">

      <h2>📤 Upload Learning Material</h2>

      <input
        type="file"
        onChange={(e)=>{
          setFile(e.target.files[0]);
          setFileName(e.target.files[0].name);
        }}
      />

      <button onClick={uploadFile}>
        Upload
      </button>

      {message && (
        <p>{message}</p>
      )}

    </div>
  );
}

export default UploadBox;