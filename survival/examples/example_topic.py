FILE = '租房找住處篇'
OPEN = '租房子和找住處（看房、租金、押金、水電、房東）'

SCENES = [
 ([
  ('我想租一間套房，有空房嗎？', 'Quiero alquilar un estudio. ¿Hay alguno disponible?', "I'd like to rent a studio. Is there one available?"),
  ('我可以先看房嗎？', '¿Puedo ver el apartamento primero?', 'Can I see it first?'),
  ('房子離捷運站多遠？', '¿Qué tan lejos está de la estación del metro?', 'How far is it from the MRT station?'),
  ('這附近安全嗎？', '¿Es seguro este barrio?', 'Is this neighborhood safe?'),
 ], [
  ('租', 'alquilar', 'rent'), ('套房', 'estudio', 'studio apartment'), ('雅房', 'cuarto compartido', 'room with shared bathroom'),
  ('看房', 'ver el lugar', 'view the property'), ('房東', 'casero', 'landlord'), ('仲介', 'agente inmobiliario', 'real estate agent'),
  ('安全', 'seguro', 'safe'),
 ], '例：旅客和房屋仲介站在一間套房門口看房'),
 ([
  ('一個月租金多少？', '¿Cuánto es el alquiler mensual?', 'How much is the monthly rent?'),
  ('押金要付幾個月？', '¿Cuántos meses de depósito hay que pagar?', 'How many months of deposit do I need to pay?'),
  ('租金包含水電費嗎？', '¿El alquiler incluye agua y luz?', 'Does the rent include utilities?'),
  ('可以用轉帳付租金嗎？', '¿Puedo pagar el alquiler por transferencia?', 'Can I pay the rent by bank transfer?'),
 ], [
  ('租金', 'alquiler', 'rent'), ('押金', 'depósito', 'deposit'), ('水電費', 'agua y luz', 'utilities'),
  ('管理費', 'cuota de edificio', 'management fee'), ('轉帳', 'transferencia', 'bank transfer'),
  ('現金', 'efectivo', 'cash'), ('每月', 'cada mes', 'every month'),
 ], '例：旅客和房東坐在桌前，桌上有計算機和租金資料'),
 ([
  ('租約要簽多久？', '¿Por cuánto tiempo es el contrato?', 'How long is the lease?'),
  ('可以養寵物嗎？', '¿Se permiten mascotas?', 'Are pets allowed?'),
  ('可以讓朋友來過夜嗎？', '¿Pueden quedarse amigos a dormir?', 'Can friends stay overnight?'),
  ('提前退租要怎麼辦？', '¿Qué pasa si quiero terminar el contrato antes?', 'What happens if I want to end the lease early?'),
 ], [
  ('租約', 'contrato', 'lease'), ('簽約', 'firmar contrato', 'sign the contract'), ('寵物', 'mascota', 'pet'),
  ('過夜', 'pasar la noche', 'stay overnight'), ('退租', 'dejar el alquiler', 'move out'),
  ('提前', 'con anticipación', 'ahead of time'), ('規定', 'regla', 'rule'),
 ], '例：旅客拿筆準備簽租約，房東在旁邊說明'),
 ([
  ('房間有冷氣和熱水器嗎？', '¿La habitación tiene aire acondicionado y calentador de agua?', 'Does the room have air conditioning and a water heater?'),
  ('有洗衣機嗎？', '¿Hay lavadora?', 'Is there a washing machine?'),
  ('網路是房東提供的嗎？', '¿El internet lo proporciona el casero?', 'Does the landlord provide the internet?'),
  ('家具可以自己換嗎？', '¿Puedo cambiar los muebles?', 'Can I change the furniture myself?'),
 ], [
  ('冷氣', 'aire acondicionado', 'air conditioner'), ('熱水器', 'calentador', 'water heater'), ('洗衣機', 'lavadora', 'washing machine'),
  ('家具', 'muebles', 'furniture'), ('網路', 'internet', 'internet'), ('床', 'cama', 'bed'), ('衣櫃', 'armario', 'wardrobe'),
 ], '例：旅客在套房裡打開衣櫃與冷氣，檢查設備'),
 ([
  ('鑰匙有幾把？', '¿Cuántas llaves hay?', 'How many keys are there?'),
  ('垃圾什麼時候倒？', '¿Cuándo se saca la basura?', 'When do I take out the trash?'),
  ('水龍頭漏水了，可以請人來修嗎？', 'El grifo gotea. ¿Pueden enviar a alguien a repararlo?', 'The faucet is leaking. Can you send someone to fix it?'),
  ('電費要怎麼繳？', '¿Cómo se paga la luz?', 'How do I pay the electricity bill?'),
 ], [
  ('鑰匙', 'llave', 'key'), ('倒垃圾', 'sacar basura', 'take out the trash'), ('水龍頭', 'grifo', 'faucet'),
  ('漏水', 'gotear', 'leak'), ('修', 'reparar', 'repair'), ('電費', 'factura de luz', 'electricity bill'), ('繳', 'pagar', 'pay'),
 ], '例：旅客在廚房指著漏水的水龍頭，打電話給房東'),
 ([
  ('我下個月要搬家。', 'Me mudo el mes que viene.', "I'm moving out next month."),
  ('押金什麼時候退？', '¿Cuándo me devuelven el depósito?', 'When will I get my deposit back?'),
  ('可以請你來檢查房間嗎？', '¿Puede venir a revisar el apartamento?', 'Could you come and inspect the room?'),
  ('這個損壞不是我弄的。', 'Este daño no lo hice yo.', "I didn't cause this damage."),
 ], [
  ('搬家', 'mudarse', 'move house'), ('退押金', 'devolver depósito', 'refund the deposit'), ('檢查', 'revisar', 'inspect'),
  ('損壞', 'daño', 'damage'), ('弄壞', 'romper', 'break'), ('清潔', 'limpieza', 'cleaning'), ('通知', 'avisar', 'notify'),
 ], '例：旅客提著紙箱，房東在檢查空蕩蕩的房間'),
]

