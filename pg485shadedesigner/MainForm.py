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
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Location = System.Drawing.Point(26, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(129, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Styles"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Pink
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Location = System.Drawing.Point(161, 36)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(129, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Sizes"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Pink
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Location = System.Drawing.Point(26, 107)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(129, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Colors"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(26, 176)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(264, 32)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Pink
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Location = System.Drawing.Point(161, 107)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(129, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Price:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Gainsboro
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Location = System.Drawing.Point(161, 136)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(129, 25)
		self._label5.TabIndex = 8
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Regular Shades",
			"Folding Shades",
			"Roman Shades"]))
		self._comboBox1.Location = System.Drawing.Point(26, 65)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(129, 24)
		self._comboBox1.TabIndex = 9
		self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["25 inches",
			"27 inches",
			"32 inches",
			"40 inches"]))
		self._comboBox2.Location = System.Drawing.Point(161, 65)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(129, 24)
		self._comboBox2.TabIndex = 10
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["Natural",
			"Blue",
			"Teal",
			"Green",
			"Red"]))
		self._comboBox3.Location = System.Drawing.Point(26, 136)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(129, 24)
		self._comboBox3.TabIndex = 11
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(161, 214)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(129, 32)
		self._button2.TabIndex = 12
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.Location = System.Drawing.Point(26, 214)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(129, 32)
		self._button3.TabIndex = 13
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(343, 302)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "pg485shadedesigner"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def ListBox1SelectedIndexChanged(self, sender, e):
		pass



	def Button1Click(self, sender, e):
		tot = 50
		if self._comboBox1.SelectedItem == "Folding Shades":
			tot += 10
		if self._comboBox1.SelectedItem == "Roman Shades":
			tot += 15
			
		if self._comboBox2.SelectedItem == "27 inches":
			tot += 2
		if self._comboBox2.SelectedItem == "32 inches":
			tot += 4
		if self._comboBox2.SelectedItem == "40 inches":
			tot += 6
		
		if self._comboBox3.SelectedItem == "Natural":
			tot += 5
		
		self._label5.Text = "$" + str(tot)
		pass

	def ComboBox1SelectedIndexChanged(self, sender, e):
		
		pass

	def ListBox2SelectedIndexChanged(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._label5.Text = ""
		pass