
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form3(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(148, 156)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(92, 39)
		self._button1.TabIndex = 5
		self._button1.Text = "Exit"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(30, 25)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(333, 125)
		self._groupBox1.TabIndex = 4
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Earth"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightPink
		self._label2.Location = System.Drawing.Point(190, 29)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(118, 80)
		self._label2.TabIndex = 1
		self._label2.Text = """Terrestrial
1 AU
5.967 x 10^24 kg
-50°C to 50°C  """
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightPink
		self._label1.Location = System.Drawing.Point(6, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(187, 80)
		self._label1.TabIndex = 0
		self._label1.Text = """Type
Average distance from the sun
Mass
Surface temperature"""
		# 
		# Form3
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(423, 287)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form3"
		self.Text = "Form3"
		self.FormClosing += self.Form3FormClosing
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.Close()
		self.parent.Show()
		pass

	def Form3FormClosing(self, sender, e):
		self.parent.Show()
		pass