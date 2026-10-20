T = []

def add(name, lines, vocab, extra, qa, supp, es, en, p2):
    T.append(dict(name=name, lines=lines.strip().split("\n"), vocab=vocab.strip().split("\n"),
                  extra=extra, qa=qa, supp=supp, es=es, en=en,
                  p2=[tuple(x.split("|")) for x in p2.strip().split("\n")]))

add("跟室友吵架",
"""我跟室友住在一起半年了
一開始大家相處得還不錯
後來他常常把碗堆在水槽
好幾天都不洗，臭味越來越重
我忍無可忍，終於開口提醒他
他卻說我太愛計較
我們大吵一架，氣氛變得很尷尬
冷戰只會讓問題更難解決""",
"""室友|compañero(a) de casa|roommate
相處|llevarse (con alguien)|get along
堆|amontonar|pile up
水槽|fregadero|sink
臭味|mal olor|bad smell
越來越|cada vez más|more and more
忍無可忍|no aguantar más|can't take it anymore
開口|abrir la boca, decir algo|speak up
提醒|recordar, avisar|remind
卻|pero (contraste)|yet, but
計較|ser quisquilloso|be petty
吵一架|pelearse|have a fight
氣氛|ambiente|atmosphere
尷尬|incómodo|awkward
冷戰|guerra fría, ley del hielo|silent treatment""",
"",
"我跟室友住在一起多久了? // 一開始我們相處得怎麼樣? // 後來室友做了什麼? // 我為什麼終於開口? // 室友怎麼回應? // 吵架以後氣氛怎麼樣? // 我覺得冷戰會怎麼樣?",
"忍無可忍（再也無法忍受的時候） // 卻（我好心提醒他，他卻說我愛計較） // 只會+V（冷戰只會讓問題更難解決、生氣只會更糟）",
"Llevo medio año viviendo con mi compañero de casa. Al principio nos llevábamos bastante bien. Después, él empezó a dejar los platos amontonados en el fregadero. Pasaban varios días sin lavarlos y el olor era cada vez peor. Ya no aguanté más y por fin se lo mencioné. Pero él dijo que yo era demasiado quisquilloso. Tuvimos una gran pelea y el ambiente quedó muy incómodo. La ley del hielo solo hará que el problema sea más difícil de resolver.",
"I've lived with my roommate for half a year. At first we got along fine. Later he often piled dishes in the sink. He wouldn't wash them for days and the smell kept getting worse. I couldn't take it anymore and finally spoke up. But he said I was too petty. We had a big fight and the atmosphere became awkward. The silent treatment only makes the problem harder to solve.",
"""你有跟別人合租的經驗嗎?|¿Has compartido casa con otras personas?|Have you ever shared a place with others?
你覺得跟室友相處最難的是什麼?|¿Qué es lo más difícil de convivir con un compañero de casa?|What do you think is hardest about living with a roommate?
你會怎麼跟室友分配家事?|¿Cómo repartirías las tareas del hogar con un compañero?|How would you divide chores with a roommate?
如果室友一直不洗碗，你會怎麼說?|Si tu compañero nunca lava los platos, ¿qué le dirías?|If your roommate never washes the dishes, what would you say?
你比較喜歡直接說還是用暗示的方式?|¿Prefieres decir las cosas directamente o insinuarlas?|Do you prefer saying things directly or hinting?
在你的國家，大家怎麼處理這種小衝突?|En tu país, ¿cómo se manejan estos conflictos pequeños?|In your country, how do people handle small conflicts like this?
你覺得冷戰有用嗎? 為什麼?|¿Crees que la ley del hielo funciona? ¿Por qué?|Do you think the silent treatment works? Why?
吵架以後，誰應該先道歉?|¿Quién debería pedir perdón primero después de una pelea?|After a fight, who should apologize first?
如果談不攏，你會搬走嗎?|Si no se ponen de acuerdo, ¿te mudarías?|If you can't reach an agreement, would you move out?
你覺得住一個人和跟別人住，哪一個比較好?|¿Qué es mejor: vivir solo o con otras personas?|Which is better: living alone or with others?""")

