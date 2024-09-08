from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    kommen = None
    gehen_min = None
    gehen_max = None
    wochenarbeitszeit = "40"  # Standardmäßig 40 Stunden Woche

    if request.method == "POST":
        kommen_str = request.form.get("kommen")
        wochenarbeitszeit = request.form.get("wochenarbeitszeit", "40")

        try:
            # Konvertiere die eingegebene Kommen-Zeit
            kommen = datetime.strptime(kommen_str, "%H:%M:%S")

            # Berechne die Arbeitszeit basierend auf der Wochenarbeitszeit
            if wochenarbeitszeit == "35":
                arbeitszeit = timedelta(hours=7, minutes=30)  # Arbeitszeit inkl. 30 Minuten Pause
            else:
                arbeitszeit = timedelta(hours=8, minutes=30)  # Arbeitszeit inkl. 30 Minuten Pause

            # Berechnung von Gehen min
            gehen_min = kommen + arbeitszeit

            # Berechnung von Gehen max
            # Maximal 10 Stunden Arbeitszeit + 45 Minuten Pause
            gehen_max = kommen + timedelta(hours=10) + timedelta(minutes=45)

        except ValueError:
            pass  # Fehlerhafte Eingabe ignorieren

    return render_template("index.html", kommen=kommen, gehen_min=gehen_min, gehen_max=gehen_max, wochenarbeitszeit=wochenarbeitszeit)

if __name__ == "__main__":
    app.run()

