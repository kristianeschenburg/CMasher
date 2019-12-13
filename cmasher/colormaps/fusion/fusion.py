from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.15269566, 0.01594210, 0.06988881],
           [0.15825218, 0.01698613, 0.07448610],
           [0.16381559, 0.01801391, 0.07904903],
           [0.16938824, 0.01902024, 0.08357670],
           [0.17497227, 0.02000000, 0.08806795],
           [0.18056933, 0.02094854, 0.09252115],
           [0.18618125, 0.02186079, 0.09693475],
           [0.19180964, 0.02273184, 0.10130694],
           [0.19745571, 0.02355734, 0.10563546],
           [0.20312086, 0.02433247, 0.10991812],
           [0.20880647, 0.02505241, 0.11415254],
           [0.21451331, 0.02571326, 0.11833582],
           [0.22024232, 0.02631087, 0.12246503],
           [0.22599426, 0.02684139, 0.12653697],
           [0.23176973, 0.02730126, 0.13054822],
           [0.23756918, 0.02768731, 0.13449511],
           [0.24339322, 0.02799614, 0.13837386],
           [0.24924171, 0.02822590, 0.14218023],
           [0.25511451, 0.02837495, 0.14590987],
           [0.26101189, 0.02844103, 0.14955835],
           [0.26693291, 0.02842451, 0.15312083],
           [0.27287751, 0.02832433, 0.15659247],
           [0.27884443, 0.02814220, 0.15996819],
           [0.28483274, 0.02787955, 0.16324286],
           [0.29084134, 0.02753849, 0.16641124],
           [0.29686854, 0.02712298, 0.16946810],
           [0.30291252, 0.02663769, 0.17240825],
           [0.30897122, 0.02608836, 0.17522660],
           [0.31504239, 0.02548174, 0.17791823],
           [0.32112348, 0.02482582, 0.18047848],
           [0.32721154, 0.02413013, 0.18290307],
           [0.33330350, 0.02340514, 0.18518817],
           [0.33939638, 0.02266162, 0.18733027],
           [0.34548643, 0.02191286, 0.18932678],
           [0.35157038, 0.02117156, 0.19117542],
           [0.35764438, 0.02045243, 0.19287499],
           [0.36370491, 0.01976980, 0.19442473],
           [0.36974824, 0.01913910, 0.19582493],
           [0.37577077, 0.01857585, 0.19707658],
           [0.38176904, 0.01809548, 0.19818146],
           [0.38773974, 0.01771347, 0.19914209],
           [0.39367973, 0.01744507, 0.19996177],
           [0.39958615, 0.01730503, 0.20064439],
           [0.40545640, 0.01730756, 0.20119435],
           [0.41128814, 0.01746625, 0.20161659],
           [0.41707934, 0.01779395, 0.20191636],
           [0.42282828, 0.01830274, 0.20209920],
           [0.42853351, 0.01900391, 0.20217081],
           [0.43419385, 0.01990800, 0.20213703],
           [0.43980839, 0.02102481, 0.20200373],
           [0.44537650, 0.02236329, 0.20177660],
           [0.45089772, 0.02393184, 0.20146133],
           [0.45637175, 0.02573832, 0.20106358],
           [0.46179860, 0.02778978, 0.20058845],
           [0.46717826, 0.03009310, 0.20004129],
           [0.47251097, 0.03265447, 0.19942678],
           [0.47779699, 0.03547995, 0.19874971],
           [0.48303675, 0.03857509, 0.19801427],
           [0.48823063, 0.04190477, 0.19722484],
           [0.49337920, 0.04533361, 0.19638501],
           [0.49848295, 0.04885560, 0.19549855],
           [0.50354245, 0.05246016, 0.19456891],
           [0.50855829, 0.05613794, 0.19359908],
           [0.51353106, 0.05988082, 0.19259203],
           [0.51846134, 0.06368175, 0.19155052],
           [0.52334968, 0.06753461, 0.19047725],
           [0.52819668, 0.07143406, 0.18937444],
           [0.53300287, 0.07537552, 0.18824429],
           [0.53776881, 0.07935505, 0.18708888],
           [0.54249498, 0.08336925, 0.18591011],
           [0.54718187, 0.08741520, 0.18470977],
           [0.55182995, 0.09149040, 0.18348952],
           [0.55643964, 0.09559271, 0.18225093],
           [0.56101135, 0.09972030, 0.18099554],
           [0.56554545, 0.10387162, 0.17972470],
           [0.57004228, 0.10804535, 0.17843965],
           [0.57450218, 0.11224039, 0.17714162],
           [0.57892543, 0.11645581, 0.17583175],
           [0.58331227, 0.12069081, 0.17451137],
           [0.58766296, 0.12494477, 0.17318140],
           [0.59197769, 0.12921716, 0.17184282],
           [0.59625664, 0.13350755, 0.17049678],
           [0.60049995, 0.13781560, 0.16914425],
           [0.60470775, 0.14214109, 0.16778605],
           [0.60888014, 0.14648377, 0.16642339],
           [0.61301718, 0.15084356, 0.16505701],
           [0.61711892, 0.15522035, 0.16368797],
           [0.62118537, 0.15961411, 0.16231725],
           [0.62521654, 0.16402486, 0.16094574],
           [0.62921239, 0.16845259, 0.15957459],
           [0.63317286, 0.17289743, 0.15820467],
           [0.63709789, 0.17735940, 0.15683719],
           [0.64098737, 0.18183867, 0.15547315],
           [0.64484118, 0.18633534, 0.15411376],
           [0.64865919, 0.19084955, 0.15276021],
           [0.65244121, 0.19538149, 0.15141373],
           [0.65618709, 0.19993128, 0.15007576],
           [0.65989658, 0.20449916, 0.14874755],
           [0.66356950, 0.20908526, 0.14743075],
           [0.66720557, 0.21368981, 0.14612684],
           [0.67080453, 0.21831301, 0.14483750],
           [0.67436611, 0.22295502, 0.14356461],
           [0.67788999, 0.22761609, 0.14230996],
           [0.68137585, 0.23229639, 0.14107563],
           [0.68482337, 0.23699614, 0.13986380],
           [0.68823217, 0.24171554, 0.13867669],
           [0.69160188, 0.24645478, 0.13751682],
           [0.69493213, 0.25121406, 0.13638677],
           [0.69822249, 0.25599358, 0.13528928],
           [0.70147255, 0.26079351, 0.13422734],
           [0.70468187, 0.26561404, 0.13320407],
           [0.70785001, 0.27045535, 0.13222275],
           [0.71097649, 0.27531759, 0.13128691],
           [0.71406086, 0.28020092, 0.13040026],
           [0.71710262, 0.28510549, 0.12956671],
           [0.72010127, 0.29003143, 0.12879035],
           [0.72305631, 0.29497887, 0.12807554],
           [0.72596723, 0.29994790, 0.12742676],
           [0.72883351, 0.30493864, 0.12684874],
           [0.73165462, 0.30995115, 0.12634639],
           [0.73443003, 0.31498551, 0.12592479],
           [0.73715922, 0.32004174, 0.12558920],
           [0.73984165, 0.32511988, 0.12534501],
           [0.74247679, 0.33021994, 0.12519777],
           [0.74506413, 0.33534188, 0.12515309],
           [0.74760315, 0.34048567, 0.12521671],
           [0.75009333, 0.34565125, 0.12539436],
           [0.75253419, 0.35083851, 0.12569182],
           [0.75492525, 0.35604733, 0.12611484],
           [0.75726603, 0.36127756, 0.12666908],
           [0.75955612, 0.36652901, 0.12736013],
           [0.76179510, 0.37180145, 0.12819340],
           [0.76398258, 0.37709464, 0.12917414],
           [0.76611821, 0.38240828, 0.13030734],
           [0.76820170, 0.38774203, 0.13159774],
           [0.77023277, 0.39309552, 0.13304977],
           [0.77221122, 0.39846833, 0.13466751],
           [0.77413687, 0.40386001, 0.13645469],
           [0.77600962, 0.40927004, 0.13841463],
           [0.77782945, 0.41469787, 0.14055024],
           [0.77959637, 0.42014290, 0.14286400],
           [0.78131049, 0.42560450, 0.14535795],
           [0.78297201, 0.43108193, 0.14803371],
           [0.78458119, 0.43657447, 0.15089242],
           [0.78613838, 0.44208132, 0.15393484],
           [0.78764406, 0.44760163, 0.15716125],
           [0.78909879, 0.45313449, 0.16057155],
           [0.79050321, 0.45867899, 0.16416524],
           [0.79185809, 0.46423414, 0.16794145],
           [0.79316437, 0.46979884, 0.17189894],
           [0.79442299, 0.47537209, 0.17603613],
           [0.79563505, 0.48095278, 0.18035117],
           [0.79680179, 0.48653975, 0.18484187],
           [0.79792464, 0.49213177, 0.18950575],
           [0.79900496, 0.49772771, 0.19434016],
           [0.80004432, 0.50332634, 0.19934218],
           [0.80104441, 0.50892642, 0.20450869],
           [0.80200701, 0.51452672, 0.20983640],
           [0.80293413, 0.52012589, 0.21532172],
           [0.80382766, 0.52572276, 0.22096109],
           [0.80468967, 0.53131609, 0.22675077],
           [0.80552232, 0.53690464, 0.23268687],
           [0.80632783, 0.54248721, 0.23876543],
           [0.80710851, 0.54806261, 0.24498237],
           [0.80786670, 0.55362968, 0.25133358],
           [0.80860481, 0.55918732, 0.25781488],
           [0.80932526, 0.56473444, 0.26442207],
           [0.81003050, 0.57027003, 0.27115092],
           [0.81072299, 0.57579311, 0.27799721],
           [0.81140518, 0.58130277, 0.28495673],
           [0.81207972, 0.58679806, 0.29202509],
           [0.81274908, 0.59227815, 0.29919806],
           [0.81341552, 0.59774241, 0.30647173],
           [0.81408137, 0.60319018, 0.31384208],
           [0.81474926, 0.60862071, 0.32130478],
           [0.81542167, 0.61403338, 0.32885569],
           [0.81610036, 0.61942795, 0.33649157],
           [0.81678817, 0.62480368, 0.34420784],
           [0.81748695, 0.63016037, 0.35200121],
           [0.81819885, 0.63549767, 0.35986798],
           [0.81892611, 0.64081526, 0.36780440],
           [0.81967060, 0.64611297, 0.37580716],
           [0.82043411, 0.65139072, 0.38387313],
           [0.82121909, 0.65664815, 0.39199823],
           [0.82202656, 0.66188554, 0.40018042],
           [0.82285870, 0.66710267, 0.40841599],
           [0.82371744, 0.67229949, 0.41670163],
           [0.82460384, 0.67747627, 0.42503525],
           [0.82551949, 0.68263309, 0.43341401],
           [0.82646594, 0.68777007, 0.44183516],
           [0.82744484, 0.69288728, 0.45029574],
           [0.82845747, 0.69798494, 0.45879337],
           [0.82950490, 0.70306338, 0.46732598],
           [0.83058837, 0.70812283, 0.47589127],
           [0.83170905, 0.71316357, 0.48448704],
           [0.83286801, 0.71818592, 0.49311119],
           [0.83406629, 0.72319019, 0.50176173],
           [0.83530503, 0.72817668, 0.51043647],
           [0.83658533, 0.73314569, 0.51913321],
           [0.83790779, 0.73809768, 0.52785070],
           [0.83927317, 0.74303306, 0.53658732],
           [0.84068221, 0.74795225, 0.54534156],
           [0.84213588, 0.75285557, 0.55411142],
           [0.84363540, 0.75774329, 0.56289444],
           [0.84518059, 0.76261608, 0.57169073],
           [0.84677218, 0.76747433, 0.58049871],
           [0.84841181, 0.77231818, 0.58931505],
           [0.85009872, 0.77714844, 0.59814098],
           [0.85183442, 0.78196527, 0.60697334],
           [0.85361898, 0.78676924, 0.61581180],
           [0.85545300, 0.79156074, 0.62465496],
           [0.85733708, 0.79634019, 0.63350137],
           [0.85927157, 0.80110804, 0.64235012],
           [0.86125682, 0.80586474, 0.65120031],
           [0.86329372, 0.81061062, 0.66004984],
           [0.86538175, 0.81534633, 0.66889970],
           [0.86752270, 0.82007195, 0.67774580],
           [0.86971583, 0.82478816, 0.68658960],
           [0.87196152, 0.82949538, 0.69543018],
           [0.87426133, 0.83419375, 0.70426386],
           [0.87661459, 0.83888389, 0.71309208],
           [0.87902177, 0.84356618, 0.72191377],
           [0.88148352, 0.84824093, 0.73072734],
           [0.88400075, 0.85290842, 0.73953068],
           [0.88657330, 0.85756911, 0.74832427],
           [0.88920173, 0.86222332, 0.75710696],
           [0.89188662, 0.86687134, 0.76587761],
           [0.89462859, 0.87151346, 0.77463504],
           [0.89742844, 0.87614990, 0.78337778],
           [0.90028705, 0.88078089, 0.79210422],
           [0.90320498, 0.88540665, 0.80081379],
           [0.90618322, 0.89002734, 0.80950508],
           [0.90922288, 0.89464305, 0.81817656],
           [0.91232527, 0.89925383, 0.82682655],
           [0.91549189, 0.90385964, 0.83545317],
           [0.91872454, 0.90846037, 0.84405428],
           [0.92202532, 0.91305582, 0.85262744],
           [0.92539674, 0.91764567, 0.86116973],
           [0.92884183, 0.92222945, 0.86967767],
           [0.93236418, 0.92680655, 0.87814698],
           [0.93596810, 0.93137619, 0.88657233],
           [0.93965884, 0.93593743, 0.89494635],
           [0.94344228, 0.94048919, 0.90326058],
           [0.94732508, 0.94503036, 0.91150406],
           [0.95131441, 0.94955998, 0.91966230],
           [0.95541703, 0.95407768, 0.92771676],
           [0.95963758, 0.95858437, 0.93564471],
           [0.96397569, 0.96308327, 0.94342013],
           [0.96842214, 0.96758121, 0.95101597],
           [0.97295466, 0.97208912, 0.95841520],
           [0.97753779, 0.97662151, 0.96561627],
           [0.98212842, 0.98119340, 0.97264191],
           [0.98668707, 0.98581600, 0.97953727],
           [0.99118833, 0.99049355, 0.98636053],
           [0.99562415, 0.99522369, 0.99316724],
           [1.00000000, 1.00000000, 1.00000000],
           [0.99286730, 0.99599373, 0.99614814],
           [0.98570130, 0.99201794, 0.99234023],
           [0.97850500, 0.98807098, 0.98857659],
           [0.97128061, 0.98415148, 0.98485755],
           [0.96402980, 0.98025830, 0.98118343],
           [0.95675388, 0.97639044, 0.97755454],
           [0.94945385, 0.97254703, 0.97397122],
           [0.94213052, 0.96872728, 0.97043381],
           [0.93478367, 0.96493074, 0.96694300],
           [0.92741428, 0.96115657, 0.96349897],
           [0.92002294, 0.95740406, 0.96010196],
           [0.91260996, 0.95367261, 0.95675237],
           [0.90517453, 0.94996196, 0.95345107],
           [0.89771724, 0.94627141, 0.95019826],
           [0.89023871, 0.94260026, 0.94699415],
           [0.88273791, 0.93894831, 0.94383968],
           [0.87521510, 0.93531495, 0.94073521],
           [0.86767109, 0.93169941, 0.93768081],
           [0.86010366, 0.92810186, 0.93467806],
           [0.85251495, 0.92452109, 0.93172638],
           [0.84490304, 0.92095716, 0.92882722],
           [0.83726916, 0.91740916, 0.92598046],
           [0.82961175, 0.91387698, 0.92318739],
           [0.82193224, 0.91035967, 0.92044780],
           [0.81422838, 0.90685730, 0.91776342],
           [0.80650196, 0.90336881, 0.91513381],
           [0.79875172, 0.89989396, 0.91256023],
           [0.79097748, 0.89643222, 0.91004337],
           [0.78317989, 0.89298284, 0.90758344],
           [0.77535836, 0.88954537, 0.90518140],
           [0.76751212, 0.88611942, 0.90283832],
           [0.75964204, 0.88270414, 0.90055436],
           [0.75174803, 0.87929894, 0.89833027],
           [0.74383001, 0.87590321, 0.89616678],
           [0.73588801, 0.87251632, 0.89406462],
           [0.72792211, 0.86913761, 0.89202452],
           [0.71993230, 0.86576642, 0.89004726],
           [0.71191917, 0.86240197, 0.88813333],
           [0.70388310, 0.85904350, 0.88628335],
           [0.69582429, 0.85569031, 0.88449810],
           [0.68774337, 0.85234156, 0.88277813],
           [0.67964110, 0.84899642, 0.88112393],
           [0.67151833, 0.84565401, 0.87953598],
           [0.66337606, 0.84231345, 0.87801471],
           [0.65521541, 0.83897379, 0.87656047],
           [0.64703677, 0.83563427, 0.87517423],
           [0.63884212, 0.83229380, 0.87385586],
           [0.63063346, 0.82895129, 0.87260527],
           [0.62241137, 0.82560593, 0.87142346],
           [0.61417873, 0.82225650, 0.87030979],
           [0.60593731, 0.81890198, 0.86926455],
           [0.59768948, 0.81554126, 0.86828756],
           [0.58943783, 0.81217323, 0.86737864],
           [0.58118552, 0.80879669, 0.86653714],
           [0.57293484, 0.80541060, 0.86576323],
           [0.56469007, 0.80201364, 0.86505554],
           [0.55645450, 0.79860469, 0.86441358],
           [0.54823156, 0.79518261, 0.86383682],
           [0.54002602, 0.79174613, 0.86332368],
           [0.53184227, 0.78829406, 0.86287301],
           [0.52368496, 0.78482526, 0.86248343],
           [0.51555907, 0.78133854, 0.86215344],
           [0.50746978, 0.77783280, 0.86188137],
           [0.49942265, 0.77430689, 0.86166531],
           [0.49142353, 0.77075975, 0.86150313],
           [0.48347841, 0.76719032, 0.86139263],
           [0.47559348, 0.76359762, 0.86133146],
           [0.46777506, 0.75998071, 0.86131721],
           [0.46002970, 0.75633872, 0.86134727],
           [0.45236412, 0.75267082, 0.86141888],
           [0.44478510, 0.74897626, 0.86152922],
           [0.43729950, 0.74525436, 0.86167541],
           [0.42991420, 0.74150451, 0.86185450],
           [0.42263612, 0.73772620, 0.86206351],
           [0.41547206, 0.73391896, 0.86229955],
           [0.40842891, 0.73008242, 0.86255953],
           [0.40151344, 0.72621629, 0.86284042],
           [0.39473229, 0.72232034, 0.86313926],
           [0.38809192, 0.71839442, 0.86345317],
           [0.38159865, 0.71443845, 0.86377930],
           [0.37525864, 0.71045242, 0.86411483],
           [0.36907778, 0.70643639, 0.86445707],
           [0.36306172, 0.70239045, 0.86480345],
           [0.35721585, 0.69831477, 0.86515145],
           [0.35154527, 0.69420955, 0.86549871],
           [0.34605476, 0.69007505, 0.86584298],
           [0.34074877, 0.68591156, 0.86618210],
           [0.33563140, 0.68171940, 0.86651406],
           [0.33070640, 0.67749892, 0.86683699],
           [0.32597710, 0.67325047, 0.86714916],
           [0.32144646, 0.66897446, 0.86744888],
           [0.31711702, 0.66467128, 0.86773461],
           [0.31299088, 0.66034135, 0.86800502],
           [0.30906971, 0.65598506, 0.86825881],
           [0.30535474, 0.65160283, 0.86849481],
           [0.30184670, 0.64719509, 0.86871187],
           [0.29854589, 0.64276223, 0.86890904],
           [0.29545215, 0.63830465, 0.86908547],
           [0.29256481, 0.63382273, 0.86924036],
           [0.28988277, 0.62931684, 0.86937299],
           [0.28740445, 0.62478736, 0.86948270],
           [0.28512780, 0.62023461, 0.86956892],
           [0.28305032, 0.61565894, 0.86963107],
           [0.28116911, 0.61106064, 0.86966874],
           [0.27948085, 0.60644000, 0.86968153],
           [0.27798185, 0.60179728, 0.86966909],
           [0.27666802, 0.59713272, 0.86963109],
           [0.27553495, 0.59244656, 0.86956724],
           [0.27457790, 0.58773898, 0.86947730],
           [0.27379190, 0.58301017, 0.86936104],
           [0.27317167, 0.57826027, 0.86921827],
           [0.27271178, 0.57348942, 0.86904879],
           [0.27240657, 0.56869773, 0.86885245],
           [0.27225028, 0.56388527, 0.86862909],
           [0.27223700, 0.55905210, 0.86837857],
           [0.27236075, 0.55419827, 0.86810075],
           [0.27261552, 0.54932379, 0.86779550],
           [0.27299526, 0.54442863, 0.86746268],
           [0.27349393, 0.53951278, 0.86710216],
           [0.27410552, 0.53457616, 0.86671379],
           [0.27482409, 0.52961871, 0.86629742],
           [0.27564375, 0.52464031, 0.86585289],
           [0.27655872, 0.51964085, 0.86538002],
           [0.27756333, 0.51462017, 0.86487862],
           [0.27865202, 0.50957810, 0.86434849],
           [0.27981937, 0.50451445, 0.86378941],
           [0.28106012, 0.49942901, 0.86320111],
           [0.28236913, 0.49432153, 0.86258334],
           [0.28374143, 0.48919175, 0.86193579],
           [0.28517223, 0.48403940, 0.86125815],
           [0.28665689, 0.47886417, 0.86055007],
           [0.28819091, 0.47366572, 0.85981116],
           [0.28976997, 0.46844372, 0.85904101],
           [0.29138992, 0.46319780, 0.85823916],
           [0.29304674, 0.45792755, 0.85740514],
           [0.29473659, 0.45263258, 0.85653840],
           [0.29645577, 0.44731243, 0.85563839],
           [0.29820071, 0.44196667, 0.85470449],
           [0.29996801, 0.43659480, 0.85373605],
           [0.30175438, 0.43119633, 0.85273236],
           [0.30355667, 0.42577074, 0.85169266],
           [0.30537185, 0.42031747, 0.85061615],
           [0.30719700, 0.41483597, 0.84950198],
           [0.30902932, 0.40932564, 0.84834921],
           [0.31086609, 0.40378588, 0.84715686],
           [0.31270470, 0.39821605, 0.84592389],
           [0.31454262, 0.39261551, 0.84464919],
           [0.31637740, 0.38698359, 0.84333156],
           [0.31820667, 0.38131959, 0.84196975],
           [0.32002814, 0.37562279, 0.84056242],
           [0.32183955, 0.36989247, 0.83910817],
           [0.32363873, 0.36412786, 0.83760548],
           [0.32542357, 0.35832819, 0.83605279],
           [0.32719195, 0.35249267, 0.83444839],
           [0.32894179, 0.34662050, 0.83279049],
           [0.33067104, 0.34071086, 0.83107721],
           [0.33237770, 0.33476293, 0.82930654],
           [0.33405974, 0.32877585, 0.82747636],
           [0.33571517, 0.32274878, 0.82558443],
           [0.33734198, 0.31668087, 0.82362838],
           [0.33893835, 0.31057115, 0.82160578],
           [0.34050217, 0.30441882, 0.81951393],
           [0.34203131, 0.29822306, 0.81735002],
           [0.34352370, 0.29198306, 0.81511110],
           [0.34497749, 0.28569784, 0.81279410],
           [0.34639044, 0.27936666, 0.81039570],
           [0.34776019, 0.27298888, 0.80791239],
           [0.34908483, 0.26656357, 0.80534055],
           [0.35036187, 0.26009021, 0.80267628],
           [0.35158888, 0.25356825, 0.79991546],
           [0.35276371, 0.24699702, 0.79705382],
           [0.35388342, 0.24037642, 0.79408675],
           [0.35494577, 0.23370596, 0.79100948],
           [0.35594770, 0.22698583, 0.78781691],
           [0.35688639, 0.22021618, 0.78450372],
           [0.35775908, 0.21339730, 0.78106426],
           [0.35856226, 0.20653021, 0.77749264],
           [0.35929267, 0.19961606, 0.77378264],
           [0.35994704, 0.19265635, 0.76992770],
           [0.36052159, 0.18565342, 0.76592097],
           [0.36101234, 0.17861026, 0.76175533],
           [0.36141520, 0.17153066, 0.75742330],
           [0.36172584, 0.16441945, 0.75291711],
           [0.36193966, 0.15728269, 0.74822872],
           [0.36205178, 0.15012794, 0.74334985],
           [0.36205724, 0.14296445, 0.73827187],
           [0.36195053, 0.13580380, 0.73298618],
           [0.36172581, 0.12866018, 0.72748415],
           [0.36137727, 0.12155071, 0.72175694],
           [0.36089860, 0.11449629, 0.71579604],
           [0.36028326, 0.10752220, 0.70959330],
           [0.35952450, 0.10065872, 0.70314114],
           [0.35861556, 0.09394195, 0.69643248],
           [0.35754931, 0.08741448, 0.68946192],
           [0.35631884, 0.08112583, 0.68222517],
           [0.35491739, 0.07513269, 0.67471986],
           [0.35333851, 0.06949832, 0.66694595],
           [0.35157631, 0.06429105, 0.65890615],
           [0.34962566, 0.05958143, 0.65060635],
           [0.34748252, 0.05543774, 0.64205593],
           [0.34514413, 0.05192004, 0.63326796],
           [0.34260931, 0.04907315, 0.62425926],
           [0.33987862, 0.04692002, 0.61505025],
           [0.33695451, 0.04545688, 0.60566455],
           [0.33384136, 0.04465176, 0.59612840],
           [0.33054538, 0.04444705, 0.58646989],
           [0.32707450, 0.04476563, 0.57671800],
           [0.32343804, 0.04551891, 0.56690168],
           [0.31964641, 0.04661505, 0.55704886],
           [0.31571075, 0.04796584, 0.54718563],
           [0.31164264, 0.04949023, 0.53733650],
           [0.30745369, 0.05111859, 0.52752281],
           [0.30315530, 0.05279265, 0.51776318],
           [0.29875837, 0.05446589, 0.50807296],
           [0.29427335, 0.05610064, 0.49846566],
           [0.28971002, 0.05766820, 0.48895209],
           [0.28507738, 0.05914747, 0.47954053],
           [0.28038355, 0.06052363, 0.47023691],
           [0.27563583, 0.06178694, 0.46104509],
           [0.27084104, 0.06293004, 0.45196850],
           [0.26600531, 0.06394863, 0.44300913],
           [0.26113400, 0.06484105, 0.43416759],
           [0.25623172, 0.06560784, 0.42544305],
           [0.25130289, 0.06624945, 0.41683516],
           [0.24635140, 0.06676744, 0.40834278],
           [0.24138064, 0.06716421, 0.39996418],
           [0.23639355, 0.06744271, 0.39169711],
           [0.23139265, 0.06760632, 0.38353892],
           [0.22638008, 0.06765865, 0.37548663],
           [0.22135841, 0.06760158, 0.36753890],
           [0.21632909, 0.06743924, 0.35969209],
           [0.21129371, 0.06717468, 0.35194349],
           [0.20625363, 0.06681103, 0.34429018],
           [0.20121041, 0.06635033, 0.33673027],
           [0.19616452, 0.06579670, 0.32925957],
           [0.19111698, 0.06515241, 0.32187567],
           [0.18606900, 0.06441903, 0.31457681],
           [0.18102097, 0.06359940, 0.30735975],
           [0.17597330, 0.06269590, 0.30022161],
           [0.17092644, 0.06171047, 0.29315986],
           [0.16588073, 0.06064493, 0.28617200],
           [0.16083638, 0.05950098, 0.27925551],
           [0.15579384, 0.05827961, 0.27240858],
           [0.15075315, 0.05698225, 0.26562875],
           [0.14571404, 0.05561056, 0.25891321],
           [0.14067634, 0.05416571, 0.25225957],
           [0.13564028, 0.05264791, 0.24566637],
           [0.13060585, 0.05105757, 0.23913184],
           [0.12557198, 0.04939640, 0.23265254],
           [0.12053936, 0.04766314, 0.22622830],
           [0.11550677, 0.04585913, 0.21985580],
           [0.11047426, 0.04398349, 0.21353410],
           [0.10544091, 0.04203645, 0.20726079],
           [0.10040665, 0.04001069, 0.20103507],
           [0.09536987, 0.03792887, 0.19485383]]

test_cm = ListedColormap(cm_data, name="fusion")