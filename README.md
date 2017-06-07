# SGE研修用簡易ランキングサーバ

## 起動方法

```sh
$ docker-compose up -d
$ pip install -r requirements.txt
$ gunicorn api:api
```