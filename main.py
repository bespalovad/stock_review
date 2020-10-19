import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

class Company:
	def __init__ (self, name, link, color):
		super(Company, self).__init__()
		self.name = name
		self.link = link
		self.color = color
	
	def change_name (self, name):
		self.name = name
		
	def change_link (self, link):
		self.link = link
	
	def change_color (self, color):
		self.color = color
	
class Company_List:
	def __init__(self):
		super(Company_List, self).__init__()
		company_list = []
		self.company_list = company_list
		
	def add_company (self, name, link, color):
		new_company = Company (name, link, color)
		self.company_list.append(new_company)
	
	def return_company (self, index):
		return self.company_list[index]
		
	def remove_company (self, index):
		self.company_list.pop(index)
	
class Window (QtWidgets.QMainWindow):
	def __init__ (self):
		super(Window, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

def main():
	app = QtWidgets.QApplication ([])
	win = Window()
	win.show()
	sys.exit(app.exec())

if __name__ == '__main__':
	main()

