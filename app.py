import os
import random
from datetime import datetime

from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Motto dne o ženách – mění se každý den podle dne v roce.
MOTTA = [
    "Žena, která čte, je nebezpečná – má vlastní myšlenky. (Rori Manchester)",
    "Nejsilnější věc, kterou může žena udělat, je zůstat sama sebou. (Marilyn Monroe)",
    "Ženy nejsou jen polovina lidské rasy, jsou celý svět. (Charlotte Perkins Gilman)",
    "Krása ženy se neprojevuje v tváři, ale v srdci. (Dr. Seuss)",
    "Žena s cílem je ženou v pohybu. (Anna Quindlenová)",
    "Nenech si líbit nic, co bys neměla dát i mužům. (Margaret Thatcherová)",
    "Ženy, kteří se bojí žen, jsou vždycky ženy. (Tennessee Williams)",
    "Žena, která stojí za pravdou, i když se třesou kolena, je nejsilnější žena, jakou znám. (Oprah Winfrey)",
]

# Lehké, vtipné radosti pro kolo osudu.
POVOLY = [
    ("🔮", "Dnes je skvělý den začít něco nového. Třeba ten projekt, co odkládáš od ledna."),
    ("☕", "Kozmický vzkaz: nejdřív káva, potom rozhodnutí. Vždycky."),
    ("💃", "Někdo na tebe dnes myslí s obdivem. Pravděpodobně tvůj kočka, až přijdeš domů."),
    ("🌙", "Dnes večer se splní něco malého. Začni tím, že si to nahlas přeješ."),
    ("🍀", "Štěstí přeje připraveným. Ty jsi připravená. Štěstí se právě obouvá."),
    ("🐌", "Dnes neběh. Plíž se elegantně jako slimák v hedvábném šátku."),
    ("🎭", "Něco se bude dít. Zůstań u toho a hlavně se neptej 'proč já' – ptej se 'proč ne'."),
    ("🌈", "Po každém dešti duha, po každém deadline volno. Fyzika to potvrzuje."),
    ("👑", "Dnes vládni. I nad ovladačem. I nad dálkovým ovladačem. I nad tím posledním soustem."),
    ("🚪", "Otevři dnes jedny dveře, které jsou zavřené déle než měsíc. Třeba tu skříň."),
    ("⭐", "Splň si dnes jedno malinké přání. Hvězdný rozpočet to utáhne."),
    ("🦋", "Motýli v břiše? Signál, že je čas na dobrodružství. Nebo na oběd."),
]


@app.route("/")
def home():
    """Úvodní strana se zápisem, mottem dne a analogovými hodinami."""
    today = datetime.now()
    return render_template(
        "index.html",
        server_time=today.strftime("%H:%M:%S"),
        motto=MOTTA[today.timetuple().tm_yday % len(MOTTA)],
        date=today.strftime("%-d. %-m. %Y"),
    )


@app.route("/api/povol")
def povol():
    """Náhodné ponaučení pro kolo osudu."""
    emoji, text = random.choice(POVOLY)
    return jsonify({"emoji": emoji, "text": text})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("FLASK_PORT", 5052)),
        debug=True,
    )
