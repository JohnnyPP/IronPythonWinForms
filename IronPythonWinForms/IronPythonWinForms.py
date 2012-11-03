import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference("System.Drawing")

from System.Windows.Forms import *
from System.Drawing import Size, Point

class MyForm(Form):
    def __init__(self):
         button = Button()
         button.Text = 'Test'
         button.Location = Point(10, 10)
         self.Controls.Add(button)


form = MyForm()
Application.Run(form)
