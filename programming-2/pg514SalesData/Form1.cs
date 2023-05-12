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

namespace pg514SalesData
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            decimal[] decSales = null;
            decimal decTotal = 0.0m;
            decimal decAverage = 0.0m;
            decimal decHighest = 0.0m;
            decimal decLowest = 0.0m;

            if (GetSalesData(ref decSales))
            {
                decTotal = GetTotal(decSales);
                decAverage = GetAvg(decSales);
                decHighest = GetHighest(decSales);
                decLowest = GetLowest(decSales);
            }
            label1.Text = decTotal.ToString("$.00");
            label2.Text = decAverage.ToString("$.00");
            label3.Text = decHighest.ToString("$.00");
            label4.Text = decLowest.ToString("$.00");
        }

        private bool GetSalesData(ref decimal[] decSales)
        {
            decimal[] decSalesData;
            int intNumDays = 0;
            int intCount = 0;
            bool blnSuccess = false;

            string strNumDays = Interaction.InputBox("For how many days do you have sales?");

            if (!int.TryParse(strNumDays, out intNumDays))
            {
                MessageBox.Show("You entered a non-numeric value.", "Error");
                return false;
            }
            if (intNumDays > 0)
            {
                decSalesData = new decimal[intNumDays];
                for (intCount = 0; intCount < intNumDays; intCount++)
                {
                    bool blnValid = false;
                    while (blnValid != true)
                    {
                        blnValid = decimal.TryParse(Interaction.InputBox("Enter the sales for day # " + (intCount + 1).ToString()), out decSalesData[intCount]);
                        if (blnValid != true)
                        {
                            MessageBox.Show("Please enter a valid number");
                        }
                    }
                }
                decSales = decSalesData;
                blnSuccess = true;

            }
            else
            {
                MessageBox.Show("You must enter at least one day of sales.");
            }
            return blnSuccess;
        }

        private decimal GetTotal(decimal[] decValues)
        {
            decimal dectot = 0.0m;
            int intCount;

            for (intCount = 0; intCount < decValues.Length; intCount++)
            {
                dectot += decValues[intCount];

            }
            return dectot;
        }
        private decimal GetAvg(decimal[] decValues)
        {
            return GetTotal(decValues) / decValues.Length;
        }
        private decimal GetHighest(decimal[] decValues)
        {
            decimal decHighest = decValues[0];
            int intCount;

            for (intCount = 1; intCount < decValues.Length; intCount++)
            {
                if (decValues[intCount] > decHighest) decHighest = decValues[intCount];
            }
            return decHighest;
        }
        private decimal GetLowest(decimal[] decValues)
        {
            decimal decLowest = decValues[0];
            int intCount;

            for (intCount = 1; intCount < decValues.Length; intCount++)
            {
                if (decValues[intCount] < decLowest) decLowest = decValues[intCount];
            }
            return decLowest;
        }
    }
}