add("加班",
"""最近公司的案子特別多
主管每天下班前才交代工作
害我連續一個禮拜都加班到九點
雖然有加班費，我卻不開心
因為我已經好久沒陪家人吃飯
同事說這是常態，早就習慣了
但我覺得健康比績效更重要
我打算下個月跟主管好好談談""",
"""案子|proyecto, caso de trabajo|project (work case)
交代|encargar, asignar|assign, instruct
下班|salir del trabajo|get off work
害|hacer que (algo malo pase)|cause (trouble) to
連續|consecutivo|consecutive
加班|hacer horas extra|work overtime
加班費|pago por horas extra|overtime pay
陪|acompañar|accompany
常態|lo normal, algo habitual|the norm
早就|desde hace tiempo|long ago, already
習慣|acostumbrarse|get used to
績效|rendimiento|performance
健康|salud|health
打算|pensar hacer, planear|plan to
好好談談|hablar con calma|have a proper talk""",
"",
"最近公司怎麼樣? // 主管什麼時候交代工作? // 我連續加班了多久? // 雖然有加班費，我為什麼不開心? // 同事怎麼看加班? // 我覺得什麼比績效更重要? // 我打算怎麼做?",
"害+O+V（害我連續加班、害我遲到、害大家等） // 早就…了（早就習慣了、早就知道了） // 雖然…卻…（雖然有加班費，我卻不開心）；打算",
"Últimamente en la empresa hay muchos proyectos. Mi jefe asigna el trabajo justo antes de salir, y por eso trabajé horas extra hasta las nueve durante toda una semana. Aunque pagan las horas extra, no estoy contento, porque hace mucho que no ceno con mi familia. Mis compañeros dicen que es lo normal y que ya se acostumbraron. Pero yo creo que la salud es más importante que el rendimiento. Pienso hablar con mi jefe con calma el próximo mes.",
"Lately the company has had a lot of projects. My boss assigns work just before we leave each day, which made me work overtime until nine for a whole week. Although there's overtime pay, I'm not happy, because I haven't had dinner with my family in a long time. My coworkers say this is normal and they got used to it long ago. But I think health is more important than performance. I plan to have a proper talk with my boss next month.",
"""你的國家加班常見嗎? 加班會有加班費嗎?|En tu país, ¿es común hacer horas extra? ¿Las pagan?|In your country, is overtime common? Is it paid?
你覺得工作和生活應該怎麼平衡?|¿Cómo crees que se debe equilibrar el trabajo y la vida personal?|How do you think work and life should be balanced?
如果主管下班前才交代工作，你會怎麼辦?|Si tu jefe asigna trabajo justo al salir, ¿qué haces?|If your boss assigns work right before you leave, what do you do?
你敢對主管說「不」嗎? 為什麼?|¿Te atreves a decirle «no» a tu jefe? ¿Por qué?|Do you dare say "no" to your boss? Why?
你覺得加班費能補償犧牲的時間嗎?|¿Crees que el pago de horas extra compensa el tiempo sacrificado?|Do you think overtime pay makes up for the lost time?
你覺得為什麼有些公司的加班變成常態?|¿Por qué crees que en algunas empresas las horas extra son lo normal?|Why do you think overtime becomes the norm in some companies?
你覺得健康、薪水和興趣，哪一個最重要?|¿Qué es más importante: la salud, el salario o los intereses?|Which is most important: health, salary, or interest?
如果同事都習慣加班，你會跟著加班嗎?|Si todos tus compañeros se acostumbran a las horas extra, ¿las harías tú también?|If all your coworkers are used to overtime, would you stay late too?
你理想中的工作時間是怎麼樣的?|¿Cómo sería tu horario de trabajo ideal?|What would your ideal working hours look like?
如果要跟主管談這件事，你會怎麼開口?|Si fueras a hablar de esto con tu jefe, ¿cómo empezarías?|If you were to talk to your boss about this, how would you start?""")

