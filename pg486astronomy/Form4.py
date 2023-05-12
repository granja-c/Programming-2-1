
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form4(Form):
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
		self._button1.Location = System.Drawing.Point(166, 156)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(92, 39)
		self._button1.TabIndex = 7
		self._button1.Text = "Exit"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(48, 25)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(333, 125)
		self._groupBox1.TabIndex = 6
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Mars"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightPink
		self._label2.Location = System.Drawing.Point(190, 29)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(118, 80)
		self._label2.TabIndex = 1
		self._label2.Text = """Terrestrial
1.5237 AU
0.6424  x 10^24 kg
-140°C to 40°C  """
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
		# Form4
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(478, 319)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form4"
		self.Text = "Form4"
		self.FormClosing += self.Form4FormClosing
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.Close()
		self.parent.Show()
		pass

	def Form4FormClosing(self, sender, e):
		self.parent.Show()
		pass