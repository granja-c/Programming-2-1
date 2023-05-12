using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace strinterview7
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a string: ");
            string wrd = Console.ReadLine().ToLower();

            int vow = 0;
            int cons = 0;

            for (int lcv = 0; lcv < wrd.Length; lcv++) {
                char let = wrd[lcv];
                if (let == 'a' || let == 'e' || let == 'i' || let == 'o' || let == 'u') {
                    vow++;
                }
                else if (let >= 'a' && let <= 'z') cons++;
            }
            Console.WriteLine(wrd + " contains " + vow + " vowels and " + cons + " consonants");
            Console.ReadKey();
        }
    }
}
