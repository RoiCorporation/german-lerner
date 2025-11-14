#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random;



#_________________________________________________________________________________________________________________________#


# lists


# colores
colores = {'negro/-a': 'schwarz', 'rojo/-a': 'rot', 'amarillo/-a': 'gelb', 'azul oscuro/-a': 'dunkelblau', 'azul': 'blau',
           'azul claro/-a': 'hellblau', 'marrón': 'braun', 'violeta': 'violett', 'rosa': 'rosa', 'naranja': 'orange',
           'verde oscuro/-a': 'dunkelgrün', 'verde': 'grün', 'verde claro/-a': 'hellgrün', 'turquesa': 'türkis',
           'gris': 'grau', 'blanco/-a': 'weiß', 'beige': 'beige', 'plateado/-a': 'silbern', 'dorado/-a': 'golden'};


# meses y estaciones
dias_meses_y_estaciones = {'el día, -es': 'der Tag, die Tage', 'el lunes': 'der Montag', 'el martes': 'der Dienstag',
                           'el miércoles': 'der Mittwoch', 'el jueves': 'der Donnerstag', 'el viernes': 'der Freitag',
                           'el sábado': 'der Samstag', 'el domingo': 'der Sonntag', 'enero': 'Januar', 'febrero': 'Februar',
                           'marzo': 'März', 'abril': 'April', 'mayo': 'Mai', 'junio': 'Juni', 'julio': 'Juli',
                           'agosto': 'August', 'septiembre': 'September', 'octubre': 'Oktober', 'noviembre': 'November',
                           'diciembre': 'Dezember', 'la primavera': 'der Frühling', 'el verano': 'der Sommer',
                           'el otoño': 'der Herbst', 'el invierno': 'der Winter', 'el mes, -es': 'der Monat, die Monate',
                           'la estación del año, -es': 'die Jahreszeit, die Jahreszeiten'};


# partes de la cara
partes_de_la_cara = {'la cabeza, -s': 'der Kopf, die Köpfe', 'la cara, -s': 'das Gesicht, die Gesichter',
                     'la oreja, -s': 'das Ohr, die Ohren', 'la nariz, -es': 'die Nase, die Nasen',
                     'el cabello, -s': 'das Haar, die Haare', 'la frente, -s': 'die Stirn, die Stirnen',
                     'el cuello, -s': 'der Hals, die Hälse', 'la mandíbula, -s': 'der Kiefer, die Kiefer',
                     'la boca, -s': 'der Mund, die Münder', 'el labio, -s': 'die Lippe, die Lippen',
                     'la lengua, -s': 'die Zunge, die Zungen', 'el diente, -s': 'der Zahn, die Zähne',
                     'la mejilla, -s(1)': 'die Wange, die Wangen', 'la mejilla, -s(2)': 'die Backe, die Backen',
                     'la barbilla, -s': 'das Kinn, die Kinne', 'la barba, -s': 'der Bart, die Bärte',
                     'el ojo, -s': 'das Auge, die Augen', 'el párpado, -s': 'das Augenlid, die Augenlider',
                     'la pupila, -s': 'die Pupille, die Pupillen', 'el iris, -es': 'die Regenbogenhaut, die Regenbogenhäute',
                     'la pestaña, -s': 'die Wimper, die Wimpern', 'la ceja, -s': 'die Augenbraue, die Augenbrauen'};


# medios de transporte
medios_de_transporte = {'el avión, -es': 'das Flugzeug, die Flugzeuge', 'el helicóptero, -s': 'der Hubschrauber, die Hubschrauber',
                        'la bicicleta, -s': 'das Fahrrad, die Fahrräder', 'el coche, -s': 'das Auto, die Autos',
                        'el carruaje, -s': 'die Kutsche, die Kutschen', 'el bus, -es': 'der Bus, die Busse',
                        'el globo aerostático, -s': 'der Heißluftballon, die Heißluftballons',
                        'la motocicleta, -s': 'das Motorrad, die Motorräder', 'el scooter, -s': 'der Motorroller, die Motorroller',
                        'el tractor, -es': 'der Traktor, die Traktoren', 'el camión, -es': 'der Lastwagen, die Lastwägen',
                        'el taxi, -s': 'das Taxi, die Taxis', 'el tren, -es(1)': 'die Bahn, die Bahnen',
                        'el tren, -es(2)': 'der Zug, die Züge', 'el metro, -s': 'die U-Bahn, die U-Bahnen',
                        'el tren metropolitano, -es': 'die S-Bahn, die S-Bahnen', 'el tranvía, -s': 'die Straßenbahn, die Straßenbahnen',
                        'el teleférico, -s': 'die Seilbahn, die Seilbahnen', 'el barco, -s': 'das Schiff, die Schiffe',
                        'el bote, -s': 'das Boot, die Boote', 'la ambulancia, -s': 'der Krankenwagen, die Krankenwägen',
                        'el sumergible, -s': 'das Tauchboot, die Tauchboote', 'el submarino, -s': 'das U-Boot, die U-Boote'};


