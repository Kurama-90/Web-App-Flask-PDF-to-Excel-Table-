from flask import Flask, request, send_file, render_template
import pdfplumber
import pandas as pd
import os

app = Flask(__name__)

# Dossier de sauvegarde temporaire des fichiers
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Route pour la page d'accueil et télécharger le fichier PDF
@app.route('/')
def index():
    return render_template('index.html')

# Route pour télécharger et convertir le PDF en Excel
@app.route('/convert', methods=['POST'])
def convert_pdf_to_excel():
    # Vérifier si le fichier a été envoyé
    if 'pdf_file' not in request.files:
        return "No file part", 400

    pdf_file = request.files['pdf_file']

    # Vérifier si le fichier est un PDF
    if pdf_file.filename == '':
        return "No selected file", 400

    if pdf_file and pdf_file.filename.endswith('.pdf'):
        # Sauvegarder le fichier PDF
        pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
        pdf_file.save(pdf_path)

        # Liste pour stocker les DataFrames de chaque page
        all_tables = []

        # Ouvrir le PDF et parcourir chaque page
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                table = page.extract_table()

                # Si une table est trouvée sur la page, la convertir en DataFrame et l'ajouter à la liste
                if table:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    all_tables.append(df)

        # Si des tables ont été extraites, les concaténer
        if all_tables:
            final_df = pd.concat(all_tables, ignore_index=True)

            # Sauvegarder le DataFrame final en fichier Excel
            excel_path = os.path.join(OUTPUT_FOLDER, 'converted_file.xlsx')
            final_df.to_excel(excel_path, index=False)

            # Retourner le fichier Excel à l'utilisateur
            return send_file(excel_path, as_attachment=True)

        return "No tables found in the PDF", 400

    return "Invalid file format. Only PDF allowed.", 400

if __name__ == '__main__':
    app.run(debug=True)
