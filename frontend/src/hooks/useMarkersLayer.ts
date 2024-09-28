import React, { useContext } from 'react';
import { IconLayer } from '@deck.gl/layers';
import { MainContext } from '../context/MainContext';

const useMarkersLayer = () => {
  const { settings: {
    startPosition, endPosition
  } } = useContext(MainContext);

  const data = []

  if (startPosition) {
    data.push(
      {
        coordinates: startPosition,
        color: [3, 110, 135]
      }
    )
  }

  if (endPosition) {
    data.push(
      {
        coordinates: endPosition,
        color: [14, 200, 207]
      }
    )
  }

  return new IconLayer<any>({
    id: 'IconLayer',
    data: data,
    getColor: (d: any) => d.color,
    getIcon: (d: any) => 'marker',
    getPosition: (d: any) => d.coordinates,
    getSize: 40,
    iconAtlas: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.png',
    iconMapping: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.json',
    pickable: true
  });
};

export default useMarkersLayer;