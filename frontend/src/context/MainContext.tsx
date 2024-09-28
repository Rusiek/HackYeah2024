import { createContext, ReactNode, useState } from "react"
import { MapViewState } from 'deck.gl';
import { INITIAL_VIEW_STATE } from "../utils/MapUtils";

type MapType = {
  mapViewState: MapViewState;
  setMapViewState: any;
}

type MainContextType = {
  map: MapType
}

export const MainContext = createContext<MainContextType>({
  map: {
    mapViewState: INITIAL_VIEW_STATE,
    setMapViewState: () => { }
  }
})

export const MainContextProvider = ({ children }: {
  children: ReactNode
}) => {
  const [mapViewState, setMapViewState] = useState<MapViewState>(INITIAL_VIEW_STATE)

  return <MainContext.Provider value={{
    map: {
      mapViewState,
      setMapViewState,
    }
  }}>
    {children}
  </MainContext.Provider>
}