from PyQt6.QtWidgets import QMainWindow

def apply_stylesheets(widget):
  StyleSheet = ("""
            QWidget {
            background-color: #2e2e2e;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #ffffff;
        }
        QLabel {
            color: #ffffff;
            font-weight: bold;
        }
        QLineEdit {
            padding: 10px;
            border: 1px solid #444;
            border-radius: 5px;
            font-size: 14px;
            background-color: #444;
            color: #ffffff;
        }
                
        QPushButton {
        background-color: #00008B;
        color: white;
        padding: 10px 20px; /* Aumenta o padding horizontal para centralizar o texto */
        font-size: 16px;
        border: none;
        border-radius: 5px;
        margin-top: 10px;
        text-align: justify;
        }
                
        QPushButton:hover {
            background-color: #4169E1;
        }
        QTableWidget {
            background-color: #4F4F4F;
            border: 1px solid #555;
            border-radius: 5px;
            font-size: 14px;
            color: #ffffff;
        }
        QHeaderView::section {
            background-color: #4682B4;
            color: white;
            padding: 5px;
            border: none;
        }
        """)

  widget.setStyleSheet(StyleSheet)