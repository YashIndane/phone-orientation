/*
This function will fetch the orientation of phone from the API
and update the image on webpage
*/
function updateOrientation(){

    var xhr = new XMLHttpRequest();
    var queryString = "http://<IP>/cgi-bin/up-down-API.py";
    xhr.open("GET", queryString, true);
    xhr.send();

    xhr.onload = function(){

        var response = xhr.responseText;
        document.getElementById("facedir").innerHTML = response;
        console.log(response);
        
        var img = document.getElementById("imgname");

        var upPath = "https://raw.githubusercontent.com/YashIndane/repo-images/main/frontphoto.png";
        var downPath = "https://raw.githubusercontent.com/YashIndane/repo-images/main/backphoto.png";

        img.src = (response.trim() == "up") ? upPath : downPath;
    }
}

// Time in ms
var fetchTime = 500;

updateOrientation();
setInterval(updateOrientation, fetchTime);