add("收到罰單",
"""今天早上我騎機車去上班
因為趕時間，隨便停在路邊
想說只要停五分鐘就好
沒想到回來就看到一張罰單
原來那裡是禁止停車的紅線
我氣得想跟警察理論
但是仔細想想確實是我不對
只好乖乖去繳六百塊的罰款""",
"""機車|motocicleta, scooter|scooter
趕時間|tener prisa|be in a hurry
隨便|sin cuidado, como sea|casually, carelessly
路邊|borde de la calle|roadside
沒想到|para mi sorpresa|unexpectedly
罰單|multa (el papel)|ticket (fine)
原來|resulta que|it turns out
禁止|prohibido|prohibited
紅線|línea roja|red line
氣得|tan enojado que…|so angry that…
理論|discutir, reclamar|argue it out
仔細|con atención|carefully
確實|realmente|indeed
乖乖|obedientemente|obediently
罰款|multa (dinero)|fine (money)""",
"",
"今天早上我怎麼去上班? // 我為什麼隨便停車? // 我本來打算停多久? // 回來後我發現什麼? // 那個地方為什麼不能停車? // 我一開始想怎麼做? // 最後我怎麼處理?",
"隨便+V（隨便停、隨便吃、隨便說） // 氣得+V（氣得想理論、氣得說不出話） // 確實（確實是我不對；=en verdad，用來承認事實）；想說…",
"Esta mañana fui al trabajo en scooter. Como tenía prisa, lo estacioné sin cuidado en la orilla de la calle. Pensé que solo serían cinco minutos. Pero al volver, ¡me encontré con una multa en el vehículo! Resulta que ahí había una línea roja de prohibido estacionarse. Me enojé tanto que quise discutir con el policía, pero pensándolo bien, de verdad fue mi culpa. No me quedó más remedio que ir obedientemente a pagar la multa de seiscientos dólares.",
"This morning I rode my scooter to work. Because I was in a hurry, I parked carelessly at the roadside. I figured it would only be five minutes. But when I came back, I found a ticket on it. It turns out that was a no-parking red line. I was so angry I wanted to argue with the police officer, but thinking it over, it really was my fault. I had no choice but to go and pay the 600-dollar fine obediently.",
"""你有收過罰單嗎? 是因為什麼?|¿Has recibido alguna multa? ¿Por qué razón?|Have you ever got a ticket? What for?
在你的國家，違規停車會罰多少錢?|En tu país, ¿cuánto cuesta una multa por estacionar mal?|In your country, how much is the fine for illegal parking?
你覺得趕時間是亂停車的好理由嗎?|¿Crees que tener prisa es una buena excusa para estacionar mal?|Do you think being in a hurry is a good excuse for parking illegally?
收到罰單的時候，你會想跟警察理論嗎?|Al recibir una multa, ¿te dan ganas de discutir con el policía?|When you get a ticket, do you want to argue with the officer?
你覺得罰款的金額合理嗎?|¿Te parece razonable el monto de las multas?|Do you think the fine amounts are reasonable?
你覺得為什麼有人明知不能停還是停?|¿Por qué crees que algunos estacionan aunque sepan que no se puede?|Why do you think some people park even though they know they shouldn't?
在你的國家，大家比較常騎機車、開車還是搭大眾運輸?|En tu país, ¿qué se usa más: moto, auto o transporte público?|In your country, do people mostly ride scooters, drive, or take public transit?
如果你被冤枉了，你會怎麼申訴?|Si te multaran injustamente, ¿cómo lo apelarías?|If you were wrongly fined, how would you appeal?
你覺得停車位不夠的問題要怎麼解決?|¿Cómo crees que se puede resolver la falta de estacionamientos?|How do you think the lack of parking spaces can be solved?
你有沒有因為一時方便而後悔的經驗?|¿Alguna vez te arrepentiste de hacer algo solo por comodidad?|Have you ever regretted doing something just for convenience?""")

add("被放鴿子",
"""我上週訂了一間人氣餐廳
為了這一天，我等了兩個月
結果朋友臨時放我鴿子
餐廳要求我們十分鐘內到
否則就會取消訂位
我又氣又失望，只好一個人去
沒想到服務生竟然很貼心
還特別送了我一份甜點""",
"""人氣|popular|popular
訂位|reservar mesa|reservation
結果|el resultado fue que|as it turned out
臨時|a último momento|at the last minute
放…鴿子|dejar plantado(a)|stand someone up
要求|exigir, pedir|require
否則|de lo contrario|otherwise
取消|cancelar|cancel
又…又…|tan… y tan…|both… and…
失望|decepcionado|disappointed
只好|no tener más remedio que|have no choice but to
服務生|mesero(a)|server
貼心|atento, considerado|thoughtful
特別|especialmente|specially
甜點|postre|dessert""",
"",
"我上週訂了什麼? // 我為什麼期待這一天? // 結果朋友怎麼了? // 餐廳要求我們怎麼樣? // 如果沒有準時到，會怎麼樣? // 我當時的心情怎麼樣? // 服務生做了什麼讓我很意外?",
"臨時+V（臨時取消、臨時有事） // 否則（要求十分鐘內到，否則取消） // 又…又…（又氣又失望、又累又餓）；放鴿子＝不守約",
"La semana pasada reservé en un restaurante muy popular. Esperé este día durante dos meses. Pero mi amigo me plantó a último momento. El restaurante nos pidió llegar en diez minutos; de lo contrario cancelarían la reserva. Estaba enojado y decepcionado, así que no me quedó más remedio que ir solo. Para mi sorpresa, el mesero fue muy amable y además me regaló un postre.",
"Last week I booked a very popular restaurant. I had waited two months for this day. But my friend stood me up at the last minute. The restaurant required us to arrive within ten minutes, otherwise they'd cancel the reservation. I was both angry and disappointed, so I had no choice but to go alone. Unexpectedly, the server was really thoughtful and even gave me a free dessert.",
"""你有被放鴿子的經驗嗎? 你的心情怎麼樣?|¿Alguna vez te han dejado plantado(a)? ¿Cómo te sentiste?|Have you ever been stood up? How did you feel?
你有放過別人鴿子嗎? 為什麼?|¿Has plantado a alguien? ¿Por qué?|Have you ever stood someone up? Why?
如果臨時不能去，你會怎麼通知對方?|Si no puedes ir a último momento, ¿cómo avisas?|If you can't make it at the last minute, how do you let the other person know?
你覺得有什麼理由可以臨時取消?|¿Qué razones te parecen válidas para cancelar a último momento?|What reasons do you think are acceptable for canceling at the last minute?
在你的國家，訂位後沒去會有什麼後果?|En tu país, ¿qué pasa si reservas y no vas?|In your country, what happens if you book and don't show up?
你覺得餐廳要求準時，否則取消，合理嗎?|¿Te parece razonable que el restaurante exija puntualidad o cancele?|Do you think it's reasonable for a restaurant to demand punctuality or cancel?
一個人去餐廳吃飯，你覺得怎麼樣?|¿Qué te parece ir a un restaurante solo(a)?|How do you feel about dining alone at a restaurant?
你有沒有因為服務很好而特別感動的經驗?|¿Alguna vez te conmovió un servicio especialmente bueno?|Have you ever been especially moved by great service?
你會給小費或特別感謝服務生嗎?|¿Das propina o agradeces especialmente al mesero?|Do you tip or specially thank servers?
如果朋友一直放你鴿子，你還會繼續約他嗎?|Si un amigo te planta una y otra vez, ¿seguirías invitándolo?|If a friend keeps standing you up, would you still invite them?""")

