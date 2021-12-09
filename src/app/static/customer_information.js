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
    .then(data => {
        console.log(data)
        document.querySelector("#full_names").innerText=data.full_name
        document.querySelector("#cust_number").innerText=data.cust_number
        document.querySelector("#cust_email").innerText=data.cust_email
        document.querySelector("#cust_street").innerText=data.cust_street + ', ' + data.cust_state + ', ' + data.cust_country
        document.querySelector("#cust_ids").innerText=data.id_number
        document.querySelector("#doc_types").innerText=data.doc_type
        document.querySelector("#card_numbers").innerText=data.card_number
        document.querySelector("#exp_dates").innerText=data.exp_date
        document.querySelector("#cvv_nums").innerText="************" + data.cvv_num
        document.querySelector("#notess").innerText=data.notes
    });

})