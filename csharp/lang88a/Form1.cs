using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lang88a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int sum = num1 + num2;
            int prod = num1 * num2;
            double avg = (double)sum / 2.0;
            int diff = num1 - num2;
            int abs = Math.Abs(diff);
            int max = 0;
            int min = 0;
            if(num1 > num2) {
                max = num1;
                min = num2;
            } else {
                max = num2;
                min = num1;
            }
            label12.Text = sum.ToString();
            label11.Text = diff.ToString();
            label10.Text = prod.ToString();
            label9.Text = avg.ToString();
            label8.Text = abs.ToString();
            label7.Text = max.ToString();
            label13.Text = min.ToString();

        }
    }
}
