import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 16
		self._listBox1.Location = System.Drawing.Point(56, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(271, 308)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(56, 371)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(134, 42)
		self._button1.TabIndex = 1
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(196, 371)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(131, 42)
		self._button2.TabIndex = 2
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.Location = System.Drawing.Point(56, 328)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(271, 37)
		self._button3.TabIndex = 3
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(474, 489)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "prog122a"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		for num in range(1, 51):
			sqd = num ** 2
			sqrt = math.sqrt(num)
			self._listBox1.Items.Add(str(num) + "\t" + str(sqd) + "\t" + str(round(sqrt, 4)))
		pass

	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button2Click(self, sender, e):
		Application.Exit()
		pass