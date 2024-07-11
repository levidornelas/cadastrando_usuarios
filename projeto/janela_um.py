from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import requests
from database import cadastrar_usuario, atualizar_usuarios, deletar_usuarios
from api_cpf import verifica_cpf
from stylesheets import apply_stylesheets


class JanelaPrincipal_um(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexão com o banco!")
        self.setFixedSize(643, 650)
        self.show()  # Faz a tela ser exibida
        apply_stylesheets(self)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)  # Adicionando central_widget como o widget central

        main_layout = QVBoxLayout(central_widget)
        form_layout = QFormLayout()

        # Campos do formulário
        self.cpf_input = QLineEdit()
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.cep_input = QLineEdit()
        self.rua_input = QLineEdit()
        self.bairro_input = QLineEdit()
        self.cidade_input = QLineEdit()
        self.estado_input = QLineEdit()

        # Criando o formulário com 'FormLayout.'
        form_layout.addRow("CPF:", self.cpf_input)
        self.cpf_input.editingFinished.connect(self.validar_cpf)  # Conectando a função de validação de CPF ao campo de inserção de texto, assim que a digitação no campo é finalizada.
        self.cpf_input.setInputMask('000.000.000-00')  # Uma 'InputMask' serve para deixar a inserção das informações mais intuitiva ao usuário.

        form_layout.addRow("Nome:", self.name_input)        
        form_layout.addRow("Idade:", self.age_input)
        form_layout.addRow("CEP:", self.cep_input)
        self.cep_input.editingFinished.connect(self.consulta_cep)  # Conectando a função de buscar o CEP digitado, assim que a digitação no campo é finalizada.
        self.cep_input.setInputMask('00000-000')

        form_layout.addRow("Rua:", self.rua_input)
        form_layout.addRow("Bairro:", self.bairro_input)
        form_layout.addRow("Cidade:", self.cidade_input)
        form_layout.addRow("Estado:", self.estado_input)

        main_layout.addLayout(form_layout) #Adicionando o layout de formulário ao Layout principal.

        # Botão para cadastrar aluno
        self.submit_button = QPushButton("Cadastrar usuário")
        self.submit_button.clicked.connect(self.registrar_usuario)
        main_layout.addWidget(self.submit_button, Qt.AlignmentFlag.AlignLeft)

        self.update_button = QPushButton("Atualizar usuário")
        self.update_button.clicked.connect(self.atualizando)
        main_layout.addWidget(self.update_button, Qt.AlignmentFlag.AlignCenter)

        self.delete_button = QPushButton("Deletar usuário")
        self.delete_button.clicked.connect(self.deletando)
        main_layout.addWidget(self.delete_button, Qt.AlignmentFlag.AlignCenter)

        self.skip_button = QPushButton('Listagem de usuários')
        self.skip_button.clicked.connect(self.tela_listagem)
        main_layout.addWidget(self.skip_button)

        # Label para mostrar o status
        self.status_label = QLabel('')
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignJustify)
        main_layout.addWidget(self.status_label)

        self.setCentralWidget(central_widget)  # Exibindo widget na tela: !!! Importante.
        central_widget.setLayout(main_layout)  # Adicionando o 'main_layout' ao central widget.


    def consulta_cep(self):
        cep = self.cep_input.text().strip().replace('-', '')

        if len(cep) != 8 or not cep.isdigit():
            QMessageBox.warning(self, 'Atenção', 'Por favor insira um CEP válido.')
            return

        try:
            resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            resposta.raise_for_status()
            dados = resposta.json()

            if 'erro' in dados:
                QMessageBox.warning(self, 'Atenção', 'CEP não encontrado.')
            else:
                self.rua_input.setText(dados.get('logradouro', ''))
                self.bairro_input.setText(dados.get('bairro', ''))
                self.cidade_input.setText(dados.get('localidade', ''))
                self.estado_input.setText(dados.get('uf', ''))

        except requests.exceptions.RequestException:
            QMessageBox.critical(self, 'Erro', 'Houve um erro ao procurar o CEP.')

    def validar_cpf(self):
        cpf = self.cpf_input.text()

        if verifica_cpf(cpf):
            pass
        else:
            QMessageBox.critical(self, 'Erro', 'CPF inválido.')
            return

    def registrar_usuario(self):
        # Obter dados do formulário
        cpf = self.cpf_input.text()
        name = self.name_input.text()
        age = self.age_input.text()
        cep = self.cep_input.text()
        rua = self.rua_input.text()
        bairro = self.bairro_input.text()
        cidade = self.cidade_input.text()
        estado = self.estado_input.text()

        # Chamar a função para inserir dados no banco de dados
        status = cadastrar_usuario(cpf, name, age, cep, rua, bairro, cidade, estado)
        self.status_label.setText(status)

        #Limpando os dados para o preenchimento de outro usuário:
        self.cpf_input.clear()
        self.name_input.clear()
        self.age_input.clear()
        self.cep_input.clear()
        self.rua_input.clear()
        self.bairro_input.clear()
        self.cidade_input.clear()
        self.estado_input.clear()

    def atualizando(self):  # Chamando a função para atualizar usuários, de 'database.py'
        cpf = self.cpf_input.text()
        name = self.name_input.text()
        age = self.age_input.text()
        cep = self.cep_input.text()
        rua = self.rua_input.text()
        bairro = self.bairro_input.text()
        cidade = self.cidade_input.text()
        estado = self.estado_input.text()

        status = atualizar_usuarios(cpf, name, age, cep, rua, bairro, cidade, estado)
        self.status_label.setText(status)

    def deletando(self):  # Chamando a função para deletar usuários, de 'database.py'
        cpf = self.cpf_input.text()
        status = deletar_usuarios(cpf)

        self.status_label.setText(status)
        self.cpf_input.clear()

    def tela_listagem(self):
        from janela_dois import JanelaPrincipal_dois
        
        self.janela_listagem = JanelaPrincipal_dois()
        self.janela_listagem.show()
        self.close()
