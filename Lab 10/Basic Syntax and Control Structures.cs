using System;

class Calculator
{
    static void Main()
    {
        // Accept user input
        Console.Write("Enter first number: ");
        double num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter second number: ");
        double num2 = Convert.ToDouble(Console.ReadLine());

        // Perform operations
        double sum = num1 + num2;
        double difference = num1 - num2;
        double product = num1 * num2;
        double quotient = num2 != 0 ? num1 / num2 : double.NaN;

        // Display results
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine($"Difference: {difference}");
        Console.WriteLine($"Product: {product}");
        Console.WriteLine($"Quotient: {quotient}");

        // Check if sum is even or odd
        if ((int)sum % 2 == 0)
            Console.WriteLine("Sum is even.");
        else
            Console.WriteLine("Sum is odd.");
    }
}
