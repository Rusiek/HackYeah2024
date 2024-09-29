import { useContext } from "react";
import { MainContext } from '../context/MainContext';

const FailedLoadTooltip = () => {

  const { settings: {
    failedLoad
  } } = useContext(MainContext);



  return ( 
    <div className={`tab failed-tooltip tooltip ${failedLoad > 0 ? 'toggle-visible' : 'toggle-hidden'}`}>
      Could not determine path!
    </div>
  );
}
 
export default FailedLoadTooltip;