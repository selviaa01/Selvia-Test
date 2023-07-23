from flask import Flask, render_template

app = Flask(__name__)

def dense_ranking(scores, gits_scores):
    # Buat daftar skor unik secara terurut dari nilai terbesar ke nilai terkecil
    unique_scores = sorted(set(scores), reverse=True)

    # Buat kamus untuk menyimpan peringkat berdasarkan skor unik
    rank_dict = {score: rank + 1 for rank, score in enumerate(unique_scores)}

    # Fungsi untuk mendapatkan peringkat berdasarkan skor
    def get_rank(score):
        return rank_dict.get(score)

    # Hitung peringkat GITS berdasarkan skor yang didapatkan
    gits_ranks = [get_rank(gits_score) for gits_score in gits_scores]

    return gits_ranks

@app.route('/')
def index():
    # Input dari contoh soal
    all_scores = [100, 100, 50, 40, 40, 20, 10]
    gits_scores = [5, 25, 50, 120]

    # Hasil keluaran berdasarkan contoh soal
    result = dense_ranking(all_scores, gits_scores)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
