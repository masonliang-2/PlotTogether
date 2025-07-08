import React, { createContext, useState, useEffect } from 'react';
import { fetchDataPoints } from '../apiService';

export const ChartDataContext = createContext();

export const ChartDataProvider = ({ children }) => {
    const [dataPoints, setDataPoints] = useState([]);

    useEffect(() => {
        const getDataPoints = async () => {
            try {
                const data = await fetchDataPoints();
                setDataPoints(data);
            } catch (error) {
                console.error("Error fetching data points:", error);
            }
        };

        getDataPoints();
    }, []);

    return (
        <ChartDataContext.Provider value={{ dataPoints, setDataPoints }}>
            {children}
        </ChartDataContext.Provider>
    );
};