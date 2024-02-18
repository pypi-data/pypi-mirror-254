# *********************************************************************
# This Original Work is copyright of 51 Degrees Mobile Experts Limited.
# Copyright 2023 51 Degrees Mobile Experts Limited, Davidson House,
# Forbury Square, Reading, Berkshire, United Kingdom RG1 3EU.
#
# This Original Work is licensed under the European Union Public Licence
# (EUPL) v.1.2 and is subject to its terms as set out below.
#
# If a copy of the EUPL was not distributed with this file, You can obtain
# one at https://opensource.org/licenses/EUPL-1.2.
#
# The 'Compatible Licences' set out in the Appendix to the EUPL (as may be
# amended by the European Commission) shall be deemed incompatible for
# the purposes of the Work and the provisions of the compatibility
# clause in Article 5 of the EUPL shall not apply.
#
# If using the Work as, or as part of, a network application, by
# including the attribution notice(s) required under Article 5 of the EUPL
# in the end user terms of the application under an appropriate heading,
# such notice(s) shall fulfill the requirements of that article.
# ********************************************************************* 

import unittest

from fiftyone_pipeline_core.flowelement import FlowElement
from fiftyone_pipeline_core.pipelinebuilder import PipelineBuilder
from fiftyone_pipeline_core.elementdata_dictionary import ElementDataDictionary
from fiftyone_pipeline_core.aspectproperty_value import AspectPropertyValue


class TestEngine(FlowElement):

    def __init__(self):

        super(TestEngine, self).__init__()

        self.datakey = "test"

        self.properties = { 
            "javascript" : {
                "type" : "javascript"
            },
            "apvGood" : {
                "type" : "string"
            },
            "apvBad" : {
                "type" : "string"
            },
            "normal" : {
                "type" : "boolean"
            }
        }


    def process_internal(self, flowdata):
 
        contents = {}

        contents["javascript"] = "console.log('hello world')"
        contents["normal"] = True

        contents["apvGood"] = AspectPropertyValue(None, "Value")
        contents["apvBad"] =  AspectPropertyValue("No value")

        data =  ElementDataDictionary(self, contents)

        flowdata.set_element_data(data)


class TestPipeline():

    def __init__(self, minify = None):

  
        if minify == None:
            pipelineSettings = {}
        else:
            jsSettings = {'minify' : minify}
            pipelineSettings = {'javascript_builder_settings' : jsSettings}
        
        self.Pipeline = PipelineBuilder(pipelineSettings)\
            .add(TestEngine())\
            .build()


class DelayedExecutionEngine1(FlowElement):

    def __init__(self):

        super(DelayedExecutionEngine1, self).__init__()

        self.datakey = "delayedexecutiontest1"

        self.properties = {
            "one" : {
                "delayexecution" : False,
                "type" : 'javascript'
            },
            "two" : {
                "evidenceproperties" : ['jsontestengine']
            }
        }

    def process_internal(self, flowdata):

        contents = {
            "one" : 1,
            "two" : 2
        }

        data = ElementDataDictionary(self, contents)

        flowdata.set_element_data(data)


class DelayedExecutionEngine2(FlowElement):

    def __init__(self):

        super(DelayedExecutionEngine2, self).__init__()

        self.datakey = "delayedexecutiontest2"
            
        self.properties = {
            "one" : {
                "delayexecution" : True,
                "type" : 'javascript'
            },
            "two" : {
                "evidenceproperties" : ['one']
            }
        }

    def process_internal(self, flowdata):


        contents = {
            "one" : 1,
            "two" : 2
        }

        data =  ElementDataDictionary(self, contents)

        flowdata.set_element_data(data)


