using System;

class Student
{
    public string Name { get; set; }
    public int ID { get; set; }
    public int Marks { get; set; }

    public Student(string name, int id, int marks)
    {
        Name = name;
        ID = id;
        Marks = marks;
    }

    public string GetGrade()
    {
        if (Marks >= 90) return "A";
        else if (Marks >= 75) return "B";
        else if (Marks >= 60) return "C";
        else return "F";
    }

    public void DisplayDetails()
    {
        Console.WriteLine($"Student: {Name}, ID: {ID}, Marks: {Marks}, Grade: {GetGrade()}");
    }
}

class StudentIITGN : Student
{
    public string HostelName { get; set; }

    public StudentIITGN(string name, int id, int marks, string hostel) : base(name, id, marks)
    {
        HostelName = hostel;
    }

    public void DisplayIITGNDetails()
    {
        DisplayDetails();
        Console.WriteLine($"Hostel: {HostelName}");
    }

    static void Main()
    {
        StudentIITGN student = new StudentIITGN("Rashid", 101, 85, "Jwalamukhi");
        student.DisplayIITGNDetails();
    }
}
