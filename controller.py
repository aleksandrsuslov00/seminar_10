import text
import view
from model import PhoneBook

def search_func(book: PhoneBook, msg: str):
    word = view.input_info(msg)
    result = book.search(word)
    view.show_contacts(result, text.search_contact_error(word))
    return result

def start():
    pb = PhoneBook()
    while True:
        choice = view.main_menu()
        
        if choice == '1':
            pb.open_file()
            view.print_msg(text.open_successful)
        
        elif choice == '2':
            pb.save_file()
            view.print_msg(text.save_successful)
        
        elif choice == '3':
            view.show_contacts(pb.phone_book, text.empty_phone_book_error)
        
        elif choice == '4': 
            contact = view.input_new_contact(text.input_new_contact)
            pb.new_contact(contact)
            view.print_msg(text.contact_successful_result(contact[0], 0))
        
        elif choice == '5':
            search_func(pb, text.input_search_word)
       
        elif choice == '6':
            if search_func(pb, text.input_edit_word):
                u_id = view.input_info(text.input_edit_id)
                new_contact = view.input_new_contact(text.input_edit_contact)
                name = pb.edit(int(u_id), new_contact)
                view.print_msg(text.contact_successful_result(name, 1))
        
        elif choice == '7':
            if search_func(pb, text.input_delete_word):
                u_id = view.input_info(text.input_delete_id)
                confirm_name = pb.phone_book.get(int(u_id))
                if view.input_info(text.confirm_delete_contact(confirm_name)).lower() == 'y':
                    name = pb.delete(int(u_id))
                    view.print_msg(text.contact_successful_result(name, 2))
        
        elif choice == '8':
            if pb.original_book != pb.phone_book:
                if view.input_info(text.confirm_save_changes).lower() == 'y':
                    pb.save_file()
            view.print_msg(text.exit_from_menu)
            break
            
        else: 
            view.print_msg(text.input_main_menu_error)
            
