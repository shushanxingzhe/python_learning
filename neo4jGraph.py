from neo4j import GraphDatabase


class neo4jDB(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def write_greeting(self):
        with self._driver.session() as session:
            session.run("create (g:Greeting {from:'someone',message:'hello'})")

    def read_greeting(self):
        with self._driver.session() as session:
            greeting = session.run("match (g:Greeting) return g")
            print(greeting.single())

    def update_greeting(self):
        with self._driver.session() as session:
            session.run("match (g:Greeting) set g.message = 'hello world'")

    def delete_greeting(self):
        with self._driver.session() as session:
            session.run("match (g:Greeting) where g.message = 'hello world' delete g")


neoDB = neo4jDB('bolt://10.60.47.53:7687', 'liujiafu', 'liujiafu')
print("write")
neoDB.write_greeting()
neoDB.read_greeting()
print("update")
neoDB.update_greeting()
neoDB.read_greeting()
print("delete")
neoDB.delete_greeting()
neoDB.read_greeting()
