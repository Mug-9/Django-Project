def func(str):
    arr = []
    for item in str.split(','):
        arr.append(item)
    return arr




anhui = ['所有城市','合肥', '铜陵', '黄山', '池州', '宣城', '巢湖', '淮南', '宿州','六安','滁州','淮北','阜阳','马鞍山','安庆','蚌埠','芜湖','亳州']
guangdong = ['所有城市','广州','深圳','东莞','云浮','佛山','湛江','江门','惠州','珠海','韶关','阳江','茂名','潮州','揭阳','中山','清远','肇庆','河源','梅州','汕头','汕尾']
guangxi = '所有城市,南宁,柳州,桂林,贺州,贵港,玉林,河池,北海,钦州,防城港,百色,梧州,来宾,崇左'
guangxi_list = []
for item in guangxi.split(','):
    guangxi_list.append(item)
gansu = func('所有城市,兰州,庆阳,定西,武威,酒泉,张掖,嘉峪关,平凉,天水,白银,金昌,陇南,临夏,甘南')
guizou = func('所有城市,贵阳,黔南,六盘水,遵义,黔东南,铜仁,安顺,毕节,黔西南')
hebei = func('所有城市,石家庄,衡水,张家口,承德,秦皇岛,廊坊,沧州,保定,唐山,邯郸,邢台')
heilongjiang = func('所有城市,哈尔滨,大庆,伊春,大兴,安岭,黑河,鹤岗,七台河,齐齐哈尔,佳木斯,牡丹江,鸡西,绥化,双鸭山')
henan = func('所有城市,郑州,南阳,新乡,开封,焦作,平顶山,许昌,安阳,驻马店,信阳,鹤壁,周口,商丘,洛阳,漯河,濮阳,三门峡,济源')
hunan = func('所有城市,长沙,岳阳,衡阳,株洲,湘潭,益阳,郴州,湘西,娄底,怀化,常德,张家界,永州,邵阳')
hubei = func('所有城市,武汉,黄石,荆州,襄阳,黄冈,荆门,宜昌,十堰,随州,恩施,鄂州,咸宁,孝感,仙桃,天门,潜江,神农架')
hainan = func('所有城市,海口,万宁,琼海,三亚,儋州,东方,五指山,文昌,陵水,澄迈,乐东,临高,定安,昌江,屯昌,保亭,白沙,琼中')
jilin = func('所有城市,长春,四平,辽源,松原,吉林,通化,白山,白城,延边')
jiangsu = func('所有城市,南京,苏州,无锡,连云港,淮安,扬州,泰州,盐城,徐州,常州,南通,镇江,宿迁')
jiangxi = func('所有城市,南昌,九江,鹰潭,抚州,上饶,赣州,吉安,萍乡,景德镇,新余,宜春')
liaojin = func('所有城市,沈阳,大连,盘锦,鞍山,朝阳,锦州,铁岭,丹东,本溪,营口,抚顺,阜新,辽阳,葫芦岛')
neimenggu = func('所有城市,呼和浩特,包头,鄂尔多斯,巴彦淖尔,乌海,阿拉善盟,锡林郭勒盟,赤峰,通辽,呼伦贝尔,乌兰察布,兴安盟')
jingxia = func('所有城市,银川,吴忠,固原,石嘴山,中卫')
qinghai = func('所有城市,西宁,海西,海东,玉树,海南,海北,黄南,果洛')
shanghai = []
sicuan = func('所有城市,成都,宜宾,绵阳,广元,遂宁,巴中,内江,泸州,南充,德阳,乐山,广安,资阳,自贡,攀枝花,达州,雅安,眉山,甘孜,阿坝,凉山')
shandong = func('所有城市,济南,滨州,青岛,烟台,临沂,潍坊,淄博,东营,聊城,菏泽,枣庄,德州,威海,济宁,泰安,莱芜,日照')
shanxi = func('所有城市,太原,大同,长治,忻州,晋中,临汾,运城,晋城,朔州,阳泉,吕梁')
shanxi2 = func('所有城市,西安,铜川,安康,宝鸡,商洛,渭南,汉中,咸阳,榆林,延安')
tianjin = []
taiwan = []
xizang = func('所有城市,拉萨,日喀则,那曲,林芝,山南,昌都,阿里')
xianggang = [],
xinjiang = func('所有城市,乌鲁木齐,石河子,吐鲁番,昌吉,哈密,阿克苏,克拉玛依,博尔塔拉,阿勒泰,喀什,和田,巴音郭楞,伊犁,塔城,克孜勒苏柯尔克孜,五家渠,阿拉尔,图木舒克')
yunnan = func('所有城市,昆明,玉溪,楚雄,大理,昭通,红河,曲靖,丽江,临沧,文山,保山,普洱,西双版纳,德宏,怒江,迪庆')
zejiang = func('所有城市,杭州,丽水,金华,温州,台州,衢州,宁波,绍兴,嘉兴,湖州,舟山')


province = {
    'A - G': {'安徽': anhui, '澳门': [], '北京': [], '重庆':[], '福建':[], '广东': guangdong, '广西': guangxi_list, '甘肃': gansu,
            '贵州': guizou,},
    'H - J': {'河北': hebei, '黑龙江':heilongjiang, '河南': henan, '湖南': hunan, '湖北': hubei, '海南': hainan,
            '吉林':jilin, '江苏': jiangsu, '江西': jiangxi,},
    'L - S': {'辽宁': liaojin, '内蒙古': neimenggu, '宁夏': jingxia, '青海':qinghai,
            '上海':shanghai, '四川': sicuan, '山东': shandong, '山西':shanxi, '陕西':shanxi2,},
    'T - Z': {'天津':tianjin, '台湾':taiwan,
            '西藏':xizang, '香港':xianggang, '新疆':xinjiang, '云南':yunnan, '浙江':zejiang}
            }

def fun3(args):
    for item in args:
        print('{')
        print('value: \'%s\',' % item)
        print('label: \'%s\',' % item)
        print('},')



def fun2(args):
    for item in args:
        print('{')
        print('value: \'%s\',' % item)
        print('label: \'%s\',' % item)
        if len(args[item]) != 0:
            print('children: [')
            fun3(args[item])
            print(']')
        print('},')


print('[')


for item in province:
    print('{')
    print('value: \'%s\',' % item)
    print('label: \'%s\',' % item)
    print('children: [')
    fun2(province[item])
    print(']')
    print('},')
print(']')