# ropa
ropa = {'los pantalones vaqueros': 'die Jeans', 'la falda, -s': 'der Rock, die Röcke', 'la camisa, -s': 'das Hemd, die Hemden',
        'el abrigo, -s': 'der Mantel, die Mäntel', 'la camiseta, -s': 'das T-Shirt, die T-Shirts',
        'la blusa, -s': 'die Bluse, die Blusen', 'la chaqueta, -s': 'die Jacke, die Jacken',
        'el chaleco, -s': 'die Weste, die Westen', 'el jersey, -s': 'der Pullover, die Pullover',
        'el impermeable, -s(1)': 'der Regenmantel, die Regenmäntel', 'el impermeable, -s(2)': 'die Regenjacke, die Regenjacken',
        'el traje, -s': 'der Anzug, die Anzüge', 'el vestido, -s': 'das Kleid, die Kleider',
        'el chándal, -es': 'der Trainingsanzug, die Trainingsanzüge', 'el pijama, -s': 'der Pyjama, die Pyjamas',
        'el pantalón, -es': 'die Hose, die Hosen', 'el pantalón corto': 'die kurze Hose', 'la ropa interior, -s': 'die Unterhose, die Unterhosen',
        'la camiseta interior, -s': 'das Unterhemd, die Unterhemden', 'el zapato, -s': 'der Schuh, die Schuhe',
        'el zapato deportivo, -s': 'der Turnschuh, die Turnschuhe', 'la zapatilla de casa, -s': 'der Hausschuh, die Hausschuhe',
        'la chancleta, -s': 'der Badeschuh, die Badeschuhe', 'el zapato de tacón, -s': 'der Stöckelschuh, die Stöckelschuhe',
        'la sandalia, -s': 'die Sandale, die Sandalen', 'el gorro, -s': 'die Mütze, die Mützen', 'el sombrero, -s': 'der Hut, die Hüte',
        'la bufanda, -s': 'der Schal, die Schals', 'la corbata, -s': 'die Krawatte, die Krawatten', 'el cinturón, -es': 'der Gürtel, die Gürtel',
        'el guante, -s': 'der Handschuh, die Handschuhe', 'el calcetín, -es': 'die Socke, die Socken',
        'el bañador, -es': 'der Badeanzug, die Badeanzüge'};


# partes del cuerpo humano
partes_del_cuerpo_humano = {'la cabeza, -s': 'der Kopf, die Köpfe', 'el cuello, -s': 'der Hals, die Hälse',
                            'la nuca, -s': 'der Nacken, die Nacken', 'el hombro, -s': 'die Schulter, die Schultern',
                            'la espalda, -s': 'der Rücken, die Rücken', 'el pecho, -s': 'die Brust, die Brüste',
                            'la columna vertebral, -es': 'die Wirbelsäule, die Wirbelsäulen', 'la barriga, -s': 'der Bauch, die Bäuche',
                            'el brazo, -s': 'der Arm, die Arme', 'la mano, -s': 'die Hand, die Hände', 'la cadera, -s': 'die Hüfte, die Hüften',
                            'la nalga, -s': 'das Gesäß, die Gesäße', 'la pierna, -s': 'das Bein, die Beine', 'la rodilla, -s': 'das Knie, die Knie',
                            'el pie, -s': 'der Fuß, die Füße', 'el hueso, -s': 'der Knochen, die Knochen', 'el músculo, -s': 'der Muskel, die Muskeln',
                            'la articulación, -es': 'das Gelenk, die Gelenke', 'el pulmón, -es': 'die Lunge, die Lungen',
                            'el corazón, -es': 'das Herz, die Herzen', 'el cerebro, -s': 'das Gehirn, die Gehirne', 'la costilla, -s': 'die Rippe, die Rippen',
                            'el estómago, -s': 'der Magen, die Mägen', 'el hígado, -s': 'die Leber, die Lebern', 'el intestino, -s': 'der Darm, die Därme',
                            'el riñón, -es': 'die Niere, die Nieren', 'el codo, -s': 'der Ellbogen, die Ellbogen',
                            'la muñeca, -s': 'das Handgelenk, die Handgelenke', 'el tobillo, -s': 'der Knöchel, die Knöchel'};


# animales
animales = {'el perro, -s': 'der Hund, die Hunde', 'la perra, -s': 'die Hündin, die Hündinnen',
            'el gato, -s': 'der Kater, die Kater', 'la gata, -s': 'die Katze, die Katzen',
            'el ratón, -es': 'die Maus, die Mäuse', 'la rata, -s': 'die Ratte, die Ratten', 'la liebre, -s': 'der Hase, die Hasen',
            'el conejo, -s': 'das Kaninchen, die Kaninchen', 'el zorro, -s': 'der Fuchs, die Füchse', 'la zorra, -s': 'die Füchsin, die Füchsinnen',
            'el lobo, -s': 'der Wolf, die Wölfe', 'la loba, -s': 'die Wölfin, die Wölfe', 'el cerdo, -s': 'das Schwein, die Schweine',
            'la oveja, -s': 'das Schaf, die Schafe', 'la cabra, -s': 'die Ziege, die Ziegen', 'la vaca, -s': 'die Kuh, die Kühe',
            'el burro, -s': 'der Esel, die Esel', 'la burra, -s': 'die Eselin, die Eselinnen',
            'el toro, -s': 'der Stier, die Stiere', 'el caballo, -s': 'das Pferd, die Pferde', 'la yegua, -s': 'die Stute, die Stuten',
            'el mono, -s': 'der Affe, die Affen', 'la mona, -s': 'die Äffin, die Äffinnen', 'el elefante, -s': 'der Elefant, die Elefanten',
            'la jirafa, -s': 'die Giraffe, die Giraffen', 'el león, -es': 'der Löwe, die Löwen', 'la leona, -s': 'die Löwin, die Löwinnen',
            'el tigre, -s': 'der Tiger, die Tiger', 'la tigresa, -s': 'die Tigerin, die Tigerinnen', 'el oso, -s': 'der Bär, die Bären',
            'la osa, -s': 'die Bärin, die Bärinnen', 'el pingüino, -s': 'der Pinguin, die Pinguine',
            'el cocodrilo, -s': 'das Krokodil, die Krokodile', 'la serpiente, -s': 'die Schlange, die Schlangen',
            'el pez, -es': 'der Fisch, die Fische', 'el tiburón, -es': 'der Hai, die Haie', 'el pulpo, -s': 'der Krake, die Kraken',
            'el calamar, -es': 'der Tintenfisch, die Tintenfische', 'el cangrejo, -s': 'der Krebs, die Krebse',
            'la tortuga, -s': 'die Schildkröte, die Schildkröten', 'el delfín, -es': 'der Delphin, die Delphine',
            'el gallo, -s': 'der Hahn, die Hähne', 'la gallina, -s': 'das Huhn, die Hühner', 'el pájaro, -s': 'der Vogel, die Vögel',
            'el águila, -s': 'der Adler, die Adler', 'la paloma, -s': 'die Taube, die Tauben', 'el cuervo, -s': 'der Rabe, die Raben',
            'la mosca, -s': 'die Fliege, die Fliegen', 'la abeja, -s': 'die Biene, die Bienen', 'la avispa, -s': 'die Wespe, die Wespen',
            'la hormiga, -s': 'die Ameise, die Ameisen', 'la araña, -s': 'die Spinne, die Spinnen',
            'el ciervo, -s': 'der Hirsch, die Hirsche', 'la cierva, -s': 'die Hirschkuh, die Hirschkühe',
            'la ardilla, -s': 'das Eichhörnchen, die Eichhörnchen', 'el murciélago, -s': 'die Fledermaus, die Fledermäuse',
            'la gaviota, -s': 'die Möwe, die Möwen', 'el gusano, -s': 'der Wurm, die Würmer',
            'el rinoceronte, -s': 'das Nashorn, die Nashörner', 'el caracol, -es': 'die Schnecke, die Schnecken',
            'el mosquito, -s': 'die Mücke, die Mücken', 'el lagarto, -s': 'die Echse, die Echsen'};


