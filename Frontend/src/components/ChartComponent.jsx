import React, { useEffect, useRef } from "react";
import { Chart } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

const ChartComponent = ({ dataPoints, bestFit, interpolation, chartType = "scatter" }) => {
  const chartRef = useRef(null);

  const xValues = dataPoints.map((point) => point.x_value);
  const yValues = dataPoints.map((point) => point.y_value);

  const minX = Math.min(...xValues);
  const maxX = Math.max(...xValues);
  const bestFitLine = [
    { x: minX, y: bestFit.slope * minX + bestFit.intercept },
    { x: maxX, y: bestFit.slope * maxX + bestFit.intercept },
  ];

  const data = {
    datasets: [
      {
        label: chartType === "scatter" ? "Scatter Dataset" : "Line Dataset",
        data: dataPoints.map((point) => ({ x: point.x_value, y: point.y_value })),
        backgroundColor: chartType === "scatter" ? "rgba(75, 192, 192, 1)" : "rgba(0, 0, 0, 0)",
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: chartType === "line" ? 2 : 0,
        showLine: chartType === "line",
        pointRadius: chartType === "scatter" ? 5 : 0,
      },
      {
        label: "Best Fit Line",
        data: bestFitLine,
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 2,
        showLine: true,
        pointRadius: 0,
        fill: false,
      },
      {
        label: "Interpolation",
        data: interpolation.map((point) => ({ x: point.x, y: point.y })),
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 2,
        showLine: true,
        pointRadius: 0,
        fill: false,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: {
        type: "linear",
        position: "bottom",
      },
    },
  };

  useEffect(() => {
    if (chartRef.current) {
      chartRef.current.resize();
    }
  }, [chartType]);

  return (
    <div className="chart-container">
      <Chart ref={chartRef} type={chartType} data={data} options={options} />
    </div>
  );
};

export default ChartComponent;