def type_text(text):

    ucount = 0

    lcount = 0

    dcount = 0

    scount = 0

    for i in text:

        if i.isupper():

            # print(f"{i} uppercase")

            ucount += 1

        elif i.islower():

            # print(f"{i} lowercase")
            lcount += 1

        elif i.isdigit():

            dcount += 1

            # print(f"{i} digit")

        else:

            scount += 1

            # print(f"{i} special character")

    print(f"{ucount} uppercase \n{lcount} lowercase \n{dcount} digits \n{scount} special characters")

type_text("ProgramMING@123")