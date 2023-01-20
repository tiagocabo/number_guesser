window.addEventListener('load', () => {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    //Resizing

    //canvas.height = window.innerHeight;
    //canvas.width = window.innerWidth;
    canvas.height = 200;
    canvas.width = canvas.height;
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
        ctx.lineCap = 'round';
        
        ctx.lineTo(e.clientX, e.clientY);
        ctx.strokeStyle = "red";
        ctx.lineWidth = 10;
        ctx.stroke();
        //ctx.beginPath();
        ctx.moveTo(e.clientX, e.clientY);

    }


    function download(filename, array) {
        var element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(array));
        element.setAttribute('download', filename);
      
        element.style.display = 'none';
        document.body.appendChild(element);
      
        element.click();
      
        document.body.removeChild(element);
      }


    //eventListeners
    canvas.addEventListener('mousedown', startPosition);
    canvas.addEventListener('mouseup', endPosition);
    canvas.addEventListener('mousemove', draw);

    /* CLEAR BUTTON */
    document.getElementById('clear_button').addEventListener("click", function()
    {
        console.log("click clear");
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        document.getElementById('prediction_res').value = "Prediction";

    }, false);

    // bind event handler to clear button
    document.getElementById('Predict').addEventListener('click', function() {
        //window.alert("cleared ");
        var numbers = ctx.getImageData(0, 0, canvas.height, canvas.width);
        //ctx.putImageData(numbers, 10, 10);
        //ctx.clearRect(0, 0, canvas.width, canvas.height);
        //console.log(numbers.data);

        var http = new XMLHttpRequest();

        http.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                //console.log(this.responseText);
                document.getElementById('prediction_res').value = this.responseText;
            }
        };

        //download("numbers", numbers.data);

        var pixel_data = numbers.data;
        var url = "http://3.8.91.75:8080/predict";

        http.open("POST",url, true );

        //Send the proper header information along with the request
        http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        var params = "pixels=" + pixel_data.toString();
        //console.log(params);


        http.send(params);

        
      }, false);

})