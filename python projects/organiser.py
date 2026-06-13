from pathlib import Path
find_dir = Path("/home/jamal012004/projects/python/python projects/dummy files")
extension_map = {
'.txt': 'Documents',
'.pdf': 'Documents',
'.jpg': 'Images',
'.png': 'Images'
}

for file in find_dir.iterdir():
 if file.is_file():
  ext = file.suffix
   if ext in extension_map:
     file_name = extension_map[ext]
    
  
