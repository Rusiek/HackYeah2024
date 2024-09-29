import React, { useContext, useEffect, useState } from 'react';
import { MainContext } from '../context/MainContext';
import { TripsLayer } from '@deck.gl/geo-layers';
import { getShortestPath } from '../services/PathsService';

const usePathfindingLayer = () => {
  const { settings: { startPosition, endPosition, selectedOption, setSinglePath }, data: { singlePath } } = useContext(MainContext)

  const theme = {
    trailColor: [255, 255, 255]
  };

  useEffect(() => {
    if (startPosition != null && endPosition != null) {
      getShortestPath(startPosition, endPosition, selectedOption?.[2] == 1 ? true : false, selectedOption?.[4] == 1 ? true : false)
      .then(response => {
        console.log(response)
      })
    }
  }, [startPosition, endPosition, selectedOption])

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