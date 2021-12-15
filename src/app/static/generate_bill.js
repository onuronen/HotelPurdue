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
        document.querySelector("#full_names").innerText=data.cust_fname + " " + data.cust_lname
        document.querySelector("#emails").innerText=data.cust_email
        document.querySelector("#phone_numbers").innerText=data.cust_number
        document.querySelector("#streets").innerText=data.cust_street
        document.querySelector("#states").innerText=data.cust_state
        document.querySelector("#countrys").innerText=data.cust_country
        document.querySelector("#id_numbers").innerText=data.customer_id
        document.querySelector("#id_types").innerText=data.doc_type
        document.querySelector("#card_numbers").innerText="************" + data.id_number
        
        
        document.querySelector("#room_numbers").innerText=data.room_number
        document.querySelector("#room_types").innerText=data.room_type
        document.querySelector("#check_ins").innerText=data.start_date
        document.querySelector("#check_outs").innerText=data.end_date

        document.querySelector("#room_charges").innerText=data.room_charge
        //document.querySelector("#bar_charges").innerText=data.room_type
        //document.querySelector("#add_charges").innerText=data.
        document.querySelector("#taxes").innerText=data.tax
        document.querySelector("#totals").innerText=data.total
    });

})