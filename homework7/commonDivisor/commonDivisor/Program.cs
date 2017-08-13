using System;

namespace commonDivisor
{
    class Program
    {
        static void Main(string[] args)
        {
            GreatestComDiv test1 = new GreatestComDiv();
            Console.Write(test1.GCDOfTwo(10, 35));
            Console.Write("\n");
            Console.Write(test1.GCDOfArray(new int[] { 23,12,21 }));
            Console.Write("\n");
            Console.Write(test1.GCDOfTwo(123, 456));
            Console.Write("\n");
            Console.Write(test1.GCDOfArray(new int[] { 240, 15, 210 ,25}));
            Console.Write("\n");
        }
    }
}