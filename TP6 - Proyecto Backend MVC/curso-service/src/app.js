const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

const cursoRoutes = require('./routes/cursoRoutes');
app.use('/cursos', cursoRoutes);

module.exports = app;
