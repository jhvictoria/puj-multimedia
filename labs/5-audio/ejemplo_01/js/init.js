window.onload = init;
var context;
var bufferLoader;

function init() {
	contextClass = (window.AudioContext ||
					window.webkitAudioContext ||
					window.mozAudioContext ||
					window.oAudioContext ||
					window.msAudioContext);
	if (contextClass) {
		// Web Audio API is available.
		context = new contextClass();
		$("#AudioAPI").html("soporta Web Audio API");
	} else {
		$("#AudioAPI").html("No soporta Web Audio API");
		return;
	}

	bufferLoader = new BufferLoader(
		context,
		[
			'../media/sound/bg.mp3',
			'../media/sound/tada.mp3'
		], finishedLoading
	);
	bufferLoader.load();
}

function finishedLoading(bufferList) {
	var source1 = context.createBufferSource();
	var source2 = context.createBufferSource();

	source1.buffer = bufferList[0];
	source2.buffer = bufferList[1];


	var feedback = context.createGain();
	feedback.gain.value = 1.0;

	var low_pass_filter = context.createBiquadFilter();
	
	//realizar conexiones
	source1.connect(feedback);
	feedback.connect(low_pass_filter);
	low_pass_filter.connect(context.destination);
	
	source2.connect(context.destination);

	source1.start();
	source2.start();
}
