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

export const getPath = () => {
  return axios.get(`${API_BASE_URL}/paths/1`)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching paths:', error);
      throw error;
    });
};