# deportes
deportes = {'el bádminton': 'das Badminton', 'el béisbol': 'der/das Baseball', 'el baloncesto': 'der Basketball',
            'los bolos': 'der Kegel / das Bowling', 'el ciclismo': 'der Radsport', 'el fútbol': 'der Fußball',
            'el golf': 'das Golf', 'la gimnasia': 'das Turnen', 'montar a caballo': 'reiten',
            'el hockey sobre hielo': 'das Eishockey', 'el remo': 'das Rudern',
            'esquiar': 'das Schifahren / das Skifahren', 'la natación': 'das Schwimmen', 'el tenis': 'das Tennis',
            'el tenis de mesa': 'das Tischtennis', 'el voleibol': 'der/das Volleyball', 'el waterpolo': 'der Wasserball',
            'navegar a vela': 'segeln', 'el paracaidismo': 'das Fallschirmspringen', 'el buceo': 'das Tauchen',
            'el judo': 'das Judo', 'el karate': 'das Karate', 'el taekwondo': 'das Taekwondo',
            'el jugador, -es': 'der Spieler, die Spieler', 'la jugadora, -s': 'die Spielerin, die Spielerinnen',
            'la pelota, -s(1)': 'der Ball, die Bälle', 'la pelota, -s(2)': 'der Spielball, die Spielbälle',
            'el balón, -es': 'der Ball, die Bälle'};


# familia
familia = {'el hermano, -s(neutro)': 'das Geschwister, die Geschwister', 'el hermano, -s': 'der Bruder, die Brüder',
           'la hermana, -s': 'die Schwester, die Schwestern', 'los padres(progenitores)': 'die Eltern', 'el padre, -s': 'der Vater, die Väter',
           'la madre, -s': 'die Mutter, die Mütter', 'los abuelos(progenitores)': 'die Großeltern',
           'el abuelo, -s(formal)': 'der Großvater, die Großväter', 'el abuelo, -s(informal)': 'der Opa, die Opas',
           'la abuela, -s(formal)': 'die Großmutter, die Großmütter', 'la abuela, -s(informal)': 'die Oma, die Omas',
           'los bisabuelos(progenitores)': 'die Urgroßeltern', 'el bisabuelo, -s': 'der Urgroßvater, die Urgroßväter',
           'la bisabuela, -s': 'die Urgroßmutter, die Urgroßmütter', 'el tatarabuelo, -s': 'der Ururgroßvater, die Ururgroßväter',
           'la tatarabuela, -s': 'die Ururgroßmutter, die Ururgroßmütter', 'el tío, -s': 'der Onkel, die Onkel',
           'la tía, -s': 'die Tante, die Tanten', 'el primo, -s': 'der Cousin, die Cousins',
           'la prima, -s': 'die Cousine, die Cousinen', 'el cuñado, -s': 'der Schwager, die Schwäger',
           'la cuñada, -s': 'die Schwägerin, die Schwägerinnen', 'el hijo, -s(descendientes)': 'das Kind, die Kinder',
           'el hijo, -s': 'der Sohn, die Söhne', 'la hija, -s': 'die Tochter, die Töchter',
           'el sobrino, -s': 'der Neffe, die Neffen', 'la sobrina, -s': 'die Nichte, die Nichten',
           'el nieto, -s': 'der Enkel, die Enkel', 'la nieta, -s': 'die Enkelin, die Enkelinnen',
           'el bisnieto, -s': 'der Urenkel, die Urenkel', 'la bisnieta, -s': 'die Urenkelin, die Urenkelinnen',
           'el prometido, -s': 'der Verlobte, die Verlobten', 'la prometida, -s': 'die Verlobte, die Verlobten',
           'el nieto, -s(descendientes)': 'das Enkelkind, die Enkelkinder',
           'el bisnieto, -s(decendientes)': 'das Urenkelkind, die Urenkelkinder', 'el matrimonio, -s': 'die Ehe, die Ehen',
           'el esposo, -s(1)': 'der Ehemann, die Ehemänner', 'la esposa, -s(1)': 'die Ehefrau, die Ehefrauen',
           'el esposo, -s(2)': 'der Gatte, die Gatten', 'la esposa, -s(2)': 'die Gattin, die Gattinnen',
           'el pariente, -s': 'der Verwandte, die Verwandten', 'la parienta, -s': 'die Verwandte, die Verwandten',
           'el padrastro, -s': 'der Stiefvater, die Stiefväter', 'la madrastra, -s': 'die Stiefmutter, die Stiefmütter',
           'el hermanastro, -s': 'der Stiefbruder, die Stiefbrüder', 'la hermanastra, -s': 'die Stiefschwester, die Stiefschwestern',
           'el hijastro, -s': 'der Stiefsohn, die Stiefsöhne', 'la hijastra, -s': 'die Stieftochter, die Stieftöchter'};


