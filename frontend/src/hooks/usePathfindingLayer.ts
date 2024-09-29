import React, { useContext } from 'react';
import { MainContext } from '../context/MainContext';
import { TripsLayer } from '@deck.gl/geo-layers';

const usePathfindingLayer = () => {
  const { settings: { startPosition, endPosition }, data: { singlePath } } = useContext(MainContext)

  const theme = {
    trailColor: [255, 255, 255]
  };

  if (!startPosition || !endPosition) return null

  return new TripsLayer<Trip>({
    id: 'pathfinding',
    data: [singlePath],
    getPath: d => d.path,
    getTimestamps: d => d.timestamps,
    getColor: d => theme.trailColor,
    opacity: 1,
    widthMinPixels: 3,
    rounded: true,
    fadeTrail: false,
    currentTime: Infinity,
    shadowEnabled: false
  })
};

export default usePathfindingLayer;