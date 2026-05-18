const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

const inscripcionRoutes = require('./routes/inscripcionRoutes');
app.use('/inscripciones', inscripcionRoutes);

module.exports = app;