# partes de la casa
partes_de_la_casa = {"la habitación, -es(1)": "das Zimmer, die Zimmer", "la habitación, -es(2)": "der Raum, die Räume",
                     "la sala de estar, -s": "das Wohnzimmer, die Wohnzimmer",
                     "el dormitorio, -s": "das Schlafzimmer, die Schlafzimmer", "el baño, -s(1)": "das Badezimmer, die Badezimmer",
                     "el baño, -s(2)": "das Bad, die Bäder", "el cuarto de estudio, -s": "das Arbeitszimmer, die Arbeitszimmer",
                     "la cocina, -s": "die Küche, die Küchen", "el cuarto, -s": "die Kammer, die Kammern",
                     "la cámara, -s": "die Kammer, die Kammern", "el sótano, -s": "der Keller, die Keller",
                     "la despensa, -s": "die Speisekammer, die Speisekammern", "el desván, -es(1)": "der Dachboden, die Dachböden",
                     "el desván, -es(2)": "die Dachkammer, die Dachkammern", "el garaje, -s": "die Garage, die Garagen",
                     "el balcón, -es": "der Balkon, die Balkons", "la terraza, -s": "die Terrasse, die Terrassen",
                     "el jardín, -es": "der Garten, die Gärten", "el techo, -s": "das Dach, die Dächer",
                     "el tejado, -s": "das Dach, die Dächer", "el suelo, -s(1)": "der Grund, die Gründe",
                     "el suelo, -s(2)": "der Boden, die Böden", "la pared, -es": "die Wand, die Wände",
                     "el pasillo, -s": "der Flur, die Flure", "la escalera, -s": "die Treppe, die Treppen",
                     "el ascensor, -es": "der Fahrstuhl, die Fahrstühle"};


# profesiones
profesiones = {"el electricista, -a": "der Elektriker, die Elektrikerin", "el jardinero, -a": "der Gärtner, die Gärtnerin",
               "el mecánico, -a": "der Automechaniker, die Automechanikerin",
               "el conductor de autobus, -a": "der Busfahrer, die Busfahrerin", "el peluquero, -a": "der Friseur, die Friseurin",
               "el trabajador de carreteras, -a": "der Straßenarbeiter, die Straßenarbeiterin",
               "el panadero, -a": "der Bäcker, die Bäckerin", "el albañil, -a": "der Maurer, die Maurerin",
               "el campesino, -a": "der Landwirt, die Landwirtin", "el fotógrafo, -a": "der Fotograf, die Fotografin",
               "el pintor, -a": "der Maler, die Malerin", "el arquitecto, -a": "der Architekt, die Architektin",
               "el profesor, -a": "der Lehrer, die Lehrerin", "el cocinero, -a": "der Koch, die Köchin",
               "el basurero, -a": "der Müllwerker, die Müllwerkerin", "el carnicero, -a": "der Metzger, die Metzgerin",
               "el camarero, -a": "der Kellner, die Kellnerin", "el dentista, -a": "der Zahnarzt, die Zahnärztin",
               "el dependiente, -a": "der Verkäufer, die Verkäuferin", "el actor, -iz": "der Schauspieler, die Schauspielerin",
               "el artista, -a": "der Künstler, die Künstlerin", "el obrero, -a": "der Bauarbeiter, die Bauarbeiterin",
               "el médico, -a": "der Arzt, die Ärztin", "el ingeniero, -a": "der Ingenieur, die Ingenieurin",
               "el bombero, -a": "der Feuerwehrmann, die Feuerwehrfrau", "el pastelero, -a": "der Konditor, die Konditorin",
               "la ama de casa": "die Hausfrau", "el enfermero, -a": "der Krankenpfleger, die Krankenpflegerin",
               "el piloto, -a (de avión)": "der Flugzeugpilot, die Flugzeugpilotin",
               "el policía, -a": "der Polizist, die Polizistin", "el cartero, -a": "der Briefträger, die Briefträgerin",
               "el secretario, -a": "der Sekretär, die Sekretärin", "el cantante, -a": "der Sänger, die Sängerin",
               "el veterinario, -a": "der Tierarzt, die Tierärztin", "el soldado, -a": "der Soldat, die Soldatin",
               "el carpintero, -a": "der Tischler, die Tischlerin",
               "el hombre de negocios, -a": "der Geschäftsmann, die Geschäftsfrau",
               "el detective, -a": "der Detektiv, die Detektivin", "el fontanero, -a": "der Klempner, die Klempnerin",
               "el cirujano, -a": "der Chirurg, die Chirurgin", "el escritor, -a": "der Schriftsteller, die Schriftstellerin",
               "el empleado de gasolinera": "der Tankwart", "el agente secreto, -a": "der Geheimagent, die Geheimagentin",
               "el abogado, -a": "der Rechtsanwalt, die Rechtsanwältin", "el juez, -a": "der Richter, die Richterin",
               "el periodista, -a": "der Journalist, die Journalistin", "la mujer de la limpieza": "die Putzfrau",
               "el cajero, -a": "der Kassierer, die Kassiererin", "el pescador, -a": "der Fischer, die Fischerin"};

 
