
#we have 3 sides of triangle. #is it triangle?
#find sqrt of triangle.
#if it's not a triangle - msg wrong data
#area of triangle = (p(p-a)(p-b)(p-c))**(0.5)
#p=(a+b+c)/2
side1=int(input('Input side 1:'))
side2=int(input('Input side 2:'))
side3=int(input('Input side 3:'))
if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side2) > side1:
    poluperimetr=(side1+side2+side3)/2
    area_triangle= (poluperimetr*(poluperimetr-side1)*(poluperimetr-side2)*(poluperimetr-side3))**(1/2)
    print('It is a triangle, are of triangle = {}'.format(int(area_triangle)))
else:
    print('wrong data')
