import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

function getResidentsReport(callback) {
  return fetch('http://localhost:8000/residents/report/')
    .then(response => response.json())
    .then(data => callback(data));
}

function getSyncDB(callback) {
  return fetch('http://localhost:8000/residents/sync/')
    .then(response => response.json())
    .then(data => callback(data));
}

function getClearDB(callback) {
  return fetch('http://localhost:8000/residents/clear/')
    .then(response => response.json())
    .then(data => callback(data));
}

function getGenderEmoji(gender) {
  if (gender === 'female') {
    return '👩';
  }
  else if (gender === 'male') {
    return '👨';
  }
  return '👤';
}

function Character({ data }) {
  return (<div className="App-planet-character">
    <h3>{getGenderEmoji(data.gender)} {data.name}</h3>
    {/* <span>Gender: {data.gender}</span> */}
  </div>);
}

function PlanetResidents({ planet }) {
  return (<div>
    <h1>🪐 {planet.name}</h1>
    <div>Gravity: <span className="App-planet-detail">{planet.gravity}</span></div>
    <div>Climate: <span className="App-planet-detail">{planet.climate}</span></div>
    <h2>Characters</h2>
    <div className="App-planet-characters">
      {planet.characters?.map((character) => <Character data={character} />)}
    </div>
  </div>);
}

function App() {
  const [residents, setResidents] = useState();
  useEffect(() => {
    getResidentsReport((data) => {
      console.log(JSON.stringify(data))
      setResidents(data);
    });
  }, []);

  function reload() {
    getResidentsReport((data) => {
      setResidents(data);
    });
  }

  return (
    <div className="App">
      <div>
        <button onClick={() => {
          getSyncDB((data) => {
            if (data && data.status === 'success') {
              alert(`Planets created: ${data.planets_created}, characters created: ${data.characters_created}`)
            }
          })
        }} className="App-button">
          Sync data to DB
        </button>
        <button onClick={() => {
          getClearDB((data) => {
            if (data && data.status === 'success') {
              alert(`Planets deleted: ${data.planets_deleted}, characters deleted: ${data.characters_deleted}`)
            }
          })
        }} className="App-button">
          Clear DB
        </button>
        <button onClick={reload} className="App-button">
          Reload data
        </button>
      </div>
      <div></div>
      <header className="App-main">
        <p>
          {(residents && residents.planets?.length > 0) ? residents?.planets?.map((planet) => {
            return <PlanetResidents planet={planet} />
          }) : <h2>No data available</h2>}
        </p>
      </header>
    </div>
  );
}

export default App;
