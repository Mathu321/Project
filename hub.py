import mother as n
while True:
    print('1.Create Database')
    print('2.Admin Functions')
    print('3.User Functions')
    print('4.Exit')
    Ch=int(input('Choice:'))
    if Ch==1:
        n.db_creation()
        print('Database Created')
    elif Ch==2:
        while True:
            print('1.Create Admin Table')
            print('2.Insert Admin Record')
            print("3.Display Admins")
            print('4.Update Admin')
            print('5.Delete Admin')
            print('6.Libray Functions')
            print('7.Book Functions')
            print('8.Exit')
            ch=int(input('Choice:'))
            if ch==1:
                n.cr_admin()
                print('Table Created')
            elif ch==2:
                n.in_admin()
            elif ch==3:
                n.display_admin()
            elif ch==4:
                n.upd_admin()
                print('Updated')
            elif ch==5:
                n.drop_admin()
                print('Deleted')
            elif ch==6:
                while True:
                    print('1.Create Library Table')
                    print('2.Insert Library Record')
                    print('3.Display Library Records')
                    print('4.Update Library Record')
                    print('5.Search Library Record')
                    print('6.Clear Library Record')
                    print('7.Exit')
                    cH=int(input('Choice:'))
                    if cH==1:
                        n.cr_lib()
                        print('Table Created')
                    elif cH==2:
                        n.in_lib()
                    elif cH==3:
                        n.display_lib()
                    elif cH==4:
                        n.upd_lib()
                        print('Updated')
                    elif cH==5:
                        n.search_lib()
                    elif cH==6:
                        n.clear_lib()
                        print('Cleared')
                    elif cH==7:
                        break
            elif ch==7:
                while True:
                    print('1.Create Book Table')
                    print('2.Insert Book')
                    print('3.Display Book Records')
                    print('4.Update Book Record')
                    print('5.Search Book')
                    print('6.Delete Book Record')
                    print('7.Exit')
                    cH=int(input('Choice:'))
                    if cH==1:
                        n.cr_book()
                        print('Table Created')
                    elif cH==2:
                        n.in_book()
                    elif cH==3:
                        n.display_book()
                    elif cH==4:
                        n.upd_book()
                        print('Updated')
                    elif cH==5:
                        n.search_book()
                    elif cH==6:
                        n.drop_book()
                        print('Deleted')
                    elif cH==7:
                        break
            elif ch==8:
                break
    elif Ch==3:
        while True:
            print('1.Create User Table')
            print('2.Insert User Record')
            print("3.Display User")
            print('4.Update User')
            print('5.Delete User')
            print('6.Search User')
            print('7.Exit')
            cH=int(input('Choice:'))
            if cH==1:
               n.tb_user()
               print('Table Created')
            elif cH==2:
               n.in_user()
            elif cH==3:
               n.display_user()
            elif cH==4:
               n.upd_user()
               print('Updated')
            elif cH==5:
               n.drop_user()
               print('Deleted')
            elif cH==6:
                n.search_user()
            elif cH==7:
                break
    elif Ch==4:
        break
















            












            
    
