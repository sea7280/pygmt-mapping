import numpy as np
import pygmt
import datetime
import pandas as pd

class gmt:
    def __init__(self, log) -> None:
        self.fig = pygmt.Figure()
        self.log = log
    
    def base(self, title, min_lon, max_lon, min_lat, max_lat):
        self.title = title  #データタイトル
        self.projection = "M15c"
        self.region = [min_lon, max_lon, min_lat, max_lat]
        self.fig.basemap(region=self.region, projection=self.projection, frame=True)
        
        
    def plot_image(self, path, label_lat, label_lon, label_data, cmap, plotsize, vmin, vmax, unit, types):
        df = pd.read_csv(path)
        pygmt.makecpt(cmap=cmap,series = [vmin, vmax, 0.1])
        #データのプロット
        self.fig.plot(
            x    = df[label_lon],
            y    = df[label_lat],
            fill = df[label_data],
            cmap=True,
            style = f"{types}{plotsize}c",
        )
        self.fig.coast(frame = [f'WSen+t{self.title}'], shorelines=True,land="lightgray")
        self.fig.colorbar(frame=["x+l", f"y+l{unit}"], scale=1)
    
    #def counter_image(self, path, label_lat, label_lon, label_data, annotation, level, pensize, fontsize):
        
        
        
    
    #def line_image():