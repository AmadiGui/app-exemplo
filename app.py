from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route('/')
def hello_world():
    return 'Hello, UFABC agora com SonarQube! \o/'

# @app.route('/duplicate')
# def hello_world_duplicate():  # Função duplicada
#     return 'Hello, UFABC agora com SonarQube!'

# # Função muito longa
# def long_function():
#     if True:
#         print("This is a very long function that should be broken down into smaller functions.")
#         # Código adicional longo e complexo
#         for i in range(1000):
#             print(i)

# # Variável de senha hardcoded (má prática de segurança)
# def insecure_function():
#     password = "hardcoded_password"
#     print(f"Password is: {password}")

# # Código inalcançável
# def unreachable_code():
#     return
#     print("This code is unreachable")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    # long_function()
    # insecure_function()
    # unreachable_code()
