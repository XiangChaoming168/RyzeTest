import time
from app import app1


@app1.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app1.run(debug=True, port=9090)
    # from app.model import db
    # db.create_all()

    # from app.model import db
    # with app1.app_context():
    #     # 删除所有继承自db.Model的表
    #     db.drop_all()
    #     # 创建所有继承自db.Model的表
    #     db.create_all()
