# STDIN
foo = input()

# STDOUT
print("\n{} from STDIN".format(foo))
print("\n#######Start#######")
print("Hello from STDOUT")
print("#######Finish######\n")

#STDERR
raise RuntimeError("Hello from STDERR")
