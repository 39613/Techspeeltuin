img = document.getElementById("camera");
sensor = document.getElementById("sensorValue")

timestamp = new Date().getTime();

img.src = "../../img/camera.jpg?t=" + timestamp;

path = "/sensorData.json"

fetch(path)
.then(response=>response.json())
.then(data=>{
    sensor.innerHTML = "{distance}: " + data.distance
})