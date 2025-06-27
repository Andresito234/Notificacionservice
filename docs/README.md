# 📬 NotificationService

NotificationService es un microservicio diseñado bajo el patrón de Clean Architecture que permite crear, listar y actualizar notificaciones para usuarios. Está construido con FastAPI y utiliza SQLite como base de datos.

## 🚀 Características

- Crear notificaciones
- Obtener notificaciones por `user_id`
- Marcar notificaciones como leídas
- Estructura limpia y escalable (Clean Architecture)

## 🧱 Tecnologías

- Python 3.11
- FastAPI
- Pydantic v2
- SQLAlchemy
- SQLite
- Docker

## 📦 Instalación

```bash
git clone https://github.com/tuusuario/NotificationService.git
cd NotificationService
pip install -r requirements.txt
uvicorn main:app --reload
```

## 📬 Endpoints

| Método | Ruta                    | Descripción                   |
|--------|-------------------------|-------------------------------|
| POST   | /notifications/         | Crear nueva notificación      |
| GET    | /notifications/{user_id}| Listar notificaciones por usuario |
| PUT    | /notifications/{id}/read | Marcar notificación como leída |

## 🧪 Pruebas

```bash
pytest
```

## 🐳 Docker

```bash
docker build -t notification-service .
docker run -p 8000:8000 notification-service
```