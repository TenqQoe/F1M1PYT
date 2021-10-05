Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> 3*10
30
>>> 100-10
90
>>> 25/5
5.0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> print ('Mijn naam is Tenq')
Mijn naam is Tenq
>>> naam = Tenq
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    naam = Tenq
NameError: name 'Tenq' is not defined
>>> naam = 'Tenq'
>>> print(naam)
Tenq
>>> print(naam.upper())
TENQ
>>> print(naam[0:2])
Te
>>> print(naam[::-1])
qneT
>>> leeftijd = 15
>>> print('Hallo ' + naam + ' ban je al ' +str(leeftijd) + ' jaar?')
Hallo Tenq ban je al 15 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
16
>>> leeftijd = leeftijd -1
>>> leeftijd
15
>>> leeftijd = leeftijd + 1
>>> leeftijd
16
>>> if leeftijd < 18:
	hoelang_tot18 = 18 - leeftijd
	print('Over ' + str(hoelang_tot18) + 'jaar wordt je 18')

	
Over 2jaar wordt je 18
>>> if leeftijd > 18:
	hoelang_al18 = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18) + ' jaar geleden dat je 18 werd ;-)')

	
>>> if leeftijd = 18:
	
SyntaxError: invalid syntax
>>> if leeftijd == 18:
	jebent_18 = 18
	print('Je bent precies ' + str(jebent_18) + ' jaar')

	
>>> from random import randint
>>> randint(0,1000)
197
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
950
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 950
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2021-10-05 12:39:48.658955
>>> datum.strftime('%A %d %B %Y')
'Tuesday 05 October 2021'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'dinsdag 05 oktober 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime(%A %d %B %Y')
	       
SyntaxError: invalid syntax
>>> datum
datetime.datetime(2021, 10, 5, 12, 39, 48, 658955)
>>> datum.strftime('%A %d %B %Y')
'martedì 05 ottobre 2021'
>>> 