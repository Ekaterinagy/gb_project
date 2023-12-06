## Урок 2. Кроссбраузерное тестирование с Selenium WebDriver

### Задание 2

Условие: Добавить в наш тестовый проект шаг добавления поста после входа. Должна выполняться проверка на наличие названия поста на странице сразу после его создания.

Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.

Что ещё можно почитать:
• Начинаем работать с Selenium в Python

Решение:


```python
def test_step3(site, log_xpath, pass_xpath, btn_xpath, btn_create_post,
               btn_save_post, tittle_post_xpath, description_post_xpath,
               content_post_xpath, tittle_save_post):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    time.sleep(testdata["sleep_time"])
    btn_create = site.find_element("xpath", btn_create_post)
    btn_create.click()
    time.sleep(testdata["sleep_time"])
    input1 = site.find_element("xpath", tittle_post_xpath)
    input1.send_keys('Котики')
    input2 = site.find_element("xpath", description_post_xpath)
    input2.send_keys('Самые милые существа')
    input2 = site.find_element("xpath", content_post_xpath)
    input2.send_keys('Котики самые милые существа на земле')
    btn_post = site.find_element("xpath", btn_save_post)
    btn_post.click()
    time.sleep(testdata["sleep_time"])
    result = site.find_element("xpath", tittle_save_post)
    assert result.text == "Котики"
```

```commandline
Testing started at 15:41 ...

============================= test session starts =============================
collecting ... collected 3 items

test_1.py::test_step1 PASSED                                             [ 33%]
test_1.py::test_step2 PASSED                                             [ 66%]
test_1.py::test_step3 PASSED                                             [100%]

============================= 3 passed in 29.48s ==============================

Process finished with exit code 0
```