FILL = [
 ([
  '旅客：你好，我想租一間[套房]。',
  '仲介：有的，你想什麼時候[看房]？',
  '旅客：明天下午。請問[租金]多少？',
  '仲介：一個月一萬二，[押金]兩個月。',
  '旅客：[水電費]要另外付嗎？',
  '仲介：要，[租約]一年。',
 ], [
  'Viajero: Hola, quiero alquilar un estudio.',
  'Agente: Claro, ¿cuándo quiere ver el lugar?',
  'Viajero: Mañana por la tarde. ¿Cuánto es el alquiler?',
  'Agente: Doce mil dólares taiwaneses al mes, y dos meses de depósito.',
  'Viajero: ¿Se paga aparte el agua y la luz?',
  'Agente: Sí, y el contrato es de un año.',
 ], [
  "Guest: Hello, I'd like to rent a studio.",
  'Agent: Sure. When would you like to view it?',
  'Guest: Tomorrow afternoon. How much is the rent?',
  'Agent: NT$12,000 a month, with a two-month deposit.',
  'Guest: Are utilities paid separately?',
  'Agent: Yes, and the lease is for one year.',
 ]),
 ([
  '旅客：房東，我的[水龍頭][漏水]了。',
  '房東：不好意思，我請人來[修]。',
  '旅客：謝謝。請問什麼時候[倒垃圾]？',
  '房東：晚上七點，在樓下。',
  '旅客：還有，我只有一把[鑰匙]。',
  '房東：我明天再給你一把。',
 ], [
  'Viajero: Casero, el grifo está goteando.',
  'Casero: Disculpe, voy a mandar a alguien a repararlo.',
  'Viajero: Gracias. ¿Cuándo se saca la basura?',
  'Casero: A las siete de la noche, abajo.',
  'Viajero: Además, solo tengo una llave.',
  'Casero: Mañana le doy otra.',
 ], [
  'Guest: Landlord, my faucet is leaking.',
  'Landlord: Sorry, I will send someone to fix it.',
  'Guest: Thanks. When do I take out the trash?',
  'Landlord: At 7 p.m., downstairs.',
  'Guest: Also, I only have one key.',
  'Landlord: I will give you another one tomorrow.',
 ]),
]

