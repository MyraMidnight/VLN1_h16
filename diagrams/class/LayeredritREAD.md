## Layeredrit

útskýrir myndrænt hvernig UI-, Logic- og IO lög munu vinna saman.

LLAPI og IOAPI munu bæði vera klasar sem innihalda öll functions af sínu lagi,

þessi functions munu síðan sjá um allt functionality í forritinu.

Á öllum functions er stutt lýsing á hvað function þarf að geta gert til að uppfyla kröfur,

einnig er væg hugmynd um hvaða variables og upplýsingar það mun þurfa.

Mikilvægasta fallið er DataPipe í IOAPI sem mun sjá um að ná í eða skila data í skrá,

það sem heldur um skrárnar eftir að búið er að ná í þær er variable filePackage,

það er dictionary þar sem key:filename og value:list of lines (frá skrá),

LLAPI munu taka við filePackage og vinna með hann og breyta eins og þarf og síðan skila því,

DataPipe mun þá sjá um að skrifa yfir allar skrár í package og þannig uppfæra/bæta við.
