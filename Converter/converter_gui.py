import sys
print("Which GUI do you prefer? (pyqt5/tkinter)")
gui_choice = input("Choice: ").strip().lower()

if gui_choice == "pyqt5":
    from PyQt5.QtWidgets import (
        QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox
    )
    from converter_values import L, A, V, M, T, options

    # Νέο help string για GUI
    gui_help = '''\
Unit Converter Instructions:

1. Select a unit category (e.g. Length, Area, Volume, Mass, Time).
2. Select the starting unit (From unit).
3. Enter the value you want to convert.
4. Select or type one or more target units (To unit(s)), separated by commas if more than one.
5. Click "Convert" to see the results.

To see the unit symbols, click "Symbols".
'''

    CATEGORY_MAP = {
        'Length': L,
        'Area': A,
        'Volume': V,
        'Mass': M,
        'Time': T
    }

    class ConverterGUI(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Unit Converter')
            self.init_ui()

        def init_ui(self):
            layout = QVBoxLayout()

            # Category selection
            self.category_label = QLabel('Category:')
            self.category_combo = QComboBox()
            self.category_combo.addItems(CATEGORY_MAP.keys())
            self.category_combo.currentTextChanged.connect(self.update_units)

            # From unit
            self.from_label = QLabel('From unit:')
            self.from_combo = QComboBox()

            # Value
            self.value_label = QLabel('Value:')
            self.value_edit = QLineEdit()
            self.value_edit.setPlaceholderText('Enter value')

            # To unit(s)
            self.to_label = QLabel('To unit(s):')
            self.to_combo = QComboBox()
            self.to_combo.setEditable(True)
            self.to_combo.setInsertPolicy(QComboBox.NoInsert)

            # Convert button
            self.convert_btn = QPushButton('Convert')
            self.convert_btn.clicked.connect(self.convert)

            # Result
            self.result_text = QTextEdit()
            self.result_text.setReadOnly(True)

            # Help and Symbols
            self.help_btn = QPushButton('Help')
            self.help_btn.clicked.connect(self.show_help)
            self.symbols_btn = QPushButton('Symbols')
            self.symbols_btn.clicked.connect(self.show_symbols)

            # Layouts
            row1 = QHBoxLayout()
            row1.addWidget(self.category_label)
            row1.addWidget(self.category_combo)
            row2 = QHBoxLayout()
            row2.addWidget(self.from_label)
            row2.addWidget(self.from_combo)
            row3 = QHBoxLayout()
            row3.addWidget(self.value_label)
            row3.addWidget(self.value_edit)
            row4 = QHBoxLayout()
            row4.addWidget(self.to_label)
            row4.addWidget(self.to_combo)
            row5 = QHBoxLayout()
            row5.addWidget(self.convert_btn)
            row5.addWidget(self.help_btn)
            row5.addWidget(self.symbols_btn)

            layout.addLayout(row1)
            layout.addLayout(row2)
            layout.addLayout(row3)
            layout.addLayout(row4)
            layout.addLayout(row5)
            layout.addWidget(self.result_text)

            self.setLayout(layout)
            self.update_units(self.category_combo.currentText())

        def update_units(self, category):
            units = list(CATEGORY_MAP[category].keys())
            self.from_combo.clear()
            self.from_combo.addItems(units)
            self.to_combo.clear()
            self.to_combo.addItems(units)

        def convert(self):
            category = self.category_combo.currentText()
            from_unit = self.from_combo.currentText()
            value_str = self.value_edit.text()
            to_units = self.to_combo.currentText().split(',')
            try:
                value = float(value_str)
            except ValueError:
                QMessageBox.warning(self, 'Error', 'Invalid value!')
                return
            table = CATEGORY_MAP[category]
            if from_unit not in table:
                QMessageBox.warning(self, 'Error', 'Invalid from unit!')
                return
            results = []
            for to_unit in to_units:
                to_unit = to_unit.strip()
                if to_unit not in table:
                    results.append(f"{to_unit}: Invalid unit")
                    continue
                try:
                    result = round(value * table[to_unit] / table[from_unit], 6)
                    results.append(f"{to_unit}: {result}")
                except Exception as e:
                    results.append(f"{to_unit}: Error")
            self.result_text.setText('\n'.join(results))

        def show_help(self):
            QMessageBox.information(self, 'Help', gui_help)

        def show_symbols(self):
            QMessageBox.information(self, 'Symbols', options['symbols'])

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = ConverterGUI()
        window.show()
        sys.exit(app.exec_())

elif gui_choice == "tkinter":
    import tkinter as tk
    from tkinter import ttk, messagebox
    from converter_values import L, A, V, M, T, options

    gui_help = '''\
Unit Converter Instructions:

1. Select a unit category (e.g. Length, Area, Volume, Mass, Time).
2. Select the starting unit (From unit).
3. Enter the value you want to convert.
4. Select or type one or more target units (To unit(s)), separated by commas if more than one.
5. Click "Convert" to see the results.

To see the unit symbols, click "Symbols".
'''

    CATEGORY_MAP = {
        'Length': L,
        'Area': A,
        'Volume': V,
        'Mass': M,
        'Time': T
    }

    class ConverterTk(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title('Unit Converter')
            self.geometry('400x400')
            self.create_widgets()

        def create_widgets(self):
            # Category
            tk.Label(self, text='Category:').pack()
            self.category = ttk.Combobox(self, values=list(CATEGORY_MAP.keys()), state='readonly')
            self.category.pack()
            self.category.bind('<<ComboboxSelected>>', self.update_units)
            self.category.current(0)

            # From unit
            tk.Label(self, text='From unit:').pack()
            self.from_unit = ttk.Combobox(self, state='readonly')
            self.from_unit.pack()

            # Value
            tk.Label(self, text='Value:').pack()
            self.value_entry = tk.Entry(self)
            self.value_entry.pack()

            # To unit(s) - editable ComboBox
            tk.Label(self, text='To unit(s) (comma separated):').pack()
            self.to_units = ttk.Combobox(self)
            self.to_units.pack()

            # Convert button
            tk.Button(self, text='Convert', command=self.convert).pack(pady=5)
            # Help and Symbols
            tk.Button(self, text='Help', command=self.show_help).pack(side='left', padx=10, pady=5)
            tk.Button(self, text='Symbols', command=self.show_symbols).pack(side='right', padx=10, pady=5)

            # Result
            self.result = tk.Text(self, height=10, width=40)
            self.result.pack(pady=10)

            self.update_units()

        def update_units(self, event=None):
            cat = self.category.get() if hasattr(self, 'category') else list(CATEGORY_MAP.keys())[0]
            units = list(CATEGORY_MAP[cat].keys())
            self.from_unit['values'] = units
            self.from_unit.current(0)
            self.to_units['values'] = units
            if units:
                self.to_units.set(units[0])

        def convert(self):
            cat = self.category.get()
            from_unit = self.from_unit.get()
            value_str = self.value_entry.get()
            to_units = self.to_units.get().split(',')
            try:
                value = float(value_str)
            except ValueError:
                messagebox.showwarning('Error', 'Invalid value!')
                return
            table = CATEGORY_MAP[cat]
            if from_unit not in table:
                messagebox.showwarning('Error', 'Invalid from unit!')
                return
            results = []
            for to_unit in to_units:
                to_unit = to_unit.strip()
                if to_unit not in table:
                    results.append(f"{to_unit}: Invalid unit")
                    continue
                try:
                    result = round(value * table[to_unit] / table[from_unit], 6)
                    results.append(f"{to_unit}: {result}")
                except Exception:
                    results.append(f"{to_unit}: Error")
            self.result.delete('1.0', tk.END)
            self.result.insert(tk.END, '\n'.join(results))

        def show_help(self):
            messagebox.showinfo('Help', gui_help)

        def show_symbols(self):
            messagebox.showinfo('Symbols', options['symbols'])

    if __name__ == '__main__':
        app = ConverterTk()
        app.mainloop()
else:
    print("Invalid choice. Please run the program again and select 'pyqt5' or 'tkinter'.")
