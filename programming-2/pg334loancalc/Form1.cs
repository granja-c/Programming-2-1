using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace pg334loancalc
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        const int min = 6;
        const int max = 48;
        const float mpy = 12.0f;

        const double newrate = 0.089;
        const double usedrate = 0.095;

        double annualrate = newrate;

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            int months = 0;
            double loan = 0.0;
            int cnt = 0;
            double intr = 0.0;
            double payment = 0.0;
            double princ = 0.0;

            if (radioButton2.Checked)
            {
                annualrate = usedrate;
            }
            try {
                months = int.Parse(textBox3.Text);
                loan = double.Parse(textBox1.Text) - double.Parse(textBox2.Text);
            } catch (Exception ex) {
                MessageBox.Show("Please enter numeric values:");
                return;
            }
            payment = Financial.Pmt(annualrate / mpy, months, -loan);
            for (cnt = 1; cnt <= months; cnt++) {
                string res = string.Empty;
                intr = Financial.IPmt(annualrate / mpy, cnt, months, -loan);
                princ = Financial.PPmt(annualrate / mpy, cnt, months, -loan);
                res += "Month: " + cnt;
                res += "  Payment: " + payment.ToString("$.00");
                res += "  Interest: " + intr.ToString("$.00");
                res += "  Principal: " + princ.ToString("$.00");
                listBox1.Items.Add(res);
            }
            label1.Text = annualrate.ToString(".00%");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.CausesValidation = false;
            textBox2.CausesValidation = false;
            textBox3.CausesValidation = false;
            radioButton1.Checked = true;
            radioButton2.Checked = false;
            annualrate = newrate;
            label1.Text = newrate.ToString(".00%");
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            label1.Text = "";
            listBox1.Items.Clear();
            label1.Text = newrate.ToString(".00%");
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_CausesValidationChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_Validating(object sender, CancelEventArgs e)
        {
            double _x = 0;
            if (!double.TryParse(textBox1.Text, out _x))
            {
                MessageBox.Show("Cost must be a number.", "Invalid Vehicle Cost");
                textBox1.SelectAll();
                e.Cancel = true;

            }
            else
            {
                e.Cancel = false;
            }
        }

        private void textBox2_Validating(object sender, CancelEventArgs e)
        {
            double _x = 0;
            if (!double.TryParse(textBox1.Text, out _x))
            {
                MessageBox.Show("Down payment must be a number.", "Invalid Down Payment");
                textBox2.SelectAll();
                e.Cancel = true;

            }
            else
            {
                e.Cancel = false;
            }
        }

        private void textBox3_Validating(object sender, CancelEventArgs e)
        {
            double _x = 0;
            if (!double.TryParse(textBox1.Text, out _x))
            {
                MessageBox.Show("Months must be a number.", "Invalid Month Amount");
                textBox3.SelectAll();
                e.Cancel = true;

            }
            else
            {
                e.Cancel = false;
            }
        }

        private void groupBox3_Enter(object sender, EventArgs e)
        {

        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            label1.Text = usedrate.ToString(".00%");
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            label1.Text = newrate.ToString(".00%");
        }
    }
}
