using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg535CatchMe
{
    public partial class Form1 : Form
    {
        private string[] strCap = { "Click here!", "Try again!", "Where are you?", "I'm over here!", "Not even close", "Try harder!"};
        private Random rand = new Random();
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("You got me!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_MouseEnter(object sender, EventArgs e)
        {
            int intIndex = rand.Next(strCap.Length);
            button1.Text = strCap[intIndex];
            button1.Left = rand.Next(this.Width - button1.Width);
            button1.Top = rand.Next(this.Height - button1.Height - 30);
        }
    }
}
