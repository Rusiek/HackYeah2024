import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

const ROUTES_BASE_API_URL = 'http://localhost:5005';

export const getPaths = () => {
  return axios.get(`${ROUTES_BASE_API_URL}/get_edges`)
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

export const getWeather = (lat, long) => {
  return axios.get(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${long}&hourly=temperature_2m,weather_code&forecast_days=1`)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching paths:', error);
      throw error;
    });
}

export const getLocation = (location: string) => {
  return axios.get(`https://geocoding-api.open-meteo.com/v1/search?name=${location}&count=1&language=en&format=json`)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching location:', error);
      throw error;
    });
}

export const getShortestPath = (start, end, avoidUnsafe, preferVelo) => {
  return axios.post(`${ROUTES_BASE_API_URL}/get_data`, {
    start: start,
    end: end,
    avoidUnsafe: avoidUnsafe,
    preferVelo: preferVelo
  })
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching paths:', error);
      throw error;
    });
}

export const getGpx = (vertices, should_get_waypoints) => {
  return axios.post(`${ROUTES_BASE_API_URL}/gpx`, {
    vertices: vertices,
    should_get_waypoints: should_get_waypoints
  })
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching paths:', error);
      throw error;
    });
}