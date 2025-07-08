import React, { useState } from "react";
import { deleteDataPoint, updateDataPoint, createDataPoint } from "../apiService";

const EditableTable = ({ dataPoints, refreshDataPoints }) => {
  const [editingRow, setEditingRow] = useState(null);
  const [editedX, setEditedX] = useState("");
  const [editedY, setEditedY] = useState("");
  const [newX, setNewX] = useState("");
  const [newY, setNewY] = useState("");

  const handleEdit = (point) => {
    setEditingRow(point.id);
    setEditedX(point.x_value);
    setEditedY(point.y_value);
  };

  const handleSave = async (id) => {
    try {
      await updateDataPoint(id, Number(editedX), Number(editedY));
      setEditingRow(null);
      refreshDataPoints();
    } catch (error) {
      console.error("Error updating data point:", error);
    }
  };

  const handleCancel = () => {
    setEditingRow(null);
  };

  const handleDelete = async (id) => {
    try {
      await deleteDataPoint(id);
      refreshDataPoints();
    } catch (error) {
      console.error("Error deleting data point:", error);
    }
  };

  const handleCreate = async () => {
    try {
      await createDataPoint(Number(newX), Number(newY));
      setNewX("");
      setNewY("");
      refreshDataPoints();
    } catch (error) {
      console.error("Error creating data point:", error);
    }
  };

  return (
    <div className="editable-table-container">
        {/* Input Fields and Button */}
      <div className="data-input">
        <h3>New Data Point</h3>
        <div className="xy-input">
          <input
            type="number"
            placeholder="X Value"
            value={newX}
            onChange={(e) => setNewX(e.target.value)}
          />
          <input
            type="number"
            placeholder="Y Value"
            value={newY}
            onChange={(e) => setNewY(e.target.value)}
          />
        </div>
        <button onClick={handleCreate}>Add</button>
      </div>
      
      {/* Table Component */}
      <div className="editable-table">
        <h3 className="center">Data Table</h3>
        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th className="variable">X Value</th>
                <th className="variable">Y Value </th>
                <th className="action">Actions</th>
              </tr>
            </thead>
            <tbody>
              {dataPoints.map((point) => (
                <tr key={point.id}>
                  <td className="variable">
                    {editingRow === point.id ? (
                      <input
                        type="number"
                        value={editedX}
                        onChange={(e) => setEditedX(e.target.value)}
                      />
                    ) : (
                      point.x_value
                    )}
                  </td>
                  <td className="variable">
                    {editingRow === point.id ? (
                      <input
                        type="number"
                        value={editedY}
                        onChange={(e) => setEditedY(e.target.value)}
                      />
                    ) : (
                      point.y_value
                    )}
                  </td>
                  <td className="action">
                    {editingRow === point.id ? (
                      <>
                        <button onClick={() => handleSave(point.id)}>Save</button>
                        <button onClick={handleCancel}>Cancel</button>
                      </>
                    ) : (
                      <>
                        <button onClick={() => handleEdit(point)}>Edit</button>
                        <button onClick={() => handleDelete(point.id)}>Delete</button>
                      </>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default EditableTable;