using System;
using System.Collections.Generic;

namespace AtraccionParque
{
    public class Atraccion
    {
        private Queue<string> colaEspera = new Queue<string>();
        private const int CapacidadMaxima = 30;

        public void LlegadaPersona(string nombre)
        {
            if (colaEspera.Count < CapacidadMaxima)
            {
                colaEspera.Enqueue(nombre);
                Console.WriteLine($"{nombre} ha llegado a la cola. Posición: {colaEspera.Count}");
            }
            else
            {
                Console.WriteLine($"Lo sentimos {nombre}, la atracción está llena.");
            }
        }

        public void SubirAAtraccion()
        {
            if (colaEspera.Count > 0)
            {
                string persona = colaEspera.Dequeue();
                Console.WriteLine($"¡{persona} subió a la atracción!");
            }
            else
            {
                Console.WriteLine("No hay nadie en la cola.");
            }
        }

        public void MostrarCola()
        {
            Console.WriteLine("\n--- Estado de la Cola ---");
            foreach (var persona in colaEspera)
            {
                Console.WriteLine($"- {persona}");
            }
            Console.WriteLine($"Total en espera: {colaEspera.Count} / {CapacidadMaxima}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Atraccion montanaRusa = new Atraccion();

            // Simulación
            montanaRusa.LlegadaPersona("Juan");
            montanaRusa.LlegadaPersona("Maria");
            montanaRusa.LlegadaPersona("Pedro");

            montanaRusa.MostrarCola();

            montanaRusa.SubirAAtraccion(); // Sale Juan primero
            
            montanaRusa.MostrarCola();

            Console.WriteLine("\nPresiona cualquier tecla para salir...");
            Console.ReadKey();
        }
    }
}
