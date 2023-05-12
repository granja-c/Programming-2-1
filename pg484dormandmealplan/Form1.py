
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent, dorm):
		self.InitializeComponent()
		self.parent = parent
		self.dorm = dorm
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Location = System.Drawing.Point(54, 140)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(144, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "Total: "
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(54, 18)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(135, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Pick a meal plan:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(54, 44)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(144, 27)
		self._button1.TabIndex = 2
		self._button1.Text = "7 meals per week"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(54, 77)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(144, 27)
		self._button2.TabIndex = 3
		self._button2.Text = "14 meals per week"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.Location = System.Drawing.Point(54, 110)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(144, 27)
		self._button3.TabIndex = 4
		self._button3.Text = "Unlimited meals"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.LightGray
		self._button4.Location = System.Drawing.Point(54, 207)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(144, 27)
		self._button4.TabIndex = 5
		self._button4.Text = "Exit"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.LightGray
		self._button5.Location = System.Drawing.Point(54, 174)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(144, 27)
		self._button5.TabIndex = 6
		self._button5.Text = "Clear"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# Form1
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(269, 243)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "Form1"
		self.Text = "Form1"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		tot = self.dorm + 1500
		self._label1.Text = "Total: $" + str(tot)
		pass

	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		tot = self.dorm + 560
		self._label1.Text = "Total: $" + str(tot)
		pass

	def Button2Click(self, sender, e):
		tot = self.dorm + 1095
		self._label1.Text = "Total: $" + str(tot)
		pass

	def Button4Click(self, sender, e):
		self.parent.Show()
		self.Close()
		pass

	def Button5Click(self, sender, e):
		self._label1.Text = "Total: "
		pass