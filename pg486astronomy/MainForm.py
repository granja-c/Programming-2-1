import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._button10 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(41, 101)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(103, 37)
		self._button1.TabIndex = 0
		self._button1.Text = "Mercury"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(41, 144)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(103, 37)
		self._button2.TabIndex = 1
		self._button2.Text = "Venus"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.Location = System.Drawing.Point(41, 186)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(103, 37)
		self._button3.TabIndex = 2
		self._button3.Text = "Earth"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.LightGray
		self._button4.Location = System.Drawing.Point(41, 229)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(103, 37)
		self._button4.TabIndex = 3
		self._button4.Text = "Mars"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.LightGray
		self._button5.Location = System.Drawing.Point(158, 144)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(103, 37)
		self._button5.TabIndex = 6
		self._button5.Text = "Uranus"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.LightGray
		self._button6.Location = System.Drawing.Point(158, 101)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(103, 37)
		self._button6.TabIndex = 5
		self._button6.Text = "Saturn"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.LightGray
		self._button7.Location = System.Drawing.Point(41, 272)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(103, 37)
		self._button7.TabIndex = 4
		self._button7.Text = "Jupiter"
		self._button7.UseVisualStyleBackColor = False
		self._button7.Click += self.Button7Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.Location = System.Drawing.Point(44, 38)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(217, 50)
		self._label1.TabIndex = 7
		self._label1.Text = "Pick a planet:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.Color.LightGray
		self._button8.Location = System.Drawing.Point(158, 187)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(103, 37)
		self._button8.TabIndex = 8
		self._button8.Text = "Neptune"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.LightGray
		self._button9.Location = System.Drawing.Point(158, 229)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(103, 37)
		self._button9.TabIndex = 9
		self._button9.Text = "Pluto"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# button10
		# 
		self._button10.BackColor = System.Drawing.Color.Silver
		self._button10.Location = System.Drawing.Point(158, 272)
		self._button10.Name = "button10"
		self._button10.Size = System.Drawing.Size(103, 37)
		self._button10.TabIndex = 10
		self._button10.Text = "Exit"
		self._button10.UseVisualStyleBackColor = False
		self._button10.Click += self.Button10Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(318, 360)
		self.Controls.Add(self._button10)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "pg486astronomy"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def Button5Click(self, sender, e):
		from Form7 import *
		form7 = Form7(self, "Hello, world!")
		form7.Show()
		self.Hide()
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self)
		form1.Show()
		self.Hide()
		pass

	def Button2Click(self, sender, e):
		from Form2v2 import *
		form2 = Form2v2(self)
		form2.Show()
		self.Hide()
		pass

	def Button7Click(self, sender, e):
		from Form5 import *
		form5 = Form5(self)
		form5.Show()
		self.Hide()
		pass

	def Button3Click(self, sender, e):
		from Form3 import *
		form3 = Form3(self)
		form3.Show()
		self.Hide()
		pass

	def Button4Click(self, sender, e):
		from Form4 import *
		form4 = Form4(self)
		form4.Show()
		self.Hide()
		pass

	def Button6Click(self, sender, e):
		from Form6 import *
		form6 = Form6(self)
		form6.Show()
		self.Hide()
		pass

	def Button10Click(self, sender, e):
		Application.Exit()
		pass

	def Button8Click(self, sender, e):
		from Form8 import *
		form8 = Form8(self, "Hello, world!")
		form8.Show()
		self.Hide()
		pass

	def Button9Click(self, sender, e):
		from Form9 import *
		form9 = Form9(self, "Hello, world!")
		form9.Show()
		self.Hide()
		pass