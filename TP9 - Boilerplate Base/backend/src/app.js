const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

app.get('/health', (req, res) => res.json({ status: 'ok' }));

// Registrar acá las rutas de cada entidad
const itemRoutes = require('./routes/itemRoutes');
app.use('/items', itemRoutes);

module.exports = app;
