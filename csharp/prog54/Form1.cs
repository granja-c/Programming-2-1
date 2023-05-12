using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog54
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double miles = 0;
            double gal = 0;
            double mpg = 0;
            if (comboBox1.Text == "1970 VW Bug") {
                miles = 286;
                gal = 9;
            } else if (comboBox1.Text == "1979 Firebird") {
                miles = 412;
                gal = 40;
            } else if (comboBox1.Text == "1980 Subaru") {
                miles = 361;
                gal = 18;
            } else if (comboBox1.Text == "1975 Cutlass") {
                miles = 161;
                gal = 11;
            }
            else {
                MessageBox.Show("Invalid Car Selection");
                return;
            }
            mpg = miles / gal;
            mpg = Math.Round(mpg, 3);
            label1.Text = miles.ToString();
            label2.Text = gal.ToString();
            label3.Text = mpg.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
