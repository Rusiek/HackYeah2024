import { useState, useContext } from "react";
import { getLocation } from '../services/PathsService';
import { MainContext } from '../context/MainContext';
import { BiSearchAlt } from "react-icons/bi";


const Searchbar = () => {
  const [search, setSearch] = useState('')
  const [tooltipId, setTooltipId] = useState(-1)
  const [errorMessege, setErrorMessege] = useState('Nie znaleziono miejsca!')
  const [searchVisible, setSearchVisible] = useState(false)

  const { map: {
    setMapViewState
  } } = useContext(MainContext);



  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearch((e.target as HTMLInputElement).value)
  }

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    getLocation(search).then((data) => {
      if(!data.results) {
        setErrorMessege('Nie znaleziono miejsca!')
        toggleVisibility()
        return
      }
      const result = data.results[0]
      // Lesser Poland and adjacent voivodeships
      if(!['Lesser Poland', 'Silesia', 'Subcarpathia', 'Świętokrzyskie', 'Presov'].includes(result.admin1)){
        setErrorMessege('Poza obszarem!')
        toggleVisibility()
        setSearch(result.name)
        return
      }
      
      const {latitude, longitude} = result
      setSearch(result.name)
      setMapViewState({
        latitude: latitude,
        longitude: longitude,
        zoom: 13,
        maxZoom: 20,
        bearing: 0
      })
      
    }).catch(() => {
      setErrorMessege('Wystąpił błąd!')
      toggleVisibility()
    })
  }

  const toggleVisibility = () => {
    if(tooltipId > 1){
      clearTimeout(tooltipId)
    }
    const timeout = setTimeout(() => {
      setTooltipId(-1)
    }, 4000) 
    setTooltipId(timeout as unknown as number)
  }

  const handleClick = () => {
    setSearchVisible(prev => !prev)
  }

  return ( 
    <>
      <div className="export find" onClick={handleClick}>
        <BiSearchAlt />
      </div>
      <div style={{visibility: tooltipId > 1 ? 'visible' : 'hidden'}} className='tooltip tab'>
        {errorMessege}
      </div>
      <div className="searchbar tab" style={{visibility: searchVisible ? 'visible' : 'hidden'}}>
        <div className="box">
          <form action="None" onSubmit={handleSubmit}>
            <input className="field" type="text" value={search} onChange={(e) => handleChange(e)} />
          </form>
        </div>
      </div>
    </>
   );
}
 
export default Searchbar;