
namespace formsapptest
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.startButton = new System.Windows.Forms.Button();
            this.selFoldButton = new System.Windows.Forms.Button();
            this.printsLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // startButton
            // 
            this.startButton.Location = new System.Drawing.Point(310, 88);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(169, 41);
            this.startButton.TabIndex = 1;
            this.startButton.Text = "Start";
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // selFoldButton
            // 
            this.selFoldButton.Location = new System.Drawing.Point(310, 247);
            this.selFoldButton.Name = "selFoldButton";
            this.selFoldButton.Size = new System.Drawing.Size(169, 41);
            this.selFoldButton.TabIndex = 2;
            this.selFoldButton.Text = "Select Folder";
            this.selFoldButton.UseVisualStyleBackColor = true;
            this.selFoldButton.Click += new System.EventHandler(this.selFoldButton_Click);
            // 
            // printsLabel
            // 
            this.printsLabel.AutoSize = true;
            this.printsLabel.Location = new System.Drawing.Point(78, 260);
            this.printsLabel.Name = "printsLabel";
            this.printsLabel.Size = new System.Drawing.Size(0, 15);
            this.printsLabel.TabIndex = 3;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(782, 391);
            this.Controls.Add(this.printsLabel);
            this.Controls.Add(this.selFoldButton);
            this.Controls.Add(this.startButton);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.Button selFoldButton;
        private System.Windows.Forms.Label printsLabel;
    }
}

