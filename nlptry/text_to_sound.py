# coding=utf-8
import pyttsx3

# 模块初始化
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                        #printing current voice rate
engine.setProperty('rate', 220)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print(volume)                          #printing current volume level
engine.setProperty('volume',1.5)    # setting up volume level  between 0 and 1


print('准备开始语音播报...')
# 设置要播报的Unicode字符串
engine.say("I will speak this text，人生苦短，我用Python")
engine.runAndWait()


west_journey = '''
《西游记》
作者：[明]吴承恩
第一回　灵根育孕源流出　心性修持大道生
诗曰：
混沌未分天地乱，茫茫渺渺无人见。
自从盘古破鸿蒙，开辟从兹清浊辨。
覆载群生仰至仁，发明万物皆成善。
欲知造化会元功，须看西游释厄传。
盖闻天地之数，有十二万九千六百岁为一元。将一元分为十二会，乃子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥之十二支也。每会该一万八百岁。且就一日而论：子时得阳气，而丑则鸡鸣；寅不通光，而卯则日出；辰时食后，而巳则挨排；日午天中，而未则西蹉；申时晡而日落酉；戌黄昏而人定亥。譬于大数，若到戌会之终，则天地昏蒙而万物否矣。再去五千四百岁，交亥会之初，则当黑暗，而两间人物俱无矣，故曰混沌。又五千四百岁，亥会将终，贞下起元，近子之会，而复逐渐开明。邵康节曰：“冬至子之半，天心无改移。一阳初动处，万物未生时。”到此，天始有根。再五千四百岁，正当子会，轻清上腾，有日，有月，有星，有辰。日、月、星、辰，谓之四象。故曰，天开于子。又经五千四百岁，子会将终，近丑之会，而逐渐坚实。易曰：“大哉乾元！至哉坤元！万物资生，乃顺承天。”至此，地始凝结。再五千四百岁，正当丑会，重浊下凝，有水，有火，有山，有石，有土。水、火、山、石、土谓之五形。故曰，地辟于丑。又经五千四百岁，丑会终而寅会之初，发生万物。历曰：“天气下降，地气上升；天地交合，群物皆生。”至此，天清地爽，阴阳交合。再五千四百岁，正当寅会，生人，生兽，生禽，正谓天地人，三才定位。故曰，人生于寅。感盘古开辟，三皇治世，五帝定伦，世界之间，遂分为四大部洲：曰东胜神洲，曰西牛贺洲，曰南赡部洲，曰北俱芦洲。这部书单表东胜神洲。海外有一国土，名曰傲来国。国近大海，海中有一座山，唤为花果山。此山乃十洲之祖脉，三岛之来龙，自开清浊而立，鸿蒙判后而成。真个好山！有词赋为证。赋曰：
势镇汪洋，威宁瑶海。势镇汪洋，潮涌银山鱼入穴；威宁瑶海，波翻雪浪蜃离渊。木火方隅高积上，东海之处耸崇巅。丹崖怪石，削壁奇峰。丹崖上，彩凤双鸣；削壁前，麒麟独卧。峰头时听锦鸡鸣，石窟每观龙出入。林中有寿鹿仙狐，树上有灵禽玄鹤。瑶草奇花不谢，青松翠柏长春。仙桃常结果，修竹每留云。一条涧壑藤萝密，四面原堤草色新。正是百川会处擎天柱，万劫无移大地根。那座山，正当顶上，有一块仙石。其石有三丈六尺五寸高，有二丈四尺围圆。三丈六尺五寸高，按周天三百六十五度；二丈四尺围圆，按政历二十四气。上有九窍八孔，按九宫八卦。四面更无树木遮阴，左右倒有芝兰相衬。盖自开辟以来，每受天真地秀，日精月华，感之既久，遂有灵通之意。内育仙胞，一日迸裂，产一石卵，似圆球样大。因见风，化作一个石猴，五官俱备，四肢皆全。便就学爬学走，拜了四方。目运两道金光，射冲斗府。惊动高天上圣大慈仁者玉皇大天尊玄穹高上帝，驾座金阙云宫灵霄宝店，聚集仙卿，见有金光焰焰，即命千里眼、顺风耳开南天门观看。二将果奉旨出门外，看的真，听的明。须臾回报道：“臣奉旨观听金光之处，乃东胜神洲海东傲来小国之界，有一座花果山，山上有一仙石，石产一卵，见风化一石猴，在那里拜四方，眼运金光，射冲斗府。如今服饵水食，金光将潜息矣。”玉帝垂赐恩慈曰：“下方之物，乃天地精华所生，不足为异。”
那猴在山中，却会行走跳跃，食草木，饮涧泉，采山花，觅树果；与狼虫为伴，虎豹为群，獐鹿为友，猕猿为亲；夜宿石崖之下，朝游峰洞之中。真是“山中无甲子，寒尽不知年。”一朝天气炎热，与群猴避暑，都在松阴之下顽耍。你看他一个个：
跳树攀枝，采花觅果；抛弹子，邷么儿；跑沙窝，砌宝塔；赶蜻蜓，扑八蜡；参老天，拜菩萨；扯葛藤，编草帓；捉虱子，咬又掐；理毛衣，剔指甲；挨的挨，擦的擦；推的推，压的压；扯的扯，拉的拉，青松林下任他顽，绿水涧边随洗濯。一群猴子耍了一会，却去那山涧中洗澡。见那股涧水奔流，真个似滚瓜涌溅。古云：“禽有禽言，兽有兽语。”众猴都道：“这股水不知是那里的水。我们今日赶闲无事，顺涧边往上溜头寻看源流，耍子去耶！”喊一声，都拖男挈女，呼弟呼兄，一齐跑来，顺涧爬山，直至源流之处，乃是一股瀑布飞泉。但见那：
一派白虹起，千寻雪浪飞；海风吹不断，江月照还依。
冷气分青嶂，馀流润翠微；潺湲名瀑布，真似挂帘帷。
'''
engine.say(west_journey)
engine.runAndWait()
