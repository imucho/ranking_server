import falcon

class RankingResource:
    def on_get(self, req, res):
        res.body = "hoge"

    def on_post(self, req, res):
        res.body = "hogehoge"

api = falcon.API()
api.add_route('/', RankingResource())
