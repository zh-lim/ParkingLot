import sys
from app.carparkDisplay import CarparkDisplay

def start_file_mode(interface,file):
  if not file.lower().endswith(".txt"):
    return
  filepath = file
  with open(filepath) as fp:
    for line in fp:
      inputs = line.split()
      res = interface.parse_action(inputs)
      if res is not None:
        print(res)
  return


def start_shell_mode(interface):
  cmd = ""
  while cmd != "exit":
    print("$ ", end="")
    cmd = input()
    inputs = cmd.split()
    res = interface.parse_action(inputs)
    if res is not None:
        print(res)
  return

def main():
  interface = CarparkDisplay()
  arglen = len(sys.argv)
  if arglen == 2:
    start_file_mode(interface,sys.argv[1])
  elif arglen == 1:
    start_shell_mode(interface)
  else:
    print("Invalid command!")

if __name__ == '__main__':
  main()