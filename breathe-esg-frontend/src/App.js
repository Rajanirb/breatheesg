import axios from "axios";
import React, { useEffect, useState } from "react";
import API from "./api/api";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

import "./App.css";

function App() {

  const [dashboard, setDashboard] = useState(null);
  const [file, setFile] = useState(null);
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    fetchDashboard();
    fetchRecommendations();
  }, []);

  const fetchDashboard = async () => {

    try {

      const response = await API.get(
        "dashboard-summary/"
      );

      setDashboard(response.data);

    } catch (error) {

      console.error(error);

    }
  };

  const fetchRecommendations = async () => {

    try {

      const response = await API.get(
        "ai-recommendations/"
      );

      setRecommendations(
        response.data.recommendations
      );

    } catch (error) {

      console.error(error);

    }
  };

  const uploadCSV = async () => {

    if (!file) {

      alert("Please select CSV file");
      return;

    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      await axios.post(
        "https://breatheesg-ht27.onrender.com/api/upload-csv/",
        formData
      );

      alert("CSV Uploaded Successfully");

      fetchDashboard();

    } catch (error) {

      console.error(error);

    }
  };

  if (!dashboard) {

    return <h1>Loading...</h1>;

  }

  const chartData = [
    {
      name: "Scope 1",
      emission: dashboard.scope_1,
    },
    {
      name: "Scope 2",
      emission: dashboard.scope_2,
    },
    {
      name: "Scope 3",
      emission: dashboard.scope_3,
    },
  ];

  return (

    <div className="container">

      <h1>Breathe ESG Dashboard</h1>

      <div className="card-grid">

        <div className="card">
          <h2>Total Emissions</h2>
          <p>{dashboard.total_emissions.toFixed(2)} kgCO2e</p>
        </div>

        <div className="card">
          <h2>Scope 1</h2>
          <p>{dashboard.scope_1.toFixed(2)}</p>
        </div>

        <div className="card">
          <h2>Scope 2</h2>
          <p>{dashboard.scope_2.toFixed(2)}</p>
        </div>

        <div className="card">
          <h2>Scope 3</h2>
          <p>{dashboard.scope_3.toFixed(2)}</p>
        </div>

        <div className="card">
          <h2>Suspicious Records</h2>
          <p>{dashboard.suspicious_records}</p>
        </div>

      </div>

      <div
        style={{
          marginTop: "30px",
          marginBottom: "30px"
        }}
      >

        <input
          type="file"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
        />

        <button
          onClick={uploadCSV}
          style={{
            marginLeft: "10px",
            padding: "10px 20px",
            backgroundColor: "#00b894",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer"
          }}
        >
          Upload CSV
        </button>

      </div>

      <div className="chart-container">

        <h2>Emission Analytics</h2>

        <ResponsiveContainer
          width="100%"
          height={400}
        >

          <BarChart data={chartData}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="name" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="emission"
              fill="#00b894"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

      <div
        className="chart-container"
        style={{ marginTop: "30px" }}
      >

        <h2>AI Sustainability Recommendations</h2>

        {
          recommendations.map((item, index) => (

            <div
              key={index}
              style={{
                background: "#ecfdf5",
                padding: "15px",
                borderRadius: "10px",
                marginBottom: "10px",
                color: "black",
                fontWeight: "bold"
              }}
            >
              {item}
            </div>

          ))
        }

      </div>

    </div>
  );
}

export default App;