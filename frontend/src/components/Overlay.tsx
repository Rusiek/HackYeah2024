import React, { useContext, useRef, useState } from 'react';
import { LuLayers } from "react-icons/lu";
import { TbRoad } from "react-icons/tb";
import { PiRoadHorizon } from "react-icons/pi";
import { PiRoadHorizonFill } from "react-icons/pi";
import { MainContext } from '../context/MainContext';

const Overlay = () => {
  const { settings: {
    setSelectedOption, coordinatePickingState, setCoordinatePickingState, startPosition, endPosition
  } } = useContext(MainContext);

  return (
    <div className="overlay">

      <div className="group">
        <span className="label">Punkt początkowy</span>
        <div className="field" onClick={() => {
          setCoordinatePickingState(1)
        }}>
          {coordinatePickingState == 1 ? <div>Wybierz punkt na mapie...</div> : <div>
            {startPosition
              ? <div>{startPosition?.[0].toFixed(5)}, {startPosition?.[1].toFixed(5)}</div>
              : <div><b>KLIKNIJ</b> aby wybrać</div>}
          </div>}
        </div>
      </div>
      <div className="group">
        <span className="label">Punkt końcowy</span>
        <div className="field" onClick={() => {
          setCoordinatePickingState(2)
        }}>
          {coordinatePickingState == 2 ? <div>Wybierz punkt na mapie...</div> : <div>
            {endPosition
              ? <div>{endPosition?.[0].toFixed(5)}, {endPosition?.[1].toFixed(5)}</div>
              : <div><b>KLIKNIJ</b> aby wybrać</div>}
          </div>}
        </div>
      </div>
      <div className="buttons">
        <button onClick={() => setSelectedOption(0)}>
          <LuLayers />
          <span>Wszystkie ścieżki</span>
        </button>
        <button onClick={() => setSelectedOption(1)}>
          <TbRoad />
          <span>Trasa - Wariant <b>A</b></span>
        </button>
        <button onClick={() => setSelectedOption(2)}>
          <PiRoadHorizon />
          <span>Trasa - Wariant <b>B</b></span>
        </button>
        <button onClick={() => setSelectedOption(3)}>
          <PiRoadHorizonFill />
          <span>Trasa - Wariant <b>C</b></span>
        </button>
      </div>
    </div>
  );
};

export default Overlay;