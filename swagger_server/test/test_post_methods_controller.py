# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.course import Course  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPostMethodsController(BaseTestCase):
    """PostMethodsController integration test stubs"""

    def test_add_course(self):
        """Test case for add_course

        
        """
        body = Course()
        response = self.client.open(
            '/peraprojects/courses/1.0.0/add/{semester}/{courseCode}/'.format(semester='semester_example', courseCode='courseCode_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
