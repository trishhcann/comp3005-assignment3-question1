COMP 3005, Assignment 3, Question 1
Trisha Toocaram, 101267603

Video demo: https://youtu.be/JcbeSoVGM70?si=3D923eZkpdfobq4M

## Files Included
| File | Description |
|------|--------------|
| `app.py` | Main Python application containing CRUD functions |
| `database/studentdb.sql` | SQL script to create the table and insert sample data |
| `README.md` | Instructions on how to compile, run, and verify the application |


Database Setup
1. Open pgAdmin  
2. Create a new database named `studentdb`
3. Run the SQL script to create and populate the table:
        In pgAdmin: open Query Tool → load studentdb.sql →  Execute


Compile and run the application
    -Install required package: pip install psycopg2-binary
    -Update connection settings in app.py if needed:
        user="postgres"
        password="YOUR_PASSWORD" (postgres)
        database="studentdb"
        host="localhost"
        port=5432
    -Run the program: python3 app.py







