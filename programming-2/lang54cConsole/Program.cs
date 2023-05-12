using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lang54cConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the diameter:");
            int d = int.Parse(Console.ReadLine());
            double pi = 3.14159;
            double rad = d / 2.0;
            double area = rad * rad * pi;
            double circ = pi * rad * 2;

            Console.WriteLine("The radius is: " + Math.Round(rad, 3));
            Console.WriteLine("The area is: " + Math.Round(area, 3));
            Console.WriteLine("The circumference is: " + Math.Round(circ, 3));
            Console.ReadKey();
        }
    }
}
