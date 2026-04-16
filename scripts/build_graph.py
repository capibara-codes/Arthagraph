import os
import pandas as pd
from neo4j import GraphDatabase
from dotenv import load_dotenv

# 1. Setup & Connection
load_dotenv()
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(user, password))

def create_nodes():
   def create_nodes():
    # Get the directory where the script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Go up one level to the main Arthagraph folder and find the data CSVs
    ancient_path = os.path.join(base_dir, '..', 'data', 'ancient_sites.csv')
    modern_path = os.path.join(base_dir, '..', 'data', 'modern_hubs.csv')

    # Load our data using the new paths
    df_ancient = pd.read_csv(ancient_path)
    df_modern = pd.read_csv(modern_path)
    

    with driver.session() as session:
        # Clear existing data (Be careful with this in real jobs!)
        session.run("MATCH (n) DETACH DELETE n")
        
        # Create Ancient Site Nodes
        for _, row in df_ancient.iterrows():
            session.run("""
                CREATE (a:AncientSite {id: $id, name: $name, type: $type, commodity: $comm})
            """, id=row['site_id'], name=row['name'], type=row['type'], comm=row['commodity'])
        
        # Create Modern Hub Nodes
        for _, row in df_modern.iterrows():
            session.run("""
                CREATE (m:ModernHub {id: $id, name: $name, specialty: $spec})
            """, id=row['hub_id'], name=row['name'], spec=row['specialty'])

        # Create Relationships (The IKS Magic!)
        # Let's connect BKC Mumbai to Sopara because they are both maritime financial centers
        session.run("""
            MATCH (a:AncientSite {name: 'Sopara'}), (m:ModernHub {name: 'BKC Mumbai'})
            CREATE (m)-[:EVOLVED_FROM]->(a)
        """)
        
        # Let's connect Hinjewadi to Junnar (Ancient trade hub near Pune)
        session.run("""
            MATCH (a:AncientSite {name: 'Junnar'}), (m:ModernHub {name: 'Hinjewadi Pune'})
            CREATE (m)-[:GEOGRAPHIC_SUCCESSOR]->(a)
        """)

    print("✅ Graph successfully populated with IKS and FinTech nodes!")

if __name__ == "__main__":
    create_nodes()
    driver.close()