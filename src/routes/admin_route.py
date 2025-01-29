from flask import Flask, request, jsonify
from helpers.utils import app
from src.db import execute_query,get_db_connection

@app.route('/')
def home():
    return "TESt SERVER"

@app.route('/GET/FixAsset')
def fixedasset():
    return execute_query('SELECT * FROM "Asset"')

@app.route('/GET/Emp')
def emp():
    return execute_query('SELECT * FROM "EmpDetail"')


@app.route('/POST/adduser', methods=['POST'])
def insert():
    try:
        data = request.get_json()  # JSON
        emp_id = data.get('emp_id')
        name = data.get('name')
        last_name = data.get('last_name')
        section_code = data.get('section_code')
        print(data)

        #return jsonify({"message": f"Aldeadly Insert"}), 201

        if not all([emp_id, name, last_name, section_code]):
            return jsonify({"error": "Missing required fields"}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL INSERT INTO
        sql = """
        INSERT INTO "EmpDetail" (EmpID, Name, LastName, Section_Code)
        VALUES (%s, %s, %s, %s) RETURNING EmpID;
        """
        sql2 = """ INSERT INTO public."EmpDetail" VALUES (%s, %s, %s, %s)"""

        cursor.execute(sql2, (emp_id, name, last_name, section_code))
        #emp_id = cursor.fetchone()[0] 

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Employee added successfully!", "EmpID": emp_id}), 201
    
    except Exception as e:
         return jsonify({"error": str(e)}), 500