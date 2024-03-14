import numpy as np
import pygmt
import datetime
import tkinter as tk
import pandas as pd

class gmt:
    def __init__(self, log) -> None:
        self.fig = None
        self.log = log
        self.sybol_dict = {"-":"-",
                           "+":"+",
                           "star":"a",
                           "circle":"c",
                           "diamond":"d",
                           "octagon":"g",
                           "hexagon":"h",
                           "inverted triangle":"i",
                           "pentagon":"n",
                           "point":"p",
                           "square":"s",
                           "triangle":"t",
                           "cross":"x",
                           "dash":"y"}
        start_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.log.insert(tk.END,"start time->" + str(start_time)+"\n")
        self.log.insert(tk.END,"\n")
        self.log.see("end")
    
    def base(self, title, min_lon, max_lon, min_lat, max_lat):
        #basemapを実行するたびにリセットするようにここでpygmtをインスタンス化
        self.fig = pygmt.Figure()
        self.title = title  #データタイトル
        self.projection = "M15c"
        self.region = [min_lon, max_lon, min_lat, max_lat]
        self.fig.basemap(region=self.region, projection=self.projection, frame=True)
        now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.log.insert(tk.END,"end time->" + str(now_time)+"\n")
        self.log.insert(tk.END,"basemap setting->"+"\n")
        self.log.insert(tk.END,"Region"+"\n")
        self.log.insert(tk.END,f"Latitude->{min_lat}-{max_lat}"+"\n")
        self.log.insert(tk.END,f"Longitude->{min_lon}-{max_lon}"+"\n")
        self.log.insert(tk.END,f"map title->{title}"+"\n")
        self.log.insert(tk.END,"\n")
        self.log.see("end")
        
    def plot_image(self, path, label_lat, label_lon, label_data, cmap, plotsize, vmin, vmax, unit, types):
        if self.fig == None:
            #basemapを実行していない場合は実行しない
            now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            self.log.insert(tk.END,"end time->" + str(now_time)+"\n")
            self.log.insert(tk.END,f"Error->please set a basemap"+"\n")
            self.log.insert(tk.END,"\n")
            self.log.see("end")
        else:
            df = pd.read_csv(path)
            symbol = self.sybol_dict[types]
            pygmt.makecpt(cmap=cmap,series = [vmin, vmax], continuous = True)
            #データのプロット
            self.fig.plot(
                x    = df[label_lon],
                y    = df[label_lat],
                fill = df[label_data],
                cmap=True,
                style = f"{symbol}{plotsize}c",
            )
            self.fig.colorbar(frame=[f"y+l{unit}"], scale=1)
            #log
            now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            self.log.insert(tk.END,"end time->" + str(now_time)+"\n")
            self.log.insert(tk.END,"created plot image->"+"\n")
            self.log.insert(tk.END,f"Lat:Lon label->{label_lat}:{label_lon} "+"\n")
            self.log.insert(tk.END,f"data label->{label_data}"+"\n")
            self.log.insert(tk.END,f"cmap->{cmap}"+"\n")
            self.log.insert(tk.END,f"plotsize->{plotsize}"+"\n")
            self.log.insert(tk.END,f"color range->{vmin}-{vmax}"+"\n")
            self.log.insert(tk.END,f"symbol->{types}"+"\n")
            self.log.insert(tk.END,"\n")
            self.log.see("end")
    
    def counter_image(self, path, label_lat, label_lon, label_data, annotation, level, pensize):
        if self.fig == None:
            #basemapを実行していない場合は実行しない
            now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            self.log.insert(tk.END,"end time->" + str(now_time)+"\n")
            self.log.insert(tk.END,f"Error->please set a basemap"+"\n")
            self.log.insert(tk.END,"\n")
            self.log.see("end")
        else:
            df = pd.read_csv(path)
            self.fig.contour(
            pen=f"{pensize}p,black",
            # pass the data as 3 1-D data columns
            x=df[label_lon],
            y=df[label_lat],
            z=df[label_data],
            # set the contours z values intervals to 10
            levels=level,
            # set the contours annotation intervals to 20
            annotation=annotation,
            )
            #log
            now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            self.log.insert(tk.END,"end time->" + str(now_time)+"\n")
            self.log.insert(tk.END,"created counter image->"+"\n")
            self.log.insert(tk.END,f"Lat:Lon label->{label_lat}:{label_lon} "+"\n")
            self.log.insert(tk.END,f"data label->{label_data}"+"\n")
            self.log.insert(tk.END,f"annotation->{annotation}"+"\n")
            self.log.insert(tk.END,f"level->{level}"+"\n")
            self.log.insert(tk.END,f"pensize->{pensize}"+"\n")
            self.log.insert(tk.END,"\n")
            self.log.see("end")

    def line_image(self, path, label_lat, label_lon, label_text, color, plotsize, pensize, fontsize, types, delta_x, delta_y):
        if self.fig == None:
            #basemapを実行していない場合は実行しない
            now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            self.log.insert(tk.END,"end time->" + str(now_time)+"\n")
            self.log.insert(tk.END,f"Error->please set a basemap"+"\n")
            self.log.insert(tk.END,"\n")
            self.log.see("end")
        else:
            df = pd.read_csv(path, encoding='cp932')
            symbol = self.sybol_dict[types]
            self.fig.plot(x=df[label_lon], y=df[label_lat], pen=f"{pensize}p,{color}")
            self.fig.plot(x=df[label_lon], y=df[label_lat], style=f"{symbol}{plotsize}c", fill=color)
            for i in range(len(df[label_text])):
                self.fig.text(text=df[label_text][i], x=df[label_lon][i]+delta_x, y=df[label_lat][i]+delta_y, font=f"{fontsize}p")
            #log
            now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            self.log.insert(tk.END,"end time->" + str(now_time)+"\n")
            self.log.insert(tk.END,"created line image->"+"\n")
            self.log.insert(tk.END,f"Lat:Lon label->{label_lat}:{label_lon} "+"\n")
            self.log.insert(tk.END,f"text label->{label_text}"+"\n")
            self.log.insert(tk.END,f"color->{color}"+"\n")
            self.log.insert(tk.END,f"plotsize->{plotsize}"+"\n")
            self.log.insert(tk.END,f"pensize->{pensize}"+"\n")
            self.log.insert(tk.END,f"fontsize->{fontsize}"+"\n")
            self.log.insert(tk.END,f"symbol->{types}"+"\n")
            self.log.insert(tk.END,f"delta x:y->{delta_x}:{delta_y}"+"\n")
            self.log.insert(tk.END,"\n")
            self.log.see("end")
            
    def show_img(self):
        self.fig.coast(frame = [f'WSen+t{self.title}'], shorelines=True,land="lightgray")
        now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.log.insert(tk.END,"end time->" + str(now_time)+"\n")
        self.log.insert(tk.END,f"Completed mapping."+"\n")
        self.log.insert(tk.END,"\n")
        self.log.see("end")
        self.fig.show()
        