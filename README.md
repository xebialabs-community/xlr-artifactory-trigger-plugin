# Preface #

This document describes the functionality provided by the XL Release Artifactory Trigger plugin.

See the **[XL Release Documentation](https://docs.xebialabs.com/xl-release/)**] for background information on XL Release concepts.

# Overview #

The XL Release Artifactory trigger plugin provides a trigger which automatically generates new releases when a new version of a specified artifact is published to [Artifactory](http://www.jfrog.com/artifactory/). It uses information in `maven-metadata.xml` to determine when new artifacts are published.

# Requirements #

* **Requirements**
	* **XL Release** 4.x

# Installation #

* Place the plugin JAR file into your `SERVER_HOME/plugins` directory.
* Add the following permission to you `SERVER_HOME/conf/script.policy` file:

```	
permission java.lang.RuntimePermission "accessClassInPackage.com.sun.org.apache.xerces.internal.*";

```
* Restart the server  

# Usage #

First, you need to add an entry in the [Configuration](https://docs.xebialabs.com/xl-release/how-to/create-custom-configuration-types-in-xl-release.html#configuration-page) section with information on how to connect to your Artifactory repository:

![Trigger Configuration](/triggerConfig.png)

The next step is to configure a new [trigger](https://docs.xebialabs.com/xl-release/how-to/create-a-release-trigger.html) for your XL Release [template](https://docs.xebialabs.com/xl-release/how-to/create-a-release-template.html):

![Configuration](/triggerTemplate.png)