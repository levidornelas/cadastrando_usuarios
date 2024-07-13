import psycopg2

#A maioria dos campos estão vazios por motivos de segurança, ainda que se trate apenas de um projeto pessoal.
DATABASE = 'senac'
PORT = '1144' 
USER = 'postgres'
PASSWORD = '1144' 
HOST = 'localhost'

def cadastrar_usuario(cpf, nome, idade, cep, rua, bairro, cidade, estado):
    try:
        # Conexão ao banco de dados PostgreSQL
        connection = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )

        cursor = connection.cursor()
        # Inserir dados do aluno
        inserir_sql = """INSERT INTO usuarios (cpf, nome, idade, cep, rua, bairro, cidade, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        gravar_insert = (cpf, nome, idade, cep, rua, bairro, cidade, estado)
        cursor.execute(inserir_sql, gravar_insert)
        connection.commit() #garantir que todas as alterações sejam refletidas permanentemente no banco.
        cursor.close()
        connection.close()
        return "Usuário cadastrado com sucesso!"
    except Exception as e:
        return f"Erro ao cadastrar: {e}"


def listar_usuarios():
    try:
        # Conexão ao banco de dados PostgreSQL
        connection = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )

        cursor = connection.cursor()
        # Selecionar todos os usuários
        cursor.execute("SELECT * FROM usuarios")
        users = cursor.fetchall() #retorna todos os valores da tabela
        cursor.close()
        connection.close()

        return users
    except Exception as e:
        return f"Erro ao listar cadastros: {e}"

def atualizar_usuarios(cpf,nome, idade, cep, rua, bairro, cidade, estado):
    try:
            # Conexão ao banco de dados PostgreSQL
        connection = psycopg2.connect(
                database=DATABASE,
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT
            )

        cursor = connection.cursor()
        # Atualizar os dados:
        atualizar_sql = """UPDATE usuarios SET nome = %s, idade = %s, cep = %s, rua = %s, bairro = %s, cidade = %s, estado = %s WHERE cpf = %s"""
        atualizar_dados = (nome, idade, cep, rua, bairro, cidade, estado, cpf)
        cursor.execute(atualizar_sql, atualizar_dados)
        connection.commit()
        cursor.close()
        connection.close()
        return "Dados atualizados com sucesso!"

    except Exception as e:
        return f"Erro ao atualizar usuários: {e}"    


def deletar_usuarios(cpf):
    try:
            # Conexão ao banco de dados PostgreSQL
        connection = psycopg2.connect(
                database=DATABASE,
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT
            )
        
        cursor = connection.cursor()
        deletar_sql = "DELETE FROM usuarios WHERE cpf = %s"
        cursor.execute(deletar_sql, (cpf,))
        connection.commit()
        cursor.close()
        connection.close()
        return "Cadastro deletado com sucesso!"

    except Exception as e:
        return f'Erro ao excluir usuarios: {e}'

def register_users(username,password):
    try:
        # Conexão ao banco de dados PostgreSQL
        connection = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        cursor = connection.cursor()
        # Inserir dados do aluno
        inserir_sql = """INSERT INTO users (username,password) VALUES (%s, %s)"""
        gravar_insert = (username,password)
        cursor.execute(inserir_sql, gravar_insert)
        connection.commit() #garantir que todas as alterações sejam refletidas permanentemente no banco.
        cursor.close()
        connection.close()
        return "Usuário cadastrado com sucesso!"
    
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")

def check_login(username,password):
    try:
        # Conexão ao banco de dados PostgreSQL
        conexao = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        cursor = conexao.cursor()
        consulta = "SELECT username, password FROM users WHERE username = %s AND password = %s"
        cursor.execute(consulta, (username, password))
        user = cursor.fetchone()
        cursor.close()
        conexao.close()
        
        if user:
            return 'Login realizado com sucesso.'
        else:
            return 'Login ou senha estão incorretos.'
        
    except psycopg2.Error as e:
        print(f"Erro ao verificar usuário: {e}")
        return 'Erro ao verificar usuário.'
    