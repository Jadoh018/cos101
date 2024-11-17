def a():
    velocity=float(input("input your velocity:"))
    time=float(input("input your time:"))
    #displacement= velocity*time
    output=(velocity*time)
    print(output)


def b():
    displacement=int(input("what is the displacement:"))
    time=int(input("what is time:"))
    #velocity=displacement/time
    output=(displacement/time)
    print(output)

def c():
        mass=int(input("what is the mass:"))
        acceleration=int(input("what is acceleration:"))
        #force=mass*acceleration
        output=(mass*acceleration)
        print(output)

def d():
        force=int(input("what is force:"))
        distance=int(input("what is distance:"))
        #energy=force*distance
        output=(force*distance)
        print(output)

def e():
    mass=int(input("what is mass:"))
    velocity=int(input("what is velocity:"))
    #momentum=mass*velocity
    output=(mass*velocity)
    print(output)

def main():
    user_choice = input("choose from a -e: ")
    if user_choice == "a":
         a()
    elif user_choice == "b":
        b()
    elif user_choice == "c":
        c()
    elif user_choice == "d":
        d()
    elif user_choice == "e":
        e()
if __name__ == '__main__':
        main()






