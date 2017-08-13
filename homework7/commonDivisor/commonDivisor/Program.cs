using System;

namespace commonDivisor
{
    class Program
    {
        static void Main(string[] args)
        {
            GreatestComDiv test1 = new GreatestComDiv();
            Console.Write(test1.GCDOfTwo(10, 35));
            Console.Write(test1.GCDOfArray(new int[] { 23,12,21 }));
        }
    }
}