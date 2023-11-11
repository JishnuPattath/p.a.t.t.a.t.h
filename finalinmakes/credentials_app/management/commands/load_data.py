from django.core.management.base import BaseCommand
from credentials_app.models import Course, Module

class Command(BaseCommand):
    help = 'Load Courses and Modules'

    def handle(self, *args, **kwargs):
        Module.objects.all().delete()
        course_names = [
            'Computer Science', 'Civil Engineering', 'Electrical Engineering', 'Film Studies'
        ]

        if not Course.objects.count():
            for course_name in course_names:
                Course.objects.create(name=course_name)

        # Computer Science
        cs = Course.objects.get(name='Computer Science')

        compsci_modules = [
            'AI',
            'Machine Learning',
            'Web Development',
            'Software Engineering', 
            'NoSQL Databases'
        ]

        for module in compsci_modules:
            Module.objects.create(name=module, course=cs)

        # Civil
        civil, created = Course.objects.get_or_create(name='Civil Engineering')
        civil_modules = [
            'Construction',
            'Building Management',
            'Soil Theory',

        ]

        for module in civil_modules:
            Module.objects.create(name=module, course=civil)


        # EEE
        EEE, created = Course.objects.get_or_create(name='Electrical Engineering')
        EEE_modules = [
            'Control systems',
            'Power Electronics',
            'Transformers',

        ]

        for module in EEE_modules:
            Module.objects.create(name=module, course=EEE)

        # ECE
        ECE, created = Course.objects.get_or_create(name='Electronics Engineering')
        ECE_modules = [
            'Embedded Systems',
            'Digital Signal Processing',
            'RTOS',
            'VLSI',
            'Microcontroller and Architecture 8051'

        ]

        for module in ECE_modules:
            Module.objects.create(name=module, course=ECE)

        # MECH
        Mech, created = Course.objects.get_or_create(name='Mechanical Engineering')
        Mech_modules = [
            'Hydraulics',
            'Engineering Drawing',
            'Material Science'

        ]

        for module in Mech_modules:
            Module.objects.create(name=module, course=Mech)
