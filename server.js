const express = require('express');
const neo4j = require('neo4j-driver');
require('dotenv').config({ path: '../.env' });

const app = express();
const driver = neo4j.driver(process.env.NEO4J_URI, neo4j.auth.basic(process.env.NEO4J_USERNAME, process.env.NEO4J_PASSWORD));

app.use(express.static('public')); // This serves your HTML/CSS

app.get('/api/data', async (req, res) => {
    const session = driver.session();
    try {
        const result = await session.run('MATCH (m:ModernHub)-[r]->(a:AncientSite) RETURN m.name as modern, a.name as ancient');
        const data = result.records.map(record => ({
            modern: record.get('modern'),
            ancient: record.get('ancient')
        }));
        res.json(data);
    } finally {
        await session.close();
    }
});

app.listen(3000, () => console.log('🚀 ArthaGraph running on http://localhost:3000'));