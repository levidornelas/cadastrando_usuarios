import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon 
from PyQt6.QtCore import Qt
from stylesheets import apply_stylesheets
from janela_um import JanelaPrincipal_um
from janela_dois import JanelaPrincipal_dois

class JanelaPrincipal(QMainWindow): #classe principal que vai conter elementos  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexão com o banco!")
        self.setFixedSize(643, 680)
        self.show() # faz a tela ser exibida
        apply_stylesheets(self)
       

        #Criando os widgets para mudança de tela:
        self.troca_telas = QStackedWidget()
        self.janela_um = JanelaPrincipal_um()
        self.janela_dois = JanelaPrincipal_dois()
        
        
        self.troca_telas.addWidget(self.janela_um)
        self.troca_telas.addWidget(self.janela_dois)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.troca_telas)

        self.botao_janela_um = QPushButton("Cadastro de usuários")
        self.botao_janela_um.clicked.connect(self.mudar_para_janela_um)
        botao_janela_um_layout = QHBoxLayout()
        botao_janela_um_layout.addWidget(self.botao_janela_um)
        botao_janela_um_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addLayout(botao_janela_um_layout)

        # Botão para a segunda janela
        self.botao_janela_dois = QPushButton("Lista de usuários cadastrados")
        self.botao_janela_dois.clicked.connect(self.mudar_para_janela_dois)
        botao_janela_um_layout.addWidget(self.botao_janela_dois)
        botao_janela_um_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    
    def mudar_para_janela_um(self):
        self.troca_telas.setCurrentWidget(self.janela_um)
    
    def mudar_para_janela_dois(self):
        self.troca_telas.setCurrentWidget(self.janela_dois)
        self.janela_dois.atualizar()



qt = QApplication(sys.argv) #variavel qt instanciando a classe QApplication: permite usar recursos do SO
app = JanelaPrincipal() #instaciando a classe
sys.exit(qt.exec()) #encerra totalmente a aplicação assim que fechada
