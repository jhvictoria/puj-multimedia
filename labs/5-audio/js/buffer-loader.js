function BufferLoader(context, urlList, callback) {
    this.context = context;         //Contexto: Plugin de audio del navegador
    this.urlList = urlList;         //array de urls de audios a decargar
    this.onload = callback;         //Func callback a llamar una vez los audios sean descargados
    this.bufferList = new Array();  //buffer de cada audio descargado
    this.loadCount = 0;             //cantidad de audios ya descargados
}

//Itera por cada una de las URLs this.urlList para cargar su buffer en el bufferList
BufferLoader.prototype.load = function() {
    for (var i = 0; i < this.urlList.length; ++i)
        this.loadBuffer(this.urlList[i], i);
}

BufferLoader.prototype.loadBuffer = function(url, index) {
    var loader = this;

    //Se debe cargar el buffer de forma asincrona
    var request = new XMLHttpRequest();
    request.responseType = "arraybuffer";
    request.open("GET", url, true);
    
    request.onload = function() {
        // Decodificar los datos de audio de request.response de forma asincrona
        loader.context.decodeAudioData(
            request.response,
            function(buffer) {
                if(!buffer) {
                    alert('error decoding file data: ' + url);
                    return;
                }
                console.log(buffer);
                console.log(buffer.getChannelData(0));
                loader.bufferList[index] = buffer;
                if(++loader.loadCount == loader.urlList.length)
                    loader.onload(loader.bufferList);
            },
            function(error) {
                console.error('decodeAudioData error', error);
            }
        );
    }

    request.onerror = function() {
        alert('BufferLoader: XHR error');
    }

    request.send();
}
