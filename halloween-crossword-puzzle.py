import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# main application
application = QApplication([])
window = QMainWindow()
widget = QWidget()

# set window properties
window.setCentralWidget(widget)
window.setWindowTitle("Halloween Crossword Puzzle")
window.setGeometry(640,640,815,990)

# application background
background = window.palette()
background.setColor(window.backgroundRole(), Qt.white)
window.setPalette(background)

# QUESTION 1
txt_one = QLabel(widget)
txt_one.setText("1")
txt_one.move(50,10)
txt_one1 = QLineEdit(widget)
txt_one1.resize(40,40)
txt_one1.move(50, 40)
txt_one2 = QLineEdit(widget)
txt_one2.resize(40,40)
txt_one2.move(50, 80)
txt_one3 = QLineEdit(widget)
txt_one3.resize(40,40)
txt_one3.move(50, 120)
txt_one4 = QLineEdit(widget)
txt_one4.resize(40,40)
txt_one4.move(50, 160)
txt_one5 = QLineEdit(widget)
txt_one5.resize(40,40)
txt_one5.move(50, 200)
txt_one6 = QLineEdit(widget)
txt_one6.resize(40,40)
txt_one6.move(50, 240)
txt_one7 = QLineEdit(widget)
txt_one7.resize(40,40)
txt_one7.move(50, 280)
txt_one8 = QLineEdit(widget)
txt_one8.resize(40,40)
txt_one8.move(50, 320)
txt_one9 = QLineEdit(widget)
txt_one9.resize(40,40)
txt_one9.move(50, 360)

# QUESTION 2
txt_two = QLabel(widget)
txt_two.setText("2")
txt_two.move(30,200)
txt_two1 = QLineEdit(widget)
txt_two1.resize(40,40)
txt_two1.move(90, 200)
txt_two2 = QLineEdit(widget)
txt_two2.resize(40,40)
txt_two2.move(130, 200)
txt_two3 = QLineEdit(widget)
txt_two3.resize(40,40)
txt_two3.move(170, 200)
txt_two4 = QLineEdit(widget)
txt_two4.resize(40,40)
txt_two4.move(210, 200)
txt_two5 = QLineEdit(widget)
txt_two5.resize(40,40)
txt_two5.move(250, 200)
txt_two6 = QLineEdit(widget)
txt_two6.resize(40,40)
txt_two6.move(290, 200)
txt_two7 = QLineEdit(widget)
txt_two7.resize(40,40)
txt_two7.move(330, 200)

# QUESTION 3
txt_three = QLabel(widget)
txt_three.setText("3")
txt_three.move(230,80)
txt_three1 = QLineEdit(widget)
txt_three1.resize(40,40)
txt_three1.move(250, 80)
txt_three2 = QLineEdit(widget)
txt_three2.resize(40,40)
txt_three2.move(290, 80)
txt_three3 = QLineEdit(widget)
txt_three3.resize(40,40)
txt_three3.move(330, 80)
txt_three4 = QLineEdit(widget)
txt_three4.resize(40,40)
txt_three4.move(370, 80)
txt_three5 = QLineEdit(widget)
txt_three5.resize(40,40)
txt_three5.move(410, 80)
txt_three6 = QLineEdit(widget)
txt_three6.resize(40,40)
txt_three6.move(450, 80)
txt_three7 = QLineEdit(widget)
txt_three7.resize(40,40)
txt_three7.move(490, 80)
txt_three8 = QLineEdit(widget)
txt_three8.resize(40,40)
txt_three8.move(530, 80)
txt_three9 = QLineEdit(widget)
txt_three9.resize(40,40)
txt_three9.move(570, 80)
txt_three10 = QLineEdit(widget)
txt_three10.resize(40,40)
txt_three10.move(610, 80)
txt_three11 = QLineEdit(widget)
txt_three11.resize(40,40)
txt_three11.move(650, 80)
txt_three12 = QLineEdit(widget)
txt_three12.resize(40,40)
txt_three12.move(690, 80)

# QUESTION 4
txt_four = QLabel(widget)
txt_four.setText("4")
txt_four.move(450, 10)
txt_four1 = QLineEdit(widget)
txt_four1.resize(40,40)
txt_four1.move(450, 40)
txt_four2 = QLineEdit(widget)
txt_four2.resize(40,40)
txt_four2.move(450, 120)
txt_four3 = QLineEdit(widget)
txt_four3.resize(40,40)
txt_four3.move(450, 160)
txt_four4 = QLineEdit(widget)
txt_four4.resize(40,40)
txt_four4.move(450, 200)
txt_four5 = QLineEdit(widget)
txt_four5.resize(40,40)
txt_four5.move(450, 240)
txt_four6 = QLineEdit(widget)
txt_four6.resize(40,40)
txt_four6.move(450, 280)
txt_four7 = QLineEdit(widget)
txt_four7.resize(40,40)
txt_four7.move(450, 320)
txt_four8 = QLineEdit(widget)
txt_four8.resize(40,40)
txt_four8.move(450, 360)

# QUESTION 5
txt_five = QLabel(widget)
txt_five.setText("5")
txt_five.move(430,320)
txt_five1 = QLineEdit(widget)
txt_five1.resize(40,40)
txt_five1.move(490, 320)
txt_five2 = QLineEdit(widget)
txt_five2.resize(40,40)
txt_five2.move(530, 320)
txt_five3 = QLineEdit(widget)
txt_five3.resize(40,40)
txt_five3.move(570, 320)
txt_five4 = QLineEdit(widget)
txt_five4.resize(40,40)
txt_five4.move(610, 320)

