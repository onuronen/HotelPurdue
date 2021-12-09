//url = "https://hotel-purdue.herokuapp.com/"
url = "http://127.0.0.1:5000/"

document.querySelector("#res_lookup").addEventListener("click", function(evt) {
    
    var check_in = document.getElementById("check_in").value;
    var room_number = document.getElementById("room_number").value;

    if (!check_in || !room_number) {
        return;
    }

    fetch(url + "reservation_lookup", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'check_in': check_in,
            'room_number': room_number
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        //console.log(data.end_date)
        document.querySelector("#full_name").innerText=data.full_name
        document.querySelector("#guest_number").innerText=data.guest_number
        document.querySelector("#room_numbers").innerText=data.room_number
        //console.log(data.room_number)
        document.querySelector("#room_type").innerText=data.room_type
        document.querySelector("#start_date").innerText=data.start_date
        document.querySelector("#end_date").innerText=data.end_date
        document.querySelector("#reservation_date").innerText=data.reservation_date
        document.querySelector("#notes").innerText=data.notes
        //document.querySelector("#room_id").innerText=data['0'].room_id
        //document.querySelector("#room_type").innerText=data['0'].room_type
        //document.querySelector("#room_number").innerText=data['0'].room_number
        //document.querySelector("#room_rate").innerText=data['0'].price
        //document.querySelector("#room_occupancy").innerText=data['0'].max_occupancy
    });

})