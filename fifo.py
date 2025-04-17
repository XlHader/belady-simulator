import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                            QSpinBox, QTextEdit, QTableWidget, QTableWidgetItem,
                            QTabWidget, QGridLayout, QGroupBox, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import random
from collections import deque

class BeladySimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador de Anomalía de Belady - FIFO")
        self.setGeometry(100, 100, 1200, 800)
        
        # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Layout principal
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        # Crear las diferentes secciones
        self.create_input_section(layout)
        self.create_simulation_section(layout)
        self.create_results_section(layout)
        
        # Aplicar estilo
        self.apply_styles()

    def create_input_section(self, parent_layout):
        input_group = QGroupBox("Configuración de Simulación")
        layout = QGridLayout()

        # Secuencia de páginas
        layout.addWidget(QLabel("Secuencia de páginas:"), 0, 0)
        self.sequence_input = QLineEdit()
        self.sequence_input.setPlaceholderText("Ingrese números separados por comas (ej: 1,2,3,4,1,2,5)")
        layout.addWidget(self.sequence_input, 0, 1, 1, 2)

        # Número de marcos
        layout.addWidget(QLabel("Marcos 1:"), 1, 0)
        self.frames1_input = QSpinBox()
        self.frames1_input.setRange(1, 10)
        self.frames1_input.setValue(3)
        layout.addWidget(self.frames1_input, 1, 1)

        layout.addWidget(QLabel("Marcos 2:"), 1, 2)
        self.frames2_input = QSpinBox()
        self.frames2_input.setRange(1, 10)
        self.frames2_input.setValue(4)
        layout.addWidget(self.frames2_input, 1, 3)

        # Botones
        button_layout = QHBoxLayout()
        self.simulate_btn = QPushButton("Simular FIFO")
        self.simulate_btn.clicked.connect(self.simulate_fifo)
        self.random_btn = QPushButton("Generar Secuencia Aleatoria")
        self.random_btn.clicked.connect(self.generate_random_sequence)
        self.clear_btn = QPushButton("Limpiar")
        self.clear_btn.clicked.connect(self.clear_all)
        
        button_layout.addWidget(self.simulate_btn)
        button_layout.addWidget(self.random_btn)
        button_layout.addWidget(self.clear_btn)
        
        layout.addLayout(button_layout, 2, 0, 1, 4)
        
        input_group.setLayout(layout)
        parent_layout.addWidget(input_group)

    def create_simulation_section(self, parent_layout):
        self.tab_widget = QTabWidget()
        
        # Tab para cada simulación
        self.sim1_table = QTableWidget()
        self.sim2_table = QTableWidget()
        
        self.tab_widget.addTab(self.sim1_table, "Simulación Marcos 1")
        self.tab_widget.addTab(self.sim2_table, "Simulación Marcos 2")
        
        parent_layout.addWidget(self.tab_widget)

    def create_results_section(self, parent_layout):
        results_group = QGroupBox("Resultados")
        layout = QVBoxLayout()
        
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        layout.addWidget(self.results_text)
        
        results_group.setLayout(layout)
        parent_layout.addWidget(results_group)

    def apply_styles(self):
        # Estilo para los botones
        button_style = """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """
        
        # Estilo para los grupos
        group_style = """
            QGroupBox {
                font-weight: bold;
                border: 2px solid #4CAF50;
                border-radius: 6px;
                margin-top: 6px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 7px;
                padding: 0px 5px 0px 5px;
            }
        """
        
        self.setStyleSheet(button_style + group_style)

    def fifo_page_replacement(self, sequence, num_frames):
        frames = deque(maxlen=num_frames)
        page_faults = 0
        simulation_history = []
        fault_history = []

        for page in sequence:
            is_fault = False
            if page not in frames:
                page_faults += 1
                is_fault = True
                if len(frames) == num_frames:
                    frames.popleft()
                frames.append(page)
            simulation_history.append(list(frames))
            fault_history.append(is_fault)

        return simulation_history, page_faults, fault_history

    def update_simulation_table(self, table, sequence, history, faults, num_frames):
        table.clear()
        table.setRowCount(num_frames + 1)  # +1 para la fila de fallos
        table.setColumnCount(len(sequence))
        
        # Establecer encabezados
        table.setHorizontalHeaderLabels([str(x) for x in sequence])
        table.setVerticalHeaderLabels(['Marco ' + str(i+1) for i in range(num_frames)] + ['Fallo'])

        # Llenar la tabla
        for col, (state, is_fault) in enumerate(zip(history, faults)):
            # Llenar marcos
            for row in range(num_frames):
                item = QTableWidgetItem()
                if row < len(state):
                    item.setText(str(state[row]))
                else:
                    item.setText('-')
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row, col, item)
            
            # Marcar fallos
            fault_item = QTableWidgetItem('F' if is_fault else '')
            fault_item.setTextAlignment(Qt.AlignCenter)
            if is_fault:
                fault_item.setBackground(QColor(255, 200, 200))
            table.setItem(num_frames, col, fault_item)

        # Ajustar tamaño de columnas
        table.resizeColumnsToContents()

    def simulate_fifo(self):
        try:
            sequence = [int(x.strip()) for x in self.sequence_input.text().split(',')]
            frames1 = self.frames1_input.value()
            frames2 = self.frames2_input.value()

            # Simular con ambos números de marcos
            history1, faults1, fault_history1 = self.fifo_page_replacement(sequence, frames1)
            history2, faults2, fault_history2 = self.fifo_page_replacement(sequence, frames2)

            # Actualizar tablas
            self.update_simulation_table(self.sim1_table, sequence, history1, fault_history1, frames1)
            self.update_simulation_table(self.sim2_table, sequence, history2, fault_history2, frames2)

            # Mostrar resultados
            result_text = f"Resultados de la simulación:\n\n"
            result_text += f"Con {frames1} marcos: {faults1} fallos\n"
            result_text += f"Con {frames2} marcos: {faults2} fallos\n\n"

            if faults2 > faults1:
                result_text += "¡ANOMALÍA DE BELADY DETECTADA!\n"
                result_text += f"Más marcos ({frames2}) resultaron en más fallos ({faults2}) "
                result_text += f"que menos marcos ({frames1}, {faults1} fallos)"
            else:
                result_text += "No se detectó anomalía de Belady en esta secuencia."

            self.results_text.setText(result_text)

        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingrese una secuencia válida de números separados por comas.")

    def generate_random_sequence(self):
        length = random.randint(10, 15)
        max_page = 5
        sequence = [random.randint(1, max_page) for _ in range(length)]
        self.sequence_input.setText(','.join(map(str, sequence)))
        self.simulate_fifo()

    def clear_all(self):
        self.sequence_input.clear()
        self.frames1_input.setValue(3)
        self.frames2_input.setValue(4)
        self.sim1_table.clear()
        self.sim2_table.clear()
        self.results_text.clear()

def main():
    app = QApplication(sys.argv)
    
    # Establecer estilo global
    app.setStyle('Fusion')
    
    # Crear y mostrar la ventana
    window = BeladySimulator()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
