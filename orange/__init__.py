from orange import config 

def start():
  if not config.get_installed():
      print("installing ...")
      config.set_installed(True)
  print(config.get_installed())
