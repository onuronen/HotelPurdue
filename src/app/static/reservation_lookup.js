//url = "https://hotel-purdue.herokuapp.com/"
url = "http://127.0.0.1:5000/"

document.querySelector("#res_lookup").addEventListener("click", function(evt) {
    
    var check_in = document.getElementById("check_in").value;
    var room_number = document.getElementById("room_number").value;

    if (!check_in || !room_number) {
        return;
    }

    fetch(url + "customer_lookup", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'check_in': check_in,
            'room_number': room_number
        }
    })
    .then(response => response.json())
    .then(data => console.log(data));

})