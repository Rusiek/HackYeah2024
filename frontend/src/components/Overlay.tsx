import React, { useContext, useRef, useState } from 'react';
import { LuLayers } from "react-icons/lu";
import { FaCarCrash } from "react-icons/fa";
import { PiRoadHorizon } from "react-icons/pi";
import { PiRoadHorizonFill } from "react-icons/pi";
import { MainContext } from '../context/MainContext';

const Overlay = () => {
  const { settings: {
    selectedOption, setSelectedOption, coordinatePickingState, setCoordinatePickingState, startPosition, endPosition
  } } = useContext(MainContext);

  const changeOption = (id) => {
    setSelectedOption(prev => {
      const newOption = [...prev]
      newOption[id] = (newOption[id] + 1) % 2
      return newOption
    })
  }

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
        <button onClick={() => changeOption(0)} className={`${selectedOption?.[0] == 1 && "active"}`}>
          <LuLayers />
          <span>Wszystkie ścieżki</span>
        </button>
        <button onClick={() => changeOption(1)} className={`${selectedOption?.[1] == 1 && "active"}`}>
          <FaCarCrash />
          <span>Wypadki drogowe</span>
        </button>
        <button onClick={() => changeOption(2)} className={`${selectedOption?.[2] == 1 && "active"}`}>
          <PiRoadHorizon />
          <span>Trasa - Wariant <b>B</b></span>
        </button>
        <button onClick={() => changeOption(3)} className={`${selectedOption?.[3] == 1 && "active"}`}>
          <PiRoadHorizonFill />
          <span>Trasa - Wariant <b>C</b></span>
        </button>
      </div>
    </div>
  );
};

export default Overlay;