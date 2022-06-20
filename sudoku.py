# -*- coding: utf-8 -*-
"""
@author: Danny Foley
@project: sudoku solver
"""

from tkinter import *
import array
import time

class Sudoku:
    columns = 9
    rows = 9
    
    def __init__(self):
        self.grid = [[0 for x in range(columns)] for y in range(rows)]
        self.poss = [[0 for x in range(columns)] for y in range(rows)]
        self.r = [[0 for x in range(columns)] for y in range(rows)]
        self.c = [[0 for x in range(columns)] for y in range(rows)]
    
    def printgrid(self, r, c, k):
        print("ROW ", r+1, " COL ", c+1, "NUMBER ENTERED: ",k )
        for i in range(rows):
            print("GRID: ", self.grid[i])
            
    def value_check():
    
    def update(self):
        for i in range(columns):
            for j in range(rows):
                self.r[i][j] = self.grid[i][j]
                self.c[i][j] = self.grid[j][i]
    def solve(self):
        for i in range(columns):
            for j in range(rows):
                self.r[i][j] = self.grid[i][j]
                self.c[i][j] = self.grid[j][i]
        
        for i in range(columns):
            for j in range(rows):
                if(self.grid[i][j] == 0):
                    self.poss[i][j] = check_3x3(i, j)
                    temp = self.poss[i][j]
                    for k in reversed(self.poss[i][j]):
                        if k in self.c[j]:
                            temp.remove(k)
                    for k in reversed(self.poss[i][j]):
                        if k in self.r[i]:
                            temp.remove(k)
                    self.poss[i][j] = temp
                    if len(self.poss[i][j]) == 1:
                        self.grid[i][j] = self.poss[i][j][0]
                        self.poss[i][j] = 0
                        value[i][j].set(grid[i][j])
                        printgrid(i, j, self.grid[i][j])
                        return solve()
                print("col:", j+1, "row:" , i+1," ", poss[i][j])
                
        result = check_columns()
        if(result):
            return solve()
        
        result = check_rows()
        if(result):
            return solve()
            
        result = check_3x3s()
        if(result):
            return solve()
        
        for i in range(columns):
            for j in range(rows):
                if(grid[i][j] == 0):
                    return -1
                else:
                    return 0
    

LOOP_ACTIVE = True
columns = 9
rows = 9
r = [[0 for x in range(columns)] for y in range(rows)]
c = [[0 for x in range(columns)] for y in range(rows)]
entry = [[0 for x in range(columns)] for y in range(rows)]
grid = [[0 for x in range(columns)] for y in range(rows)]
win = Tk() # give title and dimensions
value = [[0 for x in range(columns)] for y in range(rows)]
poss = [[0 for x in range(columns)] for y in range(rows)]

def exitloop():
    solve()
    print("done")
def printgrid(r, c, k):
    print("ROW ", r+1, " COL ", c+1, "NUMBER ENTERED: ",k )
    for i in range(rows):
        print("GRID: ", grid[i])      
def value_check(): #makes sure that the value of the cells is always between 1 and 9 and is only 1 character long, also imports value array into grid array
    for i in range(columns):
        for j in range(rows):
            if(len(value[i][j].get()) > 1):
                what = value[i][j].get()
                value[i][j].set(what[:1])
            if(value[i][j].get() != "" and (value[i][j].get() < "1" or value[i][j].get() > "9")):
                value[i][j].set("")
    for i in range(columns):
        for j in range(rows):
            if(value[i][j].get() != ""):
                grid[i][j] = int(value[i][j].get())
                
            else:
                grid[i][j] = 0
    win.after(1, value_check)
def fill():
    found = 0
    i = 0
    j = 0
    for i in range(columns):
        for j in range(rows):
            if(grid[i][j] == 0 and found == 0):
                if(len(poss[i][j]) == 2):
                    grid[i][j] = poss[i][j][0]
                    tempi = i
                    tempj = j
                    found = 1
            else:
                break
        if(found == 1):
            break
    pregrid = grid
    filled = solve()
    if(filled):
        correct = check_correct()
        if(correct == 0):
            return 0
        else:
            solved = 0
            for i in range(rows):
                for j in range(columns):
                    grid[i][j] = pregrid[i][j]
