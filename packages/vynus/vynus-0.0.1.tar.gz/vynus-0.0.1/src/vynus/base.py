import nbformat

def extract(nb_path):
  nb = nbformat.read(nb_path, as_version=4)
  cells = nb['cells']
  return cells[0]['source']