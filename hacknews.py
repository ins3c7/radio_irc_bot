#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# HackNews IRC Bot
# Coded by ins3c7 and Zirou
#
# Coded for Priv8 Server
#
# Thanks xin0x, hc0d3r, HyOgA, idz, chk_, vL, VitaoDoidao, psycco, PoMeRaNo and all the #NOSAFE family.
#
# Let's Rock! ;D
#
#

import json, os, socket, time, base64, sys, threading, random, urllib2
import unidecode, requests, BeautifulSoup, tweepy, facebook
from imgurpython import ImgurClient

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

reload(sys)
sys.setdefaultencoding('Cp1252')

os.system('clear')

class HackNews:

	def __init__(self, server, port, nick, name, email, channel, ajoin, admin, prefix, verbose, banner, xplAlive, owner, Imgur):

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.s.connect((server, port))
		except:
			print 'ERRO: Não foi possível conectar ao HOST: {} e PORTA: {}'.format(str(server),str(port))
			time.sleep(5)
			exit(1)

		time.sleep(0.5)
		self.s.recv(4096)
		self.nick = nick
		self.name = name
		self.email = email
		self.channel = channel
		self.ajoin = ajoin
		self.admin = admin
		self.server = server
		self.prefix = prefix
		self.verbose = verbose
		self.banner = banner
		self.xplAlive = xplAlive
		
		self.owner = owner
		self.Imgur = Imgur

		self.portscan_find = False
		self.data = ''
		self.command = None
		self.close = False

		self.followers = ['nickwho55','a_gooodz','Alex_Palmer5','Zackdetweiler','MoolaJay','SunnyKh56188551','toyofalger88','live_ahh_myra','MariiRo29764918','Mohamed65901521','JohnYouTuber1','yungxpolo','k3n_sh1n','suzan_szz','raufa_saeed','defensiveduck','Frases_Kali','thesecretjockey','AlejandraZanc12','canaltodiboa','Xpiris_','Palmosnews','klanad2','Himansh015','d2smoove__','JGF357','myersdestiny878','DaianeFlaju','iteexam','Richard_Lollo','dailykoma','Naomikn47600517','tommytizzy1','kwstaskaietsi','antkajiki','Flajulietes','stavaresaa','InfidelWorld','OTLSPORTS','in2bassguitar','Mc1993Daniel','rustygreen59','Syriabetween','the_guruman','Fixer1_','Global_Kitchens','sOPacORniO','EZ_Krahlin','naysha_xetri','LynStanleyFANS','FahadShah829','JazRiveraV','DanielBrasilia','CssInfinity','zesty_warriors','Ri2n0h2','T4gUp','imreisy','YingNuiC9','correiopratodos','duda_della_Bian','dori_jonic','VisualMaster69','NicoleMak00','ahr_limbago','RoseeRayy','AJGAMING02','EyesTrib','HellenO69','thedamndad','ManishT29588381','TeRRy_Tsak','Alina_DOOD','antikouvas','dallas_rafael','katelynfrary','EciFaithlykah12','Savannahhoove16','sontshikazie17','EIlmohh','mandithavaz','Leryapereira01','jnr_tugah','BlaxLee','ManuzinhaPerez6','loirinnha_meiga','VicToria_1151','AriasJannier','1907yigitFB1','KethylaCarvalho','sodiq_salith','leadintogold','Dibiaggiogois1','goalkeepergoico','lacroudevez','BraveVega_','BraveSaamihszer','BraveLeaves','BraveNyel','GusArtistry','artofdmnd','Turnlolrt','Kxbzor','SW__world','kaahbutera1992','official_diomer','deyse_maria12','perao57','AlbiDeak','bobby_lorenzana','nuntendi','lindacortezmai1','Erlei005','erikardahlberg','FrancisPouhe','BraveAnthonyy','TorenceZawan','MadamDaminKowts','paixao_susana','dim_lionths','51c15953aa6048c','LiberioApdeAbre','miraclesndfaith','jsilva980','AnimalAbusers','seekdivinetruth','SomersetBean','1withtheplanet','0x736A','areyou_awake','hackerfantastic','itsaNewDay2day','chico_apache','sagitaire69120','missuhappybird','MatocNation','FreeMattDehart','northwind1ndn','AnonyRenelution','FuxNet','LauriLoveX','ImTheShmoo','canadianglen','BladeNeon','SanityBell','IdCountryGal7','ins3c7','ZZFCbr','amt1945','i12shares','loretta66004507','karinawhitehe15','BraveSyndicate','chrisshort74011','marcellowd7','matildalove2151','Risqify','norakr4mer','F_B_R_','cassand04350096','MrMaintainit','lmorrellhopa','BessieKnightq','SamuelWilke','evaparrish1948','freeshare3','johnrosa29171','LexOneGTPS','randomheartss','best9facts','bl2_leonardo','Dyce_Music','MerrileeGeer','ethical_Sec','HeadbandO','more_fun01','ate_vc','DomBouillet','TamaraSka7','straysneedlove','Catgirl0818','luansantana','reddogsusie','kaylama54674519','EddieZ71','BH14Detainees','rapifireio','Sn4k3_Mind','postkneejerk','BottecchiaUK','mokime7_lisa','native_shamrock','Cheyenn09354958','dan_gosforthcc','Chief_Tatanka','N8tiveWarri0r','alexmulatinho','mikakiwanini','TheRealYoG','ChirliAmancio','HausderWunder','zerocx_uk','AmyGarnerTweets','qbitcc','easterbunny312','rotrujo','incawarrior','Paw_Printz','HardTimesClub','apps_haven','RioRadiantStars','WakeUpMFers','streetskitchen','cherrivarisco','evelyn_m_k','Angelou45328491','alicialoughlin1','couragefound','KaalGroup','notaxiwarrior','_Anonymous_swe_','deathonaplate','powhatannative','hytrade','dolphinshelp','GothgrrlParker','Oz_catness','stoptaijikillzo','t0p_100','saveallanimals2','Smgh4Susan','0x680x690x67','KarinBorjeesson','StlGal_36','natonewman','C1TYofFL1NT','RealFKNNews','AmericanIndian8','censorednewsnow','GeorgeBearClaw','YourAnonNews','justice4cephus','hackerinfozone','AnonTrumanSec','giselle1900','SusanDuncanolp','MIMI_A1067931','MemPetsAlive','DogsRuleNC','MuellerDebi','edmartinsjr','MeowMiya88','Catherine_Riche','stwissmann','jijmpel','DogRescueTweets','speedy23567','_Cryptosphere','AnonBlackflagz','Delo_Taylor','steve_sps','myhackerhouse','TruthIzSexy','PerroneAngelika','OpChemtrails','IntelGroupGlobl','skycranewife','HAX','CassandraRules','JonnyRocks_BR','tigressuk','NoLove4USGov','CommanderXanon','susanmcgraw88','NonaLishus','fiondavision','c5d1b2025a3e4f0','LikeASir___','bibi_soso42','mindcanyoncom','smcarrs','OpSeaWorldAnon','_FeralGirl','AnonUKRadio','AnonMohandas','XDEVASTATEDX','CorinaRK','anonycast','charliemamma2','PaulJDeHart','jilleeeebean','GuckyTheGerbil','Ivy_Middleton','Mark_S_Aldrich','GoogleExpertUK','freeanons','GandhiJump','88blackhatss','Leann02','kathy_simonik','JuneStoyer','Monsterbuddy_','SaveAliAlNimr','AnonswedenInfo','RJennromao','kittyhundal','peteswildlife','JornalOGlobo','ActuallyNPH','kanyewest','TheEllenShow','inspirou','britneyspears','trutherbotbrwn','smullin02','PriscillaLakerv','AnonOpBeastBot','trutherbotsilve','TheGilbert23Mom','calfune','ruthmen','MIPooh','WinglessBird_','SoulsDefence','TKrypt_','TheRealToriNYC','michele19373444','gypsyjacs','lillabet1952','BrendaPerrott','Raluca_Florea','RuthDSegura','Crabbiez1','heavydemon2012','awkward_1110','morwennajh','chgyn','fionacrarey','DebbieMcqueen11','RayJoha2','ANONYMOUSX51820','Dakota7075','dogsrppltoo','YokoToTheRescue','Misty_Blue7','Rockdeverdade','KennaSecurity','LeiSecaRJ','dois_dinheir1','ivsonburatto','adaircommodo','_fgd1','StrategicSec','AnonymissCrazy','LeandroJungles','Cyber_War_News','bitormetal','LykordzSec','Hebr0n1337','dglife','d3m0l1d0r_','anon_guerreiro','News2Tor','KDTrey5','kourtneykardash','ladygaga','KylieJenner','opturkey2','justinbieber','RedeGlobo','felipeneto','SignosFodas','frasesdebebadas','CAPRICHO','FrasesDeRenato','marcosmion','RecitouOriente','rockinrio','DaniloGentili','Adele','LaskalaHackerTM','50cent','El14sJun10r','TanyaInAlameda','trutherbotwhite','ANONShadeSeptem','An0nKn0wledge','trutherbotgray','4nbltruths','trutherbotgreen','Peregr1nu5','trutherbotblue','Protect_Wldlife','_Heidi_13','sophiacrews','MaalikR3l0aded','FAQinCongress','wawwoski1','Kaidinn','InfoSec_WC','NubsAnimalWatch','Sanguinarious','Wildchick1a','tweet4cetacea','gaviota330','CyberToolsBooks','ginachron','yocomu','Maree71439592','yeti_001','dianne_bromley','Islandgirl_Rita','AnonJackAzzz','Aldana_Angel','LeiaSkye1','Beleafer1','sphelan4594','PittBullWarrior','MCAnews','HackerOrientado','clandestine4','_AnimalAdvocate','Gdad1','Krizachs','Z0mbieGh0st','AnonyChange','AnonymissStar','AnonymousJobsUS','Lous666','CampsTravel','srtadrenaline','marcolini_penha','MrNegroMilitant','in_shad0ws','NN2ed_s4ur0n','gurudovale','Jhaddix','judithpoe','seafoambay','Drake','ZanteStrays','cmsNetherlands','m3rry_an4rchy_','VsbRth','Z3rou','grm_chikn','trutherbotpink','dileo_karen','katrinabeach19','TheDailyShow','BigSean','iamdiddy','BrunoMars','Makeeasymoney19','Tip','UberFacts','POTUS','NBA','blakeshelton','YouTube','CNN','realDonaldTrump','KendallJenner','ConanOBrien','selenagomez','ArianaGrande','khloekardashian','nytimes','wizkhalifa','MileyCyrus','rihanna','NFL','jtimberlake','danieltosh','katyperry','KevinHart4real','cnnbrk','KimKardashian','espn','jornalnacional','taylorswift13','BarackObama','GloboNews','SportsCenter','Estadao','jimmyfallon','VEJA','globoesportecom','TiagoLeifert','oserginho','juliococielo','VoceNaoSabiaQ','neymarjr','marcoluque','SabrinaSato','luscas','LucasRanngel','Anitta','MarceloTas','CaioCastro','FabioPorchat','VibePositiva','LucianoHuck','RecitoBobMarIey','majutrindade','humdaora','relatojovens','Pitty','rafinhabastos','naosejatrouxa','ivetesangalo','Tatawerneck','jorgeemateus','pefabiodemelo','SintoniaVerso','ClaudiaLeitte','Legendarios','programapanico','moixsec','gusttavo_lima','Pontifex_pt','TheAnonMovement','anonzeus3','HackingTutors','h0t_p0ppy','_RektFaggot_','WauchulaGhost','Socialism4Jobs','trutherbotornge','MccuneD37','AnonyMiss2209','artyHannah','Knicks_Feed','tyboogiebeats','_Rodrigoquadros','chsafe','ExtraHop','LisaRM_B','_gsv','CheCommodore','moham1391','albertomozgz','M_A_N_U74','rehan_yousufzai','netcajun','Guille_Hartek','OpenNSM','Anon4dolphin','ferbalos','_tarcisio','MUI_jovi_anon','PalAnonymous','jwbranda','Honoka_enbot','DjBrujo','FrugalGlobal','manimalvinyl','semanadolinux','lloyd8kristy','SMBDigitalMedia','xPolymorphiax','AgilityForex','kiranbogati71','miniparfumsmall','KC8GRQ','Marlonfer10','whitehatsec','brentmdev','Sam___Hurley','CryptoBullionX','pythontrending','ShadowFiend691','AnonForAnimals','hackandbeers','AnonIsis','greennomad61','GridCyberSec','Tio_Vampyryty','OpenstackRR','CProgram_app','pitwar2022','ItIsAMovement','NyuSecurity','CampuseroClub','Uroubouros','maldevel','hacks4pancakes','Elverojaguar','M_R_TEMPEL','h3xpos3d','SysAdmHowto','motisecurity','InfoSecHotSpot','xxx_m4h','TechInfected','LoukasKaramp','FreeLauriLove','Hypolytaviola','FMSepulveda','Sprek3rsSec','DumpAnalysis','TutanotaTeam','jlist','RHYNOnetworks','loridowney3','0modelolz','BSidesLatam','BalaozinhoOFC','free_anons','trutherbotred','TheVengeant','syberk','Yisa_Lal','hacker_center','MsAnonGhost','aka_Gb','AnonyOpTurkey_','H4ckint0sh_','OpHunAnon','rebel_raven_rdn','TobitowTHA','samikarahan42','Red62azazel','Input_d3vices','Ch3z15m3','turk_time','ilona_57','ChingonRasta','eddie1971nyc','SunR1zSec','AnonyOpBEAST','9h057','AnonymousDaisy0','TropicalAussie','Mr_Anonymous22p','an0n_ym0u','Scr1P7_py_B07_','Gal10n','val_4n0n','r5_black','RedFactionX','OpTrumpTruth','guerrilla_black','trutherbotgold','turan_ordu','WilliamlDotson','serialhaxor','Campuseira','Ninjaacr13','fabaof','t0ny_0x','rootsystem2010','enr1g','MrSagarBedi','peadorn','UnknowSec','kraken_kall','Epl3sh','fidelissauro','madcatownz','0x27null','Alias_PadaWan','brunorocha932','noobbugs','ZeroSnuup','leonoar','r_bisao','RuanAragao','coffnix','CheckSecure','bl4d33z','ocixela','lnmesquita','WebResearchTool','wivysmiguel','mindukk4','birdfreesky','jeffersonbrun0','mesrine_29','msl_tecnologias','casimiroabate15','4st4r0th_d3m0n','StStasi','Zeero404','LastMalware','jayro_lopes','AliSniffer','iamfitog','Strato162','blendermito1999','SSHROCKS','MtrSI','rndm25','vizhhu','LouisDaniel_bro','massimozanchi','DrSHA67','ZoiderSec','triippy_zay','sfteamsf','earicc','St4nWtb','sk8alado','MrKryptonet','_diegobecker_','Tiberius8','overcyber','defsecnsattack','by_Daniel','Vinicius_MafiaM','tchweize','l4_v0lpe','_VictorXisto','1B4nksy','blackman4040','wc4d3r','Z1ph0x','Willbugs','Apress_Fredoom','_s0ph0s_','deex36','Pica_de_aco_699','og_ginger43','Ir4qu14n0','fwhibbit_blog','CheshireCatJr','Down404','vladinc_uk','GustavoGuhGame','TheMobCyber','mu7ammadhawlery','BhikharamJeen','xina1i','12th_cl','piflag','ComteCodix','FreeGaza65','alcantaragui89','Gubi_Uknoun','1nc0gni7o_h4x0r','rvkiran799','TCrypt1','fuckintrashbag','PartidoPirataBR','phdigitos','_niourk','_jrmaster','N1n4_M00r3','lnxm4n','AnonN1NJ4BR','UnlockUnknown','mathStanley','iierr0r','Kazooza1','jcgfreitas','ChristopheCelio','FrancEstudillo','matutin','mercenarymba','TycoSecProTech','bl0nd1n','zaid_Almokhtar','fiercecyber','kukhyun_lee','g4ngst4s3cur1ty','sanskarmodi_','AnthonyGrandle','6ab0_17','TechhouseIT','Jesukrusty','Katadhin','Miremiau_','shnoogie_','jasonericgroves','TeachPrivacy','garimella_vinay','citywidemesh','Matt_Ridgway','brianrcollette','poulgar','xajckop','SizzlinWizzlin','DarrylLampert','phd_phuc','simon0117','sleyckttor','freebitflow','brza37','albadi1992','buttsmithprolvl','ArdianBajraliu','Lodags','steve_mtb','HG_Jeannine','a4funk','sherilyn321','Libre_Rouamba','yjd333','Chukpadeh','iZacRoy','wuyonglala','merlinuxs','TheBradmonster','1369833786Nick','JakobHarrison90','AvijitNoyon','Mansi1526','habilfathan13','Rabeamax','AdliTassak','Aliirani1990','sanfander','zaheerchoonara','SeifHateb','krober_biz','WetEvents','geekyfreaky30','ded5ec','Inarcangel','aicha_styles','Scholsey86','FSUlaurakelly','BuyukkayaArda','_thekey_','GeoPolitikon','Nightwindzero','jan_968','2somi1','trylinuxos','abakymich','paulhschwartz1','hieuxinhe94','qntmpkts','cyb_c1ph3r','amador_aqp','zinking','ddn_hacker','infolooksol','twtr_jim','chriskerstiens','AtsonWin','itshiteshchopra','FrancisckLam','NinhaSosa','peddycoart','SATSathish0','DreamingLoveJoy','wattsderro','ArnaudKleinveld','mnawrath','jhlim90','justink32143145','d43m0n3y3','techjacks','Karine_doc','TorelloJeff','nipunshihara','RZimmermeyer','JHesselbarth','Entrepreneurix','Mirwitch','astral_lights','SnoopysBerry','juangares','FS_CTI','KadoyoJr','alvaroandresmc','alaeaqi','JuanDavidB','kiyocchi_','obscuredsource','MoussalliAli','venky18m','wilofice','ycjkang','luocaodan','vaalmelzu','Phishing_Bear','whisteo','wajahat_etc','Eddini81976','sp0k3zan0n','PortilloHector_','pmendezgjr','Aaqibhus','flashcrash619','handwashcold','lolxJT','Thronelife38','Muheebwah','DTSChina','1eesec','B0bby_RS','Hr0wp','FavazzaVincent','JeremyFrois','DDosScripts','markusvandeep','Chillentito','5fruits','l3n6m0','u_s_3_r','master_kula','NanashiEra','anasmuharris8_n','peacefulanimal','piiiles','Abhie11280708','assbot1234','beethesurfer','CnwillSec','rockingusername','ECsasar','ipersona','kic_ae','d3falt_r00tman','AnonSynx','AlisonGloede','tw_early','pedrogomis','xor_function','biasys','d14turbo','woahgabe','PrestigeCode','mathmare_','sabrynacode','SylvieGagne4','dinn9012','wrayder','wiref4lcon','An0nSoHr4D','goto0026','ju1cy0x00','sallery1','demonolith','ThePigeonOfTime','PhoBokChoi','Dark_Sigil','Decelist','MrBenSpring','gregorgoyo','wismartzy','TahirKilinc','sergibarroso','Y4r4G_','Viktorlmpersson','tariqwrt','Med_Alch','jaradatmusa','kaganisildak','GGransby','Moryan37','kevi_sutton','abdoudiagna','KyleMarshIT','CoreSentinel','viren1311','PasulaDeepu','Merozey','Atif7rbi','slntmile','daniel427','sqli_wiki','Cor3Zer0','morwnbrg','Kelelefuq','Do0zy8','abo00odsy','chernobylmega','f000000l','TheWikiBoatBR','Msaliiih','_Kinka_','RasrizalRosdi','musa_sana','JoyceJames666','altayyldz','DGML0','GloBalAnon32','bolajiogidan','tarbaha12','securityinject','MKedrick','Its_Ani_Friends','iFhd5','dkordyban','darthguinea','JoseAnt72860048','auben3','emmanuel_idachi','MildzQn','asdisalnum','BDBenzir','CaraOriel','blockchainadv','0xdays','aaronvan1964','mileycasindra9','Zafpyr']

		self.log_dir = os.path.abspath('log')

		if not os.path.exists(self.log_dir):
			os.mkdir(self.log_dir)

		print '\nInicializando...\n'

	def SendCommand(self, cmd):
		comm = cmd + '\r\n'
		self.s.send(comm)

	def SendMsg(self, canal, msg):
		msg = msg + '\r\n'
		self.s.send('PRIVMSG ' + canal + ' ' + msg + '\r\n')

	def SendPingResponse(self):
		if self.data.find('PING') != -1:
			self.SendCommand('PONG ' + self.data.split()[1])

	def Logging(self, canal, nick, message):
		if canal == self.nick:
			canal = nick
		canal = canal.upper()
		f = open('log/'+ canal +'.log', 'a')
		f.write(message +'\n')
		f.close()

	def SendAllChans(self, nick, canal, message):
		try:
			for channel in ajoin:
				self.SendMsg(channel, str(message) + ' ')
			self.SendMsg(canal, self.banner + 'Mensagens enviadas. ')
		except:
			self.SendMsg(canal, self.banner + 'Algo deu errado. ')

