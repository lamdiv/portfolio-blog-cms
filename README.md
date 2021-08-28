# portfolio

This is the personal website with ability to add projects and create blogs with search functionality.

## Setup Process

**Requirements** 
- pip
- venv 

**Some Required Changes**
            
Find ```settings.py``` in ```project/protfolio``` folder and add Email and Password of your Gmail account. Enable the less secure application feature in your google account. This account will send you the email when people try to contact you.

```bash
EMAIL_HOST_USER = "your email"
EMAIL_HOST_PASSWORD = "your password"
```
Now, find ```views.py``` in ```project/home``` folder and add another email account. This account will receive the email sent by your previous account.

```bash
send_mail(f'{name} sent mail through lamdiv',
                      f'{message}\n\nname: {name} \nemail: {email}',
                      settings.EMAIL_HOST_USER,
                      ['your email'],fail_silently=False)
```


**Commands**

```bash
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```
Now virtual environment is created and all the dependencies are installed.

Run ```python manage.py migrate``` to create database table and create superuser by ```python manage.py createsuperuser```.



## License
[MIT](https://choosealicense.com/licenses/mit/)
