# 🧱 Arquitectura del Proyecto

Este microservicio implementa el patrón **Clean Architecture**, lo cual permite mantener una separación clara entre las capas de dominio, aplicación, infraestructura y presentación.

## 🧩 Estructura de Carpetas

```
NotificationService/
├── domain/         # Entidades y lógica del negocio
├── use_cases/      # Casos de uso (crear, obtener, actualizar)
├── infrastructure/ # Adaptadores a la BD (SQLAlchemy)
├── presentation/   # Rutas de FastAPI
├── tests/          # Pruebas unitarias
├── main.py         # Punto de entrada del sistema
└── requirements.txt
```

## 🔄 Flujo de Datos

1. El usuario envía una solicitud HTTP a un endpoint.
2. La capa de presentación (FastAPI) recibe la solicitud.
3. Se llama al caso de uso correspondiente.
4. El caso de uso utiliza las interfaces definidas en `domain` para acceder al repositorio.
5. La infraestructura implementa esas interfaces para conectarse a la base de datos.
6. Se retorna la respuesta al cliente.

## ⚙️ Principios aplicados

- **Dependency Inversion**: las capas internas no dependen de las externas.
- **Separation of Concerns**: cada módulo tiene una responsabilidad clara.
- **Testabilidad**: los casos de uso se pueden probar de forma aislada.