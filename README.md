# Smart-Dog
Smart-Dog is an innovative online platform designed to help dog owners to get knowledge in canine training. The platform offers content in Ukrainian. Administrators have the ability to create and manage courses, engage with users on forums, and send feedbacks. Meanwhile, users can enroll in courses, share feedback, participate in discussions, and receive personalized support.

# Instructions for the "SmartDog" Information System - Canine School

1. Download the project from the repository.
2. Activate the virtual environment: Ensure that the virtual environment is activated. In the terminal or command prompt, navigate to the project directory and activate the virtual environment:
- On Windows: **ll_env\Scripts\activate**
- On macOS and Linux: **source ll_env/bin/activate**
3. Install Django: After activating the virtual environment, install Django using pip:
- **pip install django**
4. Generate a SECRET_KEY using the terminal by running the following command:
- **python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"**
5. Create secrets.py file in the smart_dog directory where the settings.py file is located:
- **SECRET_KEY = 'YOUR_SECRET_KEY'**
6. Run the development server: Start the Django server to run the project locally:
- **python manage.py runserver**
7. Access the project: Open a web browser and go to the address provided by the development server, usually **http://127.0.0.1:8000/**.
8. Additionally, a superuser has been created, and the administrator interface is accessible at **http://127.0.0.1:8000/admin/**.
