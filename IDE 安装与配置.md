# intellij IDEA
[https://www.jetbrains.com/idea/download/#section=linux](https://www.jetbrains.com/idea/download/#section=linux)

  Linux Installation Instructions
  ------------------------------------------------------------------------------
  1. Unpack the IntelliJ IDEA distribution archive that you downloaded to
     where you wish to install the program. We will refer to this destination
     location as your {installation home} below.

  2. Open a console and cd into "{installation home}/bin" and type:

       ./idea.sh

     to start the application. As a side effect, this will initialize various
     configuration files in the ~/.IntelliJIdea2019.1 directory.

  3. [OPTIONAL] Add "{installation home}/bin" to your PATH environment
     variable so that you may start IntelliJ IDEA from any directory.

  4. [OPTIONAL] To adjust the value of the JVM heap size, create
      ~/.IntelliJIdea2019.1/config/idea.vmoptions (or idea64.vmoptions
      if using a 64-bit JDK), and set the -Xms and -Xmx parameters. To see how
      to do this, you can reference the vmoptions file under
      "{installation home}/bin" as a model.

  [OPTIONAL] Changing the location of "config" and "system" directories
  ------------------------------------------------------------------------------
  By default, IntelliJ IDEA stores all your settings under the ~/.IntelliJIdea2019.1/config
  directory and uses ~/.IntelliJIdea2019.1/system as a data cache.
  If you want to change these settings,

  1. Open a console and cd into ~/.IntelliJIdea2019.1/config

  2. Create the file "idea.properties" and open it in an editor. Set the
     idea.system.path and/or idea.config.path variables as desired, for
     example:

     idea.system.path=~/custom/system
     idea.config.path=~/custom/config

  3. Note that we recommend to store data cache ("system" directory) on a disk
     with at least 1GB of free space.
     
激活码
-----------------------------------------------
[http://idea.lanyus.com/](http://idea.lanyus.com/)

# eclipse

[https://www.eclipse.org/downloads/](https://www.eclipse.org/downloads/)

- Oracle JDK
```bash
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
# Oracle JDK 8
sudo apt-get install oracle-java8-installer
```
- Managing Java
```bash
sudo update-alternatives --config java
```
- Setting the JAVA_HOME Environment Variable
```bash
sudo bash -c "echo -e '\nJAVA_HOME=\"/usr/lib/jvm/java-8-oracle\"' >> /etc/environment"
source /etc/environment
```
# visual studio code

[https://code.visualstudio.com/download](https://code.visualstudio.com/download)

```bash
sudo dpkg -i *.deb
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM1MzE4NDA3NCwtMTQ4Nzk4MDU1MywtND
Q0Njg3ODgxLC0xNjE5MzI3ODA3LC01MzQzNjM1NzMsMTQ4MzA5
NjQ0LDU5NTIxNTU3MSw3NDk4MjAyOSw0NjQ0MzQ3MywtMjA4OD
c0NjYxMl19
-->