def solve():
    for i in range(columns):
        for j in range(rows):
            r[i][j] = grid[i][j]
            c[i][j] = grid[j][i]
    
    for i in range(columns):
        for j in range(rows):
            if(grid[i][j] == 0):
                poss[i][j] = check_3x3(i, j)
                temp = poss[i][j]
                for k in reversed(poss[i][j]):
                    if k in c[j]:
                        temp.remove(k)
                for k in reversed(poss[i][j]):
                    if k in r[i]:
                        temp.remove(k)
                poss[i][j] = temp
                if len(poss[i][j]) == 1:
                    grid[i][j] = poss[i][j][0]
                    poss[i][j] = 0
                    value[i][j].set(grid[i][j])
                    printgrid(i, j, grid[i][j])
                    return solve()
            print("col:", j+1, "row:" , i+1," ", poss[i][j])
            
    result = check_columns()
    if(result):
        return solve()
    
    result = check_rows()
    if(result):
        return solve()
        
    result = check_3x3s()
    if(result):
        return solve()
    
    for i in range(columns):
        for j in range(rows):
            if(grid[i][j] == 0):
                return -1
            else:
                return 0  
def check_columns():
    for i in range(columns):
        got1 = 0
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range (rows):
            if(grid[j][i] == 0):
                print("POSS IN", j + 1, " ", i + 1, " ", poss[j][i])
                for k in poss[j][i]:
                    count[k-1] += 1
        print("COUNT FOR COL ", i + 1, " ", count)        
        for k, val in enumerate(count):
            if (val == 1):
                for m in range(rows):
                    if(grid[m][i] == 0):
                        if k+1 in poss[m][i]:
                            grid[m][i] = k+1
                            value[m][i].set(grid[m][i])
                            printgrid(m, i, grid[m][i])
                            got1 = 1
                            return got1
    return got1
def check_correct():
    correct_col = check_columns_correct()
    correct_row = check_rows_correct()
    if(correct_col == 0 and correct_row == 0):
        return 0
    return -1       
def check_rows_correct():
    for i in range(rows):
        got1 = 0
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range (columns):
            if(grid[i][j] == 0):
                print("POSS IN ROW", i + 1, " COL", j + 1," ", poss[i][j])
                for k in poss[i][j]:
                    count[k-1] += 1
        print("COUNT FOR ROW ", i + 1, " ", count)
        for k, val in enumerate(count):
            if(val == 1):
                got1 += 1
        if(got1 != 9):
            return -1
    return 0
def check_columns_correct():
    for i in range(columns):
        got1 = 0
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range (rows):
            if(grid[j][i] == 0):
                print("POSS IN", j + 1, " ", i + 1, " ", poss[j][i])
                for k in poss[j][i]:
                    count[k-1] += 1
        print("COUNT FOR COL ", i + 1, " ", count)        
        for k, val in enumerate(count):
            if (val == 1):
                got1 += 1
        if(got1 != 9):
            return -1
    return 0
def check_rows():
    for i in range(rows):
        got1 = 0
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range (rows):
            if(grid[i][j] == 0):
                print("POSS IN ROW", i + 1, " COL", j + 1," ", poss[i][j])
                for k in poss[i][j]:
                    count[k-1] += 1
        print("COUNT FOR ROW ", i + 1, " ", count)
        for k, val in enumerate(count):
            if (val == 1):
                for m in range(rows):
                    if(grid[i][m] == 0):
                        if k+1 in poss[i][m]:
                            grid[i][m] = k+1
                            value[i][m].set(grid[i][m])
                            printgrid(i, m, grid[i][m])
                            got1 = 1
                            return got1
    return got1
