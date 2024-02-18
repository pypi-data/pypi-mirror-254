import setuptools


# Определение requests как requirements для того, чтобы этот пакет работал. Зависимости проекта.
# requirements = ["requests<=2.21.0"]

# Функция, которая принимает несколько аргументов. Она присваивает эти значения пакету.
setuptools.setup(
    # Имя дистрибутива пакета. Оно должно быть уникальным, поэтому добавление вашего имени пользователя в конце является обычным делом.
    name="cas_tg",
    # Номер версии вашего пакета. Обычно используется семантическое управление версиями.
    version="0.0.7",
    # Имя автора.
    author="wispace",
    # Его почта.
    author_email="wiforumit@gmail.com",
    # Краткое описание, которое будет показано на странице PyPi.
    description="Checking if user banned by CAS (Combot Anti-Spam System)",
    # Длинное описание, которое будет отображаться на странице PyPi. Использует README.md репозитория для заполнения.
    long_description="""
check(id: str|int) -> bool
Check if a user banned by CAS (Combot Anti-Spam System).

- Args:
    - id (str | int): The user ID to be checked.

- Returns:
    - bool: Returns True if the user is banned or False if the user is not banned.

---

get_messages(id) -> dict[str, list, str]
Check information about user.
- Args:
    - id (str | int): The user ID to be checked.
- Returns:
    - dict[str, list, str]: Returns the number of spam messages, messages, and the time of the ban. If there is no user in ban, returns None.
""",
    # Определяет тип контента, используемый в long_description.
    long_description_content_type="text/markdown",
    # URL-адрес, представляющий домашнюю страницу проекта. Большинство проектов ссылаются на репозиторий.
    url="https://wispace.ru/",
    # Находит все пакеты внутри проекта и объединяет их в дистрибутив.
    packages=setuptools.find_packages(),
    # requirements или dependencies, которые будут установлены вместе с пакетом, когда пользователь установит его через pip.
    # install_requires=requirements,
    # Предоставляет pip некоторые метаданные о пакете. Также отображается на странице PyPi.
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Требуемая версия Python.
    python_requires='>=3.6',
)