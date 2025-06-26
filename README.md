# NotificationService

## Descripción

NotificationService es un microservicio básico que implementa un sistema de notificaciones utilizando los principios de Clean Architecture. Este servicio permite crear notificaciones, obtener notificaciones por usuario y marcar notificaciones como leídas.

## Estructura del Proyecto

```
NotificationService
├── app
│   ├── domain
│   │   ├── entities.py          # Define la entidad Notification
│   │   └── repositories.py      # Define la interfaz NotificationRepository
│   ├── infrastructure
│   │   ├── database.py          # Configura la base de datos SQLite
│   │   └── repositories.py      # Implementa NotificationRepository
│   ├── presentation
│   │   ├── api.py               # Define los endpoints de la API REST
│   │   └── schemas.py           # Define los modelos de Pydantic
│   ├── use_cases
│   │   ├── create_notification.py # Lógica para crear notificaciones
│   │   ├── get_notifications.py   # Lógica para obtener notificaciones
│   │   └── mark_as_read.py        # Lógica para marcar notificaciones como leídas
│   └── main.py                   # Punto de entrada de la aplicación
├── tests
│   ├── test_api.py               # Pruebas unitarias para los endpoints de la API
│   └── __init__.py               # Marca el directorio de pruebas como un paquete
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Documentación del proyecto
```

## Requisitos

- Python 3.8 o superior
- SQLite

## Instalación

1. Clona el repositorio:

   ```
   git clone <URL_DEL_REPOSITORIO>
   cd NotificationService
   ```

2. Instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar el servicio, utiliza el siguiente comando:

```
python app/main.py
```

La API estará disponible en `http://localhost:8000`.

## Endpoints

- `POST /notifications`: Crear una nueva notificación.
- `GET /notifications/{user_id}`: Obtener notificaciones por usuario.
- `PUT /notifications/{id}/read`: Marcar una notificación como leída.
- `GET /health`: Verificar el estado del servicio.

## Pruebas

Para ejecutar las pruebas, utiliza el siguiente comando:

```
pytest tests/
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o un pull request.