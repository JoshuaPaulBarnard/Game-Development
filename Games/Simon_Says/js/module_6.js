// current level
var level = 1;
// current turn
var turn = 0;
// current score
var score = 0;
// boolean: is a turn is active or not?
var active = false;
// boolean: are click handlers active?
var handler = false;
// array (list) of generated pads
var genSequence = [];
// array (list) of users pads selected
var plaSequence = [];
// array for loosing pad flashes
var lostSequence =[1,2,3,4,2,3,4,1,3,4,1,2,4,1,2,3];
// sound clip for playing game
var cheer = new Audio('audio/applause.wav');
// difficulty variable
var hard = false;

// initialises the game
function init() {
	// check to see if click event handlers are already active
	if (handler === false) {
		// if not activate them
		initClickHandler();
	}
	// starts new game
	newGame();
}

function initClickHandler() {
	$('.pad').click( function(){
		if (active===true) {
			// get numeric value stored in data-pad attribute for each element
			var pad = parseInt( $(this).data('pad'), 10 );
			flash( $(this),1,300, pad );
			logPlayerSequence(pad);
		}
	});
	handler = true;
}

// resets game and generates a starts a new level
function newGame() {
	level = 1;
	score = 0;
	newLevel();
	displayLevel();
	displayScore();
	displayPattern();
}

// start a new level in game
function newLevel() {
	genSequence.length = 0;
	plaSequence.length = 0;
	turn = 0;
	active = true;
	// randomize pad with correct count for this level
	randomizePad(level);
	// show user the sequence
	displaySequence();
	displayPattern();
}

// function to make pads appear to flash
function flash(element, times, speed, pad) {
	// make sure we are supposed to flash
	if (times > 0) {
		// animate the element to appear to flash
		// animate takes two parameters:
		// 1. css property list
		// 2. animate settings property list
		if (hard == false) {
		element.stop().animate(
			{opacity: '3'},
			{
				duration: 25,
				complete: function(){
					element.stop().animate({opacity: '0.3'}, 700,'linear');
				}
			}
		);
	}
	else {
		element.stop().animate(
			{opacity: '3'},
			{
				duration: 5,
				complete: function(){
					element.stop().animate({opacity: '0.3'}, 50,'linear');
				}
			}
		);
	}
		// end of animate() statement
	}

	// call the flash function again until done correct amount of times
	if (times > 0) {
		setTimeout(function () {
			flash(element, times, speed, pad);
		}, speed);
		// subtract one from times for each time code is called
		times -= 1;
	}
}

// generate random numbers (1-3) and push onto generated array
// how many is determined by current level
function randomizePad(passes) {
	for ( i=0; i < passes; i++ ) {
		genSequence.push( Math.floor( Math.random() * 4 ) + 1 );
		// show generated sequence in browser console
		console.log(genSequence);
	}
}

// log the player-clicked pad to array then call checkSequence()
function logPlayerSequence(pad) {
	plaSequence.push(pad);
	checkSequence(pad);
}

// check to see if the pad the user pressed was next correct in sequence
function checkSequence(pad) {
	if ( pad !== genSequence[turn] ) {
		// if not correct
		incorrectSequence();
	} else {
		// if correct
		// update the score
		keepScore();
		// incrememnt the turn
		turn++;
	}

	// if completed the whole sequence
	if ( turn === genSequence.length ) {
		// increment level
		level++;
		// display level
		displayLevel();
		// disable the pads
		active=false;
		// reset the game after 1 second
		setTimeout(function(){
			newLevel();
		},1000);
	}
}

// display the generated sequence to the user
function displaySequence() {
	// loop through each value in the generated array (list)
	$.each(genSequence, function(index, val) {
		// multiply timeout by how many items in the array so that they play in order
		setTimeout(function(){
			flash( $('.shape' + val), 1, 300, val );
		}, 500 * index);
	});
}

// display the current level on screen
function displayLevel() {
	$('.level h2').text('Level: ' + level);
}

// display current score on screen
function displayScore() {
	$('.score h2').text('Score: ' + score);
}

// display the current sequence on screen
function displayPattern() {
	if (hard==false) {
		$('.seqLog h2').text('Sequence: ' + genSequence);
	}
	else {
		$('.seqLog h2').text('Sequence: ');
	}
}

// keep the score
function keepScore() {
	// calculates the score and display score on screen
	if (hard==false) {
		score += 1;
		displayScore();
	}
	else {
		score += 0.25
		displayScore();
	}
}

// if user makes a mistake
function incorrectSequence() {
	active=false;
	displayLevel();
	displayScore();
	displayPattern();
	// Flashes the pad in the looser sequence.
	$.each(lostSequence, function(index, val) {
		setTimeout(function(){
			flash( $('.shape' + val), 1, 300, val );
		}, 500 * index);
	});
	// enable the start button again
	$('.start').show();
}

// document ready
$(document).ready(function(){
	// start a game when the start button is clicked
	$('.start').click( function(){
		$(this).hide();
		init();
		cheer.play();
	});
});
