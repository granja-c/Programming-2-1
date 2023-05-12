using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int bks = int.Parse(textBox1.Text);
            int pts = 0;
            if(bks == 1){
                pts = 5;
            } else if(bks == 2){
                pts = 15;
            } else if(bks == 3){
                pts = 30;
            } else if(bks >= 4){
                pts = 60;
            } else {
                pts = 0;
            }
            label1.Text = pts + " points";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
