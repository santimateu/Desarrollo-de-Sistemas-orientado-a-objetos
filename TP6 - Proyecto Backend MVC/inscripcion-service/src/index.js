const app = require('./app');

const PORT = 3003;

app.listen(PORT, () => {
  console.log(`inscripcion-service corriendo en http://localhost:${PORT}`);
});
