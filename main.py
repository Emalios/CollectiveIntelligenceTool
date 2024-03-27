import tkinter as tk

class GridEditor:
    def __init__(self, master, rows, cols):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cell_size = 20
        self.cells = [[None for _ in range(cols)] for _ in range(rows)]
        self.create_grid()

    def create_grid(self):
        self.canvas = tk.Canvas(self.master, width=self.cols*self.cell_size, height=self.rows*self.cell_size, bg='white')
        self.canvas.pack()

        for row in range(self.rows):
            for col in range(self.cols):
                x0, y0 = col*self.cell_size, row*self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                rect = self.canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='', tags='grid_cell')
                self.cells[row][col] = rect

        #Up wall
        for i in range(1, 14):
            self.canvas.itemconfig(self.cells[6][i], fill='black')
        for i in range(17, 21):
            self.canvas.itemconfig(self.cells[6][i], fill='black')
        for i in range(24, 26):
            self.canvas.itemconfig(self.cells[6][i], fill='black')
        #Wall line
        for i in range(6, 10):
            self.canvas.itemconfig(self.cells[i][11], fill='black')
        for i in range(13, 20):
            self.canvas.itemconfig(self.cells[i][11], fill='black')
        for i in range(6, 20):
            self.canvas.itemconfig(self.cells[i][18], fill='black')
        #Down wall
        for i in range(1, 15):
            self.canvas.itemconfig(self.cells[20][i], fill='black')
        for i in range(17, 27):
            self.canvas.itemconfig(self.cells[20][i], fill='black')

        # Dessine des murs autour de la grille
        for i in range(self.rows):
            self.canvas.itemconfig(self.cells[i][0], fill='black')
            self.canvas.itemconfig(self.cells[i][-1], fill='black')
        for j in range(self.cols):
            self.canvas.itemconfig(self.cells[0][j], fill='black')
            self.canvas.itemconfig(self.cells[-1][j], fill='black')

def main():
    root = tk.Tk()
    root.title("Grid Editor")
    rows, cols = 30, 27  # Vous pouvez ajuster le nombre de lignes et de colonnes ici
    editor = GridEditor(root, rows, cols)
    root.mainloop()

if __name__ == "__main__":
    main()