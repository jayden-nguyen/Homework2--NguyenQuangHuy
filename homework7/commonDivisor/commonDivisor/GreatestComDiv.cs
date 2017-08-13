using System;
using System.Collections.Generic;
using System.Text;

namespace commonDivisor
{
    class GreatestComDiv
    {
        public int GCDOfTwo(int a, int b)
        {
            while (a != 0 && b != 0)
            {
                if (a > b)
                    a = a - b;
                else b = b - a;

            }
            if (a == 0) return b;
            else
                return a;
        }
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
