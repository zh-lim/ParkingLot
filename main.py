import sys

def start_file_input():
  return

def start_shell():
  action = ""
  while action != "exit":
    action = input()
    inputs = action.split()
    print(len(inputs))
  return

def main():
  arglen = len(sys.argv)
  if arglen == 2:
    start_file_input()
  elif arglen == 1:
    start_shell()
  else:
    print("Invalid command!")

main()