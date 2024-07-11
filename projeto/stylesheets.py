from PyQt6.QtWidgets import QMainWindow

def apply_stylesheets(widget):
  StyleSheet = ("""
    QWidget {
        background-color: #244855; /* cor principal de fundo */
        font-family: Arial, sans-serif;
        font-size: 14px;
        color: #FBE900; /* cor do texto */
    }
    QLabel {
        color: #FBE900; /* cor do texto dos labels */
        font-weight: bold;
    }
    QLineEdit {
        padding: 10px;
        border: 1px solid #90AEAD; /* cor da borda */
        border-radius: 5px;
        font-size: 14px;
        background-color: #874F41; /* cor de fundo dos inputs */
        color: #FBE900; /* cor do texto dos inputs */
    }
    
    QPushButton {
        background-color: #E64833; /* cor de fundo dos botões */
        color: #ffffff; /* cor do texto dos botões */
        padding: 10px 20px; /* Aumenta o padding horizontal para centralizar o texto */
        font-size: 16px;
        border: none;
        border-radius: 5px;
        margin-top: 10px;
        text-align: justify;
    }
    
    QPushButton:hover {
        background-color: #874F41; /* cor de fundo dos botões ao passar o mouse */
    }
    QTableWidget {
        background-color: #90AEAD; /* cor de fundo da tabela */
        border: 1px solid #E64833; /* cor da borda da tabela */
        border-radius: 5px;
        font-size: 14px;
        color: #244855; /* cor do texto da tabela */
    }
    QHeaderView::section {
        background-color: #E64833; /* cor de fundo do cabeçalho da tabela */
        color: #FBE900; /* cor do texto do cabeçalho da tabela */
        padding: 5px;
        border: none;
    }
""")


  widget.setStyleSheet(StyleSheet)