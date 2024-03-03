01.Problem Hello Python
Writing Python code requires no additional preparation – creating a file with the .py extension is all we need. So let's directly proceed with writing our first line of code. We will write the following command:

print('Hello Python')

02.Problem: Expression
Write a console-based Python program that calculates and prints the value of the following numerical expression:

(3522 + 52353) * 23 - (2336 * 501 + 23432 - 6743) * 3
Note: you are **not allowed to previously calculate the value** (for example with Windows Calculator).

03.roblem: Numbers from 1 to 20
Write a Python console program that prints the numbers from 1 to 20 on separate lines on the console.

05.Problem: Rectangle Area
Write a Python program that receives two numbers a and b, then calculates and prints the area of a rectangle with sides a and b.
Sample Input and Output
![image](https://github.com/Sasho80/1.-FirstStepsInProgramming/assets/7139995/230b729e-3886-42aa-a2c2-dc76bdef77bf)

06.Problem: Square of Stars
Write a Python console program that reads an integer positive number N from the console and prints a square of N stars on the console, like in the examples below.
   
   input   output                             input   output                                  input   output
   
![image](https://github.com/Sasho80/1.-FirstStepsInProgramming/assets/7139995/a458e71f-9aee-408b-8958-16fb799adf4b)



07.Problem: Program That Converts Levs (BGN - Bulgaria's currency) , into Euros
Let's have a look at another simple program that reads a number of levs(BGN) from the user, converts them into euro (divides them by the euro exchange rate) and prints the result. This is a program of three consecutive commands. Enter and execute them in sequence:

leva = int(input())
euro = leva / 1.95583
print(euro)

08.Problem: A Program That Plays The Music Tone 'A'
Our next program will consist of a single Python command which plays the music tone 'A' (432 hertz) for half a second (500 milliseconds):

import winsound
winsound.Beep(432, 500)

In a Windows environment we will hear a sound. Make sure your speakers aren't muted. On Linux and MacOs, the example won't work.


