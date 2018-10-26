contextClass = (window.AudioContext ||
          window.webkitAudioContext ||
          window.mozAudioContext ||
          window.oAudioContext ||
          window.msAudioContext);

context = new contextClass();

var RhythmSample = function() {
  var path = "../media/sound/"

  //Descarga todos los sonidos y crea atributos
  //dinamicos para RhythmSample.
  /*
  RhythmSample.kick
  RhythmSample.snare
  RhythmSample.hihat
  */
  loadSounds(this, {
    kick:  path + 'kick.wav',
    snare: path + 'snare.wav',
    hihat: path + 'hihat.wav'
  });
};
var sample = new RhythmSample();

RhythmSample.prototype.play = function() {
  console.log(this);
  
  // Empezamos la reproducción desde 100 milisegundos
  var startTime = context.currentTime + 0.100;

  var eighthNoteTime = 0.25;

  // Reproducir compases
  for (var bar = 0; bar < 4; bar++) {
    var time = startTime + bar * 8 * eighthNoteTime;
    
    // Sonido de bombo en los beats 1, 5
    playSound(this.kick, time);
    playSound(this.kick, time + 4 * eighthNoteTime);

    // Sonido de redoblante en los beats 3, 7
    playSound(this.snare, time + 2 * eighthNoteTime);
    playSound(this.snare, time + 6 * eighthNoteTime);

    // Sonido de hi-hat en cada tiempo del compás
    for (var i = 0; i < 8; ++i) {
      playSound(this.hihat, time + i * eighthNoteTime);
    }
  }
}

function playSound(buffer, time) {
  var source = context.createBufferSource();
  source.buffer = buffer;
  source.connect(context.destination);
  source.start(time);
}

function loadSounds(obj, soundMap, callback){
  var names = [];
  var paths = [];
  for (var name in soundMap) {
    names.push(name);
    paths.push(soundMap[name]);
  }
  bufferLoader = new BufferLoader(context, paths, function(bufferList) {
    for (var i = 0; i < bufferList.length; i++) {
      var buffer = bufferList[i];
      var name = names[i];

      //agregamos un atributo dinamico
      //ejemplo:
      /*
        > var x = function(){}
        > undefined
        > x["param"] = 4
        > 4
        > x.param
        > 4
      */
      obj[name] = buffer;
    }

    //Si hay un callback, lo podemos llamar
    if (callback) {
      callback();
    }
  });
  bufferLoader.load();
}

