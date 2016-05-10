#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

###################################################################################
#  Name: Artifactory Published Artifact Trigger
#
#  Description: Trigger new release when new version of artifact is published to the Artifactory repository
#  
###################################################################################

import sys, string, urllib
from xml.dom.minidom import parseString

if server is None:
    print "No Artifactory server provided."
    sys.exit(1)

request = HttpRequest(server, username, password)
context = "%s/%s/%s" % (repositoryId, groupId, artifactId)
metadata_path = "%s/%s" % (context, "maven-metadata.xml")
response = request.get(metadata_path, contentType = 'application/xml')

if not response.isSuccessful():
    if response.status == 404 and triggerOnInitialPublish:
        print "Artifact '%s:%s' not found in repository '%s'. Ignoring." % (groupId, artifactId, repositoryId)
        # the following initialisation is to enable a scenario where we wish
        # to trigger a release on a first publish of an artifact to Artifactory
        if not triggerState:
            artifactVersion = triggerState = '0.0.0'
    else:
        print "Failed to fetch artifact metadata from Artifactory repository %s" % server['url']
        response.errorDump()
        sys.exit(1)
else:
    dom = parseString(response.response)
    nodes = dom.getElementsByTagName("latest")
    triggerState = nodes[0].firstChild.nodeValue

    # populate output variables
    artifactVersion = triggerState
    artifactRepositoryPath = "%s/%s/%s/%s-%s" % (server['url'], context,artifactVersion, artifactId,artifactVersion)
    print artifactRepositoryPath
