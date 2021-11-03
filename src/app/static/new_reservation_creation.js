//url = "https://hotel-purdue.herokuapp.com/"
url = "http://127.0.0.1:5000/"

document.querySelector("#new_reservation_creation").addEventListener("submit", function(evt) {
    //evt.preventDefault();

    //document.querySelector(".form_error").innerHTML = null;

    var full_name = document.getElementById("full_name").value;
    var id_number= document.getElementById("id_number").value;
    var check_in = document.getElementById("check_in").value;
    var check_out = document.getElementById("check_out").value;
    var guest_number = document.getElementById("number_of_guests").value;
    var room_type = document.getElementById("room_type").value;
    var notes = document.getElementById("notes").value;
    var employee_full_name = document.getElementById("employee_full_name").value;
    var max_occupancy = document.getElementById("max_occupancy").value;
    var rate = document.getElementById("rate").value;
    var room_number = document.getElementById("room_number").value;
    
    if (!full_name || !id_number || !check_in || !check_out || !guest_number || !room_type || !room_number 
        || !employee_full_name || !max_occupancy || !rate) {
        return;
    }


    fetch(url + "customer_room_check_in", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'full_name': full_name,
            'id_number': id_number,
            'check_in': check_in,
            'check_out': check_out,
            'guest_number': guest_number,
            'room_type': room_type,
            'notes': notes,
            'employee_full_name': employee_full_name,
            'max_occupancy': max_occupancy,
            'rate': rate,
            'room_number':room_number
        }
    })
    .then(response => response.json())
    .then(data => console.log(data));

})