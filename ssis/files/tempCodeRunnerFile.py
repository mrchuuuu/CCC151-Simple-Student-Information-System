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
        """
        student_year_input = Entry(add_window_label, width = 30)
        student_year_input.grid(row = 2, column = 1)
        """
        student_year_input = Combobox(add_window_label, values = ["1", "2", "3", "4"])
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
        column_data = combobox_values('ssis/data/student.csv', column_index)
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

            with open('ssis/data/student.csv', 'a', newline = '') as student_file:
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