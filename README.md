# SGE研修用簡易ランキングサーバ

## 起動方法

```sh
$ docker-compose build server
$ docker-compose up -d
```

## API

### ログイン
```sh
POST 0.0.0.0:8000/login
```

受け取るデータ

```js
{
	"username": "hoge",
	"password": "foo"
}
```

返すデータ

```js
{
	"token": "hogehoge"
}
```

### ランキング

```sh
GET 0.0.0.0:8000/ranking
```

返すデータ

```js
[
	{
		"username": "hoge",
		"score": 100
	},
	{
		"username": "foo",
		"score": 90
	}
]
```

```sh
POST 0.0.0.0:8000/ranking
```

受け取るデータ

```js
{
	"token": "hogehoge",
	"score": 100
}
```

返すデータ

```js
{
	"username": "hoge",
	"score": 100,
	"rank": 1,
	"ranking": [
		{
			"username": "hoge",
			"score": 100
		},
		{
			"username": "foo",
			"score": 90
		}
	]
}
```