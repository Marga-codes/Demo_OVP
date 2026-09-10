import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;

// Route mappings for demos and interior URLs
app.get(['/demo1', '/demo-1'], (req, res) => {
  res.sendFile(path.join(__dirname, 'demo1.html'));
});
app.get(['/demo2', '/demo-2'], (req, res) => {
  res.sendFile(path.join(__dirname, 'demo2.html'));
});
app.get(['/demo3', '/demo-3'], (req, res) => {
  res.sendFile(path.join(__dirname, 'demo3.html'));
});
app.get('/who-we-are', (req, res) => {
  res.sendFile(path.join(__dirname, 'who-we-are.html'));
});
app.get('/what-we-do', (req, res) => {
  res.sendFile(path.join(__dirname, 'what-we-do.html'));
});
app.get('/our-work', (req, res) => {
  res.sendFile(path.join(__dirname, 'our-work.html'));
});

// Serve static files from the repository root
app.use(express.static(__dirname));

// Single-page application fallback to index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running at http://0.0.0.0:${PORT}`);
});
