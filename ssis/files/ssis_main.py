from tkinter import *
import csv
from tkinter.ttk import Combobox
    
def view_student():
    students_view_window = Toplevel()
    students_view_window.title("View Students")
    view_window_label = Frame(students_view_window,bg = '#5c9ca3')
    view_window_label.grid(row = 1, column = 1)
    
    listbox = Listbox(view_window_label, 
                      width = 55, 
                      height = 12, 
                      bg = '#c0c5c9')
    listbox.pack(padx = 10, pady = 10)

    def view_data(csv_path):
        student_list = []
        with open('data/student.csv', 'r', newline = '') as student_file:
            reader = csv.reader(student_file)
            for row in reader:
                student_list.append(row)
        
        student_file.close()
        return student_list
    
    def display_data():
        csv_path = 'data/student.csv'
        data = view_data(csv_path)
        for row in data:
            listbox.insert(END, row)
    
    display_data()
    
    button_enroll_students = Button(view_window_label,  
                                    text = "Enroll Students", 
                                    padx = 49, pady = 5, 
                                    bg = '#9cc3a3', 
                                    command = lambda: enroll_student())
    button_enroll_students.pack(pady = 5)
    def enroll_student():
        students_add_window = Toplevel()
        students_add_window.title("Enroll Students")
        add_window_label = Label(students_add_window, bg = '#5c9ca3')
        add_window_label.pack()
        
        enter_name = Label(add_window_label, text = "Enter Student Name: ", bg = '#5c9ca3')
        enter_name.grid(row = 0, column = 0)
        student_name_input = Entry(add_window_label, width = 30)
        student_name_input.grid(row = 0, column = 1)
                
        enter_id = Label(add_window_label, text = "Enter Student ID# YYYY-MMMM: ", bg = '#5c9ca3')
        enter_id.grid(row = 1, column = 0)
        student_id_input = Entry(add_window_label, width = 30)
        student_id_input.grid(row = 1, column = 1)
                
        enter_year = Label(add_window_label, text = "Enter Student Year Level: ", bg = '#5c9ca3')
        enter_year.grid(row = 2, column = 0)
        student_year_input = Entry(add_window_label, width = 30)
        student_year_input.grid(row = 2, column = 1)
                
        enter_gender = Label(add_window_label, text = "Enter Student Gender: ", bg = '#5c9ca3')
        enter_gender.grid(row = 3, column = 0)
        student_gender_input = Entry(add_window_label, width = 30)
        student_gender_input.grid(row = 3, column = 1)
        
        enter_course = Label(add_window_label, text = "Select Course Code: ", bg = '#5c9ca3')
        enter_course.grid(row = 4, column = 0)
        
        button_add = Button(add_window_label, text = "Add Student", 
                            bg = '#9cc3a3',
                            command = lambda: add_student_data())
        button_add.grid(row = 5, columnspan = 2)  
        
        def combobox_values(filename, column_index):
            column_data = []
            with open(filename, 'r') as course_file:
                reader = csv.reader(course_file)
                next(reader)
                for row in reader:
                    if column_index < len(row):
                        column_data.append(row[column_index])
            return column_data
        
        column_index = 0
        column_data = combobox_values('data/course.csv', column_index)
        student_course_input = Combobox(add_window_label, values = column_data)
        student_course_input.grid(row = 4, column = 1)
        student_course_input.current() 
        
        def add_student_data():
            student_name = student_name_input.get()
            student_id = student_id_input.get()
            student_year = student_year_input.get()
            student_gender = student_gender_input.get()
            student_course = student_course_input.get()
            field_names = ['Name', 'ID# YYYY-MMMM', 'Year Level', 'Gender', 'Course']
            student_data = {'Name': student_name,
                            'ID# YYYY-MMMM': student_id, 
                            'Year Level': student_year, 
                            'Gender': student_gender, 
                            'Course': student_course}

            with open('data/student.csv', 'a', newline = '') as student_file:
                writer = csv.DictWriter(student_file, fieldnames = field_names)
            
                if student_file.tell() == 0:
                    writer.writeheader()
            
                writer.writerow(student_data)
        
                student_file.close()
            
            student_name_input.delete(0, END)
            student_id_input.delete(0, END)
            student_year_input.delete(0, END)
            student_gender_input.delete(0, END)
            student_course_input.delete(0, END)
            
    remove_button = Button(view_window_label, 
                           text = "Remove Selected Student", 
                           padx = 22, pady = 5, 
                           bg = '#9cc3a3',  
                           command = lambda: remove_selected())
    remove_button.pack(pady = 5)
    def remove_selected():
        selected_index = listbox.curselection()
        if selected_index:
            listbox.delete(selected_index)
                
            csv_path = 'data/student.csv'
            with open(csv_path, 'r', newline = '') as student_file:
                data = list(csv.reader(student_file))
                    
            with open(csv_path, 'w', newline = '') as student_file:
                writer = csv.writer(student_file)
                for i, row in enumerate(data):
                    if i not in selected_index:
                        writer.writerow(row)
                
                student_file.close()
                
    button_edit_students= Button(view_window_label,  
                                 text = "Edit Student Details", 
                                 padx = 38, 
                                 pady = 5, 
                                 bg = '#9cc3a3',
                                 command = lambda: edit_selected())
    button_edit_students.pack(pady = 5)  
    def edit_selected():
        selected_index = listbox.curselection()
        if selected_index:
            listbox.delete(selected_index)
                
            csv_path = 'data/student.csv'
            with open(csv_path, 'r', newline = '') as student_file:
                data = list(csv.reader(student_file))
            with open(csv_path, 'w', newline = '') as student_file:
                writer = csv.writer(student_file)
                for i, row in enumerate(data):
                    if i not in selected_index:
                        writer.writerow(row)
            enroll_student()
           
