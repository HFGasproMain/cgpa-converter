from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileUpdateForm, CourseForm, GenerateTableForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile


# Create your views here.
def index(request):
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'login deets: {username} and {password}')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def dashboard(request):
	try:
		profile = Profile.objects.get(user=request.user)
	except Profile.DoesNotExist:
		profile = None
	return render(request, 'dashboard.html', {'profile': profile})



def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        form = ProfileUpdateForm()
    return render(request, 'profile_update.html', {'form': form})



def generate_table(request):
    if request.method == 'POST':
        form = GenerateTableForm(request.POST)
        if form.is_valid():
            degree = form.cleaned_data['level']
            academic_scale = form.cleaned_data['academic_scale']
            num_courses = form.cleaned_data['num_courses']
            # Perform further processing or save the data
            # Return a response or redirect as per your requirement
    else:
        form = GenerateTableForm()
    return render(request, 'generate_table.html', {'form': form})


def table_input(request):
    if request.method == "POST":
        academic_scale = request.POST.get("academic_scale")
        degree = request.POST.get("level")
        num_courses = int(request.POST.get("num_courses"))
        print(f'received table1: {academic_scale}, {degree}, {num_courses}')
        test = request.POST.get('course_unit')
        print(f'Test o: {test}')

        total_gp = 0
        total_units = 0

        for i in range(1, num_courses+1):

            print(f'i is {i}')
            print(f"Value of course_unit_{i}: {request.POST.get('course_title')}")
            course_title = request.POST.get("course_title")
            print(f'title{i} inside: {course_title}')
            course_unit = (request.POST.get("course_unit"))
            print(f'units{i} inside: {course_unit} with type {type(course_unit)}')
            score = (request.POST.get("score"))
            print(f'score inside{i}: {score}')
            grade = request.POST.get("grade")
            print(f'grade {i} => {course_unit}, {course_title}, {score}, {grade}')
            course_unit = int(course_unit)

            if academic_scale == '8':
                if grade == 'A':
                    grade_point = 8
                elif grade == 'B':
                    grade_point = 7
                elif grade == 'C':
                    grade_point = 6
                elif grade == 'D':
                    grade_point = 5
                else:
                    grade_point = 4
            elif academic_scale == '7':
                if grade == 'A':
                    grade_point = 7
                elif grade == 'B':
                    grade_point = 6
                elif grade == 'C':
                    grade_point = 5
                elif grade == 'D':
                    grade_point = 4
                else:
                    grade_point = 3
            elif academic_scale == '5':
                if grade == 'A':
                    grade_point = 5
                elif grade == 'B':
                    grade_point = 4
                elif grade == 'C':
                    grade_point = 3
                elif grade == 'D':
                    grade_point = 2
                else:
                    grade_point = 1
            else:
                if grade == 'A':
                    grade_point = 4
                elif grade == 'B':
                    grade_point = 3
                elif grade == 'C':
                    grade_point = 2
                elif grade == 'D':
                    grade_point = 1
                else:
                    grade_point = 0

            gp = course_unit * grade_point
            print(f'course_units = {course_unit} & grade_point = {grade_point}')
            print(f'GP => {gp}')
            total_gp += gp
            print(f'total_GP = {total_gp}')
            total_units += course_unit
            print(f'total_units; {total_units}')

        if total_units > 0:
            cgpa = total_gp / total_units
        else:
            cgpa = 0

        if degree == 'Masters':
            average_cgpa = 3.5
        elif degree == 'PhD':
            average_cgpa = 4.0
        else:
            average_cgpa = 0.0

        if cgpa >= average_cgpa:
            recommendation = 'Congratulations! Your CGPA is above average.'
        else:
            recommendation = 'Keep up the good work!'

        context = {
            'cgpa': cgpa,
            'degree':degree,
            'recommendation': recommendation
        }
        return render(request, 'results.html', context)
    
    return render(request, 'table_input.html')




def table_inputs(request):
    if request.method == "POST":
        form = GenerateTableForm(request.POST)
        if form.is_valid():
            course_titles = form.cleaned_data.get("course_title")
            course_units = form.cleaned_data.get("course_unit")
            scores = form.cleaned_data.get("score")
            grades = form.cleaned_data.get("grade")
            academic_scale = form.cleaned_data.get("academic_scale")
            degree = form.cleaned_data.get("degree")

            print(f'received 1: {course_units}, {scores}, {grades}, {academic_scale} {degree}')
            print(f'received 2: {academic_scale} {degree}')

            total_gp = 0
            total_units = 0

            for unit, score, grade in zip(course_units, scores, grades):
                if academic_scale == 8:
                    if grade == 'A':
                        grade_point = 8
                    elif grade == 'B':
                        grade_point = 7
                    elif grade == 'C':
                        grade_point = 6
                    elif grade == 'D':
                        grade_point = 5
                    else:
                        grade_point = 4
                elif academic_scale == 7:
                    if grade == 'A':
                        grade_point = 7
                    elif grade == 'B':
                        grade_point = 6
                    elif grade == 'C':
                        grade_point = 5
                    elif grade == 'D':
                        grade_point = 4
                    else:
                        grade_point = 3
                elif academic_scale == 5:
                    if grade == 'A':
                        grade_point = 5
                    elif grade == 'B':
                        grade_point = 4
                    elif grade == 'C':
                        grade_point = 3
                    elif grade == 'D':
                    	grade_point = 2
                    else:
                        grade_point = 1
                else:
                	if grade == 'A':
                		grade_point = 4
                	elif grade == 'B':
                		grade_point = 3
                	elif grade == 'C':
                		grade_point = 2
                	elif grade == 'D':
                		grade_point = 1
                	else:
                		grade_point = 0
                    
               	# Set grade_point based on the scale and grade mapping
                gp = float(unit) * grade_point
                total_gp += gp
                total_units += int(unit)
                print(f'totals => {gp}, {total_units}')

            # Calculate the CGPA
            if total_units > 0:
                cgpa = total_gp / total_units
                print(f'cgpa here: {cgpa}')
            else:
                cgpa = 0

            # Determine the average CGPA based on the degree
            if degree == 'Masters':
                average_cgpa = 3.5
            elif degree == 'PhD':
                average_cgpa = 4.0
            else:
                average_cgpa = 0.0

            # Generate the recommendation based on the CGPA
            if cgpa > average_cgpa:
                recommendation = 'Congratulations! Your CGPA is above average.'
            else:
                recommendation = 'Keep up the good work!'

            # Perform any other required actions or return the results

            context = {
                'form': form,
                'cgpa': cgpa,
                'recommendation': recommendation
            }
            return render(request, 'results.html', context)
    else:
        form = GenerateTableForm()

    context = {
        'form': form,
    }
    return render(request, 'table_input.html', context)
