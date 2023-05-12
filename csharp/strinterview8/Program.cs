using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace strinterview8
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a string: ");
            string txt = Console.ReadLine();
            Console.Write("Enter a character to search for: ");
            string search = Console.ReadLine();
            int tLen = txt.Length;
            int sLen = search.Length;
            int res = 0;

            for (int lcv = 0; lcv <= tLen - sLen; lcv++)
            {
                if (txt.Substring(lcv, sLen) == search) {
                    res++;
                }
            }
            if (res == 0) Console.WriteLine(search + " does not occur in " + txt);
            else if (res == 1) Console.WriteLine("The character " + search + " occurs in " + txt + " 1 time.");
            else Console.WriteLine("The character " + search + " occurs in " + txt + " " + res + " times.");
            Console.ReadKey();
        }
    }
}
