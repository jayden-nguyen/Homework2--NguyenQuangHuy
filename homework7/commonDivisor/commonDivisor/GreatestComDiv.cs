using System;
using System.Collections.Generic;
using System.Text;

namespace commonDivisor
{
    class GreatestComDiv
    {
        // method return the Greatest Common divisor of two number using Euclid algrorithm
        public int GCDOfTwo(int a, int b)
        {
            int n = 1;
            while(n != 0) {
                if (a > b)
                    a = a - b;
                else b = b - a;
                n = (a < b) ? a : b;
            }
            if (a != 0) return a;
            else return b;
            
        }
        // method return the Greatest Common divisor of a list
        public int GCDOfArray(int [] test)
        {
            int temp;
            if (test.Length == 1)
                return Math.Abs(test[0]);
            else {
                temp = Math.Abs(test[0]);
                for (int i = 0; i < test.Length; i++)
                {
                    temp = GCDOfTwo(temp, Math.Abs(test[i]));
                }
                return temp;
            }
        }
    }
}
