#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the Student structure
struct Student {
    int rollNo;
    char name[50];
    int classesAttended;
    int totalClasses;
};

// Function prototypes
void addStudent();
void markAttendance();
void viewAttendance();
void displayMenu();
void printHeader(char *title);

// File name for storing data
const char *FILENAME = "attendance_data.dat";

int main() {
    int choice;
    // Set console color (Windows specific) - 0B is Black background, Light Aqua text
    // Other color codes: 0A (Green), 0E (Yellow), 0F (White)
    system("color 0B"); 

    while(1) {
        displayMenu();
        printf("\t\t\tEnter your choice: ");
        if (scanf("%d", &choice) != 1) {
            // clear input buffer if non-integer is entered
            while(getchar() != '\n');
            continue;
        }

        switch(choice) {
            case 1:
                addStudent();
                break;
            case 2:
                markAttendance();
                break;
            case 3:
                viewAttendance();
                break;
            case 4:
                printHeader("THANK YOU FOR USING THE SYSTEM");
                exit(0);
            default:
                printf("\n\t\t\tInvalid choice! Please try again.\n");
                system("pause");
        }
    }
    return 0;
}

void printHeader(char *title) {
    system("cls"); // Clear screen (Windows specific)
    printf("\n\n");
    printf("\t\t\t======================================================\n");
    printf("\t\t\t|                                                    |\n");
    printf("\t\t\t|      ATTENDANCE MANAGEMENT SYSTEM                  |\n");
    printf("\t\t\t|                                                    |\n");
    printf("\t\t\t======================================================\n");
    printf("\n\t\t\t>>> %s <<<\n\n", title);
}

void displayMenu() {
    printHeader("MAIN MENU");
    printf("\t\t\t1. Add New Student\n");
    printf("\t\t\t2. Mark Attendance\n");
    printf("\t\t\t3. View Attendance Records\n");
    printf("\t\t\t4. Exit\n");
    printf("\n\t\t\t------------------------------------------------------\n");
}

void addStudent() {
    FILE *fp;
    struct Student s;
    printHeader("ADD NEW STUDENT");

    fp = fopen(FILENAME, "ab"); // append in binary mode (creates if doesn't exist)
    if (fp == NULL) {
        printf("\t\t\tError opening file!\n");
        return;
    }

    printf("\t\t\tEnter Roll Number: ");
    scanf("%d", &s.rollNo);
    
    // Clear input buffer before reading string
    while(getchar() != '\n');
    
    printf("\t\t\tEnter Student Name: ");
    fgets(s.name, sizeof(s.name), stdin);
    s.name[strcspn(s.name, "\n")] = 0; // Remove trailing newline from fgets

    s.classesAttended = 0;
    s.totalClasses = 0;

    fwrite(&s, sizeof(struct Student), 1, fp);
    fclose(fp);

    printf("\n\t\t\tStudent added successfully!\n");
    system("pause");
}

void markAttendance() {
    FILE *fp;
    struct Student s;
    int roll, found = 0;
    int status;
    long pos;

    printHeader("MARK ATTENDANCE");
    
    fp = fopen(FILENAME, "rb+"); // read and update in binary mode
    if (fp == NULL) {
        printf("\t\t\tNo student records found! Please add students first.\n");
        system("pause");
        return;
    }

    printf("\t\t\tEnter Roll Number to mark attendance: ");
    scanf("%d", &roll);

    // Read file sequentially to find the student
    while (fread(&s, sizeof(struct Student), 1, fp)) {
        if (s.rollNo == roll) {
            found = 1;
            printf("\n\t\t\tStudent Found: %s\n", s.name);
            printf("\t\t\tPress 1 for Present, 0 for Absent: ");
            scanf("%d", &status);

            s.totalClasses++;
            if (status == 1) {
                s.classesAttended++;
            }

            // Move file pointer back to update this specific record
            pos = ftell(fp) - sizeof(struct Student);
            fseek(fp, pos, SEEK_SET);
            fwrite(&s, sizeof(struct Student), 1, fp);
            
            printf("\n\t\t\tAttendance marked successfully!\n");
            break; // Record updated, exit loop
        }
    }

    if (!found) {
        printf("\n\t\t\tStudent with Roll Number %d not found!\n", roll);
    }

    fclose(fp);
    system("pause");
}

void viewAttendance() {
    FILE *fp;
    struct Student s;
    float percentage;

    printHeader("ATTENDANCE RECORDS");

    fp = fopen(FILENAME, "rb");
    if (fp == NULL) {
        printf("\t\t\tNo student records found! Please add students first.\n");
        system("pause");
        return;
    }

    // Print table header
    printf("\t\t%-10s %-25s %-10s %-10s %-10s\n", "Roll No", "Name", "Total", "Attended", "Percent(%)");
    printf("\t\t----------------------------------------------------------------------\n");

    // Read and print all records
    while (fread(&s, sizeof(struct Student), 1, fp)) {
        if (s.totalClasses > 0) {
            percentage = ((float)s.classesAttended / s.totalClasses) * 100.0;
        } else {
            percentage = 0.0;
        }
        printf("\t\t%-10d %-25s %-10d %-10d %-10.2f\n", 
               s.rollNo, s.name, s.totalClasses, s.classesAttended, percentage);
    }

    fclose(fp);
    printf("\n");
    system("pause");
}
