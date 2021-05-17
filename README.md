<h1>CalibrationIRT59xx(Lite)</h1>
<h2>Создание протоколов калибровки для ИРТ 5920, ИРТ 5940</h2>
<i>В Lite-версию не включены: 53М, Pt100(W100=1,3850), ТПП(S), ТПР(B), ТВР(A-1), сопротивление(R), напряжение(U100, U75).</i>

<h3>Задачи</h3>

- [X] Основной интерфейс
- [X] Вспомогательный интерфейс
- [X] Интерфейс конфигурации
- [X] Код
- [X] Шаблон
- [X] Тестирование
- [X] Согласовать с метрологами
- [ ] Добавить выгрузку просроченных протоколов из БД

<h3>Файлы, Папки</h3>

- /configurations - папка хранения конфигурации приборов
- /protocols - папка сгенерированных(сохраненных) протоколов
- mainCLBR.py - главное окно программы
- slSettings.py - окно настроек(выходные ячейки xlsx)
- main.py - < pyuic5 main.ui -o main.py > (главное окно программы)
- settings.py - < pyuic5 settings.ui -o settings.py > (окно настроек)
- parameters.ini - параметры состояния программы
- Template_CalibrationIRT59xx.xlsx - шаблон генерирумых протоколов

<h3>Минимальные требования</h3>

python 3.6, windows vista.

<h3>Установка</h3>
<p>Скачать и установить <a href="https://disk.yandex.ru/d/Pd98i-78EYUhjg">WinRAR-SFX(Clbr59xx)</a>  - обновлено 19.02.2021.</p>

<h3>Скрины</h3>

![Image alt](https://github.com/asd192/PyQt_CalibrationIRT59/blob/master/doc/screen1.jpg)
![Image alt](https://github.com/asd192/PyQt_CalibrationIRT59/blob/master/doc/screen3.jpg)
![Image alt](https://github.com/asd192/PyQt_CalibrationIRT59/blob/master/doc/screen2.jpg)




