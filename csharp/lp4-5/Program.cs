using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lp4_5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your percentage: ");
            double percent = double.Parse(Console.ReadLine());
            char grade = ' ';
            if (percent >= 90) {
                grade = 'A';
            } else if (percent >= 80) {
                grade = 'B';
            } else if (percent >= 70) {
                grade = 'C';
            } else if (percent >= 60) {
                grade = 'D';
            } else {
                grade = 'F';
            }
            Console.WriteLine("Corresponding letter grade is: " + grade);
            Console.ReadKey();
        }
    }
}