SORT = [
 ([
  '旅客：你好，我想看這間套房。',
  '仲介：好的，請跟我來。',
  '旅客：房間有冷氣嗎？',
  '仲介：有，也有熱水器和洗衣機。',
  '旅客：房子離捷運站遠嗎？',
  '仲介：走路五分鐘。',
 ], [
  'Viajero: Hola, quiero ver este estudio.',
  'Agente: Claro, sígame.',
  'Viajero: ¿La habitación tiene aire acondicionado?',
  'Agente: Sí, y también calentador de agua y lavadora.',
  'Viajero: ¿Está lejos de la estación del metro?',
  'Agente: Son cinco minutos caminando.',
 ], [
  'Guest: Hello, I would like to see this studio.',
  'Agent: Sure, please follow me.',
  'Guest: Does the room have air conditioning?',
  'Agent: Yes, and also a water heater and a washing machine.',
  'Guest: Is it far from the MRT station?',
  'Agent: It is a five-minute walk.',
 ], 3),
 ([
  '旅客：請問一個月租金多少？',
  '房東：一個月一萬二。',
  '旅客：押金要付幾個月？',
  '房東：兩個月，租約簽一年。',
  '旅客：租金包含水電費嗎？',
  '房東：不包含，要另外付。',
 ], [
  'Viajero: ¿Cuánto es el alquiler mensual?',
  'Casero: Doce mil dólares taiwaneses al mes.',
  'Viajero: ¿Cuántos meses de depósito hay que pagar?',
  'Casero: Dos meses, y el contrato es de un año.',
  'Viajero: ¿El alquiler incluye agua y luz?',
  'Casero: No, se paga aparte.',
 ], [
  'Guest: How much is the monthly rent?',
  'Landlord: NT$12,000 a month.',
  'Guest: How many months of deposit?',
  'Landlord: Two months, and the lease is for one year.',
  'Guest: Does the rent include utilities?',
  'Landlord: No, they are paid separately.',
 ], 6),
 ([
  '旅客：房東，我下個月要搬家。',
  '房東：好的，請提前通知我。',
  '旅客：我已經通知了。可以來檢查房間嗎？',
  '房東：可以，明天下午我過去。',
  '旅客：請問押金什麼時候退？',
  '房東：檢查沒問題，一週內退給你。',
  '旅客：這個損壞不是我弄的。',
  '房東：沒關係，我記下來了。',
 ], [
  'Viajero: Casero, me mudo el mes que viene.',
  'Casero: Bien, avíseme con anticipación.',
  'Viajero: Ya le avisé. ¿Puede venir a revisar el apartamento?',
  'Casero: Sí, mañana por la tarde paso.',
  'Viajero: ¿Cuándo me devuelven el depósito?',
  'Casero: Si la revisión está bien, se lo devuelvo en una semana.',
  'Viajero: Este daño no lo hice yo.',
  'Casero: No hay problema, lo anoto.',
 ], [
  'Guest: Landlord, I am moving out next month.',
  'Landlord: Okay, please notify me in advance.',
  'Guest: I already did. Can you come inspect the room?',
  'Landlord: Yes, I will come tomorrow afternoon.',
  'Guest: When will I get my deposit back?',
  'Landlord: If the inspection is fine, within a week.',
  'Guest: I did not cause this damage.',
  'Landlord: No problem, I have noted it.',
 ], 5),
]

REVIEW = ('你住哪裡', '你的房租多少', '你喜歡你的房子嗎', '租金', '押金', '房東', [
  '你住哪裡？ ¿Dónde vives?', '你的房租多少？ ¿Cuánto pagas de alquiler?', '你喜歡你的房子嗎？ ¿Te gusta tu casa?'])
