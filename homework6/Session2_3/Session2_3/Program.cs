using System;

namespace Session2_3
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			int row, col;
			Console.WriteLine (" Input the number of row: ");
			row = Int32.Parse( (Console.ReadLine ()));
			Console.WriteLine (" Input the number of column: ");
			col = Int32.Parse( (Console.ReadLine ()));
			for (int i = 0; i < row; i++) {
				for (int j = 0; j < col; j++) {
					if (i % 2 == 0) {
						if (j % 2 == 0) {
							Console.Write ("x");
						} else
							Console.Write ("*");
					} else {
						if (j % 2 == 0) {
							Console.Write ("*");
						}else
							Console.Write("x");
					}

				}Console.Write ("\n");
			}
		}
	}
}
