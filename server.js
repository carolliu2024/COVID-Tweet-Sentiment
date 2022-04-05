const express = require('express');
const app = express();

// Create server
app.listen(3000, function() {
    console.log('listening on 3000')
  });

// Make server send html page to browser
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/Map/chloro_map_ex.html')
  })

