window.addEventListener('load', () => {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    //Resizing

    //canvas.height = window.innerHeight;
    //canvas.width = window.innerWidth;
    canvas.height = 300;
    canvas.width = 300;
    //variables
    let painting = false;

    function startPosition(e){
        painting = true;
        draw(e);
    }

    function endPosition(){
        painting = false;
        ctx.beginPath();
    }

    function draw(e){
        if(!painting) return;
        ctx.linweWidth = 10;
        ctx.lineCap = 'round';
        ctx.strokeStyle = "red";
        ctx.lineTo(e.clientX, e.clientY);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(e.clientX, e.clientY);


    }


    function clean_data(){
        ctx.clearRect(0, 0, 1000, 1000);
        
        ctx.beginPath();
    }

    //eventListeners
    canvas.addEventListener('mousedown', startPosition);
    canvas.addEventListener('mouseup', endPosition);
    canvas.addEventListener('mousemove', draw);
    // bind event handler to clear button
    document.getElementById('clear').addEventListener('click', function() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        window.alert("cleared ");
        var numbers = ctx.getImageData(0, 0, canvas.height, canvas.width);
        console.log(numbers.data);
      }, false);

})