# QuickReg

### John Chen, Moiya Josephs, Anjana Rajan, Carlton Welch

## Setup

1. Move to quickreg directory
```
$ cd quickreg
```
2. Create virtual environment (only required on initial setup)
```
$ python3 -m venv ~/.virtualenvs/quickreg
```
3. Activate virtual environment
```
$ source ~/.virtualenvs/mysite/bin/activate
```
4. Install Django (only required on initial setup)
```
$ pip install Django
```
5. Launch QuickReg
```
$ python3 manage.py runserver
```
6. Open browser (optimized for Firefox) and navigate to server location (http://localhost:8000/)

## Documentation
![Login](aa2/pics/Login_picture.jpg "Login Page that appears when entering the website.")

- Login Page that appears when entering the website.
![Sign Up](aa2/pics/sign_up_pg.png "Sign up page that appears when entering the website.")

![User Types](aa2/pics/user_types.png "User Types")

- New User will enter their user type.
### Student
![Student Home](aa2/pics/student_home.png "Student Home")

Student homepage, here the user can select to request appointments, view courses, submit advising forms and send messages.

![Student_appointments](aa2/pics/student_appointments.png "Student Appointment")

Student can request appointments based on Faculty's given availabilities.

![Request Appointments](aa2/pics/request_appointments.png "Student Request Appointment")

Student can request appointment from the dates available.

![Advising Form](aa2/pics/advising_form.png "Student Advising Form" style="centerme")

Student can submit an advising form. Providing the given information and then submitting it.

img[src$="centerme"] {
  display:block;
  margin: 0 auto;
}



### Faculty

![Add/Del Courses](aa2/pics/add_del_courses.png "Student Request Appointment")

Faculty can Add and Delete any courses.

![Requested Advising All](aa2/pics/faculty_advising.png "Student Request Appointment")

Faculty can view adivising based on the unique ID from each student.

![View Submission](aa2/pics/viewing_sub.png "Student Request Appointment")

Here the faculty can view the request to be advised in detail and either request or deny it.

![Appointments](aa2/pics/appointments.png "Appointment")
