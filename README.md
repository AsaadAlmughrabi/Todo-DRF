# Todo-DRF Project Guide

## Permissions

Permissions determine whether a request should be granted or denied access. There are three levels of permissions:

1. **Project Level**
2. **Model Level**
3. **Object Level**

### Adding Permissions to Your Project

To add permissions, import the desired permissions in your views:

```python
from rest_framework.permissions import AllowAny
```

Or, if you have custom permissions, import them from your permissions file.

In your view, add the following line to specify the permissions:

```python
permission_classes = [AllowAny]
```

For custom permissions, create a class in your permissions file.

## Connecting to PostgreSQL using Django

### Steps:

1. **Add Dockerfile**: Create a `Dockerfile` for your project.
2. **Add Docker Compose**: Create a `docker-compose.yml` file.
3. **Update Settings**: Change the default database in `settings.py` to use PostgreSQL.
4. **Install psycopg2-binary**: Install this package for PostgreSQL database connectivity.
5. **Docker Compose Configuration**: In the `docker-compose.yml` file, add the database configuration and environment variables.

Example `docker-compose.yml`:

```yaml
version: "3.9"

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
```

### Making Migrations

Use the following command to make migrations and apply them:

```sh
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Full Command Sequence

1. **Stop any running containers**:

   ```sh
   docker-compose down
   ```

2. **Build and start services**:

   ```sh
   docker-compose up --build -d
   ```

3. **Make migrations**:

   ```sh
   docker-compose exec web python manage.py makemigrations
   ```

4. **Apply migrations**:

   ```sh
   docker-compose exec web python manage.py migrate
   ```

5. **Check if containers are running**:

   ```sh
   docker ps
   ```

6. **Check logs for any errors**:

   ```sh
   docker-compose logs web
   ```

7. **Test network connectivity from within the container**:
   ```sh
   docker-compose exec web curl http://127.0.0.1:8000
   ```

By following these steps, you should have a well-configured Django project with PostgreSQL as the database, running smoothly in Docker.



### Steps to Handle JWT in Django:

1. **Install the JWT Library:**

   Install the `djangorestframework-simplejwt` library, which allows you to create, refresh, and verify tokens.

   ```bash
   pip install djangorestframework-simplejwt
   ```

2. **Configure `settings.py`:**

   In your `settings.py` file, update the REST framework settings to use JWT authentication:

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_PERMISSION_CLASSES': [
           'rest_framework.permissions.AllowAny',
       ],
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework_simplejwt.authentication.JWTAuthentication',
           'rest_framework.authentication.SessionAuthentication',
           'rest_framework.authentication.BasicAuthentication',
       ],
   }
   ```

   - **`DEFAULT_PERMISSION_CLASSES`**: Sets the default permissions for your API.
   - **`DEFAULT_AUTHENTICATION_CLASSES`**: Configures the authentication methods, including JWT.

3. **Add JWT Routes in `urls.py`:**

   In your project's `urls.py`, add routes to handle token creation and refresh:

   ```python
   from django.urls import path
   from rest_framework_simplejwt import views as jwt_views

   urlpatterns = [
       path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   ]
   ```

   - **`TokenObtainPairView`**: Generates a new token.
   - **`TokenRefreshView`**: Refreshes an existing token.




