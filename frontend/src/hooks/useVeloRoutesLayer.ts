import React, { useContext, useEffect, useState } from 'react';
import { MainContext } from '../context/MainContext';
import { TripsLayer } from '@deck.gl/geo-layers';

const useVeloRoutesLayer = () => {
  const { settings: { selectedOption }, data: { veloPaths } } = useContext(MainContext)

  if (selectedOption?.[4] != 1 ) return null;

  const theme = {
    trailColor: [255, 255, 255]
  };

  return new TripsLayer<Trip>({
    id: 'velo paths',
    data: veloPaths,
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

export default useVeloRoutesLayer;