namespace Lab12_AlarmWinForms
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.txtTimeInput = new System.Windows.Forms.TextBox();
            this.lblTimeInput = new System.Windows.Forms.Label();
            this.btnStart = new System.Windows.Forms.Button();
            this.colorTimer = new System.Windows.Forms.Timer(this.components);
            this.checkTimer = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // txtTimeInput
            // 
            this.txtTimeInput.Location = new System.Drawing.Point(331, 156);
            this.txtTimeInput.Name = "txtTimeInput";
            this.txtTimeInput.Size = new System.Drawing.Size(100, 22);
            this.txtTimeInput.TabIndex = 0;
            this.txtTimeInput.TextChanged += new System.EventHandler(this.txtTimeInput_TextChanged);
            // 
            // lblTimeInput
            // 
            this.lblTimeInput.AutoSize = true;
            this.lblTimeInput.Location = new System.Drawing.Point(290, 123);
            this.lblTimeInput.Name = "lblTimeInput";
            this.lblTimeInput.Size = new System.Drawing.Size(195, 16);
            this.lblTimeInput.TabIndex = 1;
            this.lblTimeInput.Text = "Enter Target Time (HH:MM:SS):";
            this.lblTimeInput.Click += new System.EventHandler(this.lblTimeInput_Click);
            // 
            // btnStart
            // 
            this.btnStart.Location = new System.Drawing.Point(331, 184);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(100, 23);
            this.btnStart.TabIndex = 2;
            this.btnStart.Text = "Start Alarm";
            this.btnStart.UseVisualStyleBackColor = true;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // colorTimer
            // 
            this.colorTimer.Interval = 1000;
            this.colorTimer.Tick += new System.EventHandler(this.colorTimer_Tick);
            // 
            // checkTimer
            // 
            this.checkTimer.Interval = 500;
            this.checkTimer.Tick += new System.EventHandler(this.checkTimer_Tick);
            // 
            // Form1
            // 
            this.ClientSize = new System.Drawing.Size(782, 353);
            this.Controls.Add(this.btnStart);
            this.Controls.Add(this.lblTimeInput);
            this.Controls.Add(this.txtTimeInput);
            this.Name = "Form1";
            this.Text = "Alarm Clock";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion


        private System.Windows.Forms.TextBox txtTimeInput;
        private System.Windows.Forms.Label lblTimeInput;
        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.Timer colorTimer;
        private System.Windows.Forms.Timer checkTimer;
    }
}

