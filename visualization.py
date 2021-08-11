from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from tkinter import *
from sorting import *

#Sorting Algorithms
algo = ['Selection Sort', 'Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort']

def sortit():

    #Variables
    n = w.get() #Number of elements
    l = np.arange(1, n) #List of the elements from 1 to n
    length = len(l) #Length of List l
    al = var.get() #Name of the algorithm to be used

    np.random.shuffle(l) #Shuffle the elements in the list

    #Choose the algorithm based on the variable 'al'
    if al==algo[0]:
        generator = selectionsort(l)
    if al==algo[1]:
        generator = bubblesort(l)
    if al==algo[2]:
        generator = insertionsort(l)
    if al==algo[3]:
        generator =  mergesort(l, 0, len(l)-1)
    if al==algo[4]:
        generator = quicksort(l, 0, len(l)-1)

    #Plot a Bar Graph
    plt.bar(range(length), l, align='edge')

    #Function to animate the Bar Graph
    def animate(i):
        plt.cla()
        plt.bar(range(length), next(generator), align='edge')

    ani = FuncAnimation(plt.gcf(), animate, frames=generator,interval = 1, repeat=False) #Fnction to perform the Animation

    plt.show()
    plt.tight_layout()

#Tkinter Main
root = Tk()

var = StringVar()

Label(root, text="Choose the sorting algorithm and number of elements").grid(row=0, column=0)

Label(root, text="Number of elements: ").grid(row=1, column=0)
w = Scale(root, from_=1, to=100, orient=HORIZONTAL)
w.grid(row=1, column=1)

Label(root, text="Algorithm: ").grid(row=2, column=0)
g = OptionMenu(root, var, *algo)
var.set("Selection Sort")
g.grid(row=2, column=1)

Button(root, text='SORT', command=sortit).grid(row=3, column=1)

root.mainloop()
