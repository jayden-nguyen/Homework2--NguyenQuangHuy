using System;
using System.Collections.Generic;
using System.Text;

namespace binaryConvert
{
    class Convert
    {
        public void BiConvert(int [] deciToBina)
        {
            for (int i = 0; i < deciToBina.Length; i++)
            {
                var list = new List<int>();
                int n = 1;
                // create an array consist of binary digit of deciToBina[i] in order
                while (n != 0)
                {
                    list.Add(deciToBina[i] % 2);
                    n = deciToBina[i] / 2;
                    deciToBina[i] = n;
                }
                int[] arr = list.ToArray();
                int[] arr1 = new int[arr.Length];
                for (int k = 0; k < arr.Length; k++)
                {
                    arr1[k] = arr[arr.Length - 1 - k];

                }
                // Merging all digit in arr1 in to the string binary represent deciToBina[i]
                string[] result = new string[arr1.Length];
                for (int k = 0; k < result.Length; k++)
                {
                    result[k] = arr1[k].ToString();
                }
                string huy = String.Join("", result);
                // Casting into int and push into deciToBina[i]
                Int32.TryParse(huy, out deciToBina[i]);

                Console.Write(deciToBina[i]+ " ");

            }
            Console.Write("\n");
        }
    }
}
