from flask import Flask, redirect
from flask_cors import CORS
from flask import request, jsonify
from flask import render_template
import json
import datetime as dt

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db.crud import fetch_customer_by_id, fetch_customer_by_card_number
from src.db.customer_utils import insert_customer_information, fetch_customer_information, fetch_customer_information_by_name
from src.db.credit_card_utils import insert_credit_card_information, fetch_card_information
from src.db.room_information_utils import insert_room_information, fetch_room_information
from src.db.reservation_utils import insert_reservation_information,fetch_reservation_information
from src.db.employee_utils import insert_employee_information

def make_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def home_page():
        return render_template('main-menu.html')
    
    @app.route("/main-menu.html")
    def redirect_to_home():
        return redirect("/", code=302)

    @app.route("/new-reservation-existing-or-new-customer.html")
    def new_reservation_page():
        return render_template('new-reservation-existing-or-new-customer.html')

    @app.route("/new-customer.html")
    def create_reservation_page():
        return render_template('new-customer.html')

    @app.route("/new-reservation-creation.html")
    def proceed_reservation_page():
        return render_template('new-reservation-creation.html')
    
    @app.route("/customer-checkout.html")
    def customer_checkout_page():
        return render_template('customer-checkout.html')

    @app.route("/room-information.html")
    def room_information_page():
        return render_template('room-information.html')
    
    @app.route("/reservation-information.html")
    def reservation_information_page():
        return render_template('reservation-information.html')

    @app.route("/customer-information.html")
    def customer_information_page():
        return render_template('customer-information.html')

    #customer, reservation, info for other tables in different pages, otherwise lot of info
    @app.route("/check_in_customer", methods=["POST"])
    def check_in_customer_info():
        first_name = request.headers.get("first_name")
        last_name = request.headers.get("last_name")
        number = request.headers.get("phone_number")
        email = request.headers.get("email")
        street = request.headers.get("street")
        state = request.headers.get("state")
        country = request.headers.get("country")
        id_number = request.headers.get("id_number")
        doc_type = request.headers.get("id_type")
        notes = request.headers.get("notes")

        status = insert_customer_information(first_name,last_name,number,email,street,state,country,id_number,doc_type,notes)

        if status is False:
            return jsonify("Error in inserting customer info")

        #credit card info
        full_name = first_name + " " + last_name
        card_number = request.headers.get("card_number")
        exp_date = request.headers.get("expiration_date")
        cvv = request.headers.get("cvv")

        print("full name is " + full_name)
        print("card number " + card_number)
        print("exp date " + exp_date)
        print("cvv " + cvv)

        card_update_status = insert_credit_card_information(full_name, card_number,exp_date,cvv)
        if card_update_status is False:
            return jsonify("Error in Credit card number informatio")

        return jsonify("success")


    
    @app.route("/customer_room_check_in", methods=["POST"])
    def check_in_room_info():
        employee_full_name = request.headers.get("employee_full_name")
        customer_full_name = request.headers.get("full_name")

        # Room Information
        price = request.headers.get("rate")
        max_occupancy = request.headers.get("max_occupancy")
        room_type = request.headers.get("room_type")
        room_number = request.headers.get("room_number")

        room_information_status = insert_room_information(customer_full_name, room_number, room_type, price, max_occupancy)
        if room_information_status is False:
            return jsonify("Error in room information")

        #reservation
        start_date = request.headers.get("check_in")
        end_date = request.headers.get("check_out")
        reservation_date = dt.datetime.utcnow()
        guest_number = request.headers.get("guest_number")
        notes = request.headers.get("notes")

        employee_status = insert_employee_information(employee_full_name)
        if employee_status is False:
            return jsonify("Employee fullname can't be null")

        reservation_status = insert_reservation_information(customer_full_name,start_date,end_date,reservation_date,guest_number,notes)
        if reservation_status is False:
            return jsonify("Error in reservation status")
        
        return jsonify("success")

    
    @app.route("/room_lookup", methods=["POST"])
    def lookup_room_info():
        room_number = request.headers.get("room_number")
        result = fetch_room_information(room_number)
        return jsonify(result)
    
    @app.route("/customer_lookup", methods=["POST"])
    def lookup_customer_info():
        full_name = request.headers.get("full_name")
        email = request.headers.get("email")
        dict1 = fetch_customer_information(email)[0]
        dict2 = fetch_card_information(full_name)[0]
        dict2.update(dict1)

        return jsonify(dict2)


    @app.route("/reservation_lookup", methods=["POST"])
    def lookup_reservation_info():
        start_date = request.headers.get("check_in")
        reservation_dict = fetch_reservation_information(start_date)[0]

        room_number = request.headers.get("room_number")
        room_info_dict = fetch_room_information(room_number)[0]
        room_info_dict.update(reservation_dict)
        return jsonify(room_info_dict)


    @app.route("/check_out_customer", methods=["POST"])
    def generate_bill():
        room_number = request.headers.get("room_number")
        room_info_dict = fetch_room_information(room_number)[0]

        full_name = request.headers.get("full_name")
        name = full_name.split(" ")
        first_name = name[0]
        last_name = name[1]

        customer_dict = fetch_customer_information_by_name(first_name, last_name)
        room_info_dict.update(customer_dict)
        room_info_dict['room_charge'] = 350
        room_info_dict['tax'] = 25
        room_info_dict['total'] = room_info_dict['room_charge'] + room_info_dict['tax']

        return jsonify(room_info_dict)



    return app

    

