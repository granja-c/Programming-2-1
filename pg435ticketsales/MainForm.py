import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGray
		self._button1.Location = System.Drawing.Point(163, 40)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(129, 48)
		self._button1.TabIndex = 0
		self._button1.Text = "General Sales"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGray
		self._button2.Location = System.Drawing.Point(163, 94)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(129, 49)
		self._button2.TabIndex = 1
		self._button2.Text = "Student Sales"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._button1)
		self._groupBox1.Controls.Add(self._button2)
		self._groupBox1.Location = System.Drawing.Point(44, 31)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(309, 159)
		self._groupBox1.TabIndex = 2
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Select the type of ticket sales"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(19, 40)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(138, 49)
		self._label1.TabIndex = 2
		self._label1.Text = "Select General Sales for all ticket sales to the general public."
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(19, 94)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(138, 49)
		self._label2.TabIndex = 3
		self._label2.Text = "Select Student Sales for all student ticket sales."
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGray
		self._button3.ForeColor = System.Drawing.SystemColors.ControlText
		self._button3.Location = System.Drawing.Point(207, 197)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(129, 32)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightPink
		self.ClientSize = System.Drawing.Size(441, 274)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._groupBox1)
		self.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "pg435ticketsales"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from gensales import *
		gen = gensales(self)
		gen.Show()
		pass

	def Button2Click(self, sender, e):
		from studentsales import *
		stud = studentsales(self)
		stud.Show()
		pass

	def Button3Click(self, sender, e):
		Application.Close()
		pass