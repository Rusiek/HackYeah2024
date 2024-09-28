import { useContext, useRef, useState, useEffect } from 'react'
import './styles/index.scss'

import DeckGL from '@deck.gl/react';
import InteractiveMap from 'react-map-gl';
import { OBJLoader } from '@loaders.gl/obj';
import { registerLoaders } from '@loaders.gl/core';
import { INITIAL_VIEW_STATE } from './utils/MapUtils';
import { MainContext } from './context/MainContext';
import { TripsLayer } from '@deck.gl/geo-layers';
import { animate } from 'popmotion';
import Overlay from './components/Overlay';

registerLoaders([OBJLoader]);

const App = () => {
  const mapRef: any = useRef();

  const {
    map: {
      mapViewState, setMapViewState
    },
    data: {
      paths
    },
    settings: {
      coordinatePickingState, setCoordinatePickingState, setStartPosition, setEndPosition
    } } = useContext(MainContext);

  const theme = {
    buildingColor: [74, 80, 87],
    trailColor0: [255, 0, 0],
    trailColor1: [0, 255, 0],
    material: {
      ambient: 0.1,
      diffuse: 0.6,
      shininess: 32,
      specularColor: [60, 64, 70]
    },
  };

  const layers = [
    new TripsLayer<Trip>({
      id: 'trips',
      data: paths,
      getPath: d => d.path,
      getTimestamps: d => d.timestamps,
      getColor: d => (d.vendor === 0 ? theme.trailColor0 : theme.trailColor1),
      opacity: 0.3,
      widthMinPixels: 2,
      rounded: true,
      fadeTrail: false,
      currentTime: Infinity,
      shadowEnabled: false
    })
  ];

  return (
    <div>
      <Overlay />
      <DeckGL
        layers={layers}
        initialViewState={INITIAL_VIEW_STATE}
        controller={true}
        pickingRadius={5}
        viewState={mapViewState}
        onViewStateChange={(newMapViewState) => {
          setMapViewState(newMapViewState.viewState)
        }}
        onClick={(e) => {
          const coord = e?.coordinate || null;

          if (coordinatePickingState === 1) {
            setCoordinatePickingState(0)
            setStartPosition(coord)
          }
          if (coordinatePickingState === 2) {
            setCoordinatePickingState(0)
            setEndPosition(coord)
          }
        }}
      >
        <InteractiveMap
          reuseMaps={true}
          ref={mapRef}
          onLoad={() => {
            console.log("Map loaded")
          }}
          maxPitch={85}
          //mapStyle={MAP_STYLE}
          mapStyle={"mapbox://styles/mapbox/dark-v11"}
          mapboxAccessToken={import.meta.env.VITE_MAP_KEY}
        >
        </InteractiveMap>
      </DeckGL>
    </div>
  )
}

export default App
