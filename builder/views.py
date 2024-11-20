from django.shortcuts import render, redirect
from collections import defaultdict
from builder.models import *

def builder_index(request):
    return render(request, 'builder/index.html')


def resume_details(request):
    if request.method == 'GET':
        return render(request, 'builder/get_resume_details.html')
    elif request.method == 'POST':
        # Single value fields
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        summary = request.POST.get('summary')
        skills = request.POST.get('skills')

        # Dynamic fields for experience
        experiences = defaultdict(dict)
        educations = defaultdict(dict)

        # for key, value in request.POST.items():
        #     # Process experience keys
        #     if key.startswith('experience['):
        #         # Extract index and field name
        #         prefix, field = key.split('][')
        #         index = int(prefix.split('[')[1])
        #         field_name = field.rstrip(']')
        #         experiences[index][field_name] = value
            
        #     # Process education keys
        #     elif key.startswith('education['):
        #         # Extract index and field name
        #         prefix, field = key.split('][')
        #         index = int(prefix.split('[')[1])
        #         field_name = field.rstrip(']')
        #         educations[index][field_name] = value

        # Convert defaultdict to a regular list of dictionaries
        experiences_list = [experiences[i] for i in sorted(experiences)]
        educations_list = [educations[i] for i in sorted(educations)]


        # Log or process data
        print({
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "location": location,
            "summary": summary,
            "skills": skills,
            "experiences": experiences_list,
            "educations": educations_list,
        })


        resume_details = ResumeDetail.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            location=location,
            summary=summary,
            skills=skills,
        )

        for experience in experiences_list:
            resume_experience = ResumeExperience.objects.create(
                position=experience['position'],
                company=experience['company'],
                location=experience['location'],
                start_date=experience['start_date'],
                end_date=experience['end_date'],
                responsibilities=experience['responsibilities'],
            )
            resume_details.experiences.add(resume_experience)

        for education in educations_list:
            resume_education = ResumeEducation.objects.create(
                degree=education['degree'],
                field=education['field'],
                school=education['school'],
                start_date=education['start_date'],
                end_date=education['end_date'],
            )
            resume_details.educations.add(resume_education)

        resume_details.save()




        return redirect(f'resume_template/{resume_details.id}')
    

def resume_template(request, id):
    resume = ResumeDetail.objects.get(id=id)
    return render(request, 'builder/resume_template.html', {"resume": resume})