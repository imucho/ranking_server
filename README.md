# SGE研修用簡易ランキングサーバ

## 起動方法

```sh
$ docker-compose build server
$ docker-compose up -d
```

## API

### スコア

```sh
GET 0.0.0.0:/score/{score}
```

返すデータ

```js
{
	'ranking': [
		{
			'rank': number,
			'username': string,
			'weight': number,
			'score': number
		},
	],
	'rank': number
}
```

### ランキング

```sh
GET 0.0.0.0:/ranking
```

返すデータ

```js
{
	'ranking': [
		{
			'rank': number,
			'username': string,
			'weight': number,
			'score': number
		},
	],
	'rank': 0
}
```

```sh
POST 0.0.0.0:/ranking
```

受け取るデータ

```js
{
	'username': string,
	'weight': number,
	'score': number
}
```

返すデータ

```js
{
	'ranking': [
		{
			'rank': number,
			'username': string,
			'weight': number,
			'score': number
		},
	],
	'rank': number
}
```