import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.Location = System.Drawing.Point(65, 39)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 29)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Text:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(183, 39)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(119, 24)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Pink
		self._label2.Location = System.Drawing.Point(65, 96)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 29)
		self._label2.TabIndex = 2
		self._label2.Text = "Result:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Gainsboro
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Location = System.Drawing.Point(183, 95)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(119, 29)
		self._label3.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(65, 150)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 37)
		self._button1.TabIndex = 4
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(146, 150)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 37)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.Location = System.Drawing.Point(227, 150)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 37)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(400, 273)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "strint3"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		Mystr = self._textBox1.Text
		
		for lcv in range(len(Mystr)):
			a = Mystr[lcv]
			if Mystr.count(a) == 1:
				self._label3.Text = a
				break 
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label3.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass