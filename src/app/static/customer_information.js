//url = "https://hotel-purdue.herokuapp.com/"
url = "http://127.0.0.1:5000/"

document.querySelector("#customer_info_lookup").addEventListener("click", function(evt) {
    
    var full_name = document.getElementById("full_name").value;
    var email = document.getElementById("email").value;

    if (!full_name || !email) {
        return;
    }

    fetch(url + "customer_lookup", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'full_name': full_name,
            'email': email
        }
    })
    .then(response => response.json())
    .then(data => console.log(data));

})