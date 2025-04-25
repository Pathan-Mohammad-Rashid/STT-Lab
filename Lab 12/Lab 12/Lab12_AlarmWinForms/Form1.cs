using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace Lab12_AlarmWinForms
{
    public partial class Form1 : Form
    {
        private DateTime targetTime;
        private Random rnd = new Random();
        //private Timer colorTimer;
        //private Timer checkTimer;

        public Form1()
        {
            InitializeComponent();

            // Initialize timers
            colorTimer = new Timer();
            colorTimer.Interval = 1000; // 1 second
            colorTimer.Tick += colorTimer_Tick;

            checkTimer = new Timer();
            checkTimer.Interval = 500; // 0.5 seconds
            checkTimer.Tick += checkTimer_Tick;
        }

        private void btnStart_Click(object sender, EventArgs e)
        {
            // Validate time input
            if (!DateTime.TryParseExact(txtTimeInput.Text, "HH:mm:ss",
                CultureInfo.InvariantCulture, DateTimeStyles.None, out targetTime))
            {
                MessageBox.Show("Invalid time format! Please use HH:MM:SS",
                    "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Disable controls during countdown
            txtTimeInput.Enabled = false;
            btnStart.Enabled = false;

            // Start timers
            colorTimer.Start();
            checkTimer.Start();
        }

        private void colorTimer_Tick(object sender, EventArgs e)
        {
            // Change background color every second
            this.BackColor = GetRandomPastelColor();
        }

        private void checkTimer_Tick(object sender, EventArgs e)
        {
            DateTime currentTime = DateTime.Now;

            // Check if hours, minutes and seconds match
            if (currentTime.Hour == targetTime.Hour &&
                currentTime.Minute == targetTime.Minute &&
                currentTime.Second == targetTime.Second)
            {
                // Stop timers
                colorTimer.Stop();
                checkTimer.Stop();

                // Show message
                MessageBox.Show($"ALARM! Time reached: {targetTime:HH:mm:ss}",
                    "Alarm Triggered", MessageBoxButtons.OK, MessageBoxIcon.Information);

                // Reset UI
                txtTimeInput.Enabled = true;
                btnStart.Enabled = true;
                this.BackColor = SystemColors.Control;
            }
        }

        private Color GetRandomPastelColor()
        {
            // Generate pastel colors (values between 150-255)
            return Color.FromArgb(
                rnd.Next(150, 256),
                rnd.Next(150, 256),
                rnd.Next(150, 256)
            );
        }

        // These empty methods can be kept or removed
        private void Form1_Load(object sender, EventArgs e) { }
        private void lblTimeInput_Click(object sender, EventArgs e) { }
        private void txtTimeInput_TextChanged(object sender, EventArgs e) { }
    }
}