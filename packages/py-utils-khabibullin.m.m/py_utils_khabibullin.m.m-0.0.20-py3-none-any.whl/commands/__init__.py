import argparse

from commands.list_command import list_commands


def main():
  parser = argparse.ArgumentParser(
    prog="commands",
    description="",
  )

  # parser.add_argument("-l", "--list", action="store_true")
  parser.add_argument("-l", "--labels", action="append")

  args = parser.parse_args()

  if args.labels:
    list_commands(labels=args.labels)
  else:
    list_commands()
