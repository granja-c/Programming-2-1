
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class gensales(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(157, 23)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 24)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Number of tickets:"
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(50, 35)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(282, 76)
		self._groupBox1.TabIndex = 2
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How many tickets?"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radioButton3)
		self._groupBox2.Controls.Add(self._radioButton2)
		self._groupBox2.Controls.Add(self._radioButton1)
		self._groupBox2.Location = System.Drawing.Point(50, 118)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(138, 115)
		self._groupBox2.TabIndex = 3
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Section"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._label5)
		self._groupBox3.Controls.Add(self._label4)
		self._groupBox3.Controls.Add(self._label6)
		self._groupBox3.Controls.Add(self._label3)
		self._groupBox3.Controls.Add(self._label7)
		self._groupBox3.Controls.Add(self._label2)
		self._groupBox3.Location = System.Drawing.Point(194, 118)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(138, 115)
		self._groupBox3.TabIndex = 4
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(13, 24)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Section A"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(13, 55)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Section B"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(13, 85)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Section C"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 24)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(47, 23)
		self._label2.TabIndex = 0
		self._label2.Text = "Tickets:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(7, 51)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(46, 23)
		self._label3.TabIndex = 1
		self._label3.Text = "Tax:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(7, 81)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(46, 23)
		self._label4.TabIndex = 2
		self._label4.Text = "Total:"
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Gainsboro
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Location = System.Drawing.Point(59, 80)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(64, 23)
		self._label5.TabIndex = 7
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Gainsboro
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.Location = System.Drawing.Point(59, 51)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(64, 23)
		self._label6.TabIndex = 6
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Gainsboro
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label7.Location = System.Drawing.Point(58, 24)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(65, 23)
		self._label7.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(113, 239)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 35)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(194, 238)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 35)
		self._button2.TabIndex = 6
		self._button2.Text = "Close"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# gensales
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(460, 388)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "gensales"
		self.Text = "gensales"
		self.FormClosing += self.GensalesFormClosing
		self.Load += self.GensalesLoad
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)


	def GensalesLoad(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		tic = int(self._textBox1.Text)
		TAX = 0.06
		price = 0
		ticcost = 0
		salestax = 0
		tot = 0
		
		if self._radioButton1.Checked:
			price = 20
		if self._radioButton2.Checked:
			price = 15
		if self._radioButton3.Checked:
			price = 10
			
		ticcost = price * tic
		salestax = ticcost * 0.06
		tot = salestax + ticcost
		
		self._label7.Text = "$" + str(ticcost)
		self._label6.Text = "$" + str(salestax)
		self._label5.Text = "$" + str(tot)
		pass

	def Button2Click(self, sender, e):
		self.Close()
		self.parent.Show()
		pass

	def GensalesFormClosing(self, sender, e):
		self.parent.Show()
		pass