add("記帳存錢",
"""我以前從來不記帳
月底總是搞不清錢花到哪去了
去年底我下定決心開始記帳
我每天把花費記在手機裡
這才發現光是飲料就花很多
於是我改成每天自己帶水
結果半年下來省了一萬多塊
看來記帳真的是存錢的第一步""",
"""記帳|llevar las cuentas|keep a spending record
從來|nunca (hasta ahora)|never (so far)
月底|fin de mes|end of the month
搞不清|no tener claro|can't figure out
下定決心|decidirse firmemente|make up one's mind
花費|gasto|expenses
這才|solo entonces|only then
光是|solo…|just…, alone
飲料|bebida|drinks
改成|cambiar a|change to
結果|el resultado fue|as a result
省|ahorrar|save
看來|parece que|it seems
第一步|el primer paso|first step
存錢|ahorrar dinero|save money""",
"",
"我以前有沒有記帳的習慣? // 月底的時候，我常常有什麼問題? // 我什麼時候下定決心記帳? // 我怎麼記帳? // 我發現哪一項花費特別多? // 我後來怎麼改變? // 半年下來有什麼結果?",
"從來不／沒…（我從來不記帳、他從來沒遲到） // 光是…就…（光是飲料就花很多、光是路費就一千塊） // 這才…（這才發現、這才明白）；看來",
"Antes nunca llevaba las cuentas. A fin de mes siempre no tenía claro en qué se había ido el dinero. A fines del año pasado me decidí a empezar. Cada día anotaba mis gastos en el celular. Fue entonces cuando me di cuenta de que solo en bebidas gastaba mucho. Así que cambié y empecé a llevar mi propia agua todos los días. Como resultado, en medio año ahorré más de diez mil dólares. Parece que llevar las cuentas es de verdad el primer paso para ahorrar.",
"I never used to keep track of my spending. At the end of each month I could never figure out where my money had gone. At the end of last year I made up my mind to start. Every day I recorded my expenses on my phone. Only then did I realize that drinks alone cost a lot. So I switched to bringing my own water every day. As a result, in half a year I saved over 10,000 dollars. It seems tracking expenses really is the first step to saving.",
"""你有記帳的習慣嗎? 你怎麼記?|¿Llevas las cuentas de tus gastos? ¿Cómo?|Do you track your spending? How?
你覺得自己每個月最大的花費是什麼?|¿Cuál es tu mayor gasto mensual?|What is your biggest monthly expense?
你有沒有發現自己在某些東西上花太多?|¿Has notado que gastas demasiado en algo?|Have you noticed you spend too much on something?
你覺得省錢和享受生活，應該怎麼平衡?|¿Cómo equilibrar ahorrar y disfrutar la vida?|How do you balance saving money and enjoying life?
在你的國家，年輕人習慣存錢嗎?|En tu país, ¿los jóvenes suelen ahorrar?|In your country, do young people usually save money?
你有存錢的目標嗎? 是什麼?|¿Tienes una meta de ahorro? ¿Cuál?|Do you have a savings goal? What is it?
你覺得現在用手機記帳比用筆記本好嗎?|¿Crees que llevar las cuentas en el celular es mejor que en un cuaderno?|Do you think tracking on a phone is better than in a notebook?
如果突然多了一筆錢，你會存起來還是花掉?|Si de repente tuvieras dinero extra, ¿lo ahorrarías o lo gastarías?|If you suddenly had extra money, would you save or spend it?
你覺得小小的習慣，例如自己帶水，真的能省很多錢嗎?|¿Crees que pequeños hábitos, como llevar agua propia, realmente ahorran mucho?|Do you think small habits, like bringing your own water, really save a lot?
你覺得金錢教育應該從什麼時候開始?|¿A qué edad crees que debe empezar la educación financiera?|When do you think financial education should start?""")

