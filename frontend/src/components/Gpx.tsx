import React from 'react';
import { BiExport } from "react-icons/bi";

const Gpx = () => {
  return (
    <div className="export">
      <BiExport />
      <div className="label">Export do <b>GPX</b></div>
    </div>
  );
};

export default Gpx;