using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lang54bConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter num 1: ");
            int num1 = int.Parse(Console.ReadLine());
            Console.Write("Enter num 2: ");
            int num2 = int.Parse(Console.ReadLine());
            Console.Write("Enter num 3: ");
            int num3 = int.Parse(Console.ReadLine());
            Console.Write("Enter num 4: ");
            int num4 = int.Parse(Console.ReadLine());

            int summ = num1 + num2 + num3 + num4;
            double avg = (double)summ / 4;

            Console.WriteLine("The sum is: " + summ);
            Console.Write("The average is: " + Math.Round(avg, 2));
            Console.ReadKey();
        }
    }
}