# ciudad
ciudad = {"la calle, -s": "die Straße, die Straßen", "el cruce, -s": "die Kreuzung, die Kreuzungen", "el semáforo, -s": "die Ampel, die Ampeln",
         "el paso de peatones, -s": "der Zebrastreifen, die Zebrastreifen", "la plaza, -s": "der Platz, die Plätze",
         "el parking, -es": "der Parkplatz, die Parkplätze", "la casa, -s": "das Haus, die Häuser",
         "el piso, -s": "die Wohnung, die Wohnungen", "el edificio, -s": "das Gebäude, die Gebäude",
         "el ayuntamiento, -s": "das Rathaus, die Rathäuser", "el hospital, -es": "das Krankenhaus, die Krankenhäuser",
         "la estación de tren, -es": "der Bahnhof, die Bahnhöfe", "la iglesia, -s": "die Kirche, die Kirchen",
         "el estadio, -s": "das Stadion, die Stadien", "el lugar / el puesto, -s": "die Stelle, die Stellen",
         "la gasolinera, -s": "die Tankstelle, die Tankstellen", "la farmacia, -s": "die Apotheke, die Apotheken",
         "el puerto, -s": "der Hafen, die Häfen", "el aeropuerto, -s": "der Flughafen, die Flughäfen",
         "la tienda, -s(1)": "das Geschäft, die Geschäfte", "la tienda, -s(2)": "der Laden, die Läden",
         "el supermercado, -s": "der Supermarkt, die Supermärkte", "la panadería, -s": "die Bäckerei, die Bäckereien",
         "la carnicería, -s(1)": "die Metzgerei, die Metzgereien", "la carnicería, -s(2)": "die Fleischerei, die Fleischereien",
         "la pescadería, -s": "das Fischgeschäft, die Fischgeschäfte", "la frutería": "der Obst- und Gemüseladen",
         "la catedral, -es": "der Dom, die Dome", "el cine, -es": "das Kino, die Kinos", "el teatro, -s": "das Theater, die Theater",
         "la piscina, -s": "das Schwimmbad, die Schwimmbäder", "el centro comercial, -es(1)": "das Einkaufszentrum, die Einkaufszentren",
         "el centro comercial, -es(2)": "das Geschäftszentrum, die Geschäftszentren", "el banco, -s": "die Bank, die Banken",
         "el gimnasio, -s": "das Fitnessstudio, die Fitnessstudios", "la biblioteca, -s": 'die Bibliothek, die Bibliotheken',
         "el barrio, -s": "die Nachbarschaft, die Nachbarschaften", "el colegio, -s": "die Schule, die Schulen",      
         "el instituto de secundaria, -s": "die Gesamtschule, die Gesamtschulen",
         "la universidad, -es": "die Universität, die Universitäten", "la facultad, -es": "die Fakultät, die Fakultäten",
         "la guardería, -s": "der Kindergarten, die Kindergärten", "el hotel, -es": "das Hotel, die Hotels",
         "el parque": "der Park", "el tráfico, s": "der Verkehr, die Verkehre",
         "la señal de tráfico, -s": "das Verkehrszeichen, die Verkehrszeichen", "el paseo, -s": "die Promenade, die Promenaden",
         "el paseo marítimo, -s": "die Strandpromenade, die Strandpromenaden", "el carril bici, -s": "der Radweg, die Radwege",
         "el rascacielos, -s(1)": "das Hochhaus, die Hochhäuser", "el rascacielos, -s(2)": "der Wolkenkratzer, die Wolkenkratzer",
         "la avenida, -s": "die Allee, die Alleen", "la presa, -s": "das Stauwerk, die Stauwerke",
         "la cárcel, -es(1)": "das Gefängnis, die Gefängnisse", "la cárcel, -es(2)": "der Kerker, die Kerker"};


# paisaje
paisaje = {'la montaña, -s(1)': 'der Berg, die Berge', 'la montaña, -s(2)': 'das Gebirge, die Gebirge',
           'la cordillera, -s(1)': 'die Bergkette, die Bergketten', 'la cordillera, -s(2)': 'die Gebirgskette, die Gebirgsketten',
           'el valle, -s': 'das Tal, die Täler', 'el río, -s': 'der Fluss, die Flüsse', 'el afluente, -s': 'der Nebenfluss, die Nebenflüsse',
           'la costa, -s': 'die Küste, die Küsten', 'el acantilado, -s(1)': 'das Kliff, die Kliffe',
           'el acantilado, -s(2)': 'die Steilküste, die Steilküsten', 'el mar(1)': 'die See', 'el mar, -es(2)': 'das Meer, die Meere',
           'el lago, -s': 'der See, die Seen', 'la playa, -s': 'der Strand, die Strände', 'la tierra, -s': 'das Land, die Länder',
           'la llanura, -s': 'das Flachland, die Flachländer', 'el túnel, -es': 'der Tunnel, die Tunnel',
           'el puente, -s': 'die Brücke, die Brücken', 'el pueblo, -s / la aldea, -s': 'das Dorf, die Dörfer',
           'el castillo, -s(1)': 'das Schloss, die Schlösser', 'el castillo, -s(2)': 'die Burg, die Burgen',
           'la mina, -s': 'das Bergwerk, die Bergwerke', 'la cueva, -s': 'die Höhle, die Höhlen',
           'el árbol, -es': 'der Baum, die Bäume', 'el bosque, -s': 'der Wald, die Wälder',
           'el precipicio, -s': 'der Abgrund, die Abgründe', 'el volcán, -es': 'der Vulkan, die Vulkane',
           'el camino, -s': 'der Weg, die Wege'};


