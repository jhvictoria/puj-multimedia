var express = require('express');
var https = require('https');
var fs = require('fs');
var app = express();

app.use(express.static('public'));

https.createServer({
      key: fs.readFileSync('../cert/server.key'),
      cert: fs.readFileSync('../cert/server.crt')
    }, app).listen(7000);
