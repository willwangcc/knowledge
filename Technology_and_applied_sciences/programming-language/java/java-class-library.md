

<h1 align="center">
<br>
  <a href="https://docs.oracle.com/javase/8/docs/"><img src="https://i.imgur.com/PAQXiyT.png" alt="Java Docs" width=400"></a>
  <br>
    <br>
  Java
  <br><br>
</h1>

> The Java Class Library (JCL) is a set of dynamically loadable libraries that Java Virtual Machine (JVM) languages can **call at run time**.  [[wiki](http://www.wikiwand.com/en/Java_Class_Library)]

## Why?

Because the Java Platform **is not dependent on** a specific operating system, applications **cannot rely on** any of the platform-native libraries. Instead, the Java Platform provides a comprehensive set of **standard class libraries**, containing the functions common to modern operating systems.

JCL serves three purposes within the JVM:

1. Like other standard code libraries, they provide the programmer a well-known set of **useful facilities**, such as container classes and regular expression processing.
1. The library provides **an abstract interface** to tasks that would normally depend heavily on the hardware and operating system, such as network access and file access.
1. Some underlying platforms may not support all of the features a Java application expects. In these cases, the library implementation can either **emulate those features** or provide a **consistent** way to check for the presence of a specific feature.

## What 

> Main features

JCL Features are accessed through **classes** provided in **packages**.

1. `java.lang` contains fundamental classes and interfaces closely tied to the language and runtime system.
1. **I/O and networking access** the platform file system, and more generally networks through the `java.io`, `java.nio` and `java.net` packages. For networking, SCTP is available through com.sun.nio.sctp.
1. **Mathematics** package: `java.math` provides mathematical expressions and evaluation, as well as arbitrary-precision decimal and integer number datatypes.
1. **Collections and Utilities** : built-in Collection data structures, and utility classes, for Regular expressions, Concurrency, logging and Data compression.
1. GUI and 2D Graphics: the AWT package (`java.awt`) basic GUI operations and binds to the underlying native system. It also contains the 2D Graphics API. The Swing package (`javax.swing`) is built on AWT and provides a platform-independent widget toolkit, as well as a Pluggable look and feel. It also deals with editable and non-editable text components.
1. Sound: interfaces and classes for reading, writing, sequencing, and synthesizing of sound data.
1. **Text**: `java.text` deals with text, dates, numbers and messages.
1. Image package: java.awt.image and javax.imageio provide APIs to write, read, and modify images.
1. **XML**: SAX, DOM, StAX, XSLT transforms, XPath and various APIs for Web services, as SOAP protocol and JAX-WS.
1. CORBA and RMI APIs, including a built-in ORB
1. **Security** is provided by `java.security` and encryption services are provided by javax.crypto.
1. **Databases**: access to SQL databases via `java.sql`
1. Access to **Scripting** engines: The `javax.script` package gives access to any conforming **Scripting language**.
1. Applets: `java.applet` allows applications to be downloaded over a network and run within a guarded sandbox
1. Java Beans: java.beans provides ways to manipulate reusable components.
1. Introspection and reflection: java.lang.Class represents a class, but other classes such as Method and Constructor are available in java.lang.reflect.
