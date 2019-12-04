
## Helstu Vinnureglur
Forritið sjálft verður í `/main` möppunni, `/modules` heldur utanum klasana sem við ætlum að gera og prufu gögnin eru í `/main/data` (ekki breyta neinu í `STUDENTDATA`). __Stefanía sér alfarið um master__.

Við munum vera nota TRELLO til að fylgjast með hvað er verið að vinna í og hvað er búið. Hver meðlimur mun merkja trello kortin sjálfum sér til að láta aðra vita hvað þau eru að vinna í að hverju sinni.

1. `master branch` á að vera nýjasta útgáfan af heildar forritinu. Reynum að halda henni stöðugri (vera viss um að allt sé í lagi áður en merge við master).
1. __Vinnið á eigin branch__ en ekki beint á master
1. Þegar þið teljið ykkar kóða vera tilbúinn til að vera sameinaður við master, þá láta Stefaníu vita og hún sér um það.
1. [Skoðið hérna hvenær þið gerðuð síðast `push` (og hvort það tókst)](https://github.com/MyraMidnight/VLN1_h16/branches), það sýnir líka hvort þið eruð á undan eða eftir _master branch_ til að vita hvort sé ekki tímabært að uppfæra ykkar branch eða merge.
1. Farið varlega í að uppfæra ykkar branch, þ.e. vera viss um að sé búið að gera `git push` til að geta náð í gögnin aftur ef eitthvað klikkar locally.
1. `git status` er besti vinur þinn til að meta stöðuna á git og minna þig á hvaða branch þú ert í og hvort síðasta `git commit` hafi virkað. 

> Jafnvel ef þið eruð á eigin branch, þá þurfið þið samt að passa ykkur að vera vinna sem minnst útfyrir þær skrár sem skiptir ykkur máli. Þetta er til þess að minnka líkur á _merge conflicts_.

## Ýmsar upplýsingar um GIT fyrir verkefnið
>COMMENT YOUR CODE! Af því að við túlkum allt mismunandi (aldrei ættlast til þess að eitthvað sé _augljóst_, notði það til að útskýra hvað kóðinn er að gera á köflum en ekki línu fyrir línu)
>
>Þessi skilaboð koma í veg fyrir rugling og vesen þegar forrið verður stærra, flýtir fyrir ef þörf er á að sameina kóða og hjálpar alveg rosalega ef það verður t.d. _merge conflict_.


### Vinnið á réttum _branch_
Í forritunarhlutanum þurfum við að vera með á hreinu hverjir eru að vinna í hvaða klösum/kóða, til þess að koma í veg fyrir að fólk sé að vinna í sömu skránum. 

Til að koma í veg fyrir __merge conflicts__ þá ættu allir að vinna í mismunandi pörtum forritsins að hverju sinni (conflicts gerast ef fleirri en einn hefur breytt sömu skrá, þá eru tvær útgáfur og git þarf hjálp í að leysa það)

* `git branch` birtir lista af öllum local branches og segjir þér hvar þú ert.
* `git branch <new_branch_name>` býr til nýjan branch án þess að færa þig
* `git checkout -b <new_branch_name>` býr till nýjan branch og fer í hann á sama tíma.  

* `git checkout <branch_name>` færir þig á milli branches
* Þegar þið gerið nýjan branch, þá er það einfaldlega afrit af þeim branch sem þið voruð stödd í á þeirri stundu.
* Nöfnin á branches eru __case sensitive__ 

```
git checkout -b <branch_name>
git branch
git checkout <branch_name>
```

### Að gera local backups (`git commit`)
Þið getið litið á `git commit` sem einskonar _milestones_ eða _checkpoints_, þar sem git vistar locally á tölvunni ykkar hvernig verkefnið er á þeirri stundu.

Munið að það vistar bara þær skrár sem hafa verið settar á _staging area_ (notið `git status` til að sjá hvað er í þessu 'stage' og hvað ekki, áður en þið gerið commit).

1. Notið `git status` til að sjá hvaða skrár hafa breyst frá síðasta _commit_. Það birtir upplýsingar um hvaða skrár eru á _stage_ og hvaða branch þið eruð á, og jafnvel gefur leiðbeiningar hvernig á að taka skrár af _stage_ ef þörf er á.
1. Þið notið `git add .` til að bæta öllum breyttum skrám á _staging area_ (`git add <filename>` til að bæta stökum skrám, kanski viljið þið ekki senda allar breytingar í _commit_). 
1. Til að gera _commit_ þá notið þið `git commit -m "message"`, þar sem message er örstutt lýsing á hvað er búið að breytast 
1. Einungis þær skrár sem eru á _staging area_ eru vistaðar þegar þú gerir `git commit`
1. Ef þið gleymið að bæta við lýsingunni og "læsist" í terminal (git opnar oftast editor í CLI) þá bara einfaldlega reyna loka þessum CLI editor og gera commit aftur (ekki gleyma bæta lýsingunni). En auðvitað ef þið kunnið á þennan CLI text editor þá getið þið alveg bætt lýsingunni í gegnum það... 
1. notið `git status` til að staðfesta að allt sé komið í _commit_ sem þið vilduð.

```
git status
git add .
git commit -m "short description"
git status
```

### Gerið dagleg __online backup__ (`git push`)
Það sem `git push` gerir er að safna saman öllum `commits` sem þið hafið gert síðan síðasta _push_ og ýtir þeim á netið (_remote repository_). Þetta er eitthvað sem þið ættuð að gera reglulega af því þá er vinnan ykkar örugg ef eitthvað gerist fyrir tölvuna ykkar.
1. gerið það að minnsta kosti daglega t.d. í lok dags.
1. _push_ áður en þið uppfærið ykkar branch með master. 

* Branches eru bara __local__ hjá ykkur þar til þið ýtið þeim á `remote repository` með `git push`. Það prentar fyrir ykkur leiðbeiningar ef þessi tiltekni branch er ekki til á remote.
```
git status 
git push
```

### Hætta við breytingar?
Fyrst GIT er _version control_, þá getið þið auðvitað notfært það til að ná í eldri útgáfur af verkefninu. Algengast væri að bara fá síðusta _commit_ aftur. 

1. Til að hætta við allar breytingar þá notið þið `git checkout -- .` (þetta er mjög gagnlegt ef þið viljið prófa eitthvað nýtt, t.d. endurskrifa einhver kóða, og geta bara hætt við þá tilraunarstarfsemi ef illa gegnur)
1. Hægt er að nota `git checkout -- <filename>` til að hætta við breytingar í stökum skrám, þá verða þær aftur eins og í síðasta _commit_.

> Ef þið ætlið að fara út í eitthverja stóra tilraunarstarfsemi eða endurgera einhvern hluta af verkefninu þá er sniðugt að gera nýjan branch (það býr til afrit af núverandi branch).
 
```
git status
git checkout -- <filename> 
git status
```

### Uppfæra ykkar branch með master?
1. Fyrst vera viss um að öll núverandi vinna sé örugg (`commit` og `push`)
1. Farið yfir á local master og náið í nýjustu útgáfuna með `git pull`
1. Farið síðan aftur á ykkar branch og gerið `git merge master`
1. Ef engin _merge conflicts_ koma upp, þá er allt búið, en annars biður git þig um að leysa þá flækju fyrst.

```
git checkout master
git pull
git checkout <your_branch>
git merge master
```
Ef þið lendið í flækju og viljið bara hætta við þessa uppfærslu, einfaldlega nota `git checkout -- .` (í versta falli mynduð þið byrja upp á nýtt með `git clone`, þess vegna er mikilvægt að gera push áður en þið byrjið.)

### Leysa flækjur
Ef þið treystið ykkur í að leysa _merge conflicts_, þá endilega gerið það, annars getið þið bara beðið Stefaníu að kíkja á þetta.

1. Git segjir ykkur hvar flækjurnar eru, og sumir editors eins og t.d. Visual Studio Code þá er meðhöndlun á þessum fllækjum frekar einfalt. Það sýnir þér hver þín útgáfa er, útgáfan sem þú ert að ná í og spyr þig hvort þeirra þú vilt halda (eða hvort þú viljir halda báðum)
1. Þegar flækjan hefur verið leyst, þá gerið þið `commit`, en farið varlega í `push` þar til þið eruð alveg viss um að þið leystuð þessa flækju án þess að það valdi villum í kóðanum.