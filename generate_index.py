from glob import glob
import os
from pathlib import Path
root = "output_images"
tem_file= Path("template.html")
index_file=Path("index.html")
row_data_symbol = "<<---ROW-DATA-->>"
row_tem = """
<div class="row image-row">
         <div class="col-4">
            <img src="{base}"></img>
         </div>
         <div class="col-4">
            <img src="{gan}"></img>
         </div>
         <div class="col-4">
            <img src="{gan_LI}"></img>
         </div>
     
      </div>
"""
dirs = glob(os.path.join(root,"*"), recursive=True)
html_string = ""
for d in dirs:
   base = os.path.join(d,"patch","e2ecoded.png")
   gan = os.path.join(d,"patch","gan20-epoch231.png")
   gan_LI = os.path.join(d,"patch","gan_lowLR_p128_44-epoch221.png")
   html_string+=row_tem.format(base=base, gan=gan,gan_LI=gan_LI)

index_file.write_text(tem_file.read_text().replace(row_data_symbol, html_string))