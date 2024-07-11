from PyQt6.QtWidgets import QMainWindow

def apply_stylesheets(widget):
  StyleSheet = ("""
    QWidget {
        background-color: #013F3E; /* cor principal de fundo */
        font-family: Arial, sans-serif;
        font-size: 14px;
        color: #E9E0CE; /* cor do texto */
    }
    QLabel {
        color: #E9E0CE; /* cor do texto dos labels */
        font-weight: bold;
    }
    QLineEdit {
        padding: 10px;
        border: 1px solid #2B3036; /* cor da borda */
        border-radius: 5px;
        font-size: 14px;
        background-color: #2B3036; /* cor de fundo dos inputs */
        color: #E9E0CE; /* cor do texto dos inputs */
    }
    
    QPushButton {
        background-color: #3FA796; /* nova cor de fundo dos botões */
        color: #E9E0CE; /* cor do texto dos botões */
        padding: 10px 20px; /* Aumenta o padding horizontal para centralizar o texto */
        font-size: 16px;
        border: none;
        border-radius: 5px;
        margin-top: 10px;
        text-align: justify;
    }
    
    QPushButton:hover {
        background-color: #2B3036; /* cor de fundo dos botões ao passar o mouse */
    }
    QTableWidget {
        background-color: #2B3036; /* cor de fundo da tabela */
        border: 1px solid #3FA796; /* nova cor da borda da tabela */
        border-radius: 5px;
        font-size: 14px;
        color: #E9E0CE; /* cor do texto da tabela */
    }
    QHeaderView::section {
        background-color: #3FA796; /* nova cor de fundo do cabeçalho da tabela */
        color: #E9E0CE; /* cor do texto do cabeçalho da tabela */
        padding: 5px;
        border: none;
    }
""")


  widget.setStyleSheet(StyleSheet)