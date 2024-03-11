#main画面

import tkinter as tk
import sys
sys.dont_write_bytecode = True



class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)

        #メインウィンドウの生成
        self.master.geometry("840x700")
        self.master.title("pygmt-mapping")
        self.master.configure(bg="gray88")
        self.master.resizable(width=False, height=False)
    
    #フレームの生成関数
    def create_frame(self):
        
        self.mainFrame = tk.Frame(self.master, height=500, width=700, bg="gray88")
        self.mainFrame.place(x=0, y=0)

def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()


if __name__ == "__main__":
    main()