add("地震警報",
"""昨天半夜我的手機突然大響
螢幕寫著「地震警報」
我嚇得立刻從床上跳起來
幾秒鐘後，房子開始搖晃
我抓著手機躲到桌子底下
還好這次地震不算嚴重
搖了一會兒就停了
但是我一整晚都睡不著""",
"""半夜|medianoche|in the middle of the night
突然|de repente|suddenly
大響|sonar muy fuerte|ring loudly
螢幕|pantalla|screen
地震|terremoto, sismo|earthquake
警報|alerta|alert
立刻|enseguida|immediately
跳起來|saltar|jump up
搖晃|sacudirse, temblar|shake
抓著|agarrar|grab
躲|esconderse|hide, take cover
桌子底下|debajo de la mesa|under the table
還好|por suerte|luckily
不算|no se considera|not really
嚴重|grave|serious""",
"一會兒 → un rato  //  一整晚 → toda la noche",
"昨天半夜發生什麼事? // 手機螢幕上寫什麼? // 我當時有什麼反應? // 幾秒鐘後房子怎麼了? // 我躲到哪裡? // 這次地震嚴重嗎? // 地震以後我怎麼樣?",
"V得…（嚇得立刻跳起來、嚇得說不出話） // 不算+adj.（不算嚴重、不算貴、不算遠） // 一整+N（一整晚、一整天、一整個月）；一會兒",
"Anoche, a medianoche, mi celular sonó de repente muy fuerte. En la pantalla decía «alerta de terremoto». Me asusté tanto que salté de la cama al instante. Unos segundos después, la casa empezó a sacudirse. Agarré el celular y me escondí debajo de la mesa. Por suerte, este sismo no fue muy grave y se detuvo después de un rato. Pero no pude dormir en toda la noche.",
"Last night in the middle of the night, my phone suddenly rang loudly. The screen said \"earthquake alert.\" I was so scared that I jumped out of bed immediately. A few seconds later, the house began to shake. I grabbed my phone and hid under the table. Luckily, this earthquake wasn't very serious and stopped after a while. But I couldn't sleep the whole night.",
"""你經歷過地震嗎? 是什麼感覺?|¿Has vivido un terremoto? ¿Cómo fue?|Have you experienced an earthquake? What was it like?
地震的時候，你覺得應該做什麼?|Durante un sismo, ¿qué crees que se debe hacer?|What do you think you should do during an earthquake?
你的國家常常發生什麼天災?|¿Qué desastres naturales ocurren con frecuencia en tu país?|What natural disasters often happen in your country?
你覺得手機的地震警報有幫助嗎?|¿Crees que las alertas de sismo en el celular ayudan?|Do you think phone earthquake alerts are helpful?
你家有準備緊急包嗎? 裡面有什麼?|¿Tienes una mochila de emergencia? ¿Qué lleva?|Do you have an emergency kit at home? What's in it?
如果半夜發生地震，你會先做什麼?|Si hay un sismo a medianoche, ¿qué harías primero?|If an earthquake happens at midnight, what would you do first?
你覺得大家平常有足夠的防災教育嗎?|¿Crees que hay suficiente educación sobre desastres?|Do you think there is enough disaster-prevention education?
地震以後，你會覺得害怕或睡不著嗎?|Después de un sismo, ¿sientes miedo o no puedes dormir?|After an earthquake, do you feel afraid or can't sleep?
你覺得住在高樓和低樓，哪一個比較安全?|¿Qué es más seguro: vivir en un piso alto o bajo?|Do you think living on a high or low floor is safer?
如果有朋友很怕地震，你會怎麼安慰他?|Si un amigo le tiene mucho miedo a los sismos, ¿cómo lo consolarías?|If a friend is very afraid of earthquakes, how would you comfort them?""")

