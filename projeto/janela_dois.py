from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon 
from PyQt6.QtCore import Qt
from database import listar_usuarios
from stylesheets import apply_stylesheets

class JanelaPrincipal_dois(QMainWindow): #classe principal que vai conter elementos  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexão com o banco!")
        self.setFixedSize(520,500)
        self.setWindowIcon(QIcon('')) #apontando para imagem que está no mesmo diretório
        self.show() # faz a tela ser exibida
        
        apply_stylesheets(self)

        main_layout = QVBoxLayout()
        tela_principal = QWidget()
        tela_principal.setLayout(main_layout)
        self.setCentralWidget(tela_principal)
    
        self.apresentacao = QLabel('Olá. Esses são todos os usuários cadastrados até o momento:')
        main_layout.addWidget(self.apresentacao, Qt.AlignmentFlag.AlignLeft)
    
        self.table = QTableWidget()
        self.table.setColumnCount(8)  # Oito colunas para CPF, Nome, Idade, CEP, Rua, Bairro, Cidade, Estado
        self.table.setHorizontalHeaderLabels(["CPF", "Nome", "Idade", "CEP", "Rua", "Bairro", "Cidade", "Estado"])
        self.table.setMinimumSize(643, 400)
        main_layout.addWidget(self.table, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.voltar_botao = QPushButton('Voltar')
        self.voltar_botao.clicked.connect(self.voltar_tela)
        main_layout.addWidget(self.voltar_botao)

        self.carregar_usuarios()

    def carregar_usuarios(self):
        # Limpar tabela inicialmente
        self.table.setRowCount(0)

        # Obter lista de alunos cadastrados (lista de tuplas)
        usuarios = listar_usuarios()

        # Preencher tabela com os dados dos alunos
        for linha, usuario in enumerate(usuarios):
            self.table.insertRow(linha)
            # Inserir todos os campos na tabela
            for coluna, dado in enumerate(usuario):
                item = QTableWidgetItem(str(dado))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Desabilitar edição
                self.table.setItem(linha, coluna, item)

        # Ajustar a largura das colunas automaticamente
        self.table.resizeColumnsToContents()

    def atualizar(self):
        self.carregar_usuarios()

    def voltar_tela(self):
        from janela_um import JanelaPrincipal_um

        self.janelacadastro = JanelaPrincipal_um()
        self.janelacadastro.show()
        self.close()