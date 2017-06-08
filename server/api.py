import redis
import falcon
import hashlib
import json
r = redis.Redis(host='db', port=6379, db=0)

class LogInResource:
    def on_post(self, req, res):
        post_data = json.loads(req.stream.read().decode('utf-8'))
        username = post_data['username']
        password = post_data['password']
        if username is None or password is None:
            res.status = falcon.HTTP_400
        else:
            if r.hexists("username", username):
                """ユーザが存在する時"""
                hash_password = r.hget("user", username)
                if hash_password is hashlib.sha224(password.encode("utf-8")).hexdigest():
                    hash_auth = hashlib.sha224((username + password).encode("utf-8")).hexdigest()
                    res.status = falcon.HTTP_200
                    res.body = json.dumps({"token": hash_auth})
                else:
                    res.status = falcon.HTTP_401
            else:
                """ユーザが存在しない時"""
                hash_password = hashlib.sha224(password.encode("utf-8")).hexdigest()
                r.hset("user", username, hash_password)
                hash_auth = hashlib.sha224((username + password).encode("utf-8")).hexdigest()
                r.hset("auth", hash_auth, username)
                res.status = falcon.HTTP_201
                res.body = json.dumps({"token": hash_auth})

class RankingResource:
    def on_get(self, req, res):
        ranking = r.zrange("ranking", 0, 99, desc=True, withscores=True)
        dict_ranking = [{"username": k.decode('utf-8'), "score": v} for (k, v) in ranking]
        res.status = falcon.HTTP_200
        res.body = json.dumps(dict_ranking)

    def on_post(self, req, res):
        post_data = json.loads(req.stream.read().decode('utf-8'))
        token = post_data['token']
        if token is None:
            res.status = falcon.HTTP_401
            res.body = "" 
        else:
            username = r.hget("auth", token)
            if username is None:
                res.status = falcon.HTTP_401
                res.body = "" 
            else:
                score = post_data['score']
                r.zadd("ranking", username, score)
                ranking = r.zrange("ranking", 0, 99, desc=True, withscores=True)
                res.status = falcon.HTTP_201
                dict_ranking = [{"username": k.decode('utf-8'), "score": v} for (k, v) in ranking]
                user_rank = r.zrevrank("ranking", username) + 1
                return_data = {"username": username.decode('utf-8'), "score": score, "rank": user_rank, "ranking": dict_ranking}
                res.body = json.dumps(return_data)

api = falcon.API()
api.add_route('/login', LogInResource())
api.add_route('/ranking', RankingResource())
