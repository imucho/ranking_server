import falcon
import json
import MySQLdb

def getRanking():
    connector = MySQLdb.connect(
            user='root',
            passwd='ca_sge_teamf',
            host='0.0.0.0',
            db='SGE')

    cursor = connector.cursor()
    cursor.execute('SELECT username, distance, weight, score FROM ranking ORDER BY score DESC LIMIT 100')
    array = []
    for (rank, row) in enumerate(cursor.fetchall()):
        array.append({'rank': rank+1, 'username': row[0], 'distance': row[1], 'weight': row[2], 'score': row[3]})

    cursor.close
    connector.close
    return array

def getRank(score):
    if score.isdigit():
        connector = MySQLdb.connect(
                user='root',
                passwd='ca_sge_teamf',
                host='0.0.0.0',
                db='SGE')

        cursor = connector.cursor()
        cursor.execute('SELECT COUNT(*) FROM ranking WHERE score > ' + score)
        rank = cursor.fetchone()[0] + 1
        cursor.close
        connector.close
        return rank
    return 0


class RankingResource:
    def on_get(self, req, res):
        res.body = json.dumps(getRanking())

    def on_post(self, req, res):
        res.body = "hogehoge"

api = falcon.API()
api.add_route('/', RankingResource())
