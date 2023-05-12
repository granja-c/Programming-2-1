using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg347sum
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string num = Interaction.InputBox("Enter a positive integer", "Input Needed");
            int sum = 0;
            for (int lcv = 0; lcv <= int.Parse(num); lcv++){
                sum += lcv;
            }MessageBox.Show("The sum of the numbers 1 through " + num + " equals " + sum);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
           
        }
    }
}
