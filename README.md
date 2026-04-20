# ArthaGraph: IKS-Driven Financial Knowledge Engine 🏛️💳

**ArthaGraph** is a Data Engineering project that maps the relationship between ancient Indian trade routes, commodity hubs (Indian Knowledge Systems - IKS), and modern FinTech infrastructure in Maharashtra. 

Using **Graph Database** technology (Neo4j), this project identifies how historical economic centers correlate with today's financial technology hubs, providing insights into long-term urban and economic development.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Database:** Neo4j Aura DB (Graph Database)
- **Data Engineering:** Pandas (ETL), Cypher (Graph Queries)
- **Environment:** Visual Studio Code, Git/GitHub

---

## 🏗️ System Architecture
The project follows a modular Data Pipeline architecture:

1. **Extraction:** Python scripts generate/scrape historical (IKS) and modern (FinTech) data.
2. **Transformation:** Data cleaning, coordinate normalization, and relationship mapping using Python.
3. **Loading:** Data is ingested into Neo4j as Nodes (Entities) and Edges (Relationships).
4. **Analytics:** Cypher queries identify "overlaps" where modern finance sits atop ancient trade hubs.

## 📈 Roadmap & Progress
- [x] **Phase 1:** Project Initialization & Schema Design
- [x] **Phase 2:** Synthetic Data Generation (CSV)
- [x] **Phase 3:** Neo4j Cloud Connection & Environment Security
- [x] **Phase 4:** Knowledge Graph Construction & Ingestion
- [ ] **Phase 5:** Spatial Analytics & FinTech Insights

---

## 📂 Project Structure
```text
ArthaGraph/
├── data/               # Raw CSV files (Ancient & Modern)
├── scripts/            # Python ETL scripts
│   ├── generate_data.py   # Step 1: Data creation
│   └── build_graph.py     # Step 2: (In progress) Neo4j Ingestion
├── .env                # (Hidden) Credentials
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
