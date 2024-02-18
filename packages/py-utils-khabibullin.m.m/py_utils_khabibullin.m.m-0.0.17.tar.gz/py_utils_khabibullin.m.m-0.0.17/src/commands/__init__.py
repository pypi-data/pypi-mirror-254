import argparse

from commands.list_command import list_commands


def main():
  parser = argparse.ArgumentParser(
    prog="commands",
    description="",
  )

  parser.add_argument("-l", "--list", action="store_true")

  args = parser.parse_args()

  if args.list:
    list_commands()

  print(f"No command was found for the arguments: {args}")
