import React, { useContext, useEffect, useState } from 'react';
import { MainContext } from '../context/MainContext';
import { TripsLayer } from '@deck.gl/geo-layers';
import { getShortestPath } from '../services/PathsService';

const usePathfindingLayer = () => {
  const { settings: { startPosition, endPosition, setSinglePath, setFailedLoad, failedLoad }, data: { singlePath, avoidDangerous, preferVelo } } = useContext(MainContext)


  const theme = {
    trailColor: [255, 255, 255]
  };

  const _setFailedLoad = () => {
    if(failedLoad > 0) clearTimeout(failedLoad)
    const timeoutId = setTimeout(() => {
      setFailedLoad(-1)
    }, 3000)
    setFailedLoad(timeoutId)
  }

  useEffect(() => {
    if (startPosition != null && endPosition != null) {
      getShortestPath(startPosition, endPosition, avoidDangerous, preferVelo)
      .then(response => {
        setSinglePath(response.map((path, index) => ({
          vendor: path.risk,
          path: path.path,
        })))
      })
      .catch((reason) => {
        console.log('Could not determine path')
        _setFailedLoad()
      })
    }
  }, [startPosition, endPosition, avoidDangerous, preferVelo])

  if (!startPosition || !endPosition) return null

  return new TripsLayer<Trip>({
    id: 'pathfinding',
    data: singlePath,
    getPath: d => d.path,
    getTimestamps: d => d.timestamps,
    getColor: d => d.vendor == 'lo' ? [0, 255, 0] : d.vendor == 'mid' ? [255, 128, 0] : [255, 0, 0],
    opacity: 1,
    widthMinPixels: 6,
    rounded: true,
    fadeTrail: false,
    currentTime: Infinity,
    shadowEnabled: false
  })
};

export default usePathfindingLayer;