#finding a solution of A,B & C (between 1 to 20)
for A in range(1, 21):
    for B in range(1, 21):#using nested loop to iterate through the values of A and B and C
        for C in range(1, 21):
          equ1=(A + B + C == 25)
          equ2=(A * B - C == 64)
          equ3=(A > B >= C)
          if equ1 and equ2 and equ3:#verifying the equations if all the equations are true then print the values of A,B & C
            print("A:", A)
            print("B:", B)
            print("C:", C)
print("These are the values of A, B and C that satisfy the equations.")