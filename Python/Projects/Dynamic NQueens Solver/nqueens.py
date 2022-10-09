from time import time
from tkinter import *
from tkinter import ttk, messagebox
from itertools import permutations

class NQueens():

    def __init__(self, master):
        self.n = 8 # default number of queens
        self.queens = [0 for i in range(self.n)]
        self.index = 0
        self.solutions = None

        self.master = master
        self.master.title('NQueens Board')
        self.master.configure(background = '#e1d8b9')
        self.master.minsize(400, 470)
        self.master.resizable(True, True)
        self.master.bind('<Configure>', lambda e: self.draw_board())

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9')

        self.board_canvas = Canvas(self.master)
        self.board_canvas.pack()

        self.controls_frame = ttk.Frame(self.master)
        self.controls_frame.pack(side = TOP, pady = 10)

        ttk.Label(self.controls_frame, text = 'Number of Queens:',
                  font = 'Verdana 10 bold').grid(row = 0, column = 0)
        self.n_var = StringVar()
        self.n_var.set(self.n)
        Spinbox(self.controls_frame, from_ = 4, to = 99, width = 2,
                font = 'Verdana 10 bold', textvariable = self.n_var).grid(row = 0, column = 1)
        ttk.Button(self.controls_frame, text = 'Get Next Solution',
                   command = self.solution_callback).grid(row = 1, column = 0, columnspan = 2)
        ttk.Label(self.controls_frame).grid(row = 0, column = 2, padx = 10)

        self.solution_var = StringVar()
        self.time_var = StringVar()
        self.solution_var.set('--')
        self.time_var.set('--')
        ttk.Label(self.controls_frame, text = 'Solution:',
                  font = 'Verdana 10 bold').grid(row = 0, column = 3, sticky= (E))
        ttk.Label(self.controls_frame, textvariable = self.solution_var,
                  font = 'Verdana 10').grid(row = 0, column = 4, sticky = (W))
        ttk.Label(self.controls_frame, text = 'Elapsed Time:',
                  font = 'Verdana 10 bold').grid(row = 1, column = 3, sticky = (E))
        ttk.Label(self.controls_frame, textvariable = self.time_var,
                  font = 'Verdana 10').grid(row = 1, column = 4, sticky = (W))

        self.solution_callback() # begin by showing first solution to 8 queens

    def draw_board(self):
        maxboardsize = min(self.master.winfo_height() - 70, self.master.winfo_width())
        cellsize = maxboardsize // self.n
        self.board_canvas.config(height = self.n*cellsize, width = self.n*cellsize)
        self.board_canvas.delete('all')

        # color in black board cells
        for i in range(self.n):
            for j in range(self.n):
                if (i+j+self.n) % 2: # black cell
                    self.board_canvas.create_rectangle(i*cellsize, j*cellsize,
                                                i*cellsize+cellsize, j*cellsize+cellsize, fill = 'black')
            # draw a queen
            self.board_canvas.create_text(i*cellsize+cellsize//2, self.queens[i]*cellsize+cellsize//2,
                                          text = u'\u265B', font = ('Arial', cellsize//2), fill = 'orange')

    def solution_callback(self):
        try:
            input_val = int(self.n_var.get())
        except:
            messagebox.showerror(title = 'Invalid Input',
                                 message = 'Must enter a number for N.')
            return

        # check if N has changed or if this is first run
        if self.n != input_val or self.solutions == None:
            if 4 > input_val:
                messagebox.showerror(title = 'Invalid Value for N',
                                     message = 'N must be greater than 4.')
            else:
                self.n = input_val
                self.index = 0
                self.solutions = []

                start_time = time()

                # calculate new list of solutions
                columns = range(self.n)
                for perm in permutations(columns):
                    diag1 = set()
                    diag2 = set()
                    for i in columns:
                        diag1.add(perm[i]+i) # checks / diagonal
                        diag2.add(perm[i]-i) # checks \ diagonal
                    if self.n == len(diag1) == len(diag2):
                        self.solutions.append(perm)

                elapsed_time = time() - start_time
                self.time_var.set('{0:.3f}s'.format(elapsed_time))
        else:
            self.index += 1

        self.queens = self.solutions[self.index % len(self.solutions)]
        self.solution_var.set('{}/{}'.format(self.index % len(self.solutions) + 1, len(self.solutions)))
        self.draw_board()

def main():
    root = Tk()
    NQueens(root)
    root.mainloop()

if __name__ == "__main__": main()