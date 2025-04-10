using System;

class LoopExample
{
    static void PrintNumbers()
    {
        Console.WriteLine("Numbers from 1 to 10:");
        for (int i = 1; i <= 10; i++)
        {
            Console.Write(i + " ");
        }
        Console.WriteLine();
    }

    static int Factorial(int n)
    {
        int result = 1;
        for (int i = 2; i <= n; i++)
        {
            result *= i;
        }
        return result;
    }

    static void Main()
    {
        PrintNumbers();

        while (true)
        {
            Console.Write("\nEnter a number for factorial calculation (or type 'exit' to quit): ");
            string input = Console.ReadLine();
            if (input.ToLower() == "exit") break;

            int num;
            if (int.TryParse(input, out num) && num >= 0)
            {
                Console.WriteLine($"Factorial of {num} is: {Factorial(num)}");
            }
            else
            {
                Console.WriteLine("Invalid input! Please enter a non-negative integer.");
            }
        }
    }
}
