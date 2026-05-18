const app = require('./app');

const PORT = 3001;

app.listen(PORT, () => {
  console.log(`alumno-service corriendo en http://localhost:${PORT}`);
});
