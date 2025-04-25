using System;
using System.Threading;

namespace ConsoleAppAlarm
{
    // Event arguments class to hold alarm-related data
    public class AlarmEventArgs : EventArgs
    {
        public DateTime AlarmTime { get; set; }

        public AlarmEventArgs(DateTime alarmTime)
        {
            AlarmTime = alarmTime;
        }
    }

    // Publisher class
    public class AlarmClock
    {
        // Define the delegate for the event
        public delegate void AlarmEventHandler(object sender, AlarmEventArgs e);

        // Declare the event using the delegate
        public event AlarmEventHandler raiseAlarm;

        private DateTime targetTime;

        public AlarmClock(DateTime time)
        {
            targetTime = time;
        }

        // Method to continuously check current time against target time
        public void CheckTime()
        {
            Console.WriteLine("Checking time...");

            while (true)
            {
                DateTime currentTime = DateTime.Now;

                // Check if hours, minutes, and seconds match
                if (currentTime.Hour == targetTime.Hour &&
                    currentTime.Minute == targetTime.Minute &&
                    currentTime.Second == targetTime.Second)
                {
                    // Raise the event
                    OnRaiseAlarm(targetTime);
                    break;
                }

                // Wait a short time before checking again
                Thread.Sleep(500);
            }
        }

        // Method to raise the event
        protected virtual void OnRaiseAlarm(DateTime time)
        {
            // Check if there are any subscribers
            if (raiseAlarm != null)
            {
                AlarmEventArgs args = new AlarmEventArgs(time);
                raiseAlarm(this, args); // Raise the event
            }
        }
    }

    // Subscriber class
    public class AlarmListener
    {
        // Event handler method
        public void Ring_alarm(object sender, AlarmEventArgs e)
        {
            Console.WriteLine("====================================");
            Console.WriteLine($"ALARM! The time is now {e.AlarmTime.ToString("HH:mm:ss")}");
            Console.WriteLine("====================================");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Alarm Clock Application");
            Console.WriteLine("----------------------");

            // Get target time from user
            DateTime targetTime = GetTimeFromUser();

            Console.WriteLine($"Alarm set for {targetTime.ToString("HH:mm:ss")}");
            Console.WriteLine("Waiting for the alarm time...");

            // Create the publisher (AlarmClock) and subscriber (AlarmListener)
            AlarmClock clock = new AlarmClock(targetTime);
            AlarmListener listener = new AlarmListener();

            // Subscribe to the event
            clock.raiseAlarm += listener.Ring_alarm;

            // Start checking the time
            clock.CheckTime();

            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }

        // Helper method to get valid time input from user
        static DateTime GetTimeFromUser()
        {
            DateTime targetTime;
            bool validInput = false;

            do
            {
                Console.Write("Enter the target time (HH:MM:SS): ");
                string input = Console.ReadLine();

                try
                {
                    // Try to parse the time string
                    targetTime = DateTime.ParseExact(input, "HH:mm:ss",
                        System.Globalization.CultureInfo.InvariantCulture);

                    validInput = true;
                    return targetTime;
                }
                catch (Exception)
                {
                    Console.WriteLine("Invalid time format. Please use HH:MM:SS format.");
                    validInput = false;
                }
            } while (!validInput);

            // This should never be reached
            return DateTime.Now;
        }
    }
}