####################

	def imgur(self, link):
		return self.Imgur.upload_from_url(link, config=None, anon=True)['link']
			
	def migre(self, url):
		return requests.get('http://migre.me/api.txt?url='+ url).text

	def face(self, canal, msg, attachment):
		token = 'EAAIQfgyFQkwBAABmx8L0ZAZCqeTGMeYXyQgP5wFfcl0L7dZCZBMfKXtu4PcpQUwtAVwfxQJZAeQw1ZC2dGekfxBCGxyztH0qGnAi6lZC5dSafF2lI5vJpWKpTKNAlaTVfdXZCO4gZAAlNpxwygdKauwHehZBbEMAhyO4RRUolpsiXtLwZDZD'
		graph = facebook.GraphAPI(token)

		graph.put_wall_post(message=msg, attachment=attachment)

	def tweet(self, canal, msg):
		try:
			cfg = json.load(open(os.path.abspath('')+'/cfg.conf'))
			api = self.tweet_auth(cfg)
			status = api.update_status(status=msg)

		except Exception, e:
			print str(e)
			self.SendMsg('ins3c7', 'DEF TWEET: '+ str(e))

	def marketing(self, banner, ajoin):
		while not self.close:
			for x in range(700):
				if not self.close:
					time.sleep(1)
			self.SendMsg(random.choice(ajoin), banner + 'Follow us on Twitter: 4https://twitter.com/nosafe_')

	def tweet_auth(self, cfg):
		auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
		auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
		
		return tweepy.API(auth)

	def news(self, banner, canal):

		url = 'http://thehackernews.com/'
		data = requests.get(url)

		soup = BeautifulSoup.BeautifulSoup(data.text)

		url_site = url.split('//')[1].split('/')[0]

		count = 1

		for post in soup.findAll('a', href=True, attrs= {'class':'url entry-title'}):
			if count < 4:
				self.SendMsg(canal, banner + '[14{}] {}'.format('NEWS', post.text))
				self.SendMsg(canal, banner + '[14{}] 4{} from 14thehackernews'.format('NEWS', self.migre(post['href'])))
			count += 1

	def news_(self):
		url = 'http://thehackernews.com/'
		data = requests.get(url)
		soup = BeautifulSoup.BeautifulSoup(data.text)

		base = []

		for post in soup.findAll('a', href=True, attrs= {'class':'url entry-title'}):
			base.append([post.text, post['href']])

		return base


	def news_mon(self, banner, ajoin):

		old = self.news_()

		self.SendMsg('ins3c7', self.banner + '[14{}] {}'.format('thehackernews.com', 'Initialized! Monitoring...'))

		while not self.close:
			print 'Checando THEHACKERNEWS..'
			try:
				new = self.news_()
				if new[0][0] != old[0][0]:
					for canal in ajoin:
						self.SendMsg(canal, banner + '[14{}] {}'.format('EXPLOIT', 'New Post!'))
						self.SendMsg(canal, banner + '[14{}] {}'.format('EXPLOIT', new[0][0]))
						self.SendMsg(canal, banner + '[14{}] 4{}'.format('EXPLOIT', new[0][1]))
					self.tweet(canal, new[0][0] +'\n\n'+ self.migre(new[0][1]))
					old = new
				print 'THEHACKERNEWS.. OK'
				
				for x in range(180):
					if not self.close:
						time.sleep(1)
			except Exception, e:
				print 'THEHACKERNEWS ERROR:', str(e)			

	def xpl(self, names):
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		data = requests.get('https://www.exploit-db.com/', headers=headers)
		soup = BeautifulSoup.BeautifulSoup(data.text)
		
		y = 0
		base = {}


		for table in soup.findAll('table', attrs={'class':'exploit_list bootstrap-wrapper'}):

			base[names[y]] = []

			for x in range(7):
				date = table.findAll('td', attrs={'class':'date'})[x].text
				author = table.findAll('td', attrs={'class':'author'})[x].text
				description = table.findAll('td', attrs={'class':'description'})[x].text
				link = str(table.findAll('td', attrs={'class':'description'})[x]).split('href="')[1].split('">')[0]

				base[names[y]].append([date, author, description, link])

		 	y += 1

		return base

	def xlp_mon(self, banner, ajoin):
		categories = ['Remote Exploits', 'Web Application Exploits', \
				'Local & Privilege Escalation Exploits', 'PoC & Denial of Service Exploits', \
				'Exploit Shellcode Archive', 'Archived Security Papers']

		old = self.xpl(categories)

		# self.SendMsg('ins3c7', self.banner + '[14{}] {}'.format('exploit-db.com', 'Initialized! Monitoring...'))
		
		while not self.close:
			# print 'Checando EXPLOIT-DB..'
			try:
				new = self.xpl(categories)
				for category in categories:
					if new[category][0][2] != old[category][0][2]:
						for canal in ajoin:
							self.SendMsg(canal, banner + '[14{}] {}'.format('EXPLOIT', 'New exploit available!'))
							self.SendMsg(canal, banner + '[14{}] Title: 15{}'.format('EXPLOIT', new[category][0][2]))
							self.SendMsg(canal, banner + '[14{}] Author: 15{} / Date: 15{}'.format('EXPLOIT', new[category][0][1], new[category][0][0]))
							self.SendMsg(canal, banner + '[14{}] Link: 4{}'.format('EXPLOIT', new[category][0][3]))
						self.tweet(canal, 'New exploit:\n'+ category +'\n'+ new[category][0][2] +'\n\n'+ self.migre(new[category][0][3]))
						old = new
				# print 'EXPLOIT-DB.. OK'
				
				for x in range(180):
					if not self.close:
						time.sleep(1)
			except Exception, e:
				print 'EXPLOIT-DB ERROR:', str(e)

	def ycombinator(self):
		url = 'https://news.ycombinator.com/newest'
		data = requests.get(url)
		soup = BeautifulSoup.BeautifulSoup(data.text)
		base = []

		for post in soup.findAll('td', attrs={'class':'title'}):
			try:
				title = unidecode.unidecode(post.text)
				link = str(post).split('href="')[1].split('"')[0]
				base.append([title, link])
			except:
				pass

		return base

	def ycombinator_mon(self, banner, ajoin):
		old = self.ycombinator()
		self.SendMsg('ins3c7', self.banner + '[14{}] {}'.format('ycombinator.com', 'Initialized! Monitoring...'))

		while not self.close:
			print 'Checando YCOMBINATOR...'
			try:
				new = self.ycombinator()
				if new[0][0] != old[0][0]:
					for canal in ajoin:
						self.SendMsg(canal, banner + '[14{}] {}'.format('NEWS', new[0][0]))
						self.SendMsg(canal, banner + '[14{}] 4{} from 14ycombinator'.format('NEWS', self.migre(new[0][1])))
					self.tweet(canal, str(new[0][0])[0:50] +'...\n@'+ random.choice(followed) +'\n\n'+ self.migre(new[0][1]))
					old = new

				print 'YCOMBINATOR... OK'
				for x in range(10):
					if not self.close:
						time.sleep(1)
			except Exception, e:
				print 'YCOMBINATOR ERROR:', str(e)

	def ycomb0(self, banner, ajoin):
		url = 'https://news.ycombinator.com/'
		while not self.close:
			data = requests.get(url)
			soup = BeautifulSoup.BeautifulSoup(data.text)
			x=0;base = []
			for post in soup.findAll('td', attrs={'class':'title'}):
				if len(post.text) > 5:
					title = unidecode.unidecode(post.text)
					link = str(post).split('href="')[1].split('"')[0]
					base.append([title, link])
					x+=1
					if x > 30:
						break
			print 'CHECKING YCOMB0...'
			title, link = random.choice(base)
			posted_file = open('news.txt', 'r').readlines()
			if (title+'\n') not in posted_file:
				link = self.migre(link)
				for canal in ajoin:
					self.SendMsg(canal, banner + '[14{}] {}'.format('NEWS', title))
					self.SendMsg(canal, banner + '[14{}] 4{} from 14ycombinator'.format('NEWS', link))
				attachment =  {
				    'name': title,
				    'link': link,
				    }
				try:
					self.face(canal, title, attachment)
				except Exception, e:
					self.SendMsg('ins3c7', 'YCOMB0: '+ str(e))
				self.tweet(canal, str(title)[0:50] +'...\n@'+ random.choice(self.followers) +'\n\n'+ link)
				
				post_ap = open('news.txt', 'a')
				post_ap.write(title+'\n')
				post_ap.close()

				# print 'CHECKING YCOMB0... OK'
			else:
				# print 'CHECKING YCOMB0... OK (N0THING)'
				for x in range(10):
					if not self.close:
						time.sleep(1)	
				continue
			for x in range(888):
				if not self.close:
					time.sleep(1)

	def hckrnews(self, banner, ajoin):
		url = 'https://hckrnews.com/'
		while not self.close:
			data = requests.get(url)
			soup = BeautifulSoup.BeautifulSoup(data.text)
			x=0;base = []
			for post in soup.findAll('li', attrs={'class':'entry row'}):
				if len(post.text) > 5:
					title = unidecode.unidecode(post.text.replace('&nbsp;', '').replace('&apos;', "'")).lstrip('0123456789')
					link = 'http://'+ str(post.findAll('a')[1]).split('//')[1].split('">')[0]
					base.append([title, link])
					x+=1
					if x > 20:
						break

			# print 'CHECKING HCKRNEWS...'

			get_title, link = random.choice(base)
			posted_file = open('news.txt', 'r').readlines()

			title_from = get_title[::-1].split('(')[0][::-1].rstrip(')')
			title = get_title.replace(get_title[::-1].split('(')[0][::-1].rstrip(')'), '').rstrip('()')

			if (title+'\n') not in posted_file:
				link = self.migre(link)
				
				title_pt = str((requests.get('http://api.mymemory.translated.net/get?q={}&langpair=en|pt'.format(title)).json())['responseData']['translatedText']).encode('utf-8')
				
				for canal in ajoin:
					self.SendMsg(canal, banner + '[14{}] {}'.format('NEWS', title))
					self.SendMsg(canal, banner + '[14{}] 4{} from 14{}'.format('NEWS', link, title_from))
				
				attachment =  {'name': title,'link': link,}

				try:
					print '...'
					#self.face(canal, '', attachment)
					#self.tweet(canal, str(title)[0:50] +'...\n@'+ random.choice(self.followers) +'\n\n'+ link)
				except Exception, e:
					self.SendMsg('ins3c7', 'HCKRNEWS: '+ str(e))
				
				post_ap = open('news.txt', 'a')
				post_ap.write(title+'\n')
				post_ap.close()

				# print 'CHECKING HCKRNEWS... OK'
			else:
				# print 'CHECKING HCKRNEWS... OK (N0THING)'
				for x in range(10):
					if not self.close:
						time.sleep(1)	
				continue
			
			for x in range(7800):
				if not self.close:
					time.sleep(1)

	def Parse(self, banner, canal, user, cmd):
		tmp = cmd.split()
		numargs = len(tmp)
		fmt = []

		if (len(str(cmd).split()) == 0):
			return
			
		command = cmd
		command = command.split()

		# for i in range(numargs):
		# 	fmt.append(tmp[i] + ' ')

		# if user in self.admin:

		########## FUNCOES
		
		if len(command) == 1:
			if canal != self.nick:
				if command[0] == 'help' or command[0] == 'ajuda':
					self.SendMsg(canal, banner + 'Bot under construction....')

			if command[0] == 'rehash':
				if user == self.owner:
					time.sleep(1)
					self.SendCommand('QUIT Like #NoSafe -> https://fb.com/NoSafe.Priv8 ')
					self.s.close()
					self.close = True
					exit(1)
				else:
					self.SendMsg(canal, banner + '4Você não tem permissão.')


			if command[0] == 'news':
				if user in self.admin:
					try:
						self.news(banner, canal)
					except Exception, e:
						self.SendMsg(canal, banner + 'Wrong!')
						print str(e)
						self.SendMsg('ins3c7', 'command news'+ str(e))
				else:
					self.SendMsg(canal, banner + '4Você não tem permissão.')

		else:

			if command[0] == 'join':
				if user in self.admin:
					if command[1][0] == '#':
						join_channel = command[1]
					else:
						join_channel = '#' + command[1]
					self.SendCommand('JOIN %s' % join_channel)
				else:
					self.SendMsg(canal, banner + '4Você não tem permissão.')

			if command[0] == 'part':
				if user in self.admin:
					if command[1][0] == '#':
						part_channel = command[1]
					else:
						part_channel = '#' + command[1]
					self.SendCommand('PART %s Let\'s Rock!' % part_channel)
				else:
					self.SendMsg(canal, banner + '4Você não tem permissão.')

			if command[0] == 'cmd':
				if user == self.owner:
					self.SendCommand(' '.join(command[1:]))
				else:
					self.SendMsg(canal, banner + '4Você não tem permissão.')

			if command[0] == 'tweet':
				if user in self.admin:
					msg = ' '.join(command[1:]) + '\n\nPosted by ' + user + ' from ' + canal 
					try:
						self.tweet(canal, msg)
						print canal, self.banner + 'Tweet posted in 4https://twitter.com/nosafe_'
						self.SendMsg(canal, self.banner + 'Tweet posted in 4https://twitter.com/nosafe_')
					except Exception, e:
						self.SendMsg('ins3c7', 'if command[0] == tweet:'+ str(e))
						pass
				else:
					self.SendMsg(canal, banner + '4Você não tem permissão.')

			if command[0] == 'fb':
				if user in self.admin:
					msg = ' '.join(command[1:])
					try:
						if msg.find('///') != -1:
							token = 'EAAIQfgyFQkwBAABmx8L0ZAZCqeTGMeYXyQgP5wFfcl0L7dZCZBMfKXtu4PcpQUwtAVwfxQJZAeQw1ZC2dGekfxBCGxyztH0qGnAi6lZC5dSafF2lI5vJpWKpTKNAlaTVfdXZCO4gZAAlNpxwygdKauwHehZBbEMAhyO4RRUolpsiXtLwZDZD'
							graph = facebook.GraphAPI(token)
							link = msg.split('///')[1].lstrip()
							
							if link.find('imgur') == -1:
								if link.find('.gif') == -1:
									link = self.imgur(link)

							msg = msg.split('///')[0] + '\n\nPosted by ' + user + ' from ' + canal
							picture = urllib2.urlopen(link)
							graph.put_photo(picture, message=msg)
							self.SendMsg(canal, self.banner + 'Posted in FACEBOOK 4https://fb.com/NoSafe.Priv8/')
						
						elif msg.find('###') != -1:
							link = msg.split('###')[1].lstrip()
							msg = msg.split('###')[0] + '\n\nPosted by ' + user + ' from ' + canal
							self.face(canal, msg, attachment={'link':link})
							self.SendMsg(canal, self.banner + 'Posted in FACEBOOK 4https://fb.com/NoSafe.Priv8/')
						
						else:
							self.face(canal, msg, attachment={})
							self.SendMsg(canal, self.banner + 'Posted in FACEBOOK 4https://fb.com/NoSafe.Priv8/')
					except:
						self.SendMsg('ins3c7', 'if command[0] == face'+ str(e))
						pass
				else:
					self.SendMsg(canal, banner + '4Você não tem permissão.')					

			if command[0] == 'social':
				if user in self.admin:
					msg = ' '.join(command[1:]) + '\n\nPosted by ' + user + ' from ' + canal + '\n\nhttp://priv8.jp'
					try:
						self.face(canal, msg, attachment={})
						self.tweet(canal, msg)
						self.SendMsg(canal, self.banner + 'Posted in Facebook and Twitter.')
					except:
						self.SendMsg('ins3c7', 'if command[0] == face'+ str(e))
						pass
				else:
					self.SendMsg(canal, banner + '4Você não tem permissão.')	

	def run(self):

		self.SendCommand('NICK ' + self.nick)
		self.SendCommand('USER ' + self.nick + ' ' + self.name + 
			' ' + self.email + ' :' +
			base64.b16decode('507974686F6E20426F7420636F64656420696E2050726976382F234E4F53414645'))

		joined = False
		self.xplAlive = False

		version_check = False

		while not self.close:

			self.data = self.s.recv(4096)
			
			if self.verbose:
				print self.data

			if str(self.data).find('VERSION') != -1:
				exit(1)

			self.SendPingResponse()
			
			time.sleep(0.5)
			
			if str(self.data).find(str(base64.b16decode('2F4D4F5444'))) != -1:
				print '\nServer [{}] - CONNECTED! Thank\'s to use HACKNEWS BOT!\n'.format(self.server)
				self.SendMsg(str(base64.b16decode('696E73336374')), str(base64.b16decode('424F5420434F4E4E454354454421')))
			if str(self.data).find(str(base64.b16decode('6D7367204E69636B53657276204944454E54494659'))) != -1:
				self.s.send('{}'.format(base64.b16decode('505249564D5347204E49434B53455256204944454E5449465920317132773365317132773365')) + '\r\n')
			if str(self.data).find(str(base64.b16decode('50617373776F7264206163636570746564202D'))) != -1:
				self.s.send('JOIN {}\r\n'.format(self.channel))
				joined = True
				
				for channel in ajoin:self.s.send('JOIN {}\r\n'.format(channel))


			if str(self.data).find('PRIVMSG') != -1: # Confere se o dado recebido foi uma mensagem private ou para algum canal
				
				msg_time  = time.strftime('%H:%M:%S')		# Define a hora da mensagem
				user_nick = self.data.split('!')[0][1:] 	# Filtra o nick
				try:
					user_host = self.data.split()[0].split('@')[1] # Tenta filtrar o host (Variável ainda não usada)
				except:
					pass
				
				pre_user_msg	= self.data[1:].split('PRIVMSG')[1].split()[1:]	# Trabalha a mensagem bruta
				user_msg 		= ' '.join(pre_user_msg).lstrip(':') 					# Filtra apenas a mensagem
				user_channel 	= str(self.data.split('PRIVMSG')[1].split()[0])	# Filtra o canal

				print '[%s] %s %s: %s' % (str(msg_time), str(user_channel), str(user_nick), str(user_msg)) # Imprime a mensagem na tela do bot

				text_log = '[{}] {}: {}'.format(str(msg_time), str(user_nick), str(user_msg)) # Filtra o a mensagem para a função Logging()

				
				self.Logging(str(user_channel), str(user_nick), str(text_log)) # Grava os logs

				# Banner oficial:
				banner = '9(hACk4NeWs9) '

				try:
					if (str(user_msg)[0] == str(self.prefix)):
						self.Parse(banner, user_channel, user_nick, user_msg.lstrip(str(self.prefix))) # Chama a função Parse que gera todas as outras funções
				except:
					continue

			
			''' THREADS '''

			# market = threading.Thread(target=self.marketing, args=(self.banner, self.ajoin))
			# newsmon = threading.Thread(target=self.news_mon, args=(self.banner, self.ajoin))
			xplmon = threading.Thread(target=self.xlp_mon, args=(self.banner, self.ajoin))
			ycommon = threading.Thread(target=self.ycomb0, args=(self.banner, self.ajoin))
			hckr = threading.Thread(target=self.hckrnews, args=(self.banner, self.ajoin))
			
			if not self.xplAlive and joined:
				try:
					self.xplAlive = True
					# market.start()
					# newsmon.start()
					# ycommon.start()
					xplmon.start()
					hckr.start()

				except Exception, e:
					print str(e)
					self.SendMsg('ins3c7', 'THREADINGS START: '+ str(e))
				except KeyboardInterrupt:
					print 'INTERROMPIDO PELO USUÁRIO'
					self.close = True

			''' END/THREADS '''


#			self.SendCommand('NICK ' + self.nick)

			
if __name__ == '__main__':

	servidor = 'irc.priv8.jp'
	porta = 6667
	nick = 'HACKNEWS'
	nome = '#nosafe'
	email = 'hacknews@priv8.jp'
	canal_principal = '#netsplit' # Canal de comando do bot
	ajoin = [canal_principal, '#nosafe', '#priv8', '#1984']
	owner = 'ins3c7'
	admin = ['ins3c7', 'Zirou', 'xin0x', 'vL', 'hc0d3r'] # Nicks para acessos à funções especiais do bot
	prefix = '.'
	verbose = False
	xplAlive = False

	conf = json.load(open(os.path.abspath('')+'/config.conf'))
	Imgur = ImgurClient(conf['imgur_client_id'], conf['imgur_client_secret'], conf['imgur_access_token'], conf['imgur_refresh_token'])

	simple_banner = '9(hACk4NeWs9) '


bot = HackNews(servidor, porta, nick, nome, email, canal_principal, ajoin, admin, prefix, verbose, simple_banner, xplAlive, owner, Imgur)
bot.run()
