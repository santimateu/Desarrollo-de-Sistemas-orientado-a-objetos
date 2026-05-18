const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

const alumnoRoutes = require('./routes/alumnoRoutes');
app.use('/alumnos', alumnoRoutes);

module.exports = app;
