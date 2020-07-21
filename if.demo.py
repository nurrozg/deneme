email = 'sedanur@gmail.com'
password = '12345'

girilenEmail = input('email: ')
girilenPassword = input('password: ')

if (girilenEmail==email):
    if(girilenPassword==password):
        print('uygulamaya giriş başarılı ')
    else:
        print('password yanlış')
else:
    print('email yanlış ')        

