print "Please enter the number for the month in which you were born\n"
print "March = 1\nApril = 2\nMay = 3\nJune = 4\nJuly = 5\nAugust = 6"
print "September = 7\nOctober = 8\nNovember = 9\nDecember = 10\nJanuary = 11\nFebruary = 12"
A = raw_input ('Which number fits your month? ')
B = raw_input ('Please enter the day of the month on which you were born eg, 31, 25, etc.: ')
C = raw_input ('Please enter the year of the century. For example enter 89 if you were born in 1989: ')
D = raw_input ('Please enter the century. For instance, enter 19 if you were born in 1986: ')
A = int(A)
B = int(B)
C = int(C)
D = int(D)
if B==11 or B==12:
    C = C-1
W = (13*A-1)/5
X = C/4
Y = D/4
Z = W + X + Y + B + C - 2*D
R = Z%7
if R == 0:
    day = 'Sunday'
elif R == 1:
    day = 'Monday'
elif R == 2:
    day = 'Tuesday'
elif R == 3:
    day = 'Wednesday'
elif R == 4:
    day = 'Thursday'
elif R == 5:
    day = 'Friday'
elif R == 6:
    day = 'Saturday'
print 'You were born on a',day
