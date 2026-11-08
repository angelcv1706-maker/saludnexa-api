from flask import Flask, jsonify

# Beanstalk busca por defecto la variable 'application'
application = Flask(__name__)

@application.route('/')
def health_check():
    # Ruta base para que el Load Balancer verifique que el servidor está vivo
    return jsonify({
        "estado": "Activo",
        "servicio": "SaludNexa Core API",
        "version": "1.0.0",
        "entorno": "Produccion-Beanstalk"
    })

@application.route('/api/v1/pacientes')
def get_pacientes():
    # Simula una consulta a la base de datos de pacientes
    pacientes = [
        {"id": 1, "nombre": "Carlos Rojas", "edad": 45, "diagnostico": "Hipertensión"},
        {"id": 2, "nombre": "María López", "edad": 32, "diagnostico": "Chequeo general"}
    ]
    return jsonify({"success": True, "data": pacientes})

@application.route('/api/v1/citas')
def get_citas():
    # Simula una consulta de citas médicas
    citas = [
        {"id": 101, "paciente_id": 1, "fecha": "2026-11-10", "especialidad": "Cardiología"},
        {"id": 102, "paciente_id": 2, "fecha": "2026-11-12", "especialidad": "Medicina General"}
    ]
    return jsonify({"success": True, "data": citas})

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)