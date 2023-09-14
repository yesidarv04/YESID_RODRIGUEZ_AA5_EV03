from flask import Flask, request, jsonify

app = Flask(__name__)

# Diccionario para almacenar notificaciones por usuario
notifications = {}

# Ruta para enviar notificaciones
@app.route('/notificaciones', methods=['POST'])
def enviar_notificacion():
    data = request.json
    destinatario = data.get('destinatario')
    mensaje = data.get('mensaje')

    # Verificar si el usuario ya tiene notificaciones
    if destinatario not in notifications:
        notifications[destinatario] = []

    notifications[destinatario].append({'mensaje': mensaje})

    return jsonify({'mensaje': 'Notificación enviada exitosamente'})

# Ruta para ver notificaciones por usuario
@app.route('/notificaciones/<usuario>', methods=['GET'])
def obtener_notificaciones(usuario):
    if usuario in notifications:
        notificaciones_usuario = notifications[usuario]
        return jsonify({'notificaciones': notificaciones_usuario})
    else:
        return jsonify({'mensaje': 'No hay notificaciones para este usuario'})

if __name__ == '__main__':
    app.run(debug=True)
