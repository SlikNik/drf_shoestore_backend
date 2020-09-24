from shoe.models import ShoeColor, ShoeType
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create Type and Color tables'

    def handle(self, *args, **kwargs):
        try:
            ShoeType.objects.create(style='sneaker')
            ShoeType.objects.create(style='boot')
            ShoeType.objects.create(style='sandal')
            ShoeType.objects.create(style='dress')
            ShoeType.objects.create(style='other')
            ShoeColor.objects.create(color_name='Black')
            ShoeColor.objects.create(color_name='Red')
            ShoeColor.objects.create(color_name='Orange')
            ShoeColor.objects.create(color_name='Yellow')
            ShoeColor.objects.create(color_name='Green')
            ShoeColor.objects.create(color_name='Blue')
            ShoeColor.objects.create(color_name='Indigo')
            ShoeColor.objects.create(color_name='Violet')
            ShoeColor.objects.create(color_name='White')
            self.stdout.write(self.style.SUCCESS('Types and Colors populated with success!'))
        except ShoeType.DoesNotExist or ShoeColor.DoesNotExist:
            self.stdout.write(self.style.WARNING('Error in populating!'))
        

# class Command(BaseCommand):
#     help = 'Create random users'

#     def add_arguments(self, parser):
#         parser.add_argument('-types', type=str, help='Indicates the type to create')
#         parser.add_argument('-color', type=str, help='Indicates the color to be created')

#     def handle(self, *args, **kwargs):
#         types = kwargs['types']
#         color = kwargs['color']
#         if types:
#             style = types
#             ShoeType.objects.create(style=style)
#         if color:
#             color_name = color
#             ShoeColor.objects.create(color_name=color_name)