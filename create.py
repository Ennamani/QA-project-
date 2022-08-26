
from schema import *


d.create_all()
#
# ###############################
#
c1 = Colleges(college_id=1,college_name='Oxford',address='UK',director_name='John')
d.session.add(c1)
c2 = Colleges(college_id=2,college_name='Stanford',address='US',director_name='Jane')
d.session.add(c2)
c3 = Colleges(college_id=3,college_name='Barcelona',address='ES',director_name='Xavi')
d.session.add(c3)
c4 = Colleges(college_id=4,college_name='Paris',address='FR',director_name='Paul')
d.session.add(c4)
c5 = Colleges(college_id=5,college_name='Munich',address='GER',director_name='Robert')
d.session.add(c5)
#
# d.session.commit()
#
# p1 = Programs(program_id=1,program_name='Azure Cloud',fees=54545454,college_id=1)
# d.session.add(p1)
# p2 = Programs(program_id=2,program_name='Python',fees=3343434,college_id=2)
# d.session.add(p2)
# p3 = Programs(program_id=3,program_name='HTML',fees=7777777,college_id=3)
# d.session.add(p3)
# p4 = Programs(program_id=4,program_name='Flask',fees=756566,college_id=4)
# d.session.add(p4)
# p5 = Programs(program_id=5,program_name='AWS Cloud',fees=4353252,college_id=5)
# d.session.add(p5)
# p6 = Programs(program_id=6,program_name='Java',fees=435345,college_id=1)
# d.session.add(p6)
# p7 = Programs(program_id=7,program_name='C#',fees=12132,college_id=2)
# d.session.add(p7)
# p8 = Programs(program_id=8,program_name='C++',fees=87131,college_id=3)
# d.session.add(p8)
# p9 = Programs(program_id=9,program_name='Machine Learning',fees=71226,college_id=4)
# d.session.add(p9)
# p10 = Programs(program_id=10,program_name='Security',fees=82131927,college_id=5)
# d.session.add(p10)
# p11 = Programs(program_id=11,program_name='Hardware',fees=189,college_id=1)
# d.session.add(p11)
# p12 = Programs(program_id=12,program_name='Networking',fees=92310,college_id=2)
# d.session.add(p12)
# p13 = Programs(program_id=13,program_name='SQL',fees=9140342,college_id=3)
# d.session.add(p13)
# p14 = Programs(program_id=14,program_name='Google Cloud',fees=29074171049,college_id=4)
# d.session.add(p14)
#
# d.session.commit()
#
# s1 = Students(student_id=1,student_name='Mohamed',student_email='mo@gmail.com',program_id=1)
# d.session.add(s1)
# s2 = Students(student_id=2,student_name='Abdi',student_email='abdi@gmail.com',program_id=2)
# d.session.add(s2)
# s3 = Students(student_id=3,student_name='Saka',student_email='saka@gmail.com',program_id=3)
# d.session.add(s3)
# s4 = Students(student_id=4,student_name='Gabi',student_email='Gabi@gmail.com',program_id=4)
# d.session.add(s4)
# s5 = Students(student_id=5,student_name='Ben',student_email='Ben@gmail.com',program_id=5)
# d.session.add(s5)
# s6 = Students(student_id=6,student_name='Aaron',student_email='aaron@gmail.com',program_id=6)
# d.session.add(s6)
# s7 = Students(student_id=7,student_name='Granit',student_email='granit@gmail.com',program_id=7)
# d.session.add(s7)
# s8 = Students(student_id=8,student_name='Martin',student_email='martin@gmail.com',program_id=8)
# d.session.add(s8)
# s9 = Students(student_id=9,student_name='Nico',student_email='nico@gmail.com',program_id=9)
# d.session.add(s9)
# s10 = Students(student_id=10,student_name='Nuno',student_email='nuno@gmail.com',program_id=10)
# d.session.add(s10)
# s11 = Students(student_id=11,student_name='Thomas',student_email='thomas@gmail.com',program_id=11)
# d.session.add(s11)
# s12 = Students(student_id=12,student_name='Rob',student_email='rob@gmail.com',program_id=12)
# d.session.add(s12)
# s13 = Students(student_id=13,student_name='Will',student_email='will@gmail.com',program_id=12)
# d.session.add(s13)
# s14 = Students(student_id=14,student_name='Tomi',student_email='tomi@gmail.com',program_id=13)
# d.session.add(s14)
#
#
# d.session.commit()
#
# ###################################
#
# for clg in Colleges.query.all():
#     print("- ",clg.college_name)
#     for program in clg.programs:
#         print("\t - ",program.program_name)