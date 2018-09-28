var express = require('express');
var bodyParser = require('body-parser');
var app = express();

//Configuring express to use body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

//define routes
app.get('/links', function(req, res) {
  links = [];
  links = [
      {id: 0, title:'google', url:'www.google.com', tags:['google', 'search'], date: new Date(Date.now())},
      {id: 1, title:'facebook', url:'www.facebook.com', tags:['facebook', 'social'], date: new Date(Date.now())},
      {id: 2, title:'whatsapp', url:'www.whatsapp.com', tags:['whatsapp', 'chat', 'social'], date: new Date(Date.now())},
      {id: 3, title:'netflix', url:'www.netflix.com', tags:['netflix', 'video', 'social'], date: new Date(Date.now())}
    ];
  respond(res, links);
});

app.get('/tags', function(req, res) {
  tags = [];
  tags = ['google', 'search', 'whatsapp', 'facebook', 'social', 'chat', 'netflix', 'video'];
  respond(res, tags);
})


/*
Internal functions
*/
function respond(res, data){
  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.end(JSON.stringify(data));
}

/*
Server start
*/
var server = app.listen(process.env.PORT, function() {
  var port = server.address().port;
  console.log("App now running on port", port);
});
