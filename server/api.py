import falcon
import json
import MySQLdb

USER = 'teamf'
PASS = 'sge_teamf'
HOST = 'db'
DB = 'SGE'

def getRanking():
    connector = MySQLdb.connect(
            user=USER,
            passwd=PASS,
            host=HOST,
            db=DB)

    cursor = connector.cursor()
    cursor.execute('SELECT username, weight, score FROM ranking ORDER BY score DESC LIMIT 100')
    array = []
    for (rank, row) in enumerate(cursor.fetchall()):
        array.append({'rank': rank+1, 'username': row[0], 'weight': row[1], 'score': row[2]})

    cursor.close
    connector.close
    return array

def getRank(score):
    if score is not None:
        connector = MySQLdb.connect(
                user=USER,
                passwd=PASS,
                host=HOST,
                db=DB)

        cursor = connector.cursor()
        cursor.execute('SELECT COUNT(*) FROM ranking WHERE score > ' + str(score))
        rank = cursor.fetchone()[0] + 1
        cursor.close
        connector.close
        return rank
    return 0

def setRank(username='---',weight=0,score=0):
    connector = MySQLdb.connect(
            user=USER,
            passwd=PASS,
            host=HOST,
            db=DB)

    cursor = connector.cursor()
    cursor.execute('INSERT INTO ranking (username,weight,score) VALUES ("{0}",{1},{2})'.format(username,weight,score))
    cursor.close
    connector.commit()
    connector.close

class RankingResource:
    def on_get(self, req, res):
        res.body = json.dumps({'ranking': getRanking(), 'rank': 0})

    def on_post(self, req, res):
        post_data = json.loads(req.stream.read().decode('utf-8'))
        username = post_data['username']
        weight = post_data['weight']
        score = post_data['score']
        setRank(username, weight, score)
        res.body = json.dumps({'ranking': getRanking(), 'rank': getRank(score)})

class ScoreResource:
    def on_get(self, req, res, score):
        res.body = json.dumps({'ranking': getRanking(), 'rank': getRank(score)})

api = falcon.API()
api.add_route('/ranking', RankingResource())
api.add_route('/score/{score}', ScoreResource())
