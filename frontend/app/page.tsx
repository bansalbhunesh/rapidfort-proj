"use client";

import { useState } from "react";
import axios from "axios";
import { Button, Typography, Box } from "@mui/material";

export default function Home() {
  interface Metadata {
    name: string;
    size: number;
    type: string;
    lastModified: string;
    path: string;
  }

  const [file, setFile] = useState<File | null>(null);
  const [metadata, setMetadata] = useState<Metadata | null>(null);

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return; // Handle the case where no file is selected
    setFile(file);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:4003/upload", formData);
      setMetadata(response.data.metadata);
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };

  const handleConvert = async () => {
    if (!file || !metadata) {
      console.error("No file or metadata to convert");
      return;
    }

    try {
      const response = await axios.post(
        "http://localhost:4003/convert",
        { filePath: metadata.path },
        { responseType: "blob" } // Ensure the response is treated as binary
      );

      // Create a link to download the file
      const url = window.URL.createObjectURL(new Blob([response.data], { type: "application/pdf" }));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "converted.pdf");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (error) {
      console.error("Error converting file:", error);
    }
  };

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        DOCX to PDF Converter
      </Typography>
      <input type="file" accept=".docx" onChange={handleFileUpload} />
      {metadata && (
        <Box sx={{ my: 2 }}>
          <Typography variant="h6">File Metadata:</Typography>
          <pre>{JSON.stringify(metadata, null, 2)}</pre>
        </Box>
      )}
      <Button variant="contained" onClick={handleConvert} disabled={!file}>
        Convert to PDF
      </Button>
    </Box>
  );
}