# frutas y verduras
frutas_y_verduras = {'la fruta, -s(1)': 'die Frucht, die Früchte', 'la fruta(2)': 'das Obst',
                     'la manzana, -s': 'der Apfel, die Äpfel', 'la pera, -s': 'die Birne, die Birnen',
                     'el plátano, -s': 'die Banane, die Bananen', 'la uva, -s': 'die Traube, die Trauben',
                     'la fresa, -s': 'die Erdbeere, die Erdbeeren', 'la naranja, -s(1)': 'die Apfelsine, die Apfelsinen',
                     'la naranja, -s(2)': 'die Orange, die Orangen', 'la cereza, -s': 'die Kirsche, die Kirschen',
                     'la mora, -s': 'die Brombeere, die Brombeeren', 'la baya, -s': 'die Beere, die Beeren',
                     'la piña, -s': 'die Ananas, die Ananas', 'la mandarina, -s': 'die Mandarine, die Mandarinen',
                     'el kiwi, -s': 'die Kiwi, die Kiwis', 'la verdura, -s': 'das Gemüse, die Gemüse',
                     'la lechuga, -s': 'der Salat, die Salate', 'el tomate, -s': 'die Tomate, die Tomaten',
                     'la patata, -s': 'die Kartoffel, die Kartoffeln', 'la cebolla, -s': 'die Zwiebel, die Zwiebeln',
                     'la zanahoria, -s': 'die Karotte, die Karotten', 'el pimiento, -s': 'der/die Paprika, die Paprikas',
                     'el brocoli, -s': 'der Broccoli, die Broccolis', 'la coliflor, -s': 'der Blumenkohl, die Blumenkohle',
                     'la berenjena, -s': 'die Aubergine, die Auberginen', 'el ajo': 'der Knoblauch',
                     'la calabaza, -s': "der Kürbis, die Kürbisse", 'el melón, -es': 'die Melone, die Melonen',
                     'la sandía, -s': 'die Wassermelone, die Wassermelonen', 'la nuez, -es(1)': 'die Nuss, die Nüsse',
                     'la nuez, -es(2)': 'die Walnuss, die Walnüsse', 'el cacahuete, -es': 'die Erdnuss, die Erdnüsse',
                     'la almendra, -s': 'die Mandel, die Mandeln', 'la castaña, -s(1)': 'die Kastanie, die Kastanien',
                     'la castaña, -s(2)': 'die Marone, die Maronen', 'el guisante, -s': 'die Erbse, die Erbsen',
                     'el limón, -es': 'die Zitrone, die Zitronen', 'la judía, -s': 'die Bohne, die Bohnen',
                     'la seta, -s': 'der Pilz, die Pilze', 'el champiñón, -es': 'der Champignon, die Champignons'};


# mobiliario
mobiliario = {'el mueble, -s': 'das Möbel, die Möbel', 'la puerta, -s': 'die Tür, die Türen', 'la silla, -s': 'der Stuhl, die Stühle',
              'el sillón, -es': 'der Sessel, die Sessel', 'el sofá, -s': 'das Sofa, die Sofas', 'la cama, -s': 'das Bett, die Betten',
              'la mesa, -s': 'der Tisch, die Tische', 'la mesilla de noche, -s': 'der Nachttisch, die Nachttische',
              'el escritorio, -s': 'der Schreibtisch, die Schreibtische', 'la estantería, -s(1)': 'das Regal, die Regale',
              'la estantería, -s(2)': 'das Bücherregal, die Bücherregale', 'el ordenador, -es': 'der Computer, die Computer',
              'la bañera, -s': 'die Badewanne, die Badewannen', 'el vater, -es': 'die Toilette, die Toiletten',
              'el espejo, -s': 'der Spiegel, die Spiegel', 'la toalla, -s(1)': 'das Handtuch, die Handtücher',
              'la toalla, -s(2)': 'das Badetuch, die Badetücher', 'el armario, -s': 'der Schrank, die Schränke',
              'el horno, -s': 'der Ofen, die Öfen', 'el microondas, -s': 'die Mikrowelle, die Mikrowellen',
              'la cocina(fogones), -s': 'der Herd, die Herde', 'la nevera, -s': 'der Kühlschrank, die Kühlschränke',
              'el congelador, -es(1)': 'der Gefrierschrank, die Gefrierschränke', 'el congelador, -es(2)': 'das Gefrierfach, die Gefrierfächer',
              'el fregadero, -s': 'das Spülbecken, die Spülbecken', 'el lavavajillas, -s': 'die Spülmaschine, die Spülmaschinen',
              'la lavadora, -s': 'die Waschmaschine, die Waschmaschinen', 'la chimenea, -s': 'der Kamin, die Kamine',
              'el reloj de pared, -es': 'die Wanduhr, die Wanduhren', 'la ventana, -s': 'das Fenster, die Fenster',
              'la televisión': 'das Fernsehen', 'la alfombra, -s': 'der Teppich, die Teppiche'};


# colegio
colegio = {'el aula, -s': 'das Klassenzimmer, die Klassenzimmer', 'el encerado, -s': 'die Tafel, die Tafeln',
              'la tiza, -s': 'die Tafelkreide, die Tafelkreiden', 'la papelera, -s': 'der Papierkorb, die Papierkörbe',
              'el estuche, -s(1)': 'das Etui, die Etuis', 'el estuche, -s(2)': 'das Mäppchen, die Mäppchen',
              'la mochila, -s(1)': 'der Rucksack, die Rucksäcke', 'la mochila, -s(2)': 'der Ranzen, die Ranzen',
              'la mochila, -s(3)': 'der Schulranzen, die Schulranzen', 'el libro, -s': 'das Buch, die Bücher',
              'el libro de texto, -s': 'das Schulbuch, die Schulbücher', 'el cuaderno, -s(1)': 'das Notizbuch, die Notizbücher',
              'el cuaderno, -s(2)': 'das Heft, die Hefte', 'el lápiz, -es': 'der Bleistift, die Bleistifte',
              'el bolígrafo, -s(1)': 'der Kugelschreiber, die Kugelschreiber', 'el bolígrafo, -s(2)': 'der Kuli, die Kulis',
              'el afilalápiz, -es': 'der Bleistiftspitzer, die Bleistiftspitzer',
              'la goma de borrar, -s': 'der/das Radiergummi, die Radiergummis', 'el rotulador, -es': 'der Filzstift, die Filzstifte',
              'el papel, -es': 'das Papier, die Papiere', 'la regla, -s': 'das Lineal, die Lineale',
              'el celo, -s': 'das Klebeband, die Klebebänder', 'la tijera, -s': 'die Schere, die Scheren',
              'los deberes': 'die Hausaufgaben', 'el horario, -s': 'der Stundenplan, die Stundenpläne',
              'el apunte, -s': 'die Notiz, die Notizen'};


