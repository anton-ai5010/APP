# Invasion Universe MVP

Мультиплатформенное приложение для премиального киберспортивного клуба с системой бронирования, лояльности и турнирами.

## Структура проекта

```
invasion_universe_mvp/
├── mobile/                 # Flutter приложение (iOS/Android)
├── backend/               # FastAPI backend
├── infra/                 # Инфраструктура (Docker, Nginx, мониторинг)
├── docs/                  # Документация
└── .github/workflows/     # CI/CD
```

## Технологический стек

### Mobile
- Flutter 3.x с Riverpod для state management
- go_router для навигации
- Dio + Retrofit для API
- Hive для локального хранилища
- Firebase для push-уведомлений и аналитики

### Backend
- FastAPI (Python 3.11+)
- PostgreSQL 15 + SQLAlchemy 2.0
- Redis для кеширования и блокировок
- Celery для асинхронных задач
- JWT аутентификация

### Инфраструктура
- Docker + Docker Compose
- Nginx для reverse proxy
- Prometheus + Grafana для мониторинга
- GitHub Actions для CI/CD

## Быстрый старт

### Backend (Development)
```bash
cd backend
docker compose up --build
```
API будет доступен на http://localhost:8000 (документация: /docs)

### Mobile
```bash
cd mobile
flutter pub get
flutter run
```

## Основные функции MVP

1. **Аутентификация**: Регистрация/вход по email/телефону
2. **Бронирование**: Интерактивная карта зала, выбор мест и времени
3. **Платежи**: Интеграция с платежным шлюзом
4. **Лояльность**: Система баллов и уровней
5. **Турниры**: Регистрация и просмотр событий
6. **Push-уведомления**: Транзакционные и маркетинговые
7. **Контент**: Новости, меню бара
8. **Поддержка**: Система тикетов

## Документация

- [API Reference](docs/api.md)
- [Mobile Architecture](docs/mobile-architecture.md)
- [Deployment Guide](docs/deployment.md)
- [Security Guidelines](docs/security.md)

## Лицензия

Proprietary - Invasion Universe © 2025# APP
