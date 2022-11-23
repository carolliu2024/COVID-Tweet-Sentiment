const express = require('express');
const app = express();

// Create server
app.listen(process.env.PORT || 3000, function() {
    console.log('listening on 3000')
  });

// Make server send html page to browser
app.get('/', (req, res) => {
    res.sendFile(__dirname + '../Map/senti_map.html')
  })