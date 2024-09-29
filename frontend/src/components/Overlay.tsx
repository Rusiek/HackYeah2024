import React, { useContext, useRef, useState } from 'react';
import { AiOutlineSafety } from "react-icons/ai";
import { FaCarCrash } from "react-icons/fa";
import { MdDirectionsBike } from "react-icons/md";
import { FaRoad } from "react-icons/fa";
import { MainContext } from '../context/MainContext';
import { IoLocationSharp } from "react-icons/io5";
import Weather from './Weather';
import { IoClose } from "react-icons/io5";
import { FaMapLocation } from "react-icons/fa6";

const Overlay = () => {
  const { settings: {
    coordinatePickingState, setCoordinatePickingState, startPosition, endPosition,
    setStartPosition, setEndPosition, setRoadSafetyEnabled, setShowVeloMaps, setShowAccidents, setAvoidDangerous, setPreferVelo,
  }, data: { 
    roadSafetyEnabled,
    showVeloMaps,
    showAccidents,
    avoidDangerous,
    preferVelo
  } } = useContext(MainContext);

  return (
    <div className="overlay">
      <div className="tab">
        <div className="group">
          <span className="label labelStart"><IoLocationSharp /> Punkt początkowy</span>
          <div className="field" onClick={() => {
            setCoordinatePickingState(1)
          }}>
            <div>
              {coordinatePickingState == 1 ? <div>Wybierz punkt na mapie...</div> : <div>
                {startPosition
                  ? <div>{startPosition?.[0].toFixed(5)}, {startPosition?.[1].toFixed(5)}</div>
                  : <div><b>KLIKNIJ</b> aby wybrać</div>}
              </div>}
            </div>
            <div className="closeIcon" onClick={() => {
              setStartPosition(null)
            }}><IoClose /></div>
          </div>
        </div>
        <div className="group">
          <span className="label labelEnd"><IoLocationSharp /> Punkt docelowy</span>
          <div className="field" onClick={() => {
            setCoordinatePickingState(2)
          }}>
            <div>
              {coordinatePickingState == 2 ? <div>Wybierz punkt na mapie...</div> : <div>
                {endPosition
                  ? <div>{endPosition?.[0].toFixed(5)}, {endPosition?.[1].toFixed(5)}</div>
                  : <div><b>KLIKNIJ</b> aby wybrać</div>}
              </div>}
            </div>
            <div className="closeIcon" onClick={() => {
              setEndPosition(null)
            }}><IoClose /></div>
          </div>
        </div>
        <div className="buttons">
          <button onClick={() => setRoadSafetyEnabled(!roadSafetyEnabled)} className={`${roadSafetyEnabled && "active"}`} style={{
            width: 'calc(100% - 20px)'
          }}>
            <AiOutlineSafety />
            <span>Bezpieczeństwo tras</span>
          </button>
          <button onClick={() => setShowAccidents(!showAccidents)} className={`${showAccidents && "active"}`}>
            <FaCarCrash />
            <span>Wypadki z udziałem rowerów</span>
          </button>
          <button onClick={() => setAvoidDangerous(!avoidDangerous)} className={`${avoidDangerous && "active"}`}>
            <FaRoad />
            <span>Unikaj niebezpiecznych tras</span>
          </button>
          <button onClick={() => setShowVeloMaps(!showVeloMaps)} className={`${showVeloMaps && "active"}`}>
            <FaMapLocation />
            <span>Wyświetl ścieżki <b>VELO</b></span>
          </button>
          <button onClick={() => setPreferVelo(!preferVelo)} className={`${preferVelo && "active"}`}>
            <MdDirectionsBike />
            <span>Preferuj ścieżki <b>VELO</b></span>
          </button>
        </div>
      </div>
      <Weather />
    </div>
  );
};

export default Overlay;