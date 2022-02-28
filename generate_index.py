from glob import glob
import os
from pathlib import Path

from pygments import highlight

root = "output_images"
tem_file= Path("template.html")
index_file=Path("index.html")
row_data_symbol = "<<---ROW-DATA-->>"
row_data_header_symbol = "<<---ROW-HEADER-->>"
codec_desc_symbol = "<<---CODEC-DESC-->>"
codecs ={
   "base": {
      "title": "Base model",
      "desc": "The end-to-end trained model without finetuning"
   },
   "gaussian": {
      "title": "Gaussian post-processing filter",
      "desc": "The decoded image is processed using a Gaussian filter <i>(requires extra component)</i>"
   },
   "bilateral": {
      "title": "Bilateral post-processing filter",
      "desc": "The decoded image is processed using a Bilateral filter <i>(requires extra component)</i>"
   },
   "gan": {
      "title": "Finetuned model",
      "desc": "The main proposal of this paper, which is the base codec finetuned using a GANs-based approach"
   },
   "gan_LI": {
      "title": "Limitedly finetuned model",
      "desc": "Using the same approach as the finetuned codec, but with an attenuated dynamic from the adversarial component"
   },
}
desc_tem = """
   <li><b>{title}</b>: {desc}</li>
"""

row_header_tem = """
   <div class="col center {highlight}">
         <span>{title}</span>
   </div>
"""

row_tem = """
   <div class="col {highlight}">
      <img src="{img_path}" alt="{alt_text}"></img>
   </div>
"""
dirs = glob(os.path.join(root,"*"), recursive=True)
row_img_string = ""
row_header_string = ""
desc_string = ""
col_span = 12//len(codecs)
for k,v in codecs.items():
   row_header_string+=row_header_tem.format(col_span=col_span, title=v["title"], highlight="highlighted" if "gan" in k else "")
   desc_string+=desc_tem.format(title=v["title"], desc=v["desc"])
for d in dirs:
   row_img=""
   paths = {
      "base": os.path.join(d,"patch","e2ecoded.png"),
      "gan" : os.path.join(d,"patch","gan20-epoch231.png"),
      "gan_LI" : os.path.join(d,"patch","gan_lowLR_p128_44-epoch221.png"),
      "gaussian" : os.path.join(d,"patch","gaussian.png"),
      "bilateral" : os.path.join(d,"patch","bilteral.png")
   }
   for k,v in codecs.items():
      row_img+=row_tem.format(col_span=col_span, img_path=paths[k], alt_text=k, highlight="highlighted" if "gan" in k else "")
   
   row_img_string += f"""
      <div class="row image-row">
         {row_img}
      </div>
   """

index_file.write_text(tem_file.read_text().replace(row_data_header_symbol, row_header_string).replace(codec_desc_symbol, desc_string).replace(row_data_symbol, row_img_string))