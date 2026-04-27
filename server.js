const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.static('public'));

// Sample data - replace with your actual IKS graph data
const graphData = [
    { modern: "Digital Wallet", ancient: "Kashika (Shell Money)" },
    { modern: "Cryptocurrency", ancient: "Cowrie Shells" },
    { modern: "Smart Contracts", ancient: "Maqasid al-Aqad" },
    { modern: "Peer-to-Peer Transfer", ancient: "Hundi System" },
    { modern: "Blockchain Ledger", ancient: "Tamras (Trade Records)" },
    { modern: "DeFi Protocols", ancient: "Joint Liability Partnerships" }
];

app.get('/api/data', (req, res) => {
    res.json(graphData);
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
    console.log(`🏛️ ArthaGraph server running at http://localhost:${PORT}`);
});