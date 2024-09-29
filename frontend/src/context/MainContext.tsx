import { createContext, ReactNode, useEffect, useState } from "react"
import { MapViewState } from 'deck.gl';
import { INITIAL_VIEW_STATE } from "../utils/MapUtils";
import { getAccidents, getPath, getPaths, getVeloPaths } from "../services/PathsService";

type MapType = {
  mapViewState: MapViewState;
  setMapViewState: any;
}

type DataType = {
  paths: any;
  singlePath: any;
  veloPaths: any;
  accidents: any;
  roadSafetyEnabled: boolean;
  showVeloMaps: boolean;
  showAccidents: boolean; 
  avoidDangerous: boolean;
  preferVelo: boolean;
}

type SettingsType = {
  selectedOption: number[];
  setSelectedOption: any;
  coordinatePickingState: number;
  setCoordinatePickingState: any;
  startPosition: number[] | null;
  endPosition: number[] | null;
  setStartPosition: any;
  setEndPosition: any;
  setSinglePath: any;
  failedLoad: number;
  setFailedLoad: any;
  setRoadSafetyEnabled: any;
  setShowVeloMaps: any;
  setShowAccidents: any;
  setAvoidDangerous: any;
  setPreferVelo: any;
}

type MainContextType = {
  map: MapType;
  data: DataType;
  settings: SettingsType;
}

export const MainContext = createContext<MainContextType>({
  map: {
    mapViewState: INITIAL_VIEW_STATE,
    setMapViewState: () => { }
  },
  data: {
    paths: [],
    singlePath: [],
    accidents: [],
    veloPaths: [],
    roadSafetyEnabled: false,
    showVeloMaps: false,
    showAccidents: false,
    avoidDangerous: false,
    preferVelo: false
  },
  settings: {
    selectedOption: [1, 0, 0, 0, 0],
    setSelectedOption: () => { },
    coordinatePickingState: 0,
    setCoordinatePickingState: () => { },
    startPosition: null,
    endPosition: null,
    setStartPosition: () => { },
    setEndPosition: () => { },
    setSinglePath: () => { },
    failedLoad: 0,
    setFailedLoad: () => { },
    setRoadSafetyEnabled: () => { },
    setShowVeloMaps: () => { },
    setShowAccidents: () => { },
    setAvoidDangerous: () => { },
    setPreferVelo: () => { }
  }
})

export const MainContextProvider = ({ children }: {
  children: ReactNode
}) => {
  const [mapViewState, setMapViewState] = useState<MapViewState>(INITIAL_VIEW_STATE)
  const [paths, setPaths] = useState([])
  const [singlePath, setSinglePath] = useState([])
  const [veloPaths, setVeloPaths] = useState([])
  const [accidents, setAccidents] = useState([])
  const [selectedOption, setSelectedOption] = useState([1, 0, 0, 0, 0])
  const [coordinatePickingState, setCoordinatePickingState] = useState(0)
  const [startPosition, setStartPosition] = useState<number[] | null>(null);
  const [endPosition, setEndPosition] = useState<number[] | null>(null);
  
  const [failedLoad, setFailedLoad] = useState<number>(-1);

  // buttons states
  const [roadSafetyEnabled, setRoadSafetyEnabled] = useState(false);
  const [showVeloMaps, setShowVeloMaps] = useState(false);
  const [showAccidents, setShowAccidents] = useState(false);
  const [avoidDangerous, setAvoidDangerous] = useState(false);
  const [preferVelo, setPreferVelo] = useState(false);

  useEffect(() => {
    getPaths()
      .then((data) => {
        setPaths(data.map((path, index) => ({
          vendor: path.risk,
          path: path.path,
        })))
      })

    // getPath()
    //   .then((data) => {
    //     setSinglePath({
    //       vendor: 1,
    //       path: data.path
    //     })
    //   })

    getVeloPaths()
      .then((data) => {
        setVeloPaths(data.paths.map((path, index) => ({
          vendor: index,
          path: path,
        })))
      })

    getAccidents()
      .then((data) => {
        setAccidents(data)
      })
  }, [])

  return <MainContext.Provider value={{
    map: {
      mapViewState,
      setMapViewState,
    },
    data: {
      paths,
      accidents,
      singlePath,
      veloPaths,
      roadSafetyEnabled,
      showVeloMaps,
      showAccidents,
      avoidDangerous,
      preferVelo
    },
    settings: {
      selectedOption,
      setSelectedOption,
      coordinatePickingState,
      setCoordinatePickingState,
      startPosition,
      endPosition,
      setStartPosition,
      setEndPosition,
      setSinglePath,
      failedLoad,
      setFailedLoad,
      setRoadSafetyEnabled,
      setShowVeloMaps,
      setShowAccidents,
      setAvoidDangerous,
      setPreferVelo
    }
  }}>
    {children}
  </MainContext.Provider>
}