import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

def test_conn():
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        with driver.session() as session:
            result = session.run("RETURN 'Connection Successful!' as message")
            print(f"✅ Neo4j says: {result.single()['message']}")
        driver.close()
    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    test_conn()