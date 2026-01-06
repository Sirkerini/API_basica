from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, prueba de api "

@app.route("/cuadrado/<numero>")
def cuadrado(numero):
    numero_int = int(numero)
    resultado = numero_int ** 2
    return jsonify({
        "numero": numero_int, 
        "cuadrado": resultado
                   })

@app.route("/multiplicar", methods = ["POST"])
def multiplicar():
    data = request.json

    if "numero1" not in data or "numero2" not in data:
        return({"error":"Falta numeros para realizar la operacion"}), 400
    
    try:
        a = float(data["numero1"])
        b = float(data["numero2"])
    except ValueError:
        return jsonify({"error": "Solo se admiten numeros"}), 400


    resultado = data["numero1"] * data["numero2"]
    return jsonify({"Resultado": resultado})

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculadora", methods=["POST"])
def calculadora():
    data = request.json
    
    if "operacion" not in data or "numero1" not in data or "numero2" not in data:
        return jsonify({"error": "Faltan datos"}), 400

    try:
        numero1 = float(data["numero1"])
        numero2 = float(data["numero2"])
    except ValueError:
        return jsonify({"error": "Los valores deben ser números"}), 400

    operacion = data["operacion"]
    if operacion not in ["sumar", "restar", "multiplicar", "dividir"]:
        return jsonify({"error": "Operación no válida"}), 400
    
    if operacion == "sumar":
        resultado = numero1 + numero2
    elif operacion == "restar":
        resultado = numero1 - numero2
    elif operacion == "multiplicar":
        resultado = numero1 * numero2
    elif operacion == "dividir":
        if numero2 == 0:
            return jsonify({"error": "No se puede dividir entre 0"}), 400
        resultado = numero1 / numero2

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)


