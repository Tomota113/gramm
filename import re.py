import re
import csv

# Données brutes (exemple)
raw_data = """
bambara,francais
dá,dá→̌→ 2228
da,dá→̌→ 2228
dà,dà→̌→ 12
dàa,dàa→̌→ 51Voir entrée principale :dàga.
daa,dàa→̌→ 51Voir entrée principale :dàga.
dáaba,dáaba→̌dába.
daaba,dáaba→̌dába.
daabo,Daabo→̌Dabo.
dàadala,dàadala( canari créer *agent permanent )
daadala,dàadala( canari créer *agent permanent )
dàaduru,dàaduru( canari )
daaduru,dàaduru( canari )
dàamɛ,dàamɛ→̌
daamɛ,dàamɛ→̌
daamè,dàamɛ→̌
dàamu,dàamu→̌→ 81Source :(ar. da:ma 'durer').
daamu,dàamu→̌→ 81Source :(ar. da:ma 'durer').
dàan,dàan→̌→ 2dànga.
daan,dàan→̌→ 2dànga.
dàana,dàana→̌dàanɛ.dàna.
daana,dàana→̌dàanɛ.dàna.
dàanajugu,dàanajugu( comportement méchant )dàanɛjugu.dànajugu.
daanajugu,dàanajugu( comportement méchant )dàanɛjugu.dànajugu.
dàanɛ,dàanɛ→̌dàana;dàna.
daanɛ,dàanɛ→̌dàana;dàna.
daanè,dàanɛ→̌dàana;dàna.
dàanɛjugu,dàanɛjugu( comportement méchant )dàanajugu;dànajugu.
daanɛjugu,dàanɛjugu( comportement méchant )dàanajugu;dànajugu.
daanèjugu,dàanɛjugu( comportement méchant )dàanajugu;dànajugu.
dàani,dàani→̌vt.
daani,dàani→̌vt.
dàanin,dàanin( canari *diminutif )
daanin,dàanin( canari *diminutif )
dàankun,dàankun→̌→ 4dànkun.dàankun.
daankun,dàankun→̌→ 4dànkun.dàankun.
dàansɔgɔ,dàansɔgɔ( salutation )
daansɔgɔ,dàansɔgɔ( salutation )
daansògò,dàansɔgɔ( salutation )
daaru salaami,Daaru Salaami→̌Darisalamu.Darasalamu.
dába,dába→̌Voir entrée principale :dáaba.
daba,dába→̌Voir entrée principale :dáaba.
dàba,dàba→̌→ 44
dábaa,dábaa( créer *agent occasionnel )dábaga;dánbaga;dánbaa.
dabaa,dábaa( créer *agent occasionnel )dábaga;dánbaga;dánbaa.
dábaatɔ,dábaatɔ( poser *agent occasionnel *statif )Voir entrée principale :dábagatɔ.
dabaatɔ,dábaatɔ( poser *agent occasionnel *statif )Voir entrée principale :dábagatɔ.
dabaatò,dábaatɔ( poser *agent occasionnel *statif )Voir entrée principale :dábagatɔ.
dábabara,dábabara( encre calebasse )
dababara,dábabara( encre calebasse )
dàbacɛ,dàbacɛ( houe mâle )dàbacɛman.
dabacɛ,dàbacɛ( houe mâle )dàbacɛman.
dabacè,dàbacɛ( houe mâle )dàbacɛman.
dàbacɛman,dàbacɛman( houe mâle *adjectivateur )Voir entrée principale :dàbacɛ.
dabacɛman,dàbacɛman( houe mâle *adjectivateur )Voir entrée principale :dàbacɛ.
dabacèman,dàbacɛman( houe mâle *adjectivateur )Voir entrée principale :dàbacɛ.
dàbada,dàbada( houe bouche )
dabada,dàbada( houe bouche )
dàbadaba,dàbadaba( *augmentatif )
dabadaba,dàbadaba( *augmentatif )
dàbadababilen,dàbadababilen( houe bouche *augmentatif rouge )dàbadabilen.dàbadababilennin;dàbadablen.
dabadababilen,dàbadababilen( houe bouche *augmentatif rouge )dàbadabilen.dàbadababilennin;dàbadablen.
dàbadababilennin,dàbadababilennin( houe bouche *augmentatif rouge *diminutif )dàbadabilen.dàbadababilen;dàbadablen.
dabadababilennin,dàbadababilennin( houe bouche *augmentatif rouge *diminutif )dàbadabilen.dàbadababilen;dàbadablen.
dàbadabilen,dàbadabilen( houe bouche rouge )dàbadababilen;dàbadababilennin;dàbadablen.
dabadabilen,dàbadabilen( houe bouche rouge )dàbadababilen;dàbadababilennin;dàbadablen.
dàbadablen,dàbadablen( houe bouche rouge )dàbadabilen.dàbadababilen;dàbadababilennin;dàbadablen.
dabadablen,dàbadablen( houe bouche rouge )dàbadabilen.dàbadababilen;dàbadababilennin;dàbadablen.
dàbadaninbilen,dàbadaninbilen( *diminutif rouge )dàbadaninblen.
dabadaninbilen,dàbadaninbilen( *diminutif rouge )dàbadaninblen.
dàbadaninblen,dàbadaninblen( *diminutif rouge )dàbadaninbilen.dàbadaninblen.
dabadaninblen,dàbadaninblen( *diminutif rouge )dàbadaninbilen.dàbadaninblen.
dàbadugukolo,dàbadugukolo( houe terre [ terre os ] )
dabadugukolo,dàbadugukolo( houe terre [ terre os ] )
dábaga,dábaga( créer *agent occasionnel )dábaa.dánbaga;dánbaa.
dabaga,dábaga( créer *agent occasionnel )dábaa.dánbaga;dánbaa.
dábagatɔ,dábagatɔ( poser *agent occasionnel *statif )dábaatɔ.
dabagatɔ,dábagatɔ( poser *agent occasionnel *statif )dábaatɔ.
dabagatò,dábagatɔ( poser *agent occasionnel *statif )dábaatɔ.
dábaji,dábaji( encre eau )
dabaji,dábaji( encre eau )
dàbajula,dàbajula( houe commerçant )dàbajura.
dabajula,dàbajula( houe commerçant )dàbajura.
dàbajura,dàbajura( houe commerçant )Voir entrée principale :dàbajula.
dabajura,dàbajura( houe commerçant )Voir entrée principale :dàbajula.
dàba-kàla,dàba-kàla( houe tige )
daba-kala,dàba-kàla( houe tige )
dàbakalankɔyɔ,dàbakalankɔyɔ( houe tige aubergine.africaine )
dabakalankɔyɔ,dàbakalankɔyɔ( houe tige aubergine.africaine )
dabakalankòyò,dàbakalankɔyɔ( houe tige aubergine.africaine )
dàbakalasunsun,dàbakalasunsun( houe tige kaki.de.brousse )
dabakalasunsun,dàbakalasunsun( houe tige kaki.de.brousse )
dàbakamalen,dàbakamalen( houe jeune.homme )
dabakamalen,dàbakamalen( houe jeune.homme )
dàbakisɛ,dàbakisɛ( houe grain )
dabakisɛ,dàbakisɛ( houe grain )
dabakisè,dàbakisɛ( houe grain )
dàbali,dàbali→̌→ 284dàbari;dɛ̀bɛli.
dabali,dàbali→̌→ 284dàbari;dɛ̀bɛli.
dàbaliban,dàbaliban( moyen terminer )
dabaliban,dàbaliban( moyen terminer )
dàbalibana,dàbalibana( moyen maladie )
dabalibana,dàbalibana( moyen maladie )
dàbalibanko,dàbalibanko( moyen terminer affaire )
dabalibanko,dàbalibanko( moyen terminer affaire )
dàbalijuguya,dàbalijuguya( moyen méchant *abstractif )
dabalijuguya,dàbalijuguya( moyen méchant *abstractif )
dàbamasa,dàbamasa( houe roi )
dabamasa,dàbamasa( houe roi )
dàbamisi,dàbamisi( houe bovidé )
dabamisi,dàbamisi( houe bovidé )
dàbamuso,dàbamuso( houe féminin )dàbamusoman.
dabamuso,dàbamuso( houe féminin )dàbamusoman.
dàbamusoman,dàbamusoman( houe femme *adjectivateur )Voir entrée principale :dàbamuso.
dabamusoman,dàbamusoman( houe femme *adjectivateur )Voir entrée principale :dàbamuso.
daban,Daban→̌
dabanaani,Dabanaani→̌
dàbaŋana,dàbaŋana( houe champion )
dabaŋana,dàbaŋana( houe champion )
dàbaninkurun,dàbaninkurun( houe *diminutif court )
dabaninkurun,dàbaninkurun( houe *diminutif court )
dábara,dábara( bouche calebasse )
dabara,dábara( bouche calebasse )
dábarajɛ,dábarajɛ( bouche [ bouche calebasse ] blanc )
dabarajɛ,dábarajɛ( bouche [ bouche calebasse ] blanc )
dabarajè,dábarajɛ( bouche [ bouche calebasse ] blanc )
dàbari,dàbari→̌dàbali.dàbari;dɛ̀bɛli.
dabari,dàbari→̌dàbali.dàbari;dɛ̀bɛli.
dábɛ̀n,dábɛ̀n( bouche se.rencontrer )vt.Voir entrée principale :dálabɛ̀n.
dabɛn,dábɛ̀n( bouche se.rencontrer )vt.Voir entrée principale :dálabɛ̀n.
dabèn,dábɛ̀n( bouche se.rencontrer )vt.Voir entrée principale :dálabɛ̀n.
dábɛrɛbɛrɛma,dábɛrɛbɛrɛma→̌vt.
dabɛrɛbɛrɛma,dábɛrɛbɛrɛma→̌vt.
dabèrèbèrèma,dábɛrɛbɛrɛma→̌vt.
dabi,Dabi→̌
dábi,dábi→̌→ 2
dabi,dábi→̌→ 2
dàbi,dàbi→̌→ 22
dábìla,dábìla( bouche mettre )vt.
dabila,dábìla( bouche mettre )vt.
dábilabali,dábilabali( cesser [ bouche mettre ] PTCP.NEG )
dabilabali,dábilabali( cesser [ bouche mettre ] PTCP.NEG )
dàbilen,dàbilen( chanvre rouge )dàbilennin.
dabilen,dàbilen( chanvre rouge )dàbilennin.
dàbilennin,dàbilennin( chanvre rouge *diminutif )Voir entrée principale :dàbilen.
dabilennin,dàbilennin( chanvre rouge *diminutif )Voir entrée principale :dàbilen.
dàbiɲama,dàbiɲama( engoulevent force.occulte )
dabiɲama,dàbiɲama( engoulevent force.occulte )
dabinyama,dàbiɲama( engoulevent force.occulte )
dábiri,dábiri( bouche courber )vt.dábri.
dabiri,dábiri( bouche courber )vt.dábri.
dábirilan,dábirilan( renverser [ bouche courber ] *instrumental )
dabirilan,dábirilan( renverser [ bouche courber ] *instrumental )
dabo,Dabo→̌Voir entrée principale :Daabo.
dábɔ,dábɔ( bouche sortie )
dabɔ,dábɔ( bouche sortie )
dabò,dábɔ( bouche sortie )
dábɔbònbonkɔ́rɔ,dábɔbònbonkɔ́rɔ( bouche sortir menton sous )
dabɔbonbonkɔrɔ,dábɔbònbonkɔ́rɔ( bouche sortir menton sous )
dabòbonbonkòrò,dábɔbònbonkɔ́rɔ( bouche sortir menton sous )
dábɔlan,dábɔlan( commencer [ bouche sortir ] *instrumental )
dabɔlan,dábɔlan( commencer [ bouche sortir ] *instrumental )
dabòlan,dábɔlan( commencer [ bouche sortir ] *instrumental )
dábɔli,dábɔli( commencer [ bouche sortir ] *nom d'action )
dabɔli,dábɔli( commencer [ bouche sortir ] *nom d'action )
dabòli,dábɔli( commencer [ bouche sortir ] *nom d'action )
dábolo,dábolo( créer bras )
dabolo,dábolo( créer bras )
dábɔlɔ,dábɔlɔ( bouche piquet )dábɔ̀lɔ.
dabɔlɔ,dábɔlɔ( bouche piquet )dábɔ̀lɔ.
dabòlò,dábɔlɔ( bouche piquet )dábɔ̀lɔ.
dábɔlɔwɔlɔsɔ,dábɔlɔwɔlɔsɔ( bec [ bouche piquet ] faucille )
dabɔlɔwɔlɔsɔ,dábɔlɔwɔlɔsɔ( bec [ bouche piquet ] faucille )
dabòlòwòlòsò,dábɔlɔwɔlɔsɔ( bec [ bouche piquet ] faucille )
dábɔlɔwɔlɔsɔjɛman,dábɔlɔwɔlɔsɔjɛman( ibis.sacré [ bec [ bouche piquet ] faucille ] blanc [ blanc *adjectivateur ] )
dabɔlɔwɔlɔsɔjɛman,dábɔlɔwɔlɔsɔjɛman( ibis.sacré [ bec [ bouche piquet ] faucille ] blanc [ blanc *adjectivateur ] )
dabòlòwòlòsòjèman,dábɔlɔwɔlɔsɔjɛman( ibis.sacré [ bec [ bouche piquet ] faucille ] blanc [ blanc *adjectivateur ] )
dábɔnkama,dábɔnkama( commencer [ bouche sortir ] *je pour [ cou *à ] )
dabɔnkama,dábɔnkama( commencer [ bouche sortir ] *je pour [ cou *à ] )
dabònkama,dábɔnkama( commencer [ bouche sortir ] *je pour [ cou *à ] )
dábri,dábri( bouche courber )vt.dábiri.dábri.
dabri,dábri( bouche courber )vt.dábiri.dábri.
dábulu,dábulu( bouche tuyau )dáburu.dábulu.
dabulu,dábulu( bouche tuyau )dáburu.dábulu.
dàbulu,dàbulu( chanvre feuille )
dáburu,dáburu( bouche tuyau )dábulu.
daburu,dáburu( bouche tuyau )dábulu.
dácɛ̀,dácɛ̀( bouche ramasser )vr.
dacɛ,dácɛ̀( bouche ramasser )vr.
dacè,dácɛ̀( bouche ramasser )vr.
dácɛ̀n,dácɛ̀n( bouche moudre )vt.
dacɛn,dácɛ̀n( bouche moudre )vt.
dacèn,dácɛ̀n( bouche moudre )vt.
dáci,dáci( bouche trait )
daci,dáci( bouche trait )
dácogo,dácogo( créer manière )
dacogo,dácogo( créer manière )
dádà,Dádà→̌Dáuda.Dáwuda.
dada,Dádà→̌Dáuda.Dáwuda.
dáde,dáde( bouche se.taire )dáje;dáden.
dade,dáde( bouche se.taire )dáje;dáden.
dádè,dádè( bouche se.taire )vr.dájè;dádèn.
dáden,dáden( bouche se.taire )dáde.dáje;dáden.
daden,dáden( bouche se.taire )dáde.dáje;dáden.
dádèn,dádèn( bouche se.taire )vr.dádè.dájè;dádèn.
dádigi,dádigi( bouche presser )
dadigi,dádigi( bouche presser )
dádimi,dádimi( bouche souffrance )
dadimi,dádimi( bouche souffrance )
dádiya,dádiya( bouche bon.goût [ agréable *en verbe dynamique ] )
dadiya,dádiya( bouche bon.goût [ agréable *en verbe dynamique ] )
dádiyalan,dádiyalan( aiguiser [ bouche rendre.agréable [ agréable *en verbe dynamique ] ] *instrumental )
dadiyalan,dádiyalan( aiguiser [ bouche rendre.agréable [ agréable *en verbe dynamique ] ] *instrumental )
dádo,dádo→̌vt.
dado,dádo→̌vt.
dádòn,dádòn( bouche entrer )
dadon,dádòn( bouche entrer )
dádɔn,dádɔn( bouche connaître )
dadɔn,dádɔn( bouche connaître )
dadòn,dádɔn( bouche connaître )
dádɔnbali,dádɔnbali( connaître [ bouche connaître ] PTCP.NEG )
dadɔnbali,dádɔnbali( connaître [ bouche connaître ] PTCP.NEG )
dadònbali,dádɔnbali( connaître [ bouche connaître ] PTCP.NEG )
dádonkan,dádonkan( bouche entrer cou )
dadonkan,dádonkan( bouche entrer cou )
dádùgula,dádùgula( bouche terre *nom de lieu )
dadugula,dádùgula( bouche terre *nom de lieu )
dáduman,dáduman( bouche agréable [ agréable *adjectivateur ] )
daduman,dáduman( bouche agréable [ agréable *adjectivateur ] )
dáfa,dáfa( bouche remplir )vt.
dafa,dáfa( bouche remplir )vt.
dáfabali,dáfabali( compléter [ bouche remplir ] PTCP.NEG )
dafabali,dáfabali( compléter [ bouche remplir ] PTCP.NEG )
dáfaji,dáfaji( bouche remplir eau )
dafaji,dáfaji( bouche remplir eau )
dáfalan,dáfalan( compléter [ bouche remplir ] *instrumental )
dafalan,dáfalan( compléter [ bouche remplir ] *instrumental )
dáfalen,dáfalen( compléter [ bouche remplir ] *participe résultatif )
dafalen,dáfalen( compléter [ bouche remplir ] *participe résultatif )
dáfàlen,dáfàlen( bouche échanger )vr.
dáfalenya,dáfalenya( compléter [ bouche remplir ] *participe résultatif *abstractif )
dafalenya,dáfalenya( compléter [ bouche remplir ] *participe résultatif *abstractif )
dáfanɛ,dáfanɛ( bouche remplir langue )dáfanɛn.dáfanɛ.
dafanɛ,dáfanɛ( bouche remplir langue )dáfanɛn.dáfanɛ.
dafanè,dáfanɛ( bouche remplir langue )dáfanɛn.dáfanɛ.
dáfanɛn,dáfanɛn( bouche remplir langue )dáfanɛ.
dafanɛn,dáfanɛn( bouche remplir langue )dáfanɛ.
dafanèn,dáfanɛn( bouche remplir langue )dáfanɛ.
dáfara,dáfara( bouche diviser )
dafara,dáfara( bouche diviser )
dáfarakasi,dáfarakasi( bouche diviser pleurer )vi.
dafarakasi,dáfarakasi( bouche diviser pleurer )vi.
dáfasankɔrɔ,dáfasankɔrɔ( bouche résistant vieux )
dafasankɔrɔ,dáfasankɔrɔ( bouche résistant vieux )
dafasankòrò,dáfasankɔrɔ( bouche résistant vieux )
dáfata,dáfata( compléter [ bouche remplir ] *participe potentiel )
dafata,dáfata( compléter [ bouche remplir ] *participe potentiel )
dafe,Dafe→̌Daw.Ndaw.
dáfe,Dáfe→̌Voir :Daw.
dafe,Dáfe→̌Voir :Daw.
dáfɛ̀,dáfɛ̀( bouche par )
dafɛ,dáfɛ̀( bouche par )
dafè,dáfɛ̀( bouche par )
dàfe,dàfe→̌→ 3
dafe,dàfe→̌→ 3
dáfɛdugu,dáfɛdugu( auprès [ bouche par ] terre )
dafɛdugu,dáfɛdugu( auprès [ bouche par ] terre )
dafèdugu,dáfɛdugu( auprès [ bouche par ] terre )
dáfɛla,dáfɛla( auprès [ bouche par ] *nom de lieu )
dafɛla,dáfɛla( auprès [ bouche par ] *nom de lieu )
dafèla,dáfɛla( auprès [ bouche par ] *nom de lieu )
dáfele,dáfele( bouche germer )dáfalen.dáfɛlɛn.
dafele,dáfele( bouche germer )dáfalen.dáfɛlɛn.
dáfɛlɛn,dáfɛlɛn( bouche germer )dáfalen.dáfele.
dafɛlɛn,dáfɛlɛn( bouche germer )dáfalen.dáfele.
dafèlèn,dáfɛlɛn( bouche germer )dáfalen.dáfele.
dáfɛn,dáfɛn( créer chose )dánfɛn.
dafɛn,dáfɛn( créer chose )dánfɛn.
dafèn,dáfɛn( créer chose )dánfɛn.
dáfila,dáfila( jour deux )dáfla.
dafila,dáfila( jour deux )dáfla.
dáfìla,dáfìla( bouche deux )dáflà.
dáfili,dáfili( bouche erreur )dáfli.
dafili,dáfili( bouche erreur )dáfli.
dáfilici,dáfilici( bouche jeter commission )dáflici.
dafilici,dáfilici( bouche jeter commission )dáflici.
dáfilifìli,dáfilifìli( bouche jeter jeter )vt.dáflifli.
dafilifili,dáfilifìli( bouche jeter jeter )vt.dáflifli.
dáfin,dáfin( bouche noir )
dafin,dáfin( bouche noir )
dáfiɲɛ,dáfiɲɛ( bouche vent )dáfiyɛn.
dafiɲɛ,dáfiɲɛ( bouche vent )dáfiyɛn.
dafinyè,dáfiɲɛ( bouche vent )dáfiyɛn.
dáfiri,dáfiri( bouche renverser )vt.dáfri.
dafiri,dáfiri( bouche renverser )vt.dáfri.
dáfiyɛ,dáfiyɛ( bouche souffler )vt.dáfyɛ.
dafiyɛ,dáfiyɛ( bouche souffler )vt.dáfyɛ.
dafiyè,dáfiyɛ( bouche souffler )vt.dáfyɛ.
dáfiyɛn,dáfiyɛn( bouche vent )dáfiɲɛ.dáfiyɛn.
dafiyɛn,dáfiyɛn( bouche vent )dáfiɲɛ.dáfiyɛn.
dafiyèn,dáfiyɛn( bouche vent )dáfiɲɛ.dáfiyɛn.
dáfla,dáfla( jour deux )dáfila.dáfla.
dafla,dáfla( jour deux )dáfila.dáfla.
dáflà,dáflà( bouche deux )dáfìla.dáflà.
dáfli,dáfli( bouche erreur )dáfili.dáfli.
dafli,dáfli( bouche erreur )dáfili.dáfli.
dáflici,dáflici( bouche jeter commission )dáfilici.dáflici.
daflici,dáflici( bouche jeter commission )dáfilici.dáflici.
dáflifli,dáflifli( bouche jeter jeter )vt.dáfilifìli.dáflifli.
daflifli,dáflifli( bouche jeter jeter )vt.dáfilifìli.dáflifli.
dáfɔ,dáfɔ( bouche rater )vt.
dafɔ,dáfɔ( bouche rater )vt.
dafò,dáfɔ( bouche rater )vt.
dáfoni,dáfoni( bouche détacher )
dafoni,dáfoni( bouche détacher )
dáforon,dáforon( bouche aspirer )
daforon,dáforon( bouche aspirer )
dáfòron,dáfòron( bouche aspirer )vr.
dáfri,dáfri( bouche renverser )vt.dáfiri.dáfri.
dafri,dáfri( bouche renverser )vt.dáfiri.dáfri.
dàfu,dàfu( chanvre fibre )
dafu,dàfu( chanvre fibre )
dáfurugu,dáfurugu( bouche bon.ou.mauvais.côté )dáfuruku.dáfurugu.
dafurugu,dáfurugu( bouche bon.ou.mauvais.côté )dáfuruku.dáfurugu.
dáfuruku,dáfuruku( bouche bon.ou.mauvais.côté )dáfurugu.
dafuruku,dáfuruku( bouche bon.ou.mauvais.côté )dáfurugu.
dáfyɛ,dáfyɛ( bouche souffler )vt.Voir entrée principale :dáfiyɛ.
dafyɛ,dáfyɛ( bouche souffler )vt.Voir entrée principale :dáfiyɛ.
dafyè,dáfyɛ( bouche souffler )vt.Voir entrée principale :dáfiyɛ.
dága,dága→̌→ 57
daga,dága→̌→ 57
dàga,dàga→̌→ 199dàa.
dágabɔndala,dágabɔndala( assiéger sortir *je auprès [ bouche à ] )
dagabɔndala,dágabɔndala( assiéger sortir *je auprès [ bouche à ] )
dagabòndala,dágabɔndala( assiéger sortir *je auprès [ bouche à ] )
dàgadilala,dàgadilala( canari fabriquer *agent permanent )dàgadlala.
dagadilala,dàgadilala( canari fabriquer *agent permanent )dàgadlala.
dàgadlala,dàgadlala( canari fabriquer *agent permanent )dàgadilala.dàgadlala.
dagadlala,dàgadlala( canari fabriquer *agent permanent )dàgadilala.dàgadlala.
dàgadon,dàgadon( canari entrer )
dagadon,dàgadon( canari entrer )
dàgadonna,dàgadonna( canari entrer *agent permanent )
dagadonna,dàgadonna( canari entrer *agent permanent )
dágala,dágala→̌vt.
dagala,dágala→̌vt.
dágalaka,dágalaka( bouche )dágɛlɛkɛ.dágwɛlɛkɛ;dágalaka.
dagalaka,dágalaka( bouche )dágɛlɛkɛ.dágwɛlɛkɛ;dágalaka.
dágan,dágan→̌dánga.dágan.
dagan,dágan→̌dánga.dágan.
dàgan,dàgan→̌dànga.
dàganba,dàganba( arbre.Afzelia.africana *augmentatif )dàngaba.
daganba,dàganba( arbre.Afzelia.africana *augmentatif )dàngaba.
dágannan,dágannan( bouche chauffer *instrumental )dágwannan.
dagannan,dágannan( bouche chauffer *instrumental )dágwannan.
dàgannin,dàgannin( arbre.Afzelia.africana *diminutif )dànganin.
dagannin,dàgannin( arbre.Afzelia.africana *diminutif )dànganin.
dágaran,dágaran( bouche entraver )dágwaran.
dagaran,dágaran( bouche entraver )dágwaran.
dàgasigidagala,dàgasigidagala( canari asseoir canari à )Voir entrée principale :dàga-sìgi-dàga-lá.
dagasigidagala,dàgasigidagala( canari asseoir canari à )Voir entrée principale :dàga-sìgi-dàga-lá.
dàga-sìgi-dàga-lá,dàga-sìgi-dàga-lá( canari asseoir canari à )dàgasigidagala.
daga-sigi-daga-la,dàga-sìgi-dàga-lá( canari asseoir canari à )dàgasigidagala.
dágɛ,dágɛ( bouche blanc )dájɛ.dágɛ.
dagɛ,dágɛ( bouche blanc )dájɛ.dágɛ.
dagè,dágɛ( bouche blanc )dájɛ.dágɛ.
dágɛlɛkɛ,dágɛlɛkɛ( bouche )dágwɛlɛkɛ;dágalaka.
dagɛlɛkɛ,dágɛlɛkɛ( bouche )dágwɛlɛkɛ;dágalaka.
dagèlèkè,dágɛlɛkɛ( bouche )dágwɛlɛkɛ;dágalaka.
dágɛlɛn,dágɛlɛn( bouche difficile )dágwɛlɛn.
dagɛlɛn,dágɛlɛn( bouche difficile )dágwɛlɛn.
dagèlèn,dágɛlɛn( bouche difficile )dágwɛlɛn.
dágèn,dágèn( bouche )vr.dágwèn.
dagen,dágèn( bouche )vr.dágwèn.
dágɛn,dágɛn( bouche aiguiser )vt.dágwɛn.
dagɛn,dágɛn( bouche aiguiser )vt.dágwɛn.
dagèn,dágɛn( bouche aiguiser )vt.dágwɛn.
dágɛnnan,dágɛnnan( aiguiser [ bouche aiguiser ] *instrumental )dágwɛnnan.
dagɛnnan,dágɛnnan( aiguiser [ bouche aiguiser ] *instrumental )dágwɛnnan.
dagènnan,dágɛnnan( aiguiser [ bouche aiguiser ] *instrumental )dágwɛnnan.
dágeren,dágeren( bouche bouché )dágweren.
dageren,dágeren( bouche bouché )dágweren.
dagi-dagi,Dagi-Dagi→̌
dágɔbɛ,dágɔbɛ( bouche )dákɔbɛ.
dagɔbɛ,dágɔbɛ( bouche )dákɔbɛ.
dagòbè,dágɔbɛ( bouche )dákɔbɛ.
dágosi,dágosi( bouche battre )
dagosi,dágosi( bouche battre )
dágòsi,dágòsi( bouche battre )vt.dágɔ̀si.
dágɔ̀si,dágɔ̀si( bouche battre )vt.dágòsi.dágɔ̀si.
dagɔsi,dágɔ̀si( bouche battre )vt.dágòsi.dágɔ̀si.
dagòsi,dágɔ̀si( bouche battre )vt.dágòsi.dágɔ̀si.
dágu,dágu( bouche joindre )vt.dágun.dágu.
dagu,dágu( bouche joindre )vt.dágun.dágu.
dágun,dágun( bouche joindre )vt.dágu.
dagun,dágun( bouche joindre )vt.dágu.
dágunnifɛn,dágunnifɛn( bouche joindre *nom d'action chose )
dagunnifɛn,dágunnifɛn( bouche joindre *nom d'action chose )
dagunnifèn,dágunnifɛn( bouche joindre *nom d'action chose )
dàgwan,dàgwan( chanvre gombo )dàgan.dàgwan.
dagwan,dàgwan( chanvre gombo )dàgan.dàgwan.
dágwannan,dágwannan( bouche chauffer *instrumental )dágannan.dágwannan.
dagwannan,dágwannan( bouche chauffer *instrumental )dágannan.dágwannan.
dágwaran,dágwaran( bouche entraver )dágaran.dágwaran.
dagwaran,dágwaran( bouche entraver )dágaran.dágwaran.
dágwɛlɛkɛ,dágwɛlɛkɛ( bouche )dágɛlɛkɛ.dágwɛlɛkɛ;dágalaka.
dagwɛlɛkɛ,dágwɛlɛkɛ( bouche )dágɛlɛkɛ.dágwɛlɛkɛ;dágalaka.
dagwèlèkè,dágwɛlɛkɛ( bouche )dágɛlɛkɛ.dágwɛlɛkɛ;dágalaka.
dágwɛlɛn,dágwɛlɛn( bouche difficile )dágɛlɛn.dágwɛlɛn.
dagwɛlɛn,dágwɛlɛn( bouche difficile )dágɛlɛn.dágwɛlɛn.
dagwèlèn,dágwɛlɛn( bouche difficile )dágɛlɛn.dágwɛlɛn.
dágwèn,dágwèn( bouche )vr.dágèn.dágwèn.
dagwen,dágwèn( bouche )vr.dágèn.dágwèn.
dágwɛn,dágwɛn( bouche aiguiser )vt.dágɛn.dágwɛn.
dagwɛn,dágwɛn( bouche aiguiser )vt.dágɛn.dágwɛn.
dagwèn,dágwɛn( bouche aiguiser )vt.dágɛn.dágwɛn.
dágwɛnnan,dágwɛnnan( aiguiser [ bouche aiguiser ] *instrumental )dágɛnnan.dágwɛnnan.
dagwɛnnan,dágwɛnnan( aiguiser [ bouche aiguiser ] *instrumental )dágɛnnan.dágwɛnnan.
dagwènnan,dágwɛnnan( aiguiser [ bouche aiguiser ] *instrumental )dágɛnnan.dágwɛnnan.
dágweren,dágweren( bouche bouché )dágeren.dágweren.
dagweren,dágweren( bouche bouché )dágeren.dágweren.
dáhìrimɛ,dáhìrimɛ→̌→ 34dáyìrimɛ.Ar. dara:him 'drachmes'
dahirimɛ,dáhìrimɛ→̌→ 34dáyìrimɛ.Ar. dara:him 'drachmes'
dahirimè,dáhìrimɛ→̌→ 34dáyìrimɛ.Ar. dara:him 'drachmes'
dahomɛ,Dahomɛ→̌
dahomè,Dahomɛ→̌
dája,dája( bouche rendre.agréable [ agréable *en verbe dynamique ] )dádiya.dája.
daja,dája( bouche rendre.agréable [ agréable *en verbe dynamique ] )dádiya.dája.
dájà,dájà( bouche sécher )vt.
dájalan,dájalan( bouche sec )
dajalan,dájalan( bouche sec )
dàjan,dàjan( chanvre long )
dajan,dàjan( chanvre long )
dáje,dáje( bouche se.taire )dáde.dáden.
daje,dáje( bouche se.taire )dáde.dáden.
dájè,dájè( bouche se.taire )vr.dádè.dádèn.
dájɛ,dájɛ( bouche blanc )dágɛ.
dajɛ,dájɛ( bouche blanc )dágɛ.
dajè,dájɛ( bouche blanc )dágɛ.
dájɛ̀,dájɛ̀( bouche rater )vt.
dáji,dáji→̌→ 26vt.
daji,dáji→̌→ 26vt.
dájibɔn,dájibɔn( salive [ bouche eau ] répandre )
dajibɔn,dájibɔn( salive [ bouche eau ] répandre )
dajibòn,dájibɔn( salive [ bouche eau ] répandre )
dájifolofolo,dájifolofolo( salive [ bouche eau ] abandonner )
dajifolofolo,dájifolofolo( salive [ bouche eau ] abandonner )
dájìgin,dájìgin( bouche descendre )vt.
dajigin,dájìgin( bouche descendre )vt.
dájikanga,dájikanga( salive [ bouche eau ] écume )
dajikanga,dájikanga( salive [ bouche eau ] écume )
dájinɛ,dájinɛ( bouche esprit )
dajinɛ,dájinɛ( bouche esprit )
dajinè,dájinɛ( bouche esprit )
dájìra,dájìra( bouche montrer )dáyìra.
dajira,dájìra( bouche montrer )dáyìra.
dájɔ̀,dájɔ̀( bouche dresser )vr.
dajɔ,dájɔ̀( bouche dresser )vr.
dajò,dájɔ̀( bouche dresser )vr.
dájugu,dájugu( bouche méchant )
dajugu,dájugu( bouche méchant )
dájukɔrɔkuma,dájukɔrɔkuma( bouche derrière sous parole )
dajukɔrɔkuma,dájukɔrɔkuma( bouche derrière sous parole )
dajukòròkuma,dájukɔrɔkuma( bouche derrière sous parole )
dájuru,dájuru( bouche corde )
dajuru,dájuru( bouche corde )
dákabana,dákabana( bouche s'étonner *agent permanent )
dakabana,dákabana( bouche s'étonner *agent permanent )
dákabanamɔgɔ,dákabanamɔgɔ( extraordinaire [ bouche s'étonner *agent permanent ] homme )
dakabanamɔgɔ,dákabanamɔgɔ( extraordinaire [ bouche s'étonner *agent permanent ] homme )
dakabanamògò,dákabanamɔgɔ( extraordinaire [ bouche s'étonner *agent permanent ] homme )
dákajaalà,Dákajaalà→̌Dákajaalàn;Dákajaanà.
dakajaala,Dákajaalà→̌Dákajaalàn;Dákajaanà.
dákajaalàn,Dákajaalàn→̌Dákajaalà.Dákajaanà.
dakajaalan,Dákajaalàn→̌Dákajaalà.Dákajaanà.
dákajaanà,Dákajaanà→̌Dákajaalà.Dákajaalàn.
dakajaana,Dákajaanà→̌Dákajaalà.Dákajaalàn.
dákala,dákala( bouche tige )dákalama.
dakala,dákala( bouche tige )dákalama.
dákalama,dákalama( bouche tige *comme de )Voir entrée principale :dákala.
dakalama,dákalama( bouche tige *comme de )Voir entrée principale :dákala.
dákalan,dákalan( bouche coudre )Voir entrée principale :dákala.
dakalan,dákalan( bouche coudre )Voir entrée principale :dákala.
dákamana,dákamana( bouche s'étonner *agent permanent )dákabana.dákamana.
dakamana,dákamana( bouche s'étonner *agent permanent )dákabana.dákamana.
dákan,dákan( création sur )
dakan,dákan( création sur )
dákankun,dákankun( bouche sur tête )
dakankun,dákankun( bouche sur tête )
dákanma,dákanma( destin [ création sur ] *comme de )
dakanma,dákanma( destin [ création sur ] *comme de )
dákantigi,dákantigi( destin [ création sur ] maître )
dakantigi,dákantigi( destin [ création sur ] maître )
dakar,Dakar→̌Dákaro.Dakaru;Dakari.
dakari,Dakari→̌Dákaro.Dakaru;Dakar.
dákari,dákari( bouche casser )vt.
dakari,dákari( bouche casser )vt.
dákaro,Dákaro→̌→n.prop : 1Dakaru;Dakari;Dakar.
dakaro,Dákaro→̌→n.prop : 1Dakaru;Dakari;Dakar.
dakaru,Dakaru→̌Dákaro.Dakari;Dakar.
dákasa,dákasa( bouche odeur )
dakasa,dákasa( bouche odeur )
dákawuli,dákawuli( poser *infinitif se.lever )
dakawuli,dákawuli( poser *infinitif se.lever )
dákawuliteri,dákawuliteri( ami.intime [ poser *infinitif se.lever ] ami )
dakawuliteri,dákawuliteri( ami.intime [ poser *infinitif se.lever ] ami )
dákɛnɛ,dákɛnɛ( bouche clarté )
dakɛnɛ,dákɛnɛ( bouche clarté )
dakènè,dákɛnɛ( bouche clarté )
dákɛɲɛ,dákɛɲɛ( bouche égaliser )vt.dákɛnyɛ.
dakɛɲɛ,dákɛɲɛ( bouche égaliser )vt.dákɛnyɛ.
dakènyè,dákɛɲɛ( bouche égaliser )vt.dákɛnyɛ.
dákɛnɛmaya,dákɛnɛmaya( poser clarté *à *abstractif )dánkɛnɛmaya.dákɛnɛmaya.
dakɛnɛmaya,dákɛnɛmaya( poser clarté *à *abstractif )dánkɛnɛmaya.dákɛnɛmaya.
dakènèmaya,dákɛnɛmaya( poser clarté *à *abstractif )dánkɛnɛmaya.dákɛnɛmaya.
dákɛnyɛ,dákɛnyɛ( bouche égaliser )vt.Voir entrée principale :dákɛɲɛ.
dakɛnyɛ,dákɛnyɛ( bouche égaliser )vt.Voir entrée principale :dákɛɲɛ.
dakènyè,dákɛnyɛ( bouche égaliser )vt.Voir entrée principale :dákɛɲɛ.
dáko,dáko( créer affaire )
dako,dáko( créer affaire )
dákɔbɛ,dákɔbɛ( bouche )Voir entrée principale :dágɔbɛ.
dakɔbɛ,dákɔbɛ( bouche )Voir entrée principale :dágɔbɛ.
dakòbè,dákɔbɛ( bouche )Voir entrée principale :dágɔbɛ.
dákobɔrɔsi,dákobɔrɔsi( bouche laver brosse )
dakobɔrɔsi,dákobɔrɔsi( bouche laver brosse )
dakobòròsi,dákobɔrɔsi( bouche laver brosse )
dákojugu,dákojugu( créer affaire méchant )
dakojugu,dákojugu( créer affaire méchant )
dákolo,dákolo( bouche os )
dakolo,dákolo( bouche os )
dákolon,dákolon( bouche usagé )
dakolon,dákolon( bouche usagé )
dákɔlɔsila,dákɔlɔsila( bouche surveiller *agent permanent )
dakɔlɔsila,dákɔlɔsila( bouche surveiller *agent permanent )
dakòlòsila,dákɔlɔsila( bouche surveiller *agent permanent )
dákɔnkɔn,dákɔnkɔn( bouche frapper )vt.
dakɔnkɔn,dákɔnkɔn( bouche frapper )vt.
dakònkòn,dákɔnkɔn( bouche frapper )vt.
dákɔnɔna,dákɔnɔna( bouche ventre *nom de lieu )
dakɔnɔna,dákɔnɔna( bouche ventre *nom de lieu )
dakònòna,dákɔnɔna( bouche ventre *nom de lieu )
dákɔrɔbɔ,dákɔrɔbɔ( bouche dessous sortir )vt.
dakɔrɔbɔ,dákɔrɔbɔ( bouche dessous sortir )vt.
dakòròbò,dákɔrɔbɔ( bouche dessous sortir )vt.
dákɔrɔbɔla,dákɔrɔbɔla( chercher.querelle [ bouche dessous sortir ] *agent permanent )
dakɔrɔbɔla,dákɔrɔbɔla( chercher.querelle [ bouche dessous sortir ] *agent permanent )
dakòròbòla,dákɔrɔbɔla( chercher.querelle [ bouche dessous sortir ] *agent permanent )
dákɔrɔdòn,dákɔrɔdòn( bouche dessous entrer )vt.
dakɔrɔdon,dákɔrɔdòn( bouche dessous entrer )vt.
dakòròdon,dákɔrɔdòn( bouche dessous entrer )vt.
dákoron,dákoron( bouche cerner )vt.
dakoron,dákoron( bouche cerner )vt.
dákɔrɔtà,dákɔrɔtà( bouche dessous prendre )vt.
dakɔrɔta,dákɔrɔtà( bouche dessous prendre )vt.
dakòròta,dákɔrɔtà( bouche dessous prendre )vt.
dákosafunɛ,dákosafunɛ( bouche laver savon )
dakosafunɛ,dákosafunɛ( bouche laver savon )
dakosafunè,dákosafunɛ( bouche laver savon )
dáku,dáku( bouche queue )
daku,dáku( bouche queue )
dàkumu,dàkumu( chanvre aigre )
dakumu,dàkumu( chanvre aigre )
dákun,dákun( bouche tête )
dakun,dákun( bouche tête )
dákurun,dákurun( bouche court )
dakurun,dákurun( bouche court )
dákuruɲa,dákuruɲa( bouche plier fois )dákuruɲɛ.dákuruɲa.
dakuruɲa,dákuruɲa( bouche plier fois )dákuruɲɛ.dákuruɲa.
dakurunya,dákuruɲa( bouche plier fois )dákuruɲɛ.dákuruɲa.
dákuruɲɛ,dákuruɲɛ( bouche plier fois )dákuruɲa.
dakuruɲɛ,dákuruɲɛ( bouche plier fois )dákuruɲa.
dakurunyè,dákuruɲɛ( bouche plier fois )dákuruɲa.
dákurunkan,dákurunkan( bouche court cou )
dakurunkan,dákurunkan( bouche court cou )
dakuwo,Dakuwo→̌Dɛna(Agriculteurs. Beaucoup sont chrétiens.)
dála,dála( bouche à )dárɔ.
dala,dála( bouche à )dárɔ.
dàla,dàla→̌→ 24bìla;dlà.
dalaba,Dalaba→̌
dálabɛ̀n,dálabɛ̀n( bouche préparer [ *causatif se.rencontrer ] )vt.dábɛ̀n.
dalabɛn,dálabɛ̀n( bouche préparer [ *causatif se.rencontrer ] )vt.dábɛ̀n.
dalabèn,dálabɛ̀n( bouche préparer [ *causatif se.rencontrer ] )vt.dábɛ̀n.
dálabi,dálabi( bouche remplacer )vt.
dalabi,dálabi( bouche remplacer )vt.
dálabɔ,dálabɔ( bouche faire.sortir [ *causatif sortir ] )vt.
dalabɔ,dálabɔ( bouche faire.sortir [ *causatif sortir ] )vt.
dalabò,dálabɔ( bouche faire.sortir [ *causatif sortir ] )vt.
dálacaman,dálacaman( bouche.active [ bouche à ] nombreux [ nombreux *adjectivateur ] )
dalacaman,dálacaman( bouche.active [ bouche à ] nombreux [ nombreux *adjectivateur ] )
dálacɛ,dálacɛ( bouche ramasser [ *causatif ramasser ] )
dalacɛ,dálacɛ( bouche ramasser [ *causatif ramasser ] )
dalacè,dálacɛ( bouche ramasser [ *causatif ramasser ] )
dálacɛ̀,dálacɛ̀( bouche ramasser [ *causatif ramasser ] )vt.
dáladiya,dáladiya( bouche à bon.goût [ agréable *en verbe dynamique ] )
daladiya,dáladiya( bouche à bon.goût [ agréable *en verbe dynamique ] )
dáladumuni,dáladumuni( bouche *nom de lieu action.de.manger [ manger *nom d'action ] )
daladumuni,dáladumuni( bouche *nom de lieu action.de.manger [ manger *nom d'action ] )
dálafa,dálafa( bouche remplir [ *causatif remplir ] )vt.
dalafa,dálafa( bouche remplir [ *causatif remplir ] )vt.
dálafɛgɛn,dálafɛgɛn( bouche.active [ bouche à ] léger )dálafiɲɛ;dálafiyɛn;dálafyɛn.
dalafɛgɛn,dálafɛgɛn( bouche.active [ bouche à ] léger )dálafiɲɛ;dálafiyɛn;dálafyɛn.
dalafègèn,dálafɛgɛn( bouche.active [ bouche à ] léger )dálafiɲɛ;dálafiyɛn;dálafyɛn.
dálafiɲɛ,dálafiɲɛ( bouche.active [ bouche à ] léger )dálafɛgɛn.dálafiyɛn;dálafyɛn.
dalafiɲɛ,dálafiɲɛ( bouche.active [ bouche à ] léger )dálafɛgɛn.dálafiyɛn;dálafyɛn.
dalafinyè,dálafiɲɛ( bouche.active [ bouche à ] léger )dálafɛgɛn.dálafiyɛn;dálafyɛn.
dálafiyɛn,dálafiyɛn( bouche.active [ bouche à ] léger )dálafɛgɛn.dálafiɲɛ;dálafyɛn.
dalafiyɛn,dálafiyɛn( bouche.active [ bouche à ] léger )dálafɛgɛn.dálafiɲɛ;dálafyɛn.
dalafiyèn,dálafiyɛn( bouche.active [ bouche à ] léger )dálafɛgɛn.dálafiɲɛ;dálafyɛn.
dálafyɛn,dálafyɛn( bouche.active [ bouche à ] léger )dálafɛgɛn.dálafiɲɛ;dálafiyɛn;dálafyɛn.
dalafyɛn,dálafyɛn( bouche.active [ bouche à ] léger )dálafɛgɛn.dálafiɲɛ;dálafiyɛn;dálafyɛn.
dalafyèn,dálafyɛn( bouche.active [ bouche à ] léger )dálafɛgɛn.dálafiɲɛ;dálafiyɛn;dálafyɛn.
dálagɛlɛn,dálagɛlɛn( bouche.active [ bouche à ] difficile )dámagɛlɛn;dárɔgɛlɛn.
dalagɛlɛn,dálagɛlɛn( bouche.active [ bouche à ] difficile )dámagɛlɛn;dárɔgɛlɛn.
dalagèlèn,dálagɛlɛn( bouche.active [ bouche à ] difficile )dámagɛlɛn;dárɔgɛlɛn.
dálagirin,dálagirin( bouche.active [ bouche à ] lourd )
dalagirin,dálagirin( bouche.active [ bouche à ] lourd )
dálaja,dálaja( bouche à sécheresse )dámaja.
dalaja,dálaja( bouche à sécheresse )dámaja.
dálajɛ̀,dálajɛ̀( bouche réunir [ *causatif assembler ] )vt.
dalajɛ,dálajɛ̀( bouche réunir [ *causatif assembler ] )vt.
dalajè,dálajɛ̀( bouche réunir [ *causatif assembler ] )vt.
dálajugu,dálajugu( bouche.active [ bouche à ] méchant )
dalajugu,dálajugu( bouche.active [ bouche à ] méchant )
dálakà,dálakà( bouche ouvrir )vr.
dalaka,dálakà( bouche ouvrir )vr.
dálakan,dálakan( bouche à cou )dárɔkan.
dalakan,dálakan( bouche à cou )dárɔkan.
dálakango,dálakango( voeu [ bouche à cou ] désagréable )dárɔkango.
dalakango,dálakango( voeu [ bouche à cou ] désagréable )dárɔkango.
dálakɛɲɛ,dálakɛɲɛ( bouche rendre.égal [ *causatif égaliser ] )dálakɛnyɛ.
dalakɛɲɛ,dálakɛɲɛ( bouche rendre.égal [ *causatif égaliser ] )dálakɛnyɛ.
dalakènyè,dálakɛɲɛ( bouche rendre.égal [ *causatif égaliser ] )dálakɛnyɛ.
dálakɛnyɛ,dálakɛnyɛ( bouche rendre.égal [ *causatif égaliser ] )Voir entrée principale :dálakɛɲɛ.
dalakɛnyɛ,dálakɛnyɛ( bouche rendre.égal [ *causatif égaliser ] )Voir entrée principale :dálakɛɲɛ.
dálako,dálako( bouche à affaire )dárɔko.
dalako,dálako( bouche à affaire )dárɔko.
dálakon,dálakon( bouche à porte )
dalakon,dálakon( bouche à porte )
dálakɔrɔbɔ,dálakɔrɔbɔ( bouche à essayer [ dessous sortir ] )vt.
dalakɔrɔbɔ,dálakɔrɔbɔ( bouche à essayer [ dessous sortir ] )vt.
dalakòròbò,dálakɔrɔbɔ( bouche à essayer [ dessous sortir ] )vt.
dálakuma,dálakuma( bouche à parole )
dalakuma,dálakuma( bouche à parole )
dálakuna,dálakuna( bouche.active [ bouche à ] amer )dálakunan.
dalakuna,dálakuna( bouche.active [ bouche à ] amer )dálakunan.
dálakunan,dálakunan( bouche.active [ bouche à ] amer )dálakuna.dálakunan.
dalakunan,dálakunan( bouche.active [ bouche à ] amer )dálakuna.dálakunan.
dálakùru,dálakùru( bouche plier [ *causatif plier ] )vt.
dalakuru,dálakùru( bouche plier [ *causatif plier ] )vt.
dálama,dálama( bouche *en tant que )
dalama,dálama( bouche *en tant que )
dálamaa,dálamaa( bouche remuer [ *causatif toucher ] )Voir entrée principale :dálamaga.
dalamaa,dálamaa( bouche remuer [ *causatif toucher ] )Voir entrée principale :dálamaga.
dálamàa,dálamàa( bouche remuer [ *causatif toucher ] )vt.Voir entrée principale :dálamàga.
dálamaga,dálamaga( bouche remuer [ *causatif toucher ] )dálamaa.
dalamaga,dálamaga( bouche remuer [ *causatif toucher ] )dálamaa.
dálamàga,dálamàga( bouche remuer [ *causatif toucher ] )vt.dálamàa.
dálamatɔ,dálamatɔ( bouche *en tant que *statif )
dalamatɔ,dálamatɔ( bouche *en tant que *statif )
dalamatò,dálamatɔ( bouche *en tant que *statif )
dálamɛlɛkun,dálamɛlɛkun( bouche *nom de lieu engloutir )
dalamɛlɛkun,dálamɛlɛkun( bouche *nom de lieu engloutir )
dalamèlèkun,dálamɛlɛkun( bouche *nom de lieu engloutir )
dálaminɛ,dálaminɛ( bouche maintenir [ *causatif attraper ] )
dalaminɛ,dálaminɛ( bouche maintenir [ *causatif attraper ] )
dalaminè,dálaminɛ( bouche maintenir [ *causatif attraper ] )
dálamìnɛ,dálamìnɛ( bouche maintenir [ *causatif attraper ] )vt.
dálamisɛn,dálamisɛn( bouche.active [ bouche à ] petit )
dalamisɛn,dálamisɛn( bouche.active [ bouche à ] petit )
dalamisèn,dálamisɛn( bouche.active [ bouche à ] petit )
dálamìsɛnya,dálamìsɛnya( bavard [ bouche.active [ bouche à ] petit ] *abstractif )vt.
dalamisɛnya,dálamìsɛnya( bavard [ bouche.active [ bouche à ] petit ] *abstractif )vt.
dalamisènya,dálamìsɛnya( bavard [ bouche.active [ bouche à ] petit ] *abstractif )vt.
dálan,dálan( poser *instrumental )dílan.dlán.
dalan,dálan( poser *instrumental )dílan.dlán.
dálandi,dálandi( bouche.active [ bouche à ] agréable )dámandi;dárɔndi.
dalandi,dálandi( bouche.active [ bouche à ] agréable )dámandi;dárɔndi.
dálango,dálango( bouche.active [ bouche à ] désagréable )dámango.
dalango,dálango( bouche.active [ bouche à ] désagréable )dámango.
dálaɲini,dálaɲini( bouche chercher [ *causatif chercher ] )
dalaɲini,dálaɲini( bouche chercher [ *causatif chercher ] )
dalanyini,dálaɲini( bouche chercher [ *causatif chercher ] )
dálankolon,dálankolon( bouche vide [ *causatif vide ] )dárɔnkolon.
dalankolon,dálankolon( bouche vide [ *causatif vide ] )dárɔnkolon.
dálannabana,dálannabana( lit [ poser *instrumental ] à maladie )dílannabana.dlánnabana.
dalannabana,dálannabana( lit [ poser *instrumental ] à maladie )dílannabana.dlánnabana.
dálasà,dálasà( bouche faire.mourir [ *causatif mourir ] )vt.dárɔsà.
dalasa,dálasà( bouche faire.mourir [ *causatif mourir ] )vt.dárɔsà.
dàlasaɲɔ,dàlasaɲɔ( lac petit.mil [ mil ] )dlàsaɲɔ.
dalasaɲɔ,dàlasaɲɔ( lac petit.mil [ mil ] )dlàsaɲɔ.
dalasanyò,dàlasaɲɔ( lac petit.mil [ mil ] )dlàsaɲɔ.
dálasi,dálasi→̌→ 2dálasì.
dalasi,dálasi→̌→ 2dálasì.
dálasigi,dálasigi( bouche à position.assise )
dalasigi,dálasigi( bouche à position.assise )
dálasìgi,dálasìgi( bouche à asseoir )vt.
dálasɔ̀n,dálasɔ̀n( bouche à accepter )vt.
dalasɔn,dálasɔ̀n( bouche à accepter )vt.
dalasòn,dálasɔ̀n( bouche à accepter )vt.
dálasuma,dálasuma( bouche.active [ bouche à ] frais )
dalasuma,dálasuma( bouche.active [ bouche à ] frais )
dálateli,dálateli( bouche.active [ bouche à ] rapide )
dalateli,dálateli( bouche.active [ bouche à ] rapide )
dálateliya,dálateliya( moulin.à.paroles [ bouche.active [ bouche à ] rapide ] *abstractif )
dalateliya,dálateliya( moulin.à.paroles [ bouche.active [ bouche à ] rapide ] *abstractif )
dáli,dáli( poser *nom d'action )
dali,dáli( poser *nom d'action )
daliba,Daliba→̌
dáliba,dáliba( création [ créer *nom d'action ] *augmentatif )
daliba,dáliba( création [ créer *nom d'action ] *augmentatif )
dálibana,dálibana( action.de.poser [ poser *nom d'action ] maladie )
dalibana,dálibana( action.de.poser [ poser *nom d'action ] maladie )
dálifini,dálifini( création [ créer *nom d'action ] tissu )
dalifini,dálifini( création [ créer *nom d'action ] tissu )
dàlilu,dàlilu→̌→ 110dàlu.Ar. dalil 'indication'
dalilu,dàlilu→̌→ 110dàlu.Ar. dalil 'indication'
dàliluma,dàliluma( cause *comme de )dàluma.
daliluma,dàliluma( cause *comme de )dàluma.
dàliluntan,dàliluntan( cause *privatif )dàluntan.
daliluntan,dàliluntan( cause *privatif )dàluntan.
dàliluya,dàliluya( cause *abstractif )dàluya.
daliluya,dàliluya( cause *abstractif )dàluya.
daliminiyɔmu,daliminiyɔmu→̌→ 2aliminiyɔmu.daliminiyɔmu.Ar. aluminium
daliminiyòmu,daliminiyɔmu→̌→ 2aliminiyɔmu.daliminiyɔmu.Ar. aluminium
daloba,Daloba→̌
dàlu,dàlu→̌dàlilu.dàlu.Ar. dalil 'indication'
dalu,dàlu→̌dàlilu.dàlu.Ar. dalil 'indication'
dàluma,dàluma( cause *comme de )dàliluma.dàluma.
daluma,dàluma( cause *comme de )dàliluma.dàluma.
dàluntan,dàluntan( cause *privatif )dàliluntan.dàluntan.
daluntan,dàluntan( cause *privatif )dàliluntan.dàluntan.
dàluya,dàluya( cause *abstractif )dàliluya.dàluya.
daluya,dàluya( cause *abstractif )dàliluya.dàluya.
dáma,dáma→̌→ 5
dama,dáma→̌→ 5
dàma,dàma( limite *à )dànma.
dámàda,dámàda( bouche incliner [ *connecteur poser ] )vr.
damada,dámàda( bouche incliner [ *connecteur poser ] )vr.
dàmada,dàmada( puits.de.mine.d'or bouche )Voir entrée principale :dàmanda.
dámadama,dámadama→̌→ 35
damadama,dámadama→̌→ 35
dàmadàma,dàmadàma→̌dàma-dàma.dàmadàma.
dàma-dàma,dàma-dàma→̌dàmadàma.
dama-dama,dàma-dàma→̌dàmadàma.
dámadɔ,dámadɔ( nombre [ compte *comme de ] certain )dánmadɔ.
damadɔ,dámadɔ( nombre [ compte *comme de ] certain )dánmadɔ.
damadò,dámadɔ( nombre [ compte *comme de ] certain )dánmadɔ.
dàmadɔnbali,dàmadɔnbali( limite [ limite *à ] connaître PTCP.NEG )
damadɔnbali,dàmadɔnbali( limite [ limite *à ] connaître PTCP.NEG )
damadònbali,dàmadɔnbali( limite [ limite *à ] connaître PTCP.NEG )
dámadɔnin,dámadɔnin( quelques [ nombre [ compte *comme de ] certain ] *diminutif )
damadɔnin,dámadɔnin( quelques [ nombre [ compte *comme de ] certain ] *diminutif )
damadònin,dámadɔnin( quelques [ nombre [ compte *comme de ] certain ] *diminutif )
dámagɛlɛn,dámagɛlɛn( bouche.active [ bouche *connecteur ] difficile )dálagɛlɛn.dárɔgɛlɛn.
damagɛlɛn,dámagɛlɛn( bouche.active [ bouche *connecteur ] difficile )dálagɛlɛn.dárɔgɛlɛn.
damagèlèn,dámagɛlɛn( bouche.active [ bouche *connecteur ] difficile )dálagɛlɛn.dárɔgɛlɛn.
dámaja,dámaja( bouche *à sécheresse )Voir entrée principale :dálaja.
damaja,dámaja( bouche *à sécheresse )Voir entrée principale :dálaja.
dámajalan,dámajalan( sec )ntámajalan.
damajalan,dámajalan( sec )ntámajalan.
dámajatɔ,dámajatɔ( bouche *comme de sécher *statif )
damajatɔ,dámajatɔ( bouche *comme de sécher *statif )
damajatò,dámajatɔ( bouche *comme de sécher *statif )
dàmajira,dàmajira( limite [ limite *à ] montrer )dàmayira.
damajira,dàmajira( limite [ limite *à ] montrer )dàmayira.
dámakasi,dámakasi( bouche plaindre [ *connecteur pleurer ] )
damakasi,dámakasi( bouche plaindre [ *connecteur pleurer ] )
dámakàsi,dámakàsi( bouche plaindre [ *connecteur pleurer ] )
dàmakɛɲɛ,dàmakɛɲɛ( limite [ limite *à ] égaliser )dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
damakɛɲɛ,dàmakɛɲɛ( limite [ limite *à ] égaliser )dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
damakènyè,dàmakɛɲɛ( limite [ limite *à ] égaliser )dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
dàmakɛnyɛ,dàmakɛnyɛ( limite [ limite *à ] égaliser )dàmakɛɲɛ.dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
damakɛnyɛ,dàmakɛnyɛ( limite [ limite *à ] égaliser )dàmakɛɲɛ.dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
dáman,dáman→̌ntáma;dáma.
daman,dáman→̌ntáma;dáma.
dàman,Dàman→̌
dàmana,dàmana( limite endroit *mental1 )dànmana;dànmanata.
damana,dàmana( limite endroit *mental1 )dànmana;dànmanata.
dàmanata,dàmanata( limite endroit *mental2 )dànmanata.
damanata,dàmanata( limite endroit *mental2 )dànmanata.
dàmanda,dàmanda( puits.de.mine.d'or bouche )dàmada.
damanda,dàmanda( puits.de.mine.d'or bouche )dàmada.
dámandi,dámandi( bouche.active [ bouche *connecteur ] agréable )dálandi.dárɔndi.
damandi,dámandi( bouche.active [ bouche *connecteur ] agréable )dálandi.dárɔndi.
dámango,dámango( bouche *connecteur désagréable )dálango.
damango,dámango( bouche *connecteur désagréable )dálango.
dámaɲini,dámaɲini( bouche chercher.à.atteindre [ *connecteur chercher ] )vt.
damaɲini,dámaɲini( bouche chercher.à.atteindre [ *connecteur chercher ] )vt.
damanyini,dámaɲini( bouche chercher.à.atteindre [ *connecteur chercher ] )vt.
dámaɲinikɛla,dámaɲinikɛla( quémander.de.la.nourriture [ bouche chercher.à.atteindre [ *connecteur chercher ] ] faire *agent permanent )
damaɲinikɛla,dámaɲinikɛla( quémander.de.la.nourriture [ bouche chercher.à.atteindre [ *connecteur chercher ] ] faire *agent permanent )
damanyinikèla,dámaɲinikɛla( quémander.de.la.nourriture [ bouche chercher.à.atteindre [ *connecteur chercher ] ] faire *agent permanent )
dàmanta,dàmanta→̌dàmantan.dàmanta;dànmantan.
damanta,dàmanta→̌dàmantan.dàmanta;dànmantan.
dàmantan,dàmantan→̌→ 8dàmanta;dànmantan.
damantan,dàmantan→̌→ 8dàmanta;dànmantan.
damasi,Damasi→̌
dàmatɛmɛ,dàmatɛmɛ( limite [ limite *à ] passer )dànmatɛmɛ.
damatɛmɛ,dàmatɛmɛ( limite [ limite *à ] passer )dànmatɛmɛ.
damatèmè,dàmatɛmɛ( limite [ limite *à ] passer )dànmatɛmɛ.
dàmatɛ̀mɛ,dàmatɛ̀mɛ( limite [ limite *à ] passer )dànmatɛ̀mɛ.
dàmayira,dàmayira( limite [ limite *à ] montrer )dàmajira.dàmayira.
damayira,dàmayira( limite [ limite *à ] montrer )dàmajira.dàmayira.
dámìna,dámìna( bouche attraper )dámìnɛ.dámìna.
damina,dámìna( bouche attraper )dámìnɛ.dámìna.
dáminɛ,dáminɛ( bouche attraper )
daminɛ,dáminɛ( bouche attraper )
daminè,dáminɛ( bouche attraper )
dámìnɛ,dámìnɛ( bouche attraper )dámìna.
damiye,damiye→̌
dàmiyo,dàmiyo→̌
damiyo,dàmiyo→̌
dámɔ,dámɔ( bouche fouiller )vr.
damɔ,dámɔ( bouche fouiller )vr.
damò,dámɔ( bouche fouiller )vr.
damu,Damu→̌
dámù,dámù( bouche enduire )vt.dámùn.
damu,dámù( bouche enduire )vt.dámùn.
damubɔ,damubɔ→̌→ 1
damubò,damubɔ→̌→ 1
dámuguri,dámuguri( bouche remuer )vr.
damuguri,dámuguri( bouche remuer )vr.
dámùn,dámùn( bouche enduire )vt.dámù.dámùn.
damun,dámùn( bouche enduire )vt.dámù.dámùn.
dámunu,dámunu( bouche tourner )vr.
damunu,dámunu( bouche tourner )vr.
dán,dán→̌Voir entrée principale :dá.
dan,dán→̌Voir entrée principale :dá.
dàn,dàn→̌→ 269
dána,dána→̌→ 64
dana,dána→̌→ 64
dáɲa,dáɲa( poser fois )dáɲɛ.dáɲa.
daɲa,dáɲa( poser fois )dáɲɛ.dáɲa.
danya,dáɲa( poser fois )dáɲɛ.dáɲa.
dàna,dàna→̌dàanɛ.dàana.
dana,dàna→̌dàanɛ.dàana.
dànajugu,dànajugu( comportement méchant )dàanɛjugu.dàanajugu;dànajugu.
danajugu,dànajugu( comportement méchant )dàanɛjugu.dàanajugu;dànajugu.
dánan,dánan→̌
danan,dánan→̌
dàŋaniya,dàŋaniya→̌→ 2dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
daŋaniya,dàŋaniya→̌→ 2dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dánanjugu,dánanjugu( méchant )
dananjugu,dánanjugu( méchant )
dánaya,dánaya( foi [ poser *je à ] *abstractif )dánnaya.dánaya.
danaya,dánaya( foi [ poser *je à ] *abstractif )dánnaya.dánaya.
danba,Danba→̌
dànbá,Dànbá→̌
danba,Dànbá→̌
dánbaa,dánbaa( créer *agent occasionnel )dábaa.dábaga;dánbaga;dánbaa.
danbaa,dánbaa( créer *agent occasionnel )dábaa.dábaga;dánbaga;dánbaa.
dánbaga,dánbaga( créer *agent occasionnel )dábaa.dábaga;dánbaga;dánbaa.
danbaga,dánbaga( créer *agent occasionnel )dábaa.dábaga;dánbaga;dánbaa.
danbana,Danbana→̌
dànbe,dànbe→̌→ 205
danbe,dànbe→̌→ 205
dànbele,Dànbele→̌Dènbele.Dànbɛlɛ.
danbele,Dànbele→̌Dènbele.Dànbɛlɛ.
dànbɛlɛ,Dànbɛlɛ→̌Dènbele.Dànbele.
danbɛlɛ,Dànbɛlɛ→̌Dènbele.Dànbele.
danbèlè,Dànbɛlɛ→̌Dènbele.Dànbele.
dànbilen,dànbilen( rouge )dànblen.
danbilen,dànbilen( rouge )dànblen.
dànblen,dànblen( rouge )dànbilen.dànblen.
danblen,dànblen( rouge )dànbilen.dànblen.
dànbɔ,dànbɔ( limite sortir )vt.
danbɔ,dànbɔ( limite sortir )vt.
danbò,dànbɔ( limite sortir )vt.
dàncɛ,dàncɛ( limite milieu )
dancɛ,dàncɛ( limite milieu )
dancè,dàncɛ( limite milieu )
dàncɛbɔ́,dàncɛbɔ́( frontière [ limite milieu ] sortir )
dancɛbɔ,dàncɛbɔ́( frontière [ limite milieu ] sortir )
dancèbò,dàncɛbɔ́( frontière [ limite milieu ] sortir )
dánda,dánda→̌
danda,dánda→̌
dànda,dànda→̌dɛ̀ndɛ.dɛ̀ndɛn;dɛ̀ɛndɛɛn;dɛ̀ɛndɛ;dànda.
dandugu,Dandugu→̌
dáɲɛ,dáɲɛ( poser fois )dáɲa.
daɲɛ,dáɲɛ( poser fois )dáɲa.
danyè,dáɲɛ( poser fois )dáɲa.
dáɲɛburuju,dáɲɛburuju( fois [ poser fois ] origine )
daɲɛburuju,dáɲɛburuju( fois [ poser fois ] origine )
danyèburuju,dáɲɛburuju( fois [ poser fois ] origine )
dáɲɛdili,dáɲɛdili( fois [ poser fois ] racine )dáɲɛgili.
daɲɛdili,dáɲɛdili( fois [ poser fois ] racine )dáɲɛgili.
danyèdili,dáɲɛdili( fois [ poser fois ] racine )dáɲɛgili.
dáɲɛgafe,dáɲɛgafe( fois [ poser fois ] livre )
daɲɛgafe,dáɲɛgafe( fois [ poser fois ] livre )
danyègafe,dáɲɛgafe( fois [ poser fois ] livre )
dáɲɛgili,dáɲɛgili( fois [ poser fois ] racine )dáɲɛdili.dáɲɛgili.
daɲɛgili,dáɲɛgili( fois [ poser fois ] racine )dáɲɛdili.dáɲɛgili.
danyègili,dáɲɛgili( fois [ poser fois ] racine )dáɲɛdili.dáɲɛgili.
dáɲɛkun,dáɲɛkun( bouche devant tête )
daɲɛkun,dáɲɛkun( bouche devant tête )
danyèkun,dáɲɛkun( bouche devant tête )
danemariki,Danemariki→̌
dánɛ̀ri,dánɛ̀ri( bouche )vr.
danɛri,dánɛ̀ri( bouche )vr.
danèri,dánɛ̀ri( bouche )vr.
dáɲɛsɛbɛn,dáɲɛsɛbɛn( fois [ poser fois ] écrit )
daɲɛsɛbɛn,dáɲɛsɛbɛn( fois [ poser fois ] écrit )
danyèsèbèn,dáɲɛsɛbɛn( fois [ poser fois ] écrit )
dáɲɛsure,dáɲɛsure( fois [ poser fois ] abandonné )
daɲɛsure,dáɲɛsure( fois [ poser fois ] abandonné )
danyèsure,dáɲɛsure( fois [ poser fois ] abandonné )
dànfara,dànfara( limite diviser )
danfara,dànfara( limite diviser )
dànfára,dànfára( limite diviser )vt.
dànfaransi,dànfaransi→̌
danfaransi,dànfaransi→̌
dánfɛn,dánfɛn( créer chose )Voir entrée principale :dáfɛn.
danfɛn,dánfɛn( créer chose )Voir entrée principale :dáfɛn.
danfèn,dánfɛn( créer chose )Voir entrée principale :dáfɛn.
danfin,Danfin→̌
dànfin,dànfin→̌
danfin,dànfin→̌
dánga,dánga→̌→ 4dágan.
danga,dánga→̌→ 4dágan.
dànga,dànga→̌dàan.dànga.
dàngaba,dàngaba( arbre.Afzelia.africana *augmentatif )Voir entrée principale :dàganba.
dangaba,dàngaba( arbre.Afzelia.africana *augmentatif )Voir entrée principale :dàganba.
dángaden,dángaden( malédiction enfant )
dangaden,dángaden( malédiction enfant )
dángadenya,dángadenya( maudit [ malédiction enfant ] *abstractif )vt.
dangadenya,dángadenya( maudit [ malédiction enfant ] *abstractif )vt.
dàngala,dàngala→̌→ 2dànkalan.dànkaran;dàngala.
dangala,dàngala→̌→ 2dànkalan.dànkaran;dàngala.
dángalikuma,dángalikuma( maudire *nom d'action parole )
dangalikuma,dángalikuma( maudire *nom d'action parole )
dángan,dángan→̌dánkan.dángan.
dangan,dángan→̌dánkan.dángan.
dànganin,dànganin( arbre.Afzelia.africana *diminutif )Voir entrée principale :dàgannin.
danganin,dànganin( arbre.Afzelia.africana *diminutif )Voir entrée principale :dàgannin.
dangasa,Dangasa→̌Dankasa.
dàngatɔ,dàngatɔ( malpropre *statif )
dangatɔ,dàngatɔ( malpropre *statif )
dangatò,dàngatɔ( malpropre *statif )
dàngatɔya,dàngatɔya( sale [ malpropre *statif ] *abstractif )
dangatɔya,dàngatɔya( sale [ malpropre *statif ] *abstractif )
dangatòya,dàngatɔya( sale [ malpropre *statif ] *abstractif )
dàngaya,dàngaya( malpropre *abstractif )
dangaya,dàngaya( malpropre *abstractif )
dàngo,"Dàngo→̌Keyita(Ancêtre - Kabala Sinbon, petit-fils Ase Bilali.)"
dango,"Dàngo→̌Keyita(Ancêtre - Kabala Sinbon, petit-fils Ase Bilali.)"
dáɲini,dáɲini( bouche chercher )vt.
daɲini,dáɲini( bouche chercher )vt.
danyini,dáɲini( bouche chercher )vt.
dànka,dànka→̌
danka,dànka→̌
dànkalan,dànkalan→̌→ 3dànkaran;dàngala.
dankalan,dànkalan→̌→ 3dànkaran;dàngala.
dànkalankule,dànkalankule( vipère.heurtante hurler )dànkarankule.
dankalankule,dànkalankule( vipère.heurtante hurler )dànkarankule.
dánkan,dánkan→̌→ 50dángan.
dankan,dánkan→̌→ 50dángan.
dànkan,dànkan( limite cou )
dànkaniya,dànkaniya→̌→ 1dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dankaniya,dànkaniya→̌→ 1dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dánkanna,dánkanna( poser *je cou à )
dankanna,dánkanna( poser *je cou à )
dànkannaya,dànkannaya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dankannaya,dànkannaya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dànkaran,dànkaran→̌dànkalan.dànkaran;dàngala.
dankaran,dànkaran→̌dànkalan.dànkaran;dàngala.
dànkarankule,dànkarankule( vipère.heurtante hurler )Voir entrée principale :dànkalankule.
dankarankule,dànkarankule( vipère.heurtante hurler )Voir entrée principale :dànkalankule.
dankari,dankari→̌
dànkari,dànkari( limite casser )vt.
dankari,dànkari( limite casser )vt.
dankasa,Dankasa→̌Voir entrée principale :Dangasa.
dànkelen,dànkelen( dépassement un )
dankelen,dànkelen( dépassement un )
dánkɛnɛmaya,dánkɛnɛmaya( poser clarté *à *abstractif )dákɛnɛmaya.
dankɛnɛmaya,dánkɛnɛmaya( poser clarté *à *abstractif )dákɛnɛmaya.
dankènèmaya,dánkɛnɛmaya( poser clarté *à *abstractif )dákɛnɛmaya.
dànkɔnɔba,dànkɔnɔba( chanvre *augmentatif )
dankɔnɔba,dànkɔnɔba( chanvre *augmentatif )
dankònòba,dànkɔnɔba( chanvre *augmentatif )
dànkɔrɔ,dànkɔrɔ( dépassement mâle.adulte )dànkɔrɔba.
dankɔrɔ,dànkɔrɔ( dépassement mâle.adulte )dànkɔrɔba.
dankòrò,dànkɔrɔ( dépassement mâle.adulte )dànkɔrɔba.
dànkɔrɔba,dànkɔrɔba( dépassement mâle.adulte *augmentatif )Voir entrée principale :dànkɔrɔ.
dankɔrɔba,dànkɔrɔba( dépassement mâle.adulte *augmentatif )Voir entrée principale :dànkɔrɔ.
dankòròba,dànkɔrɔba( dépassement mâle.adulte *augmentatif )Voir entrée principale :dànkɔrɔ.
dànkɔrɔbaya,dànkɔrɔbaya( vieux.solitaire [ dépassement mâle.adulte *augmentatif ] *abstractif )
dankɔrɔbaya,dànkɔrɔbaya( vieux.solitaire [ dépassement mâle.adulte *augmentatif ] *abstractif )
dankòròbaya,dànkɔrɔbaya( vieux.solitaire [ dépassement mâle.adulte *augmentatif ] *abstractif )
dànkun,dànkun→̌→ 6dàankun.
dankun,dànkun→̌→ 6dàankun.
dànkúnbère,dànkúnbère( limite genou )dàn-kúnbère.dànkúnbère.
dankunbere,dànkúnbère( limite genou )dàn-kúnbère.dànkúnbère.
dàn-kúnbère,dàn-kúnbère( limite genou )dànkúnbère.
dan-kunbere,dàn-kúnbère( limite genou )dànkúnbère.
dànkunnaya,dànkunnaya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dankunnaya,dànkunnaya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dànkunnayeelenbɔlan,dànkunnayeelenbɔlan( carrefour à lumière sortir *instrumental )
dankunnayeelenbɔlan,dànkunnayeelenbɔlan( carrefour à lumière sortir *instrumental )
dankunnayeelenbòlan,dànkunnayeelenbɔlan( carrefour à lumière sortir *instrumental )
dànkunntan,dànkunntan( carrefour *privatif )
dankunntan,dànkunntan( carrefour *privatif )
dànkuru,dànkuru( bosse boule )
dankuru,dànkuru( bosse boule )
dánma,dánma( bouche *comme de )Voir entrée principale :dáma.
danma,dánma( bouche *comme de )Voir entrée principale :dáma.
dànma,dànma( limite *à )dàma.dànma.
dánmadɔ,dánmadɔ( nombre [ compte *comme de ] certain )dámadɔ.dánmadɔ.
danmadɔ,dánmadɔ( nombre [ compte *comme de ] certain )dámadɔ.dánmadɔ.
danmadò,dánmadɔ( nombre [ compte *comme de ] certain )dámadɔ.dánmadɔ.
dànmakɛɲɛ,dànmakɛɲɛ( limite [ limite *à ] égaliser )dàmakɛɲɛ.dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
danmakɛɲɛ,dànmakɛɲɛ( limite [ limite *à ] égaliser )dàmakɛɲɛ.dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
danmakènyè,dànmakɛɲɛ( limite [ limite *à ] égaliser )dàmakɛɲɛ.dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
dànmakɛnyɛ,dànmakɛnyɛ( limite [ limite *à ] égaliser )dàmakɛɲɛ.dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
danmakɛnyɛ,dànmakɛnyɛ( limite [ limite *à ] égaliser )dàmakɛɲɛ.dàmakɛnyɛ;dànmakɛɲɛ;dànmakɛnyɛ.
dànmako,dànmako( spécial [ limite *à ] affaire )
danmako,dànmako( spécial [ limite *à ] affaire )
dànmana,dànmana( limite endroit *mental1 )dàmana.dànmana;dànmanata.
danmana,dànmana( limite endroit *mental1 )dàmana.dànmana;dànmanata.
dànmanata,dànmanata( limite endroit *mental2 )dàmana.dànmana.
danmanata,dànmanata( limite endroit *mental2 )dàmana.dànmana.
dànmantan,dànmantan→̌→ 4dàmantan.dàmanta;dànmantan.
danmantan,dànmantan→̌→ 4dàmantan.dàmanta;dànmantan.
dànmatɛmɛ,dànmatɛmɛ( limite [ limite *à ] passer )dàmatɛmɛ.dànmatɛmɛ.
danmatɛmɛ,dànmatɛmɛ( limite [ limite *à ] passer )dàmatɛmɛ.dànmatɛmɛ.
danmatèmè,dànmatɛmɛ( limite [ limite *à ] passer )dàmatɛmɛ.dànmatɛmɛ.
dànmatɛ̀mɛ,dànmatɛ̀mɛ( limite [ limite *à ] passer )dàmatɛ̀mɛ.dànmatɛ̀mɛ.
dánna,dánna( poser *je à )
danna,dánna( poser *je à )
dànna,dànna( limite à )
dánnabaa,dánnabaa( foi [ poser *je à ] *agent occasionnel )
dannabaa,dánnabaa( foi [ poser *je à ] *agent occasionnel )
dánnabali,dánnabali( foi [ poser *je à ] PTCP.NEG )
dannabali,dánnabali( foi [ poser *je à ] PTCP.NEG )
dánnabaliya,dánnabaliya( mécréant [ foi [ poser *je à ] PTCP.NEG ] *abstractif )
dannabaliya,dánnabaliya( mécréant [ foi [ poser *je à ] PTCP.NEG ] *abstractif )
dànnaci,dànnaci( limite à trait )
dannaci,dànnaci( limite à trait )
dánnamaa,dánnamaa( foi [ poser *je à ] homme )Voir entrée principale :dánnamɔgɔ.
dannamaa,dánnamaa( foi [ poser *je à ] homme )Voir entrée principale :dánnamɔgɔ.
dánnamɔgɔ,dánnamɔgɔ( foi [ poser *je à ] homme )dánnamaa.
dannamɔgɔ,dánnamɔgɔ( foi [ poser *je à ] homme )dánnamaa.
dannamògò,dánnamɔgɔ( foi [ poser *je à ] homme )dánnamaa.
dánnaɲɔgɔn,dánnaɲɔgɔn( foi [ poser *je à ] pareil )
dannaɲɔgɔn,dánnaɲɔgɔn( foi [ poser *je à ] pareil )
dannanyògòn,dánnaɲɔgɔn( foi [ poser *je à ] pareil )
dánnaɲɔgɔnya,dánnaɲɔgɔnya( confident [ foi [ poser *je à ] pareil ] *abstractif )
dannaɲɔgɔnya,dánnaɲɔgɔnya( confident [ foi [ poser *je à ] pareil ] *abstractif )
dannanyògònya,dánnaɲɔgɔnya( confident [ foi [ poser *je à ] pareil ] *abstractif )
dànnaselen,dànnaselen( limite à arriver *participe résultatif )
dannaselen,dànnaselen( limite à arriver *participe résultatif )
dànnátìgɛ,dànnátìgɛ( limite à couper )vr.
dannatigɛ,dànnátìgɛ( limite à couper )vr.
dannatigè,dànnátìgɛ( limite à couper )vr.
dànnatigɛli,dànnatigɛli( s'expliquer [ limite à couper ] *nom d'action )
dannatigɛli,dànnatigɛli( s'expliquer [ limite à couper ] *nom d'action )
dannatigèli,dànnatigɛli( s'expliquer [ limite à couper ] *nom d'action )
dánnatigi,dánnatigi( foi [ poser *je à ] maître )
dannatigi,dánnatigi( foi [ poser *je à ] maître )
dánnaya,dánnaya( foi [ poser *je à ] *abstractif )dánaya.
dannaya,dánnaya( foi [ poser *je à ] *abstractif )dánaya.
dánnayamaa,dánnayamaa( foi [ foi [ poser *je à ] *abstractif ] homme )Voir entrée principale :dánnayamɔgɔ.
dannayamaa,dánnayamaa( foi [ foi [ poser *je à ] *abstractif ] homme )Voir entrée principale :dánnayamɔgɔ.
dánnayamɔgɔ,dánnayamɔgɔ( foi [ foi [ poser *je à ] *abstractif ] homme )dánnayamaa.
dannayamɔgɔ,dánnayamɔgɔ( foi [ foi [ poser *je à ] *abstractif ] homme )dánnayamaa.
dannayamògò,dánnayamɔgɔ( foi [ foi [ poser *je à ] *abstractif ] homme )dánnayamaa.
dánni,dánni( compter *nom d'action )
danni,dánni( compter *nom d'action )
dànni,dànni( semer *nom d'action )
dànnidingɛ,dànnidingɛ( semis [ semer *nom d'action ] trou )
dannidingɛ,dànnidingɛ( semis [ semer *nom d'action ] trou )
dannidingè,dànnidingɛ( semis [ semer *nom d'action ] trou )
dànniji,dànniji( semis [ semer *nom d'action ] eau )
danniji,dànniji( semis [ semer *nom d'action ] eau )
dànnikɛkoro,dànnikɛkoro( semis [ semer *nom d'action ] faire calebasse )Voir entrée principale :dànnikoro.
dannikɛkoro,dànnikɛkoro( semis [ semer *nom d'action ] faire calebasse )Voir entrée principale :dànnikoro.
dannikèkoro,dànnikɛkoro( semis [ semer *nom d'action ] faire calebasse )Voir entrée principale :dànnikoro.
dànnikɛla,dànnikɛla( semis [ semer *nom d'action ] faire *agent permanent )
dannikɛla,dànnikɛla( semis [ semer *nom d'action ] faire *agent permanent )
dannikèla,dànnikɛla( semis [ semer *nom d'action ] faire *agent permanent )
dànnikɛlan,dànnikɛlan( semis [ semer *nom d'action ] faire *instrumental )
dannikɛlan,dànnikɛlan( semis [ semer *nom d'action ] faire *instrumental )
dannikèlan,dànnikɛlan( semis [ semer *nom d'action ] faire *instrumental )
dànnikɛmasin,dànnikɛmasin( semis [ semer *nom d'action ] faire machine )
dannikɛmasin,dànnikɛmasin( semis [ semer *nom d'action ] faire machine )
dannikèmasin,dànnikɛmasin( semis [ semer *nom d'action ] faire machine )
dànnikoro,dànnikoro( semis [ semer *nom d'action ] calebasse )dànnikɛkoro.
dannikoro,dànnikoro( semis [ semer *nom d'action ] calebasse )dànnikɛkoro.
dànnisanji,dànnisanji( semis [ semer *nom d'action ] pluie [ ciel eau ] )
dannisanji,dànnisanji( semis [ semer *nom d'action ] pluie [ ciel eau ] )
dànnisira,dànnisira( semis [ semer *nom d'action ] chemin )
dannisira,dànnisira( semis [ semer *nom d'action ] chemin )
daɲɔgɔ,Daɲɔgɔ→̌Voir entrée principale :Daɲɔkɔ.
danyògò,Daɲɔgɔ→̌Voir entrée principale :Daɲɔkɔ.
dánɔgɔ,dánɔgɔ( bouche facile )dánɔgɔn.
danɔgɔ,dánɔgɔ( bouche facile )dánɔgɔn.
danògò,dánɔgɔ( bouche facile )dánɔgɔn.
dánɔgɔn,dánɔgɔn( bouche facile )dánɔgɔ.dánɔgɔn.
danɔgɔn,dánɔgɔn( bouche facile )dánɔgɔ.dánɔgɔn.
danògòn,dánɔgɔn( bouche facile )dánɔgɔ.dánɔgɔn.
dáɲɔgɔn,dáɲɔgɔn( poser *partenaire réciproque )
daɲɔgɔn,dáɲɔgɔn( poser *partenaire réciproque )
danyògòn,dáɲɔgɔn( poser *partenaire réciproque )
daɲɔkɔ,Daɲɔkɔ→̌Daɲɔgɔ.
danyòkò,Daɲɔkɔ→̌Daɲɔgɔ.
daɲon,Daɲon→̌=Dáɲɔ?
danyon,Daɲon→̌=Dáɲɔ?
dánɔrɔ,dánɔrɔ( bouche coller )vt.
danɔrɔ,dánɔrɔ( bouche coller )vt.
danòrò,dánɔrɔ( bouche coller )vt.
dánpe,dánpe→̌→ 1
danpe,dánpe→̌→ 1
dánpère,dánpère( bouche )dánpɛ̀ri;dánpɛ̀ru.
danpere,dánpère( bouche )dánpɛ̀ri;dánpɛ̀ru.
dánpɛ̀ri,dánpɛ̀ri( bouche )dánpère.dánpɛ̀ru.
danpɛri,dánpɛ̀ri( bouche )dánpère.dánpɛ̀ru.
danpèri,dánpɛ̀ri( bouche )dánpère.dánpɛ̀ru.
dánpɛ̀ru,dánpɛ̀ru( bouche )dánpère.dánpɛ̀ri.
danpɛru,dánpɛ̀ru( bouche )dánpère.dánpɛ̀ri.
danpèru,dánpɛ̀ru( bouche )dánpère.dánpɛ̀ri.
dànsagon,dànsagon( limite sauter.par.dessus )
dansagon,dànsagon( limite sauter.par.dessus )
dànsàgon,dànsàgon( limite sauter.par.dessus )vi.
dànsagonwale,dànsagonwale( transgression [ limite sauter.par.dessus ] acte )
dansagonwale,dànsagonwale( transgression [ limite sauter.par.dessus ] acte )
dánsè,dánsè→̌
danse,dánsè→̌
dansɛnɛ,Dansɛnɛ→̌Dànsɛ́ni.Dànséni;Dasɛnɛ.
dansènè,Dansɛnɛ→̌Dànsɛ́ni.Dànséni;Dasɛnɛ.
dànséni,Dànséni→̌Dànsɛ́ni.Dansɛnɛ;Dasɛnɛ.
danseni,Dànséni→̌Dànsɛ́ni.Dansɛnɛ;Dasɛnɛ.
dànsɛ́ni,Dànsɛ́ni→̌Dansɛnɛ;Dànséni;Dasɛnɛ.
dansɛni,Dànsɛ́ni→̌Dansɛnɛ;Dànséni;Dasɛnɛ.
dansèni,Dànsɛ́ni→̌Dansɛnɛ;Dànséni;Dasɛnɛ.
dànsigi,dànsigi( limite asseoir )
dansigi,dànsigi( limite asseoir )
dànsìgi,dànsìgi( limite asseoir )
dansira,Dansira→̌(utilisé pour les femmes Tarawele.)
dansogo,Dansogo→̌Keyita.Voir entrée principale :Dansoko.Dansoko;Donsogo.(Ancêtre - Jatra Dansongo.)
dansoko,Dansoko→̌Keyita.Dansogo;Donsogo.(Ancêtre - Jatra Dansongo.)
dànsúba,Dànsúba→̌
dansuba,Dànsúba→̌
dántan,dántan( bouche *privatif )
dantan,dántan( bouche *privatif )
dántanfɛn,dántanfɛn( muet [ bouche *privatif ] chose )
dantanfɛn,dántanfɛn( muet [ bouche *privatif ] chose )
dantanfèn,dántanfɛn( muet [ bouche *privatif ] chose )
dántanya,dántanya( muet [ bouche *privatif ] *abstractif )
dantanya,dántanya( muet [ bouche *privatif ] *abstractif )
dante,Dante→̌Dantɛ.
dantɛ,Dantɛ→̌Voir entrée principale :Dante.
dantè,Dantɛ→̌Voir entrée principale :Dante.
dàntɛmɛ,dàntɛmɛ( limite passer )
dantɛmɛ,dàntɛmɛ( limite passer )
dantèmè,dàntɛmɛ( limite passer )
dàntɛ̀mɛ,dàntɛ̀mɛ( limite passer )vi.
dàntigɛ,dàntigɛ( limite couper )
dantigɛ,dàntigɛ( limite couper )
dantigè,dàntigɛ( limite couper )
dàntìgɛ,dàntìgɛ( limite couper )vr.
dàntigɛli,dàntigɛli( s'expliquer [ limite couper ] *nom d'action )
dantigɛli,dàntigɛli( s'expliquer [ limite couper ] *nom d'action )
dantigèli,dàntigɛli( s'expliquer [ limite couper ] *nom d'action )
dàntɔ,dàntɔ( limite *statif )
dantɔ,dàntɔ( limite *statif )
dantò,dàntɔ( limite *statif )
dánye,dánye( créer *je *postposition polysémique )
danye,dánye( créer *je *postposition polysémique )
dányɛ̀rɛla,dányɛ̀rɛla( poser *je même à )
danyɛrɛla,dányɛ̀rɛla( poser *je même à )
danyèrèla,dányɛ̀rɛla( poser *je même à )
dányò,Dányò→̌
danyo,Dányò→̌
dàomɛ,Dàomɛ→̌
daomɛ,Dàomɛ→̌
daomè,Dàomɛ→̌
dapɛli,dapɛli→̌
dapèli,dapɛli→̌
dapisɔni,dapisɔni→̌→ 6
dapisòni,dapisɔni→̌→ 6
dara,Dara→̌
dára,Dára→̌Daramani.Daraman.
dara,Dára→̌Daramani.Daraman.
dàra,dàra→̌→ 1drà.Source :fr : mettre dans de beaux draps ?
darafuri,Darafuri→̌
daragi,daragi→̌
dáraja,"dáraja→̌→ 15Source :ar: daraga : degré, grade ?)"
daraja,"dáraja→̌→ 15Source :ar: daraga : degré, grade ?)"
dárajama,dárajama( célébrité *comme de )
darajama,dárajama( célébrité *comme de )
dàraka,dàraka→̌→ 77
daraka,dàraka→̌→ 77
dàrakase,dàrakase→̌
darakase,dàrakase→̌
daraki,Daraki→̌
dárali,dárali→̌dráli.
darali,dárali→̌dráli.
daraman,Daraman→̌Daramani.Dára.
daramani,Daramani→̌Daraman;Dára.
daramɛ,Daramɛ→̌
daramè,Daramɛ→̌
daramera,Daramera→̌Dramera.(Bergers.)
daramerra,Daramerra→̌Voir :Dramera.
dàrapo,dàrapo→̌→ 10
darapo,dàrapo→̌→ 10
darasalamu,Darasalamu→̌Darisalamu.Daaru Salaami.
darawe,Darawe→̌
darisalamu,Darisalamu→̌Daaru Salaami;Darasalamu.
dariwini,Dariwini→̌
darizan,darizan→̌→ 7Voir entrée principale :arizan.
dárɔ,dárɔ( bouche dans )Voir entrée principale :dála.
darɔ,dárɔ( bouche dans )Voir entrée principale :dála.
darò,dárɔ( bouche dans )Voir entrée principale :dála.
dàro,dàro→̌→ 7
daro,dàro→̌→ 7
dárɔda,dárɔda( bouche dans poser )vr.
darɔda,dárɔda( bouche dans poser )vr.
daròda,dárɔda( bouche dans poser )vr.
dárɔdun,dárɔdun( bouche dans manger )vr.
darɔdun,dárɔdun( bouche dans manger )vr.
daròdun,dárɔdun( bouche dans manger )vr.
dárɔgɛlɛn,dárɔgɛlɛn( bouche.active [ bouche dans ] difficile )dálagɛlɛn.dámagɛlɛn.
darɔgɛlɛn,dárɔgɛlɛn( bouche.active [ bouche dans ] difficile )dálagɛlɛn.dámagɛlɛn.
darògèlèn,dárɔgɛlɛn( bouche.active [ bouche dans ] difficile )dálagɛlɛn.dámagɛlɛn.
dárɔgɛ̀lɛya,dárɔgɛ̀lɛya( bouche dans durcir [ dur *en verbe dynamique ] )vr.
darɔgɛlɛya,dárɔgɛ̀lɛya( bouche dans durcir [ dur *en verbe dynamique ] )vr.
darògèlèya,dárɔgɛ̀lɛya( bouche dans durcir [ dur *en verbe dynamique ] )vr.
dárɔkà,dárɔkà( bouche ouvrir )vt.dálakà.dárɔkà.
darɔka,dárɔkà( bouche ouvrir )vt.dálakà.dárɔkà.
daròka,dárɔkà( bouche ouvrir )vt.dálakà.dárɔkà.
dárɔkan,dárɔkan( bouche dans cou )Voir entrée principale :dálakan.
darɔkan,dárɔkan( bouche dans cou )Voir entrée principale :dálakan.
daròkan,dárɔkan( bouche dans cou )Voir entrée principale :dálakan.
dárɔkango,dárɔkango( voeu [ bouche dans cou ] désagréable )Voir entrée principale :dálakango.
darɔkango,dárɔkango( voeu [ bouche dans cou ] désagréable )Voir entrée principale :dálakango.
daròkango,dárɔkango( voeu [ bouche dans cou ] désagréable )Voir entrée principale :dálakango.
dárɔko,dárɔko( bouche à affaire )dálako.dárɔko.
darɔko,dárɔko( bouche à affaire )dálako.dárɔko.
daròko,dárɔko( bouche à affaire )dálako.dárɔko.
dárɔmugan,dárɔmugan( bouche dans sucer )vr.
darɔmugan,dárɔmugan( bouche dans sucer )vr.
daròmugan,dárɔmugan( bouche dans sucer )vr.
dárɔndi,dárɔndi( bouche.active [ bouche dans ] agréable )dálandi.dámandi.
darɔndi,dárɔndi( bouche.active [ bouche dans ] agréable )dálandi.dámandi.
daròndi,dárɔndi( bouche.active [ bouche dans ] agréable )dálandi.dámandi.
dárɔnkolon,dárɔnkolon( bouche vide [ *causatif vide ] )dálankolon.dárɔnkolon.
darɔnkolon,dárɔnkolon( bouche vide [ *causatif vide ] )dálankolon.dárɔnkolon.
darònkolon,dárɔnkolon( bouche vide [ *causatif vide ] )dálankolon.dárɔnkolon.
dárɔsà,dárɔsà( bouche faire.mourir [ *causatif mourir ] )vt.dálasà.dárɔsà.
darɔsa,dárɔsà( bouche faire.mourir [ *causatif mourir ] )vt.dálasà.dárɔsà.
daròsa,dárɔsà( bouche faire.mourir [ *causatif mourir ] )vt.dálasà.dárɔsà.
dárɔsàma,dárɔsàma( bouche dans tirer.vers.soi )vt.
darɔsama,dárɔsàma( bouche dans tirer.vers.soi )vt.
daròsama,dárɔsàma( bouche dans tirer.vers.soi )vt.
dárɔtɔmɔ,dárɔtɔmɔ( bouche dans ramasser )
darɔtɔmɔ,dárɔtɔmɔ( bouche dans ramasser )
daròtòmò,dárɔtɔmɔ( bouche dans ramasser )
dársàlám,Dársàlám→̌
darsalam,Dársàlám→̌
dásàma,dásàma( bouche tirer.vers.soi )vt.
dasama,dásàma( bouche tirer.vers.soi )vt.
dásan,dásan→̌dósiyɛn.dásan;dósyan.
dasan,dásan→̌dósiyɛn.dásan;dósyan.
dásanfɛla,dásanfɛla( bouche le.haut [ par-dessus [ ciel par ] *nom de lieu ] )
dasanfɛla,dásanfɛla( bouche le.haut [ par-dessus [ ciel par ] *nom de lieu ] )
dasanfèla,dásanfɛla( bouche le.haut [ par-dessus [ ciel par ] *nom de lieu ] )
dásaran,dásaran( bouche faufiler )vt.
dasaran,dásaran( bouche faufiler )vt.
dasɛnɛ,Dasɛnɛ→̌Dànsɛ́ni.Dansɛnɛ;Dànséni.
dasènè,Dasɛnɛ→̌Dànsɛ́ni.Dansɛnɛ;Dànséni.
dási,dási( bouche poil )
dasi,dási( bouche poil )
dàsi,dàsi→̌→ 13→n : 1dɛ̀si.
dásigibali,dásigibali( bouche asseoir PTCP.NEG )
dasigibali,dásigibali( bouche asseoir PTCP.NEG )
dásigisigi,dásigisigi( bouche bégayer )vi.
dasigisigi,dásigisigi( bouche bégayer )vi.
dásiri,dásiri( bouche lier )
dasiri,dásiri( bouche lier )
dásìri,dásìri( bouche lier )vt.
dasizi,dasizi→̌
dásɔ̀gɔ,dásɔ̀gɔ( bouche percer )vt.dáswà.
dasɔgɔ,dásɔ̀gɔ( bouche percer )vt.dáswà.
dasògò,dásɔ̀gɔ( bouche percer )vt.dáswà.
dásònya,dásònya( bouche dérober [ voleur *abstractif ] )vt.Voir entrée principale :dásònyɛ.
dasonya,dásònya( bouche dérober [ voleur *abstractif ] )vt.Voir entrée principale :dásònyɛ.
dásònyɛ,dásònyɛ( bouche dérober [ voleur *abstractif ] )vt.dásònya.
dasonyɛ,dásònyɛ( bouche dérober [ voleur *abstractif ] )vt.dásònya.
dasonyè,dásònyɛ( bouche dérober [ voleur *abstractif ] )vt.dásònya.
dásu,dásu( bouche cadavre )
dasu,dásu( bouche cadavre )
dáswà,dáswà( bouche percer )vt.dásɔ̀gɔ.dáswà.
daswa,dáswà( bouche percer )vt.dásɔ̀gɔ.dáswà.
dátà,dátà( bouche prendre )vt.
data,dátà( bouche prendre )vt.
dátara,dátara( bouche coller )vt.
datara,dátara( bouche coller )vt.
dati,dati→̌→ 1
dátìgɛ,dátìgɛ( bouche couper )
datigɛ,dátìgɛ( bouche couper )
datigè,dátìgɛ( bouche couper )
dátigɛndala,dátigɛndala( bouche couper *je bouche à )
datigɛndala,dátigɛndala( bouche couper *je bouche à )
datigèndala,dátigɛndala( bouche couper *je bouche à )
dátiɲɛ,dátiɲɛ( bouche gâter )dátiyɛn.
datiɲɛ,dátiɲɛ( bouche gâter )dátiyɛn.
datinyè,dátiɲɛ( bouche gâter )dátiyɛn.
dátiyɛn,dátiyɛn( bouche gâter )dátiɲɛ.dátiyɛn.
datiyɛn,dátiyɛn( bouche gâter )dátiɲɛ.dátiyɛn.
datiyèn,dátiyɛn( bouche gâter )dátiɲɛ.dátiyɛn.
dátɔ,dátɔ( bouche *statif )
datɔ,dátɔ( bouche *statif )
datò,dátɔ( bouche *statif )
dàtɔ,dàtɔ( syphilis.endémique *statif )
dátoli,dátoli( bouche pourri )
datoli,dátoli( bouche pourri )
dàtu,dàtu( chanvre cracher )
datu,dàtu( chanvre cracher )
dátugu,dátugu( bouche fermer )vt.
datugu,dátugu( bouche fermer )vt.
dátugubali,dátugubali( boucher [ bouche fermer ] PTCP.NEG )
datugubali,dátugubali( boucher [ bouche fermer ] PTCP.NEG )
dátugulan,dátugulan( boucher [ bouche fermer ] *instrumental )
datugulan,dátugulan( boucher [ bouche fermer ] *instrumental )
dátunu,dátunu( bouche perdre )vi.dátunun.dátunu.
datunu,dátunu( bouche perdre )vi.dátunun.dátunu.
dátunun,dátunun( bouche perdre )vi.dátunu.
datunun,dátunun( bouche perdre )vi.dátunu.
dáuda,Dáuda→̌Dáwuda;Dádà.
dauda,Dáuda→̌Dáwuda;Dádà.
daw,Daw→̌Ndaw;Dafe.
dawidi,Dawidi→̌
dawo,Dawo→̌Voir entrée principale :Dawu.
dáwolo,dáwolo( bouche peau )
dawolo,dáwolo( bouche peau )
dáwoloɲimibana,dáwoloɲimibana( lèvre [ bouche peau ] mâcher maladie )
dawoloɲimibana,dáwoloɲimibana( lèvre [ bouche peau ] mâcher maladie )
dawolonyimibana,dáwoloɲimibana( lèvre [ bouche peau ] mâcher maladie )
dawomɛ,Dawomɛ→̌Dahomɛ.
dawomè,Dawomɛ→̌Dahomɛ.
dáwɔɔrɔ,dáwɔɔrɔ( jour six )
dawɔɔrɔ,dáwɔɔrɔ( jour six )
dawòorò,dáwɔɔrɔ( jour six )
dawu,Dawu→̌Dawo.
dáwuda,Dáwuda→̌Dáuda.Dádà.
dawuda,Dáwuda→̌Dáuda.Dádà.
dáwula,dáwula→̌→ 39
dawula,dáwula→̌→ 39
dawulabugu,Dawulabugu→̌
dáwulama,dáwulama( charme *comme de )
dawulama,dáwulama( charme *comme de )
dáwulaya,dáwulaya( charme *abstractif )vt.
dawulaya,dáwulaya( charme *abstractif )vt.
dáwuli,dáwuli( bouche se.lever )vt.
dawuli,dáwuli( bouche se.lever )vt.
dáwusu,dáwusu( bouche fumer )vr.
dawusu,dáwusu( bouche fumer )vr.
dáwusulan,dáwusulan( bouche écarquiller *instrumental )
dawusulan,dáwusulan( bouche écarquiller *instrumental )
dáyayaya,dáyayaya( bouche verbiage )
dayayaya,dáyayaya( bouche verbiage )
dáyɛlɛ,dáyɛlɛ( bouche ouvrir )
dayɛlɛ,dáyɛlɛ( bouche ouvrir )
dayèlè,dáyɛlɛ( bouche ouvrir )
dáyɛ̀lɛ,dáyɛ̀lɛ( bouche ouvrir )vt.dáyɛ̀lɛn.
dáyɛlɛlan,dáyɛlɛlan( ouvrir [ bouche ouvrir ] *instrumental )
dayɛlɛlan,dáyɛlɛlan( ouvrir [ bouche ouvrir ] *instrumental )
dayèlèlan,dáyɛlɛlan( ouvrir [ bouche ouvrir ] *instrumental )
dáyɛ̀lɛn,dáyɛ̀lɛn( bouche ouvrir )vt.dáyɛ̀lɛ.dáyɛ̀lɛn.
dayɛlɛn,dáyɛ̀lɛn( bouche ouvrir )vt.dáyɛ̀lɛ.dáyɛ̀lɛn.
dayèlèn,dáyɛ̀lɛn( bouche ouvrir )vt.dáyɛ̀lɛ.dáyɛ̀lɛn.
dàyifu,dàyifu→̌Source :Ar.
dayifu,dàyifu→̌Source :Ar.
dáyìra,dáyìra( bouche montrer )dájìra.dáyìra.
dayira,dáyìra( bouche montrer )dájìra.dáyìra.
dáyìrimɛ,dáyìrimɛ→̌dáhìrimɛ.dáyìrimɛ.Ar. dara:him 'drachmes'
dayirimɛ,dáyìrimɛ→̌dáhìrimɛ.dáyìrimɛ.Ar. dara:him 'drachmes'
dayirimè,dáyìrimɛ→̌dáhìrimɛ.dáyìrimɛ.Ar. dara:him 'drachmes'
dè,dè→̌→ 10535
de,dè→̌→ 10535
dɛ́,dɛ́→̌→ 1565
dɛ,dɛ́→̌→ 1565
dè,dɛ́→̌→ 1565
dɛ́bɛ,dɛ́bɛ→̌→ 8
dɛbɛ,dɛ́bɛ→̌→ 8
dèbè,dɛ́bɛ→̌→ 8
dɛ̀bɛ,dɛ̀bɛ→̌→ 56
dɛ́bɛdɛbɛ,dɛ́bɛdɛbɛ→̌→ 1
dɛbɛdɛbɛ,dɛ́bɛdɛbɛ→̌→ 1
dèbèdèbè,dɛ́bɛdɛbɛ→̌→ 1
dɛbɛdɛbɛnin,dɛbɛdɛbɛnin→̌
dèbèdèbènin,dɛbɛdɛbɛnin→̌
dɛ̀bɛli,dɛ̀bɛli→̌dàbali.dàbari;dɛ̀bɛli.
dɛbɛli,dɛ̀bɛli→̌dàbali.dàbari;dɛ̀bɛli.
dèbèli,dɛ̀bɛli→̌dàbali.dàbari;dɛ̀bɛli.
dɛ́bɛn,dɛ́bɛn→̌
dɛbɛn,dɛ́bɛn→̌
dèbèn,dɛ́bɛn→̌
dɛ̀bɛn,dɛ̀bɛn→̌→ 43
debi,Debi→̌
dɛ̀bi,dɛ̀bi→̌dàbi.dɛ̀bi.
dɛbi,dɛ̀bi→̌dàbi.dɛ̀bi.
dèbi,dɛ̀bi→̌dàbi.dɛ̀bi.
debo,Debo→̌
dèdegeru,dèdegeru→̌
dedegeru,dèdegeru→̌
dédenin,dédenin( *diminutif )
dedenin,dédenin( *diminutif )
dɛ̀ɛmɛdɛɛmɛ,dɛ̀ɛmɛdɛɛmɛ→̌dɛ̀mɛdɛmɛ.
dɛɛmɛdɛɛmɛ,dɛ̀ɛmɛdɛɛmɛ→̌dɛ̀mɛdɛmɛ.
dèemèdèemè,dɛ̀ɛmɛdɛɛmɛ→̌dɛ̀mɛdɛmɛ.
dɛ̀ɛmu,dɛ̀ɛmu→̌vi.jɛ̀mu.jɛ̀ɛmu;dɛ̀ɛmu;dɛ̀gɛmu.
dɛɛmu,dɛ̀ɛmu→̌vi.jɛ̀mu.jɛ̀ɛmu;dɛ̀ɛmu;dɛ̀gɛmu.
dèemu,dɛ̀ɛmu→̌vi.jɛ̀mu.jɛ̀ɛmu;dɛ̀ɛmu;dɛ̀gɛmu.
dɛ̀ɛmukan,dɛ̀ɛmukan( parole cou )jɛ̀mukan.jɛ̀ɛmukan;dɛ̀ɛmukan;dɛ̀gɛmukan.
dɛɛmukan,dɛ̀ɛmukan( parole cou )jɛ̀mukan.jɛ̀ɛmukan;dɛ̀ɛmukan;dɛ̀gɛmukan.
dèemukan,dɛ̀ɛmukan( parole cou )jɛ̀mukan.jɛ̀ɛmukan;dɛ̀ɛmukan;dɛ̀gɛmukan.
dɛ́ɛndɛ,dɛ́ɛndɛ→̌
dɛɛndɛ,dɛ́ɛndɛ→̌
dèendè,dɛ́ɛndɛ→̌
dɛ̀ɛndɛ,dɛ̀ɛndɛ→̌dɛ̀ndɛ.dɛ̀ndɛn;dɛ̀ɛndɛɛn;dɛ̀ɛndɛ;dànda.
dɛ̀ɛndɛɛn,dɛ̀ɛndɛɛn→̌dɛ̀ndɛ.dɛ̀ndɛn;dɛ̀ɛndɛɛn;dɛ̀ɛndɛ;dànda.
dɛɛndɛɛn,dɛ̀ɛndɛɛn→̌dɛ̀ndɛ.dɛ̀ndɛn;dɛ̀ɛndɛɛn;dɛ̀ɛndɛ;dànda.
dèendèen,dɛ̀ɛndɛɛn→̌dɛ̀ndɛ.dɛ̀ndɛn;dɛ̀ɛndɛɛn;dɛ̀ɛndɛ;dànda.
dèenkun,dèenkun→̌→ 2dènkun.dèngu;dɛ̀ɛnkun;dèenkun;jèenkun;jèngu;jènku.
deenkun,dèenkun→̌→ 2dènkun.dèngu;dɛ̀ɛnkun;dèenkun;jèenkun;jèngu;jènku.
dɛ́ɛnkun,dɛ́ɛnkun→̌vt.
dɛɛnkun,dɛ́ɛnkun→̌vt.
dèenkun,dɛ́ɛnkun→̌vt.
dɛ̀ɛnkun,dɛ̀ɛnkun→̌dènkun.dèngu;dɛ̀ɛnkun;dèenkun;jèenkun;jèngu;jènku.
dɛɛrudɛɛru,dɛɛrudɛɛru→̌
dèerudèeru,dɛɛrudɛɛru→̌
def,DEF→̌Voir entrée principale :dèyɛfu.
dɛ́fɛ,dɛ́fɛ→̌→ 1vt.
dɛfɛ,dɛ́fɛ→̌→ 1vt.
dèfè,dɛ́fɛ→̌→ 1vt.
deferɔkizamini,deferɔkizamini→̌→n.prop : 3
deferòkizamini,deferɔkizamini→̌→n.prop : 3
défile,défile→̌
defile,défile→̌
dɛ̀fu,dɛ̀fu→̌dèyɛfu.Fr. DEF
dɛfu,dɛ̀fu→̌dèyɛfu.Fr. DEF
dèfu,dɛ̀fu→̌dèyɛfu.Fr. DEF
dège,dège→̌→ 173
dege,dège→̌→ 173
dɛ̀gɛ,dɛ̀gɛ→̌→ 97
dɛgɛ,dɛ̀gɛ→̌→ 97
dègè,dɛ̀gɛ→̌→ 97
dègebaa,dègebaa( enseigner *agent occasionnel )
degebaa,dègebaa( enseigner *agent occasionnel )
dègedege,dègedege→̌vt.lègelege;dègedegelima.
degedege,dègedege→̌vt.lègelege;dègedegelima.
dɛ̀gɛdɛgɛ,dɛ̀gɛdɛgɛ→̌vt.
dɛgɛdɛgɛ,dɛ̀gɛdɛgɛ→̌vt.
dègèdègè,dɛ̀gɛdɛgɛ→̌vt.
dègedegeli,dègedegeli→̌dèndegelu.dègedegelu;dèndegeru;dèndege.
degedegeli,dègedegeli→̌dèndegelu.dègedegelu;dèndegeru;dèndege.
dègedegelima,dègedegelima→̌vt.dègedege.lègelege.
degedegelima,dègedegelima→̌vt.dègedege.lègelege.
dègedegelu,dègedegelu→̌dèndegelu.dègedegeli;dèndegeru;dèndege.
degedegelu,dègedegelu→̌dèndegelu.dègedegeli;dèndegeru;dèndege.
dègedegeluma,dègedegeluma→̌
degedegeluma,dègedegeluma→̌
dègeden,dègeden( enseigner enfant )
degeden,dègeden( enseigner enfant )
dègeli,dègeli( enseigner *nom d'action )
degeli,dègeli( enseigner *nom d'action )
dègelibaa,dègelibaa( enseigner *nom d'action *agent occasionnel )Voir entrée principale :dègelibaga.
degelibaa,dègelibaa( enseigner *nom d'action *agent occasionnel )Voir entrée principale :dègelibaga.
dègelibaga,dègelibaga( enseigner *nom d'action *agent occasionnel )dègelibaa.
degelibaga,dègelibaga( enseigner *nom d'action *agent occasionnel )dègelibaa.
dègelikaramɔgɔ,dègelikaramɔgɔ( apprentissage [ enseigner *nom d'action ] maître [ homme ] )
degelikaramɔgɔ,dègelikaramɔgɔ( apprentissage [ enseigner *nom d'action ] maître [ homme ] )
degelikaramògò,dègelikaramɔgɔ( apprentissage [ enseigner *nom d'action ] maître [ homme ] )
dɛ̀gɛmu,dɛ̀gɛmu→̌vi.jɛ̀mu.jɛ̀ɛmu;dɛ̀ɛmu;dɛ̀gɛmu.
dɛgɛmu,dɛ̀gɛmu→̌vi.jɛ̀mu.jɛ̀ɛmu;dɛ̀ɛmu;dɛ̀gɛmu.
dègèmu,dɛ̀gɛmu→̌vi.jɛ̀mu.jɛ̀ɛmu;dɛ̀ɛmu;dɛ̀gɛmu.
dɛ̀gɛmukan,dɛ̀gɛmukan( parole cou )jɛ̀mukan.jɛ̀ɛmukan;dɛ̀ɛmukan;dɛ̀gɛmukan.
dɛgɛmukan,dɛ̀gɛmukan( parole cou )jɛ̀mukan.jɛ̀ɛmukan;dɛ̀ɛmukan;dɛ̀gɛmukan.
dègèmukan,dɛ̀gɛmukan( parole cou )jɛ̀mukan.jɛ̀ɛmukan;dɛ̀ɛmukan;dɛ̀gɛmukan.
dɛ́gɛn,dɛ́gɛn→̌vt.
dɛgɛn,dɛ́gɛn→̌vt.
dègèn,dɛ́gɛn→̌vt.
degɛnbere,Degɛnbere→̌
degènbere,Degɛnbere→̌
dégere,dégere→̌→ 44dégre.
degere,dégere→̌→ 44dégre.
dégeresumanan,dégeresumanan( degré mesurer *instrumental )dégresumanan.fr : degré
degeresumanan,dégeresumanan( degré mesurer *instrumental )dégresumanan.fr : degré
dégre,dégre→̌dégere.dégre.
degre,dégre→̌dégere.dégre.
dégresumanan,dégresumanan( degré mesurer *instrumental )dégeresumanan.dégresumanan.fr : degré
degresumanan,dégresumanan( degré mesurer *instrumental )dégeresumanan.dégresumanan.fr : degré
dègun,dègun→̌→ 61vt.
degun,dègun→̌→ 61vt.
dekamɛtɛrɛ,dekamɛtɛrɛ→̌→ 2
dekamètèrè,dekamɛtɛrɛ→̌→ 2
dekere,dekere→̌
dekilarasɔn,dekilarasɔn→̌
dekilarasòn,dekilarasɔn→̌
dekiliki,dekiliki→̌
dɛkisitorosi,dɛkisitorosi→̌→n.prop : 1
dèkisitorosi,dɛkisitorosi→̌→n.prop : 1
dɛkisitorɔsi,dɛkisitorɔsi→̌Voir entrée principale :dɛkisitorosi.
dèkisitoròsi,dɛkisitorɔsi→̌Voir entrée principale :dɛkisitorosi.
dɛkizametazɔni,dɛkizametazɔni→̌→ 1
dèkizametazòni,dɛkizametazɔni→̌→ 1
dekodɛri,dekodɛri→̌→ 3
dekodèri,dekodɛri→̌→ 3
dɛ́lɛ,dɛ́lɛ→̌vt.
dɛlɛ,dɛ́lɛ→̌vt.
dèlè,dɛ́lɛ→̌vt.
dɛ́lɛdɛlɛdɛlɛ,dɛ́lɛdɛlɛdɛlɛ→̌dlɛ́dlɛdlɛ.
dɛlɛdɛlɛdɛlɛ,dɛ́lɛdɛlɛdɛlɛ→̌dlɛ́dlɛdlɛ.
dèlèdèlèdèlè,dɛ́lɛdɛlɛdɛlɛ→̌dlɛ́dlɛdlɛ.
délegasɔn,délegasɔn→̌→ 3Source :fr. délégation.
delegasɔn,délegasɔn→̌→ 3Source :fr. délégation.
delegasòn,délegasɔn→̌→ 3Source :fr. délégation.
dèlege,dèlege→̌→ 7délege.
delege,dèlege→̌→ 7délege.
déli,déli→̌→ 14dɛ́li.
deli,déli→̌→ 14dɛ́li.
dèli,dèli→̌→ 18dɛ̀li.
dɛ́li,dɛ́li→̌déli.dɛ́li.
dɛli,dɛ́li→̌déli.dɛ́li.
dèli,dɛ́li→̌déli.dɛ́li.
dɛ̀li,dɛ̀li→̌dèli.dɛ̀li.
dèliko,dèliko( habitude affaire )dèlimako.
deliko,dèliko( habitude affaire )dèlimako.
délilikɛla,délilikɛla( prier *nom d'action faire *agent permanent )
delilikɛla,délilikɛla( prier *nom d'action faire *agent permanent )
delilikèla,délilikɛla( prier *nom d'action faire *agent permanent )
dèlimako,dèlimako( habitude *comme de affaire )Voir entrée principale :dèliko.
delimako,dèlimako( habitude *comme de affaire )Voir entrée principale :dèliko.
dèlina,dèlina( habitude *mental1 )
delina,dèlina( habitude *mental1 )
dèlinanko,dèlinanko( habitude [ habitude *mental1 ] affaire )
delinanko,dèlinanko( habitude [ habitude *mental1 ] affaire )
dèliɲɔgɔn,dèliɲɔgɔn( avoir.l'habitude *partenaire réciproque )
deliɲɔgɔn,dèliɲɔgɔn( avoir.l'habitude *partenaire réciproque )
delinyògòn,dèliɲɔgɔn( avoir.l'habitude *partenaire réciproque )
dɛlita,dɛlita→̌→ 3
dèlita,dɛlita→̌→ 3
delɔsi,Delɔsi→̌
delòsi,Delɔsi→̌
dɛ̀mɛ,dɛ̀mɛ→̌→ 498dɛ̀mɛn.
dɛmɛ,dɛ̀mɛ→̌→ 498dɛ̀mɛn.
dèmè,dɛ̀mɛ→̌→ 498dɛ̀mɛn.
dɛ̀mɛbaa,dɛ̀mɛbaa( aider *agent occasionnel )Voir entrée principale :dɛ̀mɛbaga.
dɛmɛbaa,dɛ̀mɛbaa( aider *agent occasionnel )Voir entrée principale :dɛ̀mɛbaga.
dèmèbaa,dɛ̀mɛbaa( aider *agent occasionnel )Voir entrée principale :dɛ̀mɛbaga.
dɛ̀mɛbaga,dɛ̀mɛbaga( aider *agent occasionnel )dɛ̀mɛbaa.
dɛmɛbaga,dɛ̀mɛbaga( aider *agent occasionnel )dɛ̀mɛbaa.
dèmèbaga,dɛ̀mɛbaga( aider *agent occasionnel )dɛ̀mɛbaa.
dɛ̀mɛdɛmɛ,dɛ̀mɛdɛmɛ→̌→ 7Voir entrée principale :dɛ̀ɛmɛdɛɛmɛ.
dɛmɛdɛmɛ,dɛ̀mɛdɛmɛ→̌→ 7Voir entrée principale :dɛ̀ɛmɛdɛɛmɛ.
dèmèdèmè,dɛ̀mɛdɛmɛ→̌→ 7Voir entrée principale :dɛ̀ɛmɛdɛɛmɛ.
dɛ̀mɛn,dɛ̀mɛn→̌→ 62dɛ̀mɛ.dɛ̀mɛn.
dɛmɛn,dɛ̀mɛn→̌→ 62dɛ̀mɛ.dɛ̀mɛn.
dèmèn,dɛ̀mɛn→̌→ 62dɛ̀mɛ.dɛ̀mɛn.
dɛ̀mɛnan,dɛ̀mɛnan( aider *instrumental )
dɛmɛnan,dɛ̀mɛnan( aider *instrumental )
dèmènan,dɛ̀mɛnan( aider *instrumental )
dɛ̀mɛɲini,dɛ̀mɛɲini( aide chercher )
dɛmɛɲini,dɛ̀mɛɲini( aide chercher )
dèmènyini,dɛ̀mɛɲini( aide chercher )
dɛ̀mɛɲɔgɔn,dɛ̀mɛɲɔgɔn( aider *partenaire réciproque )
dɛmɛɲɔgɔn,dɛ̀mɛɲɔgɔn( aider *partenaire réciproque )
dèmènyògòn,dɛ̀mɛɲɔgɔn( aider *partenaire réciproque )
demifinali,demifinali→̌→ 7demi-finali.
demi-finali,demi-finali→̌demifinali.demi-finali.
démokarasi,démokarasi→̌→ 54
demokarasi,démokarasi→̌→ 54
demokarati,demokarati→̌→ 1
demokaratiki,demokaratiki→̌→ 7
dému,Dému→̌
demu,Dému→̌
dén,dén→̌→ 4572
den,dén→̌→ 4572
dèn,dèn→̌→ 4vr.dè.jè;dèn.
dɛ́n,dɛ́n→̌→ 7→v-v : 2vi.
dɛn,dɛ́n→̌→ 7→v-v : 2vi.
dèn,dɛ́n→̌→ 7→v-v : 2vi.
dèna,Dèna→̌Dako(Agriculteurs).
dena,Dèna→̌Dako(Agriculteurs).
denba,Denba→̌(Bergers.)
dénba,dénba( enfant mère )dénbaɲuman.
denba,dénba( enfant mère )dénbaɲuman.
dènba,Dènba→̌
dènbága,Dènbága→̌
denbaga,Dènbága→̌
dénbajala,dénbajala( mère [ enfant mère ] cordon )
denbajala,dénbajala( mère [ enfant mère ] cordon )
dénbajugu,dénbajugu( mère [ enfant mère ] méchant )
denbajugu,dénbajugu( mère [ enfant mère ] méchant )
dénbaɲuman,dénbaɲuman( enfant mère bon [ *adjectivateur ] )Voir entrée principale :dénba.
denbaɲuman,dénbaɲuman( enfant mère bon [ *adjectivateur ] )Voir entrée principale :dénba.
denbanyuman,dénbaɲuman( enfant mère bon [ *adjectivateur ] )Voir entrée principale :dénba.
dénbatigi,dénbatigi( mère [ enfant mère ] maître )
denbatigi,dénbatigi( mère [ enfant mère ] maître )
dénbatigiya,dénbatigiya( mère.de.famille [ mère [ enfant mère ] maître ] *abstractif )vi.
denbatigiya,dénbatigiya( mère.de.famille [ mère [ enfant mère ] maître ] *abstractif )vi.
dénbaya,dénbaya( mère [ enfant mère ] *abstractif )vi.
denbaya,dénbaya( mère [ enfant mère ] *abstractif )vi.
dénbayatigi,dénbayatigi( famille [ mère [ enfant mère ] *abstractif ] maître )
denbayatigi,dénbayatigi( famille [ mère [ enfant mère ] *abstractif ] maître )
dènbele,Dènbele→̌Dànbɛlɛ;Dànbele.
denbele,Dènbele→̌Dànbɛlɛ;Dànbele.
dénbo,dénbo( enfant excrément )
denbo,dénbo( enfant excrément )
dénbolo,dénbolo( enfant branche )
denbolo,dénbolo( enfant branche )
dɛ́nda,dɛ́nda( être.suspendu bouche )
dɛnda,dɛ́nda( être.suspendu bouche )
dènda,dɛ́nda( être.suspendu bouche )
dende,Dende→̌
dènde,dènde→̌
dende,dènde→̌
dɛndɛ,Dɛndɛ→̌
dèndè,Dɛndɛ→̌
dɛ́ndɛ,dɛ́ndɛ→̌vt.
dɛndɛ,dɛ́ndɛ→̌vt.
dɛ̀ndɛ,dɛ̀ndɛ→̌dɛ̀ndɛn;dɛ̀ɛndɛɛn;dɛ̀ɛndɛ;dànda.
dèndege,dèndege→̌dèndegelu.dègedegeli;dègedegelu;dèndegeru.
dendege,dèndege→̌dèndegelu.dègedegeli;dègedegelu;dèndegeru.
dèndegeli,dèndegeli→̌Voir entrée principale :dèndegeru.
dendegeli,dèndegeli→̌Voir entrée principale :dèndegeru.
dèndegelu,dèndegelu→̌dègedegeli;dègedegelu;dèndegeru;dèndege.
dendegelu,dèndegelu→̌dègedegeli;dègedegelu;dèndegeru;dèndege.
dèndegeru,dèndegeru→̌→ 1dèndegelu.dègedegeli;dègedegelu;dèndege.
dendegeru,dèndegeru→̌→ 1dèndegelu.dègedegeli;dègedegelu;dèndege.
dɛ̀ndɛn,dɛ̀ndɛn→̌dɛ̀ndɛ.dɛ̀ɛndɛɛn;dɛ̀ɛndɛ;dànda.
dɛndɛn,dɛ̀ndɛn→̌dɛ̀ndɛ.dɛ̀ɛndɛɛn;dɛ̀ɛndɛ;dànda.
dèndèn,dɛ̀ndɛn→̌dɛ̀ndɛ.dɛ̀ɛndɛɛn;dɛ̀ɛndɛ;dànda.
dɛ́ndɛndɛn,dɛ́ndɛndɛn→̌→ 3
dɛndɛndɛn,dɛ́ndɛndɛn→̌→ 3
dèndèndèn,dɛ́ndɛndɛn→̌→ 3
dɛ̀nɛ,dɛ̀nɛ→̌dɛ̀nɛn.dɛ̀nɛ.
dɛnɛ,dɛ̀nɛ→̌dɛ̀nɛn.dɛ̀nɛ.
dènè,dɛ̀nɛ→̌dɛ̀nɛn.dɛ̀nɛ.
dɛ̀ɲɛ,dɛ̀ɲɛ→̌→ 12
dɛɲɛ,dɛ̀ɲɛ→̌→ 12
dènyè,dɛ̀ɲɛ→̌→ 12
dɛ̀nɛn,dɛ̀nɛn→̌→ 27dɛ̀nɛ.
dɛnɛn,dɛ̀nɛn→̌→ 27dɛ̀nɛ.
dènèn,dɛ̀nɛn→̌→ 27dɛ̀nɛ.
dɛnɛnba,Dɛnɛnba→̌
dènènba,Dɛnɛnba→̌
dénfa,dénfa( enfant père )
denfa,dénfa( enfant père )
dénfaga,dénfaga( enfant tuer )
denfaga,dénfaga( enfant tuer )
dénfɔlɔya,dénfɔlɔya( enfant premier *abstractif )
denfɔlɔya,dénfɔlɔya( enfant premier *abstractif )
denfòlòya,dénfɔlɔya( enfant premier *abstractif )
dɛ̀ngɛnɛya,dɛ̀ngɛnɛya→̌→ 1dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dɛngɛnɛya,dɛ̀ngɛnɛya→̌→ 1dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dèngènèya,dɛ̀ngɛnɛya→̌→ 1dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dèngu,dèngu→̌→ 3dènkun.dɛ̀ɛnkun;dèenkun;jèenkun;jèngu;jènku.
dengu,dèngu→̌→ 3dènkun.dɛ̀ɛnkun;dèenkun;jèenkun;jèngu;jènku.
denisi,Denisi→̌
dénjɔbaliya,dénjɔbaliya( enfant dresser PTCP.NEG *abstractif )
denjɔbaliya,dénjɔbaliya( enfant dresser PTCP.NEG *abstractif )
denjòbaliya,dénjɔbaliya( enfant dresser PTCP.NEG *abstractif )
dénjugu,dénjugu( enfant méchant )
denjugu,dénjugu( enfant méchant )
dénjuguya,dénjuguya( égoïste [ enfant méchant ] *abstractif )
denjuguya,dénjuguya( égoïste [ enfant méchant ] *abstractif )
dénjuru,dénjuru( enfant corde )
denjuru,dénjuru( enfant corde )
dénkɛ,dénkɛ( enfant mâle )
denkɛ,dénkɛ( enfant mâle )
denkè,dénkɛ( enfant mâle )
dénkelendɛ̀mɛbaa,dénkelendɛ̀mɛbaa( enfant un aider *agent occasionnel )
denkelendɛmɛbaa,dénkelendɛ̀mɛbaa( enfant un aider *agent occasionnel )
denkelendèmèbaa,dénkelendɛ̀mɛbaa( enfant un aider *agent occasionnel )
dénkelenfili,dénkelenfili( enfant un jeter )
denkelenfili,dénkelenfili( enfant un jeter )
dɛ̀nkɛlɛntu,dɛ̀nkɛlɛntu→̌vt.
dɛnkɛlɛntu,dɛ̀nkɛlɛntu→̌vt.
dènkèlèntu,dɛ̀nkɛlɛntu→̌vt.
dɛ̀nkɛlɛnya,dɛ̀nkɛlɛnya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dɛnkɛlɛnya,dɛ̀nkɛlɛnya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dènkèlènya,dɛ̀nkɛlɛnya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dɛ́nkɛrɛfɛ,dɛ́nkɛrɛfɛ( mettre.à.l'écart par.côté [ côté par ] )
dɛnkɛrɛfɛ,dɛ́nkɛrɛfɛ( mettre.à.l'écart par.côté [ côté par ] )
dènkèrèfè,dɛ́nkɛrɛfɛ( mettre.à.l'écart par.côté [ côté par ] )
dɛ̀nkɛrɛnya,dɛ̀nkɛrɛnya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dɛnkɛrɛnya,dɛ̀nkɛrɛnya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dènkèrènya,dɛ̀nkɛrɛnya→̌dànkaniya.dɛ̀nkɛlɛnya;dàŋaniya;dɛ̀ngɛnɛya;dɛ̀nkɛrɛnya;dànkunnaya;dànkannaya.
dénko,dénko( enfant affaire )
denko,dénko( enfant affaire )
dénkoro,dénkoro→̌→ 1dɛ́nkuru.
denkoro,dénkoro→̌→ 1dɛ́nkuru.
dénkun,dénkun( enfant tête )
denkun,dénkun( enfant tête )
dènkun,dènkun→̌→ 1dèngu;dɛ̀ɛnkun;dèenkun;jèenkun;jèngu;jènku.
dénkundi,dénkundi( enfant rasage.de.tête [ tête raser ] )
denkundi,dénkundi( enfant rasage.de.tête [ tête raser ] )
dɛ́nkuru,dɛ́nkuru→̌dénkoro.dɛ́nkuru.
dɛnkuru,dɛ́nkuru→̌dénkoro.dɛ́nkuru.
dènkuru,dɛ́nkuru→̌dénkoro.dɛ́nkuru.
dɛ́nlɛn,dɛ́nlɛn→̌
dɛnlɛn,dɛ́nlɛn→̌
dènlèn,dɛ́nlɛn→̌
dénmarayɔrɔ,dénmarayɔrɔ( enfant garder lieu )
denmarayɔrɔ,dénmarayɔrɔ( enfant garder lieu )
denmarayòrò,dénmarayɔrɔ( enfant garder lieu )
dénmasa,dénmasa( enfant roi )
denmasa,dénmasa( enfant roi )
dénmisɛn,dénmisɛn( enfant petit )
denmisɛn,dénmisɛn( enfant petit )
denmisèn,dénmisɛn( enfant petit )
dénmisɛnman,dénmisɛnman( enfant petit [ petit *adjectivateur ] )
denmisɛnman,dénmisɛnman( enfant petit [ petit *adjectivateur ] )
denmisènman,dénmisɛnman( enfant petit [ petit *adjectivateur ] )
dénmisɛnnin,dénmisɛnnin( enfant petit *diminutif )
denmisɛnnin,dénmisɛnnin( enfant petit *diminutif )
denmisènnin,dénmisɛnnin( enfant petit *diminutif )
dénmisɛnɲɔgɔn,dénmisɛnɲɔgɔn( enfant petit *partenaire réciproque )
denmisɛnɲɔgɔn,dénmisɛnɲɔgɔn( enfant petit *partenaire réciproque )
denmisènnyògòn,dénmisɛnɲɔgɔn( enfant petit *partenaire réciproque )
dénmisɛnya,dénmisɛnya( enfant [ enfant petit ] *abstractif )
denmisɛnya,dénmisɛnya( enfant [ enfant petit ] *abstractif )
denmisènya,dénmisɛnya( enfant [ enfant petit ] *abstractif )
dénmuso,dénmuso( enfant féminin )
denmuso,dénmuso( enfant féminin )
dénnaanina,dénnaanina( enfant cajoler *agent permanent )
dennaanina,dénnaanina( enfant cajoler *agent permanent )
dénnabɔnɛtɔgɔ,dénnabɔnɛtɔgɔ( enfant *nom de lieu malheur nom )
dennabɔnɛtɔgɔ,dénnabɔnɛtɔgɔ( enfant *nom de lieu malheur nom )
dennabònètògò,dénnabɔnɛtɔgɔ( enfant *nom de lieu malheur nom )
dénnaminaden,dénnaminaden( enfant maintenir [ *causatif attraper ] enfant )dénnaminɛden.dénnɔminaden.
dennaminaden,dénnaminaden( enfant maintenir [ *causatif attraper ] enfant )dénnaminɛden.dénnɔminaden.
dénnaminɛden,dénnaminɛden( enfant maintenir [ *causatif attraper ] enfant )dénnaminaden;dénnɔminaden.
dennaminɛden,dénnaminɛden( enfant maintenir [ *causatif attraper ] enfant )dénnaminaden;dénnɔminaden.
dennaminèden,dénnaminɛden( enfant maintenir [ *causatif attraper ] enfant )dénnaminaden;dénnɔminaden.
dɛ́nnan,dɛ́nnan( mettre.à.l'écart *instrumental )
dɛnnan,dɛ́nnan( mettre.à.l'écart *instrumental )
dènnan,dɛ́nnan( mettre.à.l'écart *instrumental )
dénɲɛ̀rɛnin,dénɲɛ̀rɛnin( enfant *diminutif )dényɛ̀rɛnin.dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
denɲɛrɛnin,dénɲɛ̀rɛnin( enfant *diminutif )dényɛ̀rɛnin.dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
dennyèrènin,dénɲɛ̀rɛnin( enfant *diminutif )dényɛ̀rɛnin.dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
dɛ́nni,dɛ́nni( mettre.à.l'écart *nom d'action )
dɛnni,dɛ́nni( mettre.à.l'écart *nom d'action )
dènni,dɛ́nni( mettre.à.l'écart *nom d'action )
dénnin,dénnin( enfant *diminutif )
dennin,dénnin( enfant *diminutif )
dénɲinɛnin,dénɲinɛnin( enfant *diminutif )dényɛ̀rɛnin.dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
denɲinɛnin,dénɲinɛnin( enfant *diminutif )dényɛ̀rɛnin.dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
dennyinènin,dénɲinɛnin( enfant *diminutif )dényɛ̀rɛnin.dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
dénninkelen,dénninkelen( enfant *diminutif un )
denninkelen,dénninkelen( enfant *diminutif un )
dénnin-ó-dénnin,dénnin-ó-dénnin( enfant *diminutif *distributif enfant *diminutif )
dennin-o-dennin,dénnin-ó-dénnin( enfant *diminutif *distributif enfant *diminutif )
dénnɔminaden,dénnɔminaden( enfant maintenir [ *causatif attraper ] enfant )dénnaminɛden.dénnaminaden;dénnɔminaden.
dennɔminaden,dénnɔminaden( enfant maintenir [ *causatif attraper ] enfant )dénnaminɛden.dénnaminaden;dénnɔminaden.
dennòminaden,dénnɔminaden( enfant maintenir [ *causatif attraper ] enfant )dénnaminɛden.dénnaminaden;dénnɔminaden.
dénntan,dénntan( enfant *privatif )
denntan,dénntan( enfant *privatif )
dénntanmuso,dénntanmuso( sans.enfant [ enfant *privatif ] femme )
denntanmuso,dénntanmuso( sans.enfant [ enfant *privatif ] femme )
dénntanya,dénntanya( sans.enfant [ enfant *privatif ] *abstractif )
denntanya,dénntanya( sans.enfant [ enfant *privatif ] *abstractif )
denɔn,Denɔn→̌
denòn,Denɔn→̌
dénsaya,dénsaya( mort [ mourir *abstractif ] )
densaya,dénsaya( mort [ mourir *abstractif ] )
dénso,dénso( enfant maison )
denso,dénso( enfant maison )
dénsɔrɔ,dénsɔrɔ( enfant obtenir )
densɔrɔ,dénsɔrɔ( enfant obtenir )
densòrò,dénsɔrɔ( enfant obtenir )
dénsɔrɔbaliya,dénsɔrɔbaliya( enfant obtenir PTCP.NEG *abstractif )
densɔrɔbaliya,dénsɔrɔbaliya( enfant obtenir PTCP.NEG *abstractif )
densòròbaliya,dénsɔrɔbaliya( enfant obtenir PTCP.NEG *abstractif )
dénsu,dénsu( enfant cadavre )
densu,dénsu( enfant cadavre )
dénta,dénta( fructifier *participe potentiel )
denta,dénta( fructifier *participe potentiel )
déntigi,déntigi( enfant maître )
dentigi,déntigi( enfant maître )
déntigiya,déntigiya( personne.féconde [ enfant maître ] *abstractif )vt.
dentigiya,déntigiya( personne.féconde [ enfant maître ] *abstractif )vt.
dɛ́nw,dɛ́nw→̌téwu.déwu.
dɛnw,dɛ́nw→̌téwu.déwu.
dènw,dɛ́nw→̌téwu.déwu.
dénwolobali,dénwolobali( enfant accoucher PTCP.NEG )
denwolobali,dénwolobali( enfant accoucher PTCP.NEG )
dénwolobaliya,dénwolobaliya( sans.enfants [ enfant accoucher PTCP.NEG ] *abstractif )
denwolobaliya,dénwolobaliya( sans.enfants [ enfant accoucher PTCP.NEG ] *abstractif )
dénwolomuso,dénwolomuso( enfant accoucher femme )
denwolomuso,dénwolomuso( enfant accoucher femme )
dénwolonugu,dénwolonugu( enfant accoucher intestin )
denwolonugu,dénwolonugu( enfant accoucher intestin )
dénya,dénya( enfant *abstractif )
denya,dénya( enfant *abstractif )
dényɛ̀nin,dényɛ̀nin( enfant *diminutif )dényɛ̀rɛnin.dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
denyɛnin,dényɛ̀nin( enfant *diminutif )dényɛ̀rɛnin.dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
denyènin,dényɛ̀nin( enfant *diminutif )dényɛ̀rɛnin.dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
dényɛ̀rɛnin,dényɛ̀rɛnin( enfant *diminutif )dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
denyɛrɛnin,dényɛ̀rɛnin( enfant *diminutif )dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
denyèrènin,dényɛ̀rɛnin( enfant *diminutif )dénɲɛ̀rɛnin;dényɛ̀nin;dénɲinɛnin.
depariteman,depariteman→̌→ 1
depilase,depilase→̌→ 4
dèpite,dèpite→̌→ 147
depite,dèpite→̌→ 147
dèpitebulon,dèpitebulon( député antichambre )
depitebulon,dèpitebulon( député antichambre )
dère,dère→̌ntèle.ntère;dère.
dere,dère→̌ntèle.ntère;dère.
dɛ́rɛ,dɛ́rɛ→̌→ 229
dɛrɛ,dɛ́rɛ→̌→ 229
dèrè,dɛ́rɛ→̌→ 229
dɛ̀rɛ,dɛ̀rɛ→̌→ 12vt.dɛ̀rɛn.
dɛ́rɛɛ,dɛ́rɛɛ→̌dɛ́rrɛ.dɛ́rɛtɛtɛ;dɛ́rɛɛ;drɛ́ɛ.
dɛrɛɛ,dɛ́rɛɛ→̌dɛ́rrɛ.dɛ́rɛtɛtɛ;dɛ́rɛɛ;drɛ́ɛ.
dèrèe,dɛ́rɛɛ→̌dɛ́rrɛ.dɛ́rɛtɛtɛ;dɛ́rɛɛ;drɛ́ɛ.
déren,déren→̌vr.
deren,déren→̌vr.
dɛ̀rɛn,dɛ̀rɛn→̌vt.dɛ̀rɛ.dɛ̀rɛn.
dɛrɛn,dɛ̀rɛn→̌vt.dɛ̀rɛ.dɛ̀rɛn.
dèrèn,dɛ̀rɛn→̌vt.dɛ̀rɛ.dɛ̀rɛn.
dɛ́rɛsi,dɛ́rɛsi→̌→ 1
dɛrɛsi,dɛ́rɛsi→̌→ 1
dèrèsi,dɛ́rɛsi→̌→ 1
dɛ́rɛtɛtɛ,dɛ́rɛtɛtɛ→̌dɛ́rrɛ.dɛ́rɛɛ;drɛ́ɛ.
dɛrɛtɛtɛ,dɛ́rɛtɛtɛ→̌dɛ́rrɛ.dɛ́rɛɛ;drɛ́ɛ.
dèrètètè,dɛ́rɛtɛtɛ→̌dɛ́rrɛ.dɛ́rɛɛ;drɛ́ɛ.
dɛ́rrɛ,dɛ́rrɛ→̌dɛ́rɛtɛtɛ;dɛ́rɛɛ;drɛ́ɛ.
dɛrrɛ,dɛ́rrɛ→̌dɛ́rɛtɛtɛ;dɛ́rɛɛ;drɛ́ɛ.
dèrrè,dɛ́rrɛ→̌dɛ́rɛtɛtɛ;dɛ́rɛɛ;drɛ́ɛ.
dɛ́rsàlám,Dɛ́rsàlám→̌
dɛrsalam,Dɛ́rsàlám→̌
dèrsalam,Dɛ́rsàlám→̌
désanburu,désanburu→̌→ 12Source :fr : décembre.
desanburu,désanburu→̌→ 12Source :fr : décembre.
désantaralizasɔn,désantaralizasɔn→̌→ 39
desantaralizasɔn,désantaralizasɔn→̌→ 39
desantaralizasòn,désantaralizasɔn→̌→ 39
désantaralize,désantaralize→̌
desantaralize,désantaralize→̌
dɛ́sɛ,dɛ́sɛ→̌→ 315→n : 15
dɛsɛ,dɛ́sɛ→̌→ 315→n : 15
dèsè,dɛ́sɛ→̌→ 315→n : 15
dɛ̀sɛ,dɛ̀sɛ→̌→ 1
dɛ́sɛbaatɔ,dɛ́sɛbaatɔ( échouer *agent occasionnel *statif )Voir entrée principale :dɛ́sɛbagatɔ.
dɛsɛbaatɔ,dɛ́sɛbaatɔ( échouer *agent occasionnel *statif )Voir entrée principale :dɛ́sɛbagatɔ.
dèsèbaatò,dɛ́sɛbaatɔ( échouer *agent occasionnel *statif )Voir entrée principale :dɛ́sɛbagatɔ.
dɛ́sɛbagatɔ,dɛ́sɛbagatɔ( échouer *agent occasionnel *statif )dɛ́sɛbaatɔ.
dɛsɛbagatɔ,dɛ́sɛbagatɔ( échouer *agent occasionnel *statif )dɛ́sɛbaatɔ.
dèsèbagatò,dɛ́sɛbagatɔ( échouer *agent occasionnel *statif )dɛ́sɛbaatɔ.
dɛ́sɛlan,dɛ́sɛlan( tailler *instrumental )
dɛsɛlan,dɛ́sɛlan( tailler *instrumental )
dèsèlan,dɛ́sɛlan( tailler *instrumental )
desɛn,desɛn→̌
desèn,desɛn→̌
dɛ́sɛn,dɛ́sɛn→̌→ 1→n : 1vt.Voir entrée principale :dɛ́sɛ.
dɛsɛn,dɛ́sɛn→̌→ 1→n : 1vt.Voir entrée principale :dɛ́sɛ.
dèsèn,dɛ́sɛn→̌→ 1→n : 1vt.Voir entrée principale :dɛ́sɛ.
dɛ́sɛnyɛ̀rɛkɔ́rɔ,dɛ́sɛnyɛ̀rɛkɔ́rɔ( échouer *je même sous )dɛ́sɛ-ń-yɛ̀rɛ-kɔ́rɔ.dɛ́sɛnyɛ̀rɛkɔ́rɔ.
dɛsɛnyɛrɛkɔrɔ,dɛ́sɛnyɛ̀rɛkɔ́rɔ( échouer *je même sous )dɛ́sɛ-ń-yɛ̀rɛ-kɔ́rɔ.dɛ́sɛnyɛ̀rɛkɔ́rɔ.
dèsènyèrèkòrò,dɛ́sɛnyɛ̀rɛkɔ́rɔ( échouer *je même sous )dɛ́sɛ-ń-yɛ̀rɛ-kɔ́rɔ.dɛ́sɛnyɛ̀rɛkɔ́rɔ.
dɛ́sɛ-ń-yɛ̀rɛ-kɔ́rɔ,dɛ́sɛ-ń-yɛ̀rɛ-kɔ́rɔ( échouer *je même sous )dɛ́sɛnyɛ̀rɛkɔ́rɔ.
dɛsɛ-n-yɛrɛ-kɔrɔ,dɛ́sɛ-ń-yɛ̀rɛ-kɔ́rɔ( échouer *je même sous )dɛ́sɛnyɛ̀rɛkɔ́rɔ.
dèsè-n-yèrè-kòrò,dɛ́sɛ-ń-yɛ̀rɛ-kɔ́rɔ( échouer *je même sous )dɛ́sɛnyɛ̀rɛkɔ́rɔ.
dɛ̀si,dɛ̀si→̌→n : 1dàsi.dɛ̀si.
dɛsi,dɛ̀si→̌→n : 1dàsi.dɛ̀si.
dèsi,dɛ̀si→̌→n : 1dàsi.dɛ̀si.
desilitiri,desilitiri→̌→ 3
desimɛtɛrɛ,desimɛtɛrɛ→̌→ 12
desimètèrè,desimɛtɛrɛ→̌→ 12
détayi,détayi→̌
detayi,détayi→̌
deteba,Deteba→̌
dewaliyasɔn,dewaliyasɔn→̌
dewaliyasòn,dewaliyasɔn→̌
dewelopeman,dewelopeman→̌
déwu,déwu→̌→ 14
dewu,déwu→̌→ 14
dèyɛfu,Dèyɛfu→̌→ 2Voir entrée principale :dèyɛfu.
deyɛfu,Dèyɛfu→̌→ 2Voir entrée principale :dèyɛfu.
deyèfu,Dèyɛfu→̌→ 2Voir entrée principale :dèyɛfu.
dezɛmu,dezɛmu→̌
dezèmu,dezɛmu→̌
dezɛri,dezɛri→̌
dezèri,dezɛri→̌
deziyɛmu,deziyɛmu→̌
deziyèmu,deziyɛmu→̌
dezusitisi,dezusitisi→̌Voir entrée principale :zusitisi.
dí,dí→̌→ 92
di,dí→̌→ 92
dì,dì→̌→ 649
díbagan,díbagan( miel sans.sauce )díbanga.
dibagan,díbagan( miel sans.sauce )díbanga.
díbanga,díbanga( miel sans.sauce )Voir entrée principale :díbagan.
dibanga,díbanga( miel sans.sauce )Voir entrée principale :díbagan.
díbara,díbara( miel calebasse )
dibara,díbara( miel calebasse )
díbi,díbi→̌→ 24
dibi,díbi→̌→ 24
dìbi,dìbi→̌→ 148
díbida,díbida( four bouche )
dibida,díbida( four bouche )
dibidanin,Dibidanin→̌
díbiden,díbiden( four enfant )
dibiden,díbiden( four enfant )
dìbidibi,dìbidibi→̌→ 3
dibidibi,dìbidibi→̌→ 3
dìbi-dibi,dìbi-dibi( être.obscur être.obscur )dìbidìbi;dìibidìibi.
dibi-dibi,dìbi-dibi( être.obscur être.obscur )dìbidìbi;dìibidìibi.
dìbidìbi,dìbidìbi( être.obscur être.obscur )dìbi-dibi.dìbidìbi;dìibidìibi.
dibidibi,dìbidìbi( être.obscur être.obscur )dìbi-dibi.dìbidìbi;dìibidìibi.
díbijiri,díbijiri( four arbre )
dibijiri,díbijiri( four arbre )
dìbilan,dìbilan( être.obscur *instrumental )
dibilan,dìbilan( être.obscur *instrumental )
dìbinin,dìbinin( obscurité *diminutif )
dibinin,dìbinin( obscurité *diminutif )
díbiri,díbiri→̌→ 7
dibiri,díbiri→̌→ 7
díbɔ,díbɔ( miel sortie )
dibɔ,díbɔ( miel sortie )
dibò,díbɔ( miel sortie )
diboli,Diboli→̌
diboromuru,diboromuru→̌→ 1Voir entrée principale :boromuru.
dìdadi,dìdadi→̌→ 1
didadi,dìdadi→̌→ 1
dídɛgɛ,dídɛgɛ( miel brouet )
didɛgɛ,dídɛgɛ( miel brouet )
didègè,dídɛgɛ( miel brouet )
díden,díden( miel enfant )
diden,díden( miel enfant )
dídentɔ,dídentɔ( abeille [ miel enfant ] *statif )jídentɔ.
didentɔ,dídentɔ( abeille [ miel enfant ] *statif )jídentɔ.
didentò,dídentɔ( abeille [ miel enfant ] *statif )jídentɔ.
dídidi,dídidi→̌
dididi,dídidi→̌
didɔrɔzɛni,didɔrɔzɛni→̌→ 1Voir entrée principale :idɔrɔzɛni.
didòròzèni,didɔrɔzɛni→̌→ 1Voir entrée principale :idɔrɔzɛni.
dídɔrɔzɛni,dídɔrɔzɛni→̌→ 1ídorozɛni.ídɔrɔzɛni;dídɔrɔzɛni;hídorozɛni.Fr. hydrogène
didɔrɔzɛni,dídɔrɔzɛni→̌→ 1ídorozɛni.ídɔrɔzɛni;dídɔrɔzɛni;hídorozɛni.Fr. hydrogène
difenidaramini,difenidaramini→̌→ 14
difenilidantoyini,difenilidantoyini→̌→ 2
difenɔkisilati,difenɔkisilati→̌→ 2
difenòkisilati,difenɔkisilati→̌→ 2
díga,díga→̌
diga,díga→̌
digato,Digato→̌
dige,dige→̌
dígi,dígi→̌→ 27vt.
digi,dígi→̌→ 27vt.
dìgon,dìgon→̌→ 1
digon,dìgon→̌→ 1
dìibidìibi,dìibidìibi( être.obscur être.obscur )dìbi-dibi.dìbidìbi;dìibidìibi.
diibidiibi,dìibidìibi( être.obscur être.obscur )dìbi-dibi.dìbidìbi;dìibidìibi.
díilidiili,díilidiili→̌
diilidiili,díilidiili→̌
díina,díina→̌díinɛ.díina.ar: din = religion
diina,díina→̌díinɛ.díina.ar: din = religion
díinɛ,díinɛ→̌→ 131díina.ar: din = religion
diinɛ,díinɛ→̌→ 131díina.ar: din = religion
diinè,díinɛ→̌→ 131díina.ar: din = religion
díinɛjugu,díinɛjugu( religion méchant )
diinɛjugu,díinɛjugu( religion méchant )
diinèjugu,díinɛjugu( religion méchant )
díinɛɲɛmɔgɔ,díinɛɲɛmɔgɔ( religion dirigeant [ oeil homme ] )
diinɛɲɛmɔgɔ,díinɛɲɛmɔgɔ( religion dirigeant [ oeil homme ] )
diinènyèmògò,díinɛɲɛmɔgɔ( religion dirigeant [ oeil homme ] )
díji,díji( miel eau )
diji,díji( miel eau )
dikani,Dikani→̌
díkisɛ,díkisɛ( miel grain )
dikisɛ,díkisɛ( miel grain )
dikisè,díkisɛ( miel grain )
dikko,Dikko→̌Dikɔ;Diko.
diko,Diko→̌Dikko.Dikɔ.
dikɔ,Dikɔ→̌Dikko.Diko.
dikò,Dikɔ→̌Dikko.Diko.
díkòlen,díkòlen( miel laver *participe résultatif )
dikolen,díkòlen( miel laver *participe résultatif )
dikulɔkisisilini,dikulɔkisisilini→̌→n.prop : 17
dikulòkisisilini,dikulɔkisisilini→̌→n.prop : 17
díla,díla→̌→ 725→n : 220vt.dílan.díla;bíla;dlá;dlán.
dila,díla→̌→ 725→n : 220vt.dílan.díla;bíla;dlá;dlán.
dílan,dílan→̌→ 508→n : 224vt.díla;bíla;dlá;dlán.
dilan,dílan→̌→ 508→n : 224vt.díla;bíla;dlá;dlán.
dílannabana,dílannabana( lit [ poser *instrumental ] à maladie )dálannabana;dlánnabana.
dilannabana,dílannabana( lit [ poser *instrumental ] à maladie )dálannabana;dlánnabana.
dilaye,Dilaye→̌
díli,díli→̌→ 46gíli;bíli;dlí;líli.
dili,díli→̌→ 46gíli;bíli;dlí;líli.
dílisɛbɛn,dílisɛbɛn( action.de.donner [ donner *nom d'action ] écrit )
dilisɛbɛn,dílisɛbɛn( action.de.donner [ donner *nom d'action ] écrit )
dilisèbèn,dílisɛbɛn( action.de.donner [ donner *nom d'action ] écrit )
dilokisanidi,dilokisanidi→̌→ 10
dimansi,dimansi→̌Source :fr.
dimɛnidaranati,dimɛnidaranati→̌→ 7
dimènidaranati,dimɛnidaranati→̌→ 7
dími,dími→̌→ 602dímin.
dimi,dími→̌→ 602dímin.
dímibaatɔ,dímibaatɔ( souffrance *agent occasionnel *statif )Voir entrée principale :dímibagatɔ.
dimibaatɔ,dímibaatɔ( souffrance *agent occasionnel *statif )Voir entrée principale :dímibagatɔ.
dimibaatò,dímibaatɔ( souffrance *agent occasionnel *statif )Voir entrée principale :dímibagatɔ.
dímibagatɔ,dímibagatɔ( souffrance *agent occasionnel *statif )dímibaatɔ.
dimibagatɔ,dímibagatɔ( souffrance *agent occasionnel *statif )dímibaatɔ.
dimibagatò,dímibagatɔ( souffrance *agent occasionnel *statif )dímibaatɔ.
dímidon,dímidon( souffrance entrer )dímindon.
dimidon,dímidon( souffrance entrer )dímindon.
dímikɔrɔbɔ,dímikɔrɔbɔ( souffrance essayer [ dessous sortir ] )
dimikɔrɔbɔ,dímikɔrɔbɔ( souffrance essayer [ dessous sortir ] )
dimikòròbò,dímikɔrɔbɔ( souffrance essayer [ dessous sortir ] )
dímimadalan,dímimadalan( souffrance incliner [ *connecteur poser ] *instrumental )
dimimadalan,dímimadalan( souffrance incliner [ *connecteur poser ] *instrumental )
dímin,dímin→̌→ 1dími.dímin.
dimin,dímin→̌→ 1dími.dímin.
dímindon,dímindon( souffrance entrer )dímidon.dímindon.
dimindon,dímindon( souffrance entrer )dímidon.dímindon.
dímiya,dímiya( souffrance *abstractif )
dimiya,dímiya( souffrance *abstractif )
dímɔgɔ,dímɔgɔ→̌→ 97límɔgɔ.
dimɔgɔ,dímɔgɔ→̌→ 97límɔgɔ.
dimògò,dímɔgɔ→̌→ 97límɔgɔ.
dìna,dìna→̌Voir entrée principale :dìndan.
dina,dìna→̌Voir entrée principale :dìndan.
díɲaga,díɲaga( miel résidu )
diɲaga,díɲaga( miel résidu )
dinyaga,díɲaga( miel résidu )
dinari,dinari→̌→ 1
dinbali,Dinbali→̌
dìndan,dìndan→̌→ 2dìna.
dindan,dìndan→̌→ 2dìna.
díɲɛ,díɲɛ→̌→ 1631díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
diɲɛ,díɲɛ→̌→ 1631díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dinyè,díɲɛ→̌→ 1631díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dìɲɛ,dìɲɛ→̌→ 35jɛ̀n.dìɲɛ.
díɲɛden,díɲɛden( monde enfant )díyɛnden.
diɲɛden,díɲɛden( monde enfant )díyɛnden.
dinyèden,díɲɛden( monde enfant )díyɛnden.
díɲɛdenya,díɲɛdenya( bon.vivant [ monde enfant ] *abstractif )díyɛndenya.
diɲɛdenya,díɲɛdenya( bon.vivant [ monde enfant ] *abstractif )díyɛndenya.
dinyèdenya,díɲɛdenya( bon.vivant [ monde enfant ] *abstractif )díyɛndenya.
díɲɛlaban,díɲɛlaban( monde fin [ *causatif terminer ] )díyɛnlaban.
diɲɛlaban,díɲɛlaban( monde fin [ *causatif terminer ] )díyɛnlaban.
dinyèlaban,díɲɛlaban( monde fin [ *causatif terminer ] )díyɛnlaban.
díɲɛlatigɛ,díɲɛlatigɛ( monde faire.passer [ *causatif couper ] )díɲɛnatigɛ.díyɛnnatigɛ;jyɛ́nlatigɛ.
diɲɛlatigɛ,díɲɛlatigɛ( monde faire.passer [ *causatif couper ] )díɲɛnatigɛ.díyɛnnatigɛ;jyɛ́nlatigɛ.
dinyèlatigè,díɲɛlatigɛ( monde faire.passer [ *causatif couper ] )díɲɛnatigɛ.díyɛnnatigɛ;jyɛ́nlatigɛ.
díɲɛnabɔ,díɲɛnabɔ( monde à sortir )díyɛnnabɔ;jíɲɛnabɔ.
diɲɛnabɔ,díɲɛnabɔ( monde à sortir )díyɛnnabɔ;jíɲɛnabɔ.
dinyènabò,díɲɛnabɔ( monde à sortir )díyɛnnabɔ;jíɲɛnabɔ.
díɲɛnatigɛ,díɲɛnatigɛ( monde faire.passer [ *causatif couper ] )díɲɛlatigɛ;díyɛnnatigɛ;jyɛ́nlatigɛ.
diɲɛnatigɛ,díɲɛnatigɛ( monde faire.passer [ *causatif couper ] )díɲɛlatigɛ;díyɛnnatigɛ;jyɛ́nlatigɛ.
dinyènatigè,díɲɛnatigɛ( monde faire.passer [ *causatif couper ] )díɲɛlatigɛ;díyɛnnatigɛ;jyɛ́nlatigɛ.
díɲɛselekenaani,díɲɛselekenaani( monde angle quatre )
diɲɛselekenaani,díɲɛselekenaani( monde angle quatre )
dinyèselekenaani,díɲɛselekenaani( monde angle quatre )
díɲɛso,díɲɛso( monde maison )
diɲɛso,díɲɛso( monde maison )
dinyèso,díɲɛso( monde maison )
díɲɛsosigi,díɲɛsosigi( monde [ monde maison ] position.assise )díyɛnsosigi.
diɲɛsosigi,díɲɛsosigi( monde [ monde maison ] position.assise )díyɛnsosigi.
dinyèsosigi,díɲɛsosigi( monde [ monde maison ] position.assise )díyɛnsosigi.
díɲɛwuli,díɲɛwuli( monde se.lever )díyɛnwuli.
diɲɛwuli,díɲɛwuli( monde se.lever )díyɛnwuli.
dinyèwuli,díɲɛwuli( monde se.lever )díyɛnwuli.
dìngɛ,dìngɛ→̌→ 239dìngɛn.
dingɛ,dìngɛ→̌→ 239dìngɛn.
dingè,dìngɛ→̌→ 239dìngɛn.
dìngɛn,dìngɛn→̌→ 6dìngɛ.dìngɛn.
dingɛn,dìngɛn→̌→ 6dìngɛ.dìngɛn.
dingèn,dìngɛn→̌→ 6dìngɛ.dìngɛn.
dìngɔ,dìngɔ→̌→ 2
dingɔ,dìngɔ→̌→ 2
dingò,dìngɔ→̌→ 2
dínkamo,dínkamo( miel pollen )
dinkamo,dínkamo( miel pollen )
díńmà,díńmà( donner *je *à )
dinma,díńmà( donner *je *à )
dínɔ̀nɔ,dínɔ̀nɔ( miel jus )dí-nɔ̀ɔnɔ.dínɔ̀ɔnɔ.
dinɔnɔ,dínɔ̀nɔ( miel jus )dí-nɔ̀ɔnɔ.dínɔ̀ɔnɔ.
dinònò,dínɔ̀nɔ( miel jus )dí-nɔ̀ɔnɔ.dínɔ̀ɔnɔ.
dínɔ̀ɔnɔ,dínɔ̀ɔnɔ( miel jus )dí-nɔ̀ɔnɔ.dínɔ̀ɔnɔ;dínɔ̀nɔ.
dinɔɔnɔ,dínɔ̀ɔnɔ( miel jus )dí-nɔ̀ɔnɔ.dínɔ̀ɔnɔ;dínɔ̀nɔ.
dinòonò,dínɔ̀ɔnɔ( miel jus )dí-nɔ̀ɔnɔ.dínɔ̀ɔnɔ;dínɔ̀nɔ.
dí-nɔ̀ɔnɔ,dí-nɔ̀ɔnɔ( miel jus )dínɔ̀ɔnɔ;dínɔ̀nɔ.
di-nɔɔnɔ,dí-nɔ̀ɔnɔ( miel jus )dínɔ̀ɔnɔ;dínɔ̀nɔ.
di-nòonò,dí-nɔ̀ɔnɔ( miel jus )dínɔ̀ɔnɔ;dínɔ̀nɔ.
diparɔpisi,diparɔpisi→̌
diparòpisi,diparɔpisi→̌
dípilɔmu,dípilɔmu→̌dípulɔmu.dípilɔmu.Fr. diplôme
dipilɔmu,dípilɔmu→̌dípulɔmu.dípilɔmu.Fr. diplôme
dipilòmu,dípilɔmu→̌dípulɔmu.dípilɔmu.Fr. diplôme
dipɔlɔmu,dipɔlɔmu→̌Voir entrée principale :dípulɔmu.
dipòlòmu,dipɔlɔmu→̌Voir entrée principale :dípulɔmu.
dípulɔmu,dípulɔmu→̌→ 6dípilɔmu.Fr. diplôme
dipulɔmu,dípulɔmu→̌→ 6dípilɔmu.Fr. diplôme
dipulòmu,dípulɔmu→̌→ 6dípilɔmu.Fr. diplôme
dire,Dire→̌
dirɛkitɛri,dirɛkitɛri→̌→ 5
dirèkitèri,dirɛkitɛri→̌→ 5
direyi,Direyi→̌
díri,Díri→̌Dirisa.Ídrìsa;Idirisa;Dìrí.
diri,Díri→̌Dirisa.Ídrìsa;Idirisa;Dìrí.
dìrí,Dìrí→̌Dirisa.Ídrìsa;Idirisa;Díri.
díridara,díridara→̌vt.
diridara,díridara→̌vt.
dirisa,Dirisa→̌Ídrìsa;Idirisa;Díri;Dìrí.
dìro,dìro→̌→ 8
diro,dìro→̌→ 8
dìsa,dìsa→̌→ 41
disa,dìsa→̌→ 41
dìsá,Dìsá→̌
dìsakunkurunnin,dìsakunkurunnin( turban morceau [ tête court ] *diminutif )
disakunkurunnin,dìsakunkurunnin( turban morceau [ tête court ] *diminutif )
dísi,dísi→̌→ 152
disi,dísi→̌→ 152
dìsi,dìsi→̌→ 2
dísida,dísida( poitrine bouche )
disida,dísida( poitrine bouche )
dísidimi,dísidimi( poitrine souffrance )
disidimi,dísidimi( poitrine souffrance )
dísifilenkolonin,dísifilenkolonin( poitrine calebasse.demi-sphérique os *diminutif )dísifilennin.
disifilenkolonin,dísifilenkolonin( poitrine calebasse.demi-sphérique os *diminutif )dísifilennin.
dísifilennin,dísifilennin( poitrine calebasse.demi-sphérique *diminutif )Voir entrée principale :dísifilenkolonin.
disifilennin,dísifilennin( poitrine calebasse.demi-sphérique *diminutif )Voir entrée principale :dísifilenkolonin.
dísikolo,dísikolo( poitrine os )
disikolo,dísikolo( poitrine os )
dísikun,dísikun( poitrine tête )
disikun,dísikun( poitrine tête )
dísikunkolo,dísikunkolo( haut.de.la.poitrine [ poitrine tête ] os )
disikunkolo,dísikunkolo( haut.de.la.poitrine [ poitrine tête ] os )
disilame,Disilame→̌
dísirɔbana,dísirɔbana( poitrine dans maladie )
disirɔbana,dísirɔbana( poitrine dans maladie )
disiròbana,dísirɔbana( poitrine dans maladie )
dísirɔden,dísirɔden( poitrine dans enfant )
disirɔden,dísirɔden( poitrine dans enfant )
disiròden,dísirɔden( poitrine dans enfant )
disitiriki,disitiriki→̌→ 4
díso,díso( miel maison )
diso,díso( miel maison )
dísɔngɔ,dísɔngɔ( miel prix )
disɔngɔ,dísɔngɔ( miel prix )
disòngò,dísɔngɔ( miel prix )
dítebin,dítebin( thé.vert herbe )dùtebin.dítebin;bíndute.
ditebin,dítebin( thé.vert herbe )dùtebin.dítebin;bíndute.
díwaa,díwaa( miel rayon.de.miel )
diwaa,díwaa( miel rayon.de.miel )
diwidi,diwidi→̌
diwisɔn,diwisɔn→̌Voir entrée principale :diwizɔn.
diwisòn,diwisɔn→̌Voir entrée principale :diwizɔn.
diwizɔn,diwizɔn→̌→ 1
diwizòn,diwizɔn→̌→ 1
díya,díya( agréable *en verbe dynamique )já.
diya,díya( agréable *en verbe dynamique )já.
díyabaatɔ,díyabaatɔ( rendre.agréable [ agréable *en verbe dynamique ] *agent occasionnel *statif )díyabagatɔ.jábaatɔ;jábagatɔ.
diyabaatɔ,díyabaatɔ( rendre.agréable [ agréable *en verbe dynamique ] *agent occasionnel *statif )díyabagatɔ.jábaatɔ;jábagatɔ.
diyabaatò,díyabaatɔ( rendre.agréable [ agréable *en verbe dynamique ] *agent occasionnel *statif )díyabagatɔ.jábaatɔ;jábagatɔ.
díyabagatɔ,díyabagatɔ( rendre.agréable [ agréable *en verbe dynamique ] *agent occasionnel *statif )díyabaatɔ;jábaatɔ;jábagatɔ.
diyabagatɔ,díyabagatɔ( rendre.agréable [ agréable *en verbe dynamique ] *agent occasionnel *statif )díyabaatɔ;jábaatɔ;jábagatɔ.
diyabagatò,díyabagatɔ( rendre.agréable [ agréable *en verbe dynamique ] *agent occasionnel *statif )díyabaatɔ;jábaatɔ;jábagatɔ.
díyabɔ,díyabɔ( bon.goût [ agréable *en verbe dynamique ] sortir )
diyabɔ,díyabɔ( bon.goût [ agréable *en verbe dynamique ] sortir )
diyabò,díyabɔ( bon.goût [ agréable *en verbe dynamique ] sortir )
díyagoya,díyagoya( rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique )vt.díyakoya;jákoya;jágoya.
diyagoya,díyagoya( rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique )vt.díyakoya;jákoya;jágoya.
díyagòya,díyagòya( bon.goût [ agréable *en verbe dynamique ] désagréable *en verbe dynamique )díyakòya;jákòya;jágòya.
díyagoyabaara,díyagoyabaara( de.force [ rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique ] travail )
diyagoyabaara,díyagoyabaara( de.force [ rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique ] travail )
díyagoyafanga,díyagoyafanga( de.force [ rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique ] force )
diyagoyafanga,díyagoyafanga( de.force [ rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique ] force )
díyagoyafuru,díyagoyafuru( de.force [ rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique ] mariage )
diyagoyafuru,díyagoyafuru( de.force [ rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique ] mariage )
díyakoya,díyakoya( rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique )vt.díyagoya.díyakoya;jákoya;jágoya.
diyakoya,díyakoya( rendre.agréable [ agréable *en verbe dynamique ] désagréable *en verbe dynamique )vt.díyagoya.díyakoya;jákoya;jágoya.
díyakòya,díyakòya( bon.goût [ agréable *en verbe dynamique ] désagréable *en verbe dynamique )díyagòya.díyakòya;jákòya;jágòya.
díyaɲɔgɔn,díyaɲɔgɔn( rendre.agréable [ agréable *en verbe dynamique ] *partenaire réciproque )
diyaɲɔgɔn,díyaɲɔgɔn( rendre.agréable [ agréable *en verbe dynamique ] *partenaire réciproque )
diyanyògòn,díyaɲɔgɔn( rendre.agréable [ agréable *en verbe dynamique ] *partenaire réciproque )
díyanye,díyanye( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique )jánye.
diyanye,díyanye( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique )jánye.
díyanyebaa,díyanyebaa( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel )díyanyebaga.jányebaa.
diyanyebaa,díyanyebaa( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel )díyanyebaga.jányebaa.
díyanyebaatɔ,díyanyebaatɔ( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel *statif )díyanyebagatɔ.jányebaatɔ.
diyanyebaatɔ,díyanyebaatɔ( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel *statif )díyanyebagatɔ.jányebaatɔ.
diyanyebaatò,díyanyebaatɔ( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel *statif )díyanyebagatɔ.jányebaatɔ.
díyanyebaga,díyanyebaga( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel )díyanyebaa;jányebaa.
diyanyebaga,díyanyebaga( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel )díyanyebaa;jányebaa.
díyanyebagatɔ,díyanyebagatɔ( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel *statif )díyanyebaatɔ;jányebaatɔ.
diyanyebagatɔ,díyanyebagatɔ( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel *statif )díyanyebaatɔ;jányebaatɔ.
diyanyebagatò,díyanyebagatɔ( rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique *agent occasionnel *statif )díyanyebaatɔ;jányebaatɔ.
díyanyeko,díyanyeko( plaisir [ rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique ] affaire )jányeko.
diyanyeko,díyanyeko( plaisir [ rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique ] affaire )jányeko.
díyanyemaa,díyanyemaa( plaisir [ rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique ] homme )díyanyemɔgɔ.jányemɔgɔ;jányemaa.
diyanyemaa,díyanyemaa( plaisir [ rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique ] homme )díyanyemɔgɔ.jányemɔgɔ;jányemaa.
díyanyemɔgɔ,díyanyemɔgɔ( plaisir [ rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique ] homme )díyanyemaa;jányemɔgɔ;jányemaa.
diyanyemɔgɔ,díyanyemɔgɔ( plaisir [ rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique ] homme )díyanyemaa;jányemɔgɔ;jányemaa.
diyanyemògò,díyanyemɔgɔ( plaisir [ rendre.agréable [ agréable *en verbe dynamique ] *je *postposition polysémique ] homme )díyanyemaa;jányemɔgɔ;jányemaa.
díyanyɛrɛlamaa,díyanyɛrɛlamaa( rendre.agréable [ agréable *en verbe dynamique ] *je même à homme )jányɛrɛlamaa.
diyanyɛrɛlamaa,díyanyɛrɛlamaa( rendre.agréable [ agréable *en verbe dynamique ] *je même à homme )jányɛrɛlamaa.
diyanyèrèlamaa,díyanyɛrɛlamaa( rendre.agréable [ agréable *en verbe dynamique ] *je même à homme )jányɛrɛlamaa.
díyasana,Díyasana→̌Jásana.
diyasana,Díyasana→̌Jásana.
díyatɔ,díyatɔ→̌játɔ.jádɔ;díyatɔ.
diyatɔ,díyatɔ→̌játɔ.jádɔ;díyatɔ.
diyatò,díyatɔ→̌játɔ.jádɔ;díyatɔ.
díyatɔcɛ,díyatɔcɛ( rendre.agréable [ agréable *en verbe dynamique ] *statif mâle )
diyatɔcɛ,díyatɔcɛ( rendre.agréable [ agréable *en verbe dynamique ] *statif mâle )
diyatòcè,díyatɔcɛ( rendre.agréable [ agréable *en verbe dynamique ] *statif mâle )
díyatɔmuso,díyatɔmuso( rendre.agréable [ agréable *en verbe dynamique ] *statif femme )játɔmuso.
diyatɔmuso,díyatɔmuso( rendre.agréable [ agréable *en verbe dynamique ] *statif femme )játɔmuso.
diyatòmuso,díyatɔmuso( rendre.agréable [ agréable *en verbe dynamique ] *statif femme )játɔmuso.
dìyé,dìyé→̌→ 35
diye,dìyé→̌→ 35
diyɛlidirini,diyɛlidirini→̌→ 1
diyèlidirini,diyɛlidirini→̌→ 1
díyɛn,díyɛn→̌díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
diyɛn,díyɛn→̌díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
diyèn,díyɛn→̌díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
díyɛnden,díyɛnden( monde enfant )díɲɛden.díyɛnden.
diyɛnden,díyɛnden( monde enfant )díɲɛden.díyɛnden.
diyènden,díyɛnden( monde enfant )díɲɛden.díyɛnden.
díyɛndenya,díyɛndenya( bon.vivant [ monde enfant ] *abstractif )díɲɛdenya.díyɛndenya.
diyɛndenya,díyɛndenya( bon.vivant [ monde enfant ] *abstractif )díɲɛdenya.díyɛndenya.
diyèndenya,díyɛndenya( bon.vivant [ monde enfant ] *abstractif )díɲɛdenya.díyɛndenya.
díyɛnlaban,díyɛnlaban( monde fin [ *causatif terminer ] )díɲɛlaban.díyɛnlaban.
diyɛnlaban,díyɛnlaban( monde fin [ *causatif terminer ] )díɲɛlaban.díyɛnlaban.
diyènlaban,díyɛnlaban( monde fin [ *causatif terminer ] )díɲɛlaban.díyɛnlaban.
díyɛnnabɔ,díyɛnnabɔ( monde à sortir )díɲɛnabɔ.díyɛnnabɔ;jíɲɛnabɔ.
diyɛnnabɔ,díyɛnnabɔ( monde à sortir )díɲɛnabɔ.díyɛnnabɔ;jíɲɛnabɔ.
diyènnabò,díyɛnnabɔ( monde à sortir )díɲɛnabɔ.díyɛnnabɔ;jíɲɛnabɔ.
díyɛnnatigɛ,díyɛnnatigɛ( monde faire.passer [ *causatif couper ] )díɲɛnatigɛ.díɲɛlatigɛ;díyɛnnatigɛ;jyɛ́nlatigɛ.
diyɛnnatigɛ,díyɛnnatigɛ( monde faire.passer [ *causatif couper ] )díɲɛnatigɛ.díɲɛlatigɛ;díyɛnnatigɛ;jyɛ́nlatigɛ.
diyènnatigè,díyɛnnatigɛ( monde faire.passer [ *causatif couper ] )díɲɛnatigɛ.díɲɛlatigɛ;díyɛnnatigɛ;jyɛ́nlatigɛ.
díyɛnsosigi,díyɛnsosigi( monde [ monde maison ] position.assise )díɲɛsosigi.díyɛnsosigi.
diyɛnsosigi,díyɛnsosigi( monde [ monde maison ] position.assise )díɲɛsosigi.díyɛnsosigi.
diyènsosigi,díyɛnsosigi( monde [ monde maison ] position.assise )díɲɛsosigi.díyɛnsosigi.
díyɛnwuli,díyɛnwuli( monde se.lever )díɲɛwuli.díyɛnwuli.
diyɛnwuli,díyɛnwuli( monde se.lever )díɲɛwuli.díyɛnwuli.
diyènwuli,díyɛnwuli( monde se.lever )díɲɛwuli.díyɛnwuli.
diyetilikaribamazini,diyetilikaribamazini→̌→ 11
diyosɛzi,diyosɛzi→̌
diyosèzi,diyosɛzi→̌
dlá,dlá→̌→ 1→n : 220vt.dílan.díla;bíla;dlá;dlán.
dla,dlá→̌→ 1→n : 220vt.dílan.díla;bíla;dlá;dlán.
dlà,dlà→̌dàla.bìla;dlà.
dlán,dlán→̌→n : 220vt.dílan.díla;bíla;dlá;dlán.
dlan,dlán→̌→n : 220vt.dílan.díla;bíla;dlá;dlán.
dlánnabana,dlánnabana( lit [ poser *instrumental ] à maladie )dílannabana.dálannabana;dlánnabana.
dlannabana,dlánnabana( lit [ poser *instrumental ] à maladie )dílannabana.dálannabana;dlánnabana.
dlàsaɲɔ,dlàsaɲɔ( lac petit.mil [ mil ] )dàlasaɲɔ.dlàsaɲɔ.
dlasaɲɔ,dlàsaɲɔ( lac petit.mil [ mil ] )dàlasaɲɔ.dlàsaɲɔ.
dlasanyò,dlàsaɲɔ( lac petit.mil [ mil ] )dàlasaɲɔ.dlàsaɲɔ.
dlɛ́dlɛdlɛ,dlɛ́dlɛdlɛ→̌dɛ́lɛdɛlɛdɛlɛ.dlɛ́dlɛdlɛ.
dlɛdlɛdlɛ,dlɛ́dlɛdlɛ→̌dɛ́lɛdɛlɛdɛlɛ.dlɛ́dlɛdlɛ.
dlèdlèdlè,dlɛ́dlɛdlɛ→̌dɛ́lɛdɛlɛdɛlɛ.dlɛ́dlɛdlɛ.
dlí,dlí→̌díli.gíli;bíli;dlí;líli.
dli,dlí→̌díli.gíli;bíli;dlí;líli.
dlɔ̀,dlɔ̀→̌dɔ̀lɔ.dùlɔ;dlɔ̀.
dlɔ,dlɔ̀→̌dɔ̀lɔ.dùlɔ;dlɔ̀.
dlò,dlɔ̀→̌dɔ̀lɔ.dùlɔ;dlɔ̀.
dlɔ̀bo,dlɔ̀bo( bière.de.mil excrément )dɔ̀lɔbo.dùlɔbo;dlɔ̀bo.
dlɔbo,dlɔ̀bo( bière.de.mil excrément )dɔ̀lɔbo.dùlɔbo;dlɔ̀bo.
dlòbo,dlɔ̀bo( bière.de.mil excrément )dɔ̀lɔbo.dùlɔbo;dlɔ̀bo.
dlɔ̀donna,dlɔ̀donna( bière.de.mil entrer *agent permanent )dɔ̀lɔdonna.dùlɔdonna;dlɔ̀donna.
dlɔdonna,dlɔ̀donna( bière.de.mil entrer *agent permanent )dɔ̀lɔdonna.dùlɔdonna;dlɔ̀donna.
dlòdonna,dlɔ̀donna( bière.de.mil entrer *agent permanent )dɔ̀lɔdonna.dùlɔdonna;dlɔ̀donna.
dlɔ̀gɛrɛn,dlɔ̀gɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dlɔgɛrɛn,dlɔ̀gɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dlògèrèn,dlɔ̀gɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dlɔ̀gwɛrɛn,dlɔ̀gwɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dlɔgwɛrɛn,dlɔ̀gwɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dlògwèrèn,dlɔ̀gwɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dlɔ̀juru,dlɔ̀juru( bière.de.mil corde )dɔ̀lɔjuru.dùlɔjuru;dlɔ̀juru.
dlɔjuru,dlɔ̀juru( bière.de.mil corde )dɔ̀lɔjuru.dùlɔjuru;dlɔ̀juru.
dlòjuru,dlɔ̀juru( bière.de.mil corde )dɔ̀lɔjuru.dùlɔjuru;dlɔ̀juru.
dlɔ̀kasila,dlɔ̀kasila( bière.de.mil pleurer *agent permanent )dɔ̀lɔkasila.dùlɔkasila;dlɔ̀kasila.
dlɔkasila,dlɔ̀kasila( bière.de.mil pleurer *agent permanent )dɔ̀lɔkasila.dùlɔkasila;dlɔ̀kasila.
dlòkasila,dlɔ̀kasila( bière.de.mil pleurer *agent permanent )dɔ̀lɔkasila.dùlɔkasila;dlɔ̀kasila.
dlòki,dlòki→̌→ 4dùloki.dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
dloki,dlòki→̌→ 4dùloki.dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
dlɔ̀ki,dlɔ̀ki→̌dùloki.dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
dlɔki,dlɔ̀ki→̌dùloki.dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
dlòki,dlɔ̀ki→̌dùloki.dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
dlòkoto,dlòkoto→̌dùlokoto.dlòkoto.
dlokoto,dlòkoto→̌dùlokoto.dlòkoto.
dlɔ̀min,dlɔ̀min( bière.de.mil boire )dɔ̀lɔmin.dù̀lɔmin.
dlɔmin,dlɔ̀min( bière.de.mil boire )dɔ̀lɔmin.dù̀lɔmin.
dlòmin,dlɔ̀min( bière.de.mil boire )dɔ̀lɔmin.dù̀lɔmin.
dlɔ̀minna,dlɔ̀minna( bière.de.mil boire *agent permanent )dɔ̀lɔminna.dùlɔminna;dlɔ̀minna.
dlɔminna,dlɔ̀minna( bière.de.mil boire *agent permanent )dɔ̀lɔminna.dùlɔminna;dlɔ̀minna.
dlòminna,dlɔ̀minna( bière.de.mil boire *agent permanent )dɔ̀lɔminna.dùlɔminna;dlɔ̀minna.
dlɔ̀mɔɔni,dlɔ̀mɔɔni( bière.de.mil ramollir )dɔ̀lɔmɔɔni.dùlɔmɔɔni;dlɔ̀mɔɔni.
dlɔmɔɔni,dlɔ̀mɔɔni( bière.de.mil ramollir )dɔ̀lɔmɔɔni.dùlɔmɔɔni;dlɔ̀mɔɔni.
dlòmòoni,dlɔ̀mɔɔni( bière.de.mil ramollir )dɔ̀lɔmɔɔni.dùlɔmɔɔni;dlɔ̀mɔɔni.
dlón,dlón→̌→ 4dúlon.dlón;búlon;gúlon.
dlon,dlón→̌→ 4dúlon.dlón;búlon;gúlon.
dlɔ̀tɔ,dlɔ̀tɔ( bière.de.mil *statif )dɔ̀lɔtɔ.dùlɔtɔ;dlɔ̀tɔ.
dlɔtɔ,dlɔ̀tɔ( bière.de.mil *statif )dɔ̀lɔtɔ.dùlɔtɔ;dlɔ̀tɔ.
dlòtò,dlɔ̀tɔ( bière.de.mil *statif )dɔ̀lɔtɔ.dùlɔtɔ;dlɔ̀tɔ.
dlɔ̀tɔya,dlɔ̀tɔya( ivre [ bière.de.mil *statif ] *abstractif )dɔ̀lɔtɔya.dùlɔtɔya;dlɔ̀tɔya.
dlɔtɔya,dlɔ̀tɔya( ivre [ bière.de.mil *statif ] *abstractif )dɔ̀lɔtɔya.dùlɔtɔya;dlɔ̀tɔya.
dlòtòya,dlɔ̀tɔya( ivre [ bière.de.mil *statif ] *abstractif )dɔ̀lɔtɔya.dùlɔtɔya;dlɔ̀tɔya.
dm,dm→̌→ 18
dnán,dnán→̌dúnan.dnán.
dnan,dnán→̌dúnan.dnán.
dnánjigin,dnánjigin( étranger descendre )vt.dúnanjigin.dnánjigin.
dnanjigin,dnánjigin( étranger descendre )vt.dúnanjigin.dnánjigin.
dnánjiginso,dnánjiginso( accueillir [ étranger descendre ] maison )dúnanjiginso.dnánjiginso.
dnanjiginso,dnánjiginso( accueillir [ étranger descendre ] maison )dúnanjiginso.dnánjiginso.
dnánkɛ,dnánkɛ( étranger mâle )dúnankɛ.dnánkɛ.
dnankɛ,dnánkɛ( étranger mâle )dúnankɛ.dnánkɛ.
dnankè,dnánkɛ( étranger mâle )dúnankɛ.dnánkɛ.
dnánmuso,dnánmuso( étranger femme )dúnanmuso.dnánmuso.
dnanmuso,dnánmuso( étranger femme )dúnanmuso.dnánmuso.
dnánnama,dnánnama( étranger *en tant que )dúnannama.dnánnama.
dnannama,dnánnama( étranger *en tant que )dúnannama.dnánnama.
dnánya,dnánya( étranger *abstractif )dúnanya.dnánya.
dnanya,dnánya( étranger *abstractif )dúnanya.dnánya.
dó,dó→̌→ 7
do,dó→̌→ 7
dò,dò→̌→ 5883dòn.dò.
dɔ́,Dɔ́→̌
dɔ,Dɔ́→̌
dò,Dɔ́→̌
dɔ̀,dɔ̀→̌→ 2→n : 161jɔ̀.dɔ̀.
doboda,Doboda→̌
dɔ́bɔlan,dɔ́bɔlan( certain sortir *instrumental )
dɔbɔlan,dɔ́bɔlan( certain sortir *instrumental )
dòbòlan,dɔ́bɔlan( certain sortir *instrumental )
dɔ́bɔli,dɔ́bɔli( certain sortir *nom d'action )
dɔbɔli,dɔ́bɔli( certain sortir *nom d'action )
dòbòli,dɔ́bɔli( certain sortir *nom d'action )
dódò,dódò→̌→ 1
dodo,dódò→̌→ 1
dòdo,dòdo→̌
dɔ̀dɔ,dɔ̀dɔ→̌→ 2vt.jɔ̀jɔ.
dɔdɔ,dɔ̀dɔ→̌→ 2vt.jɔ̀jɔ.
dòdò,dɔ̀dɔ→̌→ 2vt.jɔ̀jɔ.
dɔ̀dɔli,dɔ̀dɔli( suivre *nom d'action )jɔ̀jɔli.
dɔdɔli,dɔ̀dɔli( suivre *nom d'action )jɔ̀jɔli.
dòdòli,dɔ̀dɔli( suivre *nom d'action )jɔ̀jɔli.
dɔ̀dɔlima,dɔ̀dɔlima( espionnage [ suivre *nom d'action ] *action orientée )vt.jɔ̀jɔlima.
dɔdɔlima,dɔ̀dɔlima( espionnage [ suivre *nom d'action ] *action orientée )vt.jɔ̀jɔlima.
dòdòlima,dɔ̀dɔlima( espionnage [ suivre *nom d'action ] *action orientée )vt.jɔ̀jɔlima.
dɔ́farankan,dɔ́farankan( certain ajouter *je sur )
dɔfarankan,dɔ́farankan( certain ajouter *je sur )
dòfarankan,dɔ́farankan( certain ajouter *je sur )
dofɛn,Dofɛn→̌
dofèn,Dofɛn→̌
dógi,dógi→̌→ 5dógin.
dogi,dógi→̌→ 5dógin.
dógidogi,dógidogi( tanner tanner )vt.
dogidogi,dógidogi( tanner tanner )vt.
dógin,dógin→̌dógi.dógin.
dogin,dógin→̌dógi.dógin.
dɔgitora,dɔgitora→̌→ 1
dògitora,dɔgitora→̌→ 1
dogo,Dogo→̌
dògo,dògo→̌→ 31
dogo,dògo→̌→ 31
dɔ́gɔ,dɔ́gɔ→̌→ 120lɔ́gɔ;dwá;jwá.
dɔgɔ,dɔ́gɔ→̌→ 120lɔ́gɔ;dwá;jwá.
dògò,dɔ́gɔ→̌→ 120lɔ́gɔ;dwá;jwá.
dògobaa,dògobaa( cacher *agent occasionnel )
dogobaa,dògobaa( cacher *agent occasionnel )
dogobala,Dogobala→̌
dɔ́gɔda,dɔ́gɔda( marché poser )
dɔgɔda,dɔ́gɔda( marché poser )
dògòda,dɔ́gɔda( marché poser )
dɔ́gɔden,dɔ́gɔden( marché enfant )dwáden;jwáden.
dɔgɔden,dɔ́gɔden( marché enfant )dwáden;jwáden.
dògòden,dɔ́gɔden( marché enfant )dwáden;jwáden.
dógodogo,dógodogo→̌→ 9
dogodogo,dógodogo→̌→ 9
dògodògo,dògodògo→̌
dógodogoɲɛ,dógodogoɲɛ( coin oeil )
dogodogoɲɛ,dógodogoɲɛ( coin oeil )
dogodogonyè,dógodogoɲɛ( coin oeil )
dógodogonin,dógodogonin( coin *diminutif )
dogodogonin,dógodogonin( coin *diminutif )
dɔ́gɔdɔgɔnin,dɔ́gɔdɔgɔnin( étroit étroit *diminutif )dɔ́ndɔɔnin.
dɔgɔdɔgɔnin,dɔ́gɔdɔgɔnin( étroit étroit *diminutif )dɔ́ndɔɔnin.
dògòdògònin,dɔ́gɔdɔgɔnin( étroit étroit *diminutif )dɔ́ndɔɔnin.
dɔ́gɔdɔgɔninfeerela,dɔ́gɔdɔgɔninfeerela( doucement [ étroit étroit *diminutif ] vendre *agent permanent )
dɔgɔdɔgɔninfeerela,dɔ́gɔdɔgɔninfeerela( doucement [ étroit étroit *diminutif ] vendre *agent permanent )
dògòdògòninfeerela,dɔ́gɔdɔgɔninfeerela( doucement [ étroit étroit *diminutif ] vendre *agent permanent )
dògodogoninkuma,dògodogoninkuma( cacher *diminutif parole )
dogodogoninkuma,dògodogoninkuma( cacher *diminutif parole )
dɔ́gɔdugu,dɔ́gɔdugu( marché terre )
dɔgɔdugu,dɔ́gɔdugu( marché terre )
dògòdugu,dɔ́gɔdugu( marché terre )
dogofiri,Dogofiri→̌
dɔgɔfiri,Dɔgɔfiri→̌→n.prop : 1
dògòfiri,Dɔgɔfiri→̌→n.prop : 1
dɔ́gɔfurancɛ,dɔ́gɔfurancɛ( marché distance [ distance milieu ] )dwáfurancɛ.
dɔgɔfurancɛ,dɔ́gɔfurancɛ( marché distance [ distance milieu ] )dwáfurancɛ.
dògòfurancè,dɔ́gɔfurancɛ( marché distance [ distance milieu ] )dwáfurancɛ.
dɔ́gɔjɔla,dɔ́gɔjɔla( marché dresser *agent permanent )
dɔgɔjɔla,dɔ́gɔjɔla( marché dresser *agent permanent )
dògòjòla,dɔ́gɔjɔla( marché dresser *agent permanent )
dògokatɛmɛna,dògokatɛmɛna( cacher *infinitif passer *agent permanent )
dogokatɛmɛna,dògokatɛmɛna( cacher *infinitif passer *agent permanent )
dogokatèmèna,dògokatɛmɛna( cacher *infinitif passer *agent permanent )
dɔ́gɔkɛ,dɔ́gɔkɛ( cadet mâle )dwákɛ;jwákɛ.
dɔgɔkɛ,dɔ́gɔkɛ( cadet mâle )dwákɛ;jwákɛ.
dògòkè,dɔ́gɔkɛ( cadet mâle )dwákɛ;jwákɛ.
dɔ́gɔkun,dɔ́gɔkun( marché tête )dwákun;jwákun.
dɔgɔkun,dɔ́gɔkun( marché tête )dwákun;jwákun.
dògòkun,dɔ́gɔkun( marché tête )dwákun;jwákun.
dɔ́gɔman,dɔ́gɔman( étroit *adjectivateur )
dɔgɔman,dɔ́gɔman( étroit *adjectivateur )
dògòman,dɔ́gɔman( étroit *adjectivateur )
dɔ̀gɔman,dɔ̀gɔman→̌→ 3
dɔ́gɔmaya,dɔ́gɔmaya( étroit *action orientée *abstractif )
dɔgɔmaya,dɔ́gɔmaya( étroit *action orientée *abstractif )
dògòmaya,dɔ́gɔmaya( étroit *action orientée *abstractif )
dɔ́gɔmɔ,dɔ́gɔmɔ( marché croissance )
dɔgɔmɔ,dɔ́gɔmɔ( marché croissance )
dògòmò,dɔ́gɔmɔ( marché croissance )
dɔ́gɔmuso,dɔ́gɔmuso( cadet femme )dwámuso;jwámuso.
dɔgɔmuso,dɔ́gɔmuso( cadet femme )dwámuso;jwámuso.
dògòmuso,dɔ́gɔmuso( cadet femme )dwámuso;jwámuso.
dɔ́gɔn,dɔ́gɔn→̌dɔ́gɔ.dɔ́gɔn;dwá;jwá.
dɔgɔn,dɔ́gɔn→̌dɔ́gɔ.dɔ́gɔn;dwá;jwá.
dògòn,dɔ́gɔn→̌dɔ́gɔ.dɔ́gɔn;dwá;jwá.
dɔ̀gɔn,dɔ̀gɔn→̌→ 2dùngɔ.dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dɔ̀gɔnɛ,dɔ̀gɔnɛ→̌
dɔgɔnɛ,dɔ̀gɔnɛ→̌
dògònè,dɔ̀gɔnɛ→̌
dogonin,Dogonin→̌
dɔ́gɔnin,dɔ́gɔnin( cadet *diminutif )dwánin;jwánin.
dɔgɔnin,dɔ́gɔnin( cadet *diminutif )dwánin;jwánin.
dògònin,dɔ́gɔnin( cadet *diminutif )dwánin;jwánin.
dɔ́gɔɲinina,dɔ́gɔɲinina( fagot chercher *agent permanent )dwáɲinina;jwáɲinina.
dɔgɔɲinina,dɔ́gɔɲinina( fagot chercher *agent permanent )dwáɲinina;jwáɲinina.
dògònyinina,dɔ́gɔɲinina( fagot chercher *agent permanent )dwáɲinina;jwáɲinina.
dògonna,dògonna( cacher *je à )
dogonna,dògonna( cacher *je à )
dɔ̀gɔnɔ,dɔ̀gɔnɔ→̌→ 20dɔ̀nkɔnɔ.
dɔgɔnɔ,dɔ̀gɔnɔ→̌→ 20dɔ̀nkɔnɔ.
dògònò,dɔ̀gɔnɔ→̌→ 20dɔ̀nkɔnɔ.
dògora,dògora→̌dùgura.dògora.
dogora,dògora→̌dùgura.dògora.
dɔ́gɔsiri,dɔ́gɔsiri( fagot lier )dwásiri;jwásiri.
dɔgɔsiri,dɔ́gɔsiri( fagot lier )dwásiri;jwásiri.
dògòsiri,dɔ́gɔsiri( fagot lier )dwásiri;jwásiri.
dɔgɔsɔ,dɔgɔsɔ→̌→ 1
dògòsò,dɔgɔsɔ→̌→ 1
dɔ́gɔton,dɔ́gɔton( fagot tas )
dɔgɔton,dɔ́gɔton( fagot tas )
dògòton,dɔ́gɔton( fagot tas )
dɔ̀gɔtɔrɔ,dɔ̀gɔtɔrɔ→̌→ 384dɔ̀kɔtɔrɔ.Fr. docteur
dɔgɔtɔrɔ,dɔ̀gɔtɔrɔ→̌→ 384dɔ̀kɔtɔrɔ.Fr. docteur
dògòtòrò,dɔ̀gɔtɔrɔ→̌→ 384dɔ̀kɔtɔrɔ.Fr. docteur
dɔ̀gɔtɔrɔfura,dɔ̀gɔtɔrɔfura( docteur feuille )dɔ̀kɔtɔrɔfura.
dɔgɔtɔrɔfura,dɔ̀gɔtɔrɔfura( docteur feuille )dɔ̀kɔtɔrɔfura.
dògòtòròfura,dɔ̀gɔtɔrɔfura( docteur feuille )dɔ̀kɔtɔrɔfura.
dɔ̀gɔtɔrɔmobili,dɔ̀gɔtɔrɔmobili( docteur automobile )dɔ̀kɔtɔrɔmobili.
dɔgɔtɔrɔmobili,dɔ̀gɔtɔrɔmobili( docteur automobile )dɔ̀kɔtɔrɔmobili.
dògòtòròmobili,dɔ̀gɔtɔrɔmobili( docteur automobile )dɔ̀kɔtɔrɔmobili.
dɔ̀gɔtɔrɔmuso,dɔ̀gɔtɔrɔmuso( docteur féminin )dɔ̀kɔtɔrɔmuso.
dɔgɔtɔrɔmuso,dɔ̀gɔtɔrɔmuso( docteur féminin )dɔ̀kɔtɔrɔmuso.
dògòtòròmuso,dɔ̀gɔtɔrɔmuso( docteur féminin )dɔ̀kɔtɔrɔmuso.
dɔ̀gɔtɔrɔso,dɔ̀gɔtɔrɔso( docteur maison )dɔ̀kɔtɔrɔso.
dɔgɔtɔrɔso,dɔ̀gɔtɔrɔso( docteur maison )dɔ̀kɔtɔrɔso.
dògòtòròso,dɔ̀gɔtɔrɔso( docteur maison )dɔ̀kɔtɔrɔso.
dɔ̀gɔtɔrɔya,dɔ̀gɔtɔrɔya( docteur *abstractif )dɔ̀kɔtɔrɔya.
dɔgɔtɔrɔya,dɔ̀gɔtɔrɔya( docteur *abstractif )dɔ̀kɔtɔrɔya.
dògòtòròya,dɔ̀gɔtɔrɔya( docteur *abstractif )dɔ̀kɔtɔrɔya.
dògotu,dògotu( cacher touffe )
dogotu,dògotu( cacher touffe )
dɔ́gɔya,dɔ́gɔya( étroit *en verbe dynamique )dwáya;jwáya.
dɔgɔya,dɔ́gɔya( étroit *en verbe dynamique )dwáya;jwáya.
dògòya,dɔ́gɔya( étroit *en verbe dynamique )dwáya;jwáya.
dɔ́gɔyalenba,dɔ́gɔyalenba( amoindrir [ étroit *en verbe dynamique ] *participe résultatif *augmentatif )
dɔgɔyalenba,dɔ́gɔyalenba( amoindrir [ étroit *en verbe dynamique ] *participe résultatif *augmentatif )
dògòyalenba,dɔ́gɔyalenba( amoindrir [ étroit *en verbe dynamique ] *participe résultatif *augmentatif )
dɔ́gɔyama,dɔ́gɔyama( petitesse [ étroit *en verbe dynamique ] *comme de )dwáyama;jwáyama.
dɔgɔyama,dɔ́gɔyama( petitesse [ étroit *en verbe dynamique ] *comme de )dwáyama;jwáyama.
dògòyama,dɔ́gɔyama( petitesse [ étroit *en verbe dynamique ] *comme de )dwáyama;jwáyama.
dògoyɔrɔ,dògoyɔrɔ( cacher lieu )
dogoyɔrɔ,dògoyɔrɔ( cacher lieu )
dogoyòrò,dògoyɔrɔ( cacher lieu )
dògoyɔrɔlakaba,dògoyɔrɔlakaba( parties.génitales [ cacher lieu ] à teigne )
dogoyɔrɔlakaba,dògoyɔrɔlakaba( parties.génitales [ cacher lieu ] à teigne )
dogoyòròlakaba,dògoyɔrɔlakaba( parties.génitales [ cacher lieu ] à teigne )
dògoyɔrɔlakuru,dògoyɔrɔlakuru( cacher lieu à boule )
dogoyɔrɔlakuru,dògoyɔrɔlakuru( cacher lieu à boule )
dogoyòròlakuru,dògoyɔrɔlakuru( cacher lieu à boule )
dɔ̀jan,dɔ̀jan( station.debout long )jɔ̀jan.dɔ̀jan.
dɔjan,dɔ̀jan( station.debout long )jɔ̀jan.dɔ̀jan.
dòjan,dɔ̀jan( station.debout long )jɔ̀jan.dɔ̀jan.
dɔkala,Dɔkala→̌
dòkala,Dɔkala→̌
dɔ́kɛbali,dɔ́kɛbali( certain faire PTCP.NEG )
dɔkɛbali,dɔ́kɛbali( certain faire PTCP.NEG )
dòkèbali,dɔ́kɛbali( certain faire PTCP.NEG )
dɔ́kɛla,dɔ́kɛla( certain faire *agent permanent )
dɔkɛla,dɔ́kɛla( certain faire *agent permanent )
dòkèla,dɔ́kɛla( certain faire *agent permanent )
dɔkisisikilini,dɔkisisikilini→̌→ 21
dòkisisikilini,dɔkisisikilini→̌→ 21
dɔkitora,dɔkitora→̌
dòkitora,dɔkitora→̌
dɔ̀kɔtɔrɔ,dɔ̀kɔtɔrɔ→̌→ 32dɔ̀gɔtɔrɔ.dɔ̀kɔtɔrɔ.Fr. docteur
dɔkɔtɔrɔ,dɔ̀kɔtɔrɔ→̌→ 32dɔ̀gɔtɔrɔ.dɔ̀kɔtɔrɔ.Fr. docteur
dòkòtòrò,dɔ̀kɔtɔrɔ→̌→ 32dɔ̀gɔtɔrɔ.dɔ̀kɔtɔrɔ.Fr. docteur
dɔ̀kɔtɔrɔfura,dɔ̀kɔtɔrɔfura( docteur feuille )dɔ̀gɔtɔrɔfura.dɔ̀kɔtɔrɔfura.
dɔkɔtɔrɔfura,dɔ̀kɔtɔrɔfura( docteur feuille )dɔ̀gɔtɔrɔfura.dɔ̀kɔtɔrɔfura.
dòkòtòròfura,dɔ̀kɔtɔrɔfura( docteur feuille )dɔ̀gɔtɔrɔfura.dɔ̀kɔtɔrɔfura.
dɔ̀kɔtɔrɔmobili,dɔ̀kɔtɔrɔmobili( docteur automobile )dɔ̀gɔtɔrɔmobili.dɔ̀kɔtɔrɔmobili.
dɔkɔtɔrɔmobili,dɔ̀kɔtɔrɔmobili( docteur automobile )dɔ̀gɔtɔrɔmobili.dɔ̀kɔtɔrɔmobili.
dòkòtòròmobili,dɔ̀kɔtɔrɔmobili( docteur automobile )dɔ̀gɔtɔrɔmobili.dɔ̀kɔtɔrɔmobili.
dɔ̀kɔtɔrɔmuso,dɔ̀kɔtɔrɔmuso( docteur féminin )dɔ̀gɔtɔrɔmuso.dɔ̀kɔtɔrɔmuso.
dɔkɔtɔrɔmuso,dɔ̀kɔtɔrɔmuso( docteur féminin )dɔ̀gɔtɔrɔmuso.dɔ̀kɔtɔrɔmuso.
dòkòtòròmuso,dɔ̀kɔtɔrɔmuso( docteur féminin )dɔ̀gɔtɔrɔmuso.dɔ̀kɔtɔrɔmuso.
dɔ̀kɔtɔrɔso,dɔ̀kɔtɔrɔso( docteur maison )dɔ̀gɔtɔrɔso.dɔ̀kɔtɔrɔso.
dɔkɔtɔrɔso,dɔ̀kɔtɔrɔso( docteur maison )dɔ̀gɔtɔrɔso.dɔ̀kɔtɔrɔso.
dòkòtòròso,dɔ̀kɔtɔrɔso( docteur maison )dɔ̀gɔtɔrɔso.dɔ̀kɔtɔrɔso.
dɔ̀kɔtɔrɔya,dɔ̀kɔtɔrɔya( docteur *abstractif )dɔ̀gɔtɔrɔya.dɔ̀kɔtɔrɔya.
dɔkɔtɔrɔya,dɔ̀kɔtɔrɔya( docteur *abstractif )dɔ̀gɔtɔrɔya.dɔ̀kɔtɔrɔya.
dòkòtòròya,dɔ̀kɔtɔrɔya( docteur *abstractif )dɔ̀gɔtɔrɔya.dɔ̀kɔtɔrɔya.
dóla,dóla→̌→ 2ndóla;dɔ́lɛ.
dola,dóla→̌→ 2ndóla;dɔ́lɛ.
dòlaji,dòlaji( eau )lòlaji.dòlaji.
dolaji,dòlaji( eau )lòlaji.dòlaji.
dɔ́lakelen,dɔ́lakelen( certain à un )
dɔlakelen,dɔ́lakelen( certain à un )
dòlakelen,dɔ́lakelen( certain à un )
dolari,dolari→̌→ 9dolariwari;dɔlari;dɔlariwari.
dɔlari,dɔlari→̌dolari.dolariwari;dɔlari;dɔlariwari.
dòlari,dɔlari→̌dolari.dolariwari;dɔlari;dɔlariwari.
dolariwari,dolariwari( dollar argent )dolari.dɔlari;dɔlariwari.
dɔlariwari,dɔlariwari→̌dolari.dolariwari;dɔlari;dɔlariwari.
dòlariwari,dɔlariwari→̌dolari.dolariwari;dɔlari;dɔlariwari.
dɔ́lɛ,dɔ́lɛ→̌→ 1dóla.ndóla;dɔ́lɛ.
dɔlɛ,dɔ́lɛ→̌→ 1dóla.ndóla;dɔ́lɛ.
dòlè,dɔ́lɛ→̌→ 1dóla.ndóla;dɔ́lɛ.
dólen,dólen→̌→ 3dóolen.ndóolen;ndólen;dɔ́len.
dolen,dólen→̌→ 3dóolen.ndóolen;ndólen;dɔ́len.
dɔ́len,dɔ́len→̌dóolen.dólen;ndóolen;ndólen;dɔ́len.
dɔlen,dɔ́len→̌dóolen.dólen;ndóolen;ndólen;dɔ́len.
dòlen,dɔ́len→̌dóolen.dólen;ndóolen;ndólen;dɔ́len.
dɔ̀len,dɔ̀len→̌jɔ̀len.lɔ̀len.
dólendala,dólendala( hameçon poser *agent permanent )
dolendala,dólendala( hameçon poser *agent permanent )
dólenjuru,dólenjuru( hameçon corde )
dolenjuru,dólenjuru( hameçon corde )
dólenkisɛ,dólenkisɛ( hameçon grain )
dolenkisɛ,dólenkisɛ( hameçon grain )
dolenkisè,dólenkisɛ( hameçon grain )
dólentulo,dólentulo( hameçon oreille )
dolentulo,dólentulo( hameçon oreille )
dóli,dóli→̌
doli,dóli→̌
dolo,Dolo→̌
dòlo,dòlo→̌→ 28dòolo.
dolo,dòlo→̌→ 28dòolo.
dɔ̀lɔ,dɔ̀lɔ→̌→ 309dùlɔ;dlɔ̀.
dɔlɔ,dɔ̀lɔ→̌→ 309dùlɔ;dlɔ̀.
dòlò,dɔ̀lɔ→̌→ 309dùlɔ;dlɔ̀.
dɔ̀lɔbo,dɔ̀lɔbo( bière.de.mil excrément )dùlɔbo;dlɔ̀bo.
dɔlɔbo,dɔ̀lɔbo( bière.de.mil excrément )dùlɔbo;dlɔ̀bo.
dòlòbo,dɔ̀lɔbo( bière.de.mil excrément )dùlɔbo;dlɔ̀bo.
dɔ̀lɔdonna,dɔ̀lɔdonna( bière.de.mil entrer *agent permanent )dùlɔdonna;dlɔ̀donna.
dɔlɔdonna,dɔ̀lɔdonna( bière.de.mil entrer *agent permanent )dùlɔdonna;dlɔ̀donna.
dòlòdonna,dɔ̀lɔdonna( bière.de.mil entrer *agent permanent )dùlɔdonna;dlɔ̀donna.
dɔ̀lɔgɛrɛn,dɔ̀lɔgɛrɛn( bière.de.mil évaporer )dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dɔlɔgɛrɛn,dɔ̀lɔgɛrɛn( bière.de.mil évaporer )dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dòlògèrèn,dɔ̀lɔgɛrɛn( bière.de.mil évaporer )dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dɔ̀lɔgwɛrɛn,dɔ̀lɔgwɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dɔlɔgwɛrɛn,dɔ̀lɔgwɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dòlògwèrèn,dɔ̀lɔgwɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dɔ̀lɔjuru,dɔ̀lɔjuru( bière.de.mil corde )dùlɔjuru;dlɔ̀juru.
dɔlɔjuru,dɔ̀lɔjuru( bière.de.mil corde )dùlɔjuru;dlɔ̀juru.
dòlòjuru,dɔ̀lɔjuru( bière.de.mil corde )dùlɔjuru;dlɔ̀juru.
dɔ̀lɔkasila,dɔ̀lɔkasila( bière.de.mil pleurer *agent permanent )dùlɔkasila;dlɔ̀kasila.
dɔlɔkasila,dɔ̀lɔkasila( bière.de.mil pleurer *agent permanent )dùlɔkasila;dlɔ̀kasila.
dòlòkasila,dɔ̀lɔkasila( bière.de.mil pleurer *agent permanent )dùlɔkasila;dlɔ̀kasila.
dɔ̀lɔki,dɔ̀lɔki→̌→ 11dùloki.dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
dɔlɔki,dɔ̀lɔki→̌→ 11dùloki.dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
dòlòki,dɔ̀lɔki→̌→ 11dùloki.dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
dòlokoto,dòlokoto→̌dùlokoto.dlòkoto;bòlokoto.
dolokoto,dòlokoto→̌dùlokoto.dlòkoto;bòlokoto.
dɔ̀lɔmin,dɔ̀lɔmin( bière.de.mil boire )dù̀lɔmin;dlɔ̀min.
dɔlɔmin,dɔ̀lɔmin( bière.de.mil boire )dù̀lɔmin;dlɔ̀min.
dòlòmin,dɔ̀lɔmin( bière.de.mil boire )dù̀lɔmin;dlɔ̀min.
dɔ̀lɔminbana,dɔ̀lɔminbana( consommation.d'alcool [ bière.de.mil boire ] maladie )
dɔlɔminbana,dɔ̀lɔminbana( consommation.d'alcool [ bière.de.mil boire ] maladie )
dòlòminbana,dɔ̀lɔminbana( consommation.d'alcool [ bière.de.mil boire ] maladie )
dɔ̀lɔminna,dɔ̀lɔminna( bière.de.mil boire *agent permanent )dùlɔminna;dlɔ̀minna.
dɔlɔminna,dɔ̀lɔminna( bière.de.mil boire *agent permanent )dùlɔminna;dlɔ̀minna.
dòlòminna,dɔ̀lɔminna( bière.de.mil boire *agent permanent )dùlɔminna;dlɔ̀minna.
dɔ̀lɔmɔɔni,dɔ̀lɔmɔɔni( bière.de.mil ramollir )dùlɔmɔɔni;dlɔ̀mɔɔni.
dɔlɔmɔɔni,dɔ̀lɔmɔɔni( bière.de.mil ramollir )dùlɔmɔɔni;dlɔ̀mɔɔni.
dòlòmòoni,dɔ̀lɔmɔɔni( bière.de.mil ramollir )dùlɔmɔɔni;dlɔ̀mɔɔni.
dólon,dólon→̌vt.
dolon,dólon→̌vt.
dóloo,dóloo→̌dóo.
doloo,dóloo→̌dóo.
dɔ̀lɔtigɛla,dɔ̀lɔtigɛla( bière.de.mil couper *agent permanent )
dɔlɔtigɛla,dɔ̀lɔtigɛla( bière.de.mil couper *agent permanent )
dòlòtigèla,dɔ̀lɔtigɛla( bière.de.mil couper *agent permanent )
dɔ̀lɔtɔ,dɔ̀lɔtɔ( bière.de.mil *statif )dùlɔtɔ;dlɔ̀tɔ.
dɔlɔtɔ,dɔ̀lɔtɔ( bière.de.mil *statif )dùlɔtɔ;dlɔ̀tɔ.
dòlòtò,dɔ̀lɔtɔ( bière.de.mil *statif )dùlɔtɔ;dlɔ̀tɔ.
dɔ̀lɔtɔya,dɔ̀lɔtɔya( ivre [ bière.de.mil *statif ] *abstractif )dùlɔtɔya;dlɔ̀tɔya.
dɔlɔtɔya,dɔ̀lɔtɔya( ivre [ bière.de.mil *statif ] *abstractif )dùlɔtɔya;dlɔ̀tɔya.
dòlòtòya,dɔ̀lɔtɔya( ivre [ bière.de.mil *statif ] *abstractif )dùlɔtɔya;dlɔ̀tɔya.
dóma,dóma→̌→ 26
doma,dóma→̌→ 26
dómaya,dómaya( devin *abstractif )
domaya,dómaya( devin *abstractif )
dɔ́mɛɛ,dɔ́mɛɛ→̌→ 2
dɔmɛɛ,dɔ́mɛɛ→̌→ 2
dòmèe,dɔ́mɛɛ→̌→ 2
domɛni,domɛni→̌
domèni,domɛni→̌
dòmidomi,dòmidomi→̌→ 1
domidomi,dòmidomi→̌→ 1
dominiki,Dominiki→̌
dón,dón→̌→ 3110
don,dón→̌→ 3110
dòn,dòn→̌→ 4508→n : 7→v-v : 4
dɔ́n,dɔ́n→̌
dɔn,dɔ́n→̌
dòn,dɔ́n→̌
dɔ̀n,dɔ̀n→̌→ 42
donali,Donali→̌
donba,Donba→̌
dónba,dónba( jour *augmentatif )
donba,dónba( jour *augmentatif )
dɔ̀nba,dɔ̀nba( danse *augmentatif )
dɔnba,dɔ̀nba( danse *augmentatif )
dònba,dɔ̀nba( danse *augmentatif )
dɔ́nbaa,dɔ́nbaa( connaître *agent occasionnel )Voir entrée principale :dɔ́nbaga.
dɔnbaa,dɔ́nbaa( connaître *agent occasionnel )Voir entrée principale :dɔ́nbaga.
dònbaa,dɔ́nbaa( connaître *agent occasionnel )Voir entrée principale :dɔ́nbaga.
dɔ́nbaga,dɔ́nbaga( connaître *agent occasionnel )dɔ́nbaa.
dɔnbaga,dɔ́nbaga( connaître *agent occasionnel )dɔ́nbaa.
dònbaga,dɔ́nbaga( connaître *agent occasionnel )dɔ́nbaa.
dɔ́nbagalafili,dɔ́nbagalafili( qui.connaît [ connaître *agent occasionnel ] tromper [ *causatif jeter ] )
dɔnbagalafili,dɔ́nbagalafili( qui.connaît [ connaître *agent occasionnel ] tromper [ *causatif jeter ] )
dònbagalafili,dɔ́nbagalafili( qui.connaît [ connaître *agent occasionnel ] tromper [ *causatif jeter ] )
dònbali,dònbali( entrer PTCP.NEG )
donbali,dònbali( entrer PTCP.NEG )
dɔ́nbaliya,dɔ́nbaliya( connaître PTCP.NEG *abstractif )
dɔnbaliya,dɔ́nbaliya( connaître PTCP.NEG *abstractif )
dònbaliya,dɔ́nbaliya( connaître PTCP.NEG *abstractif )
dɔ̀nbamakɔnɔ,dɔ̀nbamakɔnɔ( danse *augmentatif *connecteur attendre )
dɔnbamakɔnɔ,dɔ̀nbamakɔnɔ( danse *augmentatif *connecteur attendre )
dònbamakònò,dɔ̀nbamakɔnɔ( danse *augmentatif *connecteur attendre )
dɔnbila,Dɔnbila→̌
dònbila,Dɔnbila→̌
dònbolo,dònbolo( entrer bras )
donbolo,dònbolo( entrer bras )
dònda,dònda( entrer bouche )
donda,dònda( entrer bouche )
dòndala,dòndala( entrer bouche à )
dondala,dòndala( entrer bouche à )
dòndaladen,dòndaladen( profit [ entrer bouche à ] enfant )
dondaladen,dòndaladen( profit [ entrer bouche à ] enfant )
dòndalali,dòndalali( profit [ entrer bouche à ] *nom d'action )
dondalali,dòndalali( profit [ entrer bouche à ] *nom d'action )
dòndalama,dòndalama( profit [ entrer bouche à ] *comme de )
dondalama,dòndalama( profit [ entrer bouche à ] *comme de )
dòndo,dòndo→̌vt.
dondo,dòndo→̌vt.
dòndò,dòndò→̌→ 1dòndòn.dòndò.
dóndoli,dóndoli→̌
dondoli,dóndoli→̌
dòndòli,dòndòli
dòndon,dòndon→̌dònon.dòndon;dòno.
dondon,dòndon→̌dònon.dòndon;dòno.
dòndòn,dòndòn→̌→ 1dòndò.
dóndonnin,dóndonnin→̌
dondonnin,dóndonnin→̌
dɔ́ndɔɔnin,dɔ́ndɔɔnin( étroit étroit *diminutif )dɔ́gɔdɔgɔnin.dɔ́ndɔɔnin.
dɔndɔɔnin,dɔ́ndɔɔnin( étroit étroit *diminutif )dɔ́gɔdɔgɔnin.dɔ́ndɔɔnin.
dòndòonin,dɔ́ndɔɔnin( étroit étroit *diminutif )dɔ́gɔdɔgɔnin.dɔ́ndɔɔnin.
dɔ̀ndɔrɔnin,dɔ̀ndɔrɔnin→̌→ 3
dɔndɔrɔnin,dɔ̀ndɔrɔnin→̌→ 3
dòndòrònin,dɔ̀ndɔrɔnin→̌→ 3
dɔ́ndugu,dɔ́ndugu( connaître terre )
dɔndugu,dɔ́ndugu( connaître terre )
dòndugu,dɔ́ndugu( connaître terre )
dònfɛn,dònfɛn( entrer chose )
donfɛn,dònfɛn( entrer chose )
donfèn,dònfɛn( entrer chose )
dɔ̀nfɛn,dɔ̀nfɛn( danse chose )
dɔnfɛn,dɔ̀nfɛn( danse chose )
dònfèn,dɔ̀nfɛn( danse chose )
dònfini,dònfini( entrer tissu )dònfinin.
donfini,dònfini( entrer tissu )dònfinin.
dònfinin,dònfinin( entrer tissu )dònfini.dònfinin.
donfinin,dònfinin( entrer tissu )dònfini.dònfinin.
dòngari,dòngari→̌dɔ̀nkɔri.dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dongari,dòngari→̌dɔ̀nkɔri.dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dɔ̀ngari,dɔ̀ngari→̌dɔ̀nkɔri.dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dɔngari,dɔ̀ngari→̌dɔ̀nkɔri.dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dòngari,dɔ̀ngari→̌dɔ̀nkɔri.dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dóngò,dóngò( jour ce )dónkò;dónwò.
dongo,dóngò( jour ce )dónkò;dónwò.
dɔ̀ngɔ,dɔ̀ngɔ→̌→ 3dùngɔ.dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dɔngɔ,dɔ̀ngɔ→̌→ 3dùngɔ.dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dòngò,dɔ̀ngɔ→̌→ 3dùngɔ.dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dɔ̀ngɔli,dɔ̀ngɔli→̌dɔ̀ngɔri.
dɔngɔli,dɔ̀ngɔli→̌dɔ̀ngɔri.
dòngòli,dɔ̀ngɔli→̌dɔ̀ngɔri.
dɔ̀ngɔn,dɔ̀ngɔn→̌dùngɔ.dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dɔngɔn,dɔ̀ngɔn→̌dùngɔ.dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dòngòn,dɔ̀ngɔn→̌dùngɔ.dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dɔ̀ngɔna,dɔ̀ngɔna( désir *mental1 )dùngɔna.dɔ̀ngɔna.
dɔngɔna,dɔ̀ngɔna( désir *mental1 )dùngɔna.dɔ̀ngɔna.
dòngòna,dɔ̀ngɔna( désir *mental1 )dùngɔna.dɔ̀ngɔna.
dɔ̀ngɔri,dɔ̀ngɔri→̌Voir entrée principale :dɔ̀ngɔli.
dɔngɔri,dɔ̀ngɔri→̌Voir entrée principale :dɔ̀ngɔli.
dòngòri,dɔ̀ngɔri→̌Voir entrée principale :dɔ̀ngɔli.
dòni,dòni→̌→ 155
doni,dòni→̌→ 155
dònibatamobili,dònibatamobili( charge *augmentatif prendre automobile )
donibatamobili,dònibatamobili( charge *augmentatif prendre automobile )
dònifɛn,dònifɛn( charge chose )
donifɛn,dònifɛn( charge chose )
donifèn,dònifɛn( charge chose )
dònikala,dònikala→̌dùnun-kàla.dùnunkàla;dùnukàlan;dùnunkàlan.
donikala,dònikala→̌dùnun-kàla.dùnunkàla;dùnukàlan;dùnunkàlan.
dònita,dònita( charge prendre )
donita,dònita( charge prendre )
dònitabagan,dònitabagan( transport [ charge prendre ] bête )
donitabagan,dònitabagan( transport [ charge prendre ] bête )
dònitala,dònitala( charge prendre *agent permanent )
donitala,dònitala( charge prendre *agent permanent )
dònitalan,dònitalan( charge prendre *instrumental )
donitalan,dònitalan( charge prendre *instrumental )
dónjan,dónjan( jour long )
donjan,dónjan( jour long )
dónjatelan,dónjatelan( jour compter *instrumental )dónjatilan.
donjatelan,dónjatelan( jour compter *instrumental )dónjatilan.
dónjatilan,dónjatilan( jour compter *instrumental )dónjatelan.dónjatilan.
donjatilan,dónjatilan( jour compter *instrumental )dónjatelan.dónjatilan.
dɔ̀nka,dɔ̀nka→̌→ 2dɔ̀nkan.
dɔnka,dɔ̀nka→̌→ 2dɔ̀nkan.
dònka,dɔ̀nka→̌→ 2dɔ̀nkan.
dònkabɔ,dònkabɔ( entrer *infinitif sortir )dòn-kà-bɔ́.
donkabɔ,dònkabɔ( entrer *infinitif sortir )dòn-kà-bɔ́.
donkabò,dònkabɔ( entrer *infinitif sortir )dòn-kà-bɔ́.
dòn-kà-bɔ́,dòn-kà-bɔ́( entrer *infinitif sortir )dònkabɔ.dòn-kà-bɔ́.
don-ka-bɔ,dòn-kà-bɔ́( entrer *infinitif sortir )dònkabɔ.dòn-kà-bɔ́.
don-ka-bò,dòn-kà-bɔ́( entrer *infinitif sortir )dònkabɔ.dòn-kà-bɔ́.
dònkafilɛ,dònkafilɛ( entrer *infinitif regarder )dòn-kà-fílɛ.
donkafilɛ,dònkafilɛ( entrer *infinitif regarder )dòn-kà-fílɛ.
donkafilè,dònkafilɛ( entrer *infinitif regarder )dòn-kà-fílɛ.
dòn-kà-fílɛ,dòn-kà-fílɛ( entrer *infinitif regarder )dònkafilɛ.dòn-kà-fílɛ.
don-ka-filɛ,dòn-kà-fílɛ( entrer *infinitif regarder )dònkafilɛ.dòn-kà-fílɛ.
don-ka-filè,dòn-kà-fílɛ( entrer *infinitif regarder )dònkafilɛ.dòn-kà-fílɛ.
dɔ́nkalakari,dɔ́nkalakari→̌
dɔnkalakari,dɔ́nkalakari→̌
dònkalakari,dɔ́nkalakari→̌
dònkan,dònkan( entrer cou )
donkan,dònkan( entrer cou )
dɔ̀nkan,dɔ̀nkan→̌→ 2Voir entrée principale :dɔ̀nka.
dɔnkan,dɔ̀nkan→̌→ 2Voir entrée principale :dɔ̀nka.
dònkan,dɔ̀nkan→̌→ 2Voir entrée principale :dɔ̀nka.
dònkari,dònkari→̌→ 4dɔ̀nkɔri.dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
donkari,dònkari→̌→ 4dɔ̀nkɔri.dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dɔ̀nkari,dɔ̀nkari→̌dɔ̀nkɔri.dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dɔnkari,dɔ̀nkari→̌dɔ̀nkɔri.dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dònkari,dɔ̀nkari→̌dɔ̀nkɔri.dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dònkatɛmɛ,dònkatɛmɛ( entrer *infinitif passer )dòn-ká-tɛ̀mɛ.
donkatɛmɛ,dònkatɛmɛ( entrer *infinitif passer )dòn-ká-tɛ̀mɛ.
donkatèmè,dònkatɛmɛ( entrer *infinitif passer )dòn-ká-tɛ̀mɛ.
dòn-ká-tɛ̀mɛ,dòn-ká-tɛ̀mɛ( entrer *infinitif passer )dònkatɛmɛ.dòn-ká-tɛ̀mɛ.
don-ka-tɛmɛ,dòn-ká-tɛ̀mɛ( entrer *infinitif passer )dònkatɛmɛ.dòn-ká-tɛ̀mɛ.
don-ka-tèmè,dòn-ká-tɛ̀mɛ( entrer *infinitif passer )dònkatɛmɛ.dòn-ká-tɛ̀mɛ.
dɔ̀nkɛla,dɔ̀nkɛla( danse faire *agent permanent )
dɔnkɛla,dɔ̀nkɛla( danse faire *agent permanent )
dònkèla,dɔ̀nkɛla( danse faire *agent permanent )
dónkibaro,dónkibaro( jour nouvelle )dónkibaru.dónkibaro.
donkibaro,dónkibaro( jour nouvelle )dónkibaru.dónkibaro.
dónkibarobɔla,dónkibarobɔla( information.du.jour [ jour nouvelle ] sortir *agent permanent )dónkibarubɔla.dónkibarobɔla.
donkibarobɔla,dónkibarobɔla( information.du.jour [ jour nouvelle ] sortir *agent permanent )dónkibarubɔla.dónkibarobɔla.
donkibarobòla,dónkibarobɔla( information.du.jour [ jour nouvelle ] sortir *agent permanent )dónkibarubɔla.dónkibarobɔla.
dónkibaru,dónkibaru( jour nouvelle )dónkibaro.
donkibaru,dónkibaru( jour nouvelle )dónkibaro.
dónkibarubɔla,dónkibarubɔla( information.du.jour [ jour nouvelle ] sortir *agent permanent )dónkibarobɔla.
donkibarubɔla,dónkibarubɔla( information.du.jour [ jour nouvelle ] sortir *agent permanent )dónkibarobɔla.
donkibarubòla,dónkibarubɔla( information.du.jour [ jour nouvelle ] sortir *agent permanent )dónkibarobɔla.
dɔ̀nkili,dɔ̀nkili( danse appeler )
dɔnkili,dɔ̀nkili( danse appeler )
dònkili,dɔ̀nkili( danse appeler )
dɔ̀nkilidakɔnɔ,dɔ̀nkilidakɔnɔ( chant [ danse appeler ] oiseau )
dɔnkilidakɔnɔ,dɔ̀nkilidakɔnɔ( chant [ danse appeler ] oiseau )
dònkilidakònò,dɔ̀nkilidakɔnɔ( chant [ danse appeler ] oiseau )
dɔ̀nkilidala,dɔ̀nkilidala( chant [ danse appeler ] poser *agent permanent )
dɔnkilidala,dɔ̀nkilidala( chant [ danse appeler ] poser *agent permanent )
dònkilidala,dɔ̀nkilidala( chant [ danse appeler ] poser *agent permanent )
dónkò,dónkò( jour ce )dóngò.dónwò.
donko,dónkò( jour ce )dóngò.dónwò.
dɔ́nko,dɔ́nko( connaissance affaire )
dɔnko,dɔ́nko( connaissance affaire )
dònko,dɔ́nko( connaissance affaire )
dònkɔnɔ,dònkɔnɔ( entrer *je dans )dònnkɔnɔ.dònkɔnɔ.
donkɔnɔ,dònkɔnɔ( entrer *je dans )dònnkɔnɔ.dònkɔnɔ.
donkònò,dònkɔnɔ( entrer *je dans )dònnkɔnɔ.dònkɔnɔ.
dɔ̀nkɔnɔ,dɔ̀nkɔnɔ→̌dɔ̀gɔnɔ.dɔ̀nkɔnɔ.
dɔnkɔnɔ,dɔ̀nkɔnɔ→̌dɔ̀gɔnɔ.dɔ̀nkɔnɔ.
dònkònò,dɔ̀nkɔnɔ→̌dɔ̀gɔnɔ.dɔ̀nkɔnɔ.
dɔ̀nkɔri,dɔ̀nkɔri→̌→ 2dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dɔnkɔri,dɔ̀nkɔri→̌→ 2dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dònkòri,dɔ̀nkɔri→̌→ 2dɔ̀nkari;dɔ̀ngɔri;dònkari;dòngari;dɔ̀ngari.
dònkun,dònkun( entrer tête )
donkun,dònkun( entrer tête )
dónkunbɛn,dónkunbɛn( jour rencontre-accueil [ tête accord ] )
donkunbɛn,dónkunbɛn( jour rencontre-accueil [ tête accord ] )
donkunbèn,dónkunbɛn( jour rencontre-accueil [ tête accord ] )
dɔ́nmaa,dɔ́nmaa( connaître homme )Voir entrée principale :dɔ́nmɔgɔ.
dɔnmaa,dɔ́nmaa( connaître homme )Voir entrée principale :dɔ́nmɔgɔ.
dònmaa,dɔ́nmaa( connaître homme )Voir entrée principale :dɔ́nmɔgɔ.
dónmafila,dónmafila( jour *à deux )dónmafla.
donmafila,dónmafila( jour *à deux )dónmafla.
dónmafla,dónmafla( jour *à deux )dónmafila.dónmafla.
donmafla,dónmafla( jour *à deux )dónmafila.dónmafla.
dónmakɔnɔ,dónmakɔnɔ( jour attendre [ *connecteur attendre ] )
donmakɔnɔ,dónmakɔnɔ( jour attendre [ *connecteur attendre ] )
donmakònò,dónmakɔnɔ( jour attendre [ *connecteur attendre ] )
dɔ́nmɔgɔ,dɔ́nmɔgɔ( connaître homme )dɔ́nmaa.
dɔnmɔgɔ,dɔ́nmɔgɔ( connaître homme )dɔ́nmaa.
dònmògò,dɔ́nmɔgɔ( connaître homme )dɔ́nmaa.
dɔ́nnakari,dɔ́nnakari( connaissance rendre.inefficace [ *causatif casser ] )vt.
dɔnnakari,dɔ́nnakari( connaissance rendre.inefficace [ *causatif casser ] )vt.
dònnakari,dɔ́nnakari( connaissance rendre.inefficace [ *causatif casser ] )vt.
dónnatɛmɛ,dónnatɛmɛ( jour faire.passer [ *causatif passer ] )
donnatɛmɛ,dónnatɛmɛ( jour faire.passer [ *causatif passer ] )
donnatèmè,dónnatɛmɛ( jour faire.passer [ *causatif passer ] )
dònnbolo,dònnbolo( entrer *je bras )
donnbolo,dònnbolo( entrer *je bras )
dɔ́nni,dɔ́nni( connaître *nom d'action )
dɔnni,dɔ́nni( connaître *nom d'action )
dònni,dɔ́nni( connaître *nom d'action )
dɔ́nnibaa,dɔ́nnibaa( connaître *nom d'action *agent occasionnel )Voir entrée principale :dɔ́nnibaga.
dɔnnibaa,dɔ́nnibaa( connaître *nom d'action *agent occasionnel )Voir entrée principale :dɔ́nnibaga.
dònnibaa,dɔ́nnibaa( connaître *nom d'action *agent occasionnel )Voir entrée principale :dɔ́nnibaga.
dɔ́nnibaga,dɔ́nnibaga( connaître *nom d'action *agent occasionnel )dɔ́nnibaa.
dɔnnibaga,dɔ́nnibaga( connaître *nom d'action *agent occasionnel )dɔ́nnibaa.
dònnibaga,dɔ́nnibaga( connaître *nom d'action *agent occasionnel )dɔ́nnibaa.
dɔ́nnikɛla,dɔ́nnikɛla( science [ connaître *nom d'action ] faire *agent permanent )
dɔnnikɛla,dɔ́nnikɛla( science [ connaître *nom d'action ] faire *agent permanent )
dònnikèla,dɔ́nnikɛla( science [ connaître *nom d'action ] faire *agent permanent )
dɔ́nniya,dɔ́nniya( science [ connaître *nom d'action ] *abstractif )
dɔnniya,dɔ́nniya( science [ connaître *nom d'action ] *abstractif )
dònniya,dɔ́nniya( science [ connaître *nom d'action ] *abstractif )
dònnkɔnɔ,dònnkɔnɔ( entrer *je dans )dònkɔnɔ.
donnkɔnɔ,dònnkɔnɔ( entrer *je dans )dònkɔnɔ.
donnkònò,dònnkɔnɔ( entrer *je dans )dònkɔnɔ.
dònńkùnnabàna,dònńkùnnabàna( entrer *je tête à maladie )
donnkunnabana,dònńkùnnabàna( entrer *je tête à maladie )
dòno,dòno→̌→ 32dònon.dòndon;dòno.
dono,dòno→̌→ 32dònon.dòndon;dòno.
dɔ́nɔ,dɔ́nɔ→̌→ 4
dɔnɔ,dɔ́nɔ→̌→ 4
dònò,dɔ́nɔ→̌→ 4
dònobugun,dònobugun( coq se.blottir )dònonbugun.dònobugun.
donobugun,dònobugun( coq se.blottir )dònonbugun.dònobugun.
dònokɔrɔ,dònokɔrɔ( coq mâle.adulte )dònonkɔrɔ.dònokɔrɔ.
donokɔrɔ,dònokɔrɔ( coq mâle.adulte )dònonkɔrɔ.dònokɔrɔ.
donokòrò,dònokɔrɔ( coq mâle.adulte )dònonkɔrɔ.dònokɔrɔ.
dònon,dònon→̌→ 32dòndon;dòno.
donon,dònon→̌→ 32dòndon;dòno.
dònonbugun,dònonbugun( coq se.blottir )dònobugun.
dononbugun,dònonbugun( coq se.blottir )dònobugun.
dɔ̀nɔnkɔn,dɔ̀nɔnkɔn→̌tɔ̀nɔnkɔ.ntɔ̀nɔnkɔ;dɔ̀nɔnkɔn;tɔ̀nɔgɔ;tɔ̀rɔngɔ.
dɔnɔnkɔn,dɔ̀nɔnkɔn→̌tɔ̀nɔnkɔ.ntɔ̀nɔnkɔ;dɔ̀nɔnkɔn;tɔ̀nɔgɔ;tɔ̀rɔngɔ.
dònònkòn,dɔ̀nɔnkɔn→̌tɔ̀nɔnkɔ.ntɔ̀nɔnkɔ;dɔ̀nɔnkɔn;tɔ̀nɔgɔ;tɔ̀rɔngɔ.
dònonkɔrɔ,dònonkɔrɔ( coq mâle.adulte )dònokɔrɔ.
dononkɔrɔ,dònonkɔrɔ( coq mâle.adulte )dònokɔrɔ.
dononkòrò,dònonkɔrɔ( coq mâle.adulte )dònokɔrɔ.
dònontùlu,dònontùlu( coq huppe )dònotùlu.
donontulu,dònontùlu( coq huppe )dònotùlu.
dònonwalan,dònonwalan( coq moyen )dònowalan.
dononwalan,dònonwalan( coq moyen )dònowalan.
dònotùlu,dònotùlu( coq huppe )dònontùlu.dònotùlu.
donotulu,dònotùlu( coq huppe )dònontùlu.dònotùlu.
dònowalan,dònowalan( coq moyen )dònonwalan.dònowalan.
donowalan,dònowalan( coq moyen )dònonwalan.dònowalan.
dónse,dónse( jour arrivée )
donse,dónse( jour arrivée )
dònsɛ,dònsɛ( entrer poule )dònshɛ.dònsyɛ.
donsɛ,dònsɛ( entrer poule )dònshɛ.dònsyɛ.
donsè,dònsɛ( entrer poule )dònshɛ.dònsyɛ.
dɔ̀nsen,dɔ̀nsen( danse jambe )
dɔnsen,dɔ̀nsen( danse jambe )
dònsen,dɔ̀nsen( danse jambe )
dònshɛ,dònshɛ( entrer poule )dònsɛ;dònsyɛ.
donshɛ,dònshɛ( entrer poule )dònsɛ;dònsyɛ.
donshè,dònshɛ( entrer poule )dònsɛ;dònsyɛ.
dònso,dònso→̌→ 303
donso,dònso→̌→ 303
dònsoden,dònsoden( chasseur enfant )
donsoden,dònsoden( chasseur enfant )
dònsofɔli,dònsofɔli( chasseur action.de.dire [ dire *nom d'action ] )
donsofɔli,dònsofɔli( chasseur action.de.dire [ dire *nom d'action ] )
donsofòli,dònsofɔli( chasseur action.de.dire [ dire *nom d'action ] )
donsogo,Donsogo→̌Keyita.Voir entrée principale :Dansoko.Dansogo;Dansoko.(Ancêtre - Jatra Dansongo.)
dònsojeli,dònsojeli( chasseur griot )
donsojeli,dònsojeli( chasseur griot )
dònso-ká-wéele,dònso-ká-wéele( chasseur *possessif appeler )dònsô-k'án-wélé.
donso-ka-weele,dònso-ká-wéele( chasseur *possessif appeler )dònsô-k'án-wélé.
dònsokɛ,dònsokɛ( chasseur mâle )
donsokɛ,dònsokɛ( chasseur mâle )
donsokè,dònsokɛ( chasseur mâle )
dònsô-k'án-wélé,dònsô-k'án-wélé( chasseur *subjonctif *nous appeler )Voir entrée principale :dònso-ká-wéele.
donso-k'an-wele,dònsô-k'án-wélé( chasseur *subjonctif *nous appeler )Voir entrée principale :dònso-ká-wéele.
dònsonkɔni,dònsonkɔni( chasseur guitare-harpe )
donsonkɔni,dònsonkɔni( chasseur guitare-harpe )
donsonkòni,dònsonkɔni( chasseur guitare-harpe )
dònsotɔn,dònsotɔn( chasseur société )
donsotɔn,dònsotɔn( chasseur société )
donsotòn,dònsotɔn( chasseur société )
dònsoya,dònsoya( chasseur *abstractif )
donsoya,dònsoya( chasseur *abstractif )
dònsyɛ,dònsyɛ( entrer poule )dònshɛ.dònsɛ;dònsyɛ.
donsyɛ,dònsyɛ( entrer poule )dònshɛ.dònsɛ;dònsyɛ.
donsyè,dònsyɛ( entrer poule )dònshɛ.dònsɛ;dònsyɛ.
dɔ́nta,dɔ́nta( connaître *participe potentiel )
dɔnta,dɔ́nta( connaître *participe potentiel )
dònta,dɔ́nta( connaître *participe potentiel )
dóntɛmɛ,dóntɛmɛ( jour passer )
dontɛmɛ,dóntɛmɛ( jour passer )
dontèmè,dóntɛmɛ( jour passer )
dónwò,dónwò( jour ce )dóngò.dónkò.
donwo,dónwò( jour ce )dóngò.dónkò.
dɔ́nyɔrɔ,dɔ́nyɔrɔ( connaître lieu )
dɔnyɔrɔ,dɔ́nyɔrɔ( connaître lieu )
dònyòrò,dɔ́nyɔrɔ( connaître lieu )
dóo,dóo→̌Voir entrée principale :dóloo.
doo,dóo→̌Voir entrée principale :dóloo.
dóolen,dóolen→̌→ 1dólen;ndóolen;ndólen;dɔ́len.
doolen,dóolen→̌→ 1dólen;ndóolen;ndólen;dɔ́len.
dóoli,dóoli→̌
dooli,dóoli→̌
dóolo,dóolo→̌vi.dòolo.
doolo,dóolo→̌vi.dòolo.
dòolo,dòolo→̌→ 12Voir entrée principale :dòlo.
dɔ́ɔni,dɔ́ɔni→̌→ 320dɔ́ɔnin.dɔ́ɔni.
dɔɔni,dɔ́ɔni→̌→ 320dɔ́ɔnin.dɔ́ɔni.
dòoni,dɔ́ɔni→̌→ 320dɔ́ɔnin.dɔ́ɔni.
dɔ́ɔnin,dɔ́ɔnin→̌→ 322dɔ́ɔni.
dɔɔnin,dɔ́ɔnin→̌→ 322dɔ́ɔni.
dòonin,dɔ́ɔnin→̌→ 322dɔ́ɔni.
dɔ́ɔnindɔɔnin,dɔ́ɔnindɔɔnin( un.peu un.peu )
dɔɔnindɔɔnin,dɔ́ɔnindɔɔnin( un.peu un.peu )
dòonindòonin,dɔ́ɔnindɔɔnin( un.peu un.peu )
dɔ̀ɔntin,dɔ̀ɔntin→̌
dɔɔntin,dɔ̀ɔntin→̌
dòontin,dɔ̀ɔntin→̌
dopamini,dopamini→̌
dóra,dóra→̌→ 2
dora,dóra→̌→ 2
dóradoradora,dóradoradora→̌
doradoradora,dóradoradora→̌
dɔribugu,Dɔribugu→̌
dòribugu,Dɔribugu→̌
dorizini,dorizini→̌Voir entrée principale :orizini.
dóro,dóro→̌ntòro.
doro,dóro→̌ntòro.
dórobara,dórobara( bourses calebasse )
dorobara,dórobara( bourses calebasse )
dórodoro,dórodoro→̌
dorodoro,dórodoro→̌
dóroga,dóroga→̌→ 2→n : 25vt.dóroko.dórogo;dóroga.
doroga,dóroga→̌→ 2→n : 25vt.dóroko.dórogo;dóroga.
dórogo,dórogo→̌vi.
dorogo,dórogo→̌vi.
dórogolen,dórogolen( serrer *participe résultatif )
dorogolen,dórogolen( serrer *participe résultatif )
dòrogoto,dòrogoto→̌vi.
dorogoto,dòrogoto→̌vi.
dɔ́rɔgu,dɔ́rɔgu→̌→ 40drɔ́gu.
dɔrɔgu,dɔ́rɔgu→̌→ 40drɔ́gu.
dòrògu,dɔ́rɔgu→̌→ 40drɔ́gu.
dɔ́rɔgutala,dɔ́rɔgutala( drogue prendre *agent permanent )drɔ́gutala.
dɔrɔgutala,dɔ́rɔgutala( drogue prendre *agent permanent )drɔ́gutala.
dòrògutala,dɔ́rɔgutala( drogue prendre *agent permanent )drɔ́gutala.
dórokili,dórokili( bourses oeuf )
dorokili,dórokili( bourses oeuf )
dóroko,dóroko→̌→ 9→n : 25vt.dórogo;dóroga.
doroko,dóroko→̌→ 9→n : 25vt.dórogo;dóroga.
dɔ́rɔmɛ,dɔ́rɔmɛ→̌→ 451dɔ́rɔ̌mɛ́.Ar. dirham 'drahme'
dɔrɔmɛ,dɔ́rɔmɛ→̌→ 451dɔ́rɔ̌mɛ́.Ar. dirham 'drahme'
dòròmè,dɔ́rɔmɛ→̌→ 451dɔ́rɔ̌mɛ́.Ar. dirham 'drahme'
dɔ́rɔn,dɔ́rɔn→̌→ 567
dɔrɔn,dɔ́rɔn→̌→ 567
dòròn,dɔ́rɔn→̌→ 567
doroni,doroni→̌→ 2
dororan,dororan→̌
dose,Dose→̌
dɔsi,Dɔsi→̌
dòsi,Dɔsi→̌
dósiyɛn,dósiyɛn→̌dásan;dósyan.
dosiyɛn,dósiyɛn→̌dásan;dósyan.
dosiyèn,dósiyɛn→̌dásan;dósyan.
dóso,dóso→̌→ 3
doso,dóso→̌→ 3
dòsokodosoko,dòsokodosoko→̌
dosokodosoko,dòsokodosoko→̌
dósokɔrɔ,dósokɔrɔ( gros.chien.mâle mâle.adulte )
dosokɔrɔ,dósokɔrɔ( gros.chien.mâle mâle.adulte )
dosokòrò,dósokɔrɔ( gros.chien.mâle mâle.adulte )
dɔ̀surun,dɔ̀surun( station.debout court )jɔ̀surun.dɔ̀surun.
dɔsurun,dɔ̀surun( station.debout court )jɔ̀surun.dɔ̀surun.
dòsurun,dɔ̀surun( station.debout court )jɔ̀surun.dɔ̀surun.
dósyan,dósyan→̌→ 1dósiyɛn.dásan;dósyan.
dosyan,dósyan→̌→ 1dósiyɛn.dásan;dósyan.
dɔ́wɛrɛ,dɔ́wɛrɛ( certain autre )
dɔwɛrɛ,dɔ́wɛrɛ( certain autre )
dòwèrè,dɔ́wɛrɛ( certain autre )
dóyi,dóyi→̌
doyi,dóyi→̌
dɔ́yi,dɔ́yi→̌→ 1
dɔyi,dɔ́yi→̌→ 1
dòyi,dɔ́yi→̌→ 1
doyila,Doyila→̌Voir entrée principale :Dɔyila.
dɔyila,Dɔyila→̌Doyila.
dòyila,Dɔyila→̌Doyila.
dɔ́yili,dɔ́yili→̌jɔ́yili.
dɔyili,dɔ́yili→̌jɔ́yili.
dòyili,dɔ́yili→̌jɔ́yili.
drà,drà→̌dàra.drà.Source :fr : mettre dans de beaux draps ?
dra,drà→̌dàra.drà.Source :fr : mettre dans de beaux draps ?
draba,Draba→̌
dráli,dráli→̌dárali.dráli.
drali,dráli→̌dárali.dráli.
dramɛ,Dramɛ→̌Voir :Daramɛ.(tanneurs.)
dramè,Dramɛ→̌Voir :Daramɛ.(tanneurs.)
dramera,Dramera→̌Daramera.(Bergers.)
dràwela,Dràwela→̌
drawela,Dràwela→̌
drɛ́ɛ,drɛ́ɛ→̌dɛ́rrɛ.dɛ́rɛtɛtɛ;dɛ́rɛɛ;drɛ́ɛ.
drɛɛ,drɛ́ɛ→̌dɛ́rrɛ.dɛ́rɛtɛtɛ;dɛ́rɛɛ;drɛ́ɛ.
drèe,drɛ́ɛ→̌dɛ́rrɛ.dɛ́rɛtɛtɛ;dɛ́rɛɛ;drɛ́ɛ.
drɔ́gu,drɔ́gu→̌dɔ́rɔgu.drɔ́gu.
drɔgu,drɔ́gu→̌dɔ́rɔgu.drɔ́gu.
drògu,drɔ́gu→̌dɔ́rɔgu.drɔ́gu.
drɔ́gutala,drɔ́gutala( drogue prendre *agent permanent )dɔ́rɔgutala.drɔ́gutala.
drɔgutala,drɔ́gutala( drogue prendre *agent permanent )dɔ́rɔgutala.drɔ́gutala.
drògutala,drɔ́gutala( drogue prendre *agent permanent )dɔ́rɔgutala.drɔ́gutala.
dú,dú→̌→ 827
du,dú→̌→ 827
dù,dù→̌→ 8→n : 2Voir entrée principale :dùn.
dúba,dúba→̌dúfa.
duba,dúba→̌dúfa.
dùba,dùba→̌→ 6dùga.dùwa;dùfa;dùbaa.ar: du`a' = invocation
dùbaa,dùbaa→̌dùga.dùwa;dùba;dùfa;dùbaa.ar: du`a' = invocation
dubaa,dùbaa→̌dùga.dùwa;dùba;dùfa;dùbaa.ar: du`a' = invocation
dùbabu,dùbabu→̌vi.
dubabu,dùbabu→̌vi.
dubabugu,Dubabugu→̌Dugabugu.
dùbabuma,dùbabuma( bénédiction *comme de )
dubabuma,dùbabuma( bénédiction *comme de )
dùbaden,dùbaden( bénédiction enfant )Voir entrée principale :dùgaden.
dubaden,dùbaden( bénédiction enfant )Voir entrée principale :dùgaden.
dúbalen,dúbalen→̌
dubalen,dúbalen→̌
dúbàlen,dúbàlen→̌→ 11dúgàlen;dúfàlen;ndúbàlen;ntúfàlen.
dùbalen,dùbalen→̌dùngare.dùgalen;dùgare;dùgaren;dùbalen;dùngaren.
dubile,dubile→̌
dúdàdu,dúdàdu→̌
dudadu,dúdàdu→̌
dúden,dúden( concession enfant )
duden,dúden( concession enfant )
dùdù,Dùdù→̌
dudu,Dùdù→̌
dúfa,"dúfa→̌rn, fn.júfa.dúfa;júga."
dufa,"dúfa→̌rn, fn.júfa.dúfa;júga."
dùfa,dùfa→̌dùga.dùfa.
dúfakɛla,dúfakɛla( divination faire *agent permanent )
dufakɛla,dúfakɛla( divination faire *agent permanent )
dufakèla,dúfakɛla( divination faire *agent permanent )
dúfàlen,dúfàlen→̌→ 4dúbàlen.dúgàlen;dúfàlen;ndúbàlen;ntúfàlen.
dufalen,dúfàlen→̌→ 4dúbàlen.dúgàlen;dúfàlen;ndúbàlen;ntúfàlen.
dùfamasa,dùfamasa( vautour roi )Voir entrée principale :dùgamasa.
dufamasa,dùfamasa( vautour roi )Voir entrée principale :dùgamasa.
dùfamàsakɔrɔ,dùfamàsakɔrɔ( vautour roi vieux )dùgamàsakɔrɔ.dùfamàsakɔrɔ.
dufamasakɔrɔ,dùfamàsakɔrɔ( vautour roi vieux )dùgamàsakɔrɔ.dùfamàsakɔrɔ.
dufamasakòrò,dùfamàsakɔrɔ( vautour roi vieux )dùgamàsakɔrɔ.dùfamàsakɔrɔ.
dúfan,dúfan→̌dúga.dúgan;dúfa;dúfan.
dufan,dúfan→̌dúga.dúgan;dúfa;dúfan.
dùfon,dùfon→̌→ 10
dufon,dùfon→̌→ 10
dúga,dúga→̌→ 1dúgan;dúfa;dúfan.
duga,dúga→̌→ 1dúgan;dúfa;dúfan.
dùga,dùga→̌→ 62dùfa.
dugabugu,Dugabugu→̌Voir entrée principale :Dubabugu.
dùgaden,dùgaden( bénédiction enfant )dùbaden.
dugaden,dùgaden( bénédiction enfant )dùbaden.
dúgàlen,dúgàlen→̌→ 1dúbàlen.dúfàlen;ndúbàlen;ntúfàlen.
dugalen,dúgàlen→̌→ 1dúbàlen.dúfàlen;ndúbàlen;ntúfàlen.
dùgalen,dùgalen→̌→ 10dùngare.dùgare;dùgaren;dùbalen;dùngaren.
dùgamasa,dùgamasa( vautour roi )dùfamasa.
dugamasa,dùgamasa( vautour roi )dùfamasa.
dùgamàsakɔrɔ,dùgamàsakɔrɔ( vautour roi vieux )dùfamàsakɔrɔ.
dugamasakɔrɔ,dùgamàsakɔrɔ( vautour roi vieux )dùfamàsakɔrɔ.
dugamasakòrò,dùgamàsakɔrɔ( vautour roi vieux )dùfamàsakɔrɔ.
dúgan,dúgan→̌→ 3dúga.dúfa;dúfan.
dugan,dúgan→̌→ 3dúga.dúfa;dúfan.
dùgan,dùgan→̌jùgan.
dugaɲɛ,dugaɲɛ→̌Voir entrée principale :duwaɲɛ.
duganyè,dugaɲɛ→̌Voir entrée principale :duwaɲɛ.
dugansi,Dugansi→̌Sisigo.Voir entrée principale :Dukansi.Dùwansí;Dukansi.(originaires de Wuluma (Nord de Kayes). Forgerons (tagu).)
dùgare,dùgare→̌dùngare.dùgalen;dùgare;dùgaren;dùbalen;dùngaren.
dugare,dùgare→̌dùngare.dùgalen;dùgare;dùgaren;dùbalen;dùngaren.
dùgaren,dùgaren→̌dùngare.dùgalen;dùgare;dùgaren;dùbalen;dùngaren.
dugaren,dùgaren→̌dùngare.dùgalen;dùgare;dùgaren;dùbalen;dùngaren.
dùgawu,dùgawu→̌→ 95dùbabu;dùwawu.
dugawu,dùgawu→̌→ 95dùbabu;dùwawu.
dúgeduge,dúgeduge→̌Voir entrée principale :dúgudugu.
dugeduge,dúgeduge→̌Voir entrée principale :dúgudugu.
dùgu,dùgu→̌→ 1
dugu,dùgu→̌→ 1
dùguba,Dùguba→̌→n.prop : 1
duguba,Dùguba→̌→n.prop : 1
dùguci,dùguci( terre frapper )
duguci,dùguci( terre frapper )
dùgucila,dùgucila( terre frapper *agent permanent )
dugucila,dùgucila( terre frapper *agent permanent )
dùgudɛgɛ,dùgudɛgɛ→̌vr.
dugudɛgɛ,dùgudɛgɛ→̌vr.
dugudègè,dùgudɛgɛ→̌vr.
dùguden,dùguden( terre enfant )
duguden,dùguden( terre enfant )
dúgudugu,dúgudugu→̌→ 1dúgeduge.
dugudugu,dúgudugu→̌→ 1dúgeduge.
dùgudugu,dùgudugu→̌
dùgudùgu,dùgudùgu→̌
dùgufana,Dùgufana→̌
dugufana,Dùgufana→̌
dùgujɛ,dùgujɛ( terre blanc )
dugujɛ,dùgujɛ( terre blanc )
dugujè,dùgujɛ( terre blanc )
dùgujɛda,dùgujɛda( aube [ terre blanc ] bouche )dùgujɛnda.
dugujɛda,dùgujɛda( aube [ terre blanc ] bouche )dùgujɛnda.
dugujèda,dùgujɛda( aube [ terre blanc ] bouche )dùgujɛnda.
dùgujɛnda,dùgujɛnda( aube [ terre blanc ] bouche )dùgujɛda.dùgujɛnda.
dugujɛnda,dùgujɛnda( aube [ terre blanc ] bouche )dùgujɛda.dùgujɛnda.
dugujènda,dùgujɛnda( aube [ terre blanc ] bouche )dùgujɛda.dùgujɛnda.
dùgujukɔrɔsa,dùgujukɔrɔsa( terre dessous [ derrière sous ] serpent )
dugujukɔrɔsa,dùgujukɔrɔsa( terre dessous [ derrière sous ] serpent )
dugujukòròsa,dùgujukɔrɔsa( terre dessous [ derrière sous ] serpent )
dùgukolo,dùgukolo( terre os )
dugukolo,dùgukolo( terre os )
dùgukolokunsi,dùgukolokunsi( terre [ terre os ] cheveux [ tête ] )
dugukolokunsi,dùgukolokunsi( terre [ terre os ] cheveux [ tête ] )
dùgukolonɔ,dùgukolonɔ( terre [ terre os ] lécher )Voir entrée principale :dùgukolonɔn.
dugukolonɔ,dùgukolonɔ( terre [ terre os ] lécher )Voir entrée principale :dùgukolonɔn.
dugukolonò,dùgukolonɔ( terre [ terre os ] lécher )Voir entrée principale :dùgukolonɔn.
dùgukolonɔn,dùgukolonɔn( terre [ terre os ] lécher )dùgukolonɔ.
dugukolonɔn,dùgukolonɔn( terre [ terre os ] lécher )dùgukolonɔ.
dugukolonòn,dùgukolonɔn( terre [ terre os ] lécher )dùgukolonɔ.
dùgukolosànin,dùgukolosànin( terre [ terre os ] serpent *diminutif )
dugukolosanin,dùgukolosànin( terre [ terre os ] serpent *diminutif )
dùgukoloyɛrɛyɛrɛ,dùgukoloyɛrɛyɛrɛ( terre [ terre os ] trembler )
dugukoloyɛrɛyɛrɛ,dùgukoloyɛrɛyɛrɛ( terre [ terre os ] trembler )
dugukoloyèrèyèrè,dùgukoloyɛrɛyɛrɛ( terre [ terre os ] trembler )
dùgukɔnɔna,dùgukɔnɔna( terre dans *nom de lieu )
dugukɔnɔna,dùgukɔnɔna( terre dans *nom de lieu )
dugukònòna,dùgukɔnɔna( terre dans *nom de lieu )
dùgukuna,Dùgukuna→̌Dùgukunan.
dugukuna,Dùgukuna→̌Dùgukunan.
dùgukunan,Dùgukunan→̌Voir entrée principale :Dùgukuna.
dugukunan,Dùgukunan→̌Voir entrée principale :Dùgukuna.
dùgukunsigi,dùgukunsigi( terre cheveux [ tête ] )
dugukunsigi,dùgukunsigi( terre cheveux [ tête ] )
dùgulen,dùgulen→̌→ 65
dugulen,dùgulen→̌→ 65
dùgulentɔgɔ,dùgulentɔgɔ( autochtone nom )
dugulentɔgɔ,dùgulentɔgɔ( autochtone nom )
dugulentògò,dùgulentɔgɔ( autochtone nom )
dùgulenya,dùgulenya( autochtone *abstractif )
dugulenya,dùgulenya( autochtone *abstractif )
dùgumada,dùgumada( terre *à bouche )
dugumada,dùgumada( terre *à bouche )
dùgumadagannin,dùgumadagannin( terre *à arbre.Afzelia.africana *diminutif )dùgumadanganin.
dugumadagannin,dùgumadagannin( terre *à arbre.Afzelia.africana *diminutif )dùgumadanganin.
dùgumadanganin,dùgumadanganin( terre *à arbre.Afzelia.africana *diminutif )Voir entrée principale :dùgumadagannin.
dugumadanganin,dùgumadanganin( terre *à arbre.Afzelia.africana *diminutif )Voir entrée principale :dùgumadagannin.
dùgumadawolo,dùgumadawolo( terre *à lèvre [ bouche peau ] )
dugumadawolo,dùgumadawolo( terre *à lèvre [ bouche peau ] )
dùgumafɛn,dùgumafɛn( terre *à chose )
dugumafɛn,dùgumafɛn( terre *à chose )
dugumafèn,dùgumafɛn( terre *à chose )
dùgumakalan,dùgumakalan( terre *à lecture )
dugumakalan,dùgumakalan( terre *à lecture )
dùgumakɛlɛcɛ,dùgumakɛlɛcɛ( terre *à soldat [ querelle mâle ] )
dugumakɛlɛcɛ,dùgumakɛlɛcɛ( terre *à soldat [ querelle mâle ] )
dugumakèlècè,dùgumakɛlɛcɛ( terre *à soldat [ querelle mâle ] )
dùgumala,dùgumala( terre *comme de *nom de lieu )Voir entrée principale :dùgumana.
dugumala,dùgumala( terre *comme de *nom de lieu )Voir entrée principale :dùgumana.
dùgumana,dùgumana( terre *comme de *nom de lieu )dùgumala.
dugumana,dùgumana( terre *comme de *nom de lieu )dùgumala.
dùgumaɲamaku,dùgumaɲamaku( terre *à gingembre )
dugumaɲamaku,dùgumaɲamaku( terre *à gingembre )
dugumanyamaku,dùgumaɲamaku( terre *à gingembre )
dùgumanaso,dùgumanaso( terre *comme de *nom de lieu maison )
dugumanaso,dùgumanaso( terre *comme de *nom de lieu maison )
dùgumasa,dùgumasa( terre roi )
dugumasa,dùgumasa( terre roi )
dùgumasara,dùgumasara( terre *à paie )
dugumasara,dùgumasara( terre *à paie )
dùgumata,dùgumata( terre *à propriété )
dugumata,dùgumata( terre *à propriété )
dùgumɛnɛ,dùgumɛnɛ( terre fourmi.sp )
dugumɛnɛ,dùgumɛnɛ( terre fourmi.sp )
dugumènè,dùgumɛnɛ( terre fourmi.sp )
dúgun,dúgun→̌búgun.dúgun.
dugun,dúgun→̌búgun.dúgun.
dùgura,dùgura→̌→ 3dògora.
dugura,dùgura→̌→ 3dògora.
dúgure,dúgure→̌
dugure,dúgure→̌
dùgure,dùgure→̌
dùgurɔsa,dùgurɔsa( terre dans serpent )dùgurɔsanin.
dugurɔsa,dùgurɔsa( terre dans serpent )dùgurɔsanin.
duguròsa,dùgurɔsa( terre dans serpent )dùgurɔsanin.
dùgurɔsanin,dùgurɔsanin( terre dans serpent *diminutif )Voir entrée principale :dùgurɔsa.
dugurɔsanin,dùgurɔsanin( terre dans serpent *diminutif )Voir entrée principale :dùgurɔsa.
duguròsanin,dùgurɔsanin( terre dans serpent *diminutif )Voir entrée principale :dùgurɔsa.
dúguru,dúguru→̌dúguu.
duguru,dúguru→̌dúguu.
dùgurudɛgɛrɛ,dùgurudɛgɛrɛ→̌vi/vr.
dugurudɛgɛrɛ,dùgurudɛgɛrɛ→̌vi/vr.
dugurudègèrè,dùgurudɛgɛrɛ→̌vi/vr.
dùgusa,dùgusa( terre serpent )
dugusa,dùgusa( terre serpent )
dùgusajɛ,dùgusajɛ( terre blanc )dùgusɛjɛ.dùgusajɛ.
dugusajɛ,dùgusajɛ( terre blanc )dùgusɛjɛ.dùgusajɛ.
dugusajè,dùgusajɛ( terre blanc )dùgusɛjɛ.dùgusajɛ.
dùgusɛ,dùgusɛ( terre )dùgusa.
dugusɛ,dùgusɛ( terre )dùgusa.
dugusè,dùgusɛ( terre )dùgusa.
dùgusɛgɛ,dùgusɛgɛ( terre salpêtre )
dugusɛgɛ,dùgusɛgɛ( terre salpêtre )
dugusègè,dùgusɛgɛ( terre salpêtre )
dùgusɛjɛ,dùgusɛjɛ( terre blanc )dùgusajɛ.
dugusɛjɛ,dùgusɛjɛ( terre blanc )dùgusajɛ.
dugusèjè,dùgusɛjɛ( terre blanc )dùgusajɛ.
dùgusen,dùgusen( terre jambe )
dugusen,dùgusen( terre jambe )
dùgutaa,dùgutaa( terre aller )dùgutaga.
dugutaa,dùgutaa( terre aller )dùgutaga.
dùgutaga,dùgutaga( terre aller )Voir entrée principale :dùgutaa.
dugutaga,dùgutaga( terre aller )Voir entrée principale :dùgutaa.
dùgutɛ̀nɛ,dùgutɛ̀nɛ( terre tabou )
dugutɛnɛ,dùgutɛ̀nɛ( terre tabou )
dugutènè,dùgutɛ̀nɛ( terre tabou )
dùgutigi,dùgutigi( terre maître )
dugutigi,dùgutigi( terre maître )
dùgutigibugu,Dùgutigibugu→̌
dugutigibugu,Dùgutigibugu→̌
dùgutigiya,dùgutigiya( chef.de.village [ terre maître ] *abstractif )
dugutigiya,dùgutigiya( chef.de.village [ terre maître ] *abstractif )
dùgutigi-y'-án-wéle,dùgutigi-y'-án-wéle( chef.de.village [ terre maître ] *perfectif transitif *nous appeler )
dugutigi-y'-an-wele,dùgutigi-y'-án-wéle( chef.de.village [ terre maître ] *perfectif transitif *nous appeler )
dùgutila,dùgutila( terre moitié )dùgutilama.
dugutila,dùgutila( terre moitié )dùgutilama.
dùgutilama,dùgutilama( terre moitié *comme de )Voir entrée principale :dùgutila.
dugutilama,dùgutilama( terre moitié *comme de )Voir entrée principale :dùgutila.
dùguturu,dùguturu( terre planter )
duguturu,dùguturu( terre planter )
dúguu,dúguu→̌Voir entrée principale :dúguru.
duguu,dúguu→̌Voir entrée principale :dúguru.
dukansi,Dukansi→̌Sisigo.Dùwansí;Dugansi.(originaires de Wuluma (Nord de Kayes). Forgerons (tagu).)
dukare,Dukare→̌
dúkɛnɛ,dúkɛnɛ( concession clarté )
dukɛnɛ,dúkɛnɛ( concession clarté )
dukènè,dúkɛnɛ( concession clarté )
dúkɔnɔmɔgɔ,dúkɔnɔmɔgɔ( concession dans homme )
dukɔnɔmɔgɔ,dúkɔnɔmɔgɔ( concession dans homme )
dukònòmògò,dúkɔnɔmɔgɔ( concession dans homme )
dúkùre,Dúkùre→̌Tɔntigi. Земледельцы.
dukure,Dúkùre→̌Tɔntigi. Земледельцы.
dulayi,Dulayi→̌Abdulayi.Abdulaye;Abudulayi;Abudulaye;Abudɛli;Abuduli;Abudulu;Abdlaye;Abdul;Àbudù;Abilayi;Duleyi;Ábùlo.
dúlen,dúlen→̌→ 5
dulen,dúlen→̌→ 5
dùlenya,dùlenya( courber *participe résultatif *abstractif )dùnnenya.dùlenya.
dulenya,dùlenya( courber *participe résultatif *abstractif )dùnnenya.dùlenya.
duleyi,Duleyi→̌Abdulayi.Abdulaye;Abudulayi;Abudulaye;Abudɛli;Abuduli;Abudulu;Abdlaye;Abdul;Àbudù;Abilayi;Dulayi;Ábùlo.
dùli,dùli→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
duli,dùli→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
dùlɔ,dùlɔ→̌dɔ̀lɔ.dlɔ̀.
dulɔ,dùlɔ→̌dɔ̀lɔ.dlɔ̀.
dulò,dùlɔ→̌dɔ̀lɔ.dlɔ̀.
dùlɔbo,dùlɔbo( bière.de.mil excrément )dɔ̀lɔbo.dùlɔbo;dlɔ̀bo.
dulɔbo,dùlɔbo( bière.de.mil excrément )dɔ̀lɔbo.dùlɔbo;dlɔ̀bo.
dulòbo,dùlɔbo( bière.de.mil excrément )dɔ̀lɔbo.dùlɔbo;dlɔ̀bo.
dùlɔdonna,dùlɔdonna( bière.de.mil entrer *agent permanent )dɔ̀lɔdonna.dùlɔdonna;dlɔ̀donna.
dulɔdonna,dùlɔdonna( bière.de.mil entrer *agent permanent )dɔ̀lɔdonna.dùlɔdonna;dlɔ̀donna.
dulòdonna,dùlɔdonna( bière.de.mil entrer *agent permanent )dɔ̀lɔdonna.dùlɔdonna;dlɔ̀donna.
dùlɔgɛrɛn,dùlɔgɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dulɔgɛrɛn,dùlɔgɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dulògèrèn,dùlɔgɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dùlɔgwɛrɛn,dùlɔgwɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dulɔgwɛrɛn,dùlɔgwɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dulògwèrèn,dùlɔgwɛrɛn( bière.de.mil évaporer )dɔ̀lɔgɛrɛn.dùlɔgɛrɛn;dlɔ̀gɛrɛn;dɔ̀lɔgwɛrɛn;dùlɔgwɛrɛn;dlɔ̀gwɛrɛn.
dùlɔjuru,dùlɔjuru( bière.de.mil corde )dɔ̀lɔjuru.dùlɔjuru;dlɔ̀juru.
dulɔjuru,dùlɔjuru( bière.de.mil corde )dɔ̀lɔjuru.dùlɔjuru;dlɔ̀juru.
dulòjuru,dùlɔjuru( bière.de.mil corde )dɔ̀lɔjuru.dùlɔjuru;dlɔ̀juru.
dùlɔkasila,dùlɔkasila( bière.de.mil pleurer *agent permanent )dɔ̀lɔkasila.dùlɔkasila;dlɔ̀kasila.
dulɔkasila,dùlɔkasila( bière.de.mil pleurer *agent permanent )dɔ̀lɔkasila.dùlɔkasila;dlɔ̀kasila.
dulòkasila,dùlɔkasila( bière.de.mil pleurer *agent permanent )dɔ̀lɔkasila.dùlɔkasila;dlɔ̀kasila.
dùloki,dùloki→̌→ 29dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
duloki,dùloki→̌→ 29dùlɔki;dɔ̀lɔki;dlɔ̀ki;dlòki.
dùlɔki,dùlɔki→̌→ 75dùloki.dɔ̀lɔki;dlɔ̀ki;dlòki.
dulɔki,dùlɔki→̌→ 75dùloki.dɔ̀lɔki;dlɔ̀ki;dlòki.
dulòki,dùlɔki→̌→ 75dùloki.dɔ̀lɔki;dlɔ̀ki;dlòki.
dùlokoto,dùlokoto→̌dlòkoto.
dulokoto,dùlokoto→̌dlòkoto.
dù̀lɔmin,dù̀lɔmin( bière.de.mil boire )dɔ̀lɔmin.dù̀lɔmin;dlɔ̀min.
dulɔmin,dù̀lɔmin( bière.de.mil boire )dɔ̀lɔmin.dù̀lɔmin;dlɔ̀min.
dulòmin,dù̀lɔmin( bière.de.mil boire )dɔ̀lɔmin.dù̀lɔmin;dlɔ̀min.
dùlɔminna,dùlɔminna( bière.de.mil boire *agent permanent )dɔ̀lɔminna.dùlɔminna;dlɔ̀minna.
dulɔminna,dùlɔminna( bière.de.mil boire *agent permanent )dɔ̀lɔminna.dùlɔminna;dlɔ̀minna.
dulòminna,dùlɔminna( bière.de.mil boire *agent permanent )dɔ̀lɔminna.dùlɔminna;dlɔ̀minna.
dùlɔmɔɔni,dùlɔmɔɔni( bière.de.mil ramollir )dɔ̀lɔmɔɔni.dùlɔmɔɔni;dlɔ̀mɔɔni.
dulɔmɔɔni,dùlɔmɔɔni( bière.de.mil ramollir )dɔ̀lɔmɔɔni.dùlɔmɔɔni;dlɔ̀mɔɔni.
dulòmòoni,dùlɔmɔɔni( bière.de.mil ramollir )dɔ̀lɔmɔɔni.dùlɔmɔɔni;dlɔ̀mɔɔni.
dúlon,dúlon→̌→ 51→n : 7→v-v : 1dlón;búlon;gúlon.
dulon,dúlon→̌→ 51→n : 7→v-v : 1dlón;búlon;gúlon.
dúlondulonmugu,dúlondulonmugu( poudre )
dulondulonmugu,dúlondulonmugu( poudre )
dùlɔtɔ,dùlɔtɔ( bière.de.mil *statif )dɔ̀lɔtɔ.dùlɔtɔ;dlɔ̀tɔ.
dulɔtɔ,dùlɔtɔ( bière.de.mil *statif )dɔ̀lɔtɔ.dùlɔtɔ;dlɔ̀tɔ.
dulòtò,dùlɔtɔ( bière.de.mil *statif )dɔ̀lɔtɔ.dùlɔtɔ;dlɔ̀tɔ.
dùlɔtɔya,dùlɔtɔya( ivre [ bière.de.mil *statif ] *abstractif )dɔ̀lɔtɔya.dùlɔtɔya;dlɔ̀tɔya.
dulɔtɔya,dùlɔtɔya( ivre [ bière.de.mil *statif ] *abstractif )dɔ̀lɔtɔya.dùlɔtɔya;dlɔ̀tɔya.
dulòtòya,dùlɔtɔya( ivre [ bière.de.mil *statif ] *abstractif )dɔ̀lɔtɔya.dùlɔtɔya;dlɔ̀tɔya.
dúman,dúman( agréable *adjectivateur )
duman,dúman( agréable *adjectivateur )
dùmaŋère,dùmaŋère→̌Voir entrée principale :tùmawùle.
dumaŋere,dùmaŋère→̌Voir entrée principale :tùmawùle.
dùmáŋèré,dùmáŋèré→̌tùmawule.
dumanzana,Dumanzana→̌
dumasi,Dumasi→̌
dúmɔgɔ,dúmɔgɔ( concession homme )
dumɔgɔ,dúmɔgɔ( concession homme )
dumògò,dúmɔgɔ( concession homme )
dúmu,dúmu→̌→ 2→n : 210vt.dún.dúmu;dúmun.
dumu,dúmu→̌→ 2→n : 210vt.dún.dúmu;dúmun.
dùmu,dùmu→̌→ 3dùnu.
dúmun,dúmun→̌→ 2→n : 214vt.dún.dúmu;dúmun.
dumun,dúmun→̌→ 2→n : 214vt.dún.dúmu;dúmun.
dúmuni,dúmuni( manger *nom d'action )
dumuni,dúmuni( manger *nom d'action )
dúmunibali,dúmunibali( nourrir PTCP.NEG )
dumunibali,dúmunibali( nourrir PTCP.NEG )
dúmunibaliya,dúmunibaliya( qui.ne.mange.pas [ nourrir PTCP.NEG ] *abstractif )
dumunibaliya,dúmunibaliya( qui.ne.mange.pas [ nourrir PTCP.NEG ] *abstractif )
dúmunibɔminɛn,dúmunibɔminɛn( action.de.manger [ manger *nom d'action ] sortir outils )
dumunibɔminɛn,dúmunibɔminɛn( action.de.manger [ manger *nom d'action ] sortir outils )
dumunibòminèn,dúmunibɔminɛn( action.de.manger [ manger *nom d'action ] sortir outils )
dúmuniden,dúmuniden( action.de.manger [ manger *nom d'action ] enfant )
dumuniden,dúmuniden( action.de.manger [ manger *nom d'action ] enfant )
dúmunidɔgɔ,dúmunidɔgɔ( action.de.manger [ manger *nom d'action ] désir )
dumunidɔgɔ,dúmunidɔgɔ( action.de.manger [ manger *nom d'action ] désir )
dumunidògò,dúmunidɔgɔ( action.de.manger [ manger *nom d'action ] désir )
dúmunifɛn,dúmunifɛn( action.de.manger [ manger *nom d'action ] chose )
dumunifɛn,dúmunifɛn( action.de.manger [ manger *nom d'action ] chose )
dumunifèn,dúmunifɛn( action.de.manger [ manger *nom d'action ] chose )
dúmunikɛbaliya,dúmunikɛbaliya( action.de.manger [ manger *nom d'action ] faire PTCP.NEG *abstractif )
dumunikɛbaliya,dúmunikɛbaliya( action.de.manger [ manger *nom d'action ] faire PTCP.NEG *abstractif )
dumunikèbaliya,dúmunikɛbaliya( action.de.manger [ manger *nom d'action ] faire PTCP.NEG *abstractif )
dúmunikɛla,dúmunikɛla( action.de.manger [ manger *nom d'action ] faire *agent permanent )
dumunikɛla,dúmunikɛla( action.de.manger [ manger *nom d'action ] faire *agent permanent )
dumunikèla,dúmunikɛla( action.de.manger [ manger *nom d'action ] faire *agent permanent )
dúmunikɛminɛn,dúmunikɛminɛn( action.de.manger [ manger *nom d'action ] faire outils )
dumunikɛminɛn,dúmunikɛminɛn( action.de.manger [ manger *nom d'action ] faire outils )
dumunikèminèn,dúmunikɛminɛn( action.de.manger [ manger *nom d'action ] faire outils )
dúmunikɛɲɔgɔn,dúmunikɛɲɔgɔn( action.de.manger [ manger *nom d'action ] faire *partenaire réciproque )
dumunikɛɲɔgɔn,dúmunikɛɲɔgɔn( action.de.manger [ manger *nom d'action ] faire *partenaire réciproque )
dumunikènyògòn,dúmunikɛɲɔgɔn( action.de.manger [ manger *nom d'action ] faire *partenaire réciproque )
dúmunimɔgɔ,dúmunimɔgɔ( action.de.manger [ manger *nom d'action ] homme )
dumunimɔgɔ,dúmunimɔgɔ( action.de.manger [ manger *nom d'action ] homme )
dumunimògò,dúmunimɔgɔ( action.de.manger [ manger *nom d'action ] homme )
dúmuniŋana,dúmuniŋana( action.de.manger [ manger *nom d'action ] champion )
dumuniŋana,dúmuniŋana( action.de.manger [ manger *nom d'action ] champion )
dúmunintanya,dúmunintanya( action.de.manger [ manger *nom d'action ] *privatif *abstractif )
dumunintanya,dúmunintanya( action.de.manger [ manger *nom d'action ] *privatif *abstractif )
dúmuniyɛlɛma,dúmuniyɛlɛma( action.de.manger [ manger *nom d'action ] changer )
dumuniyɛlɛma,dúmuniyɛlɛma( action.de.manger [ manger *nom d'action ] changer )
dumuniyèlèma,dúmuniyɛlɛma( action.de.manger [ manger *nom d'action ] changer )
dumuya,Dumuya→̌Dunbiya.Dunbuya;Dunmuya.
dún,dún→̌→ 1080→n : 227vt.dúmu;dúmun.
dun,dún→̌→ 1080→n : 227vt.dúmu;dúmun.
dùn,dùn→̌→ 36
dúɲa,dúɲa→̌díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
duɲa,dúɲa→̌díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dunya,dúɲa→̌díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dúnan,dúnan→̌→ 212dnán.
dunan,dúnan→̌→ 212dnán.
dúnanfana,Dúnanfana( étranger repas )
dunanfana,Dúnanfana( étranger repas )
dúnanjigin,dúnanjigin( étranger descendre )vt.dnánjigin.
dunanjigin,dúnanjigin( étranger descendre )vt.dnánjigin.
dúnanjiginso,dúnanjiginso( accueillir [ étranger descendre ] maison )dnánjiginso.
dunanjiginso,dúnanjiginso( accueillir [ étranger descendre ] maison )dnánjiginso.
dúnankɛ,dúnankɛ( étranger mâle )dnánkɛ.
dunankɛ,dúnankɛ( étranger mâle )dnánkɛ.
dunankè,dúnankɛ( étranger mâle )dnánkɛ.
dúnanmuso,dúnanmuso( étranger femme )dnánmuso.
dunanmuso,dúnanmuso( étranger femme )dnánmuso.
dúnannama,dúnannama( étranger *en tant que )dnánnama.
dunannama,dúnannama( étranger *en tant que )dnánnama.
dúnanya,dúnanya( étranger *abstractif )dnánya.
dunanya,dúnanya( étranger *abstractif )dnánya.
duna-pɛn,Duna-Pɛn→̌
duna-pèn,Duna-Pɛn→̌
dúnbali,dúnbali( manger PTCP.NEG )
dunbali,dúnbali( manger PTCP.NEG )
dunbiya,Dunbiya→̌Dunbuya;Dumuya;Dunmuya.
dunbuya,Dunbuya→̌Dunbiya.Dumuya;Dunmuya.
dúndala,dúndala( manger bouche à )
dundala,dúndala( manger bouche à )
dùndare,dùndare→̌→ 1Source :Fulfuldé dunndare 'despotique'.
dundare,dùndare→̌→ 1Source :Fulfuldé dunndare 'despotique'.
dúnden,dúnden→̌→ 9
dunden,dúnden→̌→ 9
dùnduguma,dùnduguma( terre *à )
dunduguma,dùnduguma( terre *à )
dúnfɛn,dúnfɛn( manger chose )
dunfɛn,dúnfɛn( manger chose )
dunfèn,dúnfɛn( manger chose )
dunfin,Dunfin→̌
dùnfin,dùnfin( profond noir )
dunfin,dùnfin( profond noir )
dùnforoko,dùnforoko( gâte-bois sac.en.peau )
dunforoko,dùnforoko( gâte-bois sac.en.peau )
dùngare,dùngare→̌→ 3dùgalen;dùgare;dùgaren;dùbalen;dùngaren.
dungare,dùngare→̌→ 3dùgalen;dùgare;dùgaren;dùbalen;dùngaren.
dùngaren,dùngaren→̌dùngare.dùgalen;dùgare;dùgaren;dùbalen;dùngaren.
dungaren,dùngaren→̌dùngare.dùgalen;dùgare;dùgaren;dùbalen;dùngaren.
dùnge,dùnge→̌→ 43Source :Soninké dúnkè 'originaire'.
dunge,dùnge→̌→ 43Source :Soninké dúnkè 'originaire'.
dùngɔ,dùngɔ→̌→ 28dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dungɔ,dùngɔ→̌→ 28dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dungò,dùngɔ→̌→ 28dɔ̀ngɔ;dɔ̀ngɔn;dɔ̀gɔn.
dùngɔna,dùngɔna( désir *mental1 )dɔ̀ngɔna.
dungɔna,dùngɔna( désir *mental1 )dɔ̀ngɔna.
dungòna,dùngɔna( désir *mental1 )dɔ̀ngɔna.
dúngùru,dúngùru→̌túnfùru.
dunguru,dúngùru→̌túnfùru.
dúniya,dúniya→̌→ 18díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
duniya,dúniya→̌→ 18díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dún-kà-fá,dún-kà-fá( manger *infinitif remplir )
dun-ka-fa,dún-kà-fá( manger *infinitif remplir )
dunmuya,Dunmuya→̌Dunbiya.Dunbuya;Dumuya.
dùnnenya,dùnnenya( courber *participe résultatif *abstractif )dùlenya.
dunnenya,dùnnenya( courber *participe résultatif *abstractif )dùlenya.
dún-ń-fɛ̀,dún-ń-fɛ̀( manger *je par )
dun-n-fɛ,dún-ń-fɛ̀( manger *je par )
dun-n-fè,dún-ń-fɛ̀( manger *je par )
dúnɔ,Dúnɔ→̌
dunɔ,Dúnɔ→̌
dunò,Dúnɔ→̌
dúnta,dúnta( manger *participe potentiel )
dunta,dúnta( manger *participe potentiel )
dúntanya,dúntanya( concession *privatif *abstractif )vt.
duntanya,dúntanya( concession *privatif *abstractif )vt.
dúntulu,dúntulu( manger huile )
duntulu,dúntulu( manger huile )
dunu,Dunu→̌
dùnu,dùnu→̌Voir entrée principale :dùmu.
dunu,dùnu→̌Voir entrée principale :dùmu.
dúnufɔla,dúnufɔla( tambour dire *agent permanent )Voir entrée principale :dùnunfɔla.
dunufɔla,dúnufɔla( tambour dire *agent permanent )Voir entrée principale :dùnunfɔla.
dunufòla,dúnufɔla( tambour dire *agent permanent )Voir entrée principale :dùnunfɔla.
dùnukàlan,dùnukàlan→̌dùnun-kàla.dùnunkàla;dùnunkàlan;dònikala.
dunukalan,dùnukàlan→̌dùnun-kàla.dùnunkàla;dùnunkàlan;dònikala.
dùnun,dùnun→̌→ 101dùnu.
dunun,dùnun→̌→ 101dùnu.
dúnuɲɛ,dúnuɲɛ→̌díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dunuɲɛ,dúnuɲɛ→̌díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dununyè,dúnuɲɛ→̌díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dùnunfɔla,dùnunfɔla( tambour dire *agent permanent )dúnufɔla.
dununfɔla,dùnunfɔla( tambour dire *agent permanent )dúnufɔla.
dununfòla,dùnunfɔla( tambour dire *agent permanent )dúnufɔla.
dùnunkàla,dùnunkàla→̌dùnun-kàla.dùnunkàla;dùnukàlan;dùnunkàlan;dònikala.
dununkala,dùnunkàla→̌dùnun-kàla.dùnunkàla;dùnukàlan;dùnunkàlan;dònikala.
dùnun-kàla,dùnun-kàla→̌dùnunkàla;dùnukàlan;dùnunkàlan;dònikala.
dunun-kala,dùnun-kàla→̌dùnunkàla;dùnukàlan;dùnunkàlan;dònikala.
dùnunkàlan,dùnunkàlan→̌dùnun-kàla.dùnunkàla;dùnukàlan;dònikala.
dununkalan,dùnunkàlan→̌dùnun-kàla.dùnunkàla;dùnukàlan;dònikala.
dùnunkɔrɔ,dùnunkɔrɔ( tambour dessous )
dununkɔrɔ,dùnunkɔrɔ( tambour dessous )
dununkòrò,dùnunkɔrɔ( tambour dessous )
dúnuya,dúnuya→̌→ 48díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dunuya,dúnuya→̌→ 48díɲɛ.díyɛn;jíɲɛ;jyɛ́n;dúnuɲɛ;dúɲa;dúniya;dúnuya.Source :Ar. dunya:
dùnya,dùnya( profond *abstractif )
dunya,dùnya( profond *abstractif )
dunyo,Dunyo→̌
dura,Dura→̌
dùru,dùru→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
duru,dùru→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
dùrugu,dùrugu→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
durugu,dùrugu→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
dùruku,dùruku→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
duruku,dùruku→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
dùruntu,dùruntu→̌→ 1
duruntu,dùruntu→̌→ 1
dùrunu,dùrunu→̌vt.dùuru.dùruntu;dùrunu.
durunu,dùrunu→̌vt.dùuru.dùruntu;dùrunu.
dùrusi,dùrusi→̌→ 8vt.Source :ar: dars / durus = étude(s).
durusi,dùrusi→̌→ 8vt.Source :ar: dars / durus = étude(s).
dúrututu,dúrututu→̌
durututu,dúrututu→̌
dúsɛbɛn,dúsɛbɛn( concession écrit )
dusɛbɛn,dúsɛbɛn( concession écrit )
dusèbèn,dúsɛbɛn( concession écrit )
dúsu,Dúsu→̌
dusu,Dúsu→̌
dùsu,dùsu→̌→ 135
dùsuba,dùsuba( se.fâcher *augmentatif )
dusuba,dùsuba( se.fâcher *augmentatif )
dùsubaya,dùsubaya( coléreux [ se.fâcher *augmentatif ] *abstractif )
dusubaya,dùsubaya( coléreux [ se.fâcher *augmentatif ] *abstractif )
dùsubɔ,dùsubɔ( coeur sortir )
dusubɔ,dùsubɔ( coeur sortir )
dusubò,dùsubɔ( coeur sortir )
dùsudimi,dùsudimi( coeur souffrance )
dusudimi,dùsudimi( coeur souffrance )
dùsufaga,dùsufaga( coeur tuer )
dusufaga,dùsufaga( coeur tuer )
dùsugɛlɛnya,dùsugɛlɛnya( coeur difficile *abstractif )
dusugɛlɛnya,dùsugɛlɛnya( coeur difficile *abstractif )
dusugèlènya,dùsugɛlɛnya( coeur difficile *abstractif )
dùsugonitigi,dùsugonitigi( coeur chaud maître )
dusugonitigi,dùsugonitigi( coeur chaud maître )
dùsuja,dùsuja( coeur sécheresse )
dusuja,dùsuja( coeur sécheresse )
dùsujɛlenya,dùsujɛlenya( coeur blanc *participe résultatif *abstractif )
dusujɛlenya,dùsujɛlenya( coeur blanc *participe résultatif *abstractif )
dusujèlenya,dùsujɛlenya( coeur blanc *participe résultatif *abstractif )
dùsukasi,dùsukasi( coeur pleurs )dùsukasiko.
dusukasi,dùsukasi( coeur pleurs )dùsukasiko.
dùsukasibaatɔ,dùsukasibaatɔ( chagriner [ coeur pleurer ] *agent occasionnel *statif )
dusukasibaatɔ,dùsukasibaatɔ( chagriner [ coeur pleurer ] *agent occasionnel *statif )
dusukasibaatò,dùsukasibaatɔ( chagriner [ coeur pleurer ] *agent occasionnel *statif )
dùsukasiko,dùsukasiko( coeur pleurs affaire )Voir entrée principale :dùsukasi.
dusukasiko,dùsukasiko( coeur pleurs affaire )Voir entrée principale :dùsukasi.
dùsukasimɔgɔ,dùsukasimɔgɔ( chagrin [ coeur pleurs ] homme )
dusukasimɔgɔ,dùsukasimɔgɔ( chagrin [ coeur pleurs ] homme )
dusukasimògò,dùsukasimɔgɔ( chagrin [ coeur pleurs ] homme )
dùsukolo,dùsukolo( coeur os )
dusukolo,dùsukolo( coeur os )
dùsukun,dùsukun( coeur tête )
dusukun,dùsukun( coeur tête )
dùsukundimi,dùsukundimi( coeur [ coeur tête ] souffrance )
dusukundimi,dùsukundimi( coeur [ coeur tête ] souffrance )
dùsukungɛlɛya,dùsukungɛlɛya( coeur [ coeur tête ] dureté [ dur *en verbe dynamique ] )
dusukungɛlɛya,dùsukungɛlɛya( coeur [ coeur tête ] dureté [ dur *en verbe dynamique ] )
dusukungèlèya,dùsukungɛlɛya( coeur [ coeur tête ] dureté [ dur *en verbe dynamique ] )
dùsukunjɛlenya,dùsukunjɛlenya( coeur [ coeur tête ] blanchir *participe résultatif *abstractif )
dusukunjɛlenya,dùsukunjɛlenya( coeur [ coeur tête ] blanchir *participe résultatif *abstractif )
dusukunjèlenya,dùsukunjɛlenya( coeur [ coeur tête ] blanchir *participe résultatif *abstractif )
dùsukunnakaliya,dùsukunnakaliya( coeur [ coeur tête ] *nom de lieu douleur.aigüe )
dusukunnakaliya,dùsukunnakaliya( coeur [ coeur tête ] *nom de lieu douleur.aigüe )
dùsukunnako,dùsukunnako( coeur [ coeur tête ] *nom de lieu affaire )
dusukunnako,dùsukunnako( coeur [ coeur tête ] *nom de lieu affaire )
dùsukunnata,dùsukunnata( coeur [ coeur tête ] *mental2 )
dusukunnata,dùsukunnata( coeur [ coeur tête ] *mental2 )
dùsukunntan,dùsukunntan( coeur [ coeur tête ] *privatif )
dusukunntan,dùsukunntan( coeur [ coeur tête ] *privatif )
dùsukunntanya,dùsukunntanya( coeur [ coeur tête ] *privatif *abstractif )
dusukunntanya,dùsukunntanya( coeur [ coeur tête ] *privatif *abstractif )
dùsukunɲugu,dùsukunɲugu( coeur [ coeur tête ] nausée )dùsukunɲugun.dùsukunɲugu.
dusukunɲugu,dùsukunɲugu( coeur [ coeur tête ] nausée )dùsukunɲugun.dùsukunɲugu.
dusukunnyugu,dùsukunɲugu( coeur [ coeur tête ] nausée )dùsukunɲugun.dùsukunɲugu.
dùsukunɲugun,dùsukunɲugun( coeur [ coeur tête ] nausée )dùsukunɲugu.
dusukunɲugun,dùsukunɲugun( coeur [ coeur tête ] nausée )dùsukunɲugu.
dusukunnyugun,dùsukunɲugun( coeur [ coeur tête ] nausée )dùsukunɲugu.
dùsukunyɛrɛyɛrɛ,dùsukunyɛrɛyɛrɛ( coeur [ coeur tête ] trembler )
dusukunyɛrɛyɛrɛ,dùsukunyɛrɛyɛrɛ( coeur [ coeur tête ] trembler )
dusukunyèrèyèrè,dùsukunyɛrɛyɛrɛ( coeur [ coeur tête ] trembler )
dùsulafiliba,dùsulafiliba( coeur *nom de lieu erreur *augmentatif )
dusulafiliba,dùsulafiliba( coeur *nom de lieu erreur *augmentatif )
dùsulaminkuma,dùsulaminkuma( coeur faire.boire [ *causatif boire ] parole )
dusulaminkuma,dùsulaminkuma( coeur faire.boire [ *causatif boire ] parole )
dùsuman,dùsuman( coeur *connecteur )
dusuman,dùsuman( coeur *connecteur )
dùsumandi,dùsumandi( humeur [ coeur *connecteur ] agréable )
dusumandi,dùsumandi( humeur [ coeur *connecteur ] agréable )
dùsumandiya,dùsumandiya( affable [ humeur [ coeur *connecteur ] agréable ] *abstractif )
dusumandiya,dùsumandiya( affable [ humeur [ coeur *connecteur ] agréable ] *abstractif )
dùsumango,dùsumango( humeur [ coeur *connecteur ] désagréable )
dusumango,dùsumango( humeur [ coeur *connecteur ] désagréable )
dùsumangoya,dùsumangoya( irascible [ humeur [ coeur *connecteur ] désagréable ] *abstractif )
dusumangoya,dùsumangoya( irascible [ humeur [ coeur *connecteur ] désagréable ] *abstractif )
dùsuntan,dùsuntan( coeur *privatif )
dusuntan,dùsuntan( coeur *privatif )
dùsuɲugu,dùsuɲugu( coeur nausée )dùsuɲugun.dùsuɲugu.
dusuɲugu,dùsuɲugu( coeur nausée )dùsuɲugun.dùsuɲugu.
dusunyugu,dùsuɲugu( coeur nausée )dùsuɲugun.dùsuɲugu.
dùsuɲugun,dùsuɲugun( coeur nausée )dùsuɲugu.
dusuɲugun,dùsuɲugun( coeur nausée )dùsuɲugu.
dusunyugun,dùsuɲugun( coeur nausée )dùsuɲugu.
dùte,dùte→̌→ 8te;dùtɛ;jùte;jùtɛ.
dute,dùte→̌→ 8te;dùtɛ;jùte;jùtɛ.
dùtɛ,dùtɛ→̌dùte.te;dùtɛ;jùte;jùtɛ.
dutɛ,dùtɛ→̌dùte.te;dùtɛ;jùte;jùtɛ.
dutè,dùtɛ→̌dùte.te;dùtɛ;jùte;jùtɛ.
dùtebin,dùtebin( thé.vert herbe )dítebin;bíndute.
dutebin,dùtebin( thé.vert herbe )dítebin;bíndute.
dútigi,dútigi( concession maître )
dutigi,dútigi( concession maître )
dùuli,dùuli→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
duuli,dùuli→̌dùuru.dùli;dùuli;dùru;dùruku;dùrugu.
dúumɛ,"dúumɛ→̌→ 31→n : 3dúumi.Ar. dawm 'longue durée, permanence'"
duumɛ,"dúumɛ→̌→ 31→n : 3dúumi.Ar. dawm 'longue durée, permanence'"
duumè,"dúumɛ→̌→ 31→n : 3dúumi.Ar. dawm 'longue durée, permanence'"
dúumi,"dúumi→̌→n : 3dúumɛ.Source :Ar. dawm 'longue durée, permanence'."
duumi,"dúumi→̌→n : 3dúumɛ.Source :Ar. dawm 'longue durée, permanence'."
dúuru,dúuru→̌→ 579
duuru,dúuru→̌→ 579
dùuru,dùuru→̌dùli;dùuli;dùru;dùruku;dùrugu.
dúurunan,dúurunan( cinq *ordinal )5nan.
duurunan,dúurunan( cinq *ordinal )5nan.
dúurunin,dúurunin( cinq *diminutif )
duurunin,dúurunin( cinq *diminutif )
dùwa,dùwa→̌→ 5dùga.dùba;dùfa;dùbaa.ar: du`a' = invocation
duwa,dùwa→̌→ 5dùga.dùba;dùfa;dùbaa.ar: du`a' = invocation
duwaɲɛ,duwaɲɛ→̌→ 2duwayɛn.
duwanyè,duwaɲɛ→̌→ 2duwayɛn.
dùwansí,Dùwansí→̌Sisigo.Voir entrée principale :Dukansi.Dukansi;Dugansi.(originaires de Wuluma (Nord de Kayes). Forgerons (tagu).)
duwansi,Dùwansí→̌Sisigo.Voir entrée principale :Dukansi.Dukansi;Dugansi.(originaires de Wuluma (Nord de Kayes). Forgerons (tagu).)
dúwanzà,Dúwanzà→̌Dúwazà;Dúwazàn.
duwanza,Dúwanzà→̌Dúwazà;Dúwazàn.
dùwawu,dùwawu→̌dùgawu.dùbabu;dùwawu.
duwawu,dùwawu→̌dùgawu.dùbabu;dùwawu.
duwayɛn,duwayɛn→̌duwaɲɛ.duwayɛn.
duwayèn,duwayɛn→̌duwaɲɛ.duwayɛn.
dúwazà,Dúwazà→̌Dúwanzà.Dúwazàn.
duwaza,Dúwazà→̌Dúwanzà.Dúwazàn.
dúwazàn,Dúwazàn→̌Dúwanzà.Dúwazà.
duwazan,Dúwazàn→̌Dúwanzà.Dúwazà.
dwa,dwa→̌dɔ́gɔ.lɔ́gɔ;nɔ́gɔ;lɔ́gɔ;dwa;jwa.
dwá,dwá→̌dɔ́gɔ.lɔ́gɔ;dwá;jwá.
dwa,dwá→̌dɔ́gɔ.lɔ́gɔ;dwá;jwá.
dwáden,dwáden( marché enfant )dɔ́gɔden.dwáden;jwáden.
dwaden,dwáden( marché enfant )dɔ́gɔden.dwáden;jwáden.
dwáfurancɛ,dwáfurancɛ( marché distance [ distance milieu ] )dɔ́gɔfurancɛ.dwáfurancɛ.
dwafurancɛ,dwáfurancɛ( marché distance [ distance milieu ] )dɔ́gɔfurancɛ.dwáfurancɛ.
dwafurancè,dwáfurancɛ( marché distance [ distance milieu ] )dɔ́gɔfurancɛ.dwáfurancɛ.
dwákɛ,dwákɛ( cadet mâle )dɔ́gɔkɛ.dwákɛ;jwákɛ.
dwakɛ,dwákɛ( cadet mâle )dɔ́gɔkɛ.dwákɛ;jwákɛ.
dwakè,dwákɛ( cadet mâle )dɔ́gɔkɛ.dwákɛ;jwákɛ.
dwákun,dwákun( marché tête )dɔ́gɔkun.dwákun;jwákun.
dwakun,dwákun( marché tête )dɔ́gɔkun.dwákun;jwákun.
dwámuso,dwámuso( cadet femme )dɔ́gɔmuso.dwámuso;jwámuso.
dwamuso,dwámuso( cadet femme )dɔ́gɔmuso.dwámuso;jwámuso.
dwánin,dwánin( cadet *diminutif )dɔ́gɔnin.dwánin;jwánin.
dwanin,dwánin( cadet *diminutif )dɔ́gɔnin.dwánin;jwánin.
dwáɲinina,dwáɲinina( fagot chercher *agent permanent )dɔ́gɔɲinina.dwáɲinina;jwáɲinina.
dwaɲinina,dwáɲinina( fagot chercher *agent permanent )dɔ́gɔɲinina.dwáɲinina;jwáɲinina.
dwanyinina,dwáɲinina( fagot chercher *agent permanent )dɔ́gɔɲinina.dwáɲinina;jwáɲinina.
dwásiri,dwásiri( fagot lier )dɔ́gɔsiri.dwásiri;jwásiri.
dwasiri,dwásiri( fagot lier )dɔ́gɔsiri.dwásiri;jwásiri.
dwáya,dwáya( étroit *en verbe dynamique )dɔ́gɔya.dwáya;jwáya.
dwaya,dwáya( étroit *en verbe dynamique )dɔ́gɔya.dwáya;jwáya.
dwáyama,dwáyama( petitesse [ étroit *en verbe dynamique ] *comme de )dɔ́gɔyama.dwáyama;jwáyama.
dwayama,dwáyama( petitesse [ étroit *en verbe dynamique ] *comme de )dɔ́gɔyama.dwáyama;jwáyama.
d',d'→̌→n : 10dá.d'.

"""

# Expression régulière pour extraire les composants
pattern = re.compile(
    r"(?P<bambara1>[^,]+),(?P<bambara2>[^\(]+)\( (?P<francais>[^\)]+) \)(?P<transcription1>[^\.]+)\.(?P<transcription2>[^\.]+)\."
)

entries = []
for line in raw_data.strip().split('\n'):
    match = pattern.match(line)
    if match:
        entries.append({
            "bambara_1": match.group("bambara1").strip(),
            "bambara_2": match.group("bambara2").strip(),
            "francais": match.group("francais").strip(),
            "transcription_1": match.group("transcription1").strip(),
            "transcription_2": match.group("transcription2").strip(),
        })

# Export en CSV
with open('bambara_clean.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=entries[0].keys())
    writer.writeheader()
    writer.writerows(entries)

print(f"Données nettoyées sauvegardées dans 'bambara_clean.csv'.")