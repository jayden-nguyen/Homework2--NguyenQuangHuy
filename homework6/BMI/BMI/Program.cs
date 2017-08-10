using System;

namespace BMI
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			double Bmi, height_cm, height_m, mass;
			Console.WriteLine("PLease input your height(cm): ");
			height_cm = System.Convert.ToDouble(Console.ReadLine());
			Console.WriteLine("Please input your mass(kg): ");
			mass = System.Convert.ToDouble (Console.ReadLine ());
			height_m = height_cm / 100;
			Bmi = mass / (height_m * height_m);
			Console.WriteLine ("Your BMI is : {0}",Bmi,"\n");
			if (Bmi < 16) {
				Console.WriteLine ("Severely underweight");
			}else if(Bmi < 18.5){
				Console.WriteLine ("UnderWeight");
			}else if(Bmi < 25){
				Console.WriteLine ("Normal");
			}else if(Bmi < 30){
				Console.WriteLine ("Overweight");
			}else {
				Console.WriteLine ("Obese");
			}
		}
	}
}
