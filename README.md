Хорошо, вот дополненное описание проекта:

# Village Mystery

Это консольная игра, в которой игрок играет роль детектива, расследующего дело об убийстве мирных жителей в деревне. Игрок должен перемещаться по разным локациям, задавать вопросы персонажам и собирать улики, чтобы раскрыть преступление.

## Инструкции по запуску

Для запуска игры необходимо иметь установленный Python 3.6 или более поздней версии. Для запуска игры выполните следующие действия:

1. Склонируйте репозиторий с помощью команды:

git clone https://github.com/GoldenEagle74/Game.git

2. Перейдите в папку с проектом:

cd Game

3. Запустите игру:

python main.py

## Игровой процесс

Игроку нужно перемещаться между различными локациями, говорить с персонажами и собирать улики. В некоторых локациях игрок может выбирать, как поступить дальше, и от этих выборов зависит, сможет ли игрок решить преступление.

В процессе игры игрок должен следить за инвентарём, где хранятся все собранные улики и документы.

## Использованные методы

Для создания игры были использованы следующие методы:

- ООП: вся игра была создана с помощью объектно-ориентированного подхода, каждый персонаж и локация являются объектами, а действия игрока вызывают соответствующие методы у объектов.
- Карты: карта деревни была создана с помощью словаря, где ключами являются названия локаций, а значениями - список связанных локаций.
- Регулярные выражения: для анализа ввода игрока были использованы регулярные выражения, чтобы определить, какой метод нужно вызвать у текущего объекта.
- Исключения: для обработки ошибок и неправильного ввода игрока были использованы исключения.

## Контрибуция

Если вы хотите внести свой вклад в проект, вы можете создать pull request в этот репозиторий. Мы рассмотрим все предложения по улучшению игры.
