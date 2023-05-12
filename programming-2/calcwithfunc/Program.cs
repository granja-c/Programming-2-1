using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calcwithfunc
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Num 1: ");
            int n1 = int.Parse(Console.ReadLine());
            Console.Write("Num 2: ");
            int n2 = int.Parse(Console.ReadLine());
            Console.Write("Choose an option- add, sub, mul, or div: ");
            string op = Console.ReadLine();
            int res = 0;
            if (op == "add") res = add(n1, n2);
            else if (op == "sub") res = sub(n1, n2);
            else if (op == "mul") res = mul(n1, n2);
            else if (op == "div") res = div(n1, n2);
            Console.WriteLine("Result: " + res);
            wait();
        }
        // <access level> <static or not> <return type> <name>(<args>) {}
        // in console apps, all funcs static, not in form apps, public regardless
        public static void wait()
        {
            Console.ReadKey();
        }
        static int add(int x, int y) {
            return x + y;
        }
        static int sub(int x, int y)
        {
            return x - y;
        }
        static int mul(int x, int y)
        {
            return x * y;
        }
        static int div(int x, int y)
        {
            return x / y;
        }
    }
}
