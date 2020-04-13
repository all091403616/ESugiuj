from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from time import sleep
import time
import random

api_id = 1093774
api_hash = 'a3aa7d1efa3f4766aab4685a87ed8721'
phone = '+19806006814'
client = TelegramClient('session_name', api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

users="""omid_zarei77
Zahra_s_Azimi
Reza9351678
Mazyarhaghighi
GEMAKZ
mahn_z_56
RezaeiZahra
f1543
szarinpar2
Zahra12aa
Zzsssszz
Nima_Subzero
amirmahdizoodbin
jslclrv
alire_za_219
Zffmz
Zartosht_sh
Zashbkkncrg
Srpohyra
Zxfookk
zzzrrr123456
Zadrtyu
Zahra_abedi25
Zo_1095
znvhbh
Zero_0day
FaRadsnii
Zara_art0
Siavahhassanzadeyekta
Zara19922222
Zah08755
Zarifo
zahra_joon1398
parisa1324
z_hamideh
Zahraw888
Zenaapep
Zeynab_aya
zzkdff
rexyr
NimaaZdi
ali02430243
Zhra31
Arian8131
Zemensoi
Hamed_a_m_z
zobeirbehi
Zaarttoshttii
Zendegy135
zjhgf
leexxiii
Zahra7310
Aa_znd
ParavanehTSDKbot
yasna7782
Ali_y_a_84
REZ20201
Saye_78
i_love_you20
Shayan_khannjad
Yusef543
Haniiiiiiiiiiiiiiiii
yek_fenjan_ketabb
Nawid1381
youne1382s
Yashar_k_sh
Yousef6690
YADAGARYAMY
yazdan0022
yasaman_gh693
YoBoiShyn
yasin1122334455
elyasyk
Shayan_ys1380
yanliz137n
TACIAM
Yaskabod74
yyaallddaa20
yasertorabi
yosimm
yanliz76m
Younes3262
yasbehmard
yoyo0092
Oun_ye_pesare_bade
Loveandpeacebarber
yadegar2013
yosef87023
RB617
Yalda2009
Yazdani_Elmira
Yunes_Isa
Yaser9m
Armin_Yarie
xxxcxxxcxxxcxxx
seti_x
XxSelinxX
Xanialll
x8x900
meetmem
xfy74tduuffy
xgblteam
Xxxxxxxtfff
xlarf
Wewilldie04
WkStm
wanna_go_home
World_131
I_dont_know_what_happend
Amir_wxo
wshgwwh
Woow_000
A_K_Wins
wswr23
No1nn
ALIW736
aphoool
Amir_wolf_hp2002
Wizard6087
W0rm_cl
moradi335
Wwsayd81
W4449
wr_sylvanas
Wayfarer72
wxvxw
WfiHack
VahidAhwazi11
Vahidjodati
VeryGooooodboy
vahed0825
vickyiiiiii
viperbeauty
VampireLp
Vahidm29
Vcguvfub
Vcf5e7
moein_vha
Mr_VaMps
MHRDD_VLIZDH
Mr_jajli
VONMM
Mv652
a_m_b_volleyball
Vafa_6868
virgo_029
Vvo00ovV
vel_hakennn
emin_var
Shadmehrvahid
venimh
vahid77f
ali1934victor
M_o_h_s_e_n_m_a_g_h_s_o_u_d_i
Ubses
Unknown_656
Udiid80
Fatiii_u
unique_gamenet
ksudi_us
ungage
mahdidavri
to_r_n_a_do
sajjad_turkoghli
telesmat135
Mil_tah
Tanazmmmmm
Mahdi0097mt
Tatali78
TOOrabi2020
PRO_th
takrooou
Peyman_tm021
sina_turk87
samira_tab23
tabriz64
Mahditahmasebibbbb
Tabchipretty
Saafffaaaa
projekaran_team
Rezat29
FarivarJafariTehrani
kiana_1_9_teh
MeHdI_torkamand
shiri0991
negin_tehran23
ttttiiinaa
Shahriar800
Trsnakl
tanha1380
Mahdi_TBI"""
members=users.split('\n')

target_group = client(JoinChannelRequest(channel='eshghkade_18'))

target_group_entity = InputPeerChannel(target_group.chats[0].id, target_group.chats[0].access_hash)

i=0
u=0
flag=True
while flag:
    user_to_add=client.get_input_entity(members[i])
    if i ==len(members)-1:
        flag=False
    try:
        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
        print('added: {} -> {}'.format(str(i),members[i]))
        u+=1
    except Exception as ex:
        client.send_message('@Ashoj79','not added {} beacuse: {}\n'.format(members[i],str(ex)))
        if 'Too many requests' in str(ex):
            s=time.time()
            ss=int(s)
            ss+=7926
            print('start again at : '+str(time.ctime(s)))
            sleep(7891)
    i+=1
    if i%50==0:
        sleep(random.randint(800,1000))
    else:
        sleep(random.randint(100,200))
print(str(u)+" members added")
