var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var expressLogging = require('express-logging');
var logger = require('logops');

app.use(expressLogging(logger));

var port = process.env.PORT || 5000;

app.get('/version', function(req, res) {
    version = {version: "1.0"};
    res.end(JSON.stringify(version));
});

/*
Server start
*/
var server = app.listen(port, function() {
    var port = server.address().port;
    console.log("App now running on port", port);
});
