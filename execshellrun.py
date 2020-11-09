import subprocess

proc = subprocess.run(["ls", "-l"], check = True)
print(proc,)
print("")
#proc.args
#proc.returncode

#Alternatively
proc = subprocess.run(
    ["ls", "-l"],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
)

print(proc)
print("")

#print(proc.stdout)
print(proc.stdout.decode())
print("")

#print(proc.stderr)
print(proc.stderr.decode())
print("")