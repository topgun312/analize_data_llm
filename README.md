# ИНСТРУКЦИЯ ПО РАБОТЕ СКРИПТА
## Чтобы скачать данные из указанного URL на Kaggle, вам нужно учесть, что Kaggle требует аутентификации для доступа к своим наборам данных. Это означает, что вам нужно использовать API Kaggle или выполнить некоторые шаги для загрузки данных вручную.

### Способ 1: Использование API Kaggle. Создание учетной записи Kaggle: Если у вас еще нет учетной записи на Kaggle, создайте ее.

#### Получение API токена:
- Перейдите в свой профиль на Kaggle и выберите "Account".
- Прокрутите вниз до раздела "API" и нажмите "Create New API Token". Это загрузит файл kaggle.json, который содержит ваш API ключ.
- Установка Kaggle API:
- Убедитесь, что у вас установлен kaggle: uv add kaggle

#### Настройка API:
- Поместите файл kaggle.json в папку ~/.kaggle/ (на Linux или macOS) или C:\Users\<YourUsername>\.kaggle\ (на Windows). 
- Выполните следующую команду для создания папки .kaggle в вашем домашнем каталоге: ```mkdir -p ~/.kaggle```
- Выполните следующую команду, чтобы переместить файл из каталога куда скачали файл kaggle.json: ```mv kaggle.json ~/.kaggle/```
- Чтобы убедиться, что файл был перемещен успешно, вы можете выполнить следующую команду: ```ls -a ~/.kaggle```
- Убедитесь, что у файла есть правильные разрешения: ```chmod 600 ~/.kaggle/kaggle.json```

#### Скачивание данных:
1. Через консоль:
 - Теперь вы можете использовать команду Kaggle API для скачивания данных. Откройте терминал и выполните следующую команду: ```kaggle datasets download -d shohinurpervezshohan/freelancer-earnings-and-job-trends```
 - Это скачает ZIP-файл с набором данных в текущую директорию.
 - После скачивания распакуйте ZIP-файл: ```unzip freelancer-earnings-and-job-trends.zip```

2. Через наш скрипт после запуска.


### Запустить скрипт в терминале
1. Запустить командой ```python main.py```
2. Выбрать пункт 1 скачивания zip каталога и его распаковка в файл формата .csv
3. Выбрать пункт 2 для создания базы данных и таблицы (postgresql)
4. Выбрать пункт 3 для миграции данных c файла .csv в таблицу БД
5. Выбрать пункт 4 для дальнейших запросов
- Первые 3 пункты выполнить только 1 раз в начале работы, далее только работать с запросами

#### Основные библиотеки для работы
- "aiofiles>=24.1.0",
- "aiohttp>=3.11.18",
- "asyncpg>=0.30.0",
- "black>=25.1.0",
- "gigachat>=0.1.39.post1",
- "isort>=6.0.1",
- "kaggle>=1.7.4.5",
- "loguru>=0.7.3",
- "pandas>=2.2.3",
- "python-dotenv>=1.1.0",
- "sqlalchemy>=2.0.41",

#### Примеры запросов к Gigachat
1. Насколько выше доход у фрилансеров, принимающих оплату в криптовалюте, по сравнению с другими способами оплаты?
2. Как распределяется доход фрилансеров в зависимости от региона проживания?
3. Какой процент фрилансеров, считающих себя экспертами, выполнил менее 100 проектов?
4. Как влияет уровень опыта фрилансеров на их доход?
5. Какой средний рейтинг клиентов у фрилансеров с различными методами оплаты?