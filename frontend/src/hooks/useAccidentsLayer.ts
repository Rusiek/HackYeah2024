import React, { useContext, useMemo } from 'react';
import { MainContext } from '../context/MainContext';
import { HeatmapLayer } from '@deck.gl/aggregation-layers';

const useAccidentsLayer = () => {
  const { data: { accidents, showAccidents } } = useContext(MainContext)
  const mappedAccidents = useMemo(() => {
    return accidents.map((accident) => [+accident.long, +accident.lat, 1])
  }, [accidents])

  if (!showAccidents) return null

  return new HeatmapLayer<DataPoint>({
    data: mappedAccidents,
    id: 'heatmap-layer',
    getPosition: d => [d[0], d[1]],
    getWeight: d => d[2],
    radiusPixels: 25,
    intensity: 0.8,
    threshold: 0.03,
    colorRange: [
      [200, 30, 10, 150],
      [150, 10, 5, 200],
      [100, 0, 0, 255],
    ],
    pickable: true,
    onClick: (d) => {
      console.log("heatmap clicked", d)
    }
  })
};

export default useAccidentsLayer;