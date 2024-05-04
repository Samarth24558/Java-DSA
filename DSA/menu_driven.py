#python programme to create a menu driven for linked list and there types

import linked_list
import doubly_ll
import circular_linked_list
import circular_double_linked_list


ll=linked_list.LL()
dll=doubly_ll.DLL()
cll=circular_linked_list.CLL()
cdll=circular_double_linked_list.CDLL()

def main_menu_bar():
    #============main menu bar========================
    print("Main:")
    main_menu=["Create linked list","Insert node","Update node value","Delete node","Display linked list","Exit"]

    print("============================")
    length=len(f"{0+4}. {main_menu[4]}")
    for i in range(6):
        print("|",end="  ")
        print(f"{i+1}. {main_menu[i]}",end="")
        if(length==len(f"{i+1}. {main_menu[i]}")):
            print("  |")
        elif(length>len(f"{i+1}. {main_menu[i]}")):
            space=length-len(f"{i+1}. {main_menu[i]}")
            for j in range(space):
                print(" ",end="")
            print("  |")
    print("============================")

    #=================chosing type of linked list====================
    def createll():
        print("Create Linked List:")
        menu=["Singular","Double","Circular","Circular double","Exit"]

        print("========================")
        length=len(f"{0+3}. {menu[3]}")
        for i in range(5):
            print("|",end="  ")
            print(f"{i+1}. {menu[i]}",end="")
            if(length==len(f"{i+1}. {menu[i]}")):
                print("  |")
            elif(length>len(f"{i+1}. {menu[i]}")):
                space=length-len(f"{i+1}. {menu[i]}")
                for j in range(space):
                    print(" ",end="")
                print("  |")
        print("========================")
        
        global llch
        try:
            while True:
                ch1=int(input("Enter the number as per menu above (Create Linked List):"))
                if(ch1>5 or ch1<1):
                    ch1=int(input("Please enter valid menu number as above (Create Linked List):"))
                elif(ch1==5):
                    main_menu_bar()
                    break
                elif(ch1>=1 and ch1<5):
                    print(f"Selected {menu[ch1-1]} Linked List..!")
                    llch=ch1
        except ValueError:
            print("Please try again")    
            createll()  
    #============== inserting node programme =============
    def insert_node():
        print("Insert Node:")
        menu=["Insert at end","Insert at biginning","Insert at position","Exit"]

        print("==========================")
        length=len(f"{0+1}. {menu[1]}")
        for i in range(4):
            print("|",end="  ")
            print(f"{i+1}. {menu[i]}",end="")
            if(length==len(f"{i+1}. {menu[i]}")):
                print("  |")
            elif(length>len(f"{i+1}. {menu[i]}")):
                space=length-len(f"{i+1}. {menu[i]}")
                for j in range(space):
                    print(" ",end="")
                print("  |")
        print("=========================")
        
        try: 
            while True:
                choice=int(input("Enter the number as menu above to insert node (Insert Node): "))
                if(choice<1 or choice>4):
                    choice=int(input("Enter the valid number as above menu (Insert Node):"))
                match choice:
                    case 1:
                        match llch:
                            case 1:
                                nodes=int(input("How much node/s do you want (Insert Node): "))
                                i=nodes
                                while nodes!=0:
                                    value=str(input("Enter the node value (Insert Node): "))
                                    ll.insert_at_end(value)
                                    nodes-=1
                                print(f"{i} Node/s inserted in singular linked list at end successfully..!")
                            case 2:
                                nodes=int(input("How much node/s do you want (Insert Node): "))
                                i=nodes
                                while nodes!=0:
                                    value=str(input("Enter the node value (Insert Node): "))
                                    dll.insert_at_end(value)
                                    nodes-=1
                                print(f"{i} Node/s inserted in double linked list at end successfully..!")
                            case 3:
                                nodes=int(input("How much node/s do you want (Insert Node): "))
                                i=nodes
                                while nodes!=0:
                                    value=str(input("Enter the node value (Insert Node): "))
                                    cll.insert_at_end(value)
                                    nodes-=1
                                print(f"{i} Node/s inserted in circular linked list at end successfully..!")
                            case 4:
                                nodes=int(input("How much node/s do you want (Insert Node): "))
                                i=nodes
                                while nodes!=0:
                                    value=str(input("Enter the node value (Insert Node): "))
                                    cdll.insert_at_end(value)
                                    nodes-=1
                                print(f"{i} Node/s inserted in circular double linked list at end successfully..!")
                    case 2:
                        match llch:
                            case 1:
                                nodes=int(input("How much node/s do you want (Insert Node): "))
                                i=nodes
                                while nodes!=0:
                                    value=str(input("Enter the node value (Insert Node): "))
                                    ll.insert_at_begin(value)
                                    nodes-=1
                                print(f"{i} Node/s inserted in singular linked list at beginnig successfully..!")
                            case 2:
                                nodes=int(input("How much node/s do you want (Insert Node): "))
                                i=nodes
                                while nodes!=0:
                                    value=str(input("Enter the node value (Insert Node): "))
                                    dll.insert_at_begin(value)
                                    nodes-=1
                                print(f"{i} Node/s inserted in double linked list at beginnig successfully..!")
                            case 3:
                                nodes=int(input("How much node/s do you want (Insert Node): "))
                                i=nodes
                                while nodes!=0:
                                    value=str(input("Enter the node value (Insert Node): "))
                                    cll.insert_at_begin(value)
                                    nodes-=1
                                print(f"{i} Node/s inserted in circular linked list at beginnig successfully..!")
                            case 4:
                                nodes=int(input("How much node/s do you want (Insert Node): "))
                                i=nodes
                                while nodes!=0:
                                    value=str(input("Enter the node value (Insert Node): "))
                                    cdll.insert_at_begin(value)
                                    nodes-=1
                                print(f"{i} Node/s inserted in circular double linked list at beginnig successfully..!")
                    case 3:
                        match llch:
                            case 1:
                                value=str(input("Enter the node value (Insert Node): "))
                                pos=int(input("Enter the index (Insert Node): "))
                                ll.insert_at_end(value)
                                print(f"Node insert at {pos} index successfully..!")
                            case 2:
                                value=str(input("Enter the node value (Insert Node): "))
                                pos=int(input("Enter the index (Insert Node): "))
                                dll.insert_at_end(value)
                                print(f"Node insert at {pos} index successfully..!")
                            case 3:
                                value=str(input("Enter the node value (Insert Node): "))
                                pos=int(input("Enter the index (Insert Node): "))
                                cll.insert_at_end(value)
                                print(f"Node insert at {pos} index successfully..!")
                            case 4:
                                value=str(input("Enter the node value (Insert Node): "))
                                pos=int(input("Enter the index (Insert Node): "))
                                cdll.insert_at_end(value)
                                print(f"Node insert at {pos} index successfully..!")
                    case 4:
                        main_menu_bar()
                        break
        
        except ValueError:
            print("Try again")                
            insert_node()
                        
    #===========delete node programme================
    def delete_node():
        print("Delete Node:")
        menu=["Delete at begginning","Delete at end","Delete at position","Exit"]

        print("==========================")
        length=len(f"{0+0}. {menu[0]}")
        for i in range(4):
            print("|",end="  ")
            print(f"{i+1}. {menu[i]}",end="")
            if(length==len(f"{i+1}. {menu[i]}")):
                print("  |")
            elif(length>len(f"{i+1}. {menu[i]}")):
                space=length-len(f"{i+1}. {menu[i]}")
                for j in range(space):
                    print(" ",end="")
                print("  |")
        print("=========================")
        
        try :
            while True:
                choice=int(input("Enter the number as menu above to delete node (Delete Node): "))
                if(choice<1 or choice>4):
                    choice=int(input("Enter the valid number as above menu (Delete Node):"))
            
                match choice:
                    case 1:
                        match llch:
                            case 1:
                                nodes=int(input("How much node have to delete from beginning (Delete node): "))
                                i=nodes
                                while nodes!=0:
                                    ll.remove_head()
                                    nodes-=1
                                    
                                print(f"{i} Node/s has been deleted at starting in singular linked")
                            case 2:
                                nodes=int(input("How much node have to delete from beginning (Delete node): "))
                                i=nodes
                                while nodes!=0:
                                    dll.remove_head()
                                    nodes-=1
                                    
                                print(f"{i} Node/s has been deleted at starting in double linked")
                            case 3:
                                nodes=int(input("How much node have to delete from beginning (Delete node): "))
                                i=nodes
                                while nodes!=0:
                                    cll.remove_head()
                                    nodes-=1
                                    
                                print(f"{i} Node/s has been deleted at starting in circular linked")
                            case 4:
                                nodes=int(input("How much node have to delete from beginning (Delete node): "))
                                i=nodes
                                while nodes!=0:
                                    cdll.remove_head()
                                    nodes-=1
                                    
                                print(f"{i} Node/s has been deleted at starting in circular double linked")
                    case 2:
                        match llch:
                            case 1:
                                nodes=int(input("How much node have to delete from end (Delete node): "))
                                i=nodes
                                while nodes!=0:
                                    ll.remove_tail()
                                    nodes-=1
                                    
                                print(f"{i} Node/s has been deleted at end in singular linked")
                            case 2:
                                nodes=int(input("How much node have to delete from end (Delete node): "))
                                i=nodes
                                while nodes!=0:
                                    dll.remove_tail()
                                    nodes-=1
                                    
                                print(f"{i} Node/s has been deleted at end in double linked")
                            case 3:
                                nodes=int(input("How much node have to delete from end (Delete node): "))
                                i=nodes
                                while nodes!=0:
                                    cll.remove_tail()
                                    nodes-=1
                                    
                                print(f"{i} Node/s has been deleted at end in circular linked")
                            case 4:
                                nodes=int(input("How much node have to delete from end (Delete node): "))
                                i=nodes
                                while nodes!=0: 
                                    cdll.remove_tail()
                                    nodes-=1
                                    
                                print(f"{i} Node/s has been deleted at end in circular double linked")
                    case 3:
                        match llch:
                            case 1:
                                index=int(input("Enter the node index (Delete node): "))
                                ll.remove_at_index(index)
                                print(f"Node deleted at index {index} in singular linked list")
                            case 2:
                                index=int(input("Enter the node index (Delete node): "))
                                ll.remove_at_index(index)
                                print(f"Node deleted at index {index} in double linked list")
                            case 3:
                                index=int(input("Enter the node index (Delete node): "))
                                ll.remove_at_index(index)
                                print(f"Node deleted at index {index} in circular linked list")
                            case 4:
                                index=int(input("Enter the node index (Delete node): "))
                                ll.remove_at_index(index)
                                print(f"Node deleted at index {index} in circular double linked list")
                    case 4:
                        main_menu_bar()
                        break
        
        except AttributeError:
            print("You have not inserted node; insert node first ")        
            main_menu_bar()
        
        except ValueError:
            print("Please try again") 
            delete_node()


    # ====================== update node programme ======================
    def update_node():
                print("Update Node:")
                menu=["Update at biginning","Update at end","Update at position","Exit"]

                print("=============================")
                length=len(f"{0+0}. {menu[0]}")
                for i in range(4):
                    print("|",end="  ")
                    print(f"{i+1}. {menu[i]}",end="")
                    if(length==len(f"{i+1}. {menu[i]}")):
                        print("  |")
                    elif(length>len(f"{i+1}. {menu[i]}")):
                        space=length-len(f"{i+1}. {menu[i]}")
                        for j in range(space):
                            print(" ",end="")
                        print("  |")
                print("============================")

                try:
                    while True:
                        choice=int(input("Enter the number as menu above to update node (Update Node): "))
                        if(choice<1 or choice>4):
                            choice=int(input("Enter the valid number as above menu (Update Node):"))
                    
                        match choice:
                            case 1:
                                match llch:
                                    case 1:                            
                                        value=int(input("Enter the value update head (Update node) : "))
                                        ll.update_head(value)
                                        print(f"Head node updated with {value} value in singular linked list successfully..!")                                    
                                    case 2:
                                        value=int(input("Enter the value update head (Update node) : "))
                                        dll.update_head(value)
                                        print(f"Head node updated with {value} value in double linked list successfully..!")                                         
                                    case 3:
                                        value=int(input("Enter the value update head (Update node) : "))
                                        cll.update_head(value)
                                        print(f"Head node updated with {value} value in circular linked list successfully..!")      
                                    case 4:
                                        value=int(input("Enter the value update head (Update node) : "))
                                        cdll.update_head(value)
                                        print(f"Head node updated with {value} value circular double linked list successfully..!")      
                            case 2:
                                match llch:
                                    case 1:                            
                                        value=int(input("Enter the value update tail (Update node) : "))
                                        ll.update_tail(value)
                                        print(f"Tail node updated with {value} value in singular linked list successfully..!")                                    
                                    case 2:
                                        value=int(input("Enter the value update tail (Update node) : "))
                                        dll.update_tail(value)
                                        print(f"Tail node updated with {value} value in double linked list successfully..!")                                         
                                    case 3:
                                        value=int(input("Enter the value update tail (Update node) : "))
                                        cll.update_tail(value)
                                        print(f"Tail node updated with {value} value in circular linked list successfully..!")      
                                    case 4:
                                        value=int(input("Enter the value update tail (Update node) : "))
                                        cdll.update_tail(value)
                                        print(f"Tail node updated with {value} value circular double linked list successfully..!") 
                            case 3:
                                match llch:    
                                    case 1:                            
                                        value=int(input("Enter the value update head (Update node) : "))
                                        pos=int(input("Enter the node position (Update node): "))
                                        ll.update_at_position(value,pos)
                                        print(f"Node updated with {value} value at position {pos} in singular linked list successfully..!")                                    
                                    case 2:
                                        value=int(input("Enter the value update head (Update node) : "))
                                        pos=int(input("Enter the node position (Update node): "))
                                        dll.update_at_position(value,pos)
                                        print(f"Node updated with {value} value at position {pos} in double linked list successfully..!")                                         
                                    case 3:
                                        value=int(input("Enter the value update head (Update node) : "))
                                        pos=int(input("Enter the node position (Update node): "))
                                        cll.update_at_position(value,pos)
                                        print(f"Node updated with {value} value at position {pos} in circular linked list successfully..!")      
                                    case 4:
                                        value=int(input("Enter the value update head (Update node) : "))
                                        pos=int(input("Enter the node position (Update node): "))
                                        cdll.update_at_position(value,pos)
                                        print(f"Node updated with {value} value at position {pos} in cular double linked list successfully..!") 
                            case 4:
                                main_menu_bar()
                                break                       
                except AttributeError:
                    print("You have not inserted node; insert node first ")        
                    main_menu_bar()
                
                except ValueError:
                    print("Please try again") 
                    update_node()

    try: 
        while True:
            ch=int(input("Enter the number as per menu (Mian): "))
            if(ch>6 or ch<1):
                ch=int(input("Please enter valid menu number as above (Mian):"))                
            match ch:
                case 1:
                    createll()                    
                case 2:
                    if(llch is None):
                        print("Select type of linked list first")
                        print(llch)
                    else:
                        insert_node()                       
                case 3:
                    if(llch is None):
                        print("Select type of linked list first")
                        print(llch)
                    else:
                        update_node()
                case 4:
                    if(llch is None):
                        print("Select type of linked list first")
                        print(llch)
                    else:
                        print(llch)
                        delete_node()
                case 5:
                    match llch:
                        case 1:
                            ll.printll()
                        case 2:
                            dll.printll()
                        case 3:
                            cll.printll()
                        case 4:
                            cdll.printll()
                case 6:        
                    break                   
            
    except NameError:
        print(f"Without inserting node or choosing type of linked list cannot perfrom ''{main_menu[ch-1]}'' operation")
        main_menu_bar()
    except ValueError:
        print("Please try again") 
        

main_menu_bar()    