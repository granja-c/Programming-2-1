using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace strInterview18
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a string: ");
            string txt = Console.ReadLine();
            Console.Write("Enter a character to remove: ");
            string search = Console.ReadLine();
            int tLen = txt.Length;
            int sLen = search.Length;
            string res = txt;
            int[] ind;

            for (int cnt = 0; cnt < tLen; cnt++)
            {
                if (txt[cnt] == search[0])
                {
                    
                }
            }


        }
    }
}