add("計程車繞路",
"""下大雨，我趕著去機場
於是我叫了一輛計程車
司機一上車就問我要走哪條路
我說用導航最快的就可以
他卻說導航不準，堅持抄小路
結果越開越遠，還遇到大塞車
我急得快哭了，車資也一直跳
雖然趕上了，我卻很不滿""",
"""趕|apurarse|rush
機場|aeropuerto|airport
於是|por eso, entonces|so
計程車|taxi|taxi
司機|conductor(a)|driver
導航|navegación, GPS|navigation
不準|no ser preciso|inaccurate
堅持|insistir|insist
抄小路|tomar un atajo|take a shortcut
越…越…|cada vez más…|the more… the more…
塞車|tráfico, embotellamiento|traffic jam
急|desesperarse|anxious
車資|tarifa|fare
跳|saltar, subir (el taxímetro)|tick up
趕上|llegar a tiempo|catch (in time)""",
"不滿 → insatisfecho(a)",
"那天天氣怎麼樣? // 我為什麼要去機場? // 司機一上車問我什麼? // 我希望怎麼走? // 司機為什麼堅持抄小路? // 結果路上發生什麼事? // 最後我趕上了嗎? 我的感覺怎麼樣?",
"堅持+V（堅持抄小路、堅持不退讓） // 急得…（急得快哭了、急得睡不著） // 趕上／趕不上（趕上飛機、趕不上末班車）；雖然…卻…",
"Llovía fuerte y yo tenía prisa por llegar al aeropuerto, así que tomé un taxi. En cuanto subí, el conductor me preguntó por qué ruta quería ir. Le dije que con el GPS por la más rápida. Pero él dijo que el GPS no era preciso e insistió en tomar un atajo. Resultó que nos alejamos más y más, y además nos topamos con un gran embotellamiento. Me desesperé casi hasta llorar y la tarifa seguía subiendo. Aunque al final llegué a tiempo, quedé muy insatisfecho.",
"It was raining heavily and I was rushing to the airport, so I called a taxi. As soon as I got in, the driver asked which route to take. I said the fastest one on the GPS was fine. But he said the GPS wasn't accurate and insisted on taking a shortcut. As a result we drove farther and farther away and hit heavy traffic. I was so anxious I almost cried, and the fare kept ticking up. Although I made it in time, I was very dissatisfied.",
"""你在國外搭過計程車嗎? 經驗怎麼樣?|¿Has tomado un taxi en el extranjero? ¿Cómo fue?|Have you taken a taxi abroad? How was it?
在你的國家，搭計程車安全嗎?|En tu país, ¿es seguro tomar taxi?|In your country, is taking a taxi safe?
你比較喜歡叫計程車還是用叫車 App?|¿Prefieres pedir un taxi o usar una app de transporte?|Do you prefer hailing a taxi or using a ride-hailing app?
如果司機繞路，你會直接說嗎?|Si el conductor da un rodeo, ¿se lo dices directamente?|If the driver takes a detour, would you say something directly?
你相信導航還是相信當地司機的經驗?|¿Confías más en el GPS o en la experiencia del conductor local?|Do you trust GPS or the local driver's experience more?
趕時間的時候，你會怎麼選交通工具?|Cuando tienes prisa, ¿cómo eliges el transporte?|When you're in a hurry, how do you choose transportation?
你有沒有因為塞車而錯過重要的事?|¿Alguna vez perdiste algo importante por el tráfico?|Have you ever missed something important because of traffic?
你覺得給司機小費是必要的嗎?|¿Crees que es necesario dar propina al conductor?|Do you think tipping the driver is necessary?
和司機聊天，你覺得有趣還是尷尬?|¿Conversar con el conductor te parece divertido o incómodo?|Is chatting with drivers fun or awkward for you?
如果你不滿意服務，你會怎麼反映?|Si no estás satisfecho con el servicio, ¿cómo lo reportas?|If you're dissatisfied with the service, how do you report it?""")

add("過年被問",
"""過年回老家是最讓我緊張的事
親戚一見面就問我有沒有對象
接著問我薪水、什麼時候買房
我只好笑著說還在努力
其實我心裡一點也不輕鬆
我爸媽在旁邊也幫不上忙
還好拿到不少紅包，心情好多了
不管怎麼樣，一家團圓最重要""",
"""老家|pueblo natal, casa familiar|hometown, family home
緊張|nervioso|nervous
親戚|pariente|relatives
對象|pareja, novio(a)|partner (romantic)
接著|a continuación|next
薪水|salario|salary
買房|comprar casa|buy a house
努力|esforzarse|work hard
其實|en realidad|actually
輕鬆|relajado|relaxed
幫不上忙|no poder ayudar|unable to help
還好|por suerte|luckily
紅包|sobre rojo (regalo de dinero)|red envelope
不管怎麼樣|pase lo que pase|no matter what
團圓|reunión familiar|family reunion""",
"",
"過年回老家，我最緊張什麼? // 親戚一見面問我什麼? // 接著他們還問什麼? // 我怎麼回應? // 我心裡的感覺怎麼樣? // 我的父母有幫上忙嗎? // 什麼事讓我心情好一點?",
"一點也不+adj.（一點也不輕鬆、一點也不貴） // V不上（幫不上忙、趕不上、跟不上） // 不管怎麼樣…都…（不管怎麼樣，一家團圓最重要）；其實",
"Volver a casa por Año Nuevo es lo que más me pone nervioso. En cuanto nos vemos, los parientes me preguntan si tengo pareja. Luego preguntan cuánto gano y cuándo voy a comprar casa. No me queda más que sonreír y decir que me estoy esforzando. En realidad, por dentro no me siento nada relajado. Mis papás, a mi lado, tampoco pueden ayudarme. Por suerte recibí varios sobres rojos y me animé bastante. Pase lo que pase, lo más importante es que la familia esté reunida.",
"Going back to my hometown for the New Year is what makes me most nervous. The moment relatives see me, they ask whether I have a partner. Then they ask how much I earn and when I'll buy a house. I have no choice but to smile and say I'm still working on it. Actually, I'm not relaxed at all inside. My parents standing by can't help either. Luckily I got quite a few red envelopes, and I felt much better. No matter what, family reunion matters most.",
"""你的國家怎麼慶祝新年或重要的節日?|¿Cómo se celebra el Año Nuevo o las fiestas importantes en tu país?|How does your country celebrate New Year or major holidays?
你會回老家過節嗎? 你喜歡嗎?|¿Vuelves a tu casa familiar en las fiestas? ¿Te gusta?|Do you go back home for holidays? Do you like it?
親戚常常問你什麼問題? 你怎麼回答?|¿Qué preguntas suelen hacerte tus parientes? ¿Cómo respondes?|What questions do relatives often ask you? How do you answer?
你覺得問別人薪水或對象禮貌嗎?|¿Te parece educado preguntar el salario o la pareja?|Do you think it's polite to ask about someone's salary or partner?
如果你不想回答，你會怎麼巧妙地迴避?|Si no quieres responder, ¿cómo lo esquivas con tacto?|If you don't want to answer, how do you tactfully dodge it?
你覺得為什麼長輩這麼關心這些事?|¿Por qué crees que los mayores se interesan tanto en esto?|Why do you think older relatives care so much about these things?
你收過或給過紅包嗎? 在你的國家有類似的習慣嗎?|¿Has recibido o dado sobres rojos? ¿Hay una costumbre similar en tu país?|Have you given or received red envelopes? Is there a similar custom in your country?
你覺得家庭團聚和個人休息，哪一個比較重要?|¿Qué es más importante: reunirse en familia o descansar?|Which is more important: family reunions or personal rest?
如果你有孩子，你會問他們同樣的問題嗎?|Si tuvieras hijos, ¿les harías las mismas preguntas?|If you had children, would you ask them the same questions?
你覺得這些傳統應該保留還是改變?|¿Crees que estas tradiciones deben conservarse o cambiar?|Do you think these traditions should be kept or changed?""")