def check_3x3s():
    for i in range(rows):
        for j in range(columns):
            row = i
            col = j
            got1 = 0
            count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            if(row < 3 and col < 3): #top left
                block = 1
                left_i = 0
                right_i = 3
                left_j = 0
                right_j = 3
            elif(row < 3 and col > 2 and col < 6): #top middle
                block = 2
                left_i = 0
                right_i = 3
                left_j = 3
                right_j = 6
            elif(row < 3 and col > 5): # top right
                block = 3
                left_i = 0
                right_i = 3
                left_j = 6
                right_j = 9
            elif(row > 2 and row < 6 and col < 3): #middle left
                block = 4
                left_i = 3
                right_i = 6
                left_j = 0
                right_j = 3
            elif(row > 2 and row < 6 and col > 2 and col < 6): #center
                block = 5
                left_i = 3
                right_i = 6
                left_j = 3
                right_j = 6
            elif(row > 2 and row < 6 and col > 5): #middle right
                block = 6
                left_i = 3
                right_i = 6
                left_j = 6
                right_j = 9
            elif(row > 5 and col < 3): #bot left
                block = 7
                left_i = 6
                right_i = 9
                left_j = 0
                right_j = 3
            elif(row > 5 and col > 2 and col < 6): #bot middle
                block = 8
                left_i = 6
                right_i = 9
                left_j = 3
                right_j = 6
            elif(row > 5 and col > 5): #bot right
                block = 9
                left_i = 6
                right_i = 9 
                left_j = 6
                right_j = 9
            else:
                print("its fucked")
            for k in range(left_i,right_i):
                for l in range(left_j,right_j):
                    if(grid[k][l] == 0):
                        for m in poss[k][l]:
                            count[m-1] += 1
            print("ROW", row+1, " COL", col+1, " : ", count, "B: ", block)
            for k, val in enumerate(count):
                if (val == 1):
                    for l in range(left_i,right_i):
                        for m in range(left_j,right_j):
                            if(grid[l][m] == 0):
                                if k+1 in poss[l][m]:
                                    grid[l][m] = k+1
                                    value[l][m].set(grid[l][m])
                                    printgrid(l, m, grid[l][m])
                                    got1 = 1
                                    return got1
    return got1
def check_3x3(i, j):
    row = i
    col = j
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if(row < 3 and col < 3): #top left
        for i in range(0,3):
            for j in range(0,3):
                if(grid[i][j] != 0):
                    possible.remove(grid[i][j])
                    
    elif(row < 3 and col > 2 and col < 6): #top middle
        for i in range(0,3):
            for j in range(3,6):
                if(grid[i][j] != 0):
                    possible.remove(grid[i][j])
                    
    elif(row < 3 and col > 5): # top right
        for i in range(0,3):
            for j in range(6,9):
                if(grid[i][j] != 0):
                    possible.remove(grid[i][j])
                    
    elif(row > 2 and row < 6 and col < 3): #middle left
        for i in range(3,6):
            for j in range(0,3):
                if(grid[i][j] != 0):
                    possible.remove(grid[i][j])
                    
    elif(row > 2 and row < 6 and col > 2 and col < 6): #center
        for i in range(3,6):
            for j in range(3,6):
                if(grid[i][j] != 0):
                    possible.remove(grid[i][j])
                    
    elif(row > 2 and row < 6 and col > 5): #middle right
        for i in range(3,6):
            for j in range(6,9):
                if(grid[i][j] != 0):
                    possible.remove(grid[i][j])
                    
    elif(row > 5 and col < 3): #bot left
        for i in range(6,9):
            for j in range(0,3):
                if(grid[i][j] != 0):
                    possible.remove(grid[i][j])
                    
    elif(row > 5 and col > 2 and col < 6): #bot middle
        for i in range(6,9):
            for j in range(3,6):
                if(grid[i][j] != 0):
                    possible.remove(grid[i][j])
                    
    elif(row > 5 and col > 5): #bot right
        for i in range(6,9):
            for j in range(6,9):
                if(grid[i][j] != 0):
                    possible.remove(grid[i][j])
    else:
        print("its fucked")
    return possible
def setup():
    values = [[0, 9, 0, 6, 0, 0, 2, 0, 0],
              [0, 4, 0, 0, 0, 5, 0, 0, 0],
              [0, 0, 0, 0, 0, 7, 0, 1, 0],
              [0, 1, 2, 7, 6, 4, 0, 0, 0],
              [0, 0, 0, 0, 9, 0, 0, 0, 0],
              [0, 8, 6, 1, 0, 0, 0, 7, 0],
              [0, 0, 0, 0, 7, 1, 3, 4, 0],
              [0, 7, 4, 2, 5, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 7, 2, 0]]
    for i in range(columns):
        for j in range(rows):
            value[i][j].set(values[i][j])

def main():
    button = Button(win, text="Solve", command = exitloop).grid(row = 10, column = 4)
    for i in range(columns):
        for j in range(rows):
            value[i][j] = StringVar()
            entry[i][j] = Entry(win, font = "Helvetica 44 bold", bd = 1, width = 2, justify = "center", relief = "sunken", textvariable = value[i][j])
            entry[i][j].grid(row = i, column = j)
    
    
    setup()
    win.after(1, value_check)
    
    win.mainloop()
    
main()

