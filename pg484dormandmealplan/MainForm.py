import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(52, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(104, 20)
		self._label1.TabIndex = 4
		self._label1.Text = "Pick a dorm hall:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(52, 187)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 35)
		self._button1.TabIndex = 5
		self._button1.Text = "Exit"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(52, 59)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 28)
		self._button2.TabIndex = 6
		self._button2.Text = "Allen Hall"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(52, 89)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(104, 28)
		self._button3.TabIndex = 7
		self._button3.Text = "Pike Hall"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.LightGray
		self._button4.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(52, 119)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(104, 28)
		self._button4.TabIndex = 8
		self._button4.Text = "Farthing Hall"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.LightGray
		self._button5.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(52, 153)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(104, 28)
		self._button5.TabIndex = 9
		self._button5.Text = "University Suites"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(227, 249)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg484dormandmealplan"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, 1500)
		form1.Show()
		self.Hide()
		pass

	def Button3Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, 1600)
		form1.Show()
		self.Hide()
		pass

	def Button4Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, 1200)
		form1.Show()
		self.Hide()
		pass

	def Button5Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, 1800)
		form1.Show()
		self.Hide()
		pass