class DelayedExecutionEngine3(FlowElement):

    def __init__(self):

        super(DelayedExecutionEngine3, self).__init__()

        self.datakey = "delayedexecutiontest3"
  
        self.properties = {
            "one" : {
                "evidenceproperties" : ['two', 'three']
            },
            "two" : {
                "delayexecution" : True
            },
            "three" : {
                "delayexecution" : False
            }
        }

    def process_internal(self, flowdata):

        contents = {
            "one" : 1,
            "two" : 2,
            "three" : 3
        }

        data = ElementDataDictionary(self, contents)

        flowdata.set_element_data(data)


class JavaScriptBundlerTests(unittest.TestCase):

    def testJSONBundler(self):
    
        Pipeline = TestPipeline(False).Pipeline

        FlowData = Pipeline.create_flowdata()

        FlowData.process()

        expected = {
            'javascriptProperties' :
            [
              'test.javascript',
            ],
            'test' :
            {
                'javascript' : 'console.log(\'hello world\')',
                'apvgood' : 'Value',
                'apvbad' : None,
                'apvbadnullreason' : 'No value',
                'normal' : True,
            }
        }

        self.assertEqual(FlowData.jsonbundler.json, expected)
 

    def testJavaScriptBuilder_Minify(self):
   
        # Generate minified javascript
        Pipeline = (TestPipeline(True)).Pipeline
        FlowData = Pipeline.create_flowdata()
        FlowData.process()
        minified = FlowData.javascriptbuilder.javascript

        # Generate non-minified javascript
        Pipeline = (TestPipeline(False)).Pipeline
        FlowData = Pipeline.create_flowdata()
        FlowData.process()
        nonminified = FlowData.javascriptbuilder.javascript
        
        # Generate javascript with default settings
        Pipeline = (TestPipeline()).Pipeline
        FlowData = Pipeline.create_flowdata()
        FlowData.process()
        default = FlowData.javascriptbuilder.javascript

        # We don't want to get too specific here. Just check that 
        # the minified version is smaller to confirm that it's
        # done something.

        self.assertTrue(len(minified) < len(nonminified))

        # Check that default is to minify the output
        self.assertTrue(len(default) < len(nonminified))


    def testSequence(self):

        Pipeline = ( TestPipeline(False)).Pipeline

        FlowData = Pipeline.create_flowdata()

        FlowData.evidence.add("query.session-id", "test")
        FlowData.evidence.add("query.sequence", 10)

        FlowData.process()

        self.assertEqual(FlowData.evidence.get("query.sequence"), 11)

        self.assertEqual(len(FlowData.jsonbundler.json["javascriptProperties"]), 0)


    def test_jsonbundler_when_delayed_execution_false(self):
 
        pipeline = PipelineBuilder()

        pipeline.add(DelayedExecutionEngine1())
        pipeline = pipeline.build()

        flowdata = pipeline.create_flowdata()

        flowdata.process()

        expected = {"one" : 1, "two" : 2}
        actual = flowdata.jsonbundler.json["delayedexecutiontest1"]
        self.assertEqual(actual, expected)



    def test_jsonbundler_when_delayed_execution_true(self):

        pipeline = PipelineBuilder()

        pipeline.add(DelayedExecutionEngine2())
        pipeline = pipeline.build()

        flowdata = pipeline.create_flowdata()

        flowdata.process()

        expected = {
            "onedelayexecution" : True,
            "one" : 1,
            "twoevidenceproperties" :  ['delayedexecutiontest2.one'],
            "two" : 2
        }

        actual = flowdata.jsonbundler.json["delayedexecutiontest2"]
        self.assertEqual(actual, expected)



    def test_jsonbundler_when_delayed_execution_multiple(self):

        pipeline = PipelineBuilder()

        pipeline.add(DelayedExecutionEngine3())
        pipeline = pipeline.build()

        flowdata = pipeline.create_flowdata()

        flowdata.process()

        expected = {
            "oneevidenceproperties" : ['delayedexecutiontest3.two'],
            "one" : 1,
            "twodelayexecution": True,
            "two" : 2,
            "three" : 3
        }

        actual = flowdata.jsonbundler.json["delayedexecutiontest3"]
        self.assertEqual(actual, expected)
