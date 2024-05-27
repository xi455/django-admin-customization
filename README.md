# Django Admin Site Customization

## Want to learn how to build this?

Check out the [post](#).

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment:

    ```sh
    $ python3.11 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

1. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

1. Create a superuser and populate the database:

    ```sh
    (venv)$ python manage.py createsuperuser
    (venv)$ python manage.py populate_db
    ```
	
1. Run the development server:

    ```sh
    (venv)$ python manage.py runserver
    ```
    
1. Your Django admin site should be accessible at [http://localhost:8000/secretadmin/](http://localhost:8000/secretadmin/).

## 所實作的 admin 功能
- Basic Admin Site Customization 基本管理網站自定義

- List Display 控制清單顯示
- List Display Custom Fields 清單顯示自定義欄位

- Link Related Model Objects 連結相關模型物件

- Filter Model Objects 篩選模型物件
- Search Model Objects 搜索模型物件
- Handle Model Inlines 處理模型內聯

- Custom Admin Actions 自訂管理員操作

- Override Django Admin Templates 覆蓋 Django 管理範本
- Style Admin Site with Django Admin Interface 使用 Django 管理介面設置管理網站樣式

- Advanced Search with DjangoQL 使用 DjangoQL 進行高級搜索
- Import and Export Data with Django Import Export 使用 Django Import Export 導入和導出數據