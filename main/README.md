
## Grunnreglur og leiðarljós

__Stefanía sér alfarið um master branch__ fyrir þetta verkefni og eftir að forritunarhluti námskeiðs hefst.
* Látið Stefaníu vita ef þið viljið láta sameina ykkar branch við master (þegar hluti kóðans sem þið voruð að vinna í er _tilbúinn_)

>COMMENT YOUR CODE! Af því að við túlkum allt mismunandi (aldrei ættlast til þess að eitthvað sé _augljóst_, notði það til að útskýra hvað kóðinn er að gera á köflum en ekki línu fyrir línu)
>
>Þessi skilaboð koma í veg fyrir rugling og vesen þegar forrið verður stærra, flýtir fyrir ef þörf er á að sameina kóða og hjálpar alveg rosalega ef það verður t.d. _merge conflict_.


### Vinnið á réttum _branch_
1. Ekki vinna beint á master branch, bara hoppa yfir á réttan branch áður en þið gerið commit (eða gera nýjan branch ef eitthvað vesen er í gangi).
1. Þegar þið gerið nýjan branch, þá er það einfaldlega afrit af þeim branch sem þið voruð stödd í á þeirri stundu.
1. `git branch` sýnir ykkur listann af öllum local branches og í hverjum þið eruð stödd
1. Nöfnin á branches eru __case sensitive__ 
1. Git gefur ykkur leiðbeiningar hvernig á að tengja nýjan branch við _remote repository_ ef þið hafið aldrei gert `git push` á þeim branch. 
1. Í forritunarhlutanum þá skulum við skýra branches eftir t.d. klasanum sem þið eruð að vinna í 
1. Til að koma í veg fyrir __merge conflicts__ þá ættu allir að vinna í mismunandi pörtum forritsins að hverju sinni (conflicts gerast ef fleirri en einn hefur breytt sömu skrá, þá eru tvær útgáfur og git þarf hjálp í að leysa það)

### Gerið regluleg 'local backups' (git commit)
Þið getið litið á `git commit` sem einskonar _milestones_ eða _checkpoints_, þar sem git vistar locally á tölvunni ykkar hvernig verkefnið er á þeirri stundu.

Munið að það vistar bara þær skrár sem hafa verið settar á _staging area_ (notið `git status` til að sjá hvað er í þessu 'stage' og hvað ekki, áður en þið gerið commit).

1. Notið `git status` til að sjá hvaða skrár hafa breyst frá síðasta _commit_. Það birtir upplýsingar um hvaða skrár eru á _stage_ og hvaða branch þið eruð á, og jafnvel gefur leiðbeiningar hvernig á að taka skrár af _stage_ ef þörf er á.
1. Þið notið `git add .` til að bæta öllum breyttum skrám á _staging area_ (`git add <filename>` til að bæta stökum skrám, kanski viljið þið ekki senda allar breytingar í _commit_). 
1. Til að gera _commit_ þá notið þið `git commit -m "message"`, þar sem message er örstutt lýsing á hvað er búið að breytast 
1. Einungis þær skrár sem eru á _staging area_ eru vistaðar þegar þú gerir `git commit`
1. Ef þið gleymið að bæta við lýsingunni og "læsist" í terminal (git opnar oftast editor í CLI) þá bara einfaldlega reyna loka þessum CLI editor og gera commit aftur (ekki gleyma bæta lýsingunni). En auðvitað ef þið kunnið á þennan CLI text editor þá getið þið alveg bætt lýsingunni í gegnum það... 
1. notið `git status` til að staðfesta að allt sé komið í _commit_ sem þið vilduð.


#### Hætta við breytingar?
Fyrst GIT er _version control_, þá getið þið auðvitað notfært það til að ná í eldri útgáfur af verkefninu. Algengast væri að bara fá síðusta _commit_ aftur. 

1. Til að hætta við allar breytingar þá notið þið `git checkout -- .` (þetta er mjög gagnlegt ef þið viljið prófa eitthvað nýtt, t.d. endurskrifa einhver kóða, og geta bara hætt við þá tilraunarstarfsemi ef illa gegnur)
1. Hægt er að nota `git checkout -- <filename>` til að hætta við breytingar í stökum skrám, þá verða þær aftur eins og í síðasta _commit_.

> Ef þið ætlið að fara út í eitthverja stóra tilraunarstarfsemi eða endurgera einhvern hluta af verkefninu þá er sniðugt að gera nýjan branch (það býr til afrit af núverandi branch).
 
### Gerið dagleg 'online backup' (git push)
Það sem `git push` gerir er að safna saman öllum `commits` sem þið hafið gert síðan síðasta _push_ og ýtir þeim á netið (_remote repository_). Þetta er eitthvað sem þið ættuð að gera reglulega af því þá er vinnan ykkar örugg ef eitthvað gerist fyrir tölvuna ykkar.
1. gerið það að minnsta kosti daglega t.d. í lok dags.
1. _push_ áður en þið uppfærið ykkar branch með master. 
