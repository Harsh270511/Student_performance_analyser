# Attendance Management System (C Project)

This is a complete C language project designed for a college submission. It provides a simple, interactive, and visually appealing console interface to manage student attendance.

## Features

1. **Add New Student**: Register a new student by their Roll Number and Name.
2. **Mark Attendance**: Search for a student by their Roll Number and mark them Present (1) or Absent (0).
3. **View Attendance Records**: Displays a well-formatted table of all students, total classes, attended classes, and attendance percentage.
4. **Data Persistence**: Uses File Handling (`attendance_data.dat` created automatically) so your records are saved even after closing the program.
5. **Attractive UI**: Uses custom console colors and ASCII text borders making it perfect for presentations!

## How to Compile & Run (Windows)

**Using GCC Compiler:**
1. Open your terminal or command prompt in this folder.
2. Compile the code by running:
   ```bash
   gcc attendance_system.c -o attendance_system.exe
   ```
3. Run the compiled executable:
   ```bash
   .\attendance_system.exe
   ```

**Using an IDE (like Dev-C++, Code::Blocks, or VS Code):**
Simply open `attendance_system.c` in your IDE and click "Compile & Run" (usually F9, F11, or a 'Play' button).

## Project Presentation Tips
- Start by running the program and showcasing the **Main Menu**. Point out the nice text borders and color scheme (which is often a bonus in college projects).
- Demonstrate adding 2-3 fictional students.
- Go to the **Mark Attendance** menu and mark some present and some absent. Do this multiple times for the same student to show the total classes counter incrementing.
- Finally, select **View Attendance Records** to display the automatically calculated attendance percentage in a clean table layout.
- If asked, explain how it uses `struct` to organize data, and binary file handling (`fopen` with `"ab"`, `"rb"`, and `"rb+"`) to securely save records.
