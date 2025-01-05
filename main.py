import sys 
import json
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class ElementsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.element_label = QLabel("Enter element symbol: ", self)
        self.element_input = QLineEdit(self) 
        self.get_info_button = QPushButton("Get Element Info", self)
        self.result_label = QLabel(self)
        # Element data sourced from the Periodic Table API
        # https://github.com/thetechnohack/Periodic-Table-API
        self.load_data()
        self.initUI()

    def load_data(self):
        json_file_path = "data.json"

        try: 
            with open(json_file_path, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = None 
            print(f"Error: The file {json_file_path} was not found")
        except json.JSONDecodeError:
            self.data = None 
            print("The json file is corrupted or not valid")

    def initUI(self):
        self.setWindowTitle("Chemical Element App")
        self.setGeometry(600, 200, 500, 500)

        vbox = QVBoxLayout()
        vbox.addWidget(self.element_label)
        vbox.addWidget(self.element_input)
        vbox.addWidget(self.get_info_button)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)

        self.element_label.setAlignment(Qt.AlignCenter)
        self.element_input.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)

        self.element_label.setObjectName("element_label")
        self.element_input.setObjectName("element_input")
        self.get_info_button.setObjectName("get_info_button")
        self.result_label.setObjectName("result_label")

        self.setStyleSheet("""
        /* General styling */
        QWidget{
            background-color: #f4f4f9;
            font-family: 'Times New Roman', serif;;
            color: #333;
        }
        QLabel, QLineEdit, QPushButton{
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
        }
        /* Styling for labels */
        QLabel#element_label{
            font-size: 32px;
            font-style: normal;
            color: #2C3E50;
        }
        QLabel#result_label{
            font-size: 24px;
            color: #3498db;
            background-color: #ecf0f1;
            padding: 20px;
            margin-top: 15px;
            text-align: center;
            border: 2px solid #3498db;
        }
        /* Styling for input fields */
        QLineEdit#element_input{
            background-color: #ffffff;
            border: 2px solid #95a5a6;
            font-size: 30px;
            color: #7f8c8d;         
        }
        QLineEdit#element_input:focus{
            border: 2px solid #3498db;
            box-shadow: 0 0 5px rgba(52, 152, 219, 0.7);
        }
        /* Styling for buttons */
        QPushButton#get_info_button{
            background-color: #3498db;
            color: white;
            border: none;
            font-size: 20px;
            padding: 15px 75px;
            cursor: pointer;
        }
        QPushButton#get_info_button:hover{
            background-color: #2980b9;
        }
        QPushButton#get_info_button:pressed{
            background-color: #1c6381;
        }
        /* Styling for spacing and layout */
        QVBoxLayout{
            spacing: 20px;
            margin: 30px;
        }
    """)

        self.get_info_button.clicked.connect(self.get_element_info)

    def get_element_info(self):
        symbol = self.element_input.text().upper().strip()
        element = None 
        for item in self.data:
            if item['symbol'].upper() == symbol:
                element = item 
                break

        if element:
            result = f"Element: {element['name']}\n" \
                     f"Symbol: {element['symbol']}\n" \
                     f"Atomic Number: {element['atomicNumber']}\n" \
                     f"Atomic Mass: {element['atomicMass']}\n" \
                     f"Electronegativity: {element['electronegativity']}\n" \
                     f"Atomic Radius: {element['atomicRadius']} pm\n" \
                     f"Ion Radius: {element['ionRadius']}\n" \
                     f"Van Der Waals Radius: {element['vanDerWaalsRadius']} pm\n" \
                     f"Ionization Energy: {element['ionizationEnergy']} kJ/mol\n" \
                     f"Electron Affinity: {element['electronAffinity']} kJ/mol\n" \
                     f"Oxidation States: {element['oxidationStates']}\n" \
                     f"Standard State: {element['standardState']}\n" \
                     f"Bonding Type: {element['bondingType']}\n" \
                     f"Melting Point: {element['meltingPoint']} K\n" \
                     f"Boiling Point: {element['boilingPoint']} K\n" \
                     f"Density: {element['density']} g/cm³\n" \
                     f"Group Block: {element['groupBlock']}\n" \
                     f"Year Discovered: {element['yearDiscovered']}"
            self.result_label.setText(result)
            
        else:
            result = self.result_label.setText("Element not found. Please check the symbol and try again")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    periodic_table = ElementsApp()
    periodic_table.show()
    sys.exit(app.exec_())