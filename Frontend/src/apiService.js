import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const createDataPoint = async (x, y) => {
    try {
        const response = await axios.post(`${API_URL}crud/`, {
            operation: 'create',
            metadata: {
                changes: { x, y }
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error creating data point:", error);
        throw error;
    }
};

export const fetchDataPoints = async () => {
    try {
        const response = await axios.get(`${API_URL}get-data-points/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching data points:", error);
        throw error;
    }
};

export const deleteDataPoint = async (id) => {
    try {
        const response = await axios.post(`${API_URL}crud/`, {
            operation: "delete",
            metadata: {
                changes: { id },
            },
        });
        return response.data;
    } catch (error) {
        console.error("Error deleting data point:", error);
        throw error;
    }
};

export const updateDataPoint = async (id, x, y) => {
  try {
    const response = await axios.post(`${API_URL}crud/`, {
      operation: "update",
      metadata: {
        changes: { id, x, y },
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error updating data point:", error);
    throw error;
  }
};