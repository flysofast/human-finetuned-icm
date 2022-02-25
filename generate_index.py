from glob import glob
import os
root = "new_downloaded_images"

fps = glob(os.path.join(root,"**", "*.png"), recursive=True)
print(fps)