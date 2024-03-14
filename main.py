#main画面

import tkinter as tk
import sys
sys.dont_write_bytecode = True
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
import os
import tkinter.filedialog
import pandas as pd

import func

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)

        #カラー フォントサイズ
        self.background = "gray88"
        self.fontcolor = "black"
        self.fonts = ("", 20)
        
        #メインウィンドウの生成
        self.master.geometry("840x700")
        self.master.title("pygmt-mapping")
        self.master.configure(bg="gray88")
        self.master.resizable(width=False, height=False)
        
        #ウィジェットの配置位置
        #1段目配置位置
        self.x1 = 120
        self.y1 = 51
        #2段目配置位置
        self.x2 = [240, 430, 610]
        self.y2 = 110

        #3段目
        self.x3 = [150, 330, 510, 690]
        self.y3 = 170
        #4段目
        self.y4 = 230
        
        #各ウィジェットの作成
        self.create_frame()
        self.create_label()
        self.create_button()
        self.create_entry()
        self.create_textbox()
        self.create_combobox()
        #pygmt funcインスタンス化
        self.gmt = func.gmt(self.textbox)
        
    #フレームの生成関数
    def create_frame(self):
        #メイン設定（basemap）
        self.mainFrame = tk.Frame(self.master, height=350, width=840, bg=self.background, relief=tk.GROOVE, bd=3)
        #counterフレーム
        self.counterFrame = tk.Frame(self.master, height=300, width=840, bg=self.background, relief=tk.GROOVE, bd=3)
        #map line 用フレーム
        self.lineFrame = tk.Frame(self.master, height=300, width=840, bg=self.background, relief=tk.GROOVE, bd=3)
        #マップのプロットフレーム
        self.plotFrame = tk.Frame(self.master, height=300, width=840, bg=self.background, relief=tk.GROOVE, bd=3)
        #配置
        self.mainFrame.place(   x=0, y=0)
        self.counterFrame.place(x=0, y=350)
        self.lineFrame.place(   x=0, y=350)
        self.plotFrame.place(   x=0, y=350)

    def create_label(self):
        #mainFrame
        tk.Label(self.mainFrame, text=u'basemap'   , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10, y=10)
        tk.Label(self.mainFrame, text=u'latitude'  , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=20, y=50)
        tk.Label(self.mainFrame, text=u'―'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=220, y=47)
        tk.Label(self.mainFrame, text=u'longitude' , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10, y=100)
        tk.Label(self.mainFrame, text=u'―'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=220, y=97)
        tk.Label(self.mainFrame, text=u'title'     , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=30, y=250)


        #counterFrame
        tk.Label(self.counterFrame, text=u'counter'      , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10 , y=10)
        tk.Label(self.counterFrame, text=u'data path'    , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10 , y=47 )
        tk.Label(self.counterFrame, text=u'Label Name →' , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10 , y=self.y2)
        tk.Label(self.counterFrame, text=u'lat'          , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=200, y=self.y2)
        tk.Label(self.counterFrame, text=u'long'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=370, y=self.y2)
        tk.Label(self.counterFrame, text=u'data'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=550, y=self.y2)
        tk.Label(self.counterFrame, text=u'annotation'   , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=20 , y=self.y3)
        tk.Label(self.counterFrame, text=u'level'        , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=250, y=self.y3)
        tk.Label(self.counterFrame, text=u'pensize'      , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=420, y=self.y3)
        
        #lineFrame
        tk.Label(self.lineFrame, text=u'line'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10, y=10)
        tk.Label(self.lineFrame, text=u'data path'    , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10, y=47)
        tk.Label(self.lineFrame, text=u'Label Name →' , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10 , y=self.y2)
        tk.Label(self.lineFrame, text=u'lat'          , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=200, y=self.y2)
        tk.Label(self.lineFrame, text=u'lon'          , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=380, y=self.y2)
        tk.Label(self.lineFrame, text=u'text'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=550, y=self.y2)
        tk.Label(self.lineFrame, text=u'color'        , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=50 , y=self.y3)
        tk.Label(self.lineFrame, text=u'plotsize'     , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=230, y=self.y3)
        tk.Label(self.lineFrame, text=u'pensize'      , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=420, y=self.y3)
        tk.Label(self.lineFrame, text=u'fontsize'     , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=590, y=self.y3)
        tk.Label(self.lineFrame, text=u'types'        , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=280, y=self.y4)
        tk.Label(self.lineFrame, text=u'lavel d'      , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=30 , y=self.y4)
        tk.Label(self.lineFrame, text=u':'            , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=185, y=self.y4-2)
        #plotFrame
        tk.Label(self.plotFrame, text=u'plot'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10 , y=10)
        tk.Label(self.plotFrame, text=u'data path'    , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10 , y=47 )
        tk.Label(self.plotFrame, text=u'Label Name →' , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=10 , y=self.y2)
        tk.Label(self.plotFrame, text=u'lat'          , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=200, y=self.y2)
        tk.Label(self.plotFrame, text=u'long'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=370, y=self.y2)
        tk.Label(self.plotFrame, text=u'data'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=550, y=self.y2)
        tk.Label(self.plotFrame, text=u'cmap'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=70 , y=self.y3)
        tk.Label(self.plotFrame, text=u'plotsize'     , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=230, y=self.y3)
        tk.Label(self.plotFrame, text=u'vmin'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=430, y=self.y3)
        tk.Label(self.plotFrame, text=u'vmax'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=610, y=self.y3)
        tk.Label(self.plotFrame, text=u'unit'         , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=120, y=self.y4)
        tk.Label(self.plotFrame, text=u'types'        , bg=self.background, fg=self.fontcolor, font=self.fonts).place(x=280, y=self.y4)
        #

    #entry作成
    def create_entry(self):

        
        #mainFrame
        self.entry_min_lat = tk.Entry(self.mainFrame, width=7 , fg=self.fontcolor, font=self.fonts,justify=tk.RIGHT); self.entry_min_lat.place(x=120,y=50)
        self.entry_max_lat = tk.Entry(self.mainFrame, width=7 , fg=self.fontcolor, font=self.fonts,justify=tk.RIGHT); self.entry_max_lat.place(x=250,y=50)
        self.entry_min_lon = tk.Entry(self.mainFrame, width=7 , fg=self.fontcolor, font=self.fonts,justify=tk.RIGHT); self.entry_min_lon.place(x=120,y=100)
        self.entry_max_lon = tk.Entry(self.mainFrame, width=7 , fg=self.fontcolor, font=self.fonts,justify=tk.RIGHT); self.entry_max_lon.place(x=250,y=100)
        self.entry_title   = tk.Entry(self.mainFrame, width=20, fg=self.fontcolor, font=self.fonts)                 ; self.entry_title.place(x=85,y=250)

        #map line 
        self.entry_line_datapath   = tk.Entry(self.lineFrame, width=60, fg=self.fontcolor, font=("", 14)  ); self.entry_line_datapath.place(  x=self.x1   ,y=self.y1)
        self.entry_line_label_lat  = tk.Entry(self.lineFrame, width=8 , fg=self.fontcolor, font=self.fonts); self.entry_line_label_lat.place( x=self.x2[0],y=self.y2)
        self.entry_line_label_lon  = tk.Entry(self.lineFrame, width=8 , fg=self.fontcolor, font=self.fonts); self.entry_line_label_lon.place( x=self.x2[1],y=self.y2)
        self.entry_line_label_text = tk.Entry(self.lineFrame, width=8 , fg=self.fontcolor, font=self.fonts); self.entry_line_label_text.place(x=self.x2[2],y=self.y2)
        self.entry_line_color      = tk.Entry(self.lineFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_line_color.place(     x=self.x3[0],y=self.y3)
        self.entry_line_size       = tk.Entry(self.lineFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_line_size.place(      x=self.x3[1],y=self.y3)
        self.entry_line_pen        = tk.Entry(self.lineFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_line_pen.place(       x=self.x3[2],y=self.y3)
        self.entry_line_fontsize   = tk.Entry(self.lineFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_line_fontsize.place(  x=self.x3[3],y=self.y3)
        self.entry_line_dlat       = tk.Entry(self.lineFrame, width=4 , fg=self.fontcolor, font=self.fonts); self.entry_line_dlat.place(      x=120        ,y=self.y4)
        self.entry_line_dlon       = tk.Entry(self.lineFrame, width=4 , fg=self.fontcolor, font=self.fonts); self.entry_line_dlon.place(      x=200       ,y=self.y4)
        #counter
        self.entry_counter_datapath   = tk.Entry(self.counterFrame, width=60, fg=self.fontcolor, font=("", 14)  ); self.entry_counter_datapath.place(  x=self.x1   ,y=self.y1)
        self.entry_counter_label_lat  = tk.Entry(self.counterFrame, width=8 , fg=self.fontcolor, font=self.fonts); self.entry_counter_label_lat.place( x=self.x2[0],y=self.y2)
        self.entry_counter_label_lon  = tk.Entry(self.counterFrame, width=8 , fg=self.fontcolor, font=self.fonts); self.entry_counter_label_lon.place( x=self.x2[1],y=self.y2)
        self.entry_counter_label_data = tk.Entry(self.counterFrame, width=8 , fg=self.fontcolor, font=self.fonts); self.entry_counter_label_data.place(x=self.x2[2],y=self.y2)
        self.entry_counter_annotation = tk.Entry(self.counterFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_counter_annotation.place(x=self.x3[0],y=self.y3)
        self.entry_counter_level      = tk.Entry(self.counterFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_counter_level.place(     x=self.x3[1],y=self.y3)
        self.entry_counter_pen        = tk.Entry(self.counterFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_counter_pen.place(       x=self.x3[2],y=self.y3)
        
        #plot
        self.entry_plot_datapath   = tk.Entry(self.plotFrame, width=60, fg=self.fontcolor, font=("", 14)  ); self.entry_plot_datapath.place(  x=self.x1   ,y=self.y1)
        self.entry_plot_label_lat  = tk.Entry(self.plotFrame, width=8 , fg=self.fontcolor, font=self.fonts); self.entry_plot_label_lat.place( x=self.x2[0],y=self.y2)
        self.entry_plot_label_lon  = tk.Entry(self.plotFrame, width=8 , fg=self.fontcolor, font=self.fonts); self.entry_plot_label_lon.place( x=self.x2[1],y=self.y2)
        self.entry_plot_label_data = tk.Entry(self.plotFrame, width=8 , fg=self.fontcolor, font=self.fonts); self.entry_plot_label_data.place(x=self.x2[2],y=self.y2)
        self.entry_plot_cmap       = tk.Entry(self.plotFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_plot_cmap.place(      x=self.x3[0],y=self.y3)
        self.entry_plot_size       = tk.Entry(self.plotFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_plot_size.place(      x=self.x3[1],y=self.y3)
        self.entry_line_vmin       = tk.Entry(self.plotFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_line_vmin.place(      x=self.x3[2],y=self.y3)
        self.entry_line_vmax       = tk.Entry(self.plotFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_line_vmax.place(      x=self.x3[3],y=self.y3)
        self.entry_line_unit       = tk.Entry(self.plotFrame, width=5 , fg=self.fontcolor, font=self.fonts); self.entry_line_unit.place(      x=180  ,y=self.y4)

        #初期値
        self.entry_min_lat.insert(0, -80)
        self.entry_max_lat.insert(0, 80)
        self.entry_min_lon.insert(0, 0)
        self.entry_max_lon.insert(0, 360)
        self.entry_line_label_lat.insert(0, "lat")
        self.entry_line_label_lon.insert(0, "lon")
        self.entry_line_label_text.insert(0, "data")
        self.entry_line_color.insert(0, "red")
        self.entry_line_size.insert(0, 0.4)
        self.entry_line_pen.insert(0, 0.6)
        self.entry_line_fontsize.insert(0, 10)
        self.entry_line_dlat.insert(0, 0.5)
        self.entry_line_dlon.insert(0, 0.5)
        self.entry_counter_label_lat.insert(0, "lat")
        self.entry_counter_label_lon.insert(0, "lon")
        self.entry_counter_label_data.insert(0, "data")
        self.entry_counter_annotation.insert(0, 5)
        self.entry_counter_level.insert(0, 1)
        self.entry_counter_pen.insert(0, 0.3)
        self.entry_plot_label_lat.insert(0, "lat")
        self.entry_plot_label_lon.insert(0, "lon")
        self.entry_plot_label_data.insert(0, "data")
        self.entry_plot_cmap.insert(0, "jet")
        self.entry_plot_size.insert(0, 0.3)
        self.entry_line_vmin.insert(0, -5)
        self.entry_line_vmax.insert(0, 5)

    #テキストボックス作成 ログ出力用
    def create_textbox(self):
        self.textbox = ScrolledText(self.mainFrame, font=("",14), height=17, width=40, fg=self.fontcolor)
        self.textbox.place(x=405, y=7)

    #ボタン作成
    def create_button(self):
        #basemap
        Button = tk.Button(self.master ,text=u'set' , width=7, fg=self.fontcolor, font=self.fonts,
                        command=lambda:self.gmt.base(title   = str(self.entry_title.get()), 
                                                     min_lon = float(self.entry_min_lon.get()),
                                                     max_lon = float(self.entry_max_lon.get()),
                                                     min_lat = float(self.entry_min_lat.get()),
                                                     max_lat = float(self.entry_max_lat.get())
                                                     )
                        )
        Button.place(x=200, y=300, height=40)
        #画面切り替え
        #plot
        Button = tk.Button(self.master ,text=u'plot' , width=7, fg=self.fontcolor, font=self.fonts,
                        command=lambda:self.change_frame(self.plotFrame))
        Button.place(x=40,y=655, height=40)
        #counter
        Button = tk.Button(self.master ,text=u'counter' , width=7, fg=self.fontcolor, font=self.fonts,
                        command=lambda:self.change_frame(self.counterFrame))
        Button.place(x=150,y=655, height=40)
        #line
        Button = tk.Button(self.master ,text=u'line' , width=7, fg=self.fontcolor, font=self.fonts,
                        command=lambda:self.change_frame(self.lineFrame))
        Button.place(x=260,y=655, height=40)
        #画像出力
        Button = tk.Button(self.master ,text=u'show' , width=8, bg=self.background, fg=self.fontcolor, font=self.fonts,
                        command=lambda:self.gmt.show_img())
        Button.place(x=655,y=655, height=40)
        
        #フレーム別ボタン
        #map line 用フレーム
        Button = tk.Button(self.lineFrame ,text=u'...' , width=4, command=lambda:self.insert_entry_path(self.entry_line_datapath))
        Button.place(x=730,y=50)
        Button = tk.Button(self.lineFrame ,text=u'image' , width=7, bg=self.background, fg=self.fontcolor, font=self.fonts,
                        command=lambda:self.gmt.line_image(
                            path       = self.entry_line_datapath.get()  , 
                            label_lat  = self.entry_line_label_lat.get() ,
                            label_lon  = self.entry_line_label_lon.get() ,
                            label_text = self.entry_line_label_text.get(),
                            color      = self.entry_line_color.get()     ,
                            plotsize   = str(self.entry_line_size.get())      ,
                            pensize    = str(self.entry_line_pen.get())       ,
                            fontsize   = str(self.entry_line_fontsize.get())  ,
                            types      = self.combobox_line_type.get(),
                            delta_x    = float(self.entry_line_dlat.get())      ,
                            delta_y    = float(self.entry_line_dlon.get()),
                            )
                        )
        Button.place(x=655,y=230, height=40)

        #counterフレーム
        Button = tk.Button(self.counterFrame ,text=u'...' , width=4, command=lambda:self.insert_entry_path(self.entry_counter_datapath))
        Button.place(x=730,y=50)
        Button = tk.Button(self.counterFrame ,text=u'image' , width=7, bg=self.background, fg=self.fontcolor, font=self.fonts,
                        command=lambda:self.gmt.counter_image(
                                path       = self.entry_counter_datapath.get()  ,
                                label_lat  = self.entry_counter_label_lat.get() ,
                                label_lon  = self.entry_counter_label_lon.get() ,
                                label_data = self.entry_counter_label_data.get(),
                                annotation = float(self.entry_counter_annotation.get()),
                                level      = float(self.entry_counter_level.get())     ,
                                pensize    = str(self.entry_counter_pen.get())
                                )
                            )
        Button.place(x=655,y=230, height=40)

        #マップのプロットフレーム
        Button = tk.Button(self.plotFrame ,text=u'...' , width=4, command=lambda:self.insert_entry_path(self.entry_plot_datapath))
        Button.place(x=730,y=50)
        #プロット画像
        Button = tk.Button(self.plotFrame ,text=u'image' , width=7, bg=self.background, fg=self.fontcolor, font=self.fonts,
                        command=lambda:self.gmt.plot_image(
                            path = self.entry_plot_datapath.get(),
                            label_lat=self.entry_plot_label_lat.get(),
                            label_lon=self.entry_plot_label_lon.get(),
                            label_data=self.entry_plot_label_data.get(),
                            cmap=self.entry_plot_cmap.get(),
                            plotsize=str(self.entry_plot_size.get()),
                            vmin=float(self.entry_line_vmin.get()),
                            vmax=float(self.entry_line_vmax.get()),
                            unit=self.entry_line_unit.get(),
                            types=self.combobox_plot_type.get(),
                            )
                        )
        Button.place(x=655,y=230, height=40)

    #プルダウンリスト作成
    def create_combobox(self):
        
        #plot_types = ("-", "+", "a", "c", "d", "g", "h", "i", "n", "p", "s", "t", "x", "y")
        symbols = ("-", "+", "star", "circle", "diamond", "octagon", "hexagon", 
                   "inverted triangle", "pentagon","point", "square", "triangle", "cross", "dash")
        
        self.combobox_plot_type = ttk.Combobox(self.plotFrame, width=18, state="readonly", values=symbols, font=self.fonts); self.combobox_plot_type.place(x=350,y=230)
        self.combobox_line_type = ttk.Combobox(self.lineFrame, width=18, state="readonly", values=symbols, font=self.fonts); self.combobox_line_type.place(x=350,y=230)

    #画面切り替え関数
    def change_frame(self,frame):
        frame.tkraise()

    #パスの入力
    def insert_entry_path(self, entry):
        if len(entry.get()) > 0:
            entry.delete(0, tk.END)
        typ = [('csv file','*.csv')]
        dir = os.getcwd()
        data_path = tkinter.filedialog.askopenfilename(filetypes = typ, initialdir = dir)
        if len(data_path) > 0:
            entry.insert(tk.END,data_path)
            df = pd.read_csv(data_path, encoding='cp932', index_col=0)
            header = " ".join(list(df.columns))
            self.textbox.insert(tk.END,f"header lists->"+"\n")
            self.textbox.insert(tk.END,header+"\n")
            self.textbox.insert(tk.END,"\n")
            self.textbox.see("end")
            df = None

#メインの実行処理
def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()


#デバッグ
if __name__ == "__main__":
    main()