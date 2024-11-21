import oracledb
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5000", "http://localhost:3000"])


def get_conexao():
    return oracledb.connect(
        user="rm555997", password="090705", dsn="oracle.fiap.com.br/orcl"
    )


@app.route("/login", methods=["POST"])
def recupera_login():
    try:
        data = request.get_json()
        email = data.get("email")
        senha = data.get("senha")

        if not email or not senha:
            return jsonify({"error": "Email e senha são obrigatórios"}), 400

        with get_conexao() as conexao:
            with conexao.cursor() as cursor:
                sql = "SELECT idCliente, email FROM HUOLI_CLIENTE WHERE email = :email AND senha = :senha"
                cursor.execute(sql, {"email": email, "senha": senha})
                reg = cursor.fetchone()
                if reg:
                    return jsonify({
                        "message": "Login bem-sucedido",
                        "email": reg[1],
                        "idCliente": reg[0]
                    }), 200
                else:
                    return jsonify({"error": "Email ou senha inválido"}), 401

    except oracledb.Error as e:
        return jsonify({"error": f"Erro ao acessar o banco de dados: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/find-eletrodomesticos", methods=["GET"])
def get_eletrodomesticos():
    try:
        email = request.args.get("email")
        if not email:
            return jsonify({"error": "Email não fornecido"}), 400

        with get_conexao() as conexao:
            with conexao.cursor() as cursor:
                # Consultando o ID do cliente a partir do email
                sql_cliente = (
                    "SELECT idCliente FROM HUOLI_CLIENTE WHERE email = :email"
                )
                cursor.execute(sql_cliente, {"email": email})
                cliente = cursor.fetchone()

                if not cliente:
                    return jsonify({"error": "Cliente não encontrado"}), 404

                idCliente = cliente[0]

                # Consultando os eletrodomésticos do cliente
                sql_eletrodomesticos = """
                    SELECT idEletrodomestico, nome, marca, custoEstimado
                    FROM HUOLI_ELETRODOMESTICO
                    WHERE idCliente = :idCliente
                """
                cursor.execute(sql_eletrodomesticos, {"idCliente": idCliente})
                eletrodomesticos = cursor.fetchall()

                # Convertendo para uma lista de dicionários
                eletrodomesticos_list = [
                    {
                        "idEletrodomestico": row[0],
                        "nome": row[1],
                        "marca": row[2],
                        "custoEstimado": row[3],
                    }
                    for row in eletrodomesticos
                ]

                return jsonify(eletrodomesticos_list), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
