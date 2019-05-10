#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

###################################################################################
#  Name: Artifactory Published Artifact Trigger
#
#  Description: Trigger new release when new version of artifact is published to the Artifactory repository
#  
###################################################################################

import sys
from xml.dom.minidom import parseString

if server is None:
    print "No Artifactory server provided."
    sys.exit(1)

request = HttpRequest(server, username, password)
context = "%s/%s/%s" % (repositoryId, groupId, artifactId)
metadata_path = "%s/%s" % (context, "maven-metadata.xml")
response = request.get(metadata_path, contentType='application/xml')

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
    artifactRepositoryPath = "%s/%s/%s/%s-%s" % (server['url'], context, artifactVersion, artifactId, artifactVersion)
    print artifactRepositoryPath
