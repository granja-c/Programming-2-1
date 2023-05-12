import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._radioButton13 = System.Windows.Forms.RadioButton()
		self._radioButton14 = System.Windows.Forms.RadioButton()
		self._radioButton15 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(28, 22)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(142, 145)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Decks"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(7, 23)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(129, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Master Thrasher"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(7, 54)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(129, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Dictator of Grind"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(7, 85)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(117, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "The Street King"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radioButton4)
		self._groupBox2.Controls.Add(self._radioButton5)
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Location = System.Drawing.Point(197, 22)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(142, 145)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Truck Assembly"
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(7, 85)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(117, 24)
		self._radioButton4.TabIndex = 2
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "8.5 axel"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(7, 54)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(129, 24)
		self._radioButton5.TabIndex = 1
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "8 axel"
		self._radioButton5.UseVisualStyleBackColor = True
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(7, 23)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(129, 24)
		self._radioButton6.TabIndex = 0
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "7.75 axel"
		self._radioButton6.UseVisualStyleBackColor = True
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._radioButton7)
		self._groupBox3.Controls.Add(self._radioButton8)
		self._groupBox3.Controls.Add(self._radioButton9)
		self._groupBox3.Location = System.Drawing.Point(28, 173)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(142, 175)
		self._groupBox3.TabIndex = 2
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Wheel Sets"
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(7, 85)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(117, 24)
		self._radioButton7.TabIndex = 2
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "61 mm"
		self._radioButton7.UseVisualStyleBackColor = True
		# 
		# radioButton8
		# 
		self._radioButton8.Location = System.Drawing.Point(7, 54)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(129, 24)
		self._radioButton8.TabIndex = 1
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "55 mm"
		self._radioButton8.UseVisualStyleBackColor = True
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(7, 23)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(129, 24)
		self._radioButton9.TabIndex = 0
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "51 mm"
		self._radioButton9.UseVisualStyleBackColor = True
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(35, 288)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(117, 24)
		self._radioButton10.TabIndex = 3
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "68 mm"
		self._radioButton10.UseVisualStyleBackColor = True
		# 
		# groupBox4
		# 
		self._groupBox4.Controls.Add(self._radioButton15)
		self._groupBox4.Controls.Add(self._radioButton14)
		self._groupBox4.Controls.Add(self._radioButton11)
		self._groupBox4.Controls.Add(self._radioButton12)
		self._groupBox4.Controls.Add(self._radioButton13)
		self._groupBox4.Location = System.Drawing.Point(197, 173)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(142, 175)
		self._groupBox4.TabIndex = 4
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Miscellaneous"
		# 
		# radioButton11
		# 
		self._radioButton11.Location = System.Drawing.Point(7, 85)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(117, 24)
		self._radioButton11.TabIndex = 2
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "Riser Pads"
		self._radioButton11.UseVisualStyleBackColor = True
		# 
		# radioButton12
		# 
		self._radioButton12.Location = System.Drawing.Point(7, 54)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(129, 24)
		self._radioButton12.TabIndex = 1
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "Bearings"
		self._radioButton12.UseVisualStyleBackColor = True
		# 
		# radioButton13
		# 
		self._radioButton13.Location = System.Drawing.Point(7, 23)
		self._radioButton13.Name = "radioButton13"
		self._radioButton13.Size = System.Drawing.Size(129, 24)
		self._radioButton13.TabIndex = 0
		self._radioButton13.TabStop = True
		self._radioButton13.Text = "Grip Tape"
		self._radioButton13.UseVisualStyleBackColor = True
		# 
		# radioButton14
		# 
		self._radioButton14.Location = System.Drawing.Point(7, 115)
		self._radioButton14.Name = "radioButton14"
		self._radioButton14.Size = System.Drawing.Size(129, 24)
		self._radioButton14.TabIndex = 3
		self._radioButton14.TabStop = True
		self._radioButton14.Text = "Nuts and Bolts Kit"
		self._radioButton14.UseVisualStyleBackColor = True
		# 
		# radioButton15
		# 
		self._radioButton15.Location = System.Drawing.Point(7, 145)
		self._radioButton15.Name = "radioButton15"
		self._radioButton15.Size = System.Drawing.Size(129, 24)
		self._radioButton15.TabIndex = 5
		self._radioButton15.TabStop = True
		self._radioButton15.Text = "Assembly"
		self._radioButton15.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(383, 122)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 29)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Gainsboro
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(383, 76)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 31)
		self._label1.TabIndex = 6
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Pink
		self._label2.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label2.Location = System.Drawing.Point(383, 45)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 24)
		self._label2.TabIndex = 7
		self._label2.Text = "Price:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(616, 412)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._radioButton10)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "pg485skateboarddesigner"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		tot = 0
		if self._radioButton1.Checked:
			tot += 60
		if self._radioButton2.Checked:
			tot += 45
		if self._radioButton3.Checked:
			tot += 50
			
		if self._radioButton6.Checked:
			tot += 30
		if self._radioButton5.Checked:
			tot += 40
		if self._radioButton4.Checked:
			tot += 45
		
		if self._radioButton9.Checked:
			tot += 20
		if self._radioButton8.Checked:
			tot += 22
		if self._radioButton7.Checked:
			tot += 24
		if self._radioButton10.Checked:
			tot += 28
		
		if self._radioButton13.Checked:
			tot += 10
		if self._radioButton12.Checked:
			tot += 30
		if self._radioButton11.Checked:
			tot += 2
		if self._radioButton14.Checked:
			tot += 3
		if self._radioButton15.Checked:
			tot += 10
			
		self._label1.Text = "$" + str(tot)
		
		pass