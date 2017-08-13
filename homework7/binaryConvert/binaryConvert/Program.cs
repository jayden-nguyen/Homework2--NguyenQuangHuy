using System;
using System.Collections.Generic;
namespace binaryConvert
{
    class Program
    {
        static void Main(string[] args)
        {
            Convert convert = new Convert();
            convert.BiConvert(new int[] { 1, 2, 3 });
            convert.BiConvert(new int[] { 21, 22, 45, 123, 456 });
        }
    }
}