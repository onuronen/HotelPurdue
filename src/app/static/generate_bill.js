//url = "https://hotel-purdue.herokuapp.com/"
url = "http://127.0.0.1:5000/"

document.querySelector("#customer_check_out").addEventListener("click", function(evt) {
    
    var full_name = document.getElementById("full_name").value;
    var room_number = document.getElementById("room_number").value;

    if (!full_name || !room_number) {
        return;
    }

    fetch(url + "check_out_customer", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'full_name': full_name,
            'room_number': room_number
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    });

})