# salud
salud = {'la herida, -s(1)': 'die Wunde, die Wunden', 'la herida, -s(2)': 'die Verletzung, die Verletzungen',
         'el golpe, -s(1)': 'der Schlag, die Schläge', 'el golpe, -s(2)': 'der Anschlag, die Anschläge',
         'el esguince, -s': 'die Verstauchung, die Verstauchungen', 'la lesión, -es': 'die Verletzung, die Verletzungen',
         'el accidente, -s': 'der Unfall, die Unfälle', 'la urgencia, -s': 'die Dringlichkeit, die Dringlichkeiten',
         'la enfermedad, -es': 'die Krankheit, die Krankheiten', 'el dolor, -es': 'der Schmerz, die Schmerzen',
         'el seguro, -s': 'die Versicherung, die Versicherungen', 'el medicamento, -s': 'das Medikament, die Medikamente',
         'la pastilla, -s': 'die Tablette, die Tabletten', 'la alergia, -s': 'die Allergie, die Allergien',
         'la gripe, -s': 'die Grippe, die Grippen', 'la fiebre, -s': 'das Fieber, die Fieber',
         'la vacuna, -s': 'die Impfung, die Impfungen', 'la inyección, -es(1)': 'die Injektion, die Injektionen',
         'la inyección, -es(2)': 'die Einspritzung, die Einspritzungen', 'el resfriado, -s': 'die Erkältung, die Erkältungen',
         'la infección, -es': 'die Infektion, die Infektionen', 'el virus, -es': 'der/das Virus, die Viren'};


# tiempo
tiempo = {'soleado': 'sonnig', 'nublado(1)': 'bewölkt', 'nublado(2)': 'wolkig', 'lluvioso': 'regnerisch',
          'ventoso': 'windig', 'mojado': 'nass', 'seco': 'trocken', 'húmedo': 'feucht', 'nebuloso': 'neblig',
          'caluroso(1)': 'warm', 'caluroso(2)': 'heiß', 'frío': 'kalt', 'templado': 'mild',
          'la temperatura, -s': 'die Temperatur, die Temperaturen', 'el calor(1)': 'die Wärme',
          'el calor(2)': 'die Hitze', 'el frío': 'die Kälte', 'el sol, -es': 'die Sonne, die Sonnen',
          'la niebla, -s': 'der Nebel, die Nebel', 'la lluvia, -s': 'der Regen, die Regen', 'la gota, -s': 'der Tropfen, die Tropfen',
          'el granizo': 'der Hagel', 'los granos de granizo': 'die Graupeln', 'la nieve': 'der Schnee',
          'el copo de nieve, -s': 'die Schneeflocke, die Schneeflocken', 'la nube, -s': 'die Wolke, die Wolken',
          'el viento, -s': 'der Wind, die Winde', 'la tormenta, -s': 'das Gewitter, die Gewitter',
          'el temporal, -es': 'der Sturm, die Stürme', 'la helada, -s': 'der Frost, die Fröste'};



#_________________________________________________________________________________________________________________________#


#code


general_input = input("¡Bienvenido al repasador de alemán!\n\n"
                     
                     "¿Qué quieres hacer hoy?\n\n"
                      
                      "Repasar vocabulario ---> Pulse 1\n"
                      
                      "Exponer las listas de vocabulario ---> Pulse 2\n"
                     
                     );



if general_input == "1":


    vocab_input = input("¿Qué vocabulario quieres repasar?\n\n"
                        
                          "Verbos/acciones ---> die Verben  :  Pulse 1\n"
                        
                          "Preposiciones, conjunciones y conectores ---> Präpositionen, Konjunktionen und Konnektoren  :  Pulse 2\n"
                        
                          "Vocabulario misceláneo ---> Vermischt Wortschatz  :  Pulse 3\n"
                       
                          "Los colores ---> die Farben  :  Pulse 4\n"

                          "Los días, meses y estaciones del año ---> die Jahreszeiten und die Monate  :  Pulse 5\n"

                          "Las partes de la cara ---> das Gesicht  :  Pulse 6\n"

                          "Los medios de transporte ---> die Transportmittel  :  Pulse 7\n"

                          "La ropa ---> die Kleider  :  Pulse 8\n"

                          "Las partes del cuerpo humano ---> der Körper  :  Pulse 9\n"

                          "Los animales ---> die Tiere  :  Pulse 10\n"
                        
                          "Los deportes ---> die Sporte  :  Pulse 11\n"
                        
                          "La familia ---> die Familie  :  Pulse 12\n"
                        
                          "Las partes de la casa ---> das Haus  :  Pulse 13\n"
                        
                          "Las profesiones ---> die Berufe  :  Pulse 14\n"
                        
                          "La ciudad ---> die Stadt  :  Pulse 15\n"
                        
                          "El paisaje ---> die Landschaft  :  Pulse 16\n"
                        
                          "Las frutas y verduras ---> das Obst und Gemüse  :  Pulse 17\n"
                        
                          "El mobiliario ---> das Mobiliar  :  Pulse 18\n"
                        
                          "El colegio ---> die Schule  :  Pulse 19\n"
                        
                          "La salud ---> die Gesundheit  :  Pulse 20\n"
                        
                          "El tiempo ---> das Wetter  :  Pulse 21\n"

                         );


    print("\n");



    ###########################################################################################################################    
    
    def lerner(word_dictionary):

        sorted_word_dictionary = sorted(word_dictionary)
        lista_auxiliar_word_dictionary = []
        resultado_word_dictionary = ""


        while sorted_word_dictionary != lista_auxiliar_word_dictionary:
            índice_aleatorio_word_dictionary = random.randint(0, len(sorted_word_dictionary) - 1)
            elemento_aleatorio_word_dictionary = sorted_word_dictionary[índice_aleatorio_word_dictionary]
            if elemento_aleatorio_word_dictionary in lista_auxiliar_word_dictionary:
                continue

            else:
                lista_auxiliar_word_dictionary.insert(índice_aleatorio_word_dictionary, elemento_aleatorio_word_dictionary)
                resultado_word_dictionary = input(elemento_aleatorio_word_dictionary + " -----> ")
                if word_dictionary[sorted_word_dictionary[índice_aleatorio_word_dictionary]] == resultado_word_dictionary:
                    print("Correcto!", "\n", sorted_word_dictionary[índice_aleatorio_word_dictionary], " ----> ", word_dictionary[sorted_word_dictionary[índice_aleatorio_word_dictionary]], "\n\n")
                else:
                    print("Incorrecto!", "\n", sorted_word_dictionary[índice_aleatorio_word_dictionary], " ----> ", word_dictionary[sorted_word_dictionary[índice_aleatorio_word_dictionary]], "\n\n")
 
    
    
    ###########################################################################################################################
    
    if vocab_input == "4":
        lerner(colores)
    
    elif vocab_input == "5":
        lerner(dias_meses_y_estaciones)
    
    elif vocab_input == "6":
        lerner(partes_de_la_cara)
    
    elif vocab_input == "7":
        lerner(medios_de_transporte)
    
    elif vocab_input == "8":
        lerner(ropa)
    
    elif vocab_input == "9":
        lerner(partes_del_cuerpo_humano)
    
    elif vocab_input == "10":
        lerner(animales)
    
    elif vocab_input == "11":
        lerner(deportes)
    
    elif vocab_input == "12":
        lerner(familia)
    
    elif vocab_input == "13":
        lerner(partes_de_la_casa)
    
    elif vocab_input == "14":
        lerner(profesiones)
    
    elif vocab_input == "15":
        lerner(ciudad)
    
    elif vocab_input == "16":
        lerner(paisaje)
    
    elif vocab_input == "17":
        lerner(frutas_y_verduras)
    
    elif vocab_input == "18":
        lerner(mobiliario)
        
    elif vocab_input == "19":
        lerner(colegio)
        
    elif vocab_input == "20":
        lerner(salud)
        
    elif vocab_input == "21":
        lerner(tiempo)



