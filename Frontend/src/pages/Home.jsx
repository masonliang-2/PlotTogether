import { useState, useEffect } from "react";
//import DataInput from "../components/DataInput";
import GraphDisplay from "../components/GraphDisplay";
import AnalysisResults from "../components/AnalysisResults";
import EditableTable from "../components/EditableTable";
import { fetchDataPoints } from "../apiService";

const Home = () => {
  const [dataPoints, setDataPoints] = useState([]);

  const refreshDataPoints = async () => {
    try {
      const data = await fetchDataPoints();
      setDataPoints(data);
    } catch (error) {
      console.error("Error fetching data points:", error);
    }
  };

  useEffect(() => {
console.log("Data points:", dataPoints); // Log data points
    refreshDataPoints();
  }, []);

  return (
    <div className="home">

      <EditableTable dataPoints={dataPoints} refreshDataPoints={refreshDataPoints} />
      <GraphDisplay dataPoints={dataPoints} />
      <AnalysisResults dataPoints={dataPoints} />
    </div>
  );
};

export default Home;
