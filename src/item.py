class Item:
  name=''
  description = ''
  
  def __init__(self, name, description):
    self.name=name
    self.description = description

  def on_find(self):
    print(f'>>> found {self.name}\n')

  def on_drop(self):
    print(f'>>> dropped {self.name}\n')