using System;
using System.Linq;

namespace PS3_Q2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number of elements n and m in array a and array b");
            var inputRead = Console.ReadLine().Split(' ');
            int n = int.Parse(inputRead[0]);
            int m = int.Parse(inputRead[1]);
            //While loop to check the constraint 1 ≤ 𝑛, 𝑚 ≤ 10
            while ((n<= 1 | n>= 10) | (m <= 1 | m >= 10))
            {
                Console.WriteLine("n and m constraint violation. Enter n and m where 1 ≤ n, m ≤ 10");
                inputRead = Console.ReadLine().Split(' ');
                n = int.Parse(inputRead[0]);
                m = int.Parse(inputRead[1]);
            }
            int[] a = new int[n];
            Console.WriteLine("Enter the array elements for a");
            var inputReadArrayA = Console.ReadLine().Split(' ');
            for (int i = 0; i < n; i++)
            {
                a[i] = int.Parse(inputReadArrayA[i]);
                //While loop to check the constraint 1 ≤ 𝑎[𝑖] ≤ 100
                while ((inputReadArrayA.Count() > n) | (a[i] <= 1 | a[i] >= 100))
                {
                    
                    Console.WriteLine("invalid data. Enter the array a[i] again");
                    inputReadArrayA = Console.ReadLine().Split(' ');
                    a[i] = int.Parse(inputReadArrayA[i]);
                }
                
            }
            int[] b = new int[m];
            Console.WriteLine("Enter the array elements for b");
            var inputReadArrayB = Console.ReadLine().Split(' ');
            for (int j = 0; j < m; j++)
            {
                b[j] = int.Parse(inputReadArrayB[j]);
                //While loop to check the constraint 1 ≤ b[𝑖] ≤ 100
                while ((inputReadArrayB.Count() > m) | (b[j] <= 1 | b[j] >= 100))
                {
                    Console.WriteLine("invalid data. Enter the array b[j] again");
                    inputReadArrayB = Console.ReadLine().Split(' ');
                    b[j] = int.Parse(inputReadArrayB[j]);
                }
                
            }
            int result = getTotalX(a, b);
            Console.WriteLine("\n Output:");
            Console.WriteLine(result);
        }
        /// <summary>
        /// Returns number of integers between a and b
        /// </summary>
        /// <param name="a">int array a</param>
        /// <param name="b">int array b</param>
        /// <returns></returns>
        public static int getTotalX(int[] a, int[] b)
        {
            int count = 0;
            int factor = 0;
            int first = a[0];
            int second = 0;
            for (int i = 0; i < b.Count(); i++)
            {
                factor = findFactor(b[i], factor);
            }
            for (int i = 0; i < a.Count() - 1; i++)
            {
                first = (first * a[i + 1]) / findFactor(a[i + 1], first);
            }
            for (int i = 1; i <= factor && second <= factor; i++)
            {
                second = i * first;
                if (factor % (second) == 0)
                {
                    count = count +1;
                }
            }
            return count;
        }
        /// <summary>
        /// finds the common factor
        /// </summary>
        /// <param name="a">int a</param>
        /// <param name="b">int b</param>
        /// <returns></returns>
        static int findFactor(int a, int b)
        {
            if (a == 0)
            {
                return b;
            }
            else if (b == 0)
            { 
                return a; 
            }
            else if(a == b)
            {
                return a;
            }
            else if(a > b)
            {
                return findFactor(a - b, b);
            }
            else 
            { 
                return findFactor(a, b - a);
            }
            
        }
    }
}
