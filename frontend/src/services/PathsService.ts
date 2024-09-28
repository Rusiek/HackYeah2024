import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

export const getPaths = () => {
  return axios.get(`${API_BASE_URL}/paths/`)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching paths:', error);
      throw error;
    });
};
