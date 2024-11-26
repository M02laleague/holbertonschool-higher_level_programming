const fs = require('fs');

// Liste des fichiers main.js et leur contenu correspondant
const files = [
  { name: '0-main.html', script: '0-script.js' },
  { name: '1-main.html', script: '1-script.js' },
  { name: '2-main.html', script: '2-script.js' },
  { name: '3-main.html', script: '3-script.js' },
  { name: '4-main.html', script: '4-script.js' },
  { name: '5-main.html', script: '5-script.js' },
  { name: '6-main.html', script: '6-script.js' },
  { name: '7-main.html', script: '7-script.js' },
  { name: '8-main.html', script: '8-script.js' },
];

// Modèle de contenu HTML
const generateHTML = (scriptFile) => `
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>JavaScript DOM Manipulation</title>
  </head>
  <body>
    <header> 
      Example Header
    </header>
    <br />
    <div id="example_action">Example Action</div>
    <br />
    <ul id="list_items">
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="${scriptFile}"></script>
  </body>
</html>
`;

// Création des fichiers HTML
files.forEach(file => {
  const content = generateHTML(file.script);
  fs.writeFileSync(file.name, content, 'utf-8');
  console.log(`Fichier ${file.name} généré.`);
});