def view_course():
    course_view_window = Toplevel()
    course_view_window.title("View Courses")
    view_course_window = Label(course_view_window, bg = '#5c9ca3')
    view_course_window.pack()
    
    listbox = Listbox(view_course_window, 
                      width = 50, 
                      height = 10, 
                      bg = '#c0c5c9')
    listbox.pack(padx = 10, pady = 10)

    def view_data(file_path):
        data = []
        with open(file_path, 'r', newline = '') as course_file:
            reader = csv.reader(course_file)
            for row in reader:
                data.append(row)
        return data
    
    def display_data():
        csv_path = 'data/course.csv'
        data = view_data(csv_path)
        for row in data:
            listbox.insert(END, row)
            
    display_data()

    button_add_course = Button(view_course_window, 
                               text = "Add Courses", 
                               padx = 49, 
                               pady = 5, 
                               bg = '#9cc3a3',
                               command = lambda: add_course())
    button_add_course.pack(pady = 5)
    def add_course():
        course_add_window = Toplevel()
        course_add_window.title("Add Course")
        course_add_window = Label(course_add_window, bg = '#5c9ca3')
        course_add_window.pack()
        
        course_code = Label(course_add_window, text = "Enter Course Code: ", bg = '#5c9ca3')
        course_code.grid(row = 0, column = 0)
        course_code_input = Entry(course_add_window, width = 30)
        course_code_input.grid(row = 0, column = 1)
        
        enter_course_name = Label(course_add_window, text = "Enter Course Name: ", bg = '#5c9ca3')
        enter_course_name.grid(row = 1, column = 0)
        course_name_input = Entry(course_add_window, width = 30)
        course_name_input.grid(row = 1, column = 1)
        
        add_course_button = Button(course_add_window, 
                                   text = "Add Course", 
                                   bg = '#9cc3a3',
                                   command = lambda: button_add_course())
        add_course_button.grid(pady = 5, columnspan = 2)
        
        def button_add_course():
            course_code = course_code_input.get()
            course_name = course_name_input.get()
            
            field_names = ['Course Code', 'Course Name']
            course_data = {'Course Code': course_code,'Course Name': course_name}

            with open('data/course.csv', 'a', newline = '') as course_file:
                writer = csv.DictWriter(course_file, fieldnames = field_names)
                
                if course_file.tell() == 0:
                    writer.writeheader()
                
                writer.writerow(course_data)
            
                course_file.close()
            
            course_code_input.delete(0, END)
            course_name_input.delete(0, END)
    
    button_remove_course = Button(view_course_window, 
                                  text = "Remove Course", 
                                  padx = 41, 
                                  pady = 5, 
                                  bg = '#9cc3a3',
                                  command = lambda: remove_selected())
    button_remove_course.pack(pady = 5)
    def remove_selected():
        selected_index = listbox.curselection()
        if selected_index:
            listbox.delete(selected_index)
                
            csv_path = 'data/course.csv'
            with open(csv_path, 'r', newline = '') as student_file:
                data = list(csv.reader(student_file))
                    
            with open(csv_path, 'w', newline = '') as student_file:
                writer = csv.writer(student_file)
                for i, row in enumerate(data):
                    if i not in selected_index:
                        writer.writerow(row)
                
                student_file.close()
                
if __name__ == "__main__":
    ssis_app = Tk()
    ssis_app.title("Simple Student Information System")
    ssis_app.geometry("500x200")    
    ssis_app.configure(bg = '#c0c5c9')    
    #app_frame = Frame(ssis_app, padx = 50, pady= 50)
    #app_frame.pack(padx = 10, pady = 10)
    
    title = Label(ssis_app, 
                  text = "Simple Student Information System", 
                  bg = '#c0c5c9', 
                  font = ("Arial", 23))
    title.place(x = 8, y = 40)   
      
    button_view_students = Button(ssis_app,  
                                  text = "View Students", 
                                  padx = 47, 
                                  pady = 5,
                                  bg = '#5c9ca3',
                                  command = lambda: view_student())
    button_view_students.place(x = 160, y = 100)
            
    button_view_course = Button(ssis_app,  
                                text = "View Courses", 
                                padx = 49, 
                                pady = 5,
                                bg = '#5c9ca3',
                                command = lambda: view_course())
    button_view_course.place(x = 160, y = 140)

    ssis_app.mainloop()
