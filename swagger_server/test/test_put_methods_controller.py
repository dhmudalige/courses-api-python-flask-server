# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestPutMethodsController(BaseTestCase):
    """PutMethodsController integration test stubs"""

    def test_update_course(self):
        """Test case for update_course

        
        """
        response = self.client.open(
            '/peraprojects/courses/2.1.0/update/{semester}/{courseCode}/'.format(semester='semester_example', courseCode='courseCode_example'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
