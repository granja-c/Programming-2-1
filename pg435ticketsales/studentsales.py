
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class studentsales(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._groupBox3.SuspendLayout()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._label5)
		self._groupBox3.Controls.Add(self._label4)
		self._groupBox3.Controls.Add(self._label6)
		self._groupBox3.Controls.Add(self._label3)
		self._groupBox3.Controls.Add(self._label7)
		self._groupBox3.Controls.Add(self._label2)
		self._groupBox3.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(187, 42)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(138, 115)
		self._groupBox3.TabIndex = 6
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total"
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
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(7, 81)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(46, 23)
		self._label4.TabIndex = 2
		self._label4.Text = "Total:"
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
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(7, 51)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(46, 23)
		self._label3.TabIndex = 1
		self._label3.Text = "Tax:"
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
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 24)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(47, 23)
		self._label2.TabIndex = 0
		self._label2.Text = "Tickets:"
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(43, 42)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(138, 115)
		self._groupBox1.TabIndex = 5
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How many tickets?"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(13, 51)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 24)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(119, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Number of tickets:"
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(187, 162)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 35)
		self._button2.TabIndex = 8
		self._button2.Text = "Close"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(106, 163)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 35)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# studentsales
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(413, 266)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox1)
		self.Name = "studentsales"
		self.Text = "studentsales"
		self.FormClosing += self.StudentsalesFormClosing
		self._groupBox3.ResumeLayout(False)
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		tic = int(self._textBox1.Text)
		price = 7
		TAX = 0.06
		ticcost = 0
		salestax = 0
		tot = 0
		
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

	def StudentsalesFormClosing(self, sender, e):
		self.parent.Show()
		pass