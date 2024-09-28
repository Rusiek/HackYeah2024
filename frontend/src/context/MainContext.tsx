import { createContext, ReactNode, useEffect, useState } from "react"
import { MapViewState } from 'deck.gl';
import { INITIAL_VIEW_STATE } from "../utils/MapUtils";
import { getPaths } from "../services/PathsService";

type MapType = {
  mapViewState: MapViewState;
  setMapViewState: any;
}

type DataType = {
  paths: any;
}

type MainContextType = {
  map: MapType;
  data: DataType;
}

export const MainContext = createContext<MainContextType>({
  map: {
    mapViewState: INITIAL_VIEW_STATE,
    setMapViewState: () => { }
  },
  data: {
    paths: []
  }
})

export const MainContextProvider = ({ children }: {
  children: ReactNode
}) => {
  const [mapViewState, setMapViewState] = useState<MapViewState>(INITIAL_VIEW_STATE)
  const [paths, setPaths] = useState([])

  useEffect(() => {
    getPaths()
      .then((data) => {
        setPaths(data.paths.map((path, index) => ({
          vendor: index,
          path: path
        })))
      })
  }, [])

  return <MainContext.Provider value={{
    map: {
      mapViewState,
      setMapViewState,
    },
    data: {
      paths
    }
  }}>
    {children}
  </MainContext.Provider>
}