//url = "https://hotel-purdue.herokuapp.com/"
url = "http://127.0.0.1:5000/"

document.querySelector("#find_room").addEventListener("click", function(evt) {
    
    var room_number = document.getElementById("room_number_input").value;
    
    if (!room_number) {
        return;
    }


    fetch(url + "room_lookup", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'room_number':room_number
        }
    })
    .then(response => response.json())
    .then(data => console.log(data));

})