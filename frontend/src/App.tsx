import { useContext, useRef, useState, useEffect } from 'react'
import './styles/index.scss'

import DeckGL from '@deck.gl/react';
import InteractiveMap from 'react-map-gl';
import { OBJLoader } from '@loaders.gl/obj';
import { registerLoaders } from '@loaders.gl/core';
import { INITIAL_VIEW_STATE } from './utils/MapUtils';
import { MainContext } from './context/MainContext';
import Overlay from './components/Overlay';
import useTripsLayer from './hooks/useTripsLayer';
import useAccidentsLayer from './hooks/useAccidentsLayer';
import useMarkersLayer from './hooks/useMarkersLayer';
import Gpx from './components/Gpx';

registerLoaders([OBJLoader]);

const App = () => {
  const mapRef: any = useRef();

  const {
    map: {
      mapViewState, setMapViewState
    },
    settings: {
      coordinatePickingState, setCoordinatePickingState, setStartPosition, setEndPosition
    } } = useContext(MainContext);

  const tripsLayer = useTripsLayer()
  const accidentsLayer = useAccidentsLayer()
  const markersLayer = useMarkersLayer()

  const layers = [
    tripsLayer,
    accidentsLayer,
    markersLayer
  ];

  return (
    <div>
      <Overlay />
      <Gpx />
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
