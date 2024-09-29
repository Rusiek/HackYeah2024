import React, { useContext } from 'react';
import { MainContext } from '../context/MainContext';
import { TripsLayer } from '@deck.gl/geo-layers';

const useTripsLayer = () => {
  const { settings: { selectedOption }, data: { paths } } = useContext(MainContext)

  if (!selectedOption?.[0]) return null

  const theme = {
    trailColor: [230, 210, 0]
  };

  return new TripsLayer<Trip>({
    id: 'trips',
    data: paths,
    getPath: d => d.path,
    getTimestamps: d => d.timestamps,
    getColor: d => d.vendor == 'lo' ? [0, 255, 0] : d.vendor == 'mid' ? [255, 128, 0] : [255, 0, 0],
    opacity: 0.3,
    widthMinPixels: 2,
    rounded: true,
    fadeTrail: false,
    currentTime: Infinity,
    shadowEnabled: false
  })
};

export default useTripsLayer;