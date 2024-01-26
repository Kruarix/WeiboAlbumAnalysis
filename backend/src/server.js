const express = require('express');
const app = express();
const userRoutes = require('./api/routes/userRoutes');

app
  .use(express.json())
  .use('/api', userRoutes);

const PORT = 3000;
app.listen(PORT, ()=>{
  console.log(`Server is running on port ${PORT}`);
});

