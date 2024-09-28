import React, { useContext, useEffect, useState } from 'react';
import { MainContext } from '../context/MainContext';
import { getWeather } from '../services/PathsService';

const Weather = () => {
  const { settings: {
    endPosition
  } } = useContext(MainContext);

  const [temp, setTemp] = useState(0)

  useEffect(() => {
    if (endPosition) {
      getWeather(endPosition[1], endPosition[0])
        .then((data) => {
          setTemp(data?.hourly?.temperature_2m?.[0])
        })
    }
  }, [endPosition])

  if (!endPosition) return <></>

  return (
    <div className="tab weather">
      <div className="box">
        <img src="/images/sunwindy.png" />
        <div className="divider"></div>
        <div className="content">
          <div className="title">Pogoda w punkcie docelowym</div>
          <div className="temp">
            {temp}&deg; C
          </div>
          <div className="description">
            Słonecznie
          </div>
        </div>
      </div>
    </div>
  );
};

export default Weather;