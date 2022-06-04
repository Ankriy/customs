using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace customs
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void grid_Loaded(object sender, RoutedEventArgs e)
        {
            List<Tables> result = new List<Tables>(3);

            result.Add(new Tables("0001", "Живая Лошадь", "97%"));

            grid.ItemsSource = result;

        }
        private void ExitButton_MouseDown(object sender, MouseButtonEventArgs e)
        {
            this.Close();   
        }
        private void MinButton_MouseDown(object sender, MouseButtonEventArgs e)
        {
            this.WindowState = WindowState.Minimized;
        }
        private void ToolBar_MouseDown(object sender, MouseButtonEventArgs e)
        {
            if(e.ChangedButton == MouseButton.Left)
            {
                this.DragMove();
            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string fileName = @"C:\Users\user\Downloads\искусственный_интеллект_проводит_таможенный_контроль\predict.py" + " " + SearchBox.Text;

            MessageBox.Show(SearchBox.Text);
            Process p = new Process();
            p.StartInfo = new ProcessStartInfo("python", fileName)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            p.Start();

            string output = p.StandardOutput.ReadToEnd();
            p.WaitForExit();

            MessageBox.Show(output);
            
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            
        }
    }
}
