import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg
import codeLan as cl





class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle("Encode and Decode")

        #Set the layout
        self.setLayout(qtw.QVBoxLayout())

        #Special message
        msg = qtw.QLabel("Output")
        msg.setFont(qtg.QFont("Helvetica", 20))
        self.layout().addWidget(msg)

        #Name Entry

        entry = qtw.QLineEdit()
        entry.setObjectName("word_entry")
        entry.setText("")
        self.layout().addWidget(entry)

        #button fuction

        def press(a):
            if a == "e":
                msg.setText(cl.encode(entry.text()))

            if a == "d":
                msg.setText(cl.decode(entry.text()))

        #Button

        enButton = qtw.QPushButton("Encode",
                                 clicked = lambda: press("e"))
        self.layout().addWidget(enButton)

        deButton = qtw.QPushButton("Decode",
                                   clicked = lambda: press("d"))
        self.layout().addWidget(deButton)


        #show
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

#Run

app.exec()