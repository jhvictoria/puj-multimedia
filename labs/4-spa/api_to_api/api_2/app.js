var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var expressLogging = require('express-logging');
var logger = require('logops');
var request = require('request-json');
var client = request.createClient('http://api1:5000/');

app.use(expressLogging(logger));

var port = process.env.PORT || 3000;

app.get('/version', function(req, res) {
    client.get('version/', function(err, res2, body) {
        console.log(body.version);
        body.reference = "api2";
        res.end(JSON.stringify(body));
    });
});

/*
Server start
*/
var server = app.listen(port, function() {
	var port = server.address().port;
	console.log("App now running on port", port);
});
