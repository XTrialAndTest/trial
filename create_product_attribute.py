
from oscar.apps.catalogue.models import *



attributes={
    'Mattress_Make':['Plain','Quilted'],
    'Carpet_Make':['Shaggy','Silk'],
    "Mattress_Size":['3x6','3.5x6','4x6','4.5x6','5x6','6x6',],
    "Carpet_Size":['4x6','5x8','6x9','7x10','8x11'],
    "Thickness":['6 inches','8 inches','10 inches','12 inches'],
    # "colour":['white']
}

for key,value in attributes.items():
    # p, created = Person.objects.get_or_create(
    group,a=AttributeOptionGroup.objects.get_or_create(name=key)
#     # a=AttributeOptionGroup.objects.filter(name=x).delete()
#     c=AttributeOptionGroup.objects.all().count()
    print('```````````````````',group,a)
    
    for opt in value:
#         # print(x, [i])
#         print("================================================================",a,c)
        attr,d=AttributeOption.objects.get_or_create(group=group,option=opt)
#         # AttributeOption.objects.create(name=x)
        print('888888888888',attr,d)




r=AttributeOption.objects.all().count()
print(r)

# b=AttributeOption.objects.all()
# print(b)
# list= ['Make','Size','Thickness','Colour']


# for i in list :
#     i=AttributeOptionGroup.objects.create(name=i)
