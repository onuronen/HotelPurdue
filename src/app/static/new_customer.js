//url = "https://hotel-purdue.herokuapp.com/"
url = "http://127.0.0.1:5000/"

document.querySelector("#new_customer").addEventListener("click", function(evt) {
    //evt.preventDefault();

    //document.querySelector(".form_error").innerHTML = null;

    //console.log("HERE!")

    var first_name = document.getElementById("first_name").value;
    var last_name = document.getElementById("last_name").value;
    var phone_number = document.getElementById("phone_number").value;
    var email = document.getElementById("email").value;
    var street = document.getElementById("street").value;
    var state = document.getElementById("state").value;
    var country = document.getElementById("country").value;
    var id_number = +document.getElementById("id_number").value;
    var id_type = document.getElementById("id_type").value;
    var notes = document.getElementById("notes").value;
    var card_number = +document.getElementById("card_number").value;
    var cvv = +document.getElementById("cvv").value;
    var expiration_date = document.getElementById("expiration_date").value;

    if (!first_name || !last_name || !phone_number || !email || !street || !state || !country 
        || !id_number || !id_type || !card_number) {
        return;
    }


    fetch(url + "check_in_customer", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email,
            'street': street,
            'state': state,
            'country': country,
            'id_number': id_number,
            'id_type': id_type,
            'notes': notes,
            'card_number':card_number,
            'cvv': cvv,
            'expiration_date': expiration_date
        }
    })
    .then(response => response.json())
    .then(data => console.log(data));

})