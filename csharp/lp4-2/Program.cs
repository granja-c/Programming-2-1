using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lp4_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the weight of the package: ");
            int weight = int.Parse(Console.ReadLine());
            Console.Write("Enter the height of the package: ");
            int height = int.Parse(Console.ReadLine());
            Console.Write("Enter the length of the package: ");
            int leng = int.Parse(Console.ReadLine());
            Console.Write("Enter the width of the package: ");
            int wid = int.Parse(Console.ReadLine());
            int vol = wid * leng * height;

            if (weight > 27 && vol > 100000) {
                Console.WriteLine("Too heavy and too large.");
            } else if (weight > 27) {
                Console.WriteLine("Too heavy.");
            } else if (vol > 100000){
                Console.WriteLine("Too large.");
            } else {
                Console.WriteLine("Package is fine.");
            }
            Console.ReadKey();
        }
    }
}
