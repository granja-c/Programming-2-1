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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(91, 18)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(117, 23)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(91, 64)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(117, 23)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Location = System.Drawing.Point(26, 104)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(182, 70)
		self._label1.TabIndex = 2
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(26, 177)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(182, 39)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(26, 222)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(89, 34)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.Location = System.Drawing.Point(119, 222)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(89, 34)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(26, 18)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(59, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "Num 1:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(26, 64)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(59, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "Num 2:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(241, 276)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "lp3-7"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		
		from ClLP37 import *
		obj1 = ClLP37(num1, num2)
		obj2 = ClLP37(num2, num1)
		obj1.calc()
		obj2.calc()
		div1 = obj1.getDiv()
		mod1 = obj1.getMod()
		div2, mod2 = obj2.getDivMod()
		
		self._label1.Text = str(num1) + "/" + str(num2) + "=" +  str(div1) + "\n" 
		self._label1.Text += str(num1) + "%" + str(num2) + "=" +  str(mod1) + "\n"
		self._label1.Text += str(num2) + "/" + str(num1) + "=" +  str(div2) + "\n"
		self._label1.Text += + str(num2) + "%" + str(num1) + "=" +  str(mod2) + "\n" 
		pass

	def Button2Click(self, sender, e):
		self._label1.Text = " "
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass