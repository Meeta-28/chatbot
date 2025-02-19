import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:5000',  // Pointing to your Flask server
});

export default axiosInstance;
