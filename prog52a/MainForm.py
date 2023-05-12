import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(220, 55)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(163, 21)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(220, 111)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(163, 21)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightGray
		self._label1.Location = System.Drawing.Point(43, 55)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(158, 32)
		self._label1.TabIndex = 2
		self._label1.Text = "Length"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightGray
		self._label2.Location = System.Drawing.Point(43, 104)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(158, 35)
		self._label2.TabIndex = 3
		self._label2.Text = "Width"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Pink
		self._label4.Location = System.Drawing.Point(43, 174)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(158, 39)
		self._label4.TabIndex = 5
		self._label4.Text = "Area:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(43, 242)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(340, 53)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(43, 313)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(158, 53)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.Location = System.Drawing.Point(225, 313)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(158, 53)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Pink
		self._label5.Location = System.Drawing.Point(220, 174)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(163, 39)
		self._label5.TabIndex = 10
		self._label5.Text = "Perimeter:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(789, 595)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "prog52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		len = int(self._textBox1.Text)
		wid = int(self._textBox2.Text)
		area = len * wid
		perim = len * 2 + wid * 2
		self._label4.Text = "Area: " + str(area)
		self._label5.Text = "Perimeter: " + str(perim)
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		pass