print("Name: Banjo victoria tomisin")
print("Matric NO: 19/5692")
print("COLLEGE OF PURE AND APPLIED SCEINCES")
print("COMPUTER SCIENCE DEPARTMENT")
print("STUDENTS' COMPUTER LABORATORY RULES")
print("1) GENERAL RULES")
print("2) RIGHT OF USE")
print("3) USE OF SOFTWARE AND DATA")

digit=int(input("Enter a number: "))

if digit == 1:
    print("1) University computer laboratory including printers may only be used for "
          "official university purpose. \n private or personal work may not  be undertaken without the permission of the HOD"
          )
    print("2) Users should not create disturbance or interference with other users")
    print("3) No eating or drinking in the laboratory")
    print("4) Users shall not litter,cause any messor leave the laboratory in an untidy state")
    print("5) Users shall obey all reasonable instructrion from the the laboratory technologist")

elif digit == 2:
    print("1) Users shall only gain access to the computer laboratoryby providing I.D card"
          " or\n a written authorizationto the laboratory")
    print("2) Users shall produce a proof of identity at the request of the laboratory technologist"
          "or\n any university officials")
    print("3) Users shall not share, distribute or use access idetification or "
          "password\n other than those assigned to them")
    print("4) It is the responsibility of the student to log out after using the computer")
    print("5) Any student who intentionally or negligently fails to log out will be held"
          " responsible\n for whatever purpose the computer is used for after the moment")

elif digit == 3:
    print("1) Users should not attempt to bypass or undermine the system security")
    print("2) The system security must be observed at all times")
    print("3) No software that may attempt alter the network file servers or other equipment be loaded, developed or "
          "executed \n on university laboratory computers")
    print("4) Users shall only access those laboratory computers, "
          "system\n or data which has been specifically authorise to use")
    print("5) Only the materials related to the users courses and duties at the"
          " university\n may be downloaded from the internet")
    print("6) Users shall not send messages using email facilities to an individual or a large number "
          "of \n users that may be considered undesirable or harrasment by some or one of the recicpient" )
    print("7) Nobody should go away with any of the equipment that belong to the university from the laboratory")

else:
    print("INVALID!")


