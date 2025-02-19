import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
  const [question, setQuestion] = useState('');
  const [file, setFile] = useState(null);
  const [answer, setAnswer] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('question', question);
    if (file) {
      formData.append('file', file);
    }

    try {
      const response = await axios.post('http://127.0.0.1:5000/ask-question', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error:', error);
      setAnswer("Error getting answer.");
    }
  };

  return (
    <div>
      <h2>Upload PDF & Ask a Question</h2>
      <input
        type="file"
        onChange={handleFileChange}
        accept=".pdf,.jpg,.png"
      />
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Enter your question"
      />
      <button onClick={handleSubmit}>Ask</button>

      {answer && (
        <div>
          <h3>Chatbot Answer:</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
};

export default Chatbot;

