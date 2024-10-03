### План тестирования

| Название                      | Описание                                                                                                                                                                   | Тип теста       | Входные данные                             | Ожидаемый результат                       |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------------------------------------------|-------------------------------------------|
| test_positive_discr           | Проверяет, что функция solve_quadratic_equation возвращает список с двумя корнями уравнения при положительном дискриминанте.                                               | позитивный      | a = 1<br/> b = -4<br/>  c = -5             | \[5.0, -1.0]                              |
| test_zero_discr               | Проверяет, что функция solve_quadratic_equation возвращает список с одним корнем уравнения при дискриминанте = 0.                                                          | позитивный      | a = 2<br/>b = -4<br/>  c = 2               | \[1.0]                                    |
| test_negative_discr           | Проверяет, что функция solve_quadratic_equation возвращает сообщение "корней нет" при отрицательном дискриминанте.                                                         | позитивный      | a = 2<br/> b = -1<br/> c = 1               | \["корней нет"]                           |
| test_zero_a                   | Проверяет, что функция solve_quadratic_equation возвращает список с одним корнем при a = 0.                                                                                | позитивный      | a = 0<br/> b = 2<br/> c = -4               | \[2.0]                                    |
| test_incorrect_arguments_type | Проверяет, что функция solve_quadratic_equation возвращает сообщение об ошибке "введены неверные параметры функции", если хотя бы один из параметров не является числовым. | негативный      | a = "hello"<br/> b = 2<br/> c = -4         | \["введены неверные параметры функци"]    |
| test_less_number_of_arguments | Проверяет, что функция solve_quadratic_equation возвращает сообщение об ошибке "введены неверные параметры функции", если в функцию переданы не все аргументы.             | негативный      | b = 2<br/> c = -4                          | \["введены неверные параметры функци"]    |
| test_more_number_of_arguments | Проверяет, что функция solve_quadratic_equation возвращает сообщение об ошибке "введены неверные параметры функции", если в функцию передано больше трех аргументов.       | негативный      | a = 2<br/>b = -4<br/>  c = 2  <br/> dicr=0 |    \["введены неверные параметры функци"] |
