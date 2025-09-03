using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Semana1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer2();
            Console.ReadKey();
        }

        static void ejer1()
        {
            string nombre, carrera;
            Console.Write("Ingrese su nombre: ");
            nombre = Console.ReadLine();
            Console.Write("Ingresar su carrera: ");
            carrera = Console.ReadLine();
            Console.WriteLine($"\n{nombre}, Bienvenido al curso de Fundamentos de Algoritmos de la carrera {carrera}");
        }
        static void ejer2()
        {
            string nombre;
            nombre = "Juan";
            Console.WriteLine("\" + nombre + "\");
        }
        static void ejer3()
        {

        }
        static void ejer4()
        {

        }
        static void ejer5()
        {

        }
        static void ejer6()
        {

        }
    }
}
