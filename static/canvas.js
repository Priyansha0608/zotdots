
console.log("canvas.js executed");

var canvas = document.getElementById("c");
var ctx = canvas.getContext("2d");
var width = canvas.width;
var height = canvas.height;
var color = null;
var x;
var y;

var box_width = 20; // one box has width and height 20px

draw_grid(ctx, width, height);


function draw_grid(context, width, height){
    context.lineWidth = 0.35;
    context.strokeStyle = "slategray";
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
    var roundedX = x * 20;
    var roundedY = y * 20;
	//var roundedX = Math.round(x);
    //var roundedY = Math.round(y);
    context.fillStyle = color || '#000';
  	context.fillRect(roundedX, roundedY, 20, 20);
    context.strokeStyle = "slategray";
    context.lineWidth = 0.35;
    context.strokeRect(roundedX, roundedY, 20, 20);
}

const getCursorPosition = (canvas, event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    //console.log(x, y);
    return {x, y}; // pixel x, y
  }

function getCoordinates(x, y) {
    const x1 = Math.floor(x/box_width);
    const y1 = Math.floor(y/box_width);
    // console.log(x1, y1);
    return {x1, y1}
}

function changeColor(c) {
    color = c;
}

// draw a pixel in the correct box when mouse is clicked
canvas.addEventListener('mousedown', (e) => {
    if (color != null){
        const coords = getCursorPosition(canvas, e);
        const box = getCoordinates(coords.x, coords.y);

        drawPixel(ctx, box.x1, box.y1, color); // change color value too!!

        x = box.x1;
        y = box.y1;
        sendPixelInfo();
        return {x, y, color}
    }
})

// send info to app.py
function sendPixelInfo() {
    //console.log("in send pixel info\n")
    const formData = new FormData();
    //console.log("new formdata created\n")
    formData.append("x", x)
    formData.append("y", y)
    formData.append("color", color)
    //console.log("info appended to form data\n")
  
    const request = new XMLHttpRequest();
    //console.log("new request created\n")
    request.open('POST', '/test', true);
    //console.log("request opened\n")
    request.send(formData);
    //console.log("request sent\n")
}
