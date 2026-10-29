# Contenido de la demo Hotel Oasis (Cordoba) (es/ca/en/fr). Hechos de hoteloasiscordoba.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación Doble/Matrimonial','Triple y Cuádruple','Junior Suite y Habitación romántica'],'ca':['Habitació Doble/Matrimonial','Triple i Quàdruple','Junior Suite i Habitació romàntica'],'en':['Double room','Triple and Quadruple','Junior Suite and Romantic room'],'fr':['Chambre double','Triple et Quadruple','Junior Suite et Chambre romantique']}
RD={
'es':['Dos camas individuales o una de 1,50 m, baño completo con secador, TV, wifi y caja fuerte. También para uso individual.','Habitaciones de 18 m² para familias: la triple con cama de 1,50 m y una individual; la cuádruple con cuatro camas individuales y terraza.','La Junior Suite (hasta 3 personas, terraza privada de 6 m²) y la romántica, con cama redonda King Size y balcón.'],
'ca':['Dos llits individuals o un d\'1,50 m, bany complet amb assecador, TV, wifi i caixa forta. També per a ús individual.','Habitacions de 18 m² per a famílies: la triple amb llit d\'1,50 m i un d\'individual; la quàdruple amb quatre llits individuals i terrassa.','La Junior Suite (fins a 3 persones, terrassa privada de 6 m²) i la romàntica, amb llit rodó King Size i balcó.'],
'en':['Two single beds or one 1.50 m bed, full bathroom with hairdryer, TV, wifi and safe. Also for single use.','18 m² family rooms: the triple with a 1.50 m bed plus a single; the quadruple with four single beds and a terrace.','The Junior Suite (up to 3 people, 6 m² private terrace) and the romantic room, with a round King Size bed and balcony.'],
'fr':['Deux lits simples ou un lit de 1,50 m, salle de bain complète avec sèche-cheveux, TV, wifi et coffre-fort. Aussi en usage individuel.','Chambres familiales de 18 m² : la triple avec un lit de 1,50 m et un lit simple ; la quadruple avec quatre lits simples et une terrasse.','La Junior Suite (jusqu\'à 3 personnes, terrasse privée de 6 m²) et la chambre romantique, avec lit rond King Size et balcon.']}
ART={
'hero':('waves',9501,['#6b3a1f','#f3c58a','#f9e3bf','#2f7387','#6b3a1f','#3f220f']),
'intro':('skyline',9502,['#6b3a1f','#e8a865','#f7d8a5','#1c5262','#174452','#0f2f39']),
'r1':('columns',9511,['#edf1f2','#f6f8f9','#c4793c','#6b3a1f','#3f220f']),
'r2':('arches',9512,['#f2ebe0','#e5bf8d','#c27238','#6b3a1f','#3f220f']),
'r3':('hills',9513,['#e6eef0','#f2ecd6','#f0c27f','#a9c2a4','#7fa28a','#567a68']),
'g1':('waves',9521,['#235f71','#f0c184','#f7e0b9','#33788c','#235f71','#153e4a']),
'g2':('columns',9522,['#ebeff1','#f5f7f8','#c1763a','#6b3a1f','#3f220f']),
'g3':('skyline',9523,['#6b3a1f','#e6a561','#f6d6a1','#1b505f','#16424f','#0e2d37']),
'g4':('arches',9524,['#f1e9dd','#e2bb88','#bf6f35','#6b3a1f','#3f220f']),
'g5':('hills',9525,['#e4ecef','#f0e9d2','#eebf7b','#a6bf9f','#7c9f86','#537764']),
'g6':('waves',9526,['#1d5767','#efbe80','#f6ddb5','#2d7084','#1d5767','#123843'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Oasis Córdoba · Hotel con piscina y parking gratuito',see_rooms='Ver habitaciones',hero_k='Córdoba',hero_t='Su oasis con piscina en Córdoba',hero_s='Parking gratuito incluido en todas las reservas, recepción 24 horas y el Restaurante Axares de cocina cordobesa.',
 intro_t='Llegar y olvidarse del coche',intro_p1='El parking es gratuito e incluido en todas las reservas, y la Mezquita-Catedral está a 25 minutos a pie.',
 intro_p2='Piscina exterior de uso gratuito para los huéspedes, wifi gratuito en habitaciones y zonas comunes y caja fuerte gratuita en cada habitación.',
 stats=['Parking gratuito','Piscina exterior','Recepción 24 horas','Restaurante Axares'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Dobles, triples, cuádruples y suites. Check-in desde las 12:30 y check-out hasta las 12:00.',
 svcs=['Parking gratuito','Piscina exterior','Recepción 24 horas','Restaurante Axares','Wifi gratuito','Caja fuerte en cada habitación','Mascotas pequeñas bienvenidas','Cuna disponible'],
 loc_p='Avda. de Cádiz, 78 · 14013 Córdoba. A 25 minutos a pie de la Mezquita-Catedral.',
 chips=['¿Qué habitaciones tiene?','¿Tiene parking?','¿Tiene piscina?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Oasis Córdoba · Hotel amb piscina i pàrquing gratuït',see_rooms='Veure habitacions',hero_k='Còrdova',hero_t='El seu oasi amb piscina a Còrdova',hero_s='Pàrquing gratuït inclòs a totes les reserves, recepció 24 hores i el Restaurant Axares de cuina cordovesa.',
 intro_t='Arribar i oblidar-se del cotxe',intro_p1='El pàrquing és gratuït i inclòs a totes les reserves, i la Mesquita-Catedral és a 25 minuts a peu.',
 intro_p2='Piscina exterior d\'ús gratuït per als hostes, wifi gratuït a habitacions i zones comunes i caixa forta gratuïta a cada habitació.',
 stats=['Pàrquing gratuït','Piscina exterior','Recepció 24 hores','Restaurant Axares'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Dobles, triples, quàdruples i suites. Check-in des de les 12:30 i check-out fins a les 12:00.',
 svcs=['Pàrquing gratuït','Piscina exterior','Recepció 24 hores','Restaurant Axares','Wifi gratuït','Caixa forta a cada habitació','Mascotes petites benvingudes','Bressol disponible'],
 loc_p='Avda. de Cádiz, 78 · 14013 Còrdova. A 25 minuts a peu de la Mesquita-Catedral.',
 chips=['Quines habitacions té?','Té pàrquing?','Té piscina?','Com es reserva?']),
'en':dict(title='Hotel Oasis Córdoba · Hotel with pool and free parking',see_rooms='See the rooms',hero_k='Córdoba',hero_t='Your oasis with a pool in Córdoba',hero_s='Free parking included in every booking, 24-hour reception and the Axares Restaurant serving Cordoban cuisine.',
 intro_t='Arrive and forget about the car',intro_p1='Parking is free and included in every booking, and the Mosque-Cathedral is a 25-minute walk away.',
 intro_p2='Outdoor pool free for guests, free wifi in rooms and common areas and a free safe in every room.',
 stats=['Free parking','Outdoor pool','24-hour reception','Axares Restaurant'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Doubles, triples, quadruples and suites. Check-in from 12:30 and check-out until 12:00.',
 svcs=['Free parking','Outdoor pool','24-hour reception','Axares Restaurant','Free wifi','Safe in every room','Small pets welcome','Cot available'],
 loc_p='Avda. de Cádiz, 78 · 14013 Córdoba. A 25-minute walk from the Mosque-Cathedral.',
 chips=['What rooms does it have?','Is there parking?','Is there a pool?','How do I book?']),
'fr':dict(title='Hotel Oasis Córdoba · Hôtel avec piscine et parking gratuit',see_rooms='Voir les chambres',hero_k='Cordoue',hero_t='Votre oasis avec piscine à Cordoue',hero_s='Parking gratuit inclus dans toutes les réservations, réception 24 h/24 et le Restaurant Axares de cuisine cordouane.',
 intro_t='Arriver et oublier la voiture',intro_p1='Le parking est gratuit et inclus dans toutes les réservations, et la Mosquée-Cathédrale est à 25 minutes à pied.',
 intro_p2='Piscine extérieure gratuite pour les clients, wifi gratuit dans les chambres et les parties communes et coffre-fort gratuit dans chaque chambre.',
 stats=['Parking gratuit','Piscine extérieure','Réception 24 h/24','Restaurant Axares'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Doubles, triples, quadruples et suites. Arrivée à partir de 12h30 et départ jusqu\'à 12h00.',
 svcs=['Parking gratuit','Piscine extérieure','Réception 24 h/24','Restaurant Axares','Wifi gratuit','Coffre-fort dans chaque chambre','Petits animaux bienvenus','Lit bébé disponible'],
 loc_p='Avda. de Cádiz, 78 · 14013 Cordoue. À 25 minutes à pied de la Mosquée-Cathédrale.',
 chips=['Quelles chambres a-t-il ?','Y a-t-il un parking ?','Y a-t-il une piscine ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RU='https://reservations.verticalbooking.com/premium/index.html?id_albergo=28519&dc=9206&lingua_int=esp&id_stile=21657'
BOOK=dict(mode='engine',url={'es':RU,'ca':RU,'en':RU,'fr':RU})
D=dict(name='Hotel Oasis Córdoba',ac='#6b3a1f',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='Avda. de Cádiz, 78 · 14013 Córdoba',phones=['+34 957 29 83 11'],emails=['reservas@oasiscordoba.com'],maps='Hotel Oasis, Avenida de Cádiz 78, Córdoba',t=T)
META=dict(repo='demo-hotel-oasis-cordoba',name='Hotel Oasis Córdoba',legal_name='Hotel Oasis, S.L.',registry_ids=['CIF B14061626','Registro Mercantil de Córdoba'],
 url='https://hoteloasiscordoba.com/',domain='hoteloasiscordoba.com',municipality='Córdoba',province='Córdoba',sector='hotel con piscina, parking gratuito y restaurante en Córdoba',
 read_at='2026-10-29T13:14:00+01:00',created_at='2026-10-29T13:14:00+01:00',built_at='2026-10-29T13:25:00+01:00',audit_date='2026-10-29T11:08:00+01:00',
 rating=dict(value=4.2,coincide=['telefono'],date='2026-10-29T11:07:00+01:00',url='https://www.google.com/maps/place/Hotel+Oasis+C%C3%B3rdoba/@37.8646771,-4.7831465,17z/data=!4m9!3m8!1s0xd6d2093c5af2de3:0xa4d4013c57c9293c!5m2!4m1!1i2!8m2!3d37.8646771!4d-4.7831465!16s%2Fg%2F1v3gt7zv'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor real del hotel (Vertical Booking, el mismo enlace de su boton RESERVAR, en espanol porque la web no enlaza otras variantes); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Tiene habitaciones para familias?','K02'),('¿Cuál es la habitación romántica?','K03'),('¿Dónde está?','K04'),('¿Tiene parking?','K05'),('¿Tiene piscina?','K06'),('¿Tiene restaurante?','K07'),('¿Admiten mascotas?','K08'),('¿A qué hora es el check-in?','K09'),('¿Tienen cuna?','K10'),('¿Cómo reservo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11'),('¿Tienen spa?',None),('¿Hay traslado al aeropuerto?',None)],
'ca':[('Quines habitacions té?','K01'),('Té habitacions per a famílies?','K02'),('Quina és l\'habitació romàntica?','K03'),('On és?','K04'),('Té pàrquing?','K05'),('Té piscina?','K06'),('Té restaurant?','K07'),('Admeteu mascotes?','K08'),('A quina hora és el check-in?','K09'),('Teniu bressol?','K10'),('Com reservo?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11'),('Teniu spa?',None),('Hi ha trasllat a l\'aeroport?',None)],
'en':[('What rooms does it have?','K01'),('Are there family rooms?','K02'),('What is the romantic room?','K03'),('Where is it?','K04'),('Is there parking?','K05'),('Is there a pool?','K06'),('Is there a restaurant?','K07'),('Are pets allowed?','K08'),('What time is check-in?','K09'),('Do you have a cot?','K10'),('How do I book?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11'),('Do you have a spa?',None),('Is there an airport shuttle?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Y a-t-il des chambres familiales ?','K02'),('Quelle est la chambre romantique ?','K03'),('Où est-il ?','K04'),('Y a-t-il un parking ?','K05'),('Y a-t-il une piscine ?','K06'),('Y a-t-il un restaurant ?','K07'),('Les animaux sont-ils admis ?','K08'),('À quelle heure est l\'arrivée ?','K09'),('Avez-vous un lit bébé ?','K10'),('Comment réserver ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11'),('Avez-vous un spa ?',None),('Y a-t-il une navette aéroport ?',None)]}
