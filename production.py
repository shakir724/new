import os

val = 'Y'

while True:
  val = input('Do You Want To Build React With Django?(Y|N) : ')
  if val in ('y', 'n', 'Y', 'N'):
    if val in ('y', 'Y'):
      val = input('Do You Want A Full Reset Including Migration Files?(Y|N) : ')  
      if val in ('Y', 'y'):
        os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
        os.system('find . -path "*/migrations/*.pyc"  -delete')
        print('Migration Cleared')

      os.remove('mydatabase')
      print('Database Deleted')

      os.system('python manage.py makemigrations')
      print('New Migrations Made')

      os.system('python manage.py migrate')
      print('Migrations Done')

      import shutil
      shutil.rmtree('media')

    break

  else:
    print('Enter Valid Input')

os.chdir(os.path.join(os.getcwd(), 'reactify-ui'))
os.system('npm run collect')
print('Build Finished')