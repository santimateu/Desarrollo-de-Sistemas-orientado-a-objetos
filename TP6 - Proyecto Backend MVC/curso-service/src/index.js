const app = require('./app');

const PORT = 3002;

app.listen(PORT, () => {
  console.log(`curso-service corriendo en http://localhost:${PORT}`);
});
