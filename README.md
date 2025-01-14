# Mock Realtor Website

Fang Realtors is a dynamic, full-stack web application developed by myself and three other teammates at University of South Florida for our senior project.

## Description

This Mock Realtor Website simulates the functionalities of a real estate platform, offering users the ability to browse and search for properties using advanced filters. Built using Python and Django, the application integrates frontend, backend, and database components to provide a comprehensive demonstration of real-world development skills. It showcases my ability to learn and apply new technologies, troubleshoot deployment issues, deliver a fully functional web application, and collaborate effectively with a team to achieve project goals.

## Getting Started

### Dependencies

* Python 3.9+
* Django 3.2+
* MySQL 8.0+
* Operating System: Windows 10 or equivalent
* Libraries listed in requirements.txt

### Installing

1. Clone the repository:
```
git clone https://github.com/dmonterohub/Fang-Realtors.git
```
2. Navigate to the project directory:
```
cd Fang-Realtors
```
3. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
5. Install dependencies:
```
pip install -r requirements.txt
```
6. Configure your database connection in settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
7. Run database migrations:
```
python manage.py migrate
```

### Executing program

1. Start the development server:
```
python manage.py runserver
```
2. Open your browser and visit:
```
http://127.0.0.1:8000
```

## Help
If you encounter issues, consider the following:
* Ensure all dependencies are installed correctly.
* Verify your database credentials in settings.py.
* Check for any missing migrations with:
```
python manage.py makemigrations
```

For further assistance, open an issue in this repository.

## Authors

Myself:
* Daniel Montero | dmontero0110@outlook.com

My Teammates:
* Vincent Stankard
* Nicholas Prawl
* Randall MacDonald

## Version History

* 0.2
    * Deployment for personal portfolio purposes
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Project Completion

## License

This project is intended for educational purposes only. The code is provided as-is to showcase my development skills and is not licensed for commercial use or redistribution.

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