add("免費試用忘取消",
"""上個月我註冊了一個影音平台
它提供三十天免費試用
我心想看完想看的劇就取消
結果工作一忙就忘光了
前幾天發現信用卡被扣款了
我趕緊上網找取消的方法
沒想到按鈕藏得很深，找了半天
看來公司就是故意讓人找不到""",
"""註冊|registrarse|sign up
平台|plataforma|platform
免費試用|prueba gratuita|free trial
心想|pensar para sí|think to oneself
取消|cancelar|cancel
結果|el resultado fue|as it turned out
忘光|olvidar por completo|forget completely
信用卡|tarjeta de crédito|credit card
扣款|cobro|charge (deduct payment)
趕緊|rápidamente|hurriedly
按鈕|botón|button
藏|esconder|hide
找了半天|buscar un buen rato|search for ages
看來|parece que|it seems
故意|a propósito|on purpose""",
"",
"上個月我註冊了什麼? // 這個平台提供什麼優惠? // 我原本打算怎麼做? // 結果我為什麼沒有取消? // 我什麼時候發現被扣款? // 我怎麼找取消的方法? // 我覺得公司為什麼這樣設計?",
"心想（我心想…：pensar para uno mismo） // V光（忘光、吃光、用光、賣光） // 故意+V（故意讓人找不到、故意不說）；找了半天",
"El mes pasado me registré en una plataforma de video. Ofrecía treinta días de prueba gratuita. Pensé que cancelaría en cuanto terminara de ver las series que quería. Pero con el trabajo, lo olvidé por completo. Hace unos días vi que me habían cobrado en la tarjeta de crédito. Rápidamente busqué en internet cómo cancelar. Para mi sorpresa, el botón estaba muy escondido y tardé un buen rato en encontrarlo. Parece que la empresa lo hace a propósito para que no se encuentre.",
"Last month I signed up for a streaming platform. It offered a 30-day free trial. I thought I'd cancel after finishing the shows I wanted to watch. But I got busy with work and forgot completely. A few days ago I found my credit card had been charged. I hurriedly went online to look for how to cancel. Unexpectedly, the button was hidden deep, and I searched for ages. It seems the company does it on purpose so people can't find it.",
"""你有訂閱什麼服務嗎? 例如影音、音樂。|¿Tienes alguna suscripción, como video o música?|Do you subscribe to any services, such as streaming or music?
你有沒有忘記取消免費試用的經驗?|¿Alguna vez olvidaste cancelar una prueba gratuita?|Have you ever forgotten to cancel a free trial?
你覺得公司為什麼提供免費試用?|¿Por qué crees que las empresas ofrecen pruebas gratuitas?|Why do you think companies offer free trials?
你覺得把取消按鈕藏起來公平嗎?|¿Te parece justo esconder el botón de cancelar?|Do you think hiding the cancel button is fair?
你怎麼管理每個月自動扣款的項目?|¿Cómo controlas los cobros automáticos mensuales?|How do you manage your automatic monthly charges?
如果被多扣款，你會怎麼處理?|Si te cobran de más, ¿qué haces?|If you're charged by mistake, what do you do?
你覺得訂閱制比一次買斷好嗎?|¿Crees que la suscripción es mejor que comprar una sola vez?|Do you think subscriptions are better than one-time purchases?
你每個月花多少錢在訂閱上? 值得嗎?|¿Cuánto gastas al mes en suscripciones? ¿Vale la pena?|How much do you spend monthly on subscriptions? Is it worth it?
你認為政府應該規定公司讓取消更簡單嗎?|¿Crees que el gobierno debería obligar a facilitar la cancelación?|Do you think the government should require companies to make canceling easier?
你有沒有因為「免費」兩個字而買了不需要的東西?|¿Alguna vez compraste algo innecesario por la palabra «gratis»?|Have you ever bought something unnecessary because it said "free"?""")

