using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace strinterview16
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a string: ");
            string txt = Console.ReadLine();
            Console.Write("Enter a substring to search for: ");
            string wrd = Console.ReadLine();
            bool res = searchTxt(txt, wrd);

            Console.WriteLine("Does \"" + txt + "\" contain \"" + wrd + "?");
            if (res == true) Console.WriteLine("Yes it does.");
            else Console.WriteLine("No it does not.");

            Console.ReadKey();

            
        }

        static bool searchTxt(string text, string search)
        {
            int tLen = text.Length;
            int sLen = search.Length;

            if (sLen > tLen) return false;

            for (int lcv = 0; lcv <= tLen - sLen; lcv++)
            {
                if (text.Substring(lcv, sLen) == search) return true;
            }
            // .Substring(first index, len of substr)
            return false;
        }
    }
}
