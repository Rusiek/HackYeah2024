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

export const getAccidents = () => {
  return axios.get(`${API_BASE_URL}/accidents/`)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching paths:', error);
      throw error;
    });
};

/*
  [
    {
      ID: string,
      comune: string,
      district: string,
      lat: string,
      long: string,
      location: string,
      voivodeship: string,
      weight: string (C/L/S - Ciezki Lekki Smiertelny)
    }, itd..
  ]
*/