# QUESTION 6
txt_six = QLabel(widget)
txt_six.setText("6")
txt_six.move(130, 130)
txt_six1 = QLineEdit(widget)
txt_six1.resize(40,40)
txt_six1.move(130, 160)
txt_six2 = QLineEdit(widget)
txt_six2.resize(40,40)
txt_six2.move(130, 200)
txt_six3 = QLineEdit(widget)
txt_six3.resize(40,40)
txt_six3.move(130, 240)
txt_six4 = QLineEdit(widget)
txt_six4.resize(40,40)
txt_six4.move(130, 280)
txt_six5 = QLineEdit(widget)
txt_six5.resize(40,40)
txt_six5.move(130, 320)

# text fields
txt_fields = [ txt_one1,txt_one2,txt_one3,txt_one4,txt_one5,txt_one6,txt_one7,txt_one8,txt_one9,txt_two1,
txt_two2,txt_two3,txt_two4,txt_two5,txt_two6,txt_two7,txt_three1,txt_three2,txt_three3,txt_three4,txt_three5,
txt_three6,txt_three7,txt_three8,txt_three9,txt_three10,txt_three11,txt_three12,txt_four1,txt_four2,txt_four3,
txt_four4,txt_four5,txt_four6,txt_four7,txt_four8,txt_five1,txt_five2,txt_five3,txt_five4,txt_six1,txt_six2,
txt_six3,txt_six4,txt_six5 ]
# setting stylesheets
for i in range(len(txt_fields)):
    txt_fields[i].setStyleSheet("padding:3px;background-color:black;color:white;font-weight:bold")

# reveal the answers to the puzzle
def reveal_answers():
    # all letters
    letters = [ "h","a","l","l","o","w","e","e","n","v","e","r","l","o","o","k","m","i","c","h","a",
    "e","l","m","y","e","r","s","p","n","n","y","w","i","s","e","a","l","e","m","d","e","r","r","y" ]
    for i in range(len(letters)):
        txt_fields[i].setText(letters[i])

# clear all letters
def clear_text():
    # all text fields
    for i in range(len(txt_fields)):
        txt_fields[i].setText("")

# open a message for sam
def get_message():
    alert = QMessageBox()
    alert.setWindowTitle("From Emily")
    alert.setText("<html><h3>Happy Halloween!&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h3><h1>&nbsp;&nbsp;&#x1F383;&#x1F383;&#x1F383;</h1></html>")
    alert.exec_()

# questions key
lbl_q1 = QLabel(widget)
lbl_q1.setText("Question 1: What movie did Rob Zombie direct in 2007? (down)") # Halloween
lbl_q1.move(10,450)
lbl_q2 = QLabel(widget)
lbl_q2.setText("Question 2: What is the name of the fictional hotel in the book") # Overlook
lbl_q2.move(10,490)
lbl_q22 = QLabel(widget)
lbl_q22.setText("The Shining? (across)") # Overlook
lbl_q22.move(10,530)
lbl_q3 = QLabel(widget)
lbl_q3.setText("Question 3: What is the name of the fictional killer in the") # Michael Myers
lbl_q3.move(10,570)
lbl_q33 = QLabel(widget)
lbl_q33.setText("Halloween series? (across)") # Michael Myers
lbl_q33.move(10,610)
lbl_q4 = QLabel(widget)
lbl_q4.setText("Question 4: What is the clown's name in the Stephen King novel") # Pennywise
lbl_q4.move(10,650)
lbl_q44 = QLabel(widget)
lbl_q44.setText("IT? (down)") # Pennywise
lbl_q44.move(10,690)
lbl_q5 = QLabel(widget)
lbl_q5.setText("Question 5: What is the name of the town in Massachusetts where") # Salem
lbl_q5.move(10,730)
lbl_q55 = QLabel(widget)
lbl_q55.setText("the 1692 witch trials took place? (across)") # Salem
lbl_q55.move(10,770)
lbl_q6 = QLabel(widget)
lbl_q6.setText("Question 6: What is the name of the town in Maine that events") # Derry
lbl_q6.move(10,810)
lbl_q6 = QLabel(widget)
lbl_q6.setText("take place in the Stephen King novel IT? (down)") # Derry
lbl_q6.move(10,850)
lbl_pumpkin = QLabel(widget)
lbl_pumpkin.setText("<html><span style='font-size:60px;color:darkred'>&#x1F383;</span></html>")
lbl_pumpkin.move(10,900)
# lbl_pumpkin2 = QLabel(widget)
# lbl_pumpkin2.setText("<html><span style='font-size:60px;color:darkred'>&#x1F383;</span></html>")
# lbl_pumpkin2.move(715,900)

# more questions
# What is the title of the longest book Stephen King has written? (diagonal, The Stand)

# reveal answers button
reveal_btn = QPushButton(widget)
reveal_btn.setText("Reveal Answers")
reveal_btn.move(110,915)
reveal_btn.setStyleSheet("background-color:black;color:white;")
reveal_btn.clicked.connect(reveal_answers)

# clear text button
clear_btn = QPushButton(widget)
clear_btn.setText("Clear Letters")
clear_btn.move(330,915)
clear_btn.setStyleSheet("background-color:black;color:white;")
clear_btn.clicked.connect(clear_text)

# a message
message = QPushButton(widget)
message.setText("Click for Message")
message.move(535,915)
message.setStyleSheet("background-color:black;color:white;")
message.clicked.connect(get_message)


# show the window
window.show()
application.exec_()
