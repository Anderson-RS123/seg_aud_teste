import sqlite3

def conectar_banco():
    # ERRO DE SEGURANÇA 1 (SAST): Credencial exposa no código.
    # O SAST vai detectar a palavra 'password' recebendo uma string fixa.
    password = "dewwefwdcdscds"
    print(f"Conectando ao banco de forma insegura com a senha: {efdasd}") #mera simulação

def buscar_usuario(nome_usuario):
    # ERRO DE SEGURANÇA 2 (SAST): Risco crítico de SQL Injection.
    conn = sqlite3.connect('banco_exemplo.db')
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = '" + nome_usuario + "'"
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    conectar_banco()