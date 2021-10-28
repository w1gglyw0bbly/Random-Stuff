class hanoiBoard {
	constructor(towerSize) {
		this.towerSize = towerSize;
	}
	
	
	
	//get functions
	getTowerSize() {
		return this.towerSize;
	}
}

class piece {
	constructor(width) {
		this.width = width;
	}
	
	//get functions
	getWidth() {
		return this.width;
	}
}

function allowDrop(ev) {
	if ev.currentTarget.className == 'line'{
		break;
	}
	ev.preventDefault();
}

function drag(ev) {
	ev.dataTransfer.setData('text', ev.target.id);
}

function drop(ev) {
	ev.preventDefault();
	data = ev.dataTransfer.getData('text');
	ev.target.appendChild(document.getElementById(data));
}


board = new hanoiBoard(3);
console.log(board.getTowerSize())

testDiv = document.createElement('div')
textStuff = document.createTextNode('yo')
testDiv.appendChild(textStuff)
mainDiv = document.getElementById('columns')
//document.body.insertBefore(testDiv, mainDiv)

/*
console.log('Your mom');


x = 6;
console.log(test(x));

function test(x){
	return x + 5
}
*/