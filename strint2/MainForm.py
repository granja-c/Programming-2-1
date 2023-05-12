import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(76, 39)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter word:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(76, 135)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Anagrams?"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(204, 39)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(133, 23)
		self._textBox1.TabIndex = 2
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(76, 174)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(261, 45)
		self._button1.TabIndex = 3
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(76, 225)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(129, 39)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.Location = System.Drawing.Point(211, 225)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(126, 39)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Gainsboro
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.ForeColor = System.Drawing.Color.Black
		self._label3.Location = System.Drawing.Point(204, 135)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(133, 23)
		self._label3.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(204, 74)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(133, 23)
		self._textBox2.TabIndex = 8
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(76, 74)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Enter word 2:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(559, 433)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "strint2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word = self._textBox1.Text
		anag = self._textBox2.Text
		word = word.lower()
		anag = word.lower()
		
		if len(word) != len(anag):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word)):
				c = word[lcv]
				ind = anag.index(c)
				if ind != -1:
					anag = anag[0:ind] + anag[ind+1:]
				else:
					self._label3.Text = "False"
		self._label3.Text = str(len(anag) == 0)
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass