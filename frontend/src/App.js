import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import DataTable from 'react-data-table-component';


function App() {

  const [data, setData] = useState([]);



  useEffect(() => {
    
    const fetchData = async () => {
      const response = await fetch('http://127.0.0.1:8000/scrapApi/');
      const json = await response.json();
      setData(json);
    };

    const intervalId = setInterval(fetchData, 3000);

    return () => clearInterval(intervalId);
  }, []);


  const columns = [
    {
      name: 'Name',
      selector: row => row.name,
    },
    {
      name: 'Price',
      selector: row => row.price,
    },
    {
      name: 'percent_1h',
      selector: row => row.percent_1h,
    }, {
      name: 'percent_24h',
      selector: row => row.percent_24h,
    }, {
      name: 'percent_7d',
      selector: row => row.percent_7d,
    }, {
      name: 'market_cap',
      selector: row => row.market_cap,
    },
    {
      name: 'volume_24h',
      selector: row => row.volume_24h,
    }, {
      name: 'circulating_supply',
      selector: row => row.circulating_supply,
    },
  ];



  return (
    <div className="App">
      <header style={{
        background:"grey"}}>
        <h1>Scrapped Data</h1>
      </header>
      <DataTable
        columns={columns}
        data={data}
      />
    </div>
  );
}

export default App;
