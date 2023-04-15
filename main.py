import standard_message_sender
import various_message_sender


def menu():
    print("""Welcome to the JobSeeker!
          Actually this project was created to send CV here and there,
          but you may use it for daily business mailing as well.
          
          Before running the program please make sure all the files for the automated mailing are updated!
          
          If you're done with the double-check, please, choose from the options below: 
          - 'a' - to send a standard message to various receivers
          - 'b' - to send different messages to each receiver
          - 'q' - to quit the program.
          """)

    option = str(input("Please, type in the number here:  ")).lower()
    match option:
        case 'a':
            standard_message_sender.main()
        case 'b':
            various_message_sender.main()
        case 'q':
            print("Well, see ya later! Bye!")
            exit()
        case _:
            print("Please, use the built-in options!")
            menu()


if __name__ == '__main__':
    menu()

















4
5
6
7
8
9
10
11
12
13
14
15
16
12345679101112131415
1234567891011121314151617
1234567891011