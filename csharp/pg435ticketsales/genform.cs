using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg435ticketsales
{
    public partial class genform : Form
    {
        private Form myParent;

        public genform(Form prt)
        {
            InitializeComponent();
            this.myParent = prt;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }
        decimal decTAXRATE = 0.06m;
        private decimal CalcTax(decimal cost)
        {
            return cost * decTAXRATE;
        }

        private void genform_FormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int ticks = int.Parse(textBox1.Text);
            decimal price = 0.0m;

            if (radioButton1.Checked)
            {
                price = 20.0m;
            }
            else if (radioButton2.Checked)
            {
                price = 15.0m;
            }
            else if (radioButton3.Checked)
            {
                price = 10.0m;
            }
            decimal ticCost = ticks * price;
            decimal taxCost = CalcTax(ticCost);
            decimal tot = ticCost + taxCost;
            label1.Text = "$" + ticCost;
            label2.Text = "$" + Math.Round(taxCost, 2);
            label3.Text = "$" + Math.Round(tot, 2);
        }

        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }
    }
}