#_________________________________________________________________________________________________________________________#


elif general_input == "2":
    
    lists_input = input("¿Qué listas de vocabulario quieres exponer?\n\n"
                        
                          "Verbos/acciones ---> die Verben  :  Pulse 1\n"
                        
                          "Preposiciones, conjunciones y conectores ---> Präpositionen, Konjunktionen und Konnektoren  :  Pulse 2\n"
                        
                          "Vocabulario misceláneo ---> Vermischt Wortschatz  :  Pulse 3\n"
                       
                          "Los colores ---> die Farben  :  Pulse 4\n"

                          "Los días, meses y estaciones del año ---> die Jahreszeiten und die Monate  :  Pulse 5\n"

                          "Las partes de la cara ---> das Gesicht  :  Pulse 6\n"

                          "Los medios de transporte ---> die Transportmittel  :  Pulse 7\n"

                          "La ropa ---> die Kleider  :  Pulse 8\n"

                          "Las partes del cuerpo humano ---> der Körper  :  Pulse 9\n"

                          "Los animales ---> die Tiere  :  Pulse 10\n"
                        
                          "Los deportes ---> die Sporte  :  Pulse 11\n"
                        
                          "La familia ---> die Familie  :  Pulse 12\n"
                        
                          "Las partes de la casa ---> das Haus  :  Pulse 13\n"
                        
                          "Las profesiones ---> die Berufe  :  Pulse 14\n"
                        
                          "La ciudad ---> die Stadt  :  Pulse 15\n"
                        
                          "El paisaje ---> die Landschaft  :  Pulse 16\n"
                        
                          "Las frutas y verduras ---> das Obst und Gemüse  :  Pulse 17\n"
                        
                          "El mobiliario ---> das Mobiliar  :  Pulse 18\n"
                        
                          "El colegio ---> die Schule  :  Pulse 19\n"
                        
                          "La salud ---> die Gesundheit  :  Pulse 20\n"
                        
                          "El tiempo ---> das Wetter  :  Pulse 21\n"

                         );
    
    
    print ("\n");
    
    
    
    ###########################################################################################################################
        
    def show(word_dictionary):

        max_len_word_dictionary = 0;

        for element in word_dictionary:
            if len(element) > max_len_word_dictionary:
                max_len_word_dictionary = len(element)

        for element in word_dictionary:
            print(element, (max_len_word_dictionary - len(element)) * " ", "         ", word_dictionary[element])            

        
    
    ###########################################################################################################################

    if lists_input == "4":
        show(colores)
    
    elif lists_input == "5":
        show(dias_meses_y_estaciones)
    
    elif lists_input == "6":
        show(partes_de_la_cara)
    
    elif lists_input == "7":
        show(medios_de_transporte)
    
    elif lists_input == "8":
        show(ropa)
    
    elif lists_input == "9":
        show(partes_del_cuerpo_humano)
    
    elif lists_input == "10":
        show(animales)
    
    elif lists_input == "11":
        show(deportes)
    
    elif lists_input == "12":
        show(familia)
    
    elif lists_input == "13":
        show(partes_de_la_casa)
    
    elif lists_input == "14":
        show(profesiones)
    
    elif lists_input == "15":
        show(ciudad)
    
    elif lists_input == "16":
        show(paisaje)
    
    elif lists_input == "17":
        show(frutas_y_verduras)
    
    elif lists_input == "18":
        show(mobiliario)
        
    elif lists_input == "19":
        show(colegio)
        
    elif lists_input == "20":
        show(salud)
        
    elif lists_input == "21":
        show(tiempo)

