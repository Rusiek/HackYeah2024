import React from 'react';
import { BiExport } from "react-icons/bi";
import { getGpx } from '../services/PathsService';
import { useContext } from 'react';
import { MainContext } from '../context/MainContext';



const Gpx = () => {

  const { data: {
    singlePath
  } } = useContext(MainContext);

  const handleClick = () => {
    getGpx(singlePath)
      .then(responce => {
        const blob = new Blob([responce],{type:'application/gpx+xml'});
        const a = document.createElement('a');
        const url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = 'route.gpx';
        a.click();
        window.URL.revokeObjectURL(url);
        a.remove();
      })
      .catch((error) => {
        console.error('Error downloading the GPX file:', error);
      });
  }

  console.log(singlePath)
  return (
    <div className={`export ${singlePath && singlePath.length > 0 ? '' : 'disabled'}`} onClick={handleClick}>
      <BiExport />
      {/* <div className="label">Export do <b>GPX</b></div> */}
    </div>
  );
};

export default Gpx;