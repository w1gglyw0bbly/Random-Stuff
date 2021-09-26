console.log('test')
rocks = 0
document.getElementById('rockCounter').innerText = rocks

function userClick(){
	rocks += 1
	document.getElementById('rockCounter').innerText = rocks
	document.getElementById('clickImage').className = 'clickImage'
}