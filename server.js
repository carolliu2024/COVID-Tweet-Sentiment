const express = require('express');
const app = express();

// Create server
app.listen(process.env.PORT || 3000, function() {
    console.log('listening on 3000')
  });

// Make server send html page to browser
app.get('/', (req, res) => {
  var path = require('path'); // so path string isn't seen as malicious
  res.sendFile(path.resolve(__dirname + '/../Map/senti_map.html'))
})