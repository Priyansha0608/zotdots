
console.log("canvas.js executed");

var canvas = document.getElementById("c");
var ctx = canvas.getContext("2d");
var width = canvas.width;
var height = canvas.height;


drawPixel(ctx, 0, 0, 'red');
draw_grid(ctx, width, height);

/*window.onload = function() {
    var canvas = document.getElementById("c") //new fabric.Canvas("c")
    window.canvas = canvas
    var context = canvas.getContext('2d');
    drawPixel(context, 20, 10, 'red'); // x=20 y=10

    canvas.renderAll()
}*/

function draw_grid(context, width, height){
    context.lineWidth = 0.35;
    context.strokeStyle = "slategray"; // a lighter color!!!
    for (var x = 0; x <= width; x += width/25){
        context.beginPath();
        context.moveTo(x, 0);
        context.lineTo(x, height);
        context.stroke();
    }

    for (var y = 0; y <= height; y += height/25){
        context.beginPath();
        context.moveTo(0, y);
        context.lineTo(width, y);
        context.stroke();
    }
}
function drawPixel(context, x, y, color) {
	var roundedX = Math.round(x);
    var roundedY = Math.round(y);
    context.fillStyle = color || '#000';
  	context.fillRect(roundedX, roundedY, 50, 50);
}

const getCursorPosition = (canvas, event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    console.log(x, y);
    return {x, y}; // pixel x, y
  }

function getCoordinates(x, y) {
    const x1 = Math.floor(x/20);
    const y1 = Math.floor(y/20);
    console.log(x1, y1);
}

canvas.addEventListener('mousedown', (e) => {
    const coords = getCursorPosition(canvas, e);
    getCoordinates(coords.x, coords.y)
})