add("被劇透",
"""我等了一年的電影終於上映了
可惜我週末要加班，只能下週看
沒想到朋友竟然在群組裡劇透
把結局和最大的轉折全說了
我氣得想退出群組
他還一臉無辜地說只是隨口聊聊
結果我看電影的時候毫無期待
這才明白劇透真是毀掉一切""",
"""上映|estrenarse|be released (in theaters)
可惜|lástima|too bad
加班|hacer horas extra|work overtime
沒想到|para mi sorpresa|unexpectedly
群組|grupo (de chat)|group chat
劇透|spoiler|spoil (a plot)
結局|final|ending
轉折|giro (de la trama)|plot twist
氣得|tan enojado que…|so angry that…
退出|salirse|leave, quit
一臉無辜|con cara de inocente|with an innocent look
隨口|sin pensar, casualmente|offhandedly
毫無|sin ningún|not at all
期待|expectativa|expectation
這才明白|solo entonces comprendí|only then did I understand""",
"",
"我等了多久才等到電影上映? // 我為什麼週末不能去看? // 朋友在群組裡做了什麼? // 他說了什麼內容? // 我當時想怎麼做? // 朋友怎麼解釋? // 後來我看電影的感覺怎麼樣?",
"毫無+N（毫無期待、毫無興趣、毫無頭緒） // 隨口+V（隨口說說、隨口問問） // 可惜…（lamentarse：可惜我週末要加班）；這才明白",
"La película que esperé un año por fin se estrenó. Lástima que el fin de semana tenía que trabajar horas extra y solo podría verla la semana siguiente. Para mi sorpresa, un amigo hizo spoiler en el grupo de chat: contó el final y el giro más importante. Me enojé tanto que quise salirme del grupo. Y con cara de inocente dijo que solo estaba platicando. Así que, al ver la película, ya no sentía ninguna expectativa. Solo entonces comprendí que los spoilers lo arruinan todo.",
"The movie I had waited a year for was finally released. Too bad I had to work overtime on the weekend and could only watch it next week. Unexpectedly, a friend actually spoiled it in the group chat, telling the ending and the biggest twist. I was so angry I wanted to leave the group. He even said innocently that he was only chatting casually. As a result, I had no expectations at all when I watched the movie. Only then did I understand that spoilers ruin everything.",
"""你有被劇透的經驗嗎? 你的反應是什麼?|¿Te han hecho spoiler alguna vez? ¿Cómo reaccionaste?|Have you ever been spoiled? How did you react?
你覺得知道結局會影響看電影的樂趣嗎?|¿Crees que saber el final afecta el disfrute de una película?|Do you think knowing the ending affects your enjoyment of a movie?
你會故意先看劇透再決定要不要看嗎?|¿Lees spoilers a propósito antes de decidir si verla?|Do you read spoilers on purpose before deciding to watch?
如果朋友不小心劇透，你會怎麼說?|Si un amigo hace spoiler sin querer, ¿qué le dices?|If a friend accidentally spoils something, what do you say?
在你的國家，大家怎麼避免劇透?|En tu país, ¿cómo evita la gente los spoilers?|In your country, how do people avoid spoilers?
你最近看過什麼值得推薦的電影或劇?|¿Qué película o serie reciente recomendarías?|What recent movie or show would you recommend?
你喜歡在電影院看還是在家看? 為什麼?|¿Prefieres ver cine en una sala o en casa? ¿Por qué?|Do you prefer watching at the cinema or at home? Why?
你覺得好的電影，結局重要還是過程重要?|En una buena película, ¿qué importa más: el final o el proceso?|In a good movie, which matters more: the ending or the process?
你和朋友討論劇情的時候，會注意什麼?|Al discutir tramas con amigos, ¿a qué prestas atención?|When discussing plots with friends, what do you pay attention to?
你覺得社群網站上的劇透問題要怎麼解決?|¿Cómo crees que se puede resolver el problema de los spoilers en redes sociales?|How do you think the spoiler problem on social media can be solved?""")
