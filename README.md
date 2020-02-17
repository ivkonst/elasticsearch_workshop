# elasticsearch_workshop

---

#### Предварительная установка ПО

1. Скачать и установить [JDK](https://www.oracle.com/technetwork/java/javase/downloads/index.html)
    * Для macOS (например) - `dmg`
    * Проверить успешную установку
        ```
        java --version
        ```
    
2. Скачать и установить [Elasticsearch](https://www.elastic.co/downloads/elasticsearch)
    * Для macOS (например)
        ```
        brew tap elastic/tap
        brew install elastic/tap/elasticsearch-full
        ```
    * Проверить успешную установку
        ```
        elasticsearch --version
        ```
    * Поднять Elasticsearch  
        ```
        elasticsearch
        ```

---

#### Семинар

1. Виртуальное окружение, юпитер
    ```
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ipython kernel install --user --name=ws_elastic
    jupyter-lab
    ```

2. [Семинар](ws_elastic.ipynb)

---
