# One Conditional Statement: (One question in mid-term from this)

# if  (Required) --> One instance
# elif (Optional) --> one or more instance
# else (Optional) --> One instance

# if criteria
# 1. greater (>)
# 2. greater than (>=)
# 3. less (<)
# 4. less than (<=)
# 5. equal (=)

a = -3

print('Criteria (if):', a >= 1)
print('Criteria (elif 1):', a < -5)
print('Criteria (elif 2)', a < -7)

# -----------------------------FIRST IF----------------------------------------------------------
if a >= 1:   # If true than go to next and if fail than skip further cmd
    print("A is greater than or equal to 1")
elif a < -5:  # This means A can be -6,-7,-8,...
    print("A is less than -5")
elif a < -7:  # This means A can be -8,-9,10,... But this is overlapping 2nd condition so this will not going to print as when at 2nd option it happen it stop there & and if at 1st if the condition met it will not check for other two options
    print("A is less than -7")
else: # always comes at last, it means none of condition met do this.
    print("None of the condition have return true")

# -------------------------------ANOTHER IF-------------------------------------------------------
if a < -7:  # this will print if condition is true as it's first if condition
    print("A is less than -7")
else:
    print("None of the above")

# ---------------------------------== vs =---------------------------------------------------------

# object 1 == objects 2 ---> means the two object have the same value AND the same type (same class)
# -7.0 == -7 (Exception)
# "-7.0" not equal to -7

a = -7.0 # assign -7 value to A

if a == -7: # if a is -7 or not
    print("A is equal to -7 (New if)")

