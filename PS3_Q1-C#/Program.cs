using System;

namespace PS3_Q1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number of Test Cases");
            int t = int.Parse(Console.ReadLine());
            while (t <= 1 | t >= 10)
            {
                Console.WriteLine("The \"t\" constraint is violated. Enter t, where 1 ≤ t ≤ 10");
                t = int.Parse(Console.ReadLine());
            }
            for (int j = 0; j < t; j++)
            {
                Console.WriteLine($"Test Case {j+1}.");
                Console.WriteLine("Enter  the number of students n and the cancellation threshold k");
                var inputRead = Console.ReadLine().Split(' ');
                int n = int.Parse(inputRead[0]);
                int k = int.Parse(inputRead[1]);
                while ((n <= 1 | t >= 1000) & (k <= 1 | t >= n) )
                {
                    Console.WriteLine("The \"n\" and \"k\" constraint is violated. Enter n and k, where 1 ≤ n ≤ 1000 and 1 ≤ k ≤ n");
                    inputRead = Console.ReadLine().Split(' ');
                    n = int.Parse(inputRead[0]);
                    k = int.Parse(inputRead[1]);
                }
                int[] a = new int[n];
                Console.WriteLine("Enter the arrival times of each student in an array representation");
                var inputReadArray = Console.ReadLine().Split(' ');
                try
                {
                    for (int i = 0; i < n; i++)
                    {

                        a[i] = int.Parse(inputReadArray[i]);
                        while (a[i] <= -100 | a[i] >= 100)
                        {
                            Console.WriteLine("The \"a[i]\" constraint is violated. Enter a[i], where −100 ≤ a[i] ≤ 100 and i ∈ [1, … n]");
                            inputReadArray = Console.ReadLine().Split(' ');
                            a[i] = int.Parse(inputReadArray[i]);
                        }
                    }
                }
                catch
                {
                    Console.WriteLine($"Constraint vilolation. Enter the array again");
                    inputReadArray = Console.ReadLine().Split(' ');
                    for (int i = 0; i < n; i++)
                    {
                        a[i] = int.Parse(inputReadArray[i]);
                    }
                }
            //Calling the function angryProfessor
            string output = angryProfessor(a, k);
            Console.WriteLine(output);
            }
        }
        /// <summary>
        /// Function to check if the classes will continue or get cancelled
        /// </summary>
        /// <param name="a"> integer array</param>
        /// <param name="k">the threshold number of students</param>
        /// <returns> Yes if classes are cancelled, No if the classes continue</returns>
        public static string angryProfessor(int[] a, int k)
        {
            int count = new int();
            foreach (var item in a)
            {
                if (item <= 0)
                {
                    count++;
                }
            }
            if (count >= k)
            {
                string ans = "NO";
                return ans;
            }
            else
            {
                string ans = "YES";
                return ans;
            }  
        }
    }
}
