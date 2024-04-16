from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt
from gmpy2 import iroot


n1 = 125267411676839013904356880992044234494446196964982422223130579882047339346910691451497681975351838034684254305738613386927222900898672184001345811471784343779083336010063097729870079645284178978512325038316112509718505547104307526489798594871208559607331790920412305711830820739308995357441030646151241475357
e = 3
c1 = 53377681151597930200174280269480737905892580547675095951568028531545776989476273786562435486230550919422086944133253611872983670236114054374565938184593173194919064517779661178744278071496565181181705071524501841159717567250259220092464925447795412484629687708208662079791459184303259833667333882817260906165

n2 = 101985110329687359982214188967281711679876126442294375297547334583432698756724057183438691227371260175904715854057793173086301783390154807726779286131084537704721881438398569476214173211311977143694032174701007005033830070482491565424683664984059187439768982994371382763048098663670188786016786612348042190633
e = 3
c2 = 86370003324603283962938004647941072863866893771153362222202759619566185050496089684606274416415418388916028237984708280964054009059814813483639010674182298294505525549842057730933691736372086557397211586739691237738757897947336698446258197604918828646265244195686107866422922575275382813594250335044143485624

n3 = 83259448903366278561128205003734328779222118906091604625605804813528274055482582431201682767294594942491788720967344243567819654813240542076250030802111361571504667752481579915864184180358691091092122509649590043074189547962292835856503625214027405901620103615424259796442446412031011575671410630232956892267
e = 3
c3 = 25601241268900087228853235319569275926328919786631787991019848828558430219449358810095537362492238844266084660904521793373698736119824512458196492049138821633273765102576368573691391116632126183996786969554104441242376959688329346567745607825277943462236901478944551669406261301309719409165457168678763092118


m = crt([n1, n2, n3], [c1, c2, c3])[0]
m = iroot(m, e)[0]
m = long_to_bytes(m)
print(m)

# b'This is your destination: "https://pastes.io/1yjswxlvl2"\n'

# pearl{g00d_j0b_bu7_7h15_15_4_b4by_0n3}
