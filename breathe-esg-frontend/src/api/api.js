import axios from "axios";

const API = axios.create({
  baseURL: "https://breatheesg-ht27.onrender.com/api/",
});

export default API;