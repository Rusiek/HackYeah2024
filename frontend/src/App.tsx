import { useContext, useRef, useState } from 'react'
import './styles/index.scss'

import DeckGL from '@deck.gl/react';
import Map from 'react-map-gl';
import { OBJLoader } from '@loaders.gl/obj';
import { registerLoaders } from '@loaders.gl/core';
import { INITIAL_VIEW_STATE } from './utils/MapUtils';
import { MainContext } from './context/MainContext';

registerLoaders([OBJLoader]);

const App = () => {
  const mapRef: any = useRef();

  const { map: {
    mapViewState, setMapViewState
  } } = useContext(MainContext);

  return (
    <div>
      aaa
      <DeckGL
        layers={[]}
        initialViewState={INITIAL_VIEW_STATE}
        controller={true}
        pickingRadius={5}
        viewState={mapViewState}
        onViewStateChange={(newMapViewState) => {
          setMapViewState(newMapViewState.viewState)
        }}
      >
        <Map
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
        </Map>
      </DeckGL>
    </div>
  )
}

export default App
