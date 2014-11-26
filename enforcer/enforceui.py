import argparse
from enforcer import enforce
from string import Template
from subprocess import call
from subprocess import check_output
from subprocess import CalledProcessError

parser = argparse.ArgumentParser(description='Manage a farmfs instance.',)
parser.add_argument("--current", nargs = "+", required=True, type=str)
parser.add_argument("--goal", nargs = "+", required=True, type=str)
parser.add_argument("--remove", nargs="+", required=True, type=str)
parser.add_argument("--add", nargs="+", required=True, type=str)

"""Create a function which collects lines of output from shell program specified by command"""
def state_runner_factory(command):
  """Run command and return lines of output. Throw on error."""
  def state_runner():
    try:
      command_output = check_output(command)
    except CalledProcessError as e:
      print "Failed to run command: %s" % command
      exit(1) #TODO MAKE REPEAT SAFE
    else:
      lines = command_output.split("\n")
      d = dict.fromkeys(lines)
      print d
      return d
  return state_runner

"""Create a function which takes a key and runs a shell command"""
def state_changer_factory(command_template):
  """Run command specified by command_template and key. Throws on failure"""
  def changer(key, context):
    replace = {'NAME' : key}
    command = [Template(x).safe_substitute(replace) for x in command_template]
    ret_code = call(command)
    if ret_code != 0:
      raise Exception("Command Failed: %s")
  return changer

def main():
  args = parser.parse_args()
  current_callback = state_runner_factory(args.current)
  goal_callback = state_runner_factory(args.goal)
  remove_callback = state_changer_factory(args.remove)
  add_callback = state_changer_factory(args.add)
  converged = enforce(current_callback, goal_callback, add_callback, remove_callback)
  if converged:
    print "Converged"
  else:
    print "Not converged"

if __name__ == "__main__":
  main()
