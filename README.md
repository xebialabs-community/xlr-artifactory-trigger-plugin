# Preface #

This document describes the functionality provided by the XLR Artifactory Trigger plugin.

See the **XL Release Reference Manual** for background information on XL Release concepts.

# Overview #

This XLR Artifactory trigger plugin helps create a trigger which will automatically generate new releases when a new version of a specified artifact is published in Artifactory. It use maven-metadata.xml to find out that information from the repository.

# Requirements #

* **Requirements**
	* **XL Release** 4.x

# Installation #

Place the plugin JAR file into your `SERVER_HOME/plugins` directory.  

# Usage #


The trigger needs to be configured first under the configuration section to point to the right artifactory repository
![Trigger Configuration] (/triggerConfig.png)


The second piece of configuration is inside the XLR Template to use the trigger 
![Configuration] (/triggerTemplate.png)