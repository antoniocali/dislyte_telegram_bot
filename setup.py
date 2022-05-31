from setuptools import setup, find_packages

setup(
    name='DislyteTelegramBot',
    version='0.1',
    packages=[''],
    url='https://github.com/antoniocali/dislyte_telegram_bot',
    author='antoniodavidecali',
    author_email='antoniodavidecali@gmail.com',
    description='Dislyte Telegram Bot',
    package=find_packages(),
    install_requires=["easyocr", "python-telegram-bot>=20.0a0", "dynaconf", "markdown"]
)
