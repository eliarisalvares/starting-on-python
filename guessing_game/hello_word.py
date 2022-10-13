# Python uses dynamic typing, there is no need to declare the variable type.
# Unlike C, which allows explicit type casting of the variables, Python
# does not support explicit type casting and the variable can't be static, it
# needs to be assigned a value to exist. Also, Python uses snake case naming.
# such as: "my_variable_name" (all letters are lowercased).

hello = "hello"
world = "world"		# Create two string variables

print(hello, world, sep="_", end="!")	# Print the strings using "_"
# as the separator and "!" as the finish character
type(hello)			# Returns its type as <class 'str'>
type(world)			# Returns its type as  <class 'str'>
