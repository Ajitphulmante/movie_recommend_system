const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();

app.use(express.static('public'));

app.use(cors({
    origin: true,
    credentials: true,
  }));

app.get('/',(req,res)=>{
    res.sendFile(__dirname + "/index.html");
})


app.listen(3000,()=>{
    console.log('Server is runnig on port number 3000');
})