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
    .then(data => {
        console.log(data)
        console.log(data['0'].room_id)
        document.querySelector("#room_id").innerText=data['0'].room_id
        document.querySelector("#room_type").innerText=data['0'].room_type
        document.querySelector("#room_number").innerText=data['0'].room_number
        document.querySelector("#room_rate").innerText=data['0'].price
        document.querySelector("#room_occupancy").innerText=data['0'].max_occupancy
    });

})