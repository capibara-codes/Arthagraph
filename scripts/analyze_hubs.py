import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(user, password))

def run_analysis():
    query = """
    MATCH (m:ModernHub)-[:GEOGRAPHIC_SUCCESSOR|EVOLVED_FROM]->(a:AncientSite)
    RETURN a.name AS AncientSite, count(m) AS ModernConnectionCount, a.commodity AS HistoricalGood
    ORDER BY ModernConnectionCount DESC
    """
    
    with driver.session() as session:
        results = session.run(query)
        print("🏛️ --- ARTHAGRAPH INSIGHT REPORT --- 🏛️\n")
        for record in results:
            print(f"Ancient Site: {record['AncientSite']}")
            print(f"Historical Trade: {record['HistoricalGood']}")
            print(f"Modern FinTech Connections: {record['ModernConnectionCount']}")
            print("-" * 30)

if __name__ == "__main__":
    run_analysis()
    driver.close()