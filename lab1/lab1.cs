using System;
using System.ComponentModel;

class Program
{
    static void print_asw(double a, double b, double c)
    {
        double dis = b * b - 4 * a * c;

        if (dis < 0)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Нет корней");
            Console.ResetColor();
        }
        if (dis == 0)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("x=" + Convert.ToString(-b + Math.Sqrt(dis)));
            Console.ResetColor();
        }
        if (dis > 0)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("x1 = " + Convert.ToString((-b + Math.Sqrt(dis)) / (2 * a)));
            Console.WriteLine("x2 = " + Convert.ToString((-b - Math.Sqrt(dis)) / (2 * a)));
            Console.ResetColor();
        }
    }


    static void Main(string[] arg)
    {
        double a;
        double b;
        double c;
        Console.WriteLine("Введите коэффициенты a, b, c:");
        while (true)
        {
            try
            {
                Console.Write("Введите параметр a:");
                a = Convert.ToDouble(Console.ReadLine());
                Console.Write("Введите параметр b:");
                b = Convert.ToDouble(Console.ReadLine());
                Console.Write("Введите параметр c:");
                c = Convert.ToDouble(Console.ReadLine());
            }
            catch (FormatException)
            {
                Console.WriteLine("Неверный формат ввода!");
                continue;
            }
            break;
        }

        print_asw(a,b,